# T18 — Séries numérotées autour de la tour d'Avalon : test « 3e–11e = 1 850 m ± 18 m »

Script : `exk_e12/t18_series.py` (Python 3.11) · sortie : `t18_series.out.txt` · collecte Overpass : `t18_fetch.py`, `t18_fetch2.py` (+ `.out.txt`).
Données brutes : `t18_boundary.json`, `t18_golf.json`, `t18_ref3km_xy.json`, `t18_hameaux_rel.json`, `t18_bornes.kml` (KMZ), `t18_hameaux.gpx/.pdf`.

## Sources (URLs)
- Bornes 1822/1823 Dauphiné–Savoie, relevé KMZ : https://www.sentier-nature.com/montagne/public/traces/bornes-frontiere/bornes-frontiere-dauphine-savoie.kmz (page : https://www.sentier-nature.com/montagne/post/2014/10/05/col-granier-bornes-frontiere)
- Inventaire photo n°7–50 : https://ch-perrier.pages-perso.free.fr/chartreuse/bornes_dauphine_savoie.html (« Pas en Chartreuse pour les 1 à 6 », 7 = Les Échelles, 9-10 = St-Pierre-d'Entremont, 11 = socle au bord du précipice ; pas de coordonnées)
- Topos : https://www.altituderando.com/Les-bornes-frontiere-Dauphine-Savoie-entre-Chapareillan-et-les-Marches-et-le (bornes 39–44) ; …-le-long (45–49) ; …-entre-Pontcharra-et-Laissaud (52–58)
- Tourisme Cœur de Savoie : https://tourisme.coeurdesavoie.fr/fiches/les-bornes-sardes-6235786/
- OSM Overpass (overpass.openstreetmap.fr) : `historic=boundary_stone` à 15 km ; `golf=*`/`leisure=golf_course` 15 km ; nœuds `ref`, `lwn_name`, pylônes, hydrants à 3 km ; relation 2825942 « Randonnée des Hameaux ».
- Randonnée des Hameaux : https://www.alpes-isere.com/itineraire/randonnee-a-la-decouverte-des-hameaux-436064/ (GPX + topo PDF Isère Outdoor).

## Résultats
| Série | Effectif | 3e / 11e | 3e–11e | Verdict |
|---|---|---|---|---|
| Bornes 1822 (KMZ sentier-nature) | 35 n° (5…92) | **3 et 11 absents** | – | B05–B10 = 26,9 km → 3e–11e sont de toute façon à ≫ 1,85 km ; la borne la plus proche de la tour est à 7,3 km (n°46 OSM) |
| Bornes OSM `boundary_stone` + ref (15 km) | 14 n° (9…46) | absents | – | – |
| Paires (i,i+8) des bornes | 25 (KMZ) + 1 (OSM) | – | aucune à 1850±18 | – |
| Toutes paires de bornes | 595 / 91 | – | seule : 40–43 = 1 857 m (KMZ) / 1 854 m (OSM), hors tour (≈ 8,7 km) | sans pertinence (pas 3/11, ni i+8) |
| Pylônes RTE (OSM ref 0–20, 3 km) | 21 n° (27 pts) | 3 : 2 pylônes (lignes différentes) ; 11 : 1 | 1 144 m et 1 513 m | **non** |
| Poteaux incendie (OSM ref, 3 km) | 76 n° | 0003 et 0011 | 686 m | **non** (seule paire i,i+8 : 75–83 = 1 846 m, non 3/11) |
| Randonnée des Hameaux | 4 pastilles numérotées sur le topo (1–4) ; GPX 310 trkpt sans waypoint ; nœuds réseau OSM = noms (La Planta, Le Couvat…), **aucun numéro** | pas de 11e | – | exclu |
| Golfs ≤ 15 km | Porte-de-Savoie (8,1 km), Granier-Apremont (11,1 km) ; **0 `golf=hole`** dans OSM | trous 3/11 non géoréférencés | – | non testable (aucune coordonnée disponible ; non inventé) |
| Nœuds réseau pédestre Grésivaudan (25 nœuds ≤ 3 km) | `lwn_name` seulement, aucun `rwn_ref`/`ref` | – | – | exclu |

## Contrôle
- Pour 2 points aléatoires dans un disque de 3 km : P(d = 1850 ± 18) = 0,92 % (200 000 tirages). Sur « toutes paires » : bornes 0,17–1,1 %, pylônes 0,58 %, hydrants 1,52 % → conforme au hasard.
- Rien ne se détache : aucune paire (3e,11e) réelle à 1 850 m ±18 m dans les séries numérotées testées.

## Jugement honnête
- **Négatif / rien de significatif.** Les bornes frontière 1760/1822 de la zone Pontcharra–Chapareillan–Les Marches portent les n° 39–58 (nord) et 14–35 (Chartreuse) ; les n° 3 et 11 sont à des dizaines de km (Ain/Isère sud, Les Échelles…), jamais autour de Saint-Maximin. Elles ne peuvent pas « être trouvables de chez soi » en 3e/11e à 1,85 km.
- Les bornes frontière sont toutes ≥ 7,3 km de la tour ; la frontière actuelle de la zone est 8–9 km au NE/E.
- Limites : OSM n'a pas les n° 1–8 ; le KMZ n'a pas non plus les n° 1–4 ; coordonnées des trous de golf non disponibles ; pas d'inventaire exhaustif des bornes kilométriques/PR (non testé, pas de ref numérique dans les données OSM proches). Les pylônes ont deux lignes dupliquant les refs (ambiguïté, toutes combinaisons testées).
- Remarque sur la série de pylônes : (6,10)=1 833 m et (4,13)=1 859 m existent mais ne sont ni 3–11 ni i+8 (donc ignorables ; l'énigme impose 3e et 11e, 13e et 8e/16e donnent d'autres résultats).
