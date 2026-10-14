# R1110_TXT — Nature des 3e et 11e à partir des textes (11/10/2026)

**Verdict : RIEN de fiable (aucune nature ne passe la règle de fiabilité).** Une nature textuellement séduisante (stations du chemin de croix) n'a aucun objet réel dans 10 km ; les natures « physiques » (ponts/passerelles) sont au niveau du hasard.

## 1. Le *Roman de la Rose* — énumérations ≥ 13 (FAIT, vérifiées par script)
Script : `outils_scratch/r1110_txt_verif.py` (texte Gutenberg 16816 UTF-8, `scratch/exk_txt/g16816.txt`, pages impaires = traduction Marteau ; sortie `donnees_travail/r1110_txt_listes.json`). Numéros = lignes du fichier .txt.

| Liste (traduction Marteau) | N | 3e | 11e | 13e | Placeable ? |
|---|---|---|---|---|---|
| **Oiseaux** (l. 5887-5938) | **13** | tourterelles (l. 5888) | étourneaux (l. 5935) | perruches (l. 5938) | non (êtres vivants) |
| **Arbres** (l. 7577-7646) | 30 | dattiers (7584) | noisetiers (7636) | noix (7637) | non (plusieurs arbres par espèce, C2) |
| Carole (personnes), baronnie d'Amour (24-25 noms dans les sommaires, l. ~733-746 et ~1676-1680) | 16 / 24 | – | – | – | non (allégories) |
| Images du mur (10), flèches (5+5) | 10 | – | – | – | pas de 11e |

Notes : (a) l'énumération des oiseaux fait **exactement 13** → colle à FAQ06-133 (13e existe) et à C10 (pas de 16e). (b) Ancien français : ordre différent (3 estorniaus, 11 melles, 13 papegaus) ; l'auteur cite Marteau, donc retenir Marteau. (c) FAQ07-088 dit que la 1re phrase confirme **la zone finale**, pas les 3e/11e : le Roman (fontaine, pierre, grand pin, matin) décrit un **lieu**, pas une série. (d) La traduction ne contient aucune liste de ponts, marches ou dalles.

## 2. Autres textes
- **Chemin de croix (14 stations)** — vérifié sur Wikipedia EN : 3e = « Jesus falls for the first time », 11e = « Jesus is nailed to the Cross », 13e = « taken down from the Cross » ; chutes aux stations 3, 7, 9. Échos avec l'É12 : « Tombée par trois fois », « coupe du charpentier » (bois), « Tout commence et tout s'achève », « étapes intermédiaires » (FAQ04-115 : stations 4-10), 13e existe mais mène ailleurs, pas de 16e, écharde : 3e (chute au sol) non / 11e (croix en bois) oui. **HYPOTHÈSE textuelle**, pas un fait.
- Malory (Caxton : 21 livres, 506 chapitres — Wikipedia EN) ; Monmouth, Règle du Temple, Loyal Serviteur : listes de livres/articles/chapitres, **non placeables** (chapitres déjà morts). Non revérifié en détail (budget).
- Bible : livres, tribus, apôtres : non placeables ; apôtres/tribus déjà traités ailleurs.

## 3. Grille (3 meilleures natures)
| Critère | N1 Stations chemin de croix | N2 Ponts/passerelles (pierre-métal ≠ bois) | N3 Oiseaux du Roman |
|---|---|---|---|
| C1 même nature | ✓ | ✓ | ✓ |
| C2 un seul de chaque | ✓ (si un seul chemin) | ? (numérotation ambiguë) | ✗ |
| C3-C4 deux points / 1 850 m | ? | ✓ possible | ? |
| C5 pas visible Maps | ✓ | ✗ (ponts visibles) | ? |
| C7 écharde | ✓✓ (sol / croix bois) | ✓ | ✗ |
| C8 marcher sur | ~ (marcher le chemin) | ✓ | ✗ |
| C9 13e existe / C10 pas de 16e | ✓ / ✓ | ? | ✓ / ✓ |
| C11, C12 | ✓, ✓ | ✓, ✓ | ✓, ✓ |
| C14 étapes intermédiaires | ✓ | ✓ | ? |
| C16 codé dans énigmes/enluminures | ~ (échos textuels) | non | ~ (« chant ») |
Score indicatif : N1 ≈ 13/20 compatibles, N2 ≈ 9, N3 ≈ 7 (le reste « ? »). Les « ? » ne sont pas des ✓.

## 4. Existence réelle autour de la tour (45.4288, 6.03078)
Scripts : `r1110_txt_osm.py`, `r1110_txt_an1.py`, `r1110_txt_hasard.py` ; données `donnees_travail/r1110_txt/osm_*.json` (Overpass, rayon 10 km).
- **N1** : OSM : 33 croix de chemin, 3 oratoires, 46 mémoriaux, **aucun chemin de croix ni station** ; seul toponyme « Chemin de Croix-Verpi » (route, 7,4 km). Web : rien d'extérieur trouvé (Cevins/Barraux/Lourdes = hors zone). Paires croix+oratoires à 1 850 m ±1 % avec un point à < 2,5 km de la tour : **0** (hasard : 0,07 attendu). → **inexistant**.
- **N2** : 263 ponts/passerelles OSM, 118 sur chemins ; aucun taggé « bois » (6 « boardwalk »). Paires à 1 850 m ±1 % (un point < 2,5 km de la tour) : 15 (tous ponts) et 4 (passerelles). Test hasard 1 000 tirages : points uniformes → p < 0,001 (biaisé, les ponts suivent les rivières) ; **points jitterés de 400 m (garde le regroupement) → moyenne 16,8, p = 0,70 (tous) et 0,19 (passerelles)** → **niveau du hasard**. Cohérent avec t29/t55 des pistes écartées. Aucun lien avec un texte.
- **N3** : aucun toponyme « tourterelle/étourneau/sansonnet » dans 15 km d'après R5 (03/10, non refait : Overpass a répondu 504 ×3 sur la requête de noms, `r1110_txt_noms.py` prête à relancer).

## 5. Conclusion
- Aucune nature n'est FIABLE. La seule cohérence textuelle forte avec C7/C9/C10/C14 est **les stations du chemin de croix** (3 = 1re chute, 11 = crucifixion), mais aucun chemin de croix extérieur n'existe dans la zone → cohérent avec FAQ « pas visibles sur Maps », donc **ne pas écarter** : un chemin de croix pourrait être non cartographié (oratoires/niches, ou stations dans une chapelle) mais l'écart de 1 850 m l'exige long de ~3 km.
- Prochain test : chercher un chemin de croix extérieur long (≥ 3 km, stations ~231 m) ou une série de 14 croix/niches dans un rayon de 6 km (inventaire diocésain de Grenoble-Vienne, Mérimée/Palissy, cadastre « calvaire »), sans passer par OSM.
