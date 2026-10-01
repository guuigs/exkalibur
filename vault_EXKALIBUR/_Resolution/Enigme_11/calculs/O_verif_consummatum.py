"""É11 Consummatum est — vérification indépendante.
Lectures testées :
  - Montsalvage = le Palais (FAQ05-112 : « le Palais et Montsalvage désignent le même lieu ») = SAINT-PALAIS (64),
    ancienne capitale de la Navarre (indice officiel du 04/06/2026 « Montsalvage, l'ancienne capitale »),
    bordée par la Bidouze et la JOYEUSE (épée de Charlemagne ; FAQ07-032 « un cours d'eau devrait vous mettre la puce à l'oreille »).
  - « la même distance » = Eilean Donan → Machrie Moor (É10 ; FAQ03-224).
  - « 1f' fois très parfaitement » = π (FAQ07-231/279 : opération mathématique, « très exactement » ; la Table « parfaitement ronde » de l'É5, FAQ05-108).
  - dernier chevalier = Bayard (« le dernier chevalier », né au château Bayard, Pontcharra) → on teste SANS lui imposer la direction :
    distance Saint-Palais → château Bayard comparée à D·π.
Test du hasard : part des communes françaises situées à ±Δ de D·π depuis Saint-Palais (l'anneau), et rang de π parmi des multiplicateurs « naturels »."""
import json, math, sys
sys.stdout.reconfigure(encoding="utf-8")
R = 6371.0088
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
def brg(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    y = math.sin(lo2-lo1)*math.cos(la2); x = math.cos(la1)*math.sin(la2)-math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return math.degrees(math.atan2(y, x)) % 360
# Coordonnées Wikipédia (API coordinates, 30/09/2026)
ED = (57.27402778, -5.51611111)   # Eilean Donan
MM = (55.540829, -5.313655)       # Machrie Moor Stone Circles
SP = (43.3292, -1.0325)           # Saint-Palais
SG = (43.299265, -1.0345171)      # Stèle de Gibraltar (variante de départ citée sur Discord)
CB = (45.423611, 6.018889)        # Château Bayard (Pontcharra)
TA = (45.4288, 6.03078)           # Tour d'Avalon (Saint-Maximin)
D = hav(ED, MM); Dpi = D*math.pi
print(f"D (É10) = {D:.3f} km ; D·π = {Dpi:.2f} km")
for n, s in [("Saint-Palais", SP), ("Stèle de Gibraltar", SG)]:
    for m, t in [("château Bayard", CB), ("tour d'Avalon", TA)]:
        d = hav(s, t); print(f"  {n:18s} → {m:14s} : {d:7.2f} km  = D × {d/D:.4f} (π = 3.1416 ; écart {100*(d-Dpi)/Dpi:+.3f} %)  cap {brg(s, t):.2f}°")
print("\n== Hasard 1 : autres multiplicateurs « naturels » (depuis Saint-Palais vers château Bayard)")
d = hav(SP, CB)
for nm, k in [("π", math.pi), ("e", math.e), ("φ", (1+5**.5)/2), ("√10", 10**.5), ("3", 3), ("11", 11), ("23", 23), ("6", 6), ("4", 4)]:
    print(f"  {nm:4s} : D×k = {D*k:8.2f} km  écart à SP→Bayard {100*(D*k-d)/d:+8.3f} %")
print("\n== Hasard 2 : communes françaises dans l'anneau D·π ± 0,5 km autour de Saint-Palais")
com = json.load(open(r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Enigme_06/calculs/T1data/communes.json", encoding="utf-8"))
pts = [(c["nom"], (c["centre"]["coordinates"][1], c["centre"]["coordinates"][0])) for c in com if c.get("centre")]
ring = [(n, p) for n, p in pts if abs(hav(SP, p)-Dpi) <= 0.5]
print(f"  {len(ring)} communes sur {len(pts)} ({100*len(ring)/len(pts):.2f} %) : la distance seule NE désigne PAS Bayard, il faut l'angle.")
print("  Dans l'anneau, secteur 60–70° :", [n for n, p in ring if 60 <= brg(SP, p) <= 70])
print("\n== Angle requis (le « dernier chevalier ») — NON résolu")
a = brg(SP, CB)
print(f"  cap Saint-Palais → château Bayard = {a:.3f}° (azimut géographique)")
print(f"  relatif à l'axe de la lame É1 (352,90°) : {(a-352.9012)%360:.3f}° ; 23·π = {23*math.pi:.3f}° (proposition Discord, arrive à ~1,7 km)")
print(f"  rose des vents à 8 branches (I..VIII) : 65° ≈ entre I (N) et III (E)… aucune lecture exacte trouvée")
