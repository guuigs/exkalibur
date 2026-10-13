"""Bibliothèque : horizon réel (position des points de crête) et premier rayon de soleil, pour un observateur quelconque.
Données : dem2m (MNT 2 m), mns2m (MNS 2 m), big20m (MNT 20 m, 25 km). Voir getdem.py / getmns.py / getbig.py."""
import numpy as np, json, math, os, datetime
class Terrain:
    def __init__(self, DEM, near='mnt'):
        self.Dn = np.load(os.path.join(DEM, 'dem2m.npy')).astype(np.float64); self.Mn = json.load(open(os.path.join(DEM, 'dem2m.json')))
        self.Sn = np.load(os.path.join(DEM, 'mns2m.npy')).astype(np.float64) if near == 'mns' else self.Dn
        self.Db = np.load(os.path.join(DEM, 'big20m.npy')).astype(np.float64); self.Mb = json.load(open(os.path.join(DEM, 'big20m.json')))
    @staticmethod
    def samp(Z, M, lat, lon):
        i = (M['LA1'] - lat) / M['DLAT'] - 0.5; j = (lon - M['LO0']) / M['DLON'] - 0.5
        i0 = np.clip(np.floor(i).astype(int), 0, Z.shape[0] - 2); j0 = np.clip(np.floor(j).astype(int), 0, Z.shape[1] - 2)
        di = i - i0; dj = j - j0
        return Z[i0, j0] * (1 - di) * (1 - dj) + Z[i0 + 1, j0] * di * (1 - dj) + Z[i0, j0 + 1] * (1 - di) * dj + Z[i0 + 1, j0 + 1] * di * dj
    def ground(self, lat, lon):
        return float(self.samp(self.Dn, self.Mn, np.array([lat]), np.array([lon]))[0])
    def horizon(self, top, z0, az0=30, az1=200, step=0.05, rmin=30):
        KX = math.cos(math.radians(top[0])) * 111320.0; KY = 111132.0
        AZ = np.arange(az0, az1 + 1e-9, step)
        R1 = np.arange(rmin, 2550, 2.0); R2 = np.arange(2550, 30000, 20.0)
        out = np.zeros((AZ.size, 5))
        for k, az in enumerate(AZ):
            a = math.radians(az); best = (-99, 0, 0, 0, 0)
            for R, Z, M in ((R1, self.Sn, self.Mn), (R2, self.Db, self.Mb)):
                lat = top[0] + R * math.cos(a) / KY; lon = top[1] + R * math.sin(a) / KX
                z = self.samp(Z, M, lat, lon) - (1 - 0.13) * R ** 2 / (2 * 6371000.0)
                ang = np.degrees(np.arctan2(z - z0, R)); m = int(np.nanargmax(ang))
                if ang[m] > best[0]: best = (ang[m], R[m], lat[m], lon[m], z[m])
            out[k] = best
        return dict(AZ=AZ, HANG=out[:, 0], HR=out[:, 1], HLAT=out[:, 2], HLON=out[:, 3], HZ=out[:, 4], top=top, step=step, az0=az0)
def sunpos(dt, LAT, LON):
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
def first_light(date, H, limb=0.27, refr=0.5):
    LAT, LON = H['top']; t = datetime.datetime(date.year, date.month, date.day, 3, 0)
    n = H['AZ'].size
    while t.hour < 14:
        alt, az = sunpos(t, LAT, LON)
        k = int(round((az - H['az0']) / H['step']))
        if 0 <= k < n and alt + limb + refr >= H['HANG'][k]:
            return t, az, alt, (H['HLAT'][k], H['HLON'][k], H['HR'][k], H['HZ'][k], H['HANG'][k])
        t += datetime.timedelta(seconds=20)
    return None
