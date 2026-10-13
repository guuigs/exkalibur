---
tags:
  - "#exkalibur"
---
# É12 : reprise à zéro (13/10/2026)

> **Statut : 🟡 avancée sur la clé, 🔴 pas de pile-poil.**
> Le premier paragraphe est décodé avec une bonne confiance : « Dieu sut se montrer favorable » renvoie au *Roman de la Rose* (trad. Marteau). Les « troisième et onzième » ont d'abord été lus comme ses chapitres III et XI ; **cette lecture est rétrogradée (§ H : le critère de l'écharde la contredit)**. Lecture de travail : 3e = *Ecce Homo* (le Pavé, au départ), 11e = *Consummatum est* (la croix, au bout), soit l'endroit final à 1 850 m de la tour.
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

## 2. ~~Hypothèse forte~~ Hypothèse rétrogradée : « les troisième et onzième » = chapitres III et XI de ce Roman
> ⚠️ **Rétrogradée le 13/10 (§ H)** : la porte du chap. III est en bois (« Le guichet, qui de charme était »). Marcher dessus pieds nus pourrait donc donner une écharde, ce que l'auteur exclut pour le 3e (FAQ07-068). Le *Roman de la Rose* reste la source du vers, mais pas forcément celle des rangs.

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

---

# H. Les 3e et 11e par le lore et la suite des énigmes (13/10, suite)

Consigne de Guilhem : les 3e et 11e s'expliquent par la suite des énigmes et le lore du jeu, pas par des lieux-dits.

## H1. Banc d'essai : ce que l'auteur dit des 3e et 11e (mots exacts)
Toute lecture doit passer chacun de ces filtres.

