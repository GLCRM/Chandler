# 05 — Phasage par élévation : les quatre façades, les verrous, le calendrier

Hôpital de Chandler — Réfection de l'enveloppe · CISSS de la Gaspésie · AOC-077221 · Dossier GLCRM R-657-24
Note d'accompagnement du cahier `phasage/plan-phasage-elevations.pdf` (14 planches).
Document de travail. Les documents 01 à 04 et le cahier de phasage en plan restent valides ; la présente note ne les remplace pas.

---

## 1. Pourquoi repartir des élévations

Le cahier de phasage en plan (14 planches, feuille 010) répond à la question « dans quel ordre traiter les zones ». Il ne répond pas à celle que se pose l'entrepreneur devant un mur : **qu'est-ce que je dois décrocher, déplacer ou garder en fonction avant de démolir ce parement**.

La réponse est dans des documents organisés par façade et par élévation, pas par zone : le tableau de coordination des équipements électromécaniques de WSP (D5), les élévations d'électromécanique ME001(D) à ME003(D), et les élévations d'architecture 201, 201-A, 202, 203 et 204, qui portent chacune leurs propres notes d'appareils à retirer, toutes renvoyant aux documents d'ingénierie.

## 2. Le pivot : le tableau de coordination est déjà indexé par élévation

Les notes générales 1 et 2 du tableau D5 (révision du 11 mai 2026) l'écrivent :

> « 1. Orientation façade : Nord, Sud, Est, Ouest »
> « 2. Numérotation élévation : Se référer aux bulles d'élévations en architecture et ingénierie (A à I) »

Chaque ligne du tableau porte donc un code `Façade-Élévation-Discipline-Numéro` : `N-F-V-005` = façade nord, élévation F, ventilation, ligne 5. **93 lignes** au total, réparties ainsi :

| Façade | Lignes | Élévations |
|---|---|---|
| Sud | 30 | A |
| Ouest | 25 | B (14), C (5), E (4), I (2) |
| Nord | 23 | F |
| Est | 15 | G (10), H (4), D (1) |

Par discipline : électricité 56, ventilation 30, plomberie 5, gaz médicaux 1, protection incendie 1.

Le tableau ajoute trois états par couleur de cellule : gris « équipement non touché par les travaux » (11 lignes), orange « équipement à démanteler, non utilisé » (2), jaune « à valider avec le propriétaire » (3).

**Les 93 lignes sont toutes reprises dans le cahier**, chacune positionnée sur son élévation ou signalée comme non repérable.

## 3. Les onze repères d'élévation, et trois correspondances tranchées

Les titres des dessins écrivent la façade de chaque repère. Ils ne sont plus à lire sur le plan clé.

| Repère | Titre du dessin | Démolition | Construction | Façade (tableau D5) | Statut par rapport au cahier en plan |
|---|---|---|---|---|---|
| A | Élévation sud | 201 | 203 | Sud | confirmé |
| B | Élévation ouest | 201 | 203 | Ouest | confirmé |
| C | Élévation ouest partielle | 201-A | 203 | Ouest | **« ? » tranché : ouest** |
| D | Élévation est partielle | 201-A | 203 | Est | **« ? » tranché : est** |
| E | Élévation ouest partielle | 201-A | 203 | Ouest | confirmé |
| F | Élévation nord | 202 | 204 | Nord | confirmé |
| G | Élévation est | 202 | 204 | Est | confirmé |
| H | Élévation est partielle | 201-A | 204 | Est | **lu « nord partielle » — corrigé : est** |
| I | Élévation ouest partielle | 201-A | 204 | Ouest | confirmé |
| J | Élévation sud partielle | 201-A | 203 | — | **absent du cahier en plan** |
| K | Élévation ouest partielle | 201-A | 204 | — | **absent du cahier en plan** |

Conséquences pour les documents antérieurs, reportées dans `02-contraintes.md` (Z-24) :

1. **C et D.** Le cahier en plan portait un « ? » sur ces deux repères et les inscrivait en décision à obtenir des architectes. Les titres des dessins les tranchent. La décision tombe.
2. **H.** Le cahier en plan le lisait « nord partielle » sur le plan clé de la feuille 011. Le dessin s'intitule « Élévation est partielle » et le tableau D5 code ses quatre lignes en « E » — dont la hotte de médecine nucléaire, déjà rattachée à la face est dans `03-phasage.md`. **La lecture du plan clé était fausse ; la face est est la bonne.**
3. **J et K** n'apparaissaient nulle part dans le cahier en plan.

