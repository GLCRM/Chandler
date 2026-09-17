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
]}

# --- commentaire de fin de planche, par façade ----------------------------
COMMENTAIRES = {
 'nord': '<div class="txt"><b>Un conflit saisonnier interne à la seule façade nord.</b> Trois lignes du tableau se contredisent sur la saison :<br>'
  '<span class="cit">N-F-V-005, unité de l\'hémodialyse : « Dimanche seulement, <b>en dehors de la période estivale</b> »</span><br>'
  '<span class="cit">N-F-P-002, déshumidification : arrêt possible « sauf en période estivale »</span><br>'
  '<span class="cit">N-F-E-008, clavier de la porte de garage : « <b>En période estivale</b> »</span><br><br>'
  'La même façade porte donc une intervention qui exige l\'été et deux qui l\'excluent. « Période estivale » n\'étant définie nulle part (Z-10), '
  'la façade nord ne peut pas être traitée d\'un seul tenant sans arbitrage du CISSS.<br><br>'
  '<b>Deux verrous inverses.</b> V15 et V16 ne sont pas des appareils qui bloquent l\'architecture, mais l\'architecture qui doit livrer : une alcôve dans le nouveau revêtement pour la sortie d\'arrosage encastrée, '
  'et de nouvelles trappes d\'accès identiques, sans lesquelles la mécanique du porte-à-faux devient inaccessible.<br><br>'
  '<b>Ce que WSP doit encore écrire.</b> Le tracé et la forme des conduits temporaires de l\'unité d\'hémodialyse, la séquence de basculement et les fenêtres d\'interruption au-delà de « une journée, un conduit à la fois » (Z-29) ; '
  'la position de la prise d\'air de la centrale d\'air médical, placée sur l\'élévation F sans qu\'aucun repère ne la montre.</div>',
}

# --- synthèse des quatre façades ------------------------------------------
# Comptages établis sur les 93 lignes du tableau ME (data/d5_equipements.json).
SYNTHESE_CHIFFRES = [
 ['Façade', 'Lignes', '« Toute la durée des travaux »', 'Fenêtre nommée', 'Non touché (gris)', 'À démanteler (orange)', 'À valider (jaune)'],
 ['Sud (A)',   '30', '17', '1 — hors période estivale', '6', '2', '0'],
 ['Ouest (B, C, E, I)', '25', '14', '4 — nuit (3), période estivale (1)', '2', '0', '0'],
 ['Nord (F)',  '23', '9',  '5 — dimanche hors été, semaine, soir, période estivale', '1', '0', '2'],
 ['Est (G, H, D)', '15', '7', '4 — semaine hors été (2), vendredi-dimanche, dimanche', '2', '0', '1'],
 ['<b>Total</b>', '<b>93</b>', '<b>47</b>', '<b>14</b>', '<b>11</b>', '<b>2</b>', '<b>3</b>'],
]

# Les six lignes du tableau qui nomment la période estivale, citées mot à mot.
SAISON = [
 ['Ligne', 'Façade', 'Période écrite', 'Sens'],
 ['S-A-V-001', 'Sud', '« En dehors de la période estivale (Quelques jours en été) »', '<b>Contradictoire en elle-même</b>'],
 ['O-B-V-004', 'Ouest', '« Travailler avec persienne en fonction. En période estivale »', 'Exige l\'été'],
 ['N-F-V-005', 'Nord', '« Dimanche seulement, en dehors de la période estivale »', 'Exclut l\'été'],
 ['N-F-E-008', 'Nord', '« En période estivale »', 'Exige l\'été'],
 ['E-G-V-003', 'Est', '« Semaine, en dehors de la période estivale »', 'Exclut l\'été'],
 ['E-G-E-006', 'Est', '« Semaine, en dehors de la période estivale »', 'Exclut l\'été'],
]

SYNTHESE_TXT = (
 '<div class="txt"><b>Ce que la lecture en élévation ajoute au phasage.</b> Quarante-sept des quatre-vingt-treize lignes du tableau — la moitié — portent la mention '
 '« toute la durée des travaux » : l\'appareil est simplement hors service pendant les travaux de son secteur. La note 8 de la légende du tableau le précise : '
 '<span class="cit">« signifie que l\'équipement sera hors-fonction durant les travaux dans le secteur concerné et non durant la période complète du chantier »</span>. '
 'C\'est donc la <b>taille du secteur traité d\'un coup</b> qui détermine la durée d\'indisponibilité, et non le calendrier global. Découper une façade en tronçons plus courts '
 'réduit directement l\'indisponibilité de chaque porte, de chaque caméra et de chaque évacuation.<br><br>'
 '<b>La période estivale est contestée sur les quatre façades.</b> Six lignes la nomment : trois l\'exigent, deux l\'excluent, et une se contredit elle-même '
 '(« en dehors de la période estivale (quelques jours en été) », S-A-V-001). Aucun document ne définit « période estivale » (Z-10). Tant que le CISSS ne l\'a pas définie, '
 'aucune façade ne peut être planifiée d\'un seul tenant : c\'est la décision qui commande le plus de choses dans tout le projet.<br><br>'
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
