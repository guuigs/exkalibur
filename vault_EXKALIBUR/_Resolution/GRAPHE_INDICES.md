# Graphe des indices : la chasse vue comme un seul système

> Pour qui : l'orchestrateur et tous les sous-agents. **À lire avant de toucher une énigme.**
> But : une énigme ne se résout pas seule. Chaque élément (mot, symbole, lieu, distance) est un **nœud**. Une solution
> n'est retenue que si elle **consomme** ses nœuds de façon cohérente et **nourrit** les énigmes suivantes.
> Mis à jour à chaque énigme validée. Statuts : ✅ acquis · 🟡 probable · ⚪ ouvert · ❌ écarté (avec la raison).

## 1. Règles de pensée (le filtre rapide)

1. **Consommation** : dans une chasse fermée, l'auteur ne met pas de décor inutile. Une solution candidate doit expliquer
   *chaque* élément du texte et de l'enluminure, ou dire lequel reste et pourquoi. Plus elle laisse d'éléments de côté,
   plus elle est suspecte.
2. **Chaînage** : une solution qui ne sert à rien plus loin (pas de lieu réutilisé, pas de distance reprise, pas de
   tracé sur la carte) est suspecte. La chasse **construit une épée** sur la carte (lame, garde, quillons) : chaque énigme
   pose une pièce.
3. **Test du nul** : tout motif (distance, alignement, anagramme) est comparé à ce que le hasard produit. S'il est dans
   le bruit, on l'écarte **tout de suite**, par écrit, sans le relancer autrement.
4. **Élimination en 3 questions** (moins de 5 minutes, avant tout calcul lourd) :
   - (a) Le candidat contredit-il une réponse de la FAQ officielle ? → ❌
   - (b) Contredit-il un nœud déjà ✅ (lieu, distance, direction) ? → ❌
   - (c) Explique-t-il au moins 2 éléments indépendants (texte + image, ou texte + calcul) ? Sinon → ⚪, pas 🟡.
5. **Shark d'abord** : avant de lancer des solveurs, on cherche le consensus dans le salon Discord de l'énigme. Le
   consensus reste une **hypothèse**, qu'on vérifie par le calcul et par le filtre ci-dessus.
6. **Fait / hypothèse / intuition**, chacun avec un niveau de confiance. On préfère « pas encore trouvé » à une solution
   séduisante.

## 2. Les fils rouges (nœuds transverses)

| Fil | Où il apparaît | Ce qu'on en sait | Statut |
|---|---|---|---|
| **L'épée sur la carte** | É1 (garde + lame), É4 (« la dame du lac déplaça les quillons »), É7 (« trace la nouvelle garde »), …, fin | Le tracé final est une épée reconstruite pièce par pièce ; le coffre en découle | ✅ principe / ⚪ pièces |
| **Tour-krak = Tour de Londres** | É2 → É6 | Même tour (FAQ04-010) | ✅ |
| **Lieu très Sainte = Sainte-Chapelle** | É6 (arrivée) → É7 (départ) → É8 ? | Même lieu (FAQ03-005, 03-288) ; É6 arrive à 0,68 km | ✅ |
| **Les C** | É6 (4 C) → 5e C (Chartres ?) → 6e C | 6 C au total, reliés en une figure (FAQ 8) | ✅ 4 C / 🟡 5e / ⚪ 6e |
| **Distance des 4 C ≈ 341 km** | É6 → Noli me tangere (« la même distance que les 4 C ») | Longueur de la chaîne = 340,9 km | ✅ |
| **L'épée : nouvelle garde** | É7 | SC → Lorient ≈ parallèle à León → Foix (7,6°), ⊥ lame (86°) | 🟡 |
| **Le roi** | É4 (Rex dei gratia) = É7 (Sub rosa) | Même roi (FAQ04-036, 07-197) | ✅ |
| **Guillaume le Conquérant / Bayeux** | É6 (Hastings, 1066), É7 (Bayeux, « le Conquérant ») | Tapisserie de Bayeux | ✅ thème |
| **Unités anciennes** | É1 lieues, É4 milles romains, É12 stades | Varient selon l'énigme | ✅ principe |
| **Chiffres romains de la rose** | Carte officielle (I–VIII à la place des directions) | À utiliser dans une énigme tardive | ⚪ |
| **Montsalvage** (indice du 04/06/2026) | « son écu se dresse à dextre du cheval » | Ancienne capitale, écu sur la carte ? | ⚪ |

## 3. Nœuds par énigme (entrées → sorties)

