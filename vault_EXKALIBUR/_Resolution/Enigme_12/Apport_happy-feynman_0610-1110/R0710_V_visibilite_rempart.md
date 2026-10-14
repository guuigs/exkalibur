# R0710_V — Visibilité depuis le **chemin de rempart** de la tour d'Avalon (hauteur réelle du mur mesurée au LiDAR), et chaîne du texte rejouée pour les croisements nouvellement visibles

**Sous-agent V · 07/10/2026 · État : FINAL.** Données : LiDAR HD 1 m (MNT+MNH, mosaïque 6 × 6 km) + BD TOPO + OSM + cadastre + ortho/plan IGN + sources web (OT Belledonne, Wikipédia, POP/Mérimée, atelierdesdauphins.com, rapport Jago, cadastre 1838).
Verdict : **RIEN** (0 point de fouille survivant, comme dans toute la zone ; le rejeu depuis le vrai chemin de rempart ne change pas le résultat). Deux acquis nets : (a) **la hauteur réelle du mur / chemin de ronde mesurée au LiDAR est de 3,1 m**, pas « sol + 1,7 m » ; (b) **sans cette hauteur la tour ne voit strictement aucun croisement** — c'est le seul apport de la surélévation.

---

## 1. Règle posée AVANT de regarder

- Observateur posé sur le **pourtour du mur de la tour d'Avalon** (et non « quelque part sur le site ») ; ligne de vue sur **DSM = MNT + MNH** (le MNH IGN est **déjà** une hauteur ; canopée comprise), tolérance 0,5 m, pas d'échantillonnage 3 m.
- Cibles : **tous** les croisements de chemins (≥ 3 directions) de BD TOPO + OSM à ≤ **2 500 m** de la tour (1 404 croisements dans la mosaïque, taille lue dans `lidar_meta.json`, aucune constante en dur).
- Un croisement est « visible » si son **sol** est vu ; les filtres de coffre (public, bâti ≥ 100 m, pente ≤ 12°, hors MH, hors Pontcharra) et le déroulement du texte (roche → 10 pas N → 10 pas E → souche → 8 pas aux caps 63,7/68,6/73,9°, pas 0,75/1,5 m) sont **repris à l'identique** de `R0610_R`/`R0710_C` (aucun paramètre ajusté).
- Interdit : choisir la hauteur du mur *après* avoir vu les résultats. La hauteur est **mesurée** (LiDAR) avant tout calcul.

## 2. Configuration réelle du site (web + LiDAR)

### 2.1 Ce que disent les sources
- La **tour d'Avalon** : 33 m de haut, diamètre intérieur ~8 m, murs de 2 m au 1er étage ; **reconstruite en 1895** par les chartreux sur les ruines du donjon (Wikipédia, OT Belledonne Chartreuse, Alpes-Isère). Inscrite MH le 05/10/1992 (notice Mérimée **PA00117375**, cad. B 1505, propriété communale).
- Elle est **construite sur une motte castrale** (« butte de terre ») ; des « remparts d'enceinte » entouraient la place forte ; le **fossé d'eau / vivier** est devenu le **marais d'Avalon** (ENS).
- Donjon médiéval : **26 m** avec échauguette (atelierdesdauphins) / ~20 m, 3 étages, murs 2,5 m au sol (rapport Jago, d'après l'enquête delphinale de 1339).
- **Enceinte du château : 112 m de périmètre seulement** (« un des plus petits châteaux du Dauphiné »), avec barbacane ; l'enquête de 1339 décrit ce rempart « **haut de 15 mètres** ». Le **bourg fortifié** avait **2 enceintes et 3 portes**, la seconde (1266) longue de **360 m** sur un axe N-S.
- Vestiges actuels (atelierdesdauphins) : « le mur du bourg, **partie la plus visible au Nord**, le long d'un chemin se dirigeant vers les bois ; on peut en hiver faire le tour des **remparts Sud et Ouest** ». Un « **Rue du Rempart** » existe à Avalon (90 m au nord de la tour).
- Cadastre de 1838 : le lieu-dit au pied du château s'appelle « **Le Chêne, La Roche et Le Vivier** » (terrains privés).
- Accès : **esplanade + table d'orientation, accès libre toute l'année**, 10 min à pied depuis le hameau d'Avalon (fiche OT, lat 45,428803 / lon 6,030846) ; la tour elle-même n'ouvre qu'en été (16-19 h, week-ends, 2,50 €).

