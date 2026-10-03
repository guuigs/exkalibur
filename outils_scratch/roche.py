import numpy as np,json,math
from scipy.ndimage import gaussian_filter
from PIL import Image,ImageDraw,ImageFont
from pyproj import Transformer
t=Transformer.from_crs(4326,2154,always_xy=True);ti=Transformer.from_crs(2154,4326,always_xy=True)
M=np.load('mnt.npy',mmap_mode='r');H=np.load('mnh.npy',mmap_mode='r');X0=933000;YN=6489000
cx,cy=t.transform(6.04656,45.43577);R=110;S=7
c0=int(cx-X0)-R;r0=int(YN-cy)-R
z=np.array(M[r0:r0+2*R,c0:c0+2*R],float);h=np.array(H[r0:r0+2*R,c0:c0+2*R],float)
gy,gx=np.gradient(z);slope=np.degrees(np.arctan(np.hypot(gx,gy)))
lrm=z-gaussian_filter(z,6)
# hillshade
az,alt=math.radians(315),math.radians(40);asp=np.arctan2(-gx,gy);sl=np.arctan(np.hypot(gx,gy))
hs=np.sin(alt)*np.cos(sl)+np.cos(alt)*np.sin(sl)*np.cos(az-asp);hs=np.clip(hs*255,0,255).astype(np.uint8)
rgb=np.stack([hs,hs,hs],-1).astype(float)
rgb[slope>45]=rgb[slope>45]*0.5+np.array([200,60,60])*0.5   # parois raides en rouge
rgb[(lrm>1.2)&(slope<60)]=[255,200,0]                         # bosses (blocs) en jaune
im=Image.fromarray(rgb.astype(np.uint8)).resize((2*R*S,2*R*S),Image.NEAREST);D=ImageDraw.Draw(im)
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',20)
def P(lo,la): x,y=t.transform(lo,la);return ((x-X0-c0)*S,(YN-y-r0)*S)
O=json.load(open('osm.json'))
for wid,nds,tg in O['ways']:
  if 'highway' in tg or tg.get('waterway'):
    pts=[O['nodes'][n] for n in nds if n in O['nodes']];pp=[P(p[1],p[0]) for p in pts]
    if any(0<x<2*R*S and 0<y<2*R*S for x,y in pp): D.line(pp,fill=(0,140,255) if tg.get('waterway') else (255,0,255),width=4)
hyd=json.load(open('wfs_troncon_hydrographique.json'))
for f in hyd['features']:
  gm=f['geometry'];cs=gm['coordinates'] if gm['type']=='LineString' else [c for l in gm['coordinates'] for c in l]
  pp=[((x-X0-c0)*S,(YN-y-r0)*S) for x,y,*_ in cs]
  if any(0<x<2*R*S and 0<y<2*R*S for x,y in pp): D.line(pp,fill=(0,220,255),width=3)
for k,(la,lo) in {'prise d eau (OSM)':(45.43577,6.04656),'chute 52%':(45.43555,6.04651)}.items():
  x,y=P(lo,la);D.ellipse((x-10,y-10,x+10,y+10),outline=(0,255,0),width=4);D.text((x+12,y-12),k,fill=(255,255,255),font=F,stroke_width=3,stroke_fill=(0,0,0))
D.line((20,2*R*S-20,20+10*S,2*R*S-20),fill=(255,255,255),width=5);D.text((20,2*R*S-46),'10 m',fill=(255,255,255),font=F,stroke_width=3,stroke_fill=(0,0,0))
im.save('C/roche_lidar.jpg',quality=90)
# list prominent rock blobs: high lrm & steep, near stream end
from scipy import ndimage
mask=(lrm>1.5)|(slope>55)
lab,n=ndimage.label(mask)
res=[]
for i in range(1,n+1):
  ys,xs=np.where(lab==i)
  if len(ys)<12: continue
  yc,xc=ys.mean(),xs.mean();x=X0+c0+xc;y=YN-(r0+yc);lo,la=ti.transform(x,y)
  d=math.hypot(x-cx,y-cy);res.append((round(d),len(ys),round(float(lrm[ys,xs].max()),1),round(float(slope[ys,xs].mean())),round(float(z[ys,xs].max()-z[ys,xs].min()),1),round(float(h[ys,xs].mean()),1),round(la,6),round(lo,6)))
for r_ in sorted(res)[:15]: print('dist',r_[0],'m surf',r_[1],'m2 bosse max',r_[2],'m pente',r_[3],'° denivele',r_[4],'m canopee',r_[5],'->',r_[6],r_[7])
