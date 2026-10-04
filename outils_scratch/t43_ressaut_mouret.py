import json,math,numpy as np
from scipy import ndimage
from shapely.geometry import shape,Point,LineString
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
acc=np.load('acc.npy');fd=np.load('fdir.npy')
mv={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0].startswith(('1','2','3','4'))])
PUB=unary_union([NC,PU])
rd=[(shape(f['geometry']),f['properties'].get('nature')) for f in json.load(open('wfs_troncon_de_route.json'))['features']]
J=Point(*T.transform(6.040299,45.422426))
kx,ky=T.transform(6.040743,45.421557)
# remonter 150 m en amont du ressaut (cellule d'acc max voisine) puis descendre jusqu'à 500 m
r,c=int((YN-ky)/2),int((kx-X0)/2)
for _ in range(40):
  best=None
  for (dr,dc) in [(a,b) for a in(-1,0,1) for b in(-1,0,1) if a or b]:
    rr,cc=r+dr,c+dc;d_=mv.get(int(fd[rr,cc]))
    if d_ and rr+d_[0]==r and cc+d_[1]==c and acc[rr,cc]>300:
      if best is None or acc[rr,cc]>acc[best]: best=(rr,cc)
  if best is None: break
  r,c=best
pts=[];L=0
for i in range(400):
  X=X0+c*2+1;Y=YN-r*2-1;pts.append((X,Y,L,int(acc[r,c])))
  d_=mv.get(int(fd[r,c]))
  if d_ is None or L>600: break
  r+=d_[0];c+=d_[1];L+=2*(1.414 if d_[0] and d_[1] else 1)
line=LineString([(p[0],p[1]) for p in pts])
print('talweg tracé',round(line.length),'m ; plus proche de la jonction :',round(line.distance(J)),'m')
last=-99
for X,Y,L,a in pts:
  if L-last<15: continue
  last=L;R,C=int(YN-Y),int(X-X0);P=Point(X,Y)
  D=mnt[R-6:R+7,C-6:C+7].astype(float);bump=float((D-ndimage.gaussian_filter(D,3)).max())
  near=sorted((round(g.distance(P)),n) for g,n in rd if g.distance(P)<25)[:2]
  db=float(np.min(np.hypot(B[:,0]-X,B[:,1]-Y)));lo,la=Ti.transform(X,Y)
  print(f'{L:4.0f} m | {la:.6f},{lo:.6f} | z {mnt[R,C]:.0f} | acc {a} | saillie {bump:.1f} | jonction {P.distance(J):.0f} m | chemins {near} | maisons {db:.0f} m | public {PUB.distance(P):.0f} m | arbres {float(np.percentile(mnh[R-8:R+9,C-8:C+9],70)):.0f} m')
