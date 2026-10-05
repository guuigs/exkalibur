import json,math,subprocess,os,time,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy')
cx,cy=T.transform(6.03265,45.42775);h=120;S=8;W=2*h*S
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
Q=lambda px,py:((px-x0)*S,(y1-py)*S)
F=lambda s:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',s)
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
for i in range(8):
    if os.path.exists('z0.jpg'): os.remove('z0.jpg')
    subprocess.run(['curl','-sS','-m','120','-o','z0.jpg',u])
    try: im=Image.open('z0.jpg').convert('RGB');break
    except Exception: time.sleep(2)
d=ImageDraw.Draw(im,'RGBA')
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in l.coords],fill=(255,255,0,200),width=3)
for f in json.load(open('wfs_surface_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for p in getattr(g,'geoms',[g]):
    if p.geom_type=='Polygon': d.line([Q(*c[:2]) for c in p.exterior.coords],fill=(0,200,255,255),width=3)
J=Q(*T.transform(6.0320,45.42684));d.ellipse([J[0]-14,J[1]-14,J[0]+14,J[1]+14],outline=(255,0,255,255),width=4);d.text((J[0]+16,J[1]-10),'J16',fill=(255,0,255,255),font=F(22))
d.rectangle([0,0,W,30],fill=(0,0,0,255));d.text((8,5),'Zoom 240 m : route NE (53°) de J16 le long du marais ; routes jaune, retenue cyan',fill=(255,255,255,255),font=F(16))
im.save('/home/user/exkalibur/images_travail/t140_zoom_marais.jpg',quality=90)
# relief local
R0,C0=int(YN-y1),int(x0-X0);n=2*h
Z=mnt[R0:R0+n,C0:C0+n].astype(float);gy,gx=np.gradient(Z);sl=np.arctan(np.hypot(gx,gy));asp=np.arctan2(-gx,gy)
hs=np.clip(255*(np.cos(sl)*np.cos(np.radians(45))+np.sin(sl)*np.sin(np.radians(45))*np.cos(np.radians(315)-asp)),0,255).astype(np.uint8)
im2=Image.fromarray(hs).resize((W,W),Image.BICUBIC).convert('RGB');d2=ImageDraw.Draw(im2,'RGBA')
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d2.line([Q(*c[:2]) for c in l.coords],fill=(255,200,0,200),width=2)
d2.ellipse([J[0]-14,J[1]-14,J[0]+14,J[1]+14],outline=(255,0,255,255),width=4)
im2.save('/home/user/exkalibur/images_travail/t140_zoom_marais_lidar.jpg',quality=90)
print('ok',float(Z.min()),float(Z.max()))