### 2.2 Mesures LiDAR (MNT sol / MNH hauteur d'objet, DSM = MNT+MNH)
| Élément | MNT (m) | MNH (m) | Altitude surface (m) |
|---|---|---|---|
| Point « esplanade » de l'OT | 406,7 | **3,1** | 409,7 |
| Sommet de la motte (max MNT local) | 408,1 | — | — |
| **Tour** (centre, max MNH local) | 407,5 | **30,7** | 438,2 |
| Pourtour du mur (cercle R = 17,8 m, 22 points) | 401,9 – 406,9 | 0 – 3,6 (2,4-3,6 sur les caps 164-229°) | 401,9 – 407,1 |

- Le **sommet plat** (MNT 406-407) ne fait que ~20 × 30 m ; au-delà la motte plonge : MNT médian 401 à r = 20 m, 396 à r = 40 m, 379 à r = 90 m (350 m à 120 m à l'ouest, vers l'Isère). La motte est donc bien un éperon, mais **étroit**.
- Le LiDAR lit une **plateforme/terrasse de 3,1 m de haut** au point de l'esplanade, continue sur ~20 × 30 m (MNH 2-4 m) : c'est le **seul élément « mur » mesurable**. Aucun parapet plus haut n'existe au LiDAR (le mur de 15 m de 1339 est en ruine).
- L'orthophoto IGN 0,12 m/px confirme : la tour ronde est posée au centre d'une **terrasse herbeuse ovale** cernée d'un **mur de soutènement bas** (le « chemin de rempart » = le pourtour de cette terrasse / Place Saint-Hugues-d'Avalon, cf. plan IGN).

**Hauteur réelle retenue du mur / chemin de ronde : 3,1 m** (mesurée) — c'est ce qui remplace « sol + 1,7 m ».

## 3. Points de vue retenus (4 familles)

| Id | Description | Coord. | MNT sol | z œil |
|---|---|---|---|---|
| **P1** | sol de l'esplanade + 1,7 m | 45,428803 / 6,030846 | 406,7 | **408,4** |
| **P2** | sommet du mur / chemin de ronde + 1,7 m (hauteur mesurée 3,1 m) | 45,428803 / 6,030846 | 406,7 | **411,4** |
| **P3** | **pourtour complet du mur**, 22 points tous les 5 m (R = 17,8 m = enceinte de 112 m de périmètre), z = sol local + 3,1 m + 1,7 m | cercle autour de 45,428913 / 6,030971 | 401,9-406,9 | **406,6 – 411,8** |
| **P4** | sommet de la tour + 1,7 m | 45,428913 / 6,030971 | 407,5 | **439,9** |

*Réserve explicite* : le LiDAR ne tranche pas entre « esplanade = sol naturel (406,7) avec 3,1 m de mur à côté » et « esplanade = plateforme (409,7) ». Les deux lectures donnent le **même œil ~411,4 m** ; P1 = 408,4 est le plancher naturel. La sensibilité (§ 4.2) couvre tout l'intervalle.

## 4. Visibilité (DSM = MNT + MNH) — entonnoir par point de vue

Croisements ≤ 2,5 km : **1 053** (dont 729 dans Pontcharra) ; **324 hors Pontcharra**.

### 4.1 Entonnoir (hors Pontcharra)

| Point de vue | croisements visibles | …avec branche-eau | …avec roche-signature | points de fouille | **survivants** |
|---|---|---|---|---|---|
| **P1** esplanade sol + 1,7 | **0** | 0 | 0 | 0 | **0** |
| **P2** chemin de ronde + 3,1 m + 1,7 | **9** | 8 | 3 | 36 | **0** |
| **P3** pourtour du mur (22 pts) | **21** | 12 | 3 | 36 | **0** |
| **P2 ∪ P3** (le mur) | **21** | 12 | 3 | 36 | **0** |
| **P4** sommet de la tour + 33 m | **29** | 17 | 3 | 36 | **0** |
| *réf.* tous les croisements ≤ 2,5 km | 324 | 157 | 33 | 426 | 0 |

