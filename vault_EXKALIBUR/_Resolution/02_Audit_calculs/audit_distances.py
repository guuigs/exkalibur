"""Audit Phase 0 : controles de distance sur les pistes existantes de Guilhem.
Methode : orthodromie (haversine, R = 6371.0088 km, rayon moyen IUGG).
Coordonnees : OpenStreetMap Nominatim (requete ci-dessous), mises en cache dans coords.json.
Ce script NE resout rien : il teste la coherence chiffree des pistes deja notees.
"""
import json, math, os, sys, time, urllib.parse, urllib.request

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "coords.json")

PLACES = {
    "Rennes-le-Château": "Rennes-le-Château, Aude, France",
    "Château de Foix": "Château de Foix, Foix, France",
    "Château de Montségur": "Château de Montségur, Montségur, France",
    "Cathédrale de León": "Catedral de León, León, España",
    "Cathédrale de Valence": "Catedral de Valencia, Valencia, España",
    "Grotte de Lombrives": "Grotte de Lombrives, Ussat, France",
    "Château d'Urquhart": "Urquhart Castle, Highland",
    "Château de Tintagel": "Tintagel Castle, Cornwall, England",
    "Silchester (Calleva)": "Silchester Roman Town, Hampshire, England",
    "Abbaye de Westminster": "Westminster Abbey, London, England",
    "Tour de Londres": "Tower of London, London, England",
    "Battle Abbey (Hastings)": "Battle Abbey, Battle, East Sussex, England",
}

def geocode(q):
    url = "https://nominatim.openstreetmap.org/search?format=json&limit=1&q=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={"User-Agent": "exkalibur-audit/1.0 (personal research)"})
    r = json.loads(urllib.request.urlopen(req, timeout=30).read())
    if not r:
        return None
    return {"lat": float(r[0]["lat"]), "lon": float(r[0]["lon"]), "osm": r[0].get("display_name", "")}

cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
for name, q in PLACES.items():
    if name not in cache:
        cache[name] = geocode(q)
        time.sleep(1.1)  # politique d'usage Nominatim
json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def hav(a, b):
    R = 6371.0088
    p1, p2 = math.radians(a["lat"]), math.radians(b["lat"])
    dp, dl = p2 - p1, math.radians(b["lon"] - a["lon"])
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))

def bearing(a, b):
    p1, p2 = math.radians(a["lat"]), math.radians(b["lat"])
    dl = math.radians(b["lon"] - a["lon"])
    x = math.sin(dl) * math.cos(p2)
    y = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    return (math.degrees(math.atan2(x, y)) + 360) % 360

print("## Coordonnees (OSM Nominatim)")
for k, v in cache.items():
    print(f"- {k}: {v['lat']:.5f}, {v['lon']:.5f}  <- {v['osm'][:90]}" if v else f"- {k}: INTROUVABLE")

C = cache
# Unites (valeurs de reference usuelles, a confirmer selon l'intention du concepteur)
LIEUES = {"lieue commune (~4.444 km)": 4.444, "lieue de Paris 1674 (3.898 km)": 3.898,
          "lieue de poste (3.898 km)": 3.898, "lieue gauloise/leuga (~2.22 km)": 2.222,
          "lieue marine (5.556 km)": 5.556}
MILLE_ROMAIN = 1.4786  # km (mille pas romains, valeur la plus citee ; fourchette 1.47-1.48)

print("\n## Enigme 1 - '11 lieues vers le couchant depuis Rennes-le-Chateau'")
for cand in ["Château de Foix", "Château de Montségur"]:
    d = hav(C["Rennes-le-Château"], C[cand]); brg = bearing(C["Rennes-le-Château"], C[cand])
    print(f"- RLC -> {cand}: {d:.1f} km, cap {brg:.0f}deg")
    for u, km in LIEUES.items():
        print(f"    = {d/km:.2f} x {u}")

print("\n## Enigme 1 - geometrie de l'epee")
for a, b in [("Cathédrale de León", "Château de Foix"), ("Cathédrale de León", "Château de Montségur"),
             ("Grotte de Lombrives", "Château d'Urquhart"), ("Cathédrale de Valence", "Grotte de Lombrives"),
             ("Cathédrale de Valence", "Château d'Urquhart")]:
    print(f"- {a} -> {b}: {hav(C[a], C[b]):.1f} km, cap {bearing(C[a], C[b]):.1f}deg")

print("\n## Enigme 4 - '181 milia vers l'orient'")
print(f"- 181 milles romains x {MILLE_ROMAIN} = {181*MILLE_ROMAIN:.1f} km")
for a, b in [("Château de Tintagel", "Silchester (Calleva)"), ("Silchester (Calleva)", "Abbaye de Westminster"),
             ("Château de Tintagel", "Abbaye de Westminster")]:
    d = hav(C[a], C[b])
    print(f"- {a} -> {b}: {d:.1f} km = {d/MILLE_ROMAIN:.1f} milles romains, cap {bearing(C[a], C[b]):.0f}deg")

print("\n## Enigme 6 - Tour de Londres -> champ de bataille")
d = hav(C["Tour de Londres"], C["Battle Abbey (Hastings)"])
print(f"- Tour de Londres -> Battle Abbey: {d:.1f} km, cap {bearing(C['Tour de Londres'], C['Battle Abbey (Hastings)']):.0f}deg")
