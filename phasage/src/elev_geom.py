"""Géométrie des quatre élévations — Hôpital de Chandler R-657-24.

Chaque élévation est rendue depuis sa feuille d'architecture par un clip en
coordonnées de page ; le calque SVG utilise le même repère, décalé de l'origine
du clip. Deux chaînes d'axes servent à placer les appareils :

- chaîne numérique 1 à 16 (élévations nord et sud), total ±105 923 mm ;
- chaîne lettrée A à I (élévations est et ouest), total ±43 459 mm.

Échelle des dessins : 1:200 exact, soit 70,556 mm par unité de page (25,4 / 72
x 200). Vérifiée sur les quatre élévations dans les deux sens, chaîne d'axes et
chaîne de niveaux.
"""

MM_PAR_UNITE = 70.5556   # 1:200 exact : 25,4 / 72 x 200

# entraxes écrits, cumulés depuis l'axe 1 (ouest) pour la chaîne numérique
_NUM = [('1', 0), ('2', 7010), ('3', 7010), ('4', 7010), ('5', 7010), ('6', 7010), ('7', 7010),
        ('8', 7010), ('9', 7010), ("9'", 4318), ('10', 2692), ('11', 7417), ('12', 7036),
        ('13', 7010), ('14', 7010), ('15', 7113), ('16', 7247)]
# entraxes écrits, cumulés depuis l'axe A (nord) pour la chaîne lettrée
# D.1' est collé à D.1 (303 mm) et non à mi-chemin : le total ±43 459 mm écrit
# sur les feuilles 201 et 202 ne se retrouve qu'avec cette répartition.
_LET = [('A', 0), ('B', 5437), ("B'", 2615), ('C', 3811), ('D.1', 2997), ("D.1'", 303),
        ('D.2', 4064), ('E', 2946), ('F', 6426), ("F'", 578), ('G', 5721), ('H', 1296), ('I', 7264)]

def _cumul(chain):
    out, c = {}, 0
    for nom, d in chain:
        c += d; out[nom] = c
    return out
CUM_NUM, CUM_LET = _cumul(_NUM), _cumul(_LET)
ORDRE_NUM = [n for n, _ in _NUM]
ORDRE_LET = [n for n, _ in _LET]

# Coordonnée continue employée pour situer un appareil le long d'une élévation.
# Chaîne numérique : la coordonnée est le NUMÉRO d'axe (4,5 = à mi-chemin entre
# les axes 4 et 5) ; l'axe intercalaire 9' vaut 9,616, soit 4318 des 7010 mm qui
# séparent l'axe 9 de l'axe 10. Chaîne lettrée : la coordonnée est le RANG dans
# l'ordre des axes (0 = A, 1 = B, 2 = B', … 12 = I).
COORD_NUM = [(n, float(n)) for n in ORDRE_NUM if n != "9'"]
COORD_NUM.insert(9, ("9'", 9 + 4318 / 7010))
COORD_LET = [(n, float(i)) for i, n in enumerate(ORDRE_LET)]

NIVEAUX = [('Dessus parapet', 29820), ('Niveau 500', 28882), ('Niveau 400', 25202),
           ('Niveau 300', 21559), ('Niveau 200', 17901), ('Niveau 100', 13952),
           ('Rez-de-chaussée R00', 10000), ('Sous-sol S00', 5442)]

