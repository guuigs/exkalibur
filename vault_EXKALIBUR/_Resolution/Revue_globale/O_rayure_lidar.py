"""Rayure de l'épée (SVG de Guilhem) vs ruisseaux FINS dérivés du LiDAR HD (MNT 2 m), 3 × 3 km autour de la tour
d'Avalon. Pré-requis : O_lidar_ruisseaux.py (fichiers mnt/acc/d8 en scratch).
Candidats : chemins d'écoulement D8 de longueur L (80 m → 2,5 km) partant de chaque cellule de ruisseau (bassin ≥ A_MIN),
hors plaine (pente moyenne ≥ 4 %). Comparaison : Procrustes (similitude, rotation libre), dans les DEUX sens de parcours
(la rayure « aurait pu être tournée de 180° », FAQ06-161). Bonus : un affluent D8 doit entrer vers 82 % du tracé, du bon côté.
Contrôle du hasard : même recherche avec le SVG en miroir (qui ne devrait pas coller mieux que l'original).
"""
import json, math, re, sys
import numpy as np
OUT = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/"
SCR = r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/"
HALF = 1500
M = json.load(open(SCR + f"lidar_meta_{HALF}.json")); RES = M["RES"]; n = M["n"]; BB = M["BB"]
Z = np.load(SCR + f"mnt_{HALF}_2.npy"); acc = np.load(SCR + f"acc_{HALF}_2.npy"); d8 = np.load(SCR + f"d8_{HALF}_2.npy")
A_MIN = float(sys.argv[1]) if len(sys.argv) > 1 else 50000.0   # 5 ha
TA = (45.4288, 6.03078)
def px2ll(r, c): return (BB[2] - (r + 0.5) * M["DLAT"], BB[1] + (c + 0.5) * M["DLON"])
nb = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
stream = acc * RES * RES >= A_MIN
# nb d'affluents « ruisseau » entrant dans chaque cellule
inflow = np.zeros(Z.shape, np.int16)
rr, cc = np.nonzero(stream)
for r, c in zip(rr, cc):
    k = d8[r, c]
    if k < 0: continue
    r2, c2 = r + nb[k][0], c + nb[k][1]
    if 0 <= r2 < n and 0 <= c2 < n: inflow[r2, c2] += 1
def path_from(r, c, Lmax):
    P = [(r, c)]; L = 0.0
    while L < Lmax:
        k = d8[r, c]
        if k < 0: break
        r2, c2 = r + nb[k][0], c + nb[k][1]
        if not (0 <= r2 < n and 0 <= c2 < n): break
        L += math.hypot(*nb[k]) * RES; r, c = r2, c2; P.append((r, c))
    return P, L

# ---- SVG ----
d = re.search(r'd="([^"]+)"', open(OUT + "rayure_epee_guilhem.svg", encoding="utf-8").read()).group(1)
toks = re.findall(r"[MLVHC]|-?\d+(?:\.\d+)?", d)
subs, cur, pos, i, cmd = [], None, (0.0, 0.0), 0, None
while i < len(toks):
    t = toks[i]
    if t in "MLVHC":
        cmd = t; i += 1
        if cmd == "M": cur = []; subs.append(cur)
        continue
    if cmd in ("M", "L"): pos = (float(toks[i]), float(toks[i + 1])); i += 2
    elif cmd == "V": pos = (pos[0], float(t)); i += 1
    elif cmd == "H": pos = (float(t), pos[1]); i += 1
    elif cmd == "C": pos = (float(toks[i + 4]), float(toks[i + 5])); i += 6
    cur.append(pos)
    if cmd == "M": cmd = "L"
bottom, trib, main, loop = subs
stem = np.array([(x, -y) for x, y in main + list(reversed(bottom))[1:]])
def arcl(P): return np.r_[0, np.cumsum(np.hypot(*np.diff(P, axis=0).T))]
def resamp(P, N=64):
    s = arcl(P); t = np.linspace(0, s[-1], N); return np.c_[np.interp(t, s, P[:, 0]), np.interp(t, s, P[:, 1])]
FC = arcl(stem)[len(main) - 1] / arcl(stem)[-1]
N = 64
def norm(P): P = P - P.mean(0); return P / np.sqrt((P ** 2).sum())
A0 = norm(resamp(stem, N)); A0r = A0[::-1].copy(); Am = A0 * np.array([-1, 1]); Amr = Am[::-1].copy()
def pres(A, B):
    Mx = A.T @ B; U, S_, Vt = np.linalg.svd(Mx); dd = np.sign(np.linalg.det(U @ Vt))
    return math.sqrt(max(0.0, 2 - 2 * (S_[0] + dd * S_[1])))

# ---- recherche ----
Ls = [80 * 1.25 ** k for k in range(16)]; Ls = [L for L in Ls if L <= 2500]
slope_ok = np.hypot(*np.gradient(Z, RES)) >= 0.04
cand = [(r, c) for r, c in zip(rr, cc) if (r + c) % 3 == 0 and slope_ok[r, c]]
res, resm = [], []
for (r, c) in cand:
    for L in Ls:
        P, Lr = path_from(r, c, L)
        if Lr < 0.97 * L or len(P) < 12: continue
        xy = np.array([(cc_ * RES, -rr_ * RES) for rr_, cc_ in P], float)
        B = norm(resamp(xy, N))
        s1, s2 = pres(A0, B), pres(A0r, B); sm = min(pres(Am, B), pres(Amr, B))
        # affluent vers 82 % (sens source→aval) ou 18 % (sens inverse)
        k82 = P[min(len(P) - 1, int(FC * (len(P) - 1)))]; k18 = P[min(len(P) - 1, int((1 - FC) * (len(P) - 1)))]
        win = lambda q: max(inflow[max(0, q[0]-3):q[0]+4, max(0, q[1]-3):q[1]+4].max() - 1, 0)
        conf = win(k82) if s1 <= s2 else win(k18)
        s = min(s1, s2)
        mid = px2ll(*P[len(P) // 2])
        res.append((s, L, mid, conf, px2ll(*P[0]), px2ll(*P[-1]))); resm.append(sm)
res.sort(key=lambda x: x[0]); resm.sort()
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b)); h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2 * 6371008.8 * math.asin(math.sqrt(h))
print(f"Seuil ruisseau {A_MIN/1e4:.0f} ha | {len(cand)} départs | {len(res)} chemins testés")
print("== 15 meilleurs (résidu ; 0 = identique) ==")
seen = []
for s, L, mid, conf, a, b in res:
    if any(hav(mid, m) < 150 for m in seen): continue
    seen.append(mid)
    print(f"résidu {s:.3f} | L {L:5.0f} m | milieu {mid[0]:.5f},{mid[1]:.5f} ({hav(TA, mid):.0f} m de la tour) | confluence au bon endroit {'oui' if conf else 'non'} | de {a[0]:.5f},{a[1]:.5f} à {b[0]:.5f},{b[1]:.5f}")
    if len(seen) >= 15: break
print("== Contrôle miroir ==")
for q in (0, 0.001, 0.01, 0.05):
    i = max(0, int(q * len(res)) - 1)
    print(f"quantile {q:.1%}: réel {res[i][0]:.3f} | miroir {resm[i]:.3f}")
withconf = [x for x in res if x[3]]
print("meilleur AVEC confluence au bon endroit :", [(round(x[0], 3), round(x[1]), (round(x[2][0], 5), round(x[2][1], 5))) for x in withconf[:5]])
print("part des chemins avec confluence au bon endroit :", f"{len(withconf)}/{len(res)}")
