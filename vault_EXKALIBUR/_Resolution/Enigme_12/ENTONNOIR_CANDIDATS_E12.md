# É12 — Recherche systématique « en entonnoir » des lieux compatibles avec la checklist FAQ (05/10)
Scripts : `t93_prep.py`, `t94d_entonnoir.py`, `t96_lib.py`, `t97_final_stats.py`, `t98_paques_annees.py`, `t99_planche.py`. Planche : `images_travail/t99_planche_entonnoir.jpg`.
## Méthode
Tous les croisements (≥ 3 voies, OSM + BD TOPO) de 100 m à 2,5 km de la tour (1 281) sont mesurés sur les mêmes critères, de plus large à plus fin. Corrections par rapport aux cribles précédents : distance aux bâtiments calculée sur **tous les sommets** densifiés (3 m) des 124 784 points de bâtiments (et non le premier sommet) ; cadastre du **Moutaret (38268)** ajouté (le fichier « 38270 » était La Murette) ; public à deux niveaux : **sûr** (parcelle publique, forêt publique, voirie cartographiée) et **probable** (bande non cadastrée à ≤ 25 m d'un chemin) ; visibilité calculée depuis les murailles avec l'œil au sol OU sur le mur ; **roche non exigée au LiDAR** (la FAQ dit qu'elle n'est pas forcément visible : FAQ07-126) : tout point d'eau relié à la jonction (réseau d'eau LiDAR, ≤ 450 m le long de l'eau) compte, avec un indicateur « ressaut » à part.
## Entonnoir (cumulatif)
| Étape | Critère | Survivants |
|---|---|---|
| S0 | croisements ≥ 3 voies, 100 m – 2,5 km | **1 281** |
| S1 | maisons ≥ 100 m du croisement | 173 |
| S2 | eau : BD TOPO ≤ 150 m ou talweg ≥ 1 ha | 133 |
| S3 | clairière vue de la muraille (≥ 50 m² ouverts vus dans 60 m) | **20** |
| S4 | fin de parcours possible : eau reliée, coffre public (probable ou sûr), ≥ 100 m maisons, ≤ 30 m d'un chemin | 17 |
| S5 | distance ≤ 2,0 km | **3** |
| S6 | chemin le long de l'eau (≥ 50 % du parcours) | **2** |
| S7 | coffre en public SÛR | 2 |
## Les finalistes (S6-S7) et les voisins immédiats
| # | Lieu | Dist., cap | Terrain | Logique 3e/11e | Verdict |
|---|---|---|---|---|---|
| 1 | **Le Mouret, jonction 2** (45.423370, 6.041663) | 1 034 m, 126° | forêt à 85 %, maisons 161 m, Rebouchet à 65 m, talweg 0,9 ha, pré vu à ~60 m au NO (55 m² ouverts vus), pente 23 %, 24 points d'eau reliés (15 ressauts, 8 coffres publics sûrs) | **atteignable par la table (θ = 81°) ; Pâques 2025 (20/04, Orient 81,4-82,2°) : place 11 à 26-47 m, corde 3→11 à 1-21 m de la jonction et 7-29 m du ressaut de 4,7 m du Rebouchet** | **meilleur candidat de l'entonnoir** ; ouverture 0 %, pente forte |
| 2 | Le Mouret, jonction 1 (45.422426, 6.040299) | 1 021 m, 135° | passe S1-S3 (pré vu 441 m²) mais **aucun point d'eau relié avec coffre valide** aux critères stricts (la variante « roche à mi-chemin » n'existe que si la bande non cadastrée est publique) | table : θ = 90° = Pâques 2023 / 1524 / 2026 | à garder, dépend du public « probable » |
| 3 | Prairie près de la tour (45.426839, 6.031995) | 240 m, 161° | pâtures ouvertes, pas de forêt ni de ruisseau net (eau BD TOPO à 189 m) ; vue seulement œil sur le mur (4 m² œil au sol) | aucune | faible : « clairière » de prairie, sans eaux enchantées |
| 4 | Plaine NO (45.4476, 6.0266 ; 45.4437, 6.0141 ; 45.4410, 6.0087…) | 2,0-2,3 km, 308-354° | champs, fossés/canaux, public abondant, vu de la muraille | aucune | rejet : > 2 km, pas de forêt, pas de roche, aucune logique |
| 5 | Pontcharra sud « A » (45.419519, 6.020142) | 1 344 m, 219° | pré, eau à 100 m, chemin le long de l'eau 0 % | aucune | rejet |
## Pâques selon l'année (lever visible depuis la muraille) — `t98_paques_annees.py`
| Année | Date | Orient | place 11 → J1 / J2 / source | corde 3→11 : J1 / J2 / pont / ressaut |
|---|---|---|---|---|
| 2023 | 09/04 | 89,9-90,3° | 38-57 / 150-175 / 41-62 m | 6-25 / 104-124 / 7-28 / 124-144 m |
| 2024 | 31/03 | 95,6° | 106-130 / 252-274 / 45-63 m | 55-77 / 177-199 / 11-33 / 191-213 m |
| **2025** | **20/04** | **81,4-82,2°** | 138-165 / **26-47** / 188-221 m | 138-165 / **1-21** / 79-96 / **7-29 m** |
| 2026 | 05/04 | 92,9-93,1° | 63-90 / 204-229 / 3-17 m | 16-38 / 143-164 / 0-15 / 159-181 m |
**Date de lancement de la chasse : 22 mai 2025** (FAQ01-172 « à partir du 22 mai 2025 », FAQ01-001) ; la création a débuté fin 2023 (FAQ01-139) ; un manuscrit « écrit en 2024 » est admis (FAQ02-044). **Pâques 2023 n'est pas la date de lancement.** Le dernier Pâques avant le lancement est le **20 avril 2025**.
## Hasard honnête
Le groupe du Mouret est atteint par 4 dates de Pâques sur 2 jonctions voisines : 1524/2023/2026 → jonction 1 ; 2025 → jonction 2. Avec 4 dates × 2 sens et une seule jonction qualifiée dans le cercle de la table, la probabilité qu'une des dates tombe dans la fenêtre de J2 (θ ≈ 79-84° sur 55-125°) est d'environ **25-30 %** : **la coïncidence « Pâques 2025 → J2 » n'est pas significative par elle-même**. Le candidat est retenu pour son terrain et sa cohérence avec la FAQ (03-082, 03-152), pas pour son hasard.
## Limites
LiDAR : arbres opaques, ±1 m ; « ressaut » = pente du talweg (40-70 %), pas un bloc ; public probable = hypothèse ; la clairière exacte n'est pas vue (J2 : 0 % d'ouverture dans 30 m).

