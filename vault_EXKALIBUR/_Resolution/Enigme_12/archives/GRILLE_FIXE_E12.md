# É12 — Grille fixe d'évaluation (04/10, rédigée par Claude, validée à compléter par Guilhem)
But : noter tout lieu candidat avec les MÊMES critères et les MÊMES seuils, définis AVANT de regarder les résultats. Tout changement de seuil doit être consigné ici avec sa date et sa raison.
Règle du hasard (Guilhem) : **p ≤ 2 % idéal, 5 % maximum** pour la coïncidence qui désigne le lieu.

## Critères DURS (un seul ❌ = rejet)
| # | Critère | Source | Seuil | Données |
|---|---|---|---|---|
| H1 | Départ = muraille de la tour d'Avalon (publique toute l'année) | 06-020, 06-193, FAQ8 | muraille LiDAR (17 points) | t61 |
| H2 | Proximité | 06-244 « pas loin » ; 06-025 « très proches » ; **06-163 « le dernier kilomètre »** ; **06-083 zone = « une poignée de km »** | croisement ≤ **2,0 km** de la tour (préférence ≤ 1,5 km) | BD TOPO |
| H3 | Domaine public pour le COFFRE | 01-235, 02-097, 03-098 | public **sûr** : parcelle d'une collectivité/État, forêt publique, voirie non cadastrée (le lit de ruisseau non cadastré est « douteux » = refusé) | cadastre Etalab + fichier des personnes morales, 8 communes |
| H4 | Bâtiments | 05-107 ; règle de Guilhem | ≥ 100 m du **croisement** et du **coffre** | BD TOPO bâti |
| H5 | Visible depuis le rempart | 05-155, 05-165 | ≥ 100 m² de sol ouvert (< 1,5 m de végétation) dans 60 m du croisement, vu depuis la muraille, œil à 1,7 m au-dessus du **sol** | LiDAR 1 m |
| H6 | Eaux à suivre | 06-195, 03-082, 03-152 | cours d'eau BD TOPO ≤ 100 m **ou** talweg LiDAR ≥ 2 ha ; l'eau coule jusqu'à la roche | BD TOPO, LiDAR |
| H7 | Vrai croisement | 06-005 | ≥ 3 voies | OSM + BD TOPO |
| H8 | Roche puis coffre « tout près » | 05-051, 06-195, FAQ8 (« quitter votre route »), 06-090 | roche sur l'eau à ≤ 300 m de la jonction, **chemin à ≤ 30 m de l'eau** sur le parcours ; coffre ≤ 300 m de la jonction ; coffre ≤ 30 m d'un chemin | LiDAR, BD TOPO |
| H9 | **Logique 3e/11e** : une lecture des 3e et 11e qui MÈNE au lieu (07-133, 05-068) ET un hasard ≤ 5 % | 06-009, 06-216, 07-068, 06-133, FAQ8 | p-value par simulation placebo (centres et orientations au hasard) | t90 |
## Critères SOUPLES (notés, non éliminatoires)
S1 forêt ≥ 20 % autour (60-200 m) ; S2 ouverture ≥ 30 % dans 30 m (07-240 : « il s'agit d'identifier une jonction de chemin ») ; S3 pente du chemin ≤ 15° (fauteuil au sens large, 03-112) ; S4 eau permanente (BD TOPO) ; S5 maisons ≥ 150 m ; S6 première phrase / « chant » / enluminures 9 et 11 cohérents.
## Évaluation des candidats (04/10)
| Candidat | H2 | H3 | H4 | H5 | H6 | H7 | H8 | H9 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Le Mouret** (45.422426, 6.040299) | ✅ 1,02 km | ✅ seulement avec roche à ≤ 40 m de la jonction ; ❌ avec roche-source | ✅ 190 m / 175 m | ✅ 441 m² (le pré) | ✅ talweg 3,7 ha | ✅ 4 voies | ✅ roche ~40 m, sentier à 15-18 m | ✅/⚠️ p entre 0,1 et 2,5 % (voir §30) | **seul candidat sans ❌ dur, S2 ❌ (ouverture 3 %)** |
| A (45.419519, 6.020142, Pontcharra S) | ✅ 1,34 km | ✅ | ✅ 181 m | ✅ 338 m² | ✅ eau 98 m | ✅ | ✅ | ❌ aucune logique (cap 219°, hors de portée de la table) | rejeté (H9) |
| C (45.443603, 6.014493, Pontcharra N) | ❌ 2,08 km | ✅ | ✅ | ✅ | ✅ | ✅ | — | ❌ aucune logique (cap 322°) | rejeté |
| Le Crêt (45.430543, 6.053090) | ✅ 1,74 km | ✅ | ❌ 47 m | ✅ | ✅ | ✅ | — | ❌ (84° = ~17 avril, rien) | rejeté |
| Le Couvet (45.434748, 6.059095) | ❌ 2,29 km | ✅ | ❌ 45 m | ⚠️ 1 point de muraille | ✅ | ✅ 3 voies | ⚠️ pente 50 % | ⚠️ p ≈ 6 % (voir §30) | rejeté |
| Le Papet (45.412208, 6.023298) | ✅ 1,95 km | ✅ | ❌ 49 m | ✅ | ✅ | ✅ | — | ❌ | rejeté |
| J5 / Tire-Loup (45.426948, 6.054780) | ✅ 1,86 km | ✅ | ✅ | ❌ 0 m² | ✅ | ✅ 5 voies | — | ❌ (Machrie éliminé, FAQ06-133) | rejeté |
