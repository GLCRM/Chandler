"""Données du cahier de phasage par élévation — Hôpital de Chandler R-657-24.

La géométrie des quatre élévations (chaînes d'axes, niveaux, clips) est dans
`elev_geom.py`. Le présent module porte les correspondances de repères, les
appareils relevés façade par façade, les verrous et la séquence type.

Pour chaque appareil : code de la ligne du tableau ME ; état ; libellé court ;
repère de la feuille ME ; coordonnée d'axe [lecture] ; cote de niveau en mm ;
décalage de l'étiquette (dx, dy) ; clé du verrou.
"""
from elev_geom import GEOMS, NIVEAUX, ETATS, MM_PAR_UNITE  # noqa: F401

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
APPAREILS = {'nord': [
 ('N-F-P-002', 'coupe',    'Déshumidification, coude', 'non repéré sur ME001(D)', 15.4, 12600, (34, -96), 'V14'),
 ('N-F-P-001', 'maintenu', "Sortie d'arrosage", 'D3 plomb. — élév. F', 14.55, 10900, (-30, -52), 'V15'),
 ('N-F-E-001', 'coupe',    'Conduit PVC, lampadaires', 'D6 élec. — élév. F', 13.53, 12400, (-14, -74), 'V10'),
 ('N-F-V-001', 'coupe',    'Col de cygne, atelier GBM', 'D4 vent. — élév. F', 12.51, 10700, (10, -44), 'V8'),
 ('N-F-E-002', 'retire',   'Antenne au toit et conduit PVC', 'D7 élec. — élév. F', 11.9, 14900, (-26, -30), None),
 ('N-F-E-003', 'coupe',    'Câblage de paratonnerre', 'D11 élec. — élév. F', 11.0, 14900, (16, -30), None),
 ('N-F-V-002', 'coupe',    'Persienne RAV, saut-de-loup S17', 'D2 vent. — élév. F', 11.6, 10600, (26, -30), 'V9'),
 ('N-F-E-004', 'coupe',    'Caméra, coin escalier no 3', 'D8 élec. — élév. F', 9.70, 15600, (-36, -46), 'V11'),
 ('N-F-V-010', 'deplace',  'Persienne PAF P-05', 'D5 vent. — élév. F', 9.38, 16800, (-16, -60), None),
 ('N-F-V-005', 'coupe',    'Unité hémodialyse : 3 conduits + passerelle', 'D7 vent. — élév. F', 7.13, 17901, (0, -62), 'V1'),
 ('N-F-V-004', 'coupe',    'Ventilateur cloche, stérilisation', 'D6 vent. — élév. F', 8.23, 14200, (-52, 34), 'V7'),
 ('N-F-V-006', 'intact',   'Bi-blocs (8x) non touchés', 'D13 vent. — élév. F', 6.35, 12600, (16, 40), None),
 ('—',         'deplace',  "Sortie d'évent murale de laboratoire", 'D4 plomb. hors tableau', 6.57, 14400, (34, 18), None),
 ('N-F-V-007', 'coupe',    "Sortie d'air murale, secteur labo", 'D8 vent. — élév. F', 5.67, 14400, (30, -24), 'V5'),
 ('N-F-V-008', 'coupe',    'Persienne RAV P-06, chambre 216', 'D15 vent. — élév. F', 4.63, 21000, (-46, -26), 'V4'),
 ('N-F-V-009', 'maintenu', 'Persienne PAF P-07, soins intensifs 315', 'D9 vent. — élév. F', 4.11, 24600, (-10, -28), 'V3'),
 ('N-F-V-003', 'coupe',    'Évacuation V-53, toilette du labo', 'non repéré séparément', 3.78, 13100, (44, -18), 'V6'),
 ('N-F-V-011', 'coupe',    "Trappes d'accès pour mécanique", 'D11 vent. — élév. F', 2.75, 13300, (16, -60), 'V16'),
 ('N-F-V-012', 'deplace',  'Persienne sous porte-à-faux P-08', 'D12 vent. — élév. F', 2.52, 13000, (-62, -20), None),
 ('N-F-E-005', 'retire',   'Prise extérieure, porte nord du quai', 'D9 élec. — élév. F', 0.92, 11600, (-64, -97), None),
 ('N-F-E-006', 'coupe',    'Luminaire mural, porte piéton nord', 'D3 élec. — élév. F', 0.80, 12200, (-64, -63), 'V12'),
 ('N-F-E-007', 'coupe',    'Lecteur de carte, porte piéton nord', 'D2 élec. — élév. F', 1.02, 11100, (-64, -52), 'V12'),
 ('N-F-E-008', 'coupe',    'Clavier, porte de garage nord', 'D10 élec. — élév. F', 0.86, 10600, (-64, -33), 'V13'),
 ('N-F-GM-001','maintenu', "Prise d'air de la centrale d'air médical", 'non repéré sur ME001(D)', 3.30, 25600, (-4, -30), 'V2'),
],
 'est': [
 # relevé sur ME002D (élévation G) et ME003D (élévations partielles D et H) ;
 # positions mesurées sur la géométrie vectorielle des feuilles, ±2 % d'entraxe
 ('E-G-V-004', 'coupe',    "Capotin de la hotte de cuisine, salle communautaire", 'D6 vent. — élév. G', 7.07, 27590, (30, -26), 'VE7'),
 ('E-G-E-001', 'coupe',    'Luminaire linéaire sous parapet, tour est', 'D7 élec. — élév. G', 6.61, 29750, (-40, -26), 'VE4'),
 ('E-G-V-001', 'retire',   'Persienne P-11 du fumoir, à démanteler', 'D5 vent. — élév. G', 7.91, 23625, (-46, -26), 'VE5'),
 ('E-G-V-002', 'retire',   'Persienne P-12, usage non écrit', 'D5 vent. — élév. G', 6.67, 23625, (20, -30), 'VE5'),
 ('E-H-V-001', 'coupe',    'Conduit de la hotte de médecine nucléaire', 'D3 vent. — élév. H', 2.04, 22000, (44, -24), 'VE1'),
 ('E-G-V-003', 'coupe',    "Bi-bloc thermopompe, traitement d'eau 203", 'D7 vent. — élév. G', 7.85, 19815, (44, -16), 'VE2'),
 ('E-G-E-006', 'coupe',    'Câblage du bi-bloc, salle des serveurs', 'D11 élec. — élév. G', 7.85, 19815, (-50, -42), 'VE3'),
 ('E-G-E-002', 'coupe',    'Luminaire linéaire, basilaire est', 'D7 élec. — élév. G', 9.79, 18025, (-40, -30), 'VE4'),
 ('E-G-E-003', 'coupe',    'Luminaire linéaire, basilaire est', 'D7 élec. — élév. G', 5.54, 18025, (0, -30), 'VE4'),
 ('E-G-E-004', 'coupe',    "Conduit EMT de l'éclairage linéaire", 'D10 élec. — élév. G', 9.02, 16200, (-46, 26), 'VE4'),
 ('E-G-E-005', 'coupe',    'Caméra du stationnement est', 'D8 élec. — élév. G', 2.06, 13925, (40, -26), 'VE6'),
 ('E-H-E-001', 'coupe',    "Luminaire de la porte de l'escalier no 3", 'D3 élec. — élév. H', 3.85, 12100, (-30, 30), 'VE8'),
 ('E-H-E-002', 'coupe',    "Lecteur de carte, porte de l'escalier no 3", 'D2 élec. — élév. H', 3.34, 11115, (40, 26), 'VE8'),
 ('E-H-V-002', 'intact',   'Bi-bloc non touché', 'D6 vent. — élév. H', 0.45, 11015, (30, -26), 'VE9'),
 ('E-D-V-001', 'intact',   'Bi-bloc de la salle des serveurs, non touché', "non repéré : l'élévation D ne porte aucun axe", 0.0, 13815, (0, 0), 'VE9'),
],
 'sud': [
 # relevé sur ME002D (élévation A) ; positions mesurées sur la géométrie
 # vectorielle de la feuille, ±0,05 axe et ±150 mm. Lu de l'ouest (gauche)
 # vers l'est (droite) : l'entrée des ambulances est à l'ouest de l'axe 1.
 ('S-A-E-004', 'intact',   "Boutons d'ouverture, porte de garage", 'D4 élec. — élév. A', 0.31, 12670, (-30, -74), 'VS1'),
 ('S-A-E-005', 'intact',   'Feux rouge et vert de la porte de garage', 'D4 élec. — élév. A', 0.31, 11450, (-30, 30), 'VS1'),
 ('S-A-PI-001', 'coupe',   "Gicleurs sous le toit des ambulances", 'D1 gicl. — élév. A', 0.53, 12885, (-30, -44), 'VS2'),
 ('S-A-E-006', 'coupe',    'Enseigne AMBULANCE illuminée', 'D5 élec. — élév. A', 0.58, 13820, (0, -58), 'VS1'),
 ('S-A-E-003', 'intact',   "Contrôles d'accès et sonnette d'urgence", 'D4 élec. — élév. A', 0.78, 11330, (30, 46), 'VS1'),
 ('—',         'deplace',  "Évents de vapeur de l'autoclave (2x)", 'D2 plomb. — élév. A, hors tableau', 0.84, 18140, (16, -40), 'VS14'),
 ('S-A-E-002', 'intact',   'Luminaire de la porte piéton du garage', 'D4 élec. — élév. A', 0.86, 12930, (36, -36), 'VS1'),
 ('—',         'deplace',  'Évents de vapeur de la chaufferie (3 annoncés)', 'D3 plomb. — élév. A, hors tableau', 0.93, 17370, (52, -18), 'VS14'),
 ('—',         'deplace',  'Thermostat des câbles chauffants', 'D14 élec. — élév. A, hors tableau', 1.06, 16270, (56, -14), 'VS15'),
 ('S-A-V-001', 'deplace',  "Unité bi-bloc GREE, prélèvement urg.", 'D1 vent. — élév. A', 1.10, 10660, (48, 28), 'VS3'),
 ('S-A-E-008', 'retire',   'Ancien câblage derrière la thermopompe', 'D12 élec. — élév. A', 1.16, 11250, (58, 4), 'VS3'),
 ('S-A-E-007', 'coupe',    'Sectionneur de la thermopompe', 'D6 élec. — élév. A', 1.18, 10850, (58, 20), 'VS3'),
 ('S-A-E-012', 'intact',   'Boîte de jonction du mur de fondation', 'D4 élec. — élév. A', 1.26, 9880, (62, 32), 'VS1'),
 ('S-A-E-010', 'coupe',    'Luminaire, porte salle du personnel', 'D3 élec. — élév. A', 1.51, 13110, (52, -32), 'VS7'),
 ('S-A-E-009', 'coupe',    'Lecteur de carte, salle du personnel', 'D2 élec. — élév. A', 1.60, 11440, (58, -8), 'VS7'),
 ('S-A-E-011', 'coupe',    'Prise extérieure du secteur de pause', 'D1 élec. — élév. A', 1.62, 10770, (58, 16), 'VS7'),
 ('S-A-E-013', 'coupe',    "Prise extérieure sous l'auvent de pause", 'D1 élec. — élév. A', 2.64, 13170, (0, -32), 'VS7'),
 ('S-A-V-002', 'deplace',  "Persienne PAF P-13 de l'unité UT-2", 'D2 vent. — élév. A', 2.73, 15980, (0, -34), 'VS4'),
 ('S-A-V-003', 'deplace',  'Persienne RAV P-14, chambre 307', 'D3 vent. — élév. A', 3.62, 23650, (0, -30), 'VS5'),
 ('S-A-E-014', 'coupe',    'Bandeau lumineux, basilaire ouest n. 200', 'D7 élec. — élév. A (axes 2 à 7)', 4.50, 18010, (0, -30), 'VS6'),
 ('S-A-E-015', 'coupe',    'Bandeau lumineux, tour, sous parapet', 'D7 élec. — élév. A (axes 1 à 9)', 5.00, 29750, (0, 34), 'VS6'),
 ('S-A-E-021', 'coupe',    "Prise en hauteur, entrée principale", 'D1 élec. — élév. A', 7.33, 13670, (0, -30), 'VS13'),
 ('S-A-E-017', 'coupe',    'Bandeau lumineux, basilaire est RDC', 'D7 élec. — élév. A (axes 7 à 8,9)', 7.90, 14440, (0, 32), 'VS6'),
 ('S-A-E-024', 'coupe',    "Conduit EMT de l'éclairage linéaire", 'D10 élec. — élév. A', 9.90, 14860, (-24, -30), 'VS6'),
 ('S-A-E-019', 'coupe',    "Lecteur de carte, escalier no 4", 'D2 élec. — élév. A', 9.96, 11390, (0, 30), 'VS8'),
 ('S-A-E-020', 'deplace',  "Caméra du secteur de l'IRM mobile", 'D13 élec. — élév. A', 10.09, 14520, (34, -30), 'VS9'),
 ('S-A-V-004', 'deplace',  'Grille sous la marquise du garage IRM', 'D4 vent. — élév. A', 10.86, 13600, (0, 34), 'VS10'),
 ('S-A-E-016', 'coupe',    'Bandeau lumineux, basilaire est n. 200', 'D7 élec. — élév. A (axes 9,4 à 15)', 12.20, 18020, (0, -30), 'VS6'),
 ('S-A-E-022', 'retire',   'Conduit et câblage télécom désuets', 'D9 élec. — élév. A (axes 10,8 à 14,9)', 12.84, 10050, (0, -36), 'VS11'),
 ('S-A-E-018', 'coupe',    'Bandeau lumineux, basilaire est RDC', 'D7 élec. — élév. A (axes 11 à 16)', 13.50, 14490, (0, 32), 'VS6'),
 ('S-A-P-001', 'coupe',    "Sortie d'arrosage, stationnement IRM", 'D1 plomb. — élév. A', 14.55, 10460, (-34, -30), 'VS12'),
 ('S-A-E-023', 'coupe',    'Caméra du coin oncologie', 'D8 élec. — élév. A', 14.80, 13420, (34, -30), 'VS9'),
 ('S-A-E-001', 'intact',   "Luminaires muraux (2x), entrée du garage", 'non repéré : 7 cibles D4, 6 lignes grises', 0.50, 12000, (0, 0), 'VS1'),
],
 'ouest': [
 # relevé sur ME001D (élévation B) et ME003D (élévations partielles C, E, I) ;
 # positions mesurées sur la géométrie vectorielle, ±2 % d'entraxe. Les
 # appareils des élévations partielles sont reportés sur l'élévation B le long
 # de la même chaîne d'axes. Lu du nord (gauche) vers le sud (droite).
 ('—',         'deplace',  'Persienne PAF du service alimentaire', 'D10 vent. — élév. B, hors tableau', -0.32, 10300, (0, -44), 'VO14'),
 ('O-B-E-006', 'coupe',    "Sectionneur thermopompe observation", 'D4 élec. — élév. B', -0.05, 15640, (-16, -32), 'VO7'),
 ('O-B-V-005', 'coupe',    "Unité bi-bloc de la salle d'observation", 'D3 vent. — élév. B', 0.08, 15795, (34, -52), 'VO7'),
 ('—',         'deplace',  "Unité de vent. de l'hémodialyse et passerelle", 'D7 vent. — élév. B, hors tableau', 0.19, 19000, (44, -30), 'VO2'),
 ('O-B-E-002', 'coupe',    'Luminaire, porte labo. [à confirmer]', 'D3 élec. — élév. B', 1.19, 16585, (-20, -42), 'VO10'),
 ('O-B-E-004', 'coupe',    'Lecteur de carte, porte labo. [à confirmer]', 'D2 élec. — élév. B', 1.20, 15845, (-20, 30), 'VO10'),
 ('O-B-E-007', 'coupe',    'Bandeau lumineux sous parapet, tour ouest', 'D5 élec. — élév. B', 1.56, 30025, (0, 32), 'VO9'),
 ('O-B-V-001', 'deplace',  'Conduit PAF du bloc opératoire, en surface', 'D1 vent. — élév. B', 2.74, 19000, (-34, -30), 'VO1'),
 ('O-B-V-004', 'coupe',    'Persienne RAV P-01, garage ambulances', 'D15 vent. — élév. B', 2.82, 13440, (0, 32), 'VO5'),
 ('O-I-E-001', 'coupe',    "Luminaire, escalier no 6", 'D3 élec. — élév. I', 3.45, 12460, (0, -32), 'VO13'),
 ('O-I-E-002', 'coupe',    "Lecteur de carte, escalier no 6", 'D2 élec. — élév. I', 3.44, 11420, (0, 32), 'VO13'),
 ('—',         'deplace',  'Conduits PAF temporaires, bloc opératoire', 'D14 vent. — élév. B, hors tableau, informatif', 5.44, 18600, (0, -42), 'VO1'),
 ('O-E-E-003', 'maintenu', "Caméra de l'urgence", 'D8 élec. — élév. E', 6.02, 13010, (-34, 30), 'VO12'),
 ('O-E-E-002', 'coupe',    "Détecteur de mouvement, issue urgence", 'D9 élec. — élév. E', 6.16, 12240, (0, 36), 'VO12'),
 ('O-B-E-005', 'coupe',    'Lecteur de carte, bloc op. [à confirmer]', 'D2 élec. — élév. B', 6.36, 15665, (-20, 30), 'VO10'),
 ('O-B-E-003', 'coupe',    'Luminaire, porte bloc op. [à confirmer]', 'D3 élec. — élév. B', 6.39, 16355, (-20, -36), 'VO10'),
 ('O-E-V-001', 'intact',   'Persienne de la chambre à pression négative', 'D1 vent. — élév. E', 6.46, 12460, (20, 42), 'VO12'),
 ('O-E-E-001', 'intact',   "Lecteur de carte, issue urgence", 'D4 élec. — élév. E', 6.69, 10930, (32, 30), 'VO12'),
 ('O-B-P-001', 'deplace',  "Évents de vapeur de l'autoclave", 'D1 plomb. — élév. B', 7.04, 17550, (0, -30), 'VO3'),
 ('O-B-V-002', 'coupe',    'Persienne RAV P-02, méc. chirurgie', 'D16 vent. — élév. B', 7.82, 16460, (0, -34), 'VO6'),
 ('O-B-P-002', 'deplace',  'Évents inox du réservoir de condensé', 'D2 plomb. — élév. B', 7.93, 15850, (32, 20), 'VO4'),
 ('O-B-E-001', 'coupe',    'Thermostat Pyrotenax des câbles chauffants', 'D1 élec. — élév. B', 8.14, 16020, (42, -14), 'VO8'),
 ('—',         'coupe',    'Enseigne « ambulance urgence »', 'D5 élec. — élév. E, hors tableau', 8.65, 13655, (0, -32), 'VO12'),
 ('O-C-E-003', 'coupe',    "Luminaire mural, escalier no 4", 'D3 élec. — élév. C', 9.63, 13535, (0, 32), 'VO11'),
 ('O-B-V-003', 'deplace',  "Persienne RAV P-03 de l'unité UT-2", 'D15 vent. — élév. B', 9.71, 16040, (0, -32), 'VO6'),
 ('O-C-V-001', 'deplace',  "Persiennes échangeur IRM mobile (2)", 'D4 vent. — élév. C', 11.37, 13455, (0, -36), 'VO11'),
 ('O-C-E-004', 'maintenu', 'Prise extérieure, circuit conservé', 'D1 élec. — élév. C', 11.45, 10330, (-20, 30), 'VO11'),
 ('O-C-E-002', 'coupe',    "Luminaire, porte préparation IRM", 'D3 élec. — élév. C', 11.80, 12670, (0, -32), 'VO11'),
 ('O-C-E-001', 'deplace',  "Raccordements roulotte IRM mobile", 'D7 élec. — élév. C', 11.90, 10535, (0, 36), 'VO11'),
]}

