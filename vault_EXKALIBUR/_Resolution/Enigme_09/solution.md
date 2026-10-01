# Énigme 9 : Noli me tangere

**Statut : ✅ VALIDÉE par Guilhem le 30/09 pour le lieu (avant-dernier C = Chartres ; Chambord en réserve) ; ❓ OUVERT pour le 1er paragraphe (narrateur, jour de honte, jour de gloire).**
Consigne de Guilhem : sur les dernières énigmes, le Discord relève surtout de la supposition. Rien n'est pris pour acquis.

## Texte (photos HD IMG_4356 et IMG_4357)
> Il combattit vaillamment, jusqu'à ce que l'adversaire lui porte un coup mortel. « Adieu mes frères. N'abandonnez pas la quête. Souvenez-vous toujours, dans les moments de doute, de vous tourner vers le ciel. » Je jurai de garder l'objet tant convoité, et me retirai. Un millénaire a passé, et tout ce dont je me souviens, c'est le prix de la trahison, et sa couleur. Pour en conjurer le sort, je transformerai ce jour de honte en jour de gloire. D'ici là, j'arrivai à la croisée des chemins, entre la garde et le royaume, et parcourus la même distance des 4C, vers l'Est, jusqu'à l'avant-dernier C.

Lettrine : un **labyrinthe** circulaire (FAQ03-046 : bleu royal tirant vers le violet).

## Partie géographique (FAQ03-262 : le tracé final ne dépend pas du 1er paragraphe)
| Élément | Lecture | Nature | Confiance |
|---|---|---|---|
| la garde | **nouvelle garde É7** (Sainte-Chapelle → Rennes → Lorient) | acquis É7 | haute |
| le royaume | **É5** : « de l'Armorique à la Bretagne, sur ces pierres, je bâtirai mon royaume » → droite **Carnac → Stonehenge** (FAQ06-219 : le royaume est « plus vaste que celui des pierres dressées ») | lecture du texte | moyenne-haute |
| croisée des chemins | intersection des deux segments : **47,8321 N, −3,0050**, à 0,4 km de **Camors** (Morbihan) | calcul | haute (si les deux lignes sont justes) |
| même distance des 4C | **340,9 km** (FAQ03-047 : « la même distance que les quatre C ») | acquis É6 + FAQ | haute |
| vers l'Est | cap ≈ 77°, donc « vers l'Est » au sens large, pas plein Est | texte | moyenne |
| avant-dernier C | **cathédrale de Chartres**, à **340,26 km** (écart −0,19 %) | calcul + lettrine | voir ci-dessous |

### Pourquoi Chartres plutôt qu'un autre lieu en C
- **La distance seule ne suffit pas.** Dans l'anneau de 340,9 km ± 1 % vers l'est (cap 45 à 135°), 29 communes françaises commencent par C (`calculs/O_verif_5eC.out.txt`).
- **Chartres est le seul de ces lieux relié à un indice indépendant** : la lettrine de l'énigme est un labyrinthe circulaire, et le labyrinthe de la cathédrale de Chartres est le plus célèbre au monde.
- **Chambord** (339,1 km, cap 92°, presque plein Est) est le seul autre candidat avec du sens : Jérusalem céleste, escalier. Il n'a aucun lien avec le labyrinthe. Le modérateur Sieur Eric a écrit (30/08/2026) « Chambord n'est pas le dernier C » ; cela ne dit rien de l'avant-dernier. Piste gardée vivante, à un rang inférieur.
- **Contrôle** : avec les autres croisées possibles (garde É1 ou lame É1), Chartres et Chambord sont à plus de 250 km de l'anneau. Le résultat dépend donc bien de la lecture garde É7 × royaume É5.
- **Discord** : Loptr (22/06/2025) trouve Chartres à 341 km par un raisonnement voisin. Plusieurs joueurs donnent « CdC » (cathédrale de Chartres) en 5e C, « donné par une illustration ». Ce sont des appuis, pas des preuves.

## 1er paragraphe : OUVERT (hypothèses seulement)
- **FAQ** : « jour de gloire » daté au jour près (FAQ07-163), « aide la plus précieuse de la chasse » (FAQ05-009). Le « prix de la trahison » a une valeur numérique et une couleur métallique (FAQ07-022) ; la couleur du jour de gloire est la même que celle du jour de honte (FAQ05-129). « Un millénaire » = environ 1 000 ans, 900 est trop loin (FAQ07-060).
- **Hypothèse dominante au Discord, contestée** : prix de la trahison = 30 deniers d'argent (Judas). Jour de honte = Camlann (Arthur tué par Mordred). Narrateur = Bayard (mort en 1524), avec comme jour de gloire l'adoubement de François Ier à Marignan (14/09/1515). Objections : FAQ06-087 (le narrateur a dû « racheter ses fautes »), des anachronismes. D'autres candidats circulent : Jacques Cœur, Colomb.
- **Rien n'est validé ici.** Ce paragraphe sert aux énigmes suivantes (FAQ05-168 : « utiles pour toute la chasse »). À reprendre quand une énigme en aura besoin.

