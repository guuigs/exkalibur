# É12 — Test M2a : 3e et 11e = 3e et 11e objets d'une même classe, **rangés par distance au départ** (règle écrite le 14/10 AVANT tout calcul)

## Idée
FAQ07-120 : « toute la question, c'est de savoir quels sont ces 3e et 11e et **comment les positionner par rapport à un point de départ** ». FAQ04-115 : on va directement du 3e au 11e « en passant par des étapes intermédiaires ». Lecture la plus simple : en partant du rempart, on rencontre des objets d'une même classe, du plus proche au plus lointain ; le 3e et le 11e sont à 10 stades l'un de l'autre. Les séries **numérotées** ont déjà été testées (T18, R0610_T4 : rien) ; le **rang par distance** d'objets non numérotés ne l'a pas été.

## Règle fixée
- **Départs** (4) : donjon (45.428888, 6.031015) ; esplanade (45.42891, 6.03112) ; rue du Rempart, point BAN (45.429772, 6.03118) ; château Bayard (45.423611, 6.018889).
- **Rang** : distance en ligne droite au départ, objets triés du plus proche au plus lointain ; rang 1 = le plus proche. Objets fusionnés s'ils sont à moins de 10 m l'un de l'autre.
- **Classes** (choses « posées au sol, sur lesquelles on marche », 06-247 ; même nature, 06-009) :
  1. ponts et passerelles (OSM `bridge=*` sur une voie ; un point par ouvrage) ;
  2. passerelles seules (OSM `bridge=*` sur `highway=footway/path/track` ou `bridge=boardwalk`) ;
  3. traversées de cours d'eau par un chemin ou une route (intersection voie OSM × cours d'eau OSM) ;
  4. jonctions de chemins (nœuds OSM partagés par ≥ 3 voies `highway=*`) ;
  5. jonctions de sentiers seulement (≥ 3 voies parmi `path/footway/track/bridleway`) ;
  6. gués (`ford=*`) ;
  7. escaliers (`highway=steps`) ;
  8. croix et calvaires (`historic=wayside_cross/wayside_shrine`, `man_made=cross`) — ne se marche pas dessus, classe témoin ;
  9. fontaines, lavoirs, sources (`amenity=fountain/drinking_water/water_point`, `amenity=lavoir`, `natural=spring`) ;
  10. bancs (`amenity=bench`).
- **Critère** : |d(rang 3, rang 11) − 1 850| ≤ 18,5 m.
- **Contrôle du hasard** : pour chaque classe, 2 000 départs tirés au hasard dans un disque de 3 km autour du donjon ; part des départs qui passent le critère = p. Une touche n'est retenue que si p ≤ 2 % **et** qu'elle survit à la correction pour 10 classes × 4 départs (seuil ≈ 0,05 %), ou si deux départs voisins la donnent ensemble.
- **Ensuite seulement** : filtre public / bâti / monument (annonce du 02/07) sur le 11e et ses abords, puis ruisseau.