# --- verrous appareil <-> architecture ------------------------------------
# clé ; appareil ; ce qui doit être fait avant ; étape d'architecture bloquée ; source
VERROUS = {'nord': [
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
],
 'est': [
 ('VE1', "Conduit d'évacuation de la hotte de médecine nucléaire (E-H-V-001), axe B', toute la hauteur de la tour",
  "Aucun préalable écrit ; l'arrêt se prend du vendredi au dimanche",
  "E2 et E4 sur toute la hauteur près de l'axe B' : le conduit est modifié à la base et à la tête de la tour pour l'épaisseur du nouveau mur, supports muraux galvanisés remplacés",
  "D5 E-H-V-001 ; ME003D repère H note D3 ventilation ; ME-118, ME-119"),
 ('VE2', "Bi-bloc thermopompe de la salle de traitement d'eau 203, hémodialyse (E-G-V-003), entre F et E, niveau 200",
  "Récupérer le réfrigérant, prolonger et protéger le tubage, prévoir un support temporaire, puis remise en marche",
  "E2 : l'unité et son support au toit sont démantelés temporairement ; **coupure en semaine, hors période estivale**",
  "D5 E-G-V-003 ; ME002D note D7 ventilation ; ME-087"),
 ('VE3', "Câblage de l'unité extérieure bi-bloc de la salle des serveurs (E-G-E-006), même point que VE2",
  "Aucun préalable écrit",
  "E2 ; arrêt de courte durée, **en semaine hors période estivale** — la salle des serveurs est critique",
  "D5 E-G-E-006 ; ME002D note D11 électricité ; ME-088"),
 ('VE4', "Éclairage linéaire d'ambiance sous parapet et son conduit EMT (E-G-E-001 à 004) — bandeau continu sur toute la façade est, tour et basilaire",
  "Entreposage adéquat des luminaires déposés",
  "E2 : le bandeau est déposé sur toute la longueur traitée ; **hors service toute la durée des travaux du secteur**. C'est l'éclairage extérieur de toute la façade est",
  "D5 E-G-E-001 à E-G-E-004 ; ME002D notes D7 et D10 électricité"),
 ('VE5', "Persiennes P-11 et P-12 (E-G-V-001, E-G-V-002), entre D.2 et F, niveau 300-400",
  "Aucun préalable : aucune remise en service ni mesure temporaire requise",
  "E2 ; **le plénum dans le mur derrière la persienne est démantelé complètement** — intervention intérieure à coordonner avec l'occupant",
  "D5 E-G-V-001, E-G-V-002 ; ME002D note D5 ventilation"),
 ('VE6', "Caméra du stationnement est (E-G-E-005), entre C et B', niveau 100",
  "Entreposage adéquat",
  "E2 ; hors service toute la durée des travaux du secteur — le tableau ne prévoit pas de relocalisation temporaire, contrairement aux caméras des autres façades",
  "D5 E-G-E-005 ; ME002D note D8 électricité"),
 ('VE7', "Sortie d'air de la salle communautaire, capotin de hotte de cuisine (E-G-V-004), entre F et E, sous le niveau 500",
  "Aucun préalable écrit",
  "E2 et E4 : capotin remplacé, conduit d'évacuation prolongé selon l'épaisseur de l'enveloppe. **Le tableau marque cette ligne « à valider »** : durée et période non écrites",
  "D5 E-G-V-004 (cellule jaune) ; ME002D note D6 ventilation ; ME-142"),
 ('VE8', "Luminaire et lecteur de carte de la porte de l'escalier no 3 (E-H-E-001, E-H-E-002), entre D.1 et C, rez-de-chaussée",
  "Aucun préalable écrit",
  "E2 ; hors service toute la durée des travaux du secteur : la porte de l'escalier no 3 reste inutilisable pendant ce temps (note 8 de la légende du tableau)",
  "D5 E-H-E-001, E-H-E-002 ; ME003D repère H notes D2 et D3 électricité"),
 ('VE9', "Bi-blocs non touchés (E-H-V-002, entre A et B ; E-D-V-001, salle des serveurs)",
  "Protection pendant les travaux",
  "Aucune étape bloquée ; à ne pas heurter. E-D-V-001 dessert la salle des serveurs, marquée « critique » au tableau",
  "D5 E-H-V-002, E-D-V-001 (cellules grises) ; ME003D repères H et D notes D6 et D2 ventilation"),
],
 'sud': [
 ('VS1', "Appareils de l'entrée des ambulances : portes de garage et piéton, enseigne (S-A-E-001 à 006, S-A-E-012), à l'ouest de l'axe 1",
  "Aucun préalable écrit pour les six lignes grises « non touchées » ; l'enseigne AMBULANCE est débranchée par l'électricien puis enlevée par l'entrepreneur général",
  "E2 sous la marquise ; l'enseigne est hors service **toute la durée des travaux de ce secteur**, alors que la feuille 002 impose un panneau indicateur d'ambulance **par phase** (AR-PLN-014)",
  "D5 S-A-E-001 à 006, S-A-E-012 ; ME002D notes D4 et D5 électricité ; AR-PLN-014, AR-PLN-018"),
 ('VS2', "Gicleurs et tuyauterie sous le toit de l'entrée des ambulances (S-A-PI-001), axes 0,3 et 0,8",
  "Mise hors service de cette zone du réseau de protection incendie, obturation temporaire de la tuyauterie, récupération du glycol — deux coupures de 2 h",
  "E2 sous la marquise. **Seule ligne de protection incendie de tout le tableau** : la mise hors service d'une zone de gicleurs relève de la procédure PCI et du préavis au CISSS",
  "D5 S-A-PI-001 ; ME002D note D1 gicleurs (voir vues agrandies en plan)"),
 ('VS3', "Unité bi-bloc GREE 12 MBH, sectionneur et ancien câblage (S-A-V-001, S-A-E-007, S-A-E-008), axe 1,1",
  "Récupérer le réfrigérant, prolonger et protéger le tubage, support temporaire, puis remise en marche : l'unité reste en opération",
  "E2 et E4 ; **période écrite : en dehors de la période estivale** — mais la même cellule ajoute « quelques jours en été ». La ligne se contredit elle-même",
  "D5 S-A-V-001, S-A-E-007, S-A-E-008 ; ME002D notes D1 ventilation, D6 et D12 électricité"),
 ('VS4', "Persienne de prise d'air frais de l'unité UT-2 (S-A-V-002), axe 2,7, entre les niveaux 100 et 200",
  "Coupure rapide de nuit ou de fin de semaine, registre motorisé fermé ; filtration et grillage aviaire temporaires ; persienne récupérée et réinstallée",
  "E2 ; la ventilation du secteur de chirurgie d'un jour reste en fonction. Persienne mesurée ±1 715 x 1 680 mm alors que la note en annonce ±1 600 x 1 500 `[lecture]`",
  "D5 S-A-V-002 ; ME002D note D2 ventilation"),
 ('VS5', "Persienne de renvoi d'air de la chambre à pression négative 307 (S-A-V-003), axe 3,6, entre les niveaux 300 et 400",
  "Démantèlement quand la chambre est inoccupée ; prolongation temporaire du conduit hors des échafaudages ; grillage aviaire temporaire",
  "E2 et E4 ; la fenêtre écrite est « selon le patient dans la chambre » : elle n'est pas planifiable à l'avance et doit être tenue en réserve dans la séquence",
  "D5 S-A-V-003 ; ME002D note D3 ventilation"),
 ('VS6', "Bandeau lumineux linéaire d'ambiance et son conduit EMT (S-A-E-014 à 018, S-A-E-024) — cinq tronçons couvrant presque toute la façade",
  "Entreposage adéquat des luminaires déposés",
  "E2 sur toute la longueur traitée ; **hors service toute la durée des travaux du secteur**. C'est l'éclairage extérieur de la façade de l'entrée principale : la longueur du tronçon attaqué d'un coup fixe l'étendue laissée sans éclairage la nuit",
  "D5 S-A-E-014 à 018, S-A-E-024 ; ME002D notes D7 et D10 électricité"),
 ('VS7', "Porte de la salle du personnel et secteur de pause extérieure (S-A-E-009 à 011, S-A-E-013), axes 1,5 à 2,7",
  "Aucun préalable écrit",
  "E2 ; lecteur, luminaire et prises hors service toute la durée des travaux du secteur : la porte de la salle du personnel reste inutilisable pendant ce temps (note 8 de la légende du tableau)",
  "D5 S-A-E-009 à 011, S-A-E-013 ; ME002D notes D1, D2 et D3 électricité"),
 ('VS8', "Lecteur de carte de la porte de l'escalier no 4 (S-A-E-019), axe 10",
  "Plan d'action des issues approuvé avant toute fermeture (étape E1)",
  "E2 ; hors service toute la durée des travaux du secteur — cette porte est une issue et son chemin d'évacuation doit rester libre sur 1 650 mm (AR-PLN-006)",
  "D5 S-A-E-019 ; ME002D note D2 électricité ; AR-PLN-006"),
 ('VS9', "Caméras de la façade sud : S-A-E-020 à relocaliser, S-A-E-023 à enlever, axes 10,1 et 14,8",
  "Pour S-A-E-020 : relocalisation conservant le même champ, coupure la plus courte possible, coordination avec le propriétaire",
  "E2 ; les deux caméras ne sont pas traitées de la même façon — celle du coin oncologie est simplement hors service toute la durée des travaux, sans relocalisation prévue",
  "D5 S-A-E-020, S-A-E-023 ; ME002D notes D8 et D13 électricité"),
 ('VS10', "Grille d'entrée d'air sous la marquise de la porte de garage de l'IRM mobile (S-A-V-004), axe 10,9",
  "Aucun préalable écrit ; la grille est enlevée puis réinstallée au même endroit",
  "E2 et E6 ; elle alimente le soufflage des coussins de protection de la porte de garage et doit être en fonction **lorsque la roulotte d'IRM est en place** : la fenêtre est celle des absences de la roulotte",
  "D5 S-A-V-004 ; ME002D note D4 ventilation"),
 ('VS11', "Conduit et câblage de télécommunication désuets (S-A-E-022), axes 10,8 à 14,9, au niveau du sol",
  "Aucun préalable : le câblage ne sert plus",
  "E1 ou E2 ; cellule orange, à enlever. Il court au sol sur quatre travées, dans la zone de stationnement de l'IRM où aucun entreposage métallique n'est permis quand l'IRM est en service (AR-PLN-009)",
  "D5 S-A-E-022 (cellule orange) ; ME002D note D9 électricité ; AR-PLN-009"),
 ('VS12', "Sortie d'arrosage extérieure du stationnement de l'IRM (S-A-P-001), axe 14,6",
  "Verrou inverse : la sortie est conservée et protégée ; c'est l'architecture qui doit absorber la différence d'épaisseur du nouveau revêtement, comme au coin nord-est",
  "E4 ; le tableau l'écrit pourtant hors service toute la durée des travaux, ce qui prive le secteur de point d'eau extérieur `[à confirmer]`",
  "D5 S-A-P-001 ; ME002D note D1 plomberie"),
 ('VS13', "Prise extérieure en hauteur sur le mur de brique de l'entrée principale (S-A-E-021), axe 7,3",
  "Aucun préalable écrit",
  "E2 ; l'entrée principale est le seul endroit du site où la clôture est dessinée en trois configurations successives (feuille 002, détail 2) : le tronçon traité ici commande la configuration d'accès",
  "D5 S-A-E-021 ; ME002D note D1 électricité ; AR-PLN-019"),
 ('VS14', "Évents de vapeur de l'autoclave et de la chaufferie — **aucune ligne au tableau**, axes 0,8 à 0,9, au-dessus de la marquise",
  "Évents de l'autoclave à relocaliser **avant le début des travaux de la façade ouest**, tuyauterie prolongée sur supports temporaires déposés en toiture jusqu'au coin sud-ouest ; évents inox de la chaufferie à modifier",
  "E1 de la façade **ouest**, pas de la sud : verrou inter-façades. Les appareils sont dessinés sur l'élévation sud et l'intervention est rattachée par écrit à l'ouest. La note annonce **3 évents** (150, 150 et 200 mm) ; **un seul est dessiné**",
  "ME002D notes D2 et D3 plomberie ; D5 O-B-P-001 et O-B-P-002 (façade ouest)"),
 ('VS15', "Thermostat des câbles chauffants — **aucune ligne au tableau**, axe 1,1, niveau 100",
  "Aucun préalable écrit",
  "E2 puis E6 : à enlever, puis à réinstaller **sur la colonne** après le revêtement ; conduit EMT à remplacer et à dissimuler au-dessus du soffite jusqu'à l'entrée de la salle de mécanique. Travail d'électricité réel non inscrit au tableau de coordination",
  "ME002D note D14 électricité — aucune ligne S-A-E correspondante"),
],
 'ouest': [
 ('VO1', "Conduit de prise d'air frais du bloc opératoire et ses deux conduits temporaires 900 x 900 (O-B-V-001), axes B' à D.2, du niveau 100 au niveau 300",
  "Conduits temporaires d'air frais posés par l'entrepreneur **en parallèle** du conduit existant et raccordés au plénum sous le soffite, **en plusieurs étapes**",
  "E2 et E4 derrière le conduit existant : le parement ne peut être refait qu'une fois les conduits temporaires en service. Le bloc opératoire reste alimenté sans interruption ; fenêtre écrite « nuit ou fin de semaine, à valider si garde régionale »",
  "D5 O-B-V-001 ; ME001D notes D1 et D14 ventilation (voir vues agrandies en plans)"),
 ('VO2', "Unité de ventilation au toit de l'hémodialyse et du laboratoire, et sa passerelle d'aluminium — **aucune ligne au tableau côté ouest**, axes A à B",
  "Conduits temporaires d'alimentation et de retour d'air frais en place **avant** la démolition de l'enveloppe ; passerelle enlevée, modifiée puis réinstallée par l'entrepreneur général",
  "E2 entre les axes A et B. C'est le même appareil que N-F-V-005 sur la façade nord : les trois conduits traversent le parement de part et d'autre de l'angle nord-ouest, ce que ni le tableau ni la vue en plan ne montrent",
  "ME001D note D7 ventilation ; D5 N-F-V-005 (façade nord) ; ME014 D1 à D4 ; Z-29"),
 ('VO3', "Évents de vapeur de l'autoclave du sous-sol (O-B-P-001), entre E et F",
  "Relocalisation **avant le début des travaux de la façade ouest** : tuyauterie prolongée sur des supports temporaires déposés en toiture jusqu'au coin sud-ouest du bâtiment",
  "E1 de la façade ouest, avant toute démolition. Les évents eux-mêmes sont dessinés sur l'élévation **sud** — verrou inter-façades. Fenêtre écrite : nuit ou le matin avant 10 h",
  "D5 O-B-P-001 ; ME001D note D1 plomberie ; ME002D note D2 plomberie"),
 ('VO4', "Évents de vapeur en inox du réservoir de condensé de la chaufferie (O-B-P-002), entre E et F",
  "Drain de condensats à modifier ; aucune fenêtre écrite autre que « toute »",
  "E2 et E4 ; la colonne monte du niveau 100 au niveau 200 le long du mur traité et doit être reprise avec le nouveau parement",
  "D5 O-B-P-002 ; ME001D note D2 plomberie"),
 ('VO5', "Persienne de renvoi d'air du garage des ambulances, P-01 (O-B-V-004), entre B' et C, niveau 100",
  "Aucun préalable écrit : « travailler avec la persienne en fonction »",
  "E2 et E4 ; **période écrite : en période estivale** — l'une des trois lignes du tableau qui exigent l'été. Dimensions mesurées ±727 x 346 mm, conformes au tableau",
  "D5 O-B-V-004 ; ME001D note D15 ventilation"),
 ('VO6', "Persiennes de renvoi d'air de la chirurgie d'un jour, P-02 et P-03 (O-B-V-002, O-B-V-003), entre E et G",
  "P-03 (unité UT-2) : coupure de nuit ou de fin de semaine, système toujours en fonction. P-02 : arrêt sans limite si la température est contrôlée",
  "E2 et E4 ; plénums prolongés selon l'épaisseur de la nouvelle enveloppe. **Divergence à lever** : le tableau écrit « persienne existante à relocaliser » pour O-B-V-002 alors que la note du dessin dit « à remplacer par une persienne moins large pour libérer l'espace requis aux travaux de l'enveloppe »",
  "D5 O-B-V-002, O-B-V-003 ; ME001D notes D15 et D16 ventilation"),
 ('VO7', "Unité bi-bloc de la salle d'observation sur garde-corps et son sectionneur (O-B-V-005, O-B-E-006), à l'aplomb de l'axe A",
  "Unité enlevée temporairement ; elle est réinstallée **sur le garde-corps modifié**, donc après lui",
  "Verrou inverse en E6 : le garde-corps G-02 de la feuille 703 doit être posé avant la réinstallation de l'unité (AR-PLN-070). Hors service toute la durée des travaux du secteur — climatisation non critique",
  "D5 O-B-V-005, O-B-E-006 ; ME001D notes D3 ventilation et D4 électricité ; AR-PLN-070 ; ME-085, ME-090"),
 ('VO8', "Thermostat Pyrotenax et câble chauffant des conduits (O-B-E-001), entre F et F'",
  "Aucun préalable écrit ; thermostat réinstallé sur la colonne, conduit EMT remplacé et dissimulé au-dessus du soffite",
  "E2 à E6 ; **seule ligne du tableau bornée à la période hivernale** : « en dehors de la période hivernale », durée écrite « mois ». Le câble protège les conduits du gel : ce tronçon d'enveloppe doit être refermé avant l'hiver",
  "D5 O-B-E-001 ; ME001D note D1 électricité"),
 ('VO9', "Bandeau lumineux linéaire sous parapet de la tour ouest (O-B-E-007), entre B et B'",
  "Entreposage adéquat des luminaires déposés",
  "E2 ; hors service toute la durée des travaux du secteur. Une seule ligne ici, contre cinq au sud et quatre à l'est : l'éclairage d'ambiance de la façade ouest est plus court",
  "D5 O-B-E-007 ; ME001D note D5 électricité"),
 ('VO10', "Portes du laboratoire et du bloc opératoire : luminaires et lecteurs de carte (O-B-E-002 à 005)",
  "Aucun préalable écrit",
  "E2 ; les quatre appareils sont hors service toute la durée des travaux de leur secteur. **Lequel des deux couples dessert le laboratoire et lequel le bloc opératoire n'est pas déterminable sur les feuilles ME** : les bulles sont identiques. Le plan du niveau 100 doit trancher `[à confirmer]`",
  "D5 O-B-E-002 à 005 ; ME001D notes D2 et D3 électricité"),
 ('VO11', "Secteur de la roulotte d'IRM mobile, élévation partielle C (O-C-E-001 à 004, O-C-V-001)",
  "Composants de raccordement de la roulotte enlevés puis relocalisés au même endroit ; persiennes de l'échangeur enlevées puis réinstallées après le revêtement",
  "E2 et E6 ; tout reste en fonction **lorsque la roulotte est en place** — la fenêtre est celle de ses absences. Contrainte de site liée : aucun entreposage métallique dans cette zone quand l'IRM est en service (AR-PLN-009)",
  "D5 O-C-E-001 à 004, O-C-V-001 ; ME003D repère C notes D1, D3, D4 et D7"),
 ('VO12', "Entrée de l'urgence, élévation partielle E (O-E-E-001 à 003, O-E-V-001) et enseigne « ambulance urgence » hors tableau",
  "Caméra et détecteur relocalisés avec boîte étanche en surface et câblage dissimulé dans l'entreplafond ; enseigne débranchée par l'électricien et enlevée par l'entrepreneur général",
  "E2 ; **la caméra de l'urgence ne tolère aucun arrêt** (O-E-E-003, « aucun arrêt » écrit au tableau) : la relocalisation doit être faite et vérifiée avant la dépose. Le lecteur de carte et la persienne de la chambre à pression négative sont marqués non touchés",
  "D5 O-E-E-001 à 003, O-E-V-001 ; ME003D repère E notes D1 ventilation, D4, D5, D8 et D9 électricité"),
 ('VO13', "Porte de l'escalier no 6, élévation partielle I (O-I-E-001, O-I-E-002)",
  "Plan d'action des issues approuvé avant toute fermeture (étape E1)",
  "E2 ; luminaire et lecteur hors service toute la durée des travaux du secteur : l'escalier no 6 reste inutilisable pendant ce temps",
  "D5 O-I-E-001, O-I-E-002 ; ME003D repère I notes D2 et D3 électricité ; AR-PLN-006"),
 ('VO14', "Persienne de prise d'air frais du service alimentaire au sous-sol — **aucune ligne au tableau**, à gauche de l'axe A",
  "Soufflage de tôle remplacé par l'entrepreneur général et persienne remplacée ; conduit à modifier pour l'ajout d'un registre coupe-feu",
  "E2 et E4 ; le registre coupe-feu renvoie à une vue agrandie en plan. Aucune ligne du tableau ne couvre l'appareil, alors qu'il alimente le service alimentaire du sous-sol",
  "ME001D notes D10 et D17 ventilation — aucune ligne O-B correspondante"),
]}

