"""Données du cahier de phasage par élévation — Hôpital de Chandler R-657-24.

Repères géométriques calés sur la feuille 202 (élévation F, nord), rendu
`img/A202_elev_nord.png` = clip page Rect(70, 450, 1600, 930) de la feuille.
Le calque SVG utilise viewBox "0 0 1530 480" : svg = page − (70, 450).

Échelle du dessin : 1:200, soit 70,71 mm par unité de page, vérifiée dans les
deux sens (chaîne d'axes horizontale et chaîne de niveaux verticale).
"""

# --- chaîne d'axes de l'élévation nord, de 16 (est) à 1 (ouest) ------------
# entraxes écrits sur la feuille 202, cumulés depuis l'axe 16
ENTRAXES = [('16', 0), ('15', 7247), ('14', 7113), ('13', 7010), ('12', 7010), ('11', 7036),
            ('10', 7417), ("9'", 2692), ('9', 4318), ('8', 7010), ('7', 7010), ('6', 7010),
            ('5', 7010), ('4', 7010), ('3', 7010), ('2', 7010), ('1', 7010)]
MM_PAR_UNITE = 70.71
X_AXE_16 = 12.0            # position svg de l'axe 16
Y_RDC = 450.0              # position svg du niveau R00 (10 000)

def _cumul():
    out, c = {}, 0
    for nom, d in ENTRAXES:
        c += d; out[nom] = c
    return out
CUMUL = _cumul()                      # nom d'axe -> distance en mm depuis l'axe 16

def _mm_axe(n):
    """Distance en mm depuis l'axe 16 pour un numéro d'axe entier, extrapolée
    au-delà de l'axe 1 (vers l'ouest) et de l'axe 16 (vers l'est) au pas de 7010 mm."""
    if 1 <= n <= 16: return CUMUL[str(n)]
    if n < 1: return CUMUL['1'] + (1 - n) * 7010
    return CUMUL['16'] - (n - 16) * 7010

def ax(a):
    """Position svg x d'une coordonnée d'axe continue (16 = est, 1 = ouest).

    Un entier donne l'axe lui-même ; 13,5 tombe à mi-chemin entre les axes 14 et 13.
    L'axe 9' vaut 9,616 (4318 mm des 7010 mm qui séparent l'axe 9 de l'axe 10)."""
    if isinstance(a, str): a = 9.616 if a == "9'" else float(a)
    lo = int(a) if a >= 0 else int(a) - 1
    f = a - lo
    m = _mm_axe(lo) + f * (_mm_axe(lo + 1) - _mm_axe(lo))
    return X_AXE_16 + m / MM_PAR_UNITE

NIVEAUX = [('Dessus parapet', 29820), ('Niveau 500', 28882), ('Niveau 400', 25202),
           ('Niveau 300', 21559), ('Niveau 200', 17901), ('Niveau 100', 13952),
           ('Rez-de-chaussée R00', 10000), ('Sous-sol S00', 5442)]
def niv(mm_abs):
    """Position svg y d'une cote de niveau, en millimètres absolus du projet."""
    return Y_RDC - (mm_abs - 10000) / MM_PAR_UNITE
NIV = {n: niv(v) for n, v in NIVEAUX}

# --- correspondance élévation <-> façade ----------------------------------
# Source écrite : titres des dessins (feuilles 201, 201-A, 202, 203, 204) et
# codage du tableau de coordination D5 (légende : « 1. Orientation façade :
# Nord, Sud, Est, Ouest ; 2. Numérotation élévation : se référer aux bulles
# d'élévations en architecture et ingénierie (A à I) »).
REPERES = [
 # lettre, titre du dessin, feuille démolition, feuille construction, façade D5, nb lignes D5, ancienne lecture du cahier en plan
 ('A', 'Élévation sud',              '201',   '203', 'Sud',   30, 'sud — confirmé'),
 ('B', 'Élévation ouest',            '201',   '203', 'Ouest', 14, 'ouest — confirmé'),
 ('C', 'Élévation ouest partielle',  '201-A', '203', 'Ouest',  5, '« ? » — tranché : ouest'),
 ('D', 'Élévation est partielle',    '201-A', '203', 'Est',    1, '« ? » — tranché : est'),
 ('E', 'Élévation ouest partielle',  '201-A', '203', 'Ouest',  4, 'ouest — confirmé'),
 ('F', 'Élévation nord',             '202',   '204', 'Nord',  23, 'nord — confirmé'),
 ('G', 'Élévation est',              '202',   '204', 'Est',   10, 'est — confirmé'),
 ('H', 'Élévation est partielle',    '201-A', '204', 'Est',    4, 'lue « nord partielle » — corrigé : est'),
 ('I', 'Élévation ouest partielle',  '201-A', '204', 'Ouest',  2, 'ouest — confirmé'),
 ('J', 'Élévation sud partielle',    '201-A', '203', '—',      0, 'absente du cahier en plan'),
 ('K', 'Élévation ouest partielle',  '201-A', '204', '—',      0, 'absente du cahier en plan'),
]

