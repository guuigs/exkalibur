# R0610_D1 — L'épée et le calice : rôle « crucial à toute fin du jeu » (06/10/2026)

**Verdict : RIEN de fiable (aucun des 3 mécanismes calculables ne tient). Lecture textuelle FAIBLE à moyenne : « revenue là où elle n'avait jamais cessé d'être » = « encore dans son rocher » = la grande roche.**
Budget vision : 15/20. Recadrages : `images_travail/r0610_D1_*.jpg`. Scripts : `outils_scratch/r0610_d1_*.py`. Données : `donnees_travail/r0610_d1_horizon*.{npz,npy,json}`.

---
## 1. Épée peinte vs épée réelle (FAIT = observation ; photos de téléphone, résolution limitée)

Sources : planche (IMG_4334), HD IMG_4336 (pommeau), IMG_4339 (garde, ricasso) ; réel : `epee_reelle_*.jpg`, photos de l'Atelier Thibaud (8256×5504, page atelierthibaud.com/epee-du-puy-du-fou) et photo « dans la roche » (Puy du Fou).

| Élément | Épée peinte | Épée réelle (Atelier Thibaud, 124 cm, lame 92 cm) | Différence |
|---|---|---|---|
| Pommeau | octogone doré, **8 segments** à rayons (traits) autour d'un disque rouge cerclé de blanc. Comptage sur le zoom : ~8-9 traits sombres par segment (64-72 au total, bords compris ; répartition quasi uniforme [8,9,8,9,9,9,9,9]). Le « ~52 » des joueurs et le « au moins une cinquantaine » de l'auteur sont compatibles ; **pas de nombre exact lisible** (`r0610_d1_pommeau_traits.py`) | octogone à 8 faces ; faces cardinales à lettres gothiques N, E, S, O (FAQ05-092), faces intermédiaires à entrelacs ; **spinelle rouge** (6,23 ct) dans un **anneau cannelé** (le « rayonnement ») | lettres et entrelacs absents du peint (FAQ02-123, 02-226) ; les cannelures rayonnantes deviennent 8 secteurs rayés |
| Pierre centrale | disque rouge avec **trois losanges blancs** (2 en haut, 1 en bas) | spinelle taillée, sans motif | **motif des 3 losanges propre au peint** |
| Garde | quillon gauche à tête de dragon (gueule ouverte) ; anneau doré suspendu à droite (enl. 4, FAQ03-220) ; **bloc central doré** : collet puis pile de bandes annelées qui se resserrent vers le bas (coupe vue de profil), deux points sur la face, **de chaque côté une patte écailleuse quadrillée qui l'enserre** (= FAQ07-048) | quillons en S à têtes de dragon aux deux extrémités ; **au centre un nœud triple (triquetra)** ; aucun calice sur la face photographiée | **calice entre pattes de dragons : peint seulement** |
| Ricasso | gravure dorée irrégulière : couronne de brins à bourgeons en haut, entrelacs dessous ; **pas de croix celtique lisible** | croix celtique entourée d'épis, puis « ARTHURUS PENDRAGON » dans la gouttière | FAQ03-194 : motif réel « pas représenté… n'a pas d'importance » |
| Lame | acier sombre, sans gouttière visible, **fissure** longue (boucle fermée ~45 %, fourche ~82 %) | acier clair à gouttière, **aucune fissure** | fissure = ajout du peintre ; « la fissure vous donne un élément » (FAQ8) |

**Conclusion sur la face.** Les trois photos réelles disponibles (plat, Atelier, dans la roche) montrent **toutes la même face** (triquetra + croix celtique). La face peinte est donc très probablement le **revers**, que nous n'avons pas. FAQ8 : « images en ultra HD, en long, en large et en travers… demandez sur le Discord ». **Le revers réel est la pièce manquante n° 1** (pommeau-revers, garde-revers, gravure du ricasso et de la lame). Nous ne sollicitons personne (règle 1).