# --- commentaire de fin de planche, par façade ----------------------------
COMMENTAIRES = {
 'nord': '<div class="txt"><b>Un conflit saisonnier interne à la seule façade nord.</b> Trois lignes du tableau se contredisent sur la saison : N-F-V-005 (unité de l\'hémodialyse) exige le dimanche <b>hors période estivale</b>, N-F-P-002 (déshumidification) autorise l\'arrêt <b>sauf en période estivale</b>, et N-F-E-008 (clavier de la porte de garage) est écrit <b>en période estivale</b>. La même façade porte donc une intervention qui exige l\'été et deux qui l\'excluent — voir la planche de synthèse pour le texte exact des six lignes concernées et pour la fenêtre estivale retenue.<br><br>'
  '<b>Deux verrous inverses.</b> V15 et V16 ne sont pas des appareils qui bloquent l\'architecture, mais l\'architecture qui doit livrer : une alcôve dans le nouveau revêtement pour la sortie d\'arrosage encastrée, et de nouvelles trappes d\'accès identiques, sans lesquelles la mécanique du porte-à-faux devient inaccessible.<br><br>'
  '<b>Ce que WSP doit encore écrire.</b> Le tracé et la forme des conduits temporaires de l\'unité d\'hémodialyse, la séquence de basculement et les fenêtres d\'interruption au-delà de « une journée, un conduit à la fois » (Z-29) ; la position de la prise d\'air de la centrale d\'air médical, placée sur l\'élévation F sans qu\'aucun repère ne la montre.</div>',
 'est': '<div class="txt"><b>Un bandeau lumineux continu commande toute la façade.</b> Les lignes E-G-E-001 à 004 ne sont pas quatre appareils ponctuels mais un <b>éclairage linéaire continu sous parapet</b>, sur la tour et sur le basilaire, avec son conduit d\'alimentation. Il est hors service pendant toute la durée des travaux du secteur traité. Sur une façade de plus de cent mètres, la longueur du tronçon attaqué d\'un coup détermine donc directement l\'étendue de façade laissée sans éclairage extérieur la nuit.<br><br><b>Deux interruptions sont bornées à la semaine hors période estivale</b> : le bi-bloc de la salle de traitement d\'eau de l\'hémodialyse (E-G-V-003) et le câblage du bi-bloc de la salle des serveurs (E-G-E-006), deux locaux critiques. Elles tombent au même endroit de l\'élévation, entre les axes F et E au niveau 200 : <b>une seule fenêtre peut servir aux deux</b> si elles sont coordonnées.<br><br><b>Trois écarts entre le tableau et les dessins</b>, à faire lever par WSP : le tableau situe E-G-E-006 à la salle des serveurs alors que le dessin accole cette bulle à l\'unité LG du toit ; le tableau dit « persienne à relocaliser » pour E-G-V-001 et 002 alors que la note du dessin dit « à démanteler complètement, aucune remise en service » ; le tableau écrit « supports muraux » pour E-G-V-003 alors que la note dit « support au toit ».<br><br><b>Deux repères sans ligne au tableau.</b> Le sectionneur de thermopompe du repère D (note D6 électricité de ME003D) ne porte aucune ligne. Et l\'unité de ventilation de l\'hémodialyse apparaît aussi sur l\'élévation est partielle H, alors que le tableau ne la porte qu\'au nord (N-F-V-005) — cohérent si l\'intervention est une affaire de face nord, `[à confirmer]`.<br><br><b>Une élévation sans axe.</b> Le repère D de la feuille ME003D ne porte aucune ligne d\'axe : la position de E-D-V-001 n\'est pas déterminable et n\'est donc pas dessinée ici.</div>',
 'sud': '<div class="txt"><b>Tout se joue à l\'ouest de l\'axe 1.</b> Treize des trente-trois appareils relevés sur la façade sud sont concentrés sous et autour de la marquise de l\'entrée des ambulances, '
  'dans une bande de moins de six mètres qui déborde la trame numérotée. On y trouve la seule ligne de protection incendie de tout le tableau (gicleurs à mettre hors service, glycol à récupérer), '
  'l\'enseigne AMBULANCE, l\'unité bi-bloc du prélèvement d\'urgence, les évents de vapeur de l\'autoclave et de la chaufferie, et les six lignes grises « non touchées » du groupe D4. '
  'Ce mètre linéaire de façade est le plus chargé du projet : il concentre l\'accès des ambulances, un réseau de gicleurs et deux réseaux de vapeur.<br><br>'
  '<b>Trois travaux réels n\'ont aucune ligne au tableau.</b> Le thermostat des câbles chauffants (note D14 électricité), les évents de vapeur de l\'autoclave (D2 plomberie) et ceux de la chaufferie (D3 plomberie) '
  'sont repérés sur le dessin mais absents du tableau de coordination. Les évents de l\'autoclave sont rattachés par écrit à la façade <b>ouest</b> : ils sont physiquement au sud et doivent être relocalisés avant le début de l\'ouest. '
  'Et la note de la chaufferie annonce <b>trois</b> évents (150, 150 et 200 mm) alors qu\'un seul est dessiné.<br><br>'
  '<b>Six lignes grises, sept cibles indiscernables.</b> Le groupe D4 « équipement existant à conserver » porte sept cibles identiques sur le dessin — de simples carrés sans marquage — pour six lignes du tableau. '
  'L\'appariement individuel est impossible sur les feuilles ME ; les lignes S-A-E-001 (deux luminaires) ne sont donc pas positionnées séparément.<br><br>'
  '<b>Une zone non identifiée au-dessus de la marquise.</b> Une deuxième bulle D1 ventilation pointe un rectangle gris à contour tireté d\'environ 1,47 x 1,17 m, alors que l\'unité bi-bloc qu\'elle décrit est repérée quatre mètres plus bas. '
  'Au même endroit, la feuille 201 porte sa note 24 « conduit de ventilation existant à démolir, voir documents d\'ingénierie ». Ce que représente cette zone n\'est pas déterminable `[à confirmer]` — à faire lever par WSP avant le phasage de ce tronçon.</div>',
 'ouest': '<div class="txt"><b>La façade ouest porte les plus gros travaux temporaires du chantier.</b> Deux conduits de prise d\'air frais de 900 x 900 mm, montant du niveau 100 au niveau 300 sur toute la largeur D.1\'–D.2, '
  'doivent être installés et raccordés au plénum sous le soffite <b>avant</b> de toucher au parement derrière le conduit existant du bloc opératoire — et l\'installation elle-même est écrite « en plusieurs étapes ». '
  'C\'est la plus grosse installation provisoire de tout le projet, et elle n\'apparaît nulle part dans le découpage en plan.<br><br>'
  '<b>L\'unité d\'hémodialyse est ici aussi, et sans ligne au tableau.</b> La note D7 ventilation de ME001D la repère sur l\'élévation ouest avec sa passerelle d\'aluminium et ses trois conduits, mais le tableau ne la porte qu\'au nord (N-F-V-005). '
  'Les conduits traversent le parement de part et d\'autre de l\'angle nord-ouest : <b>le nord et l\'ouest ne peuvent pas être planifiés séparément sur ce point</b> (Z-29).<br><br>'
  '<b>Trois verrous inter-façades partent d\'ici.</b> Les évents de l\'autoclave, dessinés au sud, sont à relocaliser avant le début de l\'ouest ; la prise d\'air médical temporaire se pose à l\'ouest pour permettre le nord ; '
  'les conduits temporaires de l\'hémodialyse précèdent la démolition au nord comme à l\'ouest. L\'ordre des façades est commandé par l\'électromécanique, pas par l\'architecture.<br><br>'
  '<b>Le seul verrou hivernal du projet.</b> Le thermostat Pyrotenax et son câble chauffant (O-B-E-001) sont la seule ligne du tableau bornée « en dehors de la période hivernale », avec une durée écrite en <b>mois</b>. '
  'Sur la même façade, la persienne du garage des ambulances (O-B-V-004) est écrite « en période estivale ». La façade ouest est donc une façade de belle saison.<br><br>'
  '<b>Quatre lignes non départageables.</b> Les luminaires et lecteurs des portes du laboratoire et du bloc opératoire (O-B-E-002 à 005) correspondent à deux couples de bulles identiques ; les feuilles ME ne permettent pas de dire lequel est lequel. '
  'De même, les numéros de persiennes P-01 à P-18 portés sur les dessins ne renvoient à aucune nomenclature retrouvée dans le jeu — l\'appariement repose sur la concordance des dimensions mesurées `[lecture]`.</div>',
}

