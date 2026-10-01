# T1 : rapport terrain IGN (bassin, clairière, toponymes, fort Barraux)

Date : 30/09/2026. Scripts : `T1_bassin2.py`, `T1_clairiere.py`, `T1_toponymes.py`, `T1_livrables.py` (sorties `.out.txt`). Sources : BD TOPO v3 (GeoJSON en cache), altimétrie IGN RGE ALTI, cadastre Etalab (lieux-dits), photo IMG_4342.

## Verdict
- **Bassin de l'enluminure 9 : aucune ressemblance forte** avec un plan d'eau IGN à ≤ 6 km de la tour (Maupas 0,83 ; Cheylas 0,60 ; Lônes 0,48 ; 18 surfaces sur 62 dépassent 0,80). Le contour est un blob trop générique. Confiance dans « non identifié » : haute ; confiance dans une identification quelconque : très faible (< 5 %).
- **Clairière** : sur 217 jonctions de chemins à ≤ 2,5 km de la tour, **aucune ne cumule** les 5 filtres. Le meilleur candidat n'a que 3 ou 4 filtres et aucun indice indépendant ne le désigne.
- **Toponymes** : « Avalon » (lieu-dit cadastral, 90 m de la tour), « Tire-Loup » (1,6 km E), « Château Bayard » (1,1 km) ; rien pour étoile, émeraude, diamant, ancre, lune, souche, charpentier, coupe.
- **Fort Barraux** : 0 jonction avec trouée, 0 en domaine public ; eau+vue+versant est = 4 jonctions sur le flanc ouest. Piste vivante, non favorite.
- **Bilan : pas de solution.** Filtres trop lâches, ou clairière trop petite pour la BD TOPO.

## 1. Bassin (enluminure 9)

**FAIT** (recadrage HD de IMG_4342 tournée de 90° ; contrôle `T1_bassin_trace_controle.png`) :
- Étang bleu allongé (rapport petit/grand axe ≈ 0,58), extrémité gauche en pointe émoussée, lobe large à droite, bord haut légèrement creusé là où tombe une fine cascade issue du rocher rayonnant : le ruisseau **alimente** l'étang, aucune sortie visible. 2 poissons.
- Les **2 cygnes** sont sur le grand lac pâle de l'arrière-plan, pas dans l'étang.
- Rocher jaune-gris à rayons dorés portant la coupe ; grand arbre à fruits jaunes à droite.
- Horizon, de gauche à droite : chaîne bleutée ; butte grise avec petite tour/bâtiment blanc ; village orange à toits pointus et clochers ; longue muraille orange à arcades et créneaux ; montagnes roses et bleues.

**Comparaison IGN** (62 surfaces d'eau hors cours d'eau à ≤ 6 km, IoU invariant aux rotations ±20° et symétries ; planche `T1_bassin_planche.png`) :

| Plan d'eau IGN | Distance / cap | IoU |
|---|---|---|
| Retenue 30709375 (Intermittent) | 3.0 km / 327° | 0.88 |
| Plan d'eau de gravière 03273243 (Intermittent) | 3.4 km / 304° | 0.87 |
| Réservoir-bassin 90275409 (Intermittent) | 2.4 km / 236° | 0.87 |
| Retenue 07503763 (Permanent) | 3.7 km / 216° | 0.86 |
| Réservoir-bassin d'orage 07503206 (Permanent) | 2.8 km / 307° | 0.84 |
| **Étangs du Maupas** | 3.6 km / 216° | 0.83 |
| **Bassin du Cheylas** | 6.0 km / 214° | 0.60 |
| **Plan d'Eau des Lônes** | 2.7 km / 320° | 0.48 |

**Test du hasard** : médiane IoU 0,74 ; 29/62 ≥ 0,75 ; 18/62 ≥ 0,80. Un blob quelconque « colle » à ~0,7, donc la forme seule ne prouve rien. **Abandon de la piste « forme » : non discriminante.** Piste restante : l'arrière-plan (grand lac, muraille orange, butte à tour blanche) est peut-être la vue depuis le site.