# --- états d'un appareil (couleurs du calque) -----------------------------
ETATS = {
 'retire':   ('#b71c1c', 'Retiré définitivement'),
 'deplace':  ('#8e24aa', 'Déplacé temporairement puis réinstallé'),
 'maintenu': ('#1b5e20', 'Maintenu en fonction sans interruption'),
 'coupe':    ('#e65100', 'Maintenu avec interruption convenue'),
 'intact':   ('#546e7a', 'Non touché par les travaux'),
}

# --- appareils de la façade nord (élévation F) ----------------------------
# code D5 ; état ; libellé court ; repère de la feuille ME001(D) ; coordonnée
# d'axe [lecture] ; cote de niveau du point (mm) ; position de l'étiquette
# (dx, dy en unités svg depuis le point) ; verrou (clé de VERROUS ou None)
APPAREILS = [
 ('N-F-P-002', 'coupe',    'Déshumidification, coude', 'non repéré sur ME001(D)', 15.4, 12600, (34, -96), 'V14'),
 ('N-F-P-001', 'maintenu', "Sortie d'arrosage", 'D3 plomberie', 14.55, 10900, (-30, -52), 'V15'),
 ('N-F-E-001', 'coupe',    'Conduit PVC, lampadaires', 'D6 électricité', 13.53, 12400, (-14, -74), 'V10'),
 ('N-F-V-001', 'coupe',    'Col de cygne, atelier GBM', 'D4 ventilation', 12.51, 10700, (10, -44), 'V8'),
 ('N-F-E-002', 'retire',   'Antenne au toit et conduit PVC', 'D7 électricité', 11.9, 14900, (-26, -30), None),
 ('N-F-E-003', 'coupe',    'Câblage de paratonnerre', 'D11 électricité', 11.0, 14900, (16, -30), None),
 ('N-F-V-002', 'coupe',    'Persienne RAV, saut-de-loup S17', 'D2 ventilation', 11.6, 10600, (26, -30), 'V9'),
 ('N-F-E-004', 'coupe',    'Caméra, coin escalier no 3', 'D8 électricité', 9.70, 15600, (-36, -46), 'V11'),
 ('N-F-V-010', 'deplace',  'Persienne PAF P-05', 'D5 ventilation', 9.38, 16800, (-16, -60), None),
 ('N-F-V-005', 'coupe',    'Unité hémodialyse : 3 conduits + passerelle', 'D7 ventilation', 7.13, 17901, (0, -62), 'V1'),
 ('N-F-V-004', 'coupe',    'Ventilateur cloche, stérilisation', 'D6 ventilation', 8.23, 14200, (-52, 34), 'V7'),
 ('N-F-V-006', 'intact',   'Bi-blocs (8x) non touchés', 'D13 ventilation', 6.35, 12600, (16, 40), None),
 ('—',         'deplace',  "Sortie d'évent murale de laboratoire", 'D4 plomberie — aucune ligne D5', 6.57, 14400, (34, 18), None),
 ('N-F-V-007', 'coupe',    "Sortie d'air murale, secteur labo", 'D8 ventilation', 5.67, 14400, (30, -24), 'V5'),
 ('N-F-V-008', 'coupe',    'Persienne RAV P-06, chambre 216', 'D15 ventilation', 4.63, 21000, (-46, -26), 'V4'),
 ('N-F-V-009', 'maintenu', 'Persienne PAF P-07, soins intensifs 315', 'D9 ventilation', 4.11, 24600, (-10, -28), 'V3'),
 ('N-F-V-003', 'coupe',    'Évacuation V-53, toilette du labo', 'non repéré séparément', 3.78, 13100, (44, -18), 'V6'),
 ('N-F-V-011', 'coupe',    "Trappes d'accès pour mécanique", 'D11 ventilation', 2.75, 13300, (16, -60), 'V16'),
 ('N-F-V-012', 'deplace',  'Persienne sous porte-à-faux P-08', 'D12 ventilation', 2.52, 13000, (-62, -20), None),
 ('N-F-E-005', 'retire',   'Prise extérieure, porte nord du quai', 'D9 électricité', 0.92, 11600, (-64, -97), None),
 ('N-F-E-006', 'coupe',    'Luminaire mural, porte piéton nord', 'D3 électricité', 0.80, 12200, (-64, -63), 'V12'),
 ('N-F-E-007', 'coupe',    'Lecteur de carte, porte piéton nord', 'D2 électricité', 1.02, 11100, (-64, -52), 'V12'),
 ('N-F-E-008', 'coupe',    'Clavier, porte de garage nord', 'D10 électricité', 0.86, 10600, (-64, -33), 'V13'),
 ('N-F-GM-001','maintenu', "Prise d'air de la centrale d'air médical", 'non repéré sur ME001(D)', 3.30, 25600, (-4, -30), 'V2'),
]

