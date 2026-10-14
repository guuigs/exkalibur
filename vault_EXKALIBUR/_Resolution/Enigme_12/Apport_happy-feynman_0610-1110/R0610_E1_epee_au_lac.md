# R0610_E1 — « L'épée retournée au lac » : test de l'hypothèse combinée (06/10/2026)

**Verdict : RIEN de fiable spatialement.** La légende confirme le retour de l'épée à l'**eau** (jamais à la pierre), mais appliquée à la règle lac → clairière → eaux enchantées → roche, l'hypothèse re-converge sur l'unique étang naturel proche de la tour — le **Vivier d'Avalon** — déjà testé et écarté (J16, t43/t54). Aucun plan d'eau ≤ 2,5 km ne satisfait la conjonction complète des critères.

---

## 1. Sources littéraires (vérifiées, citations) — MISSIONS (1)

Le scénario du brief est **confirmé tel quel**. Le détail exact, par source :

| Source | Qui jette | Combien de fois | Où | La main |
|---|---|---|---|---|
| **Vulgate, *La Mort le roi Artu*** (c.1230) | **Girflet** (Griflet) | désobéit **deux fois**, jette à la **3e** | dans un **lac** proche | « une main de femme surgit du lac » (puis Morgane emmène Arthur à Avalon) |
| **Malory, *Le Morte d'Arthur*, XXI.5** (1485) | **Bedivere** | désobéit **deux fois**, jette à la **3e** | dans un **lac** | « an arm and an hand above the water… caught it, and so shook it **thrice** and brandished » |
| **Geoffroy de Monmouth, *Historia Regum Britanniae* IX** (c.1136) | — (aucune scène de lancer) | — | épée **Caliburnus « forgée dans l'île d'Avalon »** | — |
| **Wace, *Roman de Brut*** (c.1155) | — (idem, suit Geoffroy) | — | **Caliburne/Escalibor forgée à Avalon** | — |
| **Lancelot-Graal (Vulgate)** | la Dame du Lac (Viviane) **donne** l'épée à Arthur ; *Mort Artu* la lui fait rendre par Girflet | | **lac** | |

