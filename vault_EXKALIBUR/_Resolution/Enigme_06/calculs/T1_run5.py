"""T1_run5 : (a) même parcours+phrase où rouges ET bleus donnent CHACUN un nom en C (communes+curated+latin, longueur>=4) ;
(b) rouges+bleus (14 lettres) = 2 noms en C (somme de hash), avec/sans S,T. Phrases 24 lettres seulement. Hasard : plateaux aléatoires."""
import sys, time
sys.path.insert(0, ".")
from T1_lib import *
sets = load_names()
H1 = {}
for sn in ("curated", "latin", "communes"):
    for n, d in sets[sn].items():
        if len(n) >= 4: H1.setdefault(int(hword(n)), []).append(d[0])
allh = np.array(sorted(H1), np.int64)
PH = ["Pater noster qui es in caelis", "Pater noster qui es in coelis", "Notre Père qui es aux cieux", "Our Father which art in heaven", "Our Father who art in heaven",
      "Pater noster qui es in celis"]
TR = all_traversals(); ORD = list(TR.values()); P = order_to_pos(ORD)
def run(R, Bi, Bp):
    B = Bi + Bp; a = set(); b = set()
    for ph in PH:
        L = norm(ph)
        if len(L) != 24: continue
        hl = hletters(L)
        HC = hl[P]
        hr = (HC * R).sum(1); hb = (HC * B).sum(1)
        okr = np.isin(hr, allh); okb = np.isin(hb, allh)
        for i in np.nonzero(okr & okb)[0]:
            a.add((ph, int(i), H1[int(hr[i])][0], H1[int(hb[i])][0]))
        for s, t in [(0,0),(1,0),(0,1),(1,1)]:
            hrb = hr + hb + (int(HL[18]) if s else 0) + (int(HL[19]) if t else 0)
            for i in range(len(ORD)):
                tot = int(hrb[i])
                cand = np.isin(tot - allh, allh)
                for h in allh[cand][:5]:
                    b.add((ph, s, t, H1[int(h)][0], H1[tot - int(h)][0]))
    return a, b
R, Bi, Bp = board_masks(); t0 = time.time()
a, b = run(R, Bi, Bp)
print("REEL (a) R et B chacun un nom:", len(a)); [print(x) for x in sorted(a)[:30]]
print("REEL (b) R+B(+S,T) = 2 noms:", len(b)); [print(x) for x in sorted(b)[:30]]
print(f"{time.time()-t0:.0f}s", flush=True)
NB = int(sys.argv[1]); rs = np.random.default_rng(9); ca = []; cb = []
for i in range(NB):
    perm = rs.permutation(24)
    Rr = np.zeros(24, np.int64); Rr[perm[:7]] = 1
    Bii = np.zeros(24, np.int64); Bii[perm[7:10]] = 1
    Bpp = np.zeros(24, np.int64); Bpp[perm[10:14]] = 1
    x, y = run(Rr, Bii, Bpp); ca.append(len(x)); cb.append(len(y))
for nm, c, r in (("a", ca, len(a)), ("b", cb, len(b))):
    c = np.array(c); print(f"HASARD ({nm}) x{NB}: moy={c.mean():.1f} max={c.max()} rang {(c>=r).sum()}/{NB} >= réel({r})")
