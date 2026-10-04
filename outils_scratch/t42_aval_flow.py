import numpy as np,json,math
from scipy import ndimage
from shapely.geometry import shape,Point
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
acc=np.load('acc.npy');fd=np.load('fdir.npy')
mv={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
rd=[shape(f['geometry']) for f in json.load(open('wfs_troncon_de_route.json'))['features']]
jx,jy=T.transform(6.040299,45.422426)
r,c=int((YN-jy)/2),int((jx-X0)/2)
# snap au talweg le plus proche acc>500
w=acc[r-8:r+9,c-8:c+9];ys,xs=np.where(w>500);k=np.argmin(np.hypot(ys-8,xs-8));r,c=r-8+ys[k],c-8+xs[k]
L=0;last=-99
Dm=mnt.astype(np.float32)
for i in range(400):
  X=X0+c*2+1;Y=YN-r*2-1
  if L-last>=20:
    last=L;R,C=int(YN-Y),int(X-X0)
    D=Dm[R-12:R+13,C-12:C+13];bump=float((D-ndimage.gaussian_filter(D,4)).max())
    gy,gx=np.gradient(ndimage.uniform_filter(D,3));sl=float(np.median(np.degrees(np.arctan(np.hypot(gx,gy)))))
    dr=min(g.distance(Point(X,Y)) for g in rd);db=float(np.min(np.hypot(B[:,0]-X,B[:,1]-Y)))
    lo,la=Ti.transform(X,Y);v=int(Vp[R-5:R+6,C-5:C+6].sum())
    print(f'{L:4.0f} m | {la:.6f},{lo:.6f} | z {mnt[R,C]:.0f} | acc {int(acc[r,c])} | pente {sl:.0f}° | saillie max {bump:.1f} m | chemin {dr:.0f} m | maisons {db:.0f} m | vu pied ±5 m {v}')
    if db<40: break
  d=mv.get(int(fd[r,c]))
  if d is None: break
  r+=d[0];c+=d[1];L+=2*(1.414 if d[0] and d[1] else 1)