**Fait clé (réponse à la question « toute version où l'épée retourne à la pierre / au perron ? ») : il n'en existe AUCUNE.** L'« épée dans la pierre » (enclume sur un perron, cimetière, Noël) est un motif **distinct**, introduit par Robert de Boron (*Merlin*, c.1200) : c'est l'épée du **sacre** d'Arthur, qui chez Malory **se brise** ensuite contre Pellinoré et est remplacée par Excalibur, l'épée **du lac**, donnée par la Dame du Lac. À la mort d'Arthur, l'épée revient toujours à l'**eau** (le lac / la Dame du Lac), jamais à la pierre. Les deux épées ne sont confondues que dans les réécritures modernes (Disney, Boorman). *(Sources : Wikipedia « Excalibur » [en], Wikipedia « Girflet » [fr], mythology.stackexchange q.507.)*

Nuance : la légende fait **donner** (pas forger) l'épée par la Dame du Lac ; c'est Geoffroy qui la dit **forgée à Avalon**. L'É1 du jeu (« Elle la forgea ») fusionne les deux — cohérent avec l'hypothèse « la Dame du Lac est à l'origine de l'épée ».

**Conclusion mission (1) : l'hypothèse « l'épée retournée au lac » est la version canonique exacte. Le texte du jeu (« tombée par trois fois… revenue là où elle n'avait jamais cessé d'être ») reprend précisément les 3 lancers de Girflet/Bedivere. Le point d'arrivée est l'EAU, pas la pierre.**

---

## 2. Inventaire des plans d'eau ≤ 2,5 km (BD TOPO hydro surfacique + OSM) — MISSION (2)

Règle de sélection (posée AVANT de regarder, cf. §3) : `clairière = jonction de chemins près du lac de l'épée ; eaux enchantées = le ruisseau relié à ce lac ; grande roche = là où l'épée n'a jamais cessé d'être`.

Données : BD TOPO `surface_hydrographique` (67 surfaces, fenêtre 7,6×6,7 km, WFS IGN) + `troncon_hydrographique` + `troncon_de_route` (8 494 croisements) + `batiment` + `commune` (13 communes) ; LiDAR HD local 1 m (tuile J16, X 936000-938000 / Y 6484000-6486500). OSM `natural=water` ≤ 2,6 km : seul « **Le Bréda** » (rivière) nommé — aucun étang nommé. **18 plans d'eau ≤ 2,5 km.**

**Répartition par commune** : **Pontcharra (interdite) = 13/18**, Saint-Maximin = 3, Laissaud = 1, Barraux = 1.

| dist | nature | aire m² | commune | ruisseau (BD TOPO) | croisem. ≤150 m | bâti | roche LiDAR | visible tour | lat,lon |
|---|---|---|---|---|---|---|---|---|---|
| **146 m** | **Retenue (étang)** | **10 372** | **Saint-Maximin** | non (244 m ; seul un talweg exutoire) | **74** | **17 m** | 2,3 m (motte) | 26/415 | 45.42840, 6.03275 |
| 448 m | Retenue | 4 321 | Pontcharra | **oui (14 m)** | 69 | 37 m | (talus) | 0/171 | 45.43262, 6.02885 |
| 644 m | Écoulement naturel (Bréda) | 19 602 | Pontcharra | rivière | 175 | 2 m | (berge) | 20/785 | 45.43444, 6.03340 |
| 830 m | Réservoir-bassin | 198 | Saint-Maximin | non | 10 | 30 m | 1,5 m | 0/8 | 45.42656, 6.04110 |
| 1 606 m | Écoulement naturel | 20 416 | Pontcharra | rivière | 466 | 1 m | — | hors tuile | 45.43774, 6.01477 |
| 1 712 m | Réservoir-bassin | 105 | Saint-Maximin | non | 17 | 3 m | — | hors tuile | 45.43396, 6.05168 |
| 1 761–2 397 m | 11 bassins/réservoirs + 3 rivières | 105–9 456 | Pontcharra (10), Laissaud (1), Barraux (1) | variables | — | 3–88 m | — | hors tuile | — |

**Lecture** : en dehors de Pontcharra, il n'existe qu'**un seul** plan d'eau naturel de type étang/vivier/lac à ≤ 2,5 km : la **Retenue de 1 ha à 146 m de la tour, au pied sud-est de la motte, dans le lieu-dit « Le Chêne, la Roche et le Vivier »** = le **Vivier d'Avalon / Marais d'Avalon**. Tout le reste est soit en Pontcharra, soit un bassin artificiel de 100–2 000 m², soit une rivière.

---

## 3. Règle posée AVANT de regarder — MISSION (3)

> Le « lac de l'épée » (où elle n'a jamais cessé d'être, visible du rempart) est le plan d'eau qui, **en un seul et même lieu**, fournit : **(a)** la clairière = jonction de chemins à ≤ 150 m ; **(b)** les eaux enchantées = un ruisseau entrant/sortant relié à ce plan d'eau ; **(c)** la grande roche = une bosse rocheuse au bord de l'eau ; avec les contraintes invariantes du jeu : **(d)** visible depuis le rempart, **(e)** domaine public, **(f)** bâti ≥ 100 m, **(g)** hors Pontcharra.

Zéro paramètre ajusté après coup.

---

## 4. Classification et test du hasard — MISSION (4)

Application de la règle aux 18 plans d'eau :

- **Vivier d'Avalon (146 m)** — seul candidat « étang » naturel en zone autorisée. Satisfait : clairière (74 croisements ≤150 m, dont J16), roche (motte, 2,3 m), hors Pontcharra, partiellement public, partiellement visible (26/415 cellules). **Échoue** : **(b) aucun ruisseau BD TOPO relié** (244 m ; seul un exutoire-talweg LiDAR), **(f) bâti à 17 m**.
- **Retenue 448 m (Pontcharra)** — satisfait (b) ruisseau à 14 m, mais **échoue (g) Pontcharra** et **(d) invisible** (0/171).
- Tous les autres : rivières (pas un « lac ») ou bassins artificiels, en Pontcharra ou sans roche/clairière conjoints.

**Résultat : 0 plan d'eau satisfait la conjonction complète (a)–(g).**

**Test du hasard.** Sur 18 plans d'eau ≤ 2,5 km, **1 seul** est un étang naturel non-rivière dans les communes autorisées (1/18 ≈ 5,6 %) ; c'est précisément celui qu'on connaissait déjà (Vivier d'Avalon) et qu'on a déjà écarté. Si l'on impose en plus les critères de la règle (ruisseau relié + bâti ≥ 100 m), ce candidat tombe et il reste **0**. Autrement dit : l'hypothèse « lac de l'épée » **n'apporte aucune sélection nouvelle** — elle re-désigne un point déjà testé, avec un hasard non significatif (le seul « étang » près de la tour est trivialement repéré par sa proximité, pas par la logique de l'épée). Aucun signal ≤ 2 %.

