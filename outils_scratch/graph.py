import json,numpy as np,math,collections
from pyproj import Transformer
tr=Transformer.from_crs(4326,2154,always_xy=True)
# --- edges: BD TOPO + OSM
E=[]  # (coords L93 list, src, nature)
for f in json.load(open('wfs_troncon_de_route.json'))['features']:
    g=f['geometry']; p=f['properties']
    cs=g['coordinates'] if g['type']=='LineString' else [c for l in g['coordinates'] for c in l]
    E.append(([(c[0],c[1]) for c in cs],'BDT',p.get('nature')))
d=json.load(open('osm.json'));Nn=d['nodes']
for wid,nds,t in d['ways']:
    if 'highway' in t:
        cs=[tr.transform(Nn[n][1],Nn[n][0]) for n in nds if n in Nn]
        if len(cs)>1: E.append((cs,'OSM',t['highway']))
# node degree by snapping endpoints/vertices on 3 m grid
deg=collections.defaultdict(set); kinds=collections.defaultdict(set)
for k,(cs,src,nat) in enumerate(E):
    for i,c in enumerate(cs):
        key=(round(c[0]/3),round(c[1]/3))
        # count each neighbor direction
        for j in (i-1,i+1):
            if 0<=j<len(cs):
                o=cs[j]; ang=round(math.degrees(math.atan2(o[1]-c[1],o[0]-c[0]))/20)
                deg[(src,key)].add((k,j>i)); kinds[(src,key)].add(nat)
J=[]
for (src,key),s in deg.items():
    if len(s)>=3:
        J.append({'x':key[0]*3,'y':key[1]*3,'src':src,'deg':len(s),'nat':sorted(map(str,kinds[(src,key)]))})
print(len(J),'jonctions brutes')
# merge BDT/OSM duplicates within 15 m
J.sort(key=lambda j:-j['deg']); keep=[]
for j in J:
    if all((j['x']-k['x'])**2+(j['y']-k['y'])**2>225 for k in keep): keep.append(j)
print(len(keep),'jonctions fusionnées')
json.dump(keep,open('junctions.json','w'))
