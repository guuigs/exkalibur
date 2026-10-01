# 00 — ÉTAT (à relire EN PREMIER à chaque reprise)

> `GRAPHE_INDICES.md` (fils rouges, entrées → sorties de chaque énigme, filtre d'élimination en 3 questions) est à lire juste après ce fichier.

**Dernière mise à jour :** 01/10/2026 (nettoyage des fichiers).
**Objectif imposé par Guilhem :** une zone de ±50 m avec ≥ 95 % de confiance pour le coffre. Autonomie pour la réflexion ; on ne le sollicite que pour connecter un outil ou lire un détail d'illustration.
**Phase :** énigmes 1 à 11 validées ; **énigme 12 non résolue**.

## Règles de travail (Guilhem)
- Les notes existantes de Guilhem sont en **lecture seule**. Tout le travail va dans `_Resolution/`, sauf `../00 - Solutions validées.md`.
- N'invente jamais le contenu d'une énigme. Aucune action hors vault, web et le dépôt GitHub `guuigs/exkalibur` sans accord. Discord : **lecture seule**.
- Fait / hypothèse / intuition, avec une confiance. « Pas encore trouvé » plutôt qu'une zone séduisante. Une zone ne s'annonce qu'avec un décompte et un contrôle indépendant.
- Mode « shark » : validation officielle (auteur, FAQ) = on prend ; rumeurs et Discord = pistes seulement.
- Sous-agents sur Sonnet 5.5 en priorité, bascule sur DeepSeek à 90 % d'usage (skill `subagent-model-guard`).
- À chaque énigme validée : mettre à jour le récapitulatif, le KML (+ `gen_svg.py`), `GRAPHE_INDICES.md`, ce fichier et `Journal.md`.

## Tableau de bord
| # | Titre | Statut | Solution |
|---|---|---|---|
| 1 | In principio | ✅ | Épée : garde León → Foix, lame Lombrives → Urquhart, pommeau Valence |
| 2 | Terra incognita | ✅ | TROIANOVA = Londres, Tour de Londres |
| 3 | Ecce Homo | ✅ | TI + LG + carré SATOR = Tintagel |
| 4 | Rex dei gratia | ✅ | Tintagel → Silchester → Westminster |
| 5 | Lux in tenebris | ✅ | Stonehenge + Carnac |
| 6 | Libera nos a malo | ✅ | 4 C (340,9 km) ; Tour → Battle → Sainte-Chapelle |
| 7 | Sub rosa | ✅ | Garde Sainte-Chapelle → Rennes → Brocéliande → Lorient |
| 8 | Ultima cena | ✅ | 666² pieds romains → Payns |
| 9 | Noli me tangere | ✅ | Croisée garde É7 × royaume É5 → 340,9 km → Chartres |
| 10 | Omnia vincit amor | ✅ | Eilean Donan → Machrie Moor, 193,1 km |
| 11 | Consummatum est | ✅ (angle 64,99° non expliqué) | Saint-Palais → château Bayard (D × π, ≈ 50 m de Bayard) |
| 12 | Ad vitam aeternam | 🔴 | départ probable tour d'Avalon / Rue du Rempart (Saint-Maximin, Isère) ; 3e et 11e non identifiés |

## Énigme 12 : où en est-on
Tout est dans **`Enigme_12/solution.md`** (faits, règles de la FAQ, pistes vivantes, pistes abandonnées, prochaines actions). En une ligne : le départ est probable, le reste est ouvert, aucune zone n'est défendable.

## Numérotation des enluminures
L'auteur les numérote dans l'ordre de lecture (R1G=1, R1D=2, R2G=3, R2D=4, R3G=5, R3D=6, R4G=7, R4D=8, R5G=9, R5D=10, R6G=11, R6D=12). Énigme N ≠ toujours enluminure N (FAQ02-096). Voir `03_Correspondance_illustrations.md`.

## Fichiers
- `GRAPHE_INDICES.md` ; `01_Contexte.md`, `02_Audit.md`, `03_Correspondance_illustrations.md`, `Pistes_transverses.md`, `Journal.md`.
- `Enigme_NN/` : un dossier par énigme ; `Enigme_12/solution.md` et `illustration_e12.md`.
- `Revue_globale/` : scripts, sorties et données de l'É12 (voir son `README.md`) ; `FAQ_E12_complet.md`.
- `Communaute/` : FAQ officielle de l'auteur (`faq_officielle_auteur.json`, 1 852 Q/R), transcription FAQ8, lectures Discord (propos de tiers).
- `Sources/` : photos HD du 29/09 (`photos_HD_2026-09-29/INDEX.md`) ; `Carte/` : carte officielle et KML.
- `_archive_brut_2026-10-01.zip` : notes de travail, briefs et rapports de sous-agents d'avant le nettoyage.