---

## 5. Ce qui change par rapport à J16 / Vivier d'Avalon — MISSION (5)

**Ce que l'hypothèse apporte de neuf :**
1. La **légitimité textuelle** : « tombée par trois fois… revenue là où elle n'avait jamais cessé d'être » = les **3 lancers** de Girflet/Bedivere, et l'arrivée est **l'eau** (canon, vérifié). Ce point n'était qu'« de mémoire » dans le dossier ; il est maintenant sourcé.
2. La **règle explicite** lac → clairière / ruisseau / roche, appliquée à l'ensemble des plans d'eau (pas seulement au Vivier), confirme que **le Vivier d'Avalon est le seul étang naturel de la zone autorisée** — donc le seul « bassin » de l'enluminure 9 possible.

**Ce qui ne change pas (pourquoi J16/Vivier avaient échoué — on relit les mêmes causes) :**
- **J16** (jonction de la Route du Vivier, clairière du crible « depuis chez soi ») : branche est testée → **0/66 points de fouille** valables (bois privé ou berge 27–36°) — `R0610_J16_est.md`.
- **Vivier d'Avalon comme zone du coffre** : **bâti à moins de 100 m** (ici 17 m), **Espace naturel sensible**, exutoire en zone bâtie, rien de visible du pied — `t43`, `t54`, `PISTES_ECARTEES` #54.
- Le Vivier n'a **pas de ruisseau entrant/sortant cartographié** : les « eaux enchantées » de la règle ne sont qu'un talweg LiDAR intermittent, pas un cours d'eau BD TOPO.

**Conclusion** : l'hypothèse combinée est **textuellement juste mais spatialement stérile**. Elle explique *pourquoi* l'enl. 9 montre un bassin (c'est le retour de l'épée au lac, topographiquement lié au 1er paragraphe, FAQ06-069), sans donner de coordonnée de fouille nouvelle. Le coffre n'est pas « au lac » ; le lac est le **confirmateur visuel de la zone**, pas le lieu du creusement.

---

## 6. Fichiers produits
- `outils_scratch/r0610_e1_fetch.py`, `r0610_e1_lac.py` ; données `outils_scratch/scratch_e1/` (bdtopo_surface_hydro, troncon_hydro/route, batiment, commune, e1_plans_eau.json).

**Recommandé ensuite** : traiter le Vivier/marais comme **indice de nature** (bassin = image de zone), pas de position ; chercher la clairière (jonction visible du rempart) et la grande roche **indépendamment** du plan d'eau, puis tester si le « ruisseau enchanté » réel (Rebouchet, Perrière) remonte vers une roche nommée. Aucun nouveau déplacement sur place.
