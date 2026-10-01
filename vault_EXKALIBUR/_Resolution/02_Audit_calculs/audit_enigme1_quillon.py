"""Audit Phase 0 (complement) : 'jusqu'a pres de 11 lieues vers le couchant depuis Rennes-le-Chateau,
dans ce chateau ou brule la memoire du pays cathare' -> quels chateaux cathares a l'ouest, et a combien ?
Orthodromie haversine R=6371.0088 km ; coordonnees OSM Nominatim (cache coords.json).
"""
import json, math, os, sys, time, urllib.parse, urllib.request
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__)); CACHE = os.path.join(HERE, "coords.json")
cache = json.load(open(CACHE, encoding="utf-8"))
EXTRA = {"Château de Puivert": "Château de Puivert, Aude", "Château de Roquefixade": "Château de Roquefixade, Ariège",
         "Château de Lordat": "Château de Lordat, Ariège", "Château d'Usson": "Château d'Usson, Rouze, Ariège",
         "Château de Montaillou": "Montaillou, Ariège", "Château de Montréal-de-Sos": "Montréal-de-Sos, Auzat, Ariège",
         "Château de Termes": "Château de Termes, Aude", "Château d'Arques": "Château d'Arques, Aude",
         "Château de Peyrepertuse": "Château de Peyrepertuse, Aude", "Château de Quéribus": "Château de Quéribus, Aude",
         "Château de Puilaurens": "Château de Puilaurens, Aude", "Château de Lastours": "Châteaux de Lastours, Aude",
         "Château de Carcassonne": "Château comtal, Carcassonne"}
for k, q in EXTRA.items():
    if k not in cache:
        u = "https://nominatim.openstreetmap.org/search?format=json&limit=1&q=" + urllib.parse.quote(q)
        r = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "exkalibur-audit/1.0"}), timeout=30).read())
        cache[k] = {"lat": float(r[0]["lat"]), "lon": float(r[0]["lon"]), "osm": r[0]["display_name"]} if r else None
        time.sleep(1.1)
json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
def hav(a, b):
    p1, p2 = math.radians(a["lat"]), math.radians(b["lat"]); dp, dl = p2 - p1, math.radians(b["lon"] - a["lon"])
    return 2 * 6371.0088 * math.asin(math.sqrt(math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2))
def brg(a, b):
    p1, p2 = math.radians(a["lat"]), math.radians(b["lat"]); dl = math.radians(b["lon"] - a["lon"])
    return (math.degrees(math.atan2(math.sin(dl)*math.cos(p2), math.cos(p1)*math.sin(p2)-math.sin(p1)*math.cos(p2)*math.cos(dl))) + 360) % 360
R = cache["Rennes-le-Château"]
print("chateau | km | cap | lieues: commune 4.444 / Paris 3.898 / leuga 2.222 / marine 5.556")
rows = []
for k in ["Château de Foix", "Château de Montségur"] + list(EXTRA):
    v = cache.get(k)
    if not v: print(k, "INTROUVABLE"); continue
    d = hav(R, v); rows.append((d, k, brg(R, v)))
for d, k, b in sorted(rows):
    print(f"{k:28s} {d:6.1f} km  cap {b:5.0f}  | {d/4.444:5.2f} / {d/3.898:5.2f} / {d/2.222:5.2f} / {d/5.556:5.2f}  <- {cache[k]['osm'][:60]}")
print("\nRappel : 'couchant' = ouest (cap ~270) ; 'pres de 11' = un peu moins de 11.")
