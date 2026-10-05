"""Textes des planches du plan de phasage complet (option R). Prose courante ;
chaque exigence citée renvoie au registre (AR-DEV, AR-PLN, ME, ST, CI-…) ou à
une ligne du tableau de coordination de WSP (N-F-…, S-A-…, E-G-…, O-B-…)."""

ENSEMBLE = (
 "<b>Ce que propose ce plan.</b> L'ordre est celui du plan clé des architectes — basilaire est, tour, basilaires nord, ouest et sud —, "
 "retenu comme option de référence dans le cahier en plan. Ce plan y ajoute ce qui manquait : un calendrier dans la période de travail GLCRM, "
 "les zones de chantier et les clôtures phase par phase, et, pour chaque phase, les murs travaillés avec les appareils qu'il faut couper, déplacer ou maintenir.<br><br>"
 "<b>D'où viennent les dates.</b> Aucun document ne fixe de durée. Les durées sont celles qu'indique le plan clé (±5, ±8 et ±4 mois) ; "
 "la fenêtre est celle de GLCRM — installation en novembre 2026, travaux de janvier 2027 à décembre 2028 — et la période estivale va du 24 juin au 15 août. "
 "Tout ce qui est daté sur ce cahier est donc un `[choix]`, à confirmer avec le CISSS.<br><br>"
 "<b>Ce qui place les phases.</b> Huit lignes du tableau de WSP sont bornées par une saison. L'enchaînement proposé les fait toutes tomber du bon côté de l'été, "
 "sauf une dont le sens est à trancher (O-B-V-004). Il impose en contrepartie environ sept mois de travaux d'enveloppe sous enceintes chauffées : "
 "c'est inévitable, puisque 17 mois de travaux doivent tenir dans une fenêtre qui ne compte que 12 mois hors de novembre à avril.")

ELEVATIONS = (
 "<b>Comment lire.</b> Les élévations de la feuille 011 ne portent pas de couleurs de phase ; seul le plan clé en porte. Les bandes ci-dessus reportent "
 "chaque zone du plan clé sur les quatre élévations, axe par axe : c'est une `[lecture]`, à faire confirmer par les architectes. "
 "La tour est verte au-dessus des toits des basilaires ; chaque basilaire prend la couleur de sa phase jusqu'à son parapet.<br><br>"
 "<b>Ce que le report fait voir.</b> Chaque façade est partagée entre deux ou trois phases. La façade nord, par exemple, est travaillée en phase 1 à l'est (basilaire est), "
 "en phase 2 en hauteur (tour) et en phase 3 au pied de la tour (laboratoire et garage des ambulances). C'est pourquoi le conflit saisonnier de la façade nord "
 "se règle de lui-même dans l'option R : ses trois lignes saisonnières tombent dans trois phases différentes.<br><br>"
 "<b>Les élévations partielles.</b> Le tableau de WSP code l'orientation du mur, pas sa place dans le bâtiment. Les appareils de l'élévation partielle C "
 "(roulotte d'IRM mobile) sont sur le mur ouest du volume de l'IRM, et ceux de l'élévation I (porte de l'escalier no 6) sur le mur ouest de la cour nord-est : "
 "ils appartiennent tous les deux au basilaire est, donc à la phase 1, même s'ils sont codés « ouest ».")

F0 = {
 'quoi': "<b>Avant le premier travail sur l'enveloppe</b>, tout ce que les documents exigent « avant le début » : autorisation de débuter après assurances et garanties (CI-CTR-005), "
  "première réunion (CI-CTR-015), réunion d'ordonnancement au plus tard dix jours ouvrables après l'attribution (AR-DEV-050), calendriers, "
  "plans émis pour construction — ceux du dossier sont pour soumission (ST-005, ME-160) —, plan de sécurité incendie approuvé par le CISSS, l'établissement et le service incendie (AR-DEV-197), "
  "méthodologie PCI et plan des cloisons pour chaque phase (AR-DEV-148, AR-DEV-203), instrumentation du bruit et des vibrations en place (AR-DEV-130, AR-DEV-131), "
  "piquages sur les réseaux existants (AR-DEV-030), agent de mise en service (AR-DEV-256).",
 'avant': "<b>Ce qui doit être lancé dès novembre</b> pour que la phase 1 démarre en janvier : les dessins d'atelier des fenêtres et du revêtement, "
  "puisque rien ne se fabrique avant leur retour, et le prototype de la première fenêtre, qui se fait en présence de l'architecte au début de la phase 1 (AR-PLN-050). "
  "Côté WSP, le tracé des conduits temporaires de l'hémodialyse doit être écrit avant mai 2027, date à laquelle ils doivent être posés (Z-29).",
 'chantier': "<b>Site.</b> La feuille 001 ne montre qu'une configuration de clôture (note 23). La zone clôturée de l'ouest, réservée à l'entrepreneur, sert de base pour toute la durée : "
  "roulottes, entreposage et conteneur y sont placés `[choix]`, avec l'accès de chantier sud-ouest. Le devis situe le bureau de chantier dans un stationnement étagé que la feuille 001 ne montre pas (AR-DEV-180). "
  "Les barrières sont verrouillables « selon les phasages » (AR-DEV-190), l'accès du chantier reste séparé de celui de l'hôpital (AR-DEV-029), et tout déplacement de voie se prévient trois semaines d'avance (AR-DEV-139).",
 'valider': "<b>À obtenir avant janvier 2027.</b> Confirmation des dates et de la période estivale ; régime PCI applicable à Chandler (C-01) ; plage horaire de travail (Z-01) ; "
  "approbation du calendrier d'exécution et du calendrier d'arrêt des installations (AR-DEV-026, AR-DEV-032) ; ascenseur no 1 et escalier désigné (CI-TAB-002).",
}