| Filtre | Réponse de l'auteur |
|---|---|
| Écharde | Pieds nus « sur la troisième » : non. « Par contre, sur le onzième, oui, c'est possible » (07-068). ⇒ le 3e n'est pas en bois, le 11e peut l'être. |
| Marcher | « Il faudra marcher surtout sur l'une des deux » (06-247). |
| Entre les deux | « Vous allez directement de la troisième à la onzième, mais ça va vous amener à passer par des étapes intermédiaires » (04-115). |
| Autres rangs | Un 13e existe (« on aurait pu aller jusqu'au treizième ? Oui, tout à fait »), mais il « ne vous mènerait pas au bon endroit » (06-133). 8e et 16e : « incorrect » (FAQ8). |
| Nature | Même nature, un seul de chaque (06-009, 06-216). Pas un chevalier (07-065). Pas de couleurs (07-244). |
| Visibilité | Pas visibles sur Maps (rappel en 05-074). À « se voient-ils sur Maps ? des remparts ? » : « vous n'avez pas encore identifié ce qu'ils peuvent être » (06-227). ⇒ ce ne sont pas des objets qu'on regarde. |
| Placement | Deux points à placer, un pour chacun (05-074, 07-063). « Toute la question, c'est de savoir quels sont ces 3e et 11e et comment les positionner par rapport à un point de départ » (07-120). « Ce que vous en faites avec la distance, le point de départ » (07-180). |
| Enluminures | Visibles dessus ? « C'est l'une des clés » (05-093). L'enl. 11 aide à en placer « une partie » (07-239). « Tout est codé » (04-027). |
| Lieu | L'ultime traversée mène là où ils « prennent tout leur sens » (05-196). |
| Genre | Quand l'auteur parle de lui-même, il met le masculin (« quels sont ces troisième et onzième », « sur le onzième »). Il ne reprend le féminin que si la question l'emploie. |

## H2. Lectures confrontées au banc d'essai
| Lecture | Pour | Contre | Verdict |
|---|---|---|---|
| **Chapitres III et XI du *Roman de la Rose*** | vers « Dieu sut… » au chap. XI ; l'É7 cite le chap. XIII | la porte du chap. III est « de charme », donc en bois : écharde possible sur le 3e, contraire à 07-068 | **rétrogradée** |
| **Passion : 3e titre *Ecce Homo*, 11e titre *Consummatum est*** (la suite des énigmes) | La tradition place *Ecce Homo* sur le **Lithostrotos, « le Pavé »** (Jn 19,13), un dallage de pierre : pas d'écharde. *Consummatum est* est dit **sur la croix**, en bois : écharde. Même nature (deux scènes de la Passion, deux titres). Les « étapes intermédiaires » sont les **stations du chemin de croix**. « Tombée par trois fois » = les trois chutes du Christ (stations 3, 7, 9). L'enl. 11 montre le **Golgotha (3 croix) et un chemin de pierres qui y monte** (07-239). Selon la tradition du chemin de croix, le prétoire est dans la **forteresse Antonia, une tour du rempart**, comme notre départ. | Il n'y a pas de 13e énigme, sauf à compter en **stations** : 3e = 1re chute (sur le pavé), 11e = crucifiement (bois), 13e = descente de croix (pas « le bon endroit »), pas de 16e. | **passe tous les filtres** ; meilleure lecture pour l'écharde et la « suite des énigmes » |
| **Travaux d'Hercule** : 3 = biche de Cérynie, 11 = pommes d'or des Hespérides gardées par le dragon Ladon | Biche dans l'enl. 3. L'enl. 3 « n'aurait pas pu être placée ailleurs » (03-212) ; sa biche « ne pourrait pas être un cerf » (05-026) : la biche de Cérynie est une femelle aux bois d'or. Dragon dans l'enl. 11. Avalon = île des pommes = jardin des Hespérides (05-196). Un « 13e travail » existe dans la culture (06-133). Mythologie utile (02-288), pomme importante (02-117). Un joueur parle des « éléments des enluminures évoquant les travaux d'Hercule », sans démenti (07-221). Autres travaux repérables : hydre + crabe (enl. 4), taureau blanc (enl. 2), sanglier (enl. 12), juments (balance, enl. 6), lions (bandeau du haut). | « Marcher sur » et l'écharde s'appliquent mal à des travaux ; aucune règle de placement trouvée | **meilleure lecture pour les enluminures** |
| **Apôtres** (ordre des évangiles) | Les livres des personnages de bord portent des chiffres : **II** (R1D, bâton) et **VI** (R5D, couteau = Barthélemy, 6e dans les trois évangiles synoptiques). Dans l'ordre de Marc ou de Matthieu, le 11e est Simon, à la scie (R6D) : du bois. Un 13e existe (Matthias ou Paul). | Le 3e est Jacques ou Jean selon la liste. R4D (X) et R6G (croix à anneau) portent des croix, pas des chiffres. L'auteur refuse de dire que ce sont des apôtres (03-007). Aucune règle de placement. | piste ouverte : les livres sont un code à part (03-255) |
| **Pierres en croix de l'enl. 11** (2 × 11 pierres ; R en 5e et 11e ; croisement à la 6e) | « une partie » (07-239) ; le croisement ressemble à une « jonction des chemins » | ce sont des pierres, donc pas d'écharde sur le 11e ; les nombres 1, 3, √5 vont avec le cercle des pierres à symboles (07-035) | outil de placement possible, pas les 3e/11e eux-mêmes |

## H3. Ce que ces lectures font de la distance
Les deux lectures qui passent le mieux (Passion, Hercule) mettent le **3e au départ** et le **11e au bout**. Pour la Passion : le Pavé d'*Ecce Homo* = le rempart, et la croix = l'endroit final. Pour Hercule : Avalon = le jardin des pommes. Combinées avec 07-120 et 06-166 (« le chemin de rempart est un point de départ ; après, c'est l'astre glorieux ; c'est là que les 3e et 11e seront utiles »), elles donnent la lecture la plus simple : **l'endroit final est à 1 850 m ± 1 % du sommet de la tour**, dans un secteur éclairé le matin.

- Sur cet anneau (1 832-1 868 m), **une seule jonction de chemins de la BD TOPO est visible depuis le sommet de la tour : Le Couvat** (45.43286, 6.05405), à 1 864 m, cap 77° (`scripts/visib_jonctions.out.txt`). Les autres jonctions à ±1 % (caps 141°, 145°, 239°) sont masquées par le relief. Témoin : un anneau au hasard contient une jonction « bois + ruisseau + sans bâtiment » dans 32 % des cas. Ce n'est donc pas une preuve, seulement le seul candidat qui reste sous cette lecture.
- **La clairière de Muraillat (1 212 m) n'est pas expliquée par ces lectures.** Trois rapprochements ont été testés et écartés :
  - **1 155,7 m = 5,00 × 231,25 m.** Si les rangs 3 et 11 sont espacés de 8 intervalles égaux (231,25 m chacun), Muraillat serait à 5 intervalles d'un point de la Rue du Rempart. Mais cette rue couvre toutes les distances entre 1 114 et 1 213 m de Muraillat. Ce n'est donc pas un signal.
  - **La droite de l'É11 prolongée passe à ≈ 12 m de Muraillat.** Mais Muraillat a été choisie pour son cap (≈ 66°), qui est déjà celui de cette droite à 1° près : le raisonnement tourne en rond.
  - **Le point à 1 850 m dans l'axe tour → Muraillat** (45.43598, 6.05233) tombe dans un hameau (bâtiments à 33 m). Rien n'y ressemble à un 11e.

## H4. Statut et suite
- Lecture de travail : **3e = *Ecce Homo* au départ (pierre), 11e = *Consummatum est* au bout (bois)**, avec les stations du chemin de croix comme étapes intermédiaires. Confiance **moyenne** : elle passe tous les filtres de la FAQ, mais elle n'a encore désigné aucun lieu exact.
- La lecture « travaux d'Hercule » reste la meilleure pour les enluminures. Les deux peuvent se compléter : les titres pour placer, les enluminures pour confirmer.
- **Muraillat perd sa place de candidat n° 1** sous ces lectures, car elle n'est pas à 1 850 m. Elle ne redeviendrait prioritaire que si une lecture des 3e/11e la place entre deux points distants de 1 850 m.
- Prochaines actions :
  1. Reprendre l'anneau 1 832-1 868 m avec tous les chemins (OSM, BD TOPO, traces LiDAR), et pas seulement les jonctions BD TOPO ; tester la visibilité de chacun depuis le sommet de la tour.
  2. Examiner Le Couvat en détail : ruisseau à garder à gauche, roche qui barre le passage, bâtiment à 81 m.
  3. Compter les maillons d'or (biche ≈ 4 au cou, dragon : 1 anneau à la griffe) et voir si un nombre donne un cap ou un rang.

---

# I. Visibilité réelle depuis le sommet du donjon (13/10, soir)

## I1. Correction de position (fait)
- Le point utilisé jusqu'ici pour « la tour » (45.429083, 6.030808) est **à 27 m du donjon**. Le bâti IGN donne « Tour, donjon », 34,5 m de haut, centroïde **45.428888, 6.031015**. Le MNS LiDAR HD place le sommet à **437,6 m** (sol 408,8 m) en 45.428899, 6.031011.
- Toutes les distances sont désormais prises depuis ce centroïde. Avec une tolérance de ±18,5 m sur 1 850 m, l'écart compte.
- Nouvelles valeurs : Muraillat **1 207 m / 64,3°** ; jonction du Couvat **1 856 m / 76,2°** ; cascade de la Burge **2 031 m / 57,0°**.

## I2. Méthode
- Modèles IGN téléchargés par WMS-R sur une grille de 2 m : RGE ALTI (sol) et **MNS LiDAR HD (sol + arbres + bâtiments)**. Emprise 45.404-45.454 N, 5.998-6.064 E. Scripts : `scripts/viewshed_mns.py` (rayons tous les 0,05°, pas de 1 m), `ring_all.py` (toutes les jonctions BD TOPO + OSM), `visible_patches.py`, `eau_visible.py`, `viewshed_map.py`. Les données (≈ 60 Mo) restent hors dépôt.
- Œil à 1 m sous le point le plus haut du MNS. Le résultat ne change pas entre −4 m et +2 m.
- Deux niveaux de visibilité, parce que l'auteur dit seulement « l'endroit est **dans le champ de vision** » (05-155), et non « on en voit le sol » :
  - **stricte** : on voit le sol de l'endroit par-dessus les arbres ;
  - **large** : seul le relief est pris en compte.

## I3. Résultats (visibilité stricte)
- Dans l'anneau 1 832-1 868 m, seulement **6 %** du sol est visible. Vers l'est, la forêt et la crête du Bréda masquent presque tout.
- **Muraillat, Le Couvat, la cascade de la Burge et le pont des Bretonnières ne sont pas visibles.**
  - Muraillat : le relief seul laisse passer de justesse (−0,5 m), mais des arbres de 12 à 32 m entre 918 et 1 202 m coupent la vue.
  - Le Couvat : le relief masque déjà de 0,3 m, et des arbres de 24 m se dressent juste devant la jonction.
- **Seule zone visible à l'est sur l'anneau : le pré A**, centré en 45.43057, 6.05462. Il est à 1 857 m, cap 84,2°, sous la ligne à haute tension, en forêt communale de Saint-Maximin. Son sol est dégagé sur ≈ 2 300 m². Un chemin passe à 17-31 m, le ruisseau de Tapon (intermittent) à 72-81 m, dans un ravin. Mais la jonction la plus proche (45.43103, 6.05345) n'est pas visible et touche une grange. C'est un candidat faible.
- Les autres jonctions visibles sur l'anneau sont à l'ouest et au nord : centre de Pontcharra (bâtiments à 3-60 m) et plaine de l'Isère (champs, fossé du Coisetan). Pas de clairière ni de roche.
- Le relief + la forêt font que **très peu de clairières en forêt sont réellement visibles** depuis le sommet. Sous la visibilité stricte, aucun candidat ne réunit à la fois clairière en forêt, jonction, ruisseau, roche possible et absence de bâti.
- Eaux visibles depuis le sommet : petits ruisseaux du village à l'est (450-750 m) et le Rebouchet (116°, 650 m) ; le Bréda en plaine au nord-ouest (600-1 200 m) ; le Coisetan au nord (2,2 km) ; le canal de Renevier à l'ouest.

## I4. Conséquence
- Si « dans le champ de vision » veut dire « on voit le sol », **les candidats de l'est (Muraillat, Couvat, Bréda) tombent**. Le seul point visible sur l'anneau est le pré A, sans jonction convaincante.
- Si l'expression veut seulement dire « dans la direction regardée, sans crête devant », Muraillat (relief −0,5 m) et Le Couvat (+0,3 m) restent à la limite.
- Dans les deux cas, **la visibilité ne suffit pas à désigner un lieu**. Il faut d'abord comprendre les 3e/11e.

## I5. Maillons d'or (décompte provisoire, photos HD)
| Élément | Enluminure | Décompte |
|---|---|---|
| Lion noir (bandeau du haut) | 1-2 | ≈ 4 maillons |
| Biche | 3 | ≈ 4 maillons au cou (« il n'y en a pas qu'autour du cou », 06-176) |
| Garde de l'épée | 2-3 | 2 maillons et une plaque gravée |
| Soldat romain | 9 | 1 maillon tenu en main, plus une manchette dorée en 4 éléments |
| Dragon | 11 | **2 anneaux entrelacés** à la patte |
| Couronne (bordure du bas) | 11-12 | bandeau de ≈ 5-6 maillons |

Aucun usage trouvé à ce stade. À tester : chiffres de la boussole I-VIII, nombres de pas, rangs.

Images : `images/visibilite_sommet_est_mns.jpg` (rouge = sol visible depuis le sommet, bleu = anneau 1 850 m ± 1 %, vert = couvert > 4 m) ; `images/pre_A_cap84_visible.jpg` (magenta = sol visible ; orthophoto IGN).

## I6. Visibilité au sens large (relief seul) sur l'anneau ±1 %, moitié est
Calcul `OBST=mnt` (`viewshed_mns.py` → `vis_polar_mnt.npz`), puis `ring_all.py`. Depuis le donjon, seules trois jonctions de l'anneau 1 832-1 868 m sont hors du masque du relief côté est et sud :

| Jonction | Distance / cap | Ce qu'on voit sur l'orthophoto et le LiDAR | Verdict |
|---|---|---|---|
| **Le Couvat** (45.43306, 6.05390 et 45.43288, 6.05406) | 1 847-1 855 m / 75,5-76,2° | Fin de route, puis fourche de chemins sur une croupe NE-SO. Pâture en bordure du hameau (maisons à 64-77 m). **Pas de ruisseau à la jonction** : le Tapon coule dans son ravin à 130 m. | faible |
| Route du Crêt des Moines (45.43524, 6.05272) | 1 837 m / 67,4° | Carrefour de routes goudronnées, maisons à 84 m | écarté (pas un chemin) |
| Jonction sud (45.41246, 6.03601) | 1 868 m / 167,9° (limite) | Piste forestière et sentier **en forêt dense**, sans clairière. Ruisseau en ravin à ≈ 100 m. Plein sud. | faible (contredit « restée clairière », 03-274) |

**Bilan de l'anneau sous la lecture Passion** (endroit final à 1 850 m ± 1 % du donjon) : la zone **Le Couvat – pré A – ravin du Tapon** (caps 75-84°, 1 847-1 857 m) est la seule à l'est qui soit visible, strictement (pré A) ou largement (Le Couvat). Le ravin rocheux du Tapon (eau à 72-130 m) pourrait porter la « grande roche ». Mais aucune jonction de cette zone n'a à la fois un ruisseau tout proche et des maisons à distance. **Rien n'est démontré.** La vérification ne peut se faire que sur place (ruisseau non cartographié, roche, souche).
