# R0710_C — Chaîne complète (jonction visible du rempart → branche qui suit l'eau → grande roche → pas → coffre public) appliquée à TOUTES les jonctions, avec test du hasard (07/10/2026)

**Verdict : RIEN** (0 point de fouille survivant, et ce **partout** : la vraie tour, les 1 000 tours fictives et les 630 croisements de la mosaïque en donnent tous 0).

⚠️ **Correction de Guilhem appliquée** : le critère « eau à senestre » est **supprimé**. L'eau peut être à **gauche OU à droite** de la branche ; on ne garde que « la branche suit un cours d'eau (≤ 60 m sur 0-400 m) ». Le côté est noté dans les tableaux mais **n'est plus un filtre**. L'entonnoir et le test du hasard sont refaits avec cette règle.

---

## 1. Données et méthode (règle posée AVANT de regarder)

- **Géoréférence** : mosaïque LiDAR HD 1 m `donnees_travail/r0610_R_roches/`, taille lue dans `lidar_meta.json` + forme réelle du tableau (`YMAX = Y0 + nrows·res`), **aucune taille codée en dur** (conforme à l'audit de `R0610_J16_est_v2`). X0 934000, Y0 6483000, 6000 × 6000 m, YMAX 6489000.
- **Tour d'Avalon** 45,4288 / 6,03078 → L93 (936937, 6485589), sol MNT 406,3 m ; **sommet de tour = sol + 33 m = 439,3 m**.
- **Croisements** : BD TOPO `troncon_de_route` + OSM `highway` (géométrie réelle Overpass), autoroutes/bretelles exclues. Nœud = extrémités regroupées à ≤ 4 m + tronçons traversants ; croisement si **≥ 3 directions distinctes** (fusion 25°). 4 398 tronçons → **1 404 croisements** dans la mosaïque, dont **630 hors Pontcharra**.
- **Visibilité** (œil nu) : ligne de vue sur **MNT+MNH (canopée comprise)**, tolérance 0,5 m, depuis {**sommet de tour +33 m**, **esplanade +1,7 m**, **Rue du Rempart +1,7 m**}.
- **Branche** : chaîne de tronçons en s'éloignant du nœud (virage ≤ 100°), jusqu'à 600 m. **Suit l'eau** si l'eau (BD TOPO hydro + surfaces + OSM waterway) est à ≤ 60 m sur la **majorité** des échantillons de 0-400 m ; le côté gauche/droite (produit vectoriel) est noté mais **non filtré**.
- **Grande roche** = signature figée de `R0610_R_nature_roche` §1.3 : `MNT − gauss(6 m) ≥ 1,5 m`, canopée < 3 m, blob ≥ 10 m², **≤ 6 m d'un cours d'eau**, `Δz = z_sommet − z_eau ≥ 1 m`, chemin ≤ 30 m. 51 roches dans toute la mosaïque (`roches_all.json`). Roche « atteinte » si ≤ 20 m de la branche-eau et à ≤ 400 m du croisement.
- **Déroulement** : 10 pas N → 10 pas E → souche → 8 pas aux caps {63,7° ; 68,6° ; 73,9°} et pas {0,75 ; 1,5 m} (Geod WGS84).
- **Filtres du coffre** : domaine **public** (cadastre IGN + DGFiP personnes morales 38 ; « non cadastré » = emprise publique), **bâti ≥ 100 m**, **pente ≤ 12°**, **hors MH** (≥ 100 m de la tour), **hors Pontcharra** (38314, règle de Guilhem).

---

## 2. Entonnoir (sous-ensemble : ≤ 2,5 km de la tour, hors Pontcharra, visibles du rempart)

| Étape | Nb |
|---|---|
| Croisements ≥ 3 branches ≤ 2,5 km, hors Pontcharra | **324** |
| + visibles du chemin de rempart (canopée comprise) | **179** |
| Branches (total, ces 179 croisements) | 832 |
| Branches qui suivent un cours d'eau (≤ 60 m, 0-400 m) | **217** |
| Croisements avec ≥ 1 branche-eau | **91** |
| Croisements avec une **roche-signature sur une branche-eau** | **17** |
| Roches atteintes (paires roche×branche ; roches distinctes) | **28** (12 distinctes) |
| Points de fouille calculés (roche × azimut × pas) | **168** |
| + domaine public | 26 |
| + bâti ≥ 100 m | 68 |
| + pente ≤ 12° | 44 |
| + hors MH (≥ 100 m de la tour) | 168 |
| + hors Pontcharra | 137 |
| **= SURVIVANTS (tous filtres)** | **0** |

**Le côté de l'eau ne départage rien** : sur les 217 branches-eau visibles, **108 à droite, 100 à gauche, 9 des deux** — équilibré (supprimer le « senestre » ne change donc pas le résultat, mais était bien la bonne règle).

**Sensibilité** : pente ≤ 14°, 15°, 18°, 20° → **toujours 0** survivant. Le conflit est structurel : les points **publics** (26) sont dans le lit (non cadastré) donc pentus (25-33°) ou à < 100 m d'une maison ; les points **plats et loin du bâti** (8) sont tous en **parcelle privée**. Les trois ensembles sont **disjoints**.

---

## 3. Croisements avec une grande roche dans/au bord du lit sur une branche-eau (17, tous visibles ≤ 2,5 km)

| # | jct lat, lon | d_tour | cap | roche(s) atteinte(s) — lat, lon (m², d_eau, d_bras) |
|---|---|---|---|---|
| 1 | 45.43149, 6.02697 | 422 | 313° | 45.43252, 6.02551 (16 m², 0,6 m, 17 m) |
| 2 | 45.42583, 6.03476 | 453 | 134° | 45.42567, 6.03446 (12 m², 1,8 m, 9 m) ; 45.42517, 6.03287 (11 m², 3,2 m, 13 m) |
| 3 | 45.42671, 6.03735 | 564 | 112° | 45.42462, 6.04078 (31 m², 0,5 m, 14 m) |
| 4 | 45.42636, 6.03771 | 606 | 114° | 45.42462, 6.04078 (31 m², 0,5 m, 14 m) |
| 5 | 45.42634, 6.03829 | 647 | 113° | 45.42462, 6.04078 (31 m², 0,5 m, 14 m) |
| 6 | 45.42237, 6.04034 | 1 034 | 132° | 45.42364, 6.04371 (21 m², 2,6 m, 1 m) — **bras NE du Mouret** |
| 7 | 45.42337, 6.04166 | 1 043 | 123° | 45.42364, 6.04371 (21 m²) ; 45.42462, 6.04078 (31 m²) |
| 8-10 | 45.42431→45.42385, 6.04349→6.04395 | 1 112-1 168 | 114-116° | 45.42364, 6.04371 (21 m²) |
| 11 | 45.41877, 6.02447 | 1 218 | 202° | 45.41764, 6.02530 (10 m², 2,4 m, 3 m) |
| 12 | 45.43359, 6.04490 | 1 226 | 62° | 45.43597, 6.04677 (24 m²) ; 45.43579, 6.04689 (50 m²) ; 45.43539, 6.04647 (16 m²) |
| 13 | 45.41520, 6.03208 | 1 514 | 174° | 45.41452, 6.03313 (18 m², 0,1 m, 9 m) |
| 14 | 45.43465, 6.04990 | 1 630 | 64° | 45.43579, 6.04689 (50 m²) |
| 15-17 | 45.43555-45.43576, 6.00264-6.00343 | 2 266-2 332 | 287° | 45.43682, 6.00491 (20 m²) ; 45.43738, 6.00502 (16 m²) |

Les 12 roches distinctes atteintes sont **petites à moyennes (10-50 m²)** ; aucune n'est la « grande roche très difficile à manquer » du texte. Les deux plus grosses (149 / 156 m², Perrière) ne sont pas suivies par une branche-eau visible.

---

## 4. Quasi-manques (19 points uniques n'échouant que sur UN filtre) — pistes de suite

- **10 points** n'échouent que sur « bâti ≥ 100 m » (publics, plats 2-12°, maisons à 26 m) : ex. 45.43270, 6.02584 (pente 2,7°, maisons 26 m) ; 45.42585, 6.03478 (pente 3,2°, maisons 25 m, **branche est de J16**).
- **5 points** n'échouent que sur « pente ≤ 12° » (publics, loin du bâti, mais 26-33°) : ex. 45.43556, 6.04680 (maisons 208 m) ; 45.41469, 6.03346 (maisons 100 m).
- **4 points** n'échouent que sur « public » (plats, loin du bâti, mais **parcelle privée**) : 45.43588, 6.04705 (pente 11°, maisons 244 m, parcelle **A0228**) ; 45.42534, 6.03320 (pente 9,8°, maisons 117 m, parcelle **B1331** — le cas « branche est de J16 »).

Aucun ne réunit les trois.

---

## 5. TEST DU HASARD — 1 000 tours fictives tirées au hasard dans le même paysage

Zone : 1 000 points uniformes dans la fenêtre X[936600, 937400] × Y[6485600, 6486400] (zone où le disque de 2,5 km est **entièrement** couvert par les données). Chaque tour fictive reçoit la même hauteur (+33 m) et la même chaîne.

| Compteur | Vraie tour | fictives min/med/max | moy | **P(X ≥ vraie)** | rang |
|---|---|---|---|---|---|
| croisements visibles | **180** | 2 / 81 / 190 | 75,4 | **0,7 %** | 7/1000 |
| dont suivent l'eau | **92** | 2 / 36 / 95 | 37,6 | **1,0 %** | 6/1000 |
| dont avec roche sur branche-eau | **17** | 1 / 6 / 18 | 6,7 | **1,2 %** | 3/1000 |
| **survivants (chaîne complète)** | **0** | 0 / 0 / 0 | 0 | **100 %** | 1/1000 |

**Contrôle d'altitude** (le vrai avantage de la tour est sa hauteur : motte à 406 m, +130 m sur la plaine). Sur les 58 tours fictives dont le sol est ≥ 380 m :

| Compteur | Vraie tour | médiane | **P(X ≥ vraie)** |
|---|---|---|---|
| croisements visibles | 180 | 164 | 5,2 % |
| dont suivent l'eau | 92 | 86 | 17,2 % |
| dont avec roche sur branche-eau | 17 | 14 | 20,7 % |

**Interprétation** : l'« exception » brute de la tour (top 1 %) **s'effondre dès qu'on neutralise la hauteur** (5-21 %) → elle est un **artefact de la position élevée**, pas un signal de l'énigme. Et le compteur de survivants est **0 pour la tour ET pour les 1 000 tours fictives** (comme pour les 630 croisements de la mosaïque) : la dernière étape de la chaîne **n'a aucun pouvoir discriminant** — elle élimine tout le monde.

---

## 6. Verdict, limites, suite

**RIEN.** La chaîne complète appliquée à toutes les jonctions du paysage ne désigne **aucun** point de fouille, et le test du hasard ne sauve pas la tour d'Avalon (signal nul dès qu'on contrôle la hauteur ; 0 survivant partout). Conformément aux règles 4 et 5, on ne retient pas de piste « fiable ».

