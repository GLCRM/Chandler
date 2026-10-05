"""Données du plan de phasage complet, option R — Hôpital de Chandler R-657-24.

Tout ce qui est daté ici est un [choix] de GLCRM : les documents ne fixent ni
dates ni durées, hors l'échéancier contractuel jugé inapplicable (C-14). Le
calendrier part des données de travail GLCRM (installation de chantier en
novembre 2026, travaux de janvier 2027 à décembre 2028, période estivale du
24 juin au 15 août) et des durées indicatives du plan clé (feuille 010 :
phase 1 ±5 mois, phase 2 ±8 mois, phase 3 ±4 mois).

Les bandes de phase sur les élévations sont une [lecture] : les élévations de
la feuille 011 ne portent aucune couleur, les phases sont reportées depuis les
zones du plan clé, axe par axe (environ 148 mm par pixel du plan clé ; tour des
axes 1 à 9 et B à F').
"""
import datetime as dt

D = dt.date

# --- couleurs des phases (reprises du plan clé) ----------------------------
COUL = {'0': '#78909c', '1': '#2a72b5', '2': '#43a047', '3': '#f0a830', '4': '#8e24aa',
        'NT': '#9e9e9e', 'H': '#5c6bc0'}
def famille(code):
    return code.split('.')[0] if code not in ('NT', 'H28') else ('NT' if code == 'NT' else 'H')

# --- phases et calendrier [choix] ------------------------------------------
# code, titre court, début, fin, ligne du diagramme, ce qui fixe la fenêtre
PHASES = [
 ('0',   'Phase 0 — mobilisation et préalables',            D(2026, 11, 2),  D(2026, 12, 18),
  "Installation de chantier GLCRM : novembre 2026"),
 ('1',   'Phase 1 — basilaire est (zones D, E, F)',          D(2027, 1, 4),   D(2027, 5, 31),
  "Enceintes chauffées de janvier à avril ; la déshumidification du coin nord-est ne s'arrête pas l'été"),
 ('P2',  'Préalables de la tour : contournements',           D(2027, 5, 3),   D(2027, 6, 23),
  "Conduits temporaires de l'hémodialyse (dimanches, hors été), du bloc opératoire, évents des autoclaves"),
 ('2.S', 'Phase 2 — tour, face sud',                         D(2027, 6, 1),   D(2027, 8, 13),
  "Aucune contrainte saisonnière ; chambre 307 traitée quand elle est inoccupée"),
 ('2.O', 'Phase 2 — tour, face ouest',                       D(2027, 7, 5),   D(2027, 9, 30),
  "Thermostat des câbles chauffants hors hiver ; bloc opératoire alimenté par les conduits temporaires"),
 ('2.N', 'Phase 2 — tour, face nord',                        D(2027, 8, 16),  D(2027, 11, 19),
  "Rebranchement de l'hémodialyse le dimanche, après le 15 août"),
 ('2.E', 'Phase 2 — tour, face est',                         D(2027, 10, 18), D(2028, 1, 28),
  "Bi-blocs du traitement d'eau et des serveurs en semaine hors été ; enceintes chauffées de novembre à janvier"),
 ('H28', 'Hiver 2028 — fenêtres de la tour, étapes intérieures', D(2028, 2, 1), D(2028, 4, 28),
  "Thermos, cadrage et toile derrière un bâti isolé (novembre à avril, AR-PLN-042)"),
 ('3.S', 'Phase 3 — basilaires sud (I, H, G)',               D(2028, 5, 1),   D(2028, 6, 23),
  "Bi-bloc du prélèvement d'urgence hors été ; ambulances par la porte nord"),
 ('3.N', 'Phase 3 — basilaire nord (J, B, K)',               D(2028, 5, 15),  D(2028, 8, 15),
  "Porte nord du garage : clavier « en période estivale » ; ambulances par la porte sud dès le 24 juin"),
 ('3.O', 'Phase 3 — basilaire ouest (O)',                    D(2028, 8, 16),  D(2028, 9, 29),
  "Après le revêtement nord (prise d'air médical réinstallée) ; persienne du garage : lecture à trancher"),
 ('4',   'Phase 4 — clôture et réception',                   D(2028, 10, 2),  D(2028, 12, 15),
  "Mise en service, essais intégrés, deuxième certification de l'air médical, réception"),
]
PH = {p[0]: p for p in PHASES}
DEBUT_CAL, FIN_CAL = D(2026, 11, 1), D(2028, 12, 31)
ETES = [(D(2027, 6, 24), D(2027, 8, 15)), (D(2028, 6, 24), D(2028, 8, 15))]
HIVERS = [(D(2026, 11, 1), D(2027, 4, 30)), (D(2027, 11, 1), D(2028, 4, 30)), (D(2028, 11, 1), D(2028, 12, 31))]

