# R4 — Objets numérotés ou ordonnés sur le terrain (≤ 8 km de la tour d'Avalon)

> Agent R4, 03/10/2026. Famille : bornes, parcelles, poteaux, balises, pylônes, lacets, parcours, etc.
> Départ : tour d'Avalon (45.4288723, 6.03101275). Cible C3 : 3e ↔ 11e = 1 850 m ±1 % (1 831-1 869 m), en ligne droite.
> Scripts et données : `/tmp/claude-0/-home-user-exkalibur/459ce361-0706-50f5-a5c3-fb8740ef9d66/scratchpad/R4/` (`osm8.json` = 15 tuiles API OSM /map couvrant 5,92-6,17 E × 45,35-45,50 N ; `w_point_de_repere.json` = PR BD TOPO ; `parcels_1_20.json` = parcelles cadastrales n° 1-20 de 31 communes ; `onfparc.gml` = parcellaire ONF ; `w_feuille.json` = feuilles cadastrales ; scripts `numbered.py`, `pyl2.py`, `hairpins2.py`, `onf2.py`, `routes.py`).

## 1. Ce qui a été inventorié (faits)

| Famille | Source | Numérotation sur le terrain | Effectif ≤ 8 km | 3e ↔ 11e (meilleure paire) | Témoin (i, i+8) à ±1 % |
|---|---|---|---|---|---|
| **Bornes sardes 1822** (frontière Savoie / France de 1760, rétablie en 1815-1822) | OSM + plaquette AHCS « Les bornes sardes en Cœur de Savoie » + PNR Chartreuse | gravées 1 → 67+ (n° 37 au col du Fraîne, 39-44 à Chapareillan, 49-60 dans la plaine Laissaud / Pontcharra, 66-67 vers le col de la Bourbière ; 28-32 à l'Alpe) | n° 46-60 (dont **56-60 à 1,56-1,69 km de la tour, caps 31-53°**) | **n° 3 et 11 hors zone** (Hauts de Chartreuse, entre le Guiers Vif et l'Alpe, ≥ 9-14 km), positions non publiées | — |
| Bornes « 5 », « 9 », « 14 » (Détrier / La Chapelle-du-Bard) | OSM | nombres peints/gravés, série inconnue | 3 | 9 ↔ 14 = 160 m pour 5 rangs ⇒ 3 ↔ 11 ≈ 0,25 km | — |
| **PR routiers** (bornes kilométriques, BD TOPO `point_de_repere`) | IGN | PR n = km n de chaque route | 1 676 PR, ~110 routes 38/73 | meilleurs PR3-PR11 : D109 2 329 m, D25 2 373 m, D208 2 455 m — **aucun à ±1 %** | 1/210 |
| **Pylônes RTE** (ref par ligne, tronçons fusionnés) | OSM | n° peints sur chaque pylône | ~300 numérotés | lignes 63 kV : 1 144 m (ligne qui part près de la tour), 2 313 / 4 959 m, 3 717 m — **aucun à ±1 %** | 1/167 |
| Balises de gazoduc NaTran | OSM | ref 15, 21, 29, 50 | 17 | pas = 27-60 m ⇒ 3 ↔ 11 ≈ 0,2-0,5 km ; n° 3 et 11 hors zone | — |
| Bornes incendie | OSM | ref 0003… par commune | 304 | 686 m | — |
| **Parcelles cadastrales** n° 3 et 11 d'une même section | Parcellaire Express (31 communes) | n° de parcelle | 257 sections | **aucune paire à ±1 %** (174 paires 3-11) | 0/2 083 |
| Sections cadastrales C ↔ K (3e et 11e lettres) | idem (feuilles) | lettres | 31 communes | Chapareillan AC-AK 1 932 m (+4,4 %), Porte-de-Savoie 1 662 m, Allevard 1 653 m | 0/46 |
| Feuilles cadastrales 3 ↔ 11 | idem | n° de feuille | 1 cas | La Buissière 0B : 1 977 m (+6,9 %) | — |
| **Parcelles forestières ONF** (n° ou lettres, peints sur les arbres de limite) | ONF « Parcelles forestières publiques » (WFS carmencarto) | 3/11 ou C/K | 36 forêts | **FC Saint-Maximin (A-P) : C ↔ K = 2 028 m (+9,6 %)** ; FC Pontcharra (A-V) : 1 694 m (−8,4 %) ; FC Barraux (A-N) : 1 953 m (+5,6 %) ; FC Allevard 3-11 : 2 076 m ; FC Chapareillan 3-11 : 957 m — **aucune à ±1 %** (centroïdes) | 3/192 |
| **Réseau points-nœuds pédestre** (Grésivaudan / Chartreuse / Cœur de Savoie) | OSM (`lwn_name`, 272 nœuds) | **nœuds NOMMÉS, pas numérotés** (« Tour d'Avalon », « Avalon Village », « Le Vivier », « Les Gorges »…) ; aucun `lwn_ref`/`rcn_ref` dans tout le carré | 159 nœuds + 197 poteaux | pas de 3e / 11e intrinsèque. Rang le long des itinéraires OSM (GR 965, chemin de Szombathely) : meilleure paire 3 515 m | 0/18 |
| Lacets / épingles (détection géométrique, 9 réglages) | OSM | **aucun panneau de numérotation trouvé** | routes à ≥ 11 épingles : D208 (18), D109 (12), D108 (11) | **D208 (Savoie, 7,8-9,2 km E) épingles 3 → 11 = 1 825-1 966 m selon le réglage (1 836 m au réglage central)** ; sens inverse 909-1 105 m | 2/20 (≈ 10 %) |
| Sentier thématique de Saint-Maximin (« À la découverte des hameaux ») | alpes-isere.com + BD TOPO | **9 étapes** : 1 tour d'Avalon, 2 oratoire, 3 Les Ripellets, 4 Le Crêt, 5 Les Bruns, 6 Répidon, 7 église, 8 forge, 9 Le Vivier | 9 | **pas de 11e** | — |
| ENS du marais d'Avalon | OSM | 1 panneau | 1 | emprise du marais = 232 m | — |
| Parcours santé | OSM | stations | Rotissons (St-Vincent-de-Mercuze, 9 km) ; 5 stations à Chapareillan (5,5 km), dans 200 m | ≪ 1 850 m | — |
| Parcours d'orientation de Pontcharra | web | — | **aucune trace trouvée** (CDCO 38 : Moirans, Tullins…, pas Pontcharra) | — | — |
| Anciennes gares du tram Grenoble-Chapareillan | OSM + Wikipédia | ordre des arrêts | 8 dans la zone | rangs 3 et 11 hors zone ; arrêts espacés de 1-3 km | — |
| Écluses | OSM + BD TOPO | — | **aucune** (pas d'écluse sur l'Isère ici) | — | — |
| Seuils / barrages | BD TOPO (5 seuils, 4 barrages, 3 vannes) + OSM | non numérotés | — | pas de série | — |
| Arbres remarquables, ruchers, croix de mission, ex-voto, stations de mesure | OSM (1 360 arbres sans ref), BD TOPO (croix) | aucune série numérotée trouvée | — | non testable | — |

Notes :
- Les bornes sardes sont en calcaire (fleur de lys d'un côté, croix de Savoie de l'autre, « 1822 » et un numéro). Plusieurs ont disparu (37, 38, 61-65) ou ont été refaites (46, 47, 50).
- Coïncidence sans valeur : le pylône n° 11 de la ligne 63 kV qui part près de la tour (45.44523, 6.02617) est à 1 858 m de la tour. Mais le n° 3 de la même ligne est à 1 144 m du n° 11, donc ce n'est pas une paire 3e-11e à 10 stades.

## 2. Tableau hypothèses × critères (C1-C12 du BRIEF)

✓ = compatible, ✗ = contredit (le motif est entre parenthèses), ? = indéterminé.

| Hypothèse | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bornes sardes 1822, n° 3 et 11 | ✓ | ✓ | ? (hors zone, positions inconnues) | ✗ (pierre calcaire, pas de bois) | ? | ✓ (≥ 67) | ✓ | ✓ | ✓ | ? | ? | ✓ | **ÉCARTÉE (C4)** si « écharde » veut dire bois ; sinon FAIBLE (hors zone) |
| Bornes « 5/9/14 » (Détrier) | ✓ | ? | ✗ (pas de 160 m / 5 rangs ⇒ ≈ 0,25 km) | ✗ (pierre) | ? | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ | **ÉCARTÉE (C3, déduit de l'espacement ; C4)** |
| PR routiers 3 et 11 | ✓ | ✓ (une paire par route) | ✗ (fait : aucune route à ±1 %) | ✗ (borne béton/peinture) | ✗ | ✓ | ✓ | ✓ | ✗ (faciles) | ? | ? | ✓ | **ÉCARTÉE (C3, fait)** |
| Pylônes RTE 3 et 11 | ✓ | ✗ (une paire par ligne, plusieurs lignes) | ✗ (fait) | ✗ (acier) | ✗ | ✓ | ✓ | ✓ | ✗ | ? | ? | ✓ | **ÉCARTÉE (C3, fait ; C4)** |
| Balises de gaz NaTran | ✓ | ✓ | ✗ (espacement 27-60 m) | ✗ (plastique/métal) | ✗ | ✓ | ✓ | ✓ | ? | ? | ? | ✓ | **ÉCARTÉE (C3)** |
| Parcelles cadastrales 3 et 11 | ✓ | ✗ (une paire par section) | ✗ (fait : 0/174) | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ | **ÉCARTÉE (C3, fait)** |
| Sections cadastrales C et K / feuilles 3 et 11 | ✓ | ✗ | ✗ (fait : au mieux +4,4 %) | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ | **ÉCARTÉE (C3, fait)** |
| Parcelles forestières ONF 3/11 ou C/K | ✓ | ✗ (une paire par forêt) | ✗ (fait, centroïdes : au mieux +5,6 % à Barraux, +9,6 % à Saint-Maximin) ; ce sont des surfaces, pas des points | ? | ✓ | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ | **ÉCARTÉE (C3, fait)**. Réserve : en prenant un point quelconque des parcelles C et K de Saint-Maximin, on peut obtenir de 1 791 à 2 087 m, mais ce choix serait arbitraire. |
| Points-nœuds pédestres (rangs 3 et 11) | ✓ | — | ✗ (pas de numéros ; rang le long des itinéraires : meilleure paire 3 515 m) | ✗ (poteaux de même matériau) | ✗ | ? | ✗ (pas de rang intrinsèque) | ✓ | ✗ | ? | ? | ✓ | **ÉCARTÉE (fait : nœuds nommés, pas numérotés)** |
| Épingles de la D208 (3e → 11e) | ✓ | ✓ | ✓ au réglage central (1 836 m), mais pas stable (1 825-1 966 m) | ✗ (enrobé, pas de bois) | ✓ | ✓ (18 épingles) | ? | ✓ | ? | ? | ✗ (7,8 km de la tour, en Savoie, sans lien avec le départ) | ✓ | **ÉCARTÉE (C4)**. Hasard : 10 % des paires (i, i+8) des mêmes routes tombent à ±1 %. Aucune numérotation sur place. |
| Sentier thématique Saint-Maximin | ✓ | ✓ | — | — | ✓ | ✗ (9 étapes) | ✗ (pas de 11e) | ✓ | ✗ (balisé, facile) | ? | ? | ✓ | **ÉCARTÉE (sûr : il n'existe pas de 11e étape ; C6/C7)** |
| ENS marais d'Avalon | ✓ | — | ✗ (emprise 232 m) | ? | ✓ | ✗ | ✗ | ✓ | ✗ | ? | ? | ✓ | **ÉCARTÉE (C3, fait)** |
| Parcours santé | ✓ | ✓ | ✗ (extension cartographiée < 300 m ; Rotissons à 9 km) | ✓ possible (agrès en bois) | ✓ | ? | ✓ | ✓ | ✗ | ? | ? | ✓ | **FAIBLE** (aucune paire possible avec les données ; un parcours de ~1,5 km ne donne pas 1 850 m en ligne droite entre deux stations) |
| Parcours d'orientation de Pontcharra | ✓ | ✓ | ? | ✓ possible (balises bois) | ✓ | ? | ✓ | ✓ | ✓ | ? | ? | ✓ | **FAIBLE / non testable** (existence non établie) |
| Anciennes gares du tram | ✓ | ✓ | ✗ (rangs 3/11 hors zone ; espacement de plusieurs km) | ? | ✓ (quais) | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ | **ÉCARTÉE (C3)** |
| Escaliers / marches (tour, etc.) | ✓ | ✓ | ✗ (un escalier fait ≪ 1 850 m) | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ? | ? | ✓ | **ÉCARTÉE (C3)** |
| Écluses | — | — | — | — | — | — | — | — | — | — | — | — | **ÉCARTÉE (fait : aucune dans 8 km)** |
| Seuils / barrages de correction torrentielle (RTM) numérotés | ✓ | ✓ | ? | ✓ possible (seuils bois / pierre) | ✓ (on marche sur la crête) | ? | ✓ | ✓ | ✓ (non cartographiés) | ? | ? | ✓ | **FAIBLE / non testable** : aucune série numérotée dans BD TOPO ni OSM ; la base ouvrages RTM (ONF) n'est pas accessible ici |
| Arbres remarquables, croix de mission, ex-voto, ruchers, stations de mesure | ? | ? | ? | ? | ? | ? | ? | ✓ | ? | ? | ? | ✓ | **non testable** (aucune série numérotée dans les données) |

## 3. Taux de hasard (témoins)

On compte, dans la même famille, toutes les paires de rangs (i, i+8) qui tombent à 1 850 m ±1 % :
PR 1/210 (0,5 %) ; pylônes 1/167 (0,6 %) ; parcelles cadastrales 0/2 083 ; sections 0/46 ; parcelles ONF 3/192 (1,6 %) ; épingles 2/20 (≈ 10 %) ; poteaux le long des itinéraires 0/18.
La seule paire à ±1 % (épingles 3 → 11 de la D208) est au niveau du hasard de sa propre famille. Elle dépend aussi du réglage de détection et contredit C4.

## 4. Verdict R4

**Aucune hypothèse VIVANTE dans cette famille.** Aucune paire concrète 3e ↔ 11e d'objets numérotés ou ordonnés n'est à 1 850 m ±1 % dans les 8 km, à l'exception d'épingles de route (D208) qui relèvent du hasard et contredisent C4.

Faits utiles pour les autres pistes :
1. Les poteaux du réseau du Grésivaudan ne portent pas de numéros : ce sont des **nœuds nommés**. Aucune lecture « nœud n° 3 / n° 11 » n'est possible.
2. Le sentier patrimoine de Saint-Maximin a **9 étapes seulement**. L'étape 3 est Les Ripellets.
3. Les **bornes sardes de 1822** sont la seule série numérotée « culturelle » de la zone. Elles sont difficiles à trouver, numérotées au-delà de 13, et les rangs y comptent. Mais elles sont en pierre (C4) et leurs n° 3 et 11 sont hors de la zone des 8 km. Si l'on admet une écharde sur une borne refaite ou sur un piquet de remplacement, il faudrait obtenir les coordonnées des bornes 1-15 (AHCS, PNR Chartreuse) avant de conclure.
4. Les seuils RTM numérotés (bois / pierre, on marche dessus) cochent C4 et C5 sur le papier. Mais aucune donnée ouverte ne permet de les situer. Seuls l'ONF-RTM ou un repérage sur place pourraient le faire.

## Résumé (≤ 300 mots)

R4 a inventorié dans 8 km de la tour d'Avalon les objets de terrain numérotés ou ordonnés. Sources : API OSM (15 tuiles), BD TOPO (PR, constructions), Parcellaire Express, parcellaire ONF, web.

Séries testées, avec la meilleure paire 3e-11e :
- **PR routiers** : 2 329 m au mieux.
- **Pylônes RTE** : 1 144, 2 313 et 3 717 m.
- **Parcelles cadastrales** : 0 paire sur 174.
- **Sections C/K** : +4,4 % au mieux.
- **Parcelles ONF** : Saint-Maximin C-K 2 028 m, Barraux 1 953 m, Pontcharra 1 694 m.
- **Balises de gaz**, **bornes « 9/14 »** : espacement de quelques dizaines de mètres, donc 3-11 à quelques centaines de mètres.

Aucune n'atteint 1 850 m ±1 %. Les taux de hasard de ces familles sont de 0 à 1,6 %.

Seule exception : les épingles 3 → 11 de la **D208** (Savoie, 7,8 km). Elles donnent 1 836 m au réglage central (1 825-1 966 m selon le réglage). Mais 10 % des paires témoins font aussi bien, aucune numérotation n'existe sur place, et l'enrobé contredit C4 (pas d'écharde). C'est du bruit.

Écartées sur des faits :
- Le réseau points-nœuds du Grésivaudan a des nœuds **nommés, non numérotés**.
- Le sentier patrimoine de Saint-Maximin n'a que **9 étapes** (pas de 11e).
- Le marais d'Avalon ne fait que 232 m.
- Il n'y a ni écluse ni parcours d'orientation attesté à Pontcharra.

Fait nouveau : les **bornes sardes de 1822** (frontière Savoie-France de 1760, numérotées jusqu'à 67 au moins) passent à 1,6 km de la tour (n° 56-60). C'est la seule série « culturelle » numérotée de la zone. Mais elles sont en pierre (C4), et leurs n° 3 et 11 sont dans les Hauts de Chartreuse, hors zone et non localisés.

Restent non testables faute de données : les seuils RTM numérotés (bois / pierre, on marche dessus : compatibles avec C4 et C5 sur le papier), les arbres remarquables et les croix de mission.

**Verdict : aucune hypothèse vivante dans la famille « objets numérotés de terrain ».**

Sources web : plaquette AHCS « Les bornes sardes en Cœur de Savoie » (altituderando.com), PNR Chartreuse « Patrimoine Entremonts », alpes-isere.com (parcours thématique Saint-Maximin), data.gouv.fr (parcelles forestières ONF).
