# -*- coding: utf-8 -*-
"""Helpers É12 : projection locale, données IGN, MNT LiDAR, visibilité, altimétrie IGN."""
import json, math, urllib.request, urllib.parse
import numpy as np
from shapely.geometry import shape, Point
from shapely.strtree import STRtree
from shapely.ops import transform

S = r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/"
R = 6371008.8
TA = (45.429083, 6.030808)   # tour d'Avalon
RP = (45.42977, 6.03118)     # Rue du Rempart
CB = (45.423611, 6.018889)   # château Bayard
lat0 = 45.43
kx = 111320 * math.cos(math.radians(lat0)); ky = 110574

def xy(lon, lat): return ((lon - 6.03) * kx, (lat - lat0) * ky)
def inv(x, y): return (y / ky + lat0, x / kx + 6.03)
def hav(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1] - a[1]); dp = p2 - p1
    h = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(h))
def az(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1]-a[1])
    return (math.degrees(math.atan2(math.sin(dl)*math.cos(p2), math.cos(p1)*math.sin(p2)-math.sin(p1)*math.cos(p2)*math.cos(dl)))+360) % 360
def dest(p, brg, d):
    la1, lo1 = map(math.radians, p); b = math.radians(brg); dr = d / R
    la2 = math.asin(math.sin(la1)*math.cos(dr) + math.cos(la1)*math.sin(dr)*math.cos(b))
    lo2 = lo1 + math.atan2(math.sin(b)*math.sin(dr)*math.cos(la1), math.cos(dr)-math.sin(la1)*math.sin(la2))
    return (math.degrees(la2), math.degrees(lo2))

def load(name):
    d = json.load(open(S + "ign/" + name, encoding="utf-8")); out = []
    for f in d["features"]:
        try:
            out.append((transform(lambda x, y, z=None: xy(x, y), shape(f["geometry"])), f["properties"]))
        except Exception:
            pass
    return out

meta = json.load(open(S + "exk_e12/lidar_meta_1500.json")); BB = meta["BB"]; DLAT = meta["DLAT"]; DLON = meta["DLON"]
M = np.load(S + "exk_e12/mnt_1500_2.npy")
def alt(lat, lon):
    r = int(round((BB[2]-lat)/DLAT)); c = int(round((lon-BB[1])/DLON))
    if 0 <= r < M.shape[0] and 0 <= c < M.shape[1]: return float(M[r, c])
    return None
def visible(src, la, lo, h_obs=12, h_tgt=2, n=500):
    a0 = alt(*src) + h_obs; a1 = alt(la, lo)
    if a1 is None: return None, None
    a1 += h_tgt; worst = 0.0
    for k in range(1, n):
        t = k/n; z = alt(src[0]+(la-src[0])*t, src[1]+(lo-src[1])*t)
        line = a0 + (a1-a0)*t
        if z is not None and z > line + 0.5: worst = max(worst, z-line)
    return worst == 0.0, round(worst, 1)

def alti(points):
    lons = "|".join(f"{p[1]:.6f}" for p in points); lats = "|".join(f"{p[0]:.6f}" for p in points)
    url = "https://data.geopf.fr/altimetrie/1.0/calcul/alti/rest/elevation.json?" + urllib.parse.urlencode(
        dict(lon=lons, lat=lats, resource="ign_rge_alti_wld", zonly="true"))
    return json.loads(urllib.request.urlopen(url, timeout=90).read())["elevations"]

def wms(lat, lon, half=150, px=1200, layer="ORTHOIMAGERY.ORTHOPHOTOS", fn="x.jpg"):
    from PIL import Image; import io
    dlat = half/ky; dlon = half/kx
    url = ("https://data.geopf.fr/wms-r/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=" + layer +
           "&STYLES=&CRS=EPSG:4326&BBOX=%f,%f,%f,%f&WIDTH=%d&HEIGHT=%d&FORMAT=image/jpeg" % (lat-dlat, lon-dlon, lat+dlat, lon+dlon, px, px))
    b = urllib.request.urlopen(url, timeout=90).read(); im = Image.open(io.BytesIO(b)); im.save(S + "exk_e12/" + fn); return S + "exk_e12/" + fn

def sun_dec(day_of_year):
    g = 2*math.pi/365*(day_of_year-1)
    return math.degrees(0.006918-0.399912*math.cos(g)+0.070257*math.sin(g)-0.006758*math.cos(2*g)+0.000907*math.sin(2*g)-0.002697*math.cos(3*g)+0.00148*math.sin(3*g))
def sun_az_at_alt(dec, lat, h):
    """azimut (depuis N, sens horaire) du soleil levant quand sa hauteur vraie = h (deg)."""
    d, p, hh = map(math.radians, (dec, lat, h))
    cosA = (math.sin(d) - math.sin(p)*math.sin(hh)) / (math.cos(p)*math.cos(hh))
    return math.degrees(math.acos(max(-1, min(1, cosA))))
