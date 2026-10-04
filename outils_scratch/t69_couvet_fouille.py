import json,math,pickle,numpy as np
from scipy import ndimage
from shapely.geometry import shape,Point,LineString
from shapely.ops import linemerge,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
PUB=unary_union([pickle.load(open('PUB_general.pkl','rb')),shape(json.load(open('cad/noncad.json')))]).buffer(0)
K=Point(*T.transform(6.059095,45.434748));B_=np.array(B)
segs=[shape(f['geometry']) for f in json.load(open('large/troncon_hydrographique.json'))['features'] if 'Burge' in str(f['properties'].get('cpx_toponyme_de_cours_d_eau'))]
L=linemerge([LineString([c[:2] for c in s.coords]) for s in segs]);L=max(getattr(L,'geoms',[L]),key=lambda l:l.length)
s0=L.project(K)
rd=[(shape(f['geometry']),f['properties'].get('nature')) for f in json.load(open('large/troncon_de_route.json'))['features'] if shape(f['geometry']).distance(K)<900]
print('roche (amont m) | saillie | coffre public ? pas 0,65 / 0,75 / 1,48 (jour dernier 74°) | maisons min | chemin')
best=[]
for d in range(60,560,5):
  p=L.interpolate(s0-d);lo,la=Ti.transform(p.x,p.y);R,C=int(YN-p.y),int(p.x-X0)
  D=mnt[R-6:R+7,C-6:C+7].astype(float);bump=float((D-ndimage.gaussian_filter(D,2.5)).max())
  p2=L.interpolate(s0-d-10);drop=z(mnt,p2.x,p2.y)-z(mnt,p.x,p.y)
  res=[];hm=[];cf=[]
  for pas in (0.65,0.75,1.48):
    l1,a1,_=G.fwd(lo,la,0,10*pas);l1,a1,_=G.fwd(l1,a1,90,10*pas);l2,a2,_=G.fwd(l1,a1,74.0,8*pas)
    q=Point(*T.transform(l2,a2));ok=PUB.contains(q);res.append(ok);hm.append(float(np.min(np.hypot(B_[:,0]-q.x,B_[:,1]-q.y))));cf.append((a2,l2))
  g,n=min(rd,key=lambda t:t[0].distance(p))
  if drop>=4 or any(res):
    print(f'{d:4d} m {la:.6f},{lo:.6f} | chute/10 m {drop:+.1f} saillie +{bump:.1f} | {"".join("✓" if r else "·" for r in res)} | maisons {min(hm):.0f} m | {n} {g.distance(p):.0f} m | coffre(0,75) {cf[1][0]:.6f},{cf[1][1]:.6f}')
