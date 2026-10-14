# R0710_L4 — Nature de la bande non cadastrée du point L4 (45.424709, 6.041016)

**Date** : 07/10/2026 · **Sous-agent** L4-EMPRISE · **État : complet sur la question posée, partiel sur le cadastre de 1838**
**Verdict (résumé)** : **la bande non cadastrée de L4 n'est pas une emprise de chemin public** → **l'atout « domaine public » de la variante L4 tombe**. La bande est un **corridor de cours d'eau (ravin encaissé)** ; l'eau la plus proche est bien le **Rebouchet cartographié** (intermittent) à 14,7 m. Verdict global sur la variante L4 : **PISTE FAIBLE** (elle perd son seul avantage). Le **contrôle sur L6** (le point retenu par MB) est positif : là, la bande non cadastrée est bien un chemin.

---

## 1. La question et la réponse courte

**Question** : la bande non cadastrée de 4 m (dans les bois, 0,3 m d'une limite de parcelle) est-elle une **emprise de chemin communal (domaine public)** ou le **lit d'un ruisseau non domanial (privé des riverains)** ?

**Réponse** : **cours d'eau / fond de ravin, pas chemin.** Aucun chemin n'est cartographié sur la bande par **trois sources indépendantes** (BD TOPO, OSM, Plan IGN) ; le chemin le plus proche est à **30 m**. La bande suit en revanche le **talweg d'un ravin encaissé** (jusqu'à −18 m sous le LiDAR HD officiel) et **longe le Ruisseau de Rebouchet cartographié** (intermittent) à 14,7 m. Un lit de cours d'eau non domanial appartient aux riverains : **L4 n'est pas sur le domaine public**.

---

## 2. Faits géométriques (bande extraite)

Méthode : rasterisation des parcelles Etalab/DGFiP (Saint-Maximin 38426 + voisines), buffer 0,75 m pour éliminer les faux trous de joint, composante connexe contenant L4. Polygone exporté.

| Mesure | Valeur |
|---|---|
| Surface de la composante (fenêtre 500 m) | **7 087 m²** |
| Largeur (2×EDT) | médiane **2,0 m**, p75 2,8 m, p90 4,0 m, **max 4,5 m** (10 m à un nœud) |
| Étendue | x[937 555, 937 954], y[648 4966, 648 5340] → **~400 × 375 m** |
| Orientation (PCA) | **138,5°** (NNW–SSE), allongement 4,6 |
| Continuité | **≥ 300 m continue**, un seul tenant de z 512 m (S) à 405 m (N) : **descente monotone, 107 m de dénivelé sur 400 m** |
| Distance au chemin BD TOPO | **médiane 16,7 m**, min 0,7 m, 12,3 % ≤ 6 m |
| Distance à l'eau cartographiée | médiane 10,4 m, **35 % ≤ 6 m**, 49 % ≤ 10 m |
| Extrémité aval | 45,42634 / 6,03855, z 405,9 : la bande **fusionne avec l'eau et un chemin** à la sortie du vallon |
| Cadastre au point | **non cadastré**, parcelle privée B0547 à **0,1 m** ; BD TOPO : chemin 30,2 m, sentier 32,1 m ; Rebouchet 14,7 m |

Un corridor de 2–4 m qui **descend en pente régulière sur 400 m** et **rejoint le réseau hydrographique** est une signature de thalweg, pas de chemin (un chemin suit des courbes de niveau ou des lacets).

---

## 3. Topographie : L4 est au fond d'un ravin (et le LiDAR du projet est juste)

