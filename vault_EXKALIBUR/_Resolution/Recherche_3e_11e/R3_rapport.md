# R3 : séries internes au jeu (« troisième et onzième », É12)

Sous-agent R3, 03/10/2026. Famille étudiée : les séries **internes au jeu** (énigmes, panneaux, lettrines, Hercule, Machrie Moor, cartes et Tarot, croix PATERNOSTER, les « C », livres numérotés, maillons, les 25 lettres, Winchester, π).
Sources lues : BRIEF, `00 - Solutions validées.md`, `Enigme_12/solution.md` (en entier), `FAQ_E12_complet.md`, `faq_officielle_auteur.json` (thèmes #ENLUMINURE11 et #CONSUMMATUMEST en entier, plus des recherches ciblées), `faq8f.txt` (recherches ciblées), T15B, T15D, T17A, T12B. Images : IMG_4345, IMG_4363, IMG_4364 (schéma de Guilhem), `images_travail/A_REGARDER_enluminure11_HD2.jpg`.
Scripts et sorties : `scratchpad/R3/gabarit.py` → `gabarit.out.txt`, `scratchpad/R3/g.py` (recherche dans la FAQ).
Convention : **FAIT** = réponse de l'auteur ou calcul vérifié. **HYP** = interprétation.

---

## 0. Résumé (300 mots)

**Aucune série interne au jeu ne fournit, à elle seule, deux points réels séparés de 1 850 m.** Dix séries sont **ÉCARTÉES (sûr)**, chacune par une réponse de l'auteur. Pour quatre d'entre elles, la réponse décisive n'avait pas encore servi :
- FAQ8 : « le chemin de marche sur l'enluminure onze représente-t-il un lieu réel ? … non » (élimine les rangs de la croix PATERNOSTER et des pierres du chemin) ;
- FAQ8 : « Dieu sut se montrer favorable… la décrypter, non » (élimine les 25 lettres) ;
- FAQ8 : les maillons « auraient pu être placés ailleurs sans que ça change quoi que ce soit » (aucun 3e ni 11e groupe n'a de sens) ;
- FAQ8 : « vos six C » (pas de 11e C).

Trois séries restent **FAIBLES** : les travaux d'Hercule, le Tarot et le gabarit Machrie Moor. Elles sont cohérentes avec la grille, mais aucune n'a de prise sur le terrain.

**Test du gabarit Machrie** (MM3→MM11 ×9,68 = 1 850 m, cap 93,3°). Je l'ai testé sur 3 départs × 4 ancrages, avec un témoin qui fait tourner la figure sur 360°. Le résultat est **au niveau du hasard**. Exemple : la jonction de Tire-Loup, à 106 m du point projeté, a p = 0,68 (68 % des orientations au hasard tombent aussi près d'une jonction). C'est donc un **non-signal**.

**« ? = 21 » ou « ? = 11 »** :
- L'auteur appelle ce signe un « point d'interrogation » qui cache **un nombre à trouver** (FAQ05-163). Ce nombre se déduit (« les trois chiffres vous aiguillent », « orientez-vous », « comptez par vous-même ») : **la forme du glyphe ne permet pas de le lire**.
- De plus, la FAQ03-137 dit que le « deux à l'envers » à côté du trèfle **est la lettre C**. Il faut vérifier que le « 2 inversé » de Guilhem n'est pas ce C.
- Si « ? » vaut 21, le gabarit Machrie perd son ancre (il n'existe pas de cercle 21). Il ne reste alors que de la numérologie : XXI = le Monde, 21 pierres, 21 = 11e nombre impair, 1+3+5+21 = 30. Rien ne se projette sur le terrain.
- Le mot « nombre » choisi par l'auteur (FAQ07-294) favorise 11 contre 2. La forme de la croix favorise 21. Aucune des deux lectures ne donne un lieu.

**Contrainte structurelle à retenir (FAQ04-115)** : on va « directement de la troisième à la onzième », mais on « passe par des étapes intermédiaires ». Les éléments 4 à 10 se trouvent donc entre les deux, le long du segment. Une série abstraite (rangs, lettres, cartes) ne l'explique pas. Il faut un alignement physique d'objets, ou une figure posée sur la carte.

---

## 1. Faits de l'auteur qui pèsent sur toute la famille (vérifiés dans les sources)

| Réf. | Texte (extrait) | Effet |
|---|---|---|
| FAQ04-115 | « Vous allez directement de la troisième à la onzième, mais en fait ça va vous amener vous verrez à passer par des étapes intermédiaires. » | Les éléments 4 à 10 sont **sur le trajet**. La série a donc une disposition spatiale ordonnée. |
| FAQ8 (01:23:40) | « Est-ce que le chemin de marche sur l'enluminure onze représente un lieu réel de la quête ? … euh non. » | La croix de pierres n'est **pas une carte du terrain** et ses rangs ne sont pas des lieux. |
| FAQ8 (00:18:08) | « Ai-je raison d'essayer de décrypter cette phrase ? — La décrypter, non, mais… cette phrase est importante. » | Exclut le comptage de lettres dans « Dieu sut se montrer favorable ». |
| FAQ8 (maillons) | « ils auraient pu en effet être placés ailleurs, sans que ça change quoi que ce soit » ; « pas grave si vous êtes à un ou deux près » | Ni l'ordre ni le rang des maillons ne comptent. |
| FAQ8 (01:01:58) | « les tracés que vous pourriez faire avec vos six, enfin avec tous vos C » ; Chartres = « avant-dernier C » | La série des C compte **6 éléments**. |
| FAQ03-137 | « Au niveau de la pierre où on peut deviner un trèfle, est-ce un deux à l'envers à côté ? — Et non, il s'agit de la lettre C. » | **Le « 2 à l'envers » près du trèfle est le C.** |
| FAQ05-091 / 05-163 / 06-100 / 07-294 | « notez bien le point d'interrogation… "orientez-vous" pour compléter » ; « Un nombre » ; « les trois chiffres vous aiguillent sur le chiffre » ; « Plutôt vers le nombre important… Je vous laisse compter par vous-même » | Le « ? » est une **inconnue à calculer**, pas un chiffre à lire. |
| FAQ07-035, FAQ8 (00:18:50) | la croix à R et les pierres en cercle « servent différemment » ; pierres à chiffres et pierres à cartes = « deux cryptos différentes » (mais « une seule solution à la fin ») | Additionner les 21 pierres de la croix et les chiffres revient à mélanger deux cryptos. |
| FAQ8 (00:17:11), FAQ8 (01:03:23), FAQ07-215 | l'île au sud est utile « pour leur nature, pour leur nombre, pour la distance » ; « compte-les : … Elle » ; « le compte-lé vous sert… autrement » ; enl.11 = « représentation des L qui entourent le roi et leur compte 1, 3, 5 » → « certains d'entre vous avancent » | **Le « compte-les » de l'É10 resservirait dans l'enluminure 11.** C'est la piste la plus directe pour la valeur du « ? ». |
| FAQ03-320 | « Est-ce qu'il y a une treizième énigme ? — À proprement parler, non. » | La série « énigmes » n'a pas de 13e élément (C6). |
| FAQ06-183 | le livre « vous permet en effet de résoudre une énigme en particulier » | Les livres numérotés servent ailleurs. |
| FAQ04-186 | « Enluminure 11, le visuel est-il confirmateur pour nos deux lieux à trouver ? — Pour l'un d'entre eux, oui. » | ⚠ Classé sous #ENLUMINURE11. Les « deux lieux » peuvent être ceux de l'É11 (Montsalvage et l'arrivée). **Ne pas le compter comme une preuve pour les 3e/11e** (nuance à C10). |
| FAQ06-025 + FAQ06-244 | les chemins de la jonction ne sont pas le chemin de rempart, « même s'ils sont très proches » ; le coffre n'est pas loin du rempart | Les 3e/11e (1 850 m) servent à **trouver** une clairière proche. Ils ne sont pas forcément la clairière elle-même. |

---

## 2. Tableau hypothèse × critères

✓ = compatible, ✗ = contredit (avec la source), ? = indéterminé. C1 même nature · C2 un seul de chaque · C3 deux points à 1 850 m en ligne droite · C4 écharde sur le 11e seulement · C5 on marche sur l'un · C6 un 13e existe · C7 les rangs comptent · C8 pas de chevalier ni de jeu de 52 · C9 difficiles, nature trouvée par un joueur · C10 visibles dans les enluminures · C11 servent à trouver la clairière · C12 genre.

| # | Série (3e / 11e) | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | Énigmes 1-12 et leurs lieux (Tintagel / Saint-Palais ou rempart) | ✓ | ✓ | **✗** (≈ 1 000 km) | ? | ? | **✗** (FAQ03-320) | ✓ | ✓ | **✗** (plusieurs dizaines de joueurs ont les lieux, alors que FAQ06-109 dit que personne n'a nature et position) | ✓ | ? | ✓ | **ÉCARTÉE (sûr)** : C3, C6, C9 |
| S2 | N° de panneau (enl.3 / enl.11) | ✗ (paysage / croix) | ✓ | **✗** (pas des points sur une carte, FAQ05-074) | ? | ? | **✗** (12 panneaux) | ✓ | ✓ | **✗** (visibles de tous) | ✓ | ? | ✓ | **ÉCARTÉE (sûr)** comme objets. Elle reste valable comme « où regarder » (FAQ05-093, FAQ07-239). |
| S3 | Lettrines I T E R L L S U N O C A (E / C) | ✓ | ✓ | **✗** (des lettres) | ✗ | ✗ | ✗ (12 ; 13 seulement avec un préambule non établi) | ✓ | ✓ | ✗ | ✓ | ? | ✓ | **ÉCARTÉE** (C3, C6). FAQ06-270 : les lettrines servent « à trouver quelque chose », sans doute autre chose. |
| S4 | Travaux d'Hercule, liste d'Apollodore (biche / pommes et dragon) | ✓ | ✓ | ? (aucun couple sur le terrain ; Herculée à 1 870-1 889 m de la tour, soit +1,1 à +2,1 %, hors de la tolérance de 1 %) | ✓ (pommier = bois ; biche = pas de bois) | ? | ? (le « 13e travail », les filles de Thespios, est une expression courante) | ✓ (8e juments ; il n'y a pas de 16e) | ✓ | ? | ✓✓ (seuls rangs qui coïncident : biche en enl.3, dragon en enl.11) | ? | ✓ (« la » biche / « le » onzième) | **FAIBLE** : bonne lecture, aucune projection |
| S5 | Cercles MM3 / MM11 de Machrie Moor, en place à Arran | ✓ | ✓ | **✗** (191 m = 1 stade, FAQ05-106 « vous en avez 10 ») | ✓✓ (MM11 a des trous de poteaux en bois) | ✓ | ✗ (pas de MM13) | ✓ | ✓ | ✓ | ✓ (FAQ8 : l'île aide à décoder l'enl.11 ; « carte rudimentaire : oui ») | ✗ | ✓ | **ÉCARTÉE (sûr)** en place, pour C3 |
| S5' | **Gabarit Machrie** : objets locaux disposés comme MM3→MM11 ×9,68 (1 850 m, cap 93,3°) | ✓ | ✓ | ✓ (par construction) | ✓ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | **test au niveau du hasard (§4)** | ✓ | **FAIBLE** (dépend de « ? = 11 ») |
| S6 | Jeu français de 52 (3 / valet) | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ (roi = 13) | ✓ | **✗** (FAQ07-156 « ensemble de 52 : non » ; valets = Lancelot, Hector, Ogier, La Hire, ce qui contredit FAQ07-065) | ? | ✓ | ? | ✓ | **ÉCARTÉE (sûr)** : C8 |
| S7 | Tarot, enseignes (1-10, V = 11, C = 12, D = 13, R = 14) | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ (le valet n'est pas un chevalier) | ? | ≈ (le **C** = Cavalier n'existe qu'au Tarot ; la **D** = Dame est le **13e** rang au Tarot) | ? | ✓ | **FAIBLE** (voir §3d) |
| S8 | Tarot, atouts III / XI (XIII = Mort, XXI = Monde) | ✓ | ✓ | ✗ | ✗ (Impératrice / Force : pas de bois) | ✗ | ✓ | ✓ | ✓ | ? | ✗ (aucun atout peint) | ? | ✓ | **FAIBLE** |
| S9 | Croix PATERNOSTER, rangs 3 = T et 11 = R | ✓ | **✗** (2 lignes, donc deux T au rang 3 et deux R au rang 11, contre FAQ06-216) | **✗** (FAQ8 : le chemin de marche n'est pas un lieu réel) | ✗ (le R est une pierre) | ✓ | ✗ (11 par ligne) | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | **ÉCARTÉE (sûr)** : FAQ8 et FAQ06-216 |
| S10 | 3e et 11e pierres du chemin de l'enl.11 | ✓ | ? | **✗** (FAQ8, idem) | ✗ | ✓ | ✓ (21 pierres) | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | **ÉCARTÉE (sûr)**. NB : c'est la seule série qui imite parfaitement FAQ04-115 (étapes intermédiaires). |
| S11 | Les « C » (Clairvaux… Chartres, dernier C) | ✓ | ✓ | ✗ | ? | ? | **✗** (6 C, FAQ8) | ✓ | ✓ | ✗ | ✓ | ? | ✓ | **ÉCARTÉE (sûr)** : il n'y a pas de 11e |
| S12 | Livres numérotés (I, II, III, VI, II) | ✓ | ✗ (II deux fois) | ✗ | ? | ? | ✗ (5 livres, rien au-delà de VI) | ✓ | ✓ | ✗ | ✓ | ? | ✓ | **ÉCARTÉE** comme série (FAQ06-183 : ils servent à une énigme précise). « III » (enl.5) reste un indice vers le chemin de croix, qui relève d'une autre famille. |
| S13 | Groupes de maillons | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ (12 groupes) | **✗** (FAQ8 : on pourrait les placer ailleurs sans rien changer, donc aucun rang) | ✓ | ✗ | ✓ | ✗ | ✓ | **ÉCARTÉE (sûr)** : FAQ8 |
| S14 | 25 lettres DIEUSUTSEMONTRERFAVORABLE (3 = E, 11 = O, 13 = T, 8 = S, 16 = R) | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ? | ✗ | ? | ✓ | **ÉCARTÉE (sûr)** : FAQ8 « la décrypter, non ». Note anecdotique : E/O = Est/Ouest, S et R pour 8/16 ; ce n'est qu'une coïncidence. |
| S15 | Chevaliers de Winchester | ✓ | ✓ | ✗ | – | – | ✓ | ✓ | **✗** FAQ07-065 | – | – | – | – | **ÉCARTÉE (sûr)** |
| S16 | Décimales de π (3e = 1, 11e = 8, 13e = 7) | ✓ | ✗ (les valeurs se répètent) | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ? | ✗ | ? | – | **FAIBLE à écarter** : aucun objet, aucune prise physique |
| S17 | Nombres impairs prolongés depuis 1, 3, 5 (3e = 5, 11e = 21, 13e = 25) | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ? | ≈ (1, 3, 5 peints) | ? | – | **FAIBLE** (numérologie) |

---

## 3. Notes par série vivante ou faible

### 3a. Hercule (S4)
- **FAIT** : seuls les rangs 3 (biche, enl.3) et 11 (dragon Ladon, enl.11) tombent sur l'enluminure de même numéro (T15D).
- C4 s'accorde : l'arbre des Hespérides est du bois, la biche n'en est pas. C12 aussi : « la » biche, « le » onzième.
- Projection testée (positions des lieux-dits cadastraux, BD TOPO et OSM, 1 272 noms à moins de 6 km) :
  - **Herculée** est à 1 870 m (centroïde T14) ou 1 889 m (ce calcul) de la tour, soit +1,1 à +2,1 %, donc hors de la tolérance de 1 %. Il n'a pas de partenaire « biche » ou « pomme » à 1 850 m ±1 %.
  - Il y a **10 noms par hasard** dans l'anneau de 1 831 à 1 869 m autour de la tour : Chante-Merle, Les Gorges, Le Couvat, Pouchat, La Gare…
  - Brame-Farine (crête des cerfs) est à 3,76 km (chalet) ou 4,2 km (sommet).
  - Les vergers BD TOPO sont partout (plus de 150 polygones), sans pouvoir discriminant.
- **Verdict FAIBLE.** C'est une couche de lecture (« pourquoi 3 et 11 »), pas un placement.

### 3b. Machrie Moor (S5 en place, S5' en gabarit)
- En place : MM3 et MM11 sont à **191 m**, alors que l'É12 dit « **dix** stades ». ÉCARTÉE.
- Gabarit : voir §4. Ce n'est un candidat que si « ? = 11 » et si l'on admet que les 3e/11e locaux reproduisent la figure, ce qu'aucun texte ne dit. Point fort conservé : la correspondance **pierre / bois** (MM3 = pierres ; MM11 = pierres posées sur un ancien cercle de poteaux).

### 3c. Le jeu français, écarté pour de bon
FAQ07-156 (« un ensemble de 52 sur le chemin des remparts ? — Non ») vise exactement le jeu de 52. En plus, les quatre valets français portent des noms de chevaliers (Lancelot, Hector, Ogier, La Hire), ce qui va contre FAQ07-065.

### 3d. Tarot (S7, S8) : observation nouvelle, sans projection
- **FAIT** : le **C** du rocher ♣ ne peut pas être une figure du jeu français, qui n'a pas de Cavalier. Au Tarot, le rang 11 est le Valet, le 12 le **C**avalier, le 13 la **D**ame et le 14 le Roi.
- Les deux lettres peintes, **D et C, sont donc les rangs 13 et 12** du Tarot. « Le treizième ne vous mènerait pas au bon endroit » (FAQ06-133) colle à la **Dame** peinte, et le 11e serait le Valet, absent de l'image.
- FAQ07-106 dit que les versions de figures « de l'époque » sont plus utiles. FAQ05-143 : l'Excuse ? « Très bonne question ». FAQ8 : le jeu de cartes, « vous en aurez besoin, mais pour autre chose ».
- **Rien ne transforme ces rangs en deux points à 1 850 m** (C3, C4 et C5 restent sans réponse). FAIBLE.

---

## 4. Test « ? = 21 » et « 1, 3, 5 vous aiguillent sur le nombre »

### 4a. Ce que dit l'auteur
- Le « point d'interrogation » est son propre mot (FAQ05-091). Il est « sur la pierre » et sert à trouver « **un nombre** » (FAQ05-163).
- On le complète en s'orientant (« orientez-vous pour compléter », FAQ05-091). Les 1, 3, 5 « vous aiguillent », et le résultat est « **plutôt le nombre** » que le chiffre (FAQ06-100, FAQ07-294).
- Conséquence : **c'est une inconnue**. Si Guilhem voit un « 2 inversé », c'est très probablement le « ? » peint (une question mark à main levée ressemble à un 2 sans base), ou bien **le C du trèfle** (FAQ03-137). **Dans les deux cas, on ne lit pas 11 ou 21 dans la forme du signe.**
- ⚠ Point de contrôle pour Guilhem : le signe est-il **sur ou contre la roche au trèfle** ? Si oui, c'est le C (réponse explicite de l'auteur). Est-il sur la **pierre gris-bleu séparée** (quadrant haut-droite, T15B) ? Alors c'est le « ? ».
- Mes recadrages d'IMG_4345 et d'IMG_4363 sont trop flous pour trancher (`scratchpad/R3/trefle*.jpg`).

### 4b. Valeurs candidates et ce que chacune entraîne

| Valeur de « ? » | Comment on y arrive | Accord avec les mots de l'auteur | Effet sur les pistes |
|---|---|---|---|
| **11** | 1, 3 et 5 = numéros des cercles de Bryce. Une fois orienté nord en haut, le « ? » tombe là où se trouve MM11 (meilleur ajustement : résidu 0,47 contre 0,52 pour MM2, T15B) | « aiguillent » ✓ ; « orientez-vous » ✓ ; « nombre » (2 chiffres) ✓ ; « comptez » ? | Le gabarit 3 → 11 tient (cap 93°), mais le test est au niveau du hasard (§5) |
| **2** | même lecture, avec MM2 ; ou la suite 1, 2, 3, 5 en tournant | « chiffre », alors que l'auteur corrige en « nombre » ✗ | aucun |
| **21** | compter les pierres de la croix (11 + 11 − 1) ; 11e nombre impair | « comptez par vous-même » ✓ ; mais elle **mélange** deux cryptos (FAQ07-035) ; « orientez-vous » n'y sert à rien | **Machrie** : il n'existe pas de cercle 21, le gabarit perd son ancre visuelle et il ne reste que l'argument pierre/bois. **Tarot** : XXI = le Monde, dernier atout (« tout s'achève ») ; 21 pierres = 21 atouts, l'Excuse étant hors croix. Pure symbolique, aucune projection. **Pierres** : écartées (FAQ8, chemin de marche). Curiosité : 1+3+5+21 = 30 (« prix de la trahison » ?), sans suite. |
| **résultat du « compte-les » de l'É10** | « je vous laisse compter » + « le compte-les vous sert autrement » + FAQ07-215 (« L qui entourent le roi… compte 1, 3, 5 ») + l'île utile « pour leur nombre » | ✓✓ : c'est la lecture qui relie **toutes** les réponses | La valeur dépend de ce qu'on compte autour du « roi » (siège de Fingal = MM5 : 8 + 15 pierres ? ou nombre de cercles ?). Ce n'est pas tranché ici : cela relève de l'É10, hors de ma famille. **À recommander comme prochaine piste.** |

**Conclusion sur 21.** « ? = 21 » ne crée **aucune** piste géographique nouvelle et en affaiblit une (Machrie). Le mot « nombre » de l'auteur distingue 11 de 2 ; il ne distingue pas 11 de 21. La lecture la plus conforme à l'ensemble des réponses est « ? = compte-les de l'É10 ». Le « ? » peut alors très bien **ne pas valoir 3 ou 11**, et l'enluminure 11 n'aiderait à placer qu'**une partie** (FAQ07-239) : par exemple une orientation ou une échelle.

---

## 5. Projections testées (séries vivantes ou faibles → deux points réels)

### 5a. Gabarit Machrie (S5'), `gabarit.py`
- **Méthode** :
  - On part des NGR à 10 m de T12B, avec MM3–MM11 = 191,0 m, d'où une échelle ×9,683.
  - Cap vrai calculé avec une convergence OS de −2,73° ; la convergence Lambert 93 est corrigée.
  - Départs : tour, Rue du Rempart, Le Vivier. Ancrages : on pose au départ MM3, MM5 (le « roi » = siège de Fingal, l'idée d'Avalon), MM11 ou MM1.
  - Mesure : distance à la jonction de chemins la plus proche (1 985 jonctions BD TOPO + OSM, `junc_attrs.json`) et à la jonction visible depuis la tour la plus proche.
  - **Témoin** : même figure tournée de 0 à 359° autour du départ. p = part des rotations qui font au moins aussi bien.

| Départ | Ancrage | 3e (lat, lon) | 11e (lat, lon) | Jonction la plus proche (p) | Jonction visible (p) |
|---|---|---|---|---|---|
| Tour | 3e au départ | 45.42887, 6.03101 | **45.42791, 6.05463** (1 850 m, 93,3°) | 106 m (**0,68**) | 319 m (0,59) |
| Rue du Rempart | 3e au départ | 45.42977, 6.03118 | 45.42880, 6.05480 | 81 m (0,52) | 237 m (0,46) |
| Le Vivier | 3e au départ | 45.42898, 6.03404 | 45.42801, 6.05766 | 26 m (0,17) | 457 m (0,66) |
| Tour | MM5 (roi) au départ | 45.43819, 6.04899 (1 746 m, 53,6°) | 45.43722, 6.07261 (3 382 m, 74°) | 26 m (0,13) / 210 m (0,72) | 240 m (0,47) / 1 091 m (0,65) |
| Tour | 11e au départ | 45.42983, 6.00739 (273°) | 45.42887, 6.03101 | 53 m (0,32) | 53 m (0,07) |
| Le Vivier | 11e au départ | 45.42994, 6.01042 | départ | 18 m (0,07) | 18 m (**0,01**) |

- Avec environ 24 tests, une valeur de p = 0,01 est attendue par hasard. Le meilleur cas est d'ailleurs un **rond-point de Pontcharra**, à 21 m d'un bâtiment, ce qui exclut un lieu de coffre (FAQ05-107).
- **Le cas « Tire-Loup » de solution.md** (11e à 45.42791, 6.05463, jonction de 5 chemins à 106 m) a **p = 0,68** : deux orientations au hasard sur trois tombent au moins aussi près d'une jonction. **Ce n'est pas un indice.**
- **Verdict : aucun signal.** Le gabarit reste une idée, sans appui dans les données.

### 5b. Hercule, Tarot, lettres, π, nombres impairs
Aucune règle non arbitraire ne les transforme en deux points. Pour Hercule, le test par toponymes (§3a) est négatif : **0 couple** (biche ou cerf ; pomme, Avalon ou dragon) à 1 850 m ±1 %. Seul « atout cœur », à 1 090 m de la tour, rappelle le Tarot : c'est une **résidence** de Pontcharra, donc du bruit.

### 5c. Ce que FAQ04-115 impose à toute projection future
Entre le 3e et le 11e, il doit y avoir sur la ligne (ou tout près) **sept éléments de la même série**, espacés d'environ 231 m s'ils sont réguliers. Aucune série interne ne l'assure sur le terrain. Cela pousse vers une **suite d'objets physiques alignés**, comme ceux étudiés par les autres familles (passerelles d'un même ruisseau, supports d'une ligne, stations, bornes), et non vers une liste abstraite.

---

## 6. Recommandations
1. **Guilhem, sur l'original** : dire où est le « 2 inversé ».
   - Sur ou contre la roche au trèfle : c'est le **C** (FAQ03-137).
   - Sur la pierre gris-bleu séparée : c'est le **« ? »**, qui se calcule et ne se lit pas.
2. Pour obtenir le « ? », exploiter le **« compte-les » de l'É10** (FAQ07-215, FAQ8 « vous sert autrement », « leur nombre »). C'est la seule piste qui satisfait toutes les réponses sur le « ? ».
3. Ne plus présenter la jonction de Tire-Loup ni « ? = 21 » comme des indices de placement : le test de rotation les met au niveau du hasard.
4. Garder S4 (Hercule) et S7 (Tarot : D = 13, C = 12) comme lectures du « pourquoi 3 et 11 ». La nature physique des 3e/11e doit venir d'une série d'objets alignés (FAQ04-115) et vérifier C4/C5. Elle relève des autres familles.
