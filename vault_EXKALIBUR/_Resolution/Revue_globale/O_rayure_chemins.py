"""[VARIANTE CHEMINS, 01/10] Rayure de l'épée (SVG de Guilhem) vs réseau de SENTIERS/CHEMINS IGN BD TOPO (idée : le chemin entre la 3e et la 11e station).
Hypothèse (Guilhem, conviction perso) : la rayure = schéma du ruisseau de la zone finale.
FAQ : FAQ06-161 (la rayure aurait pu être tournée de 180° : Oui) ; FAQ03-059 (aurait pu être placée ailleurs sur la lame : Oui)
      ; FAQ04-093 (à utiliser pour un tracé MyMaps ? pas de réponse).
Méthode : tronc principal du SVG (haut → confluence → bas), rééchantillonné ; pour chaque confluence IGN
(degré ≥ 3), chaque choix amont/aval et chaque longueur L (150 m → 14 km), on marche le long du réseau et on
compare par Procrustes (similitude, rotation libre, SANS symétrie miroir). Contrôle : même recherche avec le SVG
en miroir (une vraie correspondance doit battre nettement le miroir).
"""
import json, math, re, sys, itertools
import numpy as np

S = r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/ign/"
OUT = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/"
TA = (45.4288, 6.03078)  # tour d'Avalon
LAT0, LON0 = TA
KX = math.cos(math.radians(LAT0)) * 111320.0
KY = 110540.0

# ---------- SVG ----------
d = re.search(r'd="([^"]+)"', open(OUT + "rayure_epee_guilhem.svg", encoding="utf-8").read()).group(1)
toks = re.findall(r"[MLVHC]|-?\d+(?:\.\d+)?", d)
subs, cur, pos, i, cmd = [], None, (0.0, 0.0), 0, None
while i < len(toks):
    t = toks[i]
    if t in "MLVHC":
        cmd = t; i += 1
        if cmd == "M":
            cur = []; subs.append(cur)
        continue
    if cmd in ("M", "L"):
        pos = (float(toks[i]), float(toks[i + 1])); i += 2
    elif cmd == "V":
        pos = (pos[0], float(t)); i += 1
    elif cmd == "H":
        pos = (float(t), pos[1]); i += 1
    elif cmd == "C":
        pos = (float(toks[i + 4]), float(toks[i + 5])); i += 6
    cur.append(pos)
    if cmd == "M": cmd = "L"
bottom, trib, main, loopside = subs
stem_svg = main + list(reversed(bottom))[1:]
def to_up(p): return [(x, -y) for x, y in p]   # SVG y vers le bas -> y vers le haut (sinon miroir implicite)
stem_svg = np.array(to_up(stem_svg)); trib_svg = np.array(to_up(trib))

def arclen(P):
    s = np.r_[0, np.cumsum(np.hypot(*np.diff(P, axis=0).T))]; return s
def resample(P, n=64):
    s = arclen(P); t = np.linspace(0, s[-1], n)
    return np.c_[np.interp(t, s, P[:, 0]), np.interp(t, s, P[:, 1])]
s_svg = arclen(stem_svg); conf_idx = len(main) - 1
FC = s_svg[conf_idx] / s_svg[-1]
N = 64
A = resample(stem_svg, N); A = A - A.mean(0); A_norm = np.sqrt((A ** 2).sum())
A0 = A / A_norm
Amir = A0 * np.array([-1, 1])  # contrôle miroir
trib_vec_svg = trib_svg[min(2, len(trib_svg) - 1)] - trib_svg[0]

def procrustes(B):
    """Retourne (résidu normalisé 0..~1.4, R, scale, t) pour aligner A0 sur B (rotation propre)."""
    Bc = B - B.mean(0); bn = np.sqrt((Bc ** 2).sum())
    if bn == 0: return 9, None
    B0 = Bc / bn
    M = A0.T @ B0
    U, Sg, Vt = np.linalg.svd(M)
    dd = np.sign(np.linalg.det(U @ Vt))
    D = np.diag([1, dd])
    R = U @ D @ Vt
    res = np.sqrt(max(0.0, 2 - 2 * (Sg[0] + dd * Sg[1])))
    return res, R
def procrustes_mir(B):
    Bc = B - B.mean(0); B0 = Bc / np.sqrt((Bc ** 2).sum())
    M = Amir.T @ B0; U, Sg, Vt = np.linalg.svd(M); dd = np.sign(np.linalg.det(U @ Vt))
    return np.sqrt(max(0.0, 2 - 2 * (Sg[0] + dd * Sg[1])))

# ---------- réseau IGN ----------
F = json.load(open(S + "troncon_de_route.geojson", encoding="utf-8"))["features"]
import time; T0=time.time()
def loc(lon, lat): return ((lon - LON0) * KX, (lat - LAT0) * KY)
def inv(x, y): return (LAT0 + y / KY, LON0 + x / KX)
edges, adj = [], {}
def key(p): return (round(p[0]), round(p[1]))
for f in F:
    pr = f["properties"]
    if pr.get("nature") not in ("Sentier", "Chemin", "Route empierrée", "Escalier"): continue
    g = f["geometry"]; lines = [g["coordinates"]] if g["type"] == "LineString" else g["coordinates"]
    for ln in lines:
        P = np.array([loc(c[0], c[1]) for c in ln])
        if len(P) < 2: continue
        if min(abs(P[:,0]).min(), abs(P[:,1]).min()) > 6500: continue
        eid = len(edges)
        name = pr.get("cpx_toponyme_de_cours_d_eau") or ""
        edges.append((P, key(P[0]), key(P[-1]), name))
        adj.setdefault(key(P[0]), []).append(eid); adj.setdefault(key(P[-1]), []).append(eid)

