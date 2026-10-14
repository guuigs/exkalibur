# É12 : nature des 3e/11e, gabarit de la Via Dolorosa, contour du bassin (14/10, nuit)

## 1. Relecture des 52 réponses de la FAQ sur les 3e/11e — une correction
- **07-068** : pieds nus, « sur la troisième : non [pas d'écharde]. Par contre, sur le onzième, oui, c'est possible ». L'auteur passe spontanément au **masculin** pour le 11e (le joueur avait dit « la troisième ») ; 03-293 : les deux genres sont possibles.
- **Correction pour la lecture « chapitres III et XI du *Roman de la Rose* »** (tête de liste de la session cloud) : le chap. III, c'est **le guichet de bois de charme** qu'ouvre dame Oiseuse. Une porte en bois donne une écharde possible **sur la 3e**, ce que 07-068 exclut. La parade (« on franchit le guichet sans marcher dessus ») contredit 06-247 (« il faudra marcher surtout sur l'une des deux »). Cette lecture perd donc son statut « passe toutes les D » : **à rétrograder au même rang que les autres**.
- Rappels utiles : on place **deux points** sur la carte, qui ne se voient pas sur Maps (05-074) ; ils ne servent pas à confirmer le tracé de l'É11 (07-281) ; il faut d'abord faire l'ultime traversée (04-134) ; « tout est codé » dans les enluminures, la carte ou les énigmes (04-027).

## 2. Règle VD : le chemin de croix de la Via Dolorosa réelle comme gabarit
Règle commitée avant le calcul (`VD_regle_via_dolorosa.md`) ; stations I à XIII et tombeau = OSM (`data/osm_via_dolorosa.json`) ; script `scripts/vd_via_dolorosa.py`.
- Pourquoi cette série : 3e station = 1re chute (pavé de pierre) ; 11e = cloué sur la croix (bois) ; 13e existe, pas de 16e ; « directement de la 3e à la 11e en passant par des étapes intermédiaires » ; « tombée par trois fois » ; titres *Ecce Homo* / *Consummatum est* ; « marche vers la Jérusalem terrestre, utile autrement ».
- Placement sans paramètre libre : échelle fixée par III → XI = 1 850 m (×6,78), orientation de la carte réelle, station I ou III posée au départ.
- **Résultat : négatif.**
  - Station I au départ : XI-XIII tombent à 2,95 km à l'OSO, en terrain privé non boisé.
  - Station III au départ : XI tombe **dans Pontcharra**, en terrain privé, à 7-46 m de bâtiments.
- Seule curiosité : depuis la rue du Rempart, variante III, la **XIVe** (tombeau) tombe dans un bois public de la C.C. Le Grésivaudan au bord du Bréda (45.42118, 6.00839 ; bâti 51 m, eau 20 m). Depuis l'esplanade, à 96 m de là, elle tombe sur une parcelle privée (crédit-bail immobilier). Trop fragile pour compter : **noté, non retenu**.
- La lecture « chemin de croix » reste la plus cohérente avec la FAQ pour la **nature**. C'est son **placement** qui manque : le gabarit brut ne marche pas.

## 3. E19 : contour du bassin de l'enl. 9 contre tous les plans d'eau à ≤ 15 km
Script `scripts/e19_bassin_15km.py` (même contour peint et même mesure que t124) : **499 formes**.
- Le meilleur score d'IoU est 0,90 (une retenue sans nom à 16 km) ; 20 formes dépassent 0,85.
- La meilleure partie du Lac du Vernay est **16e** (0,854) ; le grand lac est 82e (0,813).
- **Conclusion : le contour seul ne discrimine pas** (la forme peinte est un ovale arrondi que la moitié des étangs imite). La remarque de l'auteur (« le contour de ces eaux permettrait peut-être d'identifier une réponse ») vise sans doute un détail du contour (cascade, roche, arbre, coupe), pas la silhouette globale.

## 4. Où en est-on
Mort cette nuit : le modèle « 10 stades = départ → clairière » sur toutes les directions (R1410d) ; M2a et M2b (R1410c) ; règle J ; gabarit Via Dolorosa brut ; silhouette du bassin.

Vivant :
- **(a)** nature « chemin de croix » (passe les D) avec un placement à trouver (orientation par le ciel ?) ;
- **(b)** un autre départ ;
- **(c)** les sens de « marche » non testés (marche d'escalier ; Les Marches).
