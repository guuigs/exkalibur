"""Solveur B / É6 — test du hasard de l'alignement Tour -> Battle -> lieu.
Méthode : Wikipedia (en) geosearch (list=geosearch, pages géolocalisées) le long de l'axe Tour->Battle prolongé (cap 149,1°, 100-700 km),
puis sur des axes de CONTRÔLE (mêmes distances, caps décalés de +/-1..15° depuis la Tour) ; on compte les articles « sacrés » (regex sur le titre)
situés à <= 1 km (et <= 0,5 km) de la géodésique. Mesure : combien de lieux sacrés notables « tombent » sur un axe quelconque ?
Sortie : solveurB_06_hasard_alignement.json + .out.txt. Limites : geosearch plafonne à 500 pages par requête (rayon 3 km -> Paris tronqué :
l'axe principal est échantillonné plus finement, rayon 1,2 km / pas 2 km)."""
import sys, json, re, math, time, concurrent.futures as cf, urllib.request, urllib.parse
sys.path.insert(0, "."); from solveurB_geo import *
T = (51.5081124, -0.0759493); B = wiki_coords(["Battle Abbey"])["Battle Abbey"][:2]
AX = cap(T, B)
SACRED = re.compile(r"cathedral|cathédrale|basilica|basilique|abbey|abbaye|priory|prieuré|church|église|eglise|chapel|chapelle|notre-dame|saint|sainte|st\.? |minster|collégiale|collegiate|sanctuary|monastery|monastère|temple|shrine|calvary|chartreuse", re.I)
def geosearch(lat, lon, rad):
    url = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode({"action": "query", "list": "geosearch", "gscoord": f"{lat}|{lon}", "gsradius": rad, "gslimit": 500, "format": "json", "gsprimary": "primary"})
    for k in range(4):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40))["query"]["geosearch"]
        except Exception as e:
            time.sleep(1.5)
    return None
def scan_axis(bearing, d0, d1, step, rad, tol):
    pts = [dest(T, bearing, d) for d in np_arange(d0, d1, step)]
    found = {}; trunc = 0; fail = 0
    with cf.ThreadPoolExecutor(6) as ex:
        for res in ex.map(lambda p: geosearch(p[0], p[1], rad), pts):
            if res is None: fail += 1; continue
            if len(res) >= 500: trunc += 1
            for r in res: found[r["pageid"]] = r
    end = dest(T, bearing, d1 + 5)
    hits = []
    for r in found.values():
        p = (r["lat"], r["lon"]); xt = xtrack(T, end, p); al = along(T, end, p)
        if abs(xt) <= tol and d0 <= al <= d1: hits.append((r["title"], round(xt, 3), round(al, 1)))
    return hits, len(found), trunc, fail
def np_arange(a, b, s):
    x = a; out = []
    while x <= b: out.append(x); x += s
    return out
if __name__ == "__main__":
    out = {}
    # axe principal, échantillonnage fin
    hits, n, tr, fl = scan_axis(AX, 60, 700, 2.0, 1500, 1.0)
    sac = [h for h in hits if SACRED.search(h[0])]
    print(f"AXE PRINCIPAL cap {AX:.3f}° : {n} pages vues, tronquées {tr}, échecs {fl}; dans la bande ±1 km : {len(hits)} pages, dont {len(sac)} 'sacrées' (regex)")
    for h in sorted(sac, key=lambda h: h[2]): print("   ", h)
    out["main"] = {"bearing": AX, "hits": hits, "sacred": sac, "seen": n, "trunc": tr, "fail": fl}
    # contrôles
    ctrl = {}
    for dth in list(range(-15, 0)) + list(range(1, 16)):
        b = AX + dth
        h, n2, tr2, fl2 = scan_axis(b, 100, 500, 3.5, 2100, 1.0)   # rayon 2 km / pas 4 km, couvre la bande
        s = [x for x in h if SACRED.search(x[0])]
        s05 = [x for x in s if abs(x[1]) <= 0.5]
        ctrl[dth] = {"all": len(h), "sacred": len(s), "sacred05": len(s05), "trunc": tr2, "fail": fl2}
        print(f"contrôle {dth:+3d}° (cap {b:.1f}) : bande ±1 km : {len(h)} pages, {len(s)} sacrées (dont {len(s05)} à ±0,5 km) ; tronq {tr2} échecs {fl2}")
    out["controls"] = ctrl
    # même fenêtre 100-500 km pour l'axe principal
    h, n3, tr3, fl3 = scan_axis(AX, 100, 500, 3.5, 2100, 1.0)
    s = [x for x in h if SACRED.search(x[0])]
    out["main_100_500"] = {"all": len(h), "sacred": len(s)}
    print("axe principal fenêtre 100-500 km (mêmes paramètres que contrôles) :", len(h), "pages,", len(s), "sacrées")
    json.dump(out, open("solveurB_06_hasard_alignement.json", "w", encoding="utf-8"), ensure_ascii=False)
