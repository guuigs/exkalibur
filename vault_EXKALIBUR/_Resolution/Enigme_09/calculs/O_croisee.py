"""É9 Noli me tangere : « j'arrivai à la croisée des chemins, entre la garde et le royaume, et parcourus la même distance
des 4C, vers l'Est, jusqu'à l'avant-dernier C ».
Test systématique : pour chaque ligne « garde » (É1 ancienne, É7 nouvelle) × chaque ligne « royaume » candidate
(É4 chemin royal, É5 Carnac→Stonehenge, É1 lame), on calcule l'intersection (grand cercle et segment),
puis le point à 340,9 km plein Est (cap 90° sur le grand cercle, et Est « constant » sur le parallèle).
On ne conclut rien ici : on liste les points d'arrivée, que l'on confronte ensuite à des lieux en C."""
import math, sys
sys.stdout.reconfigure(encoding="utf-8")
R = 6371.0088
D4C = 340.9
P = {
 "León": (42.5994383, -5.5671632), "Foix": (42.965574, 1.604881),
 "Urquhart": (57.3241399, -4.4420013), "Valence": (39.4752858, -0.3754667),
 "Sainte-Chapelle": (48.855375, 2.3449609), "Rennes": (48.1117, -1.6836), "Lorient": (47.7494, -3.3799),
 "Tintagel": (50.6672813, -4.7585053), "Silchester": (51.3538459, -1.1005385), "Westminster": (51.4993695, -0.1272993),
 "Carnac": (47.5918383, -3.0835991), "Stonehenge": (51.178882, -1.826215),
}
def v(p):
    la, lo = map(math.radians, p); return (math.cos(la)*math.cos(lo), math.cos(la)*math.sin(lo), math.sin(la))
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def norm(a): n = math.sqrt(sum(x*x for x in a)); return tuple(x/n for x in a)
def ll(u): return math.degrees(math.asin(u[2])), math.degrees(math.atan2(u[1], u[0]))
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
def dest(a, t, d):
    la1, lo1 = map(math.radians, a); t = math.radians(t); dr = d/R
    la2 = math.asin(math.sin(la1)*math.cos(dr)+math.cos(la1)*math.sin(dr)*math.cos(t))
    lo2 = lo1+math.atan2(math.sin(t)*math.sin(dr)*math.cos(la1), math.cos(dr)-math.sin(la1)*math.sin(la2))
    return math.degrees(la2), math.degrees(lo2)
def inter(a1, a2, b1, b2):
    n1 = norm(cross(v(a1), v(a2))); n2 = norm(cross(v(b1), v(b2)))
    x = norm(cross(n1, n2)); c = ll(x); c2 = ll(tuple(-t for t in x))
    # garder la solution la plus proche de la zone (Europe)
    return c if hav(c, a1) < hav(c2, a1) else c2
def on_seg(p, a, b): return hav(a, p)+hav(p, b)-hav(a, b) < 1.0
GARDES = {"garde É1 (León–Foix)": ("León", "Foix"), "garde É7 (Sainte-Chapelle–Lorient)": ("Sainte-Chapelle", "Lorient")}
ROY = {"É5 Carnac–Stonehenge (royaume des pierres dressées)": ("Carnac", "Stonehenge"),
       "É4 Tintagel–Silchester": ("Tintagel", "Silchester"), "É4 Silchester–Westminster": ("Silchester", "Westminster"),
       "É1 lame Urquhart–Valence": ("Urquhart", "Valence")}
for gn, (g1, g2) in GARDES.items():
    for rn, (r1, r2) in ROY.items():
        X = inter(P[g1], P[g2], P[r1], P[r2])
        s1, s2 = on_seg(X, P[g1], P[g2]), on_seg(X, P[r1], P[r2])
        e_gc = dest(X, 90, D4C)
        dlon = D4C/(R*math.cos(math.radians(X[0])))
        e_par = (X[0], X[1]+math.degrees(dlon))
        print(f"{gn} × {rn}\n   croisée {X[0]:.4f},{X[1]:.4f} (sur segment garde: {s1}, royaume: {s2})"
              f"\n   +340,9 km Est : grand cercle → {e_gc[0]:.4f},{e_gc[1]:.4f} ; parallèle → {e_par[0]:.4f},{e_par[1]:.4f}")
