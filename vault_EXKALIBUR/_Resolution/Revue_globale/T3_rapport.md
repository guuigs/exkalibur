# T3 : revue des zones d'ombre des énigmes 1 à 11 (30/09/2026)

Méthode : recherche FAQ par mots concrets (`T3_faq_zones.py`, `T3_faq_zones2.py`, `T3_narrateur.py`), calculs par script (`T3_e1_lieues.py`, `T3_jour_dernier.py`, `T3_e11_rhumb_soleil.py`, `T3_c6_e11angle.py`, `T3_figure_C_666.py`, `T3_wiki_avalon.py`), tous archivés avec leur `.out.txt`. Rien n'a été pris sur Discord. Chaque affirmation est marquée FAIT / HYPOTHÈSE / INTUITION. Wikipédia (API) sert uniquement aux dates et aux lieux.

## 1. Tableau de synthèse

| Zone d'ombre | Avant | Après | Preuve principale | Confiance |
|---|---|---|---|---|
| **É1** Foix à 53,7 km = 12 lieues, « près de 11 » | fragile | **inchangée, très légèrement renforcée** | Foix reste à 53,68 km, quel que soit le point de mesure (±0,1 km). Cap 274,8° (« Couchant » ✓). La lieue est libre (FAQ01-002). 53,68 km font 11,00 lieues de 4,88 km, 10,74 de 5,0 km, 11,12 de 4,83 km (`T3_e1_lieues.out`). FAQ02-155 : « ce n'est pas exactement onze ». Autres candidats à 10,5–10,99 lieues : Lordat (4,44 km, cap 248°), Tarascon (5 km), Gudanes. Ils n'ont ni « pays cathare » ni « quillon » à l'est de la garde. Le parallélisme garde ↔ nouvelle garde : Foix 7,7° (meilleur des 8 candidats, mais l'écart est petit) | moyenne |
| **É2** 9e mot = Alexandrie | peu prouvé | **Alexandrie affaiblie** (le résultat TROIANOVA n'en dépend pas) | FAQ01-051 : les genres de la charade comptent (« seule ma septième est au féminin »). FAQ02-281 : les items respectent le genre de leur solution. « Mon dernier » est masculin, donc le 9e mot devrait être masculin. Alexandrie est féminin. FAQ02-078 : on peut chercher « une personne », « pas nécessairement » une chose ou un lieu. Le 9e mot est probablement **un homme en A** (Auguste ? Agrippa ? Antoine ?). Aucune FAQ n'en désigne un. TROIANOVA est validé, donc il n'y a pas de conséquence sur la suite | moyenne (objection de genre) |
| **É5** panneau R5R ou R3G | incertain | **R5D (enluminure 10 de l'auteur) plutôt que R3G** ; à ne pas confondre avec « enluminure 5 » | Les FAQ parlent de deux « enluminures » différentes. « Enluminure dix » = soleil doré, cercle de pierres, chevalier couronné (FAQ03-371, 05-126, 03-357, 03-290). « Enluminure cinq » = nappe/vitrail, barque, cornemuse (FAQ04-062, 06-093, 07-079). La nappe donne « une solution intermédiaire » (FAQ07-079, 06-103 : pas Montsalvage), c'est-à-dire É10 (`Enigme_10` : R3G). R3G porte donc É10, pas É5. « R5R » n'existe pas (nomenclature G/D). Les pierres de R5D (menhirs, soleil) collent à É5 (Stonehenge/Carnac) | moyenne (l'appariement est indirect) |
| **É6** plateau → lettres | fait, mécanisme flou | **inchangée** | Voir §3. Aucun nouvel élément | — |
| **É6** 5e et 6e C, « les 6 C forment une figure » | 5e = Chartres, 6e inconnu | **Hypothèse nouvelle : le 6e C = un point de passage sur la droite É11 (Saint-Palais → Bayard → Avalon)**. Jamais prouvée | FAIT : FAQ06-252 « le sixième et dernier C est un point de passage, vous passez dessus » ; FAQ06-071 il oriente ; FAQ07-058 toujours un C aujourd'hui ; FAQ07-271 ce n'est pas Montsalvage ; FAQ07-166 la figure ne croise pas la lame É1. CALCUL : la chaîne Clairvaux → Cîteaux → Cluny → Clermont → Chartres → château Bayard **se recoupe** (Cluny–Clermont est croisé par Chartres–Bayard à 8 km de Cluny). 19 communes en C bordent la droite SP → Avalon à ±2 km : le **test du hasard interdit de choisir**. Le château Bayard est lui-même un « C » (Château) : simple curiosité | faible (hypothèse) |
| **É6** question « Ligne 8 » | origine inconnue | **Ligne 8 = un rectangle parisien** (48,83–48,87 N ; 2,29–2,35 E) dans le KML de l'épée. Elle n'a **aucun** lien avec É6 dans les notes | Le KML n'a aucune « Ligne 8 » pour É6 : c'est un objet du dossier « Epée – énigme 1 » (`Carte/extraire_kml.out.txt`). C'est probablement un essai (l'enveloppe de Paris, île de la Cité). La question reste à poser à Guilhem | faible |
| **É7** balance, 2 juments, lance, rose | non consommés | **inchangée (non consommés)** | FAQ04-149 : ce sont bien des juments (pas des étalons : FAQ07-191). FAQ06-123 : il n'est **pas nécessaire** que la garde soit juste pour interpréter balance + 2 juments, donc ce n'est pas une mesure géométrique fine. FAQ03-029 : pas de réponse (utile pour cette énigme ou une suivante ?). FAQ03-295 : les auteurs médiévaux de « la Rose » sont un bon axe. Rien ne relie ces éléments à É8–É12 | faible |
| **É8** « numéro 1 » = Tibère | fragile | **renforcée** | 18 pétales × 37 = 666 : sur 100 années possibles, seule 37 donne exactement 666 (`T3_figure_C_666.out`). FAQ04-067 : il n'y a pas de controverse sur l'an de mort du numéro un (Jésus, 30/33, aurait été controversé ; Tibère 16/03/37 ne l'est pas). FAQ03-205 : « numéro un » = le chiffre 1. FAQ05-103 : l'idée qu'il est « numéro 1 » est cruciale. Ce qui reste inexpliqué : pourquoi « numéro 1 » pour Tibère (2e empereur) ? | moyenne-haute (résultat) / basse (pourquoi Tibère) |
| **É8** Lincoln / Hugues d'Avalon devant la zone finale | en réserve | **confirmation forte** | FAIT (Wikipédia fr) : Hugues d'Avalon (= Hugues de Lincoln) est né en 1140 au château d'Avalon, **Saint-Maximin (Isère)**. La **tour d'Avalon** y a été érigée par les chartreux en 1895 pour l'honorer. FAQ07-016 : la plus haute tour « existe encore, mais pas en entier » : la flèche de Lincoln (1311–1548, effondrée) colle. FAQ06-082 : c'est l'époque du narrateur qui donne la tour. Lincoln est la plus haute de 1311 à 1548 : ok pour 1524. FAQ03-169 : le lieu de la tour ≠ celui de l'humble serviteur (Payns) ✓. Le lien E8 → E12 est donc **cohérent avec la droite É11 qui passe par la tour d'Avalon**. Limite : « Avalon » est déjà dans le texte É12, donc la convergence n'est pas totalement indépendante | moyenne-haute |
| **É9** narrateur = Bayard | ouvert | **plutôt renforcé** (voir §2) | 11 FAQ compatibles fortement, 0 incompatible franche, 3 tensions mineures | moyenne |
| **« Jour dernier »** | non calculé | **Hypothèse : jour dernier = jour de mort/gloire du narrateur = 30/04/1524 (julien)** | Voir §4. Lever à Avalon : 63,66° (julien) ; 67,97° (grégorien proleptique) | moyenne-faible |
| **É10** « compte-les » | ouvert | **inchangé : nombre non trouvé** ; consommation plus loin non démontrée | FAQ07-177 : compter « au sens mathématique ». FAQ07-053 : objets non vivants. FAQ07-147 : c'est un résultat différent de la distance. FAQ07-151 : ça sert « plus tard ». FAQ07-064 : c'est « un résultat intermédiaire » utilisé dans un calcul. Candidats : 6 cercles, 23 blocs (siège de Fingal), 4… Aucun lien numérique net avec 1, 3, 5, ? (FAQ07-215, 07-294 : « le nombre important »). Sur ~17 000 formules simples testées sur {1, 3, 5, N} (N ≤ 120), 14 tombent à ±0,03° de 64,99, toutes via « N = 65 ± un terme » (par ex. 5×13) : c'est du bruit, pas une dérivation | faible |
| **É11** origine de l'angle 64,99° | ouverte | **Hypothèse : azimut du lever du soleil, le jour de mort de Bayard** | Voir §4 | moyenne-faible |

## 2. Fil « narrateur = Bayard » : passage au crible de la FAQ

Corpus : 144 items du thème #NARRATEUR + 79 autres mentions (`T3_narrateur_faq.out.txt`). Seuls les items qui discriminent sont listés.

**Compatibles (dans l'ordre de force).**
- FAQ07-050 : le narrateur aide à identifier « sans se tromper » le dernier chevalier (« beaucoup de façons »). FAQ07-222 : le narrateur pourrait être vu comme le dernier chevalier (« excellente question »). Bayard a le surnom « le dernier chevalier ».
- FAQ07-030 : un lien fort et évident, utile en fin de jeu, dans la zone finale. FAQ07-165 : un lieu « extrêmement important et intrinsèquement lié au narrateur ». FAQ06-235 : le narrateur est associé à un lieu réel visible sur carte. Le château Bayard (naissance) est à 1,0 km de la tour d'Avalon.
- FAQ04-103 : « pas grand-chose à se reprocher » ; FAQ06-116 : « pur », parti pris consensuel ; FAQ07-235 : « bonne publicité » ; FAQ07-026 : pas bienheureux. Tout cela colle à « sans peur et sans reproche ». C'est ce qui départage le plus Bayard de Colomb (controversé) et de Jacques Cœur (condamné en 1453).
- FAQ06-128 : il a donné sa vie pour sa cause. FAQ07-119 : il a subi « des actes lâches » (Bayard est tiré dans le dos par une arquebuse). FAQ06-129 : il écrit parce que son temps est compté. FAQ06-087 : une dernière longue bataille. FAQ06-040 : il écrit au futur (« je transformerai »). C'est la retraite de la Sesia.
- FAQ06-095 / 07-155 : le narrateur n'a pas vécu le jour de honte. « Un millénaire » = environ 1 000 ans, 900 est trop loin (FAQ03-006, 07-060). Camlann (537) → 1524 = 987 ans ✓. Jacques Cœur (1456) : 919 ans, exclu par FAQ07-060. Colomb (1506) : 969 ans, possible.
- FAQ06-241 / 05-057 : le manuscrit aurait pu être imprimé de son vivant (après 1450). FAQ06-159 : portrait au pinceau. FAQ07-106 : l'auteur accepte la prémisse « à l'époque de mon narrateur, les noms de figures de cartes étaient variables » et répond « 15e-16e siècles » ; FAQ07-100 : cartes françaises. Les couleurs françaises datent des années 1480-1500. L'époque 15e-16e est donc admise. Bayard (1473-1524) ✓.
- FAQ06-249 / 07-047 / 07-211 / 07-265 / 06-281 : rue à son nom, enseigné à l'école, statue réelle. Bayard ✓ (mais aussi Colomb, Jacques Cœur : non discriminant).
- FAQ07-094 : « aspect romanesque » de sa profession ; FAQ06-051 / 07-081 : métier commun, modernisé (soldat/officier ?).
- FAQ07-225 : c'est un homme ✓. FAQ07-140 : personnage historique de premier ordre avec un lien très fort au mythe arthurien (la chevalerie).
- FAQ05-099 : « le chemin de rempart peut être anachronique au narrateur » : **Oui**. La tour d'Avalon date de **1895** : cet anachronisme est prévu. FAQ07-290 va dans le même sens.
- FAQ07-071 : le jeu de cartes aide à identifier le dernier chevalier « et vice-versa ».

**Incompatibles.** Aucune réponse FAQ n'exclut Bayard.

**Tensions mineures.**
- FAQ06-087 (« racheter ses fautes ») face à FAQ04-103 (« pas grand-chose à se reprocher »). Pas de contradiction stricte.
- « Métier » (FAQ05-135, 07-081) : « chevalier » n'est pas un métier commun. Il faut lire soldat/capitaine.
- FAQ05-104 : le « combat d'une vie » lui aurait coûté sa gardienne de lumière. Je n'ai **aucun** fait de la biographie de Bayard qui l'explique. C'est le point faible n° 1 à investiguer.
- FAQ06-197 : il « aurait pu » marcher sur les chemins de la jonction, « je ne pense pas qu'il l'ait fait ». C'est curieux si les chemins sont à 1 km du château Bayard. Pas contradictoire (chemins récents ?).

**Sur les questions du brief.**
- *Jour de gloire = Marignan (13-15/09/1515) ?* Non concluant. Rien dans la FAQ ne l'impose. FAQ06-040 dit que le jour de gloire est **futur au moment de l'écriture** ; FAQ06-087 dit que le narrateur se bat pour l'atteindre ; FAQ05-009 dit qu'il l'a atteint. Marignan est en 1515 et l'adoubement est une gloire déjà acquise en 1515. Le futur « je transformerai » colle mieux avec la mort en 1524.
- *Jour de honte ?* Camlann (537) est cohérent avec « millénaire » et « coup mortel porté par l'adversaire » (Arthur/Mordred). Judas (33) n'est pas compatible avec Bayard (≈1 490 ans).
- *Prix de la trahison ?* FAQ07-022 : valeur numérique + couleur **métallique**. FAQ05-129 : le jour de gloire a la même couleur. 30 deniers d'argent (Judas) est un candidat naturel, mais la FAQ n'établit pas que la trahison de « honte » est celle de Judas (elle peut être celle de Mordred ou de Bourbon en 1523). **Non résolu.**
- *Contre-lectures.* Jacques Cœur : exclu par « 900 ans trop loin » et par l'absence de reproche (condamné). Colomb : la couleur/prix de la trahison est difficile à voir, « personnage pur / consensuel » et « pas grand-chose à se reprocher » sont contestables. Aucune ne contredit formellement la FAQ, mais aucune ne relie Avalon.

## 3. É6 : plateau → lettres

Rien de nouveau dans la FAQ. Les lettres des pions (ND CITEAUX / CLAIRVAUX, anagrammes exactes ; FAQ03-058 : « les anagrammes sont parfaites ») restent le mécanisme retenu (`Enigme_06`). Un seul fait : FAQ03-061 « vous avez trouvé tous les C jusqu'à l'avant-dernier. Il en reste deux ».

## 4. Jour dernier et angle de l'É11 (`T3_jour_dernier`, `T3_e11_rhumb_soleil`)

**FAIT (calcul).** Azimuts du soleil à la tour d'Avalon (45,4288 N, 6,0308 E), horizon −0,833°.

| Date | Lever | Coucher |
|---|---|---|
| **30/04/1524 julien** (= 10/05 grég.) | **63,66°** | 296,34° |
| 30/04/1524 grégorien proleptique | 67,97° | 292,03° |
| Marignan 13/09/1515 (julien) | 88,56° | 271,44° |
| Colomb † 20/05/1506 | 57,31° | 302,69° |
| Solstice été / hiver / équinoxe | 54,44° / 123,51° / 89,36° | — |

Le calcul est vérifié sur les équinoxes/solstices (déclinaison ±23,44°, 89,4°).

**HYPOTHÈSE (angle de l'É11).** À **Saint-Palais**, le lever du soleil le 30/04/1524 (julien) est à **64,69°** (64,97° avec un horizon à −0,567°). Le cap Saint-Palais → château Bayard est de **64,99°** (64,97° vers la tour d'Avalon). L'écart est de 0,3° avec l'horizon standard, soit 3,2 km de décalage latéral à 607 km. Or FAQ07-267 exige un angle « quasiment parfait ». Test du hasard :
- 3 jours par an tombent à ±0,3° de 64,99° (0,8 %) ;
- j'ai regardé 6 dates liées à Bayard (Marignan, Brescia, Garigliano, Mézières, mort) : une seule ressort, la mort ;
- le taux de fausses alertes pour « au moins une date sur 6 » est d'environ 5 %.
C'est **intéressant mais pas probant**. Ce qui la renforce : FAQ06-115 (« se tourner vers le ciel » est le bon départ pour un autre élément crucial), FAQ07-104 (la précession n'a pas d'importance : il s'agit du ciel visible aujourd'hui), FAQ07-163 (le jour de gloire est daté jj/mm/aaaa précisément), FAQ05-009 (c'est « l'aide la plus précieuse »), FAQ07-186 (« jour dernier » = un jour, pas un moment). L'idée : la mort de Bayard = le « jour dernier » = le jour de gloire (pas prouvée).

**Ce qui l'affaiblit.** Un auteur qui utiliserait un outil en ligne avec « 30/04/1524 » obtiendrait 67,97° (grégorien proleptique), pas 64,69°. Il faudrait qu'il ait pris 10/05/1524 grégorien. Et la question FAQ07-141 dit que My Maps ne mesure pas les angles : il faut un rapporteur (loxodromie sur Mercator : 67,4° pour la même arrivée). Le 64,99° est un cap géodésique.

**Conséquence pratique (FAIT, calcul).** Pour É12, huit pas de 0,7–0,8 m ≈ 6 m. L'écart entre les azimuts candidats (63,7° et 68,0°) est de 4,3°, soit **≈ 0,45 m** au bout des 8 pas. Il faut donc creuser large autour du point d'arrivée, mais le choix de la date change peu la fouille. L'azimut réel de la boussole diffère aussi de la déclinaison magnétique locale (~+2°) : il faut viser en azimut vrai ou corriger.

## 5. Pistes restantes (au moins 3 vivantes)

1. **Angle 64,99° = azimut du lever du 30/04/1524** (moyenne-faible) : à confronter à d'autres « dernières » dates du narrateur.
2. **6e C = point de passage sur la droite É11** : à tester une fois la zone finale connue (19 candidats en C sur la droite).
3. **9e mot d'É2 = homme en A** : sans conséquence, mais utile pour le fil « personnes en A ».
4. **Compte-les (É10)** : 23 blocs × ? : non tranché.

Abandons : aucune formule « nombre × constante » ne donne 64,99° (0,15 coups attendus par hasard, 0 trouvé). Marignan comme jour dernier : son azimut (88–89°) est incompatible avec l'angle É11 (65°).

## 6. Fichiers

`T3_faq_search.py`, `T3_faq_zones.py` (+ `.out.txt`), `T3_faq_zones2.py` (+ `.out.txt`), `T3_narrateur.py`, `T3_narrateur_faq.out.txt`, `T3_e1_lieues.py` (+ `.out.txt`), `T3_jour_dernier.py` (+ `.out.txt`), `T3_e11_rhumb_soleil.py` (+ `.out.txt`), `T3_c6_e11angle.py` (+ `.out.txt`), `T3_figure_C_666.py` (+ `.out.txt`), `T3_wiki_avalon.py` (+ `.out.txt`), `T3_notes.md`.
