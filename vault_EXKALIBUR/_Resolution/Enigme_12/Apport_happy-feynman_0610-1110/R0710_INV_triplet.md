# R0710_INV — Recherche INVERSE du triplet de l'É12 (eau cartographiée ≤ 10 m + bande publique ≤ 10 m + roche-signature ≤ 30 m) — 07/10/2026

**Verdict : PISTE FAIBLE — le triplet EXISTE, mais il est BANAL.** Aucune combinaison de seuils n'élimine la coïncidence tant que la « roche » reste la signature large (LRM ≥ 1,5 m, MNH < 3 m, ≥ 10 m²) : **8 894 cellules (3,5 ha, 49 amas)** dans 2,5 km. Le seul seuil qui tue le triplet est celui de la **grande** roche : LRM ≥ 2,5 m **et** ≥ 50 m² → **0**. La coïncidence eau+chemin+roche est donc **fréquente et ne localise rien** ; c'est la définition de la roche (et non la coïncidence) qui porte l'information.

Règles et faits : BUG corrigé — le MNH IGN est une **hauteur** (0–50 m, médiane 2,6 m) : la « canopée nue » est `MNH < 3` (et non `MNH − MNT < 3`) ; le DSM pour la visibilité est `MNT + MNH`. Grille 2 m sur la mosaïque LiDAR HD 6 × 6 km (1 m), géoréférence lue dans `lidar_meta.json` (X0 934000, YMAX 6489000), aucune taille en dur. Tour d'Avalon = (45,4288 / 6,03078) → L93 (936 938 / 6 485 589), sol 406,3 m. Cadastre Etalab (16 655 parcelles dans la fenêtre) + DGFiP personnes morales 38 ; **2 fichiers de commune corrompus (« NoSuchKey » : 38070, 38267)** → leur emprise est comptée « non cadastré » (limite connue).

---

## 1. Règle posée AVANT de regarder la carte (aucun paramètre ajusté)

