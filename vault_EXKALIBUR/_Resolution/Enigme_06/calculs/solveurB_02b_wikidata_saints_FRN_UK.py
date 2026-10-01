"""Solveur B / É6 — Wikidata (SPARQL, CSV) : lieux de culte/religieux notables (sitelinks >= SL) France+Angleterre(+Benelux)
-> solveurB_saints_wikidata.json. WDQS limite à 1 req/min et tronque ~150 ko : on découpe en 2 boîtes, SELECT DISTINCT minimal."""
import sys, json, urllib.request, urllib.parse, time, csv, io
sys.path.insert(0, "."); from solveurB_geo import *
CLS = "wd:Q2977 wd:Q163687 wd:Q160742 wd:Q108325 wd:Q16970 wd:Q44613 wd:Q317557 wd:Q3146899 wd:Q1128397 wd:Q56750"
SL = 6
BOXES = {"FR-N": (-5.2, 47.0, 8.5, 51.2), "UK": (-6.0, 49.9, 2.0, 55.5)}  # FR-S déjà obtenu (solveurB_saints_wikidata_FRS.json)
def q(w, s, e, n):
    return f"""SELECT DISTINCT ?i ?lat ?lon ?sl WHERE {{
  VALUES ?cls {{ {CLS} }}
  SERVICE wikibase:box {{ ?i wdt:P625 ?c. bd:serviceParam wikibase:cornerSouthWest "Point({w} {s})"^^geo:wktLiteral; wikibase:cornerNorthEast "Point({e} {n})"^^geo:wktLiteral }}
  ?i wdt:P31 ?cls; wikibase:sitelinks ?sl. FILTER(?sl >= {SL})
  BIND(geof:latitude(?c) AS ?lat) BIND(geof:longitude(?c) AS ?lon) }}"""
res = {r["id"]: r for r in json.load(open("solveurB_saints_wikidata_FRS.json"))}
for nm, box in BOXES.items():
    for attempt in range(8):
        try:
            url = "https://query.wikidata.org/sparql?" + urllib.parse.urlencode({"query": q(*box)})
            req = urllib.request.Request(url, headers={"User-Agent": "hermes-solveurB/1.0 (treasure-hunt research)", "Accept": "text/csv"})
            txt = urllib.request.urlopen(req, timeout=170).read().decode("utf-8", "replace")
            rows = list(csv.DictReader(io.StringIO(txt))); break
        except Exception as ex:
            print(nm, "erreur", ex); time.sleep(75); rows = None
    if rows is None: continue
    for r in rows:
        k = r["i"].split("/")[-1]; res[k] = {"id": k, "lat": float(r["lat"]), "lon": float(r["lon"]), "sl": int(r["sl"])}
    print(nm, len(rows), "lignes; cumul", len(res)); time.sleep(65)
json.dump(list(res.values()), open("solveurB_saints_wikidata.json", "w", encoding="utf-8"))
print("distincts:", len(res))
