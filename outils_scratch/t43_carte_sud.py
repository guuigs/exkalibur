import json,math,subprocess,numpy as np
from PIL import Image,ImageDraw
from shapely.geometry import shape
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
px,py=T.transform(6.03115,45.42887)
x0,x1,y0,y1=px-350,px+450,py-700,py+100
W=int(x1-x0);Hh=int(y1-y0)
lo0,la0=Ti.transform(x0,y0);lo1,la1=Ti.transform(x1,y1)
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={Hh}&FORMAT=image/jpeg"
for i in range(4):
  r=subprocess.run(['curl','-sS','-m','120','-o','ortho_sud.jpg',u])
  if r.returncode==0: break
im=Image.open('ortho_sud.jpg').convert('RGB').resize((W,Hh))
ov=Image.new('RGBA',(W,Hh),(0,0,0,0));d=ImageDraw.Draw(ov)
R0,C0=int(YN-y1),int(x0-X0);V=Vp[R0:R0+Hh,C0:C0+W]
a=np.zeros((Hh,W,4),np.uint8);a[V]=(255,255,0,90);ov=Image.alpha_composite(ov,Image.fromarray(a));d=ImageDraw.Draw(ov)
P=lambda x,y:(x-x0,y1-y)
for f in json.load(open('wfs_troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': d.line([P(*c[:2]) for c in g.coords],fill=(0,160,255,255),width=3)
for f in json.load(open('wfs_surface_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for gg in getattr(g,'geoms',[g]):
    if gg.geom_type=='Polygon': d.polygon([P(*c[:2]) for c in gg.exterior.coords],outline=(0,90,255,255))
for f in json.load(open('wfs_troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': d.line([P(*c[:2]) for c in g.coords],fill=(255,255,255,170),width=1)
for m in M:
  if x0<m[0]<x1 and y0<m[1]<y1:
    q=P(m[0],m[1]);d.ellipse([q[0]-5,q[1]-5,q[0]+5,q[1]+5],outline=(255,0,0,255),width=2)
for bx,by in B:
  if x0<bx<x1 and y0<by<y1: q=P(bx,by);d.rectangle([q[0]-1,q[1]-1,q[0]+1,q[1]+1],fill=(255,0,255,255))
q=P(px,py);d.ellipse([q[0]-7,q[1]-7,q[0]+7,q[1]+7],fill=(255,0,0,255))
for nm,la,lo in (('JS1',45.426839,6.031995),('JS2',45.424634,6.031943),('Vivier',45.42844,6.03290)):
  xx,yy=T.transform(lo,la);q=P(xx,yy);d.text((q[0]+8,q[1]-6),nm,fill=(255,255,255,255))
d.line([(20,Hh-20),(120,Hh-20)],fill=(255,255,255,255),width=3);d.text((20,Hh-35),'100 m',fill=(255,255,255,255))
Image.alpha_composite(im.convert('RGBA'),ov).convert('RGB').save('t43_secteur_sud.jpg',quality=88)
print(W,Hh)
