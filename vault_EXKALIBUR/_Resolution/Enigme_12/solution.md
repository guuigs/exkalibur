---
tags:
  - "#exkalibur"
---
# Énigme 12 : Ad vitam aeternam

**Mise au propre le 01/10/2026.** Le détail chronologique d'avant le nettoyage est dans `../_archive_brut_2026-10-01.zip`.

> **Statut : 🟡 départ probable (secteur tour d'Avalon / Rue du Rempart) ; 🔴 le reste n'est pas résolu.**
> Aucune zone de 50 m défendable à ce jour. Les troisième et onzième ne sont pas identifiés, ni la clairière, ni la grande roche, ni la souche.
> Règle : on préfère « pas encore trouvé » à une zone séduisante. Une zone ne sera annoncée qu'avec un décompte et un contrôle indépendant.

## 1. Texte (photo HD IMG_4359)
> Dieu sut se montrer favorable ; dix stades romains séparaient les troisième et onzième. Le roi avait rejoint les fées, et laissé son épée aux portes d'Avalon. L'épée, évidemment. L'épée, depuis toujours ! Là était la dernière clé de la quête du Graal. Tombée par trois fois, elle était revenue là où elle n'avait jamais cessé d'être.
> Tout commence et tout s'achève. J'entends le chant retentir. J'ai fait une dernière veille au chemin de rempart, et l'endroit m'est apparu au matin, illuminé par l'astre glorieux qui magnifiait le ruisseau.
> Dans la clairière, à la jonction des chemins, j'ai suivi à senestre les eaux enchantées jusqu'à la grande roche, puis fis dix pas au nord, autant à l'est. Arrivé à la souche-majesté, je fis huit derniers pas, et ma boussole suivait le jour dernier.
> Là, tu trouveras la coupe du charpentier.

**Parcours à rebours** : coffre ← 8 pas à la boussole ← souche-majesté ← 10 pas N + 10 pas E ← grande roche ← eaux enchantées suivies à senestre ← jonction de chemins dans la clairière ← 3e et 11e + distance + départ ← chemin de rempart. Les trois séries de pas font ≈ 35 m en tout : **toute la difficulté est de trouver la clairière ou la roche**.

## 2. Établi (faits vérifiés ou sources officielles)
| Fait | Source / calcul | Niveau |
|---|---|---|
| L'arrivée de l'É11 est le départ de l'É12 | FAQ05-195 | officiel |
| Arrivée É11 : Saint-Palais → ×π de 193,13 km = 606,74 km, cap 64,99° → **≈ 50 m du château Bayard** | script `O_verif_consummatum.py` (dossier É11) | calcul |
| La même droite prolongée de 1,07 km passe par la **tour d'Avalon** (cap 64,97°) | calcul ; FAQ07-256 « si vous devez dépasser le lieu du dernier chevalier, ce sera très finement » | calcul + FAQ |
| Avalon = gaulois *abalon* = « la pommeraie » ; vivier creusé en 1261 ; Hugues d'Avalon (évêque de Lincoln, attribut : un cygne) né dans le donjon | rapport Jago « La tour et l'étang d'Avalon » | source tierce lue en entier |
| L'étang d'Avalon est un **Espace Naturel Sensible** (2009) ; bâtiments à 44-95 m de la mare ⇒ pas la zone du coffre (FAQ05-107 et FAQ8) | Jago, isere.fr, orthophoto IGN | vérifié |
| **Rue du Rempart**, Saint-Maximin (45.42977, 6.03118), à 82 m de la tour : voie publique | BAN / OSM | vérifié |
| Tour d'Avalon : 407 m d'altitude, vue ouest/sud, rien vers le sud-est | LiDAR IGN 2 m | calcul |
| « Jour dernier » = 30/04/1524 (mort de Bayard) | validé par Guilhem ; lever à 63,7° (calendrier julien) | validé |
| Stade romain = 185 m ; 10 stades = **1 850 m à ±1 %**, en ligne droite | FAQ05-172, FAQ07-120 | officiel |
| Le coffre est éloigné de tout bâtiment ; terrain public, hors monument historique et hors zone protégée | FAQ05-107, FAQ8 | officiel |

## 3. Règles de l'auteur (FAQ)
**Troisième et onzième**
- Même nature (FAQ06-009), un seul de chaque (FAQ06-216), difficiles à trouver (FAQ06-292), trouvables de chez soi (FAQ04-114). Le 3e ne donne pas d'écharde pieds nus, le 11e peut en donner (FAQ07-068). Aucun lien avec un chevalier en particulier (FAQ07-065).
- Ils servent à identifier la clairière, avec la distance et le départ (FAQ07-133, FAQ07-180, FAQ06-166). Il faut marcher surtout sur l'un des deux (FAQ06-247). On peut aller de l'un à l'autre en passant par des étapes intermédiaires (FAQ04-115).
- Ils sont « l'une des clés » et visibles sur les enluminures ; l'enluminure 11 aide à en placer « une partie » (FAQ05-093, FAQ07-239).
- Rangs : « huitième et seizième » donnerait un résultat incorrect (FAQ8) : les rangs 3 et 11 comptent en eux-mêmes. « Le treizième ne vous mènerait pas au bon endroit » (FAQ06-133). **Le 13e n'est pas dans l'énigme** : c'est une déduction de cette seule réponse.
- Personne ne les a correctement identifiés (FAQ06-109, FAQ07-236). **Leur nature différente est une simple supposition de Guilhem** ; la FAQ dit « même nature ».

**Paragraphe 1**
- Il est lié à la suite « d'un point de vue spatial et topographique » (FAQ06-069).
- « Dieu sut se montrer favorable » : 25 lettres, laissées en français dans la version anglaise (FAQ07-218), crucial, agit comme confirmateur de la zone (FAQ07-088).
- Identifier le roi qui a rejoint les fées n'aide pas pour les 3e et 11e (FAQ05-094). Le point-virgule ne lie pas forcément les deux moitiés (FAQ07-201).
- La « dernière clé » : une dernière intuition, cruciale pour trouver la clairière (FAQ8). L'épée réelle (triquetra, dragon) est très utile.

**Lieu**
- Le chemin de rempart est un point précis (FAQ07-268), accessible toute l'année (FAQ06-020), « d'un mur ou d'une tour », pas une formation naturelle (FAQ8). Il n'est pas l'un des chemins de la jonction (FAQ06-025).
- La clairière est la jonction de chemins, un croisement de sentiers au sens premier (FAQ06-005), visible à l'œil nu depuis le rempart et proche (FAQ05-155, FAQ06-244). Personne ne l'a trouvée (FAQ06-102, FAQ06-269, FAQ07-149).
- La grande roche bloque le passage (FAQ03-211 : très difficile à manquer). On la rejoint en suivant les eaux enchantées (FAQ06-195), qui coulent jusqu'à elle et au-delà (FAQ03-082). On la touche sans danger, mais difficilement sans se mouiller (FAQ06-180, FAQ06-198). Elle n'est pas visible sur Google Maps (FAQ07-126). Les 10 pas partent de « l'étape d'après » (FAQ06-178), avec une seule étape entre roche et souche (FAQ07-182). La souche n'est pas visible depuis la roche (FAQ06-167).
- Pas : même unité pour les 10 + 10 + 8 (FAQ06-034, FAQ06-204). Boussole réelle (FAQ06-282). Pas de neuvième pas : on creuse (FAQ05-039, FAQ06-043).
- Pour trouver la jonction, il faut concaténer plusieurs choses (FAQ06-206). On peut creuser « partout dans le domaine public tant que ce ne sont pas des zones protégées » (FAQ8). 3 équipes sont passées à moins de 150 m du coffre (FAQ8).

**Illustrations**
- La coupe de l'enluminure 9 est la coupe du charpentier (FAQ07-005). Le contour de son bassin est exploitable (FAQ03-308, FAQ07-052). Ses 6 dessins du ciel s'interprètent une fois la zone trouvée (FAQ06-067), et ne donnent pas le « jour dernier » (FAQ8 : il ne faut pas lever la tête).
- Anneaux dorés : leur nombre accroché à un élément est important, « oui, tout à fait » (FAQ06-205). Il faut compter les chaînons de la biche, il n'y en a pas qu'autour du cou (FAQ06-176). Leur usage se comprend « sans beaucoup de prérequis » (FAQ05-166). Les maillons sont « un peu partout » et c'est à nous de déterminer ce qu'on en fait (FAQ03-125).
- Enluminure 11 : quatre pierres aux couleurs de cartes ; lettres **D et C seulement**, et le C du trèfle n'est pas un 2 à l'envers (FAQ03-335, FAQ03-137). Ne pas compléter les pierres carreau et pique avec des lettres ; « notez le point d'interrogation » = un **nombre** (FAQ05-091, FAQ05-163). La place de chaque pierre est importante, telle quelle (FAQ06-058). Pierres à symboles et pierres de la croix (R) = deux éléments distincts (FAQ07-035).

## 4. Ce qu'on lit sur les illustrations (observé)
- **Lame de l'épée centrale** : un tracé en zigzag (fichier `Revue_globale/rayure_epee_guilhem.svg`, 77 segments, tronc de 64 sommets descendant à ≈ 170°, un embranchement et une petite boucle), trois losanges dans le pommeau, un anneau d'or (maillons) sur le côté droit du manche, l'inscription SCRIPSIT XXV.
- **Enluminure 9** : soldat romain (casque à crinière rouge, cape rouge) qui tient **un maillon de chaîne en or** (ni lance, ni bannière), crâne aux pieds, rocher blanc à coupe, étang avec 2 poissons dorés et des cygnes, ruisseau, arbre à fruits dorés. Ciel : loup + glyphe blanc (« V » + signe à boucle fermée, lu comme ♀ avec réserve), étoile, arc-en-ciel, âne + émeraude, diamant + ancre, croissant.
- **Chaînes d'or** : cou de la biche (enl. 3), 4-5 maillons ; garde de l'épée, 2 maillons + un élément plat gravé ; patte du dragon (enl. 11), 1-2 maillons en « 8 » ; soldat (enl. 9), 1 maillon. **Décompte à faire à la photo HD**, panneau par panneau.
- **Enluminure 11** : dragon blanc à 3 têtes ; quatre pierres ♥ + D (haut gauche), ♣ + C (haut droite), ♠ (bas gauche), ♦ (bas droite) ; trois nombres : **3** (blanc), **√5** (rose, le signe racine est confirmé par Guilhem sur l'original), **1** (bleu) ; une croix de pierres de 11 cases par bras, centre vide, avec des **R en 5e et 11e position** (lecture du schéma de Guilhem, non recomptée sur la photo).
- **Enluminure 12** : voir `illustration_e12.md` (tour effondrée à deux yeux = Lincoln, vieillard à la scie, sanglier rouge).

## 5. Pistes vivantes (aucune validée)
| # | Piste | Pour | Manque / prochain test |
|---|---|---|---|
| P1 | **3e = biche de Cérynie, 11e = pommes d'or (dragon Ladon)** : 3e et 11e travaux d'Hercule (liste d'Apollodore). Enl. 3 = biche à chaîne d'or, enl. 11 = dragon blanc à chaîne ; Avalon = pommeraie | rang + animal exacts pour 3 et 11 ; FAQ02-117 (pommes), FAQ02-288 (mythologie), FAQ07-221 (question joueur sur les travaux, non démentie) | aucune paire de lieux à 1 850 m ; les autres enluminures ne suivent pas l'ordre des travaux ; « 13e » incompatible avec 12 travaux. Idée : les 3e/11e seraient une **clé** qui dit quoi mesurer, pas deux lieux nommés |
| P2 | **Croix de l'enl. 11 comme gabarit** : R à 1 et 5 cases du centre sur chaque bras ⇒ produit 5 sur les deux bras, les 4 R sont sur un cercle de rayon √13 ; 1, 3, √5 = distance proche, moyenne, moyenne géométrique | les trois nombres colorés décrivent exactement cette géométrie ; les R en 5 et 11 | à quoi sert-elle sur le terrain ? Tester des carrefours dont deux branches font 1 et 5 unités (unité = 231 m si 8 cases = 10 stades) avec témoins aléatoires ; sens exact des R à recompter |
| P3 | **Comptage des maillons** par enluminure et sur la lame | FAQ06-205, 06-176, 05-166 | décompte maillon par maillon sur les photos HD ; définir ce qu'on compte |
| P4 | **Grande roche = rocher de l'épée** (rocher blanc à coupe de l'enl. 9), eaux enchantées = ruisseau | FAQ06-210, FAQ07-005, FAQ03-148 (question de joueur) | un ruisseau de moins de 1 km de la tour qui coule vers une roche sur terrain public : absent de la BD TOPO ; LiDAR 2 m insuffisant |
| P5 | **Ruisseau de Tapon / La Planta** (1,3-1,5 km ENE) : seul ruisseau de pente avec verger | verger à 14 m du ruisseau ; azimut proche du lever | maisons à 35 m ; aucune clairière ni roche à l'œil sur l'orthophoto ; à vérifier sur le terrain |
| P6 | Les 3e/11e comme stations d'un parcours nommé ; solution = nom du chemin entre les deux (idée de Guilhem, logique de la Passion) | cohérent avec la Passion de toute la chasse | aucun chemin de croix dans les données (BD TOPO, OSM, Wikidata) ; chapelles/oratoires non exclus |

## 6. Pistes abandonnées (et pourquoi)
| Piste | Raison |
|---|---|
| Zones A/B/C (Chêne-Roche-Vivier, Pierre Gros, Corbassière) | coïncidences de noms sans base ; bâtiments à 57-88 m (FAQ05-107) |
| Étang d'Avalon comme zone du coffre | ENS + bâtiments proches ; reste un repère de départ |
| Nombre d'or 1 850/φ = 1 144 m | la distance Bayard-tour varie de 622 à 2 036 m selon D et le cap ; ~7 % de chances au hasard avec une constante parmi 12 |
| Azimut du lever comme mécanisme principal | FAQ07-180 : ne pas s'en obnubiler ; aucun ruisseau ≤ 100 m à 1 850 m dans le secteur 56-75° |
| Rayure de la lame : profil d'altitude, tracé de chemin ou de ruisseau, code de virages G/D | corrélation max 0,93 contre 0,72-0,99 pour des courbes aléatoires ; pas mieux que le miroir ; 62 virages sans paliers, aucune lecture |
| Phrase de 25 lettres : anagrammes, palindromes, Vigenère, SATOR 5×5, valeurs numériques, lecture inversée sur 2 410 toponymes | aucun résultat ; « AVALON » formable par hasard dans ~6 % des fenêtres |
| Classes d'objets BD TOPO/OSM à 1 850 m (17 classes, croix, ponts, fontaines…) | toutes au niveau du hasard |
| Chemin de croix proche de la tour, apôtres en toponymes | aucun chemin de croix dans OSM (4 km) ; 15 toponymes d'apôtres, aucune paire à 1 850 m |
| Cartes à jouer pour placer les 3e/11e | Bayard est le seul chevalier local ; aucun nom de carte utile autour ; cartes ↔ chevaliers relèvent de l'É11 |
| 3e/11e = ponts d'un même cours d'eau (72 cours d'eau, BD TOPO + OSM, 128 numérotations) | 0 paire à 1 850 ±18 m avec l'un des deux près de la tour ; taux 2,3 % ≈ hasard (0,9-2,2 %) — `Revue_globale/T15_T17/T15_ponts.*` |
| 3e/11e = stations d'un chemin de croix réel | aucun chemin de croix extérieur à stations numérotées à ≤ 6 km ; croix quelconques : 2 paires à 1 850 m pour 2,0 attendues — `T15_chemin_croix.*` |
| 3e/11e = 3e et 11e heures solaires du 30/04/1524 depuis le rempart | directions ≈ 95° et ≈ 275° ; une seule jonction qualifiée (Tapon, 1 920 m, az. 92°), p = 18 % ; 0 paire à 1 850 m — `T15_solaire.*` |
| Pont des Bretonnières (idée Guilhem) comme 11e ou repère | 2 085 m de la tour (+12,7 %), rang 10/11/12 selon la source ; rien de significatif à 1 850 m près d'Avalon — `Enigme_12/T16_pont_Bretonnieres.md`, `T16*`, `T17*` |
| 3e/11e = postes d'un parcours numéroté (CO, parcours de santé, patrimoine) | parcours ≤ 10 postes autour d'Avalon ; parcours de santé de Pontcharra : 3→11 ≈ 835 m ; aucune paire à 1 850 m — `T18_parcours.*` |
| 3e/11e = bornes numérotées (frontière Savoie–Dauphiné 1760, pylônes, poteaux incendie, golf, réseau pédestre) | bornes frontière n° 39-58 près de Pontcharra (≥ 7 km) ; pylônes 3→11 = 1 144/1 513 m ; aucun 3-11 à 1 850 m ; golfs sans données — `T18_series.*` |
| Parcelles ONF à lettres, scieries, Machrie Moor | hors fenêtre ou échelle fausse |
| Saint Maurice pour le soldat de l'enl. 9 | lecture d'un agent sans vision ; reste « possible », non établi |
| Brame-Farine (biche), Champ Lernier, Cernon, Merlin, Maupas, « les trois têtes » | échos de noms sans lien démontré ; à plus de 2 km du rempart sauf Merlin |

## 7. Erreurs corrigées (à ne pas répéter)
- Une citation inventée (« mes pas m'ont porté vers le premier jour ») : elle n'existe pas dans le texte.
- FAQ05-122 est une question de joueur, pas une validation.
- « Aucun chemin de rempart cartographié » était faux : la Rue du Rempart existe.
- FAQ03-293 était un bug audio : le sens « deux étapes » est retiré.
- L'écharde vient de FAQ07-068, pas de l'énigme. Le 13e vient de FAQ06-133, pas de l'énigme.
- Le « ? » du schéma de Guilhem veut dire « j'hésite entre deux lettres » ; il n'est pas peint sur l'enluminure.
- Les rapports de sous-agents sans vision (identité du soldat, nombre d'or) ne valent rien avant vérification par l'orchestrateur.

## 8. Géographie utile
| Élément | Position | Distance de la tour |
|---|---|---|
| Tour d'Avalon (TA) | 45.429083, 6.030808 | 0 |
| Château Bayard (CB) | 45.423611, 6.018889 | ≈ 1,08 km |
| Lieu-dit « avalon » | 45.42997, 6.03217 | 145 m |
| Rue du Rempart | 45.42977, 6.03118 | 82 m |
| Mare de l'étang d'Avalon | ≈ 45.4290, 6.0336 | ≈ 250 m |
| Nœud « Le Vivier » (réseau pédestre) | 45.42898, 6.03404 | ≈ 240 m |
| Ruisseau de Tapon / La Planta | ≈ 45.436, 6.047 | 1,3-1,5 km ENE |
| Brame-Farine (sommet) | 45.39121, 6.03796 | 4,2 km SSE |

Données de travail : MNT LiDAR 2 m (`mnt_1500_2.npy`, emprise 45.4107-45.4469 N, 6.0052-6.0564 E), toponymes `noms_4km.json`, réseau pédestre `T11_roches_web/reseau_gresivaudan_noeuds.json`.

## 9. Prochaines actions
1. Décompter les maillons sur les photos HD (biche, garde, dragon, soldat) et en tirer une série de nombres (P3).
2. Tester la croix de l'enl. 11 comme gabarit sur les carrefours de sentiers autour d'Avalon, avec témoins aléatoires (P2).
3. Chercher la clairière sur le terrain : orthophoto et LiDAR fin autour de Tapon / La Planta et des versants dominés par la tour (P4, P5). Jonction de chemins visible depuis le rempart, ruisseau de moins de 1 km.
4. Rien n'est à annoncer sans zone, décompte et contrôle indépendant.

## 10. Fichiers
- `illustration_e12.md` : lecture détaillée de l'enluminure 12.
- `../Revue_globale/` : scripts de test et leurs sorties (`*.py`, `*.out.txt`), `rayure_epee_guilhem.svg`, `FAQ_E12_complet.md`, cartes et orthophotos.
- `../Communaute/` : FAQ officielle de l'auteur (JSON), transcription FAQ8, lectures Discord (propos de tiers, hors dépôt GitHub).
- `../_archive_brut_2026-10-01.zip` : toutes les notes de travail, briefs et rapports de sous-agents d'avant le nettoyage.
