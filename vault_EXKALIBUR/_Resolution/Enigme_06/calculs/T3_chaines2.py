"""T3 — variantes chronologiques/thématiques (ordre fixé a priori). Coordonnées solveurB_C_coords.json."""
import sys, itertools, json
sys.path.insert(0, ".")
from solveurB_geo import hav
sys.stdout.reconfigure(encoding="utf-8")
C = json.load(open("solveurB_C_coords.json", encoding="utf-8"))
P = {k: (v[0], v[1]) for k, v in C.items()}
URQ, VAL = (57.3241399, -4.4420013), (39.4752858, -0.3754667)
def seg_cross(p1, p2, q1, q2):
    def o(a, b, c): return (b[1]-a[1])*(c[0]-b[0]) - (b[0]-a[0])*(c[1]-b[1])
    a, b, c, d = (p1[1], p1[0]), (p2[1], p2[0]), (q1[1], q1[0]), (q2[1], q2[0])
    return (o(a, b, c)*o(a, b, d) < 0) and (o(c, d, a)*o(c, d, b) < 0)
def length(n): return sum(hav(P[a], P[b]) for a, b in zip(n, n[1:]))
def crosses(n): return any(seg_cross(P[a], P[b], URQ, VAL) for a, b in zip(n, n[1:]))
CH = {
 "A Cluny>Clermont>Cîteaux>Clairvaux (dates : 1095 oct, 1095 nov, 1098 fondation Cîteaux, 1115 Clairvaux)": ["Cluny","Clermont","Cîteaux","Clairvaux"],
 "B Clermont>Cluny>Cîteaux>Clairvaux (piste joueurs)": ["Clermont","Cluny","Cîteaux","Clairvaux"],
 "C Cluny>Clermont>Clairvaux (3 C)": ["Cluny","Clermont","Clairvaux"],
 "D Cluny>Clermont>Cîteaux>Clairvaux>Châlons(-Troyes?)": ["Cluny","Clermont","Cîteaux","Clairvaux","Châlons-en-Champagne"],
 "E Templiers 1127-29 : Chinon>Caen>Canterbury>Cassel>Clairvaux (Anjou,Normandie,Angleterre,Flandre,Champagne) [C non attestés]": ["Chinon","Caen","Canterbury","Cassel","Clairvaux"],
 "F Clermont>Cluny>Clairvaux>Cîteaux (mêmes 4 C, autre ordre)": ["Clermont","Cluny","Clairvaux","Cîteaux"],
 "G Cluny>Clermont>Cîteaux>Chaource? -": None,
}
for k, ch in CH.items():
    if not ch: continue
    L = length(ch)
    print(f"{k}\n    L={L:7.2f}  {100*(L/341.60-1):+.2f} % (SC)  {100*(L/342.01-1):+.2f} % (ND)  lame:{crosses(ch)}  jambes:" + ", ".join(f"{a}-{b} {hav(P[a],P[b]):.1f}" for a,b in zip(ch,ch[1:])))
print("\nToutes permutations des 4 C {Cluny,Clermont,Cîteaux,Clairvaux} :")
for p in itertools.permutations(["Cluny","Clermont","Cîteaux","Clairvaux"]):
    if p[0]<p[-1]:
        L=length(p); print(f"   {' > '.join(p):45s} {L:7.2f} {'<== ±1 %' if abs(L/341.6-1)<=.01 else ''}")
