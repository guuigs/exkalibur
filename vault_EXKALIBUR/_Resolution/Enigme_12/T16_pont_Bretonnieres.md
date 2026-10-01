---
tags:
  - "#exkalibur"
---
# É12 — Pont des Bretonnières (piste de Guilhem, 01/10/2026)

Pont des Bretonnières : 45.439475, 6.053043 (Google Maps), sur le Bréda, chemin rural. Scripts : `exk_e12/T16_breda_ponts.py` (OSM) et `T16b_breda_bdtopo.py` (BD TOPO), avec leurs sorties `.out.txt`.

| Mesure (haversine) | Valeur | Écart à 1 850 m |
|---|---|---|
| depuis la tour d'Avalon | 2 085 m, cap 56,3° | +12,7 % |
| depuis la Rue du Rempart | 2 019 m, cap 57,7° | +9,1 % |
| depuis le lieu-dit « avalon » | 1 942 m | +5,0 % |
| depuis l'église de Saint-Maximin | 1 747 m | −5,6 % |

Tolérance de l'auteur ≈ 1 % (1 832-1 868 m) : **aucune de ces mesures n'est dans la fenêtre.**

**Rang sur le Bréda depuis l'Isère** : 10e pont (BD TOPO) ; 11e si l'on compte le barrage (OSM : 12e avec un tracé de LGV en projet). Le compte dépend de la source et de la règle (barrages, seuils, projets), donc on ne peut pas en tirer un « onzième » solide. Les 3e et 11e ponts depuis l'embouchure sont à 2,2-5,7 km l'un de l'autre, pas à 1 850 m.

**À 1 850 ±18 m du pont** : le pont du Chemin de Combe Forêt (1 849 m) et un pont de piste (1 834 m). Avec ≈ 3,4 ponts/km² dans le secteur, on en attend environ 1,4 par hasard dans cet anneau : ce n'est pas un signal.

**Visibilité** : le pont n'est pas visible depuis le sommet de la tour (relief qui masque de ≈ 20 m d'après le LiDAR).

**Verdict** : la piste est gardée comme repère (vue vers l'est-nord-est, cap ≈ 56-58°, proche du lever du soleil de mai), mais elle n'est pas validée. Ni la distance ni le rang ne tombent juste.

## Variante de Guilhem (01/10) : 11e = un pont du Bréda, 3e = autre chose plus près d'Avalon
Script `exk_e12/T17_onzieme_pont.py` (+ `.out.txt`). Toutes classes BD TOPO + OSM, cherchées à 1 850 ±18 m du 11e candidat et à ≤ 800 m de la tour.

| 11e candidat | Distance à la tour | Objets à 1 850 m près d'Avalon | Attendu par hasard |
|---|---|---|---|
| Pont des Bretonnières | 2 085 m | 2 (réservoir couvert, banc, ~680 m au nord de la tour) | 6,4 |
| Pont du barrage (pont isolé) | 973 m | 0 (l'anneau ne passe pas près de la tour) | 0 |
| Barrage | 1 023 m | 0 | 0 |

- Autour du Pont des Bretonnières, l'anneau de 1 850 m passe à **235 m de la tour, en plein marais/étang d'Avalon** (nœud « Le Vivier » à 1 875 m, point d'eau à 1 873 m). Mais c'est mécanique : la tour est à 2 085 m, donc l'anneau traverse forcément le secteur. Un marais étendu contient toujours un point à 1 850 m. **Pas un signal.**
- Pont du barrage ou barrage comme 11e : à moins de 1 km de la tour, un 3e à 1 850 m serait de l'autre côté, à plus de 870 m d'Avalon. Il ne serait donc pas « près d'Avalon ».
- Contrainte officielle : 3e et 11e de **même nature** (FAQ06-009). Si le 11e est un pont, le 3e est un pont. Aucun pont à 1 850 ±18 m du Pont des Bretonnières dans un rayon de 3,8 km autour de la tour.
- Écharde : pas de matériau renseigné dans OSM ni dans la BD TOPO pour ces ponts. À vérifier sur photo (Street View / sur place).

**Verdict** : non concluant. L'idée « 3e et 11e de nature différente » reste contredite par FAQ06-009.
