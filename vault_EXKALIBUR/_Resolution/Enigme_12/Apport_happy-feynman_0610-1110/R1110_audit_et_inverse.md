# R1110 — Audit des travaux DeepSeek (06-07/10) + chaîne inverse roche → souche (11/10/2026)

## 1. Erreurs relevées dans les vagues du 06-07/10
| # | Erreur | Type | Effet |
|---|---|---|---|
| 1 | `CANOPY = MNH − MNT` toujours présent dans `r0610_C_lib.py` (relevé le 07/10, jamais corrigé ni relancé) | technique | chaîne C : vue calculée sur sol nu, filtre « roche nue » inactif |
| 2 | Recherche inverse (INV) : roche exigée hors couvert (MNH < 3 m) | interprétation | FAQ07-126 (roche probablement pas visible sur Maps) ⇒ cible exclue par construction |
| 3 | « Visible du rempart » = ligne de vue stricte avec canopée | interprétation | FAQ05-155 dit « dans le champ de vision » ; Discord 06/10 : aucune clairière à jonction visible sur satellite |
| 4 | Seuils inventés (bâti ≥ 100 m, pente ≤ 12°) | interprétation | FAQ05-107 ne chiffre pas |
| 5 | « Clairière » jamais mesurée | interprétation | FAQ03-274, 06-230 |
| 6 | N1 bâtie sur FAQ03-293 (transcription collée) | interprétation | piste morte d'avance |
| 7 | Budget dépensé sur l'enl. 11 et le ciel | méthode | FAQ8 : « une fois au départ, vous pouvez oublier l'enl. 11 » ; FAQ07-180 « ne soyez pas obnubilé par l'astre » |

Les « 0 survivant » qui reposent sur 1-4 ne valent pas élimination.

## 2. Fait gagné : l'angle de l'É11
Saint-Palais → Grande Chartreuse : cap 65,010° ; prolongé de 193,125 km × π → **82 m du château Bayard** (Bayard à 45 m de la droite). Tour d'Avalon : 1,2 km après, 460 m de côté (tolérance FAQ8 ~1 %). Confirme la droite indépendamment de Bayard (déjà noté dans `RAISONNEMENT_logique_auteur.md` §27, ici recalculé).

## 3. r1110_A — crible roche sous bois (règle fixée avant)
`outils_scratch/r1110_A_roches_sous_bois.py`, sorties `donnees_travail/r1110_A/`. 48 roches (41 sous couvert) ; 4 clairières-jonctions liées à une roche contre **3,7 en moyenne pour des croisements décalés au hasard** → **niveau du hasard**. Meilleure : jonction 45.43653, 6.05768 (cap 65,6° = lever du jour dernier, vue, ouverte 62 %) + bloc 258 m² 45.43832, 6.05382 — ortho : gorge boisée de la Bréda (grand cours d'eau, FAQ06-180), aucun point de fouille valable. **Piste faible.**

## 4. r1110_B — chaîne inverse roche → 10 N + 10 E → souche → 8 pas
`outils_scratch/r1110_B_souche_inverse.py`, sorties `donnees_travail/r1110_B/`, ortho `images_travail/r1110_B/`. Pas 0,75 / 1,0 / 1,48 m (passus : un joueur calibre roche-souche ≈ 20 m sur place, Discord 08/10) ; caps 61° / 63,7° / 68°. 56 roches, 504 chaînes, 53 fins publiques et plates, **dont toutes sauf deux en commune de Pontcharra (38314, règle de Guilhem)** ; restent 45.45871, 6.01085 (Chapareillan, 3,5 km, roche 19 m²) et 45.42535, 6.03319 (Saint-Maximin, roche 11 m², pente 17°, bâti 118 m ; ortho : lisière de ruisseau entre prés). **Rien de fiable.**

## 5. Discord 04-11/10
Aucun coffre trouvé. Souche « ressemblante » d'un joueur (secteur tour d'Avalon, roche mouillée ~20 m, pas romain) ; il lui manque le jour dernier ; aucune validation d'Étienne ; FAQ d'octobre reportée. Personne n'a les 3e/11e.

## 6. Conséquences de méthode
- La zone n'est plus le verrou des joueurs avancés ; le jour dernier (30/04/1524, nôtre) et les 3e/11e le sont.
- Le point exact sans raisonnement ne gagne pas (FAQ03-283) : investir dans le dossier de raisonnement + 3e/11e.
- Le LiDAR/BD TOPO ne voient ni souche ni « grande roche » de façon fiable : le plafond « depuis chez soi » sans les 3e/11e est atteint.