## Pistes écartées
| Piste | Raison |
|---|---|
| Garde É1 (León–Foix) comme « garde » | la garde a été déplacée en É7 ; la croisée tombe en Galice, et 340,9 km Est ne mènent à aucun C pertinent |
| « Royaume » = chemin royal É4 | pas d'intersection en Europe avec aucune des deux gardes |
| Le Mans (342 km plein Ouest de Clairvaux) | ne part pas d'une croisée garde × royaume |

## Variantes du « royaume » sans la ligne de l'É5 (demande de Guilhem, 30/09) : `calculs/O_variantes_royaume.py`
Règles : (a) 340,9 km plein Est ; (b) anneau ±1 %, cap 45-135°, avec une liste de lieux en C notables fixée avant le calcul.
| Croisée | Où | (a) plein Est | (b) lieux notables dans l'anneau |
|---|---|---|---|
| **A. réf. garde É7 × royaume É5** | Camors (56) | Cravant (45) à 1,2 km | **Chartres, Chambord**, Cravant |
| B. garde É7 × lame É1 | Monterfil (35), Brocéliande | Chapelon (45) à 3,4 km | aucun (Corbeil-Essonnes à 333 km, hors tolérance) |
| C. Sainte-Chapelle (garde × chemin du Conquérant) | Paris | Cutting (57) à 12 km | aucun |
| D. garde É7 × frontière Bretagne/Maine | Juvigné (53) | Courgenay (89) à 5 km | aucun |
| E. garde É1 × lame É1 | Pyrénées, Larrau | rien à moins de 22 km | aucun (Collioure à 332 km, −2,6 %) |
| F. garde É1 × royaume É5 | océan (Galice) | rien | aucun |
| G/H. garde É7 × chemin royal É4 | pas de croisement en Europe | écarté | écarté |
**Conclusion** : aucune autre lecture ne produit un lieu en C porteur de sens. Seule la lecture A donne des candidats notables, ce qui renforce le royaume = É5. Plein Est depuis A, on tombe sur Cravant (45), village sans lien connu : c'est du bruit, et le « vers l'Est » est donc à lire au sens large. Le choix entre Chartres et Chambord reste à trancher (lettrine labyrinthe → Chartres).

## Pourquoi « royaume » = Carnac → Stonehenge : lore et déduction (30/09)
**Déduction**
1. « entre **la garde** et **le royaume** » met deux objets sur le même plan. La garde est une ligne déjà tracée (É1, puis É7). Le royaume doit donc être, lui aussi, un objet déjà construit dans la chasse : c'est la règle de réemploi observée partout (É6 reprend la Tour d'É2, É7 la Sainte-Chapelle d'É6, É9 la distance d'É6).
2. Le mot « royaume » n'apparaît que dans deux textes :
   - **É4** : « l'aurore… embrassait le royaume ». C'est un décor, sans lieu. La ligne définie dans É4 s'appelle « **chemin** royal », et la Dame du Lac y déplace les **quillons** : elle relève donc de la garde, pas du royaume (interprétation).
   - **É5** : le roi définit lui-même son royaume, avec deux bornes : « de l'Armorique à la Bretagne, **sur ces pierres, je bâtirai mon royaume** ». Les deux codes donnent justement CARNAC et STANENGES.
3. La **FAQ06-219** (classée #LUXINTENEBRIS) : « le royaume est plus vaste que celui des pierres dressées ? » → « Oui, tout à fait ». L'auteur reconnaît qu'il y a un royaume dans É5.
4. **Géométrie** : c'est la seule lecture où les deux lignes se croisent dans la zone de jeu, sur leurs segments, et mènent à des lieux en C notables.

**Lore**
- « Armorique » = la Petite-Bretagne ; « Bretagne » = la Grande-Bretagne, au sens médiéval. Chez Geoffroy de Monmouth et Wace, le royaume d'Arthur s'étend des deux côtés de la Manche, et le peuple celte est le même (écho d'É1, « la mission des Celtes », et d'É4, « le peuple celte »).
- Les deux bornes sont les plus grands sanctuaires de pierres dressées. Stonehenge est la « Danse des Géants » dressée par Merlin (Geoffroy de Monmouth) ; Carnac, ce sont les alignements.
- Dans É5, le roi tire l'épée **puis** fonde son royaume sur les pierres, dans la même scène. La « croisée entre la garde et le royaume » d'É9 reprend cette image : l'épée posée en croix sur le royaume.
- La croisée tombe en Armorique (Camors, Morbihan), sur la garde qui vient de traverser Brocéliande.

**Limites**
- L'argument le plus fort est textuel (points 1 à 3). Le « renfort » par le calcul est modeste : c'est une élimination parmi les lectures que j'ai imaginées, et la liste de lieux notables contenait Chartres dès le départ.
- La FAQ05-160 (« la garde et le royaume doivent-ils se toucher ? ») : l'auteur ne répond pas.
- « Plus vaste » pourrait aussi désigner une zone (Grande-Bretagne + Armorique), et non une ligne. Testé (variante D, entrée de la garde en Bretagne) : rien n'en sort.
