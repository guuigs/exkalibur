# -*- coding: utf-8 -*-
"""T12C_02 : croisements de sentiers + filtres + témoins aléatoires.

Sources croisements : (1) nœuds réseau pédestre OSM (reseau_gresivaudan_noeuds.json) ;
(2) nœuds BD TOPO degré>=3 (Chemin+Sentier).
Filtres : trouée de végétation (hors Bois/Forêt), <=150 m d'un cours d'eau, >=150 m de tout
bâtiment, visible du départ (LOS), cône solaire (regard vers le soleil), forêt publique.
Imprime le taux de passage de CHAQUE filtre + combinaisons, et pour des départs témoins aléatoires.
"""
import json, math, random
import numpy as np
from shapely.geometry import Point, shape
from shapely.strtree import STRtree
from shapely.ops import transform

def xy_to_metric(x, y, z=None):   # x=lon, y=lat -> mètres (plan tangent local)
    return (x * 111132.0 * COS0, y * 111132.0)

S = r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/"
R = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/"
E = S + "exk_e12/"
I = S + "ign/"

meta = json.load(open(E + "lidar_meta_1500.json"))
BB = meta["BB"]; n = meta["n"]; RES = meta["RES"]
la0, lo0, la1, lo1 = BB
DLAT = (la1 - la0) / (n - 1); DLON = (lo1 - lo0) / (n - 1)
DLATm = DLAT * 111132.0
DLONm = DLON * 111132.0 * math.cos(math.radians((la0 + la1) / 2))
COS0 = math.cos(math.radians((la0 + la1) / 2))
mnt = np.load(E + "mnt_1500_2.npy").astype(np.float64)

def latlon_to_ij(lat, lon):
    return (la1 - lat) / (la1 - la0) * (n - 1), (lon - lo0) / (lo1 - lo0) * (n - 1)

def angdiff(a, b):
    d = abs(a - b) % 360.0
    return min(d, 360.0 - d)

def los_visible(i0, j0, z0, it, jt, zt, tol=1.0):
    d = max(abs(it - i0), abs(jt - j0))
    if d < 1:
        return True
    steps = int(math.ceil(d))
    for s in range(1, steps):
        t = s / steps
        i = i0 + (it - i0) * t; j = j0 + (jt - j0) * t
        zi = int(round(i)); zj = int(round(j))
        if 0 <= zi < n and 0 <= zj < n:
            if mnt[zi, zj] > z0 + (zt - z0) * t + tol:
                return False
    return True

# ---- 1. croisements OSM ----
osm = json.load(open(E + "reseau_gresivaudan_noeuds.json", encoding="utf-8"))
osm_cross = [(x["lat"], x["lon"], x.get("nom")) for x in osm]

# ---- 2. nœuds BD TOPO degré>=3 (Chemin + Sentier) ----
routes = json.load(open(I + "troncon_de_route.geojson", encoding="utf-8"))["features"]
paths = [f for f in routes if f["properties"].get("nature") in ("Chemin", "Sentier")]
COS = math.cos(math.radians((la0 + la1) / 2))
def snap(lat, lon, g=6.0):
    return (round(lat * 111132.0 / g), round(lon * 111132.0 * COS / g))
from collections import defaultdict
node_tids = defaultdict(set)
node_xy = {}
for f in paths:
    tid = f["properties"]["cleabs"]
    g = f["geometry"]
    if g is None or g["type"] != "LineString":
        continue
    for c in g["coordinates"]:
        lon, lat = c[0], c[1]
        k = snap(lat, lon)
        node_tids[k].add(tid)
        if k not in node_xy:
            node_xy[k] = (lat, lon)
bd_junc = [(node_xy[k][0], node_xy[k][1], len(node_tids[k])) for k, t in node_tids.items() if len(t) >= 3]
print("Chemins/Sentiers BD TOPO :", len(paths), "| nœuds degré>=3 :", len(bd_junc))

# ---- fusion des croisements (dédupl. 15 m) ----
def dedupe(pts, tol_m=15.0):
    out = []
    for lat, lon, lbl in pts:
        if all(math.hypot((lat - a) * 111132.0, (lon - b) * 111132.0 * COS) > tol_m for a, b, _ in out):
            out.append((lat, lon, lbl))
    return out
crossings = dedupe([(la, lo, "OSM:" + (nm or "")) for la, lo, nm in osm_cross] +
                   [(la, lo, "BDTOPO:deg%d" % dg) for la, lo, dg in bd_junc])
print("Croisements uniques (OSM + BD TOPO degré>=3) :", len(crossings))

# ---- couches de référence ----
hydro_feats = json.load(open(I + "troncon_hydrographique_12km.geojson", encoding="utf-8"))["features"]
hydro_lines = [transform(xy_to_metric, shape(f["geometry"])) for f in hydro_feats if f["geometry"] and f["geometry"]["type"] == "LineString"]
htree = STRtree(hydro_lines)

