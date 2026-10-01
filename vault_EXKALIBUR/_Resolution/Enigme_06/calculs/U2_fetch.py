import sys, json, urllib.request, urllib.parse
sys.stdout.reconfigure(encoding="utf-8")
def q(sparql):
    u="https://query.wikidata.org/sparql?format=json&query="+urllib.parse.quote(sparql)
    r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (research script)"})
    return json.load(urllib.request.urlopen(r,timeout=120))["results"]["bindings"]
Q={
"deities":'SELECT DISTINCT ?l WHERE { ?x wdt:P31/wdt:P279* wd:Q178885. ?x rdfs:label ?l. FILTER(LANG(?l) IN ("fr","en","la")) }',
"drinks":'SELECT DISTINCT ?l WHERE { ?x wdt:P279*/wdt:P31 ?t. VALUES ?t {wd:Q154 wd:Q282 wd:Q44 wd:Q40050 wd:Q36964 wd:Q3314483} ?x rdfs:label ?l. FILTER(LANG(?l) IN ("fr","en")) }',
"wines":'SELECT DISTINCT ?l WHERE { ?x wdt:P31/wdt:P279* wd:Q1273037. ?x rdfs:label ?l. FILTER(LANG(?l)="fr") }',
}
for k,s in Q.items():
    try:
        rows=q(s); L=sorted({r["l"]["value"] for r in rows})
        json.dump(L,open(f"U2data/{k}.json","w",encoding="utf-8"),ensure_ascii=False)
        print(k,len(L),L[:15])
    except Exception as e: print(k,"ERR",e)
