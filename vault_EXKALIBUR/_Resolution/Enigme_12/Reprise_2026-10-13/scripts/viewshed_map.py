"""Carte du champ de vision (sol visible depuis le sommet du donjon) sur ombrage MNT, anneau 1 850 m ± 1 %."""
import numpy as np, json, math, sys, os
from PIL import Image, ImageDraw
DEM = sys.argv[1]; OUT = sys.argv[2]; NPZ = sys.argv[3] if len(sys.argv) > 3 else 'vis_polar.npz'
M = json.load(open(os.path.join(DEM, 'dem2m.json'))); DTM = np.load(os.path.join(DEM, 'dem2m.npy')); MNS = np.load(os.path.join(DEM, 'mns2m.npy'))
V = np.load(os.path.join(DEM, NPZ)); VIS0, top = V['VIS0'], V['top']
NY, NX = DTM.shape
lat = M['LA1'] - (np.arange(NY) + 0.5) * M['DLAT']; lon = M['LO0'] + (np.arange(NX) + 0.5) * M['DLON']
KX = math.cos(math.radians(top[0])) * 111320.0; KY = 111132.0
X = (lon[None, :] - top[1]) * KX; Y = (lat[:, None] - top[0]) * KY
R = np.hypot(X, Y); A = (np.degrees(np.arctan2(X, Y)) + 360) % 360
ia = np.round(A / 0.05).astype(int) % VIS0.shape[0]; ir = np.round(R).astype(int) - 1
ok = (ir >= 0) & (ir < VIS0.shape[1])
vis = np.zeros_like(DTM, bool); vis[ok] = VIS0[ia[ok], ir[ok]] > 0
gy, gx = np.gradient(DTM, 2.0); sh = np.clip(0.6 + 0.5 * (-gx * 0.7 + gy * 0.7) / np.sqrt(1 + gx ** 2 + gy ** 2), 0, 1)
canopy = (MNS - DTM) > 4
rgb = np.stack([sh * 255] * 3, -1)
rgb[canopy] = rgb[canopy] * np.array([0.55, 0.8, 0.55])
rgb[vis] = np.array([230, 40, 40])
ring = np.abs(R - 1850) <= 18.5
rgb[ring & ~vis] = rgb[ring & ~vis] * 0.5 + np.array([0, 0, 255]) * 0.5
im = Image.fromarray(rgb.astype(np.uint8))
d = ImageDraw.Draw(im)
def px(la, lo): return ((lo - M['LO0']) / M['DLON'], (M['LA1'] - la) / M['DLAT'])
for name, la, lo in json.loads(os.environ.get('PTS', '[]')):
    x, y = px(la, lo); d.ellipse([x - 9, y - 9, x + 9, y + 9], outline=(255, 255, 0), width=3); d.text((x + 11, y - 6), name, fill=(255, 255, 0))
x, y = px(top[0], top[1]); d.rectangle([x - 6, y - 6, x + 6, y + 6], fill=(0, 0, 0))
crop = os.environ.get('CROP')
if crop: im = im.crop(tuple(int(v) for v in crop.split(',')))
im.save(OUT, quality=85)
print(im.size)