## 2. Clairière : jonctions (tour d'Avalon, rayon 2,5 km)

Méthode : nœuds à ≥ 3 branches de `troncon_de_route` (Sentier/Chemin/Route empierrée). **Trouée** = hors forêt/bois (`zone_de_vegetation`), < 15 % de forêt à 20 m et ≥ 35 % entre 25 et 90 m. **Eau** = tronçon hydro « Ecoulement naturel » ≤ 150 m. **Public** = dans une `foret_publique` (proxy, pas le cadastre). **Vue** = ligne de vue terrain seul, tour +8 m vers point +1,7 m (RGE ALTI, sans végétation ni bâti). **Versant est** = pente ≥ 4 % et descente au cap 45–135°.

**Limite** : vue et versant ne sont calculés que pour les jonctions avec trouée OU ruisseau ≤ 150 m (économie d'appels altimétrie) ; les chiffres « vue » et « versant est » sont donc des minorants, sans effet sur les combinaisons avec eau ou trouée. Trouée = seuil strict ; en le relâchant (≥ 15 % de forêt autour), 9 jonctions et 4 avec eau.

**Test du hasard** (217 jonctions) :

| Filtre | Passent | Part |
|---|---|---|
| trouée | 2 | 0.9 % |
| ruisseau ≤ 150 m | 101 | 46.5 % |
| forêt publique | 21 | 9.7 % |
| vue depuis la tour | 57 | 26.3 % |
| versant est | 3 | 1.4 % |

Combinés : trouée+eau = 2 ; trouée+eau+vue = 2 ; eau+public+vue = 4 ; eau+vue+est = 1 ; **les 5 ensemble = 0**. Espérance par hasard (indépendance) ≈ 0.0003. Avec des filtres aussi lâches (eau 46 %, vue 26 %), un candidat à 3 filtres n'informe pas.

**Top 10** (score = nb de filtres + bonus proximité − distance/10 km) :

| # | Lat, Lon | Dist/cap | Nature | Filtres | Ruisseau (dist ; flux ; cap du ruisseau depuis la jonction) | Score |
|---|---|---|---|---|---|---|
| T01 | 45.44825, 6.02694 | 2171 m / 352° | Chemin/Route empierrée | eau≤150m public vue (3/5) | 28 m ; sans nom ; coule vers 224° ; ruisseau au 135° | 3.78 |
| T02 | 45.41707, 6.05150 | 2074 m / 129° | Chemin/Sentier | eau≤150m public vue (3/5) | 31 m ; sans nom ; coule vers 271° ; ruisseau au 178° | 3.29 |
| T03 | 45.41630, 6.05584 | 2396 m / 125° | Chemin/Sentier | eau≤150m public vue (3/5) | 13 m ; sans nom ; coule vers 273° ; ruisseau au 2° | 3.26 |
| T04 | 45.41622, 6.05582 | 2400 m / 126° | Chemin/Sentier | eau≤150m public vue (3/5) | 22 m ; sans nom ; coule vers 273° ; ruisseau au 4° | 3.26 |
| T05 | 45.41512, 6.02803 | 1527 m / 188° | Chemin | trouée eau≤150m vue (3/5) | 83 m ; Ruisseau de la Perrière ; coule vers 293° ; ruisseau au 23° | 2.85 |
| T06 | 45.43103, 6.05345 | 1788 m / 82° | Chemin | eau≤150m vue (2/5) | 45 m ; Ruisseau de Tapon ; coule vers 338° ; ruisseau au 252° | 2.82 |
| T07 | 45.44758, 6.02674 | 2100 m / 351° | Chemin/Route empierrée | eau≤150m vue (2/5) | 7 m ; sans nom ; coule vers 217° ; ruisseau au 308° | 2.79 |
| T08 | 45.44766, 6.02656 | 2111 m / 351° | Chemin/Route empierrée | eau≤150m vue (2/5) | 8 m ; sans nom ; coule vers 217° ; ruisseau au 128° | 2.79 |
| T09 | 45.44922, 6.02885 | 2262 m / 356° | Chemin | eau≤150m vue (2/5) | 6 m ; sans nom ; coule vers 223° ; ruisseau au 313° | 2.77 |
| T10 | 45.43902, 6.00284 | 2458 m / 298° | Sentier | eau≤150m vue versant-E (3/5) | 145 m ; l'Isère ; coule vers 178° ; ruisseau au 87° | 2.75 |

**Lecture.** T05 (45.41512, 6.02803, Ruisseau de la Perrière, 1,5 km au sud) est la seule vraie trouée avec ruisseau nommé du top, avec vue théorique marginale (dégagement 7 m) ; le ruisseau coule vers l'ONO (293°) et passe à 23 m. Son versant regarde l'ouest, pas l'est. T10 a un versant est net (44 %) mais hors trouée et sur l'Isère. T01–T04 sont en forêt publique avec vue théorique (le relief seul ; la forêt gênera). **Aucun n'est retenu.** La direction d'écoulement est celle du tronçon BD TOPO au point le plus proche (sens de saisie corrigé si « Sens inverse »).

## 3. Toponymes (≤ 5,5 km ; distance et cap depuis la tour)

| Terme | Toponyme | Dist | Cap | Source |
|---|---|---|---|---|
| avalon | AVALON | 0.09 km | 24° | cadastre:Saint-Maximin |
| bayard | VERGER DE BAYARD | 1.06 km | 230° | cadastre:Pontcharra |
| bayard | château bayard | 1.10 km | 237° | BDTOPO:toponymie |
| bayard | CHATEAU BAYARD | 1.17 km | 238° | cadastre:Pontcharra |
| bayard | caserne bayard | 1.56 km | 302° | BDTOPO:toponymie |
| bayard | bayard | 1.62 km | 310° | BDTOPO:toponymie |
| bayard | BOIS BAYARD | 1.74 km | 266° | cadastre:Pontcharra |
| bayard | CHENEVIERE DE BAYARD | 2.04 km | 294° | cadastre:Pontcharra |
| bayard | la bayarde et lepinay | 2.54 km | 221° | BDTOPO:toponymie |
| bayard | A BAYARD | 4.51 km | 137° | cadastre:Allevard |
| chant | CHANTE-MERLE | 1.87 km | 59° | cadastre:Saint-Maximin |
| chant | chantabord | 2.54 km | 18° | BDTOPO:toponymie |
| chant | CHANTE MERLE | 5.00 km | 161° | cadastre:Crêts en Belledonne |
| clairière | le clairfait | 3.90 km | 193° | BDTOPO:toponymie |
| clairière | LA MATRE ET CLAIRFAIT | 3.92 km | 190° | cadastre:Pontcharra |
| clairière | BOIS DU CLAIRFAIT | 4.02 km | 185° | cadastre:Pontcharra |
| clairière | bois de clairfait | 4.17 km | 179° | BDTOPO:toponymie |
| clairière | clair matin | 5.22 km | 151° | BDTOPO:toponymie |
| fontaine | fontaine de la frace | 3.43 km | 86° | BDTOPO:toponymie |
| fontaine | les fontanettes | 4.09 km | 78° | BDTOPO:toponymie |
| fontaine | FONTAINE ANTREE | 4.51 km | 141° | cadastre:Allevard |
| fontaine | lotissement des fontanettes | 4.55 km | 205° | BDTOPO:toponymie |
| fontaine | FONTANIL | 5.13 km | 195° | cadastre:Crêts en Belledonne |
| fée | le fayet | 4.55 km | 256° | BDTOPO:toponymie |
| fée | château du fayet | 4.71 km | 255° | BDTOPO:toponymie |
| fée | bois du fayet | 5.20 km | 252° | BDTOPO:toponymie |
| loup | tire-loup | 1.60 km | 98° | BDTOPO:toponymie |
| loup | tire loup | 1.60 km | 98° | BDTOPO:toponymie |
| loup | tire loup et les taches | 1.60 km | 98° | BDTOPO:toponymie |
| rempart | LE CRET DU MUR | 2.56 km | 184° | cadastre:Pontcharra |
| rempart | MOLLARD BILLARD ET LES MURAILLES | 3.83 km | 133° | cadastre:Allevard |
| roche | LE CHENE LA ROCHE ET LE VIVIER | 0.13 km | 116° | cadastre:Saint-Maximin |
| roche | PRE CROCHET | 0.71 km | 285° | cadastre:Pontcharra |
| roche | le rochat | 1.40 km | 189° | BDTOPO:toponymie |
| roche | COTE ROCHAT | 2.21 km | 83° | cadastre:Saint-Maximin |
| roche | côte rochat | 2.46 km | 94° | BDTOPO:toponymie |
| roche | roche morte | 3.05 km | 206° | BDTOPO:toponymie |
| roche | maison de roche morte | 3.05 km | 206° | BDTOPO:toponymie |
| roche | LA ROCHE | 5.18 km | 164° | cadastre:Crêts en Belledonne |
| âne | ehpad le granier | 0.76 km | 336° | BDTOPO:toponymie |
| âne | h.l.m. granier | 4.80 km | 211° | BDTOPO:toponymie |
| âne | centre de secours de chapareillan-granier | 4.88 km | 321° | BDTOPO:toponymie |
| âne | BUGANIERE | 5.04 km | 106° | cadastre:La Chapelle-du-Bard |

Les ~52 « Fontaine » sans nom de `detail_hydrographique` ne sont pas listées : les plus proches sont à 0,91 km (166°), 0,92 km (204°), 1,11 km (358°), 1,15 km (87° et 264°). **Aucun** toponyme pour émeraude, diamant, ancre, étoile, lune, souche, charpentier, coupe, dame ; « Chante-Merle » (1,87 km, 59°) évoque « chant » ; « Le Cret du Mur » (2,56 km, 184°) et « Mollard Billard et les Murailles » (3,8 km, 132°) évoquent le rempart ; « Tire-Loup » (1,6 km, 98°) évoque le loup ; « Le Fayet » (4,55 km, 255°) n'a qu'une étymologie (hêtre), pas le sens de fée. Les noms « âne » sont des faux positifs (Granier, Buganière). **Test du hasard** : 3 067 noms dans 6,5 km ; « roche » ou « loup » y sont banals ; seul « Avalon » est indépendant (et déjà connu). Tire-Loup : HYPOTHÈSE faible.

## 4. Alternative : fort Barraux (45.4358, 5.98723 ; ~3,5 km cap 283° de la tour)

Rayon 1,5 km, 32 jonctions : trouée 0, eau 7, public 0, vue 5, versant est 5 ; eau+vue+est = 4. Meilleurs (aucun n'a la trouée) :

| # | Lat, Lon | Dist du fort | Nature | Filtres | Flux |
|---|---|---|---|---|---|
| F01 | 45.43813, 5.97173 | 1238 m / 282° | Chemin/Sentier | eau≤150m vue versant-E | ruisseau à 5 m, coule vers 97° |
| F02 | 45.43814, 5.97167 | 1243 m / 282° | Sentier | eau≤150m vue versant-E | ruisseau à 6 m, coule vers 102° |
| F03 | 45.43543, 5.97445 | 999 m / 268° | Chemin | eau≤150m vue versant-E | ruisseau à 129 m, coule vers 103° |
| F04 | 45.43671, 5.97364 | 1066 m / 275° | Chemin/Sentier | eau≤150m vue versant-E | ruisseau à 116 m, coule vers 101° |

Les 4 premiers sont sur le versant est de la montagne à l'ouest du fort (descente vers l'est, ruisseau à quelques mètres, vue théorique sur le relief). Cohérent avec « l'astre du matin sur le ruisseau », mais sans trouée dans la BD TOPO et hors forêt publique dans les données. **Non retenu, piste vivante.** Le fort est un monument historique : c'est le chemin de rempart, pas le lieu du coffre.

## 4b. Qu'est-ce qu'un « chemin de rempart » accessible toute l'année ? (Wikipedia fr, pages publiques)

- **FAIT** (fr.wikipedia « Tour d'Avalon ») : tour des chartreux de 1895 sur les bases du donjon de l'ancien château d'Avalon (avant 1049) ; inscrite MH le 05/10/1992. La page ne décrit **aucune muraille ni chemin de ronde**. Il n'y a donc pas, dans cette source, de « rempart » au sens strict à Avalon : au mieux le pied de la tour ou l'ancienne enceinte (non documentée ici).
- **FAIT** (« Château Bayard ») : propriété privée avec domaine viticole et musée dans deux salles ; ne satisfait pas « accès gratuit toute l'année » pour l'intérieur. Les abords (chemins extérieurs) restent à vérifier.
- **FAIT** (« Fort Barraux ») : enceinte, fossé, pavillon et chapelle protégés (inscrit 1988, classé 1990) ; propriété communale ; visites guidées de mai à septembre, salle louée pour événements. Le **chemin de ronde intérieur n'est donc pas accessible toute l'année** ; en revanche le fossé et les glacis extérieurs sont des chemins publics probables (**HYPOTHÈSE**, à vérifier).
- **Lecture des contraintes FAQ** (FAQ06-020 toute l'année ; FAQ06-025 le chemin de rempart n'est pas un des chemins de la jonction mais très proche ; FAQ07-268 point précis) : « chemin de rempart » = plutôt un **sentier longeant une muraille ou une enceinte, en libre accès**, qu'un chemin de ronde de monument payant. Critères à tester sur place : (1) un mur/enceinte ancienne visible ; (2) un chemin ouvert sans billet ; (3) une vue sur une trouée avec ruisseau. Confiance : moyenne (30 % que ce soit Avalon, 15 % Barraux, reste inconnu). Ces pourcentages sont des estimations, pas des mesures.
- Autres « murailles » IGN à moins de 5 km : « Le Cret du Mur » (2,56 km, 184°) et « Mollard Billard et les Murailles » (3,83 km, 133°, cadastre Allevard) : **pistes vivantes** pour un « rempart » non monumental, non testées en jonctions.

## À vérifier sur place ou ensuite
- La vraie clairière peut être absente de la BD TOPO (trouée < 30 m, sous-bois) : contrôler l'orthophoto IGN ou le LiDAR HD (MNH) pour chaque candidat, T05 d'abord.
- Visibilité réelle depuis la tour : refaire avec le MNS LiDAR (végétation et bâti), pas le MNT.
- Chercher sur place un ruisseau qui coule à gauche jusqu'à une roche qui bloque le passage (absent de BD TOPO).
- Domaine public : vérifier au cadastre parcellaire (non fait ici).
- Le chemin de rempart précis : FAQ06-025 dit qu'il n'est pas l'un des chemins de la jonction, mais très proche.
- L'arrière-plan de l'enluminure 9 (lac, muraille orange crénelée, butte à tour blanche) : à comparer avec des panoramas de la vallée.

## Fichiers
`T1_candidats.kml`, `T1_bassin_planche.png`, `T1_bassin_trace_controle.png`, `T1_bassin_scores.json`, `T1_tour_jonctions.json`, `T1_fort_jonctions.json`, `T1_toponymes.json`, `T1_*.out.txt`, `T1_notes.md`.
