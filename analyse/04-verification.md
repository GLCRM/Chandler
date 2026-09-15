# 04 — Vérification adverse du plan de phasage

**Projet** : Hôpital de Chandler — Réfection de l'enveloppe (dossier GLCRM R-657-24 ; appel d'offres AOC-077221 ; CISSS de la Gaspésie).
**Objets vérifiés** : `analyse/02-contraintes.md` (registre de 719 contraintes ; contradictions C-01 à C-40 ; zones d'ombre Z-01 à Z-28 ; renvois R-01 à R-40) et `analyse/03-phasage.md` dans sa version soumise à vérification (commit 00cd9ed), puis corrigée (commits 4d8b5ae à d9badb9).
**Question posée** : phase par phase, contrainte par contrainte, rien n'est-il violé ? Dans quelle phase chaque contrainte du registre est-elle traitée ? Quelles contraintes ne sont pas couvertes, quelles violations existent, quelles hypothèses non sourcées se sont glissées dans le phasage ?

---

## 0. Méthode

### 0.1 Trois passes indépendantes et deux contrôles automatiques

| Passe | Angle | Ce qui a été lu | Résultat brut |
|---|---|---|---|
| V1 — violations | Pour chaque fiche de phase, variante et cellule de matrice de 03 : une contrainte du registre (interdiction, fenêtre horaire, préavis, préalable) s'y oppose-t-elle ? Un préalable écrit manque-t-il ? Chaque identifiant cité dit-il ce qu'on lui fait dire ? | 03 en entier ; 02 §0, §2, §3, §4 en entier ; les 719 lignes du tableau §1 (les 158 AR-DEV cités dans les fiches en texte intégral) | 39 constats : 1 violation confirmée, 19 paraphrases inexactes, 4 préalables manquants, 6 risques non sourcés, 9 points sensibles conformes |
| V2 — hypothèses non sourcées | Pour chaque affirmation factuelle de 03 (localisation, appartenance d'une zone à une phase, ordre, classe PCI, horaire, contenu d'un document) : un identifiant est-il cité, dit-il exactement cela, et le marqueur `[lecture]` / `[choix]` / `[à confirmer]` est-il présent quand il le faut ? | 03 en entier ; 02 §0, §2, §3, §4 ; §1 identifiant par identifiant ; 01-inventaire §1, §6, §7, §8 | 61 constats : 1 non sourcée, 14 « l'identifiant ne dit pas cela », 9 marqueurs manquants, 8 extrapolations, 29 points sensibles conformes |
| V3 — exactitude des affectations | Pour chacun des 719 identifiants : la phase attribuée (découpages A et B) est-elle justifiée par les zones, la contrainte et la citation de sa propre ligne ? Les listes des fiches et de l'annexe A concordent-elles avec l'affectation ? | Les 345 affectations spécifiques et les 374 affectations par défaut, une à une ; listes de 03 comparées par script | 59 constats : 12 erreurs, 43 douteuses, 4 à marquer « non déterminable » ; 7 écarts entre les listes de 03 et l'affectation |
| Contrôle A — couverture | Chaque identifiant du registre est-il cité dans 03, et où ? Chaque identifiant cité existe-t-il ? | Script d'expansion des plages et abréviations de listes (§0.3 de 03) | 719 / 719 cités ; 0 non couvert ; 0 identifiant inexistant |
| Contrôle B — cohérence des listes | Les ensembles d'identifiants des fiches et de l'annexe A sont-ils égaux à l'affectation ? | Script | Annexe A exacte ; 4 écarts dans les fiches (corrigés) |

Chaque passe a été menée par un vérificateur qui n'avait pas rédigé 03, avec pour seule source admise le texte de 02 (et 01 pour la légende des zones). Les trois rapports bruts sont conservés hors du dépôt ; leurs constats sont repris ci-dessous après contre-vérification, un par un, contre la ligne du registre citée. Quatre constats ont été écartés ou requalifiés (§7).

### 0.2 Verdicts utilisés

| Verdict | Sens | Suite donnée |
|---|---|---|
| **Confirmé — corrigé** | Le texte du registre contredit ce que 03 affirme, ou 03 affirme sans texte | Correction dans 03, un commit par problème (§9) |
| **Confirmé — consigné** | Risque réel mais aucun texte ne permet de trancher | Ajouté à 03 comme risque non sourcé, `[à confirmer]` ou ligne du §6 |
| **Non retenu** | Le constat repose sur une lecture que le registre ne soutient pas, ou 03 le disait déjà | Motif au §7 |
| **Conforme** | Point sensible vérifié sans défaut | Listé au §3.3 |

### 0.3 Ce que cette vérification ne fait pas

Elle ne vérifie pas le registre 02 contre les documents sources (c'était l'objet de la traçabilité de la session 1), sauf incidemment : trois défauts de 02 ont été découverts et corrigés (§6). Elle ne propose aucune durée. Elle ne tranche aucun des conflits K1 à K7 de 03, qui relèvent des émetteurs des documents.

---

## 1. Résultat d'ensemble

| Question | Réponse |
|---|---|
| Contraintes non couvertes | **Aucune.** Les 719 identifiants sont cités dans 03 : 339 dans au moins une fiche de phase ou de sous-phase, 380 dans le tableau des contraintes transversales (§1.2 de 03) ; tous figurent en annexe A de 03 et dans l'annexe A du présent document avec leur phase. |
| Violations d'une contrainte par une phase | **Une seule, confirmée et corrigée** : le diagramme du découpage B (03 §3.5) dessinait la toile d'échafaudage (CI-TAB-004, « jusqu'au moment de la pose des membranes pare-intempéries ») **après** l'achèvement des façades, alors qu'elle les précède (commit 9a688dd). Aucune fiche de phase ne prescrit une coupure, un ordre ou une mesure qu'une interdiction, une fenêtre horaire, un préavis ou un préalable du registre interdit. |
| Séquences présentées comme écrites alors qu'elles sont déduites | **Trois, corrigées** : l'ordre « nord avant ouest » (ME-065/067 ne fixent que l'emplacement et le moment d'une prise d'air temporaire ; Z-02 n'exclut pas la simultanéité) ; l'achèvement des façades extérieures avant le retrait des fenêtres (portée de « travaux par l'extérieur », AR-PLN-040, non tranchée par C-36 et Z-07) ; l'antériorité de la modification du conduit de médecine nucléaire (ME-118 : « afin de permettre »). Elles restent dans 03 comme lectures marquées `[lecture]`, avec la lecture alternative. |
| Préalables écrits omis dans une fiche | **Quatre, corrigés** : prolongation temporaire du conduit de la chambre 307 (ME-056) ; fenêtre « nuit/jour si aucune chambre occupée » de la chambre 315 (ME-058) ; première certification de l'air médical à la relocalisation (ME-069) ; préavis de trois semaines avant déplacement d'une voie (AR-DEV-139). |
| Hypothèses non sourcées glissées dans 03 | **32 confirmées** (V2) plus 6 risques (V1), toutes traitées : identifiants qui ne disaient pas ce qu'on leur faisait dire (14), marqueurs `[lecture]` / `[à confirmer]` manquants (9), extrapolations (8), une affirmation sans source (légende des zones A à L, désormais renvoyée à 01-inventaire §8.5). Détail au §4. |
| Affectations ID → phase erronées | **12 erreurs et 4 localisations à marquer**, corrigées à la source (règles d'affectation), plus 27 affectations douteuses reprises et 8 laissées telles quelles avec motif (§5). Après correction : 357 affectations spécifiques, 362 par défaut ; 6 identifiants « non déterminables » (NA) dans le découpage A. |
| Défauts découverts dans 02 | Trois renvois orphelins (« voir citation intégrale en B.3/B.4/B.5 ») et quatre lignes aux colonnes décalées (AR-PLN-018 à 021) : corrigés (§6). Une divergence de localisation entre documents (zone d'ambulance) relevée, non tranchée. |

---

## 2. Couverture du registre : dans quelle phase chaque contrainte est traitée

### 2.1 Répartition

Un identifiant peut être traité dans plusieurs phases (préalable en phase 0 puis obligation continue, par exemple). Découpage A (secteurs du plan clé) après correction :

| Phase (A) | Identifiants | Contenu principal |
|---|---|---|
| 0 — préalables et mobilisation | 112 | Livrables, approbations et installations « avant le début », dont 39 se prolongent en T |
| 1 — basilaire est (D, E, F) | 36 | IRM, volets coupe-feu RC, local R-22, équipements de façade est, étapes CISSS du RC et du niveau 1 |
| 2 — tour, toutes faces | 14 | Fenêtres 2 étapes, niveaux 2 à 4, psychiatrie, soins intensifs, service alimentaire (zone A) |
| 2.N / 2.E / 2.S / 2.O | 14 / 6 / 3 / 30 | Hémodialyse et chambre 216 ; médecine nucléaire ; chambre 307 ; bloc opératoire, autoclaves, soffite |
| 3 — basilaires, toutes façades | 6 | Fenêtres RC et niveau 100, garde-corps, poteaux HSS |
| 3.N / 3.O / 3.S | 41 / 35 / 29 | Nouvelle issue, laboratoire, air médical ; autoclaves, câbles chauffants ; ambulances, entrée principale, chirurgie d'un jour, urgence |
| 4 — clôture | 58 | Essais intégrés, équilibrage, mise en service, certifications, nettoyage final, réception |
| T — transversal | 498 | Exigences continues (§1.2 de 03), dont 39 partagées avec la phase 0 et 36 avec la phase 4 |
| NA — non déterminable | 6 | AR-PLN-056, AR-PLN-079, ME-062, ME-141, ME-143, CI-TAB-013 (§6 de 03) |

Découpage B (niveaux du tableau CISSS) : 0 = 112 ; B-A (RC) = 36 sans sous-phase précisée + A.1 18, A.2 1, A.3 1, A.4 1, A.5 1, A.6 10, A.7 1 ; B-B (niveau 1 et sous-sol) = 57 + B.1.2 21, B.1.3 1, B.2.1 1, B.2.2 1 ; B-C (tour) = 26 + C.2 10, C.4 5, C.5 1 ; 4 = 58 ; T = 497. Aucun identifiant n'est NA dans le découpage B (le niveau est toujours déductible du texte ou du tableau CISSS).

### 2.2 Ce que « traité » veut dire

Une contrainte est traitée dans une phase si la fiche de cette phase (ou la sous-phase) la cite, l'intègre à ses préalables, mesures transitoires ou points de validation, ou si elle figure dans le tableau des transversales de 03 avec une modalité d'application. Pour 380 identifiants la modalité est transversale : ils s'appliquent à l'identique dans chaque phase et ne sont pas répétés fiche par fiche. La table de l'annexe A donne, pour chacun des 719 identifiants, les phases des deux découpages, les sections de 03 qui le citent et la base de l'affectation (règle spécifique motivée ou règle par défaut).

### 2.3 Identifiants dont la phase repose sur une localisation non écrite

Ils sont couverts sous réserve et listés au §6 de 03 : sous-sol non zoné au plan clé (AR-PLN-056 ; ME-025, 029 ; CI-TAB-005 ; ME-062, 141 ; AR-PLN-079 ; CI-TAB-013) ; façade ouest « tour » ou basilaire (ME-042 à 048, 084 ; ME-075 à 083) ; centrale d'air médical « toiture nord-ouest » (ME-064 à 068) ; soffite du porte-à-faux (ME-080, 096, 120 à 123) ; chambre 315, local 203, IRM mobile dont la face n'est écrite que dans un identifiant de ligne de D5 (ME-058, 087, 116) ; zone d'ambulance écrite « sud » (ME-006 à 008, ME-147) et « nord » (AR-PLN-004) ; escalier no 7 présumé être la nouvelle issue (Z-12) ; mur de fondation (ST-037) ; zones B et H rattachées aux façades nord et sud par lecture du plan clé.

---

## 3. Violations, phase par phase

### 3.1 Méthode de la passe

Pour chaque fiche (phase 0, 1, 2.N, 2.E, 2.S, 2.O, 3.N, 3.O, 3.S, 4 ; B-A, B-B, B-C), chaque variante (V-A1 à V-A4, V-K1a à V-K6b) et chaque cellule non « M » des deux matrices, le vérificateur a relevé ce que 03 prescrit ou suppose, puis cherché dans les 719 lignes une interdiction, une fenêtre horaire, un préavis ou un préalable contraire ou manquant, et comparé chaque paraphrase au texte du registre.

### 3.2 Résultat par phase

| Phase ou section de 03 | Contraintes opposables examinées | Violation | Autres défauts trouvés (corrigés) |
|---|---|---|---|
| Phase 0 (§1.1) | Livrables datés, approbations préalables, AR-DEV-058, AR-DEV-030, AR-DEV-197, AR-DEV-204 | Aucune | AR-DEV-214 fusionnait deux régimes de certification ; « 10 jours » sans « ouvrables » (AR-DEV-057, 060) ; AR-DEV-065 rangé dans un groupe sans rapport ; « accès unique » non écrit (AR-DEV-134) |
| Transversales (§1.2) | — | Aucune | ME-134 à 140 absents du tableau (repris) |
| Étapes types (§1.3) | AR-PLN-040 à 044 | Aucune | E5 placée après E4 sur une lecture de « travaux par l'extérieur » présentée comme écrite (marquée `[lecture]`, lecture alternative exposée) |
| Phase 4 (§1.4) | AR-DEV-170, AR-DEV-275, ME-069, ME-105 | Aucune | AR-DEV-273 (60 %) et AR-DEV-271 (8 semaines avant) rangés en clôture ; réinstallation des luminaires (ME-105 : « après les travaux de revêtement ») rangée en clôture ; première certification de l'air médical omise |
| Phase 1 (§2.2) | AR-PLN-009, 010 ; CI-TAB-006 à 012 ; ME-108, 110 | Aucune | ME-009 et ME-095 (chirurgie d'un jour, zone H) comptés en phase 1 ; local R-22 justifié par une « adjacence » non écrite (remplacée par ME-108 « Secteur IRM ») |
| Phase 2 — 2.N, 2.E, 2.S, 2.O (§2.3) | ME-049 à 051, 056 à 058, 087, 118, 119 ; CI-TAB-024 à 029 | Aucune | Fiche 2.S sans mesures transitoires (ME-056) ; ME-058 fenêtre omise ; ME-087 « dimanche » au lieu de « semaine » ; liste des locaux de CI-TAB-028 abrégée à tort ; « échafaudage de quatre étages » non écrit |
| Phase 3 — 3.N, 3.O, 3.S (§2.4) | ME-065 à 067, 075 à 077, 006 à 008, 092 ; AR-DEV-024, 032, 062, 198 ; CI-TAB-019 à 022 | Aucune | AR-DEV-198 déclaré « non écrit » ; ordre nord → ouest présenté comme écrit ; AR-DEV-352 cité pour la clôture plus haute (C-38) ; AR-DEV-139 absent de 3.S ; zone d'ambulance rattachée au sud sans signaler AR-PLN-004 « nord » |
| Diagramme A (§2.6) | AR-DEV-275 ; ME-067 | Aucune | Flèche « après revêtement nord → 3.O » présentée comme écrite (pointillée `[lecture]`) ; AR-DEV-275 dessiné sur une seule transition (note ajoutée) |
| Variantes (§2.7) | ME-065 ; ST-023 à 026 ; AR-PLN-036 | Aucune | V-A4 « viole ME-065 » excessif ; AR-DEV-102 cité pour la protection de toitures neuves ; appui de l'échafaudage sur les toitures présenté comme écrit |
| Matrice A (§2.8) | ME-056, 058, 087, 095, 105, 145 ; CI-TAB-005, 009 | Aucune | Codes « C » sans coupure écrite (service alimentaire, volets) ; « M » alors qu'une dépose est écrite (ME-095) ; état P manquant (ME-056) ; caméra d'urgence « Aucun arrêt » (Z-06) non signalée |
| B-A, B-B, B-C (§3.2 à §3.4) | AR-PLN-040, 045 ; CI-TAB-005 à 029 | Aucune | « Condition écrite » d'AR-PLN-040 ; AR-PLN-045 « remise » (au propriétaire) ; ME-045 « niveau non écrit » alors que « (tour) » est écrit ; listes B-B et B-C incluant ME-063 et ME-055 par plage |
| Diagramme B (§3.5) | CI-TAB-004 ; AR-PLN-040 | **Une** : toile d'échafaudage dessinée après l'achèvement des façades | Nouvelle issue et prises d'air du sous-sol dessinées comme dépendant des façades sans texte |
| Matrice B (§3.6) | Idem matrice A | Aucune | Mêmes codes que la matrice A |
| Conflits K1 à K7 (§4) | AR-DEV-198 ; AR-PLN-040 ; ME-065 ; R-30 | Aucune | K4 « non écrit » ; K1 fondé sur la lecture large d'AR-PLN-040 ; K2 « viole » ; K3 attribuait la colonne « Restriction saisonnière » à D5 au lieu de D11 |
| Validation CISSS (§5) | AR-DEV-038 ; ME-048, 087, 088 | Aucune | AR-DEV-038 (entrepreneur spécialisé → général) n'est pas un point de validation du CISSS ; « nuit » pour ME-048 (« nuit ou fin de semaine ») ; « hors été » pour ME-087/088 (« semaine, hors été ») ; « occupation de la chambre 216 » non écrite dans ME-057 |

### 3.3 Points sensibles vérifiés conformes

Conduits temporaires de l'hémodialyse avant démolition et coupures « dimanche seulement, en dehors de la période estivale » (ME-049 à 051) ; évents d'autoclaves avant la façade ouest, « nuit ou le matin avant 10 h », 24/7 (ME-075 à 077) ; médecine nucléaire « vendredi au dimanche », supports temporaires (ME-118, 119) ; jalons et préalables de la phase 0 (AR-DEV-058, 030, 197, 204) ; gicleurs du quai « 2 × 2 h », alarme fonctionnelle, préavis 48 h, calendrier du jeudi (ME-006 à 008, ME-092, AR-DEV-024, 032, 062) ; plexiglas, bâti isolé novembre–avril, thermos le même jour (AR-PLN-041, 042, 044) ; classes et horaires du tableau CISSS repris ligne à ligne (13 identifiants) ; AR-DEV-170 et 275 ; dates contractuelles (CI-CTR-001) ; seuils de température (ST-034, 035 ; AR-DEV-304, 309, 316, 317, 320, 329, 343, 144) ; correspondance phases ↔ zones marquée `[lecture]` (C-35) ; existence des 719 identifiants et des codes C-, Z-, R- cités.

---

## 4. Hypothèses non sourcées glissées dans 03

Constats confirmés, avec la correction apportée. La colonne « Source » renvoie aux constats des passes (V1-n, V2-n, V3-n).

| no | Affirmation de 03 (version vérifiée) | Ce que disent 02 / 01 | Source | Correction (commit) |
|---|---|---|---|---|
| H-01 | « Le phasage détaillé relève contractuellement de l'entrepreneur général (C-13 ; AR-DEV-013, AR-DEV-052) » | AR-DEV-013 et 052 ne disent pas qui définit le phasage ; C-13 met en regard trois attributions (entrepreneur, documents d'architecture, CISSSGA) ; ST-007 confie la séquence à l'entrepreneur | V1-24, V2-1 | Phrase réécrite avec C-13 et ST-007 (a587c39) |
| H-02 | Légende des zones A à L et liste « phase 1 = D, E, F… » sans source | La légende n'est pas dans 02 ; elle est transcrite en 01 §8.5 ; C-35 pour la lecture des couleurs | V2-21, V2-22 | Renvoi à 01 §8.5 ajouté (c772626) |
| H-03 | Zones B (laboratoire) et H (chirurgie d'un jour, urgence) aux façades nord et sud | La légende ne donne aucune orientation à B ni à H ; ST-039 : laboratoire au « basilaire nord-ouest » ; Z-24 | V2-37, V2-46 | Marqué `[lecture]` dans les titres de 3.N, 3.O, 3.S et au §2.1 (c772626) |
| H-04 | « Une seule règle écrite : … ⇒ 3.N avant 3.O » ; V-A4 « viole ME-065 » | ME-065 : prise temporaire « sur la façade ouest pour permettre les travaux de revêtement sur la façade nord » ; ME-067 : réinstallation « après » le revêtement nord ; Z-02 : simultanéité non exclue | V1-4, V2-36, V2-49 | Ordre marqué `[lecture]`, flèche pointillée, V-A4 « incompatible avec l'emplacement écrit » (74b7dfe) |
| H-05 | « Condition écrite : les fenêtres existantes ne peuvent être retirées qu'une fois les travaux par l'extérieur complétés (AR-PLN-040) » ; E5 après E4 ; K1 | AR-PLN-042 : bâti isolé « pour la durée des travaux à effectuer par l'extérieur » ; AR-PLN-046 à 048 : « étape no 1 : travaux par l'extérieur » (étape de la fenêtre) ; C-36, Z-07 non tranchés | V1-2 | Deux lectures exposées, `[lecture]`, variante V-K1d (2f7f1e3) |
| H-06 | Conduit de médecine nucléaire modifié « avant » la façade est (ME-118) | ME-118 : « afin de permettre les travaux de réfection des façades » ; « avant » non écrit | V2-8 | Antériorité marquée `[lecture]` (a587c39) |
| H-07 | Air médical « (basilaire nord-ouest) », 3.N/3.O sans réserve | ME-064 : « toiture nord-ouest » ; ME-065 : « façades nord et ouest » ; tour ou basilaire non écrit | V1-17, V2-7, V2-32 | `[à confirmer]` au §0.4, §2.4.1, §6 ; « M ? » en 2.N/2.O (f240895) |
| H-08 | « Retrait des temporaires de l'air médical après certification (ME-069) » ; certification en phase 4 seulement | ME-069 : « 2 fois, relocalisation et prise d'air permanente » | V1-13, V2-43 | Deux certifications : 3.N puis clôture (f240895) |
| H-09 | Local R-22 en phase 1 « (adjacence est) » | Aucun texte ; ME-108 : « Secteur IRM / local R-22 (RC) » ; Z-25 : « entre l'urgence et la radiologie » | V2-24 | Justification par ME-108, Z-25 cité (4d8b5ae) |
| H-10 | Zone d'ambulance rattachée à 3.S sans réserve | ME-006 à 008, ME-147 : « sud » ; AR-PLN-004 : « Zone ambulance (nord) » ; détail 1 de la feuille 002 sans orientation ; CI-TAB-016 : zone non renseignée | V2-44, V3-8, V3-14 | Divergence exposée dans 3.N, 3.S et au §6 (4d8b5ae, c772626) |
| H-11 | Escalier no 7 = nouvelle issue, façade nord | Z-12 : identité à confirmer ; ST-039 : « basilaire nord-ouest » | V2-38 | `[à confirmer]`, 3.N ou 3.O (c772626) |
| H-12 | ME-058 « face non écrite » ; ME-087 en 2.N ; ME-116 « coin nord-est » ; ME-122/123 « face non écrite » | Lignes D5 N-F-V-009 (nord), E-G-V-003 (est), S-A-P-001 et N-F-P-001 (sud et nord), N-F-V-011 (nord) selon la légende de D5 (C-31) ; D4 « coin nord-est » pour ME-116 | V2-26, V2-31, V2-33, V2-58, V3-15 | Codes de D5 cités au §6 et dans les fiches ; ME-087 en 2 toutes faces (4d8b5ae, 639b822, c772626) |
| H-13 | Sous-sol du service alimentaire en phase 2 « `[tel qu'écrit]` » | Marqueur hors nomenclature ; la tour est aux niveaux 200 à 400 ; AR-PLN-056 (sous-sol) était marqué NA pour la même raison | V2-28, V3-13 | `[à confirmer]`, Z-24, ligne ajoutée au §6 (4d8b5ae, c772626) |
| H-14 | CI-TAB-025 et 028 rangés en C.2 et C.4 sans marqueur alors que le tableau les code A.6 | Sources L33-L34 et L39-L40 : A.6 (C-30) | V2-61, V3-39 | `[choix]` au §3.1 ; double code A.6 + niveau documenté (4d8b5ae, c772626) |
| H-15 | « Occupation de la chambre 216 » comme point de validation | ME-057 ne pose aucune condition d'occupation ; D5 : « valider fréquence utilisation salle » (Z-17) | V1-22 | « non écrite dans ME-057 ; Z-17 » (c772626) |
| H-16 | Prototype en phase 1 ; code B « A » | Dépend de la première fenêtre exécutée, dont le niveau n'est pas écrit | V3-34 | Code B élargi (A, B, C), §6 (4d8b5ae) |
| H-17 | « Échafaudage de quatre étages sur les toitures du basilaire » ; « L'échafaudage de la tour s'appuie sur les toitures du basilaire (ST-023 à 026) » | ST-023 à 026 : capacités, attestation, ancrages ; rien sur la hauteur ni l'appui ; Z-27 | V2-29 | `[lecture]`, Z-27 (a587c39) |
| H-18 | « Toitures refaites avant l'échafaudage, protection des toitures neuves (AR-PLN-036, AR-DEV-102) » | AR-DEV-102 : propane et entreposage sur toiture ; AR-PLN-063 : bande de ±610 mm démolie | V1-12, V2-48 | Réécrit avec AR-PLN-063, AR-PLN-036, ST-024 (a587c39) |
| H-19 | « Accès unique depuis la rue Monseigneur-Ross Est » | AR-DEV-134 ne dit pas « unique » ; C-10 relève des régimes divergents | V2-13 | Réécrit (4d8b5ae) |
| H-20 | « La prise temporaire percerait un revêtement ouest déjà neuf (ME-156) » | Raisonnement, non un texte ; ME-156 vise l'étanchéité des percements | V2-49 | `[lecture]` (74b7dfe) |
| H-21 | Dates contractuelles rappelées sans réserve | C-14 : dates antérieures à l'émission des plans et devis, « inapplicables en l'état » | V2-4 | Renvoi à C-14 (a587c39) |
| H-22 | « D5 col. « Restriction saisonnière » … (R-30) » | R-30 et Z-10 visent D11 col. S | V2-55 | Corrigé (a587c39) |
| H-23 | « Toile solaire retirée et remise (AR-PLN-045) » | « remise au propriétaire » ; toile neuve : AR-DEV-350 | V1-27 | Réécrit (a587c39) |
| H-24 | ME-045 « faute de niveau écrit » | ME-045 zones : « Façade ouest (tour) » | V1-28, V2-35 | Réécrit ; K2 cite ME-045 plutôt que Z-24 (4d8b5ae, 74b7dfe) |
| H-25 | Locaux « 309 à 324 » (CI-TAB-028) | « 309/310/311/332/321/322/323/324 » | V2-30 | Liste telle qu'écrite (c772626) |
| H-26 | « Maintien de deux issues `[non écrit]` » | AR-DEV-198 : « 2 issues minimum, capacité d'évacuation non réduite » | V1-1 | AR-DEV-198 cité dans 3.N et K4 (b0a9f3d) |
| H-27 | « Clôture plus haute adjacente (AR-DEV-352 ; C-38) » | AR-DEV-352 : barbelé et poteaux ; la clôture plus haute est dans C-38 seulement | V1-11, V2-39, V3-16 | Réécrit ; AR-DEV-352 en 4 avec §6 (4d8b5ae, a587c39) |
| H-28 | AR-DEV-273 (60 %) et AR-DEV-271 (8 semaines avant) en phase 4 ; ME-105 réinstallation en phase 4 | Jalons antérieurs à la clôture ; ME-105 : « après les travaux de revêtement » | V1-14, V1-25, V3-18 | AR-DEV-273 en T ; AR-DEV-271 déclenché pendant la dernière phase ; ME-104 à 106 « P → M » par sous-phase (4d8b5ae, 639b822, a587c39) |
| H-29 | AR-DEV-214 « certification < 12 mois avant démarrage dans les zones du groupe 4 » | Deux régimes : < 12 mois en général ; avant le démarrage dans les zones du groupe 4 | V1-23, V2-16 | Réécrit (a587c39) |
| H-30 | AR-DEV-038 en point de validation CISSS | Relation entrepreneur spécialisé → général | V2-57 | Retiré de la ligne (a587c39) |
| H-31 | AR-DEV-065 dans le groupe « mise en service » | Essais de moins de 3 ans (dessins d'atelier) | V2-15, V3-22 | Passé en T (4d8b5ae) |
| H-32 | Codes « C » (coupure) pour les prises d'air du service alimentaire et les volets coupe-feu | CI-TAB-005, 009 ; ME-025, 029 : activité classée, aucune coupure écrite | V1-9, V2-50 | Code « I » créé (639b822) |
| H-33 | Matrice : ME-056 « C » seul ; ME-095 alarme « M » en 3.S ; ME-087 « dimanche hors été » ; ME-048 « nuit » | ME-056 : démantèlement + prolongation temporaire ; ME-095 : détecteur enlevé temporairement ; ME-087 : « Semaine » ; ME-048 : « Nuit ou week-end » | V1-5, V1-8, V1-10, V1-26 | Matrices et §5 corrigés (639b822) |
| H-34 | Caméra d'urgence « P relocalisés » sans mention du « Aucun arrêt » de D5 | Z-06 cite « Aucun arrêt » (sans identifiant) ; ME-145 : dépose temporaire | V1-16 | Exception signalée dans les matrices (639b822) |
| H-35 | Fiche 2.S sans mesures transitoires ; ME-058 sans fenêtre | ME-056 : conduit prolongé, grillage aviaire ; ME-058 : « Nuit/Jour si aucune chambre occupée » | V1-6, V1-7 | Ajoutés (639b822) |
| H-36 | 3.S sans préavis de déplacement de voie | AR-DEV-139 : trois semaines | V1-21 | Ajouté (a587c39) |
| H-37 | Troisième jalon d'AR-DEV-058 omis au §0.4 | « changements des ouvertures en relation avec l'ordonnancement opérationnel » | V1-34 | Ajouté (a587c39) |
| H-38 | AR-DEV-275 dessiné sur une seule transition | « après chaque phase » | V1-30 | Note sous le diagramme (a587c39) |
| H-39 | Délais « 10 jours » (AR-DEV-057, 060) | « dix (10) jours ouvrables » | V1-29 | Corrigé (a587c39) |
| H-40 | Risques sans texte : temporaires d'évents au coin sud-ouest (ME-075) vs 3.S et ST-026 ; portée d'AR-DEV-170 sur les escaliers temporaires ; ME-020 (percements hors heures d'occupation) vs horaire « J » ; réinstallation des évents « à la fin des travaux » | Textes cités ; aucun ne tranche | V1-18, V1-19, V1-20, V1-32 | Consignés dans 3.O, 3.S, K4, 3.N, B.1.2 (d9badb9) |

---

## 5. Affectations ID → phase contestées (passe V3)

### 5.1 Erreurs confirmées et corrigées (commit 4d8b5ae)

| ID | Codes vérifiés (A / B) | Problème | Codes corrigés (A / B) |
|---|---|---|---|
| AR-PLN-001 | 0 / 0 | « En tout temps pendant la durée des travaux » | T / T |
| AR-DEV-077 | 0 / 0 | Site occupé « pendant toute la période des travaux » | T / T |
| AR-DEV-079 | 0 / 0 | Attestation avant le début, présence continue ensuite | 0,T / 0,T |
| AR-DEV-134 | 0 / 0 | Accès « pour toute la durée des travaux » | 0,T / 0,T |
| ME-089 | 1, 2.E, 2.O, 3.O / A, B, C | « Toutes façades », « durant toute la durée » ; l'est/ouest venait de ME-144 | T / T |
| ME-009, ME-095 | 1, 3.S / A, B | Salle de mécanique de la chirurgie d'un jour seule ; l'IRM venait de ME-112 | 3.S / B |
| CI-TAB-014 | 3.S / A.1, A.7 | Ligne D11 L18 codée A.1 ; A.7 venait de CI-TAB-018 | 3.S / A.1 |
| CI-TAB-018 | 3.S / A.1, A.7 | Ligne D11 L23 codée A.7 | 3.S / A.7 |
| CI-TAB-024 | 2 / A.6, C.2 | Ligne L32 codée C.2 ; A.6 venait de CI-TAB-025 | 2 / C.2 |
| CI-TAB-027 | 2 / A.6, C.4 | Ligne L38 codée C.4 | 2 / C.4 |
| AR-PLN-018 | 3.S / A.1 | Ligne du registre mal formée (§6) ; localisation divergente | 3.S / A.1 avec §6 |

### 5.2 Affectations douteuses reprises (commit 4d8b5ae)

AR-DEV-014, 025, 028, 029, 032, 049, 166, 190, 203, 214, 284, 286 ; CI-CTR-004, 023 ; ST-020 → 0,T (mise en place avant le début, puis obligation maintenue ou répétée). AR-DEV-043, 065, 128, 153, 201, 273, 299, 353 ; CI-CTR-002 ; ST-021 ; AR-PLN-001 → T (règle de fond ou obligation répétée). AR-DEV-259 → 0,T,4. AR-DEV-125 → 0. AR-DEV-126, 154, 158 ; AR-PLN-074 ; CI-CTR-019 → T,4. AR-PLN-057 → 1, 2, 3 (niveaux nommés). AR-PLN-050, 051 → B : A, B, C. AR-PLN-004 → 3.S, 4. ME-069 → 3.N, 3.O, 4 ; ME-074 → 3.N, 3.O. ME-087 → 2 (toutes faces). ME-117 → 2.E sous réserve. ME-159 → T, 3.N. ST-031 → 1, 3 sous réserve. ST-037 → B : B. CI-TAB-009, 011 → 1 ; CI-TAB-022 → 3.N, 3.S (la lettre A contredit le niveau écrit). CI-TAB-016 ; ME-025, 029 ; CI-TAB-005 ; AR-DEV-352 → inscrits au §6.

### 5.3 Écarts entre les listes de 03 et l'affectation (corrigés par régénération, commit 4d8b5ae)

Plage « ME-059 à 084 » de B-B incluant ME-063 ; plage « ME-042 à 058 » de B-C incluant ME-055 ; AR-DEV-153 absent des groupes de la phase 0 ; ME-134 à 140 absents du tableau des transversales ; AR-PLN-004, AR-PLN-074 et ME-069 cités en phase 4 sans code 4 ; six écarts de présentation dans la colonne « Phases (A) » du §5 ; renvoi à `04-verification.md` avant que le fichier existe (levé par le présent document).

---

## 6. Défauts découverts dans le registre 02

| Défaut | Constat | Correction |
|---|---|---|
| Renvois orphelins | AR-DEV-048, 049 et 058 renvoyaient à des blocs « B.3 », « B.4 », « B.5 » absents de 02 (restes des rapports d'extraction) | Citations du devis 01 32 16.19 (p. 20 et 25) insérées (commit b410c90) |
| Lignes mal formées | AR-PLN-018 à 021 : un trait vertical non échappé dans la source (« détail 1 (001 \| 002) ») décalait les colonnes ; la colonne Zones manquait et le Type portait une localisation entre parenthèses (« façades ouest/nord-ouest », « façade sud », « façade sud-est / cour ») sans passage écrit correspondant | Colonnes rétablies, zones reprises des titres des détails de la feuille 002, type neutre (commit 4c20525) |
| Localisation divergente de la zone d'ambulance | ME-006 à 008 et ME-147 (D4, D5) : « Entrée ambulance sud » ; AR-PLN-004 (D2 001/002) : « Zone ambulance (nord) » ; détail 1 de la feuille 002 : deux configurations sans orientation ; CI-TAB-016 : zone non renseignée. Le plan clé (feuille 010) porte les symboles de porte de garage au sud du basilaire sud, près de la zone H (urgence), et à l'ouest `[lecture]` | Non tranchée ; exposée dans 03 (§2.4.1, §2.4.3, §6). À inscrire au registre comme contradiction lors de sa prochaine révision, avec la lecture du plan clé à faire confirmer par les architectes |

---

## 7. Constats non retenus ou requalifiés

| Constat | Motif |
|---|---|
| V3-13 : marquer NA (découpage A) les prises d'air du service alimentaire (ME-025, 029 ; CI-TAB-005) comme AR-PLN-056 | La ligne CI-TAB-005 écrit « zone A » ; AR-PLN-056 n'écrit aucune zone. Les deux cas ne sont pas identiques : le code 2 est conservé tel qu'écrit, avec réserve au §6 et marqueur `[à confirmer]`. |
| V3-33 et V3-58 : aligner AR-DEV-351, 352, 353 (clôtures) sur un même code | Trois contenus différents : interdiction de coupe au chantier (règle continue, T), récupération du barbelé (fin de projet, 4), échantillon avant d'entamer (répété à chaque type, T). AR-DEV-353 passé en T ; 351 et 352 inchangés. |
| V1-2 (partiellement) : renverser l'ordre E4 → E5 | Aucune des deux lectures d'AR-PLN-040 n'est écrite ; 03 conserve la lecture large comme référence et expose la lecture étroite, plutôt que de substituer une lecture à l'autre. |
| V1-4, V2-36 (partiellement) : retenir « nord et ouest simultanés » | La simultanéité n'est pas exclue par Z-02, mais l'emplacement écrit de la prise temporaire (façade ouest pendant la façade nord) rend l'ordre nord → ouest la lecture la moins risquée ; conservé comme `[lecture]` avec V-A4 non retenue « en l'état ». |
| V2-24 (partiellement) : rattacher le local R-22 à NA | ME-108 écrit « Secteur IRM / local R-22 (RC) » : la phase 1 a un fondement écrit, même si Z-25 le nuance. Conservé en 1 `[choix]` avec Z-25 cité. |
| V3-17 : AR-PLN-014 en 3.N et 3.S comme AR-PLN-004 | AR-PLN-004 a été ramené à 3.S, 4 (chemin temporaire et remise en état) ; la localisation nord/sud est traitée au §6 plutôt que par un double code sans fondement. |

---

## 8. Ce qui reste ouvert après correction

Ces points ne peuvent pas être résolus à partir des documents du dépôt ; ils sont exposés dans 03 (§4 K1 à K7, §6) et appellent une décision des émetteurs.

1. Portée de « travaux par l'extérieur » dans la note de la feuille 505 (AR-PLN-040) : commande l'articulation façades / fenêtres et le conflit K1 (architectes).
2. Ordre des façades nord et ouest et localisation tour/basilaire de la centrale d'air médical, de la prise d'air du bloc opératoire et des évents d'autoclaves (WSP).
3. Localisation de la zone d'ambulance (« sud » en D4/D5, « nord » en D2) et orientation du détail 1 de la feuille 002 (architectes, WSP).
4. Identité escalier no 7 = nouvelle issue, et ordre nouvelle issue / condamnation d'une issue existante (architectes, structure ; Z-12).
5. Régime PCI applicable (procédure du CISSS de la Gaspésie absente du dépôt ; C-01) et classes attribuées (C-02, C-03) ; signification de « J », « S », « J/S » (Z-01) ; définition de « période estivale » (Z-10) (CISSS).
6. Secteurs « non touchés » C et L présents dans les activités du tableau CISSS (C-40, K6) (architectes, CISSS).
7. Contradiction interne D4/D5 sur la caméra d'urgence (« Aucun arrêt » vs dépose temporaire, ME-145) (WSP).
8. Six identifiants non déterminables (AR-PLN-056, AR-PLN-079, ME-062, ME-141, ME-143, CI-TAB-013).
9. Nature exacte des interventions sur les conduits de l'unité de ventilation de l'hémodialyse/laboratoire du bassin 16 (tracé temporaire, nouveaux conduits, basculements, interruptions) et séquence de la passerelle : documents WSP à compléter (Z-29 ; complément §10).

---

## 9. Journal des corrections apportées à 03 (un commit par problème)

| Commit | Problème corrigé | Sections de 03 |
|---|---|---|
| 4d8b5ae | Affectations ID → phase contestées : exigences continues codées 0, codes hérités d'un regroupement, sous-sol et façades non écrites, local R-22, listes et annexe régénérées | §0.3, §1.1, §1.2, §2.2, §2.3, §2.4, §3.2 à §3.4, §5, §6, annexe A |
| b0a9f3d | AR-DEV-198 (deux issues minimum) cité au lieu de « non écrit » | §2.4.1, §4 K4 |
| 2f7f1e3 | Portée d'AR-PLN-040 marquée `[lecture]`, lecture alternative, variante V-K1d | §1.3 E5, §3.2 A.2, §3.3, §3.4, §4 K1 |
| 9a688dd | Diagramme B : toile d'échafaudage avant les façades ; nouvelle issue et prises d'air sans dépendance écrite | §3.5 |
| 74b7dfe | Ordre nord → ouest présenté comme lecture ; V-A4 reformulée ; K2 cite ME-045 | §2.4, §2.4.2, §2.6, §2.7, §4 K2 |
| f240895 | Air médical : localisation à confirmer ; deux certifications | §0.4, §2.4.1, §2.4.2, §2.5, §2.8, §3.6, §5 |
| 639b822 | Matrices fidèles au registre ; fiche 2.S ; ME-058 ; code « I » ; caméra d'urgence | §2.3, §2.3.1, §2.3.3, §2.8, §3.4, §3.6, §5 |
| c772626 | Localisations lues sur les plans marquées ; localisations divergentes ; renvoi à 01 §8.5 ; liste des locaux de CI-TAB-028 | §2.1, §2.2, §2.3, §2.3.1, §2.4.1 à §2.4.3, §2.7, §3.1, §3.4, §5 |
| a587c39 | Identifiants cités de travers et paraphrases inexactes (C-13/ST-007, C-14, AR-DEV-058, 057, 060, 214, 271, 273, 352, 102, 038, 139 ; AR-PLN-045 ; ME-118 ; R-30 ; local R-22) | En-tête, §0.1, §0.3, §0.4, §1.1, §1.4, §2.2, §2.3, §2.4.1, §2.4.3, §2.6, §2.7, §3.2, §4 K3, §5 |
| d9badb9 | Risques non sourcés consignés (ME-075 coin sud-ouest, AR-DEV-170, ME-020, ME-076) | §2.4.1, §2.4.2, §2.4.3, §3.3, §4 K4 |

Corrections au registre 02 : b410c90 (renvois orphelins), 4c20525 (lignes AR-PLN-018 à 021).

---

## 10. Complément du 2026-09-15 — unité de ventilation du bassin 16

Constat postérieur à la vérification, déclenché par une question de GLCRM sur « l'appareil de la toiture bassin 16 ». La feuille 301 numérote les toitures « BASSIN #1 » à « #23 » ; le bassin 16 est la bande nord au pied de la face nord de la tour, entre les axes 6 et 8, avec renvoi « voir plan du niveau 200 ». L'appareil qui s'y trouve est l'unité de ventilation extérieure de l'hémodialyse/laboratoire (D4 ME014, vues agrandies aux axes 6 à 8 ; passerelle et escalier P-01 de la feuille 704) `[lecture]`, identification confirmée par GLCRM.

Ce que les documents disent de cette unité est cohérent : D4 (ME004(D) note D9, ME014 notes D1 à D4) et D5 (ligne N-F-V-005) la conservent en place et en fonction, remplacent les conduits du secteur hémodialyse par des conduits temporaires puis définitifs, et enlèvent temporairement la passerelle d'accès. GLCRM précise la séquence : conduits enlevés et relocalisés temporairement pour le parement, passerelle enlevée avant et réinstallée après la modification des conduits, unité maintenue en fonction avec interruption temporaire. Ce qui n'est écrit nulle part : le tracé et la forme des conduits temporaires et définitifs, la séquence de basculement et les fenêtres d'interruption au-delà de « une journée, un conduit à la fois, dimanche hors période estivale » (ME-051). WSP doit définir la nature exacte et complète des interventions ; ses documents ne sont pas terminés. Consigné en Z-29 du registre, en §6 de 03 et sur la planche 13 du cahier, marqué `[à confirmer]`.

Deux défauts du registre corrigés au passage :

1. AR-PLN-070 citait la « note 33 » des feuilles 702 à 704 ; les bulles des notes 35 (démantèlement temporaire) et 37 (réinstallation) sont accrochées au garde-corps G-02 de la feuille 703, où un petit appareil sur support est dessiné et photographié : c'est le bi-bloc de la salle d'observation de l'urgence (ME-090, ME-085), façade sud `[lecture]`, et non l'unité d'hémodialyse. Ligne corrigée ; renvoi R-41 ajouté (les « documents d'ingénierie » visés sont ME001(D) note D3 : présent).
2. AR-PLN-070 était classé transversal par la règle « toitures et entretoits : toiture de chaque phase », alors que la note vise un appareil précis. Réaffecté à 3.S (découpage A) et B-A (découpage B), comme ME-085 et ME-090 ; fiche 3.S amendée, annexe A régénérée. Le décompte T du §2.1 ci-dessus (498) passe à 497 ; les autres décomptes de ce document ne sont pas recalculés.

Une première intégration, le même jour, avait rattaché AR-PLN-070 à l'unité d'hémodialyse et créé une contradiction C-41 entre D2 et D4/D5 ; la lecture des bulles de la feuille 703 l'infirme. C-41 a été retirée du registre avant diffusion ; la numérotation des contradictions s'arrête à C-40.

---

## Annexe A — Couverture : phase de traitement de chacun des 719 identifiants

Colonnes : phases des découpages A et B (codes du §0.2 de 03) ; sections de 03 où l'identifiant est cité (hors annexe A de 03) ; base de l'affectation (règle spécifique motivée dans l'outil d'affectation, ou règle par défaut T). Les identifiants « NA » sont traités au §6 de 03.

| ID | Contrainte (abrégée) | Type | Phases — découpage A | Phases — découpage B | Sections de 03 où l'ID est cité | Base de l'affectation |
|---|---|---|---|---|---|---|
| AR-DEV-001 | Demandes d'information à formuler avant la fermeture des soumissions | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-002 | Le début des travaux vaut acceptation des conditions existantes | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-003 | Obligation d'exécuter sans interruption pendant l'arbitrage d'un malentendu technique | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-004 | Aviser avant d'exécuter en cas d'erreur, omission ou contradiction | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-005 | Respect obligatoire des zones de chantier désignées (déplacements, entreposage, accès, circula… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-006 | Essais intégrés ULC-S1001 en fin de projet, toutes disciplines, avec préalables soumis | préalable | 4 | 4 | Phase 4, diagramme | règle spécifique |
| AR-DEV-007 | Présence continue obligatoire d'un chargé de projet et d'un surintendant | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-008 | Échéancier très court annoncé | préavis | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-009 | Nettoyage complet à la fin de chaque quart de travail, selon les normes d'entretien de l'établ… | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-010 | Protections temporaires à ériger et maintenir autour de l'édifice, des ouvertures et des échaf… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-011 | Aucune fermeture de rue, ruelle ou trottoir, en aucun temps; édifices avoisinants occupés | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-012 | Protection des ouvrages à la fin de chaque quart et par temps non clément | préalable + fenêtre h… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-013 | Travaux subdivisés en plusieurs phases selon 01 32 16.19 | autre (autre (phasage… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-014 | Documents obligatoirement conservés au chantier, dont le calendrier d'exécution approuvé | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-015 | Accès au site uniquement selon les directives de l'entrepreneur général | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-016 | Site accessible en tout temps aux usagers et employés; zones de l'entrepreneur clôturées | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-017 | Horaire des travaux renvoyé au Contrat du CISSSGA | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-018 | Double approbation avant tout percement/coupe d'un élément structural ou électromécanique | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-019 | Démontage, entreposage et réinstallation des équipements de mécanique gênant les travaux | autre (autre) | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-020 | Autorisation préalable de l'entrepreneur général et du professionnel pour toute personne accéd… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-021 | Liste des employés fournie 2 jours ouvrables avant le début des travaux | préavis | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-022 | Réunion de chantier SST obligatoire pour tout le personnel de terrain avant le début | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-023 | Interdictions sur le site : animaux, tabac, feux | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-024 | Préavis de 48 h au professionnel et au responsable du CISSSGA avant toute interruption de serv… | fenêtre horaire + pré… | T | T | Phase 1, Phase 2.E, Phase 3.S, T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-025 | Itinéraires de rechange à prévoir pour la circulation du personnel et des véhicules | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-026 | Calendrier d'arrêt/fermeture des installations actives soumis à approbation, avec information… | préalable | 0 | 0 | Phase 0, §5 validation CISSS | règle spécifique |
| AR-DEV-027 | Services temporaires obligatoires pour maintenir les systèmes critiques du bâtiment | préalable | T | T | Phase 0, T (§1.2) | règle par défaut (T) |
| AR-DEV-028 | Moyens d'accès temporaires distincts des ouvrages finis à concevoir et entretenir | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-029 | Séparation obligatoire des accès chantier / accès hospitaliers; accès hospitaliers accessibles… | préalable + interdict… | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-030 | Piquages et raccordements sur les réseaux existants à exécuter avant le début des travaux; ent… | préalable | 0 | 0 | Phase 0, diagramme, préambule / vue d'ensemble | règle spécifique |
| AR-DEV-031 | Préavis 48 h et aucune interruption sans approbation du CISSSGA | interdiction + préavis | T | T | Phase 1, T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-032 | Calendrier des travaux soumis au CISSSGA et approuvé pour toute coupure; avertissement 48 h à… | préalable + préavis | 0, T | 0, T | Phase 0, Phase 1, Phase 3.S, T (§1.2), §5 validation CISSS | règle spécifique |
| AR-DEV-033 | Installation non repérée découverte : avis immédiat + rapport écrit détaillé incluant le risqu… | interdiction + préavis | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-034 | Gêner le moins possible la circulation, surtout au service d'urgence | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-035 | Plan de sécurité du site à fournir avant d'entreprendre les travaux, avec localisation affiché… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-036 | Accès à la zone de construction par l'entrée principale seulement, sauf approbation | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-037 | Agents de sécurité issus du Corps canadien des commissionnaires pour enregistrer et escorter l… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-038 | Calendrier des heures anticipées de travail 1 semaine avant la mise en route; tout changement… | préavis | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-039 | Escorte 1 commissionnaire / 5 travailleurs en tout temps dans les zones de construction avec s… | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-040 | Droit de refuser l'accès au chantier à toute personne jugée menaçante | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-041 | Travaux en zone hospitalière selon les méthodes hospitalières : abris et filtres EPA | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-042 | Travaux bruyants en zones hospitalières : en soirée, supervisés, avec agent de contrôle du bru… | préalable + fenêtre h… | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-043 | Connaissance et respect de la réglementation du centre hospitalier par le personnel | préalable | T | T | T (§1.2) | règle spécifique |
| AR-DEV-044 | Accès des véhicules de livraison limité selon le plan de sécurité | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-045 | Livraisons hors des heures de pointe, entre 9h00 et 15h00 | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-046 | Primauté des exigences les plus sévères en cas de contradiction avec les documents du CISSSGA | autre (autre (hiérarc… | T | T | T (§1.2), §4 conflits | règle par défaut (T) |
| AR-DEV-047 | Les calendriers ne lient pas le CISSSGA ni les professionnels | autre (autre) | T | T | T (§1.2), hors-phase (préambule ou sections transversales) | règle par défaut (T) |
| AR-DEV-048 | Obligation de consulter le tableau de coordination des équipements électromécaniques de WSP, q… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-049 | Tableau des contraintes opérationnelles de l'Établissement (par phase) : horaire, durée maxima… | autre (autre (renvoi… | 0, T | 0, T | Phase 0, T (§1.2), §4 conflits | règle spécifique |
| AR-DEV-050 | Réunion d'ordonnancement au plus tard 10 jours ouvrables après l'attribution | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-051 | Cinq calendriers à soumettre (exécution avec chemin critique, hebdomadaire, dessins d'atelier,… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-052 | Chaque phase doit apparaître distinctement et être subdivisée par activité | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-053 | Cycles de révision des calendriers : 15 j pour resoumettre, 10 j de commentaires, 10 j de révi… | préalable + préavis | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-054 | Mise à jour mensuelle des calendriers, 2 jours ouvrables avant la 1re réunion de chantier du m… | préavis | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-055 | Durée des activités limitée à environ 10 jours ouvrables | autre (autre) | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-056 | Diagramme GANTT (plan d'ensemble) au plus tard 5 jours ouvrables après l'attribution | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-057 | Calendrier d'exécution au plus tard 10 jours ouvrables après acceptation du plan d'ensemble | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-058 | Jalons obligatoires incluant travaux préparatoires avant démolition et nouvelle issue | préalable | 0, 3.N | 0, B.1.2 | Phase 0, Phase 3.N, Phase B-B, diagramme, préambule / vue d'ensemble, §1.3 étapes types, §2.7 variantes, §4 conflits | règle spécifique |
| AR-DEV-059 | Examen du plan d'ensemble en 5 jours ouvrables; révision en 5 jours ouvrables si jugé inexploi… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-060 | Calendrier des travaux avec date d'achèvement pour chaque phasage dans les 10 jours ouvrables… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-061 | Délais minimaux à prévoir pour l'inspection des travaux : 5 et 10 jours ouvrables | préavis | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-062 | Calendrier hebdomadaire le jeudi AM indiquant les coupures de services | fenêtre horaire + pré… | T | T | Phase 3.S, T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-063 | Interdiction d'entreprendre les travaux avant la fin de l'examen des pièces soumises; aucun dé… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-064 | Délais d'examen : 10 jours ouvrables par lot; 10 jours ouvrables pour resoumission; 21 jours o… | préavis | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-065 | Essais ayant moins de 3 ans à la date d'attribution | préalable | T | T | T (§1.2) | règle spécifique |
| AR-DEV-066 | Aspirateur HEPA obligatoire, balai interdit, sablage avec captation HEPA, aucun matériau organ… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-067 | Passage de l'aspirateur dans toutes les cavités avant fermeture | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-068 | Essais par un agent de validation mandaté par le CISSSGA en fin de travaux; correctifs sans dé… | préalable | 4 | 4 | Phase 4 | règle spécifique |
| AR-DEV-069 | Programme de prévention transmis 10 jours avant le début; droit de refuser le démarrage | préalable + préavis | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-070 | Cycle d'examen du programme de prévention : 10 jours ouvrables d'observations, 5 jours pour re… | préavis | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-071 | Plan d'intervention d'urgence à arrimer avec la procédure d'évacuation du site | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-072 | Procédures écrites spécifiques pour tout travail à risque élevé (démolition, plan de levage, e… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-073 | Certificat d'inspection mécanique de moins d'une semaine avant l'arrivée de chaque équipement… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-074 | Le professionnel peut ordonner l'arrêt immédiat de tout équipement suspect | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-075 | Localisation des bouteilles et réservoirs de gaz soumise au professionnel | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-076 | Risques inhérents au site déclarés : lignes aériennes, services souterrains, arbres à conserve… | autre (autre) | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-077 | Le site est occupé par des employés et/ou le public pendant toute la période des travaux | préalable | T | T | T (§1.2) | règle spécifique |
| AR-DEV-078 | Arrêt immédiat des travaux en cas de danger imprévu, avec mesures temporaires | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-079 | Agent de sécurité à temps plein dès le début si l'article 2.5.3 du Code de sécurité s'applique… | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-080 | Pouvoir d'arrêt et de reprise des travaux pour raisons de SST, avec préséance sur les coûts et… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-081 | Autorisations et permis requis pour tout empiètement sur la voie publique (échafaudages, grues… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-082 | Coordination obligatoire avec le représentant du site avant tout cadenassage en site occupé | préalable | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-083 | Fiche de cadenassage transmise 48 h avant le début; vérification par un représentant du site | préavis | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-084 | Travail sous tension exigé par les besoins opérationnels des occupants : permis signé par le r… | préalable | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-085 | Décapage au jet d'abrasif : procédure écrite préalable, abrasif < 1 % de silice | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-086 | Échafaudage sur toiture, avancée de toit, marquise ou mansarde : calculs, plans scellés et aut… | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-087 | Toiles protectrices ignifuges d'échafaudage devant laisser passer la lumière naturelle jusqu'a… | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-088 | Empêcher l'accès du public aux échafaudages; passages couverts ou filets approuvés par le prof… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-089 | Plan d'ingénieur requis pour tout échafaudage portant toiles ou bâches donnant prise au vent;… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-090 | Espaces clos : informations à obtenir auprès du représentant du site; évaluation des risques 1… | préavis | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-091 | Permis d'entrée en espace clos transmis 5 jours avant; un permis par quart de travail | préavis | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-092 | Permis d'entrée spécifique au site à utiliser si le représentant du site l'exige | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-093 | Service d'intervention d'urgence de la municipalité à aviser de la tenue de travaux en espaces… | préavis | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-094 | Plan de levage 5 jours avant; éviter le survol des zones occupées; sinon plan scellé, approuvé… | interdiction + fenêtr… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-095 | Liste des plans de levage prévus pour toute la durée du chantier, dès le début | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-096 | Permis de travail à chaud émis par le responsable du site au début de chaque quart et pour cha… | préalable + fenêtre h… | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-097 | Surveillance incendie 1 h minimum après chaque travail à chaud; permis remis au responsable du… | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-098 | Inspection finale 4 h après les travaux à chaud en présence de matériaux combustibles | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-099 | Système d'extraction d'air à filtres pour tout soudage ou découpage à l'intérieur | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-100 | Garde-corps de toiture maintenus jusqu'à la toute fin du projet; démantèlement autorisé par le… | préalable + interdict… | 4, T | 4, T | Phase 4, T (§1.2), §2.7 variantes | règle spécifique |
| AR-DEV-101 | Méthode d'attache et câbles de secours par secteur ou lieu de travail distinct | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-102 | Propane sur le toit limité à une journée de travail; interdiction possible d'entreposer des ma… | interdiction | T | T | T (§1.2), §2.7 variantes | règle par défaut (T) |
| AR-DEV-103 | Tous les déchets évacués de la toiture à la fin de chaque quart; benne à au moins 3 m de toute… | interdiction + fenêtr… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-104 | Passages couverts, filets ou dispositifs vis-à-vis les accès et sorties du bâtiment; périmètre… | préalable | T | T | Phase 3.S, T (§1.2) | règle par défaut (T) |
| AR-DEV-105 | Zone des travaux au sol, manutention et bouillotte clairement barricadées, inaccessibles aux o… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-106 | Autorisation du responsable du site avant d'installer tout appareil émettant gaz ou vapeurs; v… | préalable | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-107 | Documents à transmettre avant le début du montage de charpentes métalliques (procédure de mont… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-108 | Équipements à essence interdits à l'intérieur; autres moteurs à combustion sur autorisation se… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-109 | Mesures de CO et NOx aux 30 minutes dans les locaux adjacents à la zone des travaux si le bâti… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-110 | Suspension des travaux si l'alarme CO/NOx se déclenche | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-111 | Aucun entreposage de carburant à l'intérieur du bâtiment | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-112 | Surveillance du chauffage temporaire hors des heures de travail (soirs et fins de semaine), av… | préalable + fenêtre h… | T | T | T (§1.2), §4 conflits | règle par défaut (T) |
| AR-DEV-113 | Convention avec l'exploitant électrique transmise avant tout travail à proximité de lignes aér… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-114 | Filtres MERV 8 minimum pendant la construction, MERV 13 minimum après construction et avant oc… | préalable | 4, T | 4, T | Phase 4, T (§1.2) | règle spécifique |
| AR-DEV-115 | Plan de gestion de la QAI au plus tard 10 jours après l'octroi; à réviser à chaque changement… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-116 | Approbation du professionnel avant l'achat et l'installation de tout produit liquide côté inté… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-117 | Rencontre avant le début des travaux pour valider le plan QAI | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-118 | Équipements CVCA permanents non mis en fonction pendant la construction; si nécessaire, filtra… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-119 | Conduits scellés au repos et segments non complétés scellés à la fin de chaque journée | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-120 | Dépressurisation des espaces de travail; isolement des aires par scellement des portes/fenêtre… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-121 | Isoler dans le calendrier les activités ayant une incidence sur la QAI; envisager des travaux… | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-122 | Documentation spécifique aux établissements de soins : humidité, particules, COV, polluants ex… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-123 | Interdiction de fumer à l'intérieur et à moins de 9 m d'une ouverture (tabac, cannabis, cigare… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-124 | Plans d'emplacement des cloisons temporaires et compartimentation temporaire à soumettre | préalable | 0 | 0 | Phase 0, §5 validation CISSS | règle spécifique |
| AR-DEV-125 | Calendrier de purge avec chemin critique, intégré au calendrier des travaux | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-126 | Purge en bâtiment occupé : ventilation débutant 3 h avant le matin, maintenue jusqu'à 4 270 14… | fenêtre horaire | 4, T | 4, T | T (§1.2) | règle spécifique |
| AR-DEV-127 | Arrêt des travaux sur avis de non-conformité QAI, sans délai supplémentaire ni ajustement | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-128 | Application du CNPI, dont la section 5.6 sur les chantiers de construction et de démolition | préalable | T | T | T (§1.2) | règle spécifique |
| AR-DEV-129 | Arrêt immédiat des travaux de démolition en cas de découverte d'amiante, de PCB ou de moisissu… | interdiction | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-130 | Sonomètres de classe 1 IEC 61672-1 à enregistrement continu, installés avant le début, dans le… | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-131 | Capteurs de vibration (géophones ou accéléromètres triaxiaux) installés avant le début, sur le… | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-132 | Préséance de la division 01 sur les sections techniques | autre (autre (hiérarc… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-133 | Inspection des travaux antérieurs obligatoire avant d'entreprendre ses propres travaux | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-134 | Accès aux zones de chantier à prévoir depuis le 451, rue Monseigneur-Ross Est, pour toute la d… | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-135 | Rencontre avec la Ville de Chandler avant le début des travaux | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-136 | Accès et dégagements pour véhicules d'urgence aux zones de chantier | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-137 | Signaleurs routiers et signalisation à toutes les barrières d'accès au chantier | préalable | T | T | Phase 0, T (§1.2) | règle par défaut (T) |
| AR-DEV-138 | Voies d'accès et de circulation du site jamais obstruées; accès piétonniers du public et zones… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-139 | Préavis de 3 semaines au propriétaire pour tout déplacement d'une voie d'accès ou de circulati… | préavis | T | T | Phase 3.S, T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-140 | Signaleurs lorsqu'une voie croise ou interfère avec une zone de chantier | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-141 | Mesures d'accès et de circulation intégrées au plan de chantier, validées par le CISSSGA, les… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-142 | Transports hors norme avant 7h00, avec escorte routière sur la rue Monseigneur-Ross Est | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-143 | Installations temporaires accessibles gratuitement aux occupants du site et aux professionnels | autre (autre) | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-144 | Température minimale de 10 °C maintenue là où des travaux sont en cours | préalable + fenêtre h… | T | T | T (§1.2), §4 conflits | règle par défaut (T) |
| AR-DEV-145 | Prévention de l'accumulation de poussière, vapeurs, gaz et buée dans les secteurs demeurant oc… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-146 | Gaz de combustion évacués de manière sûre, sans danger pour les personnes | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-147 | Plan du site, plan d'érosion, programme incendie, plan d'humidité et plan anti-poussière/CVCA… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-148 | Le plan anti-poussière doit indiquer l'emplacement des cloisons pour chaque phase des travaux | préalable | 0 | 0 | Phase 0, §5 validation CISSS | règle spécifique |
| AR-DEV-149 | Essais et inspection de chaque installation temporaire par les autorités avant utilisation | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-150 | Moyens d'évacuation temporaires accessibles conformes au CCQ | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-151 | Escaliers, passerelles, corridors protégés en tube d'acier type conteneur et Jersey pour la ci… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-152 | CVCA permanent utilisable seulement sur permission du propriétaire, avec MERV 8 sur chaque ret… | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-153 | Supports et structures temporaires des réseaux temporaires calculés par ingénieur; durée de vi… | préalable | T | T | Phase 2.N, T (§1.2) | règle spécifique |
| AR-DEV-154 | Matériaux existants retirés pour installer des supports temporaires : à remettre en place aprè… | autre (autre) | 4, T | 4, T | T (§1.2) | règle spécifique |
| AR-DEV-155 | Déplacement et retrait des supports temporaires selon le phasage des travaux | préalable (séquence /… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-156 | Détermination conjointe (fournisseur de services, propriétaire, utilisateurs) du moment d'inte… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-157 | Isolement des zones de travail dans les locaux occupés : débranchement des gaines et pression… | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-158 | Nettoyage quotidien puis final à l'aspirateur HEPA; cloisons anti-poussières maintenues | fenêtre horaire | 4, T | 4, T | T (§1.2) | règle spécifique |
| AR-DEV-159 | Installations de soutien situées à moins de 9 m des bâtiments : non combustibles ASTM E 136, c… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-160 | Enlèvement de la neige et de la glace sur les voies de circulation et les protections temporai… | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-161 | Tous les travaux de levage à la grue planifiés avec le Propriétaire et la municipalité | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-162 | Utilisation d'un ascenseur ou d'un escalier existants : selon les exigences du propriétaire | préalable | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-163 | Moyens d'évacuation temporaires des installations occupées existantes, selon les plans et le C… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-164 | Allée couverte de type conteneur formant tunnel d'évacuation, 2,4 m libre, éclairée selon les… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-165 | Enceinte temporaire étanche aux intempéries à l'extérieur du bâtiment | préalable | T | T | T (§1.2), §4 conflits | règle par défaut (T) |
| AR-DEV-166 | Programme de protection incendie temporaire; interdiction de fumer; examen des besoins avec le… | préalable + interdict… | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-167 | Phase d'exposition : protéger les matériaux poreux; recouvrir ou isoler les ouvertures dans le… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-168 | Matériaux hygroscopiques mouillés plus de 48 h : réputés défectueux; retrait dans les 48 h | interdiction + fenêtr… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-169 | Installations temporaires (enveloppes, chauffage, humidité, ventilation) maintenues en fonctio… | fenêtre horaire | T | T | T (§1.2), §4 conflits | règle par défaut (T) |
| AR-DEV-170 | Passage des installations temporaires de sécurité aux installations permanentes interdit avant… | interdiction | 4 | 4 | Phase 4, préambule / vue d'ensemble, §4 conflits | règle spécifique |
| AR-DEV-171 | Plan de situation de la zone clôturée, roulottes, voies d'accès et détails de clôture à prépar… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-172 | Choix du type d'échafaudage tenant compte de l'utilisation du bâtiment par les usagers et le p… | préalable | 0 | 0 | Phase 0, Phase 2 | règle spécifique |
| AR-DEV-173 | Autorisation du représentant du CISSSGA au moins 48 h avant l'installation de grues, ascenseur… | préalable + préavis | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-174 | Ascenseurs existants utilisables seulement après approbation du service technique du CISSSGA,… | préalable | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-175 | Interdiction de surcharger l'ouvrage existant | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-176 | Stationnement interdit sur le chantier; vignettes obligatoires auprès de l'hôpital; réglementa… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-177 | Entretien et déneigement des accès existants utilisés pour accéder au chantier et au stationne… | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-178 | Surveillance du chantier après les heures de travail, les jours de congé et les périodes de va… | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-179 | Barricades, couloirs et escaliers pour permettre aux usagers et au personnel d'accéder au bâti… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-180 | Bureau de chantier hors de l'enceinte contrôlée; aménagement possible dans le stationnement ét… | autre (autre) | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-181 | Roulotte des représentants fournie et raccordée dans les 30 jours suivant l'adjudication; 3 pl… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-182 | Interdiction d'utiliser les services sanitaires des bâtiments de l'hôpital | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-183 | Panneau de chantier installé dans les 3 semaines suivant la signature du contrat, à l'endroit… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-184 | Aucun autre panneau ni affiche que les panneaux d'avertissement | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-185 | Maintien et protection de la circulation durant les travaux, sauf indication contraire du CISS… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-186 | Éclairage assurant une visibilité complète pendant les quarts de soir et de nuit | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-187 | Enlèvement de la neige pendant la période des travaux; emplacement et tracé des voies soumis à… | préalable | T | T | Phase 0, T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-188 | Évacuation quotidienne des débris, déchets et emballages | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-189 | Palissade de 1,8 m combinée à des glissières Jersey et munie d'une toile anti-poussière | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-190 | Barrières d'accès verrouillables selon l'aménagement du site ET selon les phasages | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-191 | Passages abrités pour piétons (toit et côtés) avec signalisation et éclairage | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-192 | Écrans pare-poussière ou cloisons isolées pour toute activité génératrice de poussière, mainte… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-193 | Déneigement automne-hiver-printemps pour assurer la libre circulation dans la zone du chantier | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-194 | Accès et dégagements en hauteur pour véhicules d'urgence | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-195 | Déneigement pour l'escalier d'issue temporaire et permanent; renvoi à 05 51 00 | préalable | 3.N, T | B.1.2, T | Phase 3.N, Phase B-B, T (§1.2), §4 conflits | règle spécifique |
| AR-DEV-196 | Cloisons de confinement illustrées aux plans à titre indicatif seulement; l'entrepreneur doit… | autre (autre (portée)) | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-197 | Plan de sécurité incendie approuvé par le CISSSGA, l'Établissement et le service incendie de l… | préalable | 0 | 0 | Phase 0, Phase 3.S, §5 validation CISSS | règle spécifique |
| AR-DEV-198 | Aucune non-conformité induite dans les secteurs occupés : corridors 1650 mm / 2400 mm, hauteur… | interdiction | T | T | Phase 3.N, T (§1.2), §4 conflits | règle par défaut (T) |
| AR-DEV-199 | Zones de travaux isolées des secteurs occupés par une séparation coupe-feu 1 h continue jusqu'… | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-200 | Mesures supplétives à obtenir auprès de la RBQ, du service incendie et du service de sécurité… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-201 | La procédure clinique PCI du CISSSGA et le tableau des contraintes opérationnelles ont préséan… | autre (autre (hiérarc… | T | T | T (§1.2) | règle spécifique |
| AR-DEV-202 | L'échéancier doit tenir compte des délais PCI, notamment le nettoyage quotidien et celui avant… | préalable (séquence /… | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-203 | Approbation préalable de la méthodologie, des techniques, de l'implantation et des équipements… | préalable | 0, T | 0, T | Phase 0, T (§1.2), §5 validation CISSS | règle spécifique |
| AR-DEV-204 | Les travaux de construction ou de démolition ne peuvent débuter qu'après approbation de la pré… | préalable + interdict… | T | T | Phase 1, Phase B-A, T (§1.2), §1.3 étapes types, §5 validation CISSS | règle par défaut (T) |
| AR-DEV-205 | Un seul avis écrit; 2e inspection; à défaut, firme externe aux frais de l'entrepreneur | interdiction | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-206 | Suspension immédiate des travaux sur simple avis en cas de défaillance des mesures de préventi… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-207 | Agent de sécurité ou firme formée PCI affecté à temps complet si l'entrepreneur néglige les me… | autre (autre) | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-208 | Vêtements propres ou survêtement jetable (TYVEK) obligatoire pour circuler à l'intérieur du bâ… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-209 | Itinéraire de circulation intérieur imposé, approuvé par le chef de projet et l'équipe PCI; ac… | préalable + interdict… | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-210 | Dépoussiérage des chaussures, mains, visage et cheveux à chaque sortie vers le bâtiment occupé… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-211 | Enceintes de protection érigées avant tout travail de démolition ou de construction à l'intéri… | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-212 | Scellement des grilles de ventilation et des puits de mécanique à la satisfaction du propriéta… | préalable | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-213 | Pression négative : 4 changements d'air/h, différentiel minimal de 7,5 Pa entre chantier et zo… | préalable | T | T | Phase 1, T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-214 | Certification des unités de ventilation datée de moins de 12 mois; certification obligatoire A… | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-215 | Unités de ventilation branchées sur l'alimentation d'urgence lorsque possible | préalable | T | T | T (§1.2), matrice ME | règle par défaut (T) |
| AR-DEV-216 | Évacuation de l'air HEPA prioritairement vers l'extérieur, loin des prises d'air, avec protect… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-217 | Filtres HEPA et conduits flexibles neufs, inspectés et approuvés par l'équipe de prévention av… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-218 | Recirculation d'air autorisée seulement pour les clientèles des groupes 1 et 2; approbation pr… | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-219 | Manomètre visible à l'entrée du chantier; prises de mesure à au moins 5 m de l'accès | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-220 | Manomètre à enregistrement continu avec alarme reliée à un poste de contrôle pour certains sec… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-221 | Arrêt possible de l'unité de ventilation pendant les fermetures prolongées, après accord du ch… | préalable + fenêtre h… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-222 | Filtration HEPA maintenue en fonction en fin de travaux le temps d'éliminer 99,9 % des contami… | fenêtre horaire | 4, T | 4, T | T (§1.2) | règle spécifique |
| AR-DEV-223 | Mesures correctives immédiates si <7,5 Pa pendant plus de 4 h par 24 h, ou <2,5 Pa pendant plu… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-224 | Tapis collants : 1 pour les chantiers de type II, 2 par antichambre pour les types III et IV;… | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-225 | Fermeture de la zone des travaux en coordination avec le chef de projet avant de débuter | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-226 | Collaboration obligatoire en tout temps avec le service PCI de l'établissement | autre (autre) | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-227 | Tente mobile (CTM) : usage limité aux travaux de très courte durée, plafonds et entreplafonds;… | interdiction + fenêtr… | T | T | Phase 1, T (§1.2) | règle par défaut (T) |
| AR-DEV-228 | Cloison souple (CST) : très courte durée seulement, avec approbation préalable; requise pour i… | préalable + préalable… | T | T | Phase 1, T (§1.2) | règle par défaut (T) |
| AR-DEV-229 | Cloison fixe temporaire (CFT) : construite de dalle à dalle, séparation coupe-feu 1 h, portes/… | préalable | T | T | Phase 1, T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-230 | 100 m² supplémentaires de cloisons fixes temporaires CFT à prévoir en sus des quantités aux pl… | autre (autre (quantit… | T | T | Phase 1, T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-231 | Composition normalisée de la cloison CFT : 2 gypses 16 mm, colombages 92 mm (ou CH 102 mm), la… | préalable | T | T | Phase 1, T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-232 | Sas à deux portes de 915 mm avec barrure, ferme-porte et joints étanches; distance assurant qu… | préalable + interdict… | T | T | Phase 1, T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-233 | Enceintes prolongées au-dessus des plafonds finis jusqu'à la dalle structurale, avec scellemen… | préalable | T | T | Phase 1, T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-234 | Cloisons existantes temporaires (CET) : résistance au feu de 1 h; montant 92 mm et deux gypses… | préalable | T | T | Phase 1, T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-235 | Nettoyage des lieux, des sas et des abords à la fin de chaque journée de travail, à la satisfa… | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-236 | Nettoyage HEPA et linge germicide de tous les conduits électromécaniques après chaque interven… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-237 | Aspirateurs HEPA certifiés obligatoires, soumis à l'approbation du chef de projet avant utilis… | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-238 | Débris de démolition évacués à la fin de chaque journée ET à l'extérieur des heures de grands… | fenêtre horaire | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-239 | Tout matériel sorti via l'intérieur du bâtiment occupé doit être nettoyé ou emballé de façon é… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-240 | Cheminement des rebuts et extrants établi par le propriétaire pour chacune des étapes/phases d… | interdiction + préala… | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-DEV-241 | Rebuts évacués dans des contenants roulants étanches recouverts de polyéthylène scellé; conten… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-242 | Bennes à déchets maintenues fermées en tout temps; chute à déchets étanche au raccord avec la… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-243 | Séquence obligatoire de fin de travaux : fermeture des plafonds → nettoyage en profondeur → HE… | préalable + préalable… | 4, T | 4, T | Phase 4, T (§1.2), préambule / vue d'ensemble, §1.3 étapes types | règle spécifique |
| AR-DEV-244 | Reprise complète du nettoyage si insatisfaisant ou si les analyses d'air révèlent un niveau de… | interdiction | 4, T | 4, T | Phase 4, T (§1.2), §1.3 étapes types | règle spécifique |
| AR-DEV-245 | Démantèlement des enceintes seulement après approbation du nettoyage par le chef de projet et… | préalable + interdict… | 4, T | 4, T | Phase 1, Phase 4, T (§1.2), préambule / vue d'ensemble, §1.3 étapes types, §5 validation CISSS | règle spécifique |
| AR-DEV-246 | Interdiction de surcharger le bâtiment; autorisation écrite avant de découper ou percer un élé… | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-247 | Raccordements aux réseaux existants exécutés aux heures fixées par les autorités, en gênant le… | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-248 | Demande écrite préalable, avec date et heure, avant tout découpage/ragréage affectant l'intégr… | préalable + préavis | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-249 | Interdiction d'utiliser des outils pneumatiques ou à percussion sur la maçonnerie sans autoris… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-250 | Obturation complète et coupe-feu de toutes les traversées de murs, plafonds ou planchers coupe… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-251 | Voies d'accès au bâtiment maintenues exemptes de glace et de neige | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-252 | Nettoyage quotidien des aires occupées souillées, immédiatement après les travaux, pour ne pas… | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-253 | Interdiction d'utiliser le système de ventilation du bâtiment pour aérer lors de l'emploi de s… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-254 | Horaire de nettoyage établi pour que la poussière ne retombe pas sur les systèmes mécaniques | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-255 | Nettoyage final incluant les conduits de mécanique en entreplafond et le remplacement des filt… | préalable | 4 | 4 | Phase 4 | règle spécifique |
| AR-DEV-256 | Plan de gestion des déchets de construction préparé avant le début des travaux; cible de détou… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-257 | Certificat de réception avec réserves retenu tant que les documents de gestion des déchets ne… | préalable | 4 | 4 | Phase 4 | règle spécifique |
| AR-DEV-258 | Coordonnateur à la gestion des déchets présent en permanence sur le chantier | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-259 | Centre de tri reconnu RECYC-QUÉBEC participant au programme avant le démarrage et jusqu'à la r… | préalable | 0, 4, T | 0, 4, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-260 | Interdictions absolues : enfouir, déverser, brûler ou incinérer des déchets; réinstaller des i… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-261 | Exécuter les travaux en nuisant le moins possible à l'utilisation normale des lieux | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-262 | Rencontre préalable avec le représentant du CISSSGA et le professionnel pour revoir le plan et… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-263 | Plan de gestion des déchets sur le chantier incluant les techniques, la séquence et le calendr… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-264 | Coordination de la gestion des déchets de démolition avec les autres activités pour un déroule… | préalable (séquence /… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-265 | Manuels d'exploitation et d'entretien définitifs en français 2 semaines avant la réception ave… | préavis | 4 | 4 | Phase 4 | règle spécifique |
| AR-DEV-266 | Consignation des conditions au fur et à mesure; interdiction de dissimuler un ouvrage avant co… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-267 | Agent de mise en service indépendant, rémunéré par l'entrepreneur général | préalable | 0, 4 | 0, 4 | Phase 0 | règle spécifique |
| AR-DEV-268 | Certificat de réception provisoire émis seulement après réception, évaluation et approbation d… | préalable | 4 | 4 | Phase 4 | règle spécifique |
| AR-DEV-269 | Examen préalable avant le début des travaux de construction : confirmer par écrit la conformit… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-270 | Nom de l'agent de mise en service et calendrier préliminaire au plus tard 4 semaines après l'a… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-271 | Demandes de changement et procédures proposées approuvées par écrit au moins 8 semaines avant… | préavis | 4 | 4 | Phase 4 | règle spécifique |
| AR-DEV-272 | Calendrier de mise en service détaillé selon la méthode du chemin critique, soumis en même tem… | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-273 | Réunion distincte sur la portée de la mise en service lorsque les travaux sont achevés à 60 % | préalable | T | T | Phase 4, T (§1.2) | règle spécifique |
| AR-DEV-274 | Préavis de 14 jours avant la mise en route et les essais | préavis | 4 | 4 | Phase 4, §5 validation CISSS | règle spécifique |
| AR-DEV-275 | Correction des anomalies après chaque phase, avant le début de la phase suivante, avec approba… | interdiction + préala… | T | T | Phase 4, T (§1.2), diagramme, préambule / vue d'ensemble, §1.3 étapes types | règle par défaut (T) |
| AR-DEV-276 | Préavis de 21 jours avant le début de la mise en service; mise en service subordonnée à l'achè… | interdiction + préavis | 4 | 4 | Phase 4, §5 validation CISSS | règle spécifique |
| AR-DEV-277 | Mise en service des équipements sensibles à l'occupation et aux variations saisonnières à réal… | préalable + fenêtre h… | 4 | 4 | Phase 4 | règle spécifique |
| AR-DEV-278 | Arrêt immédiat des travaux si découverte d'amiante ou d'une substance désignée; reprise seulem… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-279 | Matériaux friables et dispersables : méthode particulière et mise en sac rapide | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-280 | Démolitions ne doivent pas obstruer l'évacuation des eaux ni les systèmes électriques et mécan… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-281 | Démolitions ne doivent pas générer de niveaux excessifs de pollution atmosphérique ou acoustiq… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-282 | Enceintes de protection temporaires durant la démolition pour empêcher la contamination de l'a… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-283 | Recouvrement ou abattage par voie humide des matières sèches; abat-poussière sur toutes les vo… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-284 | Plan détaillé de l'ordre de démontage et des travaux d'étaiement à soumettre avant d'entrepren… | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| AR-DEV-285 | Restrictions de bruit, de poussière, d'interférences, d'obstructions et d'heures de travail dé… | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-286 | Tous les travaux exécutés selon un échéancier préétabli et approuvé par le CISSSGA et les prof… | préalable | 0, T | 0, T | Phase 0, T (§1.2), §5 validation CISSS | règle spécifique |
| AR-DEV-287 | Ne pas nuire ni interrompre les opérations des zones adjacentes de l'Établissement | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-288 | Dynamitage interdit | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-289 | Débranchements selon les directives du professionnel; interdiction de couper ou briser les can… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-290 | Mesures pour limiter le bruit et la poussière dans les bâtiments adjacents occupés | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-291 | Ouvrage sûr et stable à la fin de chaque journée de travail | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-292 | Démolition en soulevant le moins de poussière possible; matériaux gardés mouillés; maintien de… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-293 | Matières contaminées ou dangereuses évacuées avant d'entreprendre les travaux de démolition | préalable + préalable… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-294 | Travaux à la lumière du jour aussi souvent que possible; extinction de l'éclairage en fin de j… | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-295 | Nettoyage quotidien pour assurer la sécurité des usagers; aucun débris, outil, matériau ou équ… | interdiction + fenêtr… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-296 | Interdiction des outils à percussion à proximité des murs existants à conserver; trait de scie… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-297 | Prélèvement préalable par le propriétaire des éléments à récupérer; bâtiment pris tel que livr… | préalable + préalable… | 0 | 0 | Phase 0 | règle spécifique |
| AR-DEV-298 | Remise en état des surfaces et bâtiments contigus; clôtures existantes et clôture de chantier… | préalable | 4 | 4 | Phase 4 | règle spécifique |
| AR-DEV-299 | Fiches signalétiques SIMDUT soumises avant d'introduire toute matière dangereuse sur le chanti… | préalable | T | T | T (§1.2) | règle spécifique |
| AR-DEV-300 | Maximum de 45 L de liquides inflammables ou combustibles sur le chantier sans approbation | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-301 | Transvasement de liquides inflammables interdit à l'intérieur des bâtiments et près d'une flam… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-302 | Déversement ou accident signalé immédiatement, rapport écrit dans les 24 h | préavis | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-303 | Échantillon d'ouvrage de maçonnerie : 48 h d'inspection avant d'entamer les travaux | préavis | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-304 | Maçonnerie par temps froid : ambiance 5-50 °C, maçonnerie hors gel, préchauffage des sections… | préalable + fenêtre h… | T | T | T (§1.2), §4 conflits | règle spécifique |
| AR-DEV-305 | Vaporisation du mortier pendant au moins 3 jours après la mise en œuvre; contreventement jusqu… | préalable + préalable… | T | T | T (§1.2) | règle spécifique |
| AR-DEV-306 | Étaiement temporaire de la maçonnerie maintenu; poussières de refouillement et sciage confinée… | préalable | T | T | T (§1.2) | règle spécifique |
| AR-DEV-307 | Armatures de maçonnerie : soumission au moins 5 semaines avant la mise en place | préavis | T | T | T (§1.2) | règle spécifique |
| AR-DEV-308 | Mortier et coulis : avis de 24 h à l'organisme d'essais avant la mise en place | préavis | T | T | T (§1.2) | règle spécifique |
| AR-DEV-309 | Conditions ambiantes des mortiers : 10 °C min. et 32 °C max. avant, pendant et 48 h après les… | préalable + fenêtre h… | T | T | T (§1.2) | règle spécifique |
| AR-DEV-310 | Contreventement temporaire de l'ossature à poteaux métalliques maintenu tant qu'il assure la s… | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-311 | Escaliers temporaires : éléments modulaires préfabriqués incombustibles, résistant à l'indice… | préalable | 3.N, T | B.1.2, T | Phase 3.N, Phase B-B, T (§1.2), §2.7 variantes, §4 conflits | règle spécifique |
| AR-DEV-312 | Visites de chantier du fabricant-installateur d'escaliers aux étapes 0 %, 25 %, 60 % et fin; r… | préalable | 3.N, T | B.1.2, T | Phase 3.N, Phase B-B, T (§1.2) | règle spécifique |
| AR-DEV-313 | Ébénisterie : humidité relative maintenue entre 25 % et 60 % | préalable | T | T | T (§1.2) | règle spécifique |
| AR-DEV-314 | Isolants : nettoyage à l'aspirateur HEPA et évacuation des poussières dans des contenants étan… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-315 | Réunion préalable obligatoire au moins une semaine avant le début des travaux de pare-air, ave… | préalable | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-316 | Pare-air : surfaces sèches et température supérieure à -10 °C; attendre au moins 24 h après de… | préalable + fenêtre h… | T | T | T (§1.2), §1.3 étapes types, §4 conflits | règle par défaut (T) |
| AR-DEV-317 | Pare-air : membrane d'hiver spécifiquement prescrite; température d'installation 5 °C à 40 °C | préalable + fenêtre h… | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-318 | Essais d'étanchéité in situ du pare-air par un laboratoire indépendant, gérés et financés par… | autre (autre) | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-319 | Compartimentation des cavités murales : profilés continus, espacement maximal 3 m verticalemen… | préalable | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-DEV-320 | Couverture : interdiction de poser à moins de 18 °C (bitume chaud) ou 10 °C (membranes soudées… | interdiction + fenêtr… | T | T | T (§1.2), §1.3 étapes types, §4 conflits | règle spécifique |
| AR-DEV-321 | Support de couverture sec, exempt de neige et de glace; usage de sel et de calcium interdit | interdiction + fenêtr… | T | T | T (§1.2), §1.3 étapes types | règle spécifique |
| AR-DEV-322 | Inspection de couverture par une firme indépendante accréditée AMCQ, payée par le CISSSGA, à p… | préalable | T | T | T (§1.2), §1.3 étapes types | règle spécifique |
| AR-DEV-323 | Continuité parfaite exigée dans l'exécution des travaux de couverture | préalable (séquence /… | T | T | T (§1.2), §1.3 étapes types | règle spécifique |
| AR-DEV-324 | Agent de sécurité incendie présent 1 h après la fin de la journée de travail | fenêtre horaire | T | T | T (§1.2), §1.3 étapes types | règle spécifique |
| AR-DEV-325 | Surveillant formé maintenu au moins 2 h après les travaux de soudure, rondes aux 15 minutes, p… | fenêtre horaire | T | T | T (§1.2), §1.3 étapes types | règle spécifique |
| AR-DEV-326 | Extincteur par utilisateur de chalumeau, à moins de 6 m | préalable | T | T | T (§1.2), §1.3 étapes types | règle spécifique |
| AR-DEV-327 | Évacuation de l'eau de pluie le plus loin possible de la façade du bâtiment | préalable | T | T | T (§1.2), §1.3 étapes types | règle spécifique |
| AR-DEV-328 | Protection à la fin de chaque journée ou lors d'interruption pour mauvais temps; scellements e… | fenêtre horaire | T | T | T (§1.2), §1.3 étapes types | règle spécifique |
| AR-DEV-329 | Solins : entreposage à l'abri du gel; application à la truelle au-dessus de 2 °C; support sec… | préalable + fenêtre h… | T | T | T (§1.2), §1.3 étapes types | règle spécifique |
| AR-DEV-330 | Avis au professionnel et attente de 72 h avant de dissimuler ou sceller les matériaux coupe-fe… | interdiction + préavis | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-331 | Ensembles coupe-feu exigés à la rencontre des cloisons résistantes au feu avec les murs extéri… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-332 | Visites du fabricant coupe-feu aux étapes 0 %, 25 %, 60 % et fin; rapports dans les 3 jours | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-333 | Scellants : certificat du fabricant avant le début; essais transmis au plus tard 7 jours avant… | préavis | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-334 | Attente de 48 h avant d'entreprendre les travaux d'étanchéification | fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-335 | Produits toxiques : usage restreint aux endroits évacués vers l'extérieur ou confinés, ou appl… | interdiction + préala… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-336 | Précautions pour ne pas endommager les surfaces existantes lors des reprises de joints | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-337 | Volets coupe-feu : homologation CAN/ULC-S104/S105, fabrication et installation conformes à NFP… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-338 | Murs-rideaux et fenêtres : détail d'assemblage avec la fenêtre existante exigé aux dessins d'a… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-339 | Murs-rideaux et fenêtres : inspection sans préavis et en tout temps des matériaux et de la mai… | autre (autre) | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-340 | Essais d'étanchéité in situ des murs-rideaux et fenêtres réalisés par un laboratoire indépenda… | autre (autre) | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-341 | Acier intérieur dissimulé peint à haute teneur en zinc; acier exposé placé du côté froid en hi… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-342 | Tenir compte des conditions climatiques existantes au moment de l'installation (dilatation/con… | préalable + fenêtre h… | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-343 | Vitrages : température minimale à obtenir avant le début des travaux et maintenue 24 h après | préalable + fenêtre h… | T | T | T (§1.2), §4 conflits | règle par défaut (T) |
| AR-DEV-344 | Vitrages entreposés couverts temporairement de façon non hermétique pour permettre l'aération;… | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-345 | Plaques de plâtre : revêtement à deux rangs du côté corridor lorsque trois rangs au total; pro… | préalable | T | T | T (§1.2) | règle spécifique |
| AR-DEV-346 | Puits fermés en partie supérieure par une séparation coupe-feu de résistance égale à celle des… | préalable | T | T | T (§1.2) | règle spécifique |
| AR-DEV-347 | Peinturage : ventilation adéquate et continue vérifiée; 10 °C au moins 24 h avant le début, ma… | préalable + interdict… | T | T | T (§1.2) | règle spécifique |
| AR-DEV-348 | Éclairement minimal de 323 lux vérifié avant de commencer la peinture | préalable | T | T | T (§1.2) | règle spécifique |
| AR-DEV-349 | Enlèvement des plaques-couvercles du matériel électrique avant le début des travaux de peinture | préalable | T | T | T (§1.2) | règle spécifique |
| AR-DEV-350 | Toiles solaires : toutes les mesures prises sur place avant fabrication; installateur certifié… | préalable | T | T | Phase B-A, T (§1.2) | règle par défaut (T) |
| AR-DEV-351 | Clôtures : aucune coupe permise au chantier (aucune coupe après galvanisation ou peinture) | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-DEV-352 | Clôtures : récupération et réinstallation du barbelé existant; assemblage aux poteaux existants | préalable (séquence /… | 3.N, 4 | 4, B.1.2 | Phase 3.N, Phase 4, Phase B-B, §6 NA | règle spécifique |
| AR-DEV-353 | Échantillon d'ouvrage de clôture (3 m par type) : 72 h d'examen; aucun travail ne peut débuter… | préalable + préavis | T | T | T (§1.2) | règle spécifique |
| AR-PLN-001 | Accès pompier à la borne-fontaine en tout temps | interdiction | T | T | T (§1.2) | règle spécifique |
| AR-PLN-002 | Case de stationnement réservée à l'entrepreneur | autre (autre (install… | 0 | 0 | Phase 0 | règle spécifique |
| AR-PLN-003 | Débarcadère de l'entrepreneur à coordonner | préalable + préalable… | 0 | 0 | Phase 0, §5 validation CISSS | règle spécifique |
| AR-PLN-004 | Chemin d'accès temporaire en gravier, remise en état | autre (autre (aménage… | 3.S, 4 | 4, A.1 | Phase 3.N, Phase 3.S, Phase 4, Phase B-A, §6 NA | règle spécifique |
| AR-PLN-005 | Clôturage de la zone de chantier | autre (autre) | 0 | 0 | Phase 0 | règle spécifique |
| AR-PLN-006 | Issue extérieure et chemin d'évacuation maintenus, largeur libre 1650 mm | interdiction | T | T | T (§1.2), §2.7 variantes, §4 conflits | règle par défaut (T) |
| AR-PLN-007 | Portes extérieures mises hors service | interdiction | T | T | T (§1.2), §2.7 variantes, §4 conflits | règle par défaut (T) |
| AR-PLN-008 | Marquise et pourtour des portes : coordination et plan d'action d'évacuation | préalable + préalable… | 3.S | A.1 | Phase 3.S, Phase B-A, §5 validation CISSS | règle spécifique |
| AR-PLN-009 | Zone IRM : interdiction de métal quand l'IRM est en service | interdiction | 1 | A | Phase 1, Phase B-A | règle spécifique |
| AR-PLN-010 | Porte IRM : coordination de service | préalable (séquence /… | 1 | A | Phase 1, Phase B-A, §5 validation CISSS | règle spécifique |
| AR-PLN-011 | Plan d'action requis AVANT tout travail près d'une porte d'issue | préalable | T | T | Phase 3.N, Phase B-B, T (§1.2), §1.3 étapes types, §2.7 variantes, §4 conflits | règle par défaut (T) |
| AR-PLN-012 | Gestion des flux entrepreneur / clientèle | préalable (séquence /… | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| AR-PLN-013 | Précautions sur câblage électrique souterrain lors de l'excavation du nouvel escalier | interdiction | 3.N | B.1.2 | Phase 3.N, Phase B-B, §2.7 variantes | règle spécifique |
| AR-PLN-014 | Signalisation temporaire d'entrée d'ambulance, un panneau par phase | préalable + préalable… | 3.S | A.1 | Phase 3.N, Phase 3.S, Phase B-A, §6 NA | règle spécifique |
| AR-PLN-015 | Piste cyclable : coordination avec l'établissement ET la ville | préalable (séquence /… | 0 | 0 | Phase 0, §5 validation CISSS | règle spécifique |
| AR-PLN-016 | Protection des issues et accès au bâtiment durant le chantier | autre (autre (protect… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-017 | Protection des portes de garage / accès | autre (autre (protect… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-018 | Phasage de la zone ambulance en 2 configurations | autre (phasage illust… | 3.S | A.1 | Phase 3.N, Phase 3.S, Phase B-A, §5 validation CISSS, §6 NA | règle spécifique |
| AR-PLN-019 | Phasage de l'entrée principale en 3 configurations | autre (phasage illust… | 3.S | A.1 | Phase 3.S, Phase B-A, §5 validation CISSS | règle spécifique |
| AR-PLN-020 | Gestion d'évacuation illustrée | autre (gestion illust… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-021 | Gestion de la zone IRM illustrée (unité mobile) | autre (gestion illust… | 1 | A | Phase 1, Phase B-A, §5 validation CISSS | règle spécifique |
| AR-PLN-022 | Séquençage électromécanique à lire dans le « Tableau de coordination » | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-PLN-023 | Divergences à signaler AVANT les travaux | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-PLN-024 | Vérification des conditions existantes avant exécution | préalable | 0 | 0 | Phase 0 | règle spécifique |
| AR-PLN-025 | Amiante : arrêt et avis au professionnel | préalable + interdict… | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-PLN-026 | Continuité et intégrité des séparations coupe-feu | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-027 | Protection contre intempéries, humidité, infiltrations | autre (autre (protect… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-028 | Bruit : méthodes les moins bruyantes près des installations existantes | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-029 | Poussière : chutes à déchets et conteneurs étanches | autre (autre (protect… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-030 | Démontage des parures de fenêtres et remise au propriétaire | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-031 | Persiennes à repeindre AVANT réinstallation | préalable | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-PLN-032 | Humidité / moisissure découverte : remplacer AVANT de poursuivre | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-033 | Rouille découverte : traitement avant poursuite | autre (autre) | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-034 | Éléments fixés sur cloisons à démolir : retirer et remettre au propriétaire | préalable | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-035 | Équipements non déplaçables : protection + coordination des retraits temporaires | préalable + préalable… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-036 | Voies de circulation protégées sur les toitures, maintenues jusqu'à la fin | préalable + interdict… | T | T | T (§1.2), §2.7 variantes | règle spécifique |
| AR-PLN-037 | Séquence de travaux des fenêtres renvoyée aux coupes et détails types | préalable (séquence /… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-038 | Portée d'une note spécifique délimitée par les repères « limite des travaux » | autre (autre (règle d… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-039 | Renvoi obligatoire à la feuille 002 pour le maintien des issues (toutes les feuilles de portes) | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-040 | Fenêtres existantes maintenues jusqu'à la fin des travaux extérieurs | préalable + préalable… | T | T | Phase B-A, Phase B-B, Phase B-C, T (§1.2), diagramme, préambule / vue d'ensemble, §1.3 étapes types, §4 conflits | règle par défaut (T) |
| AR-PLN-041 | Plexiglas installé et scellé dès le retrait de la fenêtre | préalable (séquence /… | T | T | Phase 1, Phase B-A, T (§1.2), préambule / vue d'ensemble, §1.3 étapes types | règle par défaut (T) |
| AR-PLN-042 | Contrainte saisonnière : bâti isolé au lieu du plexiglas de novembre à avril | fenêtre horaire | T | T | Phase B-A, T (§1.2), préambule / vue d'ensemble, §1.3 étapes types, §4 conflits | règle par défaut (T) |
| AR-PLN-043 | Finition intérieure maintenue jusqu'à fin des travaux extérieurs | préalable + préalable… | T | T | T (§1.2), préambule / vue d'ensemble, §1.3 étapes types | règle par défaut (T) |
| AR-PLN-044 | Thermos et finition posés le même jour que le retrait du plexiglas | fenêtre horaire | T | T | Phase B-A, Phase B-B, T (§1.2), diagramme, préambule / vue d'ensemble, §1.3 étapes types | règle par défaut (T) |
| AR-PLN-045 | Toile solaire retirée et remise au propriétaire | autre (autre) | T | T | Phase B-A, T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-PLN-046 | Tour : remplacement des fenêtres en 2 étapes (ext. puis int.) | préalable (séquence /… | 2 | C | Phase 2, Phase 2.O, Phase B-A, Phase B-C, préambule / vue d'ensemble, §1.3 étapes types | règle spécifique |
| AR-PLN-047 | Basilaire RDC (blocs de béton, hors IRM) : 3 étapes | préalable (séquence /… | 1, 3 | A | Phase 1, Phase B-A, préambule / vue d'ensemble, §1.3 étapes types | règle spécifique |
| AR-PLN-048 | Basilaire colombages (IRM et niv. 100) : 2 étapes | préalable (séquence /… | 1, 3 | A, B | Phase 1, Phase B-A, Phase B-B, préambule / vue d'ensemble, §1.3 étapes types | règle spécifique |
| AR-PLN-049 | Fenêtres exclues du principe en 2 étapes | interdiction | T | T | Phase 1, T (§1.2), préambule / vue d'ensemble | règle par défaut (T) |
| AR-PLN-050 | Prototype obligatoire en présence de l'architecte | préalable + interdict… | 1 | A, B, C | Phase 0, Phase 1, Phase B-A, Phase B-B, Phase B-C, diagramme, préambule / vue d'ensemble, §2.7 variantes, §6 NA | règle spécifique |
| AR-PLN-051 | Essais in situ par firme externe, en cours de travaux | préalable + interdict… | 1 | A, B, C | Phase 1, Phase B-A, Phase B-B, Phase B-C, préambule / vue d'ensemble, §1.3 étapes types, §6 NA | règle spécifique |
| AR-PLN-052 | Séparation coupe-feu en gypse existante à démolir (entretoit) | autre (autre) | T | T | T (§1.2) | règle spécifique |
| AR-PLN-053 | Percement de toiture 915 x 915 mm pour accéder à la compartimentation | préalable | T | T | T (§1.2) | règle spécifique |
| AR-PLN-054 | Nouvelle compartimentation dans l'entretoit | autre (autre) | T | T | T (§1.2) | règle spécifique |
| AR-PLN-055 | Compléter la séparation coupe-feu existante | autre (autre) | T | T | T (§1.2) | règle spécifique |
| AR-PLN-056 | Ajout de volets coupe-feu (sous-sol) | autre (autre) | NA | B | Phase B-B, matrice ME, §6 NA | règle spécifique |
| AR-PLN-057 | Nouveaux volets coupe-feu (RC, niv. 100, 200-400) | autre (autre) | 1, 2, 3 | A, B, C | Phase 1, Phase 2, Phase 2.O, Phase B-A, Phase B-B, Phase B-C, matrice ME | règle spécifique |
| AR-PLN-058 | Démantèlement partiel du plafond suspendu pour pose du volet coupe-feu | préalable | 1, 3.S | A, B | Phase 1, Phase 3.S, Phase B-A, Phase B-B | règle spécifique |
| AR-PLN-059 | Tuiles de plafond retirées temporairement pour travaux de mécanique | préalable (séquence /… | T | T | Phase 1, T (§1.2) | règle par défaut (T) |
| AR-PLN-060 | Tuiles avec gicleur : conserver et protéger | interdiction | T | T | Phase 1, T (§1.2) | règle par défaut (T) |
| AR-PLN-061 | Ouverture dans mur existant en entreplafond pour les travaux de structure | préalable + préalable… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-062 | Démolition ponctuelle de maçonnerie pour travaux de structure | préalable + préalable… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-063 | Bande de toiture à démolir pour travaux de structure | préalable + préalable… | T | T | Phase 1, T (§1.2), §1.3 étapes types, §2.7 variantes | règle par défaut (T) |
| AR-PLN-064 | Nouvel escalier d'issue | autre (autre) | 3.N | B.1.2 | Phase 3.N, Phase B-B | règle spécifique |
| AR-PLN-065 | Compartimentation verticale de l'enveloppe | autre (autre) | T | T | Phase 1, T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-PLN-066 | Tôle de compartimentation continue sur la hauteur de l'étage | autre (autre) | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-PLN-067 | Échelles démontées, à protéger, réinstallées après modification | préalable (séquence /… | T | T | T (§1.2) | règle spécifique |
| AR-PLN-068 | Échelle existante à démonter/entreposer, interventions AVANT réinstallation | préalable | T | T | T (§1.2) | règle spécifique |
| AR-PLN-069 | Percements étanchés après retrait des garde-corps | préalable (séquence /… | T | T | T (§1.2) | règle spécifique |
| AR-PLN-070 | Unité de mécanique démantelée temporairement | préalable (séquence /… | 3.S | A | Phase 3.S, Phase B-A | règle spécifique (complément §10) |
| AR-PLN-071 | Plexiglas de protection à enlever — secteur psychiatrie uniquement | autre (autre (portée… | 2 | C.4 | Phase 2, Phase 2.O, Phase B-C | règle spécifique |
| AR-PLN-072 | Garde-corps existant à conserver et protéger | interdiction | 1, 3 | B | Phase 1, Phase B-B | règle spécifique |
| AR-PLN-073 | Éléments existants du site à conserver et protéger (série) | autre (autre (protect… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-074 | Protection des plantations et remise en état | autre (autre) | 4, T | 4, T | Phase 4, T (§1.2) | règle spécifique |
| AR-PLN-075 | Revêtement de plancher existant à conserver et protéger | autre (autre (protect… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-076 | Réinstallation du plafond suspendu après travaux de mécanique | préalable (séquence /… | T | T | Phase 1, T (§1.2) | règle par défaut (T) |
| AR-PLN-077 | Nouveau plafond suspendu : trame et niveau identiques à l'existant | préalable (séquence /… | T | T | Phase 1, T (§1.2) | règle par défaut (T) |
| AR-PLN-078 | Persiennes démantelées et entreposées pendant les travaux | préalable (séquence /… | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| AR-PLN-079 | Coussin gonflable de quai d'embarquement démonté / réinstallé | préalable (séquence /… | NA | A.1 | Phase B-A, §6 NA | règle spécifique |
| AR-PLN-080 | Base membranée et trappes de toit à conserver et protéger | autre (autre (protect… | T | T | T (§1.2) | règle spécifique |
| AR-PLN-081 | Prise d'air extérieure à conserver et protéger | autre (autre (protect… | T | T | T (§1.2) | règle par défaut (T) |
| AR-PLN-082 | Réfection avec briques récupérées | préalable (séquence /… | T | T | T (§1.2) | règle par défaut (T) |
| ME-001 | Séquence (phasage) imposée par les documents d'architecture / du propriétaire ; tout ce qui es… | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ME-002 | Même exigence de phasage côté électricité | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ME-003 | Documents généraux du propriétaire/architecte contractuels (rebuts, horaires, heures de percem… | autre (renvoi / oblig… | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ME-004 | Note de phase sur les plans : travaux en plusieurs phases décrites en architecture | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ME-005 | Obligation de consulter les documents généraux du propriétaire — dont la protection des infect… | autre (renvoi pci / o… | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ME-006 | Coupure des gicleurs du quai des ambulances : 2 × 2 h | fenêtre horaire | 3.S | A.1 | Phase 3.N, Phase 3.S, Phase B-A, matrice ME, §5 validation CISSS, §6 NA | règle spécifique |
| ME-007 | Mise hors service de zone du réseau de gicleurs + obturation + récupération du glycol | interdiction | 3.S | A.1 | Phase 3.S, Phase B-A, matrice ME, §5 validation CISSS, §6 NA | règle spécifique |
| ME-008 | Remplissage au glycol par un fournisseur | préalable + fenêtre h… | 3.S | A.1 | Phase 3.S, Phase B-A, matrice ME, §6 NA | règle spécifique |
| ME-009 | Gicleurs existants à protéger durant les travaux de plafond | interdiction | 3.S | B | Phase 3.S, Phase B-B, matrice ME | règle spécifique |
| ME-010 | Gicleur à remplacer et descente relocalisée pour libérer l'espace du volet coupe-feu de fenêtre | préalable | 1 | A | Phase 1, Phase B-A, matrice ME | règle spécifique |
| ME-011 | Réseaux de gicleurs neufs utilisables en cours de travaux sur autorisation de l'ingénieur | préalable | T | T | T (§1.2), matrice ME | règle par défaut (T) |
| ME-012 | Obturation des extrémités de tuyauterie à la fin de chaque période/journée de travail | fenêtre horaire | T | T | T (§1.2), matrice ME | règle par défaut (T) |
| ME-013 | Préavis écrit de 48 h avant essais (mécanique) | préavis | 4, T | 4, T | Phase 4, T (§1.2), §1.3 étapes types | règle spécifique |
| ME-014 | Préavis de 3 jours avant essai d'étanchéité et première charge de frigorigène | préavis | 4, T | 4, T | Phase 4, T (§1.2), §1.3 étapes types | règle spécifique |
| ME-015 | Préavis de 48 h à l'ingénieur pour les essais de mise à la terre | préalable + préavis | 4, T | 4, T | Phase 4, T (§1.2), §1.3 étapes types | règle spécifique |
| ME-016 | Préavis de 2 semaines à l'ingénieur pour les essais d'électricité | préavis | 4, T | 4, T | Phase 4, T (§1.2), §1.3 étapes types | règle spécifique |
| ME-017 | Préavis de 1 semaine au propriétaire avant la mise en route électrique | préavis | 4, T | 4, T | Phase 4, T (§1.2), §1.3 étapes types, §5 validation CISSS | règle spécifique |
| ME-018 | Préavis de 48 h avant de dissimuler des ouvrages électriques | préavis | 4, T | 4, T | Phase 4, T (§1.2), §1.3 étapes types | règle spécifique |
| ME-019 | Préavis de 72 h pour la formation du personnel d'exploitation | fenêtre horaire + pré… | 4, T | 4, T | Phase 4, T (§1.2), §5 validation CISSS | règle spécifique |
| ME-020 | Tous les percements en dehors des heures d'occupation | fenêtre horaire | T | T | Phase 3.N, Phase B-B, T (§1.2) | règle par défaut (T) |
| ME-021 | Détection préalable des services avant percement (rayons X, caméra) | préalable | T | T | T (§1.2) | règle par défaut (T) |
| ME-022 | Interdiction du percement par chocs mécaniques | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| ME-023 | Percement des éléments de structure : approbation écrite préalable de l'ingénieur en structure | préalable | T | T | T (§1.2) | règle par défaut (T) |
| ME-024 | Aucun ouvrage dissimulé sans inspection préalable | préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| ME-025 | Registres coupe-feu : approbation de l'autorité compétente avant dissimulation | préalable | 2 | B.1.2 | Phase 2, Phase 2.O, Phase B-B, matrice ME, §6 NA | règle spécifique |
| ME-026 | Registre coupe-feu/fumée : fermeture sur panne de courant, détection de chaleur, détection de… | préalable (séquence /… | T | T | T (§1.2), matrice ME | règle par défaut (T) |
| ME-027 | Raccordement 120 VAC et alarme incendie des registres par l'entrepreneur en électricité | préalable (séquence /… | T | T | T (§1.2), matrice ME | règle par défaut (T) |
| ME-028 | Longueur droite de 600 mm en aval du volet pour le détecteur de fumée | préalable | T | T | T (§1.2), matrice ME | règle par défaut (T) |
| ME-029 | Registre motorisé existant à relocaliser pour permettre l'ajout du registre coupe-feu | préalable | 2 | B.1.2 | Phase 2, Phase 2.O, Phase B-B, matrice ME, §6 NA | règle spécifique |
| ME-030 | Contrôleurs et logiciels existants conservés ; aucun nouveau point de contrôle | interdiction | T | T | T (§1.2), matrice ME | règle par défaut (T) |
| ME-031 | Thermostats pneumatiques à relocaliser ; aucune sonde neuve | autre (autre) | 3.N | B.1.2 | Phase 3.N, Phase B-B, matrice ME | règle spécifique |
| ME-032 | Entrebarrages électriques requis pour assurer le fonctionnement des systèmes existants touchés | préalable (séquence /… | T | T | T (§1.2), matrice ME | règle par défaut (T) |
| ME-033 | Mise en route de la régulation en deux phases, dont une avec les systèmes en fonction | préalable (séquence /… | 4, T | 4, T | Phase 4, T (§1.2), matrice ME | règle spécifique |
| ME-034 | Simulation d'une séquence de panne de courant à la vérification | autre (autre (essai)) | 4, T | 4, T | Phase 4, T (§1.2), matrice ME | règle spécifique |
| ME-035 | Mise en service finale sous supervision des représentants du propriétaire | préalable (séquence /… | 4, T | 4, T | Phase 4, T (§1.2), matrice ME, §5 validation CISSS | règle spécifique |
| ME-036 | Alimentation primaire 120 V des contrôles depuis les panneaux d'urgence | préalable (séquence /… | T | T | T (§1.2), matrice ME | règle par défaut (T) |
| ME-037 | Volets motorisés fournis/installés par la ventilation, actuateurs par la régulation | préalable (séquence /… | T | T | T (§1.2) | règle par défaut (T) |
| ME-038 | Soupapes de contrôle fournies/raccordées par la régulation, installées par le chauffage/refroi… | préalable (séquence /… | T | T | T (§1.2) | règle par défaut (T) |
| ME-039 | Enlèvement/réinstallation des tuiles acoustiques par l'entrepreneur général | préalable (séquence /… | T | T | Phase 1, T (§1.2) | règle par défaut (T) |
| ME-040 | Obturation étanche de toute gaine conservée dont un branchement est retiré | autre (obligation) | T | T | T (§1.2) | règle par défaut (T) |
| ME-041 | Robinets de fermeture manuelle neufs accessibles en tout temps ; trappes d'accès à coordonner | préalable (séquence /… | T | T | T (§1.2) | règle par défaut (T) |
| ME-042 | Prise d'air frais du bloc opératoire maintenue en fonction ; conduits temporaires en parallèle… | préalable + interdict… | 2.O, 3.O | A, B, C | Phase 2.O, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, diagramme, matrice ME, préambule / vue d'ensemble, §4 conflits, §6 NA | règle spécifique |
| ME-043 | Étape temporaire #1 : démanteler seulement après mise en place des conduits temporaires | préalable (séquence /… | 2.O, 3.O | A, B, C | Phase 2.O, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, diagramme, matrice ME, préambule / vue d'ensemble, §4 conflits, §6 NA | règle spécifique |
| ME-044 | Étape temporaire #2 : démanteler seulement après mise en place du nouveau conduit d'air neuf s… | préalable (séquence /… | 2.O, 3.O | A, B, C | Phase 2.O, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, diagramme, matrice ME, préambule / vue d'ensemble, §4 conflits, §6 NA | règle spécifique |
| ME-045 | Nouveau conduit PAF BO installé après la fin du revêtement ; temporaires maintenus jusqu'à mis… | préalable (séquence /… | 2.O, 3.O | A, B, C | Phase 2.O, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, diagramme, matrice ME, préambule / vue d'ensemble, §4 conflits, §6 NA | règle spécifique |
| ME-046 | Entrées d'air du BO : principale chauffée et secondaire non chauffée (été/refroidissement grat… | préalable (séquence /… | 2.O, 3.O | A, B, C | Phase 2.O, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, diagramme, matrice ME, §6 NA | règle spécifique |
| ME-047 | Conduits de prise d'air temporaire du BO : 2 × 900 × 900 mm, raccordés au plénum sous soffite | autre (autre) | 2.O, 3.O | A, B, C | Phase 2.O, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, diagramme, matrice ME, §6 NA | règle spécifique |
| ME-048 | Conduit PAF du BO — coupure de nuit possible, volets à fermer | fenêtre horaire | 2.O, 3.O | A, B, C | Phase 2.O, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, diagramme, matrice ME, §5 validation CISSS, §6 NA | règle spécifique |
| ME-049 | Unité de ventilation hémodialyse/laboratoire maintenue en fonction ; conduits temporaires avan… | préalable | 2.N, 2.O | C.2 | Phase 2, Phase 2.N, Phase 2.O, Phase B-B, Phase B-C, diagramme, matrice ME, préambule / vue d'ensemble | règle spécifique |
| ME-050 | Phasage et coupures de l'unité hémodialyse/laboratoire selon l'horaire du propriétaire | fenêtre horaire | 2.N, 2.O | C.2 | Phase 2.N, Phase 2.O, Phase B-C, diagramme, matrice ME, préambule / vue d'ensemble, §5 validation CISSS | règle spécifique |
| ME-051 | Coupures d'une journée, un conduit à la fois, le dimanche, hors période estivale | fenêtre horaire | 2.N, 2.O | C.2 | Phase 2.N, Phase 2.O, Phase B-C, diagramme, matrice ME, préambule / vue d'ensemble, §4 conflits, §5 validation CISSS | règle spécifique |
| ME-052 | Conduits d'hémodialyse : point d'entrée dans la base de toit conservé ; étanchéité refaite en… | préalable (séquence /… | 2.N, 2.O | C.2 | Phase 2.N, Phase 2.O, Phase B-C, matrice ME | règle spécifique |
| ME-053 | Manchon de traversée de mur des conduits d'hémodialyse selon détail de G004 | autre (renvoi) | 2.N, 2.O | C.2 | Phase 2.N, Phase 2.O, Phase B-C, matrice ME | règle spécifique |
| ME-054 | Passerelle d'accès en aluminium enlevée temporairement et modifiée par l'entrepreneur général | préalable (séquence /… | 2.N, 2.O | C.2 | Phase 2.N, Phase 2.O, Phase B-C, matrice ME | règle spécifique |
| ME-055 | Persienne UT-2 : coupure rapide de nuit ou de fin de semaine, registre fermé, filtration et gr… | fenêtre horaire | 3.S | B | Phase 3.S, Phase B-B, matrice ME, §5 validation CISSS | règle spécifique |
| ME-056 | Chambre à pression négative #307 : démantèlement seulement quand la chambre est inoccupée | préalable + interdict… | 2.S | C.4 | Phase 2.S, Phase B-C, diagramme, matrice ME, §5 validation CISSS | règle spécifique |
| ME-057 | Chambre à pression négative #216 : prolongation temporaire du conduit RAV hors échafaudages | autre (travaux tempor… | 2.N | C.2 | Phase 2.N, Phase B-C, diagramme, matrice ME, §5 validation CISSS | règle spécifique |
| ME-058 | Soins intensifs : système d'apport d'air frais supplémentaire doit demeurer en fonction | interdiction + fenêtr… | 2 | C.4 | Phase 2, Phase 2.O, Phase B-C, matrice ME, §5 validation CISSS, §6 NA | règle spécifique |
| ME-059 | Sortie d'air du laboratoire maintenue en fonction par conduit temporaire hors échafaudages | autre (travaux tempor… | 3.N | B | Phase 3.N, Phase B-B, matrice ME | règle spécifique |
| ME-060 | Persiennes d'évacuation des laboratoires : systèmes en fonction pendant toute la durée | interdiction | 3.N | B | Phase 3.N, Phase B-B, matrice ME | règle spécifique |
| ME-061 | Évacuation V-53 (toilette du laboratoire) : filtration temporaire | autre (travaux tempor… | 3.N | B | Phase 3.N, Phase B-B, matrice ME | règle spécifique |
| ME-062 | Atelier de menuiserie : évacuation mise à l'arrêt pour toute la durée des travaux du secteur | fenêtre horaire | NA | B | Phase B-B, matrice ME, §6 NA | règle spécifique |
| ME-063 | Persiennes PAF non touchées : pré-filtre temporaire durant les travaux de la façade | autre (pci / protecti… | T | T | T (§1.2), matrice ME | règle par défaut (T) |
| ME-064 | Prise d'air de la centrale d'air médical : prise d'air temporaire obligatoire durant le chanti… | préalable | 3.N, 3.O | B | Phase 3.N, Phase 3.O, Phase B-B, matrice ME, préambule / vue d'ensemble, §4 conflits, §6 NA | règle spécifique |
| ME-065 | Prise d'air air médical temporaire sur la façade ouest pendant les travaux de la façade nord | préalable (séquence /… | 3.N, 3.O | B | Phase 3, Phase 3.N, Phase 3.O, Phase B-B, diagramme, matrice ME, préambule / vue d'ensemble, §2.7 variantes, §4 conflits, §6 NA | règle spécifique |
| ME-066 | Boîtier HEPA de la prise d'air médical installé temporairement sur la façade ouest | préalable (séquence /… | 3.N, 3.O | B | Phase 3.N, Phase 3.O, Phase B-B, diagramme, matrice ME, préambule / vue d'ensemble, §6 NA | règle spécifique |
| ME-067 | Réinstallation finale de la prise d'air médical après le revêtement de la façade nord | préalable (séquence /… | 3.N, 3.O | B | Phase 3, Phase 3.N, Phase 3.O, Phase 4, Phase B-B, diagramme, matrice ME, préambule / vue d'ensemble, §1.3 étapes types, §2.7 variantes, §4 conflits, §6 NA | règle spécifique |
| ME-068 | Air médical : système en fonction 24/7, bonbonnes requises pour la relocalisation | préalable + interdict… | 3.N, 3.O | B | Phase 3.N, Phase 3.O, Phase B-B, matrice ME, §5 validation CISSS, §6 NA | règle spécifique |
| ME-069 | Air médical : deux interventions + certification en fin de travaux | préalable (séquence /… | 3.N, 3.O, 4 | 4, B | Phase 3.N, Phase 3.O, Phase 4, Phase B-B, matrice ME, préambule / vue d'ensemble, §5 validation CISSS | règle spécifique |
| ME-070 | Gaz médicaux : brasage et main-d'œuvre certifiés, travaux déclarés à la RBQ | préalable | 3.N, 3.O, 4 | 4, B | Phase 3.N, Phase 3.O, Phase 4, Phase B-B, matrice ME | règle spécifique |
| ME-071 | Gaz médicaux : essais par laboratoire indépendant certifié BNQ/CCN, en sous-traitance du propr… | préalable (séquence /… | 3.N, 3.O, 4 | 4, B | Phase 3.N, Phase 3.O, Phase 4, Phase B-B, matrice ME | règle spécifique |
| ME-072 | Gaz médicaux : attestation écrite à l'établissement avant essais par l'organisme de contrôle | préalable (séquence /… | 3.N, 3.O, 4 | 4, B | Phase 3.N, Phase 3.O, Phase 4, Phase B-B, matrice ME, §5 validation CISSS | règle spécifique |
| ME-073 | Gaz médicaux : l'établissement choisit les emplacements d'inspection interne et doit être prés… | préalable (séquence /… | 3.N, 3.O, 4 | 4, B | Phase 3.N, Phase 3.O, Phase 4, Phase B-B, matrice ME, §5 validation CISSS | règle spécifique |
| ME-074 | Canalisations de gaz médicaux ne doivent pas servir de mise à la terre | interdiction | 3.N, 3.O | B | Phase 3.N, Phase 3.O, Phase B-B, matrice ME | règle spécifique |
| ME-075 | Évents de vapeur des autoclaves relocalisés avant le début des travaux de la façade ouest | préalable | 2.O, 3.O | B | Phase 2.O, Phase 3.O, Phase 3.S, Phase B-B, diagramme, matrice ME, préambule / vue d'ensemble, §4 conflits, §6 NA | règle spécifique |
| ME-076 | Évents d'autoclave : réinstallation au même endroit à la fin des travaux | préalable (séquence /… | 2.O, 3.O | B | Phase 2.O, Phase 3.O, Phase 4, Phase B-B, matrice ME, §1.3 étapes types, §6 NA | règle spécifique |
| ME-077 | Évents d'autoclave : fenêtre « nuit ou le matin avant 10 h », système 24/7, éloignés de la pri… | fenêtre horaire + pré… | 2.O, 3.O | B | Phase 2.O, Phase 3.O, Phase B-B, matrice ME, préambule / vue d'ensemble, §4 conflits, §5 validation CISSS, §6 NA | règle spécifique |
| ME-078 | Prolongements de tuyauterie des évents de vapeur enlevés temporairement pour permettre le revê… | préalable (séquence /… | 2.O, 3.O | B | Phase 2.O, Phase 3.O, Phase B-B, matrice ME, §6 NA | règle spécifique |
| ME-079 | Tuyauteries temporaires pour éloigner les sorties des prises d'air frais ; cols de cygne rehau… | autre (pci / qualité… | 2.O, 3.O | B | Phase 2.O, Phase 3.O, Phase B-B, matrice ME, §6 NA | règle spécifique |
| ME-080 | Évents de vapeur de la chaufferie conservés en fonction pendant toute la durée | interdiction | 2.N, 2.O, 3.N, 3.O | A, B, C | Phase 2.N, Phase 2.O, Phase 3.N, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, matrice ME, §6 NA | règle spécifique |
| ME-081 | Câble chauffant des évents de vapeur : réinstallation coordonnée avec la plomberie | préalable (séquence /… | 2.O, 3.O | B | Phase 2.O, Phase 3.O, Phase B-B, matrice ME, §6 NA | règle spécifique |
| ME-082 | Câbles chauffants : intervention hors période hivernale, durée « Mois » | fenêtre horaire | 2.O, 3.O | B | Phase 2.O, Phase 3.O, Phase B-B, matrice ME, §4 conflits, §6 NA | règle spécifique |
| ME-083 | Thermostat des câbles chauffants retiré temporairement, conduit EMT remplacé et dissimulé | préalable (séquence /… | 2.O, 3.O | B | Phase 2.O, Phase 3.O, Phase B-B, matrice ME, §6 NA | règle spécifique |
| ME-084 | Tuyauteries de glycol du BO enlevées temporairement pour permettre le revêtement | préalable (séquence /… | 2.O, 3.O | A, B, C | Phase 2.O, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, matrice ME, §4 conflits, §6 NA | règle spécifique |
| ME-085 | Bi-bloc GREE 12 MBH (sud) : récupération du réfrigérant, remise en marche pour maintenir en op… | préalable (séquence /… | 3.S | A | Phase 3.S, Phase B-A, matrice ME | règle spécifique |
| ME-086 | Bi-bloc LG 18 MBH (est) : mêmes exigences | préalable (séquence /… | 1, 2.E | A, B, C | Phase 1, Phase 2.E, Phase B-A, Phase B-B, Phase B-C, matrice ME | règle spécifique |
| ME-087 | Bi-bloc de la salle de traitement d'eau d'hémodialyse (local 203) : arrêt de courte durée, hor… | fenêtre horaire | 2 | C.2 | Phase 2.N, Phase 2.O, Phase B-C, matrice ME, §4 conflits, §5 validation CISSS, §6 NA | règle spécifique |
| ME-088 | Bi-bloc de la salle des serveurs RC : arrêt de courte durée, semaine, hors période estivale | fenêtre horaire | 1 | A | Phase 1, Phase B-A, matrice ME, §5 validation CISSS | règle spécifique |
| ME-089 | Bi-blocs divers : maintien en fonction pendant toute la durée | interdiction | T | T | Phase 2.E, Phase B-C, T (§1.2), matrice ME | règle spécifique |
| ME-090 | Bi-bloc de la salle d'observation sur garde-corps : réinstallation sur le garde-corps modifié | préalable (séquence /… | 3.S | A | Phase 3.S, Phase B-A, matrice ME | règle spécifique |
| ME-091 | Alarme incendie : système existant Notifier NFS2-3030-FR, coordination obligatoire avec le man… | préalable | 3.N | B.1.2 | Phase 3.N, Phase B-B, matrice ME | règle spécifique |
| ME-092 | Alarme incendie : fonctionnel pendant toute la durée, y compris les interruptions de courant | interdiction | T | T | Phase 3.S, T (§1.2), matrice ME | règle par défaut (T) |
| ME-093 | Travaux dans le panneau d'alarme incendie réservés à un technicien du manufacturier | interdiction | T | T | T (§1.2), matrice ME | règle par défaut (T) |
| ME-094 | Vérification complète du système après travaux + certificat | préalable (séquence /… | 4, T | 4, T | Phase 4, T (§1.2), matrice ME | règle spécifique |
| ME-095 | Détecteur de fumée relocalisé : vérification à inclure au rapport d'alarme incendie du projet | préalable (séquence /… | 3.S | B | Phase 3.S, Phase B-B, matrice ME | règle spécifique |
| ME-096 | Détecteur de fumée de gaine dans le soffite conservé | autre (protection) | 2.N, 2.O, 3.N, 3.O | A, B, C | Phase 2.N, Phase 2.O, Phase 3.N, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, §6 NA | règle spécifique |
| ME-097 | Détecteur de fumée du secteur IRM conservé et protégé | autre (protection) | 1 | A | Phase 1, Phase B-A, matrice ME | règle spécifique |
| ME-098 | Mise à l'essai intégrée CAN/ULC-S1001 par un coordonnateur des essais engagé par le propriétai… | préalable (séquence /… | 4, T | 4, T | Phase 4, T (§1.2), diagramme, §5 validation CISSS | règle spécifique |
| ME-099 | Contrôle d'accès Kantech ; contrôleur KT-1 neuf raccordé à l'existant | préalable (séquence /… | 3.N | B.1.2 | Phase 3.N, Phase B-B, matrice ME | règle spécifique |
| ME-100 | Paratonnerre : descentes intérieures et tiges de terre exclues du mandat | interdiction | T | T | T (§1.2), matrice ME | règle spécifique |
| ME-101 | Paratonnerre : identification, entreposage chez le propriétaire, limites de démolition, rappor… | préalable | T | T | T (§1.2), matrice ME | règle spécifique |
| ME-102 | Paratonnerre : plan indicatif seulement, quantités variables | autre (zone d'ombre c… | T | T | T (§1.2), matrice ME | règle spécifique |
| ME-103 | Paratonnerre exclu du tableau de coordination | autre (zone d'ombre) | T | T | T (§1.2), matrice ME | règle spécifique |
| ME-104 | Lecteurs de carte et luminaires muraux retirés temporairement et entreposés | autre (autre) | 4, T | 4, T | T (§1.2), matrice ME, §1.3 étapes types | règle spécifique |
| ME-105 | Luminaires muraux réinstallés au même endroit, angle conservé | préalable (séquence /… | 4, T | 4, T | T (§1.2), matrice ME, §1.3 étapes types | règle spécifique |
| ME-106 | Luminaires : emplacement en salle mécanique défini après installation des autres équipements | préalable (séquence /… | 4, T | 4, T | T (§1.2), matrice ME | règle spécifique |
| ME-107 | Sectionneurs de thermopompes retirés temporairement, circuit à fermer | fenêtre horaire | 2.O, 2.S, 3.O, 3.S | A, B, C | Phase 2.O, Phase 2.S, Phase 3.O, Phase 3.S, Phase B-A, Phase B-B, Phase B-C, diagramme, matrice ME | règle spécifique |
| ME-108 | Conduits EMT des circuits de prises relocalisés avant les travaux structuraux | préalable + préalable… | 1 | A.6 | Phase 1, Phase B-A, diagramme, §4 conflits | règle spécifique |
| ME-109 | Tuyauterie d'eau chaude de chauffage périphérique relocalisée pour le volet coupe-feu de fenêt… | préalable | 1 | A | Phase 1, Phase B-A | règle spécifique |
| ME-110 | Entreplafond à libérer pour l'ajout des volets coupe-feu de fenêtre | préalable | 1 | A | Phase 1, Phase B-A, diagramme | règle spécifique |
| ME-111 | Renforcement structural des colonnes A4, A5, A6 dans l'entreplafond du RC | préalable (séquence /… | 1 | A.6 | Phase 1, Phase B-A | règle spécifique |
| ME-112 | Grilles, diffuseurs et luminaires retirés temporairement ou protégés durant les travaux de pla… | autre (protection) | 1, 3.S | A, B | Phase 1, Phase 3.S, Phase B-A, Phase B-B | règle spécifique |
| ME-113 | Diffuseur de la nouvelle issue du laboratoire enlevé temporairement et réinstallé | autre (autre) | 3.N | B.1.2 | Phase 3.N, Phase B-B | règle spécifique |
| ME-114 | Cabinet de chauffage hydronique remplacé, soupape pneumatique existante réutilisée | préalable (séquence /… | 3.N | B.1.2 | Phase 3.N, Phase B-B | règle spécifique |
| ME-115 | Thermostat et soupape pneumatiques relocalisés par l'entrepreneur en plomberie/chauffage | préalable (séquence /… | 3.N | B.1.2 | Phase 3.N, Phase B-B | règle spécifique |
| ME-116 | Sorties d'arrosage extérieures à conserver et protéger | préalable (séquence /… | 1 | A.1 | Phase 1, Phase B-A, §6 NA | règle spécifique |
| ME-117 | Sorties d'évent sanitaire et de laboratoire relocalisées ; solins remplacés par l'entrepreneur… | préalable (séquence /… | 2.E | C | Phase 2.E, Phase B-C, diagramme, matrice ME, §6 NA | règle spécifique |
| ME-118 | Conduit d'évacuation de la hotte de médecine nucléaire modifié sur toute la hauteur | préalable (séquence /… | 2.E | C | Phase 1, Phase 2, Phase 2.E, Phase B-C, diagramme, matrice ME, préambule / vue d'ensemble, §6 NA | règle spécifique |
| ME-119 | Conduit de la hotte de médecine nucléaire : arrêt de courte durée, vendredi au dimanche, suppo… | fenêtre horaire | 2.E | C | Phase 2.E, Phase B-C, diagramme, matrice ME, préambule / vue d'ensemble, §5 validation CISSS | règle spécifique |
| ME-120 | Ventilateur d'évacuation en toiture : conduit conservé, calorifuge D-2 50 mm, cloisonnement da… | préalable (séquence /… | 2.N, 2.O, 3.N, 3.O | A, B, C | Phase 2.N, Phase 2.O, Phase 3.N, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, matrice ME, §6 NA | règle spécifique |
| ME-121 | Trappes d'accès dans le soffite relocalisées/remplacées par l'entrepreneur général | préalable (séquence /… | 2.N, 2.O, 3.N, 3.O | A, B, C | Phase 2.N, Phase 2.O, Phase 3.N, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, matrice ME, §6 NA | règle spécifique |
| ME-122 | Nouvelles trappes d'accès à installer durant les travaux de revêtement, dimensions et position… | préalable (séquence /… | 2.N, 2.O, 3.N, 3.O | A, B, C | Phase 2.N, Phase 2.O, Phase 3.N, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, matrice ME, §6 NA | règle spécifique |
| ME-123 | Supports déposés en toiture relocalisés pour dégager le nouveau revêtement (axe B1) | préalable (séquence /… | 2.N, 2.O, 3.N, 3.O | A, B, C | Phase 2.N, Phase 2.O, Phase 3.N, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, matrice ME, §6 NA | règle spécifique |
| ME-124 | Levage et hissage : procédure à fournir, structure non utilisable, grue planifiée avec proprié… | préalable + préalable… | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| ME-125 | Chemins d'accès des équipements à valider avec le propriétaire avant livraison | préalable | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| ME-126 | Entreposage au chantier interdit sauf autorisation du propriétaire | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| ME-127 | Matériaux entreposés nuisant aux opérations du propriétaire à déplacer | autre (obligation) | T | T | T (§1.2) | règle par défaut (T) |
| ME-128 | Avis obligatoire avant de démanteler un appareil défectueux, sinon présomption de bon état | préavis | T | T | T (§1.2) | règle par défaut (T) |
| ME-129 | Calendrier des travaux électricité dans les 15 jours ouvrables de l'attribution | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ME-130 | Liste de matériel dans les 10 jours ; interdiction de commander avant approbation | préalable + interdict… | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ME-131 | Validation des délais de livraison dès la première semaine du mandat ; 10 jours ouvrables mini… | préalable + préavis | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ME-132 | Interdiction d'entreprendre les travaux avant lettre de vérification de l'ingénieur | interdiction | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ME-133 | Interdiction de faire fonctionner les installations permanentes sans permission écrite | interdiction | T | T | T (§1.2) | règle par défaut (T) |
| ME-134 | ERE aéraulique : ne débuter que lorsque le bâtiment est en grande partie utilisable et que pla… | préalable | 4, T | 4, T | Phase 4, T (§1.2) | règle spécifique |
| ME-135 | ERE aéraulique : filtres en place et propres, registres et volets coupe-feu ouverts, conduits… | préalable | 4, T | 4, T | Phase 4, T (§1.2) | règle spécifique |
| ME-136 | ERE aéraulique : mesures dans les aires occupées (température, HR, vitesse d'air, bruit) et ré… | autre (obligation) | 4, T | 4, T | Phase 4, T (§1.2) | règle spécifique |
| ME-137 | Rapport d'équilibrage aéraulique dans les 5 jours ouvrables de la prise de lecture | préavis | 4, T | 4, T | Phase 4, T (§1.2) | règle spécifique |
| ME-138 | ERE hydronique : réseaux lavés, remplis et purgés avant les opérations | préalable | 4, T | 4, T | Phase 4, T (§1.2) | règle spécifique |
| ME-139 | Remplacement des filtres juste avant la réception provisoire | préalable (séquence /… | 4, T | 4, T | Phase 4, T (§1.2) | règle spécifique |
| ME-140 | Inspection provisoire : démonstration des systèmes avec arrêt et départ, à la charge de l'entr… | fenêtre horaire | 4, T | 4, T | Phase 4, T (§1.2) | règle spécifique |
| ME-141 | Antenne au toit et conduit PVC : usage à valider, demandé retiré | autre (zone d'ombre) | NA | B | Phase B-B, §6 NA | règle spécifique |
| ME-142 | Capotin de la hotte de cuisine de la salle communautaire remplacé ; prolongation temporaire ho… | autre (travaux tempor… | 1, 2.E | A, B, C | Phase 1, Phase 2.E, Phase B-A, Phase B-B, Phase B-C, matrice ME, §6 NA | règle spécifique |
| ME-143 | Persienne d'échangeur d'air du secteur de la roulotte IRM mobile retirée temporairement | autre (autre) | NA | A | Phase 1, Phase 3.O, Phase B-A, §6 NA | règle spécifique |
| ME-144 | Bi-bloc existant conservé : revêtement installé autour de la tuyauterie existante | préalable (séquence /… | 1, 2.E, 2.O, 3.O | A, B, C | Phase 1, Phase 2.E, Phase 2.O, Phase 3.O, Phase B-A, Phase B-B, Phase B-C, matrice ME | règle spécifique |
| ME-145 | Caméra extérieure des urgences relocalisée avec boîte étanche en surface | autre (autre) | 3.S | A.1 | Phase 3.S, Phase B-A, matrice ME | règle spécifique |
| ME-146 | Détecteur de mouvement relocalisé avec conduits dissimulés dans l'entreplafond | autre (autre) | 3.S | A.1 | Phase 3.S, Phase B-A, matrice ME | règle spécifique |
| ME-147 | Enseigne « AMBULANCE » : chaque lettre raccordée indépendamment ; nouvelle boîte de jonction 3… | autre (autre) | 3.S | A.1 | Phase 3.N, Phase 3.S, Phase B-A, matrice ME, §6 NA | règle spécifique |
| ME-148 | Isolant coupe-feu giclé : protection totale des composantes électromécaniques ou application a… | interdiction + préala… | T | T | T (§1.2) | règle par défaut (T) |
| ME-149 | Coordination de la démolition électrique avec l'entrepreneur général pour minimiser les retouc… | préalable (séquence /… | T | T | T (§1.2) | règle par défaut (T) |
| ME-150 | Protection de tous les équipements durant les travaux (débris, poussière, eau, intempéries, va… | autre (pci / protecti… | T | T | T (§1.2) | règle par défaut (T) |
| ME-151 | Empêcher la pénétration de poussière dans les installations pendant l'usage temporaire | autre (pci / protecti… | T | T | T (§1.2) | règle par défaut (T) |
| ME-152 | Approbation écrite du propriétaire pour la position finale des équipements de protection incen… | préalable | 0, T | 0, T | Phase 0, T (§1.2), §5 validation CISSS | règle spécifique |
| ME-153 | Approbation des plans de gicleurs par l'ingénieur ET l'architecte avant le début des travaux | préalable | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ME-154 | Approbation du propriétaire pour l'emplacement des trappes d'accès avant installation | préalable | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| ME-155 | Portes de visite vérifiées par l'ingénieur et l'architecte, installées par l'entrepreneur géné… | préalable (séquence /… | T | T | T (§1.2) | règle par défaut (T) |
| ME-156 | Étanchéité de tout percement de l'enveloppe selon les instructions de l'architecte | préalable (séquence /… | T | T | Phase 3, T (§1.2), §2.7 variantes, §4 conflits | règle par défaut (T) |
| ME-157 | Percement des poutres d'acier coordonné avec la structure, détails aux dessins d'atelier de st… | préalable (séquence /… | T | T | T (§1.2) | règle par défaut (T) |
| ME-158 | Supports d'équipement conçus par un ingénieur en structure aux frais du sous-traitant, approuv… | préalable + préalable… | T | T | T (§1.2) | règle par défaut (T) |
| ME-159 | Traversée d'une séparation coupe-feu d'issue interdite sauf exceptions | interdiction | 3.N, T | B.1.2, T | Phase 3.N, Phase B-B, T (§1.2) | règle spécifique |
| ME-160 | Plans émis pour construction obligatoires au chantier | interdiction | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ME-161 | Honoraires professionnels à la charge de l'entrepreneur général si la durée excède de 10 % l'é… | autre (autre (pénalit… | T | T | T (§1.2) | règle spécifique |
| ST-001 | Réviser les dessins de structure avec ceux de tous les autres professionnels avant la construc… | Préalable | 0 | 0 | Phase 0 | règle spécifique |
| ST-002 | Signaler toute anomalie ou conflit avant de commencer les travaux | Préalable | 0 | 0 | Phase 0 | règle spécifique |
| ST-003 | Interdiction de couper ou percer des ouvertures dans les éléments de structure sans permission… | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| ST-004 | Vérifier sur place les dimensions et conditions existantes avant la construction | Préalable | 0 | 0 | Phase 0 | règle spécifique |
| ST-005 | Interdiction de construire à partir des dessins émis « pour soumission » : une émission « Émis… | Interdiction + préala… | 0 | 0 | Phase 0 | règle spécifique |
| ST-006 | Interdiction de fixer les nouvelles fenêtres aux colombages, barres en Z ou éléments structura… | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| ST-007 | L'entrepreneur établit la procédure et la séquence de construction (travaux temporaires, étaie… | Préalable (séquence à… | 0 | 0 | Phase 0, hors-phase (préambule ou sections transversales) | règle spécifique |
| ST-008 | Conception et attestation des travaux temporaires par un ingénieur engagé par l'entrepreneur | Préalable | 0 | 0 | Phase 0 | règle spécifique |
| ST-009 | Interdiction d'utiliser les ancrages et éléments encastrés définitifs comme support ou contrev… | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| ST-010 | Charges de construction plafonnées aux charges de conception ; charges maximales seulement apr… | Interdiction + préala… | T | T | T (§1.2) | règle par défaut (T) |
| ST-011 | Point d'arrêt : après retrait des revêtements, examiner la structure existante et rapporter to… | Préalable (point d'ar… | T | T | T (§1.2), préambule / vue d'ensemble, §1.3 étapes types | règle par défaut (T) |
| ST-012 | Planifier pour réduire l'impact sur l'exploitation ; minimiser bruit, poussière, vibrations ;… | Préalable (échéancier) | 0 | 0 | Phase 0 | règle spécifique |
| ST-013 | Couper les services dans les zones touchées par la démolition et la construction ; réacheminer… | Préalable | T | T | T (§1.2) | règle par défaut (T) |
| ST-014 | Plans de démolition et d'étaiement signés et scellés par un ingénieur de l'entrepreneur, démon… | Préalable (livrable s… | 0 | 0 | Phase 0 | règle spécifique |
| ST-015 | Interdiction d'altérer les propriétés de l'acier structural conservé lors des coupes et de la… | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| ST-016 | Évaluer la capacité de la structure existante sous les charges de construction ; étayer si dép… | Préalable | T | T | T (§1.2) | règle par défaut (T) |
| ST-017 | Travaux à chaud : identifier les soudures sur éléments existants ou près de matériaux inflamma… | Préalable | T | T | T (§1.2) | règle par défaut (T) |
| ST-018 | Préavis d'au moins 24 heures pour l'inspection ; point d'arrêt sur la structure d'acier avant… | Préavis + préalable (… | T | T | T (§1.2), préambule / vue d'ensemble, §1.3 étapes types | règle par défaut (T) |
| ST-019 | Visites de chantier de l'ingénieur planifiées durant les heures normales de travail | Fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| ST-020 | Minimum de 10 jours ouvrables par émission de dessins d'atelier ; soumission selon la séquence… | Préalable (délai) | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| ST-021 | Interdiction de commencer la fabrication avant retour des dessins d'atelier révisés | Interdiction | T | T | T (§1.2) | règle spécifique |
| ST-022 | Interdiction de percer ou modifier les éléments de structure au chantier | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| ST-023 | Échafaudage : plans, notes de calcul et attestation signés et scellés respectant les capacités… | Préalable (livrable s… | 0, T | 0, T | Phase 0, Phase 2, T (§1.2), §2.7 variantes | règle spécifique |
| ST-024 | Interdiction de surcharger les toitures par l'entreposage de matériaux et d'équipements | Interdiction | T | T | Phase 2, Phase 3.O, T (§1.2), §2.7 variantes | règle par défaut (T) |
| ST-025 | Échafaudage : ancrages temporaires aux dalles, ou attestation scellée tenant compte de la char… | Préalable | 0, T | 0, T | Phase 0, Phase 2, T (§1.2), §2.7 variantes | règle spécifique |
| ST-026 | Aucune charge ponctuelle sur les toitures ventilées | Interdiction | T | T | Phase 2, Phase 3.O, T (§1.2), §2.7 variantes | règle par défaut (T) |
| ST-027 | Valider toutes les dimensions des éléments structuraux au chantier avant la fabrication ; vari… | Préalable | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| ST-028 | Localiser l'armature (préperçage 3 mm ou balayage) de tous les éléments en béton avant l'insta… | Préalable | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| ST-029 | Cotes en ± à coordonner avec les plans d'architecture | Préalable | T | T | T (§1.2) | règle par défaut (T) |
| ST-030 | Séquence imposée : démolition (plans d'architecture) → relevé complet des façades → coordinati… | Préalable (séquence i… | T | T | T (§1.2), préambule / vue d'ensemble, §1.3 étapes types | règle par défaut (T) |
| ST-031 | Séquence d'installation en trois étapes des renforts de poteaux HSS (soudure plaque → pose des… | Préalable (séquence i… | 1, 3 | B | Phase 1, Phase B-B, §6 NA | règle spécifique |
| ST-032 | Vérifier sur site l'emplacement des boulons d'ancrage existants avant l'exécution ; signaler t… | Préalable + préavis | 1, 3 | B | Phase 1, Phase B-B, §6 NA | règle spécifique |
| ST-033 | Retrait temporaire et soigneux de l'isolant pour visser depuis le colombage existant (détail n… | Préalable | T | T | T (§1.2) | règle par défaut (T) |
| ST-034 | Réparation de béton : température de l'air ambiant et du béton ≥ 10 °C | Préalable (condition… | T | T | T (§1.2), §1.3 étapes types, §4 conflits | règle spécifique |
| ST-035 | Béton autoplaçant : conditions thermiques > 5 °C, chauffage si requis | Préalable (condition… | T | T | T (§1.2) | règle spécifique |
| ST-036 | Démolition du béton à réparer au marteau pneumatique manuel de 7 kg maximum | Interdiction (limitat… | T | T | T (§1.2) | règle spécifique |
| ST-037 | Traitement du mur de fondation existant en cinq étapes, façades sud et nord, 17 interventions… | Préalable (séquence e… | 2.N, 2.S, 3.N, 3.S | B | Phase 2.N, Phase 2.S, Phase 3.N, Phase 3.S, Phase B-B, §6 NA | règle spécifique |
| ST-038 | Briques et colombages existants à conserver aux endroits repérés | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| ST-039 | Escalier no 7 : protéger et conserver les câbles existants | Interdiction | 3.N | B.1.2 | Phase 3.N, Phase B-B, préambule / vue d'ensemble | règle spécifique |
| ST-040 | Localiser les services d'utilités publiques et rapporter erreurs ou omissions avant de commenc… | Préalable | 0 | 0 | Phase 0 | règle spécifique |
| CI-TAB-001 | Délai de déménagement ou d'activation de 2 jours ouvrables pour chaque activité portant une cl… | Préavis (nature exact… | T | T | Phase 1, Phase B-A, T (§1.2), §1.3 étapes types, §5 validation CISSS | règle spécifique |
| CI-TAB-002 | Accès vertical dans l'existant limité à l'ascenseur no 1 et à l'escalier le plus près du chant… | Interdiction (+ confi… | T | T | Phase 0, T (§1.2), §5 validation CISSS | règle spécifique |
| CI-TAB-003 | Prioriser les accès par l'extérieur en tout temps | Interdiction (règle d… | T | T | T (§1.2) | règle spécifique |
| CI-TAB-004 | Toile fixée sur tous les échafauds ou autres équipements extérieurs jusqu'à la pose des membra… | Préalable | T | B.1.2 | Phase 2, Phase B-B, T (§1.2), diagramme, préambule / vue d'ensemble, §1.3 étapes types, §4 conflits | règle spécifique |
| CI-TAB-005 | Prises d'air du service alimentaire : classe PCI IV, horaire « S », délai 2 jours ouvrables | Fenêtre horaire (code… | 2 | B.1.2 | Phase 2, Phase 2.O, Phase B-B, diagramme, matrice ME, préambule / vue d'ensemble, §5 validation CISSS, §6 NA | règle spécifique |
| CI-TAB-006 | Fenêtres du basilaire, étape « installation plexiglass » : classe I, Tyvek et couvre-chaussure… | Fenêtre horaire + pré… | 1, 3.S | A.2 | Phase 1, Phase 3.S, Phase B-A, diagramme, préambule / vue d'ensemble, §1.3 étapes types, §4 conflits, §5 validation CISSS | règle spécifique |
| CI-TAB-007 | Fenêtres du basilaire, étapes « thermos » et « cadrage et toile », secteurs R04/R07/R10/R16/R4… | Fenêtre horaire + pré… | 1, 3.S | A.3, A.5 | Phase 1, Phase 3.S, Phase B-A, diagramme, préambule / vue d'ensemble, §1.3 étapes types, §4 conflits, §5 validation CISSS | règle spécifique |
| CI-TAB-008 | Fenêtres du basilaire, étapes « thermos » et « cadrage et toile », secteurs R33/R34/R36/R44 :… | Fenêtre horaire + pré… | 1, 3.S | A.4, A.6 | Phase 1, Phase 3.S, Phase B-A, préambule / vue d'ensemble, §1.3 étapes types, §5 validation CISSS | règle spécifique |
| CI-TAB-009 | Volets coupe-feu : classe IV, horaire « S » | Fenêtre horaire + pré… | 1 | A.6 | Phase 1, Phase B-A, diagramme, préambule / vue d'ensemble, §5 validation CISSS, §6 NA | règle spécifique |
| CI-TAB-010 | Travaux de structure en entreplafond du secteur R22 : classe IV, horaire « J/S » | Fenêtre horaire + pré… | 1 | A.6 | Phase 1, Phase B-A, diagramme, préambule / vue d'ensemble, §4 conflits, §5 validation CISSS | règle spécifique |
| CI-TAB-011 | Travaux bruyants au RC : coordination à prévoir avec l'établissement (aucune classe ni horaire) | Préalable (coordinati… | 1 | A.6 | Phase 1, Phase B-A, préambule / vue d'ensemble, §5 validation CISSS, §6 NA | règle spécifique |
| CI-TAB-012 | Travaux causant des vibrations au RC : coordination à prévoir avec l'établissement | Préalable (coordinati… | 1 | A.6 | Phase 1, Phase B-A, préambule / vue d'ensemble, §5 validation CISSS, §6 NA | règle spécifique |
| CI-TAB-013 | Entrée des marchandises, conteneurs à déchets et recyclage du CISSS, voie de circulation : con… | Non formulé (renvoi) | NA | A.1 | Phase B-A, diagramme, préambule / vue d'ensemble, §5 validation CISSS, §6 NA | règle spécifique |
| CI-TAB-014 | Entrée principale, voies de circulation et piétonnière, marquise et stationnement : renvoi aux… | Non formulé (renvoi) | 3.S | A.1 | Phase 3.S, Phase B-A, diagramme, préambule / vue d'ensemble, §5 validation CISSS | règle spécifique |
| CI-TAB-015 | Entrées des cliniques externes et de l'oncologie (feux clignotants), marquise et stationnement… | Non formulé (renvoi) | 1 | A.1 | Phase 1, Phase B-A, diagramme, préambule / vue d'ensemble, §4 conflits, §5 validation CISSS | règle spécifique |
| CI-TAB-016 | Entrée et sortie des ambulances, voie de circulation ; sonnette d'urgence publique : renvoi | Non formulé (renvoi) | 3.S | A.1 | Phase 3.N, Phase 3.S, Phase B-A, diagramme, préambule / vue d'ensemble, §5 validation CISSS, §6 NA | règle spécifique |
| CI-TAB-017 | Zone de la roulotte IRM et zone hachurée : renvoi | Non formulé (renvoi) | 1 | A.1 | Phase 1, Phase B-A, diagramme, préambule / vue d'ensemble, §5 validation CISSS | règle spécifique |
| CI-TAB-018 | Terrasse : coordination à prévoir avec l'établissement | Préalable (coordinati… | 3.S | A.7 | Phase 3.S, Phase B-A, diagramme, préambule / vue d'ensemble, §5 validation CISSS | règle spécifique |
| CI-TAB-019 | Nouvelle issue du laboratoire : classe IV, horaire « J » | Fenêtre horaire + pré… | 3.N | B.1.2 | Phase 3.N, Phase B-B, diagramme, préambule / vue d'ensemble, §2.7 variantes, §4 conflits, §5 validation CISSS | règle spécifique |
| CI-TAB-020 | Fenêtres niveau 1, secteurs 101/104/109 (thermos ; cadrage et toile) : classe III, horaire « S… | Fenêtre horaire + pré… | 1, 3.N, 3.S | B.1.2, B.2.1 | Phase 1, Phase 3.N, Phase 3.S, Phase B-B, diagramme, préambule / vue d'ensemble, §1.3 étapes types, §5 validation CISSS | règle spécifique |
| CI-TAB-021 | Fenêtres niveau 1, secteurs 105 à 124 (thermos ; cadrage et toile) : classe II, horaire « J »,… | Fenêtre horaire + pré… | 1, 3.S | B.1.3, B.2.2 | Phase 1, Phase 3.S, Phase B-B, préambule / vue d'ensemble, §1.3 étapes types, §5 validation CISSS | règle spécifique |
| CI-TAB-022 | Travaux bruyants et vibrations au niveau 1 : coordination avec l'établissement | Préalable (coordinati… | 3.N, 3.S | A.6 | Phase 3.N, Phase 3.S, Phase B-A, Phase B-B, préambule / vue d'ensemble, §5 validation CISSS, §6 NA | règle spécifique |
| CI-TAB-023 | Échelle de toiture du niveau 1 vers le niveau 2 : renvoi (texte de cellule inachevé) | Non formulé (renvoi) | 3.N | B | Phase 3.N, Phase B-B, préambule / vue d'ensemble | règle spécifique |
| CI-TAB-024 | Fenêtres niveau 2 (cadrage et toile) : classe III, horaire « J », tous les locaux | Fenêtre horaire + pré… | 2 | C.2 | Phase 2, Phase 2.N, Phase 2.O, Phase 2.S, Phase B-C, diagramme, préambule / vue d'ensemble, §1.3 étapes types, §5 validation CISSS | règle spécifique |
| CI-TAB-025 | Travaux bruyants au niveau 2 (locaux 209/210/211/236) et vibrations (locaux 209/210/211/237) :… | Préalable (coordinati… | 2 | A.6, C.2 | Phase 2, Phase 2.O, Phase B-A, Phase B-C, préambule / vue d'ensemble, §5 validation CISSS | règle spécifique |
| CI-TAB-026 | Porte d'accès, issue no 3 vers toiture 2 ; échelles toiture 2 vers toiture niveau 1 (dont toit… | Non formulé (renvoi) | 1, 2, 3.N | C | Phase 1, Phase 2.O, Phase 3.N, Phase B-C, préambule / vue d'ensemble, §4 conflits | règle spécifique |
| CI-TAB-027 | Fenêtres niveau 3 (cadrage et toile) : classe III, horaire « J » | Fenêtre horaire + pré… | 2 | C.4 | Phase 2, Phase 2.N, Phase 2.O, Phase 2.S, Phase B-C, diagramme, préambule / vue d'ensemble, §1.3 étapes types, §5 validation CISSS | règle spécifique |
| CI-TAB-028 | Travaux bruyants et vibrations au niveau 3 : coordination | Préalable (coordinati… | 2 | A.6, C.4 | Phase 2, Phase 2.O, Phase B-A, Phase B-C, préambule / vue d'ensemble, §5 validation CISSS | règle spécifique |
| CI-TAB-029 | Fenêtres niveau 4 (cadrage et toile) : classe III, horaire « J », groupe PCI 3 | Fenêtre horaire + pré… | 2 | C.5 | Phase 2, Phase 2.O, Phase B-C, diagramme, préambule / vue d'ensemble, §1.3 étapes types, §5 validation CISSS | règle spécifique |
| CI-TAB-030 | Renvoi général à la procédure PCI des conditions générales | Préalable (renvoi ver… | T | T | T (§1.2) | règle spécifique |
| CI-PCI-001 | Classification obligatoire de chaque intervention : groupe de patients à risque (1-4) × type d… | Préalable | 0, T | 0, T | Phase 0, Phase B-A, T (§1.2), §1.3 étapes types, §5 validation CISSS | règle spécifique |
| CI-PCI-002 | Fiche synthèse d'analyse du risque (annexe 1) transmise au service PCI pour les classes III et… | Préalable | 0, T | 0, T | Phase 0, Phase B-A, T (§1.2), §1.3 étapes types, §5 validation CISSS | règle spécifique |
| CI-PCI-003 | Mesures PCI jointes aux documents du projet en précisant types de cloisons, localisation, péri… | Préalable | 0, T | 0, T | Phase 0, T (§1.2), §5 validation CISSS | règle spécifique |
| CI-PCI-004 | Aviser le service PCI de tout changement dans les interventions planifiées | Préavis | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-005 | Équipe pluridisciplinaire formée et convoquée dès la planification (classes III et IV) ; l'arc… | Préalable | 0, T | 0, T | Phase 0, T (§1.2), §4 conflits, §5 validation CISSS | règle spécifique |
| CI-PCI-006 | Circuits et horaire de circulation des matériaux, du personnel, des patients et visiteurs et d… | Préalable + fenêtre h… | T | T | T (§1.2), §5 validation CISSS | règle par défaut (T) |
| CI-PCI-007 | Ouvriers : plans de circulation évitant les aires de soins ; circuit sécuritaire pour les four… | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-008 | Minimiser les déplacements d'air provoqués par un ascenseur ; analyser toutes les circulations… | Préalable | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-009 | Travaux extérieurs et excavation : évaluer les mesures contre l'infiltration de poussière (pro… | Préalable | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-010 | Eau domestique : identifier les conduites touchées, fermer/isoler, désinfecter avant remise en… | Fenêtre horaire + pré… | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-011 | Surveillance du chantier hors des heures ouvrables confiée à un agent de sécurité ou autre per… | Préalable | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-012 | Pouvoir d'interruption des travaux par le service PCI en cas de non-respect des mesures | Interdiction (arrêt) | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-013 | Entretien quotidien en fin de journée, plus fréquent en période de forte génération de poussiè… | Fenêtre horaire (quot… | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-014 | Inspection quotidienne (annexe 3) par le responsable construction et participation aux rencont… | Fenêtre horaire (quot… | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-015 | Pression négative continue 24 h/24, 7 j/7, différentiel de 7,5 Pa (0,03 po ce) ; validation pa… | Interdiction (maintie… | T | T | Phase 1, T (§1.2), §4 conflits | règle par défaut (T) |
| CI-PCI-016 | Filtration absolue (HEPA) avec évacuation directe à l'extérieur, loin de toute prise d'air ; a… | Préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-017 | Écran anti-poussière étanche dalle à dalle (classes III-IV) ; écran rigide en zone passante ou… | Préalable + interdict… | T | T | T (§1.2), §4 conflits | règle par défaut (T) |
| CI-PCI-018 | SAS (antichambre) pour tous les accès entre chantier et zones occupées, avec aspirateur HEPA e… | Préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-019 | Vêtements de protection (combinaison, couvre-chaussures) revêtus avant de sortir du chantier e… | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-020 | Sceller les conduits de distribution, de reprise et d'évacuation dans la zone cloisonnée ; fer… | Préalable | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-021 | Déchets : contenants fermés ou chariot sous bâche humide, élimination quotidienne en début ou… | Fenêtre horaire (quot… | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-022 | Zone des travaux affichée (accès réservé aux personnes autorisées, coordonnées d'urgence du re… | Préalable + interdict… | T | T | T (§1.2) | règle par défaut (T) |
| CI-PCI-023 | Séquence de fin de travaux (classes III-IV) : nettoyage final par l'entrepreneur (annexe 4) pu… | Préalable (séquence i… | 4, T | 4, T | Phase 4, T (§1.2), préambule / vue d'ensemble, §1.3 étapes types, §5 validation CISSS | règle spécifique |
| CI-PCI-024 | Contrôle de la qualité de l'air possible avant la réouverture d'un service ; accréditation par… | Préalable | 4, T | 4, T | Phase 4, T (§1.2), §1.3 étapes types, §5 validation CISSS | règle spécifique |
| CI-PCI-025 | Matériel et équipements médicaux retirés ou protégés avant le début des travaux ; anomalies (p… | Préalable + préavis | T | T | T (§1.2), §1.3 étapes types | règle par défaut (T) |
| CI-PCI-026 | Patients à haut risque identifiés et relocalisés si nécessaire (équipe pluridisciplinaire, cla… | Préalable | T | T | Phase 2.N, T (§1.2), §1.3 étapes types, §5 validation CISSS | règle par défaut (T) |
| CI-CTR-001 | Échéancier contractuel : début des travaux le 31 août 2026, fin le 31 décembre 2027 | Fenêtre (délai contra… | 0 | 0 | Phase 0, préambule / vue d'ensemble, §4 conflits | règle spécifique |
| CI-CTR-002 | Toutes les échéances du contrat sont de rigueur | Interdiction (dépasse… | T | T | T (§1.2) | règle spécifique |
| CI-CTR-003 | Échéancier exposant le phasage, les phases d'acceptation, le cheminement critique, les dates j… | Préalable | 0 | 0 | Phase 0, §4 conflits, §5 validation CISSS | règle spécifique |
| CI-CTR-004 | Échéancier remis au plus tard à la première assemblée de chantier ; mise à jour à chaque deman… | Préavis (livrable) | 0, T | 0, T | Phase 0, T (§1.2), §5 validation CISSS | règle spécifique |
| CI-CTR-005 | Délai de réalisation calculé à compter de l'autorisation de débuter, émise seulement après obt… | Préalable | 0 | 0 | Phase 0, diagramme | règle spécifique |
| CI-CTR-006 | Demande de prolongation écrite dans les 15 jours du début de l'événement (10 jours ouvrables s… | Préavis | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-007 | Ordres de changement exécutés à l'intérieur du délai de réalisation, sans incidence présumée s… | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-008 | Programme de prévention propre au chantier remis au plus tard à la première réunion de chantie… | Préalable | 0 | 0 | Phase 0 | règle spécifique |
| CI-CTR-009 | Prévention des infections nosocomiales pendant toute la durée des travaux (seule clause PCI du… | Interdiction (obligat… | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-010 | Prévention des bruits excessifs affectant le fonctionnement de l'établissement et le bien-être… | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-011 | Minimiser les inconvénients au fonctionnement et aux activités des occupants | Interdiction (obligat… | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-012 | Percements : aviser l'organisme public des percements prévus ; horaires particuliers convenus… | Préavis + fenêtre hor… | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-013 | Déplacements du personnel limités aux exigences des travaux ; port en tout temps de pièces d'i… | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-014 | Suspension des travaux possible en tout temps pour la protection de l'ouvrage, des personnes o… | Interdiction (arrêt) | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-015 | Première réunion convoquée par l'organisme public avant le début des travaux (fréquence des ré… | Préalable + préavis | 0 | 0 | Phase 0 | règle spécifique |
| CI-CTR-016 | Surintendant en présence continue sur le chantier | Interdiction (absence) | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-017 | Coordination avec d'autres entrepreneurs de l'organisme public sans effet sur le délai, sauf d… | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-018 | Installations temporaires (bureau, eau, éclairage, chauffage, électricité, communications) à l… | Préalable | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-019 | Propreté en tout temps du chantier et des lieux avoisinants ; évacuation des eaux, neige et gl… | Interdiction (obligat… | 4, T | 4, T | T (§1.2) | règle spécifique |
| CI-CTR-020 | Inspection par l'organisme public sans préavis, à des heures normales ; accès des professionne… | Fenêtre horaire | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-021 | Matières dangereuses non dénoncées : arrêt des travaux et rapport écrit immédiat ; échéancier… | Interdiction (arrêt)… | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-022 | Avis d'ouverture et de fermeture de chantier à la CNESST ; avis immédiat à l'organisme public… | Préavis | 0, 4 | 0, 4 | Phase 0, Phase 4 | règle spécifique |
| CI-CTR-023 | Déchets : sites de récupération et d'élimination déclarés avant le début des travaux ; interdi… | Préalable + interdict… | 0, T | 0, T | Phase 0, T (§1.2) | règle spécifique |
| CI-CTR-024 | Équipements et accessoires enlevés et non réutilisés offerts au propriétaire ; matériaux à réc… | Préalable | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-025 | Interdiction de communiquer sur le projet (médias, organisations locales) hors de l'organisme… | Interdiction | T | T | T (§1.2) | règle par défaut (T) |
| CI-CTR-026 | Réception : inspection dans les 10 jours ouvrables de la demande ; prise de possession anticip… | Préavis | 4 | 4 | Phase 4, diagramme, §5 validation CISSS | règle spécifique |
| CI-CTR-027 | Ordre de primauté des documents : addenda, contrat, devis, plans et dessins ; le professionnel… | Règle d'interprétatio… | T | T | T (§1.2) | règle par défaut (T) |
