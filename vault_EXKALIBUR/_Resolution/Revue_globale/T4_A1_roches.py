# T4 mission A1: roches/pierres/blocs dans 7 km autour de la tour (OSM, BD TOPO, cadastre)
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
import urllib.request, urllib.parse, time
W=r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/'
RX=re.compile(r"pierre|roche|rocher|roc\b|rocs|caillou|cailloux|bloc|gros|perron|peyre|peire|rochette|balme|baume|erratique|menhir|dolmen|pierr",re.I)
def post(q):
  for att in range(4):
    for ep in ["https://overpass-api.de/api/interpreter","https://overpass.kumi.systems/api/interpreter","https://overpass.private.coffee/api/interpreter"]:
        try:
            req=urllib.request.Request(ep,data=urllib.parse.urlencode({"data":q}).encode(),headers={"User-Agent":"exkalibur-research/1.0","Accept":"*/*"})
            return json.loads(urllib.request.urlopen(req,timeout=60).read())
        except Exception as e: print("ERR",ep,e)
    time.sleep(8)
  return None
R=6000
q=f'''[out:json][timeout:40];(
nwr(around:{R},{TA[0]},{TA[1]})["natural"~"^(stone|boulder|rock|bare_rock|cliff|peak|rocks)$"];
nwr(around:{R},{TA[0]},{TA[1]})["geological"];
nwr(around:{R},{TA[0]},{TA[1]})["name"~"pierre|roche|rocher|caillou|bloc|perron|rocs?$",i];
nwr(around:{R},{TA[0]},{TA[1]})["historic"~"^(rune_stone|wayside_shrine|boundary_stone|megalith|archaeological_site)$"];
);out center tags;'''
j=post(q)
els=[] if j is None else j["elements"]
json.dump(els,open(W+'t4_osm_roches.json','w',encoding='utf-8'))
print("OSM elements",len(els))
rows=[]
for e in els:
    c=(e.get("lat"),e.get("lon")) if "lat" in e else (e["center"]["lat"],e["center"]["lon"]) if "center" in e else None
    if not c: continue
    t=e["tags"]; rows.append((hav(TA,c),brg(TA,c),t.get("natural") or t.get("historic") or t.get("geological"),t.get("name",""),t.get("ele",""),e["type"][0]+str(e["id"]),c))
rows.sort()
from collections import Counter
print(Counter(r[2] for r in rows))
for r in rows:
    if r[0]<=7 and (r[3] or r[2] in("stone","boulder","rock","megalith","rocks")): print("%.2f km %3.0f° %-12s %-35s %s %s"%(r[0],r[1],r[2],r[3],r[4],r[5]))
# BD TOPO
print("--- BD TOPO")
for L in ["detail_orographique","toponymie","lieu_dit_non_habite","construction_ponctuelle","zone_d_activite_ou_d_interet","detail_hydrographique"]:
    try: F=load(L+"_12km")
    except Exception as ex: print(L,"absent",ex); continue
    n=0
    for f in F:
        p=f["properties"]; s=json.dumps(p,ensure_ascii=False)
        nm=" ".join(str(p.get(k,"")) for k in p if k.startswith("toponyme") or k in("nature","nom_1","nom_2","graphie","nom","nature_detaillee"))
        if RX.search(nm):
            c=cen(f["geometry"]); d=hav(TA,c)
            if d<=7: n+=1; print("%s %.2f km %3.0f° | %s"%(L,d,brg(TA,c),nm.strip()))
    print(L,len(F),"matches<=7km:",n)
# detail_orographique natures
F=load("detail_orographique_12km"); print(Counter(f["properties"].get("nature") for f in F))
