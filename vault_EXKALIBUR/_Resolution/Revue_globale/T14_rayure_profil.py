"""[T14, 01/10] Rayure de la lame lue comme PROFIL ALTIMÉTRIQUE (x(y) = altitude le long d'un trajet de 1 850 m = 10 stades).
Hypothèse de Guilhem : la rayure aide (pas forcément un ruisseau). Variante 'profil' : l'écart horizontal du tracé
SVG à son axe = altitude relative ; on cherche sur le MNT LiDAR 2 m un trajet rectiligne de 1 850 m dont le profil corrèle.
Témoins : marches aléatoires de même longueur. Aucune conclusion sans comparaison aux témoins."""
import numpy as np, math, re, json, time
from scipy.ndimage import map_coordinates
RG = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/"
E = r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/"
d = re.search(r' d="([^"]+)"', open(RG + "rayure_epee_guilhem.svg", encoding="utf-8").read()).group(1)
toks = re.findall(r"[MLHVCZ]|-?\d+\.?\d*", d)
subs = []; cur = []; x = y = 0; i = 0; cmd = None
while i < len(toks):
    t = toks[i]
    if t in "MLHVCZ": cmd = t; i += 1; continue
    if cmd == "M":
        if cur: subs.append(cur)
        x, y = float(toks[i]), float(toks[i + 1]); cur = [(x, y)]; i += 2; cmd = "L"
    elif cmd == "L": x, y = float(toks[i]), float(toks[i + 1]); cur.append((x, y)); i += 2
    elif cmd == "H": x = float(toks[i]); cur.append((x, y)); i += 1
    elif cmd == "V": y = float(toks[i]); cur.append((x, y)); i += 1
    elif cmd == "C": x, y = float(toks[i + 4]), float(toks[i + 5]); cur.append((x, y)); i += 6
subs.append(cur)
Z = np.load(E + "mnt_1500_2.npy"); BB = json.load(open(E + "lidar_meta_1500.json"))["BB"]  # [latmin,lonmin,latmax,lonmax]
lat0, lon0 = 45.4288, 6.03078
KX = math.cos(math.radians(lat0)) * 111320; KY = 110540
cx = (lon0 - BB[1]) * KX; cy = (lat0 - BB[0]) * KY; res = 2.0
trunk = np.array(subs[2]); stem = np.array(subs[0])[::-1]
full = np.vstack([trunk, stem[1:]])
ys = np.linspace(0, 837, 64); xs = np.interp(ys, full[:, 1], full[:, 0])
zf = lambda a: (a - a.mean()) / a.std()
prof = zf(xs); detr = zf(xs - np.polyval(np.polyfit(ys, xs, 1), ys))

def search(P, L, step=60, bstep=4, rad=1400):
    sx = np.arange(-rad, rad + 1, step); X0, Y0 = np.meshgrid(sx, sx); X0 = X0.ravel(); Y0 = Y0.ravel()
    t = np.linspace(0, 1, len(P)); best = (-9,); am = []
    for b in range(0, 360, bstep):
        a = math.radians(b); dx, dy = math.sin(a), math.cos(a)
        PX = cx + X0[:, None] + t[None, :] * L * dx; PY = cy + Y0[:, None] + t[None, :] * L * dy
        row = (Z.shape[0] - 1) - PY / res; col = PX / res
        ok = (row.min(1) > 0) & (row.max(1) < Z.shape[0] - 1) & (col.min(1) > 0) & (col.max(1) < Z.shape[1] - 1)
        T = map_coordinates(Z, [row.ravel(), col.ravel()], order=1, mode="nearest").reshape(PX.shape)
        sd = T.std(1); ok &= sd > 4
        pz = (T - T.mean(1, keepdims=True)) / np.where(sd > 0, sd, 1)[:, None]
        c = (pz * P[None, :]).mean(1); c[~ok] = -9
        k = c.argmax(); am.append(c[k])
        if c[k] > best[0]: best = (c[k], b, X0[k], Y0[k])
    return best, np.array(am)

if __name__ == "__main__":
    t0 = time.time()
    print("SVG : tronc+queue", len(full), "pts ; corr x~y =", round(np.corrcoef(xs, ys)[0, 1], 3))
    for nm, P in (("x(y) brut", prof), ("sans tendance", detr), ("miroir", -prof), ("inversé", prof[::-1])):
        b, am = search(P, 1850)
        print(f"{nm:14s} corr max={b[0]:.3f} cap={b[1]:3d} départ=({lat0 + b[3] / KY:.5f},{lon0 + b[2] / KX:.5f}) médiane par cap={np.median(am):.3f}", flush=True)
    rng = np.random.default_rng(1); mx = []
    for k in range(8):
        w = zf(np.cumsum(rng.normal(size=64))); mx.append(search(w, 1850)[0][0])
    print("TÉMOINS marche aléatoire corr max :", np.round(mx, 3), " moyenne", round(float(np.mean(mx)), 3))
    print(round(time.time() - t0), "s")
