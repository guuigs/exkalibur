---
tags:
  - "#exkalibur"
  - "#E12"
---
# R5 : « troisième et onzième », famille histoire locale, narrateur, Hugues d'Avalon, chartreux, Arthur/Avalon, *Roman de la Rose*, toponymie

> Rapport du 03/10/2026. FAIT = vérifié (texte, données, calcul). HYPOTHÈSE = interprétation. Je n'écarte une piste que si une réponse de l'auteur (grille C1-C12 du BRIEF) ou un fait vérifié la contredit.
> Scripts et données : scratchpad `R5/` (`gaz.py` = gazetteer de 1 463 noms (BD TOPO, cadastre, OSM) + 3 723 voies et lieux-dits BAN à moins de 15 km (`ban_voies.json`) ; `river.py`, `breda_cross.json` = franchissements du Bréda ; `osm_r5.json` = OSM étendu à 5,99-6,14 E / 45,35-45,47 N ; parcelles Etalab 38426 / 38314 / 38313).

## 1. Sources consultées
- Wikipédia FR « Saint-Maximin (Isère) » (texte brut) : liste des **12 hameaux** et du patrimoine civil.
- Office de tourisme Alpes-Isère, « Parcours thématique Saint-Maximin » : **9 étapes** (1 tour d'Avalon, 2 oratoire, 3 Les Ripellets, 4 belvédère du Crêt, 5 Les Bruns (magnanerie), 6 Répidon / chapelle Saint-Joseph, 7 église (1888), 8 forge du père Gauthier, 9 étang du Vivier).
- Maisons paysannes de France, Isère (programme du 21/10/2023) : la tour a été reconstruite par les chartreux. **FAIT** : son escalier intérieur est en **chêne** (restauré par un ébéniste).
- France-Cadastre / AD Isère 4P4/208 : le cadastre napoléonien de Saint-Maximin ne compte que **2 sections (A, B)**. Le cadastre actuel aussi.
- *Roman de la Rose*, traduction de Marteau, tome I (`Sources/roman_de_la_rose_marteau_tome1.txt`) : rubriques des chapitres, liste des oiseaux, liste des arbres, matière du guichet.
- FAQ8 (`faq8f.txt`) et `FAQ_E12_complet.md` relues pour la grille.
- Inventaires FAPI (bassins et fontaines) et inventaire régional (moulins) : **aucune liste numérotée** pour Saint-Maximin ou Pontcharra n'est accessible en ligne.

## 2. Tableau hypothèses × critères

✓ = compatible, ✗ = contredit, ? = indéterminé.

| # | Hypothèse | C1 | C2 | C3 (1 850 m) | C4 | C5 | C6 (≥13) | C7 | C8 | C9 | C10 | C11 | C12 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Séries « bayardiennes » : batailles, maisons fortes des Terrail, étapes de sa vie | ✓ | ✓ | ✗ (batailles en Italie et en Flandre ; 1 à 2 maisons fortes locales) | ? | ? | ? | ? | **✗** | ? | ? | ? | ? | **ÉCARTÉE (sûr)** : FAQ07-065, les 3e et 11e n'amènent pas à s'intéresser à un chevalier |
| A2 | Poteaux PDIPR du circuit « Sur les traces du chevalier Bayard » (3,9 km) | ✓ | ✓ | ? (pas de numéros dans OSM) | ✗ probable (poteaux en bois tous les deux) | ✗ (on ne marche pas sur un poteau) | ? | ? | ✗ (circuit nommé d'après le chevalier) | ✗ (visibles, balisés) | ? | ? | ? | **ÉCARTÉE (sûr)** : C8 ; et on ne marche pas sur un poteau (C5) |
| B1 | Hugues d'Avalon : étapes de sa vie (Avalon, Villard-Benoît, Grande Chartreuse, Witham, Lincoln…) | ✓ | ✓ | ✗ (les lieux sont à des dizaines ou des centaines de km) | ? | ? | ✗ (moins de 13 étapes) | ? | ✓ | ? | ? | ? | ? | **ÉCARTÉE** (échelle ; pas de 13e) |
| B2 | Chartreuses par ordre de fondation (3e = Portes, 1115…) | ✓ | ✓ | ✗ (sites à plus de 10 km les uns des autres) | ? | ? | ✓ | ✓ | ✓ | ? | ? | ✗ (rien près de la tour) | ? | **ÉCARTÉE** (C3 : aucune paire possible à 1,85 km) |
| B3 | Fours, moulins et granges de la seigneurie d'Avalon ou des chartreux | ? | ? | ? | ? | ? | ? | ? | ✓ | ? | ? | ? | ? | **NON TESTABLE** : aucune liste ordonnée trouvée en ligne |
| C1 | *Roman de la Rose*, **chapitres III et XI** (III = Oiseuse ouvre le guichet du mur ; XI = Narcisse à la fontaine sous le pin, qui contient « Dieu sut se montrer favorable ») | ✓ (deux chapitres) | ✓ | ? : depuis la tour ou la rue du Rempart, aucune source ou fontaine (86 points BD TOPO/OSM) à 1 850 m ±1 % (témoin : 39 % des départs aléatoires en ont une) | **✗ en lecture littérale** : FAIT, « Le guichet, qui de charme était » (bois) | ? | ✓ (XIII = flèches près de la rose, « pas le bon endroit ») | ✓ | ✓ | ✓ | ? (enl. 9 = fontaine ?) | ? | ? | **FAIBLE**. Littéralement (3e = guichet en bois) : **ÉCARTÉE (C4)**. En lecture « lieux » (3e = porte du mur, 11e = fontaine) : vivante mais sans point candidat |
| C2 | *Roman*, **liste des oiseaux de Marteau** (v. 655-675) : 1 hirondelles, 2 chardonnerets, **3 tourterelles**, 4 geai, 5 roitelet, 6 alouette, 7 mésange, 8 rossignols, 9 merles, 10 mauviettes, **11 étourneaux**, 12 bergeronnettes, **13 perruches** | ✓ | ✓ | **✗ en projection toponymique** : aucun « étourneau » ou « sansonnet » dans 15 km (BAN, cadastre, BD TOPO, OSM) ; une seule « Rue des Tourterelles » (Le Cheylas, 5 km) | ? | ? | **✓ exactement 13** (le 13e, la perruche, ne « mène » nulle part) | ✓ (pas de 16e) | ✓ | ✓ | ? | ? | ✓ (*la* tourterelle, *l'*étourneau masc. ; FAQ07-068 : « sur **le** onzième ») | **FAIBLE mais à garder** : la structure colle (13 éléments, « J'entends le chant retentir »), mais aucune projection sur la carte |
| C2' | Même liste, ancien français (3 estorniaus, 11 melles, 13 papegaus) → 11e = **CHANTE-MERLE** (lieu-dit, 1 873 m de la tour) | ✓ | ✓ | ✗ (aucun toponyme « étourneau » pour le 3e) | ? | ? | ✓ | ✓ | ✓ | ? | ? | ? | ✗ (genres m./m.) | **FAIBLE** : l'auteur cite Marteau, pas l'ancien français |
| C3 | Carole : 16 personnes (3 Amour, 11 fils du seigneur de Windsor, 13 chevalier de Courtoisie) | ✓ | ✓ | ✗ (des personnes, pas des points) | ? | ✗ | ✓ | ? | ✗ probable (9e = chevalier du lignage d'Arthur ; 11e = « bacheler ») | ? | ? | ? | ? | **ÉCARTÉE** (pas de points cartographiables ; C8 douteux) |
| C4 | Images du mur (10), flèches (5+5) | ✓ | ✓ | ✗ | ? | ? | **✗** (pas de 11e) | – | ✓ | ? | ? | ? | ? | **ÉCARTÉE (sûr)** : pas de 11e élément |
| C5 | Arbres du verger (une trentaine ; Marteau 3 dattier / 11 noisetier ou alise selon le découpage) | ✓ | ✗ (plusieurs arbres de chaque sorte dans la nature) | ✗ (aucun toponyme utile) | ✗ (bois → écharde possible aussi sur le 3e) | ? | ✓ | ✓ | ✓ | ? | ? | ? | ? | **ÉCARTÉE** (C4 : un arbre donne des échardes, donc aussi sur le 3e) |
| D1 | **12 hameaux** de Saint-Maximin (ordre Wikipédia : Avalon, Bretonnières, **Ripellets**, Bruns, Crêt, Rojons, Dobo, Repidon, Varanger, Mouret, **St-Maximin-le-Vieux**, La Combe) | ✓ | ✓ | ✗ : 1 790 m (BD TOPO, −3,2 %), de 1 700 à 1 975 m selon le point retenu | ? | ✓ | **✗** (12 éléments, liste « dont notamment ») | ? | ✓ | **✗** (visibles sur Maps ; FAQ05-074 / FAQ06-227) | ? | ? | ? | **ÉCARTÉE** : C6, et la distance n'est pas stable (zones de 200 m) |
| D2 | Parcours thématique communal (9 étapes) | ✓ | ✓ | – | ? | ✓ | **✗** (9) | – | ✓ | ✗ | ? | ? | ? | **ÉCARTÉE (sûr)** : pas de 11e |
| D3 | Cadastre : sections (napoléonien et actuel) | ✓ | ✓ | – | ? | ? | **✗** (2 sections) | – | ✓ | ? | ? | ? | ? | **ÉCARTÉE (sûr)** |
| D4 | Cadastre : parcelles n° 3 et n° 11 d'une même section (Saint-Maximin A/B, Pontcharra 23 sections, 38313) | ✓ | ✓ | **✗** : 0 paire à 1 850 m ±1 % (Saint-Maximin : 9 paires (k, k+8) à 1 850 m sur environ 3 500 parcelles, mais jamais (3, 11)) | ? | ✓ | ✓ | ✓ | ✓ | ? | ? | ? | ? | **ÉCARTÉE** (C3) |
| E1 | Fontaines, sources, lavoirs, points d'eau (BD TOPO + OSM, 86 points à moins de 6 km) | ✓ | ✗ (aucun numérotage) | ? | ? | ? | ? | ? | ✓ | ? | ? | ? | ? | **NON TESTABLE comme série**. Aucune liste numérotée trouvée. Comme cibles à 1 850 m du départ : 0 depuis la tour ou la rue du Rempart ; 1 depuis Le Vivier (point d'eau, 1 867 m, cap 202°), au niveau du hasard (39 %) |
| F1 | Ponts du **Bréda** comptés depuis l'embouchure (25 ponts relevés jusqu'à Allevard) : 3e = passerelle **métal** (45.43716, 6.01574) ; 11e = pont de la D525 (45.43091, 6.09497) | ✓ | ✓ | **✗** : 6 221 m | ✓ (métal / asphalte) | ✓ | ✓ | ✓ | ✓ | ✗ (visibles) | ? | ✗ (rien près de la tour) | ? | **ÉCARTÉE (C3)**. Une seule paire des 300 possibles tombe à 1 850 m ±1 % (ponts 14-23, 1 849 m) : niveau du hasard |
| F2 | Ponts du Bréda comptés depuis la source | ✓ | ✓ | ? (OSM téléchargé seulement jusqu'à 45,35° N) | ? | ✓ | ✓ | ✓ | ✓ | ✗ | ? | ✗ (au-delà d'Allevard, à plus de 9 km de la tour) | ? | **ÉCARTÉE en pratique** (C11 : trop loin de la clairière) |
| F3 | Moulins et scieries du Bréda (Moulin-Vieux, papeteries…) | ? | ? | ? | ? | ? | ? | ? | ✓ | ? | ? | ? | ? | **NON TESTABLE** : pas de liste ordonnée accessible |
| T1 | Toponymes ordinaux (trois, tiers, onze, treize…) | – | – | ✗ (seulement « les Trois Têtes », 3,6 km) | – | – | – | – | – | – | – | – | – | **ÉCARTÉE** |

## 3. Faits nouveaux utiles

1. **FAIT** : la liste des oiseaux de la traduction de Marteau, celle que l'auteur cite, compte **exactement 13 oiseaux**. Le 3e est la **tourterelle** (féminin), le 11e l'**étourneau** (masculin), le 13e la **perruche**. Il n'y a ni 14e ni 16e. L'ancien français compte aussi 13 oiseaux, mais dans un autre ordre (3 étourneaux, 11 merles, 13 perroquets).
   - Cette structure colle à C6 (« on aurait pu aller jusqu'au 13e, mais il ne mènerait pas au bon endroit »), à C7 (8e/16e « incorrect »), à C12 (l'auteur dit spontanément « sur **le** onzième ») et à « J'entends le chant retentir » (le chant des oiseaux derrière le mur, que seul le narrateur entend).
   - Je n'ai trouvé **aucune projection** sur la carte : aucun lieu « étourneau » ou « sansonnet » dans 15 km. Si cette piste est la bonne, les 3e et 11e seraient des objets non nommés à identifier autrement, peut-être sur les enluminures (C10). Il faudrait chercher une tourterelle et un étourneau dans les 12 enluminures en HD.
2. **FAIT** : le chapitre III du *Roman* est celui du **guichet en bois de charme**. Si « troisième » renvoie à ce guichet, la contrainte de l'écharde (aucune sur le 3e) est violée. La piste « chapitres III/XI » ne survit qu'en lisant les chapitres comme des lieux (la porte du mur, la fontaine sous le pin). Elle a un atout : FAQ04-115 dit qu'on va « directement de la troisième à la onzième » mais qu'on « passe par des étapes intermédiaires », ce qui correspond aux chapitres IV à X. Mais elle ne fournit aucun point.
3. **FAIT** : l'escalier de la tour d'Avalon est en **chêne**. Il pourrait servir pour une série de « marches », mais l'échelle de 1 850 m l'exclut.
4. **Curiosité, non retenue** : lieu-dit **CÔTE ROSE** (Pontcharra, 45.41609, 6.01828), à 1 824 m de la rue du Rempart (−1,4 %) et à 1 889 m du Vivier, au cap 213°. La « rose » est le chapitre XIII, celui qui « ne mène pas au bon endroit ». Ce lieu est dans la direction opposée au lever du soleil, et la densité de lieux-dits rend ce genre de coïncidence banal.
5. **Réserve sur le narrateur** (sans conséquence ici) : dans FAQ8, l'auteur confirme que le narrateur « a écrit des palindromes » et qu'il « a tout conçu ». Cela se lit comme la fiction du parchemin (ROMA/AMOR), et ne contredit pas Bayard.

## 4. Paires concrètes à 1 850 m ±1 % (aucune vivante)

| Paire | Coordonnées | Distance | Rangs | Taux de hasard |
|---|---|---|---|---|
| Ripellets ↔ Saint-Maximin-le-Vieux (hameaux 3 et 11) | 45.43189, 6.04958 ↔ 45.42043, 6.03347 | 1 790 m (de 1 700 à 1 975 m selon la source) | 3 / 11 | 2 paires sur 66 à ±1 % (3 %) ; écartée par C6 et C9 |
| Ponts 14 ↔ 23 du Bréda | 45.40151, 6.07989 ↔ 45.38500, 6.08275 | 1 849 m | 14 / 23 (pas 3 / 11) | 1 paire sur 300 |
| Le Vivier → point d'eau | 45.42898, 6.03404 → 45.41346, 6.02489 | 1 867 m | – | 39 % des départs aléatoires ont au moins une cible d'eau dans l'anneau |

## 5. Résumé (≤ 300 mots)

J'ai testé 20 hypothèses de la famille « histoire locale, narrateur, Hugues d'Avalon, chartreux, Avalon, *Roman de la Rose*, toponymie ». Aucune ne donne deux points à 1 850 m ±1 % qui respectent la grille.

- **Écartées (sûr)** :
  - toutes les séries liées à Bayard, par C8 (FAQ07-065) ;
  - le parcours thématique communal (9 étapes) et les sections cadastrales (A et B seulement), par C6 ;
  - les images du mur et les flèches du *Roman* (pas de 11e) ;
  - le guichet du chapitre III, en bois de charme : écharde sur le 3e, contraire à C4.
- **Écartées sur données** :
  - les 12 hameaux : liste de 12 seulement, et 3e-11e = 1 790 m, distance instable ;
  - les parcelles n° 3 et 11 : aucune paire à 1 850 m ;
  - les ponts du Bréda depuis l'embouchure : 3e-11e = 6,2 km ;
  - les toponymes ordinaux, les chartreuses, les étapes de la vie d'Hugues d'Avalon (mauvaise échelle).
- **Non testables faute de liste publiée** : fours, lavoirs et moulins numérotés de Saint-Maximin, moulins du Bréda. Les points d'eau BD TOPO/OSM ne donnent rien au-delà du hasard (39 %).
- **Seule trouvaille structurelle (FAIBLE, à garder)** : la liste des oiseaux du *Roman* dans la traduction de Marteau. Elle compte exactement 13 oiseaux : 3e = **la tourterelle**, 11e = **l'étourneau**, 13e = la perruche, pas de 16e. Elle s'accorde avec C6, C7, C12 et avec « J'entends le chant retentir ». Mais aucun lieu ne porte ces noms dans 15 km. Il faut chercher une tourterelle et un étourneau sur les enluminures HD avant d'aller plus loin.
- **Lecture « chapitres III/XI »** (porte du mur, puis fontaine de Narcisse) : elle reste possible seulement comme lecture de lieux. Elle ne propose aucun point.

**Conclusion** : ma famille ne livre pas les 3e et 11e. Le *Roman* sert de confirmateur de la zone, pas de liste à projeter, sauf peut-être la liste des oiseaux.
