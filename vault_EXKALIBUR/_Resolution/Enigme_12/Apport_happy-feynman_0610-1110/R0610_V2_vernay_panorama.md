# R0610_V2 — L'arrière-plan de l'enl. 9 est-il le panorama réel vu depuis le Lac du Vernay ? (06/10/2026)

**Verdict : PISTE FAIBLE.** Un alignement qualitatif existe (Vernay → Grand Lône → Pontcharra → tour d'Avalon sont dans la même direction, azimut ≈ 130-140°). Mais il ne distingue pas Vernay des autres plans d'eau de la plaine, les silhouettes divergent (massif continu, pas de colline isolée, tour/bourg superposés au lieu d'être séparés) et le test de corrélation de crête reste du bruit. **Direction de regard la moins mauvaise : ESE-SE (azimut ≈ 105-175°, centre ≈ 135°).** Rien de « fiable » au sens de BRIEF_AUTONOMIE (règle posée avant, pas de paramètre libre, hasard ≤ 2 %, contrôle indépendant).

Dépôt : scripts `outils_scratch/r0610_v2_*.py` ; données `donnees_travail/r0610_v2/` ; images `images_travail/r0610_V2_*.jpg`.

## 1. Lecture de l'arrière-plan de l'enl. 9 (de gauche à droite)
Images : `A_REGARDER_enluminure9.jpg`, zoom `r0610_V2_fond_enl9_zoom.jpg`. Lecture visuelle ; x en % de la largeur du paysage.
- 0-20 % : soldat (premier plan gauche) ; derrière lui collines vert-brun et montagnes bleu sombre basses.
- 20-45 % : grande nappe d'eau pâle (lac) du bord gauche jusqu'au centre, 2 cygnes blancs, rive gauche avec 2-3 petits arbres nus (presqu'île) ; chaîne bleue basse à 2-3 sommets au-dessus.
- ≈ 48 % : **colline basse à tour blanche carrée** (+ pan de mur à sa droite), pente douce montant depuis la gauche.
- 52-75 % : **bourg** de maisons rouge-brique en rangée basse, flèche fine (≈ 55 %), puis gros **clocher/église à deux tours** (≈ 62 %), puis **arcade de 4-5 arches** (≈ 70-75 %) qui prolonge le bourg vers la droite.
- Derrière : **montagne rose pointue** (sommet le plus haut du fond, ≈ 55-60 %, juste à droite de la tour), vallon, **sommet bleu** (≈ 68 %), puis relief qui retombe.
- Horizon bas : les reliefs ne dépassent la rive lointaine que de peu (pas de grande muraille).
- Premier plan : soldat 15 % (gauche), souche couchée ≈ 33 %, **étang bleu à 2 poissons** ≈ 50 %, **roche rayonnante avec coupe** et cascade au-dessus de l'étang ≈ 50-55 %, **pommier** 82-88 %.
- Écarts mesurés : tour → église ≈ 17 % de la largeur du paysage ; église → arcade ≈ 10 %.

## 2. Panorama synthétique depuis Vernay (MNT RGE ALTI via data.geopf.fr + bâti BD TOPO)
Méthode : 360 azimuts × 93 distances (100 m → 45 km), œil à 1,7 m, courbure + réfraction (k = 0,13), profil d'horizon par bandes de distance ; repères BD TOPO (Overpass était bloqué en 406 : WFS BD TOPO à la place). Point de vue = « coupe » 45.448109, 6.000635. Images : `r0610_V2_vernay_pano_90-250.jpg`, `r0610_V2_vernay_pano_95-180_vex2.jpg`, **`r0610_V2_comparaison_enl9_vernay.jpg`** (enl. 9 en haut, panorama en bas).

Repères vus depuis la coupe (azimut ; distance ; hauteur angulaire du sommet de l'objet) :
| Repère | az | d | h. ang. |
|---|---|---|---|
| Grand Lône (plan d'eau des Lônes, 13 ha, BD TOPO) | 59-136° | 0,52-0,81 km | – |
| Lac de carrière Vicat (16 ha) | 41-64° | 1,0-1,5 km | – |
| Tour d'Avalon | 132,0° | 3,19 km | +3,3° |
| Église de Pontcharra | 133,1° | 2,41 km | +0,6° |
| Grosse structure « Pont » BD TOPO (1 003 m², Pontcharra) | 129,9° | 2,69 km | – |
| Château Bayard | 148,1° | 1,89 km | +0,6° |
| Pont de la Gâche (108 m, Isère) | 168,8° | 1,44 km | 0° |
| Fort Barraux | 215,8° | 1,77 km | 0° |
| Mont Granier | 287,2° | 6,2 km | +15,2° |
| Belledonne (Grand Miceau, Pic du Frêne, Grand Charnier…) | 118-143° | 16-21 km | +7 à +8° |
| Brame-Farine (pointe, 1 190 m) | 155,3° | 7,0 km | +7,6° |
| Dent de Crolles / Chartreuse | 216° | 19 km | +5° |

Lecture pour le regard **ESE-SE (azimut 105-175°)** :
- **Concordances** : à gauche, grand plan d'eau (Grand Lône, entre Vernay et Pontcharra, « 2 plans d'eau », 8-10 m de profondeur) ; tour d'Avalon sur le versant au-dessus de Pontcharra ; ordre de gauche à droite : tour (132°) → église (133°), puis Bayard (148°), pont de la Gâche (169°) ; fond de relief lointain ; à droite de Pontcharra, pointe de Brame-Farine (155°, 7,6° d'élévation), candidate pour la « montagne rose pointue ».
- **Divergences** : (i) tour, église et grand pont tiennent dans **3°** d'azimut (la tour est à la verticale du bourg) alors que l'enluminure les sépare de ≈ 17 % puis ≈ 10 % de la largeur ; (ii) la « colline à tour » n'est pas isolée : c'est le flanc de Belledonne, avec un massif de 7-8° d'élévation sur tout le fond (115-150°) au lieu de montagnes basses ; (iii) le bourg réel est une bande continue de 105° à 165°, pas un village compact ; (iv) arcade à arches non identifiée : aucun viaduc/aqueduc dans la BD TOPO de la zone ; l'ouvrage de 1 003 m² à 130° est un pont de Pontcharra (probablement sur le Bréda ; arches non vérifiées) ; (v) **visibilité terre nue** : depuis la coupe à 1,7 m, un talus de 8 m à 100 m masque la tour (horizon 3,58° contre sommet de tour 3,31°) et l'église ; il faut un œil à ≥ 5 m (horizon alors 1,7°). La coupe est en forêt, le houppier masque probablement ; pas de LiDAR MNH sur cette zone (non testé).
- **Direction impliquée par le contour** (`t127_vernay_pos.py` : rotation 110° ⇒ « haut du tableau » = azimut 250°, regard WSW depuis la rive est) : `r0610_V2_vernay_pano_SO_190-310.jpg` montre un mur de Chartreuse de 5 à 15° (Dent de Crolles, Granier 15°), avec Fort Barraux et le bourg de Barraux à plat au pied ; **aucune colline à tour**, Granier massif absent de l'enluminure. Direction écartée.

## 3. Photos du web
Pages publiques consultées : Atout-Pêcheur (étang du Vernay, 4 ha, AAPPMA Chapareillan), Mairie de Chapareillan, Dauphiné Libéré 17/04/2017, Montagne Détente Santé, Destination Belledonne, Alpes-Isère (Grand Lône 11 ha, « berge ouest uniquement » mai-sept.). Mapillary / Google Maps / Instagram : inexploitables ici (pas d'API ni de photo récupérée).
Trois photos récupérées (`r0610_V2_photos_web_vernay.jpg`, originaux dans `r0610_V2_web/`) : rive du Vernay en roselière et boisée (Dauphiné 2017) ; groupe sur pelouse avec toit de ferme et **falaise de type Granier** au fond (ouest) ; rive boisée. **Aucune vue vers Pontcharra / Avalon, ni bourg, ni clocher, ni tour.** Photos trop petites (≈ 800 px) pour comparer des silhouettes. Conclusion : comparaison photographique *non testable* (ni confirmée ni infirmée).

## 4. Témoins et contrôle du hasard
**(a) Géométrie tour/église/pont/grand lac, par plan d'eau BD TOPO ≤ 9 km de la tour (14 plans d'eau, `r0610_v2_base.py`)** : « église à droite de la tour, à moins de 25° » est vrai pour 8/14, dont 4 voisins de Vernay dans la plaine NO de Pontcharra (Lônes 13 ha, retenue 2,3 ha, 0,8 ha, carrière Vicat 16 ha : écarts de 4 à 11°) ; faux pour Maupas (−12°) et les lacs du sud (−3 à −7°). Seul Vernay a **en plus** un plan d'eau ≥ 5 ha devant la tour dans le champ (Grand Lône à −21° de la tour), mais c'est la proximité du Grand Lône ; le Grand Lône ou Vicat serviraient aussi de points de vue. **La concordance est celle d'un secteur (NO de Pontcharra), pas de Vernay.**
**(b) Panoramas témoins** (`r0610_V2_temoins_panoramas.jpg`) :
- Vivier d'Avalon : tour à 150 m, 26° au-dessus de l'horizon ; scène impossible.
- Maupas (3,6 km S) : tour visible à 36° sur un horizon bas, mais bourg/église à gauche de la tour (24° contre 36°) = ordre inversé de l'enluminure ; pas de grand lac devant.
- Mirande (Allevard, 1,5 ha, 450 m) : tour, église, Bayard cachés par un relief proche (horizon 19°).
**(c) Corrélation de crête** (`r0610_v2_skymatch.py`) : crête de l'enl. 9 numérisée à la main (25 points, sans le soldat), corrélée à l'horizon MNT pour 120 azimuts centraux × 5 champs (30-120°) × 4 sites (480 couples site/azimut, meilleur champ gardé) :
| site | meilleur centre | corr | corr max dans 110-160° |
|---|---|---|---|
| Vernay | 12° (champ 45°) | 0,66 | **0,59** |
| Vivier | 144° (30°) | 0,67 | 0,67 |
| Maupas | 279° (90°) | 0,60 | 0,54 |
| Mirande | 297° (45°) | 0,72 | 0,51 |
Médiane tous sites 0,22, q90 0,50, q99 0,64. Le score de Vernay dans la fenêtre SE (0,585) est dépassé par 2,9 % des 480 couples (4,2 % dans la seule fenêtre 110-160°). Son maximum global est au **nord**, pas vers Pontcharra, et deux témoins font mieux. **Non discriminant**, avec numérisation subjective et champ libre.

## 5. Verdict et limites
- **PISTE FAIBLE** : un regard SE depuis les rives de Vernay aligne un grand plan d'eau (Grand Lône), Pontcharra (clocher), la tour d'Avalon et de la montagne ; cohérent avec l'idée que l'auteur a pris Avalon-Pontcharra comme décor, mais vrai de tout le secteur ≤ 3 km au NO de Pontcharra. Aucun élément spécifique (cygnes, presqu'île, arcade, montagne rose) n'a pu être confirmé.
- Prudence : l'auteur dit « positionnement pas parfait » (FAQ07-052) ; décor recomposé = hypothèse déjà posée (T13H) ; le miroir n'a pas été testé.
- Limites : MNT sans arbres (bâti BD TOPO seulement pour Pontcharra) ; panorama complet pour 4 plans d'eau, test géométrique pour 14 ; pas de 1 m LiDAR ici ; ouvrage « arcade » non identifié ; Mapillary/Google Maps non consultés.
- À tester ensuite : (1) LiDAR HD MNH sur Vernay (visibilité réelle à travers la végétation) ; (2) identifier l'ouvrage à arches (pont de Pontcharra sur le Bréda, ancien pont) ; (3) refaire le test de contour avec le Grand Lône (« 2 plans d'eau ») comme « grand lac » plutôt que le petit étang ; (4) test en miroir pour Maupas.

## Annexe : fichiers
Scripts : `r0610_v2_wfs.py` (BD TOPO), `r0610_v2_dem.py` + `r0610_v2_dem_fill.py` (MNT, reprise après erreurs 429), `r0610_v2_lib.py`, `r0610_v2_render.py`, `r0610_v2_reperes.py`, `r0610_v2_fig.py`, `r0610_v2_fig2.py`, `r0610_v2_base.py`, `r0610_v2_skymatch.py`, `r0610_v2_stats.py`. Données : `donnees_travail/r0610_v2/` (dem_*.npz, reperes*.json, v2_visibilite.json…).
