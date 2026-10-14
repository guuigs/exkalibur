# R1110_LID — Réseau de chemins LiDAR, jonctions fusionnées, shortlist classée et hasard (11/10/2026)

**Verdict : RIEN de fiable. Le score de la vraie tour est au niveau du hasard (rang 1 : p = 0,42 ; rang 2 : 0,15 ; rangs 3-10 : 0,45-0,85, rangs calculés après suppression des voisins < 100 m, `null_nms.json`).** La shortlist ci-dessous est un classement, pas une identification. Le réseau LiDAR est trop bruité et les critères C2/C3 trop larges pour discriminer ; sinon aucune piste n'atteint le seuil de 2 % de la règle de fiabilité.

Scripts : `outils_scratch/r1110_lid_01…09_*.py` ; données `donnees_travail/r1110_LID/` (Pmap, net_lidar, net_fused, junctions.npz, static.npz, null.json, shortlist.json, validation.json, sensibilite_connu.json) ; ortho `images_travail/r1110_LID/` (top01…top10 + `planche_top10.jpg`).

## 1. Extraction des chemins forestiers (étape 1)
- Variables : MNT/MNH 1 m uniquement (détecteur orienté 16 directions : replat linéaire/déblai sur lignes de 15 et 31 m, trouée linéaire MNH<3 m, pente, LRM 2/6 m, laplacien, rugosité MNH…) → HistGradientBoosting.
- Vérité terrain : sentiers/chemins BD TOPO (Sentier, Chemin) + OSM path/footway/track, **en forêt** (fraction MNH>6 m ≥ 0,6 sur 31 m) : 64 831 points (pas 2 m). Entraînement sur les blocs 1 km « pairs » d'un damier, **validation sur les blocs « impairs »** (AUC = 0,836).
- Résultats (réseau = hystérésis, squelette ; contrôle « hasard » = vérité décalée de 60 m) :

| seuil | rappel 5 m (réglage / validation) | rappel 8 m (rég. / valid.) | hasard 5 m | couverture forêt à 5 m | longueur |
|---|---|---|---|---|---|
| 0,5 (règle initiale : 1er seuil à rappel 5 m ≥ 80 % en réglage) | 0,808 / 0,773 | 0,919 / 0,897 | 0,45 | 44 % | 1 592 km |
| **0,7 (retenu, après coup, pour réduire le bruit)** | 0,783 / **0,765** | 0,880 / **0,868** | 0,35 | 32 % | 1 247 km |

- **Critère « ≥ 80 % des sentiers BD TOPO »** : atteint **à tolérance 8 m** (87-90 % en validation) ; **non atteint à 5 m** (76-77 %). Tolérance 8 m justifiée par le décalage BD TOPO sous couvert (~5-12 m, cf. r1110_A), mais c'est un choix de ma part.
- **Faiblesse majeure** : spécificité médiocre. La couverture de la forêt est 32-44 % ; le rappel d'un contrôle décalé est 35-45 %. Sur 1 247 km détectés, ~780 km sont « nouveaux » (> 8 m de tout chemin connu) : mélange inconnu de vrais chemins forestiers, de ravines et de bruit. **Aucune vérité terrain pour estimer la précision sur les chemins non cartographiés.** Le détecteur ne voit ni sol nu sous canopée (pas de nuage de points, seulement MNT/MNH) ni souche.
- Talwegs LiDAR (aire drainée ≥ 1 ha, D8) : 252 km sur 36 km² (7 km/km²), seuil fixé a priori ; très permissif (C2 vrai pour 52 % des jonctions).

## 2. Jonctions du réseau fusionné (étape 2)
Fusion = BD TOPO + OSM (doublons fusionnés par dilatation 4 px) + segments LiDAR > 8 m des lignes connues (≥ 40 px, raccordés à ≤ 25 m), squelette, élagage des éperons < 20 m. Jonction = amas de degré ≥ 3 avec ≥ 3 branches (anneau 12-15 m).
- 15 106 jonctions dans la mosaïque (les 1 404 jonctions BD TOPO/OSM de `jonctions.json` sont retrouvées à ≤ 15 m à 84 %, à ≤ 30 m à 96 %) ; 9 346 dans 2,5 km de la tour, dont 8 658 avec ≥ 1 branche LiDAR nouvelle ; **2 860 après filtre bâti ≥ 80 m** (polygones BD TOPO, toutes communes ; Pontcharra non exclue).
- Le nombre de jonctions est dominé par le bruit du réseau LiDAR : le jeu « connu seul » (sans branche nouvelle) en compte 166.

