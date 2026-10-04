import json,math,numpy as np,gzip,csv 
from shapely.geometry import shape,Point 
from shapely.ops import transform as stf,unary_union 
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000 
Vm=np.unpackbits(np.load('vs_muraille.npy'))[:N*N].reshape(N,N).astype(bool)
Vs=np.unpackbits(np.load('vs_sommet.npy'))[:N*N].reshape(N,N).astype(bool) 
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool) 
NC=shape(json.load(open('cad/noncad.json'))) 
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json')) 
PU=[stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0][:1] in '1234'] 
pm={} 
for r in csv.reader(open('cad/pm_73141.csv',encoding='latin-1'),delimiter=';'): pm[(r[5].strip(),r[6].strip().zfill(4))]=r[20] 
for f in json.load(gzip.open('cad/73141-parcelles.json.gz'))['features']: 
  p=f['properties'];o=pm.get((p['section'].lstrip('0') or p['section'],p['numero'].zfill(4))) or pm.get((p['section'],p['numero'].zfill(4))) 
  if o and o[:1] in '1234': PU.append(stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0)) 
FP=unary_union([shape(f['geometry']) for f in json.load(open('wfs_foret_publique.json'))['features']]) 
import pickle;PUB=unary_union([pickle.load(open('PUB_general.pkl','rb')),NC]+PU+[FP]).buffer(0)
HS=np.array([c[:2] for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if f['geometry']['type']=='LineString' for c in f['geometry']['coordinates']]) 
px,py=T.transform(6.03115,45.42887) 
yy,xx=np.mgrid[-150:151,-150:151];ring=((xx**2+yy**2)>=60**2)&((xx**2+yy**2)<=150**2) 
rows=[] 
for m in M: 
  x,y=m[0],m[1] 
  if not(X0+160<x<X0+6840 and YN-6840<y<YN-160): continue 
  dt=math.hypot(x-px,y-py) 
  if dt<150 or dt>1500: continue 
  r0,c0=int(YN-y),int(x-X0) 
  vp=int(Vm[r0-10:r0+11,c0-10:c0+11].sum());vs=0 
  if vp+vs<20: continue 
  dw=float(np.min(np.hypot(HS[:,0]-x,HS[:,1]-y))) 
  if dw>120: continue 
  fo=float((mnh[r0-150:r0+151,c0-150:c0+151][ring]>5).mean()) 
  pass 
  P=Point(x,y);loc=PUB.intersection(P.buffer(150)) 
  if loc.is_empty: continue 
  # surface publique à ≥100 m des maisons, dans 150 m 
  far=[g for g in getattr(loc,'geoms',[loc])] 
  area=0 
  for g in far: 
    for s in np.arange(0,1,1): 
      pass 
  pts=[] 
  gx=np.arange(x-150,x+151,5);gy=np.arange(y-150,y+151,5) 
  ok=0 
  for X in gx[::2]: 
    for Y in gy[::2]: 
      if math.hypot(X-x,Y-y)<=150 and loc.contains(Point(X,Y)) and np.min(np.hypot(B[:,0]-X,B[:,1]-Y))>=100: ok+=1 
  if ok==0: continue 
  op=float((mnh[r0-20:r0+21,c0-20:c0+21]<1.5).mean()) 
  lo,la=Ti.transform(x,y);az=G.inv(6.03115,45.42887,lo,la)[0]%360 
  rows.append((ok*100,la,lo,dt,az,vp,vs,dw,fo,op,float(np.min(np.hypot(B[:,0]-x,B[:,1]-y))),m[2])) 
print(len(rows),'croisements : vus (pied ou sommet, ±15 m), eau ≤120 m, forêt ≥40 %, terrain public à ≥100 m des maisons dans 150 m') 
for r in sorted(rows,key=lambda r:-(r[5]*5+r[6]))[:25]: 
  print(f'{r[1]:.6f},{r[2]:.6f} | tour {r[3]:.0f} m cap {r[4]:.0f}° | vu muraille {r[5]} m² | eau {r[7]:.0f} | forêt {r[8]:.2f} ouvert {r[9]:.2f} | maisons {r[10]:.0f} | public utile ~{r[0]} m² | deg {r[11]}') 
