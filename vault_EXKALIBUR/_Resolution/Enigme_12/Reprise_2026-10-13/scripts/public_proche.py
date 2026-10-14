# É12 — inventaire « public d'abord » à courte portée de la tour (≤ 1,6 km), SANS seuil de bâti inventé :
# toutes les parcelles publiques (DGFiP 1-4) ≥ 300 m², avec : distance au ruisseau BD TOPO (écoulement naturel),
# distance au bâti, part boisée, distance et cap depuis l'esplanade. Tri par distance au ruisseau.
import json, sys, math
from shapely.geometry import shape, Point
from shapely.ops import transform
from shapely.strtree import STRtree
from pyproj import Transformer
D = sys.argv[1]
t93 = Transformer.from_crs(4326, 2154, always_xy=True).transform
tll = Transformer.from_crs(2154, 4326, always_xy=True).transform
E = Point(*t93(6.03112, 45.42891))
def F(p):
    d = json.load(open(p, encoding="utf-8")); return d if isinstance(d, list) else d["features"]
def g93(geom):
    g = shape(geom); c = g.representative_point().coords[0]
    return g if abs(c[0]) > 1000 else transform(t93, g)
bat = [g93(f["geometry"]) for f in F(D + "/wfs_bati.json")]
bat = [b for b in bat if b.distance(E) < 2500]
hyd = [(g93(f["geometry"]), f["properties"]) for f in F(D + "/wfs_hydro.json")]
hyd = [(g, p) for g, p in hyd if p.get("nature") == "Ecoulement naturel" and g.distance(E) < 2500]
veg = [(g93(f["geometry"]), f["properties"].get("nature")) for f in F(D + "/wfs_veg.json")]
veg = [(g, n) for g, n in veg if g.distance(E) < 2500 and n and ("For" in n or "Bois" in n)]
bt = STRtree(bat)
rows = []
for r in json.load(open(D + "/parcelles_pm_8km.json", encoding="utf-8")):
    if r["grp"] not in ("1", "2", "3", "4") or not r.get("geom"): continue
    g = transform(t93, shape(r["geom"]))
    if g.area < 300 or E.distance(g) > 1600: continue
    dh, nh = min(((g.distance(h), (p.get("cpx_toponyme_de_cours_d_eau") or p.get("nom_permanent") or "sans nom")) for h, p in hyd), key=lambda t: t[0])
    near = bt.query(g.buffer(300)); db = min((g.distance(bat[i]) for i in near), default=300)
    # surface à ≥ 50 m du bâti
    far = g
    for i in bt.query(g.buffer(50)): far = far.difference(bat[i].buffer(50))
    wood = sum(g.intersection(v).area for v, _ in veg if v.intersects(g)) / g.area
    c = g.representative_point(); lon, lat = tll(c.x, c.y)
    az = (math.degrees(math.atan2(c.x - E.x, c.y - E.y)) + 360) % 360
    rows.append(dict(id=r["id"], den=r["den"][:26], m2=round(g.area), dist=round(E.distance(c)), az=round(az), eau=round(dh), ruisseau=nh,
                     bati=round(db), far50=round(far.area), bois=round(100 * wood), pt=f"{lat:.5f},{lon:.5f}"))
rows.sort(key=lambda x: x["eau"])
print(len(rows), "parcelles publiques ≥ 300 m² à ≤ 1,6 km")
print("id | propriétaire | m² | dist | cap | ruisseau m | nom | bâti m | m² à ≥50 m du bâti | bois % | point")
for x in rows:
    if x["eau"] <= 60: print(" | ".join(str(v) for v in x.values()))
json.dump(rows, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False)
