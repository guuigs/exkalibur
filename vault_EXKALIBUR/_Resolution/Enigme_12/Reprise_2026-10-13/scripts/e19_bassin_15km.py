# É12 — E19 : contour du bassin de l'enl. 9 comparé à TOUS les plans d'eau BD TOPO à ≤ 15 km de la tour.
# Même polygone peint (P0, relevé de t124_contour_etang.py) et même mesure (IoU après normalisation, rotation 3°, miroir permis).
# Témoin : rang du Vernay dans la liste élargie ; IoU attendue du meilleur sur N formes quelconques.
import json, math, sys
from shapely.geometry import shape, Polygon, Point
from shapely import affinity
from shapely.ops import transform
from pyproj import Transformer
O = sys.argv[1]
t93 = Transformer.from_crs(4326, 2154, always_xy=True).transform
tll = Transformer.from_crs(2154, 4326, always_xy=True).transform
TOUR = Point(*t93(6.031015, 45.428888))
pts = [(25,12),(60,12),(100,18),(150,8),(200,10),(235,12),(270,5),(300,25),(325,55),(338,100),(343,150),(335,190),(320,215),(285,228),(245,228),(210,210),(180,190),(150,165),(125,152),(95,147),(70,130),(50,105),(35,75),(22,45)]
P0 = Polygon([(x, -y) for x, y in pts]).buffer(0)
def norm(p):
    p = affinity.translate(p, -p.centroid.x, -p.centroid.y); return affinity.scale(p, 1 / math.sqrt(p.area), 1 / math.sqrt(p.area), origin=(0, 0))
N0 = norm(P0)
def best(q, step=3):
    qn = norm(q); b = (0, 0, 0)
    for m in (0, 1):
        qq = affinity.scale(qn, -1, 1, origin=(0, 0)) if m else qn
        for a in range(0, 360, step):
            r = affinity.rotate(qq, a, origin=(0, 0)); i = N0.intersection(r).area; u = N0.union(r).area
            if i / u > b[0]: b = (i / u, a, m)
    return b
C = []
for fn in ("plan_d_eau_15km.json", "surfhydro_15km.json"):
    for f in json.load(open(O + fn, encoding="utf-8")):
        g = transform(t93, shape(f["geometry"]))
        for p in getattr(g, "geoms", [g]):
            if p.geom_type == "Polygon" and 300 < p.area < 3e6:
                nm = f["properties"].get("toponyme") or f["properties"].get("cpx_toponyme") or f["properties"].get("nature") or ""
                C.append((fn[:5] + " " + str(nm), p))
# dédoublonnage (même centroïde à 5 m)
U = []
for nm, p in C:
    if all(p.centroid.distance(q.centroid) > 5 for _, q in U): U.append((nm, p))
res = []
for nm, p in U:
    b = best(p.simplify(1.0)); lo, la = tll(p.centroid.x, p.centroid.y)
    res.append((round(b[0], 3), nm, round(p.area), round(p.centroid.distance(TOUR)), round(la, 5), round(lo, 5), b[1], b[2]))
res.sort(reverse=True)
print("formes comparées :", len(res))
for i, r in enumerate(res[:20], 1): print(i, r)
for i, r in enumerate(res, 1):
    if abs(r[4] - 45.453) < 0.004 and abs(r[5] - 6.004) < 0.006: print("Vernay : rang", i, r)
