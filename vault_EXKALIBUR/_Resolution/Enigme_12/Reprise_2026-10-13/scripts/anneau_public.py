# É12 — où le domaine public touche-t-il l'anneau des 10 stades ? (règle posée avant : on ne filtre pas sur
# « tout près », on mesure ; on liste par azimut la parcelle publique la plus proche de l'anneau et son bâti.)
# Départ = esplanade de la tour d'Avalon (45.42891, 6.03112). Public = DGFiP groupes 1-4.
import json, sys, math
from shapely.geometry import shape, Point, LineString
from shapely.ops import transform
from pyproj import Transformer
P8, BATI = sys.argv[1:3]
t93 = Transformer.from_crs(4326, 2154, always_xy=True).transform
tll = Transformer.from_crs(2154, 4326, always_xy=True).transform
E = Point(*t93(6.03112, 45.42891))
def g93(geom):
    g = shape(geom); c = g.representative_point().coords[0]
    return g if abs(c[0]) > 1000 else transform(t93, g)
bati = json.load(open(BATI, encoding="utf-8")); bati = bati if isinstance(bati, list) else bati["features"]
bg = [g93(f["geometry"]) for f in bati]
from shapely.strtree import STRtree
bt = STRtree(bg)
pub = []
for r in json.load(open(P8, encoding="utf-8")):
    if r["grp"] in ("1", "2", "3", "4") and r.get("geom"):
        g = g93(r["geom"])
        if 1300 < E.distance(g.centroid) < 2400 or E.distance(g) < 2000 < E.hausdorff_distance(g):
            pub.append((g, r))
print("parcelles publiques 1,3-2,4 km :", len(pub))
ring = [Point(E.x + 1850 * math.sin(math.radians(a)), E.y + 1850 * math.cos(math.radians(a))) for a in range(360)]
# parcelles publiques qui COUPENT la couronne 1831,5-1868,5 m
ann = E.buffer(1868.5).difference(E.buffer(1831.5))
hits = []
for g, r in pub:
    if g.intersects(ann):
        part = g.intersection(ann)
        c = part.representative_point()
        az = (math.degrees(math.atan2(c.x - E.x, c.y - E.y)) + 360) % 360
        db = min(g.distance(bg[i]) for i in bt.query(g.buffer(400))) if len(bt.query(g.buffer(400))) else 999
        # surface de la parcelle à >= 100 m de tout bâtiment
        far = g
        for i in bt.query(g.buffer(100)): far = far.difference(bg[i].buffer(100))
        lon, lat = tll(c.x, c.y)
        hits.append((round(az, 1), r["id"], r["den"][:30], round(g.area), round(db), round(far.area), f"{lat:.5f},{lon:.5f}", r["nomcom"]))
hits.sort()
print("az° | parcelle | propriétaire | m² | bâti min m | m² à ≥100 m du bâti | point dans la couronne | commune")
for h in hits: print(" | ".join(map(str, h)))
print("total :", len(hits), "dont ≥ 100 m² loin du bâti :", sum(1 for h in hits if h[5] >= 100))
