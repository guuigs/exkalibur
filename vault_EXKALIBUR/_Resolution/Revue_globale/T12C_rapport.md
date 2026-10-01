# T12C — Piste photométrique/géométrique « terrain simulé » (sans présupposer 3e/11e)

**Statut : plafond « bureau » atteint.** Aucun croisement ne satisfait la chaîne complète de
contraintes depuis aucun départ candidat. Le test photométrique donne un signal directionnel
cohérent (NE, vallon du Ruisseau de Tapon) mais aucune jonction n'y survit aux filtres terrain.

## 1. Astronomie (T12C_00) — lever du soleil
Position réf. tour d'Avalon (45.429083, 6.030808). Azimut compté depuis le nord.

| Date | Déclinaison | Azimut lever | Azimut à 5° | Azimut à 10° |
|---|---|---|---|---|
| 30/04/1524 **julien** (mort Bayard) | +17.46° | **63.75°** | 70.10° | 75.22° |
| 30/04/1524 grégorien | +14.58° | **68.07°** | 74.26° | 79.33° |
| équinoxe | ~0° | 89.7° | — | — |
| solstice été | +23.5° | 54.3° | — | — |
| solstice hiver | −23.5° | 123.6° | — | — |

- **FAIT** : le « jour dernier » lève le soleil au **NE, azimut ≈ 64° (julien) / 68° (grégorien)**,
  et 70–79° dès qu'il monte un peu. Cône matinal utile ≈ **54°–80°**.
- **Sensibilité date** : 5° d'écart julien/grégorien ; ~10° entre le lever et 5° de hauteur.
- Confirme les valeurs déjà posées (63,7°/68,0°).

## 2. Viewsheds LiDAR + photométrie (T12C_01)
Méthode : viewshed « horizon par secteurs angulaires » sur MNT 2 m (2000×2000), puis test
« miroitement » (regard vers le soleil, cône ±25°) et « éclairé de face » (écoulement vers le soleil).

| Départ | œil | terrain visible | pts cours d'eau visibles |
|---|---|---|---|
| D1 sommet tour | +27 m (z≈426,6) | 54,5 % | 673 / 2843 |
| D2 pied tour | +2 m (z≈401,6) | 42,7 % | 504 / 2843 |
| D3 château Bayard | +2 m (z≈310,0) | 22,1 % | 221 / 2843 |

- **FAIT** : les cours d'eau **nommés** visibles dans le cône solaire NE sont quasi uniquement le
  **Ruisseau de Tapon** (8 pts, cap ~59°, 1,45 km) ; le reste est « (sans nom) » (rills intermittents).
  Le **Rebouchet** (ouest) et le **Bréda** (NNO) ne sont **pas** dans le cône du lever.
- **HYPOTHÈSE** : si « l'astre glorieux magnifiait le ruisseau » est à prendre photométriquement,
  le ruisseau n'est ni le Rebouchet ni le Bréda, mais le **vallon du Tapon** (NE) ou un rill sans nom.
- **Sensibilité hauteur d'œil** : 0→40 m fait passer « miroitement az64 » de 17 à 65 points (progressif,
  sans seuil) ; la conclusion qualitative (Tapon dominant) ne change pas.

## 3. Croisements + filtres + témoins (T12C_02)
Croisements = nœuds OSM « Réseau pédestre du Grésivaudan » + nœuds BD TOPO degré ≥3 (Chemin+Sentier)
= **856 uniques** (528 BD TOPO + OSM).

**Sélectivité de chaque filtre (sur 856) :**
| Filtre | passage | lecture |
|---|---|---|
| F1 d_eau ≤150 m | 293 (34,2 %) | ⚠️ NON INFORMATIF (25–50 %) |
| F2 d_bâtiment ≥150 m | 601 (70,2 %) | faible |
| F3 clairière (hors Bois/Forêt) | 419 (48,9 %) | ⚠️ NON INFORMATIF (25–50 %) |
| F4 forêt publique | 64 (7,5 %) | sélectif |
| F5 d_monument ≥150 m | 839 (98 %) | trivial |
| F6 vis D1 / F7 D2 / F8 D3 | 83 / 48 / 30 | sélectif |
| F9–F11 soleil64 D1/D2/D3 | 9 / 7 / 0 | très sélectif |

