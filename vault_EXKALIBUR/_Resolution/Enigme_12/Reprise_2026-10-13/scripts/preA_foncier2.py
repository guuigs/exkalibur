# É12 — suite du contrôle foncier du pré A : parcelles communales A1221 / A1318 (+ voisines), surfaces,
# distance réelle au bâti BD TOPO (Lambert-93), et la « cabane » (bâtiment ou non ?).
import json, sys, math
from shapely.geometry import shape, Point
from shapely.ops import transform
from pyproj import Transformer

P8, BATI = sys.argv[1], sys.argv[2]
to93 = Transformer.from_crs(4326, 2154, always_xy=True).transform
pm = json.load(open(P8, encoding="utf-8"))
bati = json.load(open(BATI, encoding="utf-8"))
print("CRS bati :", bati.get("crs"), "exemple coord :", json.dumps(bati["features"][0]["geometry"]["coordinates"])[:80])
# détecter le CRS : coordonnées > 1000 => Lambert-93
c0 = bati["features"][0]["geometry"]["coordinates"]
while isinstance(c0[0], list): c0 = c0[0]
is93 = abs(c0[0]) > 1000
bg = []
for f in bati["features"]:
    g = shape(f["geometry"])
    bg.append((g if is93 else transform(to93, g), f["properties"]))

def near_bati(lat, lon, n=3):
    P = Point(*to93(lon, lat))
    d = sorted(((P.distance(g), p) for g, p in bg), key=lambda t: t[0])[:n]
    return [(round(x), p.get("nature") or p.get("usage_1"), p.get("hauteur")) for x, p in d]

ids = {"384260000A1221", "384260000A1318", "384260000A0340", "384260000A1319", "384260000A1317"}
for r in pm:
    if r["id"] in ids or (r["com"] == "38426" and r["id"][8:10] == "0A" and r["grp"] in ("1", "2", "3", "4")):
        g = shape(r["geom"]); c = g.centroid
        g93 = transform(to93, g)
        if math.hypot((c.y - 45.4303) * 111320, (c.x - 6.0540) * 78000) > 600: continue
        print(r["id"], r["den"], "grp", r["grp"], "fj", r["fj"], f"{g93.area:.0f} m²",
              f"centre {c.y:.5f},{c.x:.5f}", "bâti:", near_bati(c.y, c.x, 2))

print()
for name, (la, lo) in {"cabane": (45.43021, 6.05380), "rive 5": (45.43032, 6.05386), "rive 6": (45.43036, 6.05371),
                       "J2": (45.43105, 6.05343), "A1": (45.43010, 6.05463), "J": (45.43054, 6.05309),
                       "pré A": (45.43057, 6.05462)}.items():
    print(f"{name:8s}", near_bati(la, lo))