- LiDAR du projet (`r0610_j16est/mnt.npy`) : L4 = **448,0 m** ; à ±10 m, 454–456 m ; à ±20 m, 463–465 m ; à ±40 m, 471–476 m. **LRM = −2,46** (−3,45 à +5 m) : gouttière profonde.
- **Contrôle indépendant (fait décisif)** : l'API d'altimétrie IGN `ign_rge_alti_wld` donne **466,8 m** à L4 (écart −18,9 m) → discordance apparente. J'ai donc téléchargé le **MNT LiDAR HD officiel de l'IGN** (`IGNF_LIDAR-HD_MNT_ELEVATION.ELEVATIONGRIDCOVERAGE`, WMS float32, L93) : **L4 = 447,93 m** — identique au mosaic du projet (448,0). Idem au Mouret (517,6 vs 517,8) et à roche C (466,1 vs 465,9).
  → **La mosaïque MNT du projet est exacte** ; c'est **RGE ALTI** (produit lissé) qui ne voit pas le ravin.
- **Ombrage du MNT LiDAR HD officiel** (fenêtre 520 m) : un **ravin mural, méandriforme et très encaissé** traverse l'image et passe à L4. Il n'apparaît pas sur l'ombrage **MNS** (le couvert forestier « bouche » le V) — cohérent avec un ravin réel sous forêt (MNH = 10,8 m d'arbres à L4).
- Conséquence : le « talweg » sous L4 est **réel**, mais le **tracé BD TOPO du Rebouchet** passe ~10–15 m à l'ouest et **~12 m plus haut** (z ≈ 460) → **BD TOPO place mal la ligne ici** (cours d'eau intermittent sous couvert).

---

## 4. Hydrographie à toutes les échelles

| Source | Ce qu'elle montre à L4 |
|---|---|
| **BD TOPO V3** (troncon_hydrographique) | **« Ruisseau de Rebouchet », nature = Écoulement naturel, persistance = Intermittent**, d = **14,7 m**. Aucun autre tronçon ≤ 60 m. |
| **BD TOPO** (troncon_de_route) | Chemin (import. 5) **30,2 m** ; Sentier 32,1 m ; Chemin 42,3 m. Rien sur la bande. |
| **Plan IGN v2** (carte actuelle) | Rebouchet en **pointillé bleu** (intermittent) passant à ~25 m à l'ouest ; **aucun chemin ni canal** au point ; ligne droite = pénstocks EDF *enterrés*, à ~135 m à l'est. |
| **OSM (Overpass)** | Aucun `waterway` ni chemin ≤ 350 m de L4. Le « Ruisseau du Rebouchet » OSM est un autre segment, à ~800 m. Autour : aménagement **hydroélectrique EDF** (conduite forcée `usage=penstock` enterrée, `surge_tank` à 45,4266/6,0412, galerie `usage=headrace`) ; ligne **400 kV RTE** (pylône A2 à 194 m). |
| **Orthophoto HR (20 cm, data.geopf.fr)** | Forêt dense à L4 (aucune trouée, aucune trace linéaire de chemin) ; lisière de pré à l'ouest ; **ligne THT** en trouée au SE. |
| **Carte de l'État-Major (~1830-1860)** | Un **cours d'eau bleu méandriforme** traverse la zone du point ; pas de chemin marqué au point. |
| **Scan 50 1950** | Forêt + cours d'eau ; trop grossier (1:50 000) pour trancher au mètre. |
| ⚠️ Scan 25 (1:25 000) | **Non disponible** sur data.geopf.fr (couche `GEOGRAPHICALGRIDSYSTEMS.MAPS.SCAN25TOUR` absente des capacités WMS/WMTS). Remplacée par État-Major + MNT LiDAR HD + ortho + Plan IGN. |

**Réponse à la sous-question** : « le Rebouchet est-il cartographié à moins de 10 m de roche C ? » → **OUI** : BD TOPO donne **6,2 m** de roche C. « L'eau la plus proche est-elle le talweg non cartographié du sud (45,4202, 6.0423) ? » → **NON** : au point sud (L6-roche, 45,420245, 6.042310) la distance à l'eau cartographiée est **255 m** — ce talweg sud n'a **aucune eau cartographiée**. **Le cours d'eau qu'on voit sur les cartes, et le seul, est le Rebouchet.**

---

## 5. Cadastre napoléonien 1838 (Archives de l'Isère) — obtenu, non géoréférencé au mètre