## 4. Calage géométrique du calque

- Position horizontale : deux chaînes d'axes. Chaîne numérique **1 à 16** pour les élévations nord et sud (entraxes écrits ±7010 x 8, 4318, 2692, 7417, 7036, 7010, 7010, 7113, 7247 ; total ±105 927 mm). Chaîne lettrée **A à I** pour les élévations est et ouest (5437, 2615, 3811, 2997, **303**, 4064, 2946, 6426, 578, 5721, 1296, 7264 ; total ±43 459 mm).
- Position verticale : chaîne de niveaux commune (sous-sol S00 à 5 442, R00 à 10 000, niveau 100 à 13 952, 200 à 17 901, 300 à 21 559, 400 à 25 202, 500 à 28 882, dessus de parapet à 29 820).
- Échelle : **1:200 exact**, soit 70,556 mm par unité de page. Les deux chaînes donnent la même échelle sur les quatre élévations, dans les deux sens — c'est ce qui vérifie le calage.
- Un point de détail qui comptait : **D.1' est à 303 mm de D.1**, et non à mi-chemin entre D.1 et D.2. C'est la seule répartition qui redonne le total ±43 459 mm imprimé sur les feuilles 201 et 202.
- Orientations vérifiées : l'axe 1 est à l'ouest et l'axe 16 à l'est ; l'axe A est au nord et l'axe I au sud. L'élévation nord se lit donc de l'est (gauche) vers l'ouest (droite), l'élévation sud de l'ouest vers l'est, l'élévation ouest du nord vers le sud, l'élévation est du sud vers le nord.

La position de chaque appareil le long de son élévation est relevée sur les repères des feuilles ME : elle est marquée `[lecture]`. **Un appareil que le dessin ne montre nulle part n'est jamais positionné** : il est signalé comme tel. Cinq lignes sont dans ce cas — N-F-P-002, N-F-V-003, N-F-GM-001, E-D-V-001 et S-A-E-001.

## 5. Les quatre façades

101 appareils relevés en tout : les 93 lignes du tableau, plus 8 appareils repérés sur les dessins ME **sans aucune ligne au tableau**.

| Façade | Appareils | Dont sans ligne au tableau | Verrous | Retiré | Déplacé | Interrompu | Sans interruption | Non touché |
|---|---|---|---|---|---|---|---|---|
| Nord (F) | 24 | 1 | 16 | 2 | 3 | 15 | 3 | 1 |
| Est (G, H, D) | 15 | 0 | 9 | 2 | 0 | 11 | 0 | 2 |
| Sud (A) | 33 | 3 | 15 | 2 | 8 | 17 | 0 | 6 |
| Ouest (B, C, E, I) | 29 | 4 | 14 | 0 | 9 | 16 | 2 | 2 |

### 5.1 Façade nord — élévation F

