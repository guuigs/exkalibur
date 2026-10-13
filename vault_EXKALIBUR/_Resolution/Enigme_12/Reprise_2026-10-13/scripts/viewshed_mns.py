"""Champ de vision réel depuis le sommet de la tour d'Avalon.
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

# sommet de la tour : max du MNS à moins de 10 m du point de référence
fi, fj = idx(*TA); I, J = np.mgrid[int(fi) - 6:int(fi) + 7, int(fj) - 6:int(fj) + 7]
w = MNS[I, J]; k = np.unravel_index(np.argmax(w), w.shape)
ti, tj = I[k], J[k]
top_lat = LA1 - (ti + 0.5) * DLAT; top_lon = LO0 + (tj + 0.5) * DLON
z_top = MNS[ti, tj]; z_gnd = DTM[ti, tj]
print('sommet MNS %.2f m (sol %.2f m, hauteur %.1f m) en %.6f %.6f' % (z_top, z_gnd, z_top - z_gnd, top_lat, top_lon))
EYE = float(os.environ.get('EYE', '-1.0'))   # œil ≈ 1 m sous le point le plus haut du MNS (parapet)
z0 = z_top + EYE
AZ = np.arange(0, 360, 0.05); R = np.arange(1.0, 2701.0, 1.0)
Rc = (1 - 0.13) * R ** 2 / (2 * 6371000.0)
VIS0 = np.zeros((AZ.size, R.size), np.uint8); VIS17 = np.zeros_like(VIS0); CAN = np.zeros((AZ.size, R.size), np.float32)
for a0 in range(0, AZ.size, 400):
    az = np.radians(AZ[a0:a0 + 400])[:, None]
    x = R[None, :] * np.sin(az); y = R[None, :] * np.cos(az)
    lat = top_lat + y / KY; lon = top_lon + x / KX
    fi, fj = idx(lat, lon)
    s = bilin(OBS, fi, fj) - Rc; g = bilin(DTM, fi, fj) - Rc
    o = (s - z0) / R; o[:, R < 6] = -np.inf          # le parapet de la tour n'est pas un obstacle
    # obstacle max jusqu'à r-3 m (on exclut la cible elle-même)
    O = np.maximum.accumulate(o, axis=1); O = np.concatenate([np.full((o.shape[0], 3), -np.inf), O[:, :-3]], axis=1)
    VIS0[a0:a0 + 400] = ((g + 0.3 - z0) / R >= O)
    VIS17[a0:a0 + 400] = ((g + 1.7 - z0) / R >= O)
    CAN[a0:a0 + 400] = (s - g)
np.savez_compressed(os.path.join(DATA, os.environ.get('OUT', 'vis_polar.npz')), VIS0=VIS0, VIS17=VIS17, CAN=CAN, AZ=AZ, R=R, top=np.array([top_lat, top_lon, z0]))
for d0, d1 in [(0, 500), (500, 1000), (1000, 1500), (1500, 1832), (1832, 1868), (1868, 2300)]:
    m = (R >= d0) & (R < d1)
    print('%4d-%4d m : sol visible %.2f %%  (personne 1,7 m : %.2f %%)' % (d0, d1, 100 * VIS0[:, m].mean(), 100 * VIS17[:, m].mean()))
