# É12 — Règle J : cap géodésique vers Jérusalem (110,98°). Test + témoin 360 caps (seuils opérationnels fixés ici, avant).
# Jonction = extrémité BD TOPO partagée par ≥ 3 tronçons, dans la couronne 1 831,5-1 868,5 m et à ≤ 25 m latéralement du cap.
# Puis : public (DGFiP 1-4) à ≤ 50 m ; bâti ≥ 50 m ; forêt BD TOPO à ≤ 50 m ; ruisseau (écoulement naturel) à ≤ 100 m.
import json, sys, math
from collections import defaultdict
from shapely.geometry import shape, Point
from shapely.ops import transform
from shapely.strtree import STRtree
from pyproj import Transformer
O, D, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
t93 = Transformer.from_crs(4326, 2154, always_xy=True).transform
tll = Transformer.from_crs(2154, 4326, always_xy=True).transform
def F(p):
    d = json.load(open(p, encoding="utf-8")); return d if isinstance(d, list) else d["features"]
def g93(geom):
    g = shape(geom); c = g.representative_point().coords[0]
    return g if abs(c[0]) > 1000 else transform(t93, g)
R = F(O + "bdt_routes.json")
ends = defaultdict(list)
for f in R:
    g = f["geometry"]; ls = [g["coordinates"]] if g["type"] == "LineString" else g["coordinates"]
    for c in ls:
        for q in (c[0], c[-1]): ends[(round(q[0], 6), round(q[1], 6))].append(f["properties"]["nature"])
J = [(Point(*t93(k[0], k[1])), v) for k, v in ends.items() if len(v) >= 3]
pub = [g93(r["geom"]) for r in json.load(open(D + "parcelles_pm_8km.json", encoding="utf-8")) if r["grp"] in ("1", "2", "3", "4") and r.get("geom")]
bat = [g93(f["geometry"]) for f in F(D + "wfs_bati.json")]
veg = [g93(f["geometry"]) for f in F(D + "wfs_veg.json") if (f["properties"].get("nature") or "").startswith(("Forêt", "Bois"))]
hyd = [g93(f["geometry"]) for f in F(O + "bdt_hydro.json") if f["properties"].get("nature") == "Ecoulement naturel"]
TP, TB, TV, TH = STRtree(pub), STRtree(bat), STRtree(veg), STRtree(hyd)
def near(tree, geoms, P, r):
    return any(geoms[i].distance(P) <= r for i in tree.query(P.buffer(r)))
def dmin(tree, geoms, P, r=400):
    c = [geoms[i].distance(P) for i in tree.query(P.buffer(r))]; return min(c) if c else r
STARTS = {"donjon": (45.428888, 6.031015), "esplanade": (45.42891, 6.03112), "rue_Rempart": (45.429772, 6.03118), "chateau_Bayard": (45.423611, 6.018889)}
def cands(S, az):
    dx, dy = math.sin(math.radians(az)), math.cos(math.radians(az)); out = []
    for P, v in J:
        vx, vy = P.x - S.x, P.y - S.y; d = math.hypot(vx, vy)
        if not 1831.5 <= d <= 1868.5: continue
        along = vx * dx + vy * dy; lat = abs(vx * dy - vy * dx)
        if along > 0 and lat <= 25: out.append((P, v, d, lat))
    return out
def score(P):
    return dict(public=near(TP, pub, P, 50), bati=round(dmin(TB, bat, P)), foret=near(TV, veg, P, 50), eau=round(dmin(TH, hyd, P)))
lines = []
# NB : la grille Lambert-93 est tournée de ~ -1,1° par rapport au nord géographique ici (convergence) ; on corrige.
lon0 = 3.0; conv = math.degrees(math.atan(math.tan(math.radians(6.03 - lon0)) * math.sin(math.radians(45.43))))  # approx. convergence
for sn, (la, lo) in STARTS.items():
    S = Point(*t93(lo, la))
    azg = 110.98 + 0 - (-conv) * 0  # placeholder kept explicit below
    azg = 110.98 - conv          # azimut géographique -> azimut grille
    cs = cands(S, azg)
    lines.append(f"## {sn} (cap géographique 110,98° → grille {azg:.2f}°) : {len(cs)} jonction(s) sur l'anneau à ≤ 25 m du cap")
    for P, v, d, lat in cs:
        lo2, la2 = tll(P.x, P.y); sc = score(P)
        lines.append(f"- {la2:.5f},{lo2:.5f} d={d:.0f} m, écart latéral {lat:.0f} m, voies {v} → {sc}")
    # point exact à 1 850 m
    Q = Point(S.x + 1850 * math.sin(math.radians(azg)), S.y + 1850 * math.cos(math.radians(azg)))
    lo2, la2 = tll(Q.x, Q.y)
    lines.append(f"  point à 1 850 m : {la2:.5f},{lo2:.5f} → {score(Q)}")
    # témoin
    npass = nany = 0
    for a in range(360):
        ok_any = False; ok_all = False
        for P, v, d, lat in cands(S, a - conv):
            ok_any = True; s = score(P)
            if s["public"] and s["bati"] >= 50 and s["foret"] and s["eau"] <= 100: ok_all = True
        nany += ok_any; npass += ok_all
    lines.append(f"  témoin 360 caps : jonction présente {nany}/360 ; jonction passant les 4 filtres {npass}/360")
open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n"); print("\n".join(lines)); print("convergence", round(conv, 3))
