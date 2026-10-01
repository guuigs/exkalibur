"""LiDAR HD (IGN, MNT 2 m) autour de la tour d'Avalon : réseau de ruisseaux FIN dérivé du relief (D8, accumulation),
puis comparaison de forme avec la rayure de l'épée (SVG de Guilhem), sur une zone proche du chemin de rempart
(FAQ06-244 : le coffre n'est pas loin du rempart ; FAQ06-025 : la jonction est très proche du rempart).
Sorties : ombrage + réseau en PNG, meilleurs candidats, contrôle miroir.
"""
import json, math, re, sys, urllib.request, itertools
import numpy as np
from PIL import Image
OUT = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/"
SCR = r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/"
TA = (45.4288, 6.03078)
HALF = float(sys.argv[1]) if len(sys.argv) > 1 else 1500.0
RES = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
CEN = (float(sys.argv[3]), float(sys.argv[4])) if len(sys.argv) > 4 else TA

def getbin(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Exkalibur research)"})
    r = urllib.request.urlopen(req, timeout=240); return r.read(), r.headers.get("Content-Type")
def wms(layer, fmt, half, res, cen):
    dlat = half / 110540; dlon = half / (111320 * math.cos(math.radians(cen[0]))); n = int(2 * half / res)
    u = ("https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=" + layer + "&STYLES=&CRS=EPSG:4326"
         f"&BBOX={cen[0]-dlat},{cen[1]-dlon},{cen[0]+dlat},{cen[1]+dlon}&WIDTH={n}&HEIGHT={n}&FORMAT=" + fmt)
    b, ct = getbin(u); return b, ct, n, (cen[0] - dlat, cen[1] - dlon, cen[0] + dlat, cen[1] + dlon)

# tuiles (le WMS limite la taille) : on assemble en blocs de 1000 px max
def mnt(half, res, cen):
    n = int(2 * half / res); T = 1000
    k = math.ceil(n / T); n = k * T; half = n * res / 2
    A = np.zeros((n, n), np.float32)
    dlat_px = res / 110540; dlon_px = res / (111320 * math.cos(math.radians(cen[0])))
    top = cen[0] + n / 2 * dlat_px; left = cen[1] - n / 2 * dlon_px
    for i in range(k):
        for j in range(k):
            c = (top - (i + 0.5) * T * dlat_px, left + (j + 0.5) * T * dlon_px)
            b, ct, m, bb = wms("IGNF_LIDAR-HD_MNT_ELEVATION.ELEVATIONGRIDCOVERAGE.WGS84G", "image/x-bil;bits=32", T * res / 2, res, c)
            if "bil" not in (ct or ""): raise SystemExit(f"WMS: {ct} {b[:300]}")
            A[i*T:(i+1)*T, j*T:(j+1)*T] = np.frombuffer(b, "<f4").reshape(T, T)
    return A, (top - n * dlat_px, left, top, left + n * dlon_px), dlat_px, dlon_px

A, BB, DLAT, DLON = mnt(HALF, RES, CEN)
A[A < -100] = np.nan
print("MNT", A.shape, "alt", float(np.nanmin(A)), "→", float(np.nanmax(A)))
np.save(SCR + f"mnt_{HALF:.0f}_{RES:.0f}.npy", A)
def px2ll(r, c): return (BB[2] - (r + 0.5) * DLAT, BB[1] + (c + 0.5) * DLON)
def ll2px(lat, lon): return (int((BB[2] - lat) / DLAT), int((lon - BB[1]) / DLON))

# ombrage
Z = np.nan_to_num(A, nan=np.nanmean(A))
gy, gx = np.gradient(Z, RES)
az, alt = math.radians(315), math.radians(45)
slope = np.arctan(np.hypot(gx, gy)); aspect = np.arctan2(-gx, gy)
hs = np.sin(alt) * np.cos(slope) + np.cos(alt) * np.sin(slope) * np.cos(az - aspect)
hs = (np.clip(hs, 0, 1) * 255).astype(np.uint8)

# D8 + accumulation, après comblement des cuvettes (priority-flood, Barnes 2014, epsilon)
import heapq
n = Z.shape[0]
Zf = Z.astype(np.float64).copy()
closed = np.zeros(Z.shape, bool); pq = []
for r in range(n):
    for c in (0, n - 1):
        heapq.heappush(pq, (Zf[r, c], r, c)); closed[r, c] = True
for c in range(1, n - 1):
    for r in (0, n - 1):
        heapq.heappush(pq, (Zf[r, c], r, c)); closed[r, c] = True
EPS = 1e-4
while pq:
    z, r, c = heapq.heappop(pq)
    for a, b in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        r2, c2 = r + a, c + b
        if 0 <= r2 < n and 0 <= c2 < n and not closed[r2, c2]:
            closed[r2, c2] = True
            if Zf[r2, c2] <= z: Zf[r2, c2] = z + EPS
            heapq.heappush(pq, (Zf[r2, c2], r2, c2))
Z = Zf
nb = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
dist = [math.hypot(a, b) * RES for a, b in nb]
Zp = np.pad(Z, 1, constant_values=np.inf)
best = np.full(Z.shape, -1, np.int8); bestdrop = np.zeros(Z.shape, np.float32)
for k, ((a, b), d) in enumerate(zip(nb, dist)):
    drop = (Z - Zp[1 + a:1 + a + n, 1 + b:1 + b + n]) / d
    m = drop > bestdrop; best[m] = k; bestdrop[m] = drop[m]
order = np.argsort(Z, axis=None)[::-1]
acc = np.ones(Z.size, np.float32)
dr = np.array([a for a, b in nb]); dc = np.array([b for a, b in nb])
bf = best.ravel()
for idx in order:
    k = bf[idx]
    if k < 0: continue
    r, c = divmod(int(idx), n); r2, c2 = r + dr[k], c + dc[k]
    if 0 <= r2 < n and 0 <= c2 < n: acc[r2 * n + c2] += acc[idx]
acc = acc.reshape(Z.shape)
np.save(SCR + f"acc_{HALF:.0f}_{RES:.0f}.npy", acc); np.save(SCR + f"d8_{HALF:.0f}_{RES:.0f}.npy", best)
AREA_MIN = 20000.0  # m² de bassin versant pour appeler ça un ruisseau (≈ 2 ha)
stream = acc * RES * RES >= AREA_MIN
img = np.dstack([hs, hs, hs]).copy()
img[stream] = [30, 110, 255]
tr, tc = ll2px(*TA); img[max(0, tr-6):tr+6, max(0, tc-6):tc+6] = [255, 0, 0]
Image.fromarray(img).save(SCR + f"lidar_hs_streams_{HALF:.0f}.png")
Image.fromarray(img).resize((1200, 1200)).save(OUT + f"LIDAR_ombrage_ruisseaux_{HALF:.0f}m.jpg", quality=88)
json.dump({"BB": BB, "DLAT": DLAT, "DLON": DLON, "RES": RES, "n": n}, open(SCR + f"lidar_meta_{HALF:.0f}.json", "w"))
print("ruisseaux (≥ 2 ha) :", int(stream.sum()), "cellules ;", "ombrage →", OUT + f"LIDAR_ombrage_ruisseaux_{HALF:.0f}m.jpg")
