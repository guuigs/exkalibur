"""Horizon réel vu du sommet du donjon d'Avalon, avec la POSITION du point de crête pour chaque cap,
puis point de l'horizon où apparaît le premier rayon du soleil à une date donnée.
Proche (< 2,6 km) : MNT 2 m (ou MNS avec NEAR=mns) ; loin (jusqu'à 30 km) : MNT 20 m. Données WMS-R IGN."""
import numpy as np, json, math, os, sys, datetime
DEM = sys.argv[1]
top = (45.428899, 6.031011); z0 = 437.64 - 1.0
KX = math.cos(math.radians(top[0])) * 111320.0; KY = 111132.0
def load(n):
    return np.load(os.path.join(DEM, n + '.npy')).astype(np.float64), json.load(open(os.path.join(DEM, n + '.json')))
NEAR = os.environ.get('NEAR', 'mnt')
Dn, Mn = load('dem2m'); Sn = np.load(os.path.join(DEM, 'mns2m.npy')).astype(np.float64) if NEAR == 'mns' else Dn
Db, Mb = load('big20m')
def samp(Z, M, lat, lon):
    i = (M['LA1'] - lat) / M['DLAT'] - 0.5; j = (lon - M['LO0']) / M['DLON'] - 0.5
    i0 = np.clip(np.floor(i).astype(int), 0, Z.shape[0] - 2); j0 = np.clip(np.floor(j).astype(int), 0, Z.shape[1] - 2)
    di = i - i0; dj = j - j0
    return Z[i0, j0] * (1 - di) * (1 - dj) + Z[i0 + 1, j0] * di * (1 - dj) + Z[i0, j0 + 1] * (1 - di) * dj + Z[i0 + 1, j0 + 1] * di * dj
AZ = np.arange(30, 200.0001, 0.05)
R1 = np.arange(30, 2550, 2.0); R2 = np.arange(2550, 30000, 20.0)
HANG = np.zeros(AZ.size); HR = np.zeros(AZ.size); HLAT = np.zeros(AZ.size); HLON = np.zeros(AZ.size); HZ = np.zeros(AZ.size)
for k, az in enumerate(AZ):
    a = math.radians(az)
    best = (-99, 0, 0, 0, 0)
    for R, Z, M in ((R1, Sn, Mn), (R2, Db, Mb)):
        lat = top[0] + R * math.cos(a) / KY; lon = top[1] + R * math.sin(a) / KX
        z = samp(Z, M, lat, lon) - (1 - 0.13) * R ** 2 / (2 * 6371000.0)
        ang = np.degrees(np.arctan2(z - z0, R)); m = int(np.nanargmax(ang))
        if ang[m] > best[0]: best = (ang[m], R[m], lat[m], lon[m], z[m])
    HANG[k], HR[k], HLAT[k], HLON[k], HZ[k] = best
np.savez(os.path.join(DEM, 'horizon_pts_%s.npz' % NEAR), AZ=AZ, HANG=HANG, HR=HR, HLAT=HLAT, HLON=HLON, HZ=HZ)
LAT, LON = top
def sunpos(dt):  # NOAA, dt en UTC
    jd = (dt - datetime.datetime(2000, 1, 1, 12)) / datetime.timedelta(days=1) + 2451545.0; T = (jd - 2451545.0) / 36525
    L0 = (280.46646 + T * (36000.76983 + T * 0.0003032)) % 360; Mm = 357.52911 + T * (35999.05029 - 0.0001537 * T)
    e = 0.016708634 - T * (0.000042037 + 0.0000001267 * T)
    C = math.sin(math.radians(Mm)) * (1.914602 - T * (0.004817 + 0.000014 * T)) + math.sin(math.radians(2 * Mm)) * (0.019993 - 0.000101 * T) + math.sin(math.radians(3 * Mm)) * 0.000289
    lam = L0 + C - 0.00569 - 0.00478 * math.sin(math.radians(125.04 - 1934.136 * T))
    eps = 23 + (26 + ((21.448 - T * (46.815 + T * (0.00059 - T * 0.001813)))) / 60) / 60 + 0.00256 * math.cos(math.radians(125.04 - 1934.136 * T))
    dec = math.degrees(math.asin(math.sin(math.radians(eps)) * math.sin(math.radians(lam))))
    y = math.tan(math.radians(eps / 2)) ** 2
    eqt = 4 * math.degrees(y * math.sin(2 * math.radians(L0)) - 2 * e * math.sin(math.radians(Mm)) + 4 * e * y * math.sin(math.radians(Mm)) * math.cos(2 * math.radians(L0)) - 0.5 * y * y * math.sin(4 * math.radians(L0)) - 1.25 * e * e * math.sin(2 * math.radians(Mm)))
    tst = (dt.hour * 60 + dt.minute + dt.second / 60 + eqt + 4 * LON) % 1440; ha = tst / 4 - 180
    phi = math.radians(LAT); d = math.radians(dec); h = math.radians(ha)
    alt = math.degrees(math.asin(math.sin(phi) * math.sin(d) + math.cos(phi) * math.cos(d) * math.cos(h)))
    az = (math.degrees(math.atan2(math.sin(h), math.cos(h) * math.sin(phi) - math.tan(d) * math.cos(phi))) + 180) % 360
    return alt, az
def first_light(date, limb=0.27, refr=0.5):
    t = datetime.datetime(date.year, date.month, date.day, 3, 0)
    while t.hour < 13:
        alt, az = sunpos(t)
        if 30 <= az <= 200:
            k = int(round((az - 30) / 0.05))
            if alt + limb + refr >= HANG[k]:
                return t, az, alt, (HLAT[k], HLON[k], HR[k], HZ[k], HANG[k])
        t += datetime.timedelta(seconds=20)
if __name__ == '__main__':
    from geographiclib.geodesic import Geodesic
    G = Geodesic.WGS84
    pairs = json.loads(os.environ.get('PAIRS', '[["1 mai","2026-05-01"],["21 déc","2026-12-21"]]'))
    res = {}
    for name, ds in pairs:
        d = datetime.date.fromisoformat(ds); t, az, alt, (la, lo, r, z, ha) = first_light(d)
        res[name] = (la, lo)
        print('%-22s %s UTC  az %6.2f°  horizon %.2f°  point de crête %.5f %.5f  à %6.0f m (alt %.0f m)' % (name, t.strftime('%H:%M:%S'), az, ha, la, lo, r, z))
    ks = list(res)
    for i in range(len(ks)):
        for j in range(i + 1, len(ks)):
            print('  distance %s – %s : %.0f m' % (ks[i], ks[j], G.Inverse(*res[ks[i]], *res[ks[j]])['s12']))
