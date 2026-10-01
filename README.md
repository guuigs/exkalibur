# Exkalibur — dossier de résolution (Guilhem)

Chasse au trésor *Exkalibur* (Puy du Fou / Unsolved Hunts, auteur Étienne Picand) : 12 énigmes, 12 enluminures, une carte. État au 01/10/2026 : **énigmes 1 à 11 résolues, énigme 12 (*Ad vitam aeternam*) non résolue** (départ probable : Rue du Rempart / tour d'Avalon, Saint-Maximin, Isère ; les 3ᵉ et 11ᵉ ne sont pas identifiés).

| Dossier | Contenu |
|---|---|
| `vault_EXKALIBUR/` | Le vault Obsidian du projet : notes de Guilhem (lecture seule) et `_Resolution/` (relevés, calculs, solutions, revue globale, FAQ de l'auteur, carte KML/SVG, photos HD). Commencer par `00 - Solutions validées.md`, puis `_Resolution/Enigme_12/solution.md` et `PLAN_ACTION.md`. |
| `skills/` | Skills Hermes liés au projet : `puzzle-hunt-solving` (méthode, pièges, recettes) et `grounded-citations`. |
| `outils_scratch/` | Helpers Python (`exk.py`), transcription de la FAQ 8, script de recherche Discord en lecture seule. |
| `images_travail/` | Recadrages et schémas de l'enluminure 11, de la rose des vents, du livre, de la rayure de l'épée. |
| `donnees_travail/` | Petits jeux de données de terrain (réseau pédestre, cours d'eau, croisements, roches). |

## Ce qui n'est PAS dans ce dépôt
- Les messages du Discord officiel (propos de tiers, serveur réservé aux acheteurs) : les fichiers `Communaute/discord_*` et `veille_*` sont exclus.
- Les gros fichiers de calcul (MNT LiDAR `.npy`, GeoJSON BD TOPO) : ils se régénèrent depuis les scripts (`T12C_*`, `O_lidar_*`) et les services IGN (data.geopf.fr).
- Aucun identifiant, jeton ni mot de passe (balayage de motifs avant publication : aucun trouvé).

## Règles du projet
Les notes originales de Guilhem sont en lecture seule ; tout le travail va dans `_Resolution/`. On sépare fait / hypothèse / intuition ; on préfère « pas encore trouvé » à une solution séduisante ; chaque calcul est un script archivé, comparé à un témoin aléatoire.
