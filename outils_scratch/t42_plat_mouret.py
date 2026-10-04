import numpy as np,json,math
from scipy import ndimage
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0].startswith(('1','2','3','4'))])
PUB=unary_union([NC,PU])
acc=np.load('acc.npy')
jx,jy=T.transform(6.040299,45.422426);R=500
r0,c0=int(YN-jy)-R,int(jx-X0)-R;D=ndimage.uniform_filter(mnt[r0:r0+2*R,c0:c0+2*R].astype(float),5)
gy,gx=np.gradient(D);sl=np.degrees(np.arctan(np.hypot(gx,gy)))
# eau : acc 2m >1500 resample
A=acc[(r0)//2:(r0+2*R)//2,(c0)//2:(c0+2*R)//2]>1500
A=np.kron(A,np.ones((2,2),bool))[:2*R,:2*R]
dw=ndimage.distance_transform_edt(~A)
H=mnh[r0:r0+2*R,c0:c0+2*R]
lab,n=ndimage.label((sl<8)&(dw<30))
res=[]
for i in range(1,n+1):
  ys,xs=np.where(lab==i)
  if len(ys)<25: continue
  X=X0+c0+xs.mean();Y=YN-(r0+ys.mean())
  db=float(np.min(np.hypot(B[:,0]-X,B[:,1]-Y)))
  if db<100: continue
  pub=PUB.distance(Point(X,Y))
  lo,la=Ti.transform(X,Y)
  res.append((round(math.hypot(X-jx,Y-jy)),round(la,6),round(lo,6),len(ys),round(float(dw[ys,xs].min())),round(db),round(pub,1),round(float(np.mean(H[ys,xs]>3)),2)))
for r in sorted(res): print('jonction %d m | %s,%s | %d m² | eau %d m | maisons %d m | dist public %.1f m | couvert %.2f'%r)
