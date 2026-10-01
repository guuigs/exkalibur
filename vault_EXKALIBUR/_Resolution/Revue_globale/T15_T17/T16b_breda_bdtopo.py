# -*- coding: utf-8 -*-
"""T16b — Contrôle indépendant BD TOPO : rang du Pont des Bretonnières parmi les franchissements du Bréda
depuis l'embouchure (Isère). Source : ign/troncon_hydrographique.geojson (cours d'eau 'le Bréda'),
ign/construction_lineaire_12km.geojson (nature Pont), ign/troncon_de_route.geojson (position_par_rapport_au_sol=1)."""
import sys
sys.path.insert(0, r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12")
sys.stdout.reconfigure(encoding="utf-8")
from geo12 import *
from shapely.geometry import Point, LineString
from shapely.ops import linemerge, unary_union

PB = (45.439475, 6.053043)
hyd = load("troncon_hydrographique_12km.geojson")
br = [g for g, p in hyd if (p.get("cpx_toponyme_de_cours_d_eau") or "").lower() == "le bréda"]
u = unary_union(br); m = linemerge(u)
parts = [m] if m.geom_type == "LineString" else sorted(m.geoms, key=lambda x: -x.length)
print("tronçons BD TOPO 'le Bréda':", len(br), "composantes:", [round(p.length) for p in parts[:6]])
L = parts[0]
a = inv(*L.coords[0]); b = inv(*L.coords[-1])
print("extrémités", [round(v, 4) for v in a], alt(*a), [round(v, 4) for v in b], alt(*b))
# orienter : début = embouchure (plus bas / plus à l'ouest près de l'Isère ~ 45.4414, 6.0046)
if hav(a, (45.4414, 6.0046)) > hav(b, (45.4414, 6.0046)):
    L = LineString(list(L.coords)[::-1])
print("longueur", round(L.length), "m ; départ (embouchure) =", [round(v, 5) for v in inv(*L.coords[0])])

cl = load("construction_lineaire_12km.geojson")
rou = load("troncon_de_route.geojson")
items = []
for g, p in cl:
    if p.get("nature") in ("Pont", "Barrage", "Gué ou radier", "Passerelle") and g.distance(L) < 15:
        c = g.centroid; items.append((L.project(c), c, "BDTOPO:" + str(p.get("nature")), p.get("nature_detaillee"), p.get("toponyme")))
for g, p in rou:
    if str(p.get("position_par_rapport_au_sol")) == "1" and g.distance(L) < 5:
        inter = g.intersection(L.buffer(5)).centroid
        items.append((L.project(inter), inter, "route_sur_pont:" + str(p.get("nature")), p.get("nom_collaboratif_gauche"), None))
items.sort(key=lambda t: t[0])
ded = []
for it in items:
    if ded and it[0] - ded[-1][0] < 20:
        ded[-1][5].append(it[2]); continue
    ded.append([it[0], it[1], it[2], it[3], it[4], [it[2]]])
k = 0
for d in ded:
    la, lo = inv(d[1].x, d[1].y)
    is_dam = all("Barrage" in s for s in d[5])
    if not is_dam: k += 1
    if hav(TA, (la, lo)) < 7000:
        print(f"{'  -' if is_dam else f'{k:3d}'} s={d[0]:6.0f} ({la:.5f},{lo:.5f}) {d[5]} {d[3]} {d[4]} | tour {hav(TA,(la,lo)):5.0f} | PB {hav(PB,(la,lo)):5.0f}")
