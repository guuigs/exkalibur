# Rangée de Léonard centrée sur le rempart — test (05/10/2026)
Scripts : `outils_scratch/t107_rangee_leonard.py` (sorties dans ce fichier). Ancrage : J2 = 45.42337, 6.04166 (1 034,1 m, cap vrai 126,35°).

## La chaîne (rangée de 12 apôtres, Christ à la place du rempart)
1. Départ T = tour/rempart = place du Christ (le « 13e » : « ne vous mènerait pas au bon endroit » = c'est le départ lui-même).
2. 12 apôtres alignés, 6 de chaque côté, espacement s = 1 850/8 = **231,25 m** (3→11 = 8 pas = 10 stades). Place k à (k−6,5)·s : la 3e à −809 m, la **11e à +1 040,6 m**.
3. Axe de la rangée = azimut du lever **visible** du soleil (relief du SE, soleil à 15° au-dessus de la crête), le jour de la fête de l'apôtre n° 11 (Simon, avec Jude : **28 octobre**) : 126,6° (126,1° le 27, 127,2° le 29).
4. Résultat : 11e place = 45.42334, 6.04172 → **7 m de J2** (rayon : 1 034 contre 1 040,6, −0,63 %). La 3e place = 45.43321, 6.02268, à 809 m au NW, **27 m de l'église Saint-Hugues de Pontcharra**, en zone bâtie ; la 11e est en forêt (canopée 19 m, 0 % ouvert).

Cohérences avec la FAQ : 3e et 11e « trouvables de chez soi » (une église, un croisement), pas d'écharde sur la 3e (ville), écharde possible sur la 11e (bois, FAQ07-068) ; « marcher surtout sur l'une des deux » = la 11e ; la 11e place est la clairière/jonction (FAQ07-133) ; 13e = place du Christ ; pas de 16e ; la phrase 1 « dix stades séparaient les troisième et onzième » donne s.
L'église Saint-Hugues : dédicace à Hugues (de Grenoble, fondateur avec Bruno de la Chartreuse, ou écho d'Hugues d'Avalon, évêque de Lincoln ; non tranché). Église moderne (Pierre Pinsard).

## Hasard (méthode : placebo, honnête)
- Bande radiale 4,5 s ±1 % : sur 173 croisements à maisons ≥100 m, **1 seul (J2)** ; attendu ≈ 2,4. Non significatif seul.
- Famille de configurations (11 fêtes d'apôtres × lever visible/plat × axe le long ou ±90° × 2 sens × rangée de 12 ou 13) : 240 configurations. Hit conjoint « 11e ≤30 m d'un croisement qualifié (maisons ≥100 m + eau) ET 3e ≤40 m d'une église » : **1 configuration (Simon et Jude 28/10, lever visible, rangée de 12)**.
- Monte-Carlo (axe aléatoire) : P(11e ≤30 m d'un croisement qualifié) = 1,7 % ; P(3e ≤40 m d'une église) = 1,35 % ; P(conjoint) = **0,41 %** par configuration. Sur les 120 configurations de la rangée de 12, on attend 0,49 hit par hasard : **p famille ≈ 39 %**. Non significatif.
- Facteur « l'église touchée est Saint-Hugues » : 1 église sur 10 de la zone, mais le lien Hugues (Avalon/Chartreuse) est un lien de lore que j'ai repéré après coup. Estimation grossière : 0,39 × 0,1 ≈ **4 %** si on compte ce bonus, avec risque d'effet « on trouve toujours un lien après coup ». Le lever visible dépend du MNT de 25 m depuis le pied (± 0,5°).

## Faiblesses
- Rangée de 12 (Christ absent) et non de 13 : ajustée sur le rayon 1 040,6 m ; la rangée de 13 de Léonard (3e/11e à ±925 m) ne donne rien.
- L'axe de la rangée est dirigé vers le soleil, alors que dans le tableau elle est perpendiculaire à l'axe Christ-spectateur : choix non justifié.
- « Même nature » (FAQ06-009) : une église et un croisement forestier ne sont pas de même nature, sauf si « nature » = « place de la table ».
- Hugues n'est pas un apôtre ; la 3e = église n'est pas un apôtre non plus.
- La fête du 28/10 n'a été repérée qu'après le cap de J2 (date non choisie a priori, mais seule fête d'apôtre dans les fenêtres 25-30/10 et 13-18/02).

## Verdict
Hypothèse la plus cohérente trouvée depuis le début pour expliquer J2 par le 3e/11e (distance et direction expliquées, 3e et 11e de natures conformes à la FAQ07-068), mais hasard famille ≈ 39 % (≈ 4 % avec le bonus Saint-Hugues). Confiance dans la zone Mouret : 8-12 %. Point exact : < 3 %.
À faire : calcul du lever depuis le haut de la muraille ; test de la date 28/10 en calendrier julien ; recherche d'un lien Hugues dans le texte/illustrations (enl. 11 : « aide à placer une partie » des deux).

## Suite (05/10/2026, après retour de Guilhem) — liens de lore et choix de la date
Scripts : t108_dates_hugues.py, t109_coffre_J2.py.

### Lien Hugues / enluminure 12 (R6D, texte Ultima cena)
Relevé de l'enluminure (illustration_e12.md) : à gauche la **tour de Lincoln** (deux yeux, tronquée) = Hugues de Lincoln/d'Avalon (concaténation FAQ07-019) ; au centre **Jésus seul à une longue table** (« incomplète, parcellaire », FAQ03-065) ; à droite le **vieillard à la scie et au livre = saint Simon le Zélote**, 11e apôtre de la liste de Matthieu (scie = bois, écharde possible, FAQ07-068).
Disposition de la rangée trouvée : église **Saint-Hugues** (3e) au NW (gauche), Christ = rempart (centre), **Simon** (11e) au SE (droite) = J2. C'est l'ordre gauche-droite de l'enluminure : Hugues – Christ – Simon. Un spectateur dont la droite pointe à 126,35° regarde vers 36° (NE).
« Même nature » (FAQ06-009) : deux **saints** (Hugues, Simon) → une église Saint-Hugues et un lieu de Simon. Hugues est aussi le nom de la « Trinité » de l'É8 (Hugues de Lincoln, de Payns, d'Avalon, modérateur 28/08/2026) ; la chapelle Saint-Hugues et la place Saint-Hugues d'Avallon sont au pied de la tour (R2_rapport). L'église Saint-Hugues de Pontcharra (Pinsard, XXe s.) est la seule église Saint-Hugues de la zone.
Le **28 octobre** (Simon et Jude) : sa **vigile** (27/10, soir) correspond à « j'ai fait une dernière veille… l'endroit m'est apparu au matin » (vigile = veille de fête ; abolie en 1955, attestée au XVIe s.). Le matin du 28/10, le lever visible est à 126,6°.

### Pâques ?
- Rangée de 12 avec axe sur le lever de Pâques (2023-2026, 1524 grégorien/julien) : 11e place au plus près d'un croisement qualifié à **358 m** (axe le long du lever) et **218 m** (axe perpendiculaire). Rien.
- Le lever de Pâques (80-99°) pointe vers la plaine ; la fête de Simon et Jude (126,6°) vers J2. Pâques reste utile pour la **table ronde** (P), pas pour la rangée.
- Fêtes de saint Hugues : Grenoble 01/04 (lever visible 95,7°), Cluny 29/04 (74,7°), Rouen 09/04 (90,2°), Lincoln 17/11 (137,0°) : aucune n'est à 126,35° ±1,7° (seules les fenêtres 13-18/02 et 25-30/10).

### Fin de parcours depuis J2 (public, maisons ≥100 m, chemin ≤30 m)
320 cellules de ressaut sur l'eau à ≤300 m de J2 ; le même petit groupe de roches à 35-46 m de J2 (80 % du trajet le long d'un chemin) donne un coffre en **public sûr** pour tous les « jours derniers » testés (28/10 : 107,6° ou 126,6° ; 30/04 : 63,7° ou 74° ; Pâques 2025 ; est) : coffre ≈ 45.42354-45.42361, 6.04136-6.04140 (pas 0,65-0,75). La date finale ne discrimine donc pas à ce stade.

### Autres versions du 3e/11e examinées
- **Table de Winchester à 25 places** (24 chevaliers + Arthur ; « SCRIPSIT XXV » ; la phrase 1 a 25 lettres) : rayon 1 096 m ; places 3 et 11 testées sur 8 dates × 2 sens × 2 positions d'Arthur : plus proche croisement qualifié à **62 m** (équinoxe, sens inverse) ; Pâques 20/04 (2025), place 3 à 67 m de J2. Aucune à ≤30 m, attendu par hasard ≈ 2-3 : non retenu.

## Suite 2 (05/10/2026, autonomie) — listes d'apôtres, spacing, PATERNOSTER, sensibilité
Scripts : t107/t108/t109, calculs ad hoc (pas de nouveau fichier). Sources internes relues : `Revue_globale/T15D_inventaire_series.md`, `T15B_enluminure11.md`.

### Les quatre listes d'apôtres donnent toutes la même date
| Liste | 3e | 11e | Fête du 11e |
|---|---|---|---|
| Mt 10 | Jacques | **Simon** | 28/10 (avec Jude) |
| Mc 3 | **Jean** | **Simon** | 28/10 |
| Lc 6 | Jacques | **Jude** | 28/10 |
| Ac 1 | Jacques | **Jude** | 28/10 |
Dans Marc, 3e = **Jean** (« Dieu a fait grâce » = « Dieu sut se montrer favorable », la phrase 1, confirmateur de zone FAQ07-088) et 11e = **Simon** (scie, enl. 12). L'étymologie de Simon (« il a entendu ») fait écho à « J'entends le chant retentir » (non démontré). Le choix de la date (28/10) ne dépend donc pas de la liste retenue.

### Enluminures et numérotation
Numérotation de l'auteur = ordre de lecture (R1G=1 … R6D=12). Enl. 12 (R6D) : tour de Lincoln à gauche, Jésus seul à la table, Simon à droite. Enl. 6 (R3D) : Jude (médaillon). Enl. 5 (R3G) : long table bleue (« motifs du dessus de la table utiles », FAQ05-152) : **9 + 9 médaillons ronds, 5 quadrilobes médians et 1 à l'extrémité** (24 médaillons) ; motifs reconnus : sabliers (≥6), rosettes à 6 pétales, **deux poissons** (Poissons ?), oiseaux, une sirène/poisson, un animal vert. Non décodé : lead ouvert (24 = 12 × 2 ? zodiaque ? la date ?).

### Espacement et PATERNOSTER (T15B §4, à faire n° 3)
T15B demandait de tester « 8 unités = 1 850 m (231 m par pierre) » avec la croix PATERNOSTER posée sur la carte. **231,25 m = l'espacement s de la rangée.** Mais le centre N de PATERNOSTER est la 6e pierre ; avec N au rempart, T(3e) est à −694 m et R(11e) à +1 156 m : 144 positions testées (10 dates × lever visible/plat × axe ou perpendiculaire × 2 sens × 2 pierres) → meilleure à 50 m d'un croisement qualifié (hasard attendu ≈ 0,7) : **négatif**. J2 correspond à la demi-pierre (11e à 4,5 s), donc à la rangée de 12 avec le Christ à la place du rempart, pas à PATERNOSTER centré sur le rempart.

### « De la 3e à la 11e, étapes intermédiaires » (FAQ04-115)
Marcher en ligne droite de la 3e place (église Saint-Hugues, NW) à la 11e (J2, SE) **passe par le rempart** (corde passant à 19,5-19,8 m du centre de la tour, pied de perpendiculaire à 785-794 m côté église et 1 034 m côté J2 ; le modèle donne 809/1 034). Les places 4 à 10 sont les étapes. Corde réelle église → J2 : 1 819 m (centroïde), 1 828 m (clocher), soit 9,83-9,88 stades ; avec la 11e place du modèle (7 m au-delà de J2) : ≈ 1 835 m (−0,8 %), dans « 1 % près » (FAQ05-172) à condition de prendre le clocher.

### Sensibilité du lever (28/10, depuis le pied de la tour)
Crête à 2,7 km, 14,8° : lever visible à 126,6°. Horizon ±1° → 125,3° à 127,9° (J2 à 126,35° ±1,7° reste couvert). Le départ pris sur le mur plutôt qu'au centre décale J2 d'une quinzaine de mètres.

### Noms de lieux près des places (rangée de Marc)
Place 1 (Pierre) : lycée Pierre du Terrail à 98 m (Pierre du Terrail = Bayard) ; place 3 (Jean) : église Saint-Hugues à 42 m ; places 6-7 : rue du Rempart / tour d'Avalon / place Saint-Hugues d'Avallon à 89-124 m ; place 11 : Varanger (lieu-dit habité) à 171 m ; place 12 : Les Tilles à 184 m. Zone urbaine dense à l'ouest : coïncidences de noms peu probantes (non comptées).

### Hasard (précisé)
- Si la chaîne (rangée de 12 centrée sur le rempart, espacement 231,25 m, axe sur le lever visible du jour de fête du 11e) avait été fixée avant de regarder J2 : 4 configurations (sens × cap), P(11e ≤10 m d'un croisement qualifié) = 0,07 % par configuration → **≈ 0,3 %**.
- Mais 12 places plutôt que 13, et la date, ont été retenues après avoir vu J2 : en comptant ces degrés de liberté, **2 % à 39 %** selon ce qu'on compte (famille de 240 configurations : 39 %). Honnêtement : **entre 2 et 20 %**, et la plupart des hypothèses concurrentes sont au-dessus.
- Le signal est donc encourageant mais pas sous 2 % de façon robuste.

### À faire
1. Décoder les motifs de la table de l'enl. 5 (poissons, sabliers, rosettes) : peuvent donner la date ou le sens de lecture de la rangée.
2. Trouver un objet réel pour la 3e (Jean/Jacques) : le clocher de Saint-Hugues, la croix de chemin à 52 m (45.43314, 6.02335) ?
3. Vérifier la corde 3e → 11e avec le clocher et la place de Simon exacte.
