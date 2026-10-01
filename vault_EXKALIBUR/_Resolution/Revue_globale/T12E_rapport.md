# T12E — Rapport : le point de départ n'est peut-être pas la Tour d'Avalon

**Id : T12E** — 01/10/2026. Méthode : géométrie (haversine/bearing), BAN (api-adresse), Overpass (kumi.systems), Wikipédia, réutilisation du pipeline T12C (viewshed + croisements LiDAR/BD TOPO/OSM).

## Réponse courte
Le « chemin de rempart » de l'É12 est, avec la meilleure confiance, la **« Rue du Rempart » de Saint-Maximin (Isère)** — une voie publique officielle (FANTOIR `384261360C`, confirmée BAN) qui longe le pied de la **Tour d'Avalon**, l'unique rue *nommée* « rempart » dans toute la zone de tolérance. La piste est **partiellement confirmée** : le départ n'est pas *la tour elle-même* (MH 1992, visite limitée juil.–août), mais la *rue* du rempart, accessible toute l'année — au **même endroit** (Saint-Maximin), pas à Barraux/Montmélian/Arvillard/Yenne.

## Fait central (nouveau, non vu en vague 1)
- OSM/Overpass + BAN révèlent une **« Rue du Rempart »** à Saint-Maximin (3 segments contigus, `highway=residential`, `ref:FR:FANTOIR=384261360C`), centrée sur **45.4295 N, 6.0312 E** — soit **1,16 km** de l'arrivée exacte de l'É11 (45.42418, 6.01790), cap 64,97°, D=607,9 km depuis Saint-Palais.
- C'est la **seule** voie nommée « rempart » dans le couloir 62-68°/600-614 km à moins de 6 km (tolérance 1 % ≈ 6 km). Les autres : Arvillard (8,1 km), Montmélian (9,2 km), Yenne (37 km).
- La solution.md de vague 1 affirmait « aucun chemin de rempart cartographié (IGN/OSM) » : c'était **faux** — OSM a bien « Rue du Rempart » (la recherche IGN BD TOPO ne la trouvait pas).

## Géométrie (T12E_01)
- Saint-Palais (43.3291, -1.0347) → arrivée É11 = **606,74 km, cap 64,99°** (≈ château Bayard, 45.4242/6.0179).
- Couloir « cap 62-68° » = **63,5 km de large** à 607 km ; l'axe (cap ~65°) reste le vrai filtre, la tolérance réelle est ~1 % ≈ **6 km** (FAQ8 « on reste dans les ordres de grandeur »).
- Tour d'Avalon = 607,87 km (cap 64,97°), +1,13 km au-delà de l'arrivée = « dépasser très finement » (FAQ07-256).

## Classement des départs (confiance honnête)

