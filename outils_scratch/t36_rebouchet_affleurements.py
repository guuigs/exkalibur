import json,math,numpy as np
from pyproj import Transformer
from scipy import ndimage
T=Transformer.from_crs(4326,2154,always_xy=True);Ti=Transformer.from_crs(2154,4326,always_xy=True)
mnt=np.load('mnt.npy');mnh=np.clip(np.nan_to_num(np.load('mnh.npy')),0,60);X0,YN=933000,6489000
h=json.load(open('wfs_troncon_hydrographique.json'))
reb=[f for f in h['features'] if f['geometry']['type']=='LineString' and (f['properties'].get('cpx_toponyme_de_cours_d_eau') or '')=='Ruisseau de Rebouchet']
segs=[]
for f in reb:
  cs=f['geometry']['coordinates']
  if cs[0][2]<cs[-1][2]: cs=cs[::-1]
  segs+= list(zip(cs,cs[1:]))
# window around reach
x0,y0=T.transform(6.0405,45.4245);x1,y1=T.transform(6.0465,45.4210)
c0,c1=int(min(x0,x1)-X0),int(max(x0,x1)-X0);r0,r1=int(YN-max(y0,y1)),int(YN-min(y0,y1))
D=mnt[r0:r1,c0:c1].astype(float)
gy,gx=np.gradient(D);slope=np.degrees(np.arctan(np.hypot(gx,gy)))
smooth=ndimage.gaussian_filter(D,8);bump=D-smooth   # local protrusion
def near(x,y):
  best=None
  for a,b in segs:
    dx,dy=b[0]-a[0],b[1]-a[1];L=dx*dx+dy*dy;t=max(0,min(1,((x-a[0])*dx+(y-a[1])*dy)/L)) if L else 0
    px,py=a[0]+t*dx,a[1]+t*dy;d=math.hypot(x-px,y-py);cr=dx*(y-a[1])-dy*(x-a[0])
    if best is None or d<best[0]: best=(d,cr,a[2]+t*(b[2]-a[2]))
  return best
cand=(slope>42)&(bump>0.8)
lab,n=ndimage.label(cand)
out=[]
for i in range(1,n+1):
  ys,xs=np.where(lab==i)
  if len(ys)<4: continue
  cy,cx=ys.mean(),xs.mean();X=X0+c0+cx;Y=YN-(r0+cy)
  d,cr,zs=near(X,Y)
  if d>35: continue
  out.append((len(ys),round(float(bump[lab==i].max()),1),round(d),'gauche' if cr>0 else 'droite',*[round(v,6) for v in Ti.transform(X,Y)[::-1]]))
print('affleurements raides (pente>55°, saillie>1,5 m) à <35 m du Rebouchet : taille(m²) saillie_max dist_ruisseau rive lat lon')
for o in sorted(out,key=lambda o:-o[0])[:15]: print(o)
