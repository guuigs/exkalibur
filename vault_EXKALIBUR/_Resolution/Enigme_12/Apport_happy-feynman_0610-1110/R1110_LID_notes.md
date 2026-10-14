# R1110_LID — notes
## REPRISE
- Fait (11/10) : étapes 1-4 complètes. Rapport : `R1110_LID_rapport.md`. Scripts `outils_scratch/r1110_lid_01…09` (+08b), données `donnees_travail/r1110_LID/`, ortho `images_travail/r1110_LID/`.
  - Étape 1 : classifieur MNT/MNH ; rappel BD TOPO en forêt 76,5 % (5 m) / 86,8 % (8 m) en validation (blocs damier) ; réseau dense, spécificité faible.
  - Étape 2 : 15 106 jonctions (>=3 branches), 2 860 retenues dans 2,5 km (bâti >= 80 m).
  - Étapes 3-4 : score 0-6, 1 000 tours fictives : au niveau du hasard. RIEN de fiable.
- En cours : rien.
- Prochaines étapes : durcir C2 + jonctions de chemins forestiers seulement (fixé avant), refaire le test ; nuage de points LiDAR HD (classe sol) pour chemins sous couvert.
- Écarté : réseau LiDAR seuil 0,5 (trop dense) ; sensibilité « connu seul » rang 3 p=0,009 = post hoc, non fiable.
Corrections de Guilhem appliquées : Pontcharra exclue seulement par distance au bâti (>= 80 m) ; réseau fusionné BD TOPO+OSM+LiDAR.
