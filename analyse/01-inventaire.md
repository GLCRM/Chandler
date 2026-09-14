# 01 — Inventaire des documents

Projet GLCRM R-657-24 — Hôpital de Chandler, réfection de l'enveloppe — appel d'offres AOC-077221 (Santé Québec – CISSS de la Gaspésie)
Session 1 — inventaire et extraction des contraintes. Date de l'inventaire : 2026-09-14.

## 0. Portée et méthode

- Le dépôt contient **50 fichiers à la racine** (49 PDF, 1 xlsx ; ~214 Mo). Il n'existe pas d'arborescence `docs/architecture`, `docs/electromecanique`, `docs/cisss` : la répartition par corpus ci-dessous est la nôtre, fondée sur l'émetteur, le numéro de dossier et le préfixe des noms de fichiers.
- Extraction : texte natif (PyMuPDF) pour 28 PDF ; **OCR** (tesseract 5, français, 300 ppp) pour les 22 PDF scannés du CISSS (141 pages : contrat et régie) ; lecture cellule par cellule du xlsx (openpyxl). Les textes extraits, index et images de travail sont dans un répertoire temporaire de session et ne sont pas versionnés.
- Convention de pagination : « p. PDF n » désigne la page physique du fichier. Les devis portent en plus une pagination interne par section (« Page n de N ») ; le contrat et la régie portent « Page x de 104 » et « Page x de 37 ».
- Confidentialité : plusieurs fichiers contiennent des noms et coordonnées de personnes (sommaire de la régie p. 2 ; cartouches et annexe 1 des documents WSP ; propriétés du fichier xlsx). Ils ne sont reproduits ni ici ni dans `02-contraintes.md`.
- Le texte des feuilles de plans (format 36 × 24 po) est extractible mais désordonné (colonnes mélangées) ; il a servi au repérage par mots-clés, la lecture fidèle des notes s'est faite sur rendu image.

## 1. Fiche projet telle qu'écrite dans les documents

| Élément | Libellé(s) rencontré(s) | Source |
|---|---|---|
| Titre du projet | « Hôpital de Chandler – Réfection de l'enveloppe » | Devis archi p. 1 ; devis ME p. 3 ; frontispices des plans archi, ME, ST |
| | « Remplacement du revêtement extérieur – Hôpital de Chandler (Travaux de construction uniquement) » | Contrat p. 1 ; régie p. 1 (OCR) |
| Adresse | « 451 rue Mgr-Ross, Chandler, QC » / « 451 rue Ross Est, Chandler » | Frontispice ME / frontispice ST (S000) — libellés différents |
| Donneur d'ouvrage | « Santé Québec – CISSS de la Gaspésie » ; « CISSS de la Gaspésie » ; « Santé Québec Gaspésie » | Contrat et régie / devis archi / devis et plans ME, S000 |
| Appel d'offres | No AOC-077221 | Tous les documents |
| Architectes | Consortium GLCRM \| Proulx Savard, dossier « GLCRM R657-24 / PS 24-108 » | Devis archi (pied de page) ; cartouche plans archi « 24-108 / R657-24 » |
| Ingénieurs | WSP Canada inc. — mécanique-électricité no CA0066110.3235 ; structure no CA0062562.5541 | Devis et plans ME ; plans ST |
| Référence client citée par WSP | « V/Réf. : R674-24 / 24-108 » | Devis ME (en-tête de chaque page) ; S000 « PROJET CLIENT : R674-24 / 24-108 » — **écart avec R657-24** |
| Émissions du devis archi | 01 « Définitif (60 %) pour approbation » 2026-05-14 ; 02 « Pour commentaire 100 % définitif » 2026-08-21 ; 03 « Pour appel d'offres » 2026-09-04 | Devis archi p. 3, tableau des révisions |
| Émissions du devis ME | A 2026-05-14 « Définitifs 60 % pour approbation » ; B 2026-08-21 « Définitifs 100 % pour approbation » ; 1 2026-09-04 « Définitifs pour soumission » | Devis ME p. 5, registre des révisions |
| Émission des plans | « Définitifs pour soumission », 4 septembre 2026 (archi, ME, ST) | Frontispices |
| Documents d'appel d'offres du CISSS | Contrat et régie : « date d'impression 26-04-13 ». La régie annonce : émission de l'appel d'offres 12 juin 2026, séance d'information 22 juin 2026, réception des soumissions 13 juillet 2026 à 10 h, contrat ferme, adjudication au prix le plus bas | Régie p. 2 « Sommaire » (OCR) — **antérieur à l'émission des plans et devis du 2026-09-04** |
| Procédure PCI | PDF créé le 2026-08-21 (métadonnées) | PCI_CISSS_CA.pdf |
| Tableau des contraintes opérationnelles | version « v3 » (nom de fichier), dernière modification 2026-09-01 (propriétés) | xlsx |

## 2. Synthèse des documents (11 documents, 50 fichiers)

