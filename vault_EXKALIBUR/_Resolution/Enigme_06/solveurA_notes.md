# Énigme 6 — Solveur A : notes (mécanisme « partie → 4 C »)

**Verdict : PAS TROUVÉ.** Aucun mécanisme testé ne sort 4 C de façon plus parlante que le hasard. Je n'ai pas de candidate sérieuse pour les 4 C. Ce qui suit dit ce qui a été lu, ce qui a été testé (scripts et sorties dans `calculs/solveurA_*`), et ce qui manque.

## (a) Inventaire de lecture du panneau (photo 1200×1600, panneau ≈ 380×260 px)

**Plateau** : 3 carrés concentriques + médianes, 24 points, cercle « 10 » au centre, à la place du 25e point qui n'existe pas. Confirmé sur la photo. Je le modélise en 7×7 (col, ligne ; ligne 0 = haut).

**Pions rouges (sphères) : 7 sur le plateau, lecture fiable** (rouge net) :
(3,0), (1,3), (1,5), (3,5), (0,6), (3,6), (4,3). Le dernier est sur le bord du cercle « 10 ».

**Pions bleus (tuiles carrées) : 7 sur le plateau** :
- illustrés : (0,0), (6,0), (1,1)
- non illustrés : (3,1), (4,2), (5,3), (5,5)
- Le releve.md lui-même place le pion moyen (4,2) « haut-milieu du carré moyen » et note le pion (3,1). J'ai relu la photo : ce sont deux pions distincts et non illustrés.

**Position** (`solveurA_position.py`) : 14 pions, donc **10 cases vides = le « 10 » du centre**. C'est tautologique (24 − 14). Ce n'est un indice que si l'auteur a choisi 14 pions pour obtenir 10. Aucun moulin n'est formé. Les menaces sont : rouge en (3,4) et (6,6), bleu en (5,1).

**Hors plateau** :
- pion rouge marqué **« S »**. Le contraste renforcé montre un S net avec une petite pointe à gauche. Je lis « S », pas « 5 ».
- pion bleu marqué **« T »**, sur un pied doré, sous l'ange. Le T est net. Ce n'est pas « IT » : les traits verticaux sont le bord de la tuile.
- Le petit objet rouge en bas à gauche, près du pied du pape : c'est une tache rouge aplatie (pétale, chaussure, tissu ?). Ce n'est pas un pion, il n'y a aucune lettre. Illisible au-delà.

**Figures des pions bleus illustrés : ILLISIBLES à cette résolution.** Chaque tuile fait environ 20×20 px. Ce que j'en tire est de la pareidolie possible, à ne pas utiliser sans photo HD :
- (0,0) : trait diagonal, bras levé, corps allongé horizontal en bas. Peut-être un personnage avec une faux ou un arc, ou un cavalier/centaure.
- (6,0) : deux montants verticaux symétriques avec une tige centrale, sur un socle. Deux piliers, une balance, un portique, des jumeaux ? Indécidable.
- (1,1) : personnage debout avec un bâton vertical à droite, terminé en T ou en Y. Sceptre, trident, marteau ? Indécidable.
- Aucune identification de dieu n'est justifiable. Voir `solveurA_tuiles_bleues.png`.

**Autres éléments lus** : pape mitré (vert clair), trois clochers (Cluny plausible mais pas prouvé), ange vert/orange, Vierge, livre jaune, arbre, personnage roux au casque ailé qui tire une flèche, « HAROLD REX INTERFECTUS EST », « MLXVI » avec 4 cloches dorées.

**Piste d'interprétation notée en passant, non testée** : la FAQ03-265 dit « certains des pions bleus **ne sont pas illustrés**. Doit-on trouver à quoi ou à qui *chacun d'eux* correspond ? » → « En effet, ça pourrait vous être très utile ». Le releve.md la lit comme « identifier les pions illustrés ». La question vise peut-être aussi les non-illustrés. Cela plaiderait pour un mécanisme fondé sur les **positions** (case = lettre, ou case = dieu) plutôt que sur les figures.

