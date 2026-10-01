"""Enigme 1 - geometrie de l'epee : tracés, intersections, alignements.
Deux cadres de calcul, systematiquement :
  (G) globe  : orthodromie / grands cercles ;
  (M) carte  : droites de la carte Web Mercator (Google My Maps).
Points : hypotheses de Guilhem (carte_guilhem_objets.json) + coords.json + OSM.
"""
import json, math, os, sys
from importlib import import_module
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.stdout.reconfigure(encoding="utf-8")
G = import_module("00_geo")

CG = json.load(open(os.path.join(HERE, "..", "..", "Carte", "carte_guilhem_objets.json"), encoding="utf-8"))
CO = json.load(open(os.path.join(HERE, "..", "..", "02_Audit_calculs", "coords.json"), encoding="utf-8"))
OV = json.load(open(os.path.join(HERE, "overpass_chateaux_rlc.json"), encoding="utf-8"))

P = {}
for o in CG:
    if o["type"] == "Point":
        P[o["name"]] = (o["coords_lonlat"][0][1], o["coords_lonlat"][0][0])
P["Grotte de Lombrives"] = (CO["Grotte de Lombrives"]["lat"], CO["Grotte de Lombrives"]["lon"])
P["Rennes-le-Château"] = (CO["Rennes-le-Château"]["lat"], CO["Rennes-le-Château"]["lon"])
for k in ["Château de Montségur", "Château de Roquefixade", "Château de Lordat", "Château de Puivert",
          "Château de Montaillou", "Château de Montréal-de-Sos", "Château de Gudanes"]:
    if k in CO:
        P[k] = (CO[k]["lat"], CO[k]["lon"])

L = P["Cathédrale de León"]; F = P["Château de Foix"]; V = P["Cathédrale Sainte-Marie de Valence"]
U = P["Château d'Urquhart"]; LO = P["Grotte de Lombrives"]; RLC = P["Rennes-le-Château"]

def fmt(p):
    return f"{p[0]:8.4f}, {p[1]:8.4f}"

print("=" * 100)
print("POINTS (lat, lon)")
for k, v in P.items():
    print(f"  {k:34s} {fmt(v)}")
print("=" * 100)

print("\n### 1) Les 4 jambes de l'epee : longueurs et caps, globe vs carte Mercator")
jambes = [("Leon -> Foix        (garde, hyp. Guilhem)", L, F),
          ("Foix -> Valence     (??? )", F, V),
          ("Urquhart -> Valence (Ligne 5)", U, V),
          ("Urquhart -> Lombrives (lame)", U, LO),
          ("Valence -> Lombrives (poignee)", V, LO),
          ("Leon -> Usson/axe ?", L, LO)]
print(f"{'jambe':38s} {'km':>7s} {'cap':>6s} | {'km Merc':>8s} {'cap Merc':>8s} | {'km loxo':>8s}")
for n, a, b in jambes:
    print(f"{n:38s} {G.hav(a,b):7.1f} {G.bearing(a,b):6.1f} | {G.merc_dist_ground(a,b):8.1f} {G.merc_bearing(a,b):8.1f} | {G.rhumb_dist2(a,b):8.1f}")

print("\n### 2) Lombrives : sur l'axe de la lame ? (ecart perpendiculaire)")
for n, a, b in [("axe Urquhart->Valence (Ligne 5)", U, V),
                ("axe Urquhart->Lombrives->Valence (brise)", None, None)]:
    if a:
        print(f"  Lombrives / {n} : globe {G.cross_track(LO, a, b):8.1f} km | Mercator {G.merc_cross_track(LO, a, b):8.1f} km"
              f" | (pied du point a {G.along_track(LO, a, b):.0f} km de {fmt(a)})")
print(f"  Lombrives / axe Urquhart->RLC : globe {G.cross_track(LO, U, RLC):8.1f} km | Mercator {G.merc_cross_track(LO, U, RLC):8.1f} km")
print(f"  RLC / axe Urquhart->Valence   : globe {G.cross_track(RLC, U, V):8.1f} km | Mercator {G.merc_cross_track(RLC, U, V):8.1f} km")
print(f"  Leon / axe Urquhart->Valence  : globe {G.cross_track(L, U, V):8.1f} km | Mercator {G.merc_cross_track(L, U, V):8.1f} km")
print(f"  Foix / axe Urquhart->Valence  : globe {G.cross_track(F, U, V):8.1f} km | Mercator {G.merc_cross_track(F, U, V):8.1f} km")
print(f"  Valence->Lombrives  : cap globe {G.bearing(V,LO):5.1f}   cap Mercator {G.merc_bearing(V,LO):5.1f}")
print(f"  Lombrives->Urquhart : cap globe {G.bearing(LO,U):5.1f}   cap Mercator {G.merc_bearing(LO,U):5.1f}")
print(f"  => coude de la lame a Lombrives : {abs(((G.bearing(LO,U)-G.bearing(V,LO))+180)%360-180):.1f} degres")

