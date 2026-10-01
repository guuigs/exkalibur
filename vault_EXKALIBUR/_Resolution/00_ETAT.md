# 00 — ÉTAT (à relire EN PREMIER à chaque reprise)

> **Méthode depuis le 30/09** : `GRAPHE_INDICES.md` (fils rouges, entrées → sorties de chaque énigme, filtre d'élimination en 3 questions, pistes écartées). À lire juste après ce fichier.

**Dernière mise à jour :** 29/09/2026 21:05
**Phase :** 1 en cours. **Énigmes 1 à 5 : ACQUISES** (décision de Guilhem, 29/09, sans revalidation).
**Décisions de Guilhem** :
- (29/09) Communauté consultable, en hypothèses uniquement. Pas de carte au trésor pour l'instant : on avance sans. Attendre sa confirmation après chaque énigme validée.
- (29/09, soir) **Mode « shark agressif »** : si une résolution est **validée officiellement** (auteur, FAQ, organisateur), on la prend et on passe à la suite. Les **rumeurs de validation** sont gardées en mémoire comme **pistes d'approche**, jamais comme des faits.
- (29/09) Subagents sur **Sonnet 5.5** en priorité ; bascule automatique sur DeepSeek à 90 % d'usage Claude (skill `subagent-model-guard`, cron toutes les 15 min).

**En cours** : É6 validée le 30/09 (Discord + calcul). **Accès Discord complet** (84 salons, dont un par énigme) : mode shark sur les énigmes 7 à 12. Ancien : Énigme 6. **Orchestration par sous-équipe** (Guilhem, 29/09 : plusieurs sous-agents par énigme, en surveillant l'usage Claude). Brief commun : `Enigme_06/BRIEF_sous_agents.md`. Lot deleg_c5ddcd99 : T1 Pater/lecture du plateau, T2 iconographie HD, T3 histoire (Urbain II, Templiers), T4 lieu très Sainte et géométrie, T5 rumeurs et FAQ transverse des C.
Solveur A : PAS TROUVÉ (photo basse définition). Solveur B interrompu : l'alignement Tour–Battle–Sainte-Chapelle n'est pas discriminant, et la contrainte de distance seule ne tranche pas.
**Si la session a été coupée** : lire `Enigme_06/REPRISE.md` (procédure de relance agent par agent).
**Prochaine action** : synthèse T1-T5 → solution candidate → vérificateur (contexte vierge).

## Tableau de bord
| # | Titre | Panneau | Statut | Solution | Prochaine action |
|---|---|---|---|---|---|
| 1 | In principio | R1G | ✅ ACQUISE (Guilhem) | Épée León–Foix–Valence–Urquhart (carte de Guilhem) | — |
| 2 | Terra incognita | R1D | ✅ ACQUISE | Londres / Tour de Londres | — |
| 3 | Ecce Homo | R2G | ✅ ACQUISE | Tintagel | — |
| 4 | Rex dei gratia | R2D | ✅ ACQUISE | Tintagel → Silchester → Westminster | — |
| 5 | Lux in tenebris | R3G ou R5D (?) | ✅ ACQUISE | Stonehenge + Carnac (Ménec) | — |
| 6 | Libera nos a malo | R4G (= enluminure 7) | ✅ VALIDÉE (shark) | 4 C = Clairvaux → Cîteaux → Cluny → Clermont (340,9 km) ; Tour → Battle → **Sainte-Chapelle** | — |
| 7 | Sub rosa | R3D (= enluminure 6) | 🟡 PROBABLE forte | Nouvelle garde **Sainte-Chapelle → Rennes → Brocéliande → Lorient** (Lorient à 0,04 km ; hasard 0,25 %) | Confirmation de Guilhem |
| 8 à 12 | — | — | ⚪ non commencées | — | — |

⚠️ **Numérotation des enluminures** : l'auteur les numérote dans l'ordre de lecture (R1G=1, R1D=2, R2G=3, R2D=4, R3G=5, R3D=6, R4G=7, R4D=8, R5G=9, R5D=10, R6G=11, R6D=12). Énigme N ≠ toujours enluminure N (FAQ02-096). La FAQ lie *Sub rosa* (É7) à la balance et aux 2 juments (enl. 6 = R3D, FAQ06-123), et *Libera nos a malo* (É6) au plateau de jeu (enl. 7 = R4G). Pour É5, l'appariement R5D de mon document 03 reste une hypothèse : la FAQ classe la nappe/table/barque (R3G) en « enluminure 5 ». Sans impact sur la solution acquise.

## Bloquants
1. ~~Carte au trésor~~ : **reçue** (photo IMG_4333), relevé dans `Carte/carte_officielle.md`. Photo à main levée : pas assez précise pour mesurer.
2. Photos HD reçues (27, `Sources/photos_HD_2026-09-29/INDEX.md`). Il manque toujours un gros plan du plateau R4G : IMG_4334 reste la meilleure source.

## Fichiers
- 01_Contexte.md · 02_Audit.md · 03_Correspondance_illustrations.md (⚠️ É5 corrigée ci-dessus)
- Communaute/ : veille + **FAQ officielle complète de l'auteur** (`faq_officielle_auteur.json`, 1 852 Q/R) + scripts d'extraction
- Journal.md · Pistes_transverses.md · Sources/ · Carte/


**30/09 : É8 Ultima cena 🟡 probable (Payns / Hugues de Payns), en attente de confirmation de Guilhem.**

**30/09 : É8 ✅ validée par Guilhem. É9 Noli me tangere en cours. Consigne : sur les dernières énigmes, le Discord relève surtout de la supposition, ne rien prendre pour acquis.**

**30/09 : É9 🟡 lieu probable (Chartres), 1er paragraphe ouvert, en attente de Guilhem.**

**30/09 : É9 ✅ (Chartres). É10 Omnia vincit amor en cours.**

**30/09 : É10 🟡 (Eilean Donan → Machrie Moor, 193,1 km), en attente de Guilhem.**

**30/09 : É10 ✅ (Guilhem). É11 🟡 (Saint-Palais → château Bayard, D·π), angle ouvert.**

**30/09 : É11 ✅ (Guilhem, angle ouvert). É12 🔴 : départ probable tour d'Avalon ; 3e/11e + terrain non résolus. Fin de la phase « de chez soi ».**

**30/09 : revue globale terminée → Revue_globale/00_SYNTHESE.md. Suite possible : LiDAR HD / orthophoto autour de la tour, préparation terrain.**
