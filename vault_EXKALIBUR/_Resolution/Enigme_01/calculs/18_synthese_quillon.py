"""Enigme 1 - synthese du quillon est : tableau de decision.
Pour chaque candidat 'chateau de la bande couchant' : les 6 lectures possibles de
'pres de 11 lieues vers le Couchant depuis Rennes-le-Chateau', plus les 3 criteres
semantiques du texte. On cherche le candidat qui satisfait le plus de criteres
SANS forcer l'unite de mesure.
"""
import json, math, os, sys
from importlib import import_module
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.stdout.reconfigure(encoding="utf-8")
G = import_module("00_geo")
CO = json.load(open(os.path.join(HERE, "..", "..", "02_Audit_calculs", "coords.json"), encoding="utf-8"))
RLC = (CO["Rennes-le-Château"]["lat"], CO["Rennes-le-Château"]["lon"])
LEON = (CO["Cathédrale de León"]["lat"], CO["Cathédrale de León"]["lon"])
LO = (CO["Grotte de Lombrives"]["lat"], CO["Grotte de Lombrives"]["lon"])
U = (57.3241399, -4.4420013)

# candidats : nom, (lat,lon), 'brule' = pertinence du critere 'ou brule la memoire du pays cathare' (0-3),
# 'auteur' = source du jugement
CAND = [
 ("Château de Montségur",          (CO["Château de Montségur"]["lat"], CO["Château de Montségur"]["lon"]), 3, "bucher du 16 mars 1244, ~220 parfaits brules (source: fr.wikipedia Montségur / Château de Montségur)"),
 ("Château de Roquefixade",        (CO["Château de Roquefixade"]["lat"], CO["Château de Roquefixade"]["lon"]), 1, "chateau cathare assiege en 1242, 'sentinelle de Montségur' ; aucun bucher (fr.wikipedia: rien sur le feu)"),
 ("Château de Foix",               (CO["Château de Foix"]["lat"], CO["Château de Foix"]["lon"]), 1, "siege des comtes de Foix, protecteurs des cathares ; aucun bucher (fr.wikipedia Foix/Château de Foix)"),
 ("Château de Puivert",            (CO["Château de Puivert"]["lat"], CO["Château de Puivert"]["lon"]), 1, "chateau cathare ; musee du Quercorb ; pas de bucher"),
 ("Château de Lordat",             (CO["Château de Lordat"]["lat"], CO["Château de Lordat"]["lon"]), 1, "chateau cathare (siege 1243) ; pas de bucher"),
 ("Château de Montréal-de-Sos",    (CO["Château de Montréal-de-Sos"]["lat"], CO["Château de Montréal-de-Sos"]["lon"]), 1, "chateau cathare majeur (Auzat) ; pas de bucher"),
 ("Château de Montaillou",         (CO["Château de Montaillou"]["lat"], CO["Château de Montaillou"]["lon"]), 1, "village cathare (Inquisition, Fournier) ; pas de bucher"),
]
OV = json.load(open(os.path.join(HERE, "overpass_chateaux_rlc.json"), encoding="utf-8"))
for el in OV["elements"]:
    t = el.get("tags", {}); h = el.get("center") or el
    if t.get("name") in ("Château de Gudanes", "Chapelle de Lujat", "Castella", "Château de Miglos", "Château de Calamès"):
        CAND.append((t["name"], (h["lat"], h["lon"]), 0, "chateau/prieure de la vallee de l'Ariege ; aucun lien cathare documente"))

UNITS = [("l.commune 4,4448", 4.4448), ("l.Paris 3,898", 3.898), ("l.metrique 4,000", 4.0),
         ("l.Artois 3,975", 3.975), ("l.Gascogne 5,847", 5.847), ("l.marine 5,556", 5.556),
         ("1/25 degre (lieues de 25 au degre)", 111.320 / 25)]

