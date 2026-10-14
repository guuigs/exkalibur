# É12 — M2b : croisements le long d'une demi-droite partant du départ (règle dans M2a_regle.md, écrite avant).
import json, sys, math
O = sys.argv[1]; OUT = sys.argv[2]
def L(n): return json.load(open(O + n, encoding="utf-8"))
KX = 111320 * math.cos(math.radians(45.4289)); KY = 111320
def xy(lon, lat): return ((lon - 6.031015) * KX, (lat - 45.428888) * KY)
def ll(p): return f"{45.428888 + p[1] / KY:.5f},{6.031015 + p[0] / KX:.5f}"
def lines_of(g):
    return [g["coordinates"]] if g["type"] == "LineString" else (g["coordinates"] if g["type"] == "MultiLineString" else [])
def segs_of(feats, pred):
    S = []
    for f in feats:
        if not pred(f["properties"]): continue
        for c in lines_of(f["geometry"]):
            g = [xy(p[0], p[1]) for p in c]; S += list(zip(g, g[1:]))
    return S
R = L("bdt_routes.json"); H = L("bdt_hydro.json")
LIGHT = ("Chemin", "Sentier", "Route empierrée")
CLASSES = {"a_toutes_voies": segs_of(R, lambda p: True), "b_chemins_sentiers": segs_of(R, lambda p: p["nature"] in LIGHT),
           "c_cours_eau": segs_of(H, lambda p: p.get("nature") == "Ecoulement naturel")}
def ray_hits(S, az, segs, maxd=4500):
    dx, dy = math.sin(math.radians(az)), math.cos(math.radians(az))
    ts = []
    for (x1, y1), (x2, y2) in segs:
        ex, ey = x2 - x1, y2 - y1
        den = dx * ey - dy * ex
        if abs(den) < 1e-12: continue
        qx, qy = x1 - S[0], y1 - S[1]
        t = (qx * ey - qy * ex) / den; u = (qx * dy - qy * dx) / den
        if 0 < t <= maxd and 0 <= u <= 1: ts.append(t)
    ts.sort(); m = []
    for t in ts:
        if not m or t - m[-1] > 5: m.append(t)
    return m
STARTS = {"donjon": (45.428888, 6.031015), "esplanade": (45.42891, 6.03112), "rue_Rempart": (45.429772, 6.03118), "chateau_Bayard": (45.423611, 6.018889)}
DIRS = {"R1_lever": 63.7, "R1_relief": 66.5, "R2_lever": 80.2, "R2_relief": 90.7, "R4_quillons": 83.6, "droite_E11": 69.9}
out = ["départ | classe | p hasard (360 dir.) | " + " | ".join(f"{k} {v}°" for k, v in DIRS.items())]
hitsl = []
for sn, (la, lo) in STARTS.items():
    S = xy(lo, la)
    for cn, segs in CLASSES.items():
        # pré-filtre des segments à < 4,6 km
        sg = [s for s in segs if math.hypot(s[0][0] - S[0], s[0][1] - S[1]) < 4700]
        def d311(az):
            h = ray_hits(S, az, sg)
            return h[10] - h[2] if len(h) >= 11 else None
        rnd = [d311(a) for a in range(360)]
        p = sum(1 for v in rnd if v is not None and abs(v - 1850) <= 18.5) / 360
        cells = []
        for k, az in DIRS.items():
            v = d311(az)
            ok = v is not None and abs(v - 1850) <= 18.5
            cells.append("—" if v is None else f"{v:.0f}{' **OUI**' if ok else ''}")
            if ok:
                h = ray_hits(S, az, sg); a = (S[0] + h[2] * math.sin(math.radians(az)), S[1] + h[2] * math.cos(math.radians(az)))
                b = (S[0] + h[10] * math.sin(math.radians(az)), S[1] + h[10] * math.cos(math.radians(az)))
                hitsl.append(f"{sn} {cn} {k}: 3e {ll(a)} ({h[2]:.0f} m), 11e {ll(b)} ({h[10]:.0f} m), 13e à {h[12]:.0f} m" if len(h) > 12 else f"{sn} {cn} {k}: 3e {ll(a)}, 11e {ll(b)}")
        out.append(f"{sn} | {cn} | {p:.3f} | " + " | ".join(cells))
out += ["", "Touches :"] + (hitsl or ["aucune"])
open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n"); print("\n".join(out))