Limites (à ne pas confondre avec un échec du lieu) :
1. **Signature de roche non discriminante** : les 51 « roches-signature » incluent talus de berge et murs ; la plus grosse suivie fait 50 m², très loin d'une « grande roche qui barre le ruisseau ». La vraie grande roche n'est peut-être pas dans cette liste.
2. **Modèle de pas / caps** : 0 survivant partout suggère que, soit les filtres (public + bâti ≥ 100 m + pente), soit le déroulement, soit la nature de la roche sont mal posés — le lieu peut exister sans être atteint par cette chaîne.
3. Le croisement du Mouret (bras NE, 21 m² dans le lit) et la branche est de J16 restent les deux meilleurs ajustements textuels, mais leurs points de fouille tombent tous soit dans le lit (pentu / à 25 m d'une maison), soit en parcelle privée.

**À tester ensuite** : (a) **ortho HD** sur les 12 roches atteintes (surtout 50 m² Tapon/Burge et 31 m² Rebouchet) pour voir si l'une est un vrai bloc qui barre ; (b) vérifier au **cadastre 1838** si une emprise publique (chemin/lit) longe ces roches, car le filtre « bâti ≥ 100 m » tue 10 quasi-manques plats et publics ; (c) revoir la **signature de roche** (un seuil de saillie plus bas ou détection de ressaut de lit) plutôt que les filtres de coffre.

---

## 7. Fichiers

- Scripts : `outils_scratch/r0610_C_lib.py`, `r0610_C_jonctions.py`, `r0610_C_roches.py`, `r0610_C_chaine.py`, `r0610_C_hasard.py`, `r0610_C_carte.py`.
- Données : `donnees_travail/r0610_C/` → `jonctions.json` (1 404 croisements attribués), `jonctions_chaine.json` (branches), `roches_all.json` (51 roches), `fouilles.json` (tous les points), `survivants.json` (0), `hasard.json`, `osm_hwy.json` / `osm_water.json` (OSM Overpass avec géométrie).
- Cartes : `images_travail/r0710_C_carte.jpg` (6 × 6 km), `images_travail/r0710_C_zoom.jpg` (2,8 × 2,4 km autour de la tour).
