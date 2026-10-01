# -*- coding: utf-8 -*-
"""T16 — Pont des Bretonnières (piste Guilhem) : rang des ponts du Bréda depuis l'embouchure / la source,
distance 3e-11e, distances à la tour. Données OSM déjà téléchargées (ov_breda.json, ov_breda_cross.json)."""
import sys, json
sys.path.insert(0, r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12")
sys.stdout.reconfigure(encoding="utf-8")
from geo12 import *
from shapely.geometry import LineString, Point

PB = (45.439475, 6.053043)  # Pont des Bretonnières (Google Maps, lien de Guilhem)
W = json.load(open(S + "exk_e12/ov_breda.json", encoding="utf-8"))
X = json.load(open(S + "exk_e12/ov_breda_cross.json", encoding="utf-8"))
W = {w["id"]: w for w in W}
starts = {(round(w["geometry"][0]["lat"], 4), round(w["geometry"][0]["lon"], 4)): w
          for w in W.values() if w["tags"].get("waterway") in ("river", "stream")}
w = W[35777426]; chain = []; seen = set()
while w and w["id"] not in seen:
    seen.add(w["id"]); chain += [(p["lat"], p["lon"]) for p in w["geometry"]]
    w = starts.get((round(w["geometry"][-1]["lat"], 4), round(w["geometry"][-1]["lon"], 4)))
BL = LineString([xy(lo, la) for la, lo in chain])
print(f"Bréda reconstruit : {len(seen)} tronçons OSM, {BL.length/1000:.1f} km, de la source à l'Isère")

cr = []
for e in X:
    t = e.get("tags", {})
    if e["type"] == "node" or len(e.get("geometry", [])) < 2: continue
    g_ = LineString([xy(p["lon"], p["lat"]) for p in e["geometry"]])
    inter = g_.intersection(BL)
    if inter.is_empty: continue
    pts = [inter] if inter.geom_type == "Point" else [q for q in getattr(inter, 'geoms', []) if q.geom_type == "Point"]
    kind = t.get("highway") or t.get("railway") or t.get("waterway") or t.get("man_made")
    for q in pts:
        cr.append((BL.project(q), q, kind, t.get("name"), t.get("bridge"), t.get("bridge:material") or t.get("material"), e["id"]))
cr.sort(key=lambda c: c[0])
ded = []
for c in cr:
    if ded and c[0] - ded[-1][0] < 12: continue
    ded.append(c)

def show(seq, titre):
    print("\n==", titre)
    for k, c in enumerate(seq, 1):
        la, lo = inv(c[1].x, c[1].y)
        print(f"{k:2d} ({la:.5f},{lo:.5f}) {str(c[2]):11s} {str(c[3])[:32]:32s} bridge={c[4]} mat={c[5]} | tour {hav(TA,(la,lo)):5.0f} m | PB {hav(PB,(la,lo)):5.0f} m")
    return seq

for excl, lab in (((), "tous franchissements (barrages inclus)"), (("dam", "weir"), "sans barrages/seuils")):
    real = [c for c in ded if c[2] not in excl]
    for sens, seq in (("depuis l'EMBOUCHURE", real[::-1]), ("depuis la SOURCE", real)):
        s = show(seq[:14] if sens.startswith("depuis l'E") else seq, f"{lab} — {sens}")
        if len(seq) >= 11:
            a, b = seq[2], seq[10]
            la, lo = inv(a[1].x, a[1].y); lb, lob = inv(b[1].x, b[1].y)
            print(f"   >>> 3e-11e = {hav((la,lo),(lb,lob)):.0f} m  (cible 1850 ±18)")
EOF_MARK = None