## Étau terrain pur (sans lore) sur le groupe NW — 05/10/2026
Script `t100_etau.py` (133 croisements ayant maisons ≥100 m + eau, ≤2,5 km), 6 critères cumulés : maisons ≥100 m ; eau ; clairière vue depuis la muraille ≥100 m² ; ressaut/roche sur l'eau à 12-300 m avec coffre public (≤40 m, maisons ≥100 m, chemin ≤30 m) ; chemin le long de l'eau ≥50 % ; coffre en public SÛR.
Niveaux : 133 → 125 → 109 → 107 → **3**. Survivants : prairie 45.42684,6.0320 (240 m, 1 seule roche), Mouret J1 (117 combinaisons, 89 sûres, mais 3 % ouvert), **NW 45.44104,6.00872 (2 204 m)**.
Groupe NW (15 croisements à 2,0-2,3 km, vus ≥100 m²) : **14/15 n'ont AUCUN ressaut sur l'eau avec coffre public** (étau E4). Le seul survivant est la digue de la Bréda au stade de Pontcharra (terrain de foot, rivière à graviers, ressaut 2,7 m = seuil/digue) : zone aménagée → écarté (cf. règle Pontcharra urbain/sportif).
Conclusion : le groupe NW n'était qu'un artefact de « terrain riche » ; aucun croisement ne passe les 6 critères en milieu naturel.
Carte : images_travail/t101_carte_NW.jpg