# --- verrous appareil <-> architecture ------------------------------------
# clé ; appareil ; ce qui doit être fait avant ; étape d'architecture bloquée ; source
VERROUS = [
 ('V1', "Unité de ventilation de l'hémodialyse et du laboratoire (N-F-V-005), axes 8 à 6, niveau 200",
  "Conduits temporaires d'alimentation et de retour en place ; passerelle d'aluminium enlevée par l'entrepreneur général",
  "E2 démolition de l'enveloppe entre les axes 8 et 6 ; modification des brides un conduit à la fois",
  "D5 N-F-V-005 ; ME001(D) note D7 ventilation ; ME014 D1 à D4 ; Z-29"),
 ('V2', "Prise d'air de la centrale de production d'air médical (N-F-GM-001)",
  "Conduit temporaire installé hors de la zone de travaux ; bonbonnes commandées",
  "E2 sur la portion concernée — position non repérée sur ME001(D) `[à confirmer]`",
  "D5 N-F-GM-001 ; ME-064 à 068 ; 03 §6"),
 ('V3', "Persienne de prise d'air frais des soins intensifs, chambre 315 (N-F-V-009), axe 4, niveau 400",
  "Prolongation temporaire du conduit hors des échafaudages ; persienne à relocaliser",
  "E2 et E4 : l'échafaudage ne peut couvrir la prise d'air sans prolongation préalable",
  "D5 N-F-V-009 ; ME-058 ; ME001(D) note D9 ventilation"),
 ('V4', "Persienne de renvoi d'air de la chambre à pression négative 216 (N-F-V-008), axe 4,6, niveau 300",
  "Prolongation temporaire du conduit RAV hors des échafaudages",
  "E2 ; E4 modifie le plénum selon l'épaisseur du revêtement",
  "D5 N-F-V-008 ; ME-057 ; ME001(D) note D15 ventilation"),
 ('V5', "Sortie d'air murale du secteur du laboratoire (N-F-V-007), axe 5,7",
  "Conduit d'évacuation temporaire prolongé hors des échafaudages",
  "E2 ; la sortie est remplacée en E4",
  "D5 N-F-V-007 ; ME-059 à 061 ; ME001(D) note D8 ventilation"),
 ('V6', "Évacuation V-53 de la toilette du laboratoire (N-F-V-003)",
  "Filtration temporaire en place",
  "E2 ; persienne relocalisée dans le nouveau revêtement en E4",
  "D5 N-F-V-003 ; ME-061"),
 ('V7', "Ventilateur d'évacuation mural en cloche, salle de mécanique de stérilisation (N-F-V-004), axe 8,2",
  "Aucun préalable écrit",
  "E2 : ventilateur enlevé ; E6 : réinstallé après le revêtement, conduit prolongé à l'intérieur du mur",
  "D5 N-F-V-004 ; ME001(D) note D6 ventilation"),
 ('V8', "Col de cygne d'évacuation de l'atelier GBM (N-F-V-001), axe 12,5",
  "Conduit temporaire si requis pour la continuité des opérations",
  "E2 ; réinstallation en E6 après la réfection de la façade",
  "D5 N-F-V-001 ; ME001(D) note D4 ventilation"),
 ('V9', "Persienne de renvoi d'air du saut-de-loup, atelier de menuiserie S17 (N-F-V-002), axe 11,6",
  "Saut-de-loup et persienne conservés ; conduit temporaire si requis",
  "E2 ; le système d'évacuation de l'atelier est arrêté toute la durée des travaux de ce secteur",
  "D5 N-F-V-002 ; ME-062 ; ME001(D) note D2 ventilation"),
 ('V10', "Conduit PVC des lampadaires de stationnement (N-F-E-001), axe 13,5",
  "Boîte de jonction si les travaux se font de jour seulement",
  "E2 et E4 ; contrainte quotidienne : le lampadaire doit être remis en fonction tous les soirs",
  "D5 N-F-E-001 ; ME001(D) note D6 électricité"),
 ('V11', "Caméra extérieure, coin de l'escalier no 3 (N-F-E-004), axe 9,7",
  "Relocalisation temporaire conservant le même champ, coupure la plus courte possible",
  "E2 ; à coordonner avec le propriétaire",
  "D5 N-F-E-004 ; ME001(D) note D8 électricité"),
 ('V12', "Luminaire mural et lecteur de carte de la porte piéton nord du quai des ambulances (N-F-E-006, N-F-E-007), axe 1",
  "Aucun préalable écrit",
  "E2 ; la porte reste hors d'usage pendant les travaux de ce secteur (note 8 de la légende du tableau D5)",
  "D5 N-F-E-006, N-F-E-007 ; ME001(D) notes D2, D3, D5 électricité"),
 ('V13', "Clavier de la porte de garage nord du quai des ambulances (N-F-E-008), axe 0,9",
  "Travaux à exécuter quand la porte est ouverte : elle se ferme automatiquement",
  "E2 ; **période écrite : estivale** — voir le conflit saisonnier signalé en bas de planche",
  "D5 N-F-E-008 ; ME001(D) note D10 électricité"),
 ('V14', "Système de déshumidification, coin nord-est (N-F-P-002), axes 15 à 16",
  "Prolongation temporaire de la sortie hors des échafaudages",
  "E2 ; arrêt possible sauf en période estivale",
  "D5 N-F-P-002"),
 ('V15', "Sortie d'arrosage extérieure encastrée, coin nord-est (N-F-P-001), axe 14,6",
  "Verrou inverse : c'est l'architecture qui doit livrer une alcôve dans le nouveau revêtement pour absorber la différence d'épaisseur",
  "E4 ; la plaque de finition est enlevée temporairement en plomberie",
  "D5 N-F-P-001 ; ME-116 (même principe au coin nord-est)"),
 ('V16', "Trappes d'accès pour la mécanique du porte-à-faux (N-F-V-011), axe 2,8",
  "Verrou inverse : nouvelles trappes fournies par l'entrepreneur général, dimensions et position identiques à l'existant",
  "E4 ; sans elles, plus d'accès au ventilateur, aux purgeurs, au détecteur de fumée de gaine et au volet motorisé",
  "D5 N-F-V-011 ; ME-121, ME-122 ; ME001(D) note D11 ventilation"),
]

