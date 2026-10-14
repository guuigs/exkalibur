"""Lune au matin des dates clés de 1524 (calendrier julien), vue d'un point de la butte d'Avalon.
Éphéméride : Meeus, Astronomical Algorithms, ch. 47 (termes principaux, précision ~0,05°),
parallaxe topocentrique, réfraction de Bennett, horizon réel (fichier H_*.npz de horizon_lib).
Usage : python3 lune_1524.py DEM_DIR [H_esplanade.npz]
Sortie : pour chaque nuit, phase, heure et azimut du lever du bord supérieur au-dessus de l'horizon réel,
et position de la lune au premier rayon du soleil."""
import math, sys, os, datetime
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from horizon_lib import sunpos

R = math.radians
LA = [(0,0,1,0,6288774,-20905355),(2,0,-1,0,1274027,-3699111),(2,0,0,0,658314,-2955968),(0,0,2,0,213618,-569925),
      (0,1,0,0,-185116,48888),(0,0,0,2,-114332,-3149),(2,0,-2,0,58793,246158),(2,-1,-1,0,57066,-152138),
      (2,0,1,0,53322,-170733),(2,-1,0,0,45758,-204586),(0,1,-1,0,-40923,-129620),(1,0,0,0,-34720,108743),
      (0,1,1,0,-30383,104755),(2,0,0,-2,15327,10321),(0,0,1,2,-12528,0),(0,0,1,-2,10980,79661),
      (4,0,-1,0,10675,-34782),(0,0,3,0,10034,-23210),(4,0,-2,0,8548,-21636),(2,1,-1,0,-7888,24208),
      (2,1,0,0,-6766,30824),(1,0,-1,0,-5163,-8379),(1,1,0,0,4987,-16675),(2,-1,1,0,4036,-12831),
      (2,0,2,0,3994,-10445),(4,0,0,0,3861,-11650),(2,0,-3,0,3665,14403),(0,1,-2,0,-2689,-7003),
      (2,0,-1,2,-2602,0),(2,-1,-2,0,2390,10056),(1,0,1,0,-2348,6322),(2,-2,0,0,2236,-9884)]
LB = [(0,0,0,1,5128122),(0,0,1,1,280602),(0,0,1,-1,277693),(2,0,0,-1,173237),(2,0,-1,1,55413),
      (2,0,-1,-1,46271),(2,0,0,1,32573),(0,0,2,1,17198),(2,0,1,-1,9266),(0,0,2,-1,8822),
      (2,-1,0,-1,8216),(2,0,-2,-1,4324),(2,0,1,1,4200),(2,1,0,-1,-3359),(2,-1,-1,1,2463),
      (2,-1,0,1,2211),(2,-1,-1,-1,2065),(0,1,-1,-1,-1870),(4,0,-1,-1,1828),(0,1,0,1,-1794)]
DT_S = 190.0  # ΔT vers 1524 (Morrison & Stephenson), en secondes

def jd_greg(dt):
    return (dt - datetime.datetime(2000, 1, 1, 12)) / datetime.timedelta(days=1) + 2451545.0

def moon_geo(jd_ut):
    T = (jd_ut + DT_S / 86400 - 2451545.0) / 36525
    Lp = 218.3164477 + 481267.88123421*T - 0.0015786*T*T + T**3/538841
    D = 297.8501921 + 445267.1114034*T - 0.0018819*T*T + T**3/545868
    M = 357.5291092 + 35999.0502909*T - 0.0001536*T*T
    Mp = 134.9633964 + 477198.8675055*T + 0.0087414*T*T + T**3/69699
    F = 93.2720950 + 483202.0175233*T - 0.0036539*T*T
    A1 = 119.75 + 131.849*T; A2 = 53.09 + 479264.290*T; A3 = 313.45 + 481266.484*T
    E = 1 - 0.002516*T - 0.0000074*T*T
    sl = sr = sb = 0.0
    for d, m, mp, f, cl, cr in LA:
        arg = R(d*D + m*M + mp*Mp + f*F); e = E**abs(m)
        sl += cl*e*math.sin(arg); sr += cr*e*math.cos(arg)
    for d, m, mp, f, cb in LB:
        sb += cb*E**abs(m)*math.sin(R(d*D + m*M + mp*Mp + f*F))
    sl += 3958*math.sin(R(A1)) + 1962*math.sin(R(Lp - F)) + 318*math.sin(R(A2))
    sb += (-2235*math.sin(R(Lp)) + 382*math.sin(R(A3)) + 175*math.sin(R(A1 - F)) + 175*math.sin(R(A1 + F))
           + 127*math.sin(R(Lp - Mp)) - 115*math.sin(R(Lp + Mp)))
    lam = (Lp + sl/1e6) % 360; bet = sb/1e6; dist = 385000.56 + sr/1000
    eps = 23.4392911 - 0.0130042*T
    ra = math.degrees(math.atan2(math.sin(R(lam))*math.cos(R(eps)) - math.tan(R(bet))*math.sin(R(eps)), math.cos(R(lam))))
    dec = math.degrees(math.asin(math.sin(R(bet))*math.cos(R(eps)) + math.cos(R(bet))*math.sin(R(eps))*math.sin(R(lam))))
    return ra % 360, dec, dist, lam

