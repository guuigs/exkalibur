import json,math,numpy as np
from collections import defaultdict
from pyproj import Transformer,Geod
T=Transformer.from_crs(4326,2154,always_xy=True);Ti=Transformer.from_crs(2154,4326,always_xy=True);G=Geod(ellps='WGS84')
X0,YN=933000,6489000
mnt=np.load('mnt.npy'); mnh=np.clip(np.nan_to_num(np.load('mnh.npy')),0,60)
def z(a,x,y): return a[int(YN-y),int(x-X0)]
CEN={'sommet':(45.4288723,6.03101275,33.0),'rue':(45.42977,6.03118,1.7)}
# --- real junctions: OSM dedup (neighbour count) ---
o=json.load(open('osm.json'));nodes=o['nodes'];seen=set();nb=defaultdict(set);kind=defaultdict(set)
for wid,nl,tags in o['ways']:
  if wid in seen or 'highway' not in tags: continue
  seen.add(wid)
  for a,b in zip(nl,nl[1:]):
    nb[a].add(b);nb[b].add(a);kind[a].add(tags['highway']);kind[b].add(tags['highway'])
J=[]
for n,s in nb.items():
  if len(s)>=3 and n in nodes:
    x,y=T.transform(nodes[n][1],nodes[n][0]);J.append([x,y,len(s),'OSM',sorted(kind[n])])
r=json.load(open('wfs_troncon_de_route.json'));E=defaultdict(list)
for f in r['features']:
  cs=f['geometry']['coordinates']
  for e in (cs[0],cs[-1]): E[(round(e[0],1),round(e[1],1))].append(f['properties']['nature'])
for k,v in E.items():
  if len(v)>=3: J.append([k[0],k[1],len(v),'BDT',sorted(set(v))])
# merge within 15 m
M=[]
for j in J:
  for m in M:
    if math.hypot(j[0]-m[0],j[1]-m[1])<15: m[4]=sorted(set(m[4])|set(j[4]));m[2]=max(m[2],j[2]);m[3]=m[3] if m[3]==j[3] else 'OSM+BDT';break
  else: M.append(list(j))
hyd=json.load(open('wfs_troncon_hydrographique.json'))
H=[c for f in hyd['features'] if f['geometry']['type']=='LineString' for c in f['geometry']['coordinates']]
H=np.array([[c[0],c[1]] for c in H])
bl=json.load(open('wfs_batiment.json'))
def fp(g):
  c=g["coordinates"]
  while isinstance(c[0][0],list): c=c[0]
  return c[0][:2]
B=np.array([fp(f["geometry"]) for f in bl["features"]])
def los(ox,oy,oz,tx,ty,canopy):
  zt=z(mnt,tx,ty)+1.5;D=math.hypot(tx-ox,ty-oy);w=-1e9
  for s in np.arange(15,D-3,1.0):
    x=ox+(tx-ox)*s/D;y=oy+(ty-oy)*s/D;h=z(mnt,x,y)+(z(mnh,x,y) if canopy else 0)
    w=max(w,h-(oz+(zt-oz)*s/D))
  return w
out=[]
for cn,(la,lo,eh) in CEN.items():
  ox,oy=T.transform(lo,la);oz=z(mnt,ox,oy)+eh
  for m in M:
    d=math.hypot(m[0]-ox,m[1]-oy)
    if not 1020<=d<=1120: continue
    lon,lat=Ti.transform(m[0],m[1]);az=G.inv(lo,la,lon,lat)[0]%360
    # openness: fraction of no-tree cells within 25 m; forest 50-120 m
    op=[];fo=[]
    for dx in range(-120,121,4):
      for dy in range(-120,121,4):
        rr=math.hypot(dx,dy);h=z(mnh,m[0]+dx,m[1]+dy)
        if rr<=25: op.append(h<2)
        elif 50<=rr<=120: fo.append(h>5)
    dw=np.min(np.hypot(H[:,0]-m[0],H[:,1]-m[1])) if len(H) else 9e9
    db=np.min(np.hypot(B[:,0]-m[0],B[:,1]-m[1]))
    out.append(dict(c=cn,lat=round(lat,6),lon=round(lon,6),d=round(d),az=round(az,1),deg=m[2],src=m[3],nat=m[4],
      ouvert=round(np.mean(op),2),foret=round(np.mean(fo),2),eau=round(dw),bati=round(db),
      relief=round(los(ox,oy,oz,m[0],m[1],False),1),arbres=round(los(ox,oy,oz,m[0],m[1],True),1),canopee=round(float(z(mnh,m[0],m[1])),1)))
json.dump(out,open('ring1068.json','w'),ensure_ascii=False,indent=0)
for e in sorted(out,key=lambda e:(e['c'],e['az'])): print(e)
