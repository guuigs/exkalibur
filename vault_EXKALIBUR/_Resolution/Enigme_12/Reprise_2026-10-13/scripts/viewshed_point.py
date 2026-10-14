"""Champ de vision réel depuis un point au sol quelconque (variable VIEW="lat,lon", œil à EYEH m au-dessus du MNT ;
NEAR = rayon en m sous lequel on ignore les obstacles, défaut 6). Variante de viewshed_mns.py.
Obstacles = MNS LiDAR HD (sol + arbres + bâtiments), cible = MNT (sol) + h.
Données : WMS-R IGN, grille 2 m (getdem.py / getmns.py), stockées hors dépôt (DATA).
Sortie : vis_polar.npz (rayons tous les 0,05°, pas de 1 m jusqu'à 2 700 m)."""
import numpy as np, json, math, sys, os
DATA = sys.argv[1] if len(sys.argv) > 1 else '.'
M = json.load(open(os.path.join(DATA, 'dem2m.json')))
DTM = np.load(os.path.join(DATA, 'dem2m.npy')).astype(np.float64)
MNS = np.load(os.path.join(DATA, 'mns2m.npy')).astype(np.float64)
OBS = MNS if os.environ.get('OBST', 'mns') == 'mns' else DTM   # obstacles : MNS (arbres) ou MNT (relief seul)
LA1, LO0, DLAT, DLON = M['LA1'], M['LO0'], M['DLAT'], M['DLON']
TA = (45.428888, 6.031015)   # centroïde BD TOPO « Tour, donjon » (h 34,5 m)
KX = math.cos(math.radians(TA[0])) * 111320.0; KY = 111132.0

def idx(lat, lon):  # indices fractionnaires (centres de pixels)
    return (LA1 - lat) / DLAT - 0.5, (lon - LO0) / DLON - 0.5

def bilin(Z, fi, fj):
    i0 = np.clip(np.floor(fi).astype(int), 0, Z.shape[0] - 2); j0 = np.clip(np.floor(fj).astype(int), 0, Z.shape[1] - 2)
    di = fi - i0; dj = fj - j0
    return (Z[i0, j0] * (1 - di) * (1 - dj) + Z[i0 + 1, j0] * di * (1 - dj) + Z[i0, j0 + 1] * (1 - di) * dj + Z[i0 + 1, j0 + 1] * di * dj)

top_lat, top_lon = map(float, os.environ['VIEW'].split(','))
fi, fj = idx(top_lat, top_lon)
z_gnd = float(bilin(DTM, np.array([fi]), np.array([fj]))[0])
z0 = z_gnd + float(os.environ.get('EYEH', '1.7'))
NEAR = float(os.environ.get('NEAR', '6'))
print('observateur %.6f %.6f sol %.2f m oeil %.2f m' % (top_lat, top_lon, z_gnd, z0))
AZ = np.arange(0, 360, 0.05); R = np.arange(1.0, 2701.0, 1.0)
Rc = (1 - 0.13) * R ** 2 / (2 * 6371000.0)
VIS0 = np.zeros((AZ.size, R.size), np.uint8); VIS17 = np.zeros_like(VIS0); CAN = np.zeros((AZ.size, R.size), np.float32)
for a0 in range(0, AZ.size, 400):
    az = np.radians(AZ[a0:a0 + 400])[:, None]
    x = R[None, :] * np.sin(az); y = R[None, :] * np.cos(az)
    lat = top_lat + y / KY; lon = top_lon + x / KX
    fi, fj = idx(lat, lon)
    s = bilin(OBS, fi, fj) - Rc; g = bilin(DTM, fi, fj) - Rc
    o = (s - z0) / R; o[:, R < NEAR] = -np.inf
    # obstacle max jusqu'à r-3 m (on exclut la cible elle-même)
    O = np.maximum.accumulate(o, axis=1); O = np.concatenate([np.full((o.shape[0], 3), -np.inf), O[:, :-3]], axis=1)
    VIS0[a0:a0 + 400] = ((g + 0.3 - z0) / R >= O)
    VIS17[a0:a0 + 400] = ((g + 1.7 - z0) / R >= O)
    CAN[a0:a0 + 400] = (s - g)
np.savez_compressed(os.path.join(DATA, os.environ.get('OUT', 'vis_polar.npz')), VIS0=VIS0, VIS17=VIS17, CAN=CAN, AZ=AZ, R=R, top=np.array([top_lat, top_lon, z0]))
for d0, d1 in [(0, 500), (500, 1000), (1000, 1500), (1500, 1832), (1832, 1868), (1868, 2300)]:
    m = (R >= d0) & (R < d1)
    print('%4d-%4d m : sol visible %.2f %%  (personne 1,7 m : %.2f %%)' % (d0, d1, 100 * VIS0[:, m].mean(), 100 * VIS17[:, m].mean()))
