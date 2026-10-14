# R0710_M1 — Le Mouret : le déroulé depuis la grande roche varie-t-il vers un point accessible ?

**Date** : 07/10/2026 — **État : COMPLET** (toutes les variantes demandées, y compris la variante (g) de Guilhem du 07/10).
**Verdict : RIEN de fiable.** 1 199 runs de variantes, **3 survivants** — tous depuis **un seul point de départ** d'une roche **qui n'est ni la grande roche du texte ni sur un bras du Mouret**, et **au niveau du hasard**. La « grande roche » du Mouret (99 m²) ne donne **aucun** survivant, même en faisant varier toutes les étapes.

⚠️ **Bug trouvé dans la géoréférence/canopée des rapports antérieurs** (voir §6) : le filtre « roche nue » (`MNH − MNT < 3`) est un **no-op** ; la « grande roche 99 m² » du Mouret est en réalité un **bosse de terrain sous forêt** (MNHmax 27 m), pas nécessairement un rocher affleurant.

Géoréférence : réutilise `r0610_j16est2_lib.py` (convention corrigée, 2 points de contrôle validés). Filtres de réussite : **(public ou non cadastré) & bâti ≥ 100 m & pente ≤ 12° & ≥ 100 m de la tour & hors Pontcharra**. Mosaic LiDAR 2 × 3 km (X 936000-938000, Y 6484000-6487000), BD TOPO du dossier `r0610_j16est` (couvre le Mouret, X 937.7 k, Y 6484.9 k — **pas** la zone aveugle des 500 m nord), cadastre Etalab + DGFiP pm 38 / 38426.

---

## 1. Rappel du point de départ et du déroulé de base (reproduit, 12 points)

Le Mouret est un **carrefour à 4 branches BD TOPO** (rayon ~7 m) à **45.422430, 6.040300** — commune **Saint-Maximin (38426)**, pas Pontcharra (vérifié par géocodage inverse IGN : « Route du Mouret », 497 route du Mouret 38530 Saint-Maximin).
Branches (chaînage BD TOPO) : **bras 0 cap 265° (O)** chemin → route ; **bras 1 cap 73° (E)** chemin → sentier → chemin → route empierrée (941 m) ; **bras 2 cap 32° (NE)** sentier → sentier → chemin (675 m) ; **bras 3 cap 191° (S)** sentier ×2 (710 m).

Roches-signature du dossier (ancienne signature, buggée, §6) à ≤ 400 m du carrefour : **3** —
**(A) 99 m²** à 45.423990, 6.042706 (dite « grande roche », d_eau 0,7 m, dans le lit du Rebouchet, à 40 m du bras 2) ;
**(B) 21 m²** à 45.423639, 6.043711 (d_eau 5,7 m, à 1,3 m du bras 2) ;
**(C) 31 m²** à 45.424619, 6.040783 (246 m du carrefour, cap 6,6° — **sur aucun bras**).

Déroulé de base (centroïde des roches A/B, 10 pas N + 10 pas E + 8 pas, pas ∈ {0,75 ; 1,5} m, azimuts 63,7/68,6/73,9°) : **12 points, tous en parcelle privée** (B0595, B0636, B0613), **bâti 22,4–41,8 m**, **pente 30,2–53,6°** → **0 survivant**. *(Reproduit au chiffre près le §4 de R0610_J16_est_v2.)*

---

## 2. Variantes une à une (puis par paires) — décompte

`r0610_M1_variantes2.py` — **1 055 runs** sur les 3 roches A/B/C (axes a–f) + 2 roches du bras 2 pour (g).

