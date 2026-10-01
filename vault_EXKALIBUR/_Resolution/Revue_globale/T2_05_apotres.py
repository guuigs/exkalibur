# Piste APOTRES : lieux nommés Jacques/Simon/Jude etc. dans 10 km de la tour d'Avalon ; routes de randonnée (Compostelle) ; couples à 1,85 km ±1 %
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
import json,urllib.request,urllib.parse,itertools,re
ROOT=r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/t2/"
def op(q):
    for ep in ("https://overpass-api.de/api/interpreter","https://overpass.private.coffee/api/interpreter"):
        try:
            req=urllib.request.Request(ep+"?data="+urllib.parse.quote(q),headers={"User-Agent":"ExkaliburResearch/1.0","Accept":"*/*"})
            return json.loads(urllib.request.urlopen(req,timeout=150).read().decode())
        except Exception as e: print("fail",ep,str(e)[:80])
q=f'''[out:json][timeout:120];(
nwr(around:10000,{TA[0]},{TA[1]})["name"~"Jacques|Simon|Compostelle|Coquille|Jude|Apôtre",i];
nwr(around:10000,{TA[0]},{TA[1]})["amenity"="place_of_worship"]["name"];
);out center tags;'''
r=op(q); els=r["elements"] if r else []
print("éléments",len(els))
pts=[]
for e in els:
    lat=e.get("lat") or e.get("center",{}).get("lat"); lon=e.get("lon") or e.get("center",{}).get("lon")
    if lat is None: continue
    t=e.get("tags",{}); pts.append(dict(id=e["type"]+"/"+str(e["id"]),lat=lat,lon=lon,name=t.get("name",""),tags={k:v for k,v in t.items() if k in("amenity","historic","building","religion","denomination","dedication","saint","highway","route","man_made","addr:city","ref")}))
json.dump(pts,open(ROOT+"apotres_pts.json","w"),ensure_ascii=False)
J=re.compile(r"jacques|jacob|compostelle|coquille|jaime|santiago",re.I); S=re.compile(r"simon",re.I)
for lab,rx in (("JACQUES",J),("SIMON",S)):
    print("\n==",lab)
    for p in sorted(pts,key=lambda p:hav(TA,(p["lat"],p["lon"]))):
        if rx.search(p["name"]+" "+str(p["tags"].get("dedication",""))+str(p["tags"].get("saint",""))): print("  d_TA=%.2f d_CB=%.2f"%(hav(TA,(p["lat"],p["lon"])),hav(CB,(p["lat"],p["lon"]))),p["id"],p["name"],p["tags"])
print("\n== lieux de culte (amenity=place_of_worship) et leurs noms")
for p in sorted(pts,key=lambda p:hav(TA,(p["lat"],p["lon"]))):
    if p["tags"].get("amenity")=="place_of_worship": print("  d_TA=%.2f"%hav(TA,(p["lat"],p["lon"])),p["id"],p["name"],p["tags"].get("denomination",""),p["tags"].get("addr:city",""))
# couples J x S
Jp=[p for p in pts if J.search(p["name"])]; Sp=[p for p in pts if S.search(p["name"])]
print("\nJ:",len(Jp),"S:",len(Sp))
for lab,lo,hi in (("185",1.8315,1.8685),("177.6",1.7582,1.7938),("192",1.9008,1.9392)):
    ok=[(round(hav((a["lat"],a["lon"]),(b["lat"],b["lon"])),4),a["name"],b["name"]) for a in Jp for b in Sp if lo<=hav((a["lat"],a["lon"]),(b["lat"],b["lon"]))<=hi]
    print(lab,"couples Jacques x Simon:",ok)
# routes de randonnée / Compostelle
q2=f'''[out:json][timeout:120];(
relation(around:12000,{TA[0]},{TA[1]})["route"~"hiking|foot"];
relation(around:30000,{TA[0]},{TA[1]})["route"~"hiking|foot"]["name"~"Jacques|Compostelle|Gebennensis|Genève|GR ?65|Via",i];
relation(around:30000,{TA[0]},{TA[1]})["route"~"hiking|foot"]["ref"~"GR ?65|GR ?9|GR ?5"];
);out tags center;'''
r2=op(q2)
print("\n== routes de randonnée")
for e in (r2["elements"] if r2 else []):
    t=e.get("tags",{}); c=e.get("center",{}); 
    print(e["id"],t.get("ref",""),t.get("name",""),t.get("network",""),t.get("route",""),"| d_TA=%.1f"%hav(TA,(c["lat"],c["lon"])) if c else "")
