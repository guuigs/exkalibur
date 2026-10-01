# -*- coding: utf-8 -*-
"""
T12-B : géométrie de Machrie Moor (île d'Arran) vs enluminure 11.
NGR (OSGB36) -> WGS84 + distances/angles en mètres de grille (exacts à <0.1% sur ~2 km).
Source des NGR : Wikipédia "Machrie Moor Stone Circles" (rév. 2026) + "Moss Farm Road Stone Circle".
"""
import math

# ---------------- NGR -> lat/lon (OSGB36 Airy) + Helmert -> WGS84 ----------------
def osgb36_to_wgs84(E, N):
    a = 6377563.396; b = 6356256.909; F0 = 0.9996012717
    lat0 = math.radians(49.0); lon0 = math.radians(-2.0)
    N0 = -100000.0; E0 = 400000.0
    e2 = 1.0 - (b*b)/(a*a)
    n = (a-b)/(a+b); n2 = n*n; n3 = n*n*n
    lat = lat0; M = 0.0
    for _ in range(10):
        lat = (N - N0 - M)/(a*F0) + lat
        Ma = (1 + n + 1.25*n2 + 1.25*n3) * (lat - lat0)
        Mb = (3*n + 3*n2 + 2.625*n3) * math.sin(lat-lat0) * math.cos(lat+lat0)
        Mc = (1.875*n2 + 1.875*n3) * math.sin(2*(lat-lat0)) * math.cos(2*(lat+lat0))
        Md = (35.0/24.0)*n3 * math.sin(3*(lat-lat0)) * math.cos(3*(lat+lat0))
        M = b * F0 * (Ma - Mb + Mc - Md)
    sinlat = math.sin(lat); coslat = math.cos(lat)
    nu = a*F0 / math.sqrt(1 - e2*sinlat*sinlat)
    rho = a*F0*(1-e2) / ((1-e2*sinlat*sinlat)**1.5)
    eta2 = nu/rho - 1
    tanlat = math.tan(lat); sec = 1.0/coslat
    dE = E - E0
    lat = lat - tanlat/(2*rho*nu)*dE**2 + tanlat/(24*rho*nu**3)*(5+3*tanlat**2+eta2-9*tanlat**2*eta2)*dE**4 - tanlat/(720*rho*nu**5)*(61+90*tanlat**2+45*tanlat**4)*dE**6
    lon = lon0 + sec/nu*dE - sec/(6*nu**3)*(nu/rho+2*tanlat**2)*dE**3 + sec/(120*nu**5)*(5+28*tanlat**2+24*tanlat**4)*dE**5 - sec/(5040*nu**7)*(61+662*tanlat**2+1320*tanlat**4+720*tanlat**6)*dE**7
    # OSGB36 -> WGS84 Helmert (Ordnance Survey 7-param)
    tx=-446.448; ty=125.157; tz=-542.060; s=20.4894e-6
    rx=-0.1502; ry=-0.2470; rz=-0.8421
    rxs=rx*math.pi/(180*3600); rys=ry*math.pi/(180*3600); rzs=rz*math.pi/(180*3600)
    # geocentric on Airy
    h=0.0
    X = (nu+h)*coslat*math.cos(lon)
    Y = (nu+h)*coslat*math.sin(lon)
    Z = ((1-e2)*nu+h)*sinlat
    X2 = tx + (1+s)*(X - rzs*Y + rys*Z)
    Y2 = ty + (1+s)*(rzs*X + Y - rxs*Z)
    Z2 = tz + (1+s)*(-rys*X + rxs*Y + Z)
    # back to lat/lon on GRS80
    a2 = 6378137.0; b2 = 6356752.314245; e22 = 1-(b2*b2)/(a2*a2)
    p = math.hypot(X2, Y2)
    lat2 = math.atan2(Z2, p*(1-e22))
    for _ in range(10):
        nu2 = a2/math.sqrt(1-e22*math.sin(lat2)**2)
        lat2 = math.atan2(Z2 + e22*nu2*math.sin(lat2), p)
    lon2 = math.atan2(Y2, X2)
    return math.degrees(lat2), math.degrees(lon2)

def dist_en(e1,n1,e2,n2):
    return math.hypot(e2-e1, n2-n1)
def brg_en(e1,n1,e2,n2):
    # angle from north, clockwise, in grid metres
    return (math.degrees(math.atan2(e2-e1, n2-n1)) + 360) % 360