## 3. Score (fixé avant d'examiner, 1 point par critère, max 6) — voir en-tête de `r1110_lid_07_score.py`
C1 clairière (ouvert MNH<2 m ≥ 50 % sur 20 m ET forêt MNH>6 m ≥ 35 % sur 30-120 m) · C2 ruisseau cartographié ou talweg ≤ 30 m · C3 bloc (MNT−gauss6 ≥ 2 m, 20-1 500 m², allongement ≤ 3,5, toute canopée) à ≤ 15 m d'un cours d'eau de la même composante, ≤ 400 m de la jonction · C4 ligne de vue sol nu depuis sommet de tour +33 m · C5 azimut 45-95° · C6 fin de chaîne (bloc +10 pas N +10 pas E +8 pas au cap 63,7°, pas 1,48 m) en pente ≤ 15° et ≥ 50 m du bâti (≥ 1 bloc lié).
Ajouts de ma part non dans la consigne (fixés avant calcul) : aire ≤ 1 500 m² et allongement ≤ 3,5 pour les blocs ; bloc ≥ 15 m du bâti et ≥ 8 m d'une route revêtue ; « même ruisseau » = même composante du masque eau dilaté à 15 m (peu sélectif : réseau hydro connecté) ; azimut en grille L93 (écart ~2° avec le nord vrai).
Répartition des scores réels (0…6) : 498 / 892 / 786 / 437 / 203 / 40 / 4. Départage de la shortlist (fixé avant) : score, aire du plus grand bloc lié, nombre de branches ; suppression des voisins à < 100 m.

## 4. Shortlist top 10 (réseau fusionné) et p de hasard par rang
p = probabilité que le k-ième meilleur candidat (après suppression des voisins < 100 m, `r1110_lid_08b_null_nms.py`) d'une tour fictive ait un score ≥ s_k (1 000 tours, altitude ±50 m de celle de la tour, ≥ 1,2 km de la vraie, disque de 2,5 km ≥ 70 % dans la mosaïque, même score ; ligne de vue et azimut recalculés).

| # | lat, lon | score | C1 C2 C3 C4 C5 C6 | d tour / az | branches (nouv.) | bâti | commune | bloc lié (lat, lon, aire, dist.) | p rang* |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 45.434904, 6.048628 | 6 | ✓✓✓✓✓✓ | 1 552 m / 62° | 4 (4) | 82 m | 38426 | 45.436794, 6.046403, 208 m², 273 m | 0,42 |
| 2 | 45.433889, 6.045207 | 6 | ✓✓✓✓✓✓ | 1 262 m / 61° | 3 (2) | 121 m | 38426 | idem, 336 m | 0,15 |
| 3 | 45.438308, 6.050031 | 5 | ✓✓✓✗✓✓ | 1 839 m / 53° | 4 (2) | 209 m | 73141 | 45.438323, 6.053808, 232 m², 295 m | 0,85 |
| 4 | 45.435066, 6.045988 | 5 | ✓✓✓✗✓✓ | 1 378 m / 58° | 4 (4) | 157 m | 38426 | 45.436794, 6.046403, 208 m², 195 m | 0,82 |
| 5 | 45.442193, 6.056287 | 5 | ✓✓✓✓✓✗ | 2 488 m / 51° | 3 (2) | 294 m | 73075 | 45.4421, 6.058381, 145 m², 164 m | 0,78 |
| 6 | 45.411113, 6.028415 | 5 | ✓✓✓✓✗✓ | 1 973 m / 183° | 7 (6) | 201 m | 38314 | 45.410197, 6.024309, 134 m², 337 m | 0,74 |
| 7 | 45.407402, 6.024336 | 5 | ✓✓✓✓✗✓ | 2 429 m / 190° | 5 (3) | 86 m | 38314 | idem, 310 m | 0,67 |
| 8 | 45.432253, 6.045398 | 5 | ✓✓✓✓✓✗ | 1 206 m / 69° | 5 (5) | 118 m | 38426 | 45.434785, 6.047368, 125 m², 321 m | 0,60 |
| 9 | 45.432699, 6.044233 | 5 | ✓✓✓✓✓✗ | 1 138 m / 65° | 4 (4) | 185 m | 38426 | idem, 337 m | 0,52 |
| 10 | 45.441663, 6.005579 | 5 | ✓✓✓✓✗✓ | 2 434 m / 304° | 7 (7) | 206 m | 38314 | 45.441264, 6.002281, 122 m², 262 m | 0,45 |

