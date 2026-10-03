import json,math,numpy as np
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
from scipy.cluster.hierarchy import fcluster,linkage
exec(open('ring1068.py').read().split('out=[]')[0])
PIED=(45.42887,6.03115);Xp,Yp=T.transform(PIED[1],PIED[0]);Zp=z(mnt,Xp,Yp)+1.7
# candidate open cells in corridor 89-103° true from the foot, 500-3000 m, 5 m grid
pts=[]
for d in np.arange(500,3000,5):
  for az in np.arange(89,103.01,0.6*500/d*5/5):
    lo,la,_=G.fwd(PIED[1],PIED[0],az,d);x,y=T.transform(lo,la)
    if not(X0+5<x<X0+6995 and YN-6995<y<YN-5): continue
    if z(mnh,x,y)>=1.5: continue
    if los(Xp,Yp,Zp,x,y,True)<0: pts.append((x,y,d,az))
print('cellules ouvertes visibles du pied dans le couloir 89-103°:',len(pts))
P=np.array([(p[0],p[1]) for p in pts])
lab=fcluster(linkage(P,'single'),15,'distance') if len(P)>1 else [1]
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
pub=[stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and (own[f['properties']['id']][0].startswith(('1','2','3','4')))]
PU=unary_union(pub)
for L in sorted(set(lab),key=lambda L:-(np.array(lab)==L).sum()):
  idx=[i for i,l in enumerate(lab) if l==L]
  if len(idx)<3: continue
  cx,cy=P[idx].mean(0);lon,lat=Ti.transform(cx,cy);az,_,dd=G.inv(PIED[1],PIED[0],lon,lat)
  js=sorted([(math.hypot(m[0]-cx,m[1]-cy),m) for m in M],key=lambda t:t[0])[:1]
  ring=np.mean([z(mnh,cx+a,cy+b)>5 for a in range(-120,121,8) for b in range(-120,121,8) if 50<=math.hypot(a,b)<=120])
  db=float(np.min(np.hypot(B[:,0]-cx,B[:,1]-cy)))
  print(f'zone {lat:.5f},{lon:.5f} | {dd:.0f} m cap {az%360:.1f}° | {len(idx)} cellules vues | croisement le + proche {js[0][0]:.0f} m ({js[0][1][2]} br) | maisons {db:.0f} | forêt autour {ring:.2f} | public à {PU.distance(Point(cx,cy)):.0f} m')
