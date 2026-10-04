import json,math,numpy as np
from scipy import ndimage
from shapely.geometry import shape,Point
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
acc=np.load('acc.npy');fd=np.load('fdir.npy')
mv={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
rd=[shape(f['geometry']) for f in json.load(open('wfs_troncon_de_route.json'))['features']]
H=[(shape(f['geometry']),f['properties']) for f in json.load(open('wfs_troncon_hydrographique.json'))['features']]
px,py=T.transform(6.03115,45.42887)
ox,oy=T.transform(6.033901,45.429055)
r,c=int((YN-oy)/2),int((ox-X0)/2)
w=acc[r-6:r+7,c-6:c+7];ys,xs=np.unravel_index(np.argmax(w),w.shape);r,c=r-6+ys,c-6+xs
L=0;last=-99
for i in range(600):
  X=X0+c*2+1;Y=YN-r*2-1
  if L-last>=25:
    last=L;R,C=int(YN-Y),int(X-X0);P=Point(X,Y)
    D=mnt[R-10:R+11,C-10:C+11].astype(float);bump=float((D-ndimage.gaussian_filter(D,4)).max())
    dr=min(g.distance(P) for g in rd);db=float(np.min(np.hypot(B[:,0]-X,B[:,1]-Y)))
    hw=min(((g.distance(P)),(p.get('cpx_toponyme_de_cours_d_eau') or p.get('nature'))) for g,p in H)
    lo,la=Ti.transform(X,Y);v=int(Vp[R-15:R+16,C-15:C+16].sum())
    print(f'{L:4.0f} m | {la:.6f},{lo:.6f} | z {mnt[R,C]:.0f} | acc {int(acc[r,c])} | saillie {bump:.1f} | chemin {dr:.0f} m | maisons {db:.0f} m | BDT {hw[0]:.0f} m {hw[1]} | vu pied ±15 {v} | tour {math.hypot(X-px,Y-py):.0f} m')
  d=mv.get(int(fd[r,c]))
  if d is None: break
  r+=d[0];c+=d[1];L+=2*(1.414 if d[0] and d[1] else 1)
  if L>1200: break