# --- synthèse des quatre façades ------------------------------------------
# Comptages établis sur les 93 lignes du tableau ME (data/d5_equipements.json).
SYNTHESE_CHIFFRES = [
 ['Façade', 'Lignes', '« Toute la durée des travaux »', 'Fenêtre nommée', 'Non touché (gris)', 'À démanteler (orange)', 'À valider (jaune)'],
 ['Sud (A)',   '30', '17', '2 — hors été (1), nuit ou fin de semaine (1)', '6', '2', '0'],
 ['Ouest (B, C, E, I)', '25', '14', '5 — nuit ou fin de semaine (3), période estivale (1), hors hiver (1)', '2', '0', '0'],
 ['Nord (F)',  '23', '9',  '4 — dimanche hors été, nuit ou jour, tous les soirs, période estivale', '1', '0', '2'],
 ['Est (G, H, D)', '15', '7', '3 — semaine hors été (2), vendredi au dimanche (1)', '2', '0', '1'],
 ['<b>Total</b>', '<b>93</b>', '<b>47</b>', '<b>14</b>', '<b>11</b>', '<b>2</b>', '<b>3</b>'],
]

# Les huit lignes du tableau bornées par une saison, citées mot à mot.
SAISON = [
 ['Ligne', 'Façade', 'Ce que le tableau écrit', 'Sens'],
 ['N-F-E-008', 'Nord', "« En période estivale » — travaux à faire lorsque la porte sera ouverte", "<b>Exige l'été</b>"],
 ['O-B-V-004', 'Ouest', '« Travailler avec persienne en fonction. En période estivale »', "<b>Exige l'été</b>"],
 ['N-F-V-005', 'Nord', '« Dimanche seulement, en dehors de la période estivale »', "Exclut l'été"],
 ['N-F-P-002', 'Nord', 'Colonne durée : « Oui, sauf en période estivale »', "Exclut l'été"],
 ['E-G-V-003', 'Est', '« Semaine, en dehors de la période estivale »', "Exclut l'été"],
 ['E-G-E-006', 'Est', '« Semaine, en dehors de la période estivale »', "Exclut l'été"],
 ['S-A-V-001', 'Sud', '« En dehors de la période estivale (Quelques jours en été) »', '<b>Contradictoire en elle-même</b>'],
 ['O-B-E-001', 'Ouest', '« En dehors de la période hivernale » — durée écrite : « Mois »', 'Seule ligne <b>hivernale</b>'],
]

