# 02 — Audit du travail existant (notes de Guilhem, lecture seule)

Échelle : **solide / plausible / fragile / invalidée**. Scripts et sorties : `02_Audit_calculs/`.
Distances en **orthodromie** (haversine, R = 6371,0088 km). Coordonnées OSM Nominatim, en cache dans `coords.json`.
⚠️ Les tracés doivent peut-être se faire **sur la carte fournie**, pas sur le globe. La carte manque : les distances ci-dessous restent provisoires.

---

## Énigme 1 — In principio (tracé de l'épée)

| Piste de Guilhem | Verdict | Raison |
|---|---|---|
| Garde, flanc ouest = **cathédrale de León** | **Solide** | « La belle lionne de Léon » renvoie à *Pulchra Leonina*, le surnom de la cathédrale. |
| Pommeau = **cathédrale de Valence** | **Solide** | Terres du Cid (Valence, 1094). Le Saint Calice y est conservé. « La porte des apôtres » est la Puerta de los Apóstoles de la cathédrale. |
| Naissance de la lame = **grotte de Lombrives** | **Solide** | Légende de la princesse Pyrène ensevelie à Lombrives (Ariège) : « le tombeau des Pyrènes ». |
| Pointe = **château d'Urquhart** | **Solide** | Ruine au bord du Loch Ness. Saint Columba et la bête (Vie de Columba, Adomnan). |
| Quillon est = **château de Foix** | **Fragile** | Calcul : RLC → Foix = **53,7 km, cap 275°** (plein ouest ✓), mais cela donne **12,1 lieues communes** (4,444 km), 13,8 lieues de Paris ou 9,7 lieues marines. Aucune unité ne donne « près de 11 » sans choix ad hoc. « Où brûle la mémoire du pays cathare » évoque le **bûcher de Montségur** (1244), mais Montségur est à 35,5 km (8,0 lieues communes, cap 261°). Autres châteaux calculés : Roquefixade 41,5 km (cap 272°, 9,3 l.), Lordat 45,2 km (10,2 l.). **À trancher** : l'unité de lieue voulue, et la mesure sur la carte fournie. |
| Géométrie globale | *Observation* | Sur le globe, Valence → Lombrives (cap 23°) puis Lombrives → Urquhart (cap 347°) : **la lame n'est pas dans l'axe de la poignée**, avec un coude d'environ 36°. Soit la construction se fait sur la carte (projection), soit l'épée n'est pas une droite. L'enluminure R1G montre un tracé en pointillés sur la carte : **il faut la carte**. |

Transcription : Guilhem n'a relevé que la « partie qui nous intéresse ». Le texte complet commence par « Les Asturies dansaient avec les voiles… » et **n'est pas transcrit**. Il faut le relever intégralement (la règle impose de tout relever).

## Énigme 2 — Terra incognita