# Repères saisonniers du tableau D5 posés sur le calendrier : ligne, phase,
# date du repère, ce qui est écrit, verdict dans l'enchaînement proposé.
REPERES_SAISON = [
 ('N-F-P-002', '1',   D(2027, 3, 15), 'arrêt « sauf en période estivale »', 'respecté — phase 1 de janvier à mai'),
 ('N-F-V-005', 'P2',  D(2027, 5, 30), '« dimanche seulement, en dehors de la période estivale »', 'respecté — basculement en mai-juin, rebranchement après le 15 août'),
 ('N-F-V-005', '2.N', D(2027, 9, 12), '« dimanche seulement, en dehors de la période estivale »', 'respecté'),
 ('O-B-E-001', '2.O', D(2027, 8, 20), '« en dehors de la période hivernale », durée « mois »', 'respecté — juillet à septembre'),
 ('E-G-V-003', '2.E', D(2027, 11, 8), '« semaine, en dehors de la période estivale »', 'respecté'),
 ('E-G-E-006', '2.E', D(2027, 11, 22), '« semaine, en dehors de la période estivale »', 'respecté — même fenêtre que E-G-V-003'),
 ('S-A-V-001', '3.S', D(2028, 5, 22), '« en dehors de la période estivale (quelques jours en été) »', 'respecté pour la première partie de la phrase'),
 ('N-F-E-008', '3.N', D(2028, 7, 10), '« en période estivale »', 'respecté — porte nord traitée du 24 juin au 15 août'),
 ('O-B-V-004', '3.O', D(2028, 8, 25), '« travailler avec persienne en fonction. En période estivale »', 'à trancher : respecté si « l\'été, garder la persienne en fonction » ; non respecté si « faire l\'été »'),
]