## (b) Pistes testées

| # | Piste | Test (script) | Résultat | Statut |
|---|---|---|---|---|
| 1 | Position → lettre. Parcours des 24 cases (lignes, colonnes, anneaux ext→int / int→ext, sens horaire/anti, 8 départs) × alphabets 23/24/26 lettres × sens direct/inversé × sous-ensembles de pions (tous rouges, tous bleus, les deux, ± S, T) → anagramme exacte d'un toponyme | `solveurA_test_alphabet.py` | 0 hit exact. 0 presque-exact | **Écartée** (aucun signal) |
| 1b | Idem avec groupes naturels de cases (anneau, haut/bas/gauche/droite, coins, milieux) | `solveurA_groups.py` | 0 hit sur ma liste curée de 44 toponymes C. 30 hits sur les ~11 800 lieux en C (Cadix, Caligny, Cikal, Cassim, Castin…), tous sur des sous-ensembles arbitraires. Le placement aléatoire des pions donne 5 à 79 hits, moyenne ≈ 30. Le réel est dans le bruit | **Écartée** |
| 2 | Anagramme de phrases du texte et de l'image (« Libera nos a malo », « Pater noster », « Preux contre dieux », « Commencera le Père… », « Harold rex interfectus est », « Sainte Chapelle », etc.) en 1 ou 2 lieux en C | `solveurA_phrases.py` | 0 hit sur 31 phrases. Le nul sur phrases aléatoires donne 3/300 hits à 2 lieux : la méthode ne produit presque rien | **Écartée** |
| 3 | Preux × dieux : noms des Neuf Preux + un dieu (grec, romain, nordique, égyptien, celte, 225 noms) ± S, T → anagramme d'un lieu en C | `solveurA_preux_dieux.py` | 2 hits, tous deux absurdes (César+Set+T → Casterets ; César+Iovis+T → Corveissiat). Le nul (dieux mélangés) donne exactement 2, aussi | **Écartée** |
| 4 | Ensembles de dieux (planètes, jours, Olympiens, Titans, « Père/Ciel ») et sous-ensembles de 1 à 3 noms, ± S, T | `solveurA_dieux_sets.py` | 0 hit significatif. Seuls résultats : Caelus→Cuélas, Ceres+S→Cressé. Nul : même ordre de grandeur | **Écartée** |
| 5 | Noms simples (preux, dieux, Olympiens, etc.) anagrammés directement en un lieu en C | `solveurA_anagram_names.py` | 5 hits, tous absurdes (Caelus→Cuélas, Castor→Castro, Clio→Cilo, César→Ceras). Le nul (mêmes mots mélangés) donne aussi 5 | **Écartée** |
| 6 | « Le Père / les cieux » comme ordre de lecture (Pater Noster, généalogie Cronos→Ouranos) | pas de test seul : il faut d'abord des éléments à ordonner | Aucun élément identifié à ordonner | **Non testable** sans les figures |
| 7 | Contrainte géographique : chaîne des 4 C de longueur 341,6 km ± 1 % (Tour→Battle→Sainte-Chapelle) | `solveurA_chaine.py`, `solveurA_geo_rayon.py`, `solveurA_chemin_coude.py` | Sur 25 C thématiques, 24 198 chaînes monotones sans aller-retour, 7 tombent dans la bande. Taux de base sur des villes en C tirées au hasard : 0,13 % des 4-sous-ensembles. Avec 12 650 sous-ensembles possibles, on attend ≈ 16 hits par hasard, j'en observe 7 : **aucun signal** | **Neutre** (ne discrimine rien) |
| 8 | Alternative pour le lieu très Sainte : les 341,6 km comme repère | `solveurA_geo_rayon.out.txt` | Sainte-Chapelle à 341,6 km, écart latéral à l'axe Tour→Battle −1,9 km (−0,4 km par le releve). Saint-Germain-des-Prés 341,3 km (−1,1 km). L'axe ne distingue pas ces sites. Aucune île sainte ne tombe sur le rayon, hors Paris | **Neutre** |

