# T1 notes
## REPRISE
- Fait : lecture du brief ; T1a recadrage enluminure 9 (images de travail t1_*.jpg dans scratch/exk_e12, rotation -90° PIL = sens correct)
- En cours : tâche 1 (bassin enluminure 9)
- Prochaines : 2 clairière, 3 toponymes, 4 fort Barraux, 5 rapport+KML
- Écarté : rien

### T1a BASSIN (fait) — scripts T1_bassin.py (v1 masque couleur), T1_bassin2.py (v2 tracé manuel), sortie T1_bassin.out.txt, planche T1_bassin_planche.png, scores T1_bassin_scores.json
- FAIT : contour peint = blob arrondi, allongé (rapport axes 0,58), pointe émoussée à gauche, lobe large à droite, léger creux en haut où tombe le ruisseau (cascade depuis la roche rayonnante) ; 2 poissons ; cygnes sur le lac à l'arrière-plan (pas dans l'étang). Horizon : muraille orange crénelée à tours + arcades, petit bâtiment blanc sur butte, montagnes roses.
- RESULTAT : 62 surfaces d'eau IGN <6 km ; IoU max 0,88 mais 18/62 >= 0,80 -> non discriminant. Étangs du Maupas 0,83 ; Bassin du Cheylas 0,60 ; Lônes 0,48. AUCUNE ressemblance forte. Confiance en « pas d'identification » : haute.

### T1b CLAIRIÈRE + T1d FORT (fait) — T1_clairiere.py, sorties T1_clairiere.out.txt (tour), T1_clairiere_fort.out.txt (fort, recalé sur 45.4358,5.98723 ; la 1re passe utilisait un point faux), T1_tour_jonctions.json, T1_fort_jonctions.json
- Tour : 217 jonctions>=3 branches <2,5 km ; trouée 2 ; eau<=150 m 101 ; domaine public (forêt communale) 21 ; vue terrain-seul 57 ; versant E 3 ; trouée+eau 2 ; 4 filtres ensemble : 0.
### T1c TOPONYMES (fait) — T1_toponymes.py/.out.txt/.json (BD TOPO + cadastre 17 communes)

### T1e LIVRABLES (fait) — T1_livrables.py -> T1_candidats.kml (dont ~40 placemarks), T1_rapport.md
## TERMINÉ
- Écarté : bassin par la forme (non discriminant) ; toutes jonctions tour (0/217 à 5 filtres) ; fort Barraux (0 trouée) = vivant, non favori ; toponymes du ciel : rien sauf Tire-Loup (faible).
- Pistes vivantes : T05 (45.41512,6.02803, Perrière), flanc ouest du fort (F01-F04), arrière-plan paysager de l'enluminure 9, LiDAR HD à faire.

### REPRISE 2 (30/09) : vérification livrables OK (KML valide, 1 Placemark par ligne mais fichier conforme) ; ajout section 4b rapport (tâche 4 : Wikipedia fr, tour/château/fort). Rien d'autre à refaire.
