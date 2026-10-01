# -*- coding: utf-8 -*-
"""T12E_02 : liste exhaustive (OSM/Overpass) des remparts/ronde/enceinte/muraille/tour/fort/château
dans le couloir (bbox 45.10-45.75 N, 5.75-6.27 E), + distance/cap/offset depuis Saint-Palais."""
import math, json, urllib.request, urllib.parse, time

R = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/"
SP = (43.3291, -1.0347)
P11 = (45.42418, 6.01790)

def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*6371.0088*math.asin(math.sqrt(h))
def brg(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    y = math.sin(lo2-lo1)*math.cos(la2)
    x = math.cos(la1)*math.sin(la2) - math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return (math.degrees(math.atan2(y, x)) + 360) % 360

BBOX = "45.10,5.75,45.75,6.27"   # sud, ouest, nord, est
QUERY = f"""[out:json][timeout:240];
(
  way["highway"]["name"~"rempart|ronde|enceinte|muraille",i]({BBOX});
  way["historic"="citywalls"]({BBOX});
  way["historic"~"fort|castle",i]({BBOX});
  way["man_made"="tower"]({BBOX});
  node["historic"~"fort|castle",i]({BBOX});
  node["man_made"="tower"]({BBOX});
  relation["historic"~"fort|castle|citywalls",i]({BBOX});
);
out center tags qt;"""

def post(url, q, tries=3):
    data = urllib.parse.urlencode({"data": q}).encode()
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data,
                headers={"User-Agent": "Mozilla/5.0 (research script)", "Content-Type": "application/x-www-form-urlencoded"})
            return urllib.request.urlopen(req, timeout=180).read().decode("utf-8", "replace")
        except Exception as e:
            print("  [%s] tentative %d échouée: %s" % (url, i+1, e))
            time.sleep(3)
    return None

mirrors = [
    "https://overpass.openstreetmap.fr/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass-api.de/api/interpreter",
]
raw = None
for m in mirrors:
    print(">>> Overpass :", m)
    raw = post(m, QUERY)
    if raw:
        break
if not raw:
    print("!!! Overpass inaccessible sur tous les miroirs")
    raise SystemExit(1)

j = json.loads(raw)
els = j.get("elements", [])
print("Éléments Overpass :", len(els))

rows = []
for e in els:
    t = e.get("type")
    lat = e.get("lat"); lon = e.get("lon")
    if lat is None and "center" in e:
        lat = e["center"]["lat"]; lon = e["center"]["lon"]
    if lat is None:
        continue
    tags = e.get("tags", {})
    name = tags.get("name") or ""
    rows.append(dict(lat=lat, lon=lon, name=name, tags=tags, typ=t, id=e.get("id")))

# trier par offset à l'arrivée É11
for r in rows:
    r["D"] = hav(SP, (r["lat"], r["lon"]))
    r["cap"] = brg(SP, (r["lat"], r["lon"]))
    r["off"] = hav((r["lat"], r["lon"]), P11)
rows.sort(key=lambda r: r["off"])

print("\n=== Résultats triés par offset à l'arrivée É11 (%.5f, %.5f) ===" % P11)
print("%-42s | %7s | %6s | %7s | %s" % ("nom", "D km", "cap°", "off km", "tags-clés"))
for r in rows:
    kt = ",".join(k for k in ("historic", "man_made", "highway", "barrier", "castle_type", "tourism", "wikipedia") if k in r["tags"])
    print("%-42s | %7.1f | %6.2f | %7.2f | %s" % ((r["name"] or r["typ"])[:42], r["D"], r["cap"], r["off"], kt[:60]))

json.dump(rows, open(R + "T12E_02_overpass.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\n[SAVE] T12E_02_overpass.json (%d éléments)" % len(rows))
