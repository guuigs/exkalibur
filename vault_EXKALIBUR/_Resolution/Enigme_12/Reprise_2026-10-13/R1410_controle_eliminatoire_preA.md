# É12 : le pré A passé aux contraintes éliminatoires du coffre (14/10/2026, poste Windows)

Ce contrôle manquait à la chaîne du 14/10 (TODO § 3, point 5 de la grille : « domaine public, loin des bâtiments »). La règle a été posée avant de regarder : **le coffre est en domaine public, sans demande d'autorisation** (01-235, 03-098), **pas sur un terrain privé ni dans un bâtiment** (02-097), **loin de tout bâtiment, public ou privé** (05-107), **pas dans une zone protégée** (FAQ8). Ce sont des contraintes **D** : une piste qui les rate tombe.

Données : cadastre Etalab (API Carto IGN), fichier DGFiP des **parcelles des personnes morales** (une parcelle absente de ce fichier appartient à une personne physique, donc privée), BD TOPO (bâtiments, réservoirs, détails hydrographiques). Scripts : `scripts/preA_foncier.py`, `preA_foncier2.py`, `preA_public.py`, `anneau_public.py` (sorties `.out.txt` à côté). Les données DGFiP/BD TOPO viennent de la branche `claude/happy-feynman-p7xsyy` (`donnees_travail/r1110_PUB/`, non versionnées car lourdes).

## 1. Propriété des points du pré A

| Point (TODO § 5) | Parcelle | Propriétaire | Bâti le plus proche |
|---|---|---|---|
| Pré A, centre | A 341 | personne physique → **privé** | 94 m |
| J2, angle nord-ouest | A 1317 | **privé** | **18 m** |
| A1, angle sud-est | A 340 | « De Bramefarine » (personne morale de droit privé, groupe 0, forme 6536 : association/indivision) → **privé** | 118 m |
| J, passage du Tapon | non cadastré | emprise de voie ou lit du ruisseau | 34 m |
| R1, ravin du Tapon | B 1 | **privé** | — |
| P3, jonction du Couvat | A 312 | **privé** | — |
| Rive droite du Tapon, de A1 à J (9 points) | A 330, A 1317, A 1319 | **privé**, sauf deux points dans A 1318 (communale, voir § 2) et un point non cadastré | 49-118 m |

## 2. La « cabane » est un réservoir d'eau communal

La « petite cabane » du § 8.2 de `TEXTES_direction.md` (45.43021, 6.05380, au bout de la piste empierrée, au bord du Tapon) n'est pas dans la couche des bâtiments, mais elle est dans la couche **BD TOPO `reservoir`** : deux objets « Réservoir d'eau ou château d'eau au sol » (3,7 m et 4 m de haut, 45.43024 / 6.05377 et 45.43034 / 6.05387).

Elle est posée sur les **seules parcelles publiques de la rive** : A 1221 (428 m²), A 1318 (473 m²) et A 1320 (37 m²), toutes à la commune de Saint-Maximin. Trois petites parcelles communales serrées autour d'un réservoir, c'est le schéma habituel d'un **périmètre de protection immédiate de captage** (clôturé, accès interdit). Ce n'est pas un endroit où l'on enterre un coffre, ni où l'on « tombe sur une grande roche ».

Il y a aussi une **fontaine** dans la BD TOPO (détail hydrographique) en 45.43012, 6.05118, à 160 m à l'ouest de J, à environ 1 575 m de l'esplanade : hors des 10 stades (−15 %), donc pas la « fontaine » du chap. XI dans ce modèle. Notée seulement.

## 3. Verdict sur le pré A

**Le pré A échoue au point 5 de la grille (contraintes D).** Toute la rive droite du Tapon devant le pré est privée, sauf l'enclos du réservoir ; en aval de J, le ruisseau entre dans le hameau (bâti à moins de 100 m). Aucun endroit de la suite « ruisseau → roche → 10 pas N + 10 pas E → souche → 8 pas » ne peut tomber en terrain public loin des maisons, quelle que soit la jonction retenue (J2, A1 ou J).