Un point de la grille est **candidat** s'il réunit **simultanément** :
- **(a)** un **cours d'eau cartographié** à ≤ Dw — BD TOPO `troncon_hydrographique` (permanent **ou intermittent**, les 212 tronçons) + OSM `waterway` stream/river/ditch/drain/canal (géométrie réelle, `donnees_travail/r0610_C/osm_water.json`, 1 758 segments). Base Dw = 10 m. *(Les surfaces hydrographiques et le `wfs_cours_d_eau` sans géométrie ne servent pas.)*
- **(b)** une **bande publique de chemin** à ≤ Dp — cellule **publique** (parcelle DGFiP groupe 1-4 **ou** non cadastré) **ET** alignée sur un chemin (≤ 3 m d'un tronçon BD TOPO/OSM, hors autoroute/bretelle) ; pour la part **non cadastrée**, exige **plate** (≤ 15°) **et nue** (`MNH < 3`) — méthode r0710_MB/E1. Base Dp = 10 m.
- **(c)** une **roche-signature** à ≤ Dr — `LRM = MNT − gauss(MNT, 6 m) ≥ 1,5 m`, `MNH < 3 m`, blob ≥ 10 m². Base Dr = 30 m.

Périmètre : ≤ 2 500 m de la tour (**4 908 756 cellules** = 19,63 km²). Aucun filtre de visibilité / bâti / pente dans le triangle de base (il est appliqué ensuite).

---

## 2. Entonnoir de seuils (relâchement progressif)

| Étage | Seuils (eau/chemin/roche ; LRM, MNH) | Points |
|---|---|---|
| 0 | 5 / 5 / 10 ; LRM 2,0 ; MNH 3 | **48** |
| 1 | **eau 10** / 5 / 10 ; LRM 2,0 | 117 |
| 2 | eau 20 / 5 / 10 | 221 |
| 3 | eau 30 / 5 / 10 | 281 |
| 4 | 30 / **chemin 10** / 10 | 496 |
| 5 | 30 / chemin 20 / 10 | 986 |
| 6 | 30 / chemin 30 / 10 | 1 476 |
| 7 | 30 / 30 / **roche 30** | 6 963 |
| 8 | 30 / 30 / roche 50 | 15 174 |
| 9 | 30 / 30 / 50 ; **LRM 1,5** | 72 314 |
| 10 | 30 / 30 / 50 ; **LRM 1,0** | 165 684 |
| 11 | 30 / 30 / 50 ; LRM 1,0 ; **MNH 5** | 176 648 |
| 12 | 30 / 30 / 50 ; LRM 1,0 ; **MNH 10** | 196 384 |
| **B** | **BASE 10 / 10 / 30 ; LRM 1,5 ; MNH 3** | **8 894** |

Sensibilité (un seuil à la fois, base 10/10/30, LRM 1,5, MNH 3) :

| eau | 0 m | 5 | 10 | 20 | 30 | 50 |
|---|---|---|---|---|---|---|
| points | 2 223 | 5 345 | **8 894** | 14 653 | 20 402 | 29 099 |

| chemin | 0 m | 5 | 10 | 20 | 30 | 50 |
|---|---|---|---|---|---|---|
| points | 1 795 | 4 891 | **8 894** | 14 521 | 18 455 | 22 498 |

| roche | 0 m | 10 | 30 | 50 | 100 |
|---|---|---|---|---|---|
| points | 233 | 2 672 | **8 894** | 13 281 | 24 965 |

| LRM | 2,5 m | 2,0 | 1,5 | 1,0 | 0,5 |
|---|---|---|---|---|---|
| points | 658 | 1 514 | **8 894** | 24 130 | 48 504 |

**Le triplet n'est jamais nul** : même à (5/5/10) il reste 48 points (31 amas). Le seul levier qui compte est la **hauteur de la roche (LRM)** ; MNH est quasi sans effet (MNH 1 → 7 805, MNH 20 → 13 729).

---

## 3. Le triplet existe-t-il ? Oui — et il est banal (test du hasard)

Masques seuls et paires (2,5 km) :

| | cellules | part de 19,63 km² |
|---|---|---|
| eau ≤ 10 m | 287 533 | 5,9 % |
| chemin public ≤ 10 m | 769 154 | 15,7 % |
| roche ≤ 30 m | 327 558 | 6,7 % |
| eau **&** chemin | 58 126 | (1,29 × l'indépendance) |
| eau **&** roche | 30 706 | (1,60 ×) |
| chemin **&** roche | 76 775 | (1,50 ×) |
| **triplet** | **8 894** | **au lieu de 3 006 sous indépendance → 2,96 ×** |

Test du hasard (200 tirages par modèle ; `hasard.json`) :

| modèle nul | min | médiane | max | **P(X ≥ 8 894)** |
|---|---|---|---|---|
| eau décalée au hasard | 1 184 | 4 302 | 8 678 | **0,000** |
| roche décalée au hasard | 1 429 | 3 620 | 8 610 | **0,000** |
| chemin décalé au hasard | 1 641 | 4 133 | 8 328 | **0,000** |

**Lecture.** Le triplet réel (8 894) est au sommet de la distribution nulle — mais la **médiane du hasard est déjà à 4 300** : un paysage de vallées donne spontanément ~4 300 triplets. L'« effet » réel n'est qu'un **facteur ≈ 2**. **Thème témoin** (courbes de niveau à la place de l'eau) : tous les 5 m → **61 723** ; tous les 10 m → **42 815** — soit **7 × plus** que l'eau. ⇒ La coïncidence est **portée par la densité du réseau linéaire** (chemins + relief + eau), pas par l'eau : le triplet **ne discrimine pas** l'eau enchantée.

---

## 4. Où sont les amas, que valent-ils ? (base 8 894 cellules, 49 amas)

Après filtres de cohérence (public **ET** bâti ≥ 100 m **ET** pente ≤ 12°) : **519 cellules, 31 amas**. Hors Pontcharra : **12 amas**. Les plus gros (2 m de résolution) :

| lat, lon | m² | commune | d_tour | bâti | pente | visib. +33 m | roche dans le lit ? | chemin aboutit ? |
|---|---|---|---|---|---|---|---|---|
| **45,43951 / 6,05305** | 276 | Laissaud (73 141) / « Les Gorges » | 2 109 | 189 | 0,6° | non | **oui** (blob à 2,8 m de l'eau, 16 m²) | **oui, à 3 m** |
| 45,43142 / 6,06154 | 116 | St-Maximin (38 426) | 2 423 | 207 | 5,2° | non | — | non |
| **45,43205 / 6,03306** | 104 | St-Maximin (38 426) | **402** | 101 | 9,7° | non | — | non |
| 45,42201 / 6,05767 | 52 | St-Maximin | 2 234 | 691 | 4,6° | non | — | oui |
| 45,43599 / 6,03929 | 12 | St-Maximin | 1 039 | 148 | 1,8° | non | — | non |
| *(8 autres amas, 4-60 m², 1,8-11,8°, bâti 100-523 m)* | | | 400-2 484 | | | non | | |

Toutes les cellules du triplet sont en **non cadastré** (emprise de chemin/ruisseau) ou, rarement, en parcelle communale → **public**. La commune est **Pontcharra (38 314) pour ~60 %** des amas (exclus par la règle de Guilhem).

**Deux cas attendus du texte — vérifiés, tous deux présents et multiples :**
1. **« la roche pose sur le lit, le chemin longe »** : signature `d_eau_blob ≤ 3 m` — présente pour au moins **4 amas** (ex. 45,43951/6,05305 ; 45,43614/6,03687 ; 45,41459/6,02070 ; 45,4139/…). Donc **le motif existe**.
2. **« le chemin aboutit à la roche » (03-041)** : distance au plus proche **bout de chemin (degré 1)** — **≤ 30 m pour 13 des 20 plus gros amas**, dont 3, 4, 7, 8 m. C'est **trivial** : la BD TOPO compte des milliers d'extrémités de tronçons ; la clause ne filtre rien.

**Le déroulé peut-il y démarrer ?** Non, pas dans un lieu privilégié : les 12 amas hors Pontcharra sont dispersés (1,0 à 2,5 km de la tour, caps variés), **aucun n'est visible du rempart (+33 m)** au critère DSM = MNT + MNH, et leurs roches sont de **petits blobs (12-276 m² de zone, roche 16-164 m²)** qui **ne barrent rien** à l'échelle d'une « grande roche ». La seule « roche » publique, plate et isolée connue (R0610_R, #17 = 45,43952/6,05298, 14 m² sur le Bréda) **est** au cœur de l'amas n°1 — mais elle ne barre pas le ruisseau et reste invisible de la tour.

---

## 5. Variantes strictes — le seuil de la « grande roche »

| définition de la roche | cellules | amas |
|---|---|---|
| BASE — LRM ≥ 1,5 ; MNH < 3 ; ≥ 10 m² | 8 894 | 49 |
| abri — LRM ≥ 2,0 ; MNH < 2 ; ≥ 30 m² | 461 | 3 |
| **dure — LRM ≥ 2,5 ; MNH < 2 ; ≥ 50 m²** | **0** | **0** |
| **sévère — LRM ≥ 3,0 ; MNH < 1,5 ; ≥ 100 m²** | **0** | **0** |
| serré distances — eau 5 / chemin 5 / roche 10 | 625 | 31 |

⇒ Une **grande** roche à découvert (≥ 50 m², ≥ 2,5 m de saillie) **n'existe nulle part** en coïncidence avec eau+chemin dans les 2,5 km : le texte exige le seul élément qui manque. C'est le **même constat** que R0610_R (29 → 7 publiques → 0 complète) et R0710_C (0/168), retrouvé **par la voie inverse**.

---

## 6. Limites

1. **Signature de roche non discriminante** (la principale) : LRM ≥ 1,5 m capte talus, berges, mur, remblais ; 327 558 cellules à ≤ 30 m. Le comptage dépend du seuil ; seul l'ordre de grandeur est solide.
2. **Cadastre** : 2 communes corrompues (38070, 38267) → « public » surestimé sur leur emprise ; pas de DGFiP pour la Savoie (73) → parcelles savoyardes comptées privées (conservateur).
3. **Bande publique** : choix de l'emprise (3 m autour du chemin, règle E1) et « plate/nue » (15° / MNH < 3) sont des paramètres figés mais discutables.
4. Le test du hasard par **décalage** des rasters n'est pas exactement un tirage d'un réseau (il conserve la structure) ; il est néanmoins un nul valable de décorrélation.

---

## 7. Conclusion et suite

**Le triplet existe dans la zone — oui, et en abondance (49 amas, dont 12 hors Pontcharra, tous publics, plusieurs plats et isolés).** Il **ne localise pas** : la médiane du hasard (eau décalée) donne déjà ~4 300 points, un thème témoin (courbes de niveau) en donne 7 × plus. Le seul filtre qui tranche est la **« grande roche »** : LRM ≥ 2,5 m et ≥ 50 m² → **0**.

**À tester ensuite :**
1. **Réorienter sur la roche, pas sur les seuils de distance** : chercher les blobs LRM ≥ 2,5 m (≥ 30-50 m²) *isolés, hors canopée*, dans tout le LiDAR étendu — c'est le seul objet qui puisse faire office de « grande roche qui barre le lit » ; les 2,5 km n'en contiennent aucun en contexte eau+chemin.
2. **Traiter le non-cadastré** : obtenir les parcelles 38070 / 38267 et un DGFiP 73 pour lever le doute « public » sur les amas savoyards (n°1).
3. **Vérifier la visibilité** des 12 amas hors Pontcharra sur **ortho HR** (le DSM LiDAR + canopée peut masquer ce que l'œil voit au printemps).
4. **Contrôle indépendant** : faire recalculer l'amas n°1 (45,43951/6,05305, « Les Gorges »/Bréda) par un second agent — c'est le seul candidat qui cumule public + plat + isolé + roche dans le lit + chemin qui aboutit.

## Fichiers

- **Rapport** : `vault_EXKALIBUR/_Resolution/Enigme_12/R0710_INV_triplet.md`
- **Scripts** (`outils_scratch/`) : `r0710_INV_build.py` (rasters eau/chemin/public), `r0710_INV_triplet.py` (entonnoir + amas), `r0710_INV_detail.py` (descriptions + variantes), `r0710_INV_hasard.py` (hasard + thème témoin), `r0710_INV_final.py` (survivants + carte).
- **Données** (`outils_scratch/donnees_travail/r0710_INV/`) : `triplet.json`, `detail.json`, `hasard.json`, `final.json`, `meta.json` + rasters `.npy` (D_WATER, D_PUBPATH, PUB, PUBPATH, D_TOUR, SLOPE2, MNH2, CAD_COVER, PUB_PARC).
- **Cartes** (`images_travail/`) : `r0710_INV_triplet_6km.jpg`, `r0710_INV_triplet_zoom.jpg`.
