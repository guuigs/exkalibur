import json,math,subprocess,os,time,pickle,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
x,y=T.transform(6.020142,45.419519);rx,ry=x,y
cx_,cy_=(x+rx)/2,(y+ry)/2;h=170;S=5;W=2*h*S
x0,x1,y0,y1=cx_-h,cx_+h,cy_-h,cy_+h
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
def wms(layer,fn):
  u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS={layer}&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
  for i in range(8):
    if os.path.exists(fn): os.remove(fn)
    subprocess.run(['curl','-sS','-m','90','-o',fn,u])
    try: return Image.open(fn).convert('RGB')
    except Exception: time.sleep(2)
Q=lambda px,py:((px-x0)*S,(y1-py)*S)
PUB2=pickle.load(open('run/PUB2.pkl','rb'));PUB3=pickle.load(open('run/PUB3.pkl','rb'))
orth=wms('HR.ORTHOIMAGERY.ORTHOPHOTOS','a0.jpg');d=ImageDraw.Draw(orth,'RGBA')
def poly(g,col):
  for p in getattr(g,'geoms',[g]):
    if p.geom_type!='Polygon' or p.is_empty: continue
    d.polygon([Q(*c[:2]) for c in p.exterior.coords],fill=col)
from shapely.geometry import box
bb=box(x0,y0,x1,y1);poly(PUB3.intersection(bb),(255,160,0,70));poly(PUB2.intersection(bb),(0,255,0,90))
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in l.coords],fill=(0,200,255,255),width=3)
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in l.coords],fill=(255,255,0,255),width=2)
BV=np.load('run/bat_dense.npy')
for bx,by in BV:
  if x0<bx<x1 and y0<by<y1: q=Q(bx,by);d.ellipse([q[0]-2,q[1]-2,q[0]+2,q[1]+2],fill=(255,0,0,255))
q=Q(x,y);d.ellipse([q[0]-14,q[1]-14,q[0]+14,q[1]+14],outline=(255,0,255),width=4)
q=Q(rx,ry);d.ellipse([q[0]-10,q[1]-10,q[0]+10,q[1]+10],outline=(255,255,255),width=4)
for r_ in (100,):
  q=Q(x,y);d.ellipse([q[0]-r_*S,q[1]-r_*S,q[0]+r_*S,q[1]+r_*S],outline=(255,0,0,200),width=2)
d.rectangle([0,0,W,34],fill=(0,0,0,255));d.text((8,6),'A 45.419519, 6.020142 : croisement (magenta) ; public sûr vert, probable orange',fill=(255,255,255),font=F(15,True))
orth.convert('RGB').save('/home/user/exkalibur/images_travail/t113_carte_A.jpg',quality=88)
lo,la=Ti.transform(rx,ry);print('roche',la,lo)
