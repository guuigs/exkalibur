# É12 — orthophoto IGN + parcelles publiques + bâti + Tapon + chemins, autour d'un point.
# usage : ortho_public.py P8 BATI HYD ROUTES lat lon demi_cote_m sortie.jpg
import json, sys, math, io, urllib.request, urllib.parse
from PIL import Image, ImageDraw
from shapely.geometry import shape
from pyproj import Transformer

P8, BATI, HYD, ROUTES = sys.argv[1:5]
lat, lon, half = float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]); OUT = sys.argv[8]
t93 = Transformer.from_crs(4326, 2154, always_xy=True).transform
X, Y = t93(lon, lat); x0, y0, x1, y1 = X - half, Y - half, X + half, Y + half
W = 1400
q = {"SERVICE": "WMS", "VERSION": "1.3.0", "REQUEST": "GetMap", "LAYERS": "ORTHOIMAGERY.ORTHOPHOTOS",
     "STYLES": "", "CRS": "EPSG:2154", "BBOX": f"{x0},{y0},{x1},{y1}", "WIDTH": W, "HEIGHT": W, "FORMAT": "image/jpeg"}
img = Image.open(io.BytesIO(urllib.request.urlopen("https://data.geopf.fr/wms-r?" + urllib.parse.urlencode(q), timeout=60).read())).convert("RGB")
d = ImageDraw.Draw(img)
def px(x, y): return ((x - x0) / (x1 - x0) * W, (y1 - y) / (y1 - y0) * W)
def coords93(geom):
    g = shape(geom); c = g.representative_point().coords[0]
    if abs(c[0]) < 1000:
        from shapely.ops import transform; g = transform(t93, g)
    return g
def draw(g, col, w=3, fill=None):
    if g.geom_type.startswith("Multi") or g.geom_type == "GeometryCollection":
        for p in g.geoms: draw(p, col, w, fill); return
    if g.geom_type == "Polygon":
        d.polygon([px(*c[:2]) for c in g.exterior.coords], outline=col, fill=fill)
        d.line([px(*c[:2]) for c in g.exterior.coords], fill=col, width=w)
    elif g.geom_type == "LineString":
        d.line([px(*c[:2]) for c in g.coords], fill=col, width=w)
from shapely.geometry import box
B = box(x0, y0, x1, y1)
def F(p):
    dd = json.load(open(p, encoding="utf-8")); return dd if isinstance(dd, list) else dd["features"]
for f in F(ROUTES):
    g = coords93(f["geometry"])
    if g.intersects(B): draw(g, (255, 140, 0), 2)
for f in F(HYD):
    g = coords93(f["geometry"])
    if g.intersects(B): draw(g, (0, 200, 255), 4)
for f in F(BATI):
    g = coords93(f["geometry"])
    if g.intersects(B): draw(g, (255, 0, 0), 2)
for r in json.load(open(P8, encoding="utf-8")):
    if not r.get("geom"): continue
    g = coords93(r["geom"])
    if not g.intersects(B): continue
    pub = r["grp"] in ("1", "2", "3", "4")
    draw(g, (0, 255, 0) if pub else (255, 255, 0), 3 if pub else 1)
    if pub:
        c = g.representative_point(); d.text(px(c.x, c.y), r["id"][-5:], fill=(0, 255, 0))
# anneau 10 stades depuis l'esplanade
E = t93(6.03112, 45.42891)
for R, col in ((1831.5, (255, 0, 255)), (1868.5, (255, 0, 255))):
    pts = [px(E[0] + R * math.sin(math.radians(a / 4)), E[1] + R * math.cos(math.radians(a / 4))) for a in range(0, 1441)]
    d.line(pts, fill=col, width=2)
# rayons 63,7° et 66,5° (grille ≈ géographique ± convergence ~1,3°)
for a in (63.7, 66.5):
    d.line([px(*E), px(E[0] + 2500 * math.sin(math.radians(a)), E[1] + 2500 * math.cos(math.radians(a)))], fill=(255, 255, 255), width=1)
img.save(OUT, quality=88); print(OUT)
