# T4 A2: OSM roches/pierres (requêtes légères, reprises)
import json,urllib.request,urllib.parse,time,math
W=r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/'
bb="45.375,5.95,45.485,6.11"
Q={"nat":f'[out:json][timeout:25];nwr["natural"~"^(stone|boulder|rock|bare_rock|rocks)$"]({bb});out center tags;',
"geo":f'[out:json][timeout:25];nwr["geological"]({bb});out center tags;',
"histo":f'[out:json][timeout:25];nwr["historic"~"^(rune_stone|boundary_stone|megalith|memorial)$"]({bb});out center tags;',
"name":f'[out:json][timeout:25];nwr["name"~"[Pp]ierre|[Rr]oche|[Rr]ocher|[Cc]aillou|[Bb]loc|[Pp]erron|[Rr]oc "]["highway"!~"."]({bb});out center tags;'}
EP=["https://overpass-api.de/api/interpreter","https://overpass.private.coffee/api/interpreter","https://overpass.kumi.systems/api/interpreter"]
res={}
for k,q in Q.items():
    for att in range(2):
        ok=False
        for ep in EP:
            try:
                req=urllib.request.Request(ep,data=urllib.parse.urlencode({"data":q}).encode(),headers={"User-Agent":"exkalibur-research/1.0","Accept":"*/*"})
                res[k]=json.loads(urllib.request.urlopen(req,timeout=35).read())["elements"]; ok=True; print(k,ep,len(res[k]),flush=True); break
            except Exception as e: print("ERR",k,ep.split('/')[2],str(e)[:60],flush=True)
        if ok: break
        time.sleep(4)
json.dump(res,open(W+'t4_osm_roches.json','w',encoding='utf-8'))
print("done")