# --- phases reportées sur les élévations [lecture] -------------------------
# (phase, de, à, z bas mm, z haut mm, étiquette). Nord et sud : numéro d'axe ;
# est et ouest : rang dans la chaîne lettrée (0 = A … 12 = I). Toit d'un
# volume d'un étage : niveau 100 + 0,5 m ; de deux étages : niveau 200 + 0,5 m.
T1, T2 = 14452, 18401
BANDES = {
 'nord': [
  ('3.N', -0.2, 1.0, 9000, T1, 'garage des ambulances, porte nord'),
  ('3.N', 1.0, 3.05, 9000, T1, 'J'),
  ('3.N', 3.05, 8.09, 9000, T2, 'B — laboratoire'),
  ('3.N', 8.09, 8.94, 9000, T1, 'K'),
  ('2.N', 1.0, 3.05, T1, 30300, 'tour'),
  ('2.N', 3.05, 8.09, T2, 30300, 'tour'),
  ('2.N', 8.09, 9.62, T1, 30300, 'tour'),
  ('1', 9.62, 14.9, 9000, T2, 'D'),
  ('NT', 14.9, 16.4, 9000, T1, 'L'),
 ],
 'sud': [
  ('3.S', -0.2, 1.11, 9000, T1, 'entrée des ambulances'),
  ('3.S', 1.11, 1.74, 9000, T1, 'I'),
  ('3.S', 1.74, 7.03, 9000, T2, 'H'),
  ('3.S', 7.03, 9.62, 9000, T1, 'G'),
  ('2.S', 1.0, 1.74, T1, 30300, 'tour'),
  ('2.S', 1.74, 7.03, T2, 30300, 'tour'),
  ('2.S', 7.03, 9.0, T1, 30300, 'tour'),
  ('1', 9.62, 14.9, 9000, T2, 'F, E, D'),
  ('NT', 14.9, 16.4, 9000, T1, 'L'),
 ],
 'ouest': [
  ('NT', -9.0, 0.0, 5442, T1, 'archives C'),
  ('3.O', 0.0, 1.0, 9000, T1, 'J'),
  ('3.O', 1.0, 9.0, 5442, T1, 'basilaire ouest'),
  ('3.O', 8.41, 10.0, T1, T2, 'pignon de H'),
  ('3.O', 9.0, 10.0, 9000, T1, 'I'),
  ('3.S', 10.0, 12.5, 9000, T1, 'entrée des ambulances'),
  ('2.O', 1.0, 9.0, T1, 30300, 'tour'),
 ],
 'est': [
  ('NT', 10.8, 12.5, 9000, T1, 'L'),
  ('1', 2.0, 10.8, 9000, T2, 'D, E'),
  ('2.E', 2.0, 8.0, T2, 30300, 'tour'),
  ('2.E', 1.0, 2.0, T1, 30300, 'tour'),
  ('3.N', 0.0, 1.0, 9000, T1, 'K'),
  ('NT', -9.0, 0.0, 9000, T1, 'archives C'),
 ],
}

# Rattachement des appareils dont la position sur l'élévation principale ne dit
# pas la phase : élévations partielles (le tableau D5 code l'orientation du
# mur, pas sa place dans le bâtiment) et appareils non repérés. [lecture]
PAR_PREFIXE = [
 ('O-C-', '1',   "élévation partielle C : mur ouest du volume de l'IRM"),
 ('O-I-', '1',   "élévation partielle I : mur ouest de la cour nord-est, basilaire est"),
 ('E-H-V-002', '3.N', "élévation partielle H : mur est du basilaire nord-est K"),
 ('E-H-', '2.E', "élévation partielle H : retrait est de la tour (escalier no 3)"),
 ('O-E-', '3.O', "élévation partielle E : basilaire ouest, issue de l'urgence"),
 ('E-D-', 'NT',  "élévation partielle D sans axe ; appareil non touché"),
]
PAR_CODE = {
 'N-F-V-005': ('2.N', "unité sur la toiture du basilaire nord ; les conduits traversent la face nord de la tour"),
 'N-F-P-002': ('1',   "« coin nord-est » : angle nord-est du basilaire est"),
 'N-F-V-003': ('3.N', "toilette du laboratoire, zone B"),
 'N-F-GM-001': ('3.N', "centrale d'air médical à la « toiture nord-ouest » — tour ou basilaire non écrit [à confirmer]"),
 'S-A-E-001': ('3.S', "entrée du garage des ambulances"),
 'O-B-V-005': ('3.O', "bi-bloc posé sur le garde-corps G-02, toiture du basilaire nord-ouest"),
 'O-B-E-006': ('3.O', "sectionneur du bi-bloc de la salle d'observation"),
}
PAR_LIBELLE = {
 ("sud", "Évents de vapeur de l'autoclave (2x)"): ('P2', "relocalisés avant le premier travail sur la façade ouest — la face ouest de la tour, en 2027 (ME-075)"),
 ("sud", "Évents de vapeur de la chaufferie (3 annoncés)"): ('3.S', "dessinés au-dessus de la marquise des ambulances"),
 ("ouest", "Unité de vent. de l'hémodialyse et passerelle"): ('2.O', "même unité que N-F-V-005 ; conduits de part et d'autre de l'angle nord-ouest"),
 ("ouest", "Persienne PAF du service alimentaire"): ('3.O', "soufflage de tôle à l'angle nord-ouest ; le tableau du CISSS écrit « zone A » [à confirmer]"),
}

