# T18 — Parcours à postes numérotés autour de la tour d'Avalon (test 3e–11e = 1 850 m ± 18 m)

Script : `exk_e12/t18_parcours.py` → `t18_parcours.out.txt` ; géoréférencement du plan : `t18_sp_geo.py` → `t18_sp_geo.out.txt` ; requêtes OSM : `t18_overpass.py`, `t18p_overpass2.py` (+ `t18_ov_*.json`, `t18p_ov2_*.json`) ; PDF/PNG locaux `t18_*.pdf/png`, `stmax.pdf`.

## Résultat
**Aucun parcours trouvé où les postes 3 et 11 sont à 1 850 m ± 18 m.** Aucune coordonnée publiée pour les postes numérotés (CO, santé, patrimoine) : seuls des plans papier/PDF sont disponibles. Un seul parcours ≥ 11 postes a pu être (approximativement) géoréférencé : d(3,11) ≈ 835 m (rejeté). Les autres sont rejetés par géométrie (taille de la carte / longueur de boucle) ou par nombre de postes (< 11).

## Parcours recensés (≤ ~8 km de la tour)
| Parcours | Postes | Longueur | d(centre/départ → tour) | 11e poste ? | Verdict | Source |
|---|---|---|---|---|---|---|
| Parcours patrimoine Saint-Maximin (PDF vérifié, rendu image) | **9** (1 Tour d'Avalon, 2 Rippelets oratoire, 3 Rippelets maison XVIIe, 4 Le Crêt, 5 Les Bruns, 6 Répidon chapelle St-Joseph, 7 Église, 8 Forge Père Gauthier, 9 Étang) ; boucle 5,2 km | 5,2 km | 0 m (poste 1 = tour) | non | impossible | https://static.apidae-tourisme.com/filestore/objets-touristiques/documents/239/64/25379055/parcours+Saint+Maximin.pdf ; https://www.alpes-isere.com/sit/parcours-thematique-saint-maximin-4704227/ |
| CO patrimoine « Au temps du chevalier Bayard » (Pontcharra–St-Maximin), balises n° 61–70 | **10** (numéros de poinçon 61–70, ordre 1–10) | 5 km | 1,45 km (départ) | non | impossible | https://pontcharra.fr/1924-parcours-d-orientation-patrimoine-bayard.htm ; PDF https://static.apidae-tourisme.com/filestore/objets-touristiques/documents/48/67/30622512/Pontcharra_patrimoine_A3_2024.pdf (balise 6 « La tour d'Avalon », 8 « Château Bayard ») |
| Parcours santé patrimoine / Générations Sport Santé, Pontcharra | **11 bornes** (exercices 1–11, version connectée Isère Outdoor) | 6,7–6,9 km | 0,88 km (départ) | oui | **d(3,11) ≈ 835 m (approx.) → rejeté** | https://pontcharra.fr/581-parcours-generations-sport-sante.htm ; https://www.alpes-isere.com/itineraire/parcours-de-sante-patrimoine-5925763/ ; GPX https://static.apidae-tourisme.com/filestore/objets-touristiques/plans/81/107/11037521/Trace_Pontcharra.gpx ; dépliant https://pontcharra.fr/cms_viewFile.php?idtf=3830&path=depliant-sport-sante.pdf |
| Randonnée des Hameaux (Isère Outdoor, OSM rel. 2825942) | 4 | 5 km | ~0 | non | impossible | PDF `t18_hameaux.pdf` |
| Parcours thématique Barraux | 10 étapes | 6,5 km | 4,2 km | non | impossible | https://www.alpes-isere.com/sit/parcours-thematique-village-de-barraux-864387/ |
| Parcours thématique Chapareillan | 8 étapes | – | 7,4 km | non | impossible | https://www.alpes-isere.com/sit/parcours-thematique-chapareillan-4634166/ |
| Sentier forestier pédagogique Plateau de la Puce (Chapareillan) | **40 bornes**, 3 pupitres | 2,3 km boucle | ~7,0 km | oui | 3→11 ≈ 8 intervalles sur 2,3 km ≈ 0,5 km → exclu | https://www.alpes-isere.com/itineraire/le-sentier-forestier-pedagogique-du-plateau-de-la-puce-492625/ |
| CO patrimoine adulte Allevard (village), balises 42–52 | **11** | 2,5 km (≈ 30 m D+, carte 1:3000) | ~5,2 km | oui | zone carte < 1 km → d(3,11) ≪ 1 832 m → exclu ; balise 11 = « balise mystère » (plaques en fonte) | https://belledonne-chartreuse.com/offres/parcours-dorientation-patrimoine-adulte-allevard-fr-4707681/ ; PDF https://static.apidae-tourisme.com/filestore/objets-touristiques/documents/251/87/32921595/Allevard_Patrimoine_A3_2025.pdf |
| CO ludique Lac de la Mirande, Allevard, balises 31–41 | **11** | 1–1,5 km | ~6,9 km (lac) | oui | zone carte 1:2000 ≈ 0,4 km → exclu ; balise 11 « les grenouilles » | https://www.alpes-isere.com/itineraire/parcours-dorientation-ludique-au-lac-de-la-mirande-5992041/ ; PDF https://static.apidae-tourisme.com/filestore/objets-touristiques/documents/250/87/32921594/Allevard_Mirande_Ludique_A3_2025.pdf ; https://isereoutdoor.fr/assets/resources/res44_9023.pdf ; FFCO https://www.ffcorientation.fr/licencie/cartographie/cartotheque/10482/ |
| Autres CO « Allevard–Le Collet » (7 et 11 balises), 7 Laux | 7 / 11 | 1,5–2,5 km | ~9,9 km | – | hors rayon (> 8 km) | https://www.allevard-les-bains.com/decouvrir/les-incontournables/parcours-dorientations/ |
| Lac Saint-Clair (La Rochette / Détrier) – CO permanente + parcours santé | nb de balises non trouvé | – | ~7,8 km (lac) | ? | non évaluable : cartes en vente à l'OT, pas de PDF, pas de coordonnées trouvés | https://www.lofficiel.net/course-d-orientation-en-val-gelon_8_2746.aspx ; https://tourisme.coeurdesavoie.fr/fiches/lac-saint-clair-327130/ |
| Sainte-Hélène-du-Lac « Promènes-toi avec Hyla » ; Sentier du système solaire (La Table, 13 panneaux, 1,3 km) | ? / 13 | 3,5 / 2,9 km | > 8 km | – | hors rayon / sans données | https://tourisme.coeurdesavoie.fr/fiches/promenes-toi-avec-hyla-6700412/ ; https://tourisme.coeurdesavoie.fr/fiches/sentier-decouverte-du-systeme-solaire-5003544/ |

Rien trouvé (recherches web) pour : Laissaud, Détrier, Arvillard, La Chapelle-Blanche, Le Cheylas, Villard-Sallet, Les Mollettes, Planaise (hors Lac Saint-Clair / Hyla ci-dessus). « Parcours sportif » Chapareillan/Barraux/Le Cheylas : aucune fiche (ville-data → « pas d'équipement »).

## OSM (Overpass, rayon 3 km autour de la tour, Pontcharra, Barraux, Chapareillan, Le Cheylas, Arvillard, Allevard, Lac St-Clair)
- `leisure=fitness_station`, `sport=orienteering`, `information=route_marker` : **0 résultat à ≤ 3 km de la tour/Pontcharra/Barraux/Chapareillan/Le Cheylas**. Seulement : fitness_station Allevard (45.37807, 6.05482, ≈ 6,3 km) et Lac St-Clair (45.45179, 6.10358, ≈ 5,4 km) – sans numéro, sans parcours.
- Pas de `ref=*` numérique sur tourisme/leisure/historic à 3 km (t18_ov_ref_num.json = vide).
- 52 `tourism=information` : poteaux de randonnée Isère/Grésivaudan (guideposts) nommés, jamais numérotés comme postes d'un parcours (Les Rippelets, Le Crêt, Les Bruns, Répidon, Le Couvat, La Planta = les étapes 2–5 et « repères rando » du parcours patrimoine Saint-Maximin).
- Les postes de CO (piquets en bois) ne sont **pas** cartographiés dans OSM ici.

## Contrôle aléatoire (santé Pontcharra, seul parcours à positions estimées)
Positions des 11 pastilles lues sur le plan et géoréférencées sur le GPX officiel (ancrage visuel de l'emprise ⇒ erreur ~ ± 50–100 m, lecture « à l'œil » ; **indicatif seulement**) :
d(3,11) ≈ 835 m ; d(1,9) ≈ 446 m ; d(2,10) ≈ 777 m ; max de toutes les paires (55) = 2 539 m ; **0** paire dans 1 850 ± 18 m (5 paires > 1 832 m, aucune n'est (i, i+8)).
Taux de « coïncidence » attendu par hasard : fenêtre 36 m / étendue ≈ 2,5 km ≈ **1,4 %** par paire ; avec 3 paires (i, i+8) ≈ 4 % : ici 0 coïncidence.
Pour les autres parcours à 11 postes, aucune distribution n'est calculable (pas de coordonnées) ; la borne supérieure géométrique suffit à les exclure.

## Jugement honnête
- **Rien de significatif** : aucun parcours numéroté à 11 postes ou plus près de la tour ne place les 3e et 11e à 1 850 m (±18 m). Le parcours patrimoine de Saint-Maximin (9 postes) et celui de Bayard (10 postes) sont trop courts pour contenir un « 11e » et ne peuvent pas expliquer « le treizième / 16e » de la FAQ.
- Limite : les coordonnées des postes de CO ne sont pas publiées (cartes PDF 1:2000/1:3000 non géoréférencées) ; seuls des ordres de grandeur sont possibles. Hypothèse « CO/parcours santé » **non confirmée, non totalement exclue** pour Lac Saint-Clair (balises non documentées) ; pour le reste, aucun candidat.
- Pistes non épuisées : cartes CO de la zone dans la Cartothèque FFCO (Pontcharra/Saint-Maximin, Lac St-Clair — pages non lisibles sans JS), CDCO38 (cdco38.fr, page vide à l'extraction), Isère Outdoor (application, tracés/balises en GeoJSON non extraits), Cirkwi/Visorando pour les balises du Lac Saint-Clair.
- Piste de nature différente à garder : « de même nature, difficiles à trouver, pieds nus : 11e donne des échardes » colle mieux à des **objets naturels/mobiliers en bois** (souches, troncs, passerelles, bancs) qu'à des balises de CO ; à tester avec d'autres séries (ponts en bois, souches « majesté »).
