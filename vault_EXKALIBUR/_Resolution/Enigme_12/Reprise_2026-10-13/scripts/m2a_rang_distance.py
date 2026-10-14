# É12 — M2a : rang par distance au départ (règle : M2a_regle.md, écrite avant).
# Source : BD TOPO (IGN) au lieu d'OSM, car Overpass répondait 504 (écart de source, pas de règle ; noté dans le rapport).
import json, sys, math, random
from collections import defaultdict
O = sys.argv[1]; OUT = sys.argv[2]
def L(n): return json.load(open(O + n, encoding="utf-8"))
KX = 111320 * math.cos(math.radians(45.4289)); KY = 111320
def xy(lon, lat): return ((lon - 6.031015) * KX, (lat - 45.428888) * KY)
def ll(p): return f"{45.428888 + p[1] / KY:.5f},{6.031015 + p[0] / KX:.5f}"
def lines_of(g):
    if g["type"] == "LineString": return [g["coordinates"]]
    if g["type"] == "MultiLineString": return g["coordinates"]
    return []
def mid(g):
    ls = lines_of(g); c = ls[0]; p = c[len(c) // 2]; return xy(p[0], p[1])
R = L("bdt_routes.json"); H = L("bdt_hydro.json"); DH = L("bdt_dethydro.json"); CP = L("bdt_consponc.json"); CL = L("bdt_conslin.json")
cls = defaultdict(list)
for f in CL:
    n = f["properties"]["nature"]
    if n == "Pont": cls["1_ponts"].append(mid(f["geometry"]))
    if n == "Ruines": cls["9_ruines"].append(mid(f["geometry"]))
LIGHT = ("Chemin", "Sentier", "Route empierrée")
for f in R:
    p = f["properties"]
    if p.get("position_par_rapport_au_sol") == "1" and p["nature"] in LIGHT: cls["2_ponts_chemins"].append(mid(f["geometry"]))
ends = defaultdict(list)
for f in R:
    for c in lines_of(f["geometry"]):
        for q in (c[0], c[-1]):
            ends[(round(q[0], 6), round(q[1], 6))].append(f["properties"]["nature"])
for k, v in ends.items():
    if len(v) >= 3:
        cls["4_jonctions"].append(xy(*k[:2]))
        if sum(1 for n in v if n in LIGHT) >= 3: cls["5_jonctions_chemins"].append(xy(*k[:2]))
def segs(c):
    g = [xy(p[0], p[1]) for p in c]; return list(zip(g, g[1:]))
def inter(a, b, c, e):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = a, b, c, e
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < 1e-9: return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1)) if 0 <= t <= 1 and 0 <= u <= 1 else None
WS = [s for f in H if f["properties"].get("nature") == "Ecoulement naturel" for c in lines_of(f["geometry"]) for s in segs(c)]
for f in R:
    for c in lines_of(f["geometry"]):
        for a, b in segs(c):
            for c2, e in WS:
                if max(a[0], b[0]) < min(c2[0], e[0]) or min(a[0], b[0]) > max(c2[0], e[0]) or max(a[1], b[1]) < min(c2[1], e[1]) or min(a[1], b[1]) > max(c2[1], e[1]): continue
                p = inter(a, b, c2, e)
                if p: cls["3_traversees_eau"].append(p)
for f in CP:
    if f["properties"]["nature"] == "Croix": cls["6_croix"].append(xy(*f["geometry"]["coordinates"][:2]))
for f in DH:
    n = f["properties"]["nature"]
    if n in ("Fontaine", "Lavoir", "Source", "Source captée", "Point d'eau"):
        cls["7_fontaines_sources"].append(xy(*f["geometry"]["coordinates"][:2]))
        if n in ("Fontaine", "Lavoir"): cls["8_fontaines_lavoirs"].append(xy(*f["geometry"]["coordinates"][:2]))
def dedup(pts, r=10):
    out = []
    for p in pts:
        if all(math.hypot(p[0] - q[0], p[1] - q[1]) > r for q in out): out.append(p)
    return out
STARTS = {"donjon": (45.428888, 6.031015), "esplanade": (45.42891, 6.03112), "rue_Rempart": (45.429772, 6.03118), "chateau_Bayard": (45.423611, 6.018889)}
TARGET, TOL = 1850.0, 18.5
def d311(S, pts):
    r = sorted(pts, key=lambda p: math.hypot(p[0] - S[0], p[1] - S[1]))
    if len(r) < 13: return None, None
    return math.hypot(r[2][0] - r[10][0], r[2][1] - r[10][1]), (r[2], r[10])
random.seed(1); rnd = []
while len(rnd) < 2000:
    x, y = random.uniform(-3000, 3000), random.uniform(-3000, 3000)
    if x * x + y * y <= 9e6: rnd.append((x, y))
out = ["classe | n (≤ 4,5 km du donjon) | départ | d(3e,11e) m | touche ±1 % | 3e | 11e | p hasard (2 000 départs)"]
for k in sorted(cls):
    pts = [p for p in dedup(cls[k]) if math.hypot(*p) < 4500]
    hits = 0
    for S in rnd:
        v, _ = d311(S, pts)
        if v is not None and abs(v - TARGET) <= TOL: hits += 1
    p = hits / len(rnd)
    for name, (la, lo) in STARTS.items():
        D, ab = d311(xy(lo, la), pts)
        if D is None: out.append(f"{k} | {len(pts)} | {name} | < 13 objets | — | | | {p:.3f}"); continue
        out.append(f"{k} | {len(pts)} | {name} | {D:.0f} | {'OUI' if abs(D - TARGET) <= TOL else 'non'} | {ll(ab[0])} | {ll(ab[1])} | {p:.3f}")
open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n"); print("\n".join(out))
