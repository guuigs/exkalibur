import json,math,pickle,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,box
from scipy import ndimage
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy')
TX,TY=936955.34,6485599.51
J=T.transform(6.03201,45.43201);cx,cy=J[0],J[1];h=230;S=3;W=2*h*S
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
R0,C0=int(YN-y1),int(x0-X0);n=2*h
Z=mnt[R0:R0+n,C0:C0+n].astype(float);gy,gx=np.gradient(Z);sl=np.arctan(np.hypot(gx,gy));asp=np.arctan2(-gx,gy)
hs=np.clip(255*(np.cos(sl)*np.cos(np.radians(45))+np.sin(sl)*np.sin(np.radians(45))*np.cos(np.radians(315)-asp)),0,255).astype(np.uint8)
im=Image.fromarray(hs).resize((W,W),Image.BICUBIC).convert('RGB');d=ImageDraw.Draw(im,'RGBA')
Q=lambda px,py:((px-x0)*S,(y1-py)*S)
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
# talweg
a2=acc[R0//2:R0//2+n//2,C0//2:C0//2+n//2]*4
yy,xx=np.where(a2>=2000)
for r_,c_ in zip(yy,xx):
    px=(c_*2+1)*S;py=(r_*2+1)*S;d.rectangle([px-3,py-3,px+3,py+3],fill=(0,120,255,160))
# bump (roches)
bump=(mnt-ndimage.gaussian_filter(mnt,2.5)).astype(np.float32)[R0:R0+n,C0:C0+n]
yy,xx=np.where(bump>=0.9)
for r_,c_ in zip(yy[::2],xx[::2]):
    px=c_*S;py=r_*S;d.ellipse([px-2,py-2,px+2,py+2],fill=(255,80,0,200))
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*q[:2]) for q in l.coords],fill=(0,255,255,255),width=2)
for f in json.load(open('wfs_surface_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for p in getattr(g,'geoms',[g]):
    if p.geom_type=='Polygon': d.line([Q(*q[:2]) for q in p.exterior.coords],fill=(0,200,255,255),width=3)
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*q[:2]) for q in l.coords],fill=(255,255,0,255),width=2)
q=Q(*J);d.ellipse([q[0]-12,q[1]-12,q[0]+12,q[1]+12],outline=(255,0,255,255),width=4)
q=Q(TX,TY);d.ellipse([q[0]-10,q[1]-10,q[0]+10,q[1]+10],outline=(0,255,0,255),width=4)
d.rectangle([0,0,W,28],fill=(0,0,0,255));d.text((6,5),'Relief LiDAR ombré : talweg bleu, bosses/roches orange (≥0,9 m), eau cyan, routes jaune ; site magenta, tour verte',fill=(255,255,255,255),font=F(14,True))
im.convert('RGB').save('/home/user/exkalibur/images_travail/t130_pierre_gros_lidar.jpg',quality=88)