# Calendrier de travail et conséquence sur les fenêtres saisonnières.
CALENDRIER = [
 ['Ce qui fixe le calendrier', 'Source', 'Ce que cela donne'],
 ['Installation de chantier en novembre 2026 ; travaux de janvier 2027 à décembre 2028',
  'Donnée de travail GLCRM `[choix]`', 'Environ 24 mois de travaux effectifs après un mois d\'installation'],
 ['Échéancier du contrat : début le 31 août 2026, fin le 31 décembre 2027',
  'D8 annexe 0.01.13 — CI-CTR-001', 'Dates jugées inapplicables en l\'état : le début contractuel précède l\'émission des plans pour soumission (C-14)'],
 ['« Période estivale » : de la mi-juin à la mi-août, approximativement du 24 juin au 15 août',
  'Définition de travail GLCRM `[choix]` — à confirmer avec le CISSS (Z-10)',
  '<b>Deux fenêtres estivales</b> dans la période : 24 juin – 15 août 2027 et 24 juin – 15 août 2028, environ 7,5 semaines chacune'],
 ['« Période hivernale » : aucune définition écrite', 'Z-10',
  'Une seule ligne du tableau s\'y réfère (O-B-E-001, durée écrite « Mois ») : le tronçon F–F\' de la façade ouest est un travail de belle saison'],
]

