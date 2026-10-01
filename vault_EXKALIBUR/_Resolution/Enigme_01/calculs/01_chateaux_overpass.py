"""Inventaire OSM (Overpass) des chateaux dans un rayon de 60 km autour de Rennes-le-Chateau.
Sortie: distance orthodromique, cap, et conversion en plusieurs lieues.
Coordonnees RLC: coords.json (OSM Nominatim).
"""
import json, math, os, sys, urllib.request, urllib.parse
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
COORDS = os.path.join(HERE, "..", "..", "02_Audit_calculs", "coords.json")
C = json.load(open(COORDS, encoding="utf-8"))
R = C["Rennes-le-Château"]; LA, LO = math.radians(R["lat"]), math.radians(R["lon"])
R_earth = 6371.0088

Q = f"""[out:json][timeout:90];
(
  node["historic"="castle"](around:70000,{R['lat']},{R['lon']});
  way["historic"="castle"](around:70000,{R['lat']},{R['lon']});
  relation["historic"="castle"](around:70000,{R['lat']},{R['lon']});
  node["historic"="fort"](around:70000,{R['lat']},{R['lon']});
  way["historic"="fort"](around:70000,{R['lat']},{R['lon']});
  node["ruins"="yes"]["historic"](around:70000,{R['lat']},{R['lon']});
  way["ruins"="yes"]["historic"](around:70000,{R['lat']},{R['lon']});
);
out center tags;"""

data = urllib.parse.urlencode({"data": Q}).encode()
req = urllib.request.Request("https://overpass-api.de/api/interpreter", data=data,
                            headers={"User-Agent": "exkalibur-audit/1.0 (research)"})
raw = json.loads(urllib.request.urlopen(req, timeout=180).read().decode())
json.dump(raw, open(os.path.join(HERE, "overpass_chateaux_rlc.json"), "w", encoding="utf-8"), ensure_ascii=False)

def hav(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dp, dl = p2 - p1, math.radians(b[1] - a[1])
    return 2 * R_earth * math.asin(math.sqrt(math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2))
def brg(a, b):
    p1, p2 = math.radians(a[0]), math.radians(b[0]); dl = math.radians(b[1] - a[1])
    return (math.degrees(math.atan2(math.sin(dl)*math.cos(p2), math.cos(p1)*math.sin(p2)-math.sin(p1)*math.cos(p2)*math.cos(dl))) + 360) % 360

UNITS = {"commune4.444": 4.444, "Paris3.898": 3.898, "gaul2.222": 2.2222, "marine5.556": 5.5556,
         "metr4.0": 4.0, "km5.0": 5.0, "naive_deg1/25": 111.320/25}
rows = []
for el in raw["elements"]:
    t = el.get("tags", {})
    h = el.get("center") or el
    if "lat" not in h or "lon" not in h:
        continue
    pt = (h["lat"], h["lon"])
    d, b = hav((R["lat"], R["lon"]), pt), brg((R["lat"], R["lon"]), pt)
    if d < 0.3:
        continue
    rows.append((d, b, t.get("name", "?"), t.get("historic", ""), t.get("ruins", ""), t.get("castle_type", ""), t.get("tourism", ""), pt))
rows.sort()
print(f"RLC {R['lat']:.4f},{R['lon']:.4f}  — {len(rows)} objets OSM (historic=castle/fort, ruines)")
print("\n### Objets entre 6 et 16 lieues communes (27-71 km) — les candidats pour 'pres de 11 lieues'")
hdr = "  km   cap  | " + " | ".join(f"{k:>13s}" for k in UNITS)
for d, b, n, h1, ru, ct, to, pt in rows:
    if 25 < d < 75:
        lieues = " | ".join(f"{d/v:13.2f}" for v in UNITS.values())
        print(f"{d:6.1f} {b:5.0f}  | {lieues}  <- {n}  [{h1}/{ru}/{ct}/{to}] {pt}")
print("\n### Bande 'couchant' stricte : cap entre 255 et 285 degres, 20-70 km")
for d, b, n, h1, ru, ct, to, pt in rows:
    if 255 <= b <= 285 and 20 < d < 70:
        print(f"{d:6.1f} {b:5.0f}  | commune {d/4.444:5.2f} | Paris {d/3.898:5.2f} | 4km {d/4:5.2f} | 5km {d/5:5.2f} | 1/25deg {d/(111.320/25):5.2f}  <- {n} {pt}")
