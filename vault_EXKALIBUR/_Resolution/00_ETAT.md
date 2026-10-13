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

**Reprise à zéro du 13/10/2026 → `Enigme_12/Reprise_2026-10-13/README.md`.** « Dieu sut se montrer favorable » est un vers du *Roman de la Rose* (trad. Marteau, Gutenberg 16816, chap. XI). L'É7 cite le chap. XIII du même livre. Hypothèse forte : 3e/11e = chap. III (porte du verger) et XI (fontaine de Narcisse sous le pin). Pas encore de pile-poil. ⚠️ Le dépôt GitHub est public.

**Suite du 13/10 (plan d'attaque)** : narrateur = Bayard (hypothèse forte) → jour dernier 10/05 grégorien ; épée = boussole (pommeau N-E-S-O) ; meilleur candidat clairière = **Muraillat / La Planta (45.43360, 6.04491)**, visible depuis la tour, cap 66° = premier rayon du 10 mai, ruisseau à gauche → ravin rocheux. À vérifier sur place. Détails : `Enigme_12/Reprise_2026-10-13/README.md` § « Suite ».

**Suite du 13/10 (3e/11e par le lore, § H du même README)** : les chapitres III/XI du *Roman de la Rose* sont rétrogradés (la porte du chap. III est en bois, alors que le 3e ne donne pas d'écharde, FAQ07-068). Lecture qui passe tous les filtres de la FAQ : **3e = *Ecce Homo* (le Pavé de pierre, au départ), 11e = *Consummatum est* (la croix en bois)**, avec les stations du chemin de croix comme « étapes intermédiaires ». Les travaux d'Hercule (biche = enl. 3, dragon des Hespérides = enl. 11) restent la meilleure lecture des enluminures. Conséquence : l'endroit final serait à 1 850 m ± 1 % de la tour. Muraillat (1 212 m) n'est plus expliquée ; seul candidat visible sur l'anneau : **Le Couvat (1 864 m, cap 77°)**, sans preuve.

**Visibilité réelle (§ I du README, 13/10 soir)** : le point « tour » était décalé de 27 m. Le vrai donjon est en **45.428888, 6.031015** (BD TOPO, 34,5 m). Avec le MNS LiDAR HD (arbres compris), **Muraillat, Le Couvat, la Burge et le Bréda ne sont pas visibles** depuis le sommet. Sur l'anneau à ±1 % côté est, seul le pré A (cap 84°, 1 857 m, sous la ligne HT) l'est. Avec le relief seul, Le Couvat (1 847-1 855 m, cap 75-76°) redevient visible. Zone à vérifier sur place : Le Couvat – pré A – ravin du Tapon. Rien n'est démontré.

**Livres des saints (relevé de Guilhem, § K du README)** : les numéros (1, 2, 3, 6, VIII = 4×II, X) suivent le **calendrier liturgique traditionnel des fêtes d'apôtres** (Matthias 1, Jacques le Mineur 2, Philippe 3, Barthélemy 6, Jude 8 = l'ermite à la lance, André 10 ; 6 livres sur 6, ex-aequo par ordre alphabétique ; le « I » de la Cène (R6D) relèverait de l'autre ordre, celui du « numéro un » d'*Ultima cena*) ; les scènes collent à la saison (neige en février, soleil en août, nuit au solstice). Hypothèse forte : **3e = Philippe et Jacques (1er mai, lendemain de la mort de Bayard), 11e = Thomas (21 décembre, non peint)**. Le mécanisme des « dix stades » reste à trouver.

**Piste de lore (§ L du README)** : le texte de l'É12 suit la fin de l'Apocalypse, la Jérusalem céleste (alpha et oméga, « la gloire de Dieu l'éclaire », fleuve et arbre de vie, muraille aux 12 fondements portant les noms des 12 apôtres, ville mesurée en stades, arc-en-ciel d'émeraude de l'enl. 9). Les 3e/11e seraient donc des fondements, c'est-à-dire des apôtres. Essais géométriques sur les dates (crêtes, levers, triangle à 60°) négatifs.

**Gabarit Jérusalem céleste (§ M du README, piste la plus solide à ce jour)** : ville carrée orientée, portes dans l'ordre d'Ap 21,13 (orient, nord, midi, occident), aux quarts des côtés ; départ = 11e porte = le donjon ; 3e porte à 1 850 m, **cap 75,96° → à 10 m de la jonction du bout de la route du Couvat** (45.43288, 6.05406). Une seule des 8 variantes touche ; hasard ≈ 5-15 %. Ruisseau de Tapon à 130 m, maisons à 60-80 m. À vérifier : ruisseau à senestre, grande roche, cadastre.

## Numérotation des enluminures
L'auteur les numérote dans l'ordre de lecture (R1G=1, R1D=2, R2G=3, R2D=4, R3G=5, R3D=6, R4G=7, R4D=8, R5G=9, R5D=10, R6G=11, R6D=12). Énigme N ≠ toujours enluminure N (FAQ02-096). Voir `03_Correspondance_illustrations.md`.

## Fichiers
- `GRAPHE_INDICES.md` ; `01_Contexte.md`, `02_Audit.md`, `03_Correspondance_illustrations.md`, `Pistes_transverses.md`, `Journal.md`.
- `Enigme_NN/` : un dossier par énigme ; `Enigme_12/solution.md` et `illustration_e12.md`.
- `Revue_globale/` : scripts, sorties et données de l'É12 (voir son `README.md`) ; `FAQ_E12_complet.md`.
- `Communaute/` : FAQ officielle de l'auteur (`faq_officielle_auteur.json`, 1 852 Q/R), transcription FAQ8, lectures Discord (propos de tiers).
- `Sources/` : photos HD du 29/09 (`photos_HD_2026-09-29/INDEX.md`) ; `Carte/` : carte officielle et KML.
- `_archive_brut_2026-10-01.zip` : notes de travail, briefs et rapports de sous-agents d'avant le nettoyage.
