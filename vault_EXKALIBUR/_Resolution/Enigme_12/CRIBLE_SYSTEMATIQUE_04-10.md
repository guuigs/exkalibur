# É12 — Critères FAQ réévalués et crible systématique (04/10)
Scripts : `t78_vs_sol.py`, `t79_pub_categories.py`, `t80_crible_systematique.py`, `t81_listes.py`, `t82_planche.py`. Planche : `images_travail/t82_planche_pretendants.jpg`.

## 1. Chaque critère, ce qu'il veut dire en mesure
| Critère (FAQ) | Ce que j'en tire | Seuil retenu | Limite honnête |
|---|---|---|---|
| **Proche** : coffre « pas loin » du rempart (06-244), chemins « très proches » (06-025), coffre « tout près » de la jonction (05-051) | un joueur, sans outil, repère l'endroit à l'œil nu depuis le rempart et y va à pied : quelques centaines de mètres à ~1,5 km ; au-delà de 2 km, une clairière devient un point minuscule | **≤ 2 km** (préférence ≤ 1,5 km) ; coffre ≤ 300 m de la jonction | aucune distance chiffrée dans la FAQ |
| **Visible** depuis le chemin de rempart (05-155, 05-165) | ce qu'on voit, c'est la **clairière** (un pré ouvert), pas le point exact du croisement sous les arbres | **≥ 100 m² de sol ouvert** vu dans un rayon de 60 m du croisement, **œil à 1,7 m au-dessus du sol** le long de la muraille (variante prudente) | LiDAR : arbres traités comme opaques, données de ~2021-2023, haies qui changent ; ±1 m de précision ; on ne peut pas garantir l'absence de vue, seulement la présence |
| Point de vue | **la muraille** autour de la tour (publique toute l'année, rappel de Guilhem) ; 17 points sur l'enceinte | — | l'ancien point « pied de la tour » masquait tout l'ouest (corrigé) |
| **Maisons** : coffre « éloigné de tout bâtiment » (05-107) ; règle de Guilhem : pas à moins de 100 m | appliqué au **croisement** (version stricte) **et** au coffre | ≥ 100 m de tout bâtiment BD TOPO | les cabanes et hangars comptent aussi |
| **Domaine public** (01-235, 02-097, 03-098) | sûr : parcelles des communes, du département, de l'État (fichier des personnes morales), forêts publiques, **voirie non cadastrée** (chemins) ; **douteux** : lit non cadastré d'un ruisseau (il appartient souvent aux riverains) | coffre possible = point public **sûr**, ≥ 100 m des bâtiments, ≤ 30 m d'un chemin (accès, fauteuil au sens large), ≤ 300 m de la jonction ; ≥ 200 m² | 8 communes couvertes (Saint-Maximin, Pontcharra, Le Moutaret, Barraux, Laissaud, La Chapelle-Blanche, Allevard, La Buissière) |
| **Eaux** à suivre depuis la jonction (06-195) | un cours d'eau cartographié ou un talweg net | eau BD TOPO ≤ 100 m **ou** talweg LiDAR ≥ 2 ha | intermittence non connue |
| **Jonction** (06-005) ; clairière (03-274) mais 07-240 : « il s'agit d'identifier une jonction de chemin » | vrai croisement (≥ 3 voies) ; un peu de forêt autour | ouvert ≥ 30 % dans 30 m, forêt ≥ 20 % dans 60-200 m | 07-240 rend l'ouverture exacte au point secondaire |

## 2. Résultat du crible (1 494 croisements entre 200 m et 3 km)
Effectifs : proche ≤ 2 km 908 ; clairière vue 701 ; **maisons ≥ 100 m : 282** (le critère le plus sélectif) ; eau 1 000 ; coffre public sûr 997 ; clairière 829.

### Prétendants (tous critères stricts)
| # | Croisement | Commune | Distance, cap | Remarques |
|---|---|---|---|---|
| 1 | **Le Mouret** 45.422426, 6.040299 | Pontcharra / Saint-Maximin (limite) | 1 021 m, 135° | passe tout **sauf** l'ouverture exacte du point (croisement en lisière, sous les arbres) ; le **pré voisin est vu** (441 m²) ; maisons 190 m ; talweg 3,7 ha + sources ; 1 350 m² de coffre public sûr possible ; FAQ07-240 couvre la lisière ; c'est aussi l'hypothèse P (Cène / aube de Pâques) |
| 2 | **A** 45.419519, 6.020142 | Pontcharra (sud, rural) | 1 344 m, 219° | **passe tous les critères** ; mais croisement en plein champ, le pré vu (338 m²) est au sud-est ; eau à 98 m (talweg faible) ; château Bayard (monument historique) à ~450 m |
| 3 | **C** 45.443603, 6.014493 | Pontcharra (nord) | 2 083 m, 322° | tout sauf la distance (2,08 km) ; lisière, maisons 234 m, talweg 7,4 ha, beaucoup de terrain communal ; voisinage industriel et ferroviaire plus au nord |
Écartés à la vue aérienne : D et E (zone industrielle, voie ferrée, gravières), F (échangeur de l'A41), le croisement Sonoco.

### Croisements à 40-100 m des maisons (si la règle des 100 m ne vaut que pour le coffre)
21 cas, dont **Le Crêt** (45.430543, 6.053090 ; 1 736 m, 84° ; maisons 47 m), **le Papet** (45.412208, 6.023298 ; 1 948 m, 198° ; maisons 49 m) et un groupe à l'ouest/nord-ouest (Pontcharra). **Le Couvet** (2 290 m ; maisons 45 m) échoue à la fois à la distance et aux maisons.