| É | Consomme | Produit (réutilisé plus loin) | Statut |
|---|---|---|---|
| 1 | Texte, R1G | Garde León → Foix ; lame Urquhart → Valence | ✅ |
| 2 | TROIANOVA | Londres / **Tour de Londres** | ✅ |
| 3 | SATOR | Tintagel | ✅ |
| 4 | milles romains | Silchester (181,4 milles) ; le roi | ✅ |
| 5 | STANENGES, π | Stonehenge, Carnac | ✅ |
| 6 | Plateau (anagrammes), Tour, Battle | **4 C**, **341 km**, **Sainte-Chapelle** | ✅ |
| 7 | Sainte-Chapelle, Evad. Ecfv → REDNES (Rennes), déroute de Conan, Brocéliande | **Nouvelle garde SC → Rennes → Paimpont → Lorient** (cap 256°, parallèle à l'ancienne garde) ; restent la balance, les 2 juments, la lance, la rose | 🟡 forte |
| 8–12 | — | — | ⚪ |

## 4. Pistes écartées (on n'y revient pas sans élément nouveau)

| Piste | Énigme | Raison |
|---|---|---|
| Lecture Pater brute du plateau (400 parcours) | É6 | Bruit (T1) |
| 4 C liés à une boisson | É6 | Bruit (U1) ; solution trouvée ailleurs |
| Preux/dieux → anagrammes de lieux | É6 | Bruit (U2) |
| Cluny → Clermont → Cadouin (3 C) | É6 | 3 C seulement ; remplacé par la chaîne à 4 C |
| Garde de Sub rosa « métaphorique » | É7 | FAQ03-088 : tracé géographique réel |
| Forêt d'Orient (Aube) comme « l'Orient » | É7 | Hors déroute ; la droite imposée par le texte passe par Rennes |
| Dol / Dinan comme point de la déroute | É7 | La complétion donne REDNES ; Dol et Dinan ne donnent rien |


## É8 Ultima cena (30/09, 🟡 probable)
- Entrées : Sainte-Chapelle (rose de l'Apocalypse, 18 pétales ; île de la Cité = départ).
- Sorties : **Payns** (Hugues de Payns), réutilisée dans *Omnia vincit amor* d'après le Discord.
- En réserve : Lincoln (plus haute tour, Dean's Eye et Bishop's Eye) ↔ Hugues d'Avalon ↔ tour d'Avalon (zone finale ?). Le fil « trois Hugues » est à suivre.
- Écartés : Lindisfarne, 666 stades, 33²+18² → Borce.

## É9 Noli me tangere (30/09, 🟡 lieu probable, 1er paragraphe ouvert)
- Entrées : garde É7 + royaume É5 (Carnac → Stonehenge) → croisée près de **Camors** ; distance 340,9 km (É6).
- Sortie : **avant-dernier C = cathédrale de Chartres** (labyrinthe de la lettrine). Il reste un C, le dernier.
- Ouvert : narrateur, jour de honte, jour de gloire, prix de la trahison (30 deniers d'argent ?) → pour les énigmes 10 à 12.
- Piste secondaire : Chambord (plein Est, 339 km).
- Note : la croisée tombe à 0,4 km de Camors, un autre nom en C. Coïncidence possible, à garder à l'œil.

## É10 Omnia vincit amor (30/09, 🟡)
- Entrées : Hugues de Payns (É8) → Règle du Temple → 10e père = Châlons (C). Le fil « Templiers » (É6 Clairvaux/Cîteaux, É8 Payns, É10 Règle) se confirme.
- Sorties : **Eilean Donan** (gardienne), **Machrie Moor / Arran** (le roi Fingal), **193,1 km** (→ É11 *Consummatum est*), un nombre « compte-les » (ouvert → É11/É12).
- Barque (enluminure et carte) : le roi rejoint la gardienne en barque ; l'É11 « jette l'ancre depuis Montsalvage » : même motif.

## É11 Consummatum est (30/09, 🟡)
- Entrées : 193,13 km (É10) ; π (« parfaitement », É5 Table ronde) ; épée (Joyeuse) ; narrateur/dernier chevalier (Bayard, fil ouvert depuis É9).
- Sorties : **Saint-Palais** (Montsalvage) → **château Bayard** (606,62 km = D·π, −0,016 %). Tour d'Avalon à 1 km (Hugues d'Avalon ↔ Lincoln É8).
- Fil « narrateur = Bayard » : É9 (jour de honte / gloire, Marignan), É11 (dernier chevalier). À vérifier en É12.
- Ouvert : dérivation de l'angle (64,99° géo ; 72,09° / lame É1).

## É12 Ad vitam aeternam (30/09, 🔴 sauf départ 🟡)
- Entrées : droite É11 prolongée → **tour d'Avalon** (+1,07 km après Bayard, FAQ07-256 « très finement ») ; Avalon ↔ Hugues de Lincoln (É8 « plus haute tour ») ; coupe = enluminure R5G (FAQ07-005).
- Ouvert : 3e et 11e (10 stades = 1,85 km), clairière (terrain), jour dernier (azimut), pas.

## Revue globale (30/09, après les 12 énigmes) : voir `Revue_globale/00_SYNTHESE.md`
- **Tour d'Avalon** 🟡+ : droite É11, É8 (Lincoln / Hugues d'Avalon), enluminure 12 (tour effondrée, deux yeux, cloche = Lincoln ; Glastonbury Tor), FAQ07-019 (É8 + enluminure 12 concaténés = « très précieux »).
- Enluminure 12 : vieillard à la scie = saint Simon (11e apôtre, Mt 10) ? D'où la piste 3e/11e = apôtres (Jacques / Simon), non placée sur le terrain.
- Rayure de l'épée : forme seule (FAQ06-161, 03-059) ; aucun cours d'eau de la BD TOPO ne correspond (contrôle miroir), il faut le LiDAR ou le terrain.
- Narrateur = Bayard 🟡 ; angle É11 et « jour dernier » = lever du soleil le 30/04/1524 (hypothèse).