| Piste | Verdict | Raison |
|---|---|---|
| Solution **Londres / Tour de Londres** | **Solide** | Deux voies indépendantes convergent : la charade et la chute. « Au centre, dès Guillaume, la tour-krak boréale s'éleva, et les joyaux du trône » désigne la White Tower (Guillaume le Conquérant) et les joyaux de la Couronne. Cohérent avec l'enluminure R1D. |
| Réponses de la charade | **Plausible → à corriger** | Avec les réponses de Guilhem, les initiales donnent **TRAIANHVA**. Avec **Octave** (3e : « premier de l'Empire ») et **Odyssée** (7e : « *Ma* septième, épopée », au féminin donc une œuvre, pas Homère), elles donnent **TROIANOVA**, soit *Troia Nova*, le nom de Londres chez Geoffroy de Monmouth. Le mécanisme d'acrostiche devient cohérent. Il reste à justifier la 9e (initiale A attendue : Alexandrie ? cf. la couronne d'or posée par Octave sur le corps d'Alexandre), et « dit LAT. » (latin ? latitude ?). |

## Énigme 3 — Ecce Homo

| Piste | Verdict | Raison |
|---|---|---|
| Tristan & Iseult (TI), Lancelot & Guenièvre (LG) | **Solide** | Deux cases ( _ _ ) par couple, donc les initiales. Le géant, le dragon et le philtre de 3 ans pour Tristan ; le bûcher pour Guenièvre. |
| **Tintagel** | **Solide (renforcé)** | L'enluminure R2G porte un **carré SATOR à trous** (« Complète le carré »). Calcul : les lettres manquantes sont **A, E, N, T**. Avec **TILG**, cela donne **exactement les 8 lettres de TINTAGEL** (8 cases). Cela explique les « NTAE » orphelins de Guilhem. « Ici Pendragon conçut son garçon » : Uther conçoit Arthur à Tintagel (Geoffroy). Réserve mineure : on prend les lettres **distinctes** du carré (A×4, T×4, E×4, N×1 au total). Ce choix reste naturel pour une anagramme. |

## Énigme 4 — Rex dei gratia

| Piste | Verdict | Raison |
|---|---|---|
| Départ = Tintagel (« le garçon » de l'énigme 3) → **Silchester** (Calleva) | **Solide (calcul)** | Tintagel → Silchester = **268,3 km = 181,4 milles romains** (1 mille = 1,4786 km), **cap 72°** (« vers l'orient » ✓). L'écart avec 181 est inférieur à 0,3 %. Chez Geoffroy de Monmouth, Arthur est sacré à **Silchester** par Dubricius. Le 269 et le « Ciltestere » de Guilhem sont confirmés. |
| « Thorn Ey » = **Westminster** | **Solide** | Thorney Island, l'île où fut fondée l'abbaye de Westminster, lieu des sacres. |
| « La dame du lac déplaça les quillons sur ce chemin royal » | **Ouvert** | Instruction de **tracé** : la garde de l'épée de l'énigme 1 est déplacée sur l'axe Tintagel → Silchester → Westminster. Sens exact encore à établir. |

## Énigme 5 — Lux in tenebris

| Piste | Verdict | Raison |
|---|---|---|
| Code 1 = Table ronde de Winchester (chevalier n°.lettre n°) → **Stonehenge** | **Solide** | Calcul avec les 24 noms dans la graphie de la table (liste Wikipedia « Round Table ») et espaces ignorés : **STANENGES**, forme médiévale de Stonehenge chez Henri de Huntingdon (XIIe s.). En comptant les espaces, on obtient STANEGGES : la variante « espaces ignorés » est donc la bonne. Test du hasard : un mot attesté qui sort d'un simple indexage. **L'ordre des noms sur la table physique reste à confirmer** sur une source primaire (photo). |
| Code 2 = « 9-1-7x9-1&2-3-C » → **Carnac** | **Solide** | Rangs des **décimales de π** (« ronde, à la décimale près », « ηὕρηκα » = Archimède) : 3, 1, 3×6 = 18, « 1 » & « 4 » = 14, 1, soit **C A R N A C**. Contrôle : la même règle appliquée à *e* et à √2 donne du charabia (HG??HC, BDJ?DC). « De l'Armorique à la Bretagne » : de Carnac à Stonehenge ✓. |
| Rôle dans la chasse | **Ouvert** | Les deux pierres (Carnac, Stonehenge) forment sans doute un segment de tracé. La suite (énigme 6 : « relie les 4 C ») les réutiliserait. |

## Énigme 6 — Libera nos a malo

| Piste | Verdict | Raison |
|---|---|---|
| Illustration = R4G (Clermont, Hastings, Annonciation, figure au casque) | **Solide** | Cf. 03_Correspondance_illustrations.md. |
| Tour de Londres → Hastings = 86 km | **Fragile** | Tour de Londres → **Battle Abbey** (le champ de bataille de 1066, Senlac) = **76,7 km**, cap 149°. Les 86 km correspondent sans doute à la ville d'Hastings, qui n'est **pas** le lieu de la bataille. Le texte dit « le champ de bataille ». |
| « Tu as les 4 C » | **Non résolu** | Candidats à tester : Carnac (énigme 5), Clermont (R4G), et d'autres toponymes en C des énigmes validées. Rien de tranché. |
| « Figure au casque ailé = Hermès » | **Fragile** | À revoir en HD. Le personnage en rouge de R4G porte une armure. Il peut s'agir de l'archange Michel ou d'un chevalier (« preux contre dieux »). |

---

## Synthèse
- **Solides** : 1 (hors quillon est), 2 (solution), 3, 4 (étapes), 5.
- **À reprendre** : quillon est de l'énigme 1 (Foix ou Montségur, unité de lieue), charade de l'énigme 2 (Octave, Odyssée, 9e), distance de l'énigme 6 (Battle ≠ Hastings).
- **Bloquant transversal** : la **carte au trésor**. Tous les tracés (énigmes 1, 4, 6) en dépendent.
