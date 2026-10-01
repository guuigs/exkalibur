# -*- coding: utf-8 -*-
"""T12C_00 : astronomie (lever du soleil : déclinaison, azimut, heure) + contrôle d'orientation du MNT."""
import math, json, numpy as np

S = r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/"
R = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/"

# ---- astronomie ----
def jd_gregorian(Y, M, D):
    a = math.floor((14 - M) / 12); y = Y + 4800 - a; m = M + 12*a - 3
    return D + math.floor((153*m + 2)/5) + 365*y + math.floor(y/4) - math.floor(y/100) + math.floor(y/400) - 32045 - 0.5

def jd_julian(Y, M, D):
    a = math.floor((14 - M) / 12); y = Y + 4800 - a; m = M + 12*a - 3
    return D + math.floor((153*m + 2)/5) + 365*y + math.floor(y/4) - 32083 - 0.5

def sun_decl(jd):
    n = jd - 2451545.0
    L = (280.460 + 0.9856474*n) % 360
    g = math.radians((357.528 + 0.9856003*n) % 360)
    lam = math.radians(L + 1.915*math.sin(g) + 0.020*math.sin(2*g))
    eps = math.radians(23.439 - 0.0000004*n)
    return math.degrees(math.asin(math.sin(eps)*math.sin(lam)))

def sun_az(dec_deg, lat_deg, alt_deg):
    dec = math.radians(dec_deg); lat = math.radians(lat_deg); alt = math.radians(alt_deg)
    cosH = (math.sin(alt) - math.sin(lat)*math.sin(dec)) / (math.cos(lat)*math.cos(dec))
    H = math.degrees(math.acos(max(-1, min(1, cosH))))
    cosA = (math.sin(dec) - math.sin(lat)*math.sin(alt)) / (math.cos(lat)*math.cos(alt))
    A = math.degrees(math.acos(max(-1, min(1, cosA))))
    return A, H

LAT, LON = 45.429083, 6.030808
print("=== T12C_00 : astronomie ===")
print("Position de référence :", LAT, LON)

cases = [
    ("30/04/1524 JULIEN (mort Bayard, calendrier historique)", jd_julian(1524, 4, 30)),
    ("30/04/1524 GREGORIEN proleptique", jd_gregorian(1524, 4, 30)),
    ("20/03 equinoxe printemps (1524 grég.)", jd_gregorian(1524, 3, 20)),
    ("23/09 equinoxe automne (1524 grég.)", jd_gregorian(1524, 9, 23)),
    ("21/06 solstice ete (1524 grég.)", jd_gregorian(1524, 6, 21)),
    ("21/12 solstice hiver (1524 grég.)", jd_gregorian(1524, 12, 21)),
    ("30/04/2026 (référence moderne, grég.)", jd_gregorian(2026, 4, 30)),
]
print("\n%-55s %8s | azimut lever | heure(solaire) | azimut a 5deg | azimut a 10deg" % ("date", "decl"))
for name, jd in cases:
    dec = sun_decl(jd)
    Ar, Hr = sun_az(dec, LAT, -0.833)
    A5, H5 = sun_az(dec, LAT, 5.0)
    A10, H10 = sun_az(dec, LAT, 10.0)
    th = 12.0 - Hr/15.0
    print("%-55s %8.3f | %9.2f deg | %8.2f h | %9.2f deg | %9.2f deg" % (name, dec, Ar, th, A5, A10))

print("\n--- sensibilite date (declinaison -> azimut lever) ---")
print("jour (grég.) : azimut lever (deg)")
for d in range(80, 141, 2):  # 21 mars (80) -> 20 mai (140)
    dec = sun_decl(jd_gregorian(1524, 1, 1) + (d - 1))
    Ar, _ = sun_az(dec, LAT, -0.833)
    if d % 10 == 0 or d in (91, 120, 130):
        print("  %3d (%s) : %6.2f" % (d, ("%.0f" % 0), Ar))

# ---- orientation MNT ----
print("\n=== Contrôle d'orientation du MNT ===")
meta = json.load(open(S + "lidar_meta_1500.json"))
BB = meta["BB"]; n = meta["n"]
la0, lo0, la1, lo1 = BB
mnt = np.load(S + "mnt_1500_2.npy")
def ij(lat, lon):
    i = (la1 - lat) / (la1 - la0) * (n - 1)
    j = (lon - lo0) / (lo1 - lo0) * (n - 1)
    return int(round(i)), int(round(j))
pts = {
    "Tour d'Avalon": (45.429083, 6.030808),
    "chateau Bayard": (45.4242, 6.0179),
    "Breda (gorge)": (45.43323, 6.02982),
    "Fort Barraux": (45.4356, 5.9871),
    "Ruisseau Rebouchet": (45.42554, 6.03362),
    "Ruisseau Perriere": (45.42090, 6.02234),
}
for k, (la, lo) in pts.items():
    i, j = ij(la, lo)
    inb = (0 <= i < n and 0 <= j < n)
    z = mnt[i, j] if inb else None
    print("  %-22s lat=%.5f lon=%.5f -> i=%4d j=%4d  z=%s %s" % (k, la, lo, i, j, ("%.1f" % z) if z is not None else "NA", "" if inb else "HORS MNT"))
print("MNT min/max z : %.1f / %.1f" % (mnt.min(), mnt.max()))
print("Breda gorge : z doit etre ~270 m et i petit (nord) -> verifie l'orientation N->S")