- Recherche résolue via l'API interne du portail : `_recherche-api/moteur?refUnique=arko_default_64ba4c7674c97` → **3 fiches pour Saint-Maximin** : **cote 4P4/208**, *Tableau d'assemblage*, *Section A*, *Section B* (fichiers image 7020/7021/7022).
- **Images téléchargées en pleine résolution (8000 px)** : `images_travail/cadnap_38426/ad_sm_TA_8k.jpg`, `ad_sm_A_8k.jpg`, `ad_sm_B_8k.jpg` (+ versions 2000 px).
- Ce qu'on y lit : le tableau d'assemblage porte les sections **A** (nord) et **B**, avec les hameaux **« Repidon »**, **« les Mourets Bau… »**, **« St Maximin »**, et un **réseau hydrographique dense tracé en bleu-vert** ; la **section B** montre « Repidon [Hameau] », « les Mourets », « la Combe », « Et Chaudan », « St Martin », de nombreux **ruisseaux (traits ondulés)** et des chemins en double trait.
- **Limite** : les registres (états de sections / matrices) **ne sont pas en ligne** (« toujours consultables en salle de lecture ») ; et il n'existe **aucun cadastre napoléonien géoréférencé** en ligne pour l'Isère (ni sur geopf, ni ailleurs). La localisation au mètre sur le plan 1838 demanderait un géoréférencement manuel (2-3 amers) que je n'ai pas terminé → **je ne conclus rien de précis du plan 1838** ; ce que j'en vois ne montre **aucun chemin** sur la zone, mais un cours d'eau.

---

## 6. Le test décisif : L4 vs L6 (même méthode, deux bandes non cadastrées)

| | **L4** (45.424709, 6.041016) | **L6** (45.420330, 6.042540 — coffre retenu par MB) |
|---|---|---|
| Cadastre | non cadastré | non cadastré |
| Distance au chemin cartographié | **30,2 m** | **0,3 m** (sur le chemin) |
| Distance à l'eau cartographiée | 14,7 m | **235 m** (aucune) |
| Coupe ±15 m | **V : 448 m au fond, 457–462 m sur les flancs** ; arbres (MNH 6–11 m) | **plat : 676–678 m partout** ; **MNH = 0** (nu, non boisé) |
| Pente au point | 5,9° (fond de ravin) | 8,2° |
| Nature | **corridor de cours d'eau / ravin** | **emprise de chemin** ✅ |

→ La même méthode classe **L6 = chemin (public)** et **L4 = cours d'eau (privé riverain)**. Le point L6 de MB **résiste** ; le point L4 **tombe**.

---

## 7. Réponse aux trois questions posées

1. **La bande est-elle une emprise de chemin communal (domaine public) ?** → **NON.** Aucun chemin (BD TOPO, OSM, Plan IGN, État-Major) sur la bande ; chemin le plus proche à 30 m ; la bande suit un thalweg encaissé et longe le Rebouchet. Elle correspond au **corridor d'un cours d'eau non domanial** → **privé des riverains**.
2. **Le ruisseau suivi est-il celui qu'on voit sur les cartes ?** → **OUI.** Le cours d'eau cartographié est le **Ruisseau de Rebouchet** (BD TOPO, *intermittent*), présent aussi sur le Plan IGN et l'État-Major, à **14,7 m** de L4 et **6,2 m** de roche C. Le « talweg du sud » (45,4202 / 6,0423) n'a **aucune eau cartographiée** (255 m).
3. **Le point 45.424709, 6.041016 est-il sur le domaine public ?** → **NON** (pas d'emprise publique identifiée sur la bande ; le « non cadastré = public » de `R0710_MB` §1 est ici **faux** — MB l'avait d'ailleurs écrit pour le lit du ruisseau, sans l'appliquer à L4).

---

## 8. Faiblesses et incertitudes (honnêtes)

