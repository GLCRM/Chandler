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
| Émission des plans | « Définitifs pour soumission », 4 septembre 2026 (archi, ME, ST). Cartouche des plans d'architecture : 01 « Préliminaires 30 % » 2026-02-27 ; 02 « Définitifs 60 % » 2026-05-14 ; 03 « Définitifs 80 % » 2026-08-03 ; 04 « Définitifs 100 % » 2026-08-21 ; 05 « Définitifs pour soumission » 2026-09-04 | Frontispices ; cartouches des feuilles archi |
| Documents d'appel d'offres du CISSS | Contrat et régie : « date d'impression 26-04-13 ». La régie annonce : émission de l'appel d'offres 12 juin 2026, séance d'information 22 juin 2026, réception des soumissions 13 juillet 2026 à 10 h, contrat ferme, adjudication au prix le plus bas | Régie p. 2 « Sommaire » (OCR) — **antérieur à l'émission des plans et devis du 2026-09-04** |
| Procédure PCI | « Date prévue d'entrée en vigueur de la procédure : le 9 juin 2017 » ; émetteur « CISSS de Chaudière-Appalaches » ; PDF créé le 2026-08-21 (métadonnées) | PCI_CISSS_CA.pdf p. 1 et 9 |
| Tableau des contraintes opérationnelles | version « v3 » (nom de fichier), dernière modification 2026-09-01 (propriétés) | xlsx |

## 2. Synthèse des documents (11 documents, 50 fichiers)

