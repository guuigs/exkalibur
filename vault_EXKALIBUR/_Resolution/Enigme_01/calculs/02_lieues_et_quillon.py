"""Enigme 1 - quillon est : les 11 lieues vers le Couchant depuis Rennes-le-Chateau.

Question : quel chateau se trouve a 'pres de 11 lieues vers le Couchant' de RLC ?
Methode : pour chaque candidat (chateaux OSM + liste cathare), on calcule plusieurs 'metriques
de distance' plausibles, puis la LONGUEUR DE LIEUE IMPLIQUEE = metrique / 11, qu'on compare
aux lieues historiques reelles. Un candidat n'est retenu que si la lieue impliquee est une
lieue historiquement attestee (ou si l'ecart a 11 lieues est < 5 %).
"""
import json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
from importlib import import_module
G = import_module("00_geo")

HERE = os.path.dirname(os.path.abspath(__file__))
COORDS = json.load(open(os.path.join(HERE, "..", "..", "02_Audit_calculs", "coords.json"), encoding="utf-8"))
OV = json.load(open(os.path.join(HERE, "overpass_chateaux_rlc.json"), encoding="utf-8"))
RLC = (COORDS["Rennes-le-Château"]["lat"], COORDS["Rennes-le-Château"]["lon"])

# lieues historiques (source : Grand Vocabulaire francais 1768 cite par fr.wikipedia 'Lieue' ;
# 1 toise = 1.9490 m ; plus lieues modernes)
LIEUES = {
    "l.metrique 4.000": 4.000,
    "l.commune Fr 4.4448 (1/25 deg)": 4.4448,
    "l.marine 5.5556 (1/20 deg)": 5.5556,
    "l.Paris/poste 3.898": 3.898,
    "l.Beauce 3.313": 3.313,
    "l.Bretagne-Anjou 4.483": 4.483,
    "l.Artois 3.975": 3.975,
    "l.Maine-Poitou 4.637": 4.637,
    "l.Bourbonnais 4.839": 4.839,
    "l.Bourgogne 5.177": 5.177,
    "l.Gascogne-Provence 5.847": 5.847,
    "l.belge 5.000": 5.000,
    "l.anglaise 4.828": 4.828,
    "l.espagnole 4.180": 4.180,
    "l.gauloise 2.222": 2.222,
}

# chateaux connus de coords.json (liste 'cathare')
CATHARES = ["Château de Foix", "Château de Montségur", "Château de Roquefixade", "Château de Lordat",
            "Château de Puivert", "Château d'Usson", "Château de Montaillou", "Château de Montréal-de-Sos",
            "Château de Termes", "Château d'Arques", "Château de Peyrepertuse", "Château de Quéribus",
            "Château de Puilaurens", "Château de Lastours", "Château de Carcassonne"]
CAND = {}
for k in CATHARES:
    if k in COORDS:
        CAND[k] = (COORDS[k]["lat"], COORDS[k]["lon"])
for el in OV["elements"]:
    t = el.get("tags", {})
    h = el.get("center") or el
    if "lat" in h and "lon" in h and t.get("name") and t["name"] not in CAND:
        CAND[t["name"]] = (h["lat"], h["lon"])

def metrics(dst):
    lat, lon = dst
    dlat, dlon = lat - RLC[0], lon - RLC[1]
    return {
        "ortho": G.hav(RLC, dst),                                   # geodesique
        "rhumb": G.rhumb_dist2(RLC, dst),                           # loxodromie
        "merc_plan": math.hypot(*[b - a for a, b in zip(G.m(*RLC), G.m(*dst))]) / 1000.0,  # regle sur carte Mercator
        "dlon_sol": abs(dlon) * 111.320 * math.cos(math.radians(RLC[0])),  # ecart de longitude, km au sol
        "dlon_deg": abs(dlon),                                      # ecart de longitude en degres
        "naive_deg": math.hypot(dlat, dlon),                        # distance 'plate carree' en degres
    }

rows = []
for n, p in CAND.items():
    mm = metrics(p)
    mm["cap"] = G.bearing(RLC, p)
    mm["cap_merc"] = G.merc_bearing(RLC, p)
    mm["pt"] = p
    mm["nom"] = n
    rows.append(mm)

print("=" * 110)
print("RENNES-LE-CHATEAU %.4f, %.4f   (source OSM Nominatim) — %d chateaux candidats" % (RLC[0], RLC[1], len(rows)))
print("=" * 110)

print("\n### 1) Le chateau se trouve-t-il a ~11 lieues ? => LIEUE IMPLIQUEE = distance / 11")
print("(on ne garde que la bande 240-300 deg : 'vers le Couchant'. Une lieue impliquee qui")
print(" tombe sur une lieue historique attestee = indice FORT.)")
print(f"\n{'chateau':34s} {'km ortho':>9s} {'cap':>5s} | {'l.ortho/11':>10s} {'l.merc/11':>10s} {'l.rhumb/11':>10s} | verdict")
for r in sorted(rows, key=lambda r: r["ortho"]):
    if not (240 <= r["cap"] <= 300) or r["ortho"] > 75:
        continue
    units = {k: v for k, v in LIEUES.items()}
    def best(mi):
        im = mi / 11.0
        cands = [(abs(im - v) / v, k) for k, v in units.items()]
        cands.sort()
        return im, cands[0]
    io, bo = best(r["ortho"]); ic, bc = best(r["merc_plan"]); ir, br = best(r["rhumb"])
    def fmt(im, b):
        return f"{im:5.2f}({b[1].split()[0]}{'*' if b[0] < 0.03 else ''})"
    print(f"{r['nom'][:33]:34s} {r['ortho']:9.1f} {r['cap']:5.0f} | {fmt(io,bo):>15s} {fmt(ic,bc):>15s} {fmt(ir,br):>15s} |")

