import json,math,numpy as np
from pyproj import Transformer
from scipy import ndimage
T=Transformer.from_crs(4326,2154,always_xy=True);Ti=Transformer.from_crs(2154,4326,always_xy=True)
X0,YN,N=933000,6489000,7000
mnt=np.load('mnt.npy');mnh=np.clip(np.nan_to_num(np.load('mnh.npy')),0,60)
dsm=mnt+mnh
obs={'sommet':(45.4288723,6.03101275,33.0),'pied':(45.42887,6.03115,1.7)}
# candidate cells every 4 m in corridor
ox,oy=T.transform(6.03101275,45.4288723)
xs=np.arange(ox+300,X0+N-5,4.0);ys=np.arange(oy-1500,oy+1500,4.0)
XX,YY=np.meshgrid(xs,ys);D=np.hypot(XX-ox,YY-oy);AZ=np.degrees(np.arctan2(XX-ox,YY-oy))%360
sel=(D>=1200)&(D<=3100)&(AZ>=70)&(AZ<=120)
cx,cy=XX[sel],YY[sel]
ri=(YN-cy).astype(int);ci=(cx-X0).astype(int)
openm=mnh[ri,ci]<1.5
cx,cy,ri,ci=cx[openm],cy[openm],ri[openm],ci[openm]
print('cellules ouvertes dans le couloir',len(cx))
V={}
for k,(la,lo,eh) in obs.items():
  x0,y0=T.transform(lo,la);z0=mnt[int(YN-y0),int(x0-X0)]+eh
  zt=mnt[ri,ci]+1.5;Dd=np.hypot(cx-x0,cy-y0)
  vis=np.ones(len(cx),bool)
  for f in np.linspace(0.01,0.995,700):
    x=x0+(cx-x0)*f;y=y0+(cy-y0)*f
    h=dsm[(YN-y).astype(int),(x-X0).astype(int)]
    near=Dd*(1-f)<4   # ignore last 4 m
    vis&= (h <= z0+(zt-z0)*f) | near
  V[k]=vis;print(k,'visibles',vis.sum())
# group visible open cells into patches; keep patches surrounded by forest
grid=np.zeros((N,N),bool)
for k in V: pass
vis_any=V['sommet']|V['pied']
pts=np.c_[cx[vis_any],cy[vis_any],V['sommet'][vis_any],V['pied'][vis_any]]
# cluster with 12 m linkage
from scipy.cluster.hierarchy import fcluster,linkage
if len(pts)>1:
  lab=fcluster(linkage(pts[:,:2],'single'),12,'distance')
else: lab=np.ones(len(pts))
r=json.load(open('wfs_troncon_de_route.json'))
J=json.load(open('axe_loup.json'))
B=[]
bl=json.load(open('wfs_batiment.json'))
def fp(g):
  c=g['coordinates']
  while isinstance(c[0][0],list): c=c[0]
  return c[0][:2]
B=np.array([fp(f['geometry']) for f in bl['features']])
out=[]
for L in np.unique(lab):
  P=pts[lab==L]
  if len(P)<4: continue
  mx,my=P[:,0].mean(),P[:,1].mean()
  # openness and forest ring of the patch (from mnh)
  ring=[mnh[int(YN-(my+dy)),int(mx+dx-X0)]>5 for dx in range(-90,91,6) for dy in range(-90,91,6) if 50<=math.hypot(dx,dy)<=90 and 0<=mx+dx-X0<N]
  lon,lat=Ti.transform(mx,my);d=math.hypot(mx-ox,my-oy);az=math.degrees(math.atan2(mx-ox,my-oy))%360
  db=float(np.min(np.hypot(B[:,0]-mx,B[:,1]-my)))
  out.append(dict(lat=round(lat,6),lon=round(lon,6),d=round(d),az=round(az,1),n_vis=len(P),vis_sommet=int(P[:,2].sum()),vis_pied=int(P[:,3].sum()),foret_autour=round(float(np.mean(ring)),2),bati=round(db)))
out.sort(key=lambda e:-e['n_vis'])
json.dump(out,open('couloir.json','w'))
for e in out[:40]: print(e)
