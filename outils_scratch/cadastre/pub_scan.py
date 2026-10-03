import json,math,numpy as np
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
pub=[]
for f in d['features']:
  o=own.get(f['properties']['id'])
  if o and (o[0].startswith(('1','2','3','4')) or 'SYND' in o[1]):
    pub.append((stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0),o[1],o[2],f['properties']['id']))
PU=unary_union([p[0] for p in pub])
X0t,Y0t=T.transform(6.03101275,45.4288723);Zs=z(mnt,X0t,Y0t)+33
Xp,Yp=T.transform(6.03115,45.42887);Zp=z(mnt,Xp,Yp)+1.7
HS=np.array([c[:2] for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if f['geometry']['type']=='LineString' for c in f['geometry']['coordinates']])
rows=[]
for m in M:
  p=Point(m[0],m[1]);dp=PU.distance(p)
  if dp>100 or not(X0+160<m[0]<X0+6840 and YN-6840<m[1]<YN-160): continue
  db=float(np.min(np.hypot(B[:,0]-m[0],B[:,1]-m[1])))
  if db<80: continue
  n=vs=vp=0
  for a in range(-100,101,10):
    for b in range(-100,101,10):
      if math.hypot(a,b)>100 or z(mnh,m[0]+a,m[1]+b)>=1.5: continue
      n+=1;vs+=los(X0t,Y0t,Zs,m[0]+a,m[1]+b,True)<0;vp+=los(Xp,Yp,Zp,m[0]+a,m[1]+b,True)<0
  ring=np.mean([z(mnh,m[0]+a,m[1]+b)>5 for a in range(-150,151,10) for b in range(-150,151,10) if 60<=math.hypot(a,b)<=150])
  rel=los(X0t,Y0t,Zs,m[0],m[1],False)
  lon,lat=Ti.transform(m[0],m[1]);az,_,dd=G.inv(6.03101275,45.4288723,lon,lat)
  near=min(pub,key=lambda t:t[0].distance(p))
  dw=float(np.min(np.hypot(HS[:,0]-m[0],HS[:,1]-m[1])))
  rows.append(dict(lat=round(lat,6),lon=round(lon,6),dist=round(dd),cap=round(az%360),br=m[2],public=round(dp),proprio=near[1],culture=near[2],maisons=round(db),eau=round(dw),ouvert100=n,vus_sommet=int(vs),vus_pied=int(vp),foret=round(float(ring),2),relief_sommet=round(rel,1)))
print(len(rows),'croisements à ≤100 m d\'un terrain public et ≥80 m des maisons')
for r in sorted(rows,key=lambda r:-(r['vus_sommet']+r['vus_pied'])): print(r)
json.dump(rows,open('pub_scan.json','w'),ensure_ascii=False)
