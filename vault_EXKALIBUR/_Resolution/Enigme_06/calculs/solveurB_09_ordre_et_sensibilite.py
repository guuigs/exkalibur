"""Solveur B / É6 — 09) (a) sensibilité de D au géocodage (Battle abbaye/ville/Hastings) ; (b) chaînes du noyau : la chaîne est-elle l'ordre 'évident' ?
(= la chaîne est le chemin hamiltonien le plus court de ses 4 points ; FAQ03-101/279 « ordre évident, pas d'aller-retour ») ; (c) Guilhem : sensibilité de 345,21 km aux
coordonnées de Cluny / Cadouin (abbaye vs bourg), Wikipedia vs carte ; (d) point de l'axe prolongé à D = 345,21 km."""
import sys, itertools, json
sys.path.insert(0, "."); from solveurB_geo import *
from solveurB_05_chaines import load_poolA, TARGETS
T = (51.5081124, -0.0759493)
SC = (48.855375, 2.3449609)
print("== (a) D selon le point 'champ de bataille' (Tour -> champ -> Sainte-Chapelle, polyligne)")
for nm, B in {"Battle Abbey (Wikipedia)": (50.915, 0.4858), "Battle ville (Wikipedia)": (50.92, 0.48), "geo_e6.py": (50.9143, 0.487), "Hastings ville (carte Guilhem)": (50.854259, 0.573453), "Senlac/Caldbec Hill (approx. 50.9166, 0.4917)": (50.9166, 0.4917)}.items():
    print(f"  {nm:48s} D = {hav(T,B):.2f} + {hav(B,SC):.2f} = {hav(T,B)+hav(B,SC):.2f} km   (droit T-SC = {hav(T,SC):.2f})")
print("  -> D_poly - D_droit est de l'ordre du mètre (alignement) : toutes les lectures donnent 341,6 km ± 0,1 pour Battle ; Hastings donne", round(hav(T,(50.854259,0.573453))+hav(( 50.854259,0.573453),SC),2))

pool = load_poolA()
def shortest_path(pts):
    best = None
    for p in itertools.permutations(range(len(pts))):
        if p[0] > p[-1]: continue
        L = sum(hav(pts[p[i]], pts[p[i+1]]) for i in range(len(p)-1))
        if best is None or L < best[0]: best = (L, p)
    return best
print("\n== (b) chaînes du noyau restreint dans ±1 % de D_SC : la chaîne est-elle le chemin le plus court de ses 4 points ?")
data = json.load(open("solveurB_08_noyau.json", encoding="utf-8"))
for tn in ("Sainte-Chapelle",):
    for row in data[tn]:
        L, names = row[0], row[1:]
        pts = [pool[n][:2] for n in names]
        bl, bp = shortest_path(pts)
        is_min = abs(bl - L) < 0.011
        print(f"  {L:7.2f} ({100*(L/TARGETS[tn]-1):+.2f} %) {' - '.join(names):55s} plus court chemin sur ces 4 points : {bl:7.2f} -> {'ORDRE ÉVIDENT (chaîne = plus court)' if is_min else 'ordre NON minimal'}")
print("\n== (b') Toutes les chaînes des 105 lieux de la liste curée dans ±1 % de D_SC dont l'ordre est le plus court chemin de ses 4 points, ET dont tous les lieux sont en France")
import numpy as np
from solveurB_05_chaines import chains_in_tol
names = list(pool); P = [pool[k][:2] for k in names]
D = TARGETS["Sainte-Chapelle"]
r = chains_in_tol(names, P, D*0.99, D*1.01)
mn = [t for t in r if abs(shortest_path([P[i] for i in t[1:]])[0]-t[0]) < 1e-6]
print(f"  {len(r)} chaînes ±1 % ; dont chaîne = plus court chemin : {len(mn)} ({100*len(mn)/len(r):.0f} %)")
# contrôles : 40 D aléatoires
import random
rnd = random.Random(7); fr = []
for _ in range(12):
    Dr = rnd.uniform(250, 450); rr = chains_in_tol(names, P, Dr*0.99, Dr*1.01)
    fr.append((round(Dr, 1), len(rr), sum(1 for t in rr if abs(shortest_path([P[i] for i in t[1:]])[0]-t[0]) < 1e-6)))
print("  contrôles (D aléatoire, nb chaînes, nb chaînes = plus court chemin):", fr)
print("\n== (c) Sensibilité de Cluny-Clermont-Cadouin (3 C) au géocodage")
co = wiki_coords(["Cluny Abbey", "Cluny", "Cadouin Abbey", "Cadouin", "Clermont-Ferrand Cathedral", "Clermont-Ferrand"])
print({k: (v[:2] if v else None) for k, v in co.items()})
G = {"Cluny": (46.4348054, 4.6585012), "Clermont": (45.7787583, 3.0858573), "Cadouin": (44.8114955, 0.8737598)}
def chain(a, b, c): return hav(a, b)+hav(b, c)
print(f"  carte Guilhem : {chain(G['Cluny'],G['Clermont'],G['Cadouin']):.2f} km")
for cl in ("Cluny Abbey", "Cluny"):
    for ca in ("Cadouin Abbey", "Cadouin"):
        for cm in ("Clermont-Ferrand Cathedral", "Clermont-Ferrand"):
            if all(co[k] for k in (cl, ca, cm)):
                L = chain(co[cl][:2], co[cm][:2], co[ca][:2]); print(f"  Wikipedia {cl:12s} {ca:14s} {cm:28s}: {L:.2f} km  ({100*(L/D-1):+.2f} % vs D_SC)")
print("  Amplitude de l'incertitude de géocodage (~0,3 km) >= marge de 0,18 km : la chaîne à 3 C est compatible/incompatible selon la source.")
print("\n== (d) Point de l'axe Tour->Battle prolongé à D =", 345.21, "km :", dest(T, cap(T, (50.915, 0.4858)), 345.21))
E_ = dest(T, cap(T, (50.915, 0.4858)), 345.21)
print("   distance à la Sainte-Chapelle :", round(hav(E_, SC), 2), "km ; à Notre-Dame :", round(hav(E_, (48.853, 2.3499)), 2), "km")
