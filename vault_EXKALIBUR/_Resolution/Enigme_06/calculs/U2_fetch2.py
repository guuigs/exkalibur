import sys, json, urllib.request, urllib.parse, time
sys.stdout.reconfigure(encoding="utf-8")
def q(sparql):
    u="https://query.wikidata.org/sparql?format=json&query="+urllib.parse.quote(sparql)
    for i in range(4):
        try:
            r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (research script)","Accept":"application/sparql-results+json"})
            return json.loads(urllib.request.urlopen(r,timeout=180).read())["results"]["bindings"]
        except Exception as e: print("retry",e); time.sleep(3)
    return []
res=set()
for lang in ("fr","en"):
    for cls in ("Q178885","Q22989102","Q4271324"):  # deity, god?, mythical character
        rows=q('SELECT DISTINCT ?l WHERE { ?x wdt:P31 wd:%s. ?x rdfs:label ?l. FILTER(LANG(?l)="%s") }'%(cls,lang))
        print(lang,cls,len(rows)); res|={r["l"]["value"] for r in rows}
# sous-classes de dieux (grec, romain...) via P31/P279*
for lang in ("fr","en"):
    rows=q('SELECT DISTINCT ?l WHERE { ?x wdt:P31/wdt:P279 wd:Q178885. ?x rdfs:label ?l. FILTER(LANG(?l)="%s") }'%lang)
    print(lang,"sub",len(rows)); res|={r["l"]["value"] for r in rows}
json.dump(sorted(res),open("U2data/deities.json","w",encoding="utf-8"),ensure_ascii=False)
print(len(res))
