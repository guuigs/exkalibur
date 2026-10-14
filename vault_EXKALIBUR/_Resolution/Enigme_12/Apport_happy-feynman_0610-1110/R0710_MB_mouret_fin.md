# R0710_MB — Le Mouret : une fin DIFFÉRENTE, sur un point de fouille public (07/10/2026)

**Verdict : PISTE FAIBLE** (une fin tient enfin sur un point **public, plat et isolé** — mais elle n'est pas au-dessus du hasard, et son maillon faible change de place selon la lecture).
**État : partiel** (1 point retenu + 1 variante ; critère « emprise réelle des chemins » exploré).

Tout est en Lambert 93 dans le code ; les coordonnées publiées sont WGS84.
Géoréférence : `r0610_j16est2_lib.py` (convention corrigée, MNH = hauteur, déjà validée — Rebouchet dans les talwegs LiDAR). Cadastre Etalab 38426 + DGFiP pm 38.

---

## 0. Le fait nouveau qui a guidé cette passe : la FAQ8 en direct

Une question posée en direct à l'auteur (FAQ8, `outils_scratch/faq8.txt`) :

> « Il est dit qu'à partir de la grande roche, faire dix pas au nord, dix pas à l'est, puis huit pas à l'ouest. Mais dans ce système, on revient sur ses pas… Est-ce que c'est normal ? »
> **Réponse :** « Euh alors, il n'est pas dit ça. […] vous faites dix pas au nord **et autant à l'est**. **Et ensuite ARRIVÉ A CE CHEMIN-LÀ, vous faites huit derniers pas.** Mais le parchemin ne vous détaille pas la nature de ces huit derniers pas. Donc il ne s'agit pas d'un aller-retour. »

Deux conséquences dures, **posées avant tout calcul** :
1. le déplacement est bien **10 pas N puis 10 pas E** (le « L ») ; la diagonale NE de 10√2 donne le **même point** (vérifié) ;
2. le point atteint après ces deux jambes (la « souche-majesté ») est **SUR UN CHEMIN** (« arrivé à ce chemin-là »). C'est donc un filtre de terrain : *le point intermédiaire doit tomber sur une bande de chemin*.
3. Corollaire : « le parchemin ne détaille pas la nature des huit derniers pas » → la nature du coffre se déduit de la **boussole** seule (question sur le « jour dernier » : « vous avez un élément dans le parchemin qui vous permet de déterminer ces huit pas »).

Autres réponses utiles relues : l'eau peut être suivie **en descendant ou en remontant** (« Le narrateur descend ou remonte les eaux enchantées — je ne répondrai pas ») ; au-delà de la roche on peut « marcher le long du ruisseau, mais ça supposerait de quitter votre route » (06-195/FAQ8) ; « le coffre n'est pas loin du chemin de rempart : Non » (06-244) ; « domaine public, pas de terrain privé » (01-235, 02-097, 03-098) ; « éloigné de tout bâtiment » (05-107) ; « fauteuil, accompagné » (03-112).

---

## 1. Cartographie du domaine public dans 400 m du Mouret (45.42243, 6.04030)

Grille 2 m sur 800 × 800 m (64 ha) ; `public` = parcelle personne morale publique (DGFiP groupe 1-4) **ou** trou de cadastre (non cadastré = emprise supposée de chemin/lit). Script `r0710_MB_diag.py`.

| | surface | part |
|---|---|---|
| **Total public** | **2,34 ha** | **3,7 %** |
| dont non cadastré (bandes de chemin + lit) | 2,04 ha | 3,2 % |
| dont 2 parcelles **communales** (Saint-Maximin) | 0,30 ha | 0,5 % |

* **Bandes publiques** (balayage E-O et N-S) : médiane **4 m**, q25 2 m, q75 6 m, q90 8 m, max 100 m. **Aucune** bande large et continue : le domaine public du secteur = un **réseau de chemins de 2 à 8 m**.
* **Parcelles communales** : seulement 2, toutes **inutilisables** — l'une (3 000 m², 45.42578/6.03994, 373 m du Mouret) porte **une maison à 23 m** et est à 29° de pente ; l'autre (30 m², 45.42300/6.03529) est collée à des maisons (8 m).
* **Lit et berges** : le ruisseau du secteur est le **Rebouchet, non domanial** → son lit et ses berges appartiennent aux **riverains** (pas de domaine public fluvial). Le « non cadastré » le long du ruisseau est un **artefact cadastral**, pas une emprise publique. → un coffre dans le lit n'est **pas** public.
* **ENS / forêt publique** : néant dans 400 m (les forêts communales commencent à ≥ 1,7 km à l'est).

**Conséquence (1)** : autour du Mouret, le **seul** terrain public exploitable est la **bande des chemins**. Le coffre doit tomber dedans.

---

## 2. Les lectures alternatives, posées avant de calculer, puis testées

Roches candidates = toutes les lectures du brief. Statut du coffre : cadastre **exact** (`cad.check`), pente LiDAR, bâti BD TOPO, bande publique (raster 2 m). Script `r0710_MB_final.py`, `r0710_MB_fins.py`, `r0710_MB_souche.py`.

| Lec. | « Grande roche » | Jonction | Coffre le plus favorable | Public ? | pente | bâti | Verdict |
|---|---|---|---|---|---|---|---|
| L1 | blob **99 m²** dans le lit du Rebouchet (45.42399, 6.04271) [bras NE, meilleur texte M1] | J1 4-bras | 45.424106, 6.042933 | non-cadastré ✓ | 8,1° | **33 m** ✗ | **ÉCHEC** (bâti) |
| L2 | **ressaut** du Rebouchet (45.423957, 6.04170) | J1 | 45.424020, 6.041870 | privé ✗ | 15-38° | 114 m | **ÉCHEC** |
| L3 | affleurement **48 m²** près de J2 (45.423697, 6.041412) | J2 | 45.423819, 6.041631 | bande ✓ | **43°** ✗ | 139 m | **ÉCHEC** (pente) |
| L4 | **bloc sous les arbres** = roche C (45.42462, 6.04078 ; LRM +2,25 m, 31 m²) | J2 | **45.424709, 6.041016** | non-cadastré ✓ | **5,9°** | **146 m** | **PASSE** |
| L5 | **source sortant du rocher** (hyp. P, 45.42177, 6.04019) | J1 | 45.421880, 6.040440 | privé B0257 ✗ | 24° | 179 m | **ÉCHEC** |
| L6 | **bloc du talweg au sud** (45.420245, 6.042310 ; LRM +2,0 m) | J1 | **45.420330, 6.042540** | **chemin public ✓** | **6,2°** | **103 m** | **PASSE** |
| L7 | diagonale NE de 10√2 au lieu du « L » | — | **identique à L1-L6** | — | — | — | aucun changement |
| L8 | diagonale NE de **10** pas (et non 10√2) | — | — | — | — | — | **0 survivant** |

Deux autres tests négatifs, importants :

* **Coffre dans l'emprise d'un chemin *cartographié* avec roche sur l'eau** (`r0710_MB_chemin.py`) : balayage de tous les points de chemin BD TOPO ≤ 400 m du Mouret, plats (≤12°), isolés (≥100 m), avec la roche remontée à ≤ 25 m d'eau cartographiée → **0 sur 118 croisements**. **La lecture littérale (suivre l'eau → roche → 10 N + 10 E + 8) ne peut pas poser le coffre sur un chemin *mappé* près du Mouret.**
* **Lecture FAQ8 stricte** (`r0710_MB_souche.py`) : intermédiaire sur une bande publique + coffre public/plat/isolé + roche = relief (LRM ≥ 1,5) ou bord d'eau → **63 hits / 2 amas** : (a) autour du bloc sud L6 ; (b) autour de J2 (roche à 11-15 m du ruisseau). Aucun amas ne coche *toutes* les clauses (voir §4).

---

## 3. Test du hasard (obligatoire)

Appliqué aux **118 croisements** ≥3 voies de la mosaïque LiDAR 2 × 3 km (hors Pontcharra, `r0610_C/jonctions.json`) ; même lecture, mêmes filtres. Scripts `r0710_MB_hasard.py`, `r0710_MB_hasard2.py`.

| Lecture | Croisements donnant ≥1 coffre public+plat+isolé | Mouret |
|---|---|---|
| roche **dans** l'eau (d_eau ≤ 3 m), 10 N + 10 E + 8 | **69 / 118 (58 %)** | 5 |
| roche au bord de l'eau (d_eau ≤ 8 m) | **76 / 118 (64 %)** | 13 |
| + relief de la roche **LRM ≥ 1,5** | 8 / 118 (6,8 %) | 1 |
| roche proche de l'eau (d_eau ≤ 20 m) | 89 / 118 (75 %) | 21 |
| **FAQ8 strict** (roche LRM ≥ 1,5 près de l'eau **et** intermédiaire sur chemin **et** coffre public/plat/isolé) | **9 / 118 (7,6 %)** | **0** |

**Conclusion (4)** : « tomber sur du public » est **banal** (58-75 % des croisements). Même la lecture FAQ8 complète réussit à **7,6 %** des croisements. Et le Mouret est **en dessous ou à** ce taux de base (terrain en pente). ⇒ Aucune de ces fins n'a de valeur de preuve ; le Mouret n'est pas privilégié par le hasard.

---

## 4. La meilleure fin — et ses faiblesses

### FINS RETENUE — « le bloc du talweg sud » (L6 / FAQ8 stricte)

| Étape | Lecture | Coordonnées |
|---|---|---|
| Jonction | le carrefour à 4 branches du **Mouret** (45.42243, 6.04030), en lisière du pré vu du rempart | — |
| « eaux enchantées » | le talweg qui descend du sud ; **on le remonte** (la FAQ autorise « descend ou remonte ») | — |
| « grande roche » | **bloc LiDAR sous les arbres** (LRM +2,0 m ; le MNH ne l'aère pas) | 45.420245, 6.042310 |
| + 10 pas N + 10 pas E | pas ≈ **1,0 m** → on **arrive sur le chemin** (bande publique 4 m) — la clause FAQ8 | 45.420330, 6.042440 |
| + 8 pas au jour dernier | az **90° (est)** → le coffre **dans l'emprise du chemin** (d_chemin 0,1 m) | **45.420330, 6.042540** |
| Coffre | **PUBLIC** (non cadastré), **pente 6,2°**, **bâti le plus proche 103 m**, cap 135,7° depuis le rempart, **1 314 m** de la tour, 289 m de la jonction, hors Pontcharra | **45.42033, 6.04254** |

**Justification ligne par ligne**
* « Dans la clairière, à la jonction des chemins » : le carrefour 4-bras du Mouret, en lisière du pré de 20 064 m² vu du rempart (validé 05/10).
* « j'ai suivi à senestre les eaux enchantées » : on remonte le talweg ; l'eau est du côté senestre du chemin qui le longe.
* « jusqu'à la grande roche » : un bloc affleure (relief LiDAR local +2,0 m, référence 45.420245/6.042310), à **3,3 m d'un chemin** — « un chemin débouche sur un rocher » (03-041), « elle vous bloquera le passage » (06-195).
* « puis fis dix pas au nord, autant à l'est » : **le point tombe sur le chemin** — exactement « arrivé à ce chemin-là » (FAQ8).
* « Arrivé à la souche-majesté » : la souche est *sur le chemin* (objet remarquable, invisible sur la carte).
* « je fis huit derniers pas, et ma boussole suivait le jour dernier » : 8 pas ≈ 8 m au cap est.
* « Là, tu trouveras la coupe du charpentier » : le point public, plat et isolé.

**Faiblesses (honnêtes, cumulées)**
1. **L'eau** : à la roche, `d_eau = 256 m` en BD TOPO/OSM — le talweg n'est **pas cartographié** (il existe en LiDAR : LRM en gouttière −1,85 m dans ±20 m). Toute la première clause repose donc sur un ruisseau non nommé.
2. **La pente** : la roche (35°) et l'intermédiaire (32°) sont sur un versant raide ; seuls les 8 derniers pas sont plats. Le « fauteuil » n'est tenu qu'au coffre.
3. **Le hasard** : 7,6 % des croisements donnent la même chaîne complète ; le Mouret est à **0** dans ce test. Aucune valeur de preuve.
4. **La distance** : 289 m de la jonction, 1 314 m du rempart, +271 m d'altitude — étire « tout près » (05-051) et « pas loin » (06-244).
5. **Le pas** : il faut prendre **1,0 m** (0,75 m place le coffre 2-3 m plus à l'ouest, hors bande). La FAQ8 refuse de dire si le pas est arrondi au dixième ou au centième.

### VARIANTE — « le bloc sous les arbres » (L4 / roche C)

Coffre **45.42471, 6.04102** (le « survivant » de R0710_M1) : lecture J2 (jonction en lisière du pré) → on suit le ruisseau à senestre → « grande roche » = le **bloc LiDAR de roche C** (45.42462, 6.04078 ; LRM +2,25 m, ~200 m² au seuil LRM≥1,5, à **6 m du ruisseau**) → 10 pas N + 10 pas E (pas 0,75 m depuis le bord-eau du bloc) → souche → 8 pas au jour dernier (63,7-90°).
Coffre **public** (non cadastré), **pente 5,9-10,3°**, **bâti 146-147 m**, **920 m** de la tour.
**Robuste** : valable pour les 4 azimuts (63,7 / 68,6 / 73,9 / 90°), pour 2 points de référence du bloc (bord E et bord NE) et pour le « L » comme pour la diagonale.
**Faiblesses** : (i) roche C est **sous canopée** (acceptée ici comme « bloc sous les arbres », sans roche nue) et **sur aucun des 4 bras** du Mouret ; (ii) le point intermédiaire n'est **pas** sur une bande (« arrivé à ce chemin-là » non tenu) ; (iii) la « bande publique » est un **trou de cadastre de 4 m dans les bois**, à **30 m de tout chemin** cartographié, à 0,3 m d'une limite privée (B0547) — fragile au mètre ; (iv) le chemin y est une corniche dans une pente à 45°.

**Compromis** : L6 (retenue) **place le coffre dans l'emprise d'un vrai chemin**, au prix d'un ruisseau non cartographié ; L4 (variante) **suit l'eau cartographiée**, au prix d'un chemin de cadastre dans les bois. Aucune ne coche les deux. C'est le résultat structurel de la passe : **au Mouret, « suivre l'eau jusqu'à la roche » et « arriver à ce chemin-là » tirent dans deux directions opposées.**

---

## 5. Fichiers

**Rapport** : `vault_EXKALIBUR/_Resolution/Enigme_12/R0710_MB_mouret_fin.md`
**Scripts** (`outils_scratch/`) : `r0710_MB_diag.py` (cartographie du public), `r0710_MB_fins.py` (lectures × roches × pas × az), `r0710_MB_inverse.py` (balayage inverse public), `r0710_MB_armes.py` (profil des bras), `r0710_MB_eaurock.py` (roche sur l'eau), `r0710_MB_chemin.py` (coffre dans l'emprise d'un chemin), `r0710_MB_souche.py` (lecture FAQ8 stricte), `r0710_MB_hasard.py` / `r0710_MB_hasard2.py` (hasard, 118 croisements), `r0710_MB_carte.py` (cartes).
**Données** (`outils_scratch/donnees_travail/r0710_MB/`) : `PUB.npy` (raster public 2 m), `PUB_mosaic.npy` (4 m, 2×3 km), `roches.json`, `bras.json`, `final_lectures.json`, `fins.json`, `inverse_hits.json`, `chemin_hits.json`, `souche_hits.json`, `hasard_croisements_*.json`, `hasard2.json`, `armes_profil.json`.
**Cartes** (`images_travail/`) : `r0710_MB_public.jpg` (domaine public + 4 bras + roches), `r0710_MB_rocheC.jpg`, `r0710_MB_fin.jpg`, `r0710_MB_fins.jpg`, `r0710_MB_lecture.jpg` (la lecture retenue J2 → roche → coffre).

**Liens** : script de géoréférence `r0610_j16est2_lib.py` ; rapport M1 `R0710_M1_mouret_variantes.md` ; faiblesses du Mouret `MOURET_FAIBLESSES_E12.md` ; FAQ8 `outils_scratch/faq8.txt` (réponse « arrivé à ce chemin-là »).

---

## 6. Ce qu'il faut tester ensuite

1. **Trancher la clause « arrivé à ce chemin-là »** : est-ce *n'importe quelle* bande de chemin (alors L6), ou le chemin **cartographié** (alors L6 tient encore, mais pas L4) ? Si le parent veut la solution la plus proche du texte, faire recalculer L6 et L4 par un second agent (contrôle indépendant).
2. **Le ruisseau enchanté non cartographié** : vérifier sur ortho HR + hydrographie IGN (cours_d_eau_intermittent, scan 25) s'il existe un talweg au sud du Mouret vers (45.4202, 6.0423) — c'est le point qui décide entre L6 et L4.
3. **Le pas** : tester 0,75 vs 1,0 m comme *cause* du choix (la FAQ refuse de répondre ; c'est un paramètre libre → pénalité).
4. **Ré-ouvrir J16** (`R0610_J16_est_v2`) : J16 a le même profil (cours d'eau + chemin public + bande large) ; la lecture FAQ8 y donne-t-elle un point public ? J16 = crible « depuis chez soi » à 240 m du rempart.
5. **Cadastre napoléonien 1838** (Archives de l'Isère) sur les deux points : chercher « la Roche », « le Chêne », et l'emprise réelle (largeur) de l'ancien chemin — c'est le seul moyen de trancher l'emprise publique.
