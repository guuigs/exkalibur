# R0710_D — Départ de l'É12 : recalcul de l'arrivée de l'É11, inventaire des « chemins de rempart », chaîne rejouée par départ alternatif

**Sous-agent D · 07/10/2026 · État : FINAL (2 séances de calcul, données LiDAR 1 m + OSM + BD TOPO + cadastre)**
Verdict : **RIEN / tour d'Avalon reste le seul départ non réfuté.** Aucun autre « chemin de rempart » du corridor ne donne de point de fouille survivant, et aucun ne bat la tour sur le seul critère où elle était en tête (le champ de vision). Deux faits nouveaux nets : (a) **le bug canopée change l'entonnoir** (le « 179 visibles » de `R0710_C` devient ≤ 29) ; (b) **quatre fortifications candidates sont hors des données LiDAR** et ne sont pas testables en l'état.

---

## 1. Règle posée AVANT de regarder

- Arrivée É11 = point à `D(E10)·π` de Saint-Palais, au cap géographique Saint-Palais → dernier chevalier. Modèle de l'É11 = **sphère** (haversine R = 6 371,0088 ; c'est celui qui a validé l'É11). Le modèle **WGS84 géodésique** est donné en regard, car il décale le cap de +0,07°.
- Variantes « défendables » : origine ∈ {centre, mairie, église Sainte-Madeleine} ; D(E10) ± 0,5 % ; multiplicateur π exact ; cap ± 0,05°.
- Le départ É12 = ce point ; sa nature doit être « chemin d'un mur ou d'une tour » (FAQ8), **pas une formation naturelle**, **point précis** (07-268), **accessible tous les mois** (06-020), et l'endroit doit être **dans le champ de vision** (05-155).

## 2. Arrivée de l'É11 recalculée et ellipse d'incertitude

Script `outils_scratch/r0710_D_11_arrivee.py` → `donnees_travail/r0710_D/arrivee.json`.

