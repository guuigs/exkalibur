# R1110_ZF — Examen fin PUB02 (Lônes de Pontcharra) et PUB17 (Les Mollettes) (11/10/2026)

**Verdict : RIEN (au mieux PISTE FAIBLE non exploitable).** Aucune chaîne complète ne tient les contraintes dures. Le test du hasard est non significatif (P ≈ 0,22 pour PUB02 ; PUB17 n'a aucune clairière au sens strict). Les seules chaînes « publiques et plates » finissent à 7-10 m du Bréda, au bord d'un stade, ou le long d'un fossé jouxtant la voie ferrée. Le critère « bloc ≥ 1 m » est lui-même trop permissif pour discriminer (445 « blocs » sur 1,5 km² à PUB02, 521 à PUB17).

Scripts : `outils_scratch/r1110_zf_01_data.py` … `_08_resume.py`, `r1110_zf_lib.py`. Données : `donnees_travail/r1110_ZF/` (`B_mnt.npy`/`B_mnh.npy` = LiDAR HD 1 m des Mollettes téléchargé via IGN WMS-R `IGNF_LIDAR-HD_MNT/MNH_ELEVATION.ELEVATIONGRIDCOVERAGE.LAMB93` ; `A_/B_{route,hydro,bati,veg,surf}.json` BD TOPO ; `A_/B_osm.json` ; `cad/` cadastre Etalab de 9 communes ; `chaines_A/B.json` ; `tableau_chaines.json` ; `finalistes.json` ; `hasard_A/B.json`). Images : `images_travail/r1110_ZF/A_overview.jpg`, `B_overview.jpg`, `planche_A.jpg`, `planche_B.jpg`.

## 1. Règles (posées avant de regarder les résultats ; seul le seuil « clairière lâche » est une sensibilité annoncée)
- **Emprise** : PUB02 et PUB17 + 500 m. LiDAR 1 m : mosaïque r0610 (PUB02, MNH direct) ; PUB17 téléchargé (1 500×2 000 m, 0 % de trous).
- **Chemins** : BD TOPO `troncon_de_route` (hors autoroutier, rond-point, fictif) + OSM `highway` (hors motorway/trunk/primary/platform). Jonction = nœud de degré ≥ 3 dans chaque source, fusion à 15 m.
- **Clairière** : ≥ 55 % de MNH < 2 m dans 15 m ET ≥ 35 % de MNH > 6 m dans l'anneau 30-60 m. Variante lâche : ≥ 40 % / ≥ 25 %.
- **Eau** : BD TOPO hydro (hors buse, Isère, Bréda) + OSM waterway (hors river) + rives des plans d'eau < 6 ha. Parcours le long du réseau ≤ 400 m, dans les deux sens (gauche/droite non tranchable).
- **Bloc** : MNT − MNT lissé (σ = 6 m) ≥ 1 m, 2-300 m², ≤ 35 m, à ≤ 12 m de l'eau parcourue. Variante « stricte » : ≥ 1,5 m, ≥ 6 m², compacte, ≤ 4 m de l'eau.
- **Chaîne** : bloc + 10 pas N + 10 pas E (souche) + 8 pas au cap {61 ; 63,7 ; 68}°, pas {0,75 ; 1,0 ; 1,48} m = 9 fins par bloc.
- **Filtres du coffre** : parcelle publique (DGFiP groupes 1-4, ONF) ou point non cadastré (Etalab) ; pente LiDAR ≤ 8° ; bâti BD TOPO ≥ 80 m ; hors ENS Isère/Natura/RN (ENS Savoie non chargés) ; hors surface d'eau. Signalés sans éliminer : ZNIEFF I, distance stade/ZAI, distance Bréda/Isère.

## 2. Entonnoir
| | PUB02 (A) | PUB17 (B) |
|---|---|---|
| jonctions dans l'emprise | 89 | 55 |
| clairière stricte / lâche | 11 / 36 | **0** / 12 |
| blocs ≥ 1 m | 445 (3 « stricts », 15 chaînes) | 521 (1 strict, hors clairière) |
| jonctions avec eau ≤ 400 m + bloc | 17 | 11 |
| clairière stricte avec fin OK | 3 | 0 |
| clairière lâche avec fin OK | 8 | 3 |

PUB02 : le secteur est coincé entre le Bréda (O), le lac de Lône (N), le stade/complexe sportif et la ZAI (SE), la voie ferrée (E). La parcelle publique PUB02 est un liseré de ~2,4 ha sur le Coisetan. PUB17 : « forêt » = lisières de peupleraie/ronciers entre drains rectilignes (BD TOPO « Canal »), sous une ligne THT.

## 3. Tableau des chaînes complètes (fin centrale pas 1,0 / cap 63,7, sinon première fin valide)
| id | jonction (lat, lon) | roche | souche | coffre | fins OK | statut | pente | bâti / stade-ZAI | ZNIEFF I |
|---|---|---|---|---|---|---|---|---|---|
| A1 | 45.44088, 6.00832 (stricte; ouvert 0.83, forêt 0.53) | 45.44165, 6.00673 (relief 1.5 m, 32 m², eau 4 m, 150 m depuis la jonction) | 45.44174, 6.00686 | 45.44177, 6.00696 (pas 1.0, cap 63.7) | 9/9 | public (parcelle) | 3.3° (max segments 13.6°) | 236 m / 120 m | oui |
| A2 | 45.44490, 6.01447 (stricte; ouvert 0.81, forêt 0.48) | 45.44467, 6.01434 (1.1 m, 3 m², eau 3 m, 24 m) | 45.44476, 6.01448 | 45.44478, 6.01457 (pas 1.0, cap 68.0) | 1/9 | public (parcelle) | 5.4° (max 21.4°) | 136 m / 101 m | non |
| A3 | 45.43902, 6.01218 (stricte; ouvert 0.71, forêt 0.4) | 45.44000, 6.00946 (1.0 m, 2 m², eau 7 m, 238 m) | 45.44009, 6.00959 | 45.44012, 6.00968 (pas 1.0, cap 63.7) | 8/9 | public (parcelle) | 4.3° (max 13.5°) | 98 m / **34 m (stade)** | oui |
| B1 | 45.47012, 6.05627 (lâche; 0.67 / 0.31) | 45.46988, 6.05604 (1.1 m, 3 m², eau 7 m, 32 m) | 45.46997, 6.05618 | 45.47000, 6.05627 (pas 1.0, cap 63.7) | 6/9 | public (parcelle) | 4.9° (max 19.8°) | 413 m / 694 m | non |
| B2 | 45.47375, 6.05594 (lâche; 0.51 / 0.26) | 45.47351, 6.05573 (1.3 m, 4 m², eau 6 m, 26 m) | 45.47360, 6.05586 | 45.47363, 6.05596 (pas 1.0, cap 63.7) | 9/9 | public (parcelle) | 4.5° (max 29.1°) | 164 m / 510 m | non |
| B3 | 45.46938, 6.05343 (lâche; 0.41 / 0.44) | 45.46721, 6.05387 (1.2 m, 6 m², eau 3 m, 245 m) | 45.46734, 6.05407 | 45.46739, 6.05420 (pas 1.48, cap 61.0) | 2/9 | public (parcelle) | 5.1° (max 27.1°) | 395 m / 820 m | non |

Les autres chaînes valides sont les mêmes coffres atteints depuis d'autres jonctions (A1 : 5 jonctions de la zone ; A3 : 5 jonctions, dont 3 dans le stade). Pente max sur les segments roche→souche→coffre : 13-29° (rives, fossés) ; le trajet « à plat pour fauteuil » n'est tenu pour aucun.

## 4. Lecture des orthos 100×100 m (vision ; croix rouge = coffre, cyan = roche, magenta = souche, jaune = jonction)
- **A1** : forêt alluviale dense, aucune clairière visible, aucun chemin sous la croix ; la roche est le **bord d'un banc de galets du Bréda** (7 m). Coffre à 25 m du grand cours : contredit 06-180 ; inaccessible en fauteuil (sous-bois). **Rejet.**
- **A2** : bord d'un fossé rectiligne (Coisetan) entre maïs et pré ; **voie ferrée à ~35 m** ; la « roche » est le talus du fossé (3 m²). Autour de la jonction : champs, pas de forêt. **Rejet.**
- **A3** : rive du Bréda (10 m), route R. Pierre de Coubertin à 4 m, **stade à 34 m** ; roche = 2 m² de relief. **Rejet** (règle stade/ZAI).
- **B1** : végétation arbustive dense, pas de clairière, pas de chemin net ; roche = 3 m² de talus de drain. **Rejet.**
- **B2** : la plus plausible visuellement : bande herbeuse ouverte le long d'un chemin, lisière de ripisylve, ligne THT proche ; mais la « roche » est une berge de fossé de 4 m² (1,3 m), la jonction est OSM seule (clairière lâche), le chemin est un sentier de drain. Pas de gros bloc. **Rejet.**
- **B3** : bosquet entre maïs et ligne THT ; fossé ; pas de clairière. **Rejet.**

## 5. Visibilité depuis le chemin de rempart (FAQ05-155)
- PUB17 : LOS sol nu 0 % depuis la rue du Rempart (R1110_PUB, MNT 10 m) : contredit 05-155 ; cap 21° ≠ lever 63,7°.
- PUB02 : sol nu 88 % (R1110_PUB). Recalcul en DSM 1 m (MNT + MNH) depuis la rue du Rempart (+1,7 m) vers A1-A3 : **non visible** (obstacles sur la pente à > 100 m de l'observateur ; la cime de canopée de A1 et A3 est à ~0,5° de passer, A2 non). Dépend du point d'observation exact : indicatif, pas décisif.

## 6. Test du hasard (script 06)
1 500 points tirés au hasard sur le réseau de chemins du même secteur (proportionnels à la longueur), mêmes règles de clairière / eau / bloc / fins / filtres.

| secteur, clairière | jonctions réelles | avec fin OK | taux hasard | P(≥ réel) | roche stricte (réel / taux / P) |
|---|---|---|---|---|---|
| PUB02 stricte | 11 | 3 | 15,1 % (22/146) | **0,22** | 1 / 5,5 % / 0,46 |
| PUB02 lâche | 36 | 8 | 16,6 % | 0,24 | 2 / 5,7 % / 0,61 |
| PUB17 stricte | 0 | 0 | 37 % | 1,0 | 0 |
| PUB17 lâche | 12 | 3 | 26,2 % | 0,65 | 0 |

Limites : hasard interne au secteur (pas de LiDAR hors mosaïque et Mollettes pour d'autres morceaux publics plats). Les points tirés sur un même chemin sont corrélés ; la P réelle serait encore moins favorable.

## 7. Fiabilité
- **Fait** : emprises, données, filtres, tableau ; PUB17 sans clairière stricte ; A1/A3 collés au Bréda ; A3 au stade ; A2 à la voie ferrée.
- **Hypothèses** : « grand cours d'eau » = Bréda/Isère (06-180) ; bâti = BD TOPO ; ENS Savoie non vérifié (PUB17) ; « clairière » mesurée par MNH, pas par l'ortho seule.
- **Intuition** : néant. La chaîne « 10 N + 10 E + 8 pas » est courte (≈ 13-20 m) : avec 445-521 micro-reliefs, des fins valides apparaissent n'importe où ; sans bloc identifiable, elle ne discrimine pas.

## 8. Ce que montrerait une visite (non faite)
- A1 : un banc de galets du Bréda en forêt dense, probablement sans clairière ni chemin ; ZNIEFF I ; enterrement plausiblement impossible/interdit.
- A2/B2 : si un bloc ou un enrochement de berge existe, vérifier qu'il est mouillé en permanence (fossés d'irrigation/drainage). B2 est le seul endroit où chemin + bande herbeuse + lisière donnent une « jonction en clairière » plausible.
- Dans les deux secteurs, chercher d'abord une **vraie roche** (≥ 1 m de haut, ≥ 3 m de long) visible depuis le sentier : le LiDAR 1 m n'en montre pas dans les chaînes retenues.

## 9. Prochain test recommandé
Crible « roche stricte » (≥ 1,5 m, compacte, au bord de l'eau) sur toute la zone ≤ 8 km avec LiDAR HD IGN (WMS-R), pour trouver de vrais blocs au bord d'un ruisseau avant d'appliquer public / plat / bâti.
