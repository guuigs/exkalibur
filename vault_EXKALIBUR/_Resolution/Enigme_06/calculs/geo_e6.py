"""Énigme 6 : géométrie de base. Orthodromie (haversine, R = 6371,0088 km). Sortie : geo_e6.out.txt
Points : coordonnées de la carte de Guilhem (Carte/carte_guilhem_objets.json) quand elles existent,
sinon coordonnées Wikipedia/OSM notées ici (source à côté)."""
import math, sys
sys.stdout.reconfigure(encoding="utf-8")
R = 6371.0088
P = {
    "Tour de Londres": (51.5081124, -0.0759493),          # carte Guilhem
    "Battle Abbey (champ de Senlac)": (50.9143, 0.4870),  # Wikipedia Battle Abbey
    "Hastings (ville)": (50.854259, 0.573453),            # carte Guilhem
    "Sainte-Chapelle": (48.855375, 2.3449609),            # carte Guilhem
    "Clermont (cathédrale)": (45.7787583, 3.0858573),     # carte Guilhem
    "Cluny (abbaye)": (46.4348054, 4.6585012),            # carte Guilhem
    "Cadouin (cloître)": (44.8114955, 0.8737598),         # carte Guilhem
    "Clairvaux (abbaye)": (48.1467, 4.7883),              # Wikipedia Abbaye de Clairvaux
    "Cîteaux (abbaye)": (47.1289, 5.0936),                # Wikipedia Abbaye de Cîteaux
    "Troyes (cathédrale)": (48.2975, 4.0786),             # Wikipedia
    "Chartres (cathédrale)": (48.4478, 1.4875),           # Wikipedia
    "Notre-Dame de Paris": (48.8530, 2.3499),             # Wikipedia
}
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
def cap(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    y = math.sin(lo2-lo1)*math.cos(la2)
    x = math.cos(la1)*math.sin(la2) - math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return (math.degrees(math.atan2(y, x)) + 360) % 360
def xtrack(a, b, p):
    """distance signée de p au grand cercle a->b (km)"""
    d13 = hav(a, p)/R; t13 = math.radians(cap(a, p)); t12 = math.radians(cap(a, b))
    return math.asin(math.sin(d13)*math.sin(t13-t12))*R
def dest(a, brg, d):
    la1, lo1 = map(math.radians, a); t = math.radians(brg); dr = d/R
    la2 = math.asin(math.sin(la1)*math.cos(dr) + math.cos(la1)*math.sin(dr)*math.cos(t))
    lo2 = lo1 + math.atan2(math.sin(t)*math.sin(dr)*math.cos(la1), math.cos(dr) - math.sin(la1)*math.sin(la2))
    return math.degrees(la2), math.degrees(lo2)
T, B, H, SC = P["Tour de Londres"], P["Battle Abbey (champ de Senlac)"], P["Hastings (ville)"], P["Sainte-Chapelle"]
print("== Axe tour krak -> champ de bataille")
for n in ("Battle Abbey (champ de Senlac)", "Hastings (ville)", "Sainte-Chapelle", "Notre-Dame de Paris"):
    print(f"Tour -> {n:32s} {hav(T, P[n]):7.2f} km  cap {cap(T, P[n]):6.2f}°")
print(f"Écart latéral de Battle Abbey à l'axe Tour->Sainte-Chapelle : {xtrack(T, SC, B):+.2f} km")
print(f"Écart latéral de Hastings    à l'axe Tour->Sainte-Chapelle : {xtrack(T, SC, H):+.2f} km")
print(f"Tour->Battle + Battle->Sainte-Chapelle = {hav(T,B)+hav(B,SC):.2f} km (vs direct {hav(T,SC):.2f})")
print("\n== Chaîne des C de la carte de Guilhem (Cluny -> Clermont -> Cadouin)")
c = [P["Cluny (abbaye)"], P["Clermont (cathédrale)"], P["Cadouin (cloître)"]]
segs = [hav(c[i], c[i+1]) for i in range(len(c)-1)]
print("segments", [round(s, 2) for s in segs], "total", round(sum(segs), 2))
print("\n== Toutes distances entre candidats C (km)")
C = ["Clermont (cathédrale)", "Cluny (abbaye)", "Cadouin (cloître)", "Clairvaux (abbaye)", "Cîteaux (abbaye)", "Chartres (cathédrale)"]
for i, a in enumerate(C):
    for b in C[i+1:]:
        print(f"{a:24s} - {b:24s} {hav(P[a], P[b]):7.2f}")
print("\n== Point à distance D de la Tour, sur l'axe Tour->Battle (cap", round(cap(T, B), 2), "°)")
for D in (300, 320, 340, 343.5, 360, 380):
    la, lo = dest(T, cap(T, B), D)
    print(f"D={D:6.1f} km -> {la:.5f}, {lo:.5f}")