| # | Document | Fichier(s) | Corpus | Émetteur | Émission / date | Pages | Extraction | Remarques d'inventaire |
|---|---|---|---|---|---|---|---|---|
| D1 | Devis technique – architecture | `R657-24 Devis Appel-d'offres 2026-09-04.pdf` | Architecture | GLCRM \| Proulx Savard | Rév. 03, 2026-09-04 (PDF créé 2026-09-04) | 585 | Texte natif | 53 sections (divisions 00 à 32) + page titre et page des sceaux ; index en annexe C |
| D2 | Plans – architecture | `R657-24 Plans Appel-doffres 2026-09-04_Partie1.pdf` à `_Partie16.pdf` | Architecture | GLCRM \| Proulx Savard | Définitifs pour soumission, 4 septembre 2026 | 79 (78 feuilles + frontispice) | Texte natif vectoriel, désordonné | 16 fichiers de 5 pages (Partie16 : 4). Ordre des feuilles = ordre de la liste des plans ; correspondance en annexe A |
| D3 | Devis – mécanique et électricité | `CA0066110.3235_Devis_ME_Définitifs_pour_soumission.pdf` | Électromécanique | WSP | Rév. 1, 2026-09-04 (PDF créé 2026-09-03) | 231 | Texte natif | 50 sections (divisions 00, 20 à 26) + annexe 1 (fiches et listes de dessins d'atelier, p. 223-231) ; index en annexe D |
| D4 | Plans – mécanique et électricité | `20260904_CA0066110.3235_Plans ME_Soumission_PDF fusionné.pdf` | Électromécanique | WSP | 2026/09/04 (cartouches des feuilles : « avril 2026 ») | 24 (23 feuilles + frontispice) | Texte natif, désordonné | Feuille **G003 « Tableau de coordination des équipements électromécaniques (à venir) » listée mais absente** ; correspondance en annexe B |
| D5 | Tableau des équipements électromécaniques | `20260511_CA0066110.3235_Chandler_Tableau des équipements MÉ.pdf` | Électromécanique | WSP | 2026-05-11 (nom de fichier et métadonnées) | 8 | Texte natif | Daté du stade « 60 % » ; rapport avec G003 « à venir » à préciser (voir 4.3) |
| D6 | Plans – structure | `CA0062562.5541_20260904_Plans ST_Définitifs pour soumission_Partie1.pdf` à `_Partie5.pdf` | Structure | WSP | 2026-09-04 | 22 (22 feuilles) | Texte natif, désordonné | **S001 « Plan d'implantation » listé sur S000 mais absent** ; aucun devis de structure dans le dépôt ; correspondance en annexe E |
| D7 | Porte-documents – structure | `CA0062562.5541_20260904_Plans ST_Définitifs pour soumission_Porte-documents.pdf` | Structure | WSP | 2026-09-08 (métadonnées) | 1 page conteneur + 22 PDF joints | Pièces jointes extraites | Portfolio PDF ; les 22 pièces (S000 à S414) ont un texte identique aux 22 pages de D6, à un marqueur « SIGN » près sur chaque feuille (version signée). **Doublon** de D6 |
| D8 | Contrat (conditions générales) de l'appel d'offres | `Construction Contrat-OAC077221_Partie1.pdf` à `_Partie21.pdf` | CISSS | Santé Québec – CISSS de la Gaspésie | Impression 2026-04-13 | 104 (21 × 5, Partie21 : 4) | **Scanné – OCR** | Page PDF globale = (N − 1) × 5 + page de la partie ; pied de page « Page x de 104 ». Table des matières p. 2-4 |
| D9 | Régie de l'appel d'offres | `Construction Régie-AOC-077221.pdf` | CISSS | Santé Québec – CISSS de la Gaspésie | Impression 2026-04-13 (PDF créé 2026-05-26) | 37 | **Scanné – OCR** | Sommaire p. 2 (dates de l'appel d'offres, mode d'adjudication) ; table des matières p. 3-4 |
| D10 | Procédure de prévention et contrôle des infections en construction | `PCI_CISSS_CA.pdf` | CISSS | CISSS de la Gaspésie | PDF créé 2026-08-21 | 24 | Texte natif | Référencée par le xlsx (« Consulter la procédure PCI des Conditions générales ») |
| D11 | Tableau des contraintes opérationnelles de l'établissement | `Tableau des contraintes opérationnelles de l'établissementv3.xlsx` | CISSS | CISSS de la Gaspésie | v3, modifié 2026-09-01 | 1 feuille « Table 1 », 43 lignes × 24 colonnes | Cellules | 38 lignes de données (L4-L41), 2 notes (L42-L43) ; plusieurs colonnes jamais remplies (voir 6.4) |

## 3. Corpus architecture

### 3.1 Devis d'architecture (D1)

- Structure : page titre (p. 1, « Enveloppe extérieure – Devis technique – Architecture »), page des sceaux (p. 2), table des matières 00 01 10 (p. 3-5) puis 53 sections. L'index complet section → pages PDF figure en annexe C.
- La table des matières annonce 55 entrées ; toutes les sections listées sont présentes et leurs nombres de pages concordent avec le contenu. Trois écarts de libellé : la TDM dit « 00 08 00 – Conditions administratives particulières » alors que l'en-tête de section dit « Clauses administratives particulières » ; la TDM dit « 01 35 00 – Procédures spéciales bpfc - biosl » et l'en-tête « Procédures spéciales (BPF / BIOSL) » ; coquille « DIVITION 12 » (p. 5).
- La TDM porte la mention : « Prendre note que les exigences prévues au document Division 01 – Exigences générales – architecture et ingénierie, émis par le Professionnel de la construction en architecture, s'appliquent au présent devis. » (p. 4). La Division 01 du présent devis (p. 13-159) en tient lieu ; aucun document distinct portant ce titre n'est dans le dépôt.
- Sections directement liées au séquencement et à l'exploitation : 00 08 00 (p. 6-12), 01 11 00 (13-16), 01 14 00 Restrictions visant les travaux (17-19), 01 32 16.19 Ordonnancement (20-27), 01 35 29 Santé-sécurité (38-63), 01 35 46 Qualité de l'air intérieur (64-71), 01 51 00 Services temporaires (79-92), 01 52 00 Installation de chantier (93-99), 01 56 00 Protections temporaires (100-103), 01 56 50 Prévention des infections (104-115), 02 41 19.13 Démolition sélective (160-166), 02 81 00 Matières dangereuses (167-172), 07 84 00 Protection coupe-feu (369-383), 08 33 23 Volets coupe-feu (413-421).

### 3.2 Plans d'architecture (D2)

- 78 feuilles réparties en séries : 000 plan du site (001, 002, 005) ; 010 phasage (010, 011 – identification des zones de travaux) ; 050 démolition des niveaux (050-054) ; 100 construction des niveaux (100-104) ; 200 élévations (201, 201-A, 202-205) ; 300 toitures et soffites (301-306) ; 400 coupes de murs types (400-407) ; 410 coupes agrandies (410-422) ; 450 détails en plan (451-455) ; 500 fenêtres et murs-rideaux (501-513) ; 600 portes (601-607) ; 700 métaux ouvrés (701-705).
- Niveaux nommés dans les titres : sous-sol, rez-de-chaussée, niveaux 100, 200, 300 et 400 (la structure ajoute un « niveau 500 » sur S204).
- Cartouche des feuilles : mention « Ne doit pas servir à l'exécution » relevée dans le texte extrait des feuilles (à mettre en regard de « Définitifs pour soumission » au frontispice — cohérent avec une émission pour soumission).
- Feuilles clés pour le séquencement : 002 (gestion de chantier détaillée), 005 (étude de code et notes générales), 010 et 011 (zones de travaux), 504 (fenêtre à obturer, escalier no 3), 505 (principe de remplacement des fenêtres en deux étapes).

## 4. Corpus électromécanique (WSP)

### 4.1 Devis mécanique-électricité (D3)

- En-tête de page : « Santé Québec Gaspésie – Hôpital de Chandler (Réfection de l'enveloppe) – V/Réf. : R674-24 / 24-108 – N/Réf. : CA0066110.3235 ».
- La TDM (p. 3-4) attribue chaque section à un ou plusieurs entrepreneurs spécialisés qui « doivent remettre leur prix de soumission à l'entrepreneur général » : Pi protection incendie, P plomberie, CR chauffage/refroidissement, CA calorifugeage, GM gaz médicaux, B balancement, V ventilation, R régulation, E électricité.
- Divisions présentes : 20 (prescriptions générales mécanique, 18 p.), 21 protection incendie, 22 plomberie (dont 22 60 00 réseaux de gaz médicaux), 23 CVCA (dont 23 33 16 registres et clapets coupe-feu et de fumée, 23 37 20 persiennes et prises d'air), 25 régulation, 26 électricité (dont 26 05 00 prescriptions générales, 18 p.). Index en annexe D.
- La TDM (p. 5) renvoie pour la liste des plans à « la page titre de ces plans ».
- Annexe 1 (p. 223-231) : fiche d'identification de dessin d'atelier et listes de dessins d'atelier par discipline (formulaires internes WSP).

### 4.2 Plans mécanique-électricité (D4)

- 23 feuilles présentes : G001, G002, G004 ; ME001(D)/ME001, ME002(D)/ME002, ME003(D)/ME003 (élévations démolition/construction) ; ME004(D)/ME004 (toitures et soffites), ME005(D) (paratonnerre – démolition) ; ME006, ME007 (localisation des travaux intérieurs, sous-sol à niveau 400) ; ME008 à ME016 (vues agrandies : quai des ambulances, toiture coin nord-ouest, prise d'air du bloc opératoire et travaux temporaires, issue laboratoire (mécanique et électricité), unité de ventilation hémodialyse/laboratoire, salle mécanique chirurgie d'un jour et prise d'air service alimentaire, divers travaux au rez-de-chaussée).
- **G003 « Tableau de coordination des équipements électromécaniques (à venir) »** : listé au frontispice avec la mention « à venir », absent du jeu (24 pages pour 25 entrées attendues).
- Les cartouches des feuilles portent « Date : avril 2026 » alors que le frontispice porte « 2026/09/04 » : la date de cartouche n'a pas été mise à jour à l'émission pour soumission (lecture du texte extrait ; à confirmer sur la case des révisions).

### 4.3 Tableau des équipements électromécaniques (D5)

- 8 pages, texte natif, daté du 2026-05-11 (nom de fichier et métadonnées), soit la date de l'émission « 60 % » des devis (2026-05-14). Il précède donc de quatre mois l'émission pour soumission et pourrait correspondre au contenu annoncé « à venir » pour la feuille G003 ; le lien n'est écrit nulle part dans les documents — à confirmer auprès de l'ingénieur.

## 5. Corpus structure (WSP)

- 22 feuilles présentes (D6) : S000 frontispice ; S002 notes générales ; S100-S102 détails typiques ; S200 plan clé ; S201-S204 vues en plan (rez-de-chaussée, niveau 100, niveaux 200-300, niveaux 400-500) ; S300-S303 élévations ; S400-S402 coupes de murs ; S410-S411 coupes et détails ; S412 charpente support ; S413-S414 escaliers.
- **S001 « Plan d'implantation »** figure dans la liste des plans de S000 mais n'est ni dans les 5 parties ni dans le porte-documents (23 entrées attendues, 22 présentes).
- Le porte-documents (D7) contient les mêmes 22 feuilles ; le texte de chaque feuille est identique à celui de D6 à un mot « SIGN » près (marqueur de signature). Il s'agit du même jeu, version signée, généré le 2026-09-08.
- Le texte extrait des cartouches des feuilles S002 à S414 comporte la mention « À des fins de construction » alors que S000 porte « Définitifs pour soumission » — incohérence de statut d'émission à confirmer sur l'image des cartouches.
- Aucun devis de structure n'est présent dans le dépôt ; les notes générales S002 sont le seul texte prescriptif de structure.

## 6. Corpus CISSS (donneur d'ouvrage)

### 6.1 Contrat de l'appel d'offres AOC-077221 (D8)

- Page titre : « Appel d'offres – Construction – Contrat – No AOC-077221 – Remplacement du revêtement extérieur – Hôpital de Chandler (Travaux de construction uniquement) – Date d'impression : 26-04-13 ». En-tête courant : « Santé Québec – CISSS de la Gaspésie – Appel d'offres no AOC-077221 ».
- Table des matières (p. 2-4) : Préambule ; 0.00 Interprétation (terminologie 0.01.01 à 0.01.38, primauté 0.02) ; puis articles numérotés jusqu'à 15.00 (durée du contrat, citée par la régie). Repérés dans l'OCR : 10.04 permis, autorisations et traçabilité des sols contaminés ; 10.10 délais et prolongation ; 11.03 ordres de changement ; 11.04 démolition et démantèlement ; clauses d'assurances et de licence (1.02).
- Qualité de l'OCR : bonne sur le corps de texte (2 000 à 2 700 caractères par page), dégradée sur les lignes de pointillés de la table des matières. Les images 300 ppp de chaque page ont servi à vérifier les citations retenues.

### 6.2 Régie de l'appel d'offres (D9)

- Page titre identique au contrat avec le mot « Régie ». Sommaire p. 2 : numéro et titre de l'appel d'offres, date d'émission 12 juin 2026, séance d'information 22 juin 2026, réception des soumissions le 13 juillet 2026 à 10 h, « contrat ferme », sollicitation publique avec soumission électronique, adjudication au prix le plus bas, durée du contrat « voir la section 15.00 du contrat », coordonnées du représentant du dossier (non reproduites).
- Table des matières p. 3-4 : terminologie ; 0.04.01 dates et délais « de rigueur » ; 1.00 objet et régie de l'appel d'offres ; 1.03 séance d'information et visite de chantier.

### 6.3 Procédure PCI (D10)

- 24 pages, texte natif, PDF créé 2026-08-21. Procédure de prévention et contrôle des infections applicable aux travaux de construction dans l'établissement (classification des risques et mesures par classe). Le xlsx y renvoie : « Consulter la procédure PCI des Conditions générales » (note no 2).

### 6.4 Tableau des contraintes opérationnelles de l'établissement, v3 (D11)

- Titre (A1) : « Tableau des contraintes opérationnelles de l'établissement pour les travaux dans le bâtiment existant ». Une seule feuille (« Table 1 »), aucune feuille masquée, aucun commentaire, aucune formule, aucune liste de validation.
- Colonnes (ligne 3) : Phase ; sous-phase ; Niveau ; Description de l'activité ; Zones ; Local ; Secteur ; Fonction / Usage ; Horaire (Chantier ; Hors chantier) ; Exigences PCI – Chantier (Groupe PCI 1 à 4 ; Type A à D ; Classe I à IV) ; Exigences PCI – Hors chantier (Groupe ; Brève description des travaux par entrepreneur ; Type ; Classe) ; Ajout à la classe PCI ; Restriction saisonnière (au tableau des ingénieurs) ; Accès au chantier (voir note no 1) ; Contraintes bruits/vibrations ; Contraintes temps de déménagement ou d'activation (jours ouvrables) ; Autres contraintes opérationnelles.
- Taux de remplissage des 38 lignes de données : Phase et sous-phase 34/38 ; Niveau 37/38 ; Description 38/38 ; Zones 34/38 ; Local 37/38 ; Horaire chantier 18/38 ; Groupe/Type/Classe PCI chantier 18/38 ; Ajout à la classe PCI 7/38 ; Bruits/vibrations 8/38 ; Temps de déménagement 19/38 (toujours « 2 jrs ») ; Autres contraintes 38/38. **Jamais remplies** : Secteur, Fonction / Usage, Horaire hors chantier, les quatre colonnes PCI hors chantier, Restriction saisonnière, Accès au chantier.
- Valeurs de la colonne Horaire chantier : « S », « J » et « J/S », sans légende dans le fichier.
- Notes de bas de tableau : no 1 (L42) « Pour tous les secteurs dans l'existant, l'entrepreneur pourra utiliser l'ascenseur #1 uniquement et l'escalier le plus près du chantier (à confirmer avec le chargé de projet de l'établissement) Prioriser les accès via l'extérieur en tout temps » ; no 2 (L43) « Consulter la procédure PCI des Conditions générales ».

## 7. Lacunes, doublons et incohérences documentaires

| # | Constat | Documents | Incidence pour l'analyse |
|---|---|---|---|
| L1 | Feuille G003 « Tableau de coordination des équipements électromécaniques » annoncée « à venir » et absente | D4 | La coordination des équipements ME n'est pas documentée dans le jeu de plans émis pour soumission ; D5 (2026-05-11) en est peut-être la version préliminaire — non écrit |
| L2 | Feuille S001 « Plan d'implantation » listée et absente | D6, D7 | Pas de plan d'implantation côté structure |
| L3 | Porte-documents ST = doublon signé des 5 parties | D6, D7 | Un seul jeu à analyser ; conserver D7 comme version signée |
| L4 | Référence de dossier client « R674-24 » (WSP) contre « R657-24 » (GLCRM) | D3, D6 vs D1, D2 | Numéro de dossier à uniformiser dans les documents WSP |
| L5 | Désignation du donneur d'ouvrage variable : « CISSS de la Gaspésie », « Santé Québec – CISSS de la Gaspésie », « Santé Québec Gaspésie » | D1, D8-D9, D3-D4-D6 | Terminologie contractuelle (« ORGANISME PUBLIC ») à confirmer |
| L6 | Adresse : « 451 rue Mgr-Ross » (ME) / « 451 rue Ross Est » (ST) | D4, D6 | Sans incidence technique ; à corriger |
| L7 | Contrat et régie imprimés le 2026-04-13 avec un calendrier d'appel d'offres juin-juillet 2026, alors que plans et devis sont émis « pour appel d'offres » le 2026-09-04 | D8, D9 vs D1-D6 | Les documents du CISSS dans le dépôt pourraient être ceux d'un lancement antérieur ou d'un calendrier reporté ; vérifier la version en vigueur (addenda, nouvelles dates) avant de s'appuyer sur leurs délais |
| L8 | Cartouches des feuilles ME datés « avril 2026 » ; cartouches ST « À des fins de construction » contre « Définitifs pour soumission » aux frontispices | D4, D6 | Statut d'émission à confirmer sur les cases de révision |
| L9 | Aucun devis de structure ; notes générales S002 seules | D6 | Les exigences d'exécution de structure ne sont disponibles que sur plan |
| L10 | Tableau xlsx v3 : colonnes Secteur, Fonction/Usage, horaires hors chantier, PCI hors chantier, restriction saisonnière et accès jamais remplies ; codes d'horaire « J » / « S » sans légende | D11 | Une partie des contraintes attendues du donneur d'ouvrage n'est pas renseignée (voir zones d'ombre dans `02-contraintes.md`) |
| L11 | Libellés de section divergents entre TDM et en-têtes (00 08 00 ; 01 35 00 « BPF / BIOSL ») ; coquille « DIVITION 12 » | D1 | Intitulé de 01 35 00 à clarifier (voir constats de lecture) |
| L12 | Renseignements personnels dans D9 (p. 2), D3 (annexe 1), D4 et D6 (cartouches), D11 (propriétés) | — | Non reproduits dans les livrables |

## 8. Constats de lecture par corpus

Compléments issus de l'analyse de contenu (agents de lecture par corpus). Voir `02-contraintes.md` pour les contraintes elles-mêmes.

<!-- CONSTATS -->

## Annexe A — Plans d'architecture : correspondance fichier / page PDF / feuille

| Fichier | Page | Feuille | Titre (liste des plans, feuille frontispice) |
|---|---|---|---|
| …_Partie1.pdf | 1 | — | Frontispice : liste des plans, « Définitifs pour soumission », 4 septembre 2026 |
| …_Partie1.pdf | 2 | 001 | Plan d'implantation |
| …_Partie1.pdf | 3 | 002 | Gestion de chantier détaillée |
| …_Partie1.pdf | 4 | 005 | Étude de code et notes générales |
| …_Partie1.pdf | 5 | 010 | Plans des niveaux – identification des zones de travaux |
| …_Partie2.pdf | 1 | 011 | Élévations – identification des zones de travaux |
| …_Partie2.pdf | 2 | 050 | Plan du sous-sol – démolition |
| …_Partie2.pdf | 3 | 051 | Plan du rez-de-chaussée – démolition |
| …_Partie2.pdf | 4 | 052 | Plan du niveau 100 – démolition |
| …_Partie2.pdf | 5 | 053 | Plan du niveau 200 – démolition |
| …_Partie3.pdf | 1 | 054 | Plans des niveaux 300 et 400 – démolition |
| …_Partie3.pdf | 2 | 100 | Plan du sous-sol – construction |
| …_Partie3.pdf | 3 | 101 | Plan du rez-de-chaussée – construction |
| …_Partie3.pdf | 4 | 102 | Plan du niveau 100 – construction |
| …_Partie3.pdf | 5 | 103 | Plan du niveau 200 – construction |
| …_Partie4.pdf | 1 | 104 | Plans des niveaux 300 et 400 – construction |
| …_Partie4.pdf | 2 | 201 | Élévations – démolition |
| …_Partie4.pdf | 3 | 201-A | Élévations – démolition |
| …_Partie4.pdf | 4 | 202 | Élévations – démolition |
| …_Partie4.pdf | 5 | 203 | Élévations – construction |
| …_Partie5.pdf | 1 | 204 | Élévations – construction |
| …_Partie5.pdf | 2 | 205 | Détails types moulures, parements types |
| …_Partie5.pdf | 3 | 301 | Plan des toitures – démolition |
| …_Partie5.pdf | 4 | 302 | Plan des toitures – construction |
| …_Partie5.pdf | 5 | 303 | Plan des soffites – démolition |
| …_Partie6.pdf | 1 | 304 | Plan des soffites – construction |
| …_Partie6.pdf | 2 | 305 | Détails toitures – démolition et construction |
| …_Partie6.pdf | 3 | 306 | Détails toitures – démolition et construction |
| …_Partie6.pdf | 4 | 400 | Compositions types |
| …_Partie6.pdf | 5 | 401 | Coupe de mur type |
| …_Partie7.pdf | 1 | 402 | Coupe de mur type |
| …_Partie7.pdf | 2 | 403 | Coupe de mur type |
| …_Partie7.pdf | 3 | 404 | Coupe de mur type |
| …_Partie7.pdf | 4 | 405 | Coupe de mur type |
| …_Partie7.pdf | 5 | 406 | Coupe de mur type |
| …_Partie8.pdf | 1 | 407 | Coupe de mur type |
| …_Partie8.pdf | 2 | 410 | Coupe de mur type agrandi – démolition et construction |
| …_Partie8.pdf | 3 | 411 | Coupe de mur type agrandi – démolition et construction |
| …_Partie8.pdf | 4 | 412 | Coupe de mur type agrandi – démolition et construction |
| …_Partie8.pdf | 5 | 413 | Coupe de mur type agrandi – démolition et construction |
| …_Partie9.pdf | 1 | 414 | Coupe de mur type agrandi – démolition et construction |
| …_Partie9.pdf | 2 | 415 | Coupe de mur type agrandi – démolition et construction |
| …_Partie9.pdf | 3 | 416 | Coupe de mur type agrandi – démolition et construction |
| …_Partie9.pdf | 4 | 417 | Coupe de mur type agrandi – démolition et construction |
| …_Partie9.pdf | 5 | 418 | Coupe de mur type agrandi – démolition et construction |
| …_Partie10.pdf | 1 | 419 | Coupe de mur type agrandi – démolition et construction |
| …_Partie10.pdf | 2 | 420 | Coupe et détail type agrandi – démolition et construction |
| …_Partie10.pdf | 3 | 421 | Détail type agrandi – démolition et construction |
| …_Partie10.pdf | 4 | 422 | Coupe – persienne – démolition et construction |
| …_Partie10.pdf | 5 | 451 | Détails en plan – démolition et construction |
| …_Partie11.pdf | 1 | 452 | Détails en plan – démolition et construction |
| …_Partie11.pdf | 2 | 453 | Détails en plan – démolition et construction |
| …_Partie11.pdf | 3 | 454 | Détails en plan – démolition et construction |
| …_Partie11.pdf | 4 | 455 | Détails en plan – démolition et construction |
| …_Partie11.pdf | 5 | 501 | Élévations types des fenêtres et murs-rideaux |
| …_Partie12.pdf | 1 | 502 | Élévations – identification des détails des fenêtres – démolition |
| …_Partie12.pdf | 2 | 503 | Élévations – identification des détails des fenêtres – construction |
| …_Partie12.pdf | 3 | 504 | Détail fenêtre à obturer escalier #3 |
| …_Partie12.pdf | 4 | 505 | Détail type du principe de remplacement des fenêtres – démolition et construction en 2 étapes |
| …_Partie12.pdf | 5 | 506 | Détail type de fenêtre (tour) – démolition et construction |
| …_Partie13.pdf | 1 | 507 | Détail type de fenêtre (tour) – démolition et construction |
| …_Partie13.pdf | 2 | 508 | Détail de fenêtre (basilaire) – démolition et construction |
| …_Partie13.pdf | 3 | 509 | Détail de fenêtre (basilaire) – démolition et construction |
| …_Partie13.pdf | 4 | 510 | Détail de fenêtre (basilaire) – démolition et construction |
| …_Partie13.pdf | 5 | 511 | Détail de fenêtre (basilaire) – démolition et construction |
| …_Partie14.pdf | 1 | 512 | Détail de fenêtre (basilaire) – démolition et construction |
| …_Partie14.pdf | 2 | 513 | Détail de fenêtre (basilaire) – démolition et construction |
| …_Partie14.pdf | 3 | 601 | Détails de porte – démolition et construction |
| …_Partie14.pdf | 4 | 602 | Détails de porte – démolition et construction |
| …_Partie14.pdf | 5 | 603 | Détails de porte – démolition et construction |
| …_Partie15.pdf | 1 | 604 | Détails de porte – démolition et construction |
| …_Partie15.pdf | 2 | 605 | Détails de porte – démolition et construction |
| …_Partie15.pdf | 3 | 606 | Détails de porte – démolition et construction |
| …_Partie15.pdf | 4 | 607 | Détails de porte – démolition et construction |
| …_Partie15.pdf | 5 | 701 | Métaux ouvrés |
| …_Partie16.pdf | 1 | 702 | Métaux ouvrés |
| …_Partie16.pdf | 2 | 703 | Métaux ouvrés |
| …_Partie16.pdf | 3 | 704 | Métaux ouvrés |
| …_Partie16.pdf | 4 | 705 | Métaux ouvrés |

## Annexe B — Plans mécanique-électricité : correspondance page PDF / feuille

| Page | Feuille | Titre (liste des plans, frontispice) |
|---|---|---|
| 1 | — | Frontispice : liste des plans, « Définitifs pour soumission », 2026/09/04 |
| 2 | G001 | Notes générales et légende mécanique |
| 3 | G002 | Notes générales et légende électrique |
| 4 | G004 | Détails |
| 5 | ME001(D) | Élévations nord / ouest – démolition |
| 6 | ME001 | Élévations nord / ouest – construction |
| 7 | ME002(D) | Élévations sud / est – démolition |
| 8 | ME002 | Élévations sud / est – construction |
| 9 | ME003(D) | Élévations partielles – démolition |
| 10 | ME003 | Élévations partielles – construction |
| 11 | ME004(D) | Toitures et soffites – démolition |
| 12 | ME004 | Toitures et soffites – construction |
| 13 | ME005(D) | Toitures – paratonnerre – démolition |
| 14 | ME006 | Sous-sol et rez-de-chaussée – existant – localisation des travaux intérieurs |
| 15 | ME007 | Niveaux 100, 200, 300 et 400 – existant – localisation des travaux intérieurs |
| 16 | ME008 | Vues agrandies et détails – quai des ambulances |
| 17 | ME009 | Vues agrandies et détails – toiture coin nord-ouest |
| 18 | ME010 | Vues agrandies et détails – prise d'air du bloc opératoire |
| 19 | ME011 | Travaux temporaires – prise d'air du bloc opératoire |
| 20 | ME012 | Vues agrandies et détails – mécanique – ajout issue laboratoire |
| 21 | ME013 | Vues agrandies et détails – électricité – ajout issue laboratoire |
| 22 | ME014 | Vues agrandies et détails – unité de ventilation hémodialyse / laboratoire |
| 23 | ME015 | Vues agrandies et détails – salle mécanique chirurgie d'un jour et prise d'air service alimentaire |
| 24 | ME016 | Vues agrandies et détails – divers travaux au rez-de-chaussée |

## Annexe C — Devis d'architecture : index des sections (pages PDF)

| Section | Titre | Pages PDF | Nb pages |
|---|---|---|---|
| 00 01 10 | Table Des Matières | 3–5 | 3 |
| 00 08 00 | Clauses Administratives Particulières | 6–12 | 7 |
| 01 11 00 | Instructions Générales | 13–16 | 4 |
| 01 14 00 | Restriction Visant Les Travaux | 17–19 | 3 |
| 01 32 16.19 | Ordonnancement Des Travaux Diagramme À Barres (Gantt) | 20–27 | 8 |
| 01 33 00 | Documents Et Échantillons À Soumettre | 28–33 | 6 |
| 01 35 00 | Procédures Spéciales (Bpf / Biosl) | 34–37 | 4 |
| 01 35 29 | Santé Sécurité | 38–63 | 26 |
| 01 35 46 | Contrôle De La Qualité De L'Air Intérieur | 64–71 | 8 |
| 01 41 00 | Exigences Réglementaires | 72–74 | 3 |
| 01 45 00 | Contrôle De La Qualité | 75–78 | 4 |
| 01 51 00 | Services D'Utilités Et D'Installations Temporaires | 79–92 | 14 |
| 01 52 00 | Installation De Chantier | 93–99 | 7 |
| 01 56 00 | Ouvrages D'Accès Et De Protection Temporaires | 100–103 | 4 |
| 01 56 50 | Mesures De Prévention Des Infections | 104–115 | 12 |
| 01 61 00 | Exigences Générales Concernant Les Produits | 116–120 | 5 |
| 01 73 00 | Exécution Des Travaux (Découpage Et Ragréage) | 121–123 | 3 |
| 01 74 00 | Nettoyage | 124–125 | 2 |
| 01 74 19 | Gestion Et Élimination Des Déchets De Construction | 126–137 | 12 |
| 01 74 21 | Gestion Et Élimination Des Déchets De Démolition | 138–144 | 7 |
| 01 78 00 | Documents/Élément À Remettre À La Fin Des Travaux | 145–150 | 6 |
| 01 91 13 | Mise En Services Exigences Generales | 151–159 | 9 |
| 02 41 19.13 | Démolition Sélective De Bâtiment | 160–166 | 7 |
| 02 81 00 | Matières Dangereuses | 167–172 | 6 |
| 04 05 00 | Maçonnerie – Exigences Générales | 173–186 | 14 |
| 04 05 13 | Mortiers À Maçonnerie | 187–194 | 8 |
| 04 05 19 | Armatures, Attaches Et Ancrages À Maçonnerie | 195–205 | 11 |
| 04 22 00 | Maçonnerie D'Élément De Béton | 206–216 | 11 |
| 05 41 13 | Ossatures À Poteaux Métalliques Résistant Aux Surcharges | 217–230 | 14 |
| 05 50 00 | Ouvrages Métalliques | 231–244 | 14 |
| 05 51 00 | Escaliers Métalliques | 245–253 | 9 |
| 06 10 00 | Petits Ouvrages De Charpenterie | 254–269 | 16 |
| 06 40 00 | Ébénisterie | 270–285 | 16 |
| 07 21 13 | Isolant En Panneaux | 286–296 | 11 |
| 07 21 16 | Isolant En Matelas | 297–304 | 8 |
| 07 27 10 | Membrane Pare Air/Vapeur Membrane Pare-Air/Écran Pluie | 305–318 | 14 |
| 07 46 16 | Revêtement Muraux Extérieurs En Aluminium Et Métal | 319–331 | 13 |
| 07 52 00 | Couverture À Membrane De Bitume Modifié | 332–358 | 27 |
| 07 62 00 | Solins Et Accessoires En Tôle | 359–368 | 10 |
| 07 84 00 | Protection Coupe-Feu | 369–383 | 15 |
| 07 92 00 | Étanchéité Des Joints | 384–397 | 14 |
| 08 11 13 | Portes Et Bâtis Métalliques Et Quincailleries | 398–412 | 15 |
| 08 33 23 | Volet Coupe-Feu | 413–421 | 9 |
| 08 44 13 | Murs Rideaux Vitrés À Ossature D'Aluminium | 422–454 | 33 |
| 08 52 00 | Fenêtres En Aluminium | 455–476 | 22 |
| 08 80 00 | Vitrages | 477–496 | 20 |
| 09 21 16 | Revêtements En Plaques De Plâtre | 497–519 | 23 |
| 09 22 16 | Ossatures Métalliques Non-Porteuses | 520–535 | 16 |
| 09 51 23 | Plafond De Carreaux Acoustiques | 536–541 | 6 |
| 09 53 23 | Assemblage De Suspension De Plafonds Acoustiques | 542–550 | 9 |
| 09 91 00 | Peinturage | 551–570 | 20 |
| 12 24 00 | Toiles Solaires À Rouleau | 571–578 | 8 |
| 32 31 13 | Clôture Grillagées | 579–585 | 7 |

## Annexe D — Devis mécanique-électricité : index des sections (pages PDF)

| Section | Titre | Pages PDF | Nb pages |
|---|---|---|---|
| 00 01 10 | Table des matières | 3–5 | 3 |
| 20 00 01 | Mécanique – Prescriptions générales (Toutes) | 6–23 | 18 |
| 21 00 01 | Protection incendie – Exigences générales (Pi) | 24–27 | 4 |
| 21 05 29 | Supports et suspensions – protection incendie (Pi) | 28–31 | 4 |
| 21 05 48 | Dispositifs antivibratoires et parasismiques – protection incendie (Pi) | 32–33 | 2 |
| 21 05 53 | Identification des réseaux – protection incendie (Pi) | 34–38 | 5 |
| 21 13 13 | Systèmes d'extincteurs automatiques sous eau (Pi) | 39–42 | 4 |
| 21 40 13 | Tuyauteries et raccords connexes (Pi) | 43–46 | 4 |
| 21 40 14 | Accessoires pour systèmes (Pi) | 47–47 | 1 |
| 22 00 01 | Plomberie – Exigences générales (P) | 48–48 | 1 |
| 22 05 29 | Supports et suspensions – plomberie (P) | 49–54 | 6 |
| 22 05 48 | Dispositifs antivibratoires et parasismiques – plomberie (P) | 55–56 | 2 |
| 22 05 53 | Identification des réseaux – plomberie (P) | 57–62 | 6 |
| 22 07 13 | Calorifuge de la tuyauterie et des équipements de plomberie (CA) | 63–69 | 7 |
| 22 13 17 | Tuyauteries d'évacuation et de ventilation – fonte et cuivre (P) | 70–74 | 5 |
| 22 60 00 | Réseaux de gaz médicaux (GM) | 75–79 | 5 |
| 23 00 01 | Chauffage / refroidissement – Exigences générales (CR) | 80–80 | 1 |
| 23 00 02 | Ventilation – Exigences générales (V) | 81–82 | 2 |
| 23 05 17 | Soudage de la tuyauterie (CR) | 83–86 | 4 |
| 23 05 23 | Robinetterie – bronze (23 05 23 01) et fonte (23 05 23 02) (CR) | 87–91 | 3 |
| 23 05 29 | Supports et suspensions – CVCA (CR-V) | 92–97 | 6 |
| 23 05 48 | Dispositifs antivibratoires et parasismiques – CVCA (CR-V) | 98–99 | 2 |
| 23 05 53 | Identification des réseaux et appareils mécaniques (CR-V) | 100–107 | 8 |
| 23 05 93 | Essai, réglage et équilibrage des systèmes hydroniques (B) | 108–111 | 4 |
| 23 05 94 | Essai, réglage et équilibrage des systèmes aérauliques (B) | 112–115 | 4 |
| 23 07 13 | Calorifuges – tuyauterie et équipements (01) ; conduits d'air et réfrigération (02) (CA) | 116–131 | 7 |
| 23 21 13 | Réseaux hydroniques – tuyauterie en acier (23 21 13 02) (CR) | 132–135 | 4 |
| 23 21 14 | Accessoires pour réseaux hydroniques (CR) | 136–138 | 3 |
| 23 22 13 | Réseaux de vapeur / condensats jusqu'à 860 kPa (CR) | 139–139 | 1 |
| 23 23 00 | Réseaux frigorifiques – tubes en cuivre (V) | 140–145 | 6 |
| 23 25 01 | Glycol – installations de CVCA (CR) | 146–147 | 2 |
| 23 31 13 | Conduits d'air métalliques – basse pression (23 31 13 01) (V) | 148–156 | 9 |
| 23 33 00 | Accessoires pour conduits d'air (V) | 157–160 | 4 |
| 23 33 14 | Registres d'équilibrage (V) | 161–162 | 2 |
| 23 33 15 | Registres de réglage motorisés et antirefoulement (V) | 163–164 | 2 |
| 23 33 16 | Registres et clapets coupe-feu et de fumée (V) | 165–167 | 3 |
| 23 37 20 | Persiennes, prises d'air et autres évents (V) | 168–169 | 2 |
| 25 00 01 | Régulation – Exigences générales (R) | 170–176 | 7 |
| 26 05 00 | Électricité – Prescriptions générales (E) | 177–194 | 18 |
| 26 05 19 | Fils et câbles 0-1000 V (E) | 195–199 | 5 |
| 26 05 26 | Mise à la terre et continuité des masses (E) | 200–201 | 2 |
| 26 05 29 | Attaches et supports (E) | 202–203 | 2 |
| 26 05 33.13 | Conduits, attaches et raccords (E) | 204–207 | 4 |
| 26 05 33.16 | Boîtes de jonction, de tirage et de répartition (E) | 208–209 | 2 |
| 26 05 33.19 | Boîtes de sortie, de dérivation et accessoires (E) | 210–211 | 2 |
| 26 05 48 | Dispositifs antivibratoires et parasismiques – électricité (E) | 212–213 | 2 |
| 26 05 83 | Connecteurs pour câbles et boîtes (E) | 214–215 | 2 |
| 26 27 26 | Dispositifs de câblage (E) | 216–219 | 4 |
| 26 28 16 | Disjoncteurs sous boîtier moulé (E) | 220–220 | 1 |
| 26 50 00 | Éclairage (E) | 221–222 | 2 |
| Annexe 1 | Fiche d'identification et listes des dessins d'atelier (Toutes) | 223–231 | 9 |

## Annexe E — Plans de structure : correspondance fichier / page PDF / feuille

| Fichier | Page | Feuille | Titre (liste des plans, S000) |
|---|---|---|---|
| …_Partie1.pdf | 1 | S000 | Page frontispice (liste des plans) |
| …_Partie1.pdf | 2 | S002 | Notes générales |
| …_Partie1.pdf | 3 | S100 | Détails typiques |
| …_Partie1.pdf | 4 | S101 | Détails typique |
| …_Partie1.pdf | 5 | S102 | Détails typiques |
| …_Partie2.pdf | 1 | S200 | Plan clé |
| …_Partie2.pdf | 2 | S201 | Vue en plan du rez-de-chaussée – construction |
| …_Partie2.pdf | 3 | S202 | Vue en plan niveau 100 – construction |
| …_Partie2.pdf | 4 | S203 | Vue en plan niveaux 200 et 300 – construction |
| …_Partie2.pdf | 5 | S204 | Vue en plan niveaux 400 et 500 – construction |
| …_Partie3.pdf | 1 | S300 | Élévations – construction |
| …_Partie3.pdf | 2 | S301 | Élévations – construction |
| …_Partie3.pdf | 3 | S302 | Élévations – construction |
| …_Partie3.pdf | 4 | S303 | Élévations – construction |
| …_Partie3.pdf | 5 | S400 | Coupes de murs |
| …_Partie4.pdf | 1 | S401 | Coupes de murs |
| …_Partie4.pdf | 2 | S402 | Coupes de murs |
| …_Partie4.pdf | 3 | S410 | Coupes et détails |
| …_Partie4.pdf | 4 | S411 | Coupes et détails |
| …_Partie4.pdf | 5 | S412 | Élévations, coupes et détails charpente support |
| …_Partie5.pdf | 1 | S413 | Élévations, coupes et détails escaliers |
| …_Partie5.pdf | 2 | S414 | Élévations, coupes et détails escaliers |

## Annexe F — Contrat AOC-077221 : correspondance partie / pages

Partie N (N = 1 à 21) = pages 5(N − 1) + 1 à 5N du document de 104 pages (Partie21 : pages 101 à 104). Le pied de page OCR « Page x de 104 » permet la vérification directe.
