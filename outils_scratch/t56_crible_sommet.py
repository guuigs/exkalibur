import json,math,numpy as np
from scipy import ndimage
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
N=7000
Vs=np.unpackbits(np.load('vs_sommet.npy'))[:N*N].reshape(N,N).astype(bool)
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
acc=np.load('acc.npy')
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0][:1] in '1234'])
FP=unary_union([shape(f['geometry']) for f in json.load(open('wfs_foret_publique.json'))['features']])
PUB=unary_union([NC,PU,FP]).buffer(0);PUBL=unary_union([PU,FP]).buffer(0)
HS=np.array([c[:2] for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if f['geometry']['type']=='LineString' for c in f['geometry']['coordinates']])
px,py=T.transform(6.03115,45.42887)
out=[]
for m in M:
  x,y=m[0],m[1]
  if not(X0+160<x<X0+6840 and YN-6840<y<YN-160): continue
  dt=math.hypot(x-px,y-py)
  if dt<300: continue
  r0,c0=int(YN-y),int(x-X0)
  vs=int(Vs[r0-10:r0+11,c0-10:c0+11].sum());vp=int(Vp[r0-10:r0+11,c0-10:c0+11].sum())
  if vs<20: continue
  db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))
  yy,xx=np.mgrid[-150:151,-150:151];ring=((xx**2+yy**2)>=60**2)&((xx**2+yy**2)<=150**2)
  forest=float((mnh[r0-150:r0+151,c0-150:c0+151][ring]>5).mean())
  op=float((mnh[r0-20:r0+21,c0-20:c0+21]<1.5).mean())
  dw=float(np.min(np.hypot(HS[:,0]-x,HS[:,1]-y)))
  a=acc[r0//2-10:r0//2+11,c0//2-10:c0//2+11].max()*4/1e4
  P=Point(x,y)
  lon,lat=Ti.transform(x,y);az=math.degrees(math.atan2(x-px,y-py))%360+2.2
  out.append(dict(db=db,lat=lat,lon=lon,dt=dt,az=az,vs=vs,vp=vp,fo=forest,op=op,dw=dw,ha=a,pub=PUB.distance(P),publ=PUBL.distance(P),deg=m[2]))
print('croisements vus du SOMMET (≥20 m² à ±10 m), hors 300 m :',len(out))
g=[o for o in out if o['db']>=100 and o['fo']>=0.30 and (o['dw']<=200 or o['ha']>=1)]
print('maisons ≥100, forêt ≥30 %, eau ≤200 m ou talweg ≥1 ha :',len(g))
for o in sorted(g,key=lambda o:o['pub']):
  print(f"{o['lat']:.6f},{o['lon']:.6f} | tour {o['dt']:.0f} m cap~{o['az']:.0f}° | vu sommet {o['vs']} pied {o['vp']} | ouvert ±20 {o['op']:.2f} forêt {o['fo']:.2f} | maisons {o['db']:.0f} | eau {o['dw']:.0f} m talweg {o['ha']:.1f} ha | public {o['pub']:.0f} m (larges {o['publ']:.0f} m) | deg {o['deg']}")
