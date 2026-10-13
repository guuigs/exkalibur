"""Zones de sol visibles depuis le sommet du donjon (MNS LiDAR HD), regroupées en taches,
avec distance au bâti, au chemin le plus proche, à la jonction la plus proche et au cours d'eau."""
import numpy as np, json, math, sys, os
from scipy import ndimage
from scipy.spatial import cKDTree as KD
DEM, CALC = sys.argv[1], sys.argv[2]
AZ0, AZ1 = float(sys.argv[3]), float(sys.argv[4]); RMIN, RMAX = float(sys.argv[5]), float(sys.argv[6])
M = json.load(open(os.path.join(DEM, 'dem2m.json'))); DTM = np.load(os.path.join(DEM, 'dem2m.npy')); MNS = np.load(os.path.join(DEM, 'mns2m.npy'))
V = np.load(os.path.join(DEM, 'vis_polar.npz')); VIS0, top = V['VIS0'], V['top']
NY, NX = DTM.shape
lat = M['LA1'] - (np.arange(NY) + 0.5) * M['DLAT']; lon = M['LO0'] + (np.arange(NX) + 0.5) * M['DLON']
KX = math.cos(math.radians(top[0])) * 111320.0; KY = 111132.0
X = (lon[None, :] - top[1]) * KX; Y = (lat[:, None] - top[0]) * KY
R = np.hypot(X, Y); A = (np.degrees(np.arctan2(X, Y)) + 360) % 360
ia = np.round(A / 0.05).astype(int) % VIS0.shape[0]; ir = np.round(R).astype(int) - 1
ok = (ir >= 0) & (ir < VIS0.shape[1])
vis = np.zeros_like(DTM, bool); vis[ok] = VIS0[ia[ok], ir[ok]] > 0
sel = vis & (R >= RMIN) & (R <= RMAX) & (A >= AZ0) & (A <= AZ1) & ((MNS - DTM) < 2)
lab, n = ndimage.label(ndimage.binary_closing(sel, iterations=2) & sel | sel)
xy = lambda la, lo: ((lo - top[1]) * KX, (la - top[0]) * KY)
lines = lambda g: [g['coordinates']] if g['type'] == 'LineString' else (g['coordinates'] if g['type'] == 'MultiLineString' else [])
B = []
for f in json.load(open(os.path.join(CALC, 'batiment.json'))):
    g = f['geometry']; rings = [g['coordinates'][0]] if g['type'] == 'Polygon' else [p[0] for p in g['coordinates']]
    for r in rings: B += [xy(p[1], p[0]) for p in r]
tB = KD(np.array(B))
P = []
for f in json.load(open(os.path.join(CALC, 'troncon_de_route.json'))):
    if f['properties']['nature'] not in ('Chemin', 'Sentier', 'Route empierrée'): continue
    for l in lines(f['geometry']):
        for a, b in zip(l, l[1:]):
            A0, B0 = np.array(xy(a[1], a[0])), np.array(xy(b[1], b[0])); k = max(1, int(np.hypot(*(B0 - A0)) / 4))
            P += [A0 + (B0 - A0) * t / k for t in range(k + 1)]
for w in json.load(open(os.path.join(CALC, 'osm.json')))['elements']:
    if w['type'] == 'way' and w.get('tags', {}).get('highway') in ('path', 'track', 'footway', 'bridleway') and w.get('geometry'):
        g = w['geometry']
        for a, b in zip(g, g[1:]):
            A0, B0 = np.array(xy(a['lat'], a['lon'])), np.array(xy(b['lat'], b['lon'])); k = max(1, int(np.hypot(*(B0 - A0)) / 4))
            P += [A0 + (B0 - A0) * t / k for t in range(k + 1)]
tP = KD(np.array(P))
J = json.load(open(os.path.join(DEM, 'ring_all_250_2600.json')))
tJ = KD(np.array([xy(j['lat'], j['lon']) for j in J]))
W = []
for f in json.load(open(os.path.join(CALC, 'troncon_hydrographique.json'))):
    for l in lines(f['geometry']): W += [xy(p[1], p[0]) for p in l]
tW = KD(np.array(W))
rows = []
for k in range(1, n + 1):
    m = lab == k; area = m.sum() * (M['DLAT'] * KY) * (M['DLON'] * KX)
    if area < 150: continue
    yy, xx = np.nonzero(m); cx, cy = X[0, xx].mean(), Y[yy, 0].mean()
    dB = tB.query([cx, cy])[0]; dP = tP.query([cx, cy])[0]; dJ, jj = tJ.query([cx, cy]); dW = tW.query([cx, cy])[0]
    rows.append(dict(lat=top[0] + cy / KY, lon=top[1] + cx / KX, d=math.hypot(cx, cy), az=(math.degrees(math.atan2(cx, cy)) + 360) % 360, area=area, bat=dB, chemin=dP, jonction=dJ, eau=dW))
rows.sort(key=lambda r: -r['area'])
print('taches visibles (sol ouvert) az %g-%g, %g-%g m : %d' % (AZ0, AZ1, RMIN, RMAX, len(rows)))
print('   az    d(m)   surface  bât  chemin jonction eau   lat lon')
for r in sorted(rows, key=lambda r: r['az']):
    print('%5.1f %6.0f %7.0f m2 %4.0f %5.0f %6.0f %6.0f   %.5f %.5f %s' % (r['az'], r['d'], r['area'], r['bat'], r['chemin'], r['jonction'], r['eau'], r['lat'], r['lon'], '<-- loin du bâti, près d\'un chemin' if r['bat'] >= 80 and r['chemin'] <= 30 else ''))
json.dump(rows, open(os.path.join(DEM, 'patches_%g_%g.json' % (AZ0, AZ1)), 'w'))
