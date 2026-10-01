# T4 B2: toutes les parcelles ONF (PARC_PUBL_FR) dans ±10 km ; codes par forêt
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
import xml.etree.ElementTree as ET
W=r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/'
base="http://ws.carmencarto.fr/WFS/105/ONF_Forets"
ns={"gml":"http://www.opengis.net/gml","ms":"http://mapserver.gis.umn.edu/mapserver"}
feats=[]
# tuiles de 0.06° pour éviter la limite
la0,la1,lo0,lo1=TA[0]-0.09,TA[0]+0.09,TA[1]-0.13,TA[1]+0.13
import itertools
la=la0
seen=set()
while la<la1:
    lo=lo0
    while lo<lo1:
        u=f"{base}?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature&TYPENAME=PARC_PUBL_FR&SRSNAME=EPSG:4326&BBOX={la},{lo},{la+0.06},{lo+0.065},EPSG:4326"
        try: t=get(u,150)
        except Exception as e: print("ERR",la,lo,e); lo+=0.065; continue
        root=ET.fromstring(t.encode("utf-8"))
        n=0
        for m in root.iter("{%s}PARC_PUBL_FR"%ns["ms"]):
            fid=m.find("ms:iidtn_frt",ns); nm=m.find("ms:llib_frt",ns); cd=m.find("ms:ccod_prf",ns)
            rings=[]
            for pl in m.iter("{%s}posList"%ns["gml"]):
                v=list(map(float,pl.text.split())); rings.append([(v[i+1],v[i]) for i in range(0,len(v),2)])  # (lon,lat)
            if not rings: continue
            key=(fid.text if fid is not None else None, cd.text if cd is not None else None, round(rings[0][0][0],5), round(rings[0][0][1],5))
            if key in seen: continue
            seen.add(key); n+=1
            feats.append({"frt":key[0],"nom":nm.text if nm is not None else "","code":key[1],"rings":rings})
        print("tile",round(la,3),round(lo,3),n,flush=True)
        lo+=0.065
    la+=0.06
json.dump(feats,open(W+'t4_parc_onf.json','w',encoding='utf-8'))
print("TOTAL",len(feats))
from collections import defaultdict
D=defaultdict(list)
for f in feats: D[(f["frt"],f["nom"])].append(f["code"])
for k,v in sorted(D.items(),key=lambda x:x[0][1]): print(k,len(v),sorted(v,key=lambda s:(len(s or ''),s or '')))