Seize verrous, presque tous entre E1 (préparation) et E2 (démolition de l'enveloppe) : les contournements électromécaniques doivent être en place avant la démolition (AR-DEV-058).

Deux d'entre eux sont des **verrous inverses**, où c'est l'architecture qui doit livrer : une alcôve dans le nouveau revêtement pour la sortie d'arrosage encastrée (N-F-P-001), et de nouvelles trappes d'accès de dimensions et de position identiques, sans lesquelles la mécanique du porte-à-faux devient inaccessible (N-F-V-011).

Un conflit saisonnier interne à la seule façade : N-F-E-008 (clavier de la porte de garage) est écrit « en période estivale », N-F-V-005 (unité d'hémodialyse) « dimanche seulement, en dehors de la période estivale », et N-F-P-002 (déshumidification) « oui, sauf en période estivale ». Ce conflit n'apparaissait pas dans le découpage par zones : il ne devient visible qu'en regroupant les appareils par façade.

### 5.2 Façade est — élévations G, H et D

**Un bandeau lumineux continu commande toute la façade.** Les lignes E-G-E-001 à 004 ne sont pas quatre appareils ponctuels mais un éclairage linéaire continu sous parapet, sur la tour et sur le basilaire, avec son conduit d'alimentation, hors service pendant toute la durée des travaux du secteur traité. Sur une façade de cette longueur, la longueur du tronçon attaqué d'un coup détermine directement l'étendue laissée sans éclairage extérieur la nuit.

**Deux interruptions sont bornées à la semaine hors période estivale** — le bi-bloc de la salle de traitement d'eau de l'hémodialyse (E-G-V-003) et le câblage du bi-bloc de la salle des serveurs (E-G-E-006), deux locaux critiques. Elles tombent au même endroit de l'élévation, entre les axes F et E au niveau 200 : **une seule fenêtre peut servir aux deux** si elles sont coordonnées.

### 5.3 Façade sud — élévation A

**Tout se joue à l'ouest de l'axe 1.** Treize des trente-trois appareils sont concentrés sous et autour de la marquise de l'entrée des ambulances, dans une bande de moins de six mètres qui déborde la trame numérotée : la seule ligne de protection incendie de tout le tableau (gicleurs à mettre hors service, glycol à récupérer, deux coupures de 2 h), l'enseigne AMBULANCE, l'unité bi-bloc du prélèvement d'urgence, les évents de vapeur de l'autoclave et de la chaufferie, et les six lignes grises du groupe D4. C'est le mètre linéaire de façade le plus chargé du projet.

Trois travaux réels n'ont aucune ligne au tableau (voir §8). Six lignes grises correspondent à sept cibles identiques sur le dessin, non départageables.

### 5.4 Façade ouest — élévations B, C, E et I

**La façade ouest porte les plus gros travaux temporaires du chantier.** Deux conduits de prise d'air frais de 900 x 900 mm, montant du niveau 100 au niveau 300 sur toute la largeur D.1'–D.2, doivent être installés et raccordés au plénum sous le soffite **avant** de toucher au parement derrière le conduit existant du bloc opératoire — et l'installation elle-même est écrite « en plusieurs étapes ». Cette installation provisoire n'apparaît nulle part dans le découpage en plan.

**L'unité d'hémodialyse est ici aussi.** La note D7 ventilation de ME001(D) la repère sur l'élévation ouest avec sa passerelle d'aluminium et ses trois conduits, alors que le tableau ne la porte qu'au nord (N-F-V-005). Les conduits traversent le parement de part et d'autre de l'angle nord-ouest : **le nord et l'ouest ne peuvent pas être planifiés séparément sur ce point** (Z-29).

**Le seul verrou hivernal du projet** est ici : le thermostat Pyrotenax et son câble chauffant (O-B-E-001), « en dehors de la période hivernale », durée écrite en **mois**. Sur la même façade, la persienne du garage des ambulances (O-B-V-004) est écrite « en période estivale ». La façade ouest est une façade de belle saison.

**Un verrou inverse** : l'unité bi-bloc de la salle d'observation se réinstalle « sur le garde-corps modifié » — le garde-corps G-02 de la feuille 703 doit donc être posé avant (AR-PLN-070).

## 6. Calendrier de travail et fenêtres saisonnières

| Ce qui fixe le calendrier | Source | Ce que cela donne |
|---|---|---|
| Installation de chantier en novembre 2026 ; travaux de janvier 2027 à décembre 2028 | Donnée de travail GLCRM `[choix]` | Environ 24 mois de travaux effectifs après un mois d'installation |
| Échéancier du contrat : début le 31 août 2026, fin le 31 décembre 2027 | D8 annexe 0.01.13 — CI-CTR-001 | Dates jugées inapplicables en l'état : le début contractuel précède l'émission des plans pour soumission (C-14) |
| « Période estivale » : de la mi-juin à la mi-août, approximativement du 24 juin au 15 août | Définition de travail GLCRM `[choix]` — à confirmer avec le CISSS (Z-10) | **Deux fenêtres estivales** dans la période : 24 juin – 15 août 2027 et 24 juin – 15 août 2028, environ 7,5 semaines chacune |
| « Période hivernale » : aucune définition écrite | Z-10 | Une seule ligne du tableau s'y réfère (O-B-E-001) |

Huit lignes du tableau sont bornées par une saison :

| Ligne | Façade | Ce que le tableau écrit | Sens |
|---|---|---|---|
| N-F-E-008 | Nord | « En période estivale » | **Exige l'été** |
| O-B-V-004 | Ouest | « Travailler avec persienne en fonction. En période estivale » | **Exige l'été** |
| N-F-V-005 | Nord | « Dimanche seulement, en dehors de la période estivale » | Exclut l'été |
| N-F-P-002 | Nord | Colonne durée : « Oui, sauf en période estivale » | Exclut l'été |
| E-G-V-003 | Est | « Semaine, en dehors de la période estivale » | Exclut l'été |
| E-G-E-006 | Est | « Semaine, en dehors de la période estivale » | Exclut l'été |
| S-A-V-001 | Sud | « En dehors de la période estivale (Quelques jours en été) » | **Contradictoire en elle-même** |
| O-B-E-001 | Ouest | « En dehors de la période hivernale » — durée écrite : « Mois » | Seule ligne **hivernale** |

**Conséquence.** Les deux lignes qui exigent l'été doivent tomber dans l'une des deux fenêtres. Or N-F-E-008 est sur la façade nord, comme N-F-V-005 et N-F-P-002 qui l'excluent : **la façade nord ne peut pas être traitée d'un seul tenant** et se scinde en au moins deux passages, de part et d'autre d'une fenêtre estivale. Avec deux fenêtres disponibles au lieu d'une, cette scission est tenable — elle ne l'était pas dans la période écrite au contrat.

## 7. Zones de chantier et clôtures

Écart central, vérifié sur les feuilles 001 et 002 :

- Les plans ne montrent **qu'une seule configuration de clôture** pour tout le site (feuille 001, note 23, sans mention de phase), plus deux détails d'accès locaux (feuille 002, détail 1 : zone d'ambulance en 2 configurations ; détail 2 : entrée principale en 3).
- Le devis exige explicitement une gestion par phase : barrières d'accès verrouillables « selon l'aménagement du site et **selon les phasages** » (AR-DEV-190), emplacements des cloisons anti-poussière « durant **chaque phase** des travaux » (AR-DEV-148), choix de l'échafaudage tenant compte « du **phasage** des travaux » (AR-DEV-172), déplacement des supports temporaires « selon le **phasage** » (AR-DEV-155).
- Le plan de chantier par phase est donc un **livrable de l'entrepreneur** (AR-DEV-171), pas une donnée des documents d'appel d'offres (Z-27).

Ne sont dessinés nulle part : implantation de clôture par phase ; zone ou emprise d'échafaudage ; position de grue et aire de levage ; aire d'entreposage ; roulotte et bureau de chantier ; emplacement du conteneur à déchets, alors que le devis renvoie aux plans d'architecture pour le trouver (AR-DEV-225) ; symbole de portail dans la légende, alors que le devis exige des signaleurs à chaque « barrière d'accès au chantier **identifiée aux plans** » (AR-DEV-137).

Une incohérence à lever : le devis situe le bureau de chantier « dans le stationnement étagé existant » (AR-DEV-180) ; la feuille 001 ne montre que des stationnements de surface.

**Trois numérotations « phase 1/2/3 » coexistent sans lien écrit** : les phases du plan clé de la feuille 010 (secteurs du bâtiment), les configurations d'accès de la feuille 002 (ambulance, marquise), et les phases du tableau du CISSS (niveaux). C'est le constat C-34. La planche de zones de chantier par phase se construit une fois cette correspondance tranchée.

## 8. Défauts documentaires relevés en lisant les quatre élévations

| Défaut | Où | Conséquence |
|---|---|---|
| Deux lignes consécutives portent le même code **N-F-E-006** | Tableau D5, page 6 | La seconde a le même contenu que N-F-E-007 : doublon ou numérotation à corriger |
| Unité de ventilation de l'hémodialyse et sa passerelle repérées sur l'élévation ouest, **sans aucune ligne O-B** | ME001(D) note D7 ventilation | L'intervention la plus lourde de l'angle nord-ouest n'a pas de fenêtre écrite côté ouest |
| Thermostat des câbles chauffants repéré au sud, **sans ligne S-A-E** | ME002(D) note D14 électricité | Travail d'électricité réel, sans arrêt ni période écrits |
| Évents de vapeur de la chaufferie : **trois annoncés** (150, 150 et 200 mm), **un seul dessiné** | ME002(D) note D3 plomberie | Quantité non fixée, aucune ligne au tableau |
| Évents de l'autoclave dessinés sur l'élévation sud, rattachés par écrit à la façade ouest | ME002(D) note D2 plomberie ; D5 O-B-P-001 | Verrou inter-façades invisible dans un découpage par zones |
| Persienne de prise d'air frais du service alimentaire repérée à l'ouest, sans ligne | ME001(D) notes D10 et D17 ventilation | Registre coupe-feu à ajouter, sans fenêtre écrite |
| Sectionneur de thermopompe du repère D, sans ligne | ME003(D) repère D note D6 électricité | Aucune fenêtre écrite |
| Enseigne « ambulance urgence » du repère E, sans ligne | ME003(D) repère E note D5 électricité | Aucune fenêtre écrite |
| **E-G-E-006** : le tableau écrit « salle des serveurs », le dessin accole la bulle à l'unité LG du toit | D5 contre ME002(D) | Localisation incertaine d'un arrêt en local critique |
| **E-G-V-001 et 002** : le tableau écrit « persienne à relocaliser », la note dit « démanteler complètement, aucune remise en service » | D5 contre ME002(D) note D5 ventilation | Nature de l'intervention non fixée |
| **E-G-V-003** : le tableau écrit « supports muraux », la note dit « support au toit » | D5 contre ME002(D) note D7 ventilation | Nature du support non fixée |
| **O-B-V-002** : le tableau écrit « persienne à relocaliser », la note dit « à remplacer par une persienne moins large » | D5 contre ME001(D) note D16 ventilation | Nature de l'intervention non fixée |
| Le repère D de ME003(D) ne porte aucune ligne d'axe | ME003(D) | E-D-V-001 n'est pas positionnable sur une élévation |
| Groupe D4 de l'élévation sud : sept cibles identiques pour six lignes grises | ME002(D) note D4 électricité | Aucune des six lignes n'est identifiable individuellement |
| Zone grise d'environ 1,47 x 1,17 m au-dessus de la marquise des ambulances, pointée par une 2e bulle D1 ventilation, alors que l'unité décrite est repérée 4 m plus bas ; la feuille 201 y porte sa note 24 « conduit de ventilation existant à démolir » | ME002(D) et D2 feuille 201 | Ce que représente cette zone n'est pas déterminable `[à confirmer]` |
| Numéros de persiennes P-01 à P-18 portés aux dessins sans nomenclature retrouvée dans le jeu | ME001(D), ME002(D), ME003(D) | L'appariement repose sur la concordance des dimensions mesurées `[lecture]` |

Deux points d'appariement restent indéterminables sur les feuilles ME et demandent le plan du niveau 100 : lequel des deux couples luminaire / lecteur de l'élévation ouest dessert le laboratoire et lequel dessert le bloc opératoire (O-B-E-002 à 005), et laquelle des deux persiennes D4 du repère C est l'échangeur et laquelle l'évacuation de toilette (O-C-V-001).

## 9. Ce que le tableau commande sur l'ordre des façades

Les seules dépendances écrites entre façades sont électromécaniques :

- la prise d'air médical temporaire se pose sur la façade ouest pour permettre les travaux de la façade nord (ME-065) et se réinstalle après le revêtement nord (ME-067) ;
- les conduits temporaires de l'hémodialyse précèdent la démolition des façades nord et ouest au niveau 200 (ME-049, Z-29) ;
- les évents des autoclaves sont relocalisés avant le début de la façade ouest (ME-075), alors qu'ils sont dessinés sur l'élévation sud ;
- le conduit de la hotte de médecine nucléaire est modifié pour permettre la façade est (ME-118).

Aucune de ces règles ne vient de l'architecture : **c'est l'électromécanique qui ordonne les façades**, ce que la vue en plan ne montrait pas.

## 10. Ce qui reste à faire

1. Obtenir du CISSS la confirmation de la période estivale retenue (mi-juin à mi-août) et l'arbitrage du conflit interne de la façade nord, ainsi que le sens de S-A-V-001.
2. Faire lever par WSP les seize défauts du §8, en priorité le rattachement de l'unité d'hémodialyse côté ouest et les trois travaux de la façade sud sans ligne au tableau.
3. Obtenir de WSP le tracé et la forme des conduits temporaires de l'unité d'hémodialyse, la séquence de basculement et les fenêtres d'interruption (Z-29).
4. Obtenir des architectes la correspondance entre les trois numérotations de phases (C-34), sans laquelle la planche de zones de chantier par phase ne peut pas être dessinée.
5. Reporter dans le cahier de phasage en plan les trois correspondances tranchées (C, D, H) et les deux repères ajoutés (J, K).
6. Arbitrer avec l'entrepreneur la longueur des tronçons traités d'un coup : c'est elle qui fixe la durée d'indisponibilité des 47 lignes marquées « toute la durée des travaux ».

---

*Sources : D2 feuilles 001, 002, 201, 201-A, 202, 203, 204 ; D4 ME001(D), ME001, ME002(D), ME002, ME003(D), ME003, ME004(D), ME014 ; D5 tableau de coordination des équipements électromécaniques (93 lignes, révision du 11 mai 2026) ; D8 annexe 0.01.13 ; D1 sections 01 51 00, 01 52 00, 01 56 00 ; `analyse/02-contraintes.md` ; `analyse/03-phasage.md` §1.3.*
