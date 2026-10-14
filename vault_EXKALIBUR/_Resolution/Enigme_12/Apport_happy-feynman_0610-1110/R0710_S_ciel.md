# R0710_S — Lien avec le CIEL : extraction FAQ, règles célestes, terrain et hasard (07/10/2026)

**Verdict : RIEN.** Aucune des 6 règles célestes posées ne produit de lieu qualifié depuis le rempart ; les quelques coïncidences sont au niveau du hasard. Détail des calculs, des filtres et des tests ci-dessous.

Fichiers : scripts `outils_scratch/r0710_S_*.py` ; données `donnees_travail/r0710_S_*.json|npy` ; cartes `images_travail/r0710_S_carte.jpg`, `r0710_S_zoom.jpg`.

---

## 1. Corpus FAQ « ciel / astre / veille / matin » — extraction et classement

Extraction automatique sur `Communaute/faq_officielle_auteur.json` (1 852 Q/R) : **105 Q/R** touchent ciel/astre/soleil/lune/étoile/planète/constellation/veille/matin/lever/illuminé/magnifiait/jour dernier ; plus la transcription `outils_scratch/faq8.txt`. Faits classés (verbatim entre guillemets) :

### 1a. Ce que fait le ciel (rôle)
| Fait | Réf |
|---|---|
| « Le ciel a toute sa place… souvenez-vous toujours dans les moments de doute de vous tourner vers le ciel. » | 03-033 |
| « Les ciels ont-ils une importance ? **Oui, le ciel est important.** » | 03-214 |
| « puis-je apercevoir une partie du ciel sur la carte ? … **oui** » | 06-151 |
| « gardez bien le ciel en tête, il n'est pas là pour rien » (lettrine Omnia) | 06-066 |
| « j'ai en effet demandé à **représenter certains astres** sur les enluminures » (Jupiter) | 07-185, 06-200 |
| les astres des enluminures aident à lire **les symboles du ciel de l'enl. 9** : « oui, tout à fait » | FAQ8 |
| « la disposition de certains éléments vous permet de comprendre ce que vous regardez » | 07-108 |
| la précession « n'a pas d'importance » | 07-104 |
| le ciel guide « **en tout dernier lieu** » | FAQ8 |

### 1b. Le « jour dernier » et « l'astre glorieux »
| Fait | Réf |
|---|---|
| rempart = **point de départ** ; « c'est **l'astre glorieux** qui vous indique où aller. C'est là que les **3e et 11e** seront utiles » | 06-166 |
| « relation avec le ciel pour trouver la **direction** **et** pour trouver **l'endroit** où vous allez arriver depuis le rempart » | 07-152 |
| « quand on parle d'astre glorieux, on parle du **ciel qui va vous guider**, mais **je ne parlerai pas de direction en tant que telle** » | 07-132 |
| « **Ne soyez pas obnubilé par la direction**… identifier les 3e et 11e et voir ce que vous en faites avec **la distance, le point de départ** » | 07-180 |
| une fois la direction trouvée, 3e/11e « permettent d'identifier la clairière : oui, tout à fait » | 07-133 |
| « magnifia le ruisseau » (pas « protégeait » : Non) | 07-009 |
| « l'endroit est dans le **champ de vision** » depuis le rempart (l'auteur y est monté) | 05-155 |
| « **pas besoin de lever la tête** pour trouver le jour dernier » | FAQ8 |
| « jour dernier » = **un jour**, pas un moment | 07-186 |
| l'astre glorieux représenté en enl. 12 ? **NRP** ; la clairière et l'astre déjà rencontrés avant ? **Non** | FAQ8 |