F1 = {
 'quoi': "<b>Le basilaire est</b> — administration et cliniques externes (D), oncologie de 1974 (E), IRM (F) — sur ses faces nord, est et sud ; l'oncologie de 2023 (L) n'est pas touchée. "
  "Fenêtres en trois étapes au rez-de-chaussée en blocs, en deux pour l'IRM et le niveau 100 (AR-PLN-047, AR-PLN-048) ; prototype en début de phase (AR-PLN-050) ; "
  "volets coupe-feu des locaux R16, R34 et R36 (ME-109, ME-110) ; renforts de colonnes dans l'entreplafond du local R-22, après relocalisation des conduits électriques (ME-108, ME-111).",
 'avant': "<b>Avant de démolir.</b> La roulotte d'IRM mobile reste servie quand elle est en place : ses raccordements sont enlevés puis remis au même endroit et les persiennes de son échangeur réinstallées après le revêtement (O-C-E-001, O-C-V-001). "
  "Le bandeau lumineux de la façade est est déposé avec son conduit (E-G-E-002 à 004) : la longueur du tronçon attaqué d'un coup fixe l'étendue laissée sans éclairage la nuit. "
  "La caméra du coin de l'escalier no 3 est relocalisée en gardant son champ (N-F-E-004). La sortie d'arrosage du coin nord-est est un verrou inverse : l'architecture doit lui livrer une alcôve (N-F-P-001).",
 'coupures': "<b>Coupures.</b> La déshumidification du coin nord-est peut s'arrêter sauf l'été (N-F-P-002) : la phase tombe de janvier à mai. "
  "L'évacuation de l'atelier de menuiserie est arrêtée pendant les travaux du secteur (N-F-V-002). Les lampadaires du stationnement sont remis en fonction tous les soirs (N-F-E-001). "
  "Les portes de l'escalier no 4 et de l'escalier no 6 perdent leur lecteur pendant le secteur (S-A-E-019, O-I-E-002) : plan d'action pour les issues avant de commencer (AR-PLN-011).",
 'chantier': "<b>Chantier et PCI.</b> Enceintes chauffées de janvier à avril (10 °C dans les zones de travaux, AR-DEV-144 ; béton à 10 °C ou plus, ST-034). "
  "Entrée des cliniques externes maintenue avec un passage protégé (CI-TAB-015). Aucun entreposage métallique dans la zone de l'IRM quand l'appareil est en service (AR-PLN-009). "
  "Classes écrites au tableau du CISSS : plexiglas classe I, thermos et cadrage II ou III, volets IV, local R-22 IV « J/S » (CI-TAB-006 à 010) — sous réserve du régime PCI (C-02).",
}

