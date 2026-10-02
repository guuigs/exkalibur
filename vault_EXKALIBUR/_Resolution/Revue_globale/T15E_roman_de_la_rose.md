---
tags:
  - "#exkalibur"
  - "#E12"
  - "#E7"
---
# T15E : le *Roman de la Rose* (trad. Pierre Marteau, 1878) et les énigmes 7 et 12

> Rapport rédigé le 02/10/2026. Les points marqués **FAIT** sont vérifiés sur le texte intégral. Les points marqués **HYPOTHÈSE** sont des interprétations.

## 0. Source obtenue (texte intégral, et pas des extraits)

- **FAIT** : le texte intégral de l'édition Marteau (4 tomes, ancien français sur les pages paires, traduction en vers sur les pages impaires, numérotation des vers de l'ancien français) est disponible sur les miroirs GitHub de Gutenberg (GITenberg), lisibles par `curl` :
  - Tome I (Guillaume de Lorris, v. 1 à env. 4 000, puis le début de Jean de Meun) : `https://raw.githubusercontent.com/GITenberg/Le-roman-de-la-rose---Tome-I_16816/master/16816-8.txt` (ISO-8859-1)
  - Tome II : `.../Le-roman-de-la-rose---Tome-II_17140/master/17140-8.txt` ; Tome III : `..._44403/master/44403-8.txt` ; Tome IV : `..._44713/master/44713-8.txt`
- Copie de travail (hors dépôt) : scratchpad `rr/rr.txt`, `trad_num.txt` (traduction numérotée), `ancien_num.txt`.
- **Numéros de vers** : ce sont ceux de Marteau, calés sur l'ancien français. La traduction suit l'original vers à vers, avec un décalage de 0 à 3 vers selon les pages. Ils diffèrent d'environ 25 à 30 vers de l'édition Langlois.

## 1. Les deux citations exactes (FAIT)

Un balayage automatique (n-grammes de 3 à 6 mots) des 12 énigmes contre les 4 tomes ne donne que **deux citations littérales**. Toutes deux sont tirées de la **traduction Marteau** et non de l'ancien français.

