# 05 — Phasage par élévation : méthode, correspondances tranchées, ce qui reste ouvert

Hôpital de Chandler — Réfection de l'enveloppe · CISSS de la Gaspésie · AOC-077221 · Dossier GLCRM R-657-24
Note d'accompagnement du cahier `phasage/plan-phasage-elevations.pdf` (4 planches, échantillon : façade nord et zones de chantier).
Document de travail. Les documents 01 à 04 et le cahier de phasage en plan restent valides ; la présente note ne les remplace pas.

---

## 1. Pourquoi repartir des élévations

Le cahier de phasage en plan (14 planches, feuille 010) répond à la question « dans quel ordre traiter les zones ». Il ne répond pas à celle que se pose l'entrepreneur devant un mur : **qu'est-ce que je dois décrocher, déplacer ou garder en fonction avant de démolir ce parement**.

La réponse est dans des documents organisés par façade et par élévation, pas par zone : le tableau de coordination des équipements électromécaniques de WSP (D5), les élévations d'électromécanique ME001 à ME003, et les élévations d'architecture 201 à 204, qui portent chacune leurs propres notes d'appareils à retirer, toutes renvoyant aux documents d'ingénierie.

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

Conséquences pour les documents antérieurs :

1. **C et D.** Le cahier en plan portait un « ? » sur ces deux repères et les inscrivait en décision à obtenir des architectes (planche 13). Les titres des dessins les tranchent. La décision tombe.
2. **H.** Le cahier en plan le lisait « nord partielle » sur le plan clé de la feuille 011. Le dessin s'intitule « Élévation est partielle » et le tableau D5 code ses quatre lignes en « E » — dont la hotte de médecine nucléaire, déjà rattachée à la face est dans `03-phasage.md`. **La lecture du plan clé était fausse ; la face est est la bonne.**
3. **J et K** n'apparaissaient nulle part dans le cahier en plan.

Ces trois points sont à reporter dans `02-contraintes.md` (Z-24) et dans le cahier en plan une fois la façade nord validée.

## 4. Calage géométrique du calque

- Position horizontale : chaîne d'axes de la feuille 202, entraxes écrits (±7247, ±7113, ±7010… entre les axes 16 et 1, total ±105 927 mm).
- Position verticale : chaîne de niveaux (R00 à 10 000, niveau 100 à 13 952, 200 à 17 901, 300 à 21 559, 400 à 25 202, 500 à 28 882, dessus de parapet à 29 820).
- Les deux chaînes donnent la même échelle, 1:200 — ce qui vérifie le calage.
- **L'axe 1 est à l'ouest, l'axe 16 à l'est.** L'élévation nord se lit donc de l'est (gauche) vers l'ouest (droite). Vérification : la sortie d'arrosage écrite « coin nord-est » tombe vers l'axe 14, et les appareils écrits « porte nord du quai des ambulances » tombent vers l'axe 1, du côté où le plan clé place la sortie d'ambulance.

La position de chaque appareil le long de l'élévation est relevée sur les repères de la feuille ME001(D) : elle est marquée `[lecture]`. **Trois lignes du tableau D5 ne sont dessinées nulle part sur l'élévation et ne sont donc pas positionnées** : N-F-P-002 (déshumidification, « coin nord-est »), N-F-GM-001 (prise d'air de la centrale d'air médical) et N-F-V-003 (évacuation V-53, sans repère propre).

## 5. Façade nord : ce que l'exercice produit

23 lignes du tableau D5 codées « N-F », plus un appareil repéré sur ME001(D) sans ligne au tableau (sortie d'évent murale de laboratoire, note D4 plomberie). Répartition par état :

| État | Lignes |
|---|---|
| Maintenu avec interruption convenue | 15 |
| Maintenu en fonction sans interruption | 3 |
| Déplacé temporairement puis réinstallé | 3 |
| Retiré définitivement | 2 |
| Non touché | 1 |

**Seize verrous** entre les appareils et la séquence d'architecture (E1 à E6 de `03-phasage.md` §1.3) sont détaillés sur la planche 3. Ils se jouent presque tous entre E1 (préparation) et E2 (démolition de l'enveloppe) : les contournements électromécaniques doivent être en place avant la démolition (AR-DEV-058).

Deux d'entre eux sont des **verrous inverses**, où c'est l'architecture qui doit livrer : une alcôve dans le nouveau revêtement pour la sortie d'arrosage encastrée (N-F-P-001), et de nouvelles trappes d'accès de dimensions et de position identiques, sans lesquelles la mécanique du porte-à-faux devient inaccessible (N-F-V-011).

