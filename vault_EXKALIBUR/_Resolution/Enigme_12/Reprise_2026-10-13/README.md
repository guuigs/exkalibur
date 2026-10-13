---
tags:
  - "#exkalibur"
---
# É12 : reprise à zéro (13/10/2026)

> **Statut : 🟡 avancée sur la clé, 🔴 pas de pile-poil.**
> Le premier paragraphe est décodé avec une bonne confiance : « Dieu sut se montrer favorable » renvoie au *Roman de la Rose* (trad. Marteau). Les « troisième et onzième » seraient ses **chapitres III (la porte du verger) et XI (la fontaine de Narcisse sous le pin)**.
> Il reste à fixer la direction donnée par « l'astre glorieux » et le rôle de l'épée. Aucune zone de 50 m n'est défendable à ce stade.
> Méthode : je repars des textes, des enluminures et des 1 852 réponses de l'auteur (+ FAQ8), sans reprendre les pistes de `../solution.md`.

## 0. Quelqu'un a-t-il trouvé ? (fait, 13/10/2026)
- **Aucune trace publique d'un coffre trouvé ni d'une solution publiée.** Sources : unsolvedhunts.com (pages *Exkalibur* et *Validation*), puydufou.com, presse, BlackTiger, chasses-au-tresor.com.
- Dernier état donné par l'auteur (FAQ8, 04/06/2026) : 3 équipes « à moins de 150 m du coffre », **aucun pile-poil exact**, découverte jugée « possible dans les prochains mois ». Plus de 20 joueurs ont trouvé les remparts.
- Non consultés : les FAQ postérieures à la FAQ8 et le Discord (hors périmètre).
- ⚠️ **Le dépôt `guuigs/exkalibur` est public** (vérifié par l'API GitHub) et indexé par les moteurs de recherche : une recherche « Exkalibur Saint-Maximin tour d'Avalon » le fait remonter.

## 1. Fait : la première phrase est un vers du *Roman de la Rose* (Marteau, chap. XI)
- *Le Roman de la Rose*, Guillaume de Lorris, traduction en vers de **Pierre Marteau** (1878), tome I, **Gutenberg n° 16816** (texte en ligne, gratuit : c'est le type de source que l'auteur dit utiliser, FAQ8).
- Chapitre **XI**, « L'Auteur ici Narcisse conte » (v. 1487), p. 99 :
  > « A sa prière raisonnable, / **Dieu sut se montrer favorable** / Et voulut que Narcisse un jour / S'en vint justement, de retour / De la chasse, vers cette source, / […] Chercher l'ombre sous le grand pin. / Par monts, par vaux, dès le matin, […] / Il vit sous l'arbre protecteur / La source vive et transparente. / […] Il se pencha sur le ruisseau. »
- **Deuxième emprunt au même livre, dans l'É7** (*Sub rosa*). L'énigme dit « Mais non, le trait qui l'a percé, goutte de sang n'avait versé ». Le chapitre XIII (p. 115) dit : « **Mais non, le trait qui m'a percé / Goutte de sang n'avait versé** ». Ce sont 8 mots consécutifs identiques. Un balayage des 12 énigmes sur le tome I ne trouve aucun autre emprunt long. Les seules suites de 4 mots communes en dehors de l'É7 et de l'É12 sont banales (« il y a deux », « jusqu'à ce que ») ; à 6 mots, il ne reste que l'É7 (`scripts/emprunts_rdlr.py` + `.out.txt`).
- ⇒ L'auteur travaille avec **cette édition précise**. Ce point n'est plus une hypothèse.
- Rubriques utiles de l'édition : chap. **III** « Comment dame Oyseuse fit tant / Qu'elle ouvrit la porte à l'amant » (v. 533) ; chap. **XI** « L'Auteur ici Narcisse conte » (v. 1487) ; chap. **XIII** « … perce l'Amant, / Dans le verger près de la Rose » (v. 1741).
- Texte de référence archivé : `sources/roman_de_la_rose_marteau_ch01-14.txt` (version moderne, chap. I à XIV).

## 2. Hypothèse forte : « les troisième et onzième » = chapitres III et XI de ce Roman
« dix stades **romains** » : jeu probable sur le *Roman*. Le chapitre III est la **porte du verger** qu'Oyseuse ouvre. Le chapitre XI est la **fontaine de Narcisse sous le pin**, là où se trouve justement le vers « Dieu sut se montrer favorable ».

Contrôle contre toutes les réponses de l'auteur sur les 3e/11e (aucune ne contredit) :

| Réponse de l'auteur | Lecture chapitres III / XI |
|---|---|
| Même nature (FAQ06-009), un seul de chaque (06-216) | deux chapitres du même livre |
| « Directement de la 3e à la 11e, mais vous passerez par des étapes intermédiaires » (04-115) | chap. IV à X : la carole, Amour qui suit l'amant, le verger, ses arbres et ses fontaines |
| « Le **treizième** ne vous mènerait pas au bon endroit » (06-133) | chap. XIII : le **rosier**, déjà utilisé pour l'É7 *Sub rosa* (citation ci-dessus) |
| « 8e et 16e : ce serait incorrect » (FAQ8) | autres chapitres, autres lieux |
| Pas visibles sur Maps ; « vous n'avez pas encore identifié ce qu'ils peuvent être » (06-227) | ce ne sont pas des objets, mais deux scènes à poser sur le terrain |
| Deux points à pointer sur la carte (05-074, 07-063) | la porte et la fontaine |
| Visibles sur les enluminures ? « C'est l'une des clés » (05-093) | **enl. 12** : porte gothique ouverte, escalier, paysage au soleil. **enl. 9** : rocher, cascade, bassin aux **deux** poissons (les deux cristaux du fond de la fontaine ?), coupe rayonnante |
| Pieds nus : pas d'écharde sur la 3e, possible sur le 11e (07-068) | seuil ou rempart de pierre, contre sous-bois et pin |
| Il faut marcher « surtout sur l'une des deux » (06-247) | on va à la fontaine, la porte n'est qu'un repère |
| Ils ne mènent à aucun chevalier (07-065), ni aux couleurs (07-244), pas un ensemble de 52 (07-156) | ✓ |
| « L'ultime traversée vous conduit à l'endroit où vos 3e et 11e prendront tout leur sens » (05-196) | l'arrivée est un **rempart** ; le verger du Roman est « clos d'un haut **mur crénelé** » qu'on longe pour trouver la porte |
| Trouvables de chez soi (04-114) ; difficiles (06-292) ; nature identifiée par un joueur (06-259) | ✓ (il faut trouver le vers) |
| « Dieu sut se montrer favorable » : « la décrypter, non, mais cette phrase est importante, il faut comprendre en quoi elle peut vous être utile » (FAQ8) ; « confirmateur de la zone finale » (07-088) | le vers ne se décrypte pas : il désigne le livre et le chapitre XI, donc la fontaine finale |

Confiance : **moyenne à haute** sur « Roman de la Rose = la clé ». **Moyenne** sur « 3e/11e = chapitres III/XI », qui est la lecture la plus simple compatible avec toute la FAQ.

## 3. Le parallèle texte de l'É12 / *Roman de la Rose* (lecture)
| É12 | Marteau |
|---|---|
| « J'entends le chant retentir » (lui seul l'entend, FAQ03-184) | chant des oiseaux du songe (chap. I à III) ; c'est un songe |
| « dernière veille… l'endroit m'est apparu au matin » | « Une nuit… je songeai qu'il était matin » (chap. I), un matin de **mai** |
| « l'astre glorieux qui magnifiait le ruisseau » | « Lorsque le soleil, qui tout guette, / Ses rais en la fontaine jette… On voit de couleurs plus de cent » (chap. XII) ; « un grand ruisseau coulait » (chap. I) |
| « chemin de rempart » | « verger immense / Tout clos d'un haut mur crénelé », qu'on contourne jusqu'à la porte (chap. II-III) |
| « laissé son épée aux portes d'Avalon » | Avalon = « la pommeraie » = le **verger**, dont la porte est le chap. III |
| « clairière… eaux enchantées… grande roche » | « En un lieu charmant j'arrivai… Une fontaine… Là, dans un blanc bassin de marbre… Sur la pierre, je vis écrites… lettres petites » (chap. X) |
| « souche-majesté » | « A l'ombre d'un pin gigantesque. / Depuis Karles, fils de Pepin, / Jamais on ne vit si beau pin » (chap. X) |

## 4. Conséquence sur le terrain (hypothèse de travail)
**Modèle** : le départ est la porte (3e), au rempart. La fontaine (11e) est à **1 850 m ± 18 m**. La direction vient du soleil du matin (« au matin… illuminé par l'astre glorieux », FAQ06-166, 07-133 : « une fois la direction de l'astre glorieux identifiée, les 3e/11e permettent directement d'identifier la clairière »).

- **Départ** : sommet de la **tour d'Avalon** (45.429083, 6.030808). Fait : la tour fait 33 m, on y monte par un escalier en chêne restauré, et le panorama « est exceptionnel » (programme Maisons Paysannes de France, 21/10/2023). Cela colle avec FAQ05-155 (« étant moi-même monté sur ce chemin de rempart ») et FAQ8 (« le chemin d'un mur ou d'une tour »). La Rue du Rempart (82 m) ou le château Bayard décalent l'anneau de 0,1 à 1 km.
- **Ruisseaux qui coupent l'anneau de 1 850 m ± 1 %** (BD TOPO, `scripts/ring.out.txt`) : **Bréda à 56°**, Tapon à 89°, Rebouchet à 130°, Perrière à 160°, ruisseaux sans nom à 164-165°, Papet à 197-207°, Rebouchet aval à 233°, canal à 240°, Bréda aval à 306°.
- **Soleil d'un matin de mai** (le songe du Roman) : 57 à 68° sur horizon plat, 64 à 79° quand le soleil passe la crête (5 à 10°) (`scripts/soleil_mai.out.txt`). Depuis la tour, cet axe **remonte les gorges du Bréda**. C'est aussi, à 1° près, le cap de la droite Saint-Palais → Bayard → tour de l'É11.
- **Secteur prioritaire** : cap 55-64° à 1 850 m, soit la traversée boisée du Bréda et le talus au sud (≈ 45.4382-45.4395 N, 6.0496-6.0520 E). Au-delà de 65°, ce sont des prés et des hameaux, exclus par FAQ05-107 (coffre loin de tout bâtiment). Images : `images/lidar_anneau_1850m_tour.jpg`, `images/lidar_breda_cap55-70.jpg`, `images/ortho_breda_cap50-90.jpg`.
- **Confiance sur ce secteur : faible**, de l'ordre de 10 %. La direction du soleil est un choix (mai, lever). L'auteur dit lui-même ne pas parler de « direction en tant que telle » (07-132). Aucun contrôle au hasard n'est encore fait sur ce secteur.

## 5. Ce qui reste ouvert
1. **L'épée, « dernière clé »** : elle sert avant l'astre (« l'astre glorieux vous guide en tout dernier lieu », FAQ8). L'épée réelle est publique et « fait partie intégrante du jeu ». Elle porte une rose des vents sur le pommeau ; la fissure de la lame dessinée « donne un élément ». Non décodée. « Tombée par trois fois… revenue là où elle n'avait jamais cessé d'être » : Bedivere et la Dame du Lac ? le rocher de l'É1 ?
2. **La position exacte de la porte (3e)**. Deux options : la porte est au rempart lui-même, ou bien ce sont les « portes d'Avalon » réelles, celles du bourg médiéval fortifié dont une maquette est exposée dans la chapelle de la tour.
3. **« Jour dernier »** (8 derniers pas). Fait : la boussole de la carte est graduée **I à VIII** dans le sens horaire (I = N, III = E, VII = O, VIII = NO). L'auteur ne dit pas si elle sert (FAQ8).
4. **Le ciel de l'enl. 9** (loup + glyphe, étoile, arc-en-ciel, âne + émeraude, diamant + ancre) : à décoder « une fois la zone trouvée » (FAQ06-067). Il pourrait donner le nom du ruisseau ou de la clairière.

## 6. Prochaines actions proposées
1. **Rendre le dépôt privé** avant d'y pousser ce dossier : décision de Guilhem.
2. Sur le terrain ou en images fines : la traversée du Bréda à 1 850 m de la tour (cap 55-64°). Chercher une jonction de sentiers dans une clairière, un ruisseau à suivre en le gardant à gauche, et une grande roche mouillée qui barre le passage.
3. Refaire l'anneau depuis la Rue du Rempart et le château Bayard. Ajouter un **témoin au hasard** : à quelle fréquence un anneau de 1 850 m coupe-t-il un ruisseau en forêt avec une jonction de sentiers à moins de 30 m ?
4. Décoder l'épée réelle : photos HD des deux faces, rose des vents du pommeau, triquetra, dragon.
5. Option stratégique : soumettre à l'auteur le décodage « chapitres III/XI » avec une capture de la clairière candidate (validation+exkalibur@unsolvedhunts.com, une demande par mois au maximum hors phase finale). Décision de Guilhem.

## 7. Fichiers
- `scripts/` : `geo.py` (géodésie WGS84), `wfs.py` (BD TOPO IGN), `ring.py` (+ `ring.out.txt`), `tiles.py` / `overlay.py` (ombrage LiDAR HD et orthophoto IGN), `drawmap.py`, `soleil_mai.out.txt`.
- `images/` : anneau 1 850 m sur ombrage LiDAR, zoom Bréda (LiDAR et ortho), enluminure 9 remise droite.
- `sources/roman_de_la_rose_marteau_ch01-14.txt` : extrait du texte Gutenberg 16816, domaine public.

---

# Suite du 13/10 : plan d'attaque sur les points flous

Plan suivi : (1) narrateur → « jour dernier » ; (2) ciel de l'enluminure 9 ; (3) épée réelle (« dernière clé ») ; (4) départ et porte ; (5) recherche systématique des clairières avec témoin ; (6) note et push. Les points (2) et (4) ne sont qu'entamés.

## A. Critères de chaque étape, d'après la FAQ (à ne pas mélanger)
| Étape | Ce que l'auteur exige | Ce qu'il N'exige PAS |
|---|---|---|
| Chemin de rempart | arrivée de l'ultime traversée ; point précis ; mur **ou tour** ; on y « monte » ; accessible toute l'année ; pas maritime, pas naturel | — |
| Clairière = « l'endroit » (05-165) | **visible à l'œil nu depuis le rempart** (05-155) ; jonction de chemins au sens premier (06-005) ; restée clairière (03-274) ; point très précis (06-230) ; identifiable sur une vue du ciel (07-078) ; chemins « très proches » du rempart (06-025) : **à l'échelle de l'Europe, 2 km convient (précision de Guilhem)** ; coffre « tout près » (05-051) | le ruisseau **n'a pas** à toucher la jonction (05-121 : « si vous avez la bonne croisée vous aurez votre réponse ») ; le ruisseau peut être absent des cartes (06-060 : « il faudra vous rendre sur place ») |
| Eaux enchantées | suivies « à senestre » ; coulent jusqu'à la roche et au-delà (03-082) ; pieds mouillés possibles avant la roche (06-090) | être visible depuis le rempart |
| Grande roche | très difficile à manquer (03-211) ; bloque le passage (06-195, FAQ8) ; mouillée, difficile à toucher sans se mouiller (06-180, FAQ8) ; pas visible sur Maps (07-126) | être visible depuis le rempart |
| Souche-majesté | 10 pas N + 10 pas E après la roche ; on ne voit plus la roche depuis la souche (06-167) ; on peut s'y asseoir (07-167) | — |
| 8 derniers pas | partent de la souche (05-043) ; direction « jour dernier » à la boussole réelle (06-282) ; « qui dit dernier jour dit aussi premier jour » (07-107) ; pas besoin de lever la tête (FAQ8) | — |
| Coffre | loin de tout bâtiment (05-107) ; domaine public, pas en zone protégée (FAQ8) | — |

## B. Narrateur (P1) : hypothèse Bayard renforcée
Profil tiré de la FAQ :
- homme réel, de premier ordre, dans les livres d'histoire, lien très fort avec le mythe arthurien ;
- vécu après 1450 (aurait pu imprimer son manuscrit) ;
- une descendance, une statue, des rues ;
- mort pour sa cause après des « actes lâches » ;
- « pur » (consensus), « pas grand-chose à se reprocher » ;
- métier commun, vu de façon « romanesque » ;
- un lieu « intrinsèquement lié » à lui.

**Bayard** (1476-1524) coche tout :
- « sans peur et sans reproche » ;
- tué par une arquebuse, l'arme qu'il jugeait lâche, et mort face au connétable de Bourbon, traître ;
- une fille (Jeanne) ;
- des statues à Grenoble et Pontcharra ;
- le château Bayard au départ de l'É12 ;
- « le narrateur a-t-il pu être considéré comme le dernier chevalier ? excellente question » (07-222).

Conséquence : **jour dernier = 30/04/1524 julien = 10/05 grégorien**. Statut : hypothèse forte, non validée.

## C. Épée (P3) : c'est une boussole
- Fait (FAQ05-092, photos de l'Atelier Thibaud) : le pommeau octogonal porte **N, E, S, O** dans le sens horaire, N vers le bout du pommeau, en alternance avec des entrelacs, autour d'une spinelle entourée d'environ 50 rayons. FAQ01-155 : « l'épée est-elle une boussole ? → l'épée est capitale, à vous d'en déterminer le sens exact ». FAQ8 : la **face** de l'épée sur la planche compte.
- La planche ne montre pas la face photographiée (croix celtique + « ARTHURUS… » sur le ricasso, triquetra sur la garde). Elle montre l'autre face, avec un entrelacs doré. Sur cette face, E et O du pommeau sont inversés.
- La boussole de la carte remplace les directions par **I à VIII** (I = N, III = E, VII = O, VIII = NO) ; « ce qui est vraiment important, c'est le remplacement des directions par des chiffres romains » (01-117). Lecture proposée : « Tout commence et tout s'achève » = I … VIII. « Dix pas au nord » = I (« premier jour »). **« Jour dernier » = VIII = nord-ouest (315°)**, à moins qu'il ne s'agisse de l'azimut du soleil le 10 mai. Statut : à tester sur place.
- « Tombée par trois fois, revenue là où elle n'avait jamais cessé d'être » : deux lectures possibles. Soit Bedivere et la Dame du Lac (trois fois, puis retour au lac), soit l'adoubement de Marignan, où Bayard remet son épée au fourreau en lui parlant. Non tranché.

## D. La fissure de la lame (SVG de Guilhem)
- Recalage local (`scripts/rayure_breda.py`) : le meilleur calage à moins de 3 km est **le Bréda** (résidu 0,111, 1,6 km). La **petite boucle triangulaire** de la fissure tombe à **1,843-1,908 km de la tour, cap 54-56°**, c'est-à-dire sur l'anneau des 10 stades. Avec des positions au hasard, on aurait environ 2 à 3 % de chances.
- **Mais** le fond des gorges n'est pas visible depuis la tour : il est masqué de 20 à 34 m (`scripts/visib_breda.out.txt`). Le contrôle miroir de la forme reste aussi bon (ancien test). **Statut : coïncidence intéressante, pas une preuve.** La boucle tombe sur la route du Bréda.
- Juste à côté, une **cascade** (OSM) sur le **ruisseau de la Burge**, à 2,03 km au cap 58°, avec 3 sentiers à 11-12 m. C'est une bonne « grande roche » potentielle, mais elle est au fond des gorges.

## E. Soleil (« astre glorieux ») avec le vrai relief
Horizon calculé depuis le sommet de la tour (`scripts/horizon.py`) ; premier rayon (`scripts/lever_reel.out.txt`) : 1er mai 71,5° ; **10 mai 66,6°** ; 31 mai 60,3° ; 21 juin 57,9° ; 21-24 avril et 19-22 août ≈ 77°.

## F. Candidats « clairière » (aucun n'est éliminé sur la seule distance)
| # | Lieu | Distance / cap depuis la tour | Visible du sommet ? | Pour | Contre |
|---|---|---|---|---|---|
| **1** | **Clairière de Muraillat / La Planta** (45.43360, 6.04491) | **1 212 m / 66°** | **oui** (dès 20 m de hauteur) | prés en clairière dans le bois ; **3 chemins** ; **ruisseau intermittent à gauche** du chemin quand on va vers le soleil levant ; **ravin rocheux** à ≈ 290 m au NE (confluent avec le Tapon, chute vers le Bréda) = grande roche plausible ; **cap = premier rayon du 10 mai (= 30/04/1524, mort de Bayard)** ; bâtiment le plus proche 149 m ; lieu-dit « Muraillat » (murailles) à 213 m | le lien avec les 1 850 m des 3e/11e n'est pas expliqué. Intuition à vérifier : la **chapelle Sainte-Anne** est à **1 852 m** de cette clairière, et *Hannah* = « grâce, faveur » (« Dieu sut se montrer favorable ») ; mais il y a un biais de recherche (13 lieux examinés) |
| 2 | Le Couvat (45.43286, 6.05405) | 1 864 m / 77° | oui (en rasant) | sur l'anneau ; fin de route + 2 chemins ; lisière | premier rayon du 22 avril / 20 août seulement ; ruisseau de Tapon à 128 m plutôt à droite ; bâtiment à 81 m |
| 3 | Gorges du Bréda (boucle de la fissure) | 1 850 m / 55° | **non** | fissure + anneau + soleil de juin | invisible depuis la tour ; route |
| 4 | Cascade de la Burge | 2 033 m / 58° | non | vraie cascade, 3 sentiers | invisible ; hors anneau (+10 %) |
| 5 | Jonction au sud (45.41245, 6.03600) | 1 892 m / 168° | oui | sur l'anneau, en lisière, loin des maisons | plein sud : pas de soleil du matin |

Témoin : un anneau de 1 850 m tiré au hasard attrape au moins une jonction « bois + ruisseau cartographié + sans bâtiment » dans 32 % des cas (`clairieres.py`, ancien critère). La distance seule ne prouve donc rien. **Ce qui distingue le candidat 1, c'est la suite clairière → ruisseau à gauche → ravin rocheux, alignée sur le soleil du jour dernier.**

## G. Prochaines actions
1. **Sur place, candidat 1** :
   - partir de la jonction (45.43360, 6.04491) et suivre le ruisseau en le gardant à gauche vers le NE, jusqu'à une roche qui barre le passage ;
   - de là, 10 pas N, puis 10 pas E, jusqu'à une souche où l'on peut s'asseoir ;
   - 8 pas vers VIII / NO (315°), et en variante vers 66,6°.
   - Prendre en photo la vue depuis le sommet de la tour au cap 66°.
2. Éclaircir le lien 1 850 m pour le candidat 1 : chapelle Sainte-Anne (porte ? 3e ?) ; portes du bourg médiéval d'Avalon (maquette dans la chapelle de la tour).
3. Ciel de l'enluminure 9 (P2), à relire avec la zone : piste « code universel = éléments chimiques ». Le loup donnerait le wolfram (W), l'arc-en-ciel l'iridium (Ir), l'étoile du matin le phosphore (P). Rien d'établi.
4. Option : envoyer à l'auteur une capture vue du ciel du candidat 1 et le cheminement (règle FAQ07-078). Décision de Guilhem.
