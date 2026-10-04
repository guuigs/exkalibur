import json,math,numpy as np
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
H=[(shape(f['geometry']),f['properties']) for f in json.load(open('wfs_troncon_hydrographique.json'))['features']]
SH=[(shape(f['geometry']),f['properties']) for f in json.load(open('wfs_surface_hydrographique.json'))['features']]
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0].startswith(('1','2','3','4'))])
PUB=unary_union([NC,PU])
px,py=T.transform(6.03115,45.42887)
rows=[]
for m in M:
  x,y=m[0],m[1];dt=math.hypot(x-px,y-py)
  if dt>700: continue
  P=Point(x,y);R,C=int(YN-y),int(x-X0)
  v10=int(Vp[R-10:R+11,C-10:C+11].sum())
  yy,xx=np.mgrid[-40:41,-40:41];dk=(xx**2+yy**2)<=1600
  v40=int((Vp[R-40:R+41,C-40:C+41]&dk).sum())
  op=float((mnh[R-30:R+31,C-30:C+31]<1.5).mean())
  db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))
  dw=min([g.distance(P) for g,p in H]+[g.distance(P) for g,p in SH])
  lo,la=Ti.transform(x,y);az,_,_=G.inv(6.03115,45.42887,lo,la)
  rows.append((round(dt),round(az%360),round(la,6),round(lo,6),v10,v40,round(op,2),round(db),round(dw),PUB.contains(P.buffer(1)) or PUB.distance(P)<2,m[2],','.join(sorted(set(m[4])))[:50]))
print(len(rows),'croisements à ≤700 m')
print('dist cap | lat,lon | vu±10 vu r40 | ouvert | maisons | eau | public | deg | nature')
for r in sorted(rows):
  if r[5]>0 or r[8]<80: print('%4d %3d° | %s,%s | %4d %5d | %.2f | %3d m | %3d m | %s | %d | %s'%r)
