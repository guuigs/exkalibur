# É12 — R0610 sentier Bayard + ponceaux (N2 web + D2 franchissements)

Date : 06/10/2026. Sous-agent « SENTIER BAYARD + PONCEAUX ». Ton factuel, aucune visite terrain, aucune demande à un tiers. Données : web (Apidae, alpes-isere, minizou, pontcharra, PDF officiels) + BD TOPO (WFS data.geopf.fr, 3 km autour de la tour).

---

## Verdict global (en tête)

- **N2 (panneaux/balises des itinéraires Bayard → série ≥13 d'objets « de même nature » liés aux écrits du narrateur) : RIEN.** Deux séries physiques existent, mais ni l'une ni l'autre n'atteint 13 éléments : le parcours thématique Saint-Maximin (9 étapes) et le parcours d'orientation patrimoine Bayard (10 balises numérotées 61–70). Aucun 11e ni 13e local ; aucun panneau numéroté sur la boucle « Sur les traces du chevalier Bayard ». Impossible de former une paire 3e/11e à 1 850 m à partir de ces dispositifs.
- **D2 (franchissements de ruisseaux par les CHEMINS, numérotés le long de chaque chemin, 3e pierre / 11e bois à 1 850 m) : RIEN.** 847 tronçons de chemin/sentier/route-empierrée et 73 franchissements chemin×ruisseau dans 3 km de la tour. Décomposé en 713 « chemins » linéaires : le plus fourni ne compte que **5 franchissements** ; aucun chemin n'a de 11e franchissement. Le test 3e↔11e est structurellement impossible.

---

## 1. N2 — Inventaire précis des itinéraires liés à Bayard autour de la tour

### 1.1 Boucle « Sur les traces du chevalier Bayard » (3,9 km)
- **Source** : fiche Apidae alpes-isere.com `375911` + minizou.fr `2336`. Départ au pied de la tour d'Avalon (45.429128, 6.03054, alt. 390 m). 3,9 km, 141 m D+, 1 h, toute l'année.
- **Itinéraire** : tour → Avalon → La Corbassière → château Bayard → La Perrière par Chaffardon → La Combe (ancien lavoir + calvaire en pierre) → Les Côtes → Le Châtelard → Le Vivier → tour.
- **Signalétique physique** : poteau indicateur « Tour d'Avallon » (gauche « Maison Bayard », droite « Rue du Rempart ») ; calvaire en pierre + ancien lavoir à « La Combe » ; château Bayard (maison forte XVe, propriété privée, fermée). **Aucun panneau numéroté** recensé sur le web.
- **KML Apidae** (`sitraLOI964088_365867_2061.kml`) : **partiel** — LineString de 51 points, longueur reconstituée **3 427 m** (au lieu de 3,9 km), bbox lat 45.41861–45.42914 / lon 6.02088–6.03065 (il couvre tour → château → La Perrière, mais pas la boucle nord La Combe/Les Côtes/Le Châtelard/Le Vivier). Sauvegardé en **GPX** : `donnees_travail/r0610_sentier/bayard.gpx` et `bayard.kml`.
- **Franchissements de ruisseaux sur le KML** (partiel) : 4 — Ruisseau de Rebouchet (×2), Ruisseau de la Perrière (×2). Le minizou confirme le passage « au-dessus du petit ruisseau Le Rechouchet » à Chaffardon (= Ruisseau de Rebouchet).

### 1.2 Parcours thématique Saint-Maximin — **9 étapes** (alpes-isere.com `4704227`)
Panneaux/plaques numérotés 1→9 (bornes patrimoine) :
1. Tour d'Avalon et son bourg (33 m, seigneurs Wallon/Romestang d'Avalon, dès l'an 1000)
2. Oratoire (ancien oratoire dans un mur)
3. Les Rippelets, maison XVIIe
4. Point de vue le Crêt (panorama Chartreuse)
5. Les Bruns, ancienne magnanerie (sériciculture)
6. Répidon — chapelle St Joseph
7. Église (achevée 1888)
8. Forge du Père Gauthier (1910)
9. Le Vivier, étang (créé 1261, prieuré clunisien)
- PDF officiel : `parcours+Saint+Maximin.pdf` (Apidae, 6,7 Mo, 2 pages image). Centré 45.428254, 6.037862.

### 1.3 Parcours d'orientation patrimoine « Au temps du Chevalier Bayard » (Pontcharra–Saint-Maximin) — **10 balises 61–70**
- 5 km, 140 m D+, 2 h, départ square Jean Menétrey (95 av. de la Gare, Pontcharra, 45.433749, 6.01339). Carte : `Pontcharra_patrimoine_A3_2024.pdf` (Apidae `30622512`).
- Balises et leurs supports (lu sur la carte) :
  - **61** La Statue Bayard (place de la mairie) — lampadaire
  - **62** Le Torrent du Bréda (derrière le château, ancienne douve) — barrière
  - **63** Bayard, une légende — limite de végétation
  - **64** Sur le côteau de Saint-Maximin (hameau d'Avalon) — lampadaire
  - **65** Le Prieuré (monastère cistercien XIIe) — lampadaire
  - **66** La Tour d'Avalon — panneau
  - **67** La Courbassière (maison défensive) — **pylône bois**
  - **68** Le Château Bayard (XVe, musée) — arbre
  - **69** Les Murailles (rive gauche du Bréda) — arbre
  - **70** L'Église de Grignon — arbre
- **Numérotation 61–70** = tranche régionale du dispositif « Espaces loisirs orientation en Isère » (balises jusqu'à 100 sur la carte de synthèse) ; ce n'est pas une série Bayard autonome.

### 1.4 Conclusion N2
Aucune série de **≥13** objets « de même nature » liés à Bayard/à ses écrits le long de ces tracés. Les seules séries numérotées sont 9 (Saint-Maximin) et 10 (orientation 61–70) — cohérent avec l'écart déjà posé dans `PISTES_ECARTEES.md` (« parcours de 9 ou 10 étapes » mort). Les chapitres III/XI/XIII du *Loyal Serviteur* citent des lieux hors zone (Savoie, Naples, Carignan) — confirmé par `R0610_N2N3_narrateur.md`. **Pas de paire 3e/11e possible** : ni le parcours de 9 (pas de 11e), ni celui de 10 balises (pas de 11e locale : la tranche s'arrête à 70, le 3e local = balise 63, pas de 11e local).

---

## 2. D2 — Franchissements de ruisseaux par les chemins (≤3 km de la tour)

**Méthode** : BD TOPO 3.0 (WFS `data.geopf.fr`, couches `troncon_de_route` et `troncon_hydrographique`), bbox EPSG:2154 de 6×6 km centrée sur la tour (936937.5, 6485588.9). Chemins = nature {Chemin, Sentier, Route empierrée} ; ruisseaux = « Écoulement naturel ». Intersections segment×segment, dédupliquées à 8 m, puis attribution à chaque « chemin » (chaîne linéaire : séquence de tronçons reliés bout-à-bout par des nœuds de degré 2).

| Quantité | Valeur |
|---|---|
| Tronçons de chemin (Chemin/Sentier/Route empierrée) dans 3 km | 847 |
| Tronçons d'écoulement naturel dans 3 km | 158 |
| **Franchissements chemin×ruisseau uniques** | **73** |
| « Chemins » linéaires (chaînes) | 713 (612 à 1 tronçon ; max 4 tronçons) |
| **Max de franchissements sur un même chemin** | **5** |

**Résultat : aucun chemin n'a 11 franchissements.** Le maximum est 5 (une route empierrée de 985 m près du Ruisseau de Rebouchet, ~2,5 km à l'est de la tour). Les 4–5 franchissements qu'on trouve sont à quelques centaines de mètres les uns des autres le long du chemin, jamais à 1 850 m. Le test « 3e franchissement (pierre) ↔ 11e (bois) à 1 850 m ±1 % » ne peut pas être évalué : il n'existe pas de 11e franchissement sur un même chemin. Verdict : la prémisse de la piste D2 (une série de ≥11 franchissements le long d'un chemin) est **fausse dans cette zone**.

**Test du hasard** : sans paire 3e/11e candidate, il n'y a aucune coïncidence à contrôler (règle 4 du brief). Le résultat est un fait de comptage (décompte exact des franchissements par chemin), pas une coïncidence ajustée. Aucun paramètre libre n'a été utilisé.

---

## 3. Ce qui est établi de positif (utile pour la suite)

1. Le lien « fort et évident » de FAQ07-030 est bien localisé et physique : la boucle « Sur les traces du chevalier Bayard » **part du pied de la tour** et traverse le pays natal de Bayard (tour → château natal → La Perrière/Chaffardon → La Combe/Le Vivier). Le narrateur (Bayard) est bien « chez lui » sur ces 3,9 km.
2. Les seuls objets physiques « de même nature » liés à Bayard dans la zone sont : **10 balises d'orientation 61–70** (dont 66 = Tour d'Avalon sur « panneau », 67 = La Courbassière sur « pylône bois ») et **9 bornes patrimoine Saint-Maximin**. Ni l'un ni l'autre ne forme la série 3e/11e à 1 850 m recherchée.
3. La boucle franchit 4 ruisseaux nommés (Rebouchet ×2, La Perrière ×2 sur le KML partiel) ; l'étang du Vivier et le Bréda encadrent la zone. Ces franchissements sont trop peu nombreux et trop rapprochés pour une numérotation 3e/11e à 10 stades.

## 4. Recommandation

- **Ne pas relancer** N2 « série ≥13 de panneaux/balises Bayard » ni D2 « 3e pierre / 11e bois à 1 850 m sur un chemin » : les deux prémisses (série ≥13, chemin à ≥11 franchissements) sont réfutées par le terrain + les données.
- Le seul angle N2 restant est la **géolocalisation fine** des 10 balises 61–70 et des 9 bornes (positions GPS absentes du web, présentes seulement sur la carte image du PDF) pour vérifier, par exemple, si **balise 63 ↔ balise 70** (ou toute paire du dispositif) tombe à 1 850 m — mais rien dans la disposition actuelle ne le suggère (parcours de 5 km étalé Pontcharra→Saint-Maximin).
- Conserver les livrables réutilisables : `bayard.gpx`/`bayard.kml`, les deux PDF (Saint-Maximin, Pontcharra), et les données BD TOPO (`wfs_troncon_de_route.json`, `wfs_troncon_hydrographique.json`) pour tout futur calcul dans 3 km.

## 5. Fichiers produits
- Scripts : `outils_scratch/r0610_fetch_bayard_wfs.py` (téléchargement BD TOPO), `outils_scratch/r0610_sentier_bayard.py` (croisements bruts + composantes), `outils_scratch/r0610_sentier_bayard_d2.py` (chaînes linéaires + numérotation).
- Données : `donnees_travail/r0610_sentier/` (bayard.kml, bayard.gpx, deux PDF, wfs_troncon_de_route.json, wfs_troncon_hydrographique.json).
- Rapport : ce fichier.

## 6. Sources
- alpes-isere.com `375911` (boucle Bayard, KML), `4704227` (parcours Saint-Maximin 9 étapes), `7125489` (orientation Bayard, PDF `Pontcharra_patrimoine_A3_2024.pdf`).
- pontcharra.fr `1924` (parcours orientation, 10 balises, PDF carte), minizou.fr `2336` (description boucle, « Rechouchet », calvaire La Combe).
- BD TOPO 3.0 via WFS data.geopf.fr (troncon_de_route, troncon_hydrographique, 3 km autour de la tour).
