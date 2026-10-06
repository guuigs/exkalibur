# Revue adverse de l'hypothèse P (jonction du Mouret) — 04/10/2026

Relecture à charge, sans rien commiter. Scripts de contrôle (scratchpad) : `adv1.py` à `adv4.py` (convergence, simulation, chord, crible 3 km). Tout est reproductible avec `exec(open('ring1068.py').read().split('out=[]')[0])`.

## 0. Ce qui tient (pour être juste)
- **Signe grille/vrai : correct.** Vérifié numériquement : 1 km vers le nord de grille donne un cap vrai de +2,2°, donc cap grille = cap vrai − 2,2°. Mon simulateur l'applique et retrouve les chiffres de §29 (Pâques 1524 : place 11 à 12 m de la source ; 2026 : 2 m).
- Le formulaire de lever (crête à 10,5°) donne bien 92,1° / 92,7° (1524 / 2026) : le calcul est cohérent.

## 1. Failles critiques

### 1.1 Contradictions avec une réponse FAQ précise
1. **FAQ03-082** (« Les eaux enchantées coulent-elles jusqu'à la grande roche ou s'arrêtent avant ? — Elles ne s'arrêtent pas avant. Elles coulent jusqu'à la grande roche et elles vont même continuer de couler »). La roche est **sur le cours de l'eau, et l'eau continue après elle**. P (lecture principale, §5/§17) fait de la roche **la source elle-même** : l'eau n'y « coule » pas « jusqu'à », elle en sort, et il n'y a rien « après ». Les variantes de repli (roche à 40 m, à 4 m, à 294 m) ne sont plus la source, mais elles ont été **choisies après coup** (voir 1.3). Cette réponse favorise une roche **en aval** de la jonction (on suit l'eau dans son sens d'écoulement), à l'opposé de P (« remonter »).
2. **FAQ03-152** (« le ruisseau et les eaux enchantées = la même chose ? — Oui ») + texte (« l'astre glorieux qui magnifiait le ruisseau »). Le ruisseau éclairé vu du rempart **est** les eaux suivies. Dans P, le ruisseau vu est le **Rebouchet au pont** (45.4262, 6.0388), et les eaux suivies sont un **talweg du Mouret** : deux cours d'eau différents. Mesure BD TOPO : le seul tronçon hydro à moins de 195 m de la jonction est un bout du Rebouchet à **195 m** ; à la source, **219 m** (aucun tronçon à < 60 m de la jonction ni de la source). Le « ruisseau » suivi dans P n'existe que dans le LiDAR (talweg), et il est intermittent (04-198 dit seulement que la météo peut bloquer). FAQ05-121 (« si vous avez la bonne croisée vous aurez votre réponse ») suggère que l'eau se voit à la bonne croisée.
3. **FAQ05-155 / 05-165 + texte** (« l'endroit m'est apparu au matin, illuminé par l'astre »). Le lieu doit être **vu** et **éclairé** au matin. Recalcul sur 1 511 croisements de la zone : la jonction du Mouret a **0 cellule visible** depuis la muraille (±10 m ; `vs_muraille`), et §5 admet que « la jonction et la source restent à l'ombre » (versant NO boisé). P ne tient qu'en remplaçant « l'endroit » par « le pré voisin ». C'est un relâchement, alors que la règle de Guilhem est de ne rien relâcher.
4. **FAQ06-025** (« très proches ») et **FAQ05-051** (« tout près ») : 1,02 km du rempart, 56-67 m du coffre à la jonction. §6 marque ⚠️ mais c'est le même écart d'échelle que pour les croisements « rejetés » ailleurs.
5. **FAQ03-211 / 06-195** (roche « très difficile à manquer », elle « bloque le passage », on peut lui « faire de gros câlins » 06-198). Aucune saillie nette au LiDAR à ±30 m de la source (§6 n°29). Une grande roche qui n'apparaît pas au LiDAR sur terrain ouvert est mauvais signe.
6. **FAQ8** (« l'astre glorieux vous guide en tout dernier lieu », donné en réponse à « avant ou après que l'épée soit revenue... ») : dans l'ordre du texte, le soleil est **après** la phrase des 3e/11e. P l'utilise **d'abord** (pour orienter la table), puis les 3e/11e. FAQ07-133 et 06-166 admettent « direction du ciel puis 3e/11e », donc tension modérée, mais pas levée. De plus FAQ07-132 (« je ne parlerai pas de direction en tant que telle ») et 07-180 (« ne soyez pas obnubilé par la direction ») sont mal servies par une construction dont **tout** dépend d'un azimut à 1° près.
7. **FAQ03-007** (« [la question] présuppose qu'il s'agit d'apôtres, ce que je n'ai pas indiqué ») : jamais confirmé. **FAQ04-051** (l'ordre n'est pas celui du « numéro un » d'*Ultima Cena*) : la Cène est déjà le thème d'*Ultima Cena* ; choisir la liste des apôtres pour 3e/11e est exactement la « famille » dont l'auteur dit que l'ordre est différent (pas contradictoire, mais défavorable).
8. **FAQ07-068 / 06-247** (« pied nu sur la troisième : pas d'écharde ; sur le onzième : possible », « marcher surtout sur l'un des deux »). Ce sont des **objets physiques** sur lesquels on marche, « à pointer » sur une carte (05-074), « trouvables de chez soi » (04-114). Des « places » géométriques sur un cercle ne se marchent pas ; l'écharde de Simon (scie) est un jeu de mots, pas une propriété physique. C'est le point que le dossier marque déjà ⚠️ ; je le classe **critique** : il dit que P n'a pas identifié la nature réelle des 3e/11e.
9. **FAQ04-115** (« directement de la troisième à la onzième, mais en passant par des étapes intermédiaires ») : P dit qu'on va **directement à la place 11** (06-247), donc la corde 3→11 n'est jamais parcourue ; les « étapes intermédiaires » (Rebouchet puis jonction) sont lues sur une corde que personne ne suit.

### 1.2 Erreurs et fragilités de calcul
- **Géométrie « 12 places + le Christ dans l'intervalle » (30° d'espacement) : choix décisif et non justifié.** FAQ06-133 parle d'un **13e** « qui existe » mais ne mène pas au bon endroit : 13 places égales (27,7°). Alors 3e et 11e sont à 221,5° et R = 989,7 m pour 1 850 m. **Simulation : avec 13 places égales, la place 11 n'approche aucune source à moins de 60 m, pour aucune orientation (0,00 %).** P ne fonctionne que dans la variante « 12 places espacées de 30° et le Christ dans la fente ». Si le Christ occupe une place (13 convives), P tombe.
- **Azimut du « lever » : second choix décisif.** Un auteur qui consulte un outil standard (lever à l'horizon plat) obtient 80,6° (Pâques 1524 grég.), 81,2° (2026), 78,9° (2023), 73,0° (**2025**, année du lancement) : place 11 à **216-366 m** de la source, aucun résultat. P exige l'azimut du **lever visible sur la crête de la Burge à 10,5°** (92-93°). Cette hauteur d'horizon est un paramètre qu'un lecteur ne peut pas deviner (FAQ07-152 dit pourtant « relation avec le ciel », pas « calcul d'horizon »).
- **Pâques n'est pas stable.** Place 11 → source (lever visible) : 1524 grég. 12 m, 2026 2 m, **2023 43 m, 2024 (31/03) 41 m, 2025 (20/04, lancement de la chasse) 152 m, équinoxe 104 m**. Le « P est stable de 1524 à 2026 » de §29.3 vient seulement du fait que ces trois Pâques tombent un 5-9 avril. Aucune date n'est fixée par le texte ni la FAQ.
- `ring1068.py` calcule la distance aux bâtiments avec **le premier sommet** de chaque emprise (B). Recalcul avec tous les sommets : Mouret = 175 m (donc la condition passe, mais les cribles antérieurs sous-estiment l'effet des grands bâtiments).

### 1.3 Choix faits après coup / degrés de liberté
Liste des paramètres ajustables de P : date (≥ 6 choix), sens de numérotation (2), place regardée (3e ou 11e), 12 ou 13 places, hauteur d'horizon / canopée (91,3 à 93,6°), liste d'apôtres, point de vue (centre / 4 points de muraille / sommet), nature de la « roche » (source à 73 m, mi-chemin à 40 m, à la jonction à 4-11 m, à 294 m : **quatre variantes en six sessions**), lecture de « à senestre » (« les deux lectures sont acceptées »), lecture du « jour dernier » (5 valeurs), pas (0,65 / 0,75 / 1,48 m). La variante « roche à 294 m » est issue d'un balayage de **1 335 cellules** de talweg pour trouver un coffre en domaine public. Rien de cela n'est contraint par le texte : P ne prédit pas le coffre, elle le **fabrique** par recherche. Le « point de fouille » varie de 400 m selon la variante.
- Le domaine public reste ❌ dans la lecture principale (source) : bois privé B0267. Les variantes publiques sont « fragiles au mètre ».
- **Mouret ne passe pas les filtres durs de Guilhem tels que le dossier les calcule** : eau BD TOPO à 195 m (> 120 m des cribles), visibilité muraille 0, pylône 400 kV à 50 m.

## 2. Alternatives à la coïncidence « place 11 près du Mouret »
- **Hasard pur** : voir §3. La zone est un massif dense en points d'eau (39 objets BD TOPO : 22 fontaines, 7 points d'eau, 5 sources, 4 sources captées, 2 lavoirs) et en croisements (1 511 à ≤ 3 km, dont 318 à 4 branches). On peut toujours trouver un objet voisin.
- **Biais de sélection de la cible** : la cible « source » (5 objets de nature « Source ») a été choisie parmi plusieurs natures hydrographiques ; avec « source ou point d'eau » le hasard par essai monte à 1,3 %, avec « source ou croisement à 4 branches » à ~4,6 % (≤ 35 m).
- **La « corde par le ruisseau vu et la jonction » n'est presque pas une preuve indépendante.** Pour une orientation au hasard (sens P), la corde 3→11 passe à ≤ 15 m d'**un** croisement à 4 branches de la zone pour **39,6 %** des orientations ; à ≤ 15 m du croisement du Mouret précisément, 1,1 %. Le « 0,44 % » joint (§9) est surtout le 1 % de la source multiplié par un facteur d'orientation lié à la même géométrie (distance place 11 – jonction ≈ 60 m) : les deux critères sont corrélés, pas indépendants.
- **Autres sources d'eau et croisements** : près de la place 11 on trouve toujours la jonction (J3) à ≤ 35 m dans 21 % des orientations ; à ≤ 60 m dans 41 %.

## 3. P-value (simulation reproductible, `adv2.py` / `adv3.py`)
Modèle : table de 12 places, cap de la place k = O ± (k−0,5)·30°, rayon 1 068 m autour de la tour (centre = tour, correction de grille −2,2° appliquée), O uniforme sur 0-360° (pas 0,1°), 2 sens de numérotation (7 200 tirages).

| Statistique pour la place 11 | ≤ 11 m | ≤ 35 m | ≤ 60 m |
|---|---|---|---|
| distance à l'une des 5 sources (nature « Source ») | 0,33 % | **1,03 %** | 2,47 % |
| idem, tous points d'eau BD TOPO (hors marais) | 0,33 % | 1,33 % | 3,92 % |
| croisement à 4 branches | 0,25 % | 3,58 % | 10,4 % |
| croisement à ≥ 3 branches | 2,36 % | 21,2 % | 40,9 % |
| **13 places égales, R = 989,7 m**, source | 0,00 % | 0,00 % | 0,00 % |

- **Non corrigé** : place 11 à ≤ 35 m d'une source = **1 % par essai** (cohérent avec 0,2-0,7 % du dossier pour ≤ 11-25 m). Source ≤ 35 m **et** corde ≤ 15 m d'un croisement 4 branches : 0,42 %.
- **Corrigé pour les essais** : les fenêtres de succès (sens P) tombent à O ≈ 91-95° (place 11) ; pour la place 3 elles tombent à O ≈ 61-65° / 211-215°, et pour la 11 à O ≈ 181-185° (sens inverse). Essais réellement faits : ≈ 5 groupes de dates (90°, Pâques ≈ 91-93, 30 avril ≈ 68-74, équinoxe 104, horizon plat ≈ 81) × 2 sens × 2 places (3 ou 11) = 20 à 24 essais, soit **p ≈ 1 − 0,99²⁰⁻²⁴ ≈ 18-21 %** pour « au moins une configuration à ≤ 35 m d'une source ». En élargissant la cible à « source ou croisement 4 branches » : **≈ 60-70 %**. Pour la configuration unique « 1524 ou 2026 + sens P + place 11 + source » la seule p-value honnête, une fois le biais « chercher ailleurs » admis, est de l'ordre de **0,1 à 0,2**, pas de 0,002.
- Observation défavorable : à l'orientation de 2023 (lancement de la chasse annoncé par Guilhem, 90,3°) la place 11 est à 41-62 m ; à 2025 (année de sortie, 22/05/2025 ; Pâques 20/04) à 152 m.

## 4. Meilleur lieu concurrent (critères durs, zone de 3 km)
Crible `adv4.py` : 1 511 croisements ; conditions : bâtiments ≥ 100 m (tous sommets), eau BD TOPO ≤ 120 m, public (parcelle publique / forêt publique / voirie non cadastrée) à ≥ 100 m des maisons dans 120 m, visible depuis la muraille (±10 m, LiDAR).
- **Mouret** : visibilité 0, eau 195 m, public 972 m², bâtiments 175 m, 1,02 km, forêt 74 % : **échoue 2 critères durs** (visibilité, eau BD TOPO).
- 123 croisements passent bâtiments + public + eau ; **quasi tous sont invisibles de la muraille** (forêt dense à l'est et au sud). Ceux qui passent aussi la visibilité :
  - **45.449243, 6.028899** (2,27 km, cap 356°, 3 branches) : eau 13 m, bâtiments 367 m, public ≈ 23 000 m², forêt 41 %, 159 cellules visibles ;
  - **45.448254, 6.026944** (2,17 km, cap 352°) : eau 30 m, bâtiments 203 m, public ≈ 20 600 m², forêt 36 %, 125 cellules ;
  - 45.443603, 6.014493 et 45.445743, 6.016445 (2,1-2,2 km NO, terrain ouvert, eau 56-102 m, bâtiments 116-233 m).
- Ce sont les seuls qui satisfont **simultanément** visibilité + eau + bâtiments + public. Ils violent « très proches » (06-025) et n'ont **aucune** logique 3e/11e (hors cercle de 1 068 m : cap 352-356°, distance 2,2 km). Je les cite comme **meilleurs satisfaiseurs des contraintes de terrain FAQ**, pas comme solutions : un crible sur 1 500 croisements en trouve forcément quelques-uns (c'est le même défaut que P, du côté opposé).
- Verdict de comparaison : **aucun lieu ne bat P sur la logique de chaîne ; P est battue sur les contraintes de terrain (visibilité, eau, public) par le groupe 45.448-45.449 / 6.027-6.029.** Une bonne solution devrait réunir les deux ; ni l'une ni l'autre ne le fait.

## 5. Verdict chiffré (mes paris)
- **P est la bonne zone (coffre à ≤ 150 m du Mouret)** : **≈ 5 %** (fourchette 3-8 %). Raisons de ne pas descendre sous 3 % : l'alignement source-place 11-jonction est réel et un peu plus étroit que le hasard seul ; raisons de ne pas monter : p corrigée ≈ 0,1-0,2, deux contradictions FAQ nettes (03-082, 03-152), visibilité nulle, 13 places = échec.
- **P exacte jusqu'au point de fouille (≤ 5 m)** : **< 1 %** (4 variantes de roche, bande publique « fragile au mètre »).
- **Une zone encore inconnue** (3e/11e = objets physiques réels, par exemple en bois, pointables de chez soi) : **≈ 85-90 %**.
- **Parcours du crible visible** (45.448-45.449) : ≈ 1-2 %.
- À faire avant tout déplacement : (a) tester 13 places égales sous les autres cibles ; (b) chercher des objets **physiques en bois** pointables à 1 850 m (FAQ07-068) ; (c) vérifier sur place s'il y a un ruisseau permanent à la jonction (sinon FAQ03-152 / 05-121 contredit P) ; (d) ne pas fixer le point de fouille avant d'avoir une roche réelle (FAQ03-211).

## Synthèse en 5 lignes
1. Le calcul de cap (grille = vrai − 2,2°) est juste ; le chiffre de 0,2-0,4 % du dossier est un p non corrigé : après essais multiples la probabilité de hasard est plutôt de 10-20 %.
2. Deux réponses FAQ contredisent la lecture principale : 03-082 (l'eau continue après la roche, donc roche ≠ source) et 03-152 (le ruisseau éclairé = les eaux suivies, or le Rebouchet est à 195 m de la jonction et sans lien mappé).
3. P dépend de deux choix invisibles du texte : 12 places espacées de 30° (13 places égales : 0 % de réussite) et le lever sur l'horizon de crête à 10,5° (lever standard : 216-366 m d'écart ; Pâques 2025 : 152 m).
4. Mouret échoue visibilité (0 cellule), eau BD TOPO (195 m) et public sûr ; le seul groupe qui passe les critères de terrain est à 2,2 km au nord (45.449, 6.029), sans logique 3e/11e.
5. Pari : P = bonne zone ≈ 5 % ; P = point de fouille exact < 1 % ; zone toujours inconnue ≈ 85-90 %.
