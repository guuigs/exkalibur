# Piste APOTRES (suite) : églises/chapelles/lieux nommés d'après un apôtre dans 10 km ; paires 3e/11e ; test du hasard ; route Compostelle
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
import json,re,itertools,urllib.request,urllib.parse,random
ROOT=r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/t2/"
pts=json.load(open(ROOT+"apotres_pts.json",encoding="utf-8"))
AP={"Jacques":r"jacques","Simon":r"simon(?!e)","Pierre":r"pierre","Barthélemy":r"barth[eé]lemy","Philippe":r"philippe","Jean(ap.)":r"saint-jean(?!-baptiste)","Jude":r"jude|thadd","Paul":r"saint-paul"}
worship=[p for p in pts if p["tags"].get("amenity")=="place_of_worship" or re.search(r"église|chapelle|oratoire|hôpital",p["name"],re.I)]
print("lieux de culte nommés:",len(worship))
byap={}
for p in worship:
    for k,rx in AP.items():
        if re.search(r"(saint|st)[- ]"+rx.replace("saint-",""),p["name"],re.I) or (rx.startswith("saint") and re.search(rx,p["name"],re.I)):
            byap.setdefault(k,[]).append(p)
for k,v in byap.items(): print(k,[(p["name"],round(hav(TA,(p["lat"],p["lon"])),2)) for p in v])
# paires entre lieux de culte de deux apôtres différents à 1,85 km
wins={"185":(1.8315,1.8685),"177.6":(1.7582,1.7938),"192":(1.9008,1.9392)}
allw=[(k,p) for k,v in byap.items() for p in v]
for lab,(lo,hi) in wins.items():
    ok=[(k1,a["name"],k2,b["name"],round(hav((a["lat"],a["lon"]),(b["lat"],b["lon"])),4)) for (k1,a),(k2,b) in itertools.combinations(allw,2) if k1!=k2 and lo<=hav((a["lat"],a["lon"]),(b["lat"],b["lon"]))<=hi]
    print(lab,"paires d'apôtres différents:",ok)
# test du hasard : sur les N lieux de culte nommés (tous), proba qu'une paire tombe dans la fenêtre
W=[p for p in worship]
tot=0;hit=0
for a,b in itertools.combinations(W,2):
    tot+=1
    if 1.8315<=hav((a["lat"],a["lon"]),(b["lat"],b["lon"]))<=1.8685: hit+=1
print("lieux de culte nommés",len(W),"paires",tot,"dans 185±1%:",hit,"=> %.4f"%(hit/tot))
# Compostelle : relations route hiking nom Jacques/Compostelle, 60 km
q=f'[out:json][timeout:50];relation(around:60000,{TA[0]},{TA[1]})["route"~"hiking|foot"]["name"~"Jacques|Compostelle|Gebennensis|Saint-Jacques",i];out tags center;'
try:
    req=urllib.request.Request("https://overpass-api.de/api/interpreter?data="+urllib.parse.quote(q),headers={"User-Agent":"ExkaliburResearch/1.0","Accept":"*/*"})
    r=json.loads(urllib.request.urlopen(req,timeout=60).read().decode())
    print("routes Jacques 60 km:",len(r["elements"]))
    for e in r["elements"]:
        c=e.get("center",{}); print(e["id"],e["tags"].get("name"),e["tags"].get("ref"),"d_TA=%.1f"%hav(TA,(c["lat"],c["lon"])))
except Exception as e: print("Overpass routes échec:",e)