### Un conflit saisonnier interne à la seule façade nord

Trois lignes du tableau se contredisent sur la saison, sur la même façade :

| Ligne | Période écrite |
|---|---|
| N-F-V-005, unité de l'hémodialyse | « Dimanche seulement, **en dehors de la période estivale** » |
| N-F-P-002, déshumidification | arrêt possible « sauf en période estivale » |
| N-F-E-008, clavier de la porte de garage | « **En période estivale** » |

« Période estivale » n'étant définie nulle part (Z-10), la façade nord ne peut pas être traitée d'un seul tenant sans arbitrage du CISSS. Ce conflit n'apparaissait pas dans le découpage par zones : il ne devient visible qu'en regroupant les appareils par façade.

## 6. Zones de chantier et clôtures

Écart central, vérifié sur les feuilles 001 et 002 :

- Les plans ne montrent **qu'une seule configuration de clôture** pour tout le site (feuille 001, note 23, sans mention de phase), plus deux détails d'accès locaux (feuille 002, détail 1 : zone d'ambulance en 2 configurations ; détail 2 : entrée principale en 3).
- Le devis, lui, exige explicitement une gestion par phase : barrières d'accès verrouillables « selon l'aménagement du site et **selon les phasages** » (AR-DEV-190), emplacements des cloisons anti-poussière « durant **chaque phase** des travaux » (AR-DEV-148), choix de l'échafaudage tenant compte « du **phasage** des travaux » (AR-DEV-172), déplacement des supports temporaires « selon le **phasage** » (AR-DEV-155).
- Le plan de chantier par phase est donc un **livrable de l'entrepreneur** (AR-DEV-171 : plan de situation de l'emprise clôturée, des roulottes, des voies d'accès et des détails de clôture), pas une donnée des documents d'appel d'offres (Z-27).

Ne sont dessinés nulle part : implantation de clôture par phase ; zone ou emprise d'échafaudage ; position de grue et aire de levage ; aire d'entreposage ; roulotte et bureau de chantier ; emplacement du conteneur à déchets, alors que le devis renvoie aux plans d'architecture pour le trouver (AR-DEV-225) ; symbole de portail dans la légende, alors que le devis exige des signaleurs à chaque « barrière d'accès au chantier **identifiée aux plans** » (AR-DEV-137).

Une incohérence à lever : le devis situe le bureau de chantier « dans le stationnement étagé existant » (AR-DEV-180) ; la feuille 001 ne montre que des stationnements de surface.

**Trois numérotations « phase 1/2/3 » coexistent sans lien écrit** : les phases du plan clé de la feuille 010 (secteurs du bâtiment), les configurations d'accès de la feuille 002 (ambulance, marquise), et les phases du tableau du CISSS (niveaux). C'est le constat C-34. La planche de zones de chantier par phase se construit une fois cette correspondance tranchée.

## 7. Défaut relevé dans le tableau D5

Deux lignes consécutives de la page 6 portent le même code **N-F-E-006** (luminaire mural, puis lecteur de carte de la porte piéton nord du quai des ambulances). La seconde a le même contenu que la ligne **N-F-E-007** de la page 7. Numérotation à corriger ou doublon à retirer — à confirmer par WSP.

## 8. Ce qui reste à faire

1. Retour sur la façade nord et sur la planche de zones de chantier avant de produire les façades est, sud et ouest.
2. Reporter dans `02-contraintes.md` et dans le cahier en plan les trois correspondances tranchées (C, D, H) et les deux repères ajoutés (J, K).
3. Obtenir de WSP : le tracé et la forme des conduits temporaires de l'unité d'hémodialyse et les fenêtres d'interruption (Z-29) ; la position de la prise d'air de la centrale d'air médical, placée sur l'élévation F par le tableau sans qu'aucun repère ne la montre ; la correction du doublon N-F-E-006.
4. Obtenir du CISSS la définition de « période estivale » (Z-10) et l'arbitrage du conflit saisonnier de la façade nord.
5. Obtenir des architectes la correspondance entre les trois numérotations de phases (C-34), sans laquelle la planche de zones de chantier par phase ne peut pas être dessinée.

---

*Sources : D2 feuilles 001, 002, 201, 201-A, 202, 203, 204 ; D4 ME001(D), ME001, ME002(D), ME002, ME003(D), ME003, ME004(D), ME014 ; D5 tableau de coordination des équipements électromécaniques (93 lignes, révision du 11 mai 2026) ; D1 sections 01 51 00, 01 52 00, 01 56 00 ; `analyse/02-contraintes.md` ; `analyse/03-phasage.md` §1.3.*
