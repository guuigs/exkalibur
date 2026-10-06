# É12 — Récapitulatif de la session autonome (04/10/2026)

## 1. Idée de Guilhem : la rayure (SVG) = le chemin de la tour au croisement final
- Structure de la rayure : un long tracé sinueux (longueur/corde = 1,62) qui finit sur un point où se rejoignent 3 traits (jonction), avec une courte « queue » qui repart.
- Test (`outils_scratch/t40_svg_route.py`) : 4 237 itinéraires réels sur les chemins BD TOPO, du pied de la tour à chaque croisement (300 m-4 km), comparés à la rayure (alignement des extrémités, puis écart moyen). Témoin : la rayure retournée en miroir.
- Résultat : meilleur score 0,046, miroir 0,045. Avec la sinuosité et la direction de la queue : réel 0,065, miroir 0,045. **Aucun signal**. L'itinéraire tour → Le Mouret est dans la moyenne (meilleur que 56 %).
- Limite : un chemin non cartographié pourrait échapper au test.

## 2. Méthode « terrain d'abord » (sans théorie sur les 3e et 11e)
- Visibilité complète depuis le pied (yeux à 1,7 m) et le sommet (+33 m) de la tour, LiDAR 1 m, arbres compris, en ignorant les 15 premiers mètres (`t40_viewshed_pied.py`).
- Crible de tous les croisements réels de la zone LiDAR (7 × 7 km) : maisons ≥ 100 m, au moins 30 m² de sol ouvert visible à 60 m, forêt ≥ 35 % autour (clairière), eau ≤ 150 m (BD TOPO ou talweg LiDAR) (`t40_terrain_first.py`).
- 117 croisements passent les deux premiers critères, 19 tous les critères, et **seulement 2 sont visibles depuis le PIED de la tour, tous les deux au MOURET** : la jonction de 4 chemins (45.422426, 6.040299 ; 411 m² visibles du pied) et la jonction 2 (45.42337, 6.041663 ; 52 m²).
- Cela recoupe, par une méthode indépendante, la table des apôtres « Christ à l'Orient » (place de Simon à 48 m de la jonction).
- Les autres sites (visibles seulement du sommet) : Le Rochat (Saint-Maximin, 1,4 km au sud, sur un chemin public), Laissaud (Le Mas de Coise, Coise, château Beauregard), Barraux (La Fournache), La Buissière, Le Cheylas, Pontcharra (écartée).

## 3. Le Mouret : ce qu'on sait maintenant
- Jonction de 4 chemins sur un chemin public (non cadastré). Le pré visible du pied de la tour commence à 39 m.
- **Un talweg LiDAR (bassin 2,5 ha) coule dans le chemin qui part vers l'est** : sur les 125 premiers mètres, il est à 1-7 m du chemin, presque toujours à GAUCHE en montant (chemin creux). On marche donc sur un chemin public, sur la rive gauche, l'eau à gauche, en montant dans la forêt. La tête du talweg est à 45.422555, 6.041822 (z 553 m).
- Le chemin de l'est continue jusqu'à 45.422164, 6.043982 (z 600 m, sur une bande publique) près du Rebouchet et de ses affleurements (rive gauche).
- Le sentier plat vers le nord-est mène à la jonction 2 (sous la ligne haute tension, couloir déboisé) ; affleurement de 48 m² haut de ~2 m à 25 m (45.423566, 6.041667) ; Rebouchet à 65 m.
- Deux sources (BD TOPO) à 74 et 162 m au sud.
- Soleil au sol : 8 h 40 le 30/04, 7 h 37 le 21/06.
- Faiblesses : le croisement est en lisière, sous les arbres ; terrains privés autour (seuls les chemins et une partie des ruisseaux sont publics) ; pente du chemin de l'est 22-35 % ; grande roche non identifiable au LiDAR (normal d'après FAQ07-126).

