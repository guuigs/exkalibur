"""U1 — chaînes de 4 lieux-boisson, ordre A PRIORI parmi {N->S, S->N, O->E, E->O, alphabétique}, sans allers-retours.
Cible D=341.61 (Sainte-Chapelle) / 342.01 ; fenêtre ±1 % autour de 341.6-342.0. Test lame Urquhart->Valence."""
import sys, json, itertools, random
sys.path.insert(0, ".")
from solveurB_geo import hav
from U1_pool import POOL
sys.stdout.reconfigure(encoding="utf-8")
C = json.load(open("U1_coords.json", encoding="utf-8"))
P = {k: (v["lat"], v["lon"]) for k, v in C.items() if v and k != "Carnac"}
fam = {k: POOL[k][2] for k in P}
URQ, VAL = (57.3241399, -4.4420013), (39.4752858, -0.3754667)
def seg_cross(p1, p2, q1, q2):
    def o(a, b, c): return (b[1]-a[1])*(c[0]-b[0]) - (b[0]-a[0])*(c[1]-b[1])
    a, b, c, d = (p1[1], p1[0]), (p2[1], p2[0]), (q1[1], q1[0]), (q2[1], q2[0])
    return (o(a, b, c)*o(a, b, d) < 0) and (o(c, d, a)*o(c, d, b) < 0)
def length(ch): return sum(hav(P[a], P[b]) for a, b in zip(ch, ch[1:]))
def crosses(ch): return any(seg_cross(P[a], P[b], URQ, VAL) for a, b in zip(ch, ch[1:]))
D0, D1 = 341.61, 342.01
def ok(L): return abs(L/D0-1) <= .01 or abs(L/D1-1) <= .01
ORD = {
 "N>S": lambda s: sorted(s, key=lambda n: -P[n][0]), "S>N": lambda s: sorted(s, key=lambda n: P[n][0]),
 "O>E": lambda s: sorted(s, key=lambda n: P[n][1]), "E>O": lambda s: sorted(s, key=lambda n: -P[n][1]),
 "alpha": lambda s: sorted(s), "alpha-inv": lambda s: sorted(s, reverse=True)}
def hits(pool):
    out = []
    for s in itertools.combinations(pool, 4):
        for on, f in ORD.items():
            ch = f(s)
            if ok(length(ch)): out.append((on, ch))
    return out
if __name__ == "__main__":
    names = sorted(P)
    print("pool", len(names), "lieux ; sous-ensembles", sum(1 for _ in itertools.combinations(names, 4)))
    H = hits(names)
    print("HITS total (ordre a priori, ±1 %):", len(H))
    # pureté de famille
    pure = [(o, c) for o, c in H if len({fam[n] for n in c}) == 1]
    print("dont 4 lieux de même famille:", len(pure))
    for o, c in pure:
        L = length(c); print(f"  [{fam[c[0]]}] {o:9s} {' > '.join(c)}  L={L:.2f}  croise lame={crosses(c)}")
    json.dump([[o, c] for o, c in H], open("U1_hits.json", "w", encoding="utf-8"), ensure_ascii=False)
    # hasard : proportion de sous-ensembles/ordres qui donnent un hit, pool total vs. pool 'faux' (villes en C au hasard = tout le pool de T3)
    T3 = json.load(open("solveurB_C_coords.json", encoding="utf-8"))
    Q = {k: (v[0], v[1]) for k, v in T3.items() if k != "Carnac"}
    P.update(Q); fam.update({k: "T3" for k in Q})
    rnd = random.Random(1); n = 0; h = 0; N = 60000
    tn = sorted(Q)
    for _ in range(N):
        s = rnd.sample(tn, 4)
        for on, f in ORD.items():
            n += 1; h += ok(length(f(s)))
    print(f"référence T3 (111 lieux en C, tirage 4) : {100*h/n:.3f} % des (sous-ensemble, ordre) tombent à ±1 %")
    # ratio pour pool U1
    P2 = {k: v for k, v in P.items() if k in names}
    tot = 0; hh = 0
    for s in itertools.combinations(names, 4):
        for on, f in ORD.items():
            tot += 1
    print(f"pool U1 : {100*len(H)/tot:.3f} % ({len(H)}/{tot})")
