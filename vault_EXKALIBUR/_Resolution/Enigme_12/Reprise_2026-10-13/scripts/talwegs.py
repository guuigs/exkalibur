"""Réseau d'écoulement (D8, après comblement des cuvettes) sur le MNT LiDAR 2 m autour d'un point,
pour repérer les ruisseaux non cartographiés. Sortie : image + liste des talwegs proches du point."""
import numpy as np, json, math, heapq, sys, os
from PIL import Image, ImageDraw
DEM = sys.argv[1]; lat0, lon0 = float(sys.argv[2]), float(sys.argv[3]); half = float(sys.argv[4]); out = sys.argv[5]
M = json.load(open(os.path.join(DEM, 'dem2m.json'))); Z = np.load(os.path.join(DEM, 'dem2m.npy')).astype(np.float64)
ci = int((M['LA1'] - lat0) / M['DLAT']); cj = int((lon0 - M['LO0']) / M['DLON']); h = int(half / 2)
z = Z[ci - h:ci + h, cj - h:cj + h].copy(); n, m = z.shape
# comblement (priority-flood)
filled = np.full_like(z, np.inf); seen = np.zeros_like(z, bool); pq = []
for i in range(n):
    for j in (0, m - 1): heapq.heappush(pq, (z[i, j], i, j)); seen[i, j] = True
for j in range(m):
    for i in (0, n - 1):
        if not seen[i, j]: heapq.heappush(pq, (z[i, j], i, j)); seen[i, j] = True
nb = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
while pq:
    v, i, j = heapq.heappop(pq); filled[i, j] = v
    for di, dj in nb:
        a, b = i + di, j + dj
        if 0 <= a < n and 0 <= b < m and not seen[a, b]:
            seen[a, b] = True; heapq.heappush(pq, (max(z[a, b], v + 1e-4), a, b))
# directions D8
dirs = np.full((n, m), -1, int)
for k, (di, dj) in enumerate(nb):
    pass
best = np.zeros((n, m)); 
for k, (di, dj) in enumerate(nb):
    sh = np.full((n, m), np.inf)
    a0, a1 = max(0, -di), n - max(0, di); b0, b1 = max(0, -dj), m - max(0, dj)
    sh[a0:a1, b0:b1] = filled[a0 + di:a1 + di, b0 + dj:b1 + dj]
    slope = (filled - sh) / math.hypot(di, dj)
    upd = slope > best
    best[upd] = slope[upd]; dirs[upd] = k
# accumulation
order = np.argsort(-filled, axis=None); acc = np.ones(n * m)
for idx in order:
    k = dirs.flat[idx]
    if k < 0: continue
    i, j = divmod(idx, m); a, b = i + nb[k][0], j + nb[k][1]
    if 0 <= a < n and 0 <= b < m: acc[a * m + b] += acc[idx]
acc = acc.reshape(n, m) * 4.0  # m² drainés
# image
gy, gx = np.gradient(z, 2.0); sh = np.clip(0.55 + 0.5 * (-gx * 0.7 + gy * 0.7) / np.sqrt(1 + gx ** 2 + gy ** 2), 0, 1)
rgb = np.stack([sh * 255] * 3, -1)
for thr, col in ((20000, (120, 170, 255)), (60000, (40, 110, 255)), (200000, (0, 40, 200))):
    rgb[acc >= thr] = col
im = Image.fromarray(rgb.astype(np.uint8)); d = ImageDraw.Draw(im)
d.ellipse([h - 6, h - 6, h + 6, h + 6], outline=(255, 0, 0), width=3)
for la, lo, lab in json.loads(os.environ.get('PTS', '[]')):
    i = int((M['LA1'] - la) / M['DLAT']) - (ci - h); j = int((lo - M['LO0']) / M['DLON']) - (cj - h)
    d.rectangle([j - 5, i - 5, j + 5, i + 5], outline=(0, 160, 0), width=2); d.text((j + 7, i - 6), lab, fill=(0, 120, 0))
im = im.resize((m * 2, n * 2), Image.NEAREST); im.save(out, quality=88)
# talwegs proches du point central
ii, jj = np.nonzero(acc >= 20000)
dd = np.hypot((ii - h) * 2.0, (jj - h) * 2.0)
o = np.argsort(dd)[:15]
print('cellules de talweg (bassin >= 2 ha) les plus proches du point :')
for k in o:
    la = M['LA1'] - (ci - h + ii[k] + 0.5) * M['DLAT']; lo = M['LO0'] + (cj - h + jj[k] + 0.5) * M['DLON']
    print('  %.0f m  bassin %.1f ha  alt %.1f m  %.5f %.5f' % (dd[k], acc[ii[k], jj[k]] / 1e4, z[ii[k], jj[k]], la, lo))
