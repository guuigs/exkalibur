# É12 — contrôle éliminatoire du pré A : propriété (cadastre Etalab/apicarto + DGFiP personnes morales),
# distance au bâti BD TOPO. Règle posée AVANT : le coffre est en domaine public (01-235, 02-097) et
# loin de tout bâtiment (05-107). On vérifie chaque point candidat de TODO_REPRISE_E12 § 5 + la rive droite du Tapon.
import json, sys, math, urllib.request, urllib.parse, time
from shapely.geometry import shape, Point

P8 = sys.argv[1]   # parcelles_pm_8km.json (DGFiP personnes morales, 8 km, géométries)
BATI = sys.argv[2] # wfs_bati.json (BD TOPO batiment)
pm = json.load(open(P8, encoding="utf-8"))
pmg = [(shape(r["geom"]), r) for r in pm if r.get("geom")]
bati = json.load(open(BATI, encoding="utf-8"))
bg = [shape(f["geometry"]) for f in bati["features"] if f.get("geometry")]

def m(lat1, lon1, lat2, lon2):
    k = 111320
    return math.hypot((lat2 - lat1) * k, (lon2 - lon1) * k * math.cos(math.radians(lat1)))

def parcelle(lat, lon):
    g = json.dumps({"type": "Point", "coordinates": [lon, lat]})
    u = "https://apicarto.ign.fr/api/cadastre/parcelle?" + urllib.parse.urlencode({"geom": g})
    for _ in range(3):
        try:
            d = json.load(urllib.request.urlopen(u, timeout=30))
            f = d.get("features", [])
            if not f:
                return None
            p = f[0]["properties"]
            return p["code_insee"] + p.get("com_abs", "000") + p["section"].rjust(2, "0") + p["numero"]
        except Exception as e:
            err = e; time.sleep(2)
    return "ERR " + str(err)

pts = {
    "pré A centre": (45.43057, 6.05462), "J2 angle NO": (45.43105, 6.05343),
    "A1 angle SE": (45.43010, 6.05463), "J passage Tapon": (45.43054, 6.05309),
    "cabane": (45.43021, 6.05380), "R1 ravin": (45.42944, 6.05466),
    "P3 Couvat": (45.43288, 6.05406),
}
# rive droite du Tapon entre A1 et J : 9 points interpolés (ligne A1 -> J, décalés de 0)
for i in range(1, 10):
    t = i / 10
    pts[f"rive A1→J {i}"] = (45.43010 + t * (45.43054 - 45.43010), 6.05463 + t * (6.05309 - 6.05463))

for name, (la, lo) in pts.items():
    P = Point(lo, la)
    hit = [r for g, r in pmg if g.contains(P)]
    k = 111320; c = math.cos(math.radians(la))
    dmin = min(P.distance(g) for g in bg)  # degrés approx
    # conversion approx : distance en degrés -> m (anisotropie négligée sauf facteur moyen)
    dm = dmin * k * (1 + c) / 2
    pid = parcelle(la, lo)
    own = f"{hit[0]['den']} (grp {hit[0]['grp']}, fj {hit[0]['fj']})" if hit else "pas dans le fichier personnes morales ⇒ personne physique (PRIVÉ)"
    if pid is None:
        own = "NON CADASTRÉ (domaine public non cadastré possible : voirie/cours d'eau)"
    print(f"{name:18s} {la:.5f},{lo:.5f}  parcelle={pid}  propriétaire={own}  bâti≈{dm:.0f} m")
