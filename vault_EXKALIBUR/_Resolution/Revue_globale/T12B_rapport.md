# T12B_rapport.md — Piste T12-B : Machrie Moor ↔ enluminure 11 (3e/11e)

**Id : T12B. Date : 01/10/2026. Nature : géographie + lecture d'énigme.**
Préfixe de sortie : `T12B_*` dans `Revue_globale/`. Scripts archivés : `T12B_machrie.py` (+ `.out.txt`), `T12B_nombres.py`.

---

## 1. Ce qui est FAIT (géographique, vérifié)

**Coordonnées des sites de Machrie Moor (île d'Arran), d'après Wikipédia/HES.**
La grille NGR `NR…` est autoritaire (liens streetmap de Wikipédia) ; les coordonnées WGS84 ci-dessous sont obtenues par ancrage sur le point officiel geohack (OSTN15) `NR 9102 3244 = 55.540829, −5.313655`, puis décalage local exact (erreur < 2 m sur 2,4 km).

| Site | NGR | WGS84 (lat, lon) | Description (HES/Wikipédia) |
|---|---|---|---|
| MM1 | NR 9120 3239 | 55.540334, −5.310845 | cercle 1 : 6 granites + 5 grès = **11 pierres** |
| MM2 | NR 9114 3241 | 55.540514, −5.311797 | cercle 2 : 3 dalles debout (3,7–4,9 m), 13,7 m Ø |
| MM3 | NR 9102 3244 | 55.540784, −5.313703 | cercle 3 : **9 pierres, 1 seule debout** (pierre) |
| MM4 | NR 9100 3235 | 55.539974, −5.314020 | cercle 4 : **4 blocs** de granite |
| MM5 | NR 9087 3234 | 55.539884, −5.316084 | Fingal's Cauldron Seat : **8 + 15 = 23 granites** |
| MM6 | NR 9073 3237 | 55.540154, −5.318307 | cairn chambré (2 dalles) |
| MM7 | NR 9063 3253 | 55.541594, −5.319894 | pierre levée 1,6 m |
| MM8 | NR 9057 3237 | 55.540154, −5.320847 | cairn chambré (pierre 1,8 m) |
| MM9 | NR 9053 3240 | 55.540424, −5.321958 | pierre levée (disparue) |
| MM10 | NR 9006 3265 | 55.542673, −5.328944 | Moss Farm Road : cairn, **23 m Ø, 7 + 5 = 12 pierres** |
| MM11 | NR 9121 3242 | 55.540604, −5.310686 | cercle 11 : **10 pierres + trous de POTEAUX (BOIS)** |
| MM12 | NR 9100 3240 | 55.540424, −5.314020 | cercle 12 (2025, enfoui) : **12 fosses** |
| Ballymichael | NR 9244 3225 | 55.539075, −5.291158 | 3 blocs (4 à l'origine), ~1,2 km E |

> ⚠️ Les colonnes « lat,lon » de `T12B_machrie.out.txt` sont **FAUSSES** (bug de conversion dans le script initial). Les **distances et caps** y sont **EXACTS** (mètres de grille). Référence autoritaire = les NGR ci-dessus.

**Distances-clés (mètres de grille, exacts à <0,1 %) :**
- **MM3 ↔ MM11 = 191 m ≈ 1 stade** (pas 10 stades).
- MM1↔MM3 = 187 m ; MM3↔MM5 = 180 m ; MM5↔MM1 = 334 m.
- **Aucune paire de sites MM à 1 850 m (±1 %).** Emprise totale ~2,4 km (MM10 → Ballymichael).
- MM7↔Ballymichael = 1 830 m et MM8↔Ballymichael = 1 872 m **encadrent** 1 850 m, mais Ballymichael est un ref à 6 chiffres (±50 m) et n'est ni « 3e » ni « 11e ».

**Comptages de pierres (série numérotée 1–12, Bryce 1861 + MM11 1978 + MM12 2025) :**
MM1=11, MM2=3, MM3=9, MM4=4, MM5=23, MM6=2, MM7=1, MM8=1, MM9=1, MM10=12, MM11=10, MM12=12 ; + Ballymichael (non numéroté) = 13e site de la zone.

---

## 2. FAITS FAQ8 (verbatim, `scratch/faq8.txt`)

- « l'endroit sur l'île au sud dans Omnia peut nous aider à décoder l'enluminure onze ? → **Oui, tout à fait.** » (~char 43694)
- « Peut-on prendre l'enluminure onze comme carte rudimentaire ? → **Oui.** » (~char 73197)
- « l'endroit utile sur cette île = **uniquement un point** [Maps], mais en zoomant vous découvrez **plus que simplement un élément**. » (~char 5589)
- « compte-les : compter *elle* ou elle + les fiers aïeux ? → **Elle.** » (~char 55135) ; « le compte-les vous sert **autrement** » (ni distance É10, ni É11) (~char 12147).
- lecture horaire E11 : « pique, puis cinq, puis trois, puis cœur — **ça n'a pas d'importance** » (l'ordre des pierres ne compte pas) (~char 12465).
- « 3e/11e auraient pu être 8e/16e ? → **Non, sinon incorrect.** » (~char 43694).
- boussole de la CARTE n'aide **pas** à localiser 3e/11e (~char 52409) ; l'essai non plus (~char 25830).
- « liste universelle (mois/apôtres/zodiaque) ? » NRP ; « matériaux différents ? » NRP ; « texte de 1 500 ans ? » NRP.

---

## 3. Résultats des 5 tests demandés

**(1) Disposition Machrie Moor vs enluminure 11 (cercle/croix).**
Le site réel = un **amas de cercles à l'Est** (MM1–5, 11, 12 dans ~340 × 100 m) + une **ligne de monuments vers l'Ouest** (MM6–10 sur ~1 km). Aucune structure en « croix » ni 4 pierres disposées en cercle/croix identifiable à cette échelle. La « croix » de l'enluminure (chemin de pierres en croix + 4 symboles dans les 4 quadrants) **ne se superpose pas** à la disposition réelle des cercles. → La « carte rudimentaire » n'est **pas une carte topographique** de Machrie Moor ; c'est un **schéma de numérotation**.

**(2) Chiffres 1, 3, 5, ? → cercles MM1/MM3/MM5/MM?.**
Triangle MM1–MM3–MM5 : côtés 187/180/334 m, angles 24,1°/130,8°/25,1°. Aucun ne redonne 1 850 m, 64,99°, 72,09°, ni un rang utile. Caps « coïncidant » (MM4→MM11 = 71,57° ≈ 72,09° ; MM5→MM12 = 65,22° ≈ 64,99°) = **niveau du hasard** (156 caps testés, fenêtre ±0,6° → ~0,5 occurrence attendue par cible). **Réfuté.**

**(3) D=500, C=100, X=10 (romains) et cartes (valet=11, dame=12, roi=13).**
D+C+X = 610. 610 vs 606,74 km (É11, D·π) = 0,54 % d'écart ; vs 607,69 km = 0,38 %. Hors sujet É12 (qui veut 1 850 m, pas la distance É11). Lecture cartes : D=Dame=12, C=Cavalier, X=10 (dix) → suite possible 12, 11, 10, 9. **Aucun nombre de Machrie Moor** (23, 11, 10, 9, 4, 12) ne se raccorde proprement à 1 850 via D/C/X. **Non concluant.**

**(4) Série numérotée ≥ 13 sur Arran (3e/11e à 1 850 m).**
La seule série numérotée canonique est **Machrie Moor 1–12** (Bryce 1861 : 1–5 cercles, 6–10 autres monuments ; MM11 en 1978 ; MM12 en 2025). Il n'existe **pas de MM13** ; Ballymichael (site HES NR93SW 16) est le 13e site de la zone mais non numéroté. **Aucune paire 3e/11e à 1 850 m** dans cette série ni dans aucun ordre géographique (O→E, S→N) testé. Les autres sites d'Arran (Auchagallon, Torrylin, Giant's Graves…) ne forment pas de série numérotée 1–13. **Réfuté comme source directe de 1 850 m.**

**(5) Témoins (contrôle du hasard).**
Toutes les coïncidences numériques ci-dessus ont été comparées à un témoin : caps sur 156 paires (hasard ≈ 0,5), paires à 1 850 m (aucune sur 78 paires), sommes/produits arbitraires (rejetés). **Rien ne dépasse le bruit.**

---

## 4. Conclusion

**Hypothèse « 3e/11e = MM3/MM11 pris tels quels » : RÉFUTÉE** par la distance (191 m = 1 stade, pas 10 stades = 1 850 m), conformément au flag « échelle » déjà posé.

**Mais la prémisse Machrie Moor → enluminure 11 est CONFIRMÉE par FAQ8**, et un signal spécifique survit :

> **Le match « écharde / bois » est fort.** FAQ07-068 : pas d'écharde sur la 3e, « oui c'est possible » sur le 11e. Or **MM11 = 10 pierres + trous de poteaux en BOIS** (cercle de pierre posé sur un cercle de bois), **MM3 = pierres seules, 1 debout**. C'est une correspondance exacte, non triviale, entre « le onzième est en bois / le troisième est en pierre » et les cercles n° 11 / n° 3 de Machrie Moor.

**Lecture retenue :** Machrie Moor fournit le **principe de la série numérotée** (des objets posés au sol, numérotés 1–13+, dont le 11e est en bois et le 3e en pierre), et l'enluminure 11 (« carte rudimentaire », chiffres 1, 3, 5, ?) en est le **gabarit** — mais les **3e/11e réels sont au site final** (Grésivaudan), séparés de 1 850 m, **pas à Machrie Moor**. Le « compte-les » d'É10 (le nombre de pierres, « elle » seule, utilisé « autrement » en É12) est la quantité qui relie les deux.

---

## 5. Deux lectures les plus prometteuses pour la vague suivante

**A. « 3e/11e » = éléments 3 et 11 d'une série numérotée ≥ 13 au site final, le 11e en BOIS, le 3e en PIERRE, distants de 1 850 m.**
- Indices alignés : FAQ07-068 (écharde/bois), FAQ06-133 (« le 13e ne mène pas au bon endroit »), FAQ06-009 (même nature), FAQ06-247 (« marcher surtout sur l'un des deux » → le chemin/élément en bois ?), FAQ05-074 (pas visibles sur Maps).
- À tester au Grésivaudan : stations d'un chemin de croix (14 ; la 11e = crucifixion/cloué sur la croix en BOIS, la 3e = 1re chute, pierre), bornes numérotées, poteaux/planches (bois) vs pierres. C'est la piste déjà la plus cohérente de `Enigme_12/solution.md` ; **T12-B la renforce** en la rattachant au gabarit Machrie Moor.

**B. Le « ? » de l'enluminure 11 = 11 (pas 7).**
- Les chiffres 1, 3, 5, ? se complètent en **1, 3, 5, 11** (les cercles impairs MM1, MM3, MM5, MM11), et non en suite impaire 1,3,5,7. Le « ? » (pierre ♦, quadrant bas-droit) désigne alors directement **l'onzième** de l'É12. Corollaire : la « 3e » (pierre ♥, chiffre 3) et la « onzième » (pierre ♦, « ? »=11) sont **deux des quatre pierres de l'enluminure** — donc l'enluminure place bien « une partie » des 3e/11e (FAQ07-239). À croiser avec la rose des vents I→VIII (« orientez-vous ») pour lever l'ambiguïté 7 vs 11.
