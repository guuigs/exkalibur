import json,math,pickle,numpy as np
from shapely.geometry import shape,Point
from shapely import contains_xy
from scipy.spatial import cKDTree
from scipy import ndimage
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy')
TX,TY=936955.34,6485599.51
PUB2=pickle.load(open('run/PUB2.pkl','rb'));PUB3=pickle.load(open('run/PUB3.pkl','rb'));BV=np.load('run/bat_dense.npy');kb=cKDTree(BV)
def line_pts(fn,step=2):
  pts=[]
  for f in json.load(open(fn))['features']:
    g=shape(f['geometry'])
    for l in getattr(g,'geoms',[g]):
      for s in np.arange(0,l.length,step): p=l.interpolate(s);pts.append((p.x,p.y))
  return np.array(pts)
kr=cKDTree(line_pts('large/troncon_de_route.json'));kh=cKDTree(line_pts('large/troncon_hydrographique.json'))
sp=[]
for f in json.load(open('wfs_surface_hydrographique.json'))['features']:
    g=shape(f['geometry'])
    for p in getattr(g,'geoms',[g]):
        if p.geom_type=='Polygon':
            for s in np.arange(0,p.exterior.length,2): q=p.exterior.interpolate(s);sp.append((q.x,q.y))
ks=cKDTree(np.array(sp))
# talweg cells (acc>=0,3 ha)
yy,xx=np.where(acc*4>=3000);TW=np.column_stack([X0+xx*2+1,YN-yy*2-1]);kt=cKDTree(TW)
bump=(mnt-ndimage.gaussian_filter(mnt,2.5)).astype(np.float32)
Jx,Jy=T.transform(6.0320,45.42684)
sN=(math.sin(math.radians(-2.2)),math.cos(math.radians(-2.2)))
def vec(az_true): a=math.radians(az_true-2.2);return math.sin(a),math.cos(a)
nE=vec(90.0)
def disp(jd,pas):
    # déplacement roche -> coffre
    v=vec(jd);return (10*pas*sN[0]+10*pas*nE[0]+8*pas*v[0],10*pas*sN[1]+10*pas*nE[1]+8*pas*v[1])
# grille de coffres possibles dans 450 m de J16
g=np.arange(-450,451,2);GX,GY=np.meshgrid(Jx+g,Jy+g);GX=GX.ravel();GY=GY.ravel()
m=np.hypot(GX-Jx,GY-Jy)<=450;GX=GX[m];GY=GY[m]
P=np.column_stack([GX,GY])
pub=contains_xy(PUB2,GX,GY);hb=kb.query(P)[0];dr=kr.query(P)[0]
okc=pub&(hb>=100)&(dr<=40)
print('coffres possibles (public sûr, maisons>=100, chemin<=40 m) dans 450 m de J16 :',okc.sum())
res=[]
for jd,nm in ((63.7,'30/04 julien'),(68.6,'30/04 plat'),(73.9,'30/04 visible')):
    for pas in (0.60,0.65,0.70,0.75,0.80):
        dx,dy=disp(jd,pas)
        for (cx,cy) in P[okc]:
            rx,ry=cx-dx,cy-dy;r_,c_=int(YN-ry),int(rx-X0)
            b=float(bump[r_-1:r_+2,c_-1:c_+2].max())
            if b>=0.5:
                dw=min(kt.query([rx,ry])[0],kh.query([rx,ry])[0],ks.query([rx,ry])[0])
                if dw<=40: res.append((b,dw,nm,pas,rx,ry,cx,cy))
print('paires (roche bosse>=0,5 m à ≤40 m d eau ; coffre autorisé) :',len(res))
res.sort(key=lambda t:-t[0])
seen=set()
for b,dw,nm,pas,rx,ry,cx,cy in res:
    key=(round(rx/6),round(ry/6))
    if key in seen: continue
    seen.add(key);lo,la=Ti.transform(rx,ry);lo2,la2=Ti.transform(cx,cy)
    print('roche %.5f,%.5f bosse %.2f eau %.0f m | %s pas %.2f -> coffre %.5f,%.5f | dist J16 %.0f m | maisons %.0f m'%(la,lo,b,dw,nm,pas,la2,lo2,math.hypot(rx-Jx,ry-Jy),kb.query([cx,cy])[0]))
    if len(seen)>=14: break
