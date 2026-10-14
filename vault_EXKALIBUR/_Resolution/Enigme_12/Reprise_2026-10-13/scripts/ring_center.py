"""Variante de ring_all.py pour un centre quelconque (variable CENTER="lat,lon"), sans visibilité.
Toutes les jonctions de chemins (BD TOPO + OSM) autour du centre, croisées avec
le champ de vision réel (MNS LiDAR HD), l'ouverture du couvert (clairière), le bâti et les cours d'eau.
Usage : python3 ring_all.py DATA_DEM DATA_CALC [dmin dmax]"""
import json, math, sys, os
import numpy as np
from scipy.spatial import cKDTree as KD
DEM, CALC = sys.argv[1], sys.argv[2]
DMIN = float(sys.argv[3]) if len(sys.argv) > 3 else 1780; DMAX = float(sys.argv[4]) if len(sys.argv) > 4 else 1920
TA = tuple(map(float, os.environ.get('CENTER', '45.428888,6.031015').split(',')))
KX = math.cos(math.radians(TA[0])) * 111320.0; KY = 111132.0
xy = lambda lat, lon: ((lon - TA[1]) * KX, (lat - TA[0]) * KY)
ll = lambda x, y: (TA[0] + y / KY, TA[1] + x / KX)
tx, ty = 0.0, 0.0
def polar(x, y):
    dx, dy = x - tx, y - ty
    return (math.degrees(math.atan2(dx, dy)) + 360) % 360, math.hypot(dx, dy)
def seen(x, y, rad=10, grid=None):
    return float('nan')
M = json.load(open(os.path.join(DEM, 'dem2m.json')))
DTM = np.load(os.path.join(DEM, 'dem2m.npy')); MNS = np.load(os.path.join(DEM, 'mns2m.npy'))
def canopy_stats(x, y, rad):
    lat, lon = ll(x, y)
    i = (M['LA1'] - lat) / M['DLAT'] - 0.5; j = (lon - M['LO0']) / M['DLON'] - 0.5
    ri = int(rad / 2.0) + 1
    I, J = np.mgrid[int(i) - ri:int(i) + ri + 1, int(j) - ri:int(j) + ri + 1]
    I = np.clip(I, 0, DTM.shape[0] - 1); J = np.clip(J, 0, DTM.shape[1] - 1)
    d = np.hypot((I - i) * M['DLAT'] * KY, (J - j) * M['DLON'] * KX)
    m = d <= rad
    h = (MNS[I, J] - DTM[I, J])[m]
    return float((h < 2).mean()), float((h > 8).mean())
lines = lambda g: [g['coordinates']] if g['type'] == 'LineString' else (g['coordinates'] if g['type'] == 'MultiLineString' else [])
# --- jonctions BD TOPO (extrémités de tronçons partagées par >= 3 tronçons)
deg, kind = {}, {}
for f in json.load(open(os.path.join(CALC, 'troncon_de_route.json'))):
    n = f['properties']['nature']
    for l in lines(f['geometry']):
        for p in (l[0], l[-1]):
            q = xy(p[1], p[0]); k = (round(q[0] / 2), round(q[1] / 2))
            deg[k] = deg.get(k, 0) + 1; kind.setdefault(k, []).append('BDT:' + n)
J = [((k[0] * 2.0, k[1] * 2.0), kind[k]) for k, v in deg.items() if v >= 3]
# --- jonctions OSM (nœuds de degré >= 3 dans le graphe des voies)
osm = json.load(open(os.path.join(CALC, 'osm.json')))['elements']
nb, pos, okind = {}, {}, {}
for w in osm:
    if w['type'] != 'way' or 'highway' not in w.get('tags', {}): continue
    ids, geo = w.get('nodes'), w.get('geometry')
    if not ids or not geo: continue
    for a, g in zip(ids, geo): pos[a] = xy(g['lat'], g['lon']); okind.setdefault(a, set()).add('OSM:' + w['tags']['highway'])
    for a, b in zip(ids, ids[1:]):
        nb.setdefault(a, set()).add(b); nb.setdefault(b, set()).add(a)
J += [(pos[a], sorted(okind[a])) for a, s in nb.items() if len(s) >= 3]
# fusion des jonctions à moins de 15 m
pts = np.array([p for p, _ in J]); used = np.zeros(len(J), bool); tree = KD(pts); merged = []
for i in range(len(J)):
    if used[i]: continue
    grp = tree.query_ball_point(pts[i], 15); used[grp] = True
    merged.append((pts[grp].mean(0), sorted(set(sum([list(J[g][1]) for g in grp], [])))))
# --- bâti, eau
B = []
for f in json.load(open(os.path.join(CALC, 'batiment.json'))):
    g = f['geometry']; rings = [g['coordinates'][0]] if g['type'] == 'Polygon' else [p[0] for p in g['coordinates']]
    for r in rings: B += [xy(p[1], p[0]) for p in r]
W = []
for f in json.load(open(os.path.join(CALC, 'troncon_hydrographique.json'))):
    for l in lines(f['geometry']):
        for a, b in zip(l, l[1:]):
            A, Bp = np.array(xy(a[1], a[0])), np.array(xy(b[1], b[0])); n = max(1, int(np.hypot(*(Bp - A)) / 5))
            W += [A + (Bp - A) * t / n for t in range(n + 1)]
for w in osm:
    if w['type'] == 'way' and 'waterway' in w.get('tags', {}) and w.get('geometry'):
        g = w['geometry']
        for a, b in zip(g, g[1:]):
            A, Bp = np.array(xy(a['lat'], a['lon'])), np.array(xy(b['lat'], b['lon'])); n = max(1, int(np.hypot(*(Bp - A)) / 5))
            W += [A + (Bp - A) * t / n for t in range(n + 1)]
tB, tW = KD(np.array(B)), KD(np.array(W))
rows = []
for p, kinds in merged:
    a, d = polar(*p)
    if not (DMIN <= d <= DMAX): continue
    lat, lon = ll(*p)
    open20, tall60 = canopy_stats(p[0], p[1], 20)[0], canopy_stats(p[0], p[1], 60)[1]
    rows.append(dict(lat=round(lat, 6), lon=round(lon, 6), d=round(d, 1), az=round(a, 1), vis0=float('nan'), vis17=float('nan'),
                     open20=round(open20, 2), tall60=round(tall60, 2), bat=round(tB.query(p)[0]), eau=round(tW.query(p)[0]), kinds=kinds))
rows.sort(key=lambda r: r['az'])
print('az     d(m)   lat        lon       vis_sol vis_1.7 ouvert20 arbres60 bât  eau  types')
for r in rows:
    flag = '±1%' if abs(r['d'] - 1850) <= 18.5 else '   '
    print('%5.1f %6.1f %s %.6f %.6f  %4.2f   %4.2f    %4.2f     %4.2f   %4d %4d  %s' % (r['az'], r['d'], flag, r['lat'], r['lon'], r['vis0'], r['vis17'], r['open20'], r['tall60'], r['bat'], r['eau'], ','.join(r['kinds'])[:90]))
json.dump(rows, open(os.environ.get('OUT', 'ring_center.json'), 'w'))