CALENDRIER_TXT = (
 '<div class="note"><b>Ce que les deux fenêtres estivales commandent.</b> Deux lignes du tableau exigent l\'été et quatre l\'excluent ; une septième se contredit. '
 'Les deux qui l\'exigent — le clavier de la porte de garage du quai des ambulances (N-F-E-008) et la persienne du garage des ambulances (O-B-V-004) — doivent tomber dans l\'une des deux fenêtres. '
 'Or <b>N-F-E-008 est sur la façade nord, comme N-F-V-005 et N-F-P-002 qui, elles, excluent l\'été</b> : la façade nord ne peut pas être traitée d\'un seul tenant. '
 'Elle se scinde nécessairement en au moins deux passages, de part et d\'autre d\'une fenêtre estivale. '
 'Avec deux fenêtres disponibles au lieu d\'une, cette scission est tenable — elle ne l\'était pas dans la période écrite au contrat.</div>')

# Ce que chaque façade impose au calendrier, une fois la période estivale fixée.
CAL_FACADES = [
 ['Façade', 'Ce que le tableau écrit sur la saison', 'Conséquence sur le découpage'],
 ['Nord', 'N-F-E-008 exige l\'été ; N-F-V-005 et N-F-P-002 l\'excluent',
  '<b>Au moins deux passages</b>, de part et d\'autre d\'une fenêtre estivale'],
 ['Ouest', 'O-B-V-004 exige l\'été ; O-B-E-001 exclut l\'hiver, avec une durée écrite en mois',
  'Façade de <b>belle saison</b> ; le tronçon F–F\' doit être refermé avant le gel'],
 ['Est', 'E-G-V-003 et E-G-E-006 : semaine, hors été — deux locaux critiques',
  'Les deux coupures tombent au même endroit (entre F et E, niveau 200) : <b>une seule fenêtre peut servir aux deux</b>'],
 ['Sud', 'S-A-V-001 se contredit ; S-A-V-002 : nuit ou fin de semaine',
  'Aucune contrainte saisonnière exploitable tant que S-A-V-001 n\'est pas levée'],
]