bldg = json.load(open(I + "batiment.geojson", encoding="utf-8"))["features"]
bldg_polys = [transform(xy_to_metric, shape(f["geometry"])) for f in bldg if f["geometry"]]
btree = STRtree(bldg_polys)

veg = json.load(open(I + "zone_de_vegetation.geojson", encoding="utf-8"))["features"]
DENSE = {"Bois", "Forêt fermée de feuillus", "Forêt fermée mixte", "Forêt fermée de conifères", "Forêt ouverte", "Lande ligneuse", "Peupleraie"}
dense_polys = [transform(xy_to_metric, shape(f["geometry"])) for f in veg if f["geometry"] and f["properties"].get("nature") in DENSE]
dtree = STRtree(dense_polys)

fpub = json.load(open(I + "foret_publique_12km.geojson", encoding="utf-8"))["features"]
fpub_polys = [transform(xy_to_metric, shape(f["geometry"])) for f in fpub if f["geometry"]]
ftree = STRtree(fpub_polys)

# monuments (proxy) : bâtiments nature Eglise/Chapelle/Château/Tour donjon
monum = [transform(xy_to_metric, shape(f["geometry"])) for f in bldg if f["geometry"] and f["properties"].get("nature") in ("Eglise", "Chapelle", "Château", "Tour, donjon")]
mtree = STRtree(monum)

def near(geoms, tree, pt, dmax):
    cand = tree.query(pt, predicate="dwithin", distance=dmax)
    return len(cand) > 0

def min_dist(tree, pt):
    idx = tree.query_nearest(pt)
    if idx is None or len(idx) == 0:
        return 1e9
    geom = tree.geometries.take(idx)[0]
    return pt.distance(geom)

# ---- attributs par croisement ----
SUN_AZ = [64.0, 75.0]
STARTS = [("D1_sommet", 45.429083, 6.030808, 27.0),
          ("D2_pied",   45.429083, 6.030808, 2.0),
          ("D3_Bayard", 45.4242,   6.0179,   2.0)]
start_ijz = {}
for nm, la, lo, he in STARTS:
    i0, j0 = latlon_to_ij(la, lo); i0 = int(round(i0)); j0 = int(round(j0))
    start_ijz[nm] = (i0, j0, mnt[i0, j0] + he)

rows = []
for (lat, lon, lbl) in crossings:
    pt = Point(lon * 111132.0 * COS0, lat * 111132.0)
    d_water = min_dist(htree, pt)
    d_bldg = min_dist(btree, pt)
    d_mon = min_dist(mtree, pt)
    in_clearing = not near(dense_polys, dtree, pt, 1.0)
    in_fpub = near(fpub_polys, ftree, pt, 1.0)
    ii, jj = latlon_to_ij(lat, lon); ii = int(round(ii)); jj = int(round(jj))
    zt = mnt[ii, jj] if (0 <= ii < n and 0 <= jj < n) else None
    r = dict(lat=lat, lon=lon, lbl=lbl, d_water=d_water, d_bldg=d_bldg, d_mon=d_mon,
             clearing=in_clearing, fpub=in_fpub)
    for nm, (i0, j0, z0) in start_ijz.items():
        if zt is None:
            r["vis_" + nm] = False; r["sun64_" + nm] = False; r["sun75_" + nm] = False; r["brg_" + nm] = -1.0
            continue
        vis = los_visible(i0, j0, z0, ii, jj, zt)
        dN = (i0 - ii) * DLATm; dE = (jj - j0) * DLONm
        brg = (math.degrees(math.atan2(dE, dN)) + 360) % 360
        r["vis_" + nm] = vis
        r["sun64_" + nm] = vis and angdiff(brg, 64.0) <= 25.0
        r["sun75_" + nm] = vis and angdiff(brg, 75.0) <= 25.0
        r["brg_" + nm] = brg
    rows.append(r)

print("\n===== Sélectivité de chaque filtre (sur %d croisements) =====" % len(rows))
def rate(cond):
    k = sum(cond(r) for r in rows)
    return k, 100.0 * k / len(rows)
filters = [
    ("F1 d_eau<=150m", lambda r: r["d_water"] <= 150),
    ("F2 d_batiment>=150m", lambda r: r["d_bldg"] >= 150),
    ("F3 en clairière (hors Bois/Forêt)", lambda r: r["clearing"]),
    ("F4 forêt publique", lambda r: r["fpub"]),
    ("F5 d_monument>=150m", lambda r: r["d_mon"] >= 150),
    ("F6 vis D1", lambda r: r["vis_D1_sommet"]),
    ("F7 vis D2", lambda r: r["vis_D2_pied"]),
    ("F8 vis D3", lambda r: r["vis_D3_Bayard"]),
    ("F9 soleil64 D1", lambda r: r["sun64_D1_sommet"]),
    ("F10 soleil64 D2", lambda r: r["sun64_D2_pied"]),
    ("F11 soleil64 D3", lambda r: r["sun64_D3_Bayard"]),
]
for name, fn in filters:
    k, p = rate(fn)
    flag = " <== NON INFORMATIF (25-50%)" if 25 <= p <= 50 else ""
    print("  %-38s %4d / %d (%.1f %%)%s" % (name, k, len(rows), p, flag))

