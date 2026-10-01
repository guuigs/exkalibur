"""É6 : vérification de la solution communautaire (Discord, salon libera-nos-a-malo, PtitNours 30/04/2026) :
 « pour les bleus ACDEINUTX anagramme de ND CITEAUX, pour les rouges ARUCALIVX anagramme de CLAIRVAUX ».
Mécanisme décrit sur le Discord : plateau 24 points = 24 lettres de l'alphabet latin médiéval (sans J, U/V, W → 23 + ?),
lu selon « Commencera le Père, et finiront les cieux » (Pater noster … in caelis, en latin) + « Amen » en hébreu.
Ici : (1) anagrammes exactes ; (2) chaîne Clairvaux–Cîteaux–Cluny–Clermont et ses variantes (Clairvaux, 3 homonymes),
comparée à D = Tour de Londres → Battle → Sainte-Chapelle ; (3) forme des 4 cloches (virage). Haversine, R = 6371,0088 km."""
import math, sys, collections, itertools
sys.stdout.reconfigure(encoding="utf-8")
def ms(s): return collections.Counter(c for c in s.upper() if c.isalpha())
print("== Anagrammes")
for src, tgt in [("ACDEINUTX", "NDCITEAUX"), ("ACDEINUTX", "CITEAUXND"), ("ARUCALIVX", "CLAIRVAUX")]:
    print(f"{src} ↔ {tgt} : {'EXACTE' if ms(src) == ms(tgt) else 'NON'}")
# coordonnées (Wikipedia, sites des abbayes / cathédrale)
P = {
 "Clairvaux (abbaye, Ville-sous-la-Ferté, Aube)": (48.1467, 4.7883),
 "Cîteaux (abbaye, Saint-Nicolas-lès-Cîteaux)": (47.1289, 5.0936),
 "Cluny (abbaye)": (46.4348054, 4.6585012),
 "Clermont (cathédrale)": (45.7787583, 3.0858573),
 "Tour de Londres": (51.5081124, -0.0759493),
 "Battle Abbey": (50.9143, 0.4870),
 "Sainte-Chapelle": (48.855375, 2.3449609),
 "Notre-Dame de Paris": (48.8530, 2.3499),
}
R = 6371.0088
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
C = ["Clairvaux (abbaye, Ville-sous-la-Ferté, Aube)", "Cîteaux (abbaye, Saint-Nicolas-lès-Cîteaux)", "Cluny (abbaye)", "Clermont (cathédrale)"]
segs = [hav(P[C[i]], P[C[i+1]]) for i in range(3)]
L = sum(segs)
print("\n== Chaîne des 4 C (ordre N → S)")
for i in range(3): print(f"  {C[i].split(' (')[0]} → {C[i+1].split(' (')[0]} : {segs[i]:.2f} km")
print(f"  TOTAL L = {L:.2f} km")
for tgt in ("Sainte-Chapelle", "Notre-Dame de Paris"):
    D = hav(P["Tour de Londres"], P["Battle Abbey"]) + hav(P["Battle Abbey"], P[tgt])
    print(f"  D (Tour → Battle → {tgt}) = {D:.2f} km ; écart L/D = {100*(L-D)/D:+.2f} %")
# point à distance L depuis la Tour en passant par Battle (ligne prolongée)
def brg(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    y = math.sin(lo2-lo1)*math.cos(la2); x = math.cos(la1)*math.sin(la2) - math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return (math.degrees(math.atan2(y, x))+360) % 360
def dest(a, t, d):
    la1, lo1 = map(math.radians, a); t = math.radians(t); dr = d/R
    la2 = math.asin(math.sin(la1)*math.cos(dr)+math.cos(la1)*math.sin(dr)*math.cos(t))
    lo2 = lo1+math.atan2(math.sin(t)*math.sin(dr)*math.cos(la1), math.cos(dr)-math.sin(la1)*math.sin(la2))
    return math.degrees(la2), math.degrees(lo2)
T, B = P["Tour de Londres"], P["Battle Abbey"]
dB = hav(T, B); X = dest(B, brg(T, B), L - dB)
print(f"\n== Point d'arrivée (Tour → Battle, prolongé jusqu'à L) : {X[0]:.5f}, {X[1]:.5f}")
for n in ("Sainte-Chapelle", "Notre-Dame de Paris"): print(f"  distance à {n} : {hav(X, P[n]):.2f} km")
print("\n== Forme : virages de la chaîne (cloches = U, deux virages ~90° même sens)")
lat0 = 47.0
xy = lambda p: (math.radians(p[1])*R*math.cos(math.radians(lat0)), math.radians(p[0])*R)
pts = [xy(P[c]) for c in C]
def turn(a, b, c):
    v1 = (b[0]-a[0], b[1]-a[1]); v2 = (c[0]-b[0], c[1]-b[1])
    return math.degrees(math.atan2(v1[0]*v2[1]-v1[1]*v2[0], v1[0]*v2[0]+v1[1]*v2[1]))
print(f"  virage à Cîteaux : {turn(*pts[0:3]):+.1f}° ; virage à Cluny : {turn(*pts[1:4]):+.1f}° (signe + = gauche)")
print(f"  rapports de segments : 1 : {segs[1]/segs[0]:.2f} : {segs[2]/segs[0]:.2f} (cloches ~ 1 : 1,85 : 1)")
