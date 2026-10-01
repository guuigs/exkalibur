# -*- coding: utf-8 -*-
"""T17 — Piste Guilhem : le 11e = un pont du Bréda (Pont des Bretonnières, ou pont du barrage),
le 3e = autre élément plus proche d'Avalon. On cherche ce qui est à 1 850 m ±18 m (±1 %) de chaque candidat 11e,
d'abord près d'Avalon (≤ 800 m de la tour), en toutes classes BD TOPO + OSM, puis avec un contrôle :
combien d'objets de la même classe on attendrait dans l'anneau par hasard (densité locale)."""
import sys, json, math, urllib.request, urllib.parse
sys.path.insert(0, r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12")
sys.stdout.reconfigure(encoding="utf-8")
from geo12 import *

C11 = {
    "Pont des Bretonnières (Google)": (45.439475, 6.053043),
    "Pont des Bretonnières (BD TOPO)": (45.43950, 6.05300),
    "Pont isolé du barrage (BD TOPO)": (45.43566, 6.03903),
    "Barrage (BD TOPO)": (45.43583, 6.03972),
}
TOL = 18.5
NEAR = 800  # m de la tour

# --- objets ponctuels de toutes classes ---
objs = []
for fn in ["construction_ponctuelle_12km.geojson", "construction_lineaire_12km.geojson", "construction_surfacique_12km.geojson",
           "detail_hydrographique_12km.geojson", "detail_orographique_12km.geojson", "lieu_dit_non_habite_12km.geojson",
           "zone_d_activite_ou_d_interet_12km.geojson", "plan_d_eau_12km.geojson"]:
    for g, p in load(fn):
        c = g.centroid; la, lo = inv(c.x, c.y)
        objs.append(("IGN:" + fn.split("_12km")[0], p.get("nature"), p.get("nature_detaillee"), p.get("toponyme"), (la, lo)))
# OSM : petits points d'intérêt autour de la tour (rayon 1,2 km)
q = """[out:json][timeout:60];
(node(around:1200,45.429083,6.030808)[~"^(historic|man_made|natural|amenity|tourism|leisure|waterway|bridge|ford|barrier)$"~"."];
 way(around:1200,45.429083,6.030808)[~"^(historic|man_made|natural|tourism|leisure|bridge)$"~"."];);
out center tags;"""
try:
    r = json.loads(urllib.request.urlopen(urllib.request.Request("https://overpass.openstreetmap.fr/api/interpreter",
        data=urllib.parse.urlencode({"data": q}).encode(), headers={"User-Agent": "curl/8.4.0"}), timeout=90).read())
    for e in r["elements"]:
        t = e.get("tags", {}); la = e.get("lat") or e.get("center", {}).get("lat"); lo = e.get("lon") or e.get("center", {}).get("lon")
        if la is None: continue
        kind = next((k + "=" + t[k] for k in ("historic", "man_made", "natural", "amenity", "tourism", "leisure", "waterway", "bridge", "ford", "barrier") if k in t), "?")
        objs.append(("OSM", kind, None, t.get("name"), (la, lo)))
    print("OSM objets ≤1,2 km :", len(r["elements"]))
except Exception as ex:
    print("OSM indisponible :", ex)

for nom, p11 in C11.items():
    print(f"\n=== 11e = {nom} {p11} | tour→11e {hav(TA,p11):.0f} m, rempart→11e {hav(RP,p11):.0f} m")
    hits = [o for o in objs if abs(hav(p11, o[4]) - 1850) <= TOL]
    near = [o for o in hits if hav(TA, o[4]) <= NEAR]
    for o in sorted(near, key=lambda o: hav(TA, o[4])):
        print(f"   PRÈS AVALON  {hav(p11,o[4]):6.0f} m | tour {hav(TA,o[4]):4.0f} m | {o[0]} | {o[1]} | {o[2]} | {o[3]} | {o[4][0]:.5f},{o[4][1]:.5f}")
    print(f"   (tous objets dans l'anneau : {len(hits)} ; dont près d'Avalon : {len(near)})")
    # contrôle : densité d'objets à ≤ NEAR de la tour, fraction de la surface du disque couverte par l'anneau
    disk = [o for o in objs if hav(TA, o[4]) <= NEAR]
    # surface de l'intersection anneau ∩ disque, Monte-Carlo
    import random; random.seed(1); inside = 0; N = 40000
    for _ in range(N):
        rr = NEAR * math.sqrt(random.random()); th = random.random() * 2 * math.pi
        pt = dest(TA, math.degrees(th), rr)
        if abs(hav(p11, pt) - 1850) <= TOL: inside += 1
    frac = inside / N
    print(f"   contrôle : {len(disk)} objets à ≤{NEAR} m de la tour × fraction {frac:.3%} = {len(disk)*frac:.1f} attendus par hasard")