SYNTHESE_TXT = (
 '<div class="txt"><b>Ce que la lecture en élévation ajoute au phasage.</b> Quarante-sept des quatre-vingt-treize lignes du tableau — la moitié — portent la mention '
 '« toute la durée des travaux » : l\'appareil est simplement hors service pendant les travaux de son secteur. La note 8 de la légende du tableau le précise : '
 '<span class="cit">« signifie que l\'équipement sera hors-fonction durant les travaux dans le secteur concerné et non durant la période complète du chantier »</span>. '
 'C\'est donc la <b>taille du secteur traité d\'un coup</b> qui détermine la durée d\'indisponibilité, et non le calendrier global. Découper une façade en tronçons plus courts '
 'réduit directement l\'indisponibilité de chaque porte, de chaque caméra et de chaque évacuation.<br><br>'
 '<b>La période estivale est contestée sur les quatre façades.</b> Sept lignes la nomment : deux l\'exigent, quatre l\'excluent, et une se contredit elle-même '
 '(« en dehors de la période estivale (quelques jours en été) », S-A-V-001) ; une huitième est bornée à l\'hiver. Aucun document ne définit ces périodes (Z-10) : '
 'le présent cahier travaille avec la définition GLCRM — mi-juin à mi-août — qui reste à confirmer avec le CISSS. C\'est la décision qui commande le plus de choses dans tout le projet.<br><br>'
 '<b>Ce que le tableau commande sur l\'ordre des façades.</b> Les seules dépendances écrites entre façades sont électromécaniques : la prise d\'air médical temporaire se pose '
 'sur la façade ouest pour permettre les travaux de la façade nord (ME-065) et se réinstalle après le revêtement nord (ME-067) ; les conduits temporaires de l\'hémodialyse '
 'précèdent la démolition des façades nord et ouest du niveau 200 (ME-049) ; les évents des autoclaves sont relocalisés avant le début de la façade ouest (ME-075) ; '
 'le conduit de la hotte de médecine nucléaire est modifié pour permettre la façade est (ME-118). Aucune de ces règles ne vient de l\'architecture : '
 '<b>c\'est l\'électromécanique qui ordonne les façades</b>, ce que la vue en plan ne montrait pas.</div>')

