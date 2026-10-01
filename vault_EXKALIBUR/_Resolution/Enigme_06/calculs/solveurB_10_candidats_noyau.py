"""Solveur B / É6 — 10) chaînes du noyau (43 lieux en C, liste curée, sans Carnac) dans ±1 % de D pour CHAQUE candidat « lieu très Sainte » plausible,
et test de spécificité : pour chaque chaîne, ordre 'évident' (= plus court chemin des 4 points), croisement de la lame (FAQ07-166), nature.
D = Tour -> Battle Abbey -> X (polyligne). Candidats X : ceux de solveurB_01."""
import sys, itertools, json
import numpy as np
sys.path.insert(0, "."); from solveurB_geo import *
from solveurB_05_chaines import load_poolA, dist_matrix
from solveurB_08_noyau import CORE, crosses_blade
pool = load_poolA(); names = [c for c in CORE if c in pool]; P = [pool[n][:2] for n in names]; n = len(names); M = dist_matrix(P)
T = (51.5081124, -0.0759493); B = (50.915, 0.4858)
X = {"Sainte-Chapelle": (48.855375, 2.3449609), "Notre-Dame de Paris": (48.8530, 2.3499), "Ste-Chapelle Vincennes": (48.8423, 2.4364), "Saint-Denis": (48.9356, 2.3597),
     "Chartres": (48.4478, 1.4878), "Vézelay": (47.4664, 3.7486), "Mont-Saint-Michel": (48.6360, -1.5110), "Sainte-Baume": (43.3167, 5.75),
     "Saintes (17)": (45.7464, -0.6333), "Reims": (49.2539, 4.0342), "Saintes-Maries-de-la-Mer": (43.4528, 4.4286), "Rosslyn": (55.8553, -3.1603), "Glastonbury": (51.1456, -2.7144), "Canterbury": (51.2797, 1.0831)}
L4 = M[:, :, None, None] + M[None, :, :, None] + M[None, None, :, :]
I = np.indices((n, n, n, n)); a, b, c, d = I
valid = (a != b) & (a != c) & (a != d) & (b != c) & (b != d) & (c != d) & (a < d)
Lv = L4[valid]; idx = np.stack([a[valid], b[valid], c[valid], d[valid]], 1)
print(f"{n} lieux ; {len(Lv):,} chaînes ; fenêtre ±1 %")
def sp(pts):
    return min(sum(hav(pts[p[i]], pts[p[i+1]]) for i in range(3)) for p in itertools.permutations(range(4)))
for tn, x in X.items():
    D = hav(T, B) + hav(B, x); m = (Lv >= D*0.99) & (Lv <= D*1.01); k = int(m.sum())
    ev = 0; ok = 0; ex = []
    for l, ix in zip(Lv[m], idx[m]):
        pts = [P[i] for i in ix]
        e = abs(sp(pts)-l) < 0.011; nb = not crosses_blade(pts)
        ev += e; ok += (e and nb)
        if e and nb: ex.append((round(float(l), 1), [names[i] for i in ix]))
    print(f"\n{tn:26s} D={D:8.2f} : {k:4d} chaînes ±1 % ; ordre évident : {ev} ; + sans croiser la lame : {ok}")
    for l, nm in sorted(ex, key=lambda t: abs(t[0]-D))[:8]: print(f"     {l:7.1f} ({100*(l/D-1):+.2f} %) {' - '.join(nm)}")
