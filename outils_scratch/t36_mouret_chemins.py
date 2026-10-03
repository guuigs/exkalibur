import json,math,numpy as np
from pyproj import Transformer,Geod
T=Transformer.from_crs(4326,2154,always_xy=True);Ti=Transformer.from_crs(2154,4326,always_xy=True);G=Geod(ellps='WGS84')
mnt=np.load('mnt.npy');mnh=np.clip(np.nan_to_num(np.load('mnh.npy')),0,60);X0,YN=933000,6489000
z=lambda a,x,y:a[int(YN-y),int(x-X0)]
jx,jy=T.transform(6.040299,45.422426)
print('z croisement',round(z(mnt,jx,jy)))
r=json.load(open('wfs_troncon_de_route.json'));h=json.load(open('wfs_troncon_hydrographique.json'))
bl=json.load(open('wfs_batiment.json'))
def fp(g):
  c=g['coordinates']
  while isinstance(c[0][0],list): c=c[0]
  return c[0][:2]
B=np.array([fp(f['geometry']) for f in bl['features']])
reb=[f for f in h['features'] if f['geometry']['type']=='LineString' and (f['properties'].get('cpx_toponyme_de_cours_d_eau') or '')=='Ruisseau de Rebouchet']
R=np.array([c[:2] for f in reb for c in f['geometry']['coordinates']])
print('Rebouchet points',len(R))
# side of junction relative to flow: find nearest segment & direction (flow from high z to low z)
segs=[]
for f in reb:
  cs=f['geometry']['coordinates']
  if cs[0][2]<cs[-1][2]: cs=cs[::-1]   # orient downstream
  for a,b in zip(cs,cs[1:]): segs.append((a,b))
def nearest(x,y):
  best=None
  for a,b in segs:
    dx,dy=b[0]-a[0],b[1]-a[1];L=dx*dx+dy*dy;t=max(0,min(1,((x-a[0])*dx+(y-a[1])*dy)/L)) if L else 0
    px,py=a[0]+t*dx,a[1]+t*dy;d=math.hypot(x-px,y-py)
    if best is None or d<best[0]: best=(d,a,b,px,py)
  return best
d,a,b,px,py=nearest(jx,jy)
cross=(b[0]-a[0])*(jy-a[1])-(b[1]-a[1])*(jx-a[0])
print(f'distance au Rebouchet {d:.0f} m ; le croisement est sur la rive {"GAUCHE" if cross>0 else "DROITE"} (sens du courant)')
# paths from junction
for f in r['features']:
  cs=[c[:2] for c in f['geometry']['coordinates']]
  e0=math.dist(cs[0],(jx,jy));e1=math.dist(cs[-1],(jx,jy))
  if min(e0,e1)<20:
    if e1<e0: cs=cs[::-1]
    Lp=sum(math.dist(cs[i],cs[i+1]) for i in range(len(cs)-1))
    far=cs[min(len(cs)-1,3)];az=math.degrees(math.atan2(far[0]-jx,far[1]-jy))%360-2.2
    zs=[z(mnt,*c) for c in cs];end=Ti.transform(*cs[-1])
    dR=[nearest(*c)[0] for c in cs]
    dB=min(float(np.min(np.hypot(B[:,0]-c[0],B[:,1]-c[1]))) for c in cs)
    sl=max(abs(zs[i+1]-zs[i])/max(1e-6,math.dist(cs[i],cs[i+1])) for i in range(len(cs)-1))
    print(f"{f['properties']['nature']:16s} cap {az%360:5.0f}° long {Lp:4.0f} m | z {zs[0]:.0f}->{zs[-1]:.0f} | pente max {sl*100:.0f} % | distance min au Rebouchet {min(dR):.0f} m | maisons min {dB:.0f} m | fin {end[1]:.5f},{end[0]:.5f}")