| Énigme | Texte de l'énigme | Marteau, Tome I | Contexte dans le Roman |
|---|---|---|---|
| **É12** (1re phrase) | « Dieu sut se montrer favorable » | v. 1523-1524 : « A sa prière raisonnable, / **Dieu sut se montrer favorable** » (ch. **XI**, « L'Auteur ici Narcisse conte ») | Écho, mourante, prie Dieu de punir Narcisse. Dieu l'exauce : Narcisse, « de retour de la chasse », vient boire à la source sous le grand pin. |
| **É7** (*Sub rosa*) | « Mais non, le trait qui l'a percé, goutte de sang n'avait versé. » | v. 1777-1778 : « **Mais non, le trait qui m'a percé / Goutte de sang n'avait versé**, / Et la plaie était toute sèche. » (ch. XIII) | Première flèche d'or du Dieu d'Amour, **Beauté**. Elle entre par l'œil jusqu'au cœur. L'Amant retire le fût, mais le fer reste dans le cœur. |

Ancien français correspondant : « Cele proiere fu resnable, / Et por ce la fist Diex estable » (v. 1523-1524). On voit que la formule « Dieu sut se montrer favorable » est **propre à Marteau**. C'est donc bien Marteau (1878, Gutenberg n° 16816) que l'auteur a utilisé.

**Conséquences (FAIT)** :
- L'énigme 7 *Sub rosa* (« sous la rose ») cite elle aussi le Roman. La « rose » de l'É7, encore sans usage dans nos notes, et le « trait » qui ne fait pas saigner (blessure d'amour, flèche Beauté) viennent de là. L'É7 et l'É12 renvoient au même livre, à 250 vers d'écart.
- La FAQ03-295 le confirme (« La lecture du roman de La Rose permet-elle de répondre à une énigme ? » → « vous avez raison de vous interroger sur des textes majeurs du Moyen Âge comme celui-ci »). La FAQ07-218 aussi : la phrase est laissée en français dans la version anglaise pour qu'elle reste cherchable telle quelle.

## 2. Reconstitution du début du Roman (traduction Marteau, verbatim)

### 2.1 Songe de mai, matin, rivière (ch. I, v. 23-130)
- v. 23-28 : « J'avais vingt ans ; c'est à cet âge / Qu'Amour prend son droit de péage / Sur les jeunes coeurs. Sur mon lit / Étendu j'étais une nuit, / Et dormais d'un sommeil paisible. / Lors je vis un songe indicible »
- v. 50 : « C'était en mai, amoureux temps »
- v. 69-79 : « Les oiselets silencieux / [...] Sont en mai, quant rit la nature, / Si gais, qu'ils montrent en chantant / [...] Le rossignol alors s'efforce / De faire noise et de chanter, / Lors de jouer, de caqueter / Le perroquet et la calandre »
- v. 88-90 : « Une nuit, m'en souvient encore, / **Je songeai qu'il était matin** ; / De mon lit je sautai soudain »
- v. 96-99 : « Puis je partis emmi la plaine / **Écouter les douces chansons / Des oiselets** dans les buissons »
- v. 105-114 : « Tout près **un grand ruisseau coulait** / Dont le murmure m'appelait ; / [...] D'un tertre vert et rocailleux / Descend, en bonds tumultueux, / L'onde aussi froide, claire et saine / Comme puits ou comme fontaine. / La Seine est un fleuve plus grand »
- v. 122-130 : « Et je vis couvert et pavé / Son lit de pierres et gravelle. / [...] Or comme claire et douce était / **Et sereine la matinée**, / Parmi la plaine diaprée, / Sans but, **je suivis le courant**, / Tout le rivage côtoyant. »
- Ancien français, v. 128-130 : « Lors m'en alai parmi la prée / **Contre val l'iave** esbanoiant, / Tot le rivage costoiant » (il descend la rivière).

### 2.2 Le mur et ses images (ch. II, v. 131-478)
- v. 131-136 : « J'aperçus un verger immense / Tout clos d'un haut mur crénelé, / Par dehors peint et ciselé / De maintes riches écritures » (ancien français : « Tot clos d'ung haut mur **bataillié** », c'est-à-dire crénelé, un rempart).
- Rubrique : « les **sept** images ». Le texte en décrit pourtant **dix** (voir §4).
- v. 475-479 : « Ces images resplendissaient d'or et d'azur / De toutes parts peintes au mur. / La muraille haute et carrée, / Mieux que haie et close et barrée ».

### 2.3 Le chant des oiseaux derrière le mur ; le tour du mur ; la porte (v. 488-532)
- v. 490-498 : « Nul lieu ne fut d'arbres plus riche / Ni d'oisillons au piteux chant ; / D'oiseaux était trois fois autant / Qu'en tout le reste de la France. »
- v. 509-514 : « **Quand j'ouïs les oiseaux chanter**, / Je me pris à me tourmenter / Par quel engin, quelle manière / Du jardin franchir la barrière »
- v. 525-532 : « Lors j'allai d'un pas assuré, / **Contournant du grand mur carré** / Avec soin toute l'étendue. / Enfin, une porte perdue / J'aperçus, guichet bas, étroit ; / Pour entrer c'est le seul endroit. / Adonc sans plus tarder encore / Je frappai sur le bois sonore. »

### 2.4 Oiseuse (ch. III, v. 533 et suiv.)
- « **Le guichet, qui de charme était**, / M'ouvrit une noble pucelle » (ancien français : « Le guichet, qui estoit de charme »). Le guichet est en bois de charme. Oiseuse a un miroir et un peigne. Elle est l'amie de Déduit, qui « De la terre des Sarrazins / [...] fit jadis venir les plantes » et fit bâtir le mur et peindre les images.
- v. 651-654 : « Dans cette **terre enchanteresse**. / [...] Je crus être [...] Dans le terrestre Paradis. »

### 2.5 Sentier, carole de Déduit (ch. IV à IX, v. 729-1330)
- v. 730-734 : « Lors donc, **à droite je m'engage / Dans un sentier** tout parfumé, / De menthe et de fenouil semé » (ancien français : « Lors m'en alai tout droit **à destre**, / Par une petitete sente »).
- Ordre des danseurs : voir §4-B.
- Le chevalier de Largesse, v. 1208-1211 : « Un beau chevalier descendant / **Du bon roi Artus de Bretaigne**, / Celui-là qui tenait l'enseigne / De Valeur et le gonfanon. » Le jouvenceau de Franchise est « Fils du seigneur de **Gundesore** » (Windsor, note de Marteau).

### 2.6 Arcs et flèches (ch. VI, v. 936-1003)
- Doux-Regard tient deux arcs, l'un noir et noueux, l'autre blanc et orné, et « cinq flèches pour chacun d'eux ». La liste est au §4-C.

### 2.7 Le verger : arbres, bêtes, ruisseaux (ch. X, v. 1371-1460)
- « Ce verger couvrait une espace / Carré dont chaque immense face / Formait des angles réguliers ». Les arbres sont espacés « De cinq à six toises » (v. 1415-1416). Liste au §4-E.
- v. 1431-1438 : « De tous côtés claires fontaines, / [...] Coulaient sous le feuillage ombreux. / Ces ruisseaux étaient si nombreux / Que Déduit fit faire une foule / De petits tuyaux où s'écoule / Par maints canaux l'onde »

### 2.8 La fontaine de Narcisse (ch. X-XII, v. 1465-1660)
- Ancien français, v. 1465 : « Tant fui **à destre et à senestre** » (le mot « senestre » est dans l'original).
- v. 1473-1486 : « En un lieu charmant j'arrivai / A la fin, et là je trouvai / Une fontaine pittoresque / **A l'ombre d'un pin gigantesque.** / **Depuis Karles, fils de Pepin, / Jamais on ne vit si beau pin** ; / Au verger n'était si bel arbre. / Là, **dans un blanc bassin de marbre** / Par Nature avec art creusé, / Le flot clair était déversé. / **Sur la pierre, je vis écrites**, / Au bord amont, lettres petites / Qui disaient : Ici, sur ce bord, / Jadis le beau Narcisse est mort. » En ancien français : « Dedens **une pierre de marbre** / Ot Nature [...] Sous le pin la fontaine assise ».
- v. 1517-1538 (ch. XI) : « [...] A sa prière raisonnable, / **Dieu sut se montrer favorable** / Et voulut que Narcisse un jour / S'en vint justement, **de retour / De la chasse, vers cette source**, / Fatigué d'une longue course, / **Chercher l'ombre sous le grand pin.** / Par monts, par vaux, **dès le matin**, / Il courait le bois et la plaine ; / [...] Il vit sous l'arbre protecteur / La source vive et transparente. / [...] Il se pencha sur le ruisseau. »
- v. 1588-1592 : « La fontaine là se termine. / [...] Le flot toujours frais et nouveau / Sourd nuit et jour à grandes ondes / Par **deux rigoles** moult profondes. »
- v. 1597-1608 : « Au fond de la fontaine aval / **Brillent deux pierres de cristal** / [...] **Lorsque le soleil, qui tout guette, / Ses rais en la fontaine jette**, / Et qu'aval la clarté descend, / On voit de couleurs plus de cent / Nuancer le cristal limpide ». Les deux cristaux reflètent chacun une moitié du verger (v. 1615-1630).
- v. 1649-1657 : Cupidon y sème la graine d'Amour, d'où le nom « **Fontaine d'Amour** ». Ancien français : « Fontaine d'Amors », plus loin le « miréors périlleus ».

### 2.9 Le rosier (v. 1675-1740)
- « Au miroir, entre mille choses, / J'élus rosiers chargés de roses / Qui se trouvaient en un détour / D'une haie enclos tout autour. » Le bouton choisi a « De feuilles quatre belles paires ». Il est gardé par ronces, épines, chardons et houx.

### 2.10 Les flèches tirées sur l'Amant (ch. XIII, v. 1741-1950)
- Amour vise « Près d'un figuier ». 1re flèche, **Beauté** : par l'œil jusqu'au cœur. L'Amant tombe, et c'est là qu'on lit « goutte de sang n'avait versé » (v. 1778). 2e, **Simplesse**. 3e, **Courtoisie** : il tombe en pâmoison « D'un olivier sous la ramure ». 4e, **Franchise** (ajout de Marteau, absent de l'ancien français). Puis **Compagnie** : « Trois fois me pâme en un moment » (v. ~1902). Enfin **Beau-Semblant**, la flèche à l'onguent. « Et ces cinq pointes là fichées / Jamais n'en seront arrachées. »
- Ch. XIV-XVII : l'Amant se rend, Amour lui ferme le cœur « D'une clef d'or » et lui donne ses commandements (v. 2161-2340) : saluer le premier, éviter les paroles vilaines, honorer les femmes, fuir l'orgueil, être élégant et propre, être gai, montrer ses talents, être large, mettre son cœur en un seul lieu. Ils ne sont pas numérotés dans le texte.

## 3. L'énigme 12 face au Roman, phrase par phrase

| É12 | Roman de la Rose (Marteau) | Statut |
|---|---|---|
| « Dieu sut se montrer favorable » | v. 1524, mot pour mot (ch. XI, Narcisse) | **FAIT** (citation) |
| « Tout commence et tout s'achève » | Rien de littéral. Le songe est à la fois début et fin (« Qui la fin du songe ouïra »). | aucune correspondance littérale |
| « J'entends le chant retentir » (FAQ03-184 : seul le narrateur l'entend) | v. 509 « Quand j'ouïs les oiseaux chanter » : l'Amant entend le chant **derrière le mur**, dans un **songe** (lui seul, puisqu'il rêve) | **HYPOTHÈSE** forte (parallèle de situation) |
| « J'ai fait une dernière veille au chemin de rempart » | Nuit de songe, puis tour du « haut mur crénelé » (*bataillié*) : « Contournant du grand mur carré » (v. 525-527) | **HYPOTHÈSE** (parallèle : nuit + rempart) |
| « et l'endroit m'est apparu au matin » | « Une nuit [...] Je songeai qu'il était matin » (v. 88-89) ; « sereine la matinée » (v. 127) ; Narcisse court « dès le matin » (v. 1530) ; « l'endroit m'est apparu » rappelle la vision du songe | **HYPOTHÈSE** |
| « illuminé par l'astre glorieux qui magnifiait le ruisseau » | « Lorsque le soleil, qui tout guette, / Ses rais en la fontaine jette » : les cristaux montrent alors « plus de cent » couleurs (v. 1603-1608). Aussi « Il se pencha sur le ruisseau » (v. 1538), où le mot « ruisseau » désigne la fontaine. | **HYPOTHÈSE** forte |
| « Dans la clairière, à la jonction des chemins » | Le réduit où danse Déduit, au bout d'une « sente » (v. 731-735) ; le « lieu charmant » de la fontaine | **HYPOTHÈSE** faible |
| « j'ai suivi à senestre » | Original : « tout droit **à destre** » (sentier vers Déduit, v. 730) ; « Tant fui à destre et **à senestre** » juste avant la fontaine (v. 1465) | **FAIT** pour le mot ; parallèle = **HYPOTHÈSE** |
| « les eaux enchantées » (FAQ : « enchantées, merveilleuses » ; ruisseau = eaux enchantées) | « suivis le courant, tout le rivage côtoyant » (v. 129-130) ; la « Fontaine d'Amour » où Cupidon a semé sa graine, le « miroir périlleux » ; « terre enchanteresse » (v. 651) | **HYPOTHÈSE** forte |
| « jusqu'à la grande roche » | « Dedens **une pierre de marbre** » (v. 1480), « Sur la pierre, je vis écrites [...] lettres » | **HYPOTHÈSE** |
| « Arrivé à la souche-majesté » | Le **pin** : « Depuis Karles, fils de Pepin, / Jamais on ne vit si beau pin ; / Au verger n'était si bel arbre » (v. 1476-1479) ; « le grand pin », « l'arbre protecteur » | **HYPOTHÈSE** (majesté = l'arbre le plus beau, comparé au règne de Charlemagne ; FAQ07-168 : la souche n'a pas « vu passer un roi », ce qui est cohérent avec une simple comparaison) |
| « dix pas au nord, autant à l'est [...] huit derniers pas » | Le verger est un **carré orienté** à angles droits (v. 1371-1373) ; la rose a « quatre belles paires » de feuilles | rien de probant |
| « Là, tu trouveras la coupe du charpentier » | Pas de charpentier. Le but du Roman est la **Rose** (cueillir le bouton) ; la fontaine est une « coupe » d'eau dans la pierre | **HYPOTHÈSE** faible |
| É12 §1 : « Tombée par trois fois » | Compagnie : « **Trois fois me pâme** en un moment » (v. ~1902) | coïncidence probable |

**Lecture d'ensemble (HYPOTHÈSE)** : le 2e paragraphe de l'É12 reprend la **trame du début du Roman**. Une nuit, puis un matin de songe. Le narrateur longe un mur crénelé (rempart), entend le chant, puis suit l'eau. Il arrive enfin, par la gauche, à la **source sous le plus beau des pins, dans une pierre**, que le soleil illumine. La 1re phrase, citation exacte du passage de Narcisse, joue le rôle de **confirmateur** (FAQ07-088). Elle évoque un chasseur qui, « de retour de la chasse », « fatigué d'une longue course », vient chercher la **source** et l'**ombre sous le grand pin**. **Prédiction testable** : la zone finale doit comporter une **source ou un ruisseau près d'un très grand pin** (ou de sa souche), avec un gros rocher, et peut-être un toponyme du type « Fontaine », « Pin », « Narcisse » ou « Amour ». Cela vaut pour le Vercors / la tour d'Avalon, si le départ est bien là.

## 4. Listes ordonnées du Roman : éléments 3, 8, 11, 13 et 16 (FAIT pour les listes)

Contraintes FAQ : troisième et onzième de même nature, un de chaque, deux points sur une carte à 1 850 m (± 1 %), on « marche surtout sur l'un des deux », pas d'écharde pieds nus sur le 3e, écharde possible sur le 11e, le 13e « ne mènerait pas au bon endroit ».

| Liste | Éléments | 3e | 8e | 11e | 13e | 16e |
|---|---|---|---|---|---|---|
| **A. Images du mur** (10) : Haine, Félonie, Vilenie, Convoitise, Avarice, Envie, Tristesse, Vieillesse, Papelardie, Pauvreté | 10 | Vilenie | Vieillesse | (n'existe pas) | – | – |
| **B1. Carole, allégories nommées dans l'ordre** : Liesse, Déduit, Dieu d'Amour, Doux-Regard, Beauté, Richesse, Largesse, Franchise, Courtoisie, Oiseuse, Jeunesse | 11 | Dieu d'Amour | Franchise | **Jeunesse** | – | – |
| **B2. Carole, toutes personnes** (avec les cavaliers) : Liesse, Déduit, Amour, Doux-Regard, Beauté, Richesse, valet de Richesse, Largesse, **chevalier du lignage d'Arthur**, Franchise, **fils du seigneur de Windsor**, Courtoisie, chevalier de Courtoisie, Oiseuse, Jeunesse, son ami | 16 | Amour | Largesse | fils du seigneur de Windsor | chevalier de Courtoisie | ami de Jeunesse |
| **C. Flèches** (5 d'or + 5 noires) : Beauté, Simplesse, Franchise, Compagnie, Beau-Semblant / Orgueil, Vilenie, Honte, Désespoir, Nouveau-Penser | 10 | Franchise | Honte | – | – | – |
| **C'. Flèches tirées** : ancien français Beauté, Simplesse, Courtoisie, Compagnie, Beau-Semblant ; Marteau ajoute Franchise en 4e | 5-6 | Courtoisie | – | – | – | – |
| **D1. Oiseaux, ancien français** (v. 661-673) : rossignols, geais, étourneaux, roitelets, tourterelles, chardonnerets, hirondelles, alouettes, lardereles, calandres, merles, mauvis, perroquets | 13 | étourneaux | alouettes | merles | perroquets | – |
| **D2. Oiseaux, Marteau** : hirondelles, chardonnerets, tourterelles, geai, roitelet, alouette, mésange, rossignols, merles, mauviettes, étourneaux, bergeronnettes, perruches | 13 | tourterelles | rossignols | étourneaux | perruches | – |
| **E1. Arbres, ancien français** (v. 1378-1408) : pommiers (grenades), noyers (muscades), amandiers, figuiers, dattiers, [épices], coings, pêches, châtaignes, noix, pommes, poires, nèfles, prunes, cerises, cormes, alises, noisettes, lauriers, pins, oliviers, cyprès, ormes, charmes, hêtres, coudriers, trembles, chênes, érables, sapins, frênes | 30 | amandier | châtaigne | poire | prune | alise |
| **E2. Arbres, Marteau** : pommiers, noyers, dattiers, figuiers, amandiers, [épices], pêches, coings, cerisiers, cormes, alises, noisetiers, châtaignes, noix, pommes, poires, nèfles, prunes, laurier, pin, ormes, hêtres, charmes, olivier, cyprès, coudriers, trembles, chênes, érables, sapins, frênes | 30 | dattier | cerisier | noisetier | noix | nèfle |
| **F. Chapitres (rubriques de Marteau)** : I Songe, II Images du mur, **III Oiseuse ouvre la porte** (guichet « de charme »), IV Liesse, V Courtoisie et la carole, VI Dieu d'Amour, VII Richesse, VIII Courtoisie, IX Jeunesse, X Amour épie l'Amant / le verger, **XI Narcisse conté** (contient « Dieu sut se montrer favorable »), XII Narcisse se mire, XIII Amour perce l'Amant, XIV-XVII hommage, clef, commandements, ... XXXII tour de Jalousie | 32+ | Oiseuse, la porte | Courtoisie | **Narcisse (la fontaine)** | flèches | clef d'or |

**Évaluation (HYPOTHÈSE)** :
- La liste F est la seule où la citation de l'É12 tombe **dans le 11e élément**. La phrase « Dieu sut se montrer favorable » est au chapitre **XI**, ce qui expliquerait son rôle de confirmateur. Le 3e serait alors la **porte** du verger, c'est-à-dire l'**entrée**. Mais la contrainte de l'écharde (aucune sur le 3e, possible sur le 11e) colle mal : le guichet du ch. III est **en bois de charme**, et la fontaine du ch. XI est en **marbre**, avec un pin. Il faudrait que le 11e réel soit lié au pin ou au bois, et le 3e à autre chose qu'à la porte. Cette piste est à tester, pas à valider.
- Les listes A à E ne remplissent ni « un de chaque » ni « deux points cartographiables marchables », sauf à y chercher des **toponymes** (un lieu-dit ou un chemin du nom d'un arbre). Par exemple en E2 : 3e dattier, 11e noisetier/coudrier, 13e noix, 8e cerisier, 16e nèfle. Je ne vois aucun lien solide.
- La contrainte « on marche dessus, écharde possible sur le 11e » désigne plutôt **deux ouvrages de même nature**, le 3e en pierre ou en métal, le 11e en bois : passerelles, ponts, marches. Le Roman n'en fournit aucune liste. **Conclusion** : le Roman sert sans doute de **confirmateur de la zone** (source sous le grand pin, roche, chant, rempart), pas de source directe pour les troisième et onzième. Je ne l'affirme pas.
- La provenance du « 8e et 16e incorrect » n'a pas été retrouvée dans `FAQ_E12_complet.md`. Le tableau donne quand même ces éléments.

## 5. Autres phrases des énigmes : citations littéraires ?

Méthode : balayage automatique des 12 énigmes (n-grammes de 3 à 6 mots) contre les 4 tomes Marteau, *Les Romans de la Table Ronde* de Paulin Paris (Gutenberg 42743, 45212, 45213) et *Tristan et Iseut* de Bédier (42256), puis recherches web entre guillemets.

| Fragment | Résultat |
|---|---|
| « Dieu sut se montrer favorable » (É12) | **FAIT** : Marteau v. 1524 (§1) |
| « le trait qui l'a percé, goutte de sang n'avait versé » (É7) | **FAIT** : Marteau v. 1777-1778 (§1) |
| « damoiselles et damoiseaux » (É3) | se trouve dans Marteau v. 1653 (les pièges de Cupidon autour de la fontaine). Formule courante : écho possible, pas une citation |
| « blessé d'un coup de lance » (É7) | dans Bédier, *Tristan et Iseut*. Formule banale |
| « la plus haute tour », « la quête du Graal », « entre le ciel et la terre », « la Dame du Lac avait » | dans Paulin Paris. Formules banales, aucune phrase entière |
| « l'espérance est toujours fille d'amour » | aucune source trouvée (web). Péguy est proche par le sens seulement |
| « Tombée par trois fois » | aucune source littéraire précise (contexte des chutes du Christ, Chemin de croix) ; Rose : « Trois fois me pâme » |
| « là où elle n'avait jamais cessé d'être », « J'entends le chant retentir », « Tout commence et tout s'achève », « épuisées de chaleur et noyées d'espace », « Les Asturies dansaient », « dans la féerie d'un geste de révolte », « féconder la terre d'Europe », « qui confinait à l'innocence », « fendant l'air, panache au vent », « Il est des forces occultes en ce monde », « jour de honte en jour de gloire », « tels des papillons de nuit » | **aucune source trouvée** (recherches web entre guillemets et corpus ci-dessus). Pour les papillons de nuit (É10), il y a un écho thématique dans Marteau v. 2441-2452 : « Chacun amant suit par coutume / Le feu qui l'art et le consume » |

Limites : la recherche web (le seul outil réseau) indexe mal les textes du XIXe siècle. On ne peut donc pas exclure d'autres citations prises dans des ouvrages non numérisés sur Gutenberg.

## 6. À faire

1. **Terrain / carte** : chercher dans la zone finale supposée une **source ou un ruisseau au pied d'un très grand pin (ou de sa souche)**, avec un gros rocher. Tester aussi les toponymes « Fontaine », « Pin », « Narcisse », « Amour », « Rose ».
2. **É7** : relire *Sub rosa* avec le ch. XIII. Le roi blessé « d'un coup de lance » qui ne saigne pas correspond à la flèche **Beauté**. Voir si la « lance offerte à la dame », la balance à deux juments et la rose s'expliquent par le Roman, par exemple par les cinq flèches d'or et les cinq noires.
3. Tester la piste « chapitres de Marteau » (III = porte / entrée, XI = fontaine de Narcisse) sur les deux points à 1 850 m, et vérifier si elle est compatible avec la contrainte de l'écharde.