sites = {
 "MM1":  (191200, 632390, "cercle 1 (ellipse 12.7x14.6m, 6 granites+5 gres=11)"),
 "MM2":  (191140, 632410, "cercle 2 (13.7m, 3 dalles 3.7-4.9m)"),
 "MM3":  (191020, 632440, "cercle 3 (9 pierres, 1 debout 4.3m)"),
 "MM4":  (191000, 632350, "cercle 4 (4 blocs granite ~0.9m)"),
 "MM5":  (190870, 632340, "cercle 5 Fingal (8+15=23 granites)"),
 "MM6":  (190730, 632370, "cairn chambre (2 dalles)"),
 "MM7":  (190630, 632530, "pierre levee 1.6m"),
 "MM8":  (190570, 632370, "cairn chambre (pierre 1.8m)"),
 "MM9":  (190500, 632400, "pierre levee (disparue)"),
 "MM10": (190060, 632650, "Moss Farm Road, cairn cercle 23m diam, 7+5=12 pierres"),
 "MM11": (191210, 632420, "cercle 11 (10 pierres + trous de poteaux BOIS)"),
 "MM12": (191000, 632400, "cercle 12 (12 fosses, enfoui, 2025)"),
 "Ballymichael": (192440, 632250, "3 blocs granite (4 a l'origine), ~1.2km E"),
}

print("="*100)
print("COORDONNEES WGS84 (lat, lon) des sites de Machrie Moor")
print("="*100)
for k,(e,n,d) in sites.items():
    la,lo = osgb36_to_wgs84(e,n)
    print(f"{k:12s} E={e:7d} N={n:7d}  ->  {la:.6f}, {lo:.6f}   ({d})")

print()
print("="*100)
print("MATRICE DES DISTANCES (metres de grille) entre sites")
print("="*100)
keys = list(sites.keys())
print("        " + "".join(f"{k[:5]:>8s}" for k in keys))
for k1 in keys:
    e1,n1,_ = sites[k1]
    row = f"{k1:8s}"
    for k2 in keys:
        e2,n2,_ = sites[k2]
        row += f"{dist_en(e1,n1,e2,n2):8.0f}"
    print(row)

print()
print("="*100)
print("PAIRES A ~1850 m (fenetre 1832-1868 m, i.e. 10 stades romains a +/-1%)")
print("="*100)
found = []
for i in range(len(keys)):
    for j in range(i+1, len(keys)):
        k1,k2 = keys[i], keys[j]
        e1,n1,_ = sites[k1]; e2,n2,_ = sites[k2]
        d = dist_en(e1,n1,e2,n2)
        if 1832 <= d <= 1868:
            found.append((k1,k2,d))
        # afficher aussi toutes les paires > 1500 m pour contexte
for k1,k2,d in found:
    print(f"  {k1} <-> {k2} : {d:.0f} m   (brg N-> {brg_en(sites[k1][0],sites[k1][1],sites[k2][0],sites[k2][1]):.1f} deg)")
if not found:
    print("  AUCUNE paire a 1850 +/-1% dans les sites listes.")
print("Toutes les paires >= 1200 m :")
for i in range(len(keys)):
    for j in range(i+1, len(keys)):
        k1,k2 = keys[i], keys[j]
        e1,n1,_ = sites[k1]; e2,n2,_ = sites[k2]
        d = dist_en(e1,n1,e2,n2)
        if d >= 1200:
            print(f"  {k1:12s} <-> {k2:12s} : {d:6.0f} m")

print()
print("="*100)
print("TRIANGLE des cercles impairs 1-3-5 (hypothese chiffres 1,3,5 de l'enluminure)")
print("="*100)
for a,b in [("MM1","MM3"),("MM3","MM5"),("MM5","MM1")]:
    e1,n1,_=sites[a]; e2,n2,_=sites[b]
    print(f"  {a} <-> {b} : {dist_en(e1,n1,e2,n2):.1f} m, brg {brg_en(e1,n1,e2,n2):.2f} deg")
# angles internes du triangle
import itertools
for P in itertools.permutations(["MM1","MM3","MM5"],3):
    pass
def angle_at(vertex, p1, p2):
    v = sites[vertex]; a = sites[p1]; b = sites[p2]
    x1,y1 = a[0]-v[0], a[1]-v[1]
    x2,y2 = b[0]-v[0], b[1]-v[1]
    ang = math.degrees(math.atan2(x2,y2) - math.atan2(x1,y1))
    ang = abs(ang % 360)
    return min(ang, 360-ang)
print(f"  angle en MM1 : {angle_at('MM1','MM3','MM5'):.2f} deg")
print(f"  angle en MM3 : {angle_at('MM3','MM1','MM5'):.2f} deg")
print(f"  angle en MM5 : {angle_at('MM5','MM1','MM3'):.2f} deg")

print()
print("="*100)
print("DISTANCES-CLES a comparer aux nombres de la chasse")
print("="*100)
pairs = [
 ("MM3","MM11", "troisieme/onzieme (1 stade ?)"),
 ("MM1","MM11", "1 et 11"),
 ("MM3","MM12", "3 et 12"),
 ("MM5","MM11", "5 et 11"),
 ("MM4","MM11", "4 et 11"),
]
for a,b,note in pairs:
    e1,n1,_=sites[a]; e2,n2,_=sites[b]
    print(f"  {a} <-> {b} : {dist_en(e1,n1,e2,n2):6.1f} m   ({note})")

# est-ce que le rapport MM3-MM11 (190m ~ 1 stade) x 10 = 1850-1900 m = un autre segment ?
print()
print("MM3<->MM11 x 10 = %.0f m" % (dist_en(*sites["MM3"][:2], *sites["MM11"][:2])*10))
