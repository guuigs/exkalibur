"""Tronçons de cours d'eau visibles depuis le sommet du donjon (MNS LiDAR HD), avec cap et distance.
Un ruisseau que « l'astre glorieux magnifiait » doit être vu depuis le rempart."""
import numpy as np, json, math, sys, os
from geographiclib.geodesic import Geodesic
G = Geodesic.WGS84
DEM, CALC = sys.argv[1], sys.argv[2]
V = np.load(os.path.join(DEM, 'vis_polar.npz')); VIS0, CAN, top = V['VIS0'], V['CAN'], V['top']
lines = lambda g: [g['coordinates']] if g['type'] == 'LineString' else (g['coordinates'] if g['type'] == 'MultiLineString' else [])
segs = []
for f in json.load(open(os.path.join(CALC, 'troncon_hydrographique.json'))):
    p = f['properties']; nm = p.get('cpx_toponyme_cours_d_eau') or p.get('toponyme') or ''
    for l in lines(f['geometry']): segs.append(('BDT', nm, p.get('persistance'), [(q[1], q[0]) for q in l]))
for w in json.load(open(os.path.join(CALC, 'osm.json')))['elements']:
    if w['type'] == 'way' and 'waterway' in w.get('tags', {}) and w.get('geometry'):
        segs.append(('OSM', w['tags'].get('name', ''), w['tags'].get('intermittent', ''), [(g['lat'], g['lon']) for g in w['geometry']]))
out = {}
for src, nm, pers, pts in segs:
    for a, b in zip(pts, pts[1:]):
        L = G.Inverse(*a, *b)['s12']; n = max(1, int(L / 3))
        for t in range(n + 1):
            la = a[0] + (b[0] - a[0]) * t / n; lo = a[1] + (b[1] - a[1]) * t / n
            r = G.Inverse(top[0], top[1], la, lo); ia = int(round((r['azi1'] % 360) / 0.05)) % VIS0.shape[0]; ir = int(round(r['s12'])) - 1
            if not (0 <= ir < VIS0.shape[1]) or r['s12'] < 300: continue
            if VIS0[ia, ir]:
                key = (nm or '(sans nom)', round(r['azi1'] % 360), round(r['s12'] / 50) * 50)
                out.setdefault(key, []).append((la, lo, src))
rows = sorted(out.items(), key=lambda kv: (kv[0][1], kv[0][2]))
print('cours d\'eau visibles (par cap arrondi et tranche de 50 m) :')
for (nm, az, d), v in rows:
    print('  cap %3d°  ~%4d m  %-28s %3d points  ex. %.5f %.5f (%s)' % (az, d, nm[:28], len(v), v[0][0], v[0][1], v[0][2]))