| Axe | Variantes testées | Runs | Survivants |
|---|---|---|---|
| **V0 base** | centroïde A/B, 10N+10E, 8 pas | 12 | **0** |
| **(b) longueur du pas** | 0,6 / 0,7 / 0,8 ; 1,4 / 1,5 / 1,6 ; **0,296** (pied romain) ; **1,48** (pas romain) | 42 | **0** |
| **(c) nord** | nord vrai ; **magnétique** (+2,5°) ; **E-O inversé** (10 N puis 10 O) ; azimut miroir (180−az) | 36 | **0** |
| **(d) souche** | roche+**10 N seul** ; roche+**10 E seul** ; roche+**1 pas** ; vraie souche (max canopée MNH ≤ 40 m) | 36 | **0** *(aucun arbre MNH ≥ 6 m détecté ≤ 40 m — cf. §6)* |
| **(e) jour dernier** | 30/04/1524 (63,7/68,6/73,9°) ; **Pâques 1524** (81,4° = 6 avril grég. / 88,0° = 27 mars julien) ; **opposé coucher** (+180°) | 20 | **0** |
| **(f) 2e roche** | roche B (21 m²) toutes variantes | (inclus) | **0** |
| **(a) pourtour** | **chaque point du pourtour** des roches A/B/C (24 pts) × 3 az × 2 pas | 396 | **3** (roche **C** seulement) |
| **(g) bras du Mouret, eau d'un côté ou de l'autre** | voir §3 | (inclus) | **0** |

**Total 1 055 runs → 3 survivants** (tous depuis la roche C). Filtre progressif : 1 055 → public/non cadastré **122** → + bâti ≥ 100 m **18** → + pente ≤ 12° **3**.

### Les 3 survivants (le seul « positif »)

