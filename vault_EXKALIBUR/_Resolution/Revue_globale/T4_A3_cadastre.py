# T4 A3: lieux-dits cadastraux (communes autour) avec pierre/roche/etc. + forêt publique BD TOPO
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
W=r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/'
# communes: Saint-Maximin 38426? on les cherche via geo.api.gouv.fr
cs=json.loads(get(f"https://geo.api.gouv.fr/communes?lat={TA[0]}&lon={TA[1]}&fields=nom,code&format=json"))
print(cs)
# communes voisines dans ~7 km
near={}
for dlat,dlon in [(0,0),(0.05,0),(-0.05,0),(0,0.07),(0,-0.07),(0.05,0.07),(-0.05,-0.07),(0.05,-0.07),(-0.05,0.07),(0.09,0),(-0.09,0),(0,0.11),(0,-0.11)]:
    try:
        for c in json.loads(get(f"https://geo.api.gouv.fr/communes?lat={TA[0]+dlat}&lon={TA[1]+dlon}&fields=nom,code&format=json")): near[c["code"]]=c["nom"]
    except Exception as e: print("err",e)
near['38314']='Pontcharra'
print(near)
import gzip
RX=re.compile(r"pierre|roche|rocher|\broc|caillou|bloc|perron|peyre|peire|balme|baume|gros|erratique|pierr|rocheu|saxe|sass",re.I)
out=[]
for code,nom in near.items():
    try:
        dep=code[:2]
        u=f"https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/{dep}/{code}/cadastre-{code}-lieux_dits.json.gz"
        req=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"})
        j=json.loads(gzip.decompress(urllib.request.urlopen(req,timeout=90).read()))
    except Exception as e: print(code,nom,"ERR",e); continue
    n=0
    for f in j["features"]:
        nm=f["properties"].get("nom","")
        c=cen(f["geometry"]); d=hav(TA,c)
        if RX.search(nm): out.append((d,brg(TA,c),nom,nm,c)); n+=1
    print(code,nom,len(j["features"]),"match",n)
out.sort()
for d,b,com,nm,c in out:
    if d<=7.5: print("%.2f km %3.0f° %-22s %s (%.5f,%.5f)"%(d,b,com,nm,*c))
json.dump(out,open(W+'t4_cadastre_roches.json','w',encoding='utf-8'))
