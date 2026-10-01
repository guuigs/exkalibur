"""T3 — chaînes 'thématiques' fixées A PRIORI (avant mesure) : ordre chronologique historique.
Coordonnées : solveurB_C_coords.json (sources notées) + Wikipedia via solveurB_geo.wiki_coords (La Chaise-Dieu).
Haversine R=6371,0088. Cibles D : Tour de Londres->Battle->Sainte-Chapelle = 341,60 ; Notre-Dame 342,01.
Test lame : segment Urquhart->Valence (carte Guilhem). Test hasard : mêmes chaînes, mais tirage aléatoire de 4 lieux du pool (111 lieux en C)."""
import sys, json, random, itertools
sys.path.insert(0, ".")
from solveurB_geo import hav, wiki_coords
sys.stdout.reconfigure(encoding="utf-8")
C = json.load(open("solveurB_C_coords.json", encoding="utf-8"))
P = {k: (v[0], v[1]) for k, v in C.items()}
wc = wiki_coords(["Abbaye de la Chaise-Dieu", "Souvigny", "Limoges", "Troyes", "Barbonne-Fayel"], "fr")
print("wiki fr:", wc)
P["Chaise-Dieu"] = tuple(wc["Abbaye de la Chaise-Dieu"][:2])
URQ, VAL = (57.3241399, -4.4420013), (39.4752858, -0.3754667)
D = {"Sainte-Chapelle": 341.60, "Notre-Dame": 342.01}

def seg_cross(p1, p2, q1, q2):
    def o(a, b, c): return (b[1]-a[1])*(c[0]-b[0]) - (b[0]-a[0])*(c[1]-b[1])
    a, b, c, d = (p1[1], p1[0]), (p2[1], p2[0]), (q1[1], q1[0]), (q2[1], q2[0])
    return (o(a, b, c)*o(a, b, d) < 0) and (o(c, d, a)*o(c, d, b) < 0)
def length(names): return sum(hav(P[a], P[b]) for a, b in zip(names, names[1:]))
def crosses(names): return any(seg_cross(P[a], P[b], URQ, VAL) for a, b in zip(names, names[1:]))

# --- chaînes a priori (ordre chronologique attesté ; sélection = C visités par Urbain II, 1095-96) ---
FAM = {
 "U1 Urbain II chrono : Chaise-Dieu(18/08/1095) > Cluny(11/09-25/10) > Clermont(nov 1095) > Carcassonne(1096)":
    ["Chaise-Dieu", "Cluny", "Clermont", "Carcassonne"],
 "U2 Urbain II sans Chaise-Dieu (3 C seulement) Cluny > Clermont > Carcassonne": ["Cluny", "Clermont", "Carcassonne"],
 "U3 Cluny > Clermont > Cahors > Carcassonne (non attesté, pour mémoire)": ["Cluny", "Clermont", "Cahors", "Carcassonne"],
 "J1 pistes joueurs : Clermont > Cluny > Cîteaux > Clairvaux (ordre géographique, non chronologique)": ["Clermont", "Cluny", "Cîteaux", "Clairvaux"],
 "J2 Cluny > Clermont > Cadouin (3 C, piste Guilhem)": ["Cluny", "Clermont", "Cadouin"],
}
print("\n== chaînes a priori")
for k, ch in FAM.items():
    L = length(ch)
    print(f"{k}\n    L={L:7.2f} km  écart/341,60 = {100*(L/D['Sainte-Chapelle']-1):+.2f} %  /342,01 = {100*(L/D['Notre-Dame']-1):+.2f} %  croise lame: {crosses(ch)}  jambes: " +
          ", ".join(f"{a}-{b} {hav(P[a],P[b]):.1f}" for a, b in zip(ch, ch[1:])))

# ordre : quelle permutation minimise la longueur / lesquelles tombent à ±1 %
print("\n== permutations de {Chaise-Dieu, Cluny, Clermont, Carcassonne}")
for perm in itertools.permutations(["Chaise-Dieu", "Cluny", "Clermont", "Carcassonne"]):
    if perm[0] < perm[-1]:
        L = length(perm); flag = "<== ±1 %" if abs(L/341.6-1) <= .01 else ""
        print(f"   {' > '.join(perm):55s} {L:7.2f} {flag}")

# --- test du hasard : proba qu'un tirage 4 lieux (ordre = plus court chemin, ou ordre libre) tombe à ±1 % de D ---
rnd = random.Random(3)
names = [n for n in P if n not in ("Carnac",) and P[n][0] > 42 and P[n][1] > -5 and P[n][1] < 8 and P[n][0] < 51]   # France métropolitaine (approx.)
print("\npool France :", len(names), "lieux")
def base(pool, N=200000):
    hit_free = hit_sp = 0
    for _ in range(N):
        s = rnd.sample(pool, 4)
        perms = [length(p) for p in itertools.permutations(s) if p[0] < p[-1]]
        if any(abs(L/341.6-1) <= .01 for L in perms): hit_free += 1
        if abs(min(perms)/341.6-1) <= .01: hit_sp += 1
    return hit_free/N, hit_sp/N
N = 30000
hf, hs = base(names, N)
print(f"tirage aléatoire de 4 lieux en C (France) : P(existe un ordre à ±1 % de 341,6) = {100*hf:.2f} %  ; P(plus court chemin à ±1 %) = {100*hs:.2f} %  (N={N})")
# une seule chaîne d'ordre imposé a priori : proba
one = 0
for _ in range(200000):
    s = rnd.sample(names, 4)
    if abs(length(s)/341.6-1) <= .01: one += 1
print(f"une chaîne d'ordre fixé (tirage ordonné) tombe à ±1 % : {100*one/200000:.3f} %")
