# É12 — Règle VD : gabarit de la Via Dolorosa (règle : VD_regle_via_dolorosa.md, écrite avant).
import json, sys, math
from shapely.geometry import shape, Point
from shapely.ops import transform
from shapely.strtree import STRtree
from pyproj import Transformer
DATA, D, O = sys.argv[1], sys.argv[2], sys.argv[3]
st = {}
ROM = {"I": 1, "II": 2, "III et IV": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13}
for e in json.load(open(DATA, encoding="utf-8"))["elements"]:
    t = e.get("tags", {}); nm = (t.get("name") or "").replace(" Statio Crucis", "").strip()
    nm2 = t.get("name:en") or ""
    if nm in ROM: st.setdefault(ROM[nm], (e["lat"], e["lon"]))
    if "IV Station" in nm2 and 4 not in st: st[4] = (e["lat"], e["lon"])
    if nm2 == "Tomb of Christ": st[14] = (e["lat"], e["lon"])
print("stations :", sorted(st))
# coordonnées locales (m) à Jérusalem
la0 = 31.779; KX = 111320 * math.cos(math.radians(la0)); KY = 110900
def loc(p): return ((p[1] - 35.23) * KX, (p[0] - la0) * KY)
L = {k: loc(v) for k, v in st.items()}
d311 = math.hypot(L[11][0] - L[3][0], L[11][1] - L[3][1]); s = 1850 / d311
print(f"III→XI à Jérusalem : {d311:.1f} m ; échelle ×{s:.3f}")
t93 = Transformer.from_crs(4326, 2154, always_xy=True).transform
tll = Transformer.from_crs(2154, 4326, always_xy=True).transform
# nord géographique en Lambert-93 ici : azimut grille = géographique − 2,2°
rot = math.radians(-2.2)
def F(p):
    d = json.load(open(p, encoding="utf-8")); return d if isinstance(d, list) else d["features"]
def g93(geom):
    g = shape(geom); c = g.representative_point().coords[0]
    return g if abs(c[0]) > 1000 else transform(t93, g)
pub = [(g93(r["geom"]), r["den"]) for r in json.load(open(D + "parcelles_pm_8km.json", encoding="utf-8")) if r.get("geom")]
pubg = [g for g, _ in pub]; TP = STRtree(pubg)
bat = [g93(f["geometry"]) for f in F(D + "wfs_bati.json")]; TB = STRtree(bat)
hyd = [g93(f["geometry"]) for f in F(O + "bdt_hydro.json") if f["properties"].get("nature") == "Ecoulement naturel"]; TH = STRtree(hyd)
veg = [(g93(f["geometry"]), f["properties"].get("nature")) for f in F(D + "wfs_veg.json")]; TV = STRtree([g for g, _ in veg])
def dmin(tree, geoms, P, r=500):
    c = [geoms[i].distance(P) for i in tree.query(P.buffer(r))]; return round(min(c)) if c else r
def info(P):
    own = [pub[i][1][:30] for i in TP.query(P) if pubg[i].contains(P)]
    v = [veg[i][1] for i in TV.query(P) if veg[i][0].contains(P)]
    return dict(pm=own or "personne physique / non cadastré", bati=dmin(TB, bat, P), eau=dmin(TH, hyd, P), veg=v or "—")
for sname, (la, lo) in {"esplanade": (45.42891, 6.03112), "rue_Rempart": (45.429772, 6.03118)}.items():
    S = t93(lo, la)
    for anc in (1, 3):
        print(f"\n== départ {sname}, station {anc} au départ")
        for k in sorted(L):
            dx, dy = (L[k][0] - L[anc][0]) * s, (L[k][1] - L[anc][1]) * s
            x = S[0] + dx * math.cos(rot) - dy * math.sin(rot); y = S[1] + dx * math.sin(rot) + dy * math.cos(rot)
            lo2, la2 = tll(x, y)
            extra = info(Point(x, y)) if k >= 10 else ""
            print(f"  {k:2d}  {la2:.5f},{lo2:.5f}  {math.hypot(dx, dy):6.0f} m du départ  {extra}")
