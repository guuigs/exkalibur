# R1110_LID2 — Shortlist É12 avec filtres éliminatoires AVANT le score (11/10/2026)

**Verdict : RIEN de fiable — et le secteur NE (Saint-Maximin, az 45-95° de la tour) est entièrement éliminé.** Sur 103 blocs rocheux, 4 seulement ont une fin de chaîne qui passe a-e ; aucun n'est au NE. Les survivants sont en forêt de Pontcharra-sud (az ~180°) et dans une carrière au bord de l'Isère (az ~300°) ; tous échouent C5 (azimut du lever). Les p de hasard « par rang » sont faibles (≈ 0,00-0,09) mais c'est un artefact de structure (§5) : non fiable.

Scripts : `outils_scratch/r1110_lid2_00_zones.py`, `_01_filtres.py`, `_02_score_hasard.py`, `_03_top10.py`, `_04_sensibilites.py`. Données : `donnees_travail/r1110_LID2/` (`rock_variants.json` = 103 blocs × 9 fins avec chaque critère ; `resultats.json` ; `top10.json` ; `sensibilites.json` ; périmètres `z_*.json`, `ens_*.json` ; `pm_73.csv` = DGFiP 2024 Savoie). Ortho : `images_travail/r1110_LID2/topNN_c100.jpg` (100×100 m, croix rouge = coffre, cyan = roche, jaune = jonction), `topNN_ctx400.jpg`, `planche_top10_ctx400.jpg`.