print("\n===== Combinaison complète (F1&F2&F3&F5 & vis & soleil) =====")
for nm, _, _, _ in STARTS:
    for az, sunkey in [("64", "sun64_"), ("75", "sun75_")]:
        k = sum(1 for r in rows if r["d_water"] <= 150 and r["d_bldg"] >= 150 and r["clearing"]
                and r["d_mon"] >= 150 and r["vis_" + nm] and r[sunkey + nm])
        print("  %-10s az=%s : %d croisements passent la chaîne complète" % (nm, az, k))

print("\n===== Liste des croisements proches d'un cours d'eau & en clairière (détail) =====")
sub = [r for r in rows if r["d_water"] <= 150 and r["clearing"] and r["d_bldg"] >= 150]
sub.sort(key=lambda r: r["d_water"])
for r in sub:
    print("  %-28s (%.5f,%.5f) d_eau=%5.0f d_bat=%5.0f clr=%d visD1=%d sun64D1=%d sun75D1=%d brgD1=%5.1f" %
          (r["lbl"][:28], r["lat"], r["lon"], r["d_water"], r["d_bldg"], r["clearing"],
           r["vis_D1_sommet"], r["sun64_D1_sommet"], r["sun75_D1_sommet"], r["brg_D1_sommet"]))

# ---- témoins aléatoires ----
print("\n===== Témoins aléatoires (départs à même distance de la tour que D3=0.83 km) =====")
TOWER = (45.429083, 6.030808)
def dist_tower(lat, lon):
    return math.hypot((lat - TOWER[0]) * 111132.0, (lon - TOWER[1]) * 111132.0 * COS)
random.seed(12)
def full_pass(vis_field, sun_field):
    return sum(1 for r in rows if r["d_water"] <= 150 and r["d_bldg"] >= 150 and r["clearing"]
               and r["d_mon"] >= 150 and r[vis_field] and r[sun_field])
cand_d3 = full_pass("vis_D3_Bayard", "sun64_D3_Bayard")
print("  D3_Bayard (0.83 km) : %d croisements chaîne complète (az64)" % cand_d3)
witness_counts = []
for _ in range(15):
    ang = random.uniform(0, 360)
    d = random.uniform(0.78, 0.88)
    lat = TOWER[0] + d * 1000 * math.sin(math.radians(ang)) / 111132.0
    lon = TOWER[1] + d * 1000 * math.cos(math.radians(ang)) / (111132.0 * COS)
    if not (la0 <= lat <= la1 and lo0 <= lon <= lo1):
        continue
    i0, j0 = latlon_to_ij(lat, lon); i0 = int(round(i0)); j0 = int(round(j0))
    z0 = mnt[i0, j0] + 2.0
    k = 0
    for r in rows:
        if not (r["d_water"] <= 150 and r["d_bldg"] >= 150 and r["clearing"] and r["d_mon"] >= 150):
            continue
        ii, jj = latlon_to_ij(r["lat"], r["lon"]); ii = int(round(ii)); jj = int(round(jj))
        if not (0 <= ii < n and 0 <= jj < n):
            continue
        zt = mnt[ii, jj]
        if los_visible(i0, j0, z0, ii, jj, zt):
            dN = (i0 - ii) * DLATm; dE = (jj - j0) * DLONm
            brg = (math.degrees(math.atan2(dE, dN)) + 360) % 360
            if angdiff(brg, 64.0) <= 25.0:
                k += 1
    witness_counts.append(k)
witness_counts = np.array(witness_counts)
print("  témoins aléatoires (n=%d) : min=%d médiane=%d max=%d moy=%.1f" %
      (len(witness_counts), witness_counts.min(), int(np.median(witness_counts)), witness_counts.max(), witness_counts.mean()))

json.dump(rows, open(R + "T12C_02_croisements.json", "w", encoding="utf-8"))
print("\n[SAVE] T12C_02_croisements.json")

# ---- focus : croisements à <=2 km de la tour ----
print("\n===== Focus zone <=2 km de la tour (pertinente) =====")
tw = (45.429083, 6.030808)
def dtw(lat, lon):
    return math.hypot((lat - tw[0]) * 111132.0, (lon - tw[1]) * 111132.0 * COS0)
near_rows = [r for r in rows if dtw(r["lat"], r["lon"]) <= 2000]
print("  croisements <=2 km :", len(near_rows))
for r in sorted(near_rows, key=lambda r: r["d_water"]):
    if r["d_water"] <= 150:
        print("  %-24s (%.5f,%.5f) d_tour=%4.0f d_eau=%4.0f d_bat=%4.0f clr=%d visD1=%d sun64D1=%d brgD1=%5.1f" %
              (r["lbl"][:24], r["lat"], r["lon"], dtw(r["lat"], r["lon"]), r["d_water"], r["d_bldg"],
               r["clearing"], r["vis_D1_sommet"], r["sun64_D1_sommet"], r["brg_D1_sommet"]))
