# Piste APOTRES : récupération unique des lieux de culte et noms 'Jacques/Simon' dans 10 km (Overpass), sauvegarde JSON
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
import json,urllib.request,urllib.parse,time
ROOT=r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/t2/"
q=f'''[out:json][timeout:150];(
nwr(around:10000,{TA[0]},{TA[1]})["amenity"="place_of_worship"];
nwr(around:10000,{TA[0]},{TA[1]})["name"~"Jacques|Simon|Compostelle|Coquille",i];
);out center tags;'''
for i in range(2):
    for ep in ("https://overpass-api.de/api/interpreter","https://overpass.private.coffee/api/interpreter"):
        try:
            req=urllib.request.Request(ep+"?data="+urllib.parse.quote(q),headers={"User-Agent":"ExkaliburResearch/1.0","Accept":"*/*"})
            r=json.loads(urllib.request.urlopen(req,timeout=170).read().decode()); 
            pts=[]
            for e in r["elements"]:
                lat=e.get("lat") or e.get("center",{}).get("lat"); lon=e.get("lon") or e.get("center",{}).get("lon"); t=e.get("tags",{})
                if lat: pts.append(dict(id=e["type"]+"/"+str(e["id"]),lat=lat,lon=lon,name=t.get("name",""),tags={k:v for k,v in t.items() if k in("amenity","building","religion","denomination","dedication","saint","highway")}))
            json.dump(pts,open(ROOT+"apotres_pts.json","w",encoding="utf-8"),ensure_ascii=False); print("OK",ep,len(pts)); raise SystemExit
        except SystemExit: raise
        except Exception as e: print("fail",ep,str(e)[:60])
    time.sleep(5)
