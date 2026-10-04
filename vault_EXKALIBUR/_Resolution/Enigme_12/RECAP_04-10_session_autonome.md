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

## 6. Session de 30 min (04/10, 06:47-07:17) — travail actif
**Robustesse de la table « Christ à l'Orient »** : avec 12 places, Simon tombe à 37-77 m de la jonction du Mouret quel que soit le centre (sommet, pied, Rue du Rempart) et le rayon (1 057-1 079 m). Avec 13 places (le Christ a sa place) : 150-190 m.
**Visibilité depuis le pied** : 15 des 32 points du mur au pied de la tour (tout le côté est) voient la clairière ; le relief ne cache la jonction depuis aucun point.
**Cohérences de la table** : on « marche surtout sur l'une des deux » (06-247) : on marche à la place 11 (Le Mouret, forêt) et pas à la 3 (Pontcharra) ; écharde possible au 11e (bois, forêt), pas à la 3e (ville) ; la « 13e place » serait celle du Christ, à l'est (90°), sur l'axe du loup : « ne vous mènerait pas au bon endroit » (06-133).
**Critères bruts de la grande roche** (FAQ) : « très difficile à manquer » (03-211) ; mouillée (FAQ8) ; « vous bloquera vraiment le passage », aller au-delà le long du ruisseau « supposerait de quitter votre route » (06-195, FAQ8) ; pieds mouillés possibles avant la roche, pas après (06-090) ; on la touche difficilement sans se mouiller (06-180) ; depuis la souche on ne la voit plus (06-167) ; une seule étape entre la roche et la souche (07-182) ; une fois la jonction trouvée, le coffre est « tout près » (05-051).
**Balayage des culs-de-sac au bord de l'eau** (`t41_deadend_rock.py`, 39 sur toute la zone) : les plus rocheux sont sur le versant de Bramefarine (2-3,4 km, cap 132-172°), dont deux sur le **Rebouchet amont, dans la forêt communale de Pontcharra** (A : 45.414182, 6.051137, escarpement de 207 m² ; B : 45.416809, 6.049903, à une confluence, en limite de la forêt communale). Depuis la jonction du Mouret : 1,16-1,85 km par les chemins, rive gauche sur 900 m puis traversée du ruisseau. Trop loin pour « tout près » ; aucune jonction visible de la tour sur ces chemins. Image : `images_travail/t41_rebouchet_amont_culs_de_sac.jpg`.
**Points de fouille au Mouret** (`t41_dig_public.py`), roche + 10 pas N + 10 pas E (souche) + 8 pas vers 90° / 67,6° / 72,4°, pas de 0,75 ou 1,48 m :
- rocher de 4 m (45.421452, 6.045319 ; 107 m² ; au bord du Rebouchet, rive droite, ~410 m de la jonction, 131 m au-dessus du bout du chemin de l'est) : fouille vers 45.42151-45.42162, 6.04549-6.04567, en bordure ou dans la bande publique du Rebouchet, maisons à 167-183 m ;
- affleurement de 48 m² (45.423697, 6.041412 ; rive gauche, à 25 m de la jonction 2) : fouille vers 45.42376-45.42386, 6.04159-6.04177, à 0-4 m de la bande publique, maisons à 136-152 m.
**Jonction 2** : sous les arbres (0 % ouvert à 40 m) : pas une clairière. **Le Rochat** (vallon de La Perrière, ruisseau permanent, sur le sentier « Sur les traces du chevalier Bayard » qui part de la tour d'Avalon) : visible seulement du sommet ; petites roches. **Champ-Laurier** (carrefour du sentier Bayard, où tombe le vecteur gourde → scie) : invisible de la tour.
