# -*- coding: utf-8 -*-
"""T12C_01 : viewsheds LiDAR depuis chaque départ + analyse photométrique (soleil bas du matin).

- viewshed (méthode horizon par secteurs angulaires) depuis D1 sommet, D2 pied, D3 Bayard.
- points de cours d'eau (tronçons BD TOPO échantillonnés) : visibilité, azimut depuis départ,
  sens d'écoulement -> test « miroitement » (regard vers le soleil) et « éclairé de face ».
- sensibilité : hauteur d'œil (2 vs 27 m) et azimut solaire (date).
"""
import json, math, numpy as np

S = r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/"
R = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/"
E = S + "exk_e12/"

meta = json.load(open(E + "lidar_meta_1500.json"))
BB = meta["BB"]; n = meta["n"]; RES = meta["RES"]
la0, lo0, la1, lo1 = BB
DLAT = (la1 - la0) / (n - 1)          # deg/ligne
DLON = (lo1 - lo0) / (n - 1)          # deg/col
DLATm = DLAT * 111132.0
DLONm = DLON * 111132.0 * math.cos(math.radians((la0 + la1) / 2))
print("DLATm=%.3f DLONm=%.3f (m/cellule)" % (DLATm, DLONm))

mnt = np.load(E + "mnt_1500_2.npy").astype(np.float64)

def latlon_to_ij(lat, lon):
    i = (la1 - lat) / (la1 - la0) * (n - 1)
    j = (lon - lo0) / (lo1 - lo0) * (n - 1)
    return i, j

def ij_to_latlon(i, j):
    lat = la1 - i * DLAT
    lon = lo0 + j * DLON
    return lat, lon

def angdiff(a, b):
    d = abs(a - b) % 360.0
    return min(d, 360.0 - d)

def viewshed(mnt, i0, j0, z0, nbins=14400, tol=1e-4):
    """Retourne un booléen n×n : True si la cellule est visible depuis (i0,j0,z0)."""
    n = mnt.shape[0]
    ii = np.arange(n, dtype=np.float64)[:, None]
    jj = np.arange(n, dtype=np.float64)[None, :]
    di = ii - i0
    dj = jj - j0
    r = np.hypot(di, dj) * RES
    el = np.arctan2(mnt - z0, r)
    ang = np.arctan2(di, dj)                     # -pi..pi ; di=nord(positif vers le bas->sud), dj=est
    abin = np.floor((ang + np.pi) / (2 * np.pi) * nbins).astype(np.int64) % nbins
    visible = np.zeros((n, n), dtype=bool)
    rflat = r.ravel(); eflat = el.ravel(); aflat = abin.ravel()
    idx = np.arange(rflat.size)
    for b in range(nbins):
        m = aflat == b
        if not m.any():
            continue
        k = idx[m]
        rr = rflat[k]; ee = eflat[k]
        o = np.argsort(rr, kind='stable')
        rr = rr[o]; ee = ee[o]
        prev = np.empty_like(ee); prev[0] = -np.inf
        if ee.size > 1:
            np.maximum.accumulate(ee[:-1], out=prev[1:])
        vis = ee > prev + tol
        visible.ravel()[k[o]] = vis
    visible[i0, j0] = False
    return visible

# ---- départs ----
TOWER = (45.429083, 6.030808)
BAYARD = (45.4242, 6.0179)
starts = [
    ("D1_sommet_tour", 45.429083, 6.030808, 27.0),
    ("D2_pied_tour",   45.429083, 6.030808, 2.0),
    ("D3_Bayard",      45.4242,   6.0179,   2.0),
]

# ---- points de cours d'eau (tronçons échantillonnés) ----
hydro = json.load(open(S + "ign/troncon_hydrographique_12km.geojson", encoding="utf-8"))["features"]

def sample_line(coords, step=15.0):
    """Échantillonne une LineString [lon,lat] tous les ~step m. Retourne liste (lat,lon) + bearing local."""
    import math
    out = []
    for a, b in zip(coords[:-1], coords[1:]):
        lon1, lat1 = a[0], a[1]; lon2, lat2 = b[0], b[1]
        dx = (lon2 - lon1) * 111132.0 * math.cos(math.radians((lat1 + lat2) / 2))
        dy = (lat2 - lat1) * 111132.0
        L = math.hypot(dx, dy)
        if L == 0:
            continue
        nseg = max(1, int(math.ceil(L / step)))
        brg = (math.degrees(math.atan2(dx, dy)) + 360) % 360
        for s in range(nseg):
            t = s / nseg
            out.append((lat1 + (lat2 - lat1) * t, lon1 + (lon2 - lon1) * t, brg))
    return out

pts = []  # (lat, lon, flow_bearing, name, nature, persistance)
for f in hydro:
    p = f["properties"]
    g = f["geometry"]
    if g is None or g["type"] != "LineString":
        continue
    name = p.get("cpx_toponyme_de_cours_d_eau") or "(sans nom)"
    nat = p.get("nature", "")
    pers = p.get("persistance", "")
    coords = g["coordinates"]
    for (lat, lon, brg) in sample_line(coords, 15.0):
        if la0 <= lat <= la1 and lo0 <= lon <= lo1:
            pts.append((lat, lon, brg, name, nat, pers))