# --- phase de chaque appareil ------------------------------------------------
import elev_data as _E

def phase_appareil(fac, app):
    """Renvoie (phase, motif) pour un appareil du cahier par élévation."""
    code, etat, lib, rep, a, mm = app[:6]
    if code in PAR_CODE: return PAR_CODE[code]
    if (fac, lib) in PAR_LIBELLE: return PAR_LIBELLE[(fac, lib)]
    for pre, ph, motif in PAR_PREFIXE:
        if code.startswith(pre): return ph, motif
    for ph, a0, a1, z0, z1, et in BANDES[fac]:
        if a0 <= a < a1 and z0 <= mm < z1:
            return ph, f"position sur l'élévation : {et} [lecture]"
    return None, 'hors des bandes'

def appareils_de(phase):
    """Appareils rattachés à une phase : liste de (façade, appareil, motif)."""
    out = []
    for fac in ('nord', 'est', 'sud', 'ouest'):
        for app in _E.APPAREILS[fac]:
            ph, motif = phase_appareil(fac, app)
            if ph == phase: out.append((fac, app, motif))
    return out

# --- plan d'implantation : éléments de chantier par phase -------------------
# Repère : découpe (40,700)-(2620,1840) de la feuille 001, affichée en 1900 x 840.
# Ce qui est écrit sur la feuille 001 (clôture note 23, zones des détails de la
# feuille 002) est déjà dans l'image ; ce qui est ajouté ici est un [choix].
BASE = [(110, 292), (178, 330), (463, 330), (463, 405), (510, 405), (492, 690), (383, 668), (45, 435)]
GARAGE = (822, 297, 862, 555)          # garage des ambulances, basilaire ouest
SITE_COMMUN = [
 ('zone', BASE, '#795548', 'hachure', 'Zone clôturée réservée à l\'entrepreneur (notes 19 et 23)'),
 ('rect', (190, 350, 300, 392), '#795548', 'plein', 'Roulottes, entreposage et conteneur [choix]'),
 ('rect', (255, 425, 445, 555), '#795548', 'trait', ''),
 ('rect', (395, 600, 455, 640), '#795548', 'plein', ''),
 ('fleche', (25, 640, 95, 515), '#3e2723', 'Accès de chantier sud-ouest (notes 32, 36)'),
 ('fleche', (1898, 712, 1815, 700), '#3e2723', 'Accès général sud-est (note 30)'),
]
# ambulances : entrée par la porte sud, sortie par la porte nord du garage
AMB_NORMAL = [('fleche', (842, 640, 842, 560), '#c62828', 'Entrée des ambulances (porte sud)'),
              ('fleche', (842, 292, 842, 215), '#c62828', 'Sortie des ambulances (porte nord)')]
AMB_PAR_NORD = [('fleche', (900, 150, 852, 288), '#c62828', 'Ambulances : entrée et sortie par la porte nord (feuille 002, détail 1)'),
                ('croix', (842, 575), '#c62828', 'Porte sud fermée')]
AMB_PAR_SUD = [('fleche', (900, 690, 852, 560), '#c62828', 'Ambulances : entrée et sortie par la porte sud (feuille 002, détail 1)'),
               ('croix', (842, 275), '#c62828', 'Porte nord fermée')]

