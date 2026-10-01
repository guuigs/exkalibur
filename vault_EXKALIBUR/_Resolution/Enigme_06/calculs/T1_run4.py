"""T1_run4 : numéro de case = rang de lettre dans un texte (Pater complet, variantes) ; 'numéro' selon 8 parcours-de-numérotation x sous-ensembles.
Exact : multiset des lettres = nom de C (1 nom), ou 2 noms (somme de hash) pour sous-ensembles >=10 lettres. Aussi: 10 cases vides / 7 rouges + 7 bleus sont des rangs -> lettres.
Test hasard : mêmes tests sur plateaux aléatoires."""
import sys, time
sys.path.insert(0, ".")
from T1_lib import *
sets = load_names()
H1 = {}
for sn in ("curated", "latin", "communes"):
    for n, d in sets[sn].items():
        if len(n) >= 5: H1.setdefault(int(hword(n)), []).append(d[0])
A1 = np.array(sorted(H1), np.int64)
PH = {"lat": "Pater noster qui es in caelis sanctificetur nomen tuum adveniat regnum tuum fiat voluntas tua sicut in caelo et in terra panem nostrum quotidianum da nobis hodie et dimitte nobis debita nostra sicut et nos dimittimus debitoribus nostris et ne nos inducas in tentationem sed libera nos a malo amen",
      "lat_court": "Pater noster qui es in caelis",
      "fr": "Notre Père qui es aux cieux que ton nom soit sanctifié que ton règne vienne que ta volonté soit faite sur la terre comme au ciel donne-nous aujourd'hui notre pain de ce jour pardonne-nous nos offenses comme nous pardonnons aussi à ceux qui nous ont offensés et ne nous soumets pas à la tentation mais délivre-nous du mal amen",
      "en": "Our Father which art in heaven hallowed be thy name thy kingdom come thy will be done in earth as it is in heaven give us this day our daily bread and forgive us our trespasses as we forgive them that trespass against us and lead us not into temptation but deliver us from evil amen",
      "harold": "Harold rex interfectus est", "libera": "Libera nos a malo"}
# numérotations 1..24 des cases (parcours tier1) : cell -> numéro
TR = all_traversals(); NUMS = list(TR.values())
def run(R, Bi, Bp):
    subs = subsets(R, Bi, Bp); found = set()
    for pn, ph in PH.items():
        L = norm(ph); n = len(L)
        Lh = hletters(L)
        for off in (0, 1):              # rang à partir de 0 ou 1 (numéro 1..24 => lettre L[num-1+off-?])
            for o in NUMS:
                pos = np.zeros(24, int)
                for p, c in enumerate(o): pos[c] = p + 1     # numéro 1..24
                for sn, (m, s, t) in subs.items():
                    cells = np.nonzero(m)[0]
                    idx = pos[cells] - 1 + off
                    if idx.max() >= n: continue
                    h = int(Lh[idx].sum()) + (int(HL[18]) if s else 0) + (int(HL[19]) if t else 0)
                    if h in H1: found.add((pn, off, sn, H1[h][0]))
    return found
R, Bi, Bp = board_masks(); t0 = time.time()
f = run(R, Bi, Bp); print("REEL:", len(f), f"{time.time()-t0:.0f}s")
for x in sorted(f)[:40]: print(x)
NB = int(sys.argv[1]); rs = np.random.default_rng(5); cs = []
for i in range(NB):
    perm = rs.permutation(24)
    Rr = np.zeros(24, np.int64); Rr[perm[:7]] = 1
    Bii = np.zeros(24, np.int64); Bii[perm[7:10]] = 1
    Bpp = np.zeros(24, np.int64); Bpp[perm[10:14]] = 1
    cs.append(len(run(Rr, Bii, Bpp)))
cs = np.array(cs); print(f"HASARD x{NB}: moy={cs.mean():.1f} sd={cs.std():.1f} max={cs.max()} ; rang {(cs>=len(f)).sum()}/{NB}")
