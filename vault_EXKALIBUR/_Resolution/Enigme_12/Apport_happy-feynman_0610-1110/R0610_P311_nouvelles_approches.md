# R0610_P311 — Pair 3e/11e par approches NOUVELLES (numérotation cadastrale, chemins/voies numérotés, sections, autres séries administratives)

**Statut : COMPLET — verdict RIEN** (07/10/2026, sous-agent P311).
Règle posée AVANT tout calcul : pour chaque approche, on définit a priori la série et
l'ordre, on balaie systématiquement le rayon **≤ 5 km** autour de la tour d'Avalon
(45.4288, 6.03078), on cherche une paire à **1 850 m ± 1 %** (1 831,5–1 868,5 m) en ligne
droite, puis on fait le **test du hasard** (≥ 1 000 tirages) et on note C1–C16.

Données : cadastre Etalab (`cadastre.data.gouv.fr`, parcelles WGS84) pour **18 communes
≤ 8 km** (2 460 à 9 240 parcelles chacune, 79 760 features au total) ; BD TOPO
`troncon_de_route` ; OSM (gazetier `donnees_travail/r0610_gaz/osm_hwy.json`, 78 514 ways) ;
Overpass (passages à niveau, bornes, ouvrages d'art). Scripts :
`outils_scratch/r0610_p311_{communes,download,A_parcelles,AC2_variantes,hasard,D_series}.py`.

---

## Approche A — Numéros cadastraux : parcelles n°3 et n°11 d'une même section

**Règle (posée avant) :** pour chaque **section** (feuille) d'une commune, on prend la
parcelle de **numéro 3** et celle de **numéro 11** (c'est exactement la structure du plan
cadastral : `id = INSEE + section + numero`) ; on mesure la distance entre leurs **points
représentatifs** (et la distance minimale entre géométries). On note si la parcelle n°13
existe dans la même section (C9).

**Résultats.**
- 18 communes ≤ 8 km, 99 sections possédant à la fois un n°3 et un n°11 → **99 paires** ;
  **45** avec au moins un point ≤ 5 km.
- **Dans la fenêtre 1 850 ± 18 m et à ≤ 5 km : 0 paire.**
- Une **seule** paire "n3 × n11 même section" tombe dans la fenêtre sur tout le rayon 8 km :
  **Porte-de-Savoie, section AA, 1 853 m** — mais ses deux points sont à **7,9 et 9,1 km**
  de la tour (commune nord, hors zone utile).
- **Raison structurelle** (décisive) : dans une section, les numéros sont attribués par
  blocs contigus. Les paires pertinentes (communes proches) sont donc *toujours courtes* :
  Saint-Maximin A 3↔11 = **64 m**, B 3↔11 = 134 m ; Pontcharra D = 83 m, AL = 128 m ;
  Barraux C = 49 m ; Le Moutaret C = 136 m. Aucune n'approche 1 850 m.

**Variante A2 (n°3 × n°11 sans contrainte de section, même commune, ≤ 5 km) :**
5 paires dans la fenêtre — 3 à Pontcharra (zone interdite : AR↔ZB 1 849 m, AR↔AH 1 848 m,
AR↔ZA 1 836 m), Le Moutaret A↔C **1 865 m** (points à 4,1 et 3,4 km, terres agricoles),
Laissaud A↔ZC **1 867 m** (3,1 / 2,9 km). **Test du hasard** : densité de paires
parcellaires dans la fenêtre = 0,640 % → sur les 384 combinaisons n3×n11 (≤ 5 km),
**2,46 paires attendues par hasard** ; les 5 observées sont au niveau du hasard
(P[X ≥ 5 | λ = 2,46] ≈ 12 %). Et toutes sont **hors du domaine public attendu** (Pontcharra
interdit, ou plaine agricole à > 3 km, « loin de tout bâtiment » non vérifié).

**Test du hasard A1** (le tirage de référence = 2 rangs aléatoires par section) :
**35,4 %** des 1 000 tirages donnent au moins une paire dans la fenêtre — la règle 3×11
donne **0** paire ≤ 5 km, soit **sous le hasard**.

**Note textuelle gardée** (pas un placement) : la FAQ dit « deux points de **même nature** »
(06-009) et « la **nature** de mes 3e/11e a été identifiée » (06-259). « Nature » est
exactement le vocabulaire cadastral (nature de culture : bois / terre / pré…). La
coïncidence de vocabulaire est réelle, mais **aucune paire cadastrale ne se place à
1 850 m** : la piste meurt sur C4.

**C1–C16 :** C4 ✗ (décisif, distance introuvable) · C5 ~ (cadastre en ligne, pas « Maps ») ·
C7 ✓ (bois ⇒ écharde) · C9 ✓ (n°13 existe presque partout) · C3/C6/C8/C11/C12 ✓ ·
C14 ✗ (aucun lien à l'enl. 11). → **RIEN.**

---

## Approche B — Chemins ruraux / voies communales numérotés (CR 3 / VC 3, CR 11 / VC 11)

**Règle :** deux voies numérotées **3** et **11** de la même catégorie (chemins ruraux,
voies communales), leur point milieu, distance 1 850 m.

**Données.** Aucun `ref` de type « CR n », « VC n », « C n », ni nom « Voie communale
numéro 3/11 » ni « Chemin rural n° 3/11 » **dans les 5 km** autour de la tour. Les seuls
`ref` de voirie locale y sont des routes départementales (D 1090 = 41 tronçons, D 523,
D 9, D 202, D 590a…) ; les noms « Voie Communale n°… » d'OSM sont ailleurs (massif de
Chartreuse/Vercors, à > 10 km). BD TOPO `troncon_de_route` : pas de champ « numéro de voie
communale » exploitable (seuls `cpx_numero`, qui sont des numéros de route classée).
Les « tableaux de voirie » communaux (numérotation VC) ne sont pas publiés en ligne pour
Saint-Maximin / Pontcharra / Laissaud.

**Verdict : RIEN** (absence de données : la série 3/11 des VC/CR n'existe pas dans la base
autour de la tour ; C4 ✗ faute de points).

---

## Approche C — Lettres de sections (C = 3e lettre, K = 11e lettre)

**Règle :** A = 1, B = 2, … ⇒ 3e lettre = **C**, 11e lettre = **K** ; on compare la section
**C** et la section **K** de la même commune (centroïdes et distance minimale).

**Résultat :** **aucune des 18 communes n'a à la fois une section « C » et une section
« K ».** Beaucoup ont une section C (Barraux, Chapareillan, Le Moutaret, Crêts en
Belledonne, Porte-de-Savoie, Sainte-Hélène-du-Lac…) ; **aucune** n'a de section « K » seule
(le K n'apparaît que dans des codes à deux lettres — AK, ZK — qui sont des sections
« nouvelles », pas le 11e rang). → **0 paire mesurable. RIEN.**

---

## Approche D — Autres séries administratives numérotées locales

**Règle :** chercher une série locale ordonnée ≥ 13 éléments où les rangs **3** et **11**
donnent deux objets ponctuels (passages à niveau SNCF « PN n », bornes kilométriques PK,
bornes/rivest, ouvrages d'art SNCF/A41).

**Résultats (Overpass, rayon 5 km).**
- **Passages à niveau** : 13 nœuds `railway=level_crossing/crossing` (1 747 → 4 891 m),
  **aucun numéro** (pas de `ref` PN) ; tous le long de la ligne SNCF Grenoble–Montmélian,
  majoritairement côté Pontcharra. Pas de série « PN 3 / PN 11 » exploitable en open data.
- **Bornes kilométriques** : **1 seul** `historic=milestone` (borne milliaire, 4 203 m).
  Pas de série PK en open data.
- **Bornes géodésiques IGN (1949)** : 23 repères, numérotés **par commune**
  (3842601-1/A/B, 38314A-1…), sans rang 3/11.
- **Ouvrages d'art (ponts/tunnels A41, D 523, D 1090…)** : portent un `ref` de **route**,
  jamais un numéro d'ouvrage ; pas de champ « OA n°3 / n°11 ».
- Rappel déjà écarté : bornes royales D 1090 à intervalle 1 949 m (+5,4 %), hors tolérance.

**Verdict : RIEN** (aucune série à 3/11 ; C4 ✗).

---

## Tableau récapitulatif

| Approche | Points candidats | Paires 1 850 ±18 m (≤5 km) | Test du hasard | Verdict |
|---|---|---|---|---|
| A1 — parcelles n3×n11 **même section** | 99 paires (45 ≤5 km) | **0** | hasard : 35,4 % des tirages donnent ≥1 paire → observé **sous le hasard** | **RIEN** |
| A2 — n3×n11 cross-section (même commune) | 384 combinaisons | 5 (Pontcharra X, Le Moutaret, Laissaud) | attendues 2,46 ; observées 5 (P ≈ 12 %) → **niveau du hasard** | **RIEN** |
| B — CR/VC numérotés 3 et 11 | 0 | 0 | — | **RIEN** (pas de données) |
| C — lettres de sections C↔K | 0 (aucune commune n'a C et K) | 0 | — | **RIEN** |
| D — PN / PK / bornes / ouvrages d'art | 0 série « n°3 + n°11 » | 0 | — | **RIEN** |

---

## Bilan et recommandations

- **Verdict global : RIEN de fiable.** Les quatre séries administratives numérotées
  (cadastre, voirie, sections, PN/PK) ne fournissent **aucune** paire à 1 850 m ± 1 %
  dans les 5 km, et là où des paires apparaissent elles sont **au niveau du hasard** et
  hors zone utile (Pontcharra interdite, plaine agricole > 3 km).
- **Raison structurelle** (à retenir contre un retour de la piste cadastre) : les numéros
  « 3 » et « 11 » d'une même section sont des **blocs contigus** (toujours < 500 m), donc
  ils ne peuvent pas être à 10 stades l'un de l'autre par construction du plan cadastral.
- **Ce qui reste ouvert** (hors P311, non tranché ici) : la **nature bois/pierre** (07-068)
  et « marchable » (06-247) continuent de pointer vers des **objets marchables** (le n°11
  en bois, le n°3 en pierre/terre) plutôt que vers des parcelles ou des voies. Combiner avec
  CD-C de `R0610_T3_faq.md` (pierres 3 et 11 du chemin de l'enluminure 11) plutôt qu'avec
  une numérotation administrative.
- **À ne plus relancer sous cette forme** : numéros de parcelles, numéros de voirie,
  lettres de sections, PN/PK.

**Faits vérifiables :** 18 parcellaires cadastraux téléchargés
`outils_scratch/cadastre/parcelles/cadastre-<INSEE>-parcelles.json.gz` ; résultats bruts
`donnees_travail/r0610_p311_A_parcelles_3_11.json`, `r0610_p311_AC_variantes.json`,
`r0610_p311_D_series.json` ; 6 scripts `outils_scratch/r0610_p311_*.py`.
