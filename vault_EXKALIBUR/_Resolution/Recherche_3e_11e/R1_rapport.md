# R1 : famille FRANCHISSEMENTS (ponts, passerelles, gués, planches)

> Agent R1, 03/10/2026. Hypothèse testée : « la troisième [passerelle] » et « le onzième [pont] » sont deux franchissements de cours d'eau, comptés le long d'un cours d'eau ou d'un itinéraire, et séparés de 1 850 m ±1 % en ligne droite.
> Scripts et données : `scratchpad/R1/` (`fetch.py`, `fetch_th.py`, `fetch_roads_ext.py`, `stems.py`, `crossings.py`, `cluster.py`, `rank.py`, `key.py`, `routes.py`, `itin.py`, `pdipr.py`, `walks.py`, `pano.py`).
> Annexe : `R1_inventaire_franchissements.csv` (864 franchissements, avec leur rang depuis la source et depuis l'embouchure).

## 1. Inventaire (données et méthode)

**Sources utilisées**
- **BD TOPO (WFS IGN)** sur 14 × 14 km centrés sur la tour : `troncon_de_route` (12 168 tronçons, avec `position_par_rapport_au_sol` : 1 = pont, « Gué ou radier », −1 = tunnel), `troncon_hydrographique`, `cours_d_eau`, `construction_lineaire` et `construction_surfacique` (227 « Pont », dont 5 « Passerelle »), `detail_hydrographique`.
- **Cours d'eau longs** : pour chaque cours d'eau, tous ses tronçons ont été récupérés (filtre CQL), y compris hors de la zone. Les routes ont été ajoutées le long de leur cours complet (65 tuiles de plus, 12 720 tronçons). Les rangs « depuis la source » sont donc complets, par exemple pour le Bréda depuis les Sept-Laux (32,4 km).
- **OSM (API /map)** sur 5,95-6,12 E × 45,37-45,49 N : 11 tuiles, 283 000 nœuds. Champs lus : `bridge=*`, `man_made=bridge`, `ford=*`, `tunnel=culvert`, `bridge:material`, `surface`, `bridge:structure`, ainsi que les relations de randonnée.

**Méthode**
- Pour chaque cours d'eau, j'ai construit le tracé principal à partir du graphe hydrographique (plus long chemin de la source à l'embouchure).
- Les franchissements sont les intersections géométriques de ce tracé avec toutes les voies, sentiers compris : BD TOPO d'une part, OSM d'autre part. J'y ai ajouté les gués OSM et les ponts `man_made=bridge`.
- Les franchissements trop proches le long du cours d'eau ont été regroupés. Le seuil a été testé à 10, 20 et 40 m pour mesurer sa sensibilité.
- Les ruisseaux sans nom ont été traités comme 87 chaînes indépendantes.

**Bilan dans un rayon de 6 km**
- 131 cours d'eau ou chaînes, dont 44 nommés et 87 sans nom.
- 864 franchissements, dont 647 à moins de 6 km de la tour.
- Parmi eux : 240 ponts, 46 passerelles piétonnes, 21 gués et environ 120 passages busés.

**Matériaux** : ils sont presque toujours inconnus. Un seul `surface=wood` à moins de 6 km (sentier sur le Bréda à Allevard, 5,5 km de la tour). Deux passerelles métalliques sur le Bréda à Pontcharra (45.43715, 6.01573 et Allevard). Aucun pas japonais (`ford=stepping_stones`) n'est cartographié. Panoramax est accessible : photos consultées pour les paires retenues. Mapillary demande un jeton.

## 2. Classement par cours d'eau et distance entre le 3e et le 11e

**Variantes testées**
- Sens : depuis la source et depuis l'embouchure.
- Huit filtres de comptage :
  - ALL : tout franchissement ;
  - WALK : sans le rail ni les tunnels routiers ;
  - PONTS, et PONTS+rail ;
  - PASSERELLES : pont sur un sentier ;
  - PIÉTON ;
  - NONMOTOR : sentiers et chemins ;
  - NONMOTOR_PONTS.
- Trois seuils de regroupement : 10, 20 et 40 m.

Une liste n'est testée que si elle compte au moins 11 éléments.

**Cours d'eau cités dans le brief (seuil 20 m)**
| Cours d'eau | Distance à la tour | Nombre de franchissements (ALL / PONTS / PASSERELLES) | Distance 3e↔11e (source / embouchure) |
|---|---|---|---|
| Bréda | 0,5 km | 44 / 38 / 18 | ALL 4 915 / 6 282 ; PONTS 10 552 / 6 235 ; PASSERELLES 5 973 / 7 440 ; aucune variante proche de 1 850 m |
| Rebouchet | 0,4 km | 19 / 10 / 0 | ALL 2 127 / 1 412 ; PONTS+rail 1 962 / 3 098 |
| Perrière | 1,1 km | 11 / 1 / 0 | ALL 2 267 / 2 189 (et pas de 12e ni de 13e) |
| Tapon | 1,5 km | 9 / 1 / 0 | moins de 11 éléments |
| Burge (passe par Bretonnières) | 2,0 km | 9 / 2 / 1 | moins de 11 éléments |
| Papet | 1,7 km | 17 / 7 / 1 | ALL 2 230 / 1 898 (+2,6 %) |
| Coisetan | 2,1 km | 33 / 22 / 4 | 2 867 à 8 978 |
| Salin | 6,8 km | 24 / 11 / 2 | 2 932 à 3 700 |
| Gelon | 7,6 km | 60 / 34 / 6 | 2 919 à 7 856 |

« Bretonnières » n'est pas un cours d'eau distinct dans la BD TOPO ni dans OSM : c'est la Burge, avec le Pont des Bretonnières sur le Bréda. L'Isère n'a pas été testée : ses rangs 3 et 11, comptés depuis la source ou depuis l'embouchure, sont à plus de 100 km.

**Toutes les paires trouvées dans la fenêtre (tous seuils et toutes variantes confondus)**
| # | Cours d'eau, variante, sens | d | 3e (lat, lon) | 11e (lat, lon) | Seuils où la paire apparaît |
|---|---|---|---|---|---|
| P1 | Rif Mort, ALL/WALK, depuis l'embouchure (16 éléments) | 1 858 m (+0,4 %) | 45.40816, 5.96675 (pont, sentier/chemin, à côté de la Rte des Ponts) | 45.42117, 5.95180 (traversée de chemin sans pont) | 10 et 20 m (disparaît à 40 m) |
| P2 | Cernon, PONTS, depuis la source (**11 éléments**) | 1 867 m (+0,9 %) | 45.45581, 5.98027 (pont de sentier) | 45.46624, 5.99901 (pont routier, asphalte) | 10, 20 et 40 m |
| P3 | Maladière (2276554820), ALL, depuis la source (15 éléments) | 1 878 m (+1,5 %) | 45.43120, 5.97950 (pont, Ch. du Séchident) | 45.41616, 5.99050 (pont, Ch. de l'Empereur) | 20 et 40 m |
| P4 | Croset, ALL, depuis la source (**12 éléments**) | 1 825 m (−1,4 %) | 45.46676, 6.07542 | 45.46058, 6.05379 (Route Victor Hugo) | 10 m |
| P5 | Dégoutés, NONMOTOR, depuis l'embouchure (**11 éléments**) | 1 830 m (−1,1 %) | 45.42093, 5.96061 | 45.42858, 5.93989 | 40 m |

Les ruisseaux sans nom ne donnent aucune paire dans la fenêtre.

## 3. Taux de hasard

**Méthode** : pour chaque liste testée, je compte la proportion de paires (k, k+8) dont la distance tombe dans la fenêtre. La somme de ces proportions donne le nombre de succès attendu par hasard pour la paire (3, 11).

| Seuil de regroupement | Tests (listes × 2 sens) | Succès à ±1 % | Attendus à ±1 % | Succès à ±2 % | Attendus à ±2 % |
|---|---|---|---|---|---|
| 10 m | 186 | 4 | 4,27 | 6 | 7,22 |
| 20 m | 164 | 4 | 4,75 | 6 | 6,88 |
| 40 m | 146 | 2 | 3,48 | 5 | 6,38 |

**Le nombre observé est égal ou inférieur au hasard. Aucun signal.**

**Itinéraires**
- **Boucles balisées** autour de la tour :
  - « À la découverte des Hameaux » (BD) et « Randonnée des Hameaux » (OSM), qui passent au carrefour Le Vivier : 9 franchissements seulement (Tapon ×4, Rebouchet ×2, ruisseaux sans nom), dont un seul pont. Il n'y a donc **pas de 11e**.
  - Chemin de Szombathely (Moûtiers → Pontcharra, à 0,5 km du rempart) : 6 franchissements.
  - GR 965 : à 4 km de la tour.
  - « Tour de Chantemerle » (BD) : un autre Chantemerle, à 6,4 km.
- **Réseau PDIPR depuis Le Vivier, la Rue du Rempart ou la tour** (énumération exhaustive des chemins) : 2 paires possibles, à 1 211 et 1 246 m. Aucune n'est dans la fenêtre.
- **300 000 marches aléatoires** sur tout le réseau routier et piéton :
  - environ 3,3 % des paires (3e, 11e) distinctes tombent à ±1 % (5 % à ±2 %) ;
  - une marche qui ne compte que les ponts n'atteint jamais 11.

Conclusion : « la 3e et la 11e passerelle d'un itinéraire » n'est pas contrainte. N'importe quel itinéraire choisi a environ 3 % de chances de donner une paire à 1 850 m. Ce n'est donc pas testable sans un itinéraire désigné par l'énigme.

## 4. Grille d'élimination

✓ = compatible, ✗ = violé, ? = non tranché.

| Hypothèse | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Famille : franchissements comptés le long d'un cours d'eau | ✓ | ✓ | ? (pas de signal au-dessus du hasard) | ? (matériaux inconnus) | ? (on marche sur les deux, pas « surtout sur l'un ») | dépend du cours d'eau | ✓ | ✓ | ? (les ponts sont faciles à trouver) | ? (ponts sur les enl. 8, 9 et 12 ; celui de l'enl. 12 est imaginaire, FAQ03-034) | ✗ pour toutes les paires trouvées | ✓ | **FAIBLE** |
| Bréda (toutes variantes) | ✓ | ✓ | ✗ (aucune paire entre 4,9 et 13,5 km) | ? | ? | ✓ | ✓ | ✓ | ? | ? | — | ✓ | **ÉCARTÉE (C3, fait vérifié sur 8 variantes × 2 sens × 3 seuils)** |
| Tapon, Burge, Perrière, Chanelle, Beau-Magny (ponts ou passerelles) | — | — | — | — | — | ✗ (moins de 11, a fortiori moins de 13) | — | — | — | — | — | — | **ÉCARTÉE (C6, sous réserve que la cartographie soit complète)** |
| P1 Rif Mort | ? (pont contre traversée sans pont) | ✓ | ✓ (+0,4 %, mais disparaît au seuil de 40 m) | ? (3e = pont maçonné à garde-corps métal sur Panoramax ; 11e = pas de pont, sans photo) | ? | ✓ (16) | ✓ | ✓ | ? | ? | ✗ (5,5 à 6,3 km de la tour, rive ouest de l'Isère, pied de la Chartreuse) | ✓ | **FAIBLE** (dans le bruit) |
| P2 Cernon | ✓ | ✓ | ✓ | ? | ? | ✗ (11 ponts seulement, pas de 13e) | ✓ | ✓ | ? | ? | ✗ (4,8 à 5 km, rive ouest) | ✓ | **ÉCARTÉE (C6)** |
| P3 Maladière | ✓ | ✓ | ✗ (+1,5 %) | ✗ (11e = pont en béton à rambarde métallique, Panoramax 2025) | ? | ✓ | ✓ | ✓ | ? | ? | ✗ | ✓ | **ÉCARTÉE (C3, C4)** |
| P4 Croset | ✓ | ✓ | ✗ (−1,4 %) | ? | ? | ✗ (12) | ✓ | ✓ | ? | ? | ✗ | ✓ | **ÉCARTÉE (C3, C6)** |
| P5 Dégoutés | ✓ | ✓ | ✗ (−1,1 %) | ? | ? | ✗ (11) | ✓ | ✓ | ? | ? | ✗ | ✓ | **ÉCARTÉE (C3, C6)** |
| Variante « 3e et 11e passerelle d'un itinéraire balisé depuis le rempart ou Le Vivier » | ✓ | ✓ | ✗ pour les boucles balisées (moins de 11) ; non testable pour un itinéraire libre (hasard ≈ 3 %) | ? | ? | ✗ pour les boucles balisées | ✓ | ✓ | ? | ? | ? | ✓ | **FAIBLE** |

**Ce que la paire P1 donnerait pour la clairière** : son cap du 3e vers le 11e est de 321°.
- Depuis la Rue du Rempart, 1 850 m à 321° mènent en 45.44271, 6.01630. C'est Pontcharra, en zone urbaine près de la confluence Bréda-Isère : visible depuis la tour, mais bâti.
- Dans le sens inverse (141°), on arrive en 45.41683, 6.04605. C'est le versant de Bramefarine, non visible depuis le sommet de la tour.
- Aucune de ces deux arrivées ne ressemble à la clairière décrite.

## 5. Limites
- Les **planches et petites passerelles non cartographiées** ne peuvent pas être exclues par les données. Le fait que les 3e et 11e ne soient « pas visibles sur Maps » est une paraphrase de joueur (FAQ05-074), pas une réponse de l'auteur. L'auteur dit seulement qu'on peut les trouver de chez soi (FAQ04-114).
- Les rangs sont sensibles au seuil de regroupement (passerelle accolée à un pont) et aux buses non cartographiées. C'est pourquoi aucune paire n'est déclarée « vivante » si elle dépend d'un seul seuil.
- Les matériaux (C4) restent inconnus pour plus de 95 % des ponts.

## Résumé (≤ 300 mots)
J'ai inventorié tous les franchissements de cours d'eau à environ 6 km autour de la tour d'Avalon, en croisant BD TOPO et OSM :
- 131 cours d'eau, dont 87 chaînes sans nom ;
- 864 franchissements : 240 ponts, 46 passerelles, 21 gués, environ 120 buses ;
- les rangs sont complets depuis la source, y compris pour le Bréda (32 km).

Pour chaque cours d'eau, j'ai calculé la distance entre le 3e et le 11e franchissement, depuis la source et depuis l'embouchure, avec 8 façons de compter et 3 seuils de regroupement.
- **Résultat : 4 paires à ±1 % pour 4,3 à 4,8 attendues par hasard. Aucun signal.**
- **Bréda** : rien entre 4,9 et 13,5 km, quelle que soit la variante. Écarté.
- **Tapon, Burge, Perrière** : moins de 11 ponts. Écartés par C6 (il faut au moins 13 éléments).
- **Paires dans la fenêtre**, toutes à 4-6 km sur la rive ouest de l'Isère :
  - Cernon : seulement 11 ponts, écarté par C6 ;
  - Maladière (+1,5 %) : 11e en béton sur Panoramax, écarté par C3 et C4 ;
  - Croset et Dégoutés : écartés par C3 et C6 ;
  - Rif Mort (1 858 m) : seule paire non écartée, mais de nature mixte (un pont et une traversée sans pont), fragile et dans le bruit. FAIBLE.
- **Itinéraires** :
  - les boucles balisées passant par Le Vivier (« Hameaux ») n'ont que 9 franchissements ;
  - le réseau PDIPR ne donne aucune paire ;
  - un itinéraire libre tombe dans la fenêtre environ 3 % du temps, donc il n'est pas contraint.

**Verdict famille : FAIBLE.** Les franchissements cartographiés ne produisent aucune paire 3e/11e au-dessus du hasard. Seules restent possibles des planches ou passerelles non cartographiées, qu'on ne peut pas tester de chez soi avec ces données.