def moon_altaz(dt_ut, lat, lon):
    jd = jd_greg(dt_ut); ra, dec, dist, lam = moon_geo(jd)
    T = (jd - 2451545.0) / 36525
    gmst = (280.46061837 + 360.98564736629*(jd - 2451545.0) + 0.000387933*T*T) % 360
    H = R((gmst + lon - ra) % 360); phi = R(lat); d = R(dec)
    alt = math.degrees(math.asin(math.sin(phi)*math.sin(d) + math.cos(phi)*math.cos(d)*math.cos(H)))
    az = (math.degrees(math.atan2(math.sin(H), math.cos(H)*math.sin(phi) - math.tan(d)*math.cos(phi))) + 180) % 360
    par = math.degrees(math.asin(6378.14/dist)); alt_t = alt - par*math.cos(R(alt))
    sd = math.degrees(math.asin(1737.4/dist))
    return alt_t, az, sd, lam

def refr(h):
    return 1/math.tan(R(h + 7.31/(h + 4.4)))/60 if h > -1.5 else 0.6

def sun_lambda(jd):
    T = (jd - 2451545.0)/36525
    L0 = 280.46646 + 36000.76983*T; Mm = R(357.52911 + 35999.05029*T)
    return (L0 + 1.914602*math.sin(Mm) + 0.019993*math.sin(2*Mm)) % 360

if __name__ == '__main__':
    DEM = sys.argv[1]; HF = sys.argv[2] if len(sys.argv) > 2 else 'H_esplanade.npz'
    H = np.load(os.path.join(DEM, HF)); AZ = H['AZ']; HANG = H['HANG']
    LAT, LON = 45.42891, 6.03112  # esplanade (vp)
    def hang(az):
        k = int(round((az - AZ[0]) / (AZ[1] - AZ[0])))
        return HANG[k] if 0 <= k < AZ.size else None
    cases = [('veille du 29 au 30 avril 1524 jul', datetime.datetime(1524, 5, 9, 20)),
             ('veille du 30 avril au 1er mai 1524 jul', datetime.datetime(1524, 5, 10, 20)),
             ('veille pascale 26-27 mars 1524 jul', datetime.datetime(1524, 4, 5, 20))]
    for lab, t0 in cases:
        t = t0; rise = None
        while t < t0 + datetime.timedelta(hours=14):
            alt, az, sd, lam = moon_altaz(t, LAT, LON); h = hang(az)
            if h is not None and alt + sd + refr(max(alt, h)) >= h and rise is None:
                rise = (t, az, alt, h)
            salt, saz = sunpos(t, LAT, LON); hs = hang(saz)
            if hs is not None and salt + 0.27 + refr(max(salt, hs)) >= hs:
                break
            t += datetime.timedelta(seconds=30)
        jd = jd_greg(t); elong = (lam - sun_lambda(jd)) % 360
        illum = (1 - math.cos(R(elong))) / 2
        print('==', lab)
        print('   élongation lune-soleil %.1f° (%s), fraction éclairée %.0f %%' % (elong, 'décroissante' if elong > 180 else 'croissante', 100*illum))
        if rise:
            tl = rise[0] + datetime.timedelta(minutes=4*LON)
            print('   lever du bord sup. au-dessus de l\'horizon réel : %s UT (%s h solaire loc.), az %.2f°, horizon %.2f°' % (rise[0].strftime('%H:%M'), tl.strftime('%H:%M'), rise[1], rise[3]))
        alt, az, sd, lam = moon_altaz(t, LAT, LON)
        print('   au premier rayon du soleil (%s UT, az soleil %.2f°) : lune az %.2f°, haut. %.2f°' % (t.strftime('%H:%M'), saz, az, alt))
