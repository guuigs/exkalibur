# T4 A5: Touvet (hit B3) ; blocs erratiques/pierres (Wikipedia FR) ; OSM retry léger
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
W=r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/'
F=json.load(open(W+'t4_parc_onf.json',encoding='utf-8'))
for f in F:
    if "Touvet" in f["nom"] and f["code"] in("3","11"):
        c=cen({"type":"Polygon","coordinates":[f["rings"][0]]}); print("Touvet",f["code"],"%.4f,%.4f"%c,"à %.1f km de la tour"%hav(TA,c))
import urllib.parse
def wp(params):
    return json.loads(get("https://fr.wikipedia.org/w/api.php?format=json&"+urllib.parse.urlencode(params)))
print("\n## Wikipedia géosearch 8 km (articles géolocalisés)")
r=wp({"action":"query","list":"geosearch","gscoord":"%f|%f"%TA,"gsradius":10000,"gslimit":500})
rx=re.compile(r"pierre|roche|rocher|bloc|erratique|menhir|caillou|rocs?\b|balme|perron|cascade|source|fontaine",re.I)
for x in r["query"]["geosearch"]:
    if rx.search(x["title"]): print("  %.2f km  %s"%(x["dist"]/1000,x["title"]))
print("total articles géolocalisés:",len(r["query"]["geosearch"]))
print("\n## Recherche texte Wikipedia")
for q in ['bloc erratique Grésivaudan Pontcharra','bloc erratique Saint-Maximin Isère','"pierre" "Saint-Maximin" Isère rocher ruisseau','bloc erratique Allevard Pontcharra La Rochette glaciaire']:
    try:
        r=wp({"action":"query","list":"search","srsearch":q,"srlimit":6})
        print("Q:",q)
        for x in r["query"]["search"]: print("   ",x["title"],"|",re.sub("<[^>]+>","",x["snippet"])[:110])
    except Exception as e: print("ERR",q,e)
print("\n## OSM retry (natural=stone|boulder, 3 km autour de la tour)")
for ep in ["https://overpass-api.de/api/interpreter","https://overpass.private.coffee/api/interpreter"]:
    try:
        q='[out:json][timeout:20];nwr["natural"~"^(stone|boulder|rock)$"](around:4000,%f,%f);out center tags;'%TA
        req=urllib.request.Request(ep,data=urllib.parse.urlencode({"data":q}).encode(),headers={"User-Agent":"exkalibur-research/1.0","Accept":"*/*"})
        els=json.loads(urllib.request.urlopen(req,timeout=30).read())["elements"]; print(ep,len(els))
        for e in els:
            c=(e.get("lat"),e.get("lon")) if "lat" in e else (e["center"]["lat"],e["center"]["lon"])
            print("  %.2f km %3.0f° %s %s"%(hav(TA,c),brg(TA,c),e["tags"].get("natural"),e["tags"].get("name","")))
        break
    except Exception as e: print("ERR",ep,str(e)[:70])
