# -*- coding: utf-8 -*-
"""T12E_01 : géométrie du couloir de départ (600-614 km, cap 62-68° depuis Saint-Palais)."""
import math, json

R = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/"

def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*6371.0088*math.asin(math.sqrt(h))

def brg(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    y = math.sin(lo2-lo1)*math.cos(la2)
    x = math.cos(la1)*math.sin(la2) - math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return (math.degrees(math.atan2(y, x)) + 360) % 360

def dest(a, bearing_deg, d_km):
    la1, lo1 = map(math.radians, (a[0], a[1]))
    br = math.radians(bearing_deg)
    d = d_km / 6371.0088
    la2 = math.asin(math.sin(la1)*math.cos(d) + math.cos(la1)*math.sin(d)*math.cos(br))
    lo2 = lo1 + math.atan2(math.sin(br)*math.sin(d)*math.cos(la1),
                           math.cos(d) - math.sin(la1)*math.sin(la2))
    return (math.degrees(la2), math.degrees(lo2))

SP = (43.3291, -1.0347)
P11 = (45.42418, 6.01790)   # arrivée exacte É11 (~50 m château Bayard)
BAYARD = (45.4242, 6.0179)
TOUR = (45.429083, 6.030808)

print("=== T12E_01 : géométrie ===")
d = hav(SP, P11); b = brg(SP, P11)
print("Saint-Palais -> arrivée É11 : %.3f km, cap %.4f°" % (d, b))
print("Saint-Palais -> château Bayard : %.3f km, cap %.4f°" % (hav(SP, BAYARD), brg(SP, BAYARD)))
print("Saint-Palais -> tour d'Avalon : %.3f km, cap %.4f°" % (hav(SP, TOUR), brg(SP, TOUR)))

# Couloir : cap 62-68°, anneau 600-614 km
print("\n=== Couloir cap 62-68°, 600-614 km ===")
# largeur angulaire du couloir en km (à la distance moyenne 607 km)
mid = (62+68)/2
wid_km = 2*math.pi*6371.0088 * (68-62)/360.0 * math.cos(math.radians(43.9))
# plus précis : largeur d'arc à la latitude d'arrivée ~45.4°
wid_km2 = (68-62) * (math.pi/180) * hav(SP, (45.42418, 6.0179))  # approx arc
print("largeur du couloir (6° de cap) à 607 km : ~%.1f km (chordale approchée)" % (6 * math.pi/180 * 607.0))
print("largeur d'arc exacte à D=%.1f km : %.1f km" % (d, (68-62)*math.pi/180*d))

# bbox du secteur (4 coins + points extrêmes)
corners = []
for D in (600.0, 614.0):
    for B in (62.0, 68.0):
        corners.append(dest(SP, B, D))
lats = [c[0] for c in corners]; lons = [c[1] for c in corners]
# les coins du secteur sont en réalité convexes selon la géodésique ; élargir de ~0.05°
print("coins :", [(round(c[0],4), round(c[1],4)) for c in corners])
print("bbox couloir (approx) : lat %.4f..%.4f, lon %.4f..%.4f" % (min(lats)-0.03, max(lats)+0.03, min(lons)-0.03, max(lons)+0.03))

# lignes de référence : cap 62°, 65°, 68° -> intersections avec anneau
for B in (62.0, 64.99, 68.0):
    p = dest(SP, B, 607.0)
    print("  cap %5.2f°, D=607 km -> (%.5f, %.5f)  offset/É11 = %.2f km" % (B, p[0], p[1], hav(p, P11)))

print("\n=== Candidats (coords approx) : distance & cap depuis SP, offset à l'arrivée É11 ===")
cands = {
    "château Bayard (Pontcharra)": (45.4242, 6.0179),
    "tour d'Avalon (Saint-Maximin)": (45.429083, 6.030808),
    "Fort Barraux": (45.4356, 5.9871),
    "Montmélian (citadelle/ville)": (45.500, 6.055),
    "Arvillard (village)": (45.442, 6.120),
    "Yenne (village)": (45.700, 5.758),
    "Pontcharra (ville)": (45.433, 6.015),
    "Chapareillan": (45.463, 5.991),
    "Les Marches": (45.499, 6.000),
    "Apremont": (45.514, 5.958),
    "Chambéry (centre)": (45.565, 5.920),
    "Saint-Pierre-d'Entremont (Chartreuse)": (45.415, 5.853),
    "La Rochette": (45.457, 6.121),
    "Allevard": (45.394, 6.075),
    "Saint-Maximin (village)": (45.427, 6.035),
}
print("%-38s | %8s | %7s | %8s" % ("lieu", "D(SP)km", "cap°", "offset km"))
for k, (la, lo) in cands.items():
    print("%-38s | %8.1f | %7.2f | %8.2f" % (k, hav(SP, (la, lo)), brg(SP, (la, lo)), hav((la, lo), P11)))

out = dict(SP=SP, P11=P11, D=hav(SP,P11), cap=brg(SP,P11),
           corridor_width_km=(68-62)*math.pi/180*hav(SP,P11),
           bbox=[min(lats)-0.03, min(lons)-0.03, max(lats)+0.03, max(lons)+0.03])
json.dump(out, open(R + "T12E_01_geometrie.json", "w", encoding="utf-8"))
print("\n[SAVE] T12E_01_geometrie.json :", out)