print("\n### 3) Ou la GARDE (Leon -> quillon est) coupe-t-elle l'AXE Urquhart->Valence (Ligne 5) ?")
print("   (globe = intersection de grands cercles ; Mercator = intersection de droites de carte)")
cands = [("Château de Foix", F), ("Château de Montségur", P["Château de Montségur"]),
         ("Château de Roquefixade", P["Château de Roquefixade"]), ("Château de Lordat", P["Château de Lordat"]),
         ("Château de Puivert", P["Château de Puivert"]), ("Grotte de Lombrives", LO),
         ("Rennes-le-Château", RLC), ("Château de Montaillou", P["Château de Montaillou"]),
         ("Château de Montréal-de-Sos", P["Château de Montréal-de-Sos"])]
for el in OV["elements"]:
    t = el.get("tags", {}); h = el.get("center") or el
    if t.get("name") in ("Château de Gudanes", "Château de Miglos", "Château de Calamès", "Chapelle de Lujat"):
        cands.append((t["name"], (h["lat"], h["lon"])))
for n, q in cands:
    gl = G.gc_intersection(L, q, U, V)
    me = G.merc_line_inter(L, q, U, V)
    g1, g2 = gl
    near = g1 if G.hav(g1, (43.0, 0.0)) < G.hav(g2, (43.0, 0.0)) else g2
    print(f"  garde Leon->{n:26s} : globe {fmt(near)}  (dist. Valencia {G.hav(near,V):6.0f} km, dist. Lombrives {G.hav(near,LO):6.0f} km)"
          f" | Mercator {fmt(me)} (dist. Lombrives {G.hav(me,LO):6.0f} km)")

print("\n### 4) La garde passe-t-elle par le ROCHER (Lombrives) ? grandes cercles Leon->X")
print("   on teste tous les chateaux OSM : ecart du chateau a la droite Mercator Leon->Lombrives, et du grand cercle")
best = []
for el in OV["elements"]:
    t = el.get("tags", {})
    h = el.get("center") or el
    if "lat" not in h or not t.get("name"):
        continue
    p = (h["lat"], h["lon"])
    d_gl = G.cross_track(p, L, LO); d_me = G.merc_cross_track(p, L, LO)
    if abs(d_me) < 12:
        best.append((abs(d_me), t["name"], p, d_gl, d_me, G.along_track(p, L, LO), G.hav(RLC, p), G.bearing(RLC, p)))
print(f"   chateaux a moins de 12 km de la droite Mercator Leon->Lombrives :")
for a, n, p, dg, dm, at, d, b in sorted(best):
    print(f"     {n:36s} {fmt(p)} ecart Merc {dm:6.1f} (globe {dg:6.1f}) | sur la droite a {at:6.0f} km de Leon | {d:5.1f} km / cap {b:5.0f} de RLC")

print("\n### 5) Etendue EST de la ligne de garde : le grand cercle Leon->Lombrives prolonge vers l'est")
n = G.norm(G.cross(G.vec(*L), G.vec(*LO)))
for d in range(0, 90, 5):
    pt = G.dest(LO, G.bearing(L, LO) + 180, d)
    n1 = n if G.dot(G.vec(*pt), n) > 0 else tuple(-x for x in n)
    print(f"   +{d:3d} km a l'est de Lombrives : {fmt(pt)} | distance a RLC {G.hav(RLC, pt):6.1f} km = {G.hav(RLC, pt)/4.4448:5.2f} l.commune / {G.hav(RLC,pt)/3.898:5.2f} l.Paris")

print("\n### 6) Le POMMEAU/POIGNEE est-il dans l'axe de la lame ?")
print(f"   Valence hors axe Urquhart->Lombrives : globe {G.cross_track(V, U, LO):8.1f} km | Mercator {G.merc_cross_track(V, U, LO):8.1f} km")
print(f"   (donc oui/non : un ecart faible signifie poignee alignee sur la lame)")

print("\n### 7) Vertex (latitude extreme) de la lame Urquhart->Lombrives et de l'axe Urquhart->Valence")
for n, a, b in [("Urquhart->Lombrives", U, LO), ("Urquhart->Valence", U, V)]:
    v = G.vertex_gc(a, b)
    print(f"   {n:22s} vertex globe : {fmt(v)} | lon de l'extremum de longitude Mercator : "
          f"x={'?'}")

print("\n### 8) Bearing de la lame Urquhart->Lombrives par tranche de latitude (globe vs Mercator)")
for lat in [42.9, 44, 46, 48, 50, 52, 54, 56, 57.3]:
    # point du grand cercle a cette latitude
    f = None
    lo_, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo_ + hi) / 2
        if G.interp_gc(U, LO, mid)[0] < lat:
            lo_ = mid
        else:
            hi = mid
    pg = G.interp_gc(U, LO, mid)
    # droite Mercator a cette latitude
    (x1, y1), (x2, y2) = G.m(*U), G.m(*LO)
    yt = G.m(lat, 0)[1]
    fr = (y1 - yt) / (y1 - y2)
    pm = G.mi(x1 + fr * (x2 - x1), yt)
    print(f"   lat {lat:5.1f} : grand cercle lon {pg[1]:7.2f} | droite Mercator lon {pm[1]:7.2f} | ecart {G.hav((lat,pg[1]),(lat,pm[1])):6.0f} km")
