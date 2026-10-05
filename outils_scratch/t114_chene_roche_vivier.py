import json,gzip,math,subprocess,os,time,pickle,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point,box
from shapely.ops import transform as stf
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51
ld=json.load(gzip.open('ld.json.gz'))
LD=[(f['properties']['nom'],stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0)) for f in ld['features']]
G1=[g for n,g in LD if n.startswith('LE CHENE')][0]
c=G1.centroid;print('centroïde',Ti.transform(c.x,c.y)[::-1],'aire %.0f m2'%G1.area,'bounds',[round(v) for v in G1.bounds],'dist tour %.0f'%c.distance(Point(TX,TY)))
for n,g in LD:
    if g.distance(G1)<1 and n!=G1 : print('voisin',n)
h=500;S=4;W=2*h*S;x0,x1,y0,y1=c.x-h,c.x+h,c.y-h,c.y+h
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
for i in range(8):
    if os.path.exists('c0.jpg'): os.remove('c0.jpg')
    subprocess.run(['curl','-sS','-m','120','-o','c0.jpg',u])
    try: im=Image.open('c0.jpg').convert('RGB');break
    except Exception: time.sleep(2)
d=ImageDraw.Draw(im,'RGBA');Q=lambda px,py:((px-x0)*S,(y1-py)*S)
PUB2=pickle.load(open('run/PUB2.pkl','rb'));PUB3=pickle.load(open('run/PUB3.pkl','rb'));bb=box(x0,y0,x1,y1)
def poly(g,col):
  for p in getattr(g,'geoms',[g]):
    if p.geom_type=='Polygon' and not p.is_empty: d.polygon([Q(*q[:2]) for q in p.exterior.coords],fill=col)
poly(PUB3.intersection(bb),(255,160,0,60));poly(PUB2.intersection(bb),(0,255,0,80))
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*q[:2]) for q in l.coords],fill=(0,200,255,255),width=3)
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*q[:2]) for q in l.coords],fill=(255,255,0,255),width=2)
BV=np.load('run/bat_dense.npy')
for bx,by in BV:
  if x0<bx<x1 and y0<by<y1: q=Q(bx,by);d.ellipse([q[0]-2,q[1]-2,q[0]+2,q[1]+2],fill=(255,0,0,255))
for p in getattr(G1,'geoms',[G1]): d.line([Q(*q[:2]) for q in p.exterior.coords],fill=(255,0,255,255),width=4)
q=Q(TX,TY);d.ellipse([q[0]-10,q[1]-10,q[0]+10,q[1]+10],outline=(0,255,0,255),width=4)
d.rectangle([0,0,W,32],fill=(0,0,0,255));d.text((8,6),'Lieu-dit LE CHENE LA ROCHE ET LE VIVIER (magenta) ; tour (vert) ; public sûr vert / probable orange ; maisons rouge ; eau bleu',fill=(255,255,255,255),font=F(15,True))
im.convert('RGB').save('/home/user/exkalibur/images_travail/t114_chene_roche_vivier.jpg',quality=88)
