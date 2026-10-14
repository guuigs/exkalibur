# R0710_L4_variante — Contrôle INDÉPENDANT de la variante L4 (« coffre 45.424709, 6.041016 »)

**Date** : 07/10/2026 · **Sous-agent** L4-VARIANTE · **État : partiel assumé** (tous les points de la mission ont été calculés ; les seuils d'acceptation du projet sont rappelés à chaque fois).
**Verdict : RIEN.** La variante L4 (coffre 45.424709, 6.041016, roche C) **ne tient aucune de ses propres clauses** : « grande roche » = pente boisée sous canopée sans affleurement (ni ortho HR ni LiDAR) ; « senestre » = faux (l'eau cartographiée est à **dextre**) ; « arrivé à ce chemin-là » = **jamais** satisfait sur tout le pourtour de la roche et les deux sens (0/2 208) ; la robustesse annoncée (2 points de référence, « L » et diagonale) est fausse ; enfin le protocole appliqué aux autres roches-signature est **plus productif ailleurs** (8/39 roches donnent la chaîne complète, 0 pour roche C) → **L4 est en dessous du hasard**.

Tout est recalculé de zéro : `outils_scratch/r0710_L4v_lib.py` + `r0710_L4v_01…12_*.py` (aucune reprise des scripts `r0610_C_*.py`, `r0610_M1_*.py`, `r0710_MB_*.py`). LiDAR HD lu via `lidar_meta.json` (mosaïque 6 × 6 km, X0 934000, Y0 6483000, 1 m) ; **MNH = hauteur** (0–70 m), **DSM = MNT + MNH** ; BD TOPO V3 + OSM (géométries réelles) ; cadastre Etalab + DGFiP personnes morales. Coordonnées publiées en WGS84.

---

## 0. Contrôle de la géoréférence (prérequis)

Les points d'eau BD TOPO à ≤ 400 m de roche C tombent bien dans les **talwegs** LiDAR : **LRM médian − 0,69 m, 58 % < − 0,5 m** (216 points). La tour (6.030971, 45.428913) tombe sur sa motte (MNT 407,5 m ; MNH 30,7 m = hauteur du bâti). ⇒ **géoréférence valide** ; les chiffres ci-dessous ne sont pas décalés (contrairement à la mosaïque `r0610_j16est`, 500 m).

**Ce qui a été reproduit à l'identique** du rapport `R0710_MB` : le coffre publié **45.424709, 6.041016** (= bord E du « bloc », pas 0,75 m, az 73,9°) sort au chiffre près ; d_bâti (polygone) **146,0 m** (ils annonçaient 146,4) ; pente 5,9° ; non cadastré ; le « trou de cadastre » fait **3 × 5 m**, à **0,12 m** de la limite de B0547 et **2,98 m** de B0666 (ils annonçaient 0,3 m et 3,1 m). La géométrie est donc reproductible — c'est le **sens** de la lecture qui ne l'est pas.

---

## 1. Jonction de départ : J2, et l'eau est à DEXTRE

**Le carrefour à 4 branches (45.42243, 6.04030) ne mène PAS à roche C.** Extraction de ses bras BD TOPO/OSM (chaînage, virage max 110°) : distance minimale d'un bras à roche C = **155 m** ; aucun bras ne se dirige au nord (caps 56 / 100 / 127 / 196 / 211 / 248°). Le carrefour est relié à **J2** par un sentier BDT de 153 m.

**J2 (45.42337, 6.04166) est le seul départ possible** : c'est exactement le **bout d'un sentier BDT de 446 m** (d=0,1 m). En marchant de J2 vers la roche :
- le point du sentier le plus proche de roche C est à **s = 171 m** de J2 (dans la fourchette « 150 à 300 m ») ;
- **le Rebouchet (eau cartographiée) est du côté DROIT (dextre)** sur **78 %** du tracé (≤ 30 m), **0 % à gauche** ; marche **inverse** = 78 % à gauche. Le ruisseau se rapproche de 42 m (à J2) jusqu'à **6 m** au niveau de la roche.

⇒ La phrase « j'ai suivi **à senestre** les eaux enchantées » est **fausse pour le seul chemin qui atteint roche C** (eau à dextre). Elle ne serait vraie qu'en parcourant le sentier en sens inverse (N→J2), c'est-à-dire en partant d'ailleurs que de la jonction. Depuis la décision de Guilhem (07/10 : senestre n'est plus un filtre) ce n'est pas éliminatoire, mais c'est une **correction factuelle** au rapport MB qui écrivait « on suit le ruisseau à senestre » : c'est l'inverse.

---

## 2. Nature de roche C : NI une grande roche, NI un bloc

**Orthophoto HR (IGN ORTHOIMAGERY.ORTHOPHOTOS, WMS)** : à 200 m comme à 80 m de côté, le point est **en pleine canopée** (feuillus denses) ; **aucun affleurement rocheux visible**, aucun bloc nu. Le pré est à l'ouest, la forêt à l'est.

**LiDAR** (carte `r0710_L4v_lidar_rocheC.jpg`) :

| Mesure | Valeur |
|---|---|
| centre : MNT / MNH (hauteur) | 465,9 m / **10,4 m** (sous arbre) |
| centre : LRM (saillie sur gauss 6 m) | **+ 2,25 m** |
| centre : pente | **38,2°** |
| blob connexe LRM ≥ 1,5 m | **200 m²**, 30 × 33 m, relief interne **11,9 m**, MNH max 22,9 m, pente moyenne **28,9°** |
| blob connexe LRM ≥ 2,0 m | **17 m² seulement** (6 × 4 m) |
| coupe N-S (centre) | MNT **478 → 444 m sur 45 m** = pente **35–49° régulière** |
| distance à l'eau cartographiée | **6,0 m** (Rebouchet) ; roche **5,2 m AU-DESSUS** de l'eau |
| distance au sentier | 13,7 m ; bâti 129 m ; tour 910 m |
| cadastre | **privé** (384260000B0547, Saint-Maximin 38426) |

**Conclusion (2)** : roche C est un **segment de versant forestier raide** où le LRM dépasse localement 1,5 m (oscillation ±2–3 m sur une pente courbe) ; il n'y a **pas de masse rocheuse compacte** (le cœur LRM ≥ 2 n'est que 17 m²). Elle ne « barre » pas le ruisseau : elle est sur la **berge**, 5 m au-dessus, à 6 m de l'eau. Le faisceau FAQ (bloc mouillé qui bloque le passage, « difficile à toucher sans se mouiller ») **n'est pas satisfait**. ⇒ la « grande roche » de L4 n'est pas identifiée ; c'est la **bosse de terrain sous forêt** déjà signalée dans `R0710_M1` § 6.

---

## 3. Le déroulé — point d'arrivée pour chaque combinaison

Départ = **bord est du bloc** (45.424627, 6.040847), 10 pas N puis 10 pas E (souche), puis 8 pas au cap.

| pas (m) | az | souche (intermédiaire) | **COFFRE** | parcelle | pente | bâti | d_chemin | d_tour | vu du rempart | filtre |
|---|---|---|---|---|---|---|---|---|---|---|
| 0,75 | 63,7 | 45.424694, 6.040943 | **45.424718, 6.041012** | non cadastré | 10,3° | 150 m | 30,1 m | 913 m | non | **PASSE** |
| 0,75 | 68,6 | 45.424694, 6.040943 | 45.424714, 6.041014 | non cadastré | 5,9° | 150 m | 30,1 m | 913 m | non | **PASSE** |
| 0,75 | 73,9 | 45.424694, 6.040943 | **45.424709, 6.041016** | non cadastré | 5,9° | 150 m | 30,1 m | 914 m | non | **PASSE** |
| 0,75 | 90,0 | 45.424694, 6.040943 | 45.424694, 6.041019 | non cadastré | 11,4° | 149 m | 30,6 m | 915 m | non | **PASSE** |
| 1,00 | 63,7 | 45.424717, 6.040975 | 45.424749, 6.041066 | privé B0666 | 58,6° | 156 m | 24,7 m | 915 m | non | échec |
| 1,00 | 68,6 | 45.424717, 6.040975 | 45.424743, 6.041070 | privé B0666 | 58,6° | 156 m | 24,8 m | 915 m | non | échec |
| 1,00 | 73,9 | 45.424717, 6.040975 | 45.424737, 6.041073 | privé B0666 | 55,0° | 155 m | 24,9 m | 916 m | non | échec |
| 1,00 | 90,0 | 45.424717, 6.040975 | 45.424717, 6.041077 | privé B0666 | 45,9° | 154 m | 25,5 m | 917 m | non | échec |
| 1,50 | 63,7 | 45.424762, 6.041039 | 45.424810, 6.041176 | privé B0666 | 47,7° | 166 m | 13,8 m | 919 m | non | échec |
| 1,50 | 68,6 | 45.424762, 6.041039 | 45.424801, 6.041181 | privé B0666 | 50,5° | 166 m | 14,1 m | 920 m | non | échec |
| 1,50 | 73,9 | 45.424762, 6.041039 | 45.424792, 6.041186 | privé B0666 | 49,4° | 166 m | 14,3 m | 921 m | non | échec |
| 1,50 | 90,0 | 45.424762, 6.041039 | 45.424762, 6.041192 | privé B0666 | 53,2° | 165 m | 15,2 m | 923 m | non | échec |

*(48 points calculés au total pour 4 points de départ × 3 pas × 4 az : `donnees_travail/r0710_L4v/deroule.json`. Le « L » (10 N puis 10 E) et la diagonale NE de 10√2 donnent le **même** point — la somme des déplacements est commutative — donc « robuste pour L et diagonale » ne teste rien.)*

**Ce que le tableau dit** :
1. le point publié est **reproduit** (pas 0,75, az 73,9) ;
2. le survivant **n'existe qu'à pas = 0,75 m** ; à 1,0 et 1,5 m la fouille tombe en **parcelle privée B0666** sur **46–59°** de pente → échec. Le paramètre libre « pas » **décide** du résultat (aucune règle ne le fixe : la FAQ refuse de dire s'il est arrondi au dixième, cf. `R0710_MB` § 4 note 5) ⇒ pénalité « paramètre ajusté » ;
3. la « robustesse pour 2 points de référence (bord E **et bord NE**) » annoncée dans MB est **fausse** : depuis le bord NE aucun azimut ne passe (privé B0666).

---

## 4. Filtres (par point, sur le coffre publié)

| Filtre | Valeur | Verdict |
|---|---|---|
| Parcelle (cadastre + DGFiP pm38) | **non cadastré** = trou de **3 × 5 m**, limites B0547 à **0,12 m**, B0666 à 2,98 m | public **fragile au mètre** |
| Pente (LiDAR) | 5,9° (mais 45–59° pour les combinaisons voisines) | OK au seul point publié |
| Distance au bâti (BD TOPO) | **146 m** (polygone) / 150 m (centroïde) | OK |
| Distance à la tour | **913 m** | OK (> 100 m) |
| Visibilité depuis le rempart (DSM) | **NON** — bloqué par le terrain même **sans** canopée (dépassement **+ 12,1 m** du MNT sous la ligne à 848 m de la tour ; **+ 32,1 m** avec canopée) | échec « vu du rempart » |
| Distance au chemin cartographié | **30 m** | la « bande publique » n'est **pas** un chemin |
| Hors Pontcharra | Saint-Maximin (38426) | OK |

---

## 5. Balayage du pourtour de roche C et des deux sens — « arrivé à ce chemin-là »

Protocole : **92 points du pourtour** du blob LRM ≥ 1,5 m ; 2 sens (10 N + 10 E et 10 E + 10 N) ; pas ∈ {0,75 ; 1,0 ; 1,5} ; az ∈ {63,7 ; 68,6 ; 73,9 ; 90} → **2 208 runs**. Sortie : `donnees_travail/r0710_L4v/perimetre_C.json`.

| Mesure | Résultat |
|---|---|
| coffres passant le filtre standard (public + plat + isolé) | **50 / 2 208** (2,3 %), tous dans le **même** trou cadastral (dispersion **9 m**) |
| distance du **coffre** au chemin cartographié | min **27,4 m**, médiane 29 m |
| distance de la **souche** au chemin cartographié | min **9,2 m** — **jamais** ≤ 6 m (0 / 2 208) |
| intermédiaire sur une bande publique **ET** coffre OK | **0 / 2 208** |
| coffres visibles depuis le sommet de la tour | **0 / 50** |

**Réponse (5)** : **NON.** Aucune variante de L4 ne satisfait simultanément « on suit l'eau cartographiée » **et** « on arrive à un chemin public » **et** « coffre public/plat/isolé ». Le seul « public » disponible est un trou de cadastre de 3 × 5 m dans les bois, à **30 m de tout chemin cartographié** et à **12 cm** d'une limite privée : ce n'est pas « le chemin » de la FAQ8. Le point intermédiaire ne tombe **jamais** sur un chemin (min 9,2 m). C'est le même résultat structurel que `R0710_MB` § 4 : au Mouret, « suivre l'eau » et « arriver à ce chemin-là » **tirent en sens opposés** — et mon calcul indépendant le confirme sur **tout** le pourtour, pas seulement sur quelques points.

---

## 6. Test du hasard — la même lecture sur TOUTES les roches-signature

Même protocole pour chaque roche : départ = centre + 12 points du pourtour (rayon = √(aire/π)) ; 3 pas ; 4 az ; 2 sens. Jeux : `roches_signature.json` (29, ancienne signature) + `roches_corr.json` (10, corrigée MNH < 3). Sortie : `donnees_travail/r0710_L4v/hasard_roches.json`.

| | roches | ≥ 1 coffre OK | ≥ 1 **chaîne complète** (coffre OK + intermédiaire sur bande) |
|---|---|---|---|
| **Roche C (Mouret)** | 1 | **3** | **0** |
| Toutes les autres | 38 | **11 roches** | **8 roches** |

- **Onze roches sur trente-neuf fabriquent un « coffre public/plat/isolé »** avec la même recette. Roche C n'est donc **pas** privilégiée ; elle est **en dessous** sur la chaîne complète : **8 autres roches** donnent la chaîne entière (à **méthode strictement identique**, 13 départs chacune) alors que roche C n'en donne **aucune** — y compris quand on lui offre **92 départs** sur son pourtour (§ 5 : 0 / 2 208).
- Champions : **#16** (45.43952, 6.05298, le seul candidat public de `R0610_R`) = **153 coffres** et **85 chaînes** ; **#34** (109 m², 45.43612, 6.03680, le sous-produit de `R0710_M1`) = **61 / 61** ; #11 (45.41458, 6.02112) = 38 / 38.
- **Taux de base du filtre « coffre OK » sur des points aléatoires** : **4,44 %** sur la mosaïque 6 × 6 km, **0,07 %** dans la fenêtre de 500 m autour de roche C. Les 50 survivants sont tous **un seul et même** trou de cadastre (dispersion 9 m) : le protocole **ne fait que déverser des points sur la même anomalie cadastrale**, pas produire une convergence.

⇒ **L4 est au niveau du bruit, et même un peu en dessous** (0 chaîne complète).

---

## 7. Cartes et fichiers

**Cartes** (`images_travail/`) :
- `r0710_L4v_carte_ortho600.jpg` — ortho 600 m : roche C (magenta), coffre publié (blanc), J2 (bleu), carrefour (vert), sentier (jaune) ;
- `r0710_L4v_lidar_rocheC.jpg` — hillshade LiDAR 300 m, LRM ≥ 1,5 m (rouge) et ≥ 2,0 m (jaune) : anomalies réparties le long du **talweg** et des pentes, pas de bloc isolé ;
- `r0710_L4v_survivants.jpg` — ortho 300 m avec les 50 coffres survivants (rouge), le départ (cyan), roche C (magenta) ;
- `r0710_L4v_ortho_600m/300m/200m/80m.jpg` — orthos brutes.

**Scripts** (`outils_scratch/`) : `r0710_L4v_lib.py`, `r0710_L4v_01_geo.py`, `_02_jonctions.py`, `_02b_dbg.py`, `_03_sentier.py`, `_04_carrefour.py`, `_05_ortho.py`, `_06_lidar.py`, `_07_deroule.py`, `_08_perimetre.py`, `_09_hasard.py`, `_10_checks.py`, `_11_carte.py`, `_12_base.py`.
**Données** (`donnees_travail/r0710_L4v/`) : `deroule.json`, `perimetre_C.json`, `hasard_roches.json`.

---

## 8. Tableau récapitulatif — clause par clause

| Clause de L4 / du texte | Contrôle indépendant | Verdict |
|---|---|---|
| « dans la clairière, à la jonction des chemins » = J2 | J2 = bout d'un sentier BDT ; le carrefour 4-branches **n'atteint pas** la roche (155 m) | ✅ J2 est le **seul** départ, mais ce n'est pas le carrefour |
| « à senestre les eaux enchantées » | eau à **DEXTRE** (78 % du tracé J2 → roche ; 0 % à gauche) | ❌ **faux** (non filtrant depuis le 07/10) |
| « la grande roche » | pente boisée 35–49°, sous canopée, cœur LRM 17 m², **aucun affleurement** à l'ortho | ❌ **pas une roche** |
| « elle vous bloquera le passage » / mouillée | roche 5,2 m **au-dessus** de l'eau, sur la berge | ❌ |
| « dix pas au nord, autant à l'est » | OK (mais pas = 0,75 m seulement) | ⚠️ paramètre libre |
| « arrivé à ce chemin-là » | intermédiaire jamais sur un chemin (min 9,2 m) ; **0 / 2 208** | ❌ |
| coffre public | trou de cadastre 3 × 5 m, à 0,12 m d'une limite privée, **30 m de tout chemin** | ⚠️ public **fragile/artefact** |
| coffre plat | 5,9° au point publié, mais 45–59° pour les combinaisons voisines | ⚠️ |
| coffre isolé (≥ 100 m du bâti) | 146 m (polygone) | ✅ |
| vu du rempart | **non** (12 m de terrain sous la ligne, sans canopée) | ❌ |
| hors Pontcharra | Saint-Maximin (38426) | ✅ |
| robustesse « 4 azimuts, 2 bords, L et diagonale » | 4 azimuts OK ; **bord NE échoue** ; L = diagonale (même point) | ❌ claim partiellement faux |
| au-dessus du hasard | 11/39 roches font un coffre OK, **8/39 font la chaîne complète**, roche C = 0 | ❌ **en dessous du hasard** |

---

## 9. Recommandations

1. **Clore L4** : verdict RIEN. Ne plus citer ce coffre comme « la variante qui suit l'eau » — il ne tient ni la nature de la roche, ni la côte de l'eau, ni la clause FAQ8, ni la visibilité, ni la robustesse.
2. **Réutiliser le vrai apport de ce contrôle** : le protocole « 10 pas N + 10 pas E + 8 au jour dernier » n'a **aucune valeur de preuve** (il produit des coffres « publics » sur 11/39 roches, dont 8 avec la chaîne complète). Ne l'employer qu'avec un **filtre dur** qui le rende rare (par ex. intermédiaire **sur le chemin cartographié** *et* roche = relief LRM ≥ 1,5 sur ≥ 30 m² *et* eau à ≤ 8 m).
3. **Le seul test qui tranche L4 vs L6** reste la nature de la roche : exiger un **affleurement visible** (ortho HR + MNH < 3 m) élimine roche C ; vérifier de même le « bloc du talweg sud » de L6 (45.420245, 6.042310, également sous arbres d'après le LiDAR ici utilisé).
4. **Ne pas confondre « non cadastré » et « public »** : les 50 survivants de roche C sont un trou de cadastre 3 × 5 m dans les bois, à 30 m de tout chemin ; tout rapport futur doit exiger la **coïncidence « non cadastré ET ≤ 6 m d'un chemin cartographié »** (jamais réalisée ici).
5. Le **paramètre « pas »** (0,75 m) est la variable qui décide du point publié : tant que la FAQ refuse de le fixer, tout point qui n'existe qu'à une seule valeur de pas doit être traité comme **bruit**.