def oriented(eid, from_node):
    P, a, b, _ = edges[eid]
    return (P, b) if a == from_node else (P[::-1], a)

def walk(node, eid, D, cap=12, visited=None):
    """Toutes les polylignes de longueur D en partant de node par l'arête eid (branchements inclus)."""
    visited = visited or {node}
    P, nxt = oriented(eid, node)
    s = arclen(P)
    if s[-1] >= D:
        k = np.searchsorted(s, D)
        t = (D - s[k - 1]) / (s[k] - s[k - 1]) if s[k] > s[k - 1] else 0
        end = P[k - 1] + t * (P[k] - P[k - 1])
        return [np.vstack([P[:k], end])]
    if nxt in visited: return []
    outs = []
    for e2 in adj.get(nxt, []):
        if e2 == eid: continue
        for tail in walk(nxt, e2, D - s[-1], cap, visited | {nxt}):
            outs.append(np.vstack([P, tail[1:]]))
            if len(outs) >= cap: return outs
    return outs

Ls = [150 * 1.2 ** k for k in range(26)]  # 150 m -> ~14 km
Ls = [L for L in Ls if L <= 5000]
res_real, res_mir = [], []
conf_nodes = [n for n, es in adj.items() if len(es) >= 3 and math.hypot(*n) <= 4500]
print("noeuds degré>=3 <=4,5 km :",len(conf_nodes),flush=True)
for n in conf_nodes:
    if time.time()-T0>230: print("ARRÊT temps (partiel)"); break
    es = adj[n]
    for eu, ed in itertools.permutations(es, 2):
        tribs = [e for e in es if e not in (eu, ed)]
        for L in Ls:
            ups = walk(n, eu, FC * L); downs = walk(n, ed, (1 - FC) * L)
            if not ups or not downs: continue
            for up, dn in itertools.islice(itertools.product(ups, downs), 16):
                stem = np.vstack([up[::-1], dn[1:]])
                B = resample(stem, N)
                r, R = procrustes(B)
                rm = procrustes_mir(B)
                # direction de l'affluent après alignement
                tv = []
                for te in tribs:
                    Pt, _ = oriented(te, n); v = Pt[min(3, len(Pt) - 1)] - Pt[0]
                    tv.append(v)
                ang = None
                if tv:
                    w = trib_vec_svg @ R  # vecteur SVG tourné dans le repère terrain
                    a2 = math.degrees(math.atan2(w[1], w[0]))
                    angs = [abs((math.degrees(math.atan2(v[1], v[0])) - a2 + 180) % 360 - 180) for v in tv]
                    ang = min(angs)
                cen = inv(*B.mean(0))
                names = sorted({edges[eu][3], edges[ed][3]} - {""})
                res_real.append((r, L, cen, ang, names, n))
                res_mir.append((rm, L, cen))

res_real.sort(key=lambda x: x[0]); res_mir.sort(key=lambda x: x[0])
def dist_km(c):
    la1, lo1, la2, lo2 = map(math.radians, (*TA, *c)); h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371.0088 * math.asin(math.sqrt(h))
print(f"SVG : tronc {len(stem_svg)} sommets, confluence à {FC:.3f} de la longueur ; {len(conf_nodes)} confluences IGN ; {len(res_real)} fenêtres testées")
print("\n== 20 meilleures correspondances (résidu Procrustes, 0 = identique) ==")
seen = []
k = 0
for r, L, cen, ang, names, n in res_real:
    if any(dist_km(cen) - 0 < 99 and math.hypot(cen[0] - c[0], cen[1] - c[1]) < 0.003 for c in seen): continue
    seen.append(cen); k += 1
    print(f"{k:2d}. résidu {r:.3f} | L={L/1000:.2f} km | centre {cen[0]:.5f},{cen[1]:.5f} | {dist_km(cen):.2f} km de la tour | écart affluent {ang if ang is None else round(ang)}° | {', '.join(names) or 'sans nom'}")
    if k >= 20: break
print("\n== Contrôle miroir (même recherche, SVG inversé gauche-droite) ==")
print("meilleur résidu réel  :", round(res_real[0][0], 3))
print("meilleur résidu miroir:", round(res_mir[0][0], 3))
qs = [0.001, 0.01, 0.05]
for q in qs:
    i = max(0, int(q * len(res_real)) - 1)
    print(f"quantile {q:.1%} : réel {res_real[i][0]:.3f} | miroir {res_mir[i][0]:.3f}")
near = [x for x in res_real if dist_km(x[2]) <= 3]
print("\nmeilleur à ≤ 3 km de la tour :", [ (round(x[0],3), round(x[1]), (round(x[2][0],5), round(x[2][1],5)), x[4]) for x in near[:5]])
json.dump([(r, L, cen, ang, names) for r, L, cen, ang, names, n in res_real[:300]], open(OUT + "O_rayure_chemins_top.json", "w", encoding="utf-8"), ensure_ascii=False)