# --- séquence type de façade (03 §1.3), rappelée pour la lecture ----------
ETAPES = [
 ('E1', 'Préparation', "Classification PCI, cloisons et SAS, scellement des grilles, approbation de la préparation des lieux, toile sur l'échafaudage, **contournements électromécaniques avant démolition**, plan d'action pour les issues"),
 ('E2', "Démolition de l'enveloppe", "Retrait des revêtements, persiennes entreposées, équipements muraux démontés ; fenêtres existantes maintenues ; débris évacués en fin de journée"),
 ('E3', 'Relevé et structure', "Point d'arrêt après retrait des revêtements, relevé complet, validation des dimensions avant fabrication, renforts et réparations de béton (≥ 10 °C)"),
 ('E4', 'Enveloppe neuve', "Pare-air, compartimentation, isolant, revêtement, solins, couverture des bandes de toiture démolies ; essais in situ"),
 ('E5', 'Fenêtres', "Retrait après achèvement des travaux par l'extérieur `[lecture]` ; plexiglas ou bâti isolé de novembre à avril ; thermos et finition le même jour que le retrait du plexiglas"),
 ('E6', 'Remise en service', "Réinstallation des équipements, essais et préavis, séquence PCI de fin de travaux, désinfection terminale, correction des anomalies avant la phase suivante"),
]
