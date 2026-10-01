"""Helpers Exkalibur (É12 / IGN). Import: exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())"""
import json, re, math, os, urllib.request, urllib.parse
from collections import Counter
R = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/"; Z = R + "_Resolution/"
S = r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/ign/"
CB = (45.423611, 6.018889)   # château Bayard
TA = (45.4288, 6.03078)      # tour d'Avalon (approx, à affiner)
def get(url, t=120):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Exkalibur research)"})
    return urllib.request.urlopen(req, timeout=t).read().decode("utf-8", "replace")
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*6371.0088*math.asin(math.sqrt(h))
def brg(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    y = math.sin(lo2-lo1)*math.cos(la2); x = math.cos(la1)*math.sin(la2) - math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return (math.degrees(math.atan2(y, x)) + 360) % 360
def _pts(g):
    t = g["type"]; c = g["coordinates"]
    if t == "Point": return [c]
    out = []
    def rec(x):
        if isinstance(x[0], (int, float)): out.append(x)
        else:
            for y in x: rec(y)
    rec(c); return out
def cen(g):
    p = _pts(g); return (sum(q[1] for q in p)/len(p), sum(q[0] for q in p)/len(p))
def load(L): return json.load(open(S + L + ".geojson", encoding="utf-8"))["features"]
def faq():
    d = json.load(open(Z + "Communaute/faq_officielle_auteur.json", encoding="utf-8")); items = []
    def walk(o):
        if isinstance(o, dict):
            if "q" in o: items.append(o)
            else:
                for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(d); return items
def wfs(layer, bb, maxf=20000):
    feats = []; start = 0
    while True:
        u = ("https://data.geopf.fr/wfs/ows?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES=" + layer +
             "&OUTPUTFORMAT=application/json&SRSNAME=EPSG:4326&COUNT=5000&STARTINDEX=%d&BBOX=%f,%f,%f,%f,urn:ogc:def:crs:EPSG::4326" % (start, *bb))
        j = json.loads(get(u, 180)); f = j.get("features", []); feats += f
        if len(f) < 5000 or len(feats) >= maxf: break
        start += 5000
    return feats