**Chaîne complète (eau & bâtiment & clairière & monument & visible & soleil) = 0 croisement**
pour D1, D2, D3 (az 64° et 75°). Témoins aléatoires (15 départs à 0,83 km de la tour) : **0 partout**.

**FAIT** : les filtres « eau » et « clairière » sont individuellement non discriminants (taux 25–50 %) ;
seul le couple « visibilité + cône solaire » réduit fortement, mais la chaîne entière ne laisse **rien**.
**FAIT** : tout croisement à ≤150 m d'un cours d'eau dans 2 km de la tour est à <150 m d'un bâtiment
(les vallons sont habités : Ripellets, Crêt, Couvat, La Combe, Chaffardon…). Aucune « clairière à la
jonction, loin de tout bâtiment, près du ruisseau » n'existe dans les données.

**Near-miss dans le cône solaire NE (cap 65–83°), tous échouent sur la distance au bâti :**
- Les Ripellets (45.43379, 6.05023) d_eau 7 m, clairière, visible, soleil ✅ — mais d_bât **8 m**.
- BDTOPO deg3 (45.43359, 6.04490) d_eau 34 m, clairière, visible, soleil ✅ — d_bât **142 m** (limite 150).
- Le Crêt (45.43105, 6.05343) d_eau 45 m, clairière, soleil ✅ — d_bât **18 m**.
- Le Couvat (45.43290, 6.05407) d_eau 131 m, soleil ✅ — d_bât 78 m, hors clairière.

## 4. Grande roche (T12C_03)
- Toponymes « roche/rocher/pierre » ≤4 km : **aucun** pertinent (seul « roche morte » 3,1 km, déjà écarté ;
  « lycée Pierre de Terrail » 1,4 km = bâtiment).
- Points orographiques « Rochers/Escarpement » ≤4 km : **aucun** (seul « les Gorges » 3,1 km).
- Lieux-dits non habités « roche/pierre » ≤4 km : **aucun**.
→ la « grande roche qui bloque le chemin » n'est pas localisable en BD TOPO près de la zone
(cohérent avec T4 : rien à <6 km). MNS−MNT (LiDAR HD) non disponible localement.

## 5. Départs D4 / D5
- **D4 Fort Barraux** (45.4356, 5.9871) : **hors MNT local** (lon < 6.00518) ; Overpass indisponible
  (403/406/timeout sur les 3 miroirs). Non analysable en viewshed sans une tuile MNT plus à l'ouest.
- **D5** (BD TOPO, 12 km) : « Tour, donjon » à 27 m = la tour d'Avalon elle-même ; châteaux à 743 m (N),
  1,42 km (N), **1,75 km NE (45.44129, 6.04503)**, et le couple Tour/château de Bayard (~1,1 km SO).
  Aucun autre « rempart/chemin de ronde » cartographié près de la tour (cohérent avec l'acquis).

## 6. Conclusion
- Le **test photométrique est cohérent** (le seul cours d'eau nommé aligné sur le lever du soleil est
  le Tapon, au NE), mais **aucun croisement ne passe la chaîne complète** ; la chaîne est vide pour les
  départs candidats **et** pour les témoins aléatoires.
- **Ce qui manque** (plafond bureau) : (i) l'identité/position des **3e et 11e** (hors mandat T12C) pour
  fixer le départ ; (ii) une tuile **MNT à l'ouest** pour tester Fort Barraux (vrais remparts) ; (iii) un
  **levé terrain** du vallon du Tapon (le seul aligné sur le soleil), où la « clairière » et la « grande
  roche » ne se voient pas dans BD TOPO (ruisseau plus fin que la carte — acquis antérieur).
- **Livraison courte : aucune boîte de 50 m à proposer** ; je ne recommande pas de zone sans un
  départ différent ou un terrain.
