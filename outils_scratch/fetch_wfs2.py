import subprocess,json,os
from concurrent.futures import ThreadPoolExecutor
def tile(args):
    lay,x,y=args
    B=f"{x},{y},{x+1750},{y+1750},EPSG:2154";feats=[];start=0
    while True:
        u=f"https://data.geopf.fr/wfs/ows?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES=BDTOPO_V3:{lay}&BBOX={B}&SRSNAME=EPSG:2154&OUTPUTFORMAT=application/json&COUNT=1000&STARTINDEX={start}"
        for t in range(5):
            r=subprocess.run(['curl','-sS','-m','300',u],capture_output=True)
            try: j=json.loads(r.stdout); break
            except: j=None
        if j is None: print('FAIL',lay,x,y); return feats
        f=j.get('features',[]); feats+=f
        if len(f)<1000: return feats
        start+=1000
for lay in ['batiment','troncon_de_route','troncon_hydrographique','zone_de_vegetation','detail_orographique']:
    args=[(lay,933000+i*1750,6482000+j*1750) for i in range(4) for j in range(4)]
    with ThreadPoolExecutor(4) as ex: res=list(ex.map(tile,args))
    seen={};[seen.setdefault(f['id'],f) for r in res for f in r]
    json.dump({'type':'FeatureCollection','features':list(seen.values())},open(f'wfs_{lay}.json','w')); print(lay,len(seen))