| # | Document | Fichier(s) | Corpus | Émetteur | Émission / date | Pages | Extraction | Remarques d'inventaire |
|---|---|---|---|---|---|---|---|---|
| D1 | Devis technique – architecture | `R657-24 Devis Appel-d'offres 2026-09-04.pdf` | Architecture | GLCRM \| Proulx Savard | Rév. 03, 2026-09-04 (PDF créé 2026-09-04) | 585 | Texte natif | 53 sections (divisions 00 à 32) + page titre et page des sceaux ; index en annexe C |
| D2 | Plans – architecture | `R657-24 Plans Appel-doffres 2026-09-04_Partie1.pdf` à `_Partie16.pdf` | Architecture | GLCRM \| Proulx Savard | Définitifs pour soumission, 4 septembre 2026 (rév. 05) | 79 (78 feuilles + frontispice) | Texte vectoriel non exploitable (glyphes non mappés) ; lecture sur rendu image | 16 fichiers de 5 pages (Partie16 : 4). Ordre des feuilles = ordre de la liste des plans ; correspondance en annexe A. Phasage du projet uniquement sur le plan clé de la feuille 010 (trois phases par secteur, cadre « Notes » vide) |
| D3 | Devis – mécanique et électricité | `CA0066110.3235_Devis_ME_Définitifs_pour_soumission.pdf` | Électromécanique | WSP | Rév. 1, 2026-09-04 (PDF créé 2026-09-03) | 231 | Texte natif | 50 sections (divisions 00, 20 à 26) + annexe 1 (fiches et listes de dessins d'atelier, p. 223-231) ; index en annexe D |
| D4 | Plans – mécanique et électricité | `20260904_CA0066110.3235_Plans ME_Soumission_PDF fusionné.pdf` | Électromécanique | WSP | 2026/09/04 (cartouches des feuilles : « avril 2026 ») | 24 (23 feuilles + frontispice) | Texte natif, désordonné | Feuille **G003 « Tableau de coordination des équipements électromécaniques (à venir) » listée mais absente** ; correspondance en annexe B |
| D5 | Tableau des équipements électromécaniques | `20260511_CA0066110.3235_Chandler_Tableau des équipements MÉ.pdf` | Électromécanique | WSP | 2026-05-11 (nom de fichier et métadonnées) | 8 | Texte natif | Daté du stade « 60 % » ; rapport avec G003 « à venir » à préciser (voir 4.3) |
| D6 | Plans – structure | `CA0062562.5541_20260904_Plans ST_Définitifs pour soumission_Partie1.pdf` à `_Partie5.pdf` | Structure | WSP | 2026-09-04 | 22 (22 feuilles) | Texte natif, désordonné | **S001 « Plan d'implantation » listé sur S000 mais absent** ; aucun devis de structure dans le dépôt ; correspondance en annexe E |
| D7 | Porte-documents – structure | `CA0062562.5541_20260904_Plans ST_Définitifs pour soumission_Porte-documents.pdf` | Structure | WSP | 2026-09-08 (métadonnées) | 1 page conteneur + 22 PDF joints | Pièces jointes extraites | Portfolio PDF ; les 22 pièces (S000 à S414) ont un contenu identique aux 22 pages de D6, à deux champs de signature électronique **vides** près (étiquette « SIGN », case Sceau). Pièces générées le 2026-09-04, conteneur du 2026-09-08. **Doublon non signé** de D6 |
| D8 | Contrat (conditions générales) de l'appel d'offres | `Construction Contrat-OAC077221_Partie1.pdf` à `_Partie21.pdf` | CISSS | Santé Québec – CISSS de la Gaspésie | Impression 2026-04-13 | 104 (21 × 5, Partie21 : 4) | **Scanné – OCR** | Page PDF globale = (N − 1) × 5 + page de la partie ; pied de page « Page x de 104 ». Table des matières p. 2-4 |
| D9 | Régie de l'appel d'offres | `Construction Régie-AOC-077221.pdf` | CISSS | Santé Québec – CISSS de la Gaspésie | Impression 2026-04-13 (PDF créé 2026-05-26) | 37 | **Scanné – OCR** | Sommaire p. 2 (dates de l'appel d'offres, mode d'adjudication) ; table des matières p. 3-4 |
| D10 | Procédure clinique PCI – mesures de prévention des infections lors des travaux de construction | `PCI_CISSS_CA.pdf` | CISSS | **CISSS de Chaudière-Appalaches** (préambule et art. 4) | Entrée en vigueur 2017-06-09 ; champ « Révisée le » vide ; PDF créé 2026-08-21 | 24 (p. 24 = doublon de la p. 10) | Texte natif | Fondée sur CSA Z317.13-12 ; aucune mention de la Gaspésie, de Chandler ni de l'AOC-077221 ; le xlsx renvoie à « la procédure PCI des Conditions générales » |
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
- Feuilles clés pour le séquencement : 002 (gestion de chantier détaillée : cinq détails, dont ambulances en deux configurations et entrée principale en trois), 005 (sommaire de code et 27 notes générales), 010 et 011 (légende des zones A à L ; plan clé « Phase 1 (±5 mois) / Phase 2 (±8 mois) / Phase 3 (±4 mois) / secteur non touché »), 501 (prototype et essais in situ), 504 (fenêtres à obturer, cage d'escalier no 3), 505 (principes de remplacement des fenêtres en deux ou trois étapes, notes plexiglas / bâti isolé de novembre à avril / thermos le même jour).
- Le texte vectoriel des feuilles d'architecture n'est pas exploitable (glyphes non mappés) : toutes les citations des plans proviennent d'une lecture sur rendu image des 79 pages.

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
- Cartouche des 22 feuilles : une seule ligne de révision « 0 – 2026-09-04 – Définitifs pour soumission » ; mention encadrée « Ce document ne doit pas être utilisé à des fins de construction », renforcée par la note générale S002-8 (« Ne pas construire à partir de ces dessins à moins qu'ils n'indiquent la mention « Émis pour construction » »). Une émission « pour construction » est donc un préalable au chantier. Sceau d'ingénieur apposé (S002 vérifié) ; fichier natif Revit « CA0062562.5541_STR_R26.rvt ».
- La liste des plans de S000 omet **S402 « Coupes de murs »**, feuille pourtant présente et référencée 14 fois depuis S201-S204, S300, S302 et S400 (une feuille annoncée non émise, une feuille émise non annoncée : total 22 dans les deux cas).
- Aucun devis de structure n'est présent dans le dépôt, et S002 n'en tient pas lieu : la feuille renvoie cinq fois à un « devis » distinct (généralités 23 et 24, dessins d'atelier 1 et 3, acier de charpente 4) pour les inspections et essais, les dessins d'atelier à soumettre, la conception des assemblages et les exigences d'érection.
- La rubrique « Inspection des travaux » de S002 est numérotée de 11 à 18 (notes 1 à 10 absentes) ; gabarit vraisemblablement tronqué.
- S002, données de conception 5 : « les valeurs des données climatiques […] ont été obtenues à partir du CNB 2020 pour la localité de Percé » (bâtiment situé à Chandler) ; catégorie de risque « protection civile », bâtiment « de grande hauteur » (notes 6 et 14).
- Le bandeau des collaborateurs du cartouche ST porte « Architecture : GLCRM / GLCRM+Proulx Savard » et « Mécanique : WSP » ; aucune case « Électricité » ni « Structure ».

## 6. Corpus CISSS (donneur d'ouvrage)

### 6.1 Contrat de l'appel d'offres AOC-077221 (D8)

- Page titre : « Appel d'offres – Construction – Contrat – No AOC-077221 – Remplacement du revêtement extérieur – Hôpital de Chandler (Travaux de construction uniquement) – Date d'impression : 26-04-13 ». En-tête courant : « Santé Québec – CISSS de la Gaspésie – Appel d'offres no AOC-077221 ».
- Table des matières (p. 2-4) : Préambule ; 0.00 Interprétation (terminologie 0.01.01 à 0.01.38, primauté 0.02) ; puis articles numérotés jusqu'à 15.00 (durée du contrat, citée par la régie). Repérés dans l'OCR : 10.04 permis, autorisations et traçabilité des sols contaminés ; 10.10 délais et prolongation ; 11.03 ordres de changement ; 11.04 démolition et démantèlement ; clauses d'assurances et de licence (1.02).
- Partie contractante (p. 12) : Santé Québec, « agissant par l'entremise de l'établissement Centre intégré de santé et de services sociaux de la Gaspésie » ; « Projet n° 077221 ». Liste des 21 annexes p. 11. **Annexe 0.01.13 – Échéancier : « Début des Travaux : 31 août 2026 / Fin des Travaux : 31 décembre 2027 »** (p. 77, vérifié sur image). **Annexe 0.01.27 – Plans et devis : « a) à compléter »** (p. 78) — la liste des plans et devis contractuels n'est pas renseignée. Ordre de primauté 0.02.02 : « a) Addenda ; b) Contrat ; c) Devis ; d) Plans et dessins » (p. 18).
- Le contrat ne contient **aucune annexe ni procédure PCI** ; son seul article sur le sujet est 10.21 (« prendre les mesures qui s'imposent en vue de prévenir les infections nosocomiales »). Il ne contient pas non plus de clause sur les heures de travail, le phasage imposé, les préavis d'interruption de services ni de pénalité de retard chiffrée (recherche exhaustive par mots-clés ; voir `02-contraintes.md`).
- Qualité de l'OCR : bonne sur le corps de texte (2 000 à 2 700 caractères par page), dégradée sur les lignes de pointillés de la table des matières. Les images 300 ppp des pages 49, 57, 59 et 77 ont servi à vérifier les citations retenues ; l'OCR s'y est révélé fidèle au mot près.

### 6.2 Régie de l'appel d'offres (D9)

- Page titre identique au contrat avec le mot « Régie ». Sommaire p. 2 : numéro et titre de l'appel d'offres, date d'émission 12 juin 2026, séance d'information 22 juin 2026, réception des soumissions le 13 juillet 2026 à 10 h, « contrat ferme », sollicitation publique avec soumission électronique, adjudication au prix le plus bas, durée du contrat « voir la section 15.00 du contrat », coordonnées du représentant du dossier (non reproduites).
- Nature : règles de l'appel d'offres et instructions aux soumissionnaires (présentation, ouverture, conformité, adjudication, sûretés) — le mot « régie » désigne la régie du processus d'appel d'offres, non une régie de chantier. Table des matières p. 3-4 : terminologie ; 0.04.01 dates et délais « de rigueur » ; 1.00 objet et régie de l'appel d'offres ; 1.03 séance d'information ; 1.04 visite des lieux « non obligatoire » le 22 juin 2026 à 10 h 30 ; 1.05 examen des lieux aux frais du soumissionnaire (« Aucune réclamation n'est recevable pour une cause découlant du lieu des Travaux »).
- Article 11.00 : « L'ORGANISME PUBLIC confirme que l'Appel d'Offres ne requiert aucune disposition particulière » (p. 35). Aucune clause sur le délai de réalisation, les phases, les jalons, la PCI ou l'occupation de l'hôpital. Une seule annexe (10.07, questionnaire de non-participation, p. 37).

### 6.3 Procédure PCI (D10)

- Titre (p. 1) : « Procédure clinique PCI — Mesures de prévention des infections lors des travaux de construction, rénovation, d'excavation, d'entretien des bâtiments, de réparation et d'installation d'équipements ». Préparée par la direction des soins infirmiers et la direction des services techniques, approuvée par le comité directeur de PCI ; « Date prévue d'entrée en vigueur de la procédure : le 9 juin 2017 » ; champ « Révisée le » non rempli ; révision prévue « tous les trois ans » (art. 5, p. 9). Référence normative : CSA Z317.13-12.
- **Émetteur : le CISSS de Chaudière-Appalaches** — préambule (p. 1) : « Le CISSS de Chaudière-Appalaches désire adopter une approche proactive […] sur les terrains ou les installations du CISSS de Chaudière-Appalaches » ; art. 4 (p. 9) : « s'applique aux installations et unités de soins du CISSS de Chaudière Appalaches ». Aucune mention de la Gaspésie, de Chandler, de Santé Québec ni de l'AOC-077221. Son applicabilité contractuelle au projet n'est établie par aucun autre document du dépôt (voir `02-contraintes.md`, contradictions).
- Structure : 1 préambule ; 2 objectifs ; 3 rôles et responsabilités (3.1 responsable du projet, 3.2 service PCI, 3.3 responsable construction, 3.4 hygiène et salubrité, 3.5 personnel d'encadrement, 3.6 équipe pluridisciplinaire) ; 4 cadre d'application ; 5 évaluation et révision ; annexe 1 fiche synthèse de l'analyse du risque (p. 10, répétée p. 24) ; annexe 2 mesures par classe I à IV (p. 11-20) ; annexe 3 inspection quotidienne classes III-IV (p. 21) ; annexe 4 nettoyage final (p. 22) ; annexe 5 nettoyage et désinfection terminale (p. 23). Méthode : groupe de patients à risque (1 à 4) × type de travaux (A à D) → classe de mesures (I à IV) par la matrice du tableau 3 (p. 4).
- Le xlsx y renvoie implicitement : « Consulter la procédure PCI des Conditions générales » (note no 2) et « Procédure PCI Classe I/II/III/IV » (18 lignes) ; la nomenclature (groupe 1-4, type A-D, classe I-IV) est celle de cette procédure — concordance de nomenclature seulement, aucun document ne nomme `PCI_CISSS_CA.pdf`.

### 6.4 Tableau des contraintes opérationnelles de l'établissement, v3 (D11)

- Titre (A1) : « Tableau des contraintes opérationnelles de l'établissement pour les travaux dans le bâtiment existant ». Une seule feuille (« Table 1 »), aucune feuille masquée, aucun commentaire, aucune formule, aucune liste de validation.
- Colonnes (ligne 3) : Phase ; sous-phase ; Niveau ; Description de l'activité ; Zones ; Local ; Secteur ; Fonction / Usage ; Horaire (Chantier ; Hors chantier) ; Exigences PCI – Chantier (Groupe PCI 1 à 4 ; Type A à D ; Classe I à IV) ; Exigences PCI – Hors chantier (Groupe ; Brève description des travaux par entrepreneur ; Type ; Classe) ; Ajout à la classe PCI ; Restriction saisonnière (au tableau des ingénieurs) ; Accès au chantier (voir note no 1) ; Contraintes bruits/vibrations ; Contraintes temps de déménagement ou d'activation (jours ouvrables) ; Autres contraintes opérationnelles.
- Taux de remplissage des 38 lignes de données : Phase et sous-phase 34/38 ; Niveau 37/38 ; Description 38/38 ; Zones 34/38 ; Local 37/38 ; Horaire chantier 18/38 ; Groupe/Type/Classe PCI chantier 18/38 ; Ajout à la classe PCI 7/38 ; Bruits/vibrations 8/38 ; Temps de déménagement 19/38 (toujours « 2 jrs ») ; Autres contraintes 38/38. **Jamais remplies** : Secteur, Fonction / Usage, Horaire hors chantier, les quatre colonnes PCI hors chantier, Restriction saisonnière, Accès au chantier.
- Valeurs de la colonne Horaire chantier : « S » (24 lignes), « J » (6 lignes : L24, L26, L28, L32, L38, L41) et « J/S » (L15), sans légende dans le fichier. Lettres de zones utilisées : A à L (les douze), sans légende. Une colonne X est comprise dans les dimensions et les fusions des notes, sans en-tête ni contenu. Aucun en-tête d'établissement, logo, date ni auteur dans la feuille.
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
| L7 | Contrat et régie imprimés le 2026-04-13 avec un calendrier d'appel d'offres juin-juillet 2026 et un échéancier contractuel « 31 août 2026 – 31 décembre 2027 » (annexe 0.01.13), alors que plans et devis sont émis « pour appel d'offres » le 2026-09-04 | D8, D9 vs D1-D6 | Les documents du CISSS dans le dépôt pourraient être ceux d'un lancement antérieur ou d'un calendrier reporté ; vérifier la version en vigueur (addenda, nouvelles dates) avant de s'appuyer sur leurs délais. Le début contractuel des travaux est antérieur à l'émission des plans pour soumission |
| L8 | Cartouches des feuilles ME datés « avril 2026 » (frontispice 2026/09/04) ; cartouches ST : « Ce document ne doit pas être utilisé à des fins de construction » + note S002-8 exigeant la mention « Émis pour construction » | D4, D6 | Date ME à confirmer sur les cases de révision ; côté ST, une émission « pour construction » est un préalable au démarrage |
| L9 | Aucun devis de structure ; notes générales S002 seules | D6 | Les exigences d'exécution de structure ne sont disponibles que sur plan |
| L10 | Tableau xlsx v3 : colonnes Secteur, Fonction/Usage, horaires hors chantier, PCI hors chantier, restriction saisonnière et accès jamais remplies ; codes d'horaire « J » / « S » sans légende | D11 | Une partie des contraintes attendues du donneur d'ouvrage n'est pas renseignée (voir zones d'ombre dans `02-contraintes.md`) |
| L11 | Libellés de section divergents entre TDM et en-têtes (00 08 00 ; 01 35 00 « BPF / BIOSL ») ; coquille « DIVITION 12 » | D1 | Intitulé de 01 35 00 à clarifier (voir constats de lecture) |
| L12 | Renseignements personnels dans D9 (p. 2, 8 et 37), D8 (p. 12, signataire), D3 (annexe 1), D4 et D6 (cartouches), D11 (propriétés) | — | Non reproduits dans les livrables |
| L13 | **La procédure PCI du dépôt est celle du CISSS de Chaudière-Appalaches (2017)**, non celle du CISSS de la Gaspésie ; le contrat ne contient aucune annexe PCI et le xlsx renvoie à « la procédure PCI des Conditions générales » | D10, D8, D11 | Le régime PCI contractuel applicable à Chandler n'est établi par aucun document ; les mesures par classe citées dans `02-contraintes.md` sont celles de D10 sous réserve de confirmation |
| L14 | Annexe 0.01.27 « Plans et devis » du contrat : « a) à compléter » alors que 0.01.27 définit les plans et devis par renvoi à cette annexe | D8 | Le statut contractuel de D1 à D6, de D10 et de D11 n'est fixé par aucun texte disponible |
| L15 | S402 « Coupes de murs » présente mais absente de la liste des plans de S000 ; S001 listée mais absente | D6 | Liste des plans ST à corriger |
| L16 | S002 renvoie cinq fois à un « devis » de structure absent du dépôt (inspections et essais, dessins d'atelier, assemblages, érection) | D6 | Exigences d'exécution de structure incomplètes sans ce devis |
| L17 | Données climatiques de conception ST « pour la localité de Percé » (S002, données de conception 5) pour un bâtiment situé à Chandler | D6 | À confirmer auprès de l'ingénieur en structure (incidence sur les charges de neige citées à S303) |
| L18 | Renvois internes erronés du contrat : 2.04.03 cite « 10.28.01 » (propreté) pour les matières dangereuses (10.29.01) ; 11.10.01 et 3.06 citent « 10.32 » (refus des travaux) pour les manuels et plans tels que construits (10.33) ; table des matières décalée (10.04.04/10.04.05, 10.08.04 absent) | D8 | À signaler au donneur d'ouvrage ; lecture des clauses par leur contenu, non par leur numéro |
| L19 | Article 3.04.01 du contrat évoque « une clause pénale prévue au Contrat » ; aucune clause pénale ni pénalité de retard n'est stipulée dans les 104 pages ni dans la régie | D8, D9 | Absence de pénalité de retard écrite ; ne pas présumer d'un montant |
| L20 | Article 10.08.04 du contrat (suivi bimensuel de l'échéancier) : phrase incomplète dans le document source (confirmé sur image, pas un défaut d'OCR) | D8 | Portée exacte de l'obligation de suivi ambiguë au document même |
| L21 | S414 (escalier no 7) : charges de pieux et de contreventement non renseignées (« Pf= XXkN, Vf= XXkN », « Tf= XXkN ») sur une émission pour soumission | D6 | Dimensionnement des pieux non fixé |
| L22 | Plans d'architecture : feuilles 010/011 porteuses du phasage avec cadre « Notes » vide ; attribution des zones aux phases seulement graphique ; titres 504/505/506 divergents entre liste et cartouche ; note 15 différente entre 001 et 002 ; texte vectoriel non exploitable | D2 | Le phasage global du projet repose sur une lecture de couleurs à faire confirmer par les architectes |

## 8. Constats de lecture par corpus

Compléments issus de l'analyse de contenu (agents de lecture par corpus). Voir `02-contraintes.md` pour les contraintes elles-mêmes.

### 8.1 Devis d'architecture (D1)

- Le devis ne définit ni les zones, ni les phases, ni les dates : 01 32 16.19 (p. 22) « Les plans et devis contractuels décrivent les contraintes techniques, les cibles de performance et une hypothèse de séquence générale de travaux. Ils ne décrivent pas un phasage et un échéancier détaillés » ; l'ordonnancement doit être « basé sur les informations contenues aux plans des feuille 002 […] feuille 010 […] et la feuille 011 » et « selon les contraintes d'ordonnancement opérationnelles de l'Établissement émis par le CISSSGA ». Des « prises de possession anticipée auront lieu pour certains secteurs » (p. 22). Aucune date, durée ni pénalité ; « un échéancier très court est réservé » (00 08 00, p. 11) ; horaire des travaux renvoyé au contrat (01 11 00, p. 14).
- Sections structurantes pour l'exploitation : 01 14 00 (accès séparés chantier/hôpital, travaux bruyants « en soirée », escorte 1 commissionnaire pour 5 travailleurs, livraisons « entre 9h00 et 15h00 »), 01 32 16.19 (calendriers, jalons, calendrier hebdomadaire « jeudi AM » avec coupures), 01 41 00 (instrumentation sonore et vibratoire 24/7, seuils « établis dès le début avec le CISSSGA »), 01 56 00 (plan de sécurité incendie approuvé avant démarrage ; corridors 1650/2400 mm, 2 issues minimum, séparation coupe-feu 1 h continue jusqu'à la dalle), 01 56 50 (régime PCI complet : pression négative 7,5 Pa / 2,5 Pa, 4 CA/h, HEPA, cloisons CTM/CST/CFT/CET, sas, nettoyage, débris hors « heures de grands achalandages », préséance des documents du CISSSGA), 02 41 19.13 (échéancier « préétabli et approuvé par le CISSSGA », ne pas interrompre les opérations des zones adjacentes).
- Lacunes : sections citées inexistantes (01 35 21 — fiche bloquante pour les dessins d'atelier ; 01 91 33 ; 01 91 02 ; 01 32 16.07 ; 25 71 00 ; 07 81 00 ; 07 81 23) ; documents cités non joints (devis de mise en service et annexes A-D ; annexe J accès aux façades ; annexe DA.7 ; rapports d'expertise en matières dangereuses ; règlement de stationnement de l'hôpital) ; placeholders (liste des espaces clos vide, p. 50 ; article Examen de 12 24 00 vide, p. 577 ; formulaire CNESST vierge, p. 62-63) ; textes hérités d'autres projets (01 35 00 BPF/BIOSL ; « la Société » en 01 32 16.19 ; « maisonnée », « salle de classe », « projet d'agrandissement ») ; tableaux de révisions divergents par section (02 41 19.13 et 02 81 00 : 2026-04-30 ; 32 31 13 : une seule révision). Détail dans `02-contraintes.md`, sections 2 et 3.

### 8.2 Corpus électromécanique (D3, D4, D5)

- Le devis ME renvoie le phasage, les horaires, les percements, les interruptions de services et la PCI aux « documents généraux d'architecture et/ou du propriétaire » (20 00 01, art. 1.4.1.2 et 1.7.1 ; G001/G002) et ne contient aucune prescription PCI propre. Il impose le maintien en tout temps des services de mécanique et d'électricité (20 00 01 art. 1.47.2 ; 26 05 00 art. 3.4.6), un préavis de 48 h et un permis par quart pour les travaux à chaud (20 00 01 art. 1.47.8), un permis du propriétaire par secteur pour rendre les détecteurs inopérants (26 05 00 art. 3.4.12), et les percements « en dehors des heures d'occupation du propriétaire » (26 05 00 art. 3.8.3).
- Les plans ME portent les séquences imposées : prise d'air du bloc opératoire maintenue en fonction par conduits temporaires en plusieurs étapes (ME010, ME011, ME001) ; évents de vapeur des autoclaves à relocaliser « AVANT LE DÉBUT DES TRAVAUX DE LA FAÇADE OUEST » (ME010) ; air médical : prise d'air et boîtier HEPA temporaires « SUR LA FAÇADE OUEST DURANT LES TRAVAUX DE LA FAÇADE NORD » (ME004, ME009) ; hémodialyse/laboratoire : conduits temporaires « AVANT LES TRAVAUX DE DÉMOLITION DE L'ENVELOPPE » et coupures « CONCORDER AVEC L'HORAIRE DU PROPRIÉTAIRE » (ME001(D), ME014) ; gicleurs du quai des ambulances : mise hors service de zone (ME008) ; alarme incendie « DOIT DEMEURER FONCTIONNEL […] INCLUANT LES INTERRUPTIONS DE COURANT » (ME013) ; « LA DURÉE DES TRAVAUX DEVANT LES PORTES DE GARAGE DES AMBULANCES EST LIMITÉE (VOIR DOCUMENTS DE PHASAGE EN ARCHITECTURE) » (ME008).
- Le tableau de coordination (D5) est le seul document qui chiffre durées et fenêtres de coupure (« 2 X 2h », « Nuit ou le matin avant 10hre », « Dimanche seulement, en dehors de la période estivale », « Aucun arrêt », « REMETTRE EN FONCTION TOUS LES SOIRS ») ; il est daté 2026-04-29 / révision 2026-05-11, contient des questions ouvertes (« Usage?? », « À valider ? ») et des commentaires du propriétaire jusqu'au 2026-05-11 ; il n'a pas été mis à jour pour les émissions B et 1 ; sa valeur contractuelle n'est établie nulle part.
- Lacunes : G003 « à venir » ; sections citées inexistantes (21 05 93, 23 82 33, 23 11 13, 28 31 00, 26 05 32, 26 05 34 ; division 28 sans contenu) ; tableau des persiennes introuvable (ME015) ; renvoi ME007 → ME008 au lieu de ME009 ; aucune feuille ME005 de construction ni section de paratonnerre ; champ « # Réf. client » vide au cartouche ; éditions de codes divergentes (chapitre V « édition 2026 » vs « édition 2018 », chacune se déclarant prévalente) ; dates de version des sections de 2023-06-20 à 2026-07-15.

### 8.3 Plans de structure (D6, D7)

- Aucun phasage géographique : la séquence de construction et de démolition est renvoyée à l'entrepreneur sous ingénierie scellée (S002 généralités 17-18, structures existantes 7). Séquences écrites : démolition (architecture) → relevé complet des façades → coordination de l'alignement avec l'architecte → fabrication (S303, note 8) ; renforcement des poteaux HSS en trois étapes (S411) ; réparations de béton (S102) ; traitement du mur de fondation (S300/S302). Point d'arrêt après retrait des revêtements (S002 str. ex. 1) ; préavis d'inspection 24 h (S002 insp. 16).
- Exploitation : « PLANIFIER LE TRAVAIL DE MANIÈRE À RÉDUIRE LES IMPACTS SUR L'EXPLOITATION DU BÂTIMENT EXISTANT […] BÂTIMENT OCCUPÉ AVEC UNE CLIENTÈLE VULNÉRABLE » (S002 str. ex. 6) ; « COUPER TOUS LES SERVICES DANS LES ZONES TOUCHÉES […] RÉACHEMINER LES SERVICES AFIN DE MAINTENIR LE RESTE DU BÂTIMENT OPÉRATIONNEL » (str. ex. 4) ; échafaudages : attestation scellée, interdiction de surcharger les toitures, aucune charge ponctuelle sur les toitures ventilées (S201-S204, S303).
- Le CISSS, Santé Québec et l'AOC-077221 ne sont mentionnés sur aucune feuille ; « issue », « R22 », « entreplafond », « grue » n'apparaissent pas.

### 8.4 Documents du CISSS (D8, D9, D10, D11)

- Contrat : échéancier « 31 août 2026 – 31 décembre 2027 » (annexe 0.01.13) ; échéancier à remettre « au plus tard à la première assemblée de chantier » avec « le phasage, chacune des phases d'acceptation du Projet […] le cheminement critique, les dates jalons » (10.08.01-02) ; « Toutes les échéances […] sont de rigueur » (0.04.01) ; prévention des infections nosocomiales (10.21) et des bruits excessifs (10.22) en clauses générales ; percements « peuvent faire l'objet d'horaires particuliers convenus » (10.26.03) ; suspension possible « pour la protection […] des personnes » (10.31) ; prise de possession anticipée par entente écrite (11.11.01). Aucune heure de travail, aucun préavis d'interruption, aucune pénalité chiffrée, aucune annexe PCI ; annexe « Plans et devis » à compléter ; renvois internes erronés (2.04.03 → 10.28.01 ; 11.10.01 → 10.32).
- Régie : règles de l'appel d'offres (dates de juin-juillet 2026, visite non obligatoire le 22 juin 2026, examen des lieux aux frais du soumissionnaire) ; « aucune disposition particulière » (11.00).
- Procédure PCI : émise par le CISSS de Chaudière-Appalaches (2017) ; classification groupe × type → classe ; mesures par classe (écran dalle à dalle et pression négative 7,5 Pa dès la classe III ; SAS et vêtements de protection en classe IV) ; fiche d'analyse du risque signée par le service PCI pour les classes III-IV ; équipe pluridisciplinaire incluant « le représentant de la conception (architecte, ingénieur) » ; pouvoir d'interruption des travaux par le service PCI ; rinçage des conduites d'eau « dans un délai maximum de 24 heures avant l'arrivée des patients ».
- Tableau des contraintes : 38 lignes transcrites intégralement dans `02-contraintes.md` (CI-TAB-001 à 030) ; six lignes portent une classe PCI inférieure à celle de la matrice de la procédure ; lignes de bruit/vibrations sans classe ni horaire ; « 2 jrs » non qualifié ; accès verticaux limités à l'ascenseur no 1 « à confirmer ».

### 8.5 Plans d'architecture (D2)

- Phasage : la feuille 010 est le seul document du dépôt qui découpe le projet en phases globales — plan clé « PHASE 1 (±5 MOIS) », « PHASE 2 (±8 MOIS) », « PHASE 3 (±4 MOIS) », « SECTEUR NON TOUCHÉ PAR LES TRAVAUX », par secteur (« BASILAIRE EST (2 ÉTAGES) », « TOUR (4 ÉTAGES) », « BASILAIRE NORD », « BASILAIRE OUEST (1 ÉTAGE) », « BASILAIRE SUD (2 ÉTAGES) »). L'attribution des zones A à L aux phases n'est lisible que par les couleurs (lecture : phase 1 ≈ basilaire est, D-E-F ; phase 2 = tour, A ; phase 3 ≈ basilaires nord, ouest et sud, B-G-H-I-J-K ; non touchés : C archives, L oncologie 2023) et doit être validée. Aucun ordre des phases, aucune date. Les durées indiquées sont celles des plans et ne sont pas reprises comme hypothèse dans l'analyse.
- Légende des zones (010/011) : A tour chambres (niveaux 200-400, 1974) ; B laboratoire (niveau 100, 1990) ; C archives (RC, 2001) ; D administration (niveau 100, 2005) et cliniques externes (RC, 1974) ; E oncologie (RC, 1974) ; F IRM (RC, 2007) ; G basilaire sud-est (1974) ; H chirurgie d'un jour (niveau 100, 2005) et urgence (RC) ; I basilaire sud-ouest ; J basilaire nord-ouest ; K basilaire nord-est ; L oncologie (RC, 2023). Terminologie de la feuille 002 : « TOUR (NIVEAUX 200, 300, 400 ET CABANON AU TOIT) », « BASILAIRE (NIVEAUX SOUS-SOL, REZ-DE-CHAUSSÉE ET NIVEAU 100 ». Neuf élévations A à I (011).
- Séquences locales écrites : ambulances en deux configurations (entrée au nord pendant les travaux au sud, puis l'inverse ; panneaux temporaires « un panneau par phase ») ; entrée principale en trois configurations (un côté de la marquise, puis l'autre, puis circulation libre) ; fenêtres : « LES FENÊTRES EXISTANTES DOIVENT DEMEURER EN PLACE JUSQU'À CE QUE LES TRAVAUX PAR L'EXTÉRIEUR SOIENT COMPLÉTÉS », plexiglas « DÈS QUE LA FENÊTRE EXISTANTE EST RETIRÉE », « DE NOVEMBRE À AVRIL, UN BATI ISOLÉ […] EST REQUIS », « LE THERMOS ET LA FINITION INTÉRIEURE DOIVENT ÊTRE INSTALLÉS LA MÊME JOURNÉE QUE LE RETRAIT DU PANNEAU DE PLEXIGLASS » ; tour en deux étapes, basilaire RDC en blocs en trois étapes, basilaire à colombages (IRM, niveau 100) en deux étapes ; prototype en présence de l'architecte (501).
- Exploitation : accès pompier à la borne-fontaine et issues extérieures (passage libre 1650 mm jusqu'à la voie publique) maintenus en tout temps ; plan d'action d'évacuation à coordonner avec l'établissement avant tout travail près d'une issue ; « AUCUN ÉLÉMENT OU ENTREPOSAGE MÉTALLIQUE […] DANS CETTE ZONE LORSQUE L'IRM EST EN SERVICE » ; coordination avec l'établissement pour la marquise, la porte IRM, le débarcadère, les flux, les équipements à retirer ; méthodes « LE MOINS DE BRUIT POSSIBLE » ; remplacement des composantes humides ou moisies avant de poursuivre.
- Compartimentation : aucun degré de résistance au feu chiffré sur les 79 feuilles (005 : « DEGRÉ DE RÉSISTANCE AU FEU — NON TOUCHÉ ») ; compartimentation d'entretoit à compléter (gypse type X 13 mm), volets coupe-feu « voir devis », tôle de compartimentation cal. 24, obturation des fenêtres de la cage d'escalier no 3 en maçonnerie sans degré.
- Lacunes : cadres « Notes » vides sur 010, 011 et 401 ; bloc « Consultants » du frontispice vide ; titres de feuilles divergents entre la liste des plans et les cartouches (504, 505, 506) ; note 15 divergente entre 001 et 002 ; note 20 absente ; note 24 de la 302 « abrogé » ; locaux R22-A à R22-D sans désignation ; aucune implantation de grue ni zone d'échafaudage.


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
