"""LiDAR HD 0,5 m (MNT) autour de la 3e porte : ombrage multidirectionnel, talwegs (D8 sur MNT lissé),
blocs rocheux candidats (bosses compactes de 1,5 à 6 m au-dessus du sol lissé, près d'un talweg)."""
import numpy as np, json, math, heapq, sys, os
from scipy import ndimage
from PIL import Image, ImageDraw
D = sys.argv[1]; CALC = sys.argv[2]; OUT = sys.argv[3]
M = json.load(open(os.path.join(D, 'mnt05.json'))); Z = np.load(os.path.join(D, 'mnt05.npy')).astype(np.float64)
S = np.load(os.path.join(D, 'mns05.npy')).astype(np.float64)
N = Z.shape[0]; R = M['RES']
def ij(lat, lon): return (M['LA1'] - lat) / M['DLAT'], (lon - M['LO0']) / M['DLON']
def ll(i, j): return M['LA1'] - i * M['DLAT'], M['LO0'] + j * M['DLON']
Zf = ndimage.gaussian_filter(Z, 1.0)
# ombrage multidirectionnel
gy, gx = np.gradient(Zf, R)
hs = np.zeros_like(Z)
for az in (315, 270, 225, 0):
    a = math.radians(az); alt = math.radians(35)
    hs += np.clip(math.sin(alt) + math.cos(alt) * (-gx * math.sin(a) + gy * math.cos(a)), 0, None) / np.sqrt(1 + gx ** 2 + gy ** 2)
hs = np.clip(hs / 4 * 255 * 1.4, 0, 255)
# talwegs : D8 sur MNT lissé (sigma 3 px), sous-échantillonné à 1 m pour la vitesse
Zc = ndimage.gaussian_filter(Z, 3.0)[::2, ::2]; n = Zc.shape[0]
filled = np.full_like(Zc, np.inf); seen = np.zeros_like(Zc, bool); pq = []
for i in range(n):
    for j in (0, n - 1): heapq.heappush(pq, (Zc[i, j], i, j)); seen[i, j] = True
for j in range(n):
    for i in (0, n - 1):
        if not seen[i, j]: heapq.heappush(pq, (Zc[i, j], i, j)); seen[i, j] = True
nb = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
while pq:
    v, i, j = heapq.heappop(pq); filled[i, j] = v
    for di, dj in nb:
        a, b = i + di, j + dj
        if 0 <= a < n and 0 <= b < n and not seen[a, b]:
            seen[a, b] = True; heapq.heappush(pq, (max(Zc[a, b], v + 1e-5), a, b))
best = np.zeros_like(Zc); dirs = np.full(Zc.shape, -1, int)
for k, (di, dj) in enumerate(nb):
    sh = np.full_like(Zc, np.inf); a0, a1 = max(0, -di), n - max(0, di); b0, b1 = max(0, -dj), n - max(0, dj)
    sh[a0:a1, b0:b1] = filled[a0 + di:a1 + di, b0 + dj:b1 + dj]
    sl = (filled - sh) / math.hypot(di, dj); u = sl > best; best[u] = sl[u]; dirs[u] = k
acc = np.ones(n * n); order = np.argsort(-filled, axis=None)
for idx in order:
    k = dirs.flat[idx]
    if k < 0: continue
    i, j = divmod(idx, n); a, b = i + nb[k][0], j + nb[k][1]
    if 0 <= a < n and 0 <= b < n: acc[a * n + b] += acc[idx]
acc = (acc.reshape(n, n) * 4.0)  # m² (cellules de 2x2 px = 1 m² ... 0,5 m * 2 = 1 m -> 1 m²)
acc = acc / 4.0
np.savez(os.path.join(D, 'flow05.npz'), acc=acc, dirs=dirs, filled=filled)
accF = np.kron(acc, np.ones((2, 2)))[:N, :N]
# blocs : bosse = Z - ouverture morphologique (rayon ~4 m), hauteur 1,2-8 m, surface 4-200 m², sol nu (MNS-MNT < 3 m ou bloc)
op = ndimage.grey_opening(Zf, size=(17, 17))
bump = Zf - op
lab, nl = ndimage.label(bump > 1.2)
blocs = []
for k, sl in enumerate(ndimage.find_objects(lab), 1):
    m = lab[sl] == k; area = m.sum() * R * R
    if not (4 <= area <= 250): continue
    hmax = bump[sl][m].max()
    if hmax > 8: continue
    ci, cj = ndimage.center_of_mass(m); ci += sl[0].start; cj += sl[1].start
    la, lo = ll(ci, cj)
    ii, jj = int(ci), int(cj)
    w = accF[max(0, ii - 20):ii + 21, max(0, jj - 20):jj + 21].max()  # bassin max à moins de 10 m
    blocs.append((la, lo, area, hmax, w))
rgb = np.stack([hs] * 3, -1)
for thr, col in ((3000, (130, 180, 255)), (20000, (40, 110, 255)), (100000, (0, 40, 190))):
    rgb[accF >= thr] = col
im = Image.fromarray(rgb.astype(np.uint8)); d = ImageDraw.Draw(im)
lines = lambda g: [g['coordinates']] if g['type'] == 'LineString' else (g['coordinates'] if g['type'] == 'MultiLineString' else [])
for f in json.load(open(os.path.join(CALC, 'troncon_de_route.json'))):
    for l in lines(f['geometry']):
        p = [ij(c[1], c[0])[::-1] for c in l]
        if any(0 <= x < N and 0 <= y < N for x, y in p): d.line(p, fill=(255, 150, 0), width=3)
for la, lo, area, h, w in blocs:
    i, j = ij(la, lo); r = 4 + min(12, area ** 0.5)
    d.ellipse([j - r, i - r, j + r, i + r], outline=(255, 0, 255) if w >= 3000 else (160, 0, 160), width=2)
for la, lo, lab_ in json.loads(os.environ.get('PTS', '[]')):
    i, j = ij(la, lo); d.ellipse([j - 9, i - 9, j + 9, i + 9], outline=(255, 0, 0), width=4); d.text((j + 12, i - 8), lab_, fill=(255, 0, 0))
im.save(OUT, quality=88)
blocs.sort(key=lambda b: -b[4])
print('blocs candidats près d un talweg (bassin >= 0,3 ha à moins de 10 m) :')
from geographiclib.geodesic import Geodesic
G = Geodesic.WGS84
for la, lo, area, h, w in blocs:
    if w >= 3000:
        dg = G.Inverse(45.43292, 6.05395, la, lo)
        print('  %.5f %.5f  surface %3.0f m²  haut. %.1f m  bassin %.1f ha  à %4.0f m de la 3e porte, cap %.0f°' % (la, lo, area, h, w / 1e4, dg['s12'], dg['azi1'] % 360))
