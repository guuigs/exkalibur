"""Solveur B / É6 — test du hasard, version analytique (aucun réseau). Question : « Tour -> Battle -> Sainte-Chapelle alignés à 0,42 km » est-il discriminant ?
Idée : Battle est à 76,7 km de la Tour ; un point de Paris à 342 km. Un décalage latéral de L km du point d'arrivée fait dévier la droite de L*76,7/342 km à Battle
(facteur 0,224). Toute la zone urbaine de Paris (~10 km de large) produit donc un décalage latéral < ~1,2 km à Battle : Battle est 'sur l'axe' de TOUT Paris.
On le mesure : grille de points dans Paris intra-muros (boîte 48,815-48,902 N ; 2,224-2,470 E), écart de Battle à la droite Tour->point.
Ensuite : proba qu'un axe Tour->Battle prolongé touche une cible ponctuelle."""
import sys, math
import numpy as np
sys.path.insert(0, "."); from solveurB_geo import *
T = (51.5081124, -0.0759493)
BATTLES = {"Battle Abbey (Wikipedia 50.915, 0.4858)": (50.915, 0.4858), "Battle ville (Wikipedia 50.92, 0.48)": (50.92, 0.48), "geo_e6.py (50.9143, 0.487)": (50.9143, 0.487), "Hastings ville (carte Guilhem)": (50.854259, 0.573453)}
la = np.linspace(48.815, 48.902, 88); lo = np.linspace(2.224, 2.470, 124)
print("== Écart latéral de Battle à la droite Tour->P, P dans Paris intra-muros (grille ~1 km)")
for nm, B in BATTLES.items():
    v = np.array([xtrack(T, (a, b), B) for a in la for b in lo])
    print(f"{nm:44s} |écart| <=0,42 km : {100*np.mean(abs(v)<=0.42):5.1f} % de Paris ; <=1 km : {100*np.mean(abs(v)<=1):5.1f} % ; <=2 km : {100*np.mean(abs(v)<=2):5.1f} % ; médiane {np.median(abs(v)):.2f} km ; max {abs(v).max():.2f}")
SC = (48.855375, 2.3449609)
print("\n== Écarts pour points de Paris nommés (Battle Abbey Wikipedia)")
B = BATTLES["Battle Abbey (Wikipedia 50.915, 0.4858)"]
for nm, P in {"Sainte-Chapelle (carte Guilhem)": SC, "Notre-Dame": (48.8530, 2.3499), "Sacré-Cœur": (48.8867, 2.3431), "Tour Eiffel": (48.8584, 2.2945), "Panthéon": (48.8462, 2.3464), "Sorbonne": (48.8487, 2.3436), "Saint-Denis basilique": (48.9356, 2.3597), "Vincennes (Ste-Chapelle)": (48.8423, 2.4364), "Sainte-Clotilde": (48.8558, 2.3187)}.items():
    print(f"{nm:34s} d(T,P)={hav(T,P):7.2f}  écart de Battle à T-P : {xtrack(T,P,B):+6.2f} km ; écart de P à l'axe T-Battle : {xtrack(T,B,P):+6.2f} km")
print("\n== Probabilité qu'un cap au hasard passe à <= w km d'une cible ponctuelle à d=341,6 km")
for w in (0.42, 1.0, 2.0):
    print(f"   w={w} km : cap uniforme 360° : {100*2*w/(2*math.pi*341.6):.3f} % ; secteur France plausible 100° : {100*2*w/(math.radians(100)*341.6):.3f} %")
print("\n== Sensibilité au géocodage de Battle : Battle 'Abbey' = 50,9143/0,4870 (geo_e6) vs Wikipedia 50,915/0,4858 : déplacement de Battle =", round(hav((50.9143, 0.4870), (50.915, 0.4858)), 3), "km ; 500 m de plus ou de moins sur Battle changent l'écart latéral à Paris de ~", round(0.5*342/76.7, 2), "km")
print("   -> l'alignement à 0,42 km n'est ni une preuve ni discriminant : l'enluminure/Guillaume/Hastings impose Battle ; la droite Londres->Paris passe par là.")
print("\n== Axe prolongé : le cap Tour->Battle (149,1°) pointe le centre de Paris ; sa largeur à 342 km pour ±1° est +-%.1f km" % (342*math.tan(math.radians(1))))
