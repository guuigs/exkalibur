# É12 — Récapitulatif de la session autonome (04/10/2026)

## 1. Idée de Guilhem : la rayure (SVG) = le chemin de la tour au croisement final
- Structure de la rayure : un long tracé sinueux (longueur/corde = 1,62) qui finit sur un point où se rejoignent 3 traits (jonction), avec une courte « queue » qui repart.
- Test (`outils_scratch/t40_svg_route.py`) : 4 237 itinéraires réels sur les chemins BD TOPO, du pied de la tour à chaque croisement (300 m-4 km), comparés à la rayure (alignement des extrémités, puis écart moyen). Témoin : la rayure retournée en miroir.
- Résultat : meilleur score 0,046, miroir 0,045. Avec la sinuosité et la direction de la queue : réel 0,065, miroir 0,045. **Aucun signal**. L'itinéraire tour → Le Mouret est dans la moyenne (meilleur que 56 %).
- Limite : un chemin non cartographié pourrait échapper au test.

## 2. Méthode « terrain d'abord » (sans théorie sur les 3e et 11e)
- Visibilité complète depuis le pied (yeux à 1,7 m) et le sommet (+33 m) de la tour, LiDAR 1 m, arbres compris, en ignorant les 15 premiers mètres (`t40_viewshed_pied.py`).
- Crible de tous les croisements réels de la zone LiDAR (7 × 7 km) : maisons ≥ 100 m, au moins 30 m² de sol ouvert visible à 60 m, forêt ≥ 35 % autour (clairière), eau ≤ 150 m (BD TOPO ou talweg LiDAR) (`t40_terrain_first.py`).
- 117 croisements passent les deux premiers critères, 19 tous les critères, et **seulement 2 sont visibles depuis le PIED de la tour, tous les deux au MOURET** : la jonction de 4 chemins (45.422426, 6.040299 ; 411 m² visibles du pied) et la jonction 2 (45.42337, 6.041663 ; 52 m²).
- Cela recoupe, par une méthode indépendante, la table des apôtres « Christ à l'Orient » (place de Simon à 48 m de la jonction).
- Les autres sites (visibles seulement du sommet) : Le Rochat (Saint-Maximin, 1,4 km au sud, sur un chemin public), Laissaud (Le Mas de Coise, Coise, château Beauregard), Barraux (La Fournache), La Buissière, Le Cheylas, Pontcharra (écartée).

## 3. Le Mouret : ce qu'on sait maintenant
- Jonction de 4 chemins sur un chemin public (non cadastré). Le pré visible du pied de la tour commence à 39 m.
- **Un talweg LiDAR (bassin 2,5 ha) coule dans le chemin qui part vers l'est** : sur les 125 premiers mètres, il est à 1-7 m du chemin, presque toujours à GAUCHE en montant (chemin creux). On marche donc sur un chemin public, sur la rive gauche, l'eau à gauche, en montant dans la forêt. La tête du talweg est à 45.422555, 6.041822 (z 553 m).
- Le chemin de l'est continue jusqu'à 45.422164, 6.043982 (z 600 m, sur une bande publique) près du Rebouchet et de ses affleurements (rive gauche).
- Le sentier plat vers le nord-est mène à la jonction 2 (sous la ligne haute tension, couloir déboisé) ; affleurement de 48 m² haut de ~2 m à 25 m (45.423566, 6.041667) ; Rebouchet à 65 m.
- Deux sources (BD TOPO) à 74 et 162 m au sud.
- Soleil au sol : 8 h 40 le 30/04, 7 h 37 le 21/06.
- Faiblesses : le croisement est en lisière, sous les arbres ; terrains privés autour (seuls les chemins et une partie des ruisseaux sont publics) ; pente du chemin de l'est 22-35 % ; grande roche non identifiable au LiDAR (normal d'après FAQ07-126).

## 4. Loup : état
- Seule clairière visible du pied sur l'axe : un pré à 1 287 m (45.42773, 6.04751), sans croisement dedans ; les croisements voisins touchent le hameau des Ripellets (maisons à 9-26 m).
- Forêt communale de Pontcharra B0071 près de l'axe, longée par un ravin LiDAR de 1,4 km ; J5 privé et invisible du pied.
- Conclusion : le loup ne passe pas le crible « terrain d'abord ».

## 5. À faire (Guilhem)
- Regarder les photos en ligne (Google Maps, photos de randonneurs) du chemin qui monte vers l'est depuis la jonction du Mouret, et de la jonction 2 (affleurement).
- Décider la lecture finale de « à senestre » au Mouret : chemin creux de l'est (eau à gauche) ou sentier vers la jonction 2 et le Rebouchet.
- Préparer la soumission : capture vue du ciel de la clairière et de la jonction, avec un paragraphe sur le parcours (FAQ07-078).
Images : `images_travail/t40_mouret_synthese.jpg`.