F2A = {
 'quoi': "<b>Mai à juin 2027 : les contournements de la tour.</b> Trois installations temporaires doivent être en place avant le premier travail sur la tour : "
  "les conduits temporaires de l'unité d'hémodialyse, posés le dimanche et avant le 24 juin (ME-049 à 051) ; les deux conduits de 900 × 900 mm qui gardent le bloc opératoire alimenté (ME-042, ME-043, ME-047) ; "
  "et la relocalisation des évents des autoclaves, de nuit ou avant 10 h, « avant le début des travaux de la façade ouest » (ME-075, ME-077). Dans l'option R, ce début est la face ouest de la tour, en juillet 2027 : "
  "les évents restent donc sur leurs supports temporaires en toiture pendant quinze mois, jusqu'à leur réinstallation à la fin de la phase 3 (ME-076).",
 'avant': "<b>Face sud, juin à août.</b> La chambre à pression négative 307 n'est démantelée qu'inoccupée, avec un conduit prolongé hors des échafaudages (S-A-V-003, ME-056). "
  "L'entrée principale est sous cette face : un passage abrité est à prévoir sous l'échafaudage (AR-DEV-191) `[choix]`.<br>"
  "<b>Face ouest, juillet à septembre.</b> Le revêtement se refait derrière le conduit existant du bloc opératoire une fois les temporaires en service (O-B-V-001). "
  "Le thermostat des câbles chauffants tombe hors de l'hiver, comme l'exige sa ligne (O-B-E-001). Les portes du laboratoire et du bloc opératoire perdent luminaire et lecteur pendant le secteur (O-B-E-002 à 005).",
 'coupures': "<b>Coupures.</b> Hémodialyse : une journée, un conduit à la fois, le dimanche, hors été — d'où la pose des temporaires en mai-juin. "
  "Bloc opératoire : nuit ou fin de semaine, sous réserve des gardes (ME-048). Persienne de l'unité UT-2 : nuit ou fin de semaine. Autoclaves : nuit ou le matin avant 10 h.",
 'chantier': "<b>Chantier.</b> Les échafaudages de la tour s'appuient sur les toitures des basilaires `[lecture]` : attestation scellée, capacités des toitures respectées, aucune charge ponctuelle sur les toitures ventilées (ST-023 à 026). "
  "La voie des ambulances passe sous l'échafaudage de la face ouest : protection en surplomb `[choix]`. L'aire de levage n'est implantée sur aucun plan (Z-27) ; plan de levage cinq jours d'avance.",
}

F2B = {
 'quoi': "<b>Face nord, 16 août à novembre 2027.</b> Les conduits de l'hémodialyse sont rebranchés le dimanche, après le 15 août, puis la passerelle d'aluminium est réinstallée, modifiée (N-F-V-005 ; ME-050, ME-054). "
  "Le conduit de la chambre 216 est prolongé hors des échafaudages (N-F-V-008) ; la prise d'air des soins intensifs, chambre 315, ne se touche que la nuit ou le jour quand aucune chambre n'est occupée (N-F-V-009, ME-058).",
 'avant': "<b>Face est, mi-octobre 2027 à janvier 2028.</b> Le conduit de la hotte de médecine nucléaire est modifié sur toute la hauteur, avec un arrêt du vendredi au dimanche (E-H-V-001 ; ME-118, ME-119). "
  "Les bi-blocs du traitement d'eau de l'hémodialyse et de la salle des serveurs se coupent en semaine, hors été, au même endroit : une seule fenêtre peut servir aux deux (E-G-V-003, E-G-E-006). "
  "La porte de l'escalier no 3, une issue, perd luminaire et lecteur pendant le secteur (E-H-E-001, E-H-E-002).",
 'coupures': "<b>Hiver 2028, février à avril : les fenêtres de la tour par l'intérieur.</b> Une fois les quatre faces refaites, les fenêtres se remplacent par l'intérieur derrière un bâti isolé, "
  "comme l'exigent les plans de novembre à avril (AR-PLN-042) ; thermos et finition le même jour que le retrait du plexiglas (AR-PLN-044). "
  "Le tableau du CISSS classe ces étapes III, horaire « J », aux niveaux 2, 3 et 4 (CI-TAB-024, 027, 029). Les fenêtres de la cage d'escalier no 3 sont obturées (feuille 504 ; Z-26).",
 'chantier': "<b>Chantier.</b> Enceintes chauffées sur l'échafaudage de la face est de novembre à janvier. Les persiennes P-11 et P-12 sont « à relocaliser » au tableau et « à démanteler complètement » sur le dessin : à faire trancher par WSP avant la face est.",
}

