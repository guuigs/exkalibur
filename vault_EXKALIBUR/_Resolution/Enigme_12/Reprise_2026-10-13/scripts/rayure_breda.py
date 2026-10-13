"""Recalage local de la fissure (SVG de Guilhem) sur le réseau BD TOPO autour de la tour d'Avalon.
Reprend la méthode de Revue_globale/O_rayure_match.py (Procrustes sans miroir, confluence à la même fraction),
restreinte aux confluences à <= 3 km de la tour, et sauvegarde la géométrie des meilleurs calages."""
import json, math, re, itertools, sys
import numpy as np
SVG = sys.argv[1]; HYD = sys.argv[2]; OUT = sys.argv[3]
TA = (45.429083, 6.030808); LAT0, LON0 = TA
KX = math.cos(math.radians(LAT0)) * 111320.0; KY = 111132.0
d = re.search(r'd="([^"]+)"', open(SVG, encoding="utf-8").read()).group(1)
toks = re.findall(r"[MLVHC]|-?\d+(?:\.\d+)?", d)
subs, cur, pos, i, cmd = [], None, (0.0, 0.0), 0, None
while i < len(toks):
    t = toks[i]
    if t in "MLVHC":
        cmd = t; i += 1
        if cmd == "M": cur = []; subs.append(cur)
        continue
    if cmd in ("M", "L"): pos = (float(toks[i]), float(toks[i+1])); i += 2
    elif cmd == "V": pos = (pos[0], float(t)); i += 1
    elif cmd == "H": pos = (float(t), pos[1]); i += 1
    elif cmd == "C": pos = (float(toks[i+4]), float(toks[i+5])); i += 6
    cur.append(pos)
    if cmd == "M": cmd = "L"
bottom, trib, main, loopside = subs
stem_svg = np.array([(x, -y) for x, y in main + list(reversed(bottom))[1:]])
trib_svg = np.array([(x, -y) for x, y in trib]); loop_svg = np.array([(x, -y) for x, y in loopside])
def arclen(P): return np.r_[0, np.cumsum(np.hypot(*np.diff(P, axis=0).T))]
def resample(P, n=64):
    s = arclen(P); t = np.linspace(0, s[-1], n)
    return np.c_[np.interp(t, s, P[:, 0]), np.interp(t, s, P[:, 1])]
s_svg = arclen(stem_svg); FC = s_svg[len(main)-1] / s_svg[-1]
N = 64; A = resample(stem_svg, N); Amean = A.mean(0); A = A - Amean; An = np.sqrt((A**2).sum()); A0 = A / An
def procrustes(B):
    Bm = B.mean(0); Bc = B - Bm; bn = np.sqrt((Bc**2).sum()); B0 = Bc / bn
    U, Sg, Vt = np.linalg.svd(A0.T @ B0); dd = np.sign(np.linalg.det(U @ Vt))
    R = U @ np.diag([1, dd]) @ Vt
    return np.sqrt(max(0.0, 2 - 2*(Sg[0] + dd*Sg[1]))), R, bn / An * (Sg[0] + dd*Sg[1]), Bm
def loc(lon, lat): return ((lon-LON0)*KX, (lat-LAT0)*KY)
def ll(x, y): return (LAT0 + y/KY, LON0 + x/KX)
F = json.load(open(HYD)); edges, adj = [], {}
key = lambda p: (round(p[0]), round(p[1]))
for f in F:
    pr = f["properties"]
    if pr.get("nature") in ("Conduit forcé", "Conduit buse", "Aqueduc"): continue
    g = f["geometry"]; lines = [g["coordinates"]] if g["type"] == "LineString" else g["coordinates"]
    for ln in lines:
        P = np.array([loc(c[0], c[1]) for c in ln])
        if len(P) < 2: continue
        eid = len(edges); edges.append((P, key(P[0]), key(P[-1]), pr.get("cpx_toponyme_de_cours_d_eau") or ""))
        adj.setdefault(key(P[0]), []).append(eid); adj.setdefault(key(P[-1]), []).append(eid)
def oriented(eid, node):
    P, a, b, _ = edges[eid]; return (P, b) if a == node else (P[::-1], a)
def walk(node, eid, D, cap=12, visited=None):
    visited = visited or {node}; P, nxt = oriented(eid, node); s = arclen(P)
    if s[-1] >= D:
        k = np.searchsorted(s, D); t = (D-s[k-1])/(s[k]-s[k-1]) if s[k] > s[k-1] else 0
        return [np.vstack([P[:k], P[k-1] + t*(P[k]-P[k-1])])]
    if nxt in visited: return []
    outs = []
    for e2 in adj.get(nxt, []):
        if e2 == eid: continue
        for tail in walk(nxt, e2, D - s[-1], cap, visited | {nxt}):
            outs.append(np.vstack([P, tail[1:]]))
            if len(outs) >= cap: return outs
    return outs
Ls = [150*1.2**k for k in range(22) if 150*1.2**k <= 6000]
res = []
for n, es in adj.items():
    if len(es) < 3 or math.hypot(*n) > 3000: continue
    for eu, ed in itertools.permutations(es, 2):
        for L in Ls:
            ups = walk(n, eu, FC*L); downs = walk(n, ed, (1-FC)*L)
            for up, dn in itertools.islice(itertools.product(ups, downs), 16):
                stem = np.vstack([up[::-1], dn[1:]]); B = resample(stem, N)
                r, R, sc, Bm = procrustes(B)
                res.append((r, L, n, eu, ed, stem, R, sc, Bm))
res.sort(key=lambda x: x[0])
out = []
for r, L, n, eu, ed, stem, R, sc, Bm in res[:400]:
    tf = lambda P: ((P - Amean) @ R) * sc + Bm  # SVG -> terrain
    cen = ll(*stem.mean(0)); conf = ll(*n)
    out.append(dict(res=r, L=L, conf=conf, center=cen, dist_conf=math.hypot(*n)/1000,
        names=sorted({edges[eu][3], edges[ed][3]} - {""}),
        stem=[ll(*p) for p in stem], svg_stem=[ll(*p) for p in tf(stem_svg)], svg_trib=[ll(*p) for p in tf(trib_svg)],
        svg_loop=[ll(*p) for p in tf(loop_svg)], svg_start=ll(*tf(stem_svg[:1])[0]), svg_end=ll(*tf(stem_svg[-1:])[0])))
json.dump(out, open(OUT, "w"))
seen = []
for o in out:
    if any(math.hypot(o['center'][0]-c[0], (o['center'][1]-c[1])*0.7) < 0.002 for c in seen): continue
    seen.append(o['center'])
    print("res %.3f L=%4.0f m conf %.5f,%.5f (%.2f km tour) centre %.5f,%.5f %s" % (o['res'], o['L'], *o['conf'], o['dist_conf'], *o['center'], o['names']))
    if len(seen) >= 15: break
