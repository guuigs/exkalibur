# R1110 HIST — Persistance historique de la clairière (11/10/2026)
**Verdict : RIEN de fiable (au mieux 3 PISTES FAIBLES au niveau du hasard).**

## Méthode (règles posées avant lecture)
Sources : WMS IGN Géoplateforme, EPSG:2154, 5×5 km centrés sur la tour (936937, 6485589) : `GEOGRAPHICALGRIDSYSTEMS.ETATMAJOR40`, `AN-IGNF_GEOGRAPHICALGRIDSYSTEMS.CASSINI`, `ORTHOIMAGERY.ORTHOPHOTOS.1950-1965`, **`IGNF_FORETS-ANCIENNES`** (forêt ancienne = boisée depuis le milieu du XIXe, issue de la BD CARTO État-major ; couleurs vérifiées sur la légende : vert foncé = ancienne, vert clair = récente, rose = disparue). Images : `donnees_travail/r1110_HIST/` (mosaïques) et `images_travail/r1110_HIST/`. Scripts : `outils_scratch/r1110_HIST_{fetch,crible,persist,fa,hasard,montage,montage2}.py`.
Étiquette « Ayallon » sur l'État-major à l'emplacement de la tour : géoréférence cohérente.

## Faits
1. **La forêt autour de la tour est en grande partie récente** : dans les 5×5 km, 20 % ancienne, 22 % récente, 3 % disparue ; parmi les pixels MNH > 5 m : 41 % ancienne, 38 % récente, 1 % disparue, 20 % non classée. Sur l'État-major et l'ortho 1950, les pentes sont des prés/cultures hachurés avec hameaux (maisons rouges) ; l'ouvert passe de ~51 % (1950, proxy texture) à 37 % (LiDAR). Donc « clairière restée clairière » est contraignant, mais la plupart des trouées ouvertes actuelles encerclées de forêt récente sont d'anciens prés.
2. **Crible A** (jonctions modernes ouvertes ≥ 40 % à 15 m, forêt ≥ 60 % à 30-70 m, eau ≤ 50 m, hors Pontcharra, ≤ 2,5 km) : 324 jonctions → 6. Lecture État-major/ortho : forêts de pente ou ponts sur l'Isère ; aucune clairière.
3. **Crible B** (patch ouvert LiDAR ≥ 300 m², ouvert en 1950, forêt autour, eau ≤ 50 m, jonction ≤ 30 m) : 2 survivants (937473, 6484706 : pré à 104 m d'une maison ; 936730, 6487895 : Savoie, 73141). Pas de clairière en forêt.
4. **Crible C (le plus net)** : patch ouvert 300-30 000 m², non « forêt disparue », anneau 15-50 m ≥ 50 % de forêt ancienne, forêt actuelle ≥ 60 % : 250 patches hors Pontcharra → 47 → **9** → eau ≤ 50 m : **2** → jonction ≤ 30 m : **1** (937242, 6484381 = Couvat : pré de 4 494 m², maison à 61 m, déjà rejeté FAQ05-107). Les 8 autres (1,4-2,4 km) sont de petites trouées de 350-1 244 m² dans la forêt ancienne, sans ruisseau cartographié (95-448 m) sauf 938584, 6483797.
5. **Hasard** : décalage aléatoire de la couche forêts anciennes (974 tirages) : 10,0 patches C attendus, observé 9 → P(≥9) = 0,50. Décalage eau+jonctions : 0,49 survivant attendu, observé 1 → P = 0,40. **Niveau du hasard.**
6. **Séries numérotées historiques** : non exploitable. Cadastre napoléonien de Saint-Maximin = 3 feuilles (tableau + sections A/B ; la page source cite aussi « S, T », incohérent), cote AD38 4P4/208 : pas de série ≥ 11 ; plans non géoréférencés/non vectorisés, nombre de sections modernes par commune < 11. Cassini et État-major : pas de numérotation. Aucun test de paire à 1 850 m possible → rien.

## Candidats (tous faibles, non fiables)
| Point (WGS84) | L93 | d tour | Constat | Score |
|---|---|---|---|---|
| 45.42689, 6.05509 | 938845, 6485450 | 1 912 m | trouée allongée (chemin forestier) de 1 044 m² en forêt ancienne à 100 %, jonction à 1 m, maison 225 m, eau 95 m | faible |
| 45.41211, 6.05093 | 938584, 6483797 | 2 433 m | gap 451 m² en forêt ancienne, confluence de ruisseaux à 29 m, maison 539 m, pas de jonction | faible, cap 137° (≠ lever) |
| 45.41783, 6.03408 | 937242, 6484381 | 1 245 m | pré du Couvat, ruisseau à 0 m, jonction 2 m, maison 61 m (rejeté FAQ05-107) | écarté |

## Limites
Hachures de l'État-major (1 m/px) : chemins en forêt illisibles ; vision ≤ 700 px/appel (10/15 appels). Seuil « ouvert 1950 » = texture ortho (accord 64 % avec LiDAR). Plafond 30 000 m² posé après un premier essai à aire libre (patches de 848 000 m² = plaine). Tests de hasard approximatifs (distance centre − rayon équivalent). Bâti/cadastre napoléonien non lu en ligne (pas de navigateur).

## Prochain test recommandé
Reprendre le crible C sans exiger la jonction OSM/BD TOPO (chemins forestiers invisibles) mais avec la ligne de vue depuis la muraille ; ou abandonner l'angle « historique » : la persistance n'est discriminante que si l'auteur a pris une trouée dans forêt ancienne, ce que rien n'impose.