F3A = {
 'quoi': "<b>Basilaires sud, mai au 23 juin 2028.</b> La seule ligne de protection incendie du tableau tombe ici : gicleurs du toit de l'entrée des ambulances mis hors service par zone, deux coupures de 2 h, glycol récupéré (S-A-PI-001 ; ME-006 à 008). "
  "Le bi-bloc du prélèvement d'urgence se démantèle hors été (S-A-V-001), la persienne de l'unité UT-2 lors d'une coupure rapide (S-A-V-002). L'entrée principale passe par trois configurations (AR-PLN-019).",
 'avant': "<b>Basilaire nord, mi-mai au 15 août 2028.</b> Laboratoire : sortie d'air et évacuation V-53 maintenues par conduits temporaires (N-F-V-007, N-F-V-003), trappes d'accès refaites à l'identique, verrou inverse (N-F-V-011). "
  "Nouvelle issue extérieure du laboratoire, classe IV « J », et escalier no 7 `[à confirmer]` : l'été pour l'excavation. "
  "Air médical : prise d'air temporaire posée sur la façade ouest au niveau du basilaire, encore à refaire, avec boîtier HEPA, bonbonnes et première certification (N-F-GM-001 ; ME-064 à 069).",
 'coupures': "<b>Les ambulances.</b> La feuille 001 place le garage des ambulances dans le basilaire ouest, entrée par la porte sud et sortie par la porte nord : "
  "les documents qui écrivaient « sud » et « nord » parlaient des deux portes du même garage. Pendant les travaux au sud, les ambulances entrent et sortent par le nord ; "
  "à partir du 24 juin, par le sud (feuille 002, détail 1). Le clavier de la porte nord est écrit « en période estivale » : il tombe du 24 juin au 15 août (N-F-E-008).",
 'chantier': "<b>Chantier.</b> Préavis de trois semaines avant chaque changement de configuration d'accès (AR-DEV-139) ; un panneau d'ambulance par configuration (AR-PLN-014), "
  "alors que l'enseigne AMBULANCE est hors service pendant le secteur (S-A-E-006). Plan de sécurité incendie couvrant la mise hors service des gicleurs (Z-08).",
}

F3B = {
 'quoi': "<b>Basilaire ouest, 16 août à septembre 2028.</b> Après le revêtement nord, la prise d'air médical est réinstallée et les temporaires retirés (ME-067), puis la façade ouest du basilaire est refaite. "
  "Les évents des autoclaves reviennent à leur place d'origine (ME-076). Le bi-bloc de la salle d'observation est sur ce côté-ci, posé sur le garde-corps G-02 de la feuille 703, "
  "et non au sud comme l'écrivait le plan de phasage : il se réinstalle sur le garde-corps modifié, qui doit donc être posé avant lui (O-B-V-005 ; AR-PLN-070).",
 'avant': "<b>Ce qui se maintient.</b> La caméra de l'issue de l'urgence ne tolère « aucun arrêt » : relocalisée et vérifiée avant la dépose (O-E-E-003). "
  "L'entrée des marchandises au sous-sol reste ouverte (CI-TAB-013). La persienne de prise d'air du service alimentaire, sans ligne au tableau, reçoit un registre coupe-feu `[à confirmer]`.",
 'coupures': "<b>À trancher.</b> La persienne du garage des ambulances est écrite « travailler avec persienne en fonction. En période estivale » (O-B-V-004). "
  "Si cela veut dire « garder la persienne en fonction l'été », septembre convient ; si cela veut dire « faire ce travail l'été », il faut commencer la phase 3.O par ce tronçon avant le 15 août, "
  "hors de l'emplacement de la prise d'air médical temporaire.",
 'chantier': "<b>Phase 4, octobre à mi-décembre 2028.</b> Essais intégrés de l'alarme incendie (AR-DEV-006, ME-098), équilibrage (ME-134 à 138), filtres remplacés avant la réception provisoire (ME-139), "
  "mise en service avec préavis de 21 et 14 jours (AR-DEV-274, AR-DEV-276), deuxième certification de l'air médical (ME-069), nettoyage final et contrôle de la qualité de l'air avant de rouvrir un service (AR-DEV-243 à 245 ; CI-PCI-023, 024), "
  "remise en état du site (AR-DEV-298), avis de fermeture (CI-CTR-022) et réception (CI-CTR-026).",
}

CALENDRIER = (
 "<b>La contrainte qui commande tout.</b> Les durées du plan clé totalisent 17 mois de travaux d'enveloppe. La fenêtre de janvier 2027 à décembre 2028 compte 24 mois, "
 "dont 12 seulement hors de la période de novembre à avril — la seule saison froide que les plans nomment (AR-PLN-042). Au moins cinq mois d'enveloppe tombent donc l'hiver, quel que soit l'ordre ; "
 "l'enchaînement proposé en place environ sept, de janvier à avril 2027 sur le basilaire est et de novembre 2027 à janvier 2028 sur la face est de la tour, "
 "parce que le basilaire nord doit attendre l'été 2028. Les enceintes chauffées ne sont pas une variante : elles sont au prix.<br><br>"
 "<b>Pourquoi l'hiver tombe sur le basilaire est et non sur la tour.</b> Un basilaire de deux étages se ferme et se chauffe plus facilement qu'un échafaudage de tour. "
 "Mettre la tour dans l'hiver 2027-2028 en entier aurait placé six mois de travaux en hauteur sous enceinte.<br><br>"
 "<b>Le chemin critique est électromécanique.</b> Si les conduits temporaires de l'hémodialyse ne sont pas posés avant le 24 juin 2027, la tour attend l'automne : "
 "leurs coupures ne se font que le dimanche, hors été. WSP doit donc avoir écrit leur tracé au printemps 2027 au plus tard (Z-29).")