### 1c. Le ciel de l'enl. 9 (code à 6 signes)
| Fait | Réf |
|---|---|
| 6 dessins : loup, étoile, arc-en-ciel, âne, ancre + **croissant de lune** (6e, à droite de l'arbre) | 05-097, 06-258 |
| « un **seul élément** permet de comprendre la majorité des signes » → « vous êtes plutôt sur la bonne piste » | FAQ8 |
| « ils ne racontent pas une histoire mais permettent d'**identifier un élément crucial** » ; « **déclic en fin de jeu** » | 07-134, 07-198 |
| à interpréter **une fois la zone finale trouvée** | 06-067 |
| les signes allant par deux se décodent **ensemble** (ancre/diamant, âne/émeraude) | 07-143 |
| **code universel** ; pas un rébus phonétique (lecture étymologique/héraldique/historique) | 06-138, 06-059 |
| l'« **aurore** » de l'enl. 9 n'a pas pu être remplacée | FAQ8 |
| astres des enl. 1 et 3 : « le point clé est davantage **la couleur** que les cratères » | 06-063 |
| une **Vénus** est sur le château de l'enl. 2 (cahier des charges) | 02-187 |

**Synthèse.** Le ciel fournit une **direction + un lieu d'arrivée** (07-152) mais l'auteur refuse le mot « direction » (07-132) et renvoie à « la distance et le point de départ » (07-180). Le « jour dernier » (la date) se **calcule** (pas par le ciel). L'« astre glorieux » n'est nommé nulle part ; les candidats sont **Soleil** (« au matin », « illuminé », « magnifiait », soleil rayonnant de l'enl. 12), **Lune** (« veille » nocturne, croissant de l'enl. 9), **Vénus/Jupiter** (astres demandés, 07-185). Aucune Q/R ne tranche.

---

## 2. Astronomie réelle (tour d'Avalon 45,4288 / 6,03078 ; ephem/PyEphem)

- **Jour dernier = 30/04/1524 (calendrier julien)**. Lever du Soleil (limbe supérieur, horizon plat) : **az 62,8°** à 04:08 UT (≈ 63,7° = « astronomique ») ; au-dessus de l'horizon réel (MNT/RGE) : **az 67,2°** (≈ « visible »). Équinoxe/Pâques 1524 (17/04 julien) : az 68,5° (≈ « plat 68,6° »). En grégorien proleptique (10/05) : az 59,1°.
- **Lune** 30/04/1524 : **croissant décroissant 13 %**, lever az 80,5°, coucher az 283,8°.
- **Lever des astres brillants** (30/04/1524) : Vénus 53,3 · Mars 66,3 · Aldébaran 67,1 · Régulus 68,9 · Altaïr 78,4 · Bételgeuse 79,1 · Procyon 80,4 · Lune 80,5 · Mercure 80,8 · Jupiter 90,9 · Saturne 98,1 · Spica 101,8 · Rigel 102,1 · **Sirius 112,7** · Arcturus 57,5 · Véga 26,5 · Pollux 45,4 · Deneb 6,7.
- **Couchers** : Soleil 296,6 · Lune 283,8 · Vénus 306,9 · Mars 293,9 · Jupiter 269,1 · Saturne 262,0.

**Qui brille au matin du 30/04/1524 ?** Lever du Soleil 04:11 (az 63,6). Présents au lever du Soleil : **Lune** (levée 02:25, az 80,5 ; **croissant décroissant 13 %**, donc visible dans le ciel du matin), **Mars** (04:00, az 66,3 — 11 min avant le Soleil, azimut quasi identique), **Jupiter** (02:28, az 90,9), **Mercure** (03:28, az 80,8), **Saturne** (02:11). **Vénus se lève à 05:42, APRÈS le Soleil → Vénus est ici l'étoile du SOIR, pas du matin** : l'hypothèse « Vénus étoile du matin » est donc incompatible avec le 30/04/1524. Seuls la **Lune** (croissant, enl. 9) et **Mars/Jupiter** (astres demandés, 07-185) sont de vrais candidats « au matin ».

---

## 3. Contrôle terrain (les filtres durs appliqués au rempart = tour d'Avalon)

Filtres : **visible du rempart** (ligne de vue sur **DSM = MNT + MNH**, MNH = hauteur de végétation 0-50 m, **non soustraite**), **public** (cadastre IGN + DGFiP 38 ; « non cadastré » = emprise publique), **bâti ≥ 100 m**, **pente ≤ 18°**, **hors Pontcharra** (Guilhem).

Résultat sur les **1 087 jonctions ≤ 2,6 km** : **3** seulement passent.
- 745 refusées par Pontcharra, 238 par « bâti < 100 m », 44 par pente, 39 privées, 18 invisibles.
- Les 3 : **J16 (45,42684 / 6,03200 ; relèvement 154,1° ; 238 m)**, et deux jonctions NW à 2 119 m (348,9°) et 2 532 m (336,6°).

Sur les points d'**eau** (rayons tous azimuts, water_dist<8 m) : **16 points** qualifiés, sur **3 relèvements seulement** : 24° (404 m, au N), **113–127°** (156–168 m, ruisselet juste au S de la tour, dans le village) et 181° (892 m, au S). Le reste du pourtour est Pontcharra ou bâti.

**Profil des azimuts « productifs »** (≥1 point d'eau qualifié) : **{24°, 113–127°, 181°} = 16 azimuts sur 360 → hasard 4,4 %**.

---

## 4. Règles célestes testées (posées AVANT de regarder) et résultats

| # | Règle | Résultat | Hasard |
|---|---|---|---|
| **R1** | Rayon du **lever du Soleil** (au jour dernier : 62,8 / 63,7 / 68,6 / 73,9° et 67,2° visible) depuis le rempart → eau/jonction qualifiée | **0** : les 5 azimuts célestes sont **hors** de l'ensemble productif | P(az au hasard = 1 point) = 4,4 % → **échec** |
| **R2** | **Première lumière / ombre portée** : point d'eau le plus tôt éclairé par le Soleil du jour dernier | 10/10 points d'eau **dans l'ombre** pour alt ≤ 10° ; seulement à alt 17,3° (az 82,3) 2/10 s'éclairent = le ruisselet à 160 m S de la tour (dans le village) | cause : à 67° le Soleil est derrière la motte de la tour pour tout son secteur visible (W) ; les rayons ENE tombent sur le bâti | 
| **R3** | 3e et 11e = **deux astres** (azimuts de lever) → deux rayons → points d'eau à **1 850 ± 18 m** | 61/171 paires d'astres donnent un couple ; **0** avec les deux points visibles ; **0** avec les deux qualifiés | 21 % des paires d'azimuts **au hasard** donnent un couple → 36 % observé = **1,7× le hasard** |
| **R4** | 3e/11e = **signes du zodiaque** Gémeaux (3e, lever 62,3°) / Verseau (11e, lever 120,7°) | 3 couples à 1 850 m, **tous** les points non qualifiés. Gémeaux 62,3 ≈ Soleil 62,8 (coïncidence d'azimut de lever) | — |
| **R5** | « Le ruisseau magnifié » = **cours d'eau aligné** sur l'azimut du lever (±5°) | 14–17 segments alignés, **tous** refusés (Pontcharra, ou bâti 38–40 m) | 17 % des azimuts **au hasard** donnent ≥1 segment qualifiable → **niveau du hasard** |
| **R6** | 3e/11e à **1 850 m du rempart** sur l'azimut de lever d'un astre (triangle équilatéral 1850-1850-1850) | 21 points d'astres : **tous** refusés (bâti 18–94 m, privé, pente, invisible). 3 paires équilatérales (Vénus+Sirius, Mars+Deneb, Aldébaran+Deneb) : toutes refusées | — |

**Contrôle direct (le plus net).** Parmi les 21 azimuts célestes (19 levers + 2 zodiaque) et les 10 couchers, **un seul** tombe dans l'ensemble productif : **Sirius (lever az 112,7°, dans 113–127°)**. Attendu au hasard = 19 × 0,044 = **0,84** → P(≥1) ≈ 57 %. **Non significatif** : la coïncidence Sirius ↔ le ruisselet à 160 m S de la tour est au niveau du bruit. Aucun coucher ne tombe dans un azimut productif.

---

## 5. Pourquoi les règles célestes échouent ici (explication structurelle)

1. **Géographie du rempart.** La tour d'Avalon est en bord de village (Saint-Maximin), à l'**est** de la vallée. Son **secteur visible** (filtres durs) est minuscule et orienté **SSE (154° = J16) et NNW (337–349°)** pour les jonctions, **N (24°), S (181°)** et **S village (113–127°)** pour l'eau. Les **lever** célestes (E-NE : 53–113°) et les **coucher** (O : 262–307°) ne tombent **jamais** sur ces relèvements.
2. **Le secteur E-NE est bâti.** Les 21 points à 1 850 m sur les azimuts d'astres tombent tous entre 6,050 et 6,054 de longitude, dans une zone à **maisons 18–94 m** et en partie **Pontcharra** → aucun ne passe.
3. **À l'instant du lever, le secteur visible est à l'ombre** (le Soleil az 67° est derrière la motte de la tour) : « illuminé… au matin » n'est cohérent ni avec l'azimut 67° du lever, ni avec un point à 150–900 m visible du rempart.
4. **Le ciel ne peut pas sauver un socle déjà vide.** R0710_C avait déjà montré 0 survivant sur la chaîne complète (toutes jonctions, y compris 1 000 tours fictives). Une **direction** céleste ne peut que **retirer** des points à un socle qui en contient déjà quasi zéro : elle ne peut pas en créer.

**Cohérence avec `PISTES_ECARTEES.md`** : ces tests confirment et chiffrent les entrées « heures solaires 3e/11e », « reflet du Soleil levant sur un ruisseau (Pâques/équinoxe) » et « N1 : 3e sur l'azimut du jour dernier à 1 850 m » → niveau du hasard.

---

## 6. Ce qui n'est PAS invalidé (limites)

- Le **jour dernier = 30/04/1524** (60 %) est supposé, non prouvé ; le script `r0710_S_sky.py` calcule n'importe quelle date.
- Le **départ = tour d'Avalon** (75 %) est supposé. Si le chemin de rempart est ailleurs, tous ces azimuts changent : c'est la variable la plus lourde.
- L'interprétation de « l'astre glorieux » comme **azimut de lever** n'est pas la seule : 07-132/07-180 poussent plutôt vers « le ciel » = le **code des 6 signes de l'enl. 9** (à décoder une fois la zone trouvée, 06-067), pas vers un cap.
- Les filtres (Pontcharra, bâti ≥ 100 m) sont ceux du **coffre** ; appliqués aux 3e/11e intermédiaires ils sont stricts. Même desserrés de « bâti », R1/R2/R5 restent négatifs (les azimuts célestes ne tombent pas sur les relèvements des jonctions/eaux, bâti ou non).

---

## 7. Recommandations

1. **Arrêter** « l'astre glorieux = azimut de lever du Soleil depuis la tour » : incompatible avec le secteur visible et au niveau du hasard.
2. Traiter le ciel comme le **code à 6 signes de l'enl. 9** (07-134/07-198, « un seul élément » FAQ8), c.-à-d. un **confirmateur de fin de jeu** (06-067), pas un pointeur depuis le rempart — cohérent avec 07-132 (« pas de direction en tant que telle »).
3. Si le ciel doit **placer** les 3e/11e, il faut d'abord **changer le point de départ** (ou le confirmer) ; le rempart-tour d'Avalon ne laisse qu'un socle de 3 jonctions / 16 points d'eau, aucun aligné sur un astre.
4. Test indépendant suggéré : reprendre la **Lune** (croissant décroissant 13 % du 30/04/1524, coucher az 283,8°) comme « veille » lumineuse, ou **Sirius** (« l'étoile » de l'enl. 9), mais **avec un autre rempart**, car depuis la tour aucun ne donne de point qualifié.

---

## 8. Faits vérifiables (chemins)

- Scripts : `outils_scratch/r0710_S_sky.py` (éphémérides), `r0710_S_geo.py` (horizon réel, rayons, `los_ok` sur DSM=MNT+MNH), `r0710_S_rules.py` (filtres, jonctions/eau), `r0710_S_profil.py`, `r0710_S_water.py`, `r0710_S_rules2.py` (R2/R3/R4/R5), `r0710_S_hasard.py`, `r0710_S_carte.py`.
- Données : `donnees_travail/r0710_S_sky.json`, `r0710_S_prof_water.npy`, `r0710_S_water.json`, `r0710_S_okj.json`, `r0710_S_prof.npy`, `r0710_S_hasard.json`.
- Cartes : `images_travail/r0710_S_carte.jpg` (3 km), `r0710_S_zoom.jpg` (1,2 km).
