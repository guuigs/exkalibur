# T13-H — Rapport : l'étang et le paysage de l'enluminure 9 comme carte de la zone finale

## Résumé (conclusion)
Le soldat est **saint Maurice** (soldat romain, patron de la Savoie ; « l'anneau doré » = la relique réelle de l'anneau de saint Maurice, trésor de la Maison de Savoie). Le paysage de fond est une **recomposition symbolique non localisable à l'échelle du bureau** (l'auteur le dit : « pas un positionnement parfait »), mais deux zones candidates tiennent par toponymie : **Maupas (SO, ~3,6 km)** et **l'Étang (NE, ~7,7 km)**. La configuration locale précise (roche → 10 pas N+10 E → souche → 8 pas → coupe, soit <30 m) est sous la résolution de BD TOPO/OSM et exige le terrain.

## 1. Plan de l'enluminure (fichier joint)
`T13H_plan_enluminure.svg` — positions relatives reconstruites. **Limite : vision LLM indisponible** (`vision_analyze` sans fournisseur) ; positions tirées de la segmentation couleur PIL (seuils HSV + salience bleue) et de la description détaillée du brief (vague 3, ligne 9). La photo est chaude/mate (salience bleue max 41/255), rendant le seuillage du « haricot » bleu ambigu ; la bande bleue principale est en haut de l'image (y≈17–33 %, large), le soldat/rouge et l'or de l'arbre au centre-bas, le rose d'aube en haut-gauche (= est). L'inventaire des éléments (étang 2 poissons+2 cygnes, rocher rayonnant à coupe, ruisseau/cascade, arbre à fruits dorés, soldat à crinière/cape rouge + anneau + crâne, château sur butte, ville à arcades, montagnes, aube, loup+glyphe V♀) provient de la description du brief, fiable.

## 2. Configurations réelles qui tiennent (appariement étang+rocher+arbre+ruisseau)
- **Maupas (SO, ~3,6 km)** — la plus riche : « Étangs du Maupas » (Retenue, plan_d_eau) + « ruisseau de Maupas » (tronçon hydro, 3,5 km) + « roche morte » (3,05 km) + « zones humides de la Rolande et du Maupas » (4,06 km) + lieu-dit « le Maupas ». « Maupas » = mauvais pas → écho à « la grande roche bloque le chemin » (FAQ8). Pieds mouillés avant la roche (FAQ06-090) cohérent avec zones humides.
- **l'Étang (NE, ~7,7 km)** — toponyme exact « l'Étang » (Lac), près de « saint-maurice » (7,5 km) et « sous le château » (7,0 km). Plus loin (hors marge 6 km) mais nom le plus littéral.
- **Étang du Grand Glairon / Étang de la Berche (~8,8 km SO)** — zone du Cheylas, moins de témoins annexes.
- Rochers nommés proches (coupe ?) : **« Pierre Hachée »** (9,4 km — « pierre coupée » → coupe du charpentier ?), « Griffes de l'Ours / Planche à laver » (7,2 km), « Marameille » (7,6 km), « rocher de saint-georges » (5,4 km).
- Aucun arbre remarquable OSM (natural=tree) dans 12 km sauf « Noyer »/« Chene » isolés vers 9 km ; rien à <5 km. **La forme de l'étang seule est non discriminante (déjà établi, test T1).**

## 3. Paysage de fond = vue réelle ? (viewshed LiDAR)
MNT 2 m vérifié (lignes nord→sud : nord bas 295 m, sud haut 613 m ; Bréda sort en plaine ~270 m au N). Tour d'Avalon à **407 m** ; vue dominante **OUEST** (val Grésivaudan : Fort Barraux, Montmélian) et **SUD** (Pontcharra/Bayard) ; SE nul (versant Belledonne) ; Belledonne visible à l'E jusqu'à 848 m. → Cohérent avec un fond « montagnes + eau + château sur butte », mais **non spécifique**. Candidats château sur butte : Fort Barraux (4,16 km O, vrais remparts), « château montmeillerat » (6,33 km, ≈ Montmélian), « château du touvet » (9,8 km), château Bayard (1,1 km). Ville à arcades/aqueduc : Montmélian ou Pontcharra (aucun aqueduc romain identifié dans les données). **Conclusion : vue réelle plausible mais non identifiable de façon unique → paysage non localisable au bureau** (conforme à la FAQ).

## 4. Identité du soldat romain = saint Maurice (confiance élevée)
- RÉPONSE auteur (FAQ04-175) : il faut l'identifier. « Soldat romain à casque à crinière rouge, cape rouge, tenant un **anneau doré**, crâne gris à ses pieds ».
- **Saint Maurice (Maurice d'Agaune)** : chef de la légion thébaine, représenté en soldat romain (casque/cotte de mailles, vérifié). **L'« anneau de saint Maurice » est une relique réelle** (abbaye de Saint-Maurice d'Agaune, « joyau de la Savoie », remis aux rois de Bourgogne pour leur couronnement, possédé par la Maison de Savoie — cohérent avec « Le roi » du texte). Crâne = décapitation des martyrs thébains. Patron de la Savoie (région de l'énigme).
- Lieux liés dans la zone : **« saint-maurice »** lieu-dit (7,51 km, 45.46444, 6.11261), « école saint-maurice » (8,16 km), « gymnase maurice cucot » (1,68 km), « stade maurice rey » (8,32 km).
- Écartés : saint Martin (cape rouge = manteau partagé, mais pas d'anneau ; lieu-dit 7,07 km), Longin (pas de toponyme, tient une lance), Pierre (pêcheur+roche mais pas soldat).

## 5. Problèmes rencontrés
- `vision_analyze` sans fournisseur vision → reconstruction PIL (sourde pour les couleurs mates).
- Étangs nommés (Maupas 45.4025, l'Étang 45.4479) hors emprise MNT (45.4107–45.4469) → viewshed impossible depuis les étangs eux-mêmes ; seul le viewshed tour (3 km) a pu être exploité.
- Bug mineur de conversion lon (min_lat utilisé pour longitude) dans 2 scripts — cosmétique, n'affecte pas les résultats en espace pixel.

## Fichiers créés
- `Revue_globale/T13H_plan_enluminure.svg`, `T13H_notes.md`, `T13H_rapport.md`.
- Scratch `exk_e12/` : `t13h_seg*.py`, `t13h_mnt.py`, `t13h_pond.py`, `t13h_ascii.py`, `t13h_crops.py`, `t13h_inv*.py`, `t13h_topo*.py`, `t13h_maupas.py`, `t13h_overpass.py`, `t13h_viewshed.py`, `t13h_pond_mask.npy`.