print("\n### 2) Toutes les unites : nombre de lieues pour les chateaux 'cathares' de la bande couchant")
print(f"{'chateau':30s} {'km':>6s} {'cap':>4s} | " + " | ".join(f"{k.split()[0][2:]:>9s}" for k in LIEUES))
for r in sorted(rows, key=lambda r: r["ortho"]):
    if not (240 <= r["cap"] <= 300) or r["ortho"] > 75:
        continue
    vals = " | ".join(f"{r['ortho']/v:9.2f}" for v in LIEUES.values())
    print(f"{r['nom'][:29]:30s} {r['ortho']:6.1f} {r['cap']:4.0f} | {vals}")

print("\n### 3) Les autres metriques (degres, longitude) : nombre de 'lieues de 25 au degre'")
print("  * dlon_deg : ecart de longitude seul, en lieues de 1/25 deg (lecture directe du meridien/longitude)")
print("  * naive_deg: sqrt(dlat^2+dlon^2) en degres -> lieues de 1/25 deg (carte 'plate carree')")
print("  * merc_plan/4.4448 : on mesure la droite sur la carte Mercator et on divise par 4,4448 km")
print(f"{'chateau':30s} {'km':>6s} {'cap':>4s} | {'dlon_lieues':>11s} {'naive_lieues':>12s} {'merc/4.4448':>11s}")
for r in sorted(rows, key=lambda r: r["ortho"]):
    if not (240 <= r["cap"] <= 300) or r["ortho"] > 75:
        continue
    print(f"{r['nom'][:29]:30s} {r['ortho']:6.1f} {r['cap']:4.0f} | {r['dlon_deg']*25:11.2f} {r['naive_deg']*25:12.2f} {r['merc_plan']/4.4448:11.2f}")

print("\n### 4) Points situes a 11 lieues EXACTEMENT a l'ouest, selon 3 lectures")
for nom, km in [("11 l.commune 4.4448", 11 * 4.4448), ("11 l.Paris 3.898", 11 * 3.898), ("11 l.metrique 4.0", 44.0)]:
    a = G.dest(RLC, 270, km)                      # orthodromie plein ouest
    b = G.merc_interp(RLC, G.dest(RLC, 270, km * 1.4), km / G.merc_dist_ground(RLC, G.dest(RLC, 270, km * 1.4)))  # droite Mercator plein ouest
    near = sorted(rows, key=lambda r: G.hav(a, r["pt"]))[:3]
    print(f"  {nom:22s} : ortho plein ouest -> {a[0]:.4f},{a[1]:.4f} | plus proches : "
          + ", ".join(f"{r['nom'][:24]} ({G.hav(a, r['pt']):.1f} km)" for r in near))
    b2 = (RLC[0], RLC[1] - km / (111.320 * math.cos(math.radians(RLC[0]))))
    near2 = sorted(rows, key=lambda r: G.hav(b2, r["pt"]))[:3]
    print(f"  {'':22s} : meme latitude, dlon = km -> {b2[0]:.4f},{b2[1]:.4f} | plus proches : "
          + ", ".join(f"{r['nom'][:24]} ({G.hav(b2, r['pt']):.1f} km)" for r in near2))
    b3 = (RLC[0], RLC[1] - 11 / 25)          # 11 lieues = 11/25 degre de longitude
    near3 = sorted(rows, key=lambda r: G.hav(b3, r["pt"]))[:3]
    print(f"  {'':22s} : 11/25 degre de lon (11,00 l. de 25 au degre) -> {b3[0]:.4f},{b3[1]:.4f} | plus proches : "
          + ", ".join(f"{r['nom'][:24]} ({G.hav(b3, r['pt']):.1f} km)" for r in near3))

print("\n### 5) Rennes-le-Chateau est-il SUR la ligne de la garde (Leon -> quillon) ?")
LEON = (COORDS["Cathédrale de León"]["lat"], COORDS["Cathédrale de León"]["lon"])
for nom in ["Château de Foix", "Château de Montségur", "Château de Roquefixade", "Château de Lordat",
            "Château de Montaillou", "Château de Montréal-de-Sos", "Château de Puivert"]:
    p = CAND[nom]
    print(f"  garde Leon->{nom:26s} : RLC a {G.cross_track(RLC, LEON, p):8.1f} km du grand cercle "
          f"| {G.merc_cross_track(RLC, LEON, p):7.1f} km de la droite Mercator "
          f"| cap Leon->chateau {G.bearing(LEON, p):5.1f}° | cap Mercator {G.merc_bearing(LEON, p):5.1f}°")

print("\n### 6) 'entre l'Aragon et le Midi' : la garde Leon->X traverse-t-elle l'Aragon (royaume) ?")
ARAGON = {"Zaragoza": (41.6488, -0.8891), "Huesca": (42.1361, -0.4087), "Jaca": (42.5700, -0.5496),
          "Barbastro": (42.0356, 0.1269), "Lleida": (41.6176, 0.6200), "Val d'Aran (Vielha)": (42.7017, 0.7950)}
for nom in ["Château de Foix", "Château de Montségur", "Château de Roquefixade", "Château de Lordat"]:
    p = CAND[nom]
    txt = ", ".join(f"{k} {G.cross_track(v, LEON, p):.0f} km" for k, v in ARAGON.items())
    print(f"  Leon->{nom:26s} : ecarts aux villes d'Aragon : {txt}")
