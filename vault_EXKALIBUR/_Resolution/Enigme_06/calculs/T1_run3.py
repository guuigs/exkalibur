"""T1_run3 : décalage de César (0..25) appliqué aux lettres de la phrase avant lecture par parcours ; clé = lettres triées (exact).
Phrases 24 lettres (+ fenêtres), parcours tier1 uniquement, sous-ensembles R,B,E,RB,... ± S ± T (S,T non décalés / décalés)."""
import sys, time
sys.path.insert(0, ".")
from T1_lib import *
sets = load_names()
KEY = {}
for sn in ("curated", "latin", "communes"):
    for n, d in sets[sn].items():
        if len(n) >= 5: KEY.setdefault("".join(sorted(n)), []).append((sn, d[0]))
TR = all_traversals(); ORD = list(TR.values())
PH = ["Pater noster qui es in caelis", "Pater noster qui es in coelis", "Notre Père qui es aux cieux", "Our Father which art in heaven", "Our Father who art in heaven",
      "Pater noster qui es in caelis sanctificetur nomen tuum", "Pater noster", "Padre nuestro que estás en el cielo"]
def shift(s, k): return "".join(chr((ord(c) - 65 + k) % 26 + 65) for c in s)
def run(R, Bi, Bp):
    subs = subsets(R, Bi, Bp); found = set()
    for ph in PH:
        L = norm(ph)
        for ws in range(0, max(1, len(L) - 23)):
            w = L[ws:ws + 24]; n = len(w)
            for k in range(26):
                ws_ = shift(w, k)
                seen = set()
                for sn, (m, s, t) in subs.items():
                    cells = np.nonzero(m)[0]
                    for o in ORD:
                        pos = {c: p for p, c in enumerate(o)}
                        if any(pos[c] >= n for c in cells): continue
                        letters = "".join(ws_[pos[c]] for c in cells)
                        for sk in ([0, 1] if (s or t) else [0]):
                            ex = ("S" if s else "") + ("T" if t else "")
                            if sk: ex = shift(ex, k)
                            key = "".join(sorted(letters + ex))
                            if (sn, key) in seen: continue
                            seen.add((sn, key))
                            for x in KEY.get(key, []): found.add((ph, ws, k, sn, sk, x[1], x[0]))
    return found
R, Bi, Bp = board_masks(); t0 = time.time()
f = run(R, Bi, Bp)
print("REEL:", len(f), f"{time.time()-t0:.0f}s")
for x in sorted(f)[:60]: print(x)
NB = int(sys.argv[1]); rs = np.random.default_rng(3); cs = []
for i in range(NB):
    perm = rs.permutation(24)
    Rr = np.zeros(24, np.int64); Rr[perm[:7]] = 1
    Bii = np.zeros(24, np.int64); Bii[perm[7:10]] = 1
    Bpp = np.zeros(24, np.int64); Bpp[perm[10:14]] = 1
    cs.append(len(run(Rr, Bii, Bpp)))
cs = np.array(cs); print(f"HASARD x{NB}: moy={cs.mean():.1f} sd={cs.std():.1f} max={cs.max()} ; rang {(cs>=len(f)).sum()}/{NB} >= réel")
