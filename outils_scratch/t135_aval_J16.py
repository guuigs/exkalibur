import json,math,pickle,numpy as np
from shapely.geometry import shape,Point,LineString
from shapely import contains_xy
from scipy.spatial import cKDTree
from scipy import ndimage
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy');fd=np.load('fdir.npy')
mv={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
PUB2=pickle.load(open('run/PUB2.pkl','rb'));BV=np.load('run/bat_dense.npy');kb=cKDTree(BV)
def line_pts(fn,step=3):
  pts=[]
  for f in json.load(open(fn))['features']:
    g=shape(f['geometry'])
    for l in getattr(g,'geoms',[g]):
      for s in np.arange(0,l.length,step): p=l.interpolate(s);pts.append((p.x,p.y))
  return np.array(pts)
kr=cKDTree(line_pts('large/troncon_de_route.json'))
bump=(mnt-ndimage.gaussian_filter(mnt,2.5)).astype(np.float32)
x,y=T.transform(6.0320,45.42684)
# départ : cellule de talweg la plus proche (acc>=0,3 ha), descente
r2,c2=int((YN-y)/2),int((x-X0)/2)
best=None
for dr in range(-10,11):
  for dc in range(-10,11):
    if acc[r2+dr,c2+dc]*4>=3000:
      dd=math.hypot(dr,dc)
      if best is None or dd<best[0]: best=(dd,r2+dr,c2+dc)
print('talweg le plus proche de J16 : %.0f m'%(best[0]*2))
r,c=best[1],best[2];path=[(r,c)]
for _ in range(400):
    m=mv.get(int(fd[r,c]))
    if not m: break
    r,c=r+m[0],c+m[1];path.append((r,c))
print('descente : %d cellules (%d m)'%(len(path),len(path)*2))
last=None
for i,(r,c) in enumerate(path):
    px,py=X0+c*2+1,YN-r*2-1
    if i%10==0:
        lo,la=Ti.transform(px,py);rr,cc=int(YN-py),int(px-X0)
        b=float(bump[rr-3:rr+4,cc-3:cc+4].max())
        print('  %3d m depuis J16 : %.5f,%.5f z=%.1f acc=%.1f ha | bosse max 6 m %.2f | maisons %.0f m | chemin %.0f m | public %s'%(i*2,la,lo,float(mnt[rr,cc]),acc[r,c]*4/1e4,b,kb.query([px,py])[0],kr.query([px,py])[0],PUB2.contains(Point(px,py))))
