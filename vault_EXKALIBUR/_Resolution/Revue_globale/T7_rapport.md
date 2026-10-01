# T7 : inventaire terrain IGN — ruisseaux, intersections de sentiers, roches (30/09/2026)

Sortie machine : `T7_terrain.json` (schéma imposé). Scripts : `T7_terrain.py`. Sources : BD TOPO v3 (GeoJSON en cache `scratch/ign/`), cadastre Etalab (reprise T4 `t4_cadastre_roches.json`). Rayon 5 km autour de la tour + corridor château Bayard → tour d'Avalon. **Aucune correspondance 1,85 km cherchée** (consigne).

## ⚠️ Correction de coordonnées (FAIT)
La tâche indique « tour d'Avalon (45.4931, 6.1497) » : **erroné** (~11 km au NE, hors Saint-Maximin). Toutes les données IGN (téléchargées autour de 45.4262, 6.0248) et tous les rapports T1–T4 utilisent **45.4288, 6.0308**. Positions exactes retenues (toponymes BD TOPO) :
- **Tour d'Avalon** = 45.4288723, 6.03101275 (« tour d'avallon », Saint-Maximin).
- **Château Bayard** = 45.42337066, 6.0189374 (« château bayard », Pontcharra) — à 1,09 km / cap 238° de la tour.

## A. Ruisseaux (FAIT, BD TOPO)
- **24 cours d'eau nommés** dans 5 km + **193 tronçons « écoulement naturel » sans nom** (0 à moins de 300 m du corridor).
- Les plus proches de la tour : **Ruisseau de Rebouchet** (0,42 km, coule ONO ; à 0,18 km de Bayard), **le Bréda** (0,49 km, coule NNO), **Ruisseau de la Perrière** (1,11 km, coule ONO), **Ruisseau de Tapon** (1,45 km).
- 4 tronçons sans nom ≤ 1 km de la tour (0,54 / 0,54 / 0,78 / 0,91 km), aucun le long du corridor.

## B. Intersections de sentiers (FAIT, liste T1 filtrée)
- 217 jonctions T1 (≥3 branches) → **22 croisements réels** (≥4 branches sentier/chemin/route empierrée). Les 195 à 3 branches = fourches/T, écartées.
- **Aucun** des 22 n'est en clairière (trouée) ; aucun ne cumule clairière+eau. Le plus proche de la tour : **45.43124, 6.02224** (4 sentiers, 720 m de la tour, 910 m de Bayard). 11 des 22 ont un ruisseau sans nom à ≤150 m.

## C. Roches / blocs (FAIT, BD TOPO + cadastre)
- **Aucun « Rochers » ni « Bloc rocheux isolé » cartographié dans 5 km** (plus proche : Rocher de Saint-Georges à 5,41 km ; les 5 blocs isolés IGN sont à >9,3 km). Cohérent avec FAQ07-126 (« grande roche non visible sur Maps »).
- Toponymes réels ≤ 5 km (5) : **LE CHENE LA ROCHE ET LE VIVIER** (0,13 km), **PIERRE GROS** (0,44 km), **LE ROCHAT** (1,42 km), **COTE ROCHAT** (2,21 km), **ROCHE MORTE** (3,07 km).
- Faux positifs écartés : PRE CROCHET (« crochet » ≠ roche), lycée Pierre de Terrail (bâtiment, nom de Bayard), Saint-Roch (saint).

## D. « Clairement identifiable »
- Ruisseaux nommés : **oui** (statut « Validé », nom officiel). Tronçons sans nom : non.
- Croisements : **oui** par position exacte (nœud BD TOPO ≥4 branches), mais aucun ne se distingue (pas de clairière).
- Roches : les 2 proches (LE CHENE LA ROCHE ET LE VIVIER, PIERRE GROS) sont identifiables par leur **nom cadastral**, mais aucune roche physique n'est cartographiée.

## Bilan
Rien de neuf décisif : le ruisseau nommé le plus proche est le **Rebouchet** (ou le Bréda), le croisement le plus proche est à **720 m** (4 sentiers, hors clairière), et la seule « grande roche » plausible reste un **toponyme** (PIERRE GROS à 0,44 km, ou la roche du lieu-dit « Le Chêne, la Roche et le Vivier » à 0,13 km), aucune roche physique n'étant cartographiée — ce qui cadre avec « non visible sur Maps ».