BOUGER = [
 ['Ce qui peut changer', 'Ce que ça déplace'],
 ['Le CISSS ne confirme pas le calendrier de janvier 2027 à décembre 2028', 'Tout le calendrier ; l\'ordre et les verrous restent valides'],
 ['La période estivale n\'est pas du 24 juin au 15 août', 'Les bornes de 2.N, 2.E, 3.S et 3.N ; le rebranchement de l\'hémodialyse'],
 ['WSP n\'a pas écrit les conduits temporaires de l\'hémodialyse en avril 2027', 'Le début de la tour, repoussé à la fin d\'août 2027 ; la face est glisse dans l\'hiver'],
 ['O-B-V-004 veut dire « faire l\'été »', 'Le début de 3.O, avancé avant le 15 août sur le tronçon du garage'],
 ['La centrale d\'air médical est sur la tour, pas sur le basilaire', 'La prise d\'air temporaire percerait la face ouest de la tour refaite en 2027 : à replacer avec WSP'],
 ['L\'escalier no 7 doit remplacer une issue condamnée', 'La nouvelle issue passe en phase 0 ou 1 (variante V-K4a du plan de phasage)'],
 ['Les enceintes chauffées sont refusées', 'L\'enveloppe s\'arrête de novembre à avril : les 17 mois de travaux ne tiennent plus dans la fenêtre, il en manque au moins cinq'],
]

DECISIONS = [
 ['Décision', 'De qui', 'Avant', 'Ce qu\'elle débloque'],
 ['Confirmer le calendrier (installation en novembre 2026, travaux de janvier 2027 à décembre 2028) et la période estivale du 24 juin au 15 août', 'CISSS', 'novembre 2026', 'Toutes les dates du plan'],
 ['Régime PCI applicable à Chandler et classes du tableau (C-01, C-02)', 'CISSS', 'novembre 2026', 'Les cloisons, sas et pressions de chaque phase'],
 ['Plage horaire de travail et sens des codes « J », « S », « J/S » (Z-01)', 'CISSS', 'novembre 2026', 'Les horaires de toutes les étapes classées'],
 ['Plans émis pour construction (ST-005, ME-160)', 'Architectes et WSP', 'décembre 2026', 'Le début de la phase 1'],
 ['Tracé et forme des conduits temporaires de l\'hémodialyse, séquence de basculement, fenêtres (Z-29) ; rattachement de l\'unité côté ouest', 'WSP', 'avril 2027', 'La pose des temporaires en mai-juin 2027, donc le début de la tour'],
 ['Report des phases sur les élévations et rattachement des élévations partielles C, I, H, E', 'Architectes', 'décembre 2026', 'Les bandes de phase de la planche 2 et la phase de chaque appareil'],
 ['Portée de « travaux par l\'extérieur » sur la feuille 505 (AR-PLN-040)', 'Architectes', 'décembre 2026', 'Le moment du retrait des fenêtres dans chaque phase'],
 ['Divergences du tableau et des dessins : E-G-V-001, 002 ; E-G-V-003 ; E-G-E-006 ; O-B-V-002', 'WSP', 'mai 2027', 'Les faces est et ouest de la tour'],
 ['Emplacement de la centrale d\'air médical (tour ou basilaire) et de sa prise d\'air temporaire', 'WSP', 'janvier 2028', 'La phase 3.N sans percer un revêtement neuf'],
 ['Escalier no 7 = nouvelle issue, et ordre avec la condamnation d\'une issue existante (Z-12)', 'Architectes et structure', 'janvier 2027', 'Le moment de la nouvelle issue (phase 0, 1 ou 3.N)'],
 ['Sens de O-B-V-004 et de S-A-V-001', 'CISSS et WSP', 'mars 2028', 'Le début de 3.O ; la phase 3.S'],
 ['Correspondance des trois numérotations « phase 1, 2, 3 » (C-34)', 'Architectes et CISSS', 'novembre 2026', 'La lecture contractuelle des zones de chantier par phase'],
 ['Aire de levage, grue et entreposage par phase (Z-27, AR-DEV-171)', 'Entrepreneur', 'phase 0', 'Le plan de chantier définitif, que ce cahier esquisse'],
]