Avec Pontcharra : P2 → 107, P3 → 133, P4 → 168 (aucun n'a de branche-eau+roche survivante non plus).

**Fait central** : depuis le **sol de l'esplanade + 1,7 m on ne voit aucun croisement** (0) ; il faut **au moins + 3 m** (P2/P3) pour en voir. Autrement dit, *le « chemin de rempart » n'est pas un confort : c'est la condition de la visibilité*.

### 4.2 Sensibilité à la hauteur de l'œil (au-dessus du sol de l'esplanade, 406,7 m)

| hauteur d'œil | z œil | croisements | +eau | +roche | points | survivants |
|---|---|---|---|---|---|---|
| +1,7 m (sol, P1) | 408,4 | 0 | 0 | 0 | 0 | 0 |
| +3,0 m | 409,7 | 4 | 3 | 3 | 36 | 0 |
| +4,8 m (**mur 3,1 m, P2**) | 411,4 | 9 | 8 | 3 | 36 | 0 |
| +6 m | 412,7 | 10 | 9 | 3 | 36 | 0 |
| +10 m | 416,7 | 15 | 10 | 3 | 36 | 0 |
| **+15 m** (mur documenté de 1339) | 421,7 | 23 | 15 | 3 | 36 | 0 |
| +26 m (donjon médiéval) | 432,7 | 27 | 16 | 3 | 36 | 0 |
| +33 m (sommet, P4) | 439,7 | 29 | 17 | 3 | 36 | 0 |
| +41 m | 447,7 | 30 | 18 | 3 | 36 | 0 |

**Le résultat de la chaîne est invariant** : dès +3 m, les **3 mêmes croisements à roche** entrent, leurs 36 points de fouille sont les mêmes, et **aucun ne survit** — jusqu'à +41 m. Même en restituant le mur de 15 m de l'enquête de 1339, on ne gagne **aucune** roche nouvelle.

## 5. Rejeu de la chaîne du texte pour les croisements visibles du mur

21 croisements hors Pontcharra visibles du mur (P2 ou P3) ; **3** portent une roche-signature sur une branche-eau (règle « eau à gauche **ou** à droite ») :

| croisement | d tour | cap | roche (m², Δz eau) | 10 pas N + 10 E + souche + 8 pas | survivants |
|---|---|---|---|---|---|
| 45,418769 / 6,024468 | 1 218 m | 202° | 45,417640 / 6,025303 (10 m² ; 4,7 m) | 12 points | **0** |
| 45,435550 / 6,003434 | 2 266 m | 287° | 45,436815 / 6,004907 (20 m²) ; 45,437380 / 6,005015 (16 m²) | 12 points | **0** |
| 45,435579 / 6,003209 | 2 283 m | 287° | idem (2 roches, cascade) | 12 points | **0** |

Total : 36 points de fouille pour le mur, **36 échecs** (tous en lit pentu, à < 100 m d'une maison, ou en parcelle privée) ; **0 quasi-manque** hors le point ci-dessous.

### Quasi-manque (un seul filtre en échec)
- **45,437471 / 6,005180** (coffre), atteint depuis la **roche 45,437380 / 6,005015, cap 63,7°, pas 0,75 m** (celui du « jour dernier »), à **2 221 m** de la tour, cap **287°** (WNW, vallée du Bréda/Perrière) : **public** ✓ (« non cadastré » = emprise publique), **pente 1,9°** ✓, **hors MH** ✓, **hors Pontcharra** ✓, **bâti 46,9 m** ✗ (manque 53 m pour passer les 100 m de 05-107). C'est le seul point de la zone du mur qui échoue sur un unique critère — et il est visible **dès + 3 m** d'œil.

## 6. Carte
`images_travail/r0710_V_visibilite_rempart.jpg` (6 × 6 km, hillshade MNT, croisements ≤ 2,5 km colorés : rouge = vu du chemin de rempart, bleu = vu du seul sommet de la tour, gris = non vu ; roches atteintes et quasi-manque entourés) et `images_travail/r0710_V_zoom.jpg` (1,2 × 1,2 km). Tables : `donnees_travail/r0710_V/visib_table.md` (133 lignes) et `..._hors_pontcharra.md` (21 lignes).

## 7. Test du hasard (repris de `R0710_D`, même DSM corrigé)
Sur 1 000 observateurs fictifs du même paysage, « visible depuis le sol + 1,7 m » (0/0/7, méd. 0) : la tour en voit **0 au sol** et **9 sur le mur** (P ≈ 1,0 %, rang 1/1 000) ; sommet **29** (P ≈ 0,0 %). Mais le **compteur de survivants est 0 pour la tour comme pour les 1 000 fictifs** → la hauteur de la tour est un **artefact de position**, et la dernière étape de la chaîne **ne discrimine personne**. (Contrôle d'altitude de `R0710_C` : dès qu'on neutralise la hauteur, P retombe à 5-21 %.)

## 8. Verdict, limites, suite

**RIEN.** Refaire la visibilité avec la **vraie hauteur du chemin de rempart (3,1 m mesurés)** change bien le point de départ — de 0 à 9 croisements hors Pontcharra (21 pour le pourtour complet, 29 du sommet) — **mais ne change pas l'arrivée** : les 3 mêmes croisements à roche, les mêmes 36 points, **0 survivant**, et ce dès + 3 m comme à + 41 m. Le seul quasi-manque (45,437471 / 6,005180) ne doit pas être surinterprété : il tombe à 2,2 km du « chemin de rempart » annoncé comme « tout près » du coffre (06-244).

**Limites (honnêteté)**
1. Le LiDAR ne fournit **aucun mur de 15 m** : la « terrasse » de 3,1 m est le seul relief anthropique mesurable au sommet ; le mur de l'enceinte (112 m de périmètre, 15 m de haut en 1339) est arasé. Si le chemin de ronde du XIIIe siècle était à +15 m, la sensibilité § 4.2 montre que **cela ne change rien** (23 croisements, mêmes 3 roches, 0 survivant).
2. Le **pourtour du mur** est modélisé par un cercle de R = 17,8 m (enceinte de 112 m) ; le LiDAR ne montre un ressaut de 2,4-3,6 m que sur les **caps 164-229°** (côté S/SO). Ailleurs la hauteur retenue est celle du sol + 3,1 m reconstitué.
3. La **signature de roche** reste non discriminante (10-20 m², talus de berge possibles ; aucune des « grandes roches très difficiles à manquer » du texte).
4. Modèle d'observateur : le « plateau » LiDAR MNH 2-4 m peut être de la végétation basse et non de la maçonnerie ; l'ambigüité esplanade = sol (406,7) vs plateforme (409,7) est levée par la sensibilité (l'œil utile est ~411 m dans les deux cas).

**À tester ensuite (recommandé)**
1. **Ortho HD des 3 roches atteintes** (45,417640/6,025303 et 45,436815/6,004907 + 45,437380/6,005015) pour voir si l'une est un vrai bloc qui barre le lit — c'est la seule façon d'améliorer la chaîne, la visibilité n'étant pas le verrou.
2. **Vérifier l'emprise publique** autour du quasi-manque (45,437471 / 6,005180) au **cadastre de 1838** et au cadastre actuel : s'il existe une bande publique le long du Bréda, ce point deviendrait le premier candidat « mur-visible » complet de tout le dossier.
3. **Ne pas** continuer à chercher une hauteur de rempart plus haute : la sensibilité montre qu'elle n'apporte rien.

## 9. Fichiers
- Scripts : `outils_scratch/r0710_V_motte.py`, `r0710_V_mur.py`, `r0710_V_map1m.py`, `r0710_V_lib.py`, `r0710_V_visib.py`, `r0710_V_chaine.py`, `r0710_V_sens.py`, `r0710_V_table.py`, `r0710_V_carte.py`.
- Données : `donnees_travail/r0710_V/` → `motte_profil.json`, `mur_anneau.json`, `visib.json`, `visib_table.md`, `visib_table_hors_pontcharra.md`, `chaine.json`, `sens.json`.
- Images : `images_travail/r0710_V_visibilite_rempart.jpg`, `images_travail/r0710_V_zoom.jpg`.
- Sources web : `fr.wikipedia.org/wiki/Tour_d'Avalon`, `pop.culture.gouv.fr/notice/merimee/PA00117375`, `belledonne-chartreuse.com` (tour d'Avalon), `alpes-isere.com` (tour + table d'orientation), `atelierdesdauphins.com/forts/avalon/` (château, bourg fortifié, vestiges, évolution), `jago.fr/pathis/.../Avalon-rapport-final.2.pdf` (rapport de recherches municipal, cadastre 1838).