## 4. Loup : état
- Seule clairière visible du pied sur l'axe : un pré à 1 287 m (45.42773, 6.04751), sans croisement dedans ; les croisements voisins touchent le hameau des Ripellets (maisons à 9-26 m).
- Forêt communale de Pontcharra B0071 près de l'axe, longée par un ravin LiDAR de 1,4 km ; J5 privé et invisible du pied.
- Conclusion : le loup ne passe pas le crible « terrain d'abord ».

## 5. À faire (Guilhem)
- Regarder les photos en ligne (Google Maps, photos de randonneurs) du chemin qui monte vers l'est depuis la jonction du Mouret, et de la jonction 2 (affleurement).
- Décider la lecture finale de « à senestre » au Mouret : chemin creux de l'est (eau à gauche) ou sentier vers la jonction 2 et le Rebouchet.
- Préparer la soumission : capture vue du ciel de la clairière et de la jonction, avec un paragraphe sur le parcours (FAQ07-078).
Images : `images_travail/t40_mouret_synthese.jpg`.

## 6. Session de 30 min (04/10, 06:47-07:17) — travail actif
**Robustesse de la table « Christ à l'Orient »** : avec 12 places, Simon tombe à 37-77 m de la jonction du Mouret quel que soit le centre (sommet, pied, Rue du Rempart) et le rayon (1 057-1 079 m). Avec 13 places (le Christ a sa place) : 150-190 m.
**Visibilité depuis le pied** : 15 des 32 points du mur au pied de la tour (tout le côté est) voient la clairière ; le relief ne cache la jonction depuis aucun point.
**Cohérences de la table** : on « marche surtout sur l'une des deux » (06-247) : on marche à la place 11 (Le Mouret, forêt) et pas à la 3 (Pontcharra) ; écharde possible au 11e (bois, forêt), pas à la 3e (ville) ; la « 13e place » serait celle du Christ, à l'est (90°), sur l'axe du loup : « ne vous mènerait pas au bon endroit » (06-133).
**Critères bruts de la grande roche** (FAQ) : « très difficile à manquer » (03-211) ; mouillée (FAQ8) ; « vous bloquera vraiment le passage », aller au-delà le long du ruisseau « supposerait de quitter votre route » (06-195, FAQ8) ; pieds mouillés possibles avant la roche, pas après (06-090) ; on la touche difficilement sans se mouiller (06-180) ; depuis la souche on ne la voit plus (06-167) ; une seule étape entre la roche et la souche (07-182) ; une fois la jonction trouvée, le coffre est « tout près » (05-051).
**Balayage des culs-de-sac au bord de l'eau** (`t41_deadend_rock.py`, 39 sur toute la zone) : les plus rocheux sont sur le versant de Bramefarine (2-3,4 km, cap 132-172°), dont deux sur le **Rebouchet amont, dans la forêt communale de Pontcharra** (A : 45.414182, 6.051137, escarpement de 207 m² ; B : 45.416809, 6.049903, à une confluence, en limite de la forêt communale). Depuis la jonction du Mouret : 1,16-1,85 km par les chemins, rive gauche sur 900 m puis traversée du ruisseau. Trop loin pour « tout près » ; aucune jonction visible de la tour sur ces chemins. Image : `images_travail/t41_rebouchet_amont_culs_de_sac.jpg`.
**Points de fouille au Mouret** (`t41_dig_public.py`), roche + 10 pas N + 10 pas E (souche) + 8 pas vers 90° / 67,6° / 72,4°, pas de 0,75 ou 1,48 m :
- rocher de 4 m (45.421452, 6.045319 ; 107 m² ; au bord du Rebouchet, rive droite, ~410 m de la jonction, 131 m au-dessus du bout du chemin de l'est) : fouille vers 45.42151-45.42162, 6.04549-6.04567, en bordure ou dans la bande publique du Rebouchet, maisons à 167-183 m ;
- affleurement de 48 m² (45.423697, 6.041412 ; rive gauche, à 25 m de la jonction 2) : fouille vers 45.42376-45.42386, 6.04159-6.04177, à 0-4 m de la bande publique, maisons à 136-152 m.
**Jonction 2** : sous les arbres (0 % ouvert à 40 m) : pas une clairière. **Le Rochat** (vallon de La Perrière, ruisseau permanent, sur le sentier « Sur les traces du chevalier Bayard » qui part de la tour d'Avalon) : visible seulement du sommet ; petites roches. **Champ-Laurier** (carrefour du sentier Bayard, où tombe le vecteur gourde → scie) : invisible de la tour.
**Sensibilité du crible « terrain d'abord »** : maisons ≥ 60-150 m, forêt autour ≥ 0,30-0,45, eau ≤ 100-200 m, surface visible du pied ≥ 10-30 m². Pour **toutes** les combinaisons, il ne reste que la paire du Mouret. Sans le critère « clairière », s'ajoutent seulement des croisements agricoles sur l'axe du loup (756-815 m de la tour, source captée à 6 m, église à 240 m) : ce sont des champs, pas des clairières → écartés.
**Ordre de vue (enl. 9)** : depuis le Mouret, la tour (315°), l'étang (324°) et l'église (343°) apparaissent de gauche à droite, comme à l'arrière-plan de l'enluminure 9. Indice qualitatif faible (les arbres masquent la vue).
**Roche C** (ressaut de 5,6 m dans le lit, 45.424003, 6.041837, 212 m de la jonction) : à 0,5 m de la bande publique. Points de fouille (`t42_dig_rocheC.py`) vers 45.42406-45.42416, 6.04201-6.04218 : un seul est public (pas de 0,75 m, cap 90°), les autres sont à 0,3-3,4 m dans le privé. **Maisons à 95-110 m** : la plus proche des habitations des trois roches → affaiblie (« éloigné de tout bâtiment », 05-107).
**Ressauts du lit (cascade + vasque, enl. 9)** (`t42_ressauts.py`, pente du lit sur ~10 m, cours d'eau à plus de 1,2 ha drainés, 700 m autour de la jonction) : le ressaut **le plus raide de toute la zone** (10,3 m de chute sur ~10 m, Rebouchet principal) est en 45.421340, 6.045389, **à 13 m du rocher A**, maisons à 153 m. Le rocher de 4 m est donc au pied ou au bord de la principale cascade du Rebouchet, ce qui colle avec l'enl. 9 (petite chute dans une vasque au pied d'un rocher). C'est un renfort net pour A.
**Point faible de A** : ~410 m de la jonction, alors que le coffre est « tout près » une fois la jonction trouvée (05-051). C'est relatif : on reste à quelques minutes de marche, alors que l'amont du Rebouchet est à 1,2-1,8 km.
**Classement des roches au Mouret** : A (cascade, 4 m, loin des maisons, bord de bande publique) > B (affleurement près de la jonction 2, sans cascade repérée) > C (près des maisons, fouille privée).
**⚠️ Critère fauteuil (FAQ03-112 : « Le coffre est-il accessible […] en fauteuil roulant ? — Oui. Je conseille à cette personne de se faire accompagner néanmoins. »)** (`t42_pente_fouille.py`, pente médiane sur 7 × 7 m) : fouille A 22° (40 %), fouille B 46° (100 %), fouille C 26° (50 %), rocher A 49°. Jonction → A : +56 m sur 407 m dans un ravin à cascade. **Aucune des trois roches n'est compatible avec un fauteuil, même accompagné.** C'est l'objection la plus forte contre la fin de parcours « chemin de l'est → Rebouchet ». Elle ne touche pas forcément la jonction elle-même.
**Zones plates (< 8°) au bord de l'eau près de la jonction** (`t42_plat_mouret.py`, maisons ≥ 100 m) : 45.422482, 6.039049 (98 m à l'ouest de la jonction, 64 m², eau à 0 m, à 1,2 m de la bande publique, maisons à 103 m) ; 45.423089, 6.039586 (92 m, 3 130 m², le fond humide du pré, privé) ; 45.423909, 6.037753 (258 m, sur la bande publique, maisons à 128 m). Elles sont toutes **en aval** (vers l'ouest et les maisons), pas en amont.
**Conséquence à trancher** : soit l'auteur entend « accessible » au sens large (le chemin, pas le point exact), et A reste en tête ; soit on prend FAQ03-112 au pied de la lettre, et la roche doit être en aval, sur terrain plat (descendre « à senestre les eaux » vers l'ouest). Cela demande de rechercher une roche sur ce tronçon aval (photos en ligne, pas visible au LiDAR).
**⚠️ Correction (07:05) : visibilité de la jonction elle-même** (`t42_aval.py`, viewshed du pied, sursol LiDAR) : le **point** de jonction du Mouret n'est pas vu ; la cellule visible la plus proche est à **41 m**. Surface visible autour : 0 m² dans un rayon de 40 m, 150 m² à 50 m, 480 m² à 60 m, 2 131 m² à 80 m. Les « 411 m² visibles » d'avant mesuraient donc le pré voisin, pas le croisement. Ce qu'on voit du pied, c'est le **pré à l'ouest de la jonction** (autour de 45.422482, 6.039049 : 475 m² visibles à 20 m, chemin à 6 m, eau à 0 m, terrain plat). Aucun des croisements voisins n'est lui-même visible (jonction OSM+BDT 45.422478, 6.038256 : 9 m² visibles à ±15 m, maisons à 58 m).
Lecture possible : la clairière (le pré) est vue du rempart et la jonction est à sa lisière est, sous les arbres (FAQ : la jonction peut être « un peu plus loin »). Mais si FAQ05-165/06-230 exigent que le point lui-même soit dans le champ de vision, Le Mouret s'affaiblit. Le viewshed LiDAR est pessimiste en lisière (houppiers) : à vérifier avec des photos prises depuis le rempart.
**Crible strict « le point du croisement est vu du pied »** (`t42_strict.py`, ≥ 20 m² vus à ±10 m, toute la zone 7 × 7 km, à plus de 300 m de la tour) : seulement **11 croisements** dans toute la zone. Dix sont dans le centre du village (mairie, école, église, parc, terrain de sport ; maisons à 8-40 m) ou au hameau des Ripellets (45.427623, 6.040649, maisons à 84 m, forêt 0,24). Le onzième est à 3,8 km. **Aucun n'est à la fois une clairière en forêt et loin des maisons.** Même depuis le sommet de la tour (+33 m), le point de jonction du Mouret est caché ; la cellule vue la plus proche est à 41 m, et la ligne de visée passe environ 15 m sous la canopée.
**Conclusion structurelle** : si l'on exige que le point exact du croisement soit vu (sans arbres), le problème n'a **pas de solution** autour de la tour. La lecture « la clairière est dans le champ de vision, le croisement est à sa lisière » est donc forcée par le terrain. Elle n'est pas un défaut propre au Mouret, ce qui remonte un peu Le Mouret après la correction de 07:05. L'auteur a pu aussi raisonner sans les arbres, au relief seul (« champ de vision » au sens large).
**Eau vers l'aval depuis la jonction** (`t42_aval_flow.py`, talweg D8, point tous les 20 m) :
- 0-45 m : pente 18-23° ;
- 65-153 m : **le pré visible du pied** (pente 5-8°, 115-121 m² vus à ±5 m), mais à 59-90 m de tout chemin, maisons à 76-117 m, aucune saillie > 1 m ;
- 175-344 m : pente 7-13°, plus rien de visible, chemin à 14-40 m ;
- 365-447 m : ravin (pente 25-34°), saillie de 3 m en 45.424192, 6.036588 (maisons à 132 m, chemin à 27 m), pas praticable en fauteuil ;
- au-delà de 470 m : maisons.

**Bilan fauteuil** : ni l'amont (A, B, C) ni l'aval n'offrent au Mouret une grande roche au bord de l'eau sur terrain praticable en fauteuil. Soit FAQ03-112 désigne une accessibilité générale (un accompagnateur aide sur un sentier), soit Le Mouret n'est pas le bon lieu. **C'est désormais le point de doute n° 1 de la piste.**
**Calibrage par la FAQ brute de la difficulté physique** :
- FAQ04-198 : les phénomènes climatiques **peuvent empêcher** d'accéder au coffre, mais le lieu n'est « pas dangereux », il est « accessible ». C'est compatible avec un bord de ruisseau qui déborde (Rebouchet, roche mouillée), moins avec un parc plat de village.
- FAQ07-210 : escalader des rochers est inutile.
- FAQ03-112 : fauteuil « oui », mais « se faire accompagner néanmoins ». Le « néanmoins » admet une difficulté réelle (sentier, pente), pas une marche lisse.

Lecture retenue (à valider par Guilhem) : « accessible » au sens d'un chemin praticable avec aide, pas d'un terrain plat au point de fouille. Le rocher A, au bord d'une cascade dans un ravin à 40 % de pente, reste à la limite de cette lecture ; c'est le doute n° 1.
**Axe narrateur (château Bayard → tour d'Avalon)** : cap 58,4° sur 1 140 m ; prolongé de 1 068 m, il tombe en 45.433904, 6.04264, et de 1 850 m en 45.437588, 6.051155, côté plaine de Pontcharra (abandonnée d'office). Il ne passe pas par Le Mouret (cap 134,6° depuis la tour). Le Mouret est en revanche **plein est du château Bayard** (94,0° ; rocher A : 96,2°). Coïncidence probable, sans valeur de preuve : on le note, on ne l'utilise pas.
**Accès à la cascade / rocher A** : un chemin (BD TOPO) et un sentier (OSM) passent à **35-45 m à l'est**, avec deux croisements de 3 branches (45.421309, 6.045840 et 45.421552, 6.045886), sous couvert total, invisibles de la tour. Mais ils sont **21-25 m plus haut** que la cascade (pente moyenne de descente 47-57 %). On atteint le rocher depuis un chemin, mais par une descente raide dans le ravin. C'est confirmé : pas praticable en fauteuil, même accompagné, sauf lecture très large de FAQ03-112.
**Crible « clairière visible + plat » sur toute la zone** (`t42_plat_clairiere.py`, ≥ 30 m² de terrain ouvert vu du pied à 60 m, pente ≤ 12° au croisement, maisons ≥ 100 m, forêt autour ≥ 0,30, eau ≤ 200 m) : **0 résultat**. En assouplissant (maisons ≥ 60 m, forêt ≥ 0,20, pente ≤ 15°), il en reste 3 :
- 45.426664, 6.033741, à 318 m de la tour, maisons à 96 m, forêt 0,21 ;
- deux croisements agricoles des Ripellets (déjà écartés).

Hors critère de forêt, on trouve un croisement plat à 3,2 km au nord (45.457067, 6.024503, en plein champ). **Conclusion** : sur la zone, « clairière en forêt » et « terrain plat praticable en fauteuil » ne se rencontrent jamais. Une des deux lectures doit être assouplie. On garde « clairière » (texte brut de l'énigme) et une lecture large de FAQ03-112 (« se faire accompagner néanmoins »).
Croisement plat restant à 318 m (45.426664, 6.033741) : écarté (voir registre).
**Fin de la session de 30 min (≈ 07:13)**.
**⚠️ Permanence de l'eau (07:11)** : la BD TOPO classe le Rebouchet **intermittent** au droit des roches A (12 m), B (32 m) et C (5 m). Il n'est **permanent** qu'en aval, de 45.421821, 6.026100 à 45.420135, 6.018686, à 1,1 km de la jonction du Mouret, vers Pontcharra. Or la FAQ parle d'une roche mouillée (FAQ8 « oui »), qu'on touche « difficilement » sans se mouiller (06-180), et l'enl. 9 montre deux poissons dans la vasque. Cela suggère une eau permanente. La classification « intermittent » de la BD TOPO est souvent prudente pour les petits ruisseaux de montagne (une cascade de 10 m est rarement sèche), mais c'est un **nouveau point faible** de la piste. Cours d'eau permanents à moins de 2,5 km de la tour : le Bréda (495 m), le Rebouchet aval (765 m), le ruisseau de la Perrière (1 121 m, vallon du Rochat), le Papet (1 745 m), le Coisetan (2 060 m), l'Isère (2 158 m).
**Croisements au bord d'une eau PERMANENTE (≤ 40 m), maisons ≥ 100 m** (Perrière, Rebouchet aval, Papet, Coisetan) : 15 sur la zone, **aucun visible du pied de la tour**. En réserve, si la règle « vu du pied » devait un jour être assouplie au sommet, il reste un groupe au **nord, à 2,1-2,3 km** (45.447584, 6.026721 ; 45.447665, 6.026558 ; 45.449243, 6.028899). Ce groupe est en terrain ouvert (0,42-0,63), à 7-9 m d'une eau permanente, avec des maisons à 128-367 m, et 2 700-4 200 m² sont vus du sommet. Il n'a aucun lien connu avec la table des apôtres (à vérifier seulement si la règle change).
**Fin de la session active (07:12)**.

## 7. Décisions du 04/10 (après la session) et recherches en ligne faites par Claude
**Décisions de Guilhem** : (1) plus aucune demande de photos ; Claude cherche lui-même ou accepte l'inconnu. Les « À faire (Guilhem) » de la section 5 sont caducs. (2) Fauteuil (FAQ03-112) au **sens large** : un sentier praticable avec un accompagnateur suffit, ce n'est plus un critère d'élimination.
**Imagerie de rue** : Panoramax ne contient aucune image autour du Mouret (bbox 6.039-6.047 / 45.4205-45.4245). Mapillary demande un jeton d'accès, donc pas d'accès. → Inconnu accepté : l'aspect réel de la roche et de la cascade ne se voit pas en ligne. C'est conforme à FAQ07-126 (la roche ne se voit pas forcément en ligne).
**Recherche web** :
- La fiche IRMA (risques naturels de l'Isère, Dossier communal synthétique) signale une « crue des ruisseaux de Tapon, de Burge, du Rechouchet [Rebouchet] et de la Perrière : débordements fréquents au niveau de la route forestière qui contourne la montagne de Bramefarine », avec une fréquence « régulièrement ». Le Rebouchet amont est donc un torrent actif.
- La route forestière (« Route empierrée » BD TOPO) croise le Rebouchet en 45.418542, 6.048698, à 404 m en amont du rocher A et à 786 m de la jonction.
- Le parcours thématique communal (9 étapes : tour d'Avalon, oratoire, Rippelets, Crêt, Bruns, Répidon, église, forge, Vivier) ne mentionne ni Le Mouret ni le Rebouchet.

**Permanence de l'eau, verdict** : la BD TOPO classe aussi « intermittent » des tronçons du Rebouchet en plein village, et « permanent » seulement le dernier kilomètre. C'est donc une classification prudente, pas une observation de lit sec. Le bassin versant est d'environ 10 ha au rocher A, donc des étiages d'été restent possibles. → **Inconnu accepté**, sans effet sur le classement.
**Classement** : Le Mouret, rocher A ~20 % (le fauteuil n'élimine plus) ; loup ~5 %.
Sources : https://www.irma-grenoble.com/04risques_isere/00commune_evenements_fiche.php?id_evenements=1051 ; https://www.alpes-isere.com/en/sit/parcours-thematique-saint-maximin-4704227/ ; https://api.panoramax.xyz/

## 8. Autres options sous contrainte de distance (04/10, demande de Guilhem)
Contraintes de distance de la FAQ, relues mot pour mot :
- 06-244 : le coffre n'est pas loin du chemin de rempart.
- 06-025 : les chemins de la jonction ne sont pas le chemin de rempart, « même s'ils sont très proches ».
- 05-051 : une fois la jonction trouvée, on est « tout près » du coffre à vol d'oiseau.
- 06-134 : des joueurs « passent proche, avant de quitter la zone pour une autre zone ».
- 06-166 : le rempart est le point de départ ; « c'est l'astre glorieux qui vous indique où aller », et c'est là que les 3e/11e servent.

**Option V — le Vivier et le pied de la tour (≤ 700 m)** (`t43_proche.py`, `t43_carte_sud.py`, `t43_vivier.py`, `t43_exutoire.py`) :
- 106 croisements à 700 m ou moins. Ceux qui sont vus du pied sont dans le bourg (maisons à 15-28 m) ou dans le centre du village.
- Le Vivier (étang de 1261, ancienne douve de l'enceinte, 10 372 m²) se vide par son angle NE (45.429055, 6.033901), juste à côté du carrefour « Le Vivier ». L'eau part ensuite vers le nord le long d'un chemin, puis plonge dans un ravin jusqu'au Bréda. **Rien n'est visible du pied** ; tout est bâti à moins de 60 m.
- Il y a bien une tache visible au sud du Vivier (839 m², 45.427198, 6.033121, maisons à 172 m), mais c'est une bande de prairie entre des haies, sans ruisseau. Pas une clairière.
- → écartée.

**Option R — « le ruisseau magnifié » vu du rempart** (`t43_ruisseau_vu.py`, `t43_rebouchet_pont.py`, image `images_travail/t43_pont_rebouchet.jpg`) :
- Depuis le pied de la tour, **un seul tronçon de cours d'eau est visible** : le Rebouchet, au cap 115-120°, à environ 600 m (45.426236, 6.038836). C'est la lecture littérale de « l'endroit m'est apparu au matin, illuminé par l'astre glorieux qui magnifiait le ruisseau ». Un lever de soleil d'hiver (azimut ~120°) serait aligné avec ce tronçon.
- Au même endroit, un croisement route + sentier au pont (45.426344, 6.038290, à 625 m du pied ; 104-135 m² vus à ±10 m, 20-40 m en amont).
- Le sentier longe le Rebouchet vers l'amont, **l'eau à GAUCHE en montant** sur 380 m (à 3-13 m de l'eau), puis entre en forêt après 60 m.
- À 376 m du pont, le lit a un ressaut de 4,7 m (pente 64 %, en 45.423957, 6.041700, maisons à 137-155 m) qui ouvre une gorge raide. Le sentier quitte alors l'eau et monte à la jonction 2 du Mouret (45.423370, 6.041663). C'est la même zone que la roche C.
- **Points forts** : cohérence avec le texte (ruisseau vu du rempart, jonction au ruisseau, suivre les eaux en les gardant à senestre, roche qui bloque) ; plus près de la tour que Le Mouret (625 m au lieu de 1 012 m).
- **Points faibles** :
  - la jonction est en bordure de hameau (maisons à 13 m) ; la « clairière » se réduit à un petit pré de hameau ;
  - la roche est à 376 m de la jonction (« tout près » discutable) ;
  - « à senestre » est lu ici comme « l'eau à ma gauche » ; c'est **l'inverse de la lecture retenue par Guilhem le 03/10** (« je suis sur la rive gauche »), à trancher par lui ;
  - le lien avec les 3e/11e (table des apôtres) n'est pas direct : Simon est au Mouret, à 400 m au SE.

**Crible global « roche à ≤ 150 m de la jonction »** (`t43_crible_proche.py`) : 23 croisements. Mais le critère « chute ≥ 4 m sur 10 m » capte toutes les ravines raides. Le meilleur cas (45.421557, 6.040743, à 103 m de la jonction du Mouret) est une ravine à 50 % de pente, avec une saillie de seulement 1,8 m, pas une roche isolée. → **non concluant** ; il faudrait un vrai détecteur de blocs (rugosité locale), à faire.
**Décision de Guilhem (04/10)** : les **deux lectures** de « à senestre » sont acceptées (je suis sur la rive gauche / l'eau est à ma gauche). L'option R reste donc valide, au même titre que Le Mouret.
**Points de fouille, option R** (`t44_dig.py 45.423957 6.041700`) : le ressaut est sur la bande publique. Fouille en 45.42402-45.42412, 6.04187-6.04205 ; un cas est public (pas de 1,48 m, cap 90° → 45.424077, 6.042047), les autres sont à 1-3 m de la bande publique ; maisons à 106-121 m.