**Le cas Cluny / Clermont / Cadouin de Guilhem** : sa chaîne à 3 C fait 345,2 km. Le 4e C n'est pas donné par un mécanisme, il est cherché après coup. Deux chaînes de 4 C thématiques tombent dans la bande de 341,6 km ± 1 % (le hasard produit 16 attendus) :
- Clairvaux–Cîteaux–Cluny–Clermont : 340,9 km.
- Conques–Clermont–Cluny–Cousance : 340,6 km. Cousance est arbitraire.

La première est thématiquement jolie (abbayes cisterciennes + Cluny + Clermont), mais elle sort d'un ensemble que j'ai moi-même choisi. **Ce n'est pas une résolution.**

## (c) Meilleure candidate pour les 4 C

**Aucune.** Confiance : nulle pour tout ensemble nommé. Test du hasard : chaque méthode a été comparée à un nul (placements aléatoires des 14 pions, noms aux lettres mélangées, phrases aléatoires). Aucune ne se détache du bruit.

**Pistes à ne pas écarter, mais non testables ici** :
1. **S + T + le « e » de Sainte = STE = abréviation de Sainte.**
   - Les pions S et T sont, selon la FAQ03-354, non remplaçables. Le e de « Sainte » est « un élément plus important » (FAQ03-232), et son teint diffère de celui du reste du mot.
   - Cela pointe peut-être vers le *lieu très Sainte* (Sainte-Chapelle ?) plutôt que vers les C.
   - Pareidolie possible. FAQ03-099 dit que le lieu très Sainte n'est pas l'un des C. À traiter comme piste de recoupement, pas comme mécanisme.
2. **Les 3 tuiles illustrées comme dieux à identifier, avec ordre « Père → cieux »** : impossible sans lire les figures.
3. **Le mécanisme peut être positionnel** (voir FAQ03-265 ci-dessus) : case = lettre, avec un alphabet ou un parcours que je n'ai pas testé (ex. lettres du nom du dieu, comptage par lignes ou anneaux, chiffres lus comme numéros de lettre A=1).

## (d) Ce qui manque

1. **Photo HD de l'enluminure** (surtout des 3 pions illustrés, des 4 pions non illustrés, des 2 hors plateau et des 3 clochers). Le blocage principal.
2. **Vérification du dénombrement des pions** : 14 sur le plateau + S + T = 16. Un mill classique en a 18. Est-ce voulu ? Si des pions sont cachés (par les personnages, le pape, le bas du plateau), le décompte de 10 cases vides ne tient plus.
3. **Ce qu'est l'« anagramme »** : de quelles lettres ? La FAQ04-189 dit « Pas forcément que le lieu d'ailleurs », donc l'anagramme identifie le lieu mais peut être plus longue ou plus riche que son nom. Je n'ai testé que des anagrammes exactes de noms.
4. **Vérification que ces C sont des noms modernes ou historiques** : le jeu emploie « Carnac », un toponyme français, et « tour-krak ». La langue des C (français, anglais, latin médiéval) n'est pas fixée : FAQ04-185 dit que les anagrammes dépendent « des langues et de la prononciation ». Mon test utilise les noms français (communes INSEE), les noms geonames (villes > 15 000 h.) et une liste curée. Pas les noms latins.

## Fichiers produits (`Enigme_06/calculs/`)

Scripts `solveurA_*.py`, sorties `solveurA_*.out.txt`, `solveurA_tuiles_bleues.png`. Les scripts lisent `communes.json` (API geo.api.gouv.fr, généré par `solveurA_fetch.py`) et `cities15000.txt` (geonames), non copiés car trop gros. Les relancer nécessite de les régénérer dans le dossier de travail.
