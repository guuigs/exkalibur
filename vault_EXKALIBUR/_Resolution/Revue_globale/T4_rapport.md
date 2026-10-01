# T4 : « la grande roche » (A) et « 3e / 11e = bois » (B), 30/09/2026

**Verdict.** A : pas de roche identifiée, mais un **lieu-dit cadastral collé à la tour**, « LE CHENE LA ROCHE ET LE VIVIER » (à 15 m de la tour), qui rassemble chêne, roche et vivier (étang). Piste vivante, **HYP de confiance faible à moyenne**, à vérifier au LiDAR ou sur place. B : les parcelles ONF numérotées existent (source trouvée), mais **aucun couple 3→11 à 1,85 km ±1 %** dans la zone. Piste « parcelles ONF » **écartée** pour Saint-Maximin, Pontcharra, Barraux et Moutaret.
Étiquettes : FAIT = mesuré ; HYP = hypothèse ; INT = intuition.

## Tableau de synthèse
| Piste | Candidats | Preuve | Test du hasard | Statut |
|---|---|---|---|---|
| A1 blocs erratiques / roches connus (Wikipedia, BD TOPO) | Rien de documenté à moins de 6 km. BD TOPO : Rochers de Saint-Georges (5,4 km), cascade « la Pierre Tombante » (5,7 km, cap 113°) | aucune | sans objet | **Abandonnée** (OSM indisponible, voir limites) |
| A2 lieux-dits cadastraux Pierre/Roche | **LE CHENE LA ROCHE ET LE VIVIER** (0,13 km, cap 116°, 7,8 ha) ; PIERRE GROS (0,44 km, cap 34°) ; LE ROCHAT (1,42 km S) ; ROCHE MORTE (3,07 km SSW) ; PIRRE GROSSE (5,7 km E) | Le premier contient une retenue BD TOPO de 10 318 m² (centre 45.42844, 6.03290, à 116 m de la tour) et un marais. Mots « chêne » (souche-majesté ?), « roche », « vivier » (étang de l'enluminure 9 ?) | 39 lieux-dits roche/pierre sur 2 476 (20 communes) ; densité 0,079/km². P(≥1 à ≤134 m) = **0,45 %** ; P(≥1 à ≤500 m) = 6 %. Test *a posteriori* (la tour est le centre) | **Vivante, à vérifier** |
| A3 lecture métaphorique | Pierre/Kepha, épée dans le roc, Bayard (Pierre Terrail), Hugues | Lycée **Pierre de Terrail** à 1,39 km (cap 308°), église **Saint-Hugues** à 0,78 km. Aucun lieu-dit roche n'est relié à ces noms | non chiffrable | **Vivante, sans preuve** |
| B1 parcelles forestières ONF numérotées | Forêts publiques de la zone | Voir section B | 244 paires (k, k+8) : 3 en fenêtre par centroïdes (1,2 %), 3 par bords (1,2 %) = bruit | **Écartée** |
| B2 scieries, ponts, clochers en bois, bornes forestières | non testé (scieries et ponts déjà faits par l'orchestrateur) | | | **Non traitée** |

## A. La grande roche
### Contraintes FAQ (FAIT, rappel du brief)
Roche qui bloque le passage le long du ruisseau (FAQ06-195), très difficile à manquer (FAQ03-211), difficile à toucher sans se mouiller (FAQ06-180), invisible depuis la souche (FAQ06-167), non visible sur Maps (FAQ07-126), « toujours à sa place ? » sans réponse (FAQ06-287). Aucune ne se teste avec des données cartographiques.

### Résultats (scripts `T4_A1_roches`, `T4_A3_cadastre`, `T4_A4_pierregros`, `T4_A5_erratiques`, `T4_A6_chene_roche`, chacun avec son `.out.txt`)
- FAIT, BD TOPO : dans `detail_orographique`, seuls les Rochers de Saint-Georges sont à moins de 7 km (5,4 km). Aucun bloc isolé. Wikipedia : aucun article de bloc erratique à moins de 10 km (recherches vides, `T4_A5`).
- FAIT, cadastre (20 communes) : liste des lieux-dits roche/pierre ci-dessus.
- **LE CHENE LA ROCHE ET LE VIVIER** (FAIT) : polygone de 7,78 ha, à **15 m** de la tour (bbox de −49 à +302 m E, de −237 à +124 m N). Il contient une retenue BD TOPO de 10 318 m² (« Intermittent ») et un marais. Plusieurs tronçons d'« écoulement naturel » intermittents passent à 116–290 m. Un lieu-dit « LE CHENE » est à 190 m (cap 302°) et un lieu-dit « AVALON » à 90 m au nord.
- HYP (confiance faible à moyenne) : ce lieu-dit réunit les mots du texte : **roche** (grande roche), **chêne** (souche-majesté ? appellation « très concrète », FAQ05-008), **vivier** (bassin de l'enluminure 9, FAQ07-052). P = 0,45 % pour « roche » seul à ≤134 m, mais le calcul est fait *a posteriori* : à ne pas surestimer. Le nom cadastral est ancien (ce n'est pas une donnée « Maps »), ce qui cadre avec FAQ07-126.
- Points défavorables (FAIT) : une retenue de 1 ha n'est pas un « ruisseau » ; le chemin de rempart n'est pas sur la jonction (FAQ06-025), et la retenue est à 116 m de la tour, sans preuve que la clairière soit là. Cette retenue n'a pas été reclassée avec le score de forme de T1 (non refait ici).
- **PIERRE GROS** (0,44 km NE, versant du Ratier) : aucun ruisseau BD TOPO à moins de 250 m (`T4_A4`). Candidat secondaire.
- Lecture métaphorique (HYP faible) : « Pierre » = Kepha ne désigne aucun lieu de la zone, sauf le lycée Pierre-de-Terrail (un bâtiment, exclu par le cahier des charges). Aucune église Saint-Pierre à moins de 4,7 km.
- Abandons : blocs erratiques (aucune donnée obtenue), lieux-dits à plus de 3 km (le chemin de rempart est à la tour).

## B. Parcelles forestières ONF
### Source (FAIT)
La couche **`PARC_PUBL_FR`** du WFS ONF `http://ws.carmencarto.fr/WFS/105/ONF_Forets` (ressource du jeu « Forêts publiques (diffusion publique) » sur data.gouv.fr) donne les polygones de parcelles, le nom de forêt et le **code de parcelle** (`ccod_prf`). Format : GML 3.1.1, WFS 1.1.0, BBOX lat,lon avec `EPSG:4326` (le JSON est refusé). Le WFS data.geopf.fr n'a aucune couche de parcelles ONF. 505 parcelles récupérées dans ±10 km (`T4_B2_parcelles_all`).

### Codes de parcelles (FAIT)
- **Saint-Maximin : 16 parcelles, lettres A à P** ; Pontcharra A–V ; Moutaret A–J ; Barraux A–N ; Sainte-Marie-du-Mont A–E ; Glapigneux 1–9.
- Forêts à numéros : Chapareillan 1–28, Allevard 1–35, Saint-Hugon 1–8 et 24–51, Boutat 1–46, Le Touvet 1–15, Saint-Pierre-de-Soucy 1–10, Crêt-en-Belledonne, Arvillard…
- Les forêts de la zone sont en lettres. Si « troisième » et « onzième » renvoient à ces parcelles, ce sont C et K (HYP : le texte dit des ordinaux, pas des lettres).

### Distances 3→11 (FAIT, `T4_B3_calcul.py` / `.out.txt`), fenêtre [1831,5 ; 1868,5] m
| Forêt | Parcelles | Centroïdes | Bords | Dans la fenêtre ? |
|---|---|---|---|---|
| Saint-Maximin | C→K | 2 022 m | 1 786 m | non (bords 2,5 % trop courts) |
| Pontcharra | C→K | 1 688 m | 1 458 m | non |
| Barraux | C→K | 1 945 m | 1 570 m | non |
| Moutaret | C→K | pas de parcelle K (A–J) | | sans objet |
| Allevard | 3→11 | 2 072 m | 1 568 m | non |
| Chapareillan | 3→11 | 959 m | 597 m | non |
| Le Touvet | 3→11 | 2 227 m | **1 839 m** | bords : oui, mais parcelles à 12,4 km (une partie) et 9,9 km de la tour, hors zone |
| Glapigneux | 3→11 | pas de 11 (1–9) | | sans objet |

### Test du hasard (FAIT)
244 paires (k, k+8), chiffres et lettres, toutes forêts : 3 en fenêtre par centroïdes (1,2 %) et 3 par bords (1,2 %). Les « hits » : Le Touvet 1→9 (c), 3→11 (bords), 7→15 (c), Allevard 17→25 et 18→26 (c), Haut-Bréda G→15 (bords). Aucun n'est à Saint-Maximin ni dans la zone de la tour.
- Abandon : parcelles ONF comme 3e/11e. Raisons : aucune paire à 1,85 km dans les forêts proches ; le seul hit près du 3→11 (Le Touvet) est à 10–12 km, dans le bruit ; les parcelles de Saint-Maximin sont des lettres. Reste possible : des parcelles d'une forêt non ONF (privée), sans données publiques.
- Non testé : plans d'aménagement PDF.

## Limites
- **Overpass a été indisponible** (504 et timeouts sur 3 miroirs, ~6 essais) : **aucune donnée OSM** sur `natural=stone/boulder/rock`. À refaire avec `T4_A2_osm.py`. `T4_A1_roches.out.txt` date de la première exécution (OSM vide, BD TOPO seule).
- L'INPG n'a pas été consulté. Mission B2 (scieries, ponts en bois, clochers de bois, bornes forestières) non traitée.

## À faire, par priorité
1. Regarder « LE CHENE LA ROCHE ET LE VIVIER » au LiDAR HD et à l'ortho : ruisseau, bloc, chêne, clairière. Comparer la forme de la retenue (10 318 m²) à l'étang de l'enluminure 9 avec `T1_bassin.py`.
2. Relancer `T4_A2_osm.py` quand Overpass répond.
3. Refaire le scan de jonctions/clairières de T1 en se limitant au polygone de 7,8 ha et à 200 m autour.

## Fichiers
`T4_A1_roches`, `T4_A2_osm`, `T4_A3_cadastre`, `T4_A4_pierregros`, `T4_A5_erratiques`, `T4_A6_chene_roche`, `T4_B1_parcelles`, `T4_B2_parcelles_all`, `T4_B3_calcul` (chacun `.py` + `.out.txt`). Données lourdes : `scratch/exk_e12/t4_parc_onf.json`, `t4_cadastre_roches.json`, `wfs_caps.xml`.