# --- séquence type de façade (03 §1.3), rappelée pour la lecture ----------
ETAPES = [
 ('E1', 'Préparation', "Classification PCI, cloisons et SAS, scellement des grilles, approbation de la préparation des lieux, toile sur l'échafaudage, **contournements électromécaniques avant démolition**, plan d'action pour les issues"),
 ('E2', "Démolition de l'enveloppe", "Retrait des revêtements, persiennes entreposées, équipements muraux démontés ; fenêtres existantes maintenues ; débris évacués en fin de journée"),
 ('E3', 'Relevé et structure', "Point d'arrêt après retrait des revêtements, relevé complet, validation des dimensions avant fabrication, renforts et réparations de béton (≥ 10 °C)"),
 ('E4', 'Enveloppe neuve', "Pare-air, compartimentation, isolant, revêtement, solins, couverture des bandes de toiture démolies ; essais in situ"),
 ('E5', 'Fenêtres', "Retrait après achèvement des travaux par l'extérieur `[lecture]` ; plexiglas ou bâti isolé de novembre à avril ; thermos et finition le même jour que le retrait du plexiglas"),
 ('E6', 'Remise en service', "Réinstallation des équipements, essais et préavis, séquence PCI de fin de travaux, désinfection terminale, correction des anomalies avant la phase suivante"),
]