1. **La bande est un réseau**, pas un ruban unique : la composante connexe réunit plusieurs tronçons (lit, berges, chemin) qui se touchent ; à L4 précisément, la largeur locale est de 2–4,5 m et la position est à 15 m du tracé BD TOPO du Rebouchet → l'identification « c'est le **lit** du Rebouchet » est **probable (≈65 %)** mais **non prouvée** : ce pourrait être une **berge**, un **fossé** ou un **ancien béal**.
2. **BD TOPO place mal le Rebouchet ici** (~10-15 m à l'ouest, ~12 m plus haut que le thalweg LiDAR) : la carte « officielle » de l'eau est donc approximative dans le bois — la coïncidence bande/eau est moins nette qu'annoncé.
3. **Cadastre 1838 non géoréférencé** : pas de preuve documentaire directe de la nature du linéaire en 1838.
4. **Pas de terrain** (règle de Guilhem) : ni largeur réelle, ni présence d'eau au sol.
5. `RGE ALTI` (API) ne voit pas le ravin — **piège à éviter** : toute vérification d'altitude par cette API dans ce secteur est fausse de ~19 m.

---

## 9. Fichiers

**Rapport** : `vault_EXKALIBUR/_Resolution/Enigme_12/R0710_L4_emprise.md`
**Scripts** (`outils_scratch/`) : `r0710_L4_recon.py`, `r0710_L4_recon2.py`, `r0710_L4_bande.py`, `r0710_L4_bande2.py` (bande + coupes), `r0710_L4_trace.py` (suivi 400 m + profil du Rebouchet), `r0710_L4_coupe.py` (coupe classe+z), `r0710_L4_check_L6.py` (contrôle L6), `r0710_L4_export.py` (polygone), `r0710_L4_cartes.py`, `r0710_L4_cartes2.py`, `diag_alti.py`, `diag_alti2.py` (contrôle d'altitude), `fetch_isere.py`, `ad_img.py`, `ad_crop.py`, `probe_ad.py`.
**Données** (`donnees_travail/r0710_L4/`) : `bande_L4.geojson` (polygone de la bande, 7 087 m²), `bande_L4.npy`, `grid.json`.
**Cartes** (`images_travail/`) : `r0710_L4_ortho_800.jpg`, `r0710_L4_ortho_120.jpg`, `r0710_L4_ortho_rocheC_60.jpg`, `r0710_L4_ortho_rocheC_250.jpg`, `r0710_L4_cad_800.png`, `r0710_L4_cad_200.png`, `r0710_L4_planign.png`, `r0710_L4_lidarHD_hillshade_520m.png`, `r0710_L4_lidarHD_hillshade_500m.png`, `r0710_L4_lidarHD_hillshade_3km.png`, `r0710_L4_lidarHD_MNS_520m.png`, `r0710_L4_etatmajeur_1km.jpg`, `r0710_L4_em40_300.jpg`, `r0710_L4_scan50_600.jpg`, `r0710_L4_scan50_300.jpg`, `r0710_L4_cadnap_tableau_zoom.jpg`, `r0710_L4_cadnap_B_repido.jpg`, dossier `cadnap_38426/` (plans AD 1838, 8 000 px).

---

## 10. Ce qu'il faut tester ensuite

1. **Appliquer le test L4/L6 aux autres bandes non cadastrées** de la zone finale (49 % du non cadastré de MB est à ≤10 m de l'eau) : combien des « emprises publiques » de MB sont en réalité des **lits de ruisseau** ? Le critère « non cadastré = public » doit être **retiré** partout où la bande n'est pas plate, non boisée et alignée sur un chemin cartographié.
2. **L6 : sécuriser la preuve de domanialité** (le point est bon sur la forme) — vérifier que le chemin est bien un **chemin rural communal** (délibération/plan de voirie, DGFiP groupe 4) et non une simple servitude.
3. **Géoréférencer le plan 1838 4P4/208 section B** (3 amers : Repidon, les Mourets, sortie du vallon) — seul moyen de trancher lit/chemin en 1838 ; les états de sections sont en salle de lecture aux AD 38.
4. **Ne pas réutiliser `RGE ALTI`** pour valider une altitude dans ce secteur (erreur localisée de ~19 m) ; utiliser le MNT LiDAR HD officiel.
