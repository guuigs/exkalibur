# -*- coding: utf-8 -*-
"""T12C_03 : (a) recherche Overpass remparts/tours/forts <=8 km (D5) ; (b) grande roche :
toponymes roche/rocher/pierre + points orographiques 'Rochers' près de la zone et du vallon de Tapon."""
import json, math, urllib.request, urllib.parse

S = r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/"
R = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/"
I = S + "ign/"
TOWER = (45.429083, 6.030808)
COS = math.cos(math.radians(45.429))

def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*6371.0088*math.asin(math.sqrt(h)) * 1000

# ---- (a) Overpass : remparts / tours / forts dans 8 km ----
q = """
[out:json][timeout:90];
(
  node["historic"~"fort|citywalls|city_gate|castle|tower|ruins|walls"](around:8000,45.429083,6.030808);
  way["historic"~"fort|citywalls|city_gate|castle|tower|ruins|walls"](around:8000,45.429083,6.030808);
  node["man_made"~"tower|fort|defensive_works"](around:8000,45.429083,6.030808);
  way["man_made"~"tower|fort"](around:8000,45.429083,6.030808);
  node["military"](around:8000,45.429083,6.030808);
  way["military"](around:8000,45.429083,6.030808);
  way["barrier"~"wall|city_wall"](around:8000,45.429083,6.030808);
  node["building"~"tower|fort"](around:8000,45.429083,6.030808);
);
out center tags 200;
"""
data = urllib.parse.urlencode({"data": q}).encode()
req = urllib.request.Request("https://overpass.openstreetmap.fr/api/interpreter", data=data,
                             headers={"User-Agent": "Mozilla/5.0 (research script)"})
try:
    j = json.loads(urllib.request.urlopen(req, timeout=120).read().decode("utf-8"))
    els = j.get("elements", [])
    print("=== Overpass : remparts/tours/forts <=8 km : %d éléments ===" % len(els))
    for e in els:
        lat = e.get("lat", e.get("center", {}).get("lat"))
        lon = e.get("lon", e.get("center", {}).get("lon"))
        tags = e.get("tags", {})
        nm = tags.get("name") or tags.get("historic") or tags.get("man_made") or tags.get("military") or tags.get("barrier") or e.get("type")
        if lat is None:
            continue
        d = hav(TOWER, (lat, lon))
        print("  %-6s %-30s (%.5f, %.5f) d=%.0f m  tags=%s" % (e["type"], nm[:30], lat, lon, d, {k: tags[k] for k in ("historic", "man_made", "military", "barrier", "building", "name") if k in tags}))
except Exception as ex:
    print("Overpass ERREUR :", ex)

# ---- (b) grande roche : toponymes + orographie près de la zone ----
print("\n=== Toponymes 'roche/rocher/pierre' dans 4 km de la tour ===")
topo = json.load(open(I + "toponymie_12km.geojson", encoding="utf-8"))["features"]
for f in topo:
    p = f["properties"]
    nom = (p.get("graphie_du_toponyme") or "").lower()
    if any(k in nom for k in ("roche", "rocher", "pierre", "rock")):
        g = f["geometry"]
        if g and g.get("coordinates"):
            c = g["coordinates"]; lat, lon = c[1], c[0]
            d = hav(TOWER, (lat, lon))
            if d <= 4000:
                print("  %-28s (%.5f,%.5f) d=%.0f m  nature=%s" % (nom[:28], lat, lon, d, p.get("nature_de_l_objet")))

print("\n=== Points orographiques 'Rochers' (detail_orographique) dans 4 km ===")
oro = json.load(open(I + "detail_orographique_12km.geojson", encoding="utf-8"))["features"]
for f in oro:
    p = f["properties"]
    if p.get("nature") in ("Rochers", "Escarpement", "Grotte", "Gorge"):
        g = f["geometry"]
        if g and g.get("coordinates"):
            c = g["coordinates"]; lat, lon = c[1], c[0]
            d = hav(TOWER, (lat, lon))
            if d <= 4000:
                print("  %-28s (%.5f,%.5f) d=%.0f m  nature=%s" % ((p.get("toponyme") or "")[:28], lat, lon, d, p.get("nature")))

print("\n=== Lieux-dits non habités 'roche/pierre' dans 4 km ===")
ld = json.load(open(I + "lieu_dit_non_habite_12km.geojson", encoding="utf-8"))["features"]
for f in ld:
    p = f["properties"]
    nom = (p.get("toponyme") or "").lower()
    if any(k in nom for k in ("roche", "rocher", "pierre", "rochettes")):
        g = f["geometry"]
        if g and g.get("coordinates"):
            c = g["coordinates"]; lat, lon = c[1], c[0]
            d = hav(TOWER, (lat, lon))
            if d <= 4000:
                print("  %-28s (%.5f,%.5f) d=%.0f m" % (nom[:28], lat, lon, d))