\* rang k : P(k-ième meilleur score fictif, NMS 100 m, ≥ s_k). Sans NMS (`null.json`) : 0,42 / 0,37 / 0,15 / 0,11 pour les 4 jonctions à 6 de la vraie tour (dont deux voisines des rangs 1-2), puis 0,78-0,85. Ortho : `images_travail/r1110_LID/topNN_*.jpg` (WMS data.geopf.fr, HR.ORTHOIMAGERY.ORTHOPHOTOS, 500 px / 100 m, croix rouge = jonction) et `planche_top10.jpg`.
Remarques ortho (lecture de la planche) : #1 petit bâti/cabane non cartographié à ~20-30 m, clairière-jardin ; #3 et #5 : jonction au bord d'une route revêtue (jonction route/chemin, pas un chemin forestier) ; #2 pré fauché + lisière ; #4 prairie ouverte en lisière ; #6, #7, #8, #9 pleine forêt/lisière sans clairière visible à l'ortho (clairière MNH sous couvert jeune ?) ; #10 banc de graviers de l'Isère (clairière = lit de rivière, élimine le candidat). Les rangs 1, 2, 4 (et 8, 9) partagent le même bloc ou un voisin : 3 candidats ≈ un seul indice. Pour C6 le bloc de fin de chaîne valide n'est pas le « meilleur bloc » (colonne bloc_chaine_ok = false) : un autre bloc lié (parmi 6-9) passe le test de terrain plat.

## 5. Distribution nulle (1 000 tours fictives)
- Jonctions retenues par tour fictive : moyenne 2 432 (1 904-3 150) contre 2 860 pour la vraie tour (disques fictifs en partie tronqués : léger biais favorable à la vraie tour).
- Meilleur score par tour fictive : 4 → 108 tours ; 5 → 475 ; 6 → 417 ; < 4 → 0. Moyenne des 10 meilleurs scores fictifs : 5,31 / 5,25 / 5,01 / 4,96 / 4,95 / 4,91 / 4,88 / 4,85 / 4,83 / 4,82.
- P(max ≥ 5) = 0,89 ; P(max ≥ 6) = 0,42 ; P(10e ≥ 5) = 0,78 ; P(10e ≥ 6) = 0,04. La vraie tour a **4 jonctions à 6** (dont 2 voisines à < 100 m des rangs 1-2 ; 2 candidats à 6 après NMS) : la moyenne fictive du 2e candidat NMS est 5,01, du 3e 4,94.
- Conclusion : le score sature (C2 vrai pour 52 % des jonctions, réseau dense). Il ne sépare pas la vraie tour des fausses.

## 6. Sensibilité post hoc (réseau « connu seul », 166 jonctions)
Même score, mêmes 1 000 tours : top réel 5, 5, 5, 4, 4, 4, 4, 3, 3, 3 ; p par rang 0,30 / 0,05 / **0,009** / 0,45 / 0,28 / 0,16 / 0,05 / 1,0 / 0,99 / 0,93 ; distribution réelle 0-6 : 48 / 55 / 45 / 11 / 4 / 3 / 0. Seul le rang 3 passe sous 2 %, mais : analyse décidée après avoir vu le résultat nul (comparaisons multiples : 10 rangs × 2 réseaux), rangs corrélés, d'autres rangs n'atteignent pas le seuil. **Non fiable** ; à citer seulement comme indice faible (top 5 dans `sensibilite_connu.json`, dont une jonction à 45.4424, 6.0057 proche de la jonction #10, banc de l'Isère).

## 7. Limites / prochaines étapes
- Étape 1 : tolérance 8 m, rappel 5 m 76,5 %, précision inconnue ; sans nuage de points LiDAR (classe sol, densité de points) pas de « sol nu sous canopée ».
- Pour discriminer, il faudrait durcir C2 (ruisseau cartographié seul ≠ talweg 1 ha), imposer « jonction de chemins forestiers uniquement » et exiger la clairière visible à l'ortho/MNH sur l'année ; chaque durcissement doit être fixé avant et refait avec le même test de hasard.
- Rien n'est fouillable sur cette base. Les 3e/11e restent le verrou.
