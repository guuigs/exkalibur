# -*- coding: utf-8 -*-
"""T12E_03 : test de cohérence É12 pour le candidat n°1 (Rue du Rempart / Tour d'Avalon, Saint-Maximin).
Réutilise les croisements T12C_02 (vis_D2_pied ≈ pied de la tour = niveau de la Rue du Rempart).
Cherche : croisement de sentiers visible à l'œil nu, proche, en trouée, avec ruisseau éclairé le matin."""
import json, math

R = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/"
rows = json.load(open(R + "T12C_02_croisements.json", encoding="utf-8"))

# --- départ : Rue du Rempart (≈ pied tour D2) ---
REMPART = (45.4295, 6.0312)
TOUR = (45.429083, 6.030808)

def d(lat, lon, ref=REMPART):
    return math.hypot((lat - ref[0]) * 111132.0, (lon - ref[1]) * 111132.0 * math.cos(math.radians(ref[0])))

# croisements visibles du pied de la tour (proxy Rue du Rempart)
vis = [r for r in rows if r["vis_D2_pied"]]
print("Croisements visibles depuis le rempart (D2 pied) : %d / %d" % (len(vis), len(rows)))

# filtres : proche (<=2 km), près d'un cours d'eau (<=150 m), en trouée, loin des bâtiments (>=150 m)
sub = [r for r in vis if r["d_water"] <= 150 and r["clearing"] and r["d_bldg"] >= 150 and d(r["lat"], r["lon"]) <= 2000]
print("  dont : d_eau<=150 & clairière & d_bat>=150 & <=2km : %d" % len(sub))
sub.sort(key=lambda r: r["d_water"])
print("%-26s | %6s | %6s | %6s | %6s | %s" % ("lbl", "d_dep", "d_eau", "d_bat", "brg°", "soleil64/75"))
for r in sub:
    print("%-26s | %6.0f | %6.0f | %6.0f | %6.1f | %d / %d" %
          (r["lbl"][:26], d(r["lat"], r["lon"]), r["d_water"], r["d_bldg"], r["brg_D2_pied"],
           r["sun64_D2_pied"], r["sun75_D2_pied"]))

# élargir : croisements visibles proches d'eau (<=150m) sans filtre clairière/bâti, <=2km
sub2 = [r for r in vis if r["d_water"] <= 150 and d(r["lat"], r["lon"]) <= 2000]
sub2.sort(key=lambda r: r["d_water"])
print("\nCroisements visibles, d_eau<=150, <=2km (sans filtre clairière/bâti) : %d" % len(sub2))
for r in sub2:
    print("%-26s | %6.0f | %6.0f | %6.0f | clr=%d | brg=%5.1f | soleil64=%d" %
          (r["lbl"][:26], d(r["lat"], r["lon"]), r["d_water"], r["d_bldg"], r["clearing"], r["brg_D2_pied"], r["sun64_D2_pied"]))

# témoins aléatoires : combien de croisements visibles+d_eau<=150 pour des départs témoins ?
import random
random.seed(12)
TOURc = (45.429083, 6.030808)
w = []
for _ in range(10):
    ang = random.uniform(0, 360); dd = random.uniform(0.3, 1.5)
    lat = TOURc[0] + dd * 1000 * math.sin(math.radians(ang)) / 111132.0
    lon = TOURc[1] + dd * 1000 * math.cos(math.radians(ang)) / (111132.0 * math.cos(math.radians(TOURc[0])))
    k = sum(1 for r in rows if r["d_water"] <= 150 and d(r["lat"], r["lon"], (lat, lon)) <= 2000 and r["clearing"])
    w.append(k)
print("\nTémoins (croisements d_eau<=150 & clairière & <=2km d'un départ aléatoire) : min=%d moy=%.1f max=%d" % (min(w), sum(w)/len(w), max(w)))
