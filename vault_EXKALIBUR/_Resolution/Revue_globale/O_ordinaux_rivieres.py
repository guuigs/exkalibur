"""3e et 11e = objets ORDONNÉS le long d'un cours d'eau (piste Guilhem + FAQ07-068 écharde) ?
Hypothèse testée : « troisième » et « onzième » = 3e et 11e PONTS (ou passerelles) d'un même cours d'eau, comptés
depuis l'embouchure ou depuis la source. Pieds nus : pont de pierre (pas d'écharde) / pont ou passerelle de bois
(écharde possible) ; « il faudra marcher surtout sur l'un des deux » (FAQ06-247) ; on passe par des étapes
intermédiaires (4e…10e, FAQ04-115) ; « le 13e ne mènerait pas au bon endroit » (FAQ06-133).
Contrainte : distance 3e–11e en ligne droite = 10 stades romains ±1 % (185 m → [1831,5 ; 1868,5] m).
Contrôle du hasard : même calcul pour TOUTES les paires (k, k+8) de chaque rivière → taux de base.
Données : BD TOPO v3 (IGN), rayon 12 km autour de la tour d'Avalon.
"""
import json, math, re, heapq
from collections import defaultdict, Counter
S = r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/ign/"
TA = (45.4288, 6.03078)
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*6371008.8*math.asin(math.sqrt(h))
KX = math.cos(math.radians(TA[0]))*111320; KY = 110540
def xy(lon, lat): return ((lon-TA[1])*KX, (lat-TA[0])*KY)
def ll(x, y): return (TA[0]+y/KY, TA[1]+x/KX)
def pts(g):
    c = g["coordinates"]; out = []
    def rec(z):
        if isinstance(z[0], (int, float)): out.append(z)
        else:
            for w in z: rec(w)
    rec(c); return out
def cen(g):
    p = pts(g); return (sum(q[1] for q in p)/len(p), sum(q[0] for q in p)/len(p))

H = json.load(open(S+"troncon_hydrographique_12km.geojson", encoding="utf-8"))["features"]
OBJ = {}
for L in ["construction_lineaire", "construction_surfacique"]:
    for f in json.load(open(S+L+"_12km.geojson", encoding="utf-8"))["features"]:
        p = f["properties"]
        if p.get("nature") == "Pont":
            OBJ.setdefault("pont", []).append((cen(f["geometry"]), p.get("nature_detaillee") or "Pont", p.get("toponyme")))
for f in json.load(open(S+"detail_hydrographique_12km.geojson", encoding="utf-8"))["features"]:
    p = f["properties"]
    if p.get("nature") in ("Cascade", "Lavoir", "Fontaine", "Source", "Source captée"):
        OBJ.setdefault(p["nature"].lower(), []).append((cen(f["geometry"]), p["nature"], p.get("toponyme")))

rivers = defaultdict(list)
for f in H:
    n = f["properties"].get("cpx_toponyme_de_cours_d_eau")
    if n and f["properties"].get("nature") not in ("Conduit forcé", "Conduit buse"):
        rivers[n].append([xy(c[0], c[1]) for c in f["geometry"]["coordinates"]])

def river_positions(segs):
    """distance à l'embouchure pour chaque sommet (tronçons en sens direct = vers l'aval)."""
    k = lambda p: (round(p[0], 1), round(p[1], 1))
    adj = defaultdict(list); outdeg = Counter(); nodes = set()
    for s in segs:
        a, b = k(s[0]), k(s[-1]); L = sum(math.dist(s[i], s[i+1]) for i in range(len(s)-1))
        adj[b].append((a, L)); outdeg[a] += 1; nodes |= {a, b}
    mouths = [n for n in nodes if outdeg[n] == 0]
    dist = {m: 0.0 for m in mouths}; pq = [(0.0, m) for m in mouths]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, 1e18): continue
        for v, L in adj[u]:
            if d+L < dist.get(v, 1e18): dist[v] = d+L; heapq.heappush(pq, (d+L, v))
    return dist, k

def project(p, segs, dist, k, tol=30):
    best = None
    for s in segs:
        dB = dist.get(k(s[-1]))
        if dB is None: continue
        cum = [0.0]
        for i in range(len(s)-1): cum.append(cum[-1]+math.dist(s[i], s[i+1]))
        for i in range(len(s)-1):
            (x1, y1), (x2, y2) = s[i], s[i+1]; dx, dy = x2-x1, y2-y1; L2 = dx*dx+dy*dy or 1e-9
            t = max(0, min(1, ((p[0]-x1)*dx+(p[1]-y1)*dy)/L2)); q = (x1+t*dx, y1+t*dy)
            e = math.dist(p, q)
            if e <= tol and (best is None or e < best[0]):
                along = cum[i]+t*math.sqrt(L2); best = (e, dB+(cum[-1]-along))
    return None if best is None else best[1]

WIN = {"185 m": (1831.5, 1868.5), "177,6 m": (1758.2, 1793.8), "192 m": (1900.8, 1939.2)}
hits, base_tot, base_hit = [], Counter(), Counter()
for obj, lst in OBJ.items():
    for name, segs in rivers.items():
        dist, k = river_positions(segs)
        items = []
        for (c, nat, top) in lst:
            p = xy(c[1], c[0]); pos = project(p, segs, dist, k)
            if pos is not None: items.append((pos, c, nat, top))
        items.sort()
        ded = []
        for it in items:
            if not ded or it[0]-ded[-1][0] > 20: ded.append(it)
        n = len(ded)
        if n < 11: continue
        for sens, seq in (("depuis l'embouchure", ded), ("depuis la source", ded[::-1])):
            for i in range(n-8):
                d = hav(seq[i][1], seq[i+8][1])
                for w, (lo, hi) in WIN.items():
                    base_tot[(obj, w)] += 1
                    if lo <= d <= hi: base_hit[(obj, w)] += 1
            d = hav(seq[2][1], seq[10][1])
            for w, (lo, hi) in WIN.items():
                if lo <= d <= hi:
                    hits.append((obj, name, sens, w, round(d), seq[2], seq[10], n))
        print(f"{obj:13s} | {name:32s} | {n:3d} objets | 3e–11e depuis embouchure {hav(ded[2][1], ded[10][1]):6.0f} m | depuis source {hav(ded[::-1][2][1], ded[::-1][10][1]):6.0f} m")
print("\n== 3e–11e dans une fenêtre de 10 stades ±1 % ==")
for h in hits:
    obj, name, sens, w, d, a, b, n = h
    print(f"{obj} | {name} ({n}) | {sens} | stade {w} | {d} m | 3e {a[1][0]:.5f},{a[1][1]:.5f} ({a[2]}, {a[3]}) → 11e {b[1][0]:.5f},{b[1][1]:.5f} ({b[2]}, {b[3]}) | 3e à {hav(TA, a[1])/1000:.2f} km de la tour, 11e à {hav(TA, b[1])/1000:.2f} km")
print("\n== Taux du hasard (toutes paires k, k+8) ==")
for key in sorted(base_tot):
    print(key, f"{base_hit[key]}/{base_tot[key]} = {100*base_hit[key]/max(1, base_tot[key]):.1f} %")
