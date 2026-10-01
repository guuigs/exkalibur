# Exkalibur — Énigme 12 — Test systématique des séries d'objets au sol
**Zone : tour d'Avalon (45.4288, 6.0308), Saint-Maximin, Isère. Rayon d'étude : 4 km.**

## But
Trouver la série d'objets au sol (≥13 éléments de même nature) dont le n°3 et le n°11 sont distants de 1850 m ±1 % (fenêtre 1831,5–1868,5 m) en ligne droite.

## Méthode
1. Recensement exhaustif via WFS IGN `BDTOPO_V3` (CRS84) des 10 familles demandées, dans une emprise >4 km (5,96–6,10 E ; 45,39–45,47 N), puis filtrage à 4 km du centre.
2. Calcul de **toutes** les paires d'éléments à 1850 m ±1 % (distance haversine).
3. Croisement de chaque paire candidate avec : proximité cours d'eau (troncon_hydrographique), proximité bois/forêt (zone_de_vegetation : Bois, Forêt fermée…), matière bois/pierre plausible, et cohérence d'un parcours partant des remparts de la tour.
4. Test de bruit : comparaison du nombre de paires observé au nombre attendu sous hypothèse nulle (répartition spatiale uniforme, anneau 1850 m × 37 m de large dans le disque de 4 km).

## Résultat du recensement (4 km)

| Famille | Source BDTOPO_V3 | n | paires 1850 m |
|---|---|---|---|
| Ponts | construction_lineaire nature=Pont | **66** | **18** |
| Passerelles | Pont detail=Passerelle | 2 | 0 |
| Croix | construction_ponctuelle nature=Croix | 8 | 0 |
| Bornes | construction_ponctuelle nature=Borne | 0 | 0 |
| Gués | (aucun type — vérifié lineaire/hydro) | 0 | 0 |
| Sources/Fontaines/Lavoirs | detail_hydrographique | **36** | **3** |
| Arbres remarquables | (absent) | 0 | 0 |
| Pierres plantées | (absent) | 0 | 0 |
| Sections empierrées | troncon_de_route nature=Route empierrée | **361** | **469** |
| Seuils/Barrages | construction_lineaire nature=Barrage (Seuil/Vanne/—) | 1 | 0 |

**Familles ≥13 éléments : ponts (66), sources/fontaines/lavoirs (36), sections empierrées (361).**

## Analyse de bruit (décisive)

| Famille | n | paires attendues (bruit) | paires observées | ratio | signal |
|---|---|---|---|---|---|
| Ponts | 66 | 18,4 | 18 | 0,98 | **aucun** |
| Sources/Fontaines/Lavoirs | 36 | 5,4 | 3 | 0,56 | aucun (sous le bruit) |
| Sections empierrées | 361 | 556 | 469 | 0,84 | aucun (sous le bruit) |

**Aucune famille ne montre de signal NET :** partout le nombre de paires à 1850 m est égal ou inférieur à ce que produirait le hasard. Le « 18 paires sur 66 ponts » est exactement le niveau de bruit attendu (18,4).

## Croisement par contraintes physiques

Contraintes de l'énigme :
- n°3 : **pas d'écharde** → matière non-bois (pierre/métal).
- n°11 : **écharde possible** → matière bois plausible.
- « on marche surtout sur l'une des deux » → l'objet est une surface sur laquelle on marche.
- n°3 et n°11 = lieux précis **non visibles sur Google Maps**.
- parcours : départ remparts de la tour, étapes intermédiaires entre la 3e et la 11e.

| Famille | matière bois/pierre | « on marche dessus » | conclusion |
|---|---|---|---|
| **Ponts** | **oui** (pont de pierre vs pont/passerelle en bois) | **oui** (on marche sur un pont) | **seule famille compatible** |
| Sections empierrées | non (empierrée = pierre, jamais bois) | oui | écartée (n°11 bois impossible) |
| Sources/Fontaines/Lavoirs | non (pierre/eau) | non | écartée |
| Croix | bois possible, mais n=8<13 | non | écartée (<13) |
| Passerelles | bois possible, mais n=2 | oui | écartée (n=2) |
| Seuils/Barrages | — | — | écartée (n=1) |
| Bornes / Gués / Arbres rem. / Pierres plantées | — | — | écartées (n=0) |

## Détail des 18 paires « ponts » à 1850 m (croisement eau/bois/distance tour)

Les ponts sont **tous** proches d'un cours d'eau par définition (un pont franchit l'eau), donc le critère « un point près de l'eau » est trivial et non discriminant. Le critère discriminant est la proximité d'un bois et la cohérence du parcours.

Paires où l'un des deux ponts est **près de la tour (<1 km, étape intermédiaire plausible)** et l'autre plus loin (destination) :
- **(2,44)** 1849 m — A (45.43566,6.03903, 997 m de la tour, à 0 m du barrage) / B (45.42370,6.02257, 857 m). Les deux <1 km → plutôt un aller-retour local qu'un parcours.
- **(6,41)** 1865 m — A (45.44762,6.02666, 2117 m) / B (45.43113,6.02222, **718 m**).
- **(18,65)** 1833 m — A (45.42227,6.00870, 1871 m) / B (45.43255,6.02706, **509 m**).
- **(41,51)** 1847 m — A (45.43113,6.02222, **718 m**) / B (45.41452,6.02200, 1730 m).

Points récurrents proches de la tour : 45.43113,6.02222 (718 m) et 45.43255,6.02706 (509 m).

Paires avec un pont en lisière de bois (bo=0 m) : (2,44), (8,38), (41,51), (42,47).

**Aucune paire ne ressort comme « signal net »** : les 18 paires sont indistinguables du bruit, et le critère « eau » est trivial pour des ponts. Le n°3/n°11 **ordonné** (le long d'un cours d'eau, en remontant depuis la tour) ne peut pas être tranché par la seule donnée BDTOPO, qui ne contient aucun champ d'ordre.

## Verdicts

- **Ponts → FAVORI** (par élimination) : seule famille ≥13 éléments qui satisfait *toutes* les contraintes physiques (matière bois/pierre, « on marche dessus », proximité eau). Mais la donnée ne confirme **aucune** paire précise : les 18 paires sont au niveau du bruit.
- Sources/Fontaines/Lavoirs → **écartée** (36 éléments mais matière tout-pierre/eau : pas de bois, on n'y marche pas ; 3 paires = sous le bruit).
- Sections empierrées → **écartée** (469 paires = bruit pur ; empierrée = pierre, incompatible avec « écharde/bois » sur n°11).
- Croix → **écartée** (8 < 13).
- Passerelles → **écartée** (2 < 13).
- Seuils/Barrages → **écartée** (1 seul).
- Bornes, Gués, Arbres remarquables, Pierres plantées → **écartées** (0 élément dans la zone).

## Conclusion
Le balayage systématique est complet. **Aucune famille ne présente de signal statistique net** : toutes les paires à 1850 m sont au niveau du hasard. **Les ponts sont la seule famille cohérente avec l'ensemble des contraintes** (≥13, matière mixte pierre/bois, surface où l'on marche, proche de l'eau) et constituent le favori **par élimination**. Pour trancher la paire n°3–n°11 exacte, il manque l'information d'**ordre** (le long de quel cours d'eau / dans quel sens depuis la tour) que la BDTOPO ne fournit pas — les ponts nommés (Pont des Lots, des Bretonnières, du Furet, de la Gache, Mathieu, des Mollettes) sont répartis sur des ruisseaux différents, sans série linéaire évidente.