class Geom:
    """Repère d'une élévation : conversion coordonnée d'axe → x svg, cote → y svg.

    `chaine`   : 'num' (axes 1 à 16) ou 'let' (axes A à I).
    `x_ref`    : (nom d'axe, position svg x de cet axe).
    `sens`     : +1 si la distance croît vers la droite, −1 sinon.
    `y_rdc`    : position svg y du niveau R00 (10 000).
    `clip`     : rectangle de page découpé sur la feuille (x0, y0, x1, y1).
    """
    def __init__(self, nom, repere, feuille, img, chaine, x_ref, sens, y_rdc, clip, gauche, droite):
        self.nom, self.repere, self.feuille, self.img = nom, repere, feuille, img
        self.chaine, self.sens, self.y_rdc, self.clip = chaine, sens, y_rdc, clip
        self.gauche, self.droite = gauche, droite       # ce que montre chaque bord
        self.cum = CUM_NUM if chaine == 'num' else CUM_LET
        self.ordre = ORDRE_NUM if chaine == 'num' else ORDRE_LET
        self.coord = COORD_NUM if chaine == 'num' else COORD_LET
        self.x_ref_nom, self.x_ref = x_ref
        self.largeur = clip[2] - clip[0]
        self.hauteur = clip[3] - clip[1]

    def mm(self, a):
        """Distance en mm depuis l'origine de la chaîne, pour une coordonnée d'axe.

        `a` accepte un nom d'axe ('B'', '9'') ou une coordonnée continue, lue
        dans le repère de la chaîne : numéro d'axe pour la chaîne numérique,
        rang dans l'ordre pour la chaîne lettrée. Les valeurs hors chaîne sont
        extrapolées avec l'entraxe de l'extrémité concernée."""
        if isinstance(a, str): return self.cum[a]
        pts = [(c, self.cum[n]) for n, c in self.coord]
        if a <= pts[0][0]:
            pas = (pts[1][1] - pts[0][1]) / (pts[1][0] - pts[0][0])
            return pts[0][1] + (a - pts[0][0]) * pas
        if a >= pts[-1][0]:
            pas = (pts[-1][1] - pts[-2][1]) / (pts[-1][0] - pts[-2][0])
            return pts[-1][1] + (a - pts[-1][0]) * pas
        for (c0, m0), (c1, m1) in zip(pts, pts[1:]):
            if c0 <= a <= c1: return m0 + (a - c0) * (m1 - m0) / (c1 - c0)
        raise ValueError(a)

    def ax(self, a):
        return self.x_ref + self.sens * (self.mm(a) - self.mm(self.x_ref_nom)) / MM_PAR_UNITE

    def niv(self, mm_abs):
        return self.y_rdc - (mm_abs - 10000) / MM_PAR_UNITE

    def axes_visibles(self):
        """Axes de la chaîne dont la position tombe dans le clip."""
        return [(n, self.ax(n)) for n in self.ordre if -6 <= self.ax(n) <= self.largeur + 6]


# Élévation nord : l'axe 1 est à l'ouest, l'axe 16 à l'est ; le dessin se lit
# de l'est (gauche) vers l'ouest (droite). Vérifié : la sortie d'arrosage écrite
# « coin nord-est » tombe vers l'axe 14 et les appareils du quai des ambulances
# vers l'axe 1, du côté où le plan clé place la sortie d'ambulance.
NORD = Geom('nord', 'F', '202', 'A202_elev_nord.png', 'num', ('16', 12.0), -1, 450.0,
            (70, 450, 1600, 930), 'est', 'ouest')
SUD = Geom('sud', 'A', '201', 'A201_elev_sud.png', 'num', ('1', 88.0), +1, 437.0,
           (200, 455, 1810, 950), 'ouest', 'est')
OUEST = Geom('ouest', 'B', '201', 'A201_elev_ouest.png', 'let', ('A', 472.0), +1, 442.0,
             (176, 1070, 1300, 1616), 'nord', 'sud')
EST = Geom('est', 'G', '202', 'A202_elev_est.png', 'let', ('I', 7.0), -1, 429.0,
           (213, 1094, 1056, 1600), 'sud', 'nord')
GEOMS = {g.nom: g for g in (NORD, SUD, EST, OUEST)}

# --- états d'un appareil (couleurs du calque) -----------------------------
ETATS = {
 'retire':   ('#b71c1c', 'Retiré définitivement'),
 'deplace':  ('#8e24aa', 'Déplacé temporairement puis réinstallé'),
 'maintenu': ('#1b5e20', 'Maintenu en fonction sans interruption'),
 'coupe':    ('#e65100', 'Maintenu avec interruption convenue'),
 'intact':   ('#546e7a', 'Non touché par les travaux'),
}
