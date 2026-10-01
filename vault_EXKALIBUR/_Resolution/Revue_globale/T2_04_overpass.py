# Piste 1 : retry Overpass (UA explicite, GET) : croix, calvaires, oratoires, mémoriaux, stations dans 6 km autour de TA et CB ; couples à 1,85 km ±1 %
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
import json,urllib.request,urllib.parse,itertools
ROOT=r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/t2/"
q=f'''[out:json][timeout:60];(
nwr(around:6000,{TA[0]},{TA[1]})["historic"~"wayside_cross|wayside_shrine|calvary|memorial|cross"];
nwr(around:6000,{TA[0]},{TA[1]})["man_made"="cross"];
nwr(around:6000,{TA[0]},{TA[1]})["name"~"[Cc]alvaire|[Cc]roix|[Ss]tation|[Oo]ratoire"];
);out center tags;'''
eps=["https://overpass-api.de/api/interpreter","https://overpass.private.coffee/api/interpreter","https://overpass.openstreetmap.fr/api/interpreter","https://maps.mail.ru/osm/tools/overpass/api/interpreter"]
res=None
for ep in eps:
    for mode in ("GET","POST"):
        try:
            hd={"User-Agent":"ExkaliburResearch/1.0 (personal research; contact: none)","Accept":"application/json","Referer":"https://overpass-turbo.eu/"}
            if mode=="GET": req=urllib.request.Request(ep+"?data="+urllib.parse.quote(q),headers=hd)
            else: req=urllib.request.Request(ep,data=("data="+urllib.parse.quote(q)).encode(),headers={**hd,"Content-Type":"application/x-www-form-urlencoded"})
            res=json.loads(urllib.request.urlopen(req,timeout=70).read().decode()); print("OK",ep,mode,len(res["elements"])); break
        except Exception as e: print("fail",ep,mode,str(e)[:80])
    if res: break
if res:
    pts=[]
    for e in res["elements"]:
        lat=e.get("lat") or e.get("center",{}).get("lat"); lon=e.get("lon") or e.get("center",{}).get("lon"); t=e.get("tags",{})
        if lat: pts.append((lat,lon,t.get("name",""),t.get("historic",t.get("man_made","")),e["type"]+"/"+str(e["id"])))
    json.dump(pts,open(ROOT+"osm_croix.json","w"),ensure_ascii=False)
    for p in sorted(pts,key=lambda p:hav(TA,p[:2])): print("%.2f km"%hav(TA,p[:2]),p[2:])
    for lab,lo,hi in (("185",1.8315,1.8685),("177.6",1.7582,1.7938),("192",1.9008,1.9392)):
        ok=[(round(hav(a[:2],b[:2]),4),a[4],a[2],b[4],b[2]) for a,b in itertools.combinations(pts,2) if lo<=hav(a[:2],b[:2])<=hi]
        print(lab,"couples:",len(ok),"/",len(pts)*(len(pts)-1)//2)
        for o in ok: print("  ",o)
