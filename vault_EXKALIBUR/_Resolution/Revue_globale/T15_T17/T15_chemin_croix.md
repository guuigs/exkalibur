# T15 — Chemins de croix / stations / calvaires ≤ 6 km de la tour d'Avalon (reprise)

Script : `T15_chemin_croix.py` — sortie : `T15_chemin_croix.out.txt` — données : `t15_candidates.json`, `t15_osm_raw.json`, `t15_osm_extra.json`, `t15_lvv38_list.json`, `t15_lvv73_list.json`.

## Résultat net
**Aucun chemin de croix extérieur (stations numérotées) n'a été trouvé dans les 6 km** (ni dans BD TOPO, ni OSM, ni les inventaires web). Donc aucune « 3e » ni « 11e » station réelle à tester : l'hypothèse « chemin de croix » n'est ni confirmée ni testable avec des données existantes. Aucune station n'a été inventée.

## Ce qui a été cherché
1. **BD TOPO IGN** (`construction_ponctuelle_12km.geojson`, nature = Croix) : 196 croix + 16 oratoires + 14 vierges sur 12 km ; 30 dans 6 km. Aucune n'a de numéro/toponyme « station ». (`toponyme` absent.)
2. **OSM Overpass** (overpass-api.de, requête 6 km, OK ; overpass.openstreetmap.fr non utilisé, 504/429 sur les requêtes plus lourdes) : 43 éléments « historic=wayside_cross/shrine, man_made=cross, nom ~ calvaire/station/croix/oratoire ». Aucun tag `ref` numérique, aucun `memorial=station`, aucun nom « Station n° ». Seul nom lié : « Chemin de Croix-Verpi » (way 537769750, Chapareillan, 45.4846, 5.9796, ~7,3 km de la tour = hors rayon) — c'est un odonyme (chemin), pas une série de stations. « Passage du Calvaire » (way 180370299) = simple rue (commune non vérifiée), 8,6 km. Les requêtes `historic=*` / `ref` plus larges ont donné des 504 (non obtenues).
3. **Inventaires lavieduvillage.fr** (https://38.lavieduvillage.fr/Calvaires.php, https://73.lavieduvillage.fr/Calvaires.php ; 971 + 746 fiches) : seules séries numérotées « Chemin de croix N° x » = Voreppe (14), La Salette-Fallavaux (14), Miribel-les-Échelles, Saint-Pierre-de-Chartreuse, Le Versoud — tous hors zone. Pour les communes cibles : Saint-Maximin 3 fiches (2380645-47, « Calvaire ? », « Croix », non lues : limite de débit du scraper), Pontcharra 2 (2380490 : chemin des Gayets 45.420792, 6.012769 = identique au nœud OSM 6516925430, croix à 1,68 km ; 2380491 non lue), Chapareillan 6 (2380128-33, coordonnées lues, toutes > 6 km de la tour ; « Calvaire ? » = point d'interrogation du site, pas de station), La Chapelle-Blanche 1, Arvillard 1, Sainte-Hélène-du-Lac 1, Myans 3 : tous « Calvaire ? / Croix » isolés, sans numéro.
4. **Chapareillan** (inventaire PNR Chartreuse, https://www.parc-chartreuse.net/content/uploads/2018/01/chapareillan.pdf) : 16 croix de chemin et oratoires recensés, aucun chemin de croix numéroté.
5. **Myans** : « chemin du Saint-Rosaire » (stations des mystères du Rosaire, pas du chemin de croix ; 4e mystère douloureux = portement de croix) https://museesavoisien-collections.savoie.fr/fr/document/myans-station-du-chemin-du-saint-rosaire-4eme-mystere-douloureux-jesus-porte-sa-croix-sur-le-chemin-du-calvaire-et-rencontre-sa-mere/6302b72f35653cb1a94635e1 ; Myans est à ~9-10 km de la tour (hors 6 km) et pas de coordonnées de stations trouvées.
6. **La Rochette** : « Les Trois Croix » (14 croix d'un calvaire du XVe s., Fontcouverte/Saint-Pancrace, Maurienne ; https://www.explore-savoie.com/randonnees-et-balades/la-rochette-et-les-trois-croix-5838314/) = autre La Rochette, Maurienne, hors zone.
7. Recherches web sans résultat pertinent pour : Saint-Maximin, Pontcharra, La Chapelle-Blanche, Laissaud, Arvillard, Détrier, Le Cheylas, Allevard, Barraux, Villard-Sallet, Le Moutaret, Sainte-Hélène-du-Lac, Les Marches, Saint-Pierre-d'Allevard (pas de page de chemin de croix extérieur). Parcours thématique de Saint-Maximin (https://www.alpes-isere.com/sit/parcours-thematique-saint-maximin-4704227/) : aucun chemin de croix mentionné. cleophas.org / patrimoine.auvergnerhonealpes.fr / POP : rien de localisé trouvé (non exhaustif — ces bases n'ont pas pu être interrogées par commune).

## Test géométrique de repli (croix non numérotées, 37 objets uniques ≤ 6 km)
- 37 croix/oratoires (BD TOPO 30, OSM 6, LVV 1 ; dédoublonnage à 25 m), 666 paires.
- **2 paires à 1850 ± 18 m** :
  - 1853,3 m : OSM node 9122972149 (45.458604, 6.054886 ; 3,78 km de la tour) ↔ OSM node 9196370724 (45.443089, 6.046208 ; 1,97 km ; croix en bois)
  - 1846,3 m : IGN CONSPONC…231404854 (45.449738, 6.086062 ; 4,89 km) ↔ IGN CONSPONC…351456726 (45.458986, 6.066402 ; 4,33 km)
- **Contrôle aléatoire** (37 points uniformes dans disque 6 km, 20 000 tirages) : 2,00 paires attendues en moyenne ; P(≥1)=86 % ; P(≥2)=59 %. → Observé = attendu : **rien de significatif**.
- De plus, aucune de ces croix n'est numérotée, donc rien ne les désigne comme « 3e » et « 11e » ; et elles sont loin du chemin de rempart (RP) / de la clairière visible à l'œil nu.

## Jugement honnête
- Hypothèse « chemin de croix (stations 3 et 11) » : **pas de support** — aucun chemin de croix extérieur recensé dans le rayon de 6 km (ni dans les communes voisines listées, pour les sources accessibles).
- Les paires à 1850 m entre croix quelconques sont indiscernables du hasard.
- Limites : OSM limité par des 504 sur les requêtes larges ; pages LVV de Saint-Maximin non lues (rate-limit) ; les chemins de croix intérieurs d'églises (stations = tableaux dans la nef) existent mais ne sont pas « marchables pied nu » ni distants de 1850 m — non traités.
- Autres pistes à tester (hors périmètre) : « troisième et onzième » = ponts/gués/bornes/marches/arches numérotés (« dixième station » ≠ chemin de croix) ; les écharde/pied nu suggèrent plutôt des **planches/marches/poutres (passerelles, ponts de bois) ou des « stations » d'un sentier balisé**.