- D(É10) = 193,125 km → **D·π = 606,720 km**.
- Sphère : SP(centre) → château Bayard = **606,621 km, cap 64,9935°** (reproduit exactement l'É11 : `O_verif_consummatum.out.txt`).
- **Arrivée de référence** (centre + π exact + D exact + cap SP→Bayard) = **45,423918 / 6,020085**.
  - écart au **château Bayard** (45,423611 / 6,018889) : **99 m** → le fameux « dépasser très finement » (07-256) est reproduit à 1 m près.
  - écart à la **tour d'Avalon** : 996 m (la tour est à +1,0 km).
- **Variante WGS84** (cap 65,0632°) : arrivée 45,419706 / 6,003658, à **1 365 m** de la référence. Les deux modèles sont à ≤ 1,4 km — c'est-à-dire bien à l'intérieur de l'incertitude de la distance.

**Ellipse d'incertitude (36 variantes)** — `arrivee.json.ellipse` :
| axe | 1 σ | 2 σ | étendue totale | rayon max |
|---|---|---|---|---|
| le long de la ligne (cap ~70°) | **± 2 571 m** | ± 5 142 m | 7 337 m | 3 998 m |
| en travers | **± 450 m** | ± 900 m | 3 542 m | — |

Lecture : l'incertitude est **presque entièrement longitudi­nale** (± 0,5 % sur D(É10) domine, ± 3,03 km), le travers ne fait que ± 0,45 km. Variantes extrêmes : D −0,5 % → 45,4146/5,9836 ; D +0,5 % → 45,4333/6,0566 ; cap ±0,05° → ±529 m ; origine église/mairie → 200-400 m. Corridor au-delà de l'arrivée (cap 64,99°) : +3 km = 45,4353/6,0549 ; +5 km = 45,4429/6,0782 ; +8 km = 45,4543/6,1130.

## 3. Inventaire des « chemins de rempart » du corridor

Script `outils_scratch/r0710_D_inventaire.py` (OSM `historic=*` bbox 45,0-45,8/5,6-6,4 + BD TOPO toponymie + repères `R0610_T1`).
`lateral` = distance signée à la droite de l'arrivée (négatif = côté ouest/amont) ; `along` = distance **au-delà** de l'arrivée le long de la droite.

| # | Site | lat / lon | d. arrivée | sur la droite | Accessible 12/12 ? | « chemin de rempart » ? |
|---|---|---|---|---|---|---|
| 1 | **Tour d'Avalon** (esplanade) | 45,428803 / 6,030846 | **1,00 km** | along +0,99 / lat −0,14 | **OUI** — « accès libre toute l'année » (alpes-isere.com, OT) | **OUI** (tour + enceinte XIVe) |
| 2 | **Château Bayard** | 45,423611 / 6,018889 | 0,10 km | along −0,10 / lat −0,01 | NON — sur rendez-vous (privé) | OUI (maison forte 1404) |
| 3 | Château de Beauregard | 45,441350 / 6,044984 | 2,74 km | along +2,58 / lat −0,94 | NON — privé | OUI (château) |
| 4 | Château Le Clément | 45,435650 / 6,028570 | 1,46 km | along +1,15 / lat −0,90 | NON — chambres d'hôtes (privé) | NON (manoir/résidence) |
| 5 | Château des Augustins | 45,441730 / 6,033120 | 2,23 km | along +1,76 / lat −1,37 | NON — privé, « bâtiments très remaniés » | NON (ancien prieuré) |
| 6 | Fort Barraux | 45,435335 / 5,987118 | 2,87 km | along −1,79 / lat **−2,24** | NON (visites mai-sept. + septembre ; 1h30 à 15h) | OUI (chemin de ronde) |
| 7 | Château de Maximy | 45,433538 / 5,977835 | 3,47 km | along −2,54 / lat −2,36 | NON — privé | NON (manoir 1703) |
| 8 | Château du Fayet | 45,417645 / 5,972474 | 3,78 km | along −3,66 / lat −0,94 | ? (privé) | OUI (château) |
| 9 | Vestiges château fort de La Buissière | 45,411915 / 5,973183 | 3,90 km | along **−3,88** / lat −0,34 | ? (ruine, accès à vérifier) | OUI (château fort) |
| 10 | Château de Bellecombe | — | 5,57 km | lat −5,27 | NON — privé | OUI |
| 11 | Citadelle de Montmélian | 45,500682 / 6,054624 | 9,31 km | lat −6,60 | site | OUI (hors corridor) |

- **Toponymes « rempart »** : aucun « Chemin des Remparts » dans le corridor ; le seul est **« Rue du Rempart »** (Avalon, 45,429725/6,031411, voie publique, ~90 m au nord de la tour) — déjà testé négatif (t57).
- **Seuls sites à la fois SUR la droite et « chemin de rempart »** : **château Bayard** (arrivée) et **tour d'Avalon** (+1,0 km). Les autres sont soit **hors ligne** (lateral ≥ 0,9 km, souvent > 2 km), soit **en amont** (along négatif : Fayet −3,7 km, La Buissière −3,9 km — donc *avant* le point calculé, incompatibles avec D·π).
- Le site le plus proche **au-delà** de l'arrivée est **Beauregard** (lat −0,94 km, +2,58 km) ; les suivants sont hors du corridor ou privés.

## 4. Chaîne complète rejouée par départ (DSM corrigé — canopée)

Scripts `outils_scratch/r0710_D_lib.py` (corrige `CANOPY = MNH`, `DSM = MNT + MNH`), `r0710_D_chaine.py`, `r0710_D_chaine2.py` → `donnees_travail/r0710_D/chaine_departs*.json`.

Entonnoir identique à `R0710_C` (jonction visible → branche qui suit l'eau, gauche **ou** droite → roche-signature → 10 pas N → 10 pas E → souche → 8 pas aux caps → filtres public / bâti ≥ 100 m / pente ≤ 12° / hors MH / hors Pontcharra), mais **DSM corrigé**, et deux modèles d'observateur : au sol (+1,7 m) et **sur le rempart** (sol + hauteur de structure + 1,7 m).

| Départ (dans la mosaïque LiDAR) | visible (sol) | visible (mur) | dont eau (mur) | dont roche (mur) | **survivants** | d. tour |
|---|---|---|---|---|---|---|
| **Tour d'Avalon (esplanade)** | 0 | **9** | 8 | 3 | **0** | 5 m |
| **Tour d'Avalon (sommet +33)** | 0 | **29** | 16 | 3 | **0** | 23 m |
| Château Bayard (arrivée) | 0 | **0** | 0 | 0 | **0** | 1 094 m |
| Château Le Clément | 0 | 2 | 0 | 0 | 0 | 780 m |
| Château des Augustins | 0 | 0 | 0 | 0 | 0 | 1 448 m |
| Château de Beauregard | 0 | 4 | 3 | 0 | 0 | 1 782 m |
| Rue du Rempart (Avalon) | 1 | 2 | 0 | 0 | 0 | 114 m |

**Effet du bug canopée** (visibles, modèle mur) : tour esplanade 136 → **9** ; tour sommet 176 → **29** ; château Bayard 111 → **0** ; Beauregard 148 → **4** ; Augustins 42 → **0** ; Le Clément 45 → 2. Autrement dit l'entonnoir de `R0710_C` partait d'un ensemble gonflé ; l'ensemble corrigé est **≤ 29** (et ≤ 9 au niveau du chemin de rempart lui-même). Le **0 survivant final tient**.

**Sites hors données** : Fort Barraux, Maximy, Fayet, La Buissière sont à l'**ouest de la mosaïque LiDAR** (x < 934 000 ; seuls 16 croisements sur 1 404 y sont) → **non testables sans nouvelles dalles**. Ils sont de toute façon hors ligne (lateral ≥ 0,34 km, le plus souvent ≥ 2 km) ou en amont.

**Test du hasard (1 000 départs fictifs, DSM corrigé)** — `r0710_D_hasard2.py` :
| compteur | fictifs min/méd/max | tour mur | tour sommet | Bayard mur |
|---|---|---|---|---|
| visibles (sol +1,7) | 0 / 0 / 7 | 9 (**P = 0,0 %**) | 29 (0,0 %) | 0 (100 %) |
| visibles (sommet structure) | 0 / 0 / 15 | 9 (**P = 1,0 %**) | 29 (0,0 %) | 0 (100 %) |
| dont roche (sommet) | 0 / 0 / 3 | 3 (P = 0,2 %) | 3 (0,2 %) | 0 |
| **survivants** | **0 / 0 / 0** | 0 (**100 %**) | 0 | 0 |

La tour garde le meilleur champ de vision (top ~1 % en contrôlant la hauteur), mais **la dernière étape (roche → pas → coffre) ne discrimine personne** : 0 survivant pour la tour, pour les 1 000 fictifs et pour tous les départs alternatifs. Château Bayard, en fond de vallée sous couvert, voit **0** jonction : il ne peut pas être le rempart d'où l'on voit « l'endroit apparu ».

## 5. Verdict

**Un autre départ est-il plus crédible que la tour d'Avalon ? NON.**
1. Sur la droite de l'É11, seuls **château Bayard** et **la tour d'Avalon** sont des « chemins de rempart ». Bayard est **privé (sur RDV, échec 06-020)** et **aveugle (0 croisement visible)** ; il est en outre *le lieu que l'on dépasse*, pas le rempart d'arrivée. Beauregard, Le Clément, Augustins, Maximy, Fayet sont **privés** ; Fort Barraux et Maximy sont **hors ligne** ; Fayet et La Buissière sont **en amont** du point calculé.
2. La chaîne complète, rejouée depuis chaque départ testable avec le **DSM corrigé**, donne **0 point de fouille survivant** partout — comme depuis la tour.
3. Le seul avantage de la tour (champ de vision) reste réel même après correction (P ≈ 0-1 %), mais **le test du hasard montre qu'il vient de sa hauteur**, pas d'un signal de l'énigme — conclusion inchangée par rapport à `R0710_C`.

**Rien ne réfute la tour d'Avalon, mais rien ne la confirme non plus de façon décisive.** Verdict global : **RIEN** (pas de départ alternatif fiable).

### Limites (honnêteté)
- **Données** : la mosaïque LiDAR (6×6 km, x ≥ 934 000) **exclut** Fort Barraux, Maximy, Fayet, La Buissière ; leur entonnoir n'est pas calculé. Un test complet demande d'étendre la mosaïque vers l'ouest (nouvelle passe `r0610_R_fetch_lidar`-like + re-détection des roches).
- **Modèle d'observateur** : résultats sensibles à la hauteur. Le chemin de rempart est modélisé « sur le mur » (sol + MNH + 1,7 m) ; le LiDAR ne distingue pas un parapet d'un arbre.
- **Roche-signature** : les 51 roches détectées restent petites (≤ 50 m² suivies) ; la « grande roche » du texte n'y est peut-être pas.
- **Modèle géodésique** : sphère vs WGS84 décale l'arrivée de 1,4 km (1 365 m), dans le sens de la longueur ; cela n'affecte pas le classement des sites (Bayard/Avalon restent les deux seuls sur la ligne).

### À tester ensuite (recommandé)
1. **Étendre la mosaïque LiDAR à x ∈ [931 000, 934 000]** et rejouer l'entonnoir pour **Fort Barraux** et **La Buissière** (les deux seuls autres remparts un peu plausibles) — c'est la seule lacune de données du dossier.
2. **Trancher le modèle d'observateur** : demander/estimer la hauteur réelle du chemin de ronde de la tour d'Avalon (le LiDAR met ~3 m au point de l'esplanade) et refaire la visibilité avec cette valeur, plutôt que sol +1,7 m.
3. Ne pas rouvrir les châteaux privés (Le Clément, Augustins, Beauregard, Maximy, Fayet) : ils violent 06-020 et/ou 01-235.

---

### Fichiers
- Scripts : `outils_scratch/r0710_D_11_arrivee.py`, `r0710_D_inventaire.py`, `r0710_D_lib.py`, `r0710_D_chaine.py`, `r0710_D_chaine2.py`, `r0710_D_hasard2.py`, `r0710_D_carte.py`.
- Données : `donnees_travail/r0710_D/` → `arrivee.json`, `inventaire.json`, `chaine_departs.json`, `chaine_departs2.json`, `hasard2.json`, `ns_gen.json`.
- Cartes : `images_travail/r0710_D_corridor.jpg` (corridor + ellipse), `images_travail/r0710_D_zoom.jpg` (vue du rempart, DSM corrigé).
