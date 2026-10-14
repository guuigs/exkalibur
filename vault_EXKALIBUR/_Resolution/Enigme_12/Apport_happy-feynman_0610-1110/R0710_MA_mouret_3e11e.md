# R0710_MA — Consolider les 3e et 11e : la « table des apôtres » et le Mouret

**Date** : 07/10/2026 · **Sous-agent** MA (mission MOURET-A) · **État : partiel** (identité 3e/11e consolidée ; chaîne finale toujours ouverte)
**Scripts** : `outils_scratch/r0710_MA_mouret_3e11e.py` (géodésie + géométrie), `r0710_MA_hasard.py`, `r0710_MA_part3.py`, `r0710_MA_part4.py`, `r0710_MA_part5.py`
**Données** : `donnees_travail/t16_jonctions_attributs.json` (1 985 jonctions : `vis`, `d_wat`, `d_chan`, `d_bld`, `d`, `cap`) ; FAQ `Communaute/faq_officielle_auteur.json` + `outils_scratch/faq8.txt`.
**Verdict** : **PISTE FAIBLE** (identité 3e/11e = la plus cohérente trouvée à ce jour ; point final au Mouret = **RIEN** — le déroulé roche→coffre échoue, cf. `R0710_M1_mouret_variantes.md`).

---

## 0. Phrase de synthèse (demandée)

