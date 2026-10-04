import json,math,numpy as np
from scipy import ndimage
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
px,py=T.transform(6.03115,45.42887)
x0,y1=px-350,py+100
# tache visible au sud du Vivier
R0,C0=int(YN-(py-100)),int(px+60-X0)
sub=Vp[R0:R0+200,C0:C0+250]
lab,n=ndimage.label(sub)
for i in range(1,n+1):
  ys,xs=np.where(lab==i)
  if len(ys)<40: continue
  X=X0+C0+xs.mean();Y=YN-(R0+ys.mean());lo,la=Ti.transform(X,Y)
  db=float(np.min(np.hypot(B[:,0]-X,B[:,1]-Y)))
  RR,CC=int(YN-Y),int(X-X0)
  print(f'tache visible {len(ys)} m² centre {la:.6f},{lo:.6f} | tour {math.hypot(X-px,Y-py):.0f} m | maisons {db:.0f} m | ouvert {float((mnh[RR-25:RR+26,CC-25:CC+26]<1.5).mean()):.2f} | haut. arbres autour {float(np.percentile(mnh[RR-40:RR+41,CC-40:CC+41],80)):.0f} m')
# Vivier : altitudes et exutoire
SH=[shape(f['geometry']) for f in json.load(open('wfs_surface_hydrographique.json'))['features']]
viv=[g for g in SH if g.distance(Point(*T.transform(6.03290,45.42844)))<5][0]
print('Vivier surface',round(viv.area),'m²')
ring=max(getattr(viv,"geoms",[viv]),key=lambda g:g.area).exterior
zs=[(mnt[int(YN-p[1]),int(p[0]-X0)],p) for p in [ring.interpolate(t,normalized=True).coords[0] for t in np.linspace(0,1,200)]]
zmin=min(zs);zmax=max(zs);lo,la=Ti.transform(*zmin[1][:2]);lo2,la2=Ti.transform(*zmax[1][:2])
print(f'bord le plus bas {zmin[0]:.1f} m en {la:.6f},{lo:.6f} ; le plus haut {zmax[0]:.1f} m en {la2:.6f},{lo2:.6f}')
# rochers LiDAR autour du Vivier (300 m)
cx,cy=T.transform(6.03290,45.42844);R=300
r0,c0=int(YN-cy)-R,int(cx-X0)-R;D=mnt[r0:r0+2*R,c0:c0+2*R].astype(float)
gy,gx=np.gradient(D);sl=np.degrees(np.arctan(np.hypot(gx,gy)));bump=D-ndimage.gaussian_filter(D,5)
lab,n=ndimage.label((sl>35)&(bump>0.6))
for i in range(1,n+1):
  ys,xs=np.where(lab==i)
  if len(ys)<4: continue
  X=X0+c0+xs.mean();Y=YN-(r0+ys.mean());lo,la=Ti.transform(X,Y)
  db=float(np.min(np.hypot(B[:,0]-X,B[:,1]-Y)))
  print(f'  saillie {len(ys)} m², {bump[lab==i].max():.1f} m : {la:.6f},{lo:.6f} | Vivier {viv.distance(Point(X,Y)):.0f} m | tour {math.hypot(X-px,Y-py):.0f} m | maisons {db:.0f} m')
