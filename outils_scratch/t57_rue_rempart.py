import json,math,numpy as np
exec(open('ring1068.py').read().split('out=[]')[0])
from shapely.geometry import shape,LineString
from shapely.ops import linemerge
L=[shape(f['geometry']) for f in json.load(open('wfs_troncon_de_route.json'))['features'] if 'REMPART' in json.dumps(f['properties']).upper()]
L=linemerge([LineString([c[:2] for c in l.coords]) for l in L])
pts=[L.interpolate(s) for s in np.arange(0,L.length+1,10)]
print('rue du Rempart',round(L.length),'m,',len(pts),'points')
tg={'N (Coisetan, 4 voies)':(6.026558,45.447665),'N2 (3 voies)':(6.026721,45.447584),'Mouret':(6.040299,45.422426),'J5':(6.054780,45.426948),'Le Crêt':(6.05309,45.430543)}
for k,(lo,la) in tg.items():
  tx,ty=T.transform(lo,la);res=[]
  for p in pts:
    oz=z(mnt,p.x,p.y)+1.7
    res.append(los(p.x,p.y,oz,tx,ty,True))
  res=np.array(res);print(f'{k:24s} vu depuis {int((res<0).sum())}/{len(pts)} points de la rue (marge min {res.min():+.1f} m) ; sans arbres : {sum(los(p.x,p.y,z(mnt,p.x,p.y)+1.7,tx,ty,False)<0 for p in pts)}/{len(pts)}')