> **3e = Jacques le Majeur** (liste de **Mt 10** ; *Jean* si l'on prend **Mc 3**), place n° 3 de la table de la Cène posée au pied de la tour d'Avalon → **45.43802, 6.03463** (cap vrai 16,4°, 1 068 m de la tour, champ ouvert, bâti le plus proche 222 m) ;
> **11e = Simon le Zélote** — le vieillard **à la scie** de l'enluminure 12 (FAQ06-238) — place n° 11 → **45.42184, 6.04019** (cap 136,4°, 1 068 m), **à 8 m de la source BD TOPO (45.42177, 6.04019)** et **66 m du carrefour du Mouret** (45.42243, 6.04030) ;
> **parce que** (a) la corde 3→11 = **1 850 m** impose un cercle de **rayon 1 068 m** centré sur le rempart (= point de départ, FAQ06-193/07-120) ; (b) l'orientation de la table par **l'aube de Pâques vue du rempart** (91,4° en 1524) est la **seule fenêtre de 360°** qui met la 11e à ≤ 100 m d'une jonction de chemins visible avec eau (P = **1,03 %**) ; (c) la 11e = **destination finale** (FAQ03-293) et l'écharde possible sur le 11e (bois de la scie de Simon) y colle (FAQ07-068).

---

## 1. Les listes canoniques : qui est 3e, qui est 11e, et l'écharde

Contrainte dure : **pas d'écharde sur la 3e, écharde possible sur la 11e** (FAQ07-068) + **on marche surtout sur l'une des deux** (06-247). L'attribut de martyr « en bois » d'un apôtre est le seul test objectif dont on dispose.

| Liste | 3e | 11e | 11e en bois ? | 3e sans bois ? | Verdict écharde |
|---|---|---|---|---|---|
| **Mt 10,2-4** (TOB) | **Jacques le Majeur** | **Simon le Zélote** | oui (scie) | oui (bâton, coquille) | ✅✅ **compatible** |
| **Mc 3,16-19** | **Jean** | **Simon le Zélote** | oui (scie) | oui (aigle, coupe) | ✅✅ **compatible** |
| Lc 6,14-16 | Jacques | Jude (Thaddée) | ambigu (massue) | oui | ⚠️ |
| Ac 1,13 | Jacques | Jude (Thaddée) | ambigu (massue) | oui | ⚠️ |
| **Canon romain** (Communicantes) | **André** (si Paul compté) / Jacques (sinon) | Simon / Thaddée | — | **non : croix en X = bois** | ❌ (écharde sur la 3e) |
| **Rangée de Léonard** (13 figures) | **André** | **Matthieu** (ou Thaddée) | — | **non : André, croix en X = bois** | ❌ (écharde sur la 3e) |
| Ordre liturgique (calendrier) | — | — | — | — | ✗ pas de série de 12 (fêtes par paires) |

**Résultat clé** : les **deux seules** listes qui donnent un **11e = Simon le Zélote** (la scie de l'enl. 12) **sans** mettre d'attribut en bois sur la 3e sont **Matthieu 10** et **Marc 3**. Ce sont aussi les deux listes où l'identification de l'apôtre « à la scie » est certaine (Simon le Zélote, et non Joseph : son attribut habituel est la hache/rabot/lys, jamais la scie seule avec un livre — `illustration_e12.md`).
- **Sens de numérotation** (tous testés) : « depuis la droite du Christ » → 11e au SE (Mouret) ✓ ; **miroir** (depuis sa gauche) → 11e à 45.4354, 6.0407, **bâti à 57 m** (échoue « loin des bâtiments ») ✗. Le sens droite est le seul bon.
- **Confirmation indépendante du 28/10** : les 4 listes synoptiques donnent la même fête du 11e (28 octobre, Simon et Jude) — donc le choix de la liste ne change pas la date.
- **FAQ04-051** (« l'ordre qui définit le *numéro un* d'Ultima Cena est-il le même que celui des 3e/11e ? → **Non**, et c'est une très bonne question ») : notre chaîne **n'utilise pas** l'ordre d'Ultima Cena ; elle utilise la **liste apostolique synoptique**. La réponse de l'auteur ne fait que confirmer que les deux ordres diffèrent → compatible.
- **Réserve honnête** : l'auteur **refuse de confirmer les apôtres** (FAQ03-007 : « ça présuppose qu'il s'agit d'apôtres, ce que je n'ai pas indiqué ») et **refuse la question « liste de douze apôtres »** (FAQ8). C'est une **inférence**, non une donnée validée.

## 2. Pourquoi les 3e et 11e sont « deux convives » : C1-C13

- **même nature** (06-009 / « oui ») : deux **places de la table de la Cène** ;
- **un seul de chaque** (06-216) : une seule table, 12 apôtres + le Christ = **13 convives** ;
- **le 13e existe** (06-133) : le 13e = **le Christ** (à l'Orient) ou Matthias (Ac 1,26, fête 14/05) ; sa place ne mène pas au bon endroit (calculée plus bas : bâti à 25 m) ;
- **8e et 16e « incorrects »** (FAQ8) : une table de 12 n'a **pas** de 16e ; le 8e serait un autre apôtre (Thomas) → incompatible avec le texte ;
- **pas un ensemble de 52** (07-156), **pas un chevalier** (07-065), **pas un ensemble de couleurs** (07-244) : ✅ ;
- **deux points à pointer, invisibles sur Maps** (05-074, 07-063, 06-227) : ✅ (des places de table ne figurent pas sur Google Maps) ;
- **trouvables de chez soi** (04-114) : ✅.

## 3. Lien avec l'enluminure 12 et « la coupe du charpentier »

- Enl. 12 : **Jésus seul à une longue table** (« enluminure incomplète, parcellaire », FAQ03-065) + à droite le **vieillard à la scie et au livre** = **saint Simon le Zélote**, le 11e de la liste de Mt/Mc (`illustration_e12.md` ; voir aussi `RANGEE_LEONARD_E12.md`). La question « mains différentes » est sans importance (FAQ06-238) → le personnage et sa **scie** sont bien voulus.
- **La coupe du charpentier** = le **but de la quête** (FAQ04-073), **le trésor** (06-291), **la coupe de l'enl. 9** (07-005), **pas un anachronisme** (06-246). La **scie** du 11e est un **outil de charpentier** : l'apôtre n° 11 (Simon) porte l'outil du métier du « charpentier », là où se trouve la coupe. **Pont thématique faible → appui qualitatif**, non une preuve.
- **FAQ04-150** : « coupe du charpentier » est « correct et bien choisi » — l'auteur ne dit pas s'il est relié au **nom du lieu** (donc pas d'exploitation d'un toponyme « charpentier »).

## 4. Géométrie : la règle posée AVANT, le cercle, où tombent la 3e et la 11e

**Règle posée avant de regarder le terrain** (hypothèse P, §5 du raisonnement d'auteur) : le départ est le **chemin de rempart = pied de la tour d'Avalon** (FAQ06-193/05-195, point précis 07-268) ; le **centre** du dispositif est le départ ; **12 places à 30°**, **corde 3→11 = 1 850 m** → **rayon R = 1 850 / (2 sin 60°) = 1 068,1 m** ; le **Christ est à l'Orient**, orienté par **l'aube de Pâques vue du rempart** (ligne 2 : veillée pascale, « dernier veille », « l'endroit m'est apparu au matin, illuminé par l'astre glorieux ») — soit **91,4°** (lever visible 1524, tour d'Avalon) à **93,0–93,6°** (2026, canopée comprise). Apôtres numérotés **depuis la droite du Christ**.

| Place | cap | coordonnées | environnement |
|---|---|---|---|
| 3e (Jacques / Jean) | 16,4° | **45.43802, 6.03463** | 1 068 m de la tour, jonction ordinaire à 28 m, **bâti à 222 m** (ouvert, non boisé au voisinage) |
| **11e (Simon)** | 136,4° | **45.42184, 6.04019** | **8 m de la source** (45.42177, 6.04019) ; **66 m du carrefour du Mouret** (4 branches) ; jonction « visible+eau » à 95 m ; **bâti à 105–178 m** |
| 13e (Christ) | 91,4° | 45.42856, 6.04442 | **bâti à 25 m** → « ne mène pas au bon endroit » ✓ (06-133) |

- **Corde 3→11 = 1 850 m** exactement (par construction) et elle **passe à 17 m du carrefour du Mouret et à 8 m de la source** → ce sont les « **étapes intermédiaires** » de FAQ04-115 (aller « directement de la 3e à la 11e »).
- **Variantes d'orientation testées** (mission : Pâques 1524, 30/04/1524, Orient, Lincoln/Payns…) : la 11e tombe sur la source/Mouret **uniquement** pour A ≈ 90–93° (Pâques / est vrai). Le **30/04/1524** (63,7-73,9°) envoie la 11e à **45.4241-45.4257, 6.0427-6.0437** (300-500 m du Mouret) ✗ ; **Lincoln 95,1-95,6°** → 113-127 m ✗.

## 5. Quelle est la « destination finale » ? (FAQ03-293)

FAQ03-293 : « … la troisième et la onzième **à la destination finale**, ou seulement **deux étapes, une intermédiaire plus la destination finale**. Il n'y a que deux étapes. »
→ Lecture littérale : la **3e = étape intermédiaire**, la **11e = destination finale** (la clairière, §FAQ07-133 « les 3e/11e permettent directement d'identifier la clairière »). Cohérent avec : l'écharde au 11e (bois), « on marche surtout sur l'une » (la 11e, 06-247), l'eau/la roche au bout du parcours. **Mais** cette lecture est celle de N1, dont le **mécanisme de placement est mort** (§4 de `R0610_N1_inverse.md` : 6 points en champs du Couvat, 0 objet, hasard 25,7 %).

## 6. Test du hasard **propre** (mission §4)

Méthode : centre de la table **fixé à la tour** (seul paramètre libre = l'orientation A) ; balayage de A de 0 à 360° (pas 0,25°) ; « jonction qualifiée » = **visible (`vis`) ET eau ≤ 100 m (`d_chan`/`d_wat`) ET bâti ≥ 100 m** ; on compte les A où la 11e (ou la 3e) est à ≤ 100 m d'une telle jonction.

| Critère | P (11e) | Fenêtre de A | P (3e) |
|---|---|---|---|
| ≤ 50 m | **0,00 %** | — | 0,00 % |
| **≤ 100 m** | **1,03 %** | **89,8 – 93,4°** (unique) | 0,97 % (fenêtre 210-213°, sans sens) |
| ≤ 150 m | 3,64 % | 85,1 – 98,1° | — |

- La **seule** fenêtre où la 11e tombe sur une jonction visible avec eau est **89,8-93,4°** → **exactement l'aube de Pâques** (91,4-93,6°) et l'est vrai. **Le Mouret ressort, et lui seul.**
- **Placebo (centres tirés au hasard dans un disque de 1,3 km, 20 000 tirages)** : P(11e ≤ 100 m d'une jonction qualifiée) = **1,79 %** (≤ 50 m : 0,445 %). → le centre fixe (la tour) n'est **pas** meilleur que le hasard : c'est **l'orientation (l'aube) qui fait tout**.
- **Fragilité décisive** : toute la fenêtre repose sur **une seule** jonction (45.42243, **6.03932**, 77 m à l'ouest du carrefour du Mouret) dont le **bâti le plus proche est à 105 m** ; dès qu'on exige **bâti ≥ 150 m**, **P = 0,00 %** (plus aucune fenêtre). Le seuil de 100 m est donc à la limite.
- Le **carrefour du Mouret proprement dit** (45.42243, 6.04030) a `vis = False` (non vu du pied) : seule la **prairie voisine** est vue (cf. `R0610_J12/MOURET_FAIBLESSES_E12.md`) — l'`vis` de `t16` est l'ancienne convention « du pied », pas la vue recalculée depuis les murailles.

## 7. Grille C1-C16 (00_PISTES_VIVANTES §1)

| | Contrainte | Score |
|---|---|---|
| C1 | même nature | ✅ deux places de la Cène |
| C2 | un seul de chaque | ✅ |
| C3 | deux points à pointer | ✅ |
| C4 | 1 850 m ±1 % en ligne droite | ✅ par construction |
| C5 | pas visibles sur Maps (06-227) | ✅ |
| C6 | trouvables de chez soi | ✅ |
| C7 | pas d'écharde sur la 3e, écharde possible sur le 11e | ✅ **si liste Mt 10 ou Mc 3** (Simon/scie) |
| C8 | on marche surtout sur l'une | ✅ la 11e (vers la source) |
| C9 | le 13e existe mais mène ailleurs | ✅ Christ à 25 m du bâti |
| C10 | 8e/16e incorrects | ✅ pas de 16e |
| C11 | pas un ensemble de 52 | ✅ |
| C12 | pas un chevalier | ✅ |
| C13 | ordre ≠ « numéro un » d'Ultima Cena | ✅ (liste synoptique, ordre distinct) |
| C14 | l'enl. 11 place « une partie » et confirme l'un des deux | ⚠️ (croix PATERNOSTER / « orientez-vous » → l'Orient ; « une partie » seulement) |
| C15 | se positionnent par rapport au point de départ | ✅ |
| C16 | le 11e ne prête pas à sourire | ✅ |

**Bilan grille : 15 ✅, 1 ⚠️ (C14), 0 ❌.** C'est le meilleur score jamais obtenu pour l'identité des 3e/11e. **Mais la grille ne teste PAS** : le hasard (§6, ~1-2 %), le **domaine public**, la **visibilité réelle**, ni surtout le **déroulé roche→coffre** — qui, lui, échoue.

## 8. Faiblesses restantes (honnêtes)

1. **La liste d'apôtres est une inférence** : l'auteur refuse de confirmer « apôtres » (03-007) et la « liste de douze apôtres » (FAQ8).
2. **Hasard ~1 % mais non robuste** : repose sur une jonction à bâti 105 m ; à bâti ≥ 150 m, P = 0 ; placebo = 1,8 %.
3. **Le point final au Mouret échoue** : le déroulé « grande roche + 10 N + 10 E + 8 » **0 survivant sur 1 199 variantes** (`R0710_M1_*`), et la « grande roche » n'est pas un rocher nu (bug canopée corrigé).
4. **La 3e place (Jacques/Jean) n'a aucun objet identifié** : jonction ordinaire à 28 m, pas de « point remarquable ».
5. **Roche ≠ source** (FAQ03-082 : l'eau coule **jusqu'à** la grande roche et **continue**) ; ruisseau suivi (talweg BD TOPO absent) ≠ ruisseau vu du rempart (Rebouchet) — tension non résolue.
6. **Domaine public** : la fouille près de la source est en **bois privé** (B0267).
7. **Visibilité** : le carrefour n'est pas vu du rempart, seule la prairie l'est.
8. **Multiplicité** : ~8-10 constructions essayées ; le rang honnête est ~2-20 % (§31 `REVUE_ADVERSE_P.md`).
9. **Si la table avait 13 places égales** (le Christ occupe une place), R = 990 m et **rien** ne tombe (t120 : 3 360 positions, aucun signal).

## 9. Recommandations

- **Tester en priorité** `r0610_R_roches.py` rejoué avec `S2 = MNH < 3` (bug canopée) : le **seul lieu du secteur où le déroulé donne des points plats/isolés en série** est la **roche de 109 m² à 45.43612, 6.03680** (à 940 m N de la tour) — hors Mouret.
- Vérifier **sur orthophoto** la 3e place (45.43802, 6.03463) : est-elle **ouverte** (pas d'écharde) comme le suppose C7 ?
- Trancher la **liste** : chercher un 3e argument (hors écharde) départageant **Matthieu** (3e=Jacques) et **Marc** (3e=Jean, « Dieu a fait grâce » = 1re phrase).
- **Ne pas relancer le point final au Mouret** sans une raison de lecture nouvelle : le `R0710_M1` est conclusif pour la fouille.

---

### Fichiers
- Rapport : `vault_EXKALIBUR/_Resolution/Enigme_12/R0710_MA_mouret_3e11e.md` (ce fichier)
- Scripts : `outils_scratch/r0710_MA_mouret_3e11e.py`, `r0710_MA_hasard.py`, `r0710_MA_part3.py`, `r0710_MA_part4.py`, `r0710_MA_part5.py`
- Pas de commit (l'orchestrateur le fait).
