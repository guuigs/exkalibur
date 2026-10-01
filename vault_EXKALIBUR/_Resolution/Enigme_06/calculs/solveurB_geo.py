"""Bibliothèque commune solveur B (É6). Orthodromie haversine R=6371,0088 km (comme geo_e6.py).
Géocodage : API MediaWiki (Wikipedia en/fr, prop=coordinates) avec cache JSON local (solveurB_coords_cache.json)."""
import math, json, os, urllib.request, urllib.parse, sys
sys.stdout.reconfigure(encoding="utf-8")
R = 6371.0088
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "solveurB_coords_cache.json")
UA = {"User-Agent": "hermes-solveurB/1.0 (treasure-hunt research; contact: local)"}

def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(min(1, math.sqrt(h)))
def cap(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    y = math.sin(lo2-lo1)*math.cos(la2)
    x = math.cos(la1)*math.sin(la2) - math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return (math.degrees(math.atan2(y, x)) + 360) % 360
def xtrack(a, b, p):
    """distance signée (km) de p au grand cercle a->b (+ = à droite)"""
    d13 = hav(a, p)/R; t13 = math.radians(cap(a, p)); t12 = math.radians(cap(a, b))
    return math.asin(math.sin(d13)*math.sin(t13-t12))*R
def along(a, b, p):
    """abscisse curviligne (km) de la projection de p sur le grand cercle a->b"""
    d13 = hav(a, p)/R; xt = xtrack(a, b, p)/R
    c = math.cos(d13)/max(1e-12, math.cos(xt))
    return math.acos(max(-1, min(1, c)))*R*(1 if math.cos(math.radians(cap(a, p)-cap(a, b))) >= 0 else -1)
def dest(a, brg, d):
    la1, lo1 = map(math.radians, a); t = math.radians(brg); dr = d/R
    la2 = math.asin(math.sin(la1)*math.cos(dr) + math.cos(la1)*math.sin(dr)*math.cos(t))
    lo2 = lo1 + math.atan2(math.sin(t)*math.sin(dr)*math.cos(la1), math.cos(dr) - math.sin(la1)*math.sin(la2))
    return math.degrees(la2), math.degrees(lo2)

def _load():
    return json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
def _save(c):
    json.dump(c, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
def wiki_coords(titles, lang="en"):
    """titles -> {titre_demandé: (lat, lon, titre_résolu)} via Wikipedia API. Cache par lang|titre."""
    c = _load(); out = {}; todo = [t for t in titles if f"{lang}|{t}" not in c]
    for i in range(0, len(todo), 40):
        batch = todo[i:i+40]
        url = f"https://{lang}.wikipedia.org/w/api.php?" + urllib.parse.urlencode({
            "action": "query", "prop": "coordinates", "titles": "|".join(batch), "format": "json",
            "redirects": 1, "coprimary": "primary", "colimit": 500, "formatversion": 2})
        import time
        for _try in range(6):
            try:
                j = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40)); break
            except Exception as ex:   # 429 : on attend
                time.sleep(25*(_try+1))
        else: raise RuntimeError('Wikipedia API indisponible')
        q = j["query"]; norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
        red = {r["from"]: r["to"] for r in q.get("redirects", [])}
        pages = {p["title"]: p for p in q["pages"]}
        for t in batch:
            t2 = red.get(norm.get(t, t), norm.get(t, t)); p = pages.get(t2)
            if p and p.get("coordinates"):
                co = p["coordinates"][0]; c[f"{lang}|{t}"] = [co["lat"], co["lon"], t2]
            else:
                c[f"{lang}|{t}"] = None
    _save(c)
    for t in titles:
        v = c[f"{lang}|{t}"]; out[t] = tuple(v) if v else None
    return out