Seules échappatoires, toutes faibles :
- l'emprise non cadastrée d'un chemin rural (on ne creuse pas dans un chemin, et l'auteur dit « domaine public », pas « chemin ») ;
- une erreur du fichier DGFiP (le millésime 2024 est récent ; peu probable sur une dizaine de parcelles d'affilée).

Conséquence pour le TODO : **« Choisir la jonction du pré A » n'a plus d'objet tant que le pré A ne passe pas le point 5.** La lecture R2 (Pâques) + visibilité reste un résultat sur la *direction*, mais l'endroit qu'elle désigne n'est pas le bon, ou la règle de visibilité est trop stricte.

## 4. Où le domaine public touche-t-il l'anneau des 10 stades ? (tout le tour)

Même règle, appliquée à l'anneau complet de 1 831,5 à 1 868,5 m autour de l'esplanade (45.42891, 6.03112). On ne chiffre pas « tout près » : on liste simplement les parcelles publiques qui **coupent** l'anneau, et la part de chacune à au moins 100 m d'un bâtiment (colonne indicative, pas un filtre de la FAQ).

- 44 parcelles publiques coupent l'anneau ; **9 seulement ont du terrain à ≥ 100 m de tout bâtiment**.
- Ces 9 se répartissent en 4 secteurs :

| Cap | Où | Ce que c'est (orthophoto) | Verdict |
|---|---|---|---|
| 354-360° | Laissaud (73), parcelles de la commune de Pontcharra B 9-12, B 1698-1699 | **champs cultivés** contre une zone d'activités | ni bois, ni clairière |
| 334° | Pontcharra ZB 70 (393 m²) | bord de champ | idem |
| 254° | Pontcharra BC 682 (C.C. Le Grésivaudan) | **zone d'activités** de Pontcharra, entre voie ferrée et entrepôts | exclu (règle de Guilhem : ville, zones d'activités, gare) |
| **144°** | **Saint-Maximin B 440, forêt communale (2,8 ha)** | forêt fermée mixte, sur une croupe à ~850 m d'altitude (450 m au-dessus de la tour), pente 3-31° (médiane 17°) | **seul secteur boisé public de tout l'anneau** |

Sur l'anneau, à 144,9° et 1 834 m : une **jonction de trois chemins** (BD TOPO, 45.41543, 6.04462), non cadastrée (emprise de chemin), à 24 m de la forêt communale B 440, bâti à 298 m. Mais : pas de clairière dans la BD TOPO (forêt fermée), le ruisseau le plus proche est à **384 m** (Rebouchet à 422 m), et **aucune lecture du texte ne donne 145°** (le lever du soleil ne dépasse jamais 123,5° ; la rose des vents IV = sud-est = 135°). → **piste faible**, notée pour mémoire, sans plus.

## 5. Ce que cela change

1. Avec le départ sur la butte d'Avalon, **aucun endroit de l'anneau des 10 stades ne réunit domaine public, bois et ruisseau**. C'était déjà la conclusion de l'entonnoir « domaine public d'abord » du 11/10 (branche `happy-feynman`, `Enigme_12/R1110_PUB_rapport.md` : « à < 3 km, aucun secteur public boisé + ruisseau + plat + loin du bâti hors Pontcharra »). Les deux méthodes, parties de bouts opposés (le texte d'un côté, le cadastre de l'autre), arrivent au même vide.
2. Il faut donc qu'une hypothèse de la chaîne soit fausse. Par ordre de fragilité :
   - **le modèle « l'endroit est à 10 stades du départ »** : les 10 stades séparent les 3e et 11e (texte), rien ne dit que l'un des deux est le rempart (07-120 dit seulement qu'on les place « par rapport à un point de départ ») ;
   - **le départ** (supposé, non validé : TODO § 1.2) ;
   - **« dans le champ de vision » pris au sens strict** : c'est une indication Q, qui ne doit pas éliminer (règle de Guilhem).
3. Le secteur est (lever du soleil) est **entièrement privé** jusqu'à la forêt communale de Saint-Maximin (A 409-411, A 173 : 2,3-2,7 km, caps 84-89°, 150-350 m du bâti, ruisseau à 300-570 m). Si le coffre est à l'est, il est vraisemblablement **plus loin que 10 stades**, dans ces forêts communales.