---
## 2. Inventaire FAQ sur l'épée, verbatim, classé

**A. Rôle général**
- FAQ01-155 « L'épée est-elle une boussole pour le jeu ? » → « L'épée est capitale dans le jeu. Ce sera à vous d'en déterminer le sens exact. »
- FAQ02-017 (épée fabriquée avec un cahier des charges en rapport avec les énigmes ?) → « Oui. » · FAQ02-085 (épée physique nécessaire à certaines énigmes ?) → « Oui, tout à fait. » · FAQ02-014 (indices directement sur l'épée ?) → « Oui. »
- FAQ03-339 → « L'épée est très importante, en effet. Je pourrais pas vous dire quels éléments en particulier. » · FAQ05-101 (enl. 11 : jouer aux cartes ?) → « Excellente remarque. N'oubliez pas l'épée dans tout cela. » · FAQ07-219 (épée indispensable pour Montsalvage ?) → « Non, pas nécessairement. »
- **FAQ8 (clé)**, à « une fois que l'épée est retournée là où elle n'a jamais cessé d'être, son pommeau a-t-il encore un rôle à jouer ? » → « **L'épée est la dernière clé. Je pourrais pas dire s'il s'agit du pommeau, de la garde ou d'autres éléments du ricasso, de le, de la lame, mais l'épée a un rôle crucial à jouer à toute fin du jeu.** » (transcription automatique)
- FAQ8 : version illustrée ou réelle ? → « la réponse est les deux puisque l'épée réelle est publique et fait partie intégrante du jeu. »

**B. Face, forme, pommeau**
- FAQ03-032 (envers ou endroit ?) → « très important de voir que c'est un côté précis de l'épée qui a été représenté, ça vous sera très utile dans la chasse. » · FAQ8 → « Non, je parle de la face de l'épée, en effet. » (et non de la garde en haut)
- FAQ04-180 (orientée différemment ?) → « Oui. » · FAQ03-151 (dimensions importantes ?) → « Non. » · FAQ06-289 (pommeau/quillons/pointe précisément sur ces enluminures ?) → « Non. » · FAQ07-212 → « Non, il n'y a pas de liberté par rapport aux tracés qui sont indiqués dans la chasse. »
- FAQ02-123 → « Oui, c'est volontaire. Il y a huit segments qui sont eux-mêmes subdivisés avec de nombreux traits. Il y en a au moins une cinquantaine. Et il sera important en effet de relever pourquoi cette épée, sous cette forme là, est présente sur l'ensemble des enluminures. » · FAQ02-226 → « …vous avez raison de noter qu'il y a des différences. »
- FAQ05-092 (réelle : « DUCS » ?) → « …dans le sens des aiguilles d'une montre, en débutant par l'inscription du haut ; N, E, S, O. Si elle avait été forgée outre-Manche, nous aurions sûrement modifié une lettre. »
- FAQ03-194 (croix celtique + épis sur le ricasso réel) → « Ce motif n'est pas représenté sur l'enluminure que vous avez sous les yeux. Donc ça n'a pas d'importance. » · FAQ03-375 → « C'est un anneau qui fait partie de l'enluminure quatre. »

**C. Calice et dragons**
- **FAQ07-048** → « ces doigts ne sont pas des doigts, il s'agit des pattes des dragons qui enserrent le calice et c'est un élément crucial en fin de chasse. »
- FAQ05-124 (colonne sans socle de la lettrine qui « tombe dans le calice ») → « ça n'a pas d'importance. » · FAQ07-005 (coupe de l'enl. 9 = coupe du charpentier ?) → « Je vous confirme que c'est le cas. » · FAQ06-291 → « Il s'agit du trésor. » · FAQ04-138 → la coupe a des dimensions qui lui permettent de rentrer dans le coffre (« Oui, tout à fait »). · FAQ04-150 → « le terme de coupe de charpentier est en effet correct et bien choisi, mais sur le fait que ce soit relié au nom du lieu, je ne pourrais pas vous dire. » · FAQ06-147 (eaux enchantées, dragons ?) → « Pas vraiment. »

**D. Fissure / rayure**
- FAQ03-059 (placée ailleurs sur la lame ?) → « Oui. » · FAQ06-161 (tournée de 180° ?) → « Oui, tout à fait. » → seule la **forme** compte. · FAQ04-093 (à prendre en compte pour un tracé MyMaps ?) → « Là-dessus, je ne peux pas répondre. » · FAQ8 → « la fissure vous donne un élément, en effet. » · FAQ8 (le tracé sur l'épée pourrait-il identifier une catégorie, p. ex. les oiseaux ?) → « Là-dessus, je ne répondrai pas. » · Intro : « Ce qui jadis fut meurtri rayonnera d'un trait glorieux. »

**E. Tracés, calque**
- FAQ04-169 → « Non. […] l'épée, telle qu'elle est représentée, vous n'avez pas besoin de faire un calque de l'épée. » · FAQ8 (logiciel de superposition d'images nécessaire ?) → « Et sans aller jusqu'au logiciel, vous pourriez en effet utiliser un calque. » (**objet non précisé, autre que l'épée** : enl. 11 « carte rudimentaire : oui » ? pommeau réel × peint ?) · FAQ8 (tracer une épée en sortant de Consummatum est ?) → « Non, vous n'aurez pas besoin de tracer une épée. » · FAQ05-145 (tracés demandés en 1, 4, 7 ; suffisants pour « la dernière clef de l'énigme 12 » ?) → « Certains tracés sont à déduire de vos résultats. » · FAQ01-245 → « Pour l'instant, vous n'avez pas plusieurs tracés à faire. » · FAQ03-260 / 04-076 : É7 « Juste la garde », pas de nouvelle lame.

**F. « Tombée par trois fois », rocher, Avalon**
- FAQ03-148 (« Quand l'épée est tombée trois fois, est-ce que c'est toi qui ramasse une et la remet à son rocher aux portes d'Avalon, juste derrière le onzième ? ») → « …je ne suis pas le narrateur, en tout cas dans l'histoire d'Exkalibur. Donc non. »
- FAQ07-136 (revenue à la position tracée en É1 ou ailleurs ?) → « Là-dessus, je ne pourrais pas vous répondre non plus. » (ni oui ni non)
- FAQ8 (« L'épée tombe par trois fois… le même astre par trois fois ») → « je ne pense pas que ça va vous être utile de voir trois fois le même astre. » · FAQ8 (l'astre guide-t-il avant ou après que l'épée soit revenue ?) → « L'astre glorieux vous guide en tout dernier lieu. »
- FAQ01-137 (« encore dans son rocher » : métaphore ?) → « Il s'agit d'une métaphore. Il n'y a pas de rocher à trouver sur la carte du jeu. **À ce stade du jeu en tout cas.** » · FAQ06-210 → « …vous pouvez faire, en effet, tout à fait comme si c'était le cas dans le jeu. De toute façon, il ne s'agit, vous l'avez compris, pas réellement d'une épée physique. » · FAQ01-097 → « “Elle est encore dans son rocher”, c'est un “s”. “S O N”. »
- FAQ04-159 (« PIERRE ? Présent !! ») → « j'ai l'impression que vous avez appelé trois fois Pierre, ça me semble intéressant. » (Pierre = prénom de Bayard ; non exploité)

**G. « Dernière clé / intuition », premier paragraphe**
- FAQ8 (« là était la dernière clé » : un code, deux clés ?) → « Il y a une dernière idée, une dernière intuition qui sera cruciale, en effet, pour pouvoir trouver la clairière. » (transcription automatique) · FAQ06-069 (1er paragraphe lié à la suite spatialement/topographiquement ?) → « Oui. » · FAQ07-088 → « la première phrase d'Ad Vitam Æternam est cruciale et agit comme confirmateur. » · FAQ05-196 → l'ultime traversée mène « à l'endroit où ma 3e et 11e prendront tout leur sens » : « Oui » · FAQ06-166 → « Le chemin de rempart est un point de départ… Et après, c'est l'astre glorieux qui vous indique où aller. C'est là que les troisième et onzième seront utiles pour résoudre cette énigme. » · FAQ07-258 → « quand tout apparaîtra » se passe **avant** la clairière. · FAQ07-198 → les symboles du ciel (enl. 9) « peuvent vous aider à avoir un déclic en fin de jeu ». · FAQ06-064 → « il y a une part d'intuition qui vous est utile et qui vous permet parfois même de prendre des raccourcis salvateurs. »

**H. Grande roche (liée à l'épée par le texte)** : FAQ06-195 « vous devez bien suivre les eaux enchantées pour trouver cette grande roche. Elle vous bloquera le passage dans tous les cas » · FAQ03-211 « une roche très difficile à manquer » · FAQ03-082 les eaux « coulent jusqu'à la grande roche et elles vont même continuer de couler » · FAQ06-198 on peut la câliner sans danger · FAQ07-126 (visible sur Maps ?) « je ne pense pas » · FAQ07-253 (nom de la roche lié au narrateur ?) « Pareil, pas de réponse là-dessus » ; FAQ8 (la grande roche porte-t-elle un nom ?) « Je ne répondrai pas à cela » (pas un « non »).

---
## 3. « Tombée par trois fois » / « revenue là où elle n'avait jamais cessé d'être »

**Fait nouveau (FAQ8)** : l'auteur accepte la prémisse d'une épée « retournée là où elle n'a jamais cessé d'être » **comme un état du jeu** après lequel l'épée (pommeau, garde, éléments du ricasso, lame) reste « la dernière clé » « à toute fin du jeu ». Ce n'est donc pas une étape qui se clôt avant la clairière : l'épée sert **encore à la toute fin**.

Lectures de « tombée par trois fois » (aucune confirmée) :
| # | Lecture | Pour | Contre | Confiance |
|---|---|---|---|---|
| T-a | trois **tracés** de l'épée : É1 (épée entière), É4 (quillons déplacés), É7 (nouvelle garde) | FAQ05-145 (tracés en 1, 4, 7 ; l'auteur ne dément pas) ; FAQ01-245 | « tombée » = posée ? ; FAQ07-136 sans réponse | 40 % |
| T-b | les trois essais de Bedivere avant de rendre Excalibur au lac (Malory, de mémoire) | l'épée retourne à l'eau d'où la Dame l'avait donnée | ce n'est pas l'épée qui tombe ; « jamais cessé d'être » ne dit pas le lac | 20 % |
| T-c | Pierre : trois reniements puis chant du coq (« J'entends le chant retentir ») ; Pierre = prénom de Bayard = pierre/roche | FAQ04-159 « trois fois Pierre, ça me semble intéressant » ; « Remets ton épée à sa place » (Mt 26,52) | l'épée n'est pas le sujet des reniements ; simple paronomase | 10 % |
| T-d | tournure rhétorique sans nombre exploitable (FAQ8 : « trois fois le même astre » pas utile) | l'auteur écarte l'astre ×3 | | 30 % |

Lectures de « revenue là où elle n'avait jamais cessé d'être » (le point **spatial**) :
1. **aux portes d'Avalon = le chemin de rempart (tour d'Avalon)** : phrase précédente « laissé son épée aux portes d'Avalon ». Cohérent avec le départ établi (FAQ06-166, 07-268). **Conséquence spatiale : seulement que la zone est celle du départ ; aucune coordonnée nouvelle.** Confiance 75 %.
2. **dans son rocher = la grande roche** : É1 dit « Elle est encore dans son rocher » ; l'auteur : « Il n'y a pas de rocher à trouver sur la carte du jeu. À ce stade du jeu en tout cas » (FAQ01-137) ; il refuse de dire si la roche a un nom. La seule roche du jeu est la grande roche (FAQ06-195). Lecture : l'épée « revient » dans la roche que les eaux enchantées mènent à rencontrer. **Conséquence : la roche est « la roche de l'épée » ; aucune contrainte géométrique.** Confiance 50 %. Elle invite à chercher une roche **nommée**.
3. la position du tracé É1 : testée (§5, M3), **aucune des droites tracées ne passe à moins de 270 km de la tour**. Écartée. Confiance < 5 %.
4. le Puy du Fou (FAQ01-024 : « L'épée est toujours au Puy du Fou ») : sens matériel, pas spatial pour la clairière.

**Conséquence topographique pour FAQ06-069** : le 1er paragraphe lie la zone à « portes d'Avalon » (lecture 1) et, par l'épée dans son rocher, à la grande roche (lecture 2) ; il donne en plus la **distance 3e-11e = dix stades** (confirmateur, FAQ07-088). Rien de plus ne s'en déduit sans la dernière intuition.

**Corrélat avec Bayard (source vérifiée dans notre copie du *Loyal Serviteur*, `scratch/bayard_loyalserviteur.txt`)** : à sa mort « Si print son espée par la poignée et baisa la croisée en signe de la croix… et cuyda tumber ; mais il eust encores le cueur de prendre l'arson de la selle… le mist soubz ung arbre ». La **croisée** = garde en croix de l'épée. Elle recoupe le vocabulaire du jeu (« croisée des chemins », É9 ; « jonction des chemins », É12) et la place du calice au centre de la garde. Dans le même livre, il « baisa par trois fois la terre » après son duel de Barletta. Pas de lien mot à mot avec « tombée par trois fois » (il « cuyda tumber » une fois).

---
## 4. « La dernière intuition cruciale » : candidats (HYPOTHÈSES)

FAQ8 la lie à **« là était la dernière clé »** = l'épée. Sûr : elle sert à **trouver la clairière**. Les autres éléments (astre = direction, 3e/11e = clairière, FAQ07-133) la placent **entre** le départ et la clairière. Candidats classés :
1. **L'épée comme carte du dernier tronçon** (lecture d'ensemble, non testable en l'état) : pommeau-rayons = l'astre glorieux / la boussole du texte (N, E, S, O réels) → garde = **croisée = jonction des chemins** (calice au centre de la croisée) → lame + fissure = **les eaux enchantées** (« trait glorieux ») → pointe / rocher = grande roche. L'ordre pommeau → garde → lame → pointe suit celui du texte (astre, jonction, ruisseau, roche). Confiance 25 %. Faille : le calice (coupe = but) serait au milieu, pas au bout.
2. La grande roche est « le rocher de l'épée » (§3, lecture 2) → chercher une roche à nom arthurien ou chevaleresque. Aucun toponyme « épée » à ≤ 15 km (§5, M1).
3. Le revers de l'épée réelle (face précise, FAQ03-032 / FAQ8) contient l'élément manquant : non vérifiable sans photo.
Hors É12 mais notés : calque (FAQ8) d'un **autre** objet que l'épée (enl. 11 en « carte rudimentaire ») ; 3 losanges de l'épée peinte ↔ « carreau » (enl. 11, FAQ8 « symbole d'un losange, carreau ») ; 52 traits ↔ 52 cartes (FAQ05-101 « n'oubliez pas l'épée » pour la crypto de l'enl. 11). Ce sont des **pistes d'É11** (angle sans dérivation), pas d'É12.

---
## 5. Mécanismes testables (règle écrite avant calcul) et résultats

Contraintes FAQ vérifiées pour chacun : pas de calque de l'épée (04-169), pas d'épée tracée après É11 (FAQ8), pas de crypto du texte (FAQ8), départ = tour (45.4288, 6.03078).

**M1 — « La grande roche = la roche de l'épée » (toponymes).** Règle : lexique {épée, espadon, glaive, Excalibur, Durandal, Joyeuse} ; rayons 6, 10, 15 km ; gazetier de 118 958 toponymes (`r0610_d1_toponymes.py`). Résultat : **0 occurrence à ≤ 15 km**. Lexique arthurien/Bayard à ≤ 6 km : Avalon (tour, marais, allée), Bayard (château, bois, verger, place, caserne), lycée Pierre du Terrail : tous déjà connus, **aucun rocher** ; « Camelot » (lieu-dit, combe, gorge) à 14,5 km cap 349° (Chartreuse, hors vue). Hasard : 81/300 ancres tirées dans le Grésivaudan ont ≥ 1 occurrence du lexique « épée » à 6 km ; le zéro ici n'a donc pas de valeur positive. **Négatif.**

**M2 — « La fissure est le profil d'horizon vu du rempart au lever du jour dernier ».** Règle (en tête de `r0610_d1_horizon_test.py`) : tronc de la rayure (SVG de Guilhem) → fonction f(y) ; horizon h(az) au pas de 1°, IGN RGE ALTI jusqu'à 70 km (36 720 points, œil à 403,3 m) ; corrélation de Pearson sur fenêtres de 30/45/60/90/120°, 4 variantes (sens × signe) ; cible = centre dans [63,7° ; 73,9°].
- Résultat brut : S_sun = 0,861 (centre 66°), mais c'est un **artefact de tendance** (la rayure et l'horizon 55-85° sont deux rampes). Mon premier hasard (mélange de phases) donnait p = 0,001 : **invalide**, car il ne conserve pas la dérive.
- Hasard correct (marche aléatoire à incréments mélangés, 1 000 tirages ; `r0610_d1_horizon_test2.py`) : médiane 0,944, **p = 0,955** (brut). **Sans tendance** : S_sun = 0,591, p(autres centres) = 0,452, p(substituts) = 0,648. Une rampe pure donne 0,94. **Aucun signal : négatif.**

**M3 — « Revenue là où elle n'avait jamais cessé d'être » = les tracés de l'épée passent près de la tour.** Règle : distance de la tour aux droites prolongées (grands cercles) É1 garde León–Foix, É1 lame Valence–Urquhart, É4 (2 tronçons), É5, É7, É9 (`r0610_d1_traces_epee.py`). Résultat : 274 / 580 / 756 / 747 / 736 / 433 / 381 km. **Aucune ne passe à moins de 270 km d'Avalon**, donc pas de test de hasard utile. Négatif. Au passage : aucun azimut de ces tracés (83,6° ; 352,9° ; 255,96° ; 76,7°) ne redonne le 64,99° de l'É11.

**Bilan de compatibilité FAQ** : aucun des trois ne viole 04-169 ni FAQ8 ; aucun ne passe le seuil de hasard (≤ 2 %).

---
## 6. Verdict et suite
- **RIEN de fiable** sur un mécanisme spatial issu de l'épée ou du calice. **Lecture à garder** : « revenue… jamais cessé d'être » = « dans son rocher » = grande roche ; l'épée est « la dernière clé » utilisée **après** son retour (pommeau, garde, ricasso ou lame, au choix de l'auteur, non précisé).
- À tester ensuite, par ordre : (1) obtenir par un humain les photos HD du **revers** de l'épée réelle et les comparer à la face peinte (garde-calice, ricasso, lame) ; (2) relever les 8 faces du pommeau réel (lettres, ordre ; inversé au revers ?) et poser une règle « pommeau = boussole des huit derniers pas » avant toute carte ; (3) identifier l'objet du « calque » de FAQ8 ; (4) FAQ05-101 + 3 losanges : lien avec la crypto de l'enl. 11 (angle de l'É11 encore sans dérivation).
