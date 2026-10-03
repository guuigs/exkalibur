import numpy as np,math,json
from PIL import Image
from pyproj import Geod,Transformer
g=Geod(ellps='WGS84');t=Transformer.from_crs(4326,2154,always_xy=True)
im=np.array(Image.open('hist/fa_big.png').convert('RGB')).astype(int)
bb=(45.4100,6.0270,45.4480,6.0820);H_,W_=im.shape[:2]
def cls(la,lo):
  x=int((lo-bb[1])/(bb[3]-bb[1])*W_);y=int((bb[2]-la)/(bb[2]-bb[0])*H_);p=im[y,x]
  if abs(p[0]-69)<6 and abs(p[1]-141)<6: return 'A'   # forêt ancienne
  if abs(p[0]-116)<6 and abs(p[1]-244)<6: return 'R'  # forêt récente
  if p[0]>250 and p[1]>250: return 'N'                # non forêt
  if p[0]>240 and p[1]<120: return 'D'                # magenta
  return '?'
M=np.load('mnt.npy',mmap_mode='r');Hh=np.load('mnh.npy',mmap_mode='r');X0=933000;YN=6489000
DB=np.load('rasters.npz')['d_bld']
def z(x,y): return float(M[int(YN-y),int(x-X0)])
bx,by=t.transform(6.03095,45.42880);zb=z(bx,by)+1.7
def vis(px,py,pz):
  D=math.hypot(px-bx,py-by);w=-1e9
  for f in np.linspace(0.01,0.99,300):
    x=bx+(px-bx)*f;y=by+(py-by)*f;line=zb+(pz-zb)*f-(D*f)*(D*(1-f))/(2*6371000)*0.87;w=max(w,z(x,y)-line)
  return w
T=(45.4288723,6.03101275);out=[]
for az10 in range(400,1401,5):
  az=az10/10
  for R in (1835,1850,1865):
    lo,la,_=g.fwd(T[1],T[0],az,R);c=cls(la,lo)
    if c not in('N','D'): continue
    # annulus 60-150 m
    ring=[cls(*g.fwd(lo,la,a,r)[1::-1]) for a in range(0,360,15) for r in (60,100,150)]
    fa=sum(1 for q in ring if q=='A')/len(ring); fr=sum(1 for q in ring if q in 'AR')/len(ring)
    px,py=t.transform(lo,la);can=float(Hh[int(YN-py),int(px-X0)]);db=float(DB[int((YN-py)/2),int((px-X0)/2)])
    if fr>=0.35 and db>60:
      out.append((az,R,round(la,5),round(lo,5),c,round(fa,2),round(fr,2),round(can,1),round(db),round(vis(px,py,z(px,py)+1.7),1)))
for o in out: print(o)
print(len(out))
