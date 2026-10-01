"""Orchestrateur É6 : test « forme des 4 cloches » (piste T2, non testée). Version optimisée (élagage par segment central).
Hypothèse : les 4 cloches reliées en pointillé autour de MLXVI dessinent la chaîne des 4 C (« relie-les une à une »).
Forme mesurée par T2 : U ouvert, segments ~ 1 : 1,85 : 1, deux angles ~90° de même sens.
Filtre forme : |ab|/|bc| et |cd|/|bc| à ±20 % de 1/1,85 ; virages en b et en c entre 60° et 120°, même sens.
Longueur : chaîne à ±1 % de D = 341,61 km (Tour → Battle → Sainte-Chapelle).
Contrôle : nombre de chaînes en U à ±1 % de 20 valeurs D aléatoires dans [250, 450] km.
Données : 111 lieux en C de solveurB_C_coords.json. Distances : haversine ; angles : projection locale."""
import json, math, sys, random
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(open("solveurB_C_coords.json", encoding="utf-8"))
names = list(d); P = [(d[k][0], d[k][1]) for k in names]; n = len(P)
R = 6371.0088
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
M = [[hav(P[i], P[j]) for j in range(n)] for i in range(n)]
lat0 = 47.0
XY = [(math.radians(p[1])*R*math.cos(math.radians(lat0)), math.radians(p[0])*R) for p in P]
def turn(a, b, c):
    v1 = (XY[b][0]-XY[a][0], XY[b][1]-XY[a][1]); v2 = (XY[c][0]-XY[b][0], XY[c][1]-XY[b][1])
    return math.degrees(math.atan2(v1[0]*v2[1]-v1[1]*v2[0], v1[0]*v2[0]+v1[1]*v2[1]))
lo, hi = (1/1.85)*0.8, (1/1.85)*1.2
shapes = []
for b in range(n):
    for c in range(n):
        if b == c or M[b][c] == 0: continue
        bc = M[b][c]
        As = [a for a in range(n) if a not in (b, c) and lo <= M[a][b]/bc <= hi]
        Ds = [x for x in range(n) if x not in (b, c) and lo <= M[c][x]/bc <= hi]
        for a in As:
            t1 = turn(a, b, c)
            if not 60 <= abs(t1) <= 120: continue
            for x in Ds:
                if x == a: continue
                t2 = turn(b, c, x)
                if 60 <= abs(t2) <= 120 and t1*t2 > 0 and names[a] < names[x]:
                    shapes.append((M[a][b]+bc+M[c][x], (names[a], names[b], names[c], names[x])))
D = 341.61
hits = sorted((round(L, 2), ch) for L, ch in shapes if abs(L-D)/D <= 0.01)
print(f"lieux: {n} ; chaînes en U (1:1,85:1, virages 60-120° même sens): {len(shapes)} ; dont ±1 % de {D} km: {len(hits)}")
for h in hits: print("  ", h)
random.seed(1)
ctrl = sorted(sum(1 for L, _ in shapes if abs(L-Dr)/Dr <= 0.01) for Dr in [random.uniform(250, 450) for _ in range(20)])
print("contrôle (20 D aléatoires 250-450 km), hits en U à ±1 % :", ctrl)
