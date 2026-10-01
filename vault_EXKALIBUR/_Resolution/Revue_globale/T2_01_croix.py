# Piste 1 : croix/calvaires/stations réels à <=6 km de la tour d'Avalon et du château Bayard ; test des couples à 1,85 km ±1 %
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
import json, itertools, urllib.parse
ROOT=r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/t2/"
def overpass(q):
    for ep in ("https://overpass-api.de/api/interpreter","https://overpass.kumi.systems/api/interpreter"):
        try:
            req=urllib.request.Request(ep,data=urllib.parse.urlencode({"data":q}).encode(),headers={"User-Agent":"Mozilla/5.0 (Exkalibur research)"})
            return json.loads(urllib.request.urlopen(req,timeout=120).read().decode())
        except Exception as e: print("overpass fail",ep,e)
    return None
q=f"""[out:json][timeout:90];(
nwr(around:6000,{TA[0]},{TA[1]})["historic"~"wayside_cross|wayside_shrine|memorial|calvary|cross"];
nwr(around:6000,{TA[0]},{TA[1]})["man_made"="cross"];
nwr(around:6000,{TA[0]},{TA[1]})["memorial"="cross"];
nwr(around:6000,{TA[0]},{TA[1]})["religion"="christian"]["tourism"];
nwr(around:6000,{TA[0]},{TA[1]})["name"~"[Cc]alvaire|[Cc]roix|[Ss]tation|Chemin de croix"];
nwr(around:6000,{CB[0]},{CB[1]})["historic"~"wayside_cross|wayside_shrine|memorial|calvary|cross"];
nwr(around:6000,{CB[0]},{CB[1]})["man_made"="cross"];
nwr(around:6000,{CB[0]},{CB[1]})["name"~"[Cc]alvaire|[Cc]roix|[Ss]tation|Chemin de croix"];
);out center tags;"""
r=overpass(q)
pts=[]
if r:
    for e in r["elements"]:
        lat=e.get("lat") or e.get("center",{}).get("lat"); lon=e.get("lon") or e.get("center",{}).get("lon")
        t=e.get("tags",{})
        pts.append(dict(src="OSM",id=f'{e["type"]}/{e["id"]}',lat=lat,lon=lon,name=t.get("name",""),tag=";".join(f"{k}={v}" for k,v in t.items() if k in("historic","man_made","memorial","amenity","tourism","religion","inscription"))))
print("OSM éléments:",len(pts))
# IGN croix (construction_ponctuelle)
n_ign=0
try:
    for f in load("construction_ponctuelle"):
        p=f["properties"]; 
        if "roix" in str(p.get("nature","")).lower() or "calvaire" in str(p.get("nature","")).lower() or "roix" in str(p.get("toponyme","")).lower():
            lo,la=f["geometry"]["coordinates"][:2]; pts.append(dict(src="IGN",id=p.get("cleabs",""),lat=la,lon=lo,name=str(p.get("toponyme") or ""),tag=str(p.get("nature")))); n_ign+=1
except Exception as e: print("IGN err",e)
print("IGN croix:",n_ign)
# Dédoublonnage grossier (même point <15 m)
uniq=[]
for p in pts:
    if p["lat"] is None: continue
    if not any(hav((p["lat"],p["lon"]),(u["lat"],u["lon"]))<0.015 for u in uniq): uniq.append(p)
print("Points uniques:",len(uniq))
json.dump(uniq,open(ROOT+"croix_pts.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
for u in sorted(uniq,key=lambda u:hav(TA,(u["lat"],u["lon"]))):
    print(f'{u["src"]} {u["id"]:>14} d_TA={hav(TA,(u["lat"],u["lon"])):.2f} d_CB={hav(CB,(u["lat"],u["lon"])):.2f} {u["tag"]} | {u["name"]}')
# Couples
for lab,lo,hi in (("185 m",1.8315,1.8685),("177,6 m",1.7582,1.7938),("192 m",1.9008,1.9392)):
    pairs=[]
    for a,b in itertools.combinations(uniq,2):
        d=hav((a["lat"],a["lon"]),(b["lat"],b["lon"]))
        if lo<=d<=hi: pairs.append((round(d,4),a["id"],a["name"],b["id"],b["name"]))
    print(f"\nCouples à {lab} ±1 % : {len(pairs)} sur {len(uniq)*(len(uniq)-1)//2} paires")
    for p in pairs: print("  ",p)
