# R0610 — N1 « 3e = étape intermédiaire, 11e = destination finale » : test inverse + hasard

**Date** : 06/10/2026 · **Sous-agent** : test de la piste N1 (00_PISTES_VIVANTES.md, §4)
**Script** : `outils_scratch/r0610_n1_inverse.py` · **Images** : `images_travail/r0610_N1_couvet.jpg` (orthophoto IGN) et `r0610_N1_couvet_annot.jpg`

## Règle posée AVANT de regarder le terrain

- La 3e est une étape intermédiaire **non boisée** (pierre, marchable pieds nus), le **11e est la destination finale** (clairière boisée), distants de 1 850 m ±18 m.
- La 3e est **placée depuis le rempart par le ciel** : elle est sur l'un des trois azimuts du jour dernier (30/04/1524 → **63,7° / 68,6° / 73,9°**) depuis la tour d'Avalon (45.4288, 6.03078).
- Géométrie vérifiée : la 3e = intersection du rayon (tour, azimut) avec le cercle (11e, 1 850 m). Les six points fournis sont reproduits à ±3 m près.

## Mission 1 — ce qu'il y a dans 60 m des six points 3e

Les six points tombent dans le secteur **Couvat/Couvet** (hameau du Couvat, à l'ouest du Couvet), terrain **agricole ouvert** (orthophoto IGN : champs/pâtures, pas de forêt) — « non boisé » est donc trivialement satisfait partout, sans valeur discriminante.

| Point 3e (zone, azimut) | Coordonnées | Dans 60 m |
|---|---|---|
| J16 @ 63,7° | 45.43607, 6.05174 | **rien** (ni carrefour, ni objet) |
| J16 @ 68,6° | 45.43485, 6.05278 | 3 carrefours routiers (31/42/43 m), bâti à 64–85 m |
| J16 @ 73,9° | 45.43345, 6.05376 | 1 carrefour (44 m), bâti à 64 m ; panneau « Le Couvat » à 65 m |
| Le Mouret @ 63,7° | 45.43650, 6.05298 | **rien** |
| Le Mouret @ 68,6° | 45.43547, 6.05503 | **rien** (plein champ cultivé) |
| Le Mouret @ 73,9° | 45.43414, 6.05715 | **rien** ; « Le Couvat et Charret » à 119 m, Burge à 160 m |

**Aucun pont, gué, dalle, croix, roche, source ni lieu-dit à ≤ 60 m d'aucun des six points.** Les seuls « objets » sont des carrefours routiers ordinaires du hameau du Couvat (service/tertiary/Chemin), à 64–85 m de bâtiments — cohérent avec la remarque déjà consignée « hameau du Couvat, maisons à 32 m » (PISTES_ECARTEES, ligne 50). Il n'y a **aucune pierre/dalle** (la 3e est censée être « pierre »).

## Mission 2 — règle inverse (sans présupposer J16/Mouret)

Sur les **595 croisements visibles du rempart** (t16 `vis=true`), 1 094 points 3e calculables (croisement × 3 azimuts) :

- **≥ 1 carrefour à ≤ 60 m : 471/1 094 = 43,1 %** — tomber sur un carrefour est banal (réseau routier dense) ;
- **≥ 1 objet ponctuel remarquable (pont/gué/croix/roche/lieu-dit/panneau) à ≤ 60 m : 145/1 094 = 13,3 %** — et ces 145 touchent surtout la « Tour d'Avalon » elle-même, des lieux-dits et panneaux d'information génériques.

Rien ne singularise J16 ni Le Mouret : les six points calculés pour elles sont **plus vides** que la moyenne (2/6 carrefours, 0/6 objet ponctuel).

## Mission 3 — test du hasard (1 000 azimuts tirés au sort, mêmes deux zones)

- Réel (6 points) : **4 carrefours** au total (3+1+0+0+0+0), et **0 objet remarquable**.
- Hasard (1 000 tirages × 2 zones) : moyenne **2,34** carrefours, médiane 2, percentile 98 = 9.
- **La fraction du hasard qui égale ou dépasse le réel (4 carrefours) = 25,7 %** — très au-dessus du seuil ≤ 2 % (ou 5 %).
- Taux de base « ≥ 1 carrefour au point 3e » : J16 42 %, Le Mouret 49 % — les 3 azimuts « jour dernier » ne font **pas mieux** que des azimuts aléatoires (Le Mouret fait 0/3, soit *moins* bien).

## Verdict

**RIEN (piste faible).** La lecture « 3e = étape intermédiaire non boisée placée sur l'azimut du jour dernier à 1 850 m du 11e » ne produit **aucun objet remarquable** (pont/gué/dalle/croix/roche/pierre) aux six points : 4/6 sont vides, 2/6 tombent sur des carrefours routiers ordinaires du hameau du Couvat. Le signal (4 carrefours) est **dans le bruit** (25,7 % du hasard, seuil ≤ 2 %). La règle inverse confirme que « tomber sur un carrefour » à 1 850 m sur un azimut quelconque est banal (43 %).

## Faits les plus importants

1. Les six points 3e sont tous en terrain **agricole ouvert** du Couvat/Couvet ; aucun pont, gué, dalle, croix, roche, source ni lieu-dit à ≤ 60 m.
2. Les seuls « objets » (2/6 points) sont des **carrefours routiers** du hameau, à 64–85 m de bâtiments — et non une « pierre ».
3. Test du hasard : le score réel (4 carrefours) est atteint ou dépassé par **25,7 %** des azimuts aléatoires (moyenne 2,34) → au niveau du bruit.

## À tester ensuite

- **Abandonner N1** comme mécanisme de placement de la 3e (consigner dans PISTES_ECARTEES).
- Prioriser **N2** : « des éléments physiques de même nature liés aux écrits du narrateur » (FAQ07-030) — c'est l'indice textuel le plus fort sur la *nature* des 3e/11e ; la nature (pas la position) reste l'inconnue.
- Ne pas relancer Le Couvet comme « 3e » : il ne ressort ni du crible strict (maisons à 45 m) ni de cette lecture.
