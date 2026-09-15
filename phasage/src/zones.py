"""Contours des zones du plan clé (feuille 010), relevés graphiquement sur le rendu 200 ppp de la découpe
Rect(910,50,1290,390) de la page (image A010_plan_cle.png, 1057 x 946 px). Toute coordonnée est une [lecture]."""
OFF = (30, 85)          # découpe d'affichage : on retire la marge gauche et le titre
CROP = (30, 85, 1030, 625)   # x0, y0, x1, y1 dans l'image 200 ppp -> 1000 x 540 px affichés
ZONES = {  # lettre : (polygone en px image, nom court, fonction (légende 010 via 01 §8.5), phase du plan clé [lecture])
 'C': ([(410,110),(508,110),(508,305),(400,305)], 'Archives', 'Archives (RC, 2001)', 'non touché'),
 'J': ([(270,318),(367,318),(367,352),(270,352)], 'Basilaire nord-ouest', 'Basilaire nord-ouest (1974), 1 étage', '3'),
 'B': ([(367,318),(605,318),(605,352),(367,352)], 'Laboratoire', 'Laboratoire (niveau 100, 1990) — basilaire nord 2 étages', '3'),
 'K': ([(605,318),(645,318),(645,352),(605,352)], 'Basilaire nord-est', 'Basilaire nord-est (1974), 1 étage', '3'),
 'A': ([(270,352),(648,352),(648,375),(678,375),(678,415),(648,415),(648,508),(270,508)], 'Tour', 'Tour des chambres (niveaux 200, 300, 400 ; 1974), 4 étages', '2'),
 'O': ([(243,352),(270,352),(270,508),(243,508)], 'Basilaire ouest', 'Basilaire ouest (1 étage) — sans lettre de zone sur le plan clé', '3'),
 'I': ([(275,508),(305,508),(305,548),(275,548)], 'Basilaire sud-ouest', 'Basilaire sud-ouest (1974), 1 étage', '3'),
 'H': ([(305,508),(555,508),(555,548),(305,548)], 'Chirurgie d\'un jour / urgence', 'Chirurgie d\'un jour (niveau 100, 2005) et urgence (RC) — basilaire sud 2 étages', '3'),
 'G': ([(555,508),(678,508),(678,548),(555,548)], 'Basilaire sud-est', 'Basilaire sud-est (1974), 1 étage', '3'),
 'P': ([(510,548),(555,548),(555,598),(510,598)], 'Saillie sud', 'Saillie sud avec portes de garage (symboles ▲▼ du plan clé) — quai des ambulances [lecture]', '3'),
 'D': ([(650,415),(735,415),(735,370),(930,370),(930,508),(650,508)], 'Administration / cliniques externes', 'Administration (niveau 100, 2005) et cliniques externes (RC, 1974) — basilaire est 2 étages', '1'),
 'F': ([(690,508),(760,508),(760,605),(690,605)], 'IRM', 'IRM (RC, 2007)', '1'),
 'E': ([(760,508),(930,508),(930,605),(760,605)], 'Oncologie 1974', 'Oncologie (RC, 1974)', '1'),
 'L': ([(930,455),(975,455),(975,605),(930,605)], 'Oncologie 2023', 'Oncologie (RC, 2023)', 'non touché'),
}
# faces de la tour (bandes) pour les sous-phases 2.N, 2.E, 2.S, 2.O
FACES_TOUR = {
 '2.N': [(270,352),(648,352),(648,368),(270,368)],
 '2.E': [(632,368),(648,368),(648,375),(678,375),(678,415),(648,415),(648,492),(632,492)],
 '2.S': [(270,492),(648,492),(648,508),(270,508)],
 '2.O': [(270,368),(286,368),(286,492),(270,492)],
}
# repères d'élévations (feuille 011, plan clé) : lettre -> (point d'ancrage sur la face, direction de vue) [lecture]
ELEV = {
 'A': ((460,590), 'N', 'Élévation sud'),
 'B': ((180,430), 'E', 'Élévation ouest'),
 'C': ((700,640), 'W', 'Élévation ouest partielle'),
 'D': ((600,640), 'E', 'Élévation est partielle'),
 'E': ((215,560), 'E', 'Élévation ouest partielle'),
 'F': ((360,290), 'S', 'Élévation nord'),
 'G': ((985,440), 'W', 'Élévation est'),
 'H': ((530,290), 'S', 'Élévation nord partielle'),
 'I': ((685,295), 'S', 'Élévation ouest partielle'),
}
def shift(poly): return [(x-OFF[0], y-OFF[1]) for x,y in poly]
