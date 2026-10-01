"""T1_run2 : idem run1 mais compte les ÉVENEMENTS DISTINCTS (phrase, fenêtre, sous-ensemble, nom) et non les parcours équivalents ; sets curated+latin+communes."""
import sys
src = open("T1_run1.py", encoding="utf-8").read().split("R, Bi, Bp = board_masks()")[0]
exec(src)
KEEP = ("curated", "latin", "communes")
HARR = {k: v for k, v in HARR.items() if k in KEEP}

def events(R, Bi, Bp):
    subs = subsets(R, Bi, Bp); ev = {k: set() for k in KEEP}
    for pn, ph in PHRASES.items():
        L = norm(ph)
        for ws, w in windows(L):
            n = len(w)
            hl = np.zeros(24, np.int64); hl[:n] = hletters(w)
            HC = np.where(P < n, hl[np.minimum(P, 23)], 0)
            for sn, (m, s, t) in subs.items():
                if int(m.sum()) + s + t < 6: continue
                ok = (P[:, m.astype(bool)] < n).all(1)
                if not ok.any(): continue
                hs = (HC * m).sum(1) + np.int64((int(HL[18]) if s else 0) + (int(HL[19]) if t else 0))
                for k, arr in HARR.items():
                    sel = ok & np.isin(hs, arr)
                    for i in np.nonzero(sel)[0]:
                        for _, d in HS[k][int(hs[i])]: ev[k].add((pn, ws, sn, d))
    return ev
PHRASES_ALL = PHRASES
R, Bi, Bp = board_masks()
ev = events(R, Bi, Bp)
print("REEL événements distincts:", {k: len(v) for k, v in ev.items()})
for k in ("curated", "latin"):
    for e in sorted(ev[k]): print(k, e)
rs = np.random.default_rng(7); NB = int(sys.argv[1]); rows = []
for i in range(NB):
    perm = rs.permutation(24)
    Rr = np.zeros(24, np.int64); Rr[perm[:7]] = 1
    Bii = np.zeros(24, np.int64); Bii[perm[7:10]] = 1
    Bpp = np.zeros(24, np.int64); Bpp[perm[10:14]] = 1
    e = events(Rr, Bii, Bpp); rows.append({k: len(v) for k, v in e.items()})
print("HASARD", NB)
for k in KEEP:
    a = np.array([r[k] for r in rows]); r0 = len(ev[k])
    print(f"  {k:9s} réel={r0} hasard moy={a.mean():.1f} sd={a.std():.1f} max={a.max()} rang {(a>=r0).sum()}/{NB} >= réel")
