# Brief commun sous-agents — Exkalibur É12 (02/10/2026)

Chasse au trésor « Exkalibur » (auteur Étienne Picand). Dernière énigme (É12) non résolue.
Zone de départ établie : tour d'Avalon, Saint-Maximin (Isère, 38530) — TA = 45.429083, 6.030808 ; « Rue du Rempart » RP = 45.42977, 6.03118 (82 m de la tour). Château Bayard CB = 45.423611, 6.018889.

Texte (exact) :
« Dieu sut se montrer favorable ; dix stades romains séparaient les troisième et onzième. Le roi avait rejoint les fées, et laissé son épée aux portes d'Avalon. L'épée, évidemment. L'épée, depuis toujours ! Là était la dernière clé de la quête du Graal. Tombée par trois fois, elle était revenue là où elle n'avait jamais cessé d'être.
Tout commence et tout s'achève. J'entends le chant retentir. J'ai fait une dernière veille au chemin de rempart, et l'endroit m'est apparu au matin, illuminé par l'astre glorieux qui magnifiait le ruisseau.
Dans la clairière, à la jonction des chemins, j'ai suivi à senestre les eaux enchantées jusqu'à la grande roche, puis fis dix pas au nord, autant à l'est. Arrivé à la souche-majesté, je fis huit derniers pas, et ma boussole suivait le jour dernier. Là, tu trouveras la coupe du charpentier. »

Règles officielles (FAQ de l'auteur, citations exactes résumées) :
- 10 stades romains = 1 850 m (stade = 185 m), en ligne droite, tolérance ≈ 1 % (18 m).
- 3e et 11e : même nature ; un seul de chaque ; difficiles à trouver ; trouvables de chez soi (internet/cartes) ; « marcher pied nu sur la troisième : pas d'écharde ; sur le onzième : oui c'est possible » ; « il faudra marcher surtout sur l'une des deux » ; « vous allez directement de la 3e à la 11e mais ça va vous amener à passer par des étapes intermédiaires » ; « le treizième ne vous mènerait pas au bon endroit » ; « huitième et seizième donnerait un résultat incorrect » ; ils ne renvoient à aucun chevalier particulier ; personne ne les a trouvés.
- Le chemin de rempart est un point précis, point de départ ; « ensuite c'est l'astre glorieux qui vous indique où aller ; c'est là que les 3e et 11e seront utiles » ; les 3e/11e + la distance + le départ permettent d'identifier la clairière.
- La clairière (jonction de chemins = croisement de sentiers) est visible à l'œil nu depuis le rempart et proche. Le coffre est sur terrain public, loin de tout bâtiment, hors monument/zone protégée. Un ruisseau (« eaux enchantées ») part de la clairière vers une grande roche qui barre le passage.
- « Jour dernier » = 30/04/1524 (calendrier julien ; = 10/05/1524 grégorien), mort de Bayard.

Données locales (Windows, Python 3.11 avec shapely/numpy) :
- Dossier : C:/Users/Admin/AppData/Local/hermes/cache/scratch/
- Module helpers : exk_e12/geo12.py (from geo12 import * : xy, inv, hav, az, dest, load(name) pour ign/*.geojson projetés en mètres locaux, alt(lat,lon) MNT LiDAR 2 m, visible(src,lat,lon), sun_dec, etc.). Ajouter sys.path.insert(0, 'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12').
- BD TOPO IGN (≈ 6 km autour) : ign/troncon_de_route.geojson (nature: Chemin, Sentier, Route empierrée…), ign/troncon_hydrographique.geojson (cpx_toponyme_de_cours_d_eau), ign/construction_lineaire.geojson (ponts), ign/construction_ponctuelle.geojson (croix, calvaires), ign/zone_de_vegetation.geojson, ign/batiment.geojson, ign/toponymie.geojson, versions *_12km.geojson.
- OSM déjà téléchargé : exk_e12/ov_bridges_waterways_7km.json (cours d'eau + ponts 7 km), exk_e12/ov_breda.json, exk_e12/ov_breda_cross.json.
- Overpass : https://overpass.openstreetmap.fr/api/interpreter (requêtes PETITES, rayon ≤ 3 km, timeout 90 ; les grosses requêtes expirent).
- Recherche web : outils web_search / web_extract.

Exigences : n'inventer aucune donnée ; toute affirmation chiffrée vient d'un script que tu écris dans exk_e12/ et dont tu gardes la sortie (.out.txt). Toujours comparer à un contrôle aléatoire (témoins). Rapport final : candidats triés, coordonnées, distances, taux de faux positifs, et ton jugement honnête (« rien de significatif » est une réponse valable). Écris en français.