| # | Départ | Offset/É11 | D(SP) km / cap° | « chemin de rempart » réel | Lien Bayard | Lien Avalon/Lincoln | Confiance |
|---|---|---|---|---|---|---|---|
| 1 | **Rue du Rempart, Saint-Maximin** (45.4295, 6.0312) | **1,16 km** | 607,9 / 64,97 | OUI — rue publique, FANTOIR `384261360C`, BAN, accessible toute l'année | indirect (1,1 km au-delà du château Bayard, « dépasser finement ») | **fort** : au pied de la Tour d'Avalon = château d'Avalon, naissance de Hugues d'Avalon (évêque de Lincoln) → « portes d'Avalon » | **HAUTE (0,7)** |
| 2 | Tour d'Avalon (45.4289, 6.0310) | 1,15 km | 607,9 / 64,98 | « chemin d'une tour » (FAQ8) ; tour 33 m, 1895, MH 1992, visite juil.–août seulement | indirect | **fort** (même lieu que #1) | MOYENNE (0,6) — même site, mais accès limité |
| 3 | Château Bayard (45.4235, 6.0186) | 0,10 km | 606,8 / 65,00 | NON (propriété privée, aucune voie « rempart ») | **fort** (naissance de Bayard) | nul | FAIBLE (0,2) comme *rempart* ; HAUTE comme *arrivée É11* |
| 4 | Fort Barraux (45.4356, 5.9871) | 2,70 km | 604,9 / 64,80 | remparts réels (fort bastionné 1597, Classé MH, visitable assoc.) mais **pas de rue « rempart »**, chemin de ronde interne | **nul** (1597 > †1524) | nul | FAIBLE (0,25) |
| 5 | Rue des Remparts Arvillard | 8,05 km | 614,8 / 65,06 | rue « Remparts » réelle | nul | nul | TRÈS FAIBLE (<0,1) |
| 6 | Rue des Remparts Montmélian (citadelle) | 9,19 km | 612,7 / 64,33 | rue « Remparts » + citadelle | nul | nul | TRÈS FAIBLE (<0,1) |
| 7 | Chemin de Ronde Yenne | 37 km | 599,5 / 61,5 | rue « Ronde » | nul | nul | TRÈS FAIBLE (<0,1) |
| — | Chemin/Impasse « Pré de Ronde » (Chapareillan, 3,2-3,4 km) | 3,2 km | 603,5 / 65,0 | FAUX POSITIF : « Pré de Ronde » = nom de pré, pas un chemin de ronde | nul | nul | ÉCARTÉ |

## Critère « l'arrivée est le lieu découvert grâce au dernier chevalier » (FAQ8)
FAQ8 verbatim : « Vous arriviez au lieu qui a été découvert grâce au dernier chevalier. » → l'arrivée est le lieu **atteint grâce à Bayard** (angle suivi depuis Montsalvage), pas un lieu *propre* à Bayard. L'É11 (Saint-Palais × π = 606,74 km) tombe ~50 m du **château Bayard** (naissance de Bayard) ; le « chemin de rempart » est 1,1 km plus loin, couvert par la tolérance 1 % et par « si vous le dépassez, ce sera très finement ». **Cohérent** : Bayard → château Bayard (arrivée), puis rue du Rempart / Tour d'Avalon (départ É12).

## Test de cohérence É12 (réutilise T12C_01/02) — candidat n°1
- Viewshed depuis la Rue du Rempart (proxy D2 pied de tour) : **48** croisements visibles ; **1 seul** passe tous les filtres bureau (d_eau≤150 m, clairière, d_bât≥150 m, ≤2 km) : `BDTOPO:deg3` à 1 405 m, **cap 218° (SO, dos au soleil)** → échoue « éclairé le matin ».
- Seul ruisseau nommé aligné vers le levant : **Ruisseau de Tapon** (NE). Son franchissement « **Les Ripellets** » (45.4338, 6.0502) est une jonction OSM **en clairière à 8 m du Tapon, cap 70,9°** (≈ soleil du matin), visible depuis le rempart — **mais à 8 m d'un bâtiment** et non significatif (témoins aléatoires : 12-21 croisements équivalents, médiane 17).
- Conclusion : **plafond « bureau » atteint** (comme T12C). Aucune boîte de 50 m n'est justifiée par les données ; « Les Ripellets/Tapon » est au mieux une piste terrain faible à vérifier sur place.

## Fichiers créés
- `T12E_notes.md`, `T12E_rapport.md`, `T12E_01_geometrie.py/.json`, `T12E_02_overpass.py/.json`, `T12E_03_coherence.py`.

## Limites / à faire
- Fort Barraux est hors de la tuile MNT locale (lon 5,987 < 6,005) : pas de viewshed LiDAR fait (nécessiterait WCS IGN LiDAR HD) — non prioritaire car candidat faible.
- Ambiguïté résiduelle : « chemin de rempart » = rue *nommée* « Rempart » vs *chemin de ronde* physique sur mur/tour. Les deux lectures convergent sur Saint-Maximin / Tour d'Avalon.
