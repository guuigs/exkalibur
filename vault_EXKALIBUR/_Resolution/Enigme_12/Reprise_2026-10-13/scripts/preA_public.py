# É12 — parcelles publiques autour du pré A et du Tapon : position vs ruisseau, distance au départ,
# bâti, nature de la végétation. Sortie = tableau. (Règle éliminatoire : public + loin du bâti.)
import json, sys, math
from shapely.geometry import shape, Point
from shapely.ops import transform
from pyproj import Transformer

P8, BATI, HYD, VEG = sys.argv[1:5]
to93 = Transformer.from_crs(4326, 2154, always_xy=True).transform
pm = json.load(open(P8, encoding="utf-8"))
bati = json.load(open(BATI, encoding="utf-8"))
def feats(d): return d if isinstance(d, list) else d["features"]
def g93(geom):
    g = shape(geom); c = g.representative_point().coords[0]
    return g if abs(c[0]) > 1000 else transform(to93, g)
bg = [(g93(f["geometry"]), f["properties"]) for f in feats(bati)]
hyd = [(g93(f["geometry"]), f["properties"]) for f in feats(json.load(open(HYD, encoding="utf-8")))]
veg = [(g93(f["geometry"]), f["properties"]) for f in feats(json.load(open(VEG, encoding="utf-8")))]
ESPL = Point(*to93(6.03112, 45.42891))
tapon = [g for g, p in hyd if (p.get("nom_permanent") or p.get("cpx_toponyme_de_cours_d_eau") or "").lower().find("tapon") >= 0]
print("tronçons Tapon :", len(tapon))
def az(P):
    dx, dy = P.x - ESPL.x, P.y - ESPL.y
    return (math.degrees(math.atan2(dx, dy)) + 360) % 360  # azimut grille Lambert (≈ convergence ~1,5°)
rows = []
for r in pm:
    if r["grp"] not in ("1", "2", "3", "4") or not r.get("geom"): continue
    g = transform(to93, shape(r["geom"]))
    c = g.centroid
    if c.distance(Point(*to93(6.0546, 45.4306))) > 900: continue
    dt = min((g.distance(t) for t in tapon), default=-1)
    db = min(g.distance(b) for b, _ in bg)
    dE = ESPL.distance(c)
    v = {}
    for vg, vp in veg:
        a = g.intersection(vg).area if g.intersects(vg) else 0
        if a: v[vp.get("nature")] = v.get(vp.get("nature"), 0) + a
    vtxt = ", ".join(f"{k} {100*a/g.area:.0f}%" for k, a in sorted(v.items(), key=lambda t: -t[1]))
    lon, lat = transform(Transformer.from_crs(2154, 4326, always_xy=True).transform, c).coords[0]
    rows.append((r["id"], r["den"][:28], round(g.area), f"{lat:.5f},{lon:.5f}", round(dE), round(az(c), 1), round(dt), round(db), vtxt))
rows.sort(key=lambda t: t[4])
print("id | propriétaire | m² | centre | dist. esplanade m | az° | dist. Tapon m | dist. bâti m | végétation BD TOPO")
for x in rows: print(" | ".join(map(str, x)))