Roche **C** (31 m², 9 × 6 m, MNHmax **22,9 m** → **sous arbre**, 8,2 m de dénivelé interne, à 6 m d'un ruisseau, 246 m N du carrefour, sur **aucun** des 4 bras) ; **point de départ unique** = son **bord est**, 45.424627, 6.040847 :

| az | pas | coffre | parcelle | bâti | pente | d_eau | d_chemin |
|---|---|---|---|---|---|---|---|
| 63,7° | 0,75 | **45.424718, 6.041012** | non cadastré (chemin/ruisseau) | 146,6 m | 10,3° | 14,8 m | 30,1 m |
| 68,6° | 0,75 | 45.424714, 6.041014 | non cadastré | 146,6 m | 5,9° | 14,8 m | 30,1 m |
| 73,9° | 0,75 | 45.424709, 6.041017 | non cadastré | 146,4 m | 5,9° | 14,7 m | 30,1 m |

*(les 3 points sont à ≤ 1 m l'un de l'autre ; azimuts du 30/04 ; **pente ≤ 15° et bâti ≥ 80 m ne changent rien** : toujours 3.)*

**Pourquoi ces 3 points ne sont PAS retenus** (4 raisons cumulées) :
1. **la roche C n'est pas « la grande roche »** du texte (31 m², sous canopée, hors du bras NE décrit) et **n'est sur aucun des 4 bras** du Mouret (155 m du bras 2) ;
2. **fragilité** : 3 survivants sur 205 runs de la roche C ; **1 seul point de départ sur 22** du pourtour ; **pas = 0,75 uniquement** ; pas 1,5 → 0 ; toutes les autres variantes (b–f) → 0 ;
3. **le « public » est un artefact** : le point tombe **à 0,3 m de la limite** de la parcelle privée B0547 (et à 3,1 m de B0666) — c'est un **trou de cadastre**, pas une parcelle publique ;
4. **niveau du hasard** (§4).

---

## 3. Variante (g) [Guilhem, 07/10] — eau à gauche OU à droite, chaque bras du Mouret

`r0610_M1_variantes2.py` (blobs signature, ≤ 60 m des bras) + `r0610_M1_g_map.py` (blobs **relâchés** : LRM ≥ 1,2, aire ≥ 5 m², d_eau ≤ 20 m, ≤ 60 m des bras).

| Bras | cap | eau à gauche | eau à droite | roches-signature ≤ 60 m | roches relâchées ≤ 60 m | déroulé complet |
|---|---|---|---|---|---|---|
| **0 (O)** | 265° | 5/66 | 8/66 | **0** | 3 (23/18/8 m², MNHmax 4,7–10,9) | 0 survivant |
| **1 (E)** | 73° | 13/95 | 2/95 | **0** | **0** | sans objet |
| **2 (NE)** | 32° | 21/68 | 32/68 | **2** (A 99 m², B 21 m²) | 9 (297/101/55/39 m², MNHmax 24–29) | **0 survivant** |
| **3 (S)** | 191° | 0/72 | 0/72 | 0 | 0 | pas d'eau → sans objet |

144 runs (g relâché sur les 2 plus gros blobs de chaque bras avec eau) → **0 survivant**.
**Conclusion (g)** : l'eau d'un côté **ou** de l'autre ne sauve rien — **bras 0 et 1 suivent bien un cours d'eau mais n'ont aucune roche-signature** ≤ 60 m ; **bras 3 n'a pas d'eau** ; **bras 2** a des roches mais son déroulé (toutes variantes) échoue. Élargir la définition de « roche » (blobs relâchés, y compris sous canopée) ne change rien : **0**.

---

## 4. Test du hasard (obligatoire) — la variante (a) n'est PAS au-dessus du hasard

`r0610_M1_hasard_a.py` — on applique **exactement la même variante (a)** (départ sur le pourtour, 24 points × 3 az × 2 pas) à **toutes** les roches-signature du secteur :

| Jeu | Roches | Runs | Survivants | Roches donnant ≥ 1 survivant |
|---|---|---|---|---|
| signature « ancienne » | **30** | 3 156 | **99** | **5 / 30** (46, 32, 12, 6, **3**) |
| signature « corrigée » (MNH<3) | **10** | 912 | 76 | **2 / 10** (46, 30) |

- La roche C du Mouret (3 survivants) est **exactement dans la moyenne basse** ; **5 roches sur 30** font au moins aussi bien, et **une roche (109 m², 45.43612/6.03680, ~940 m N de la tour) en donne 46**. ⇒ **la variante (a) fabrique des « survivants » presque partout : c'est du bruit**.
- Références de fond : déroulé **standard** depuis 40 roches du secteur → **0 / 156** ; points uniformes dans la fenêtre → **1,26 %** passent tous les filtres ; dans un rayon de **400 m autour du Mouret → 0,15 %**. Les 1 055 runs → 3 hits = **0,28 %**, pour 3 points confondus à ≤ 1 m (soit **1 point** réel vs ≈ 1,8 attendus au hasard). ⇒ **au niveau du hasard, pas au-dessus**.

**By-product à transmettre** : la roche **corrigée** de **109 m² à 45.43612, 6.03680** (MNHmax 0,1 m = vraiment nue, sur le Rebouchet amont, 1,9 m de l'eau, 940 m N de la tour) produit **46 points** plats (pente ~3–12°), isolés (bâti ≥ 100 m) et « non cadastrés » autour de **45.43622, 6.0374**. Hors mission M1 (1,5 km du Mouret, à la limite de Pontcharra) mais **c'est le seul endroit du secteur où le déroulé « marche » en masse** — à tester à part.

---

## 5. Ce qui est acquis / ce qui tombe

**Acquis**
- La géoréférence corrigée (`r0610_j16est2_lib`) est **bonne** : le Rebouchet (BD TOPO) tombe bien dans les talwegs LiDAR (médiane LRM −0,88 m, 69 % < −0,5 m) ; le Mouret tombe sur le carrefour BD TOPO ; la parcelle du Mouret est en **Saint-Maximin (38426)**, hors Pontcharra.
- Le Mouret **est** le seul lieu du secteur où l'on suit l'eau (bras 2, senestre **ou** dextre) jusqu'à une grosse anomalie de relief dans le lit — mais **cette anomalie n'est pas une roche nue** (§6) et **le déroulé échoue de façon robuste**.
- Le versant est tout en **pente 20–53°** avec bâti à 20–45 m : **aucun** des 1 199 points de fouille n'est plat et isolé sur le pourtour immédiat de la « grande roche ».

**Fait notable (négatif)** : **faire varier UNE étape ne suffit pas** — ni le point de départ (pourtour), ni le pas (0,296 → 1,6 m), ni le nord (vrai/magnétique/inversé), ni la souche, ni le jour (Pâques/coucher), ni le choix de la 2e roche, ni l'eau à droite. Il faudrait **plusieurs** modifications simultanées et une **autre roche** pour espérer un point viable, ce que le texte n'autorise pas.

---

## 6. ⚠️ Bug de la « canopée » — à corriger dans les rapports antérieurs

Dans `r0610_j16est2_lib.py` : `CANOPY = MNH_F − MNT_F`, mais **`mnh.npy` n'est pas un MNS absolu : c'est déjà un modèle de HAUTEUR** (min −0,5 m, max 46,7 m, moyenne 6,9 m — idem dans `donnees_travail/r0610_R_roches/` : −1,6 / 69,1 / 8,2). Donc `MNH − MNT ≈ −350 à −750 m` → **le critère S2 « canopée < 3 m » (roche nue, ni arbre ni bâtiment) n'a JAMAIS filtré quoi que ce soit** (script `r0610_j16est2_roches.py` l.23 et la signature de `R0610_R_nature_roche` §1.3).

Conséquences mesurées (secteur Mouret) :
- avec le filtre **correct** `MNH < 3 m` : **0 roche-signature à ≤ 400 m du Mouret** ; seulement **10** dans toute la mosaïque 2 × 3 km (toutes ≥ 1,4 km), dont la roche de 109 m² de §4 ;
- avec le filtre buggé : 30 roches, dont la « grande roche 99 m² » du Mouret — **MNHmax = 27 m ⇒ sous arbre**, la « 2e roche 21 m² » MNHmax = 23 m, la roche C MNHmax = 23 m.
- Idem pour l'inventaire des **29 roches** de `R0610_R_nature_roche` (§2) : il inclut des boss de terrain sous forêt. **Recommandation : rejouer `r0610_R_roches.py` avec S2 = `MNH < 3`** avant toute réutilisation (le candidat public #17, le 109 m² de §4, etc.).

Autre correction : dans `r0610_M1_*.py`, `Ti.transform` renvoie **(lon, lat)** — une première version en (lat, lon) avait produit 690 runs « hors grille » (détecté et corrigé ; les scripts livrés sont sains).

---

## 7. Fichiers

**Rapport** : `vault_EXKALIBUR/_Resolution/Enigme_12/R0710_M1_mouret_variantes.md`

**Cartes** (`images_travail/`) :
- `r0710_M1_mouret_carte.jpg` — Mouret, 4 bras, eau/routes, blobs (ancien vs corrigé), nuage des points de fouille ;
- `r0710_M1_roches_corr.jpg` — roches du secteur : ancienne signature (orange) vs corrigée MNH<3 (bleu) ;
- `r0710_M1_survivant_zoom.jpg` — zoom : blob 31 m², point de départ, les 3 points « survivants ».

**Scripts** (`outils_scratch/`) : `r0610_M1_mouret.py`, `r0610_M1_diag.py`, `r0610_M1_variantes.py` (axes a–f + paires, 1 442 runs), `r0610_M1_roches_corr.py` (bug canopée), **`r0610_M1_variantes2.py`** (final, a–g, 1 055 runs), `r0610_M1_g_map.py` ((g) relâché + cartes), `r0610_M1_detail.py` (détail/robustesse), `r0610_M1_hasard_a.py` (test du hasard).

**Données** (`outils_scratch/donnees_travail/r0610_M1_mouret/`) : `variantes_full.json` (1 055 runs), `variantes.json`, `roches_corr.json`, `bras_roches.json`, `bras_mouret.json`, `g_relache.json`, `hasard.json`, `hasard_a.json`, `masques.json`, `blobs.json`.

---

## 8. Prochaine étape recommandée

1. **Arrêter le Mouret** comme zone finale : la « grande roche » n'est pas une roche nue et le déroulé échoue de façon robuste (0/1 199 hors bruit).
2. **Corriger S2 (`MNH < 3`) et rejouer** `r0610_R_roches.py` + `r0610_R_final.py` : le tri « public + plat + isolé » sur 29 roches est à refaire sur la base corrigée.
3. **Tester la roche nue de 109 m² (45.43612, 6.03680)** et son point 45.43622, 6.0374 : seul lieu du secteur où le déroulé donne des points plats/isolés en série ; vérifier la commune réelle (limite 38314/38426) et l'emprise (lit de la Bréda/Rebouchet vs chemin).
