import json,math,subprocess,os,time,pickle,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,box
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51
cx,cy=T.transform(6.0335,45.4272);h=330;S=3;W=2*h*S
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
Q=lambda px,py:((px-x0)*S,(y1-py)*S)
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
for i in range(8):
    if os.path.exists('m1.jpg'): os.remove('m1.jpg')
    subprocess.run(['curl','-sS','-m','120','-o','m1.jpg',u])
    try: im=Image.open('m1.jpg').convert('RGB');break
    except Exception: time.sleep(2)
d=ImageDraw.Draw(im,'RGBA')
PUB2=pickle.load(open('run/PUB2.pkl','rb'));bb=box(x0,y0,x1,y1)
def poly(g,col):
  for p in getattr(g,'geoms',[g]):
    if p.geom_type=='Polygon' and not p.is_empty: d.line([Q(*q[:2]) for q in p.exterior.coords],fill=col,width=3)
poly(PUB2.intersection(bb),(0,255,0,255))
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*q[:2]) for q in l.coords],fill=(0,200,255,255),width=3)
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*q[:2]) for q in l.coords],fill=(255,255,0,255),width=2)
BV=np.load('run/bat_dense.npy')
for bx,by in BV:
  if x0<bx<x1 and y0<by<y1: q=Q(bx,by);d.ellipse([q[0]-2,q[1]-2,q[0]+2,q[1]+2],fill=(255,0,0,255))
n=0
for m in M:
  if m[2]>=3 and x0<m[0]<x1 and y0<m[1]<y1:
    n+=1;q=Q(m[0],m[1]);d.ellipse([q[0]-9,q[1]-9,q[0]+9,q[1]+9],outline=(255,0,255,255),width=3);d.text((q[0]+11,q[1]-9),str(n),fill=(255,0,255,255),font=F(16,True),stroke_width=2,stroke_fill=(0,0,0,255))
    lo,la=Ti.transform(m[0],m[1]);print(n,round(la,5),round(lo,5),'deg',m[2],'dist tour %.0f'%math.hypot(m[0]-TX,m[1]-TY))
q=Q(TX,TY);d.ellipse([q[0]-10,q[1]-10,q[0]+10,q[1]+10],outline=(0,255,0,255),width=4);d.text((q[0]+12,q[1]),'tour',fill=(0,255,0,255),font=F(16,True),stroke_width=2,stroke_fill=(0,0,0,255))
d.rectangle([0,0,W,28],fill=(0,0,0,255));d.text((6,5),'Marais d\'Avalon : public sûr (contour vert), maisons rouge, eau bleu, routes jaune, croisements ≥3 voies magenta',fill=(255,255,255,255),font=F(14,True))
im.convert('RGB').save('/home/user/exkalibur/images_travail/t115_marais_avalon.jpg',quality=88)