print("Points de cours d'eau dans le MNT :", len(pts))
plat = np.array([q[0] for q in pts])
plon = np.array([q[1] for q in pts])
pbrg = np.array([q[2] for q in pts])
pname = [q[3] for q in pts]
pnat = [q[4] for q in pts]
ppers = [q[5] for q in pts]
pi = (la1 - plat) / (la1 - la0) * (n - 1)
pj = (plon - lo0) / (lo1 - lo0) * (n - 1)

# ---- analyse par départ ----
AZIMUTS = [54.3, 63.75, 68.07, 75.0, 80.0, 90.0]   # solstice été, jour dernier julien, grég., 10°, 5°, equinoxe
CONE = 25.0

def summarize(name, i0, j0, z0):
    vis = viewshed(mnt, i0, j0, z0)
    # visibilité des points de cours d'eau
    vmask = vis[np.clip(np.round(pi).astype(int), 0, n-1), np.clip(np.round(pj).astype(int), 0, n-1)]
    # azimut depuis le départ
    dN = (i0 - pi) * DLATm          # + = nord du départ
    dE = (pj - j0) * DLONm          # + = est du départ
    b_start = (np.degrees(np.arctan2(dE, dN)) + 360) % 360
    dist = np.hypot(dN, dE)
    print("\n===== %s (i0=%d j0=%d z0=%.1f m, œil=%.1f m) =====" % (name, i0, j0, z0, z0))
    print("  cellules visibles (terrain) : %d / %d (%.1f %%)" % (vis.sum(), n*n, 100*vis.sum()/(n*n)))
    print("  points de cours d'eau visibles : %d / %d" % (vmask.sum(), len(pts)))
    # détail par nom de cours d'eau (uniquement les visibles)
    visnames = {}
    for k in np.where(vmask)[0]:
        visnames.setdefault(pname[k], 0)
        visnames[pname[k]] += 1
    print("  cours d'eau visibles (n pts) :", dict(sorted(visnames.items(), key=lambda x:-x[1])))
    # test photométrique par azimut
    print("  --- test 'miroitement' (regard vers le soleil, cône ±%d°) ---" % CONE)
    for az in AZIMUTS:
        in_cone = vmask & (np.array([angdiff(b, az) for b in b_start]) <= CONE)
        # face-on : écoulement vers le soleil (soleil en amont) ou vallée orientée soleil
        face = vmask & (np.array([angdiff(b, az) for b in pbrg]) <= 45.0)
        both = in_cone & face
        # répartition par nom
        def byname(m):
            d = {}
            for k in np.where(m)[0]:
                d.setdefault(pname[k], 0); d[pname[k]] += 1
            return dict(sorted(d.items(), key=lambda x: -x[1])[:8])
        print("    az=%.2f : miroitement=%3d  face-on=%3d  les2=%3d | miroir top: %s" %
              (az, in_cone.sum(), face.sum(), both.sum(), byname(in_cone)))
    return vis, b_start, dist, vmask

results = {}
for (name, la, lo, heye) in starts:
    i0, j0 = latlon_to_ij(la, lo)
    i0, j0 = int(round(i0)), int(round(j0))
    z0 = mnt[i0, j0] + heye
    print("\n>>> %s : départ (%.5f, %.5f) z_terrain=%.1f + œil %.1f = %.1f m" % (name, la, lo, mnt[i0,j0], heye, z0))
    vis, b_start, dist, vmask = summarize(name, i0, j0, z0)
    results[name] = dict(i0=i0, j0=j0, z0=z0, b_start=b_start.tolist(), dist=dist.tolist(), vmask=vmask.tolist())

json.dump(results, open(R + "T12C_01_viewsheds.json", "w", encoding="utf-8"))
print("\n[SAVE] T12C_01_viewsheds.json")

# ---- sensibilité hauteur d'œil ----
print("\n===== Sensibilité hauteur d'œil (D1, az=64°) =====")
i0, j0 = latlon_to_ij(45.429083, 6.030808); i0=int(round(i0)); j0=int(round(j0))
for he in [0.0, 2.0, 10.0, 20.0, 27.0, 40.0]:
    z0 = mnt[i0, j0] + he
    vis = viewshed(mnt, i0, j0, z0)
    vmask = vis[np.clip(np.round(pi).astype(int),0,n-1), np.clip(np.round(pj).astype(int),0,n-1)]
    dN = (i0-pi)*DLATm; dE=(pj-j0)*DLONm
    b_start = (np.degrees(np.arctan2(dE,dN))+360)%360
    in_cone = vmask & (np.array([angdiff(b,64.0) for b in b_start])<=CONE)
    print("  œil=%4.1f m : visible=%5d cellules | cours_eau visibles=%4d | miroitement(az64)=%3d" % (he, vis.sum(), vmask.sum(), in_cone.sum()))
