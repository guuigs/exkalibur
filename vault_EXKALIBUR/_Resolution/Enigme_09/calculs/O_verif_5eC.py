"""É9 Noli me tangere : vérification de la chaîne « croisée des chemins → même distance des 4C vers l'Est → avant-dernier C ».
Lectures testées (chacune ancrée dans un texte, pas choisie pour le résultat) :
  - garde    = nouvelle garde É7 (Sainte-Chapelle → Lorient) : c'est la garde en vigueur après Sub rosa.
  - royaume  = É5 : « de l'Armorique à la Bretagne, sur ces pierres, je bâtirai mon royaume » → droite Carnac → Stonehenge
               (FAQ06-219 : le royaume est « plus vaste que celui des pierres dressées »).
  - croisée  = intersection des deux segments.
  - distance = chaîne des 4 C d'É6 = 340,9 km (FAQ03-047 : « la même distance que les quatre C »).
  - vers l'Est : cap à l'est, non imposé à 90° (le Discord note que le 5e C « n'est pas plein Est »).
Nul : toutes les communes françaises dont le nom commence par C, à 340,9 km ± 1 % de la croisée, cap entre 45° et 135°.
Contrôle : les autres croisées possibles (garde É1, lame É1) avec la même règle."""
import json, math, sys
sys.stdout.reconfigure(encoding="utf-8")
R = 6371.0088; D4C = 340.9
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
def brg(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    y = math.sin(lo2-lo1)*math.cos(la2); x = math.cos(la1)*math.sin(la2)-math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return math.degrees(math.atan2(y, x)) % 360
def v(p):
    la, lo = map(math.radians, p); return (math.cos(la)*math.cos(lo), math.cos(la)*math.sin(lo), math.sin(la))
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def norm(a): n = math.sqrt(sum(x*x for x in a)); return tuple(x/n for x in a)
def inter(a1, a2, b1, b2):
    x = norm(cross(norm(cross(v(a1), v(a2))), norm(cross(v(b1), v(b2)))))
    c = (math.degrees(math.asin(x[2])), math.degrees(math.atan2(x[1], x[0])))
    return c if hav(c, a1) < 5000 else (-c[0], c[1]+180 if c[1] < 0 else c[1]-180)
P = {"SteChapelle": (48.855375, 2.3449609), "Lorient": (47.7494, -3.3799), "Carnac": (47.5918383, -3.0835991),
     "Stonehenge": (51.178882, -1.826215), "León": (42.5994383, -5.5671632), "Foix": (42.965574, 1.604881),
     "Urquhart": (57.3241399, -4.4420013), "Valence": (39.4752858, -0.3754667)}
CAND = {"Cathédrale de Chartres (labyrinthe)": (48.447778, 1.487500), "Château de Chambord": (47.616200, 1.517000)}
X = inter(P["SteChapelle"], P["Lorient"], P["Carnac"], P["Stonehenge"])
print(f"Croisée garde É7 × royaume É5 : {X[0]:.5f}, {X[1]:.5f}")
for n, c in CAND.items():
    d = hav(X, c); print(f"  → {n:36s} {d:7.2f} km (écart {100*(d-D4C)/D4C:+.2f} %), cap {brg(X, c):.1f}°")
com = json.load(open(r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Enigme_06/calculs/T1data/communes.json", encoding="utf-8"))
pts = [(c["nom"], (c["centre"]["coordinates"][1], c["centre"]["coordinates"][0])) for c in com if c.get("centre")]
def ring(x, pref="C", tol=0.01, lo=45, hi=135):
    return [(n, hav(x, p), brg(x, p)) for n, p in pts
            if n.upper().startswith(pref) and abs(hav(x, p)-D4C) <= tol*D4C and lo <= brg(x, p) <= hi]
r = ring(X)
allr = [(n, hav(X, p)) for n, p in pts if abs(hav(X, p)-D4C) <= 0.01*D4C and 45 <= brg(X, p) <= 135]
print(f"\nNul : {len(allr)} communes (toutes lettres) dans l'anneau ±1 % et cap 45-135° ; {len(r)} commencent par C :")
for n, d, b in sorted(r, key=lambda t: t[2]): print(f"   {n:32s} {d:7.2f} km cap {b:5.1f}°")
print("\nContrôle, autres croisées :")
for lab, (a1, a2, b1, b2) in {"garde É1 × royaume É5": ("León", "Foix", "Carnac", "Stonehenge"),
                              "garde É7 × lame É1": ("SteChapelle", "Lorient", "Urquhart", "Valence"),
                              "garde É1 × lame É1": ("León", "Foix", "Urquhart", "Valence")}.items():
    Y = inter(P[a1], P[a2], P[b1], P[b2])
    print(f"  {lab:24s} croisée {Y[0]:.4f},{Y[1]:.4f} ; Chartres {hav(Y, CAND['Cathédrale de Chartres (labyrinthe)']):.1f} km ; Chambord {hav(Y, CAND['Château de Chambord']):.1f} km")
