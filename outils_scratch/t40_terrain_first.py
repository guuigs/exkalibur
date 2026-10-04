import json,math,numpy as np
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
Vs=np.unpackbits(np.load('vs_sommet.npy'))[:N*N].reshape(N,N).astype(bool)
open_=mnh<1.5
acc=np.load('acc.npy')*4.0
HS=np.array([c[:2] for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if f['geometry']['type']=='LineString' for c in f['geometry']['coordinates']])
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0].startswith(('1','2','3','4'))])
NC=shape(json.load(open('cad/noncad.json')))
px,py=T.transform(6.03115,45.42887)
rows=[]
for m in M:
  x,y=m[0],m[1]
  if not(X0+160<x<X0+6840 and YN-6840<y<YN-160): continue
  dt=math.hypot(x-px,y-py)
  if dt<400: continue
  db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))
  if db<100: continue
  r0,c0=int(YN-y),int(x-X0)
  win=lambda A,R: A[r0-R:r0+R+1,c0-R:c0+R+1]
  yy,xx=np.mgrid[-60:61,-60:61];disk=(xx**2+yy**2)<=60**2
  vp=int((win(Vp,60)&win(open_,60)&disk).sum());vs=int((win(Vs,60)&win(open_,60)&disk).sum())
  if vp+vs<30: continue
  yy2,xx2=np.mgrid[-150:151,-150:151];ring=((xx2**2+yy2**2)>=60**2)&((xx2**2+yy2**2)<=150**2)
  forest=float((win(mnh,150)[ring]>5).mean())
  op30=float(win(open_,30)[(np.mgrid[-30:31,-30:31]**2).sum(0)<=900].mean())
  dw=float(np.min(np.hypot(HS[:,0]-x,HS[:,1]-y)))
  ta=win(acc,75)  # acc is 2 m grid! fix below
  rows.append([x,y,dt,m[2],db,vp,vs,forest,op30,dw])
# talweg distance using 2 m acc grid
out=[]
for x,y,dt,br,db,vp,vs,forest,op30,dw in rows:
  r2,c2=int((YN-y)/2),int((x-X0)/2);w=acc[r2-75:r2+76,c2-75:c2+76]
  ys,xs=np.where(w>=2e4);dtal=float(np.min(np.hypot(ys-75,xs-75))*2) if len(ys) else 999
  p=Point(x,y);dpub=PU.distance(p);dnc=NC.distance(p)
  lon,lat=Ti.transform(x,y);az,_,_=G.inv(6.03115,45.42887,lon,lat)
  out.append(dict(lat=round(lat,6),lon=round(lon,6),dist=round(dt),cap=round(az%360),br=br,maisons=round(db),vus_pied=vp,vus_sommet=vs,foret=round(forest,2),ouvert30=round(op30,2),ruisseau=round(dw),talweg=round(dtal),public=round(dpub),chemin_public=round(dnc)))
json.dump(out,open('terrain_first.json','w'))
print('croisements >=100 m des maisons avec >=30 m² de clairière visible à 60 m :',len(out))
good=[o for o in out if o['foret']>=0.35 and min(o['ruisseau'],o['talweg'])<=150]
print('… dont en clairière (forêt autour >=35 %) et eau <=150 m :',len(good))
for o in sorted(good,key=lambda o:-(o['vus_pied']*3+o['vus_sommet'])): print(o)