## 1. Règles (fixées avant, appliquées au point du coffre ; script 01)
Chaîne = bloc lié +10 pas N +10 pas E +8 pas au cap {61 ; 63,7 ; 68}°, pas {0,75 ; 1,0 ; 1,48} m = 9 fins par bloc. Un bloc **survit** si ≥ 1 fin passe :
- (a) domaine public : parcelle de groupe DGFiP 1-4 (dép. 38 + 73 ajouté ; Saint-Maximin via pm_38426) ; point **non cadastré** = public seulement si pente ≤ 12°, MNH < 3 m et ≤ 3 m d'une ligne de chemin/route BD TOPO/OSM ; parcelle privée / personne morale non publique = rejet ;
- (b) bâti BD TOPO (polygones, raster 1 m) ≥ 80 m ;
- (c) pente pixel LiDAR 1 m ≤ 12° ;
- (d) hors ENS Isère (4 jeux opendata.isere.fr : départementaux + locaux, observation et intervention, dont Marais d'Avallon), Natura 2000 (API Carto : 0 site dans la mosaïque), RNN/RNC/parc national (0) ; ZNIEFF I/II et PNR Chartreuse = signalés, non éliminatoires ;
- (e) commune 38314 (Pontcharra) : coffre accepté seulement en forêt (≥ 60 % de MNH > 6 m sur 15 m).

Jonction candidate = ≥ 1 bloc lié (règle LID : ≤ 400 m, même composante hydro, C2) **survivant**. Score LID inchangé (C1-C6) avec C3 = C6 = 1 par construction. Plus de filtre bâti sur la jonction (il porte sur le coffre). Même filtre statique, même score pour les 1 000 tours fictives (`null.json['fake']`).

## 2. Entonnoir (924 fins = 103 blocs × 9)
| critère | fins OK | blocs avec ≥ 1 fin OK |
|---|---|---|
| a public | 158 | 20 |
| b bâti ≥ 80 m | 654 | 75 |
| c pente ≤ 12° | 205 | 39 |
| d hors ENS/Natura/RN | 918 | 103 |
| e Pontcharra en forêt | 803 | 91 |
| **a+b+c+d+e** | – | **4** (2 en mode canonique pas 1,48 / cap 63,7) |

Échecs « unique critère » : c 106 fins, a 78, b 11, e 3. Les 158 fins « non cadastrées » échouent toutes (chemin ≤ 3 m / pente / MNH). Seules 6 fins touchent un ENS (Forêts alluviales du Grésivaudan) ; aucun bloc du NE n'est dans un ENS : ce sont (a) et (c) qui tuent. (L'ENS Marais d'Avallon est chargé mais ne contient aucune fin.)

Chaînes survivantes dans les 2,5 km de la tour : **115 jonctions candidates, 149 couples (jonction, bloc), 395 triplets (jonction, bloc, fin)** (mode canonique : 75 jonctions, 249 triplets). Les 4 blocs :
- b27 (45.44200, 5.99962) et b29 (45.44168, 6.00106), commune 38027 (Barraux) : parcelles communales ZB0213 / ZB0177 ;
- b93 (45.40798, 6.02656) et b101 (45.40581, 6.02974), Pontcharra 38314 : parcelles communales D0086 / D0181.

**Secteur NE (blocs à az 40-100°, ≤ 3 km, n = 23) : 0 survivant**, y compris R208 (45.43679, 6.04640) et R125 de r1110_D : tous échouent (a) sur 9/9 fins (parcelles privées, ou non cadastré mais trop pentu/boisé/loin d'un chemin) et presque tous (c). Sensibilité de la règle « non cadastré » (réseau fusionné ≤ 3 m, ≤ 8 m, ou aucune exigence de chemin) : 5-6 blocs survivent, **toujours 0 au NE** (`sensibilites.json`).

## 3. Top 10 survivant (mode any-9, NMS 100 m ; score C1…C6, C5 = 0 partout)
| # | sc | jonction (lat, lon) · d tour / az | roche (aire) | souche | coffre (variante) | statut cadastral | pente pixel / moy 5×5 / max 7×7 | MNH | bâti | zones | ortho |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 5 | 45.441663, 6.005579 · 2 434 m / 304° | 45.441685, 6.001062 (49 m²) b29 | 45.441775, 6.001190 | 45.441809, 6.001279 (pas 1,0 cap 61 ; 3 fins/9) | « 4 - parcelle 38027000ZB0177 » (commune de Barraux) | 4,8° / 9,5° / 33,9° | 0 | 83 m | ENS/Natura : aucun | carrière à gradins + usine de traitement à ~100 m : **non conforme** |
| 2 | 5 | 45.440231, 6.003531 · 2 480 m / 299° | b29 (+b27) | idem | idem | idem | idem | | | | idem |
| 3 | 5 | 45.439248, 6.003887 · 2 402 m / 297° | b29 | idem | idem | idem | idem | | | | idem |
| 4 | 5 | 45.411113, 6.028415 · 1 973 m / 183° | 45.407982, 6.026555 (20 m²) b93 | 45.408115, 6.026744 | 45.408163, 6.026880 (1,48 / 63,7 = canonique) | « 4 - parcelle 383140000D0086 » (commune de Pontcharra) | 11,3° / 14,2° / 45,8° | 33,3 | 303 m | ZNIEFF II Contreforts occ. de Belledonne (non éliminatoire) ; PNR Chartreuse | forêt dense, pas de bâti |
| 5 | 5 | 45.408271, 6.022887 · 2 362 m / 193° | b93 | idem | idem | idem | idem | | | idem | idem |
| 6 | 5 | 45.407402, 6.024336 · 2 429 m / 190° | b93 | idem | idem | idem | idem | | | idem | idem |
| 7 | 4 | 45.440380, 6.005702 · 2 345 m / 301° | b29 | idem #1 | idem #1 | idem #1 | | | | | carrière |
| 8 | 4 | 45.442749, 6.005715 · 2 498 m / 306° | b29 | idem #1 | idem #1 | idem #1 | | | | | carrière |
| 9 | 4 | 45.408529, 6.030346 · 2 251 m / 179° | 45.405815, 6.029738 (43 m²) b101 | 45.405905, 6.029865 | 45.405940, 6.029955 (pas 1,0 cap 61 ; 1 fin/9) | « 4 - parcelle 383140000D0181 » (commune de Pontcharra) | 5,7° / 19,3° / 50,4° | 7,2 | 390 m | ZNIEFF II, PNR | forêt, chemin à ~13 m |
| 10 | 4 | 45.407735, 6.025698 · 2 373 m / 187° | b101 | idem | idem | idem | | | | | idem |

Seulement **3 points de coffre distincts** derrière ces 10 lignes (b29, b93, b101).
Contrôle visuel des finalistes (ortho IGN) : b27/b29 = gradins de carrière avec installations industrielles au NE (sol remanié, pas un chemin/clairière) → **à éliminer** ; b93/b101 = forêt dense sans bâti visible.
Réserves sur b93/b101 : pente pixel ≤ 12° mais **pente lissée 5×5 de 14-16° (b93) et 19° (b101)**, pente max 7×7 > 45° (versant raide de Belledonne) → avec une règle de pente lissée, **0 survivant**. Les jonctions sont à 185-390 m de la roche ; l'ortho de la jonction #4 ne montre pas de clairière.
Après retrait de b27/b29 : b93 + b101 seuls, 79 jonctions, top NMS 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, toutes à az 172-195°.

## 4. Score réel
Mode any-9 : 19 jonctions à score 5, aucune à 6 (6 exigeait C5, impossible ici). Après retrait carrière : scores 3 / 4 / 5 = 39 / 33 / 7. Aucun candidat ne passe C5 (az 45-95°), alors que le départ est « à l'est » (lever 63,7°).

## 5. Distribution nulle (1 000 tours fictives, mêmes filtres)
- **81,5 % des tours fictives n'ont aucune jonction survivante** (le filtre a-e élimine 99 blocs sur 103) ; 18,5 % en ont ≥ 1 (moyenne 12,3 jonctions, max 80) ; 14,7 % ont ≥ 10 candidats NMS.
- Meilleur score fictif : 0 → 815 tours ; 4 → 100 ; 5 → 85 ; 6 → 0. P(max ≥ 5) = **0,085** (vraie tour : 5). P(max ≥ 6) = 0 (la vraie n'a pas de 6).
- p par rang (réel 5,5,5,5,5,5,4,4,4,4) : 0,085 / 0,010 / 0,000 / 0,000 / 0,000 / 0,000 / 0,012 / 0,000 / 0,000 / 0,000. Sans carrière : 0,067 / 0,000 / 0,000 / 0,147 / 0,147 / 0,107 / 0,012 / 0,147 / 0,147 / 0,147.
- **Pourquoi ce n'est pas un signal** : (i) le rang 1 reste à 0,067-0,085 (> 2 %) ; (ii) les p ≈ 0 des rangs 2-10 viennent surtout de ce que la plupart des tours fictives n'ont aucun candidat : le « hasard » est dominé par la proximité de 4 blocs, pas par le score ; les rangs sont corrélés (3 points de coffre) et ~20 comparaisons ont été faites ; (iii) C5 échoue partout ; (iv) la règle de pente est fragile (lissée → 0 survivant) ; (v) le contrôle visuel « carrière » est appliqué aux finalistes seulement (sensibilité « sans carrière » faite avec le même hasard).

## 6. Limites
- Savoie : propriétaire DGFiP ajouté, mais ENS/Natura de Savoie non vérifiés (aucun jeu chargé) ; seules 73075/73141 touchent le NE lointain (0 survivant).
- Blocs = les 103 de LID (LRM ≥ 2 m, ≤ 15 m d'eau/talweg) ; un bloc hors de cette définition n'est pas testé. BD TOPO décalée sous couvert (5-12 m) → règle « ≤ 3 m d'un chemin » stricte ; sensibilité faite (§2).
- Bâti : BD TOPO + contrôle visuel des finalistes seulement. « Zone d'activités » de Pontcharra = proxy (forêt ≥ 60 % + bâti ≥ 80 m), pas de couche PLU. ZNIEFF = signal, pas interdiction.
- Groupe DGFiP 1-4 = propriétaire public ; une parcelle communale n'est pas forcément « domaine public » au sens strict, et un chemin rural/forêt privée ouverte n'est pas capté.

## 7. Conclusion
Sous l'ensemble des contraintes de l'auteur (domaine public réel, ≥ 80 m du bâti, pente ≤ 12°, hors ENS/Natura/réserve, hors ville), **aucune chaîne roche→coffre ne survit dans le secteur NE** (Saint-Maximin / tour d'Avalon) : ni pour les ex-rangs 1, 2, 4, 8, 9 de LID, ni ailleurs entre 40° et 100°. Les survivants sont dans la mauvaise direction et ne dépassent pas le hasard de façon fiable. Soit le coffre n'est pas lié à une « grande roche » de cette définition, soit « domaine public » / réseau / pente sont à relire.