SITE = {
 '0': SITE_COMMUN + AMB_NORMAL + [
  ('zone', [(800, 95), (890, 105), (852, 178), (832, 215)], '#6d4c41', 'trait', 'Chemin temporaire en gravier (note 22)'),
 ],
 '1': SITE_COMMUN + AMB_NORMAL + [
  ('bande', [(1450, 286), (1728, 286), (1728, 320), (1450, 320)], COUL['1'], 'Échafaudage, face nord du basilaire est'),
  ('bande', [(1395, 346), (1450, 346), (1450, 380), (1395, 380)], COUL['1'], ''),
  ('bande', [(1728, 320), (1762, 320), (1762, 415), (1728, 415)], COUL['1'], 'Face est'),
  ('bande', [(1420, 626), (1728, 626), (1728, 658), (1420, 658)], COUL['1'], 'Face sud (IRM, oncologie 1974)'),
  ('rect', (1360, 662, 1790, 722), '#c62828', 'tirets', 'Zone IRM : aucun entreposage métallique, IRM en service (AR-PLN-009)'),
  ('point', (1745, 468), '#2e7d32', 'Entrée des cliniques externes maintenue, passage protégé (CI-TAB-015)'),
 ],
 '2a': SITE_COMMUN + AMB_NORMAL + [
  ('bande', [(865, 505), (1355, 505), (1355, 538), (865, 538)], COUL['2'], 'Échafaudage, face sud de la tour, sur la toiture du basilaire [lecture]'),
  ('bande', [(822, 297), (862, 297), (862, 505), (822, 505)], COUL['2'], 'Échafaudage, face ouest, sur la toiture du garage [lecture]'),
  ('rect', (1145, 552, 1258, 602), '#2e7d32', 'tirets', 'Passage abrité à l\'entrée principale (AR-DEV-191) [choix]'),
  ('rect', (1170, 255, 1293, 293), '#8e24aa', 'plein', 'Hémodialyse (bassin 16) : conduits temporaires, passerelle enlevée'),
  ('rect', (826, 380, 858, 420), '#8e24aa', 'plein', 'Conduits temporaires 2 × 900 × 900 du bloc opératoire'),
  ('ligne', [(842, 447), (842, 562), (872, 578)], '#8e24aa', 'Évents des autoclaves : tuyauterie temporaire en toiture (ME-075)'),
 ],
 '2b': SITE_COMMUN + AMB_NORMAL + [
  ('bande', [(862, 262), (1355, 262), (1355, 295), (862, 295)], COUL['2'], 'Échafaudage, face nord de la tour, sur la toiture du basilaire [lecture]'),
  ('bande', [(1355, 320), (1390, 320), (1390, 505), (1355, 505)], COUL['2'], 'Échafaudage, face est, sur la toiture du basilaire est [lecture]'),
  ('bande', [(1355, 295), (1395, 295), (1395, 345), (1355, 345)], COUL['2'], ''),
  ('rect', (1170, 255, 1293, 293), '#8e24aa', 'plein', 'Hémodialyse : rebranchement des conduits, passerelle réinstallée'),
  ('point', (1362, 322), '#8e24aa', 'Conduit de la hotte de médecine nucléaire (arrêt vendredi-dimanche)'),
 ],
 '3a': SITE_COMMUN + [
  ('bande', [(865, 555), (1355, 555), (1355, 588), (865, 588)], COUL['3'], 'Échafaudage, façade sud des basilaires I, H, G (3.S)'),
  ('bande', [(862, 216), (1355, 216), (1355, 250), (862, 250)], COUL['3'], 'Échafaudage, façade nord des basilaires J, B, K (3.N)'),
  ('rect', (945, 140, 1018, 246), '#e65100', 'plein', 'Nouvelle issue du laboratoire et escalier no 7 [lecture]'),
  ('rect', (1045, 600, 1340, 765), '#2e7d32', 'tirets', 'Entrée principale : trois configurations successives (feuille 002, détail 2)'),
  ('point', (812, 262), '#8e24aa', 'Prise d\'air médical temporaire, façade ouest [à confirmer]'),
 ] + AMB_PAR_NORD,
 '3b': SITE_COMMUN + AMB_NORMAL + [
  ('bande', [(787, 250), (822, 250), (822, 555), (787, 555)], COUL['3'], 'Échafaudage, façade ouest du basilaire ouest (3.O)'),
  ('fleche', (690, 440, 785, 440), '#2e7d32', 'Entrée des marchandises au sous-sol maintenue (CI-TAB-013)'),
  ('point', (842, 447), '#8e24aa', 'Évents des autoclaves réinstallés au même endroit (ME-076)'),
 ],
}
