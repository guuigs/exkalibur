import json,math,pickle,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point,box
from shapely import contains_xy
from scipy.spatial import cKDTree
from scipy import ndimage
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vm=np.unpackbits(np.load('vs_muraille.npy'))[:N*N].reshape(N,N).astype(bool)
TX,TY=936955.34,6485599.51
PUB2=pickle.load(open('run/PUB2.pkl','rb'));BV=np.load('run/bat_dense.npy');kb=cKDTree(BV)
def line_pts(fn,step=3):
  pts=[]
  for f in json.load(open(fn))['features']:
    g=shape(f['geometry'])
    for l in getattr(g,'geoms',[g]):
      for s in np.arange(0,l.length,step): p=l.interpolate(s);pts.append((p.x,p.y))
  return np.array(pts)
kr=cKDTree(line_pts('large/troncon_de_route.json'));kh=cKDTree(line_pts('large/troncon_hydrographique.json'))
SH=[shape(f['geometry']) for f in json.load(open('wfs_surface_hydrographique.json'))['features']]
shp=[]
for g in SH:
  for p in getattr(g,'geoms',[g]):
    if p.geom_type=='Polygon':
      for s in np.arange(0,p.exterior.length,3): q=p.exterior.interpolate(s);shp.append((q.x,q.y))
ks=cKDTree(np.array(shp))
bump=(mnt-ndimage.gaussian_filter(mnt,2.5)).astype(np.float32)
ry,rx=np.where(bump[int(YN-(TY+600)):int(YN-(TY-600)),int(TX-600-X0):int(TX+600-X0)]>=0.9)
# coordonnées roches
r0=int(YN-(TY+600));c0=int(TX-600-X0)
RK=np.column_stack([X0+c0+rx+0.5,YN-(r0+ry)-0.5]);kk=cKDTree(RK)
g=np.arange(-600,601,5);GX,GY=np.meshgrid(TX+g,TY+g);GX=GX.ravel();GY=GY.ravel()
dT=np.hypot(GX-TX,GY-TY);m=(dT>=40)&(dT<=600);GX=GX[m];GY=GY[m];dT=dT[m]
pub=contains_xy(PUB2,GX,GY);hb=kb.query(np.column_stack([GX,GY]))[0];dr=kr.query(np.column_stack([GX,GY]))[0]
dw=np.minimum(kh.query(np.column_stack([GX,GY]))[0],ks.query(np.column_stack([GX,GY]))[0]);drk=kk.query(np.column_stack([GX,GY]))[0]
ok=pub&(hb>=100)&(dr<=30)
print('points 5 m dans 600 m : %d ; public sûr %d ; +maisons>=100 %d ; +chemin<=30 m %d'%(len(GX),pub.sum(),(pub&(hb>=100)).sum(),ok.sum()))
ok2=ok&(dw<=100)
print('+ eau (ligne ou surface) <=100 m : %d ; + roche (bosse>=0,9) <=60 m : %d'%(ok2.sum(),(ok2&(drk<=60)).sum()))
lab,k=ndimage.label(np.zeros(1))
# clusters
P=np.column_stack([GX[ok2],GY[ok2]])
from scipy.cluster.hierarchy import fcluster,linkage
if len(P)>1:
  Z=linkage(P,'single');cl=fcluster(Z,12,'distance')
  for c in sorted(set(cl),key=lambda c:-(cl==c).sum())[:10]:
    q=P[cl==c];lo,la=Ti.transform(q[:,0].mean(),q[:,1].mean())
    print('amas',c,len(q),'pts (%d m²)'%(len(q)*25),'centre %.5f,%.5f'%(la,lo),'dist tour %.0f'%math.hypot(q[:,0].mean()-TX,q[:,1].mean()-TY))
pickle.dump((GX,GY,ok,ok2,hb,dw,drk,dT),open('run/zone_autorisee.pkl','wb'))