print("=" * 130)
print("SYNTHESE QUILLON EST — 'pres de 11 lieues vers le Couchant depuis Rennes-le-Chateau,'")
print("'dans ce chateau ou brule la memoire du pays cathare'")
print("=" * 130)
print(f"\n{'candidat':30s} {'km':>6s} {'cap':>4s} | " + " ".join(f"{u[0][:19]:>20s}" for u in UNITS) + " | dlon_l. naive_l.")
rows = []
for n, p, feu, src in CAND:
    d = G.hav(RLC, p); b = G.bearing(RLC, p)
    if not (235 <= b <= 305) or d > 70:
        continue
    units = [d / v for _, v in UNITS]
    dl = abs(p[1] - RLC[1]) * 25
    nv = math.hypot(p[0] - RLC[0], p[1] - RLC[1]) * 25
    rows.append((n, p, d, b, units, dl, nv, feu, src))
for n, p, d, b, units, dl, nv, feu, src in sorted(rows, key=lambda r: abs(r[4][0] - 11)):
    cells = " ".join(f"{u:20.2f}" for u in units)
    print(f"{n[:29]:30s} {d:6.1f} {b:4.0f} | {cells} | {dl:8.2f} {nv:8.2f}   [feu {feu}/3]")

print("\nQui donne 11 a moins de 4 % ? (|lieues-11|/11 <= 0.04)")
for n, p, d, b, units, dl, nv, feu, src in sorted(rows, key=lambda r: abs(r[4][0] - 11)):
    hits = [UNITS[i][0] for i in range(len(UNITS)) if abs(units[i] - 11) / 11 <= 0.04]
    if abs(dl - 11) / 11 <= 0.04: hits.append("1/25 degre en LONGITUDE (11/25 = 0,44 deg de lon)")
    if abs(nv - 11) / 11 <= 0.04: hits.append("distance en degres sur carte plate (sqrt(dlat^2+dlon^2))")
    if hits:
        print(f"  - {n:30s} : " + " ; ".join(hits) + f"   [feu {feu}/3]")

print("\n### Anatomie de l'epee : ces chateaux rendent-ils une croix plausible ?")
print("   (angle a Lombrives entre la lame Lombrives->Urquhart et le quillon Lombrives->Leon ;")
print("    ecart du chateau a la droite Mercator Leon->Lombrives = alignement garde/rocher ;")
print("    intersection garde x axe Urquhart->Valence)")
V = (CO["Cathédrale de Valence"]["lat"], CO["Cathédrale de Valence"]["lon"])
for n, p, d, b, units, dl, nv, feu, src in sorted(rows, key=lambda r: r[2]):
    a1 = G.bearing(LO, U); a2 = G.bearing(LO, LEON)
    ang = abs(((a1 - a2) + 180) % 360 - 180)
    ec = G.merc_cross_track(p, LEON, LO)
    inter = G.gc_intersection(p, LEON, U, V)
    g1, g2 = inter
    pt = g1 if G.hav(g1, (43, 0)) < G.hav(g2, (43, 0)) else g2
    print(f"   {n[:29]:30s} croix={ang:5.1f} deg | aligne garde-rocher ecart {ec:6.1f} km | garde x axe = {pt[0]:7.4f},{pt[1]:8.4f}"
          f" ({G.hav(pt, (42.75,-0.9)):5.0f} km de Jaca)")

print("\n### Points de reference pour 'pres de 11 lieues' (les 3 lectures testees)")
for nom, pt in [("11 l.commune plein ouest (48,9 km)", G.dest(RLC, 270, 11 * 4.4448)),
                ("11 l.Paris plein ouest (42,9 km)", G.dest(RLC, 270, 11 * 3.898)),
                ("11 l.metrique plein ouest (44,0 km)", G.dest(RLC, 270, 44.0)),
                ("11/25 degre de LONGITUDE", (RLC[0], RLC[1] - 11 / 25)),
                ("11/25 degre de distance en degres", None)]:
    if pt is None:
        continue
    near = sorted(CAND, key=lambda c: G.hav(pt, c[1]))[:3]
    print(f"   {nom:36s} -> {pt[0]:7.3f},{pt[1]:8.4f} | plus proches : "
          + " ; ".join(f"{c[0]} {G.hav(pt, c[1]):.1f} km" for c in near))
