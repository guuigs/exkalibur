import json,math,subprocess,gzip,csv,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
pm={}
for r in csv.reader(open('cad/pm_73141.csv',encoding='latin-1'),delimiter=';'):
  pm[(r[5].strip(),r[6].strip().zfill(4))]=(r[20],r[23])
d=json.load(gzip.open('cad/73141-parcelles.json.gz'))
pubL=[];
for f in d['features']:
  p=f['properties'];k=(p['section'].strip('0') if False else p['section'],p['numero'].zfill(4))
  o=pm.get((p['section'].lstrip('0') or p['section'],p['numero'].zfill(4))) or pm.get((p['section'],p['numero'].zfill(4)))
  if o and o[0][:1] in '1234': pubL.append(stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0))
print('parcelles publiques Laissaud',len(pubL))
FP=unary_union([shape(f['geometry']) for f in json.load(open('wfs_foret_publique.json'))['features']])
PUB=unary_union(pubL+[FP])
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
f13,f15,f18=F(13),F(15,True),F(18,True)
cx,cy=T.transform(6.026558,45.447665);h=250;S2=3;W=H=2*h*S2
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
for i in range(6):
  subprocess.run(['curl','-sS','-m','120','-o','oN.jpg',u])
  try: im=Image.open('oN.jpg').convert('RGBA');break
  except Exception: pass
Q=lambda x,y:((x-x0)*S2,(y1-y)*S2)
ov=Image.new('RGBA',(W,H));dd=ImageDraw.Draw(ov)
box=shape({'type':'Polygon','coordinates':[[(x0,y0),(x1,y0),(x1,y1),(x0,y1),(x0,y0)]]})
g_=PUB.intersection(box)
for g in getattr(g_,'geoms',[g_]):
  if g.geom_type=='Polygon': dd.polygon([Q(*c[:2]) for c in g.exterior.coords],fill=(60,255,90,70),outline=(60,255,90,220))
im=Image.alpha_composite(im,ov);dr=ImageDraw.Draw(im)
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): dr.line([Q(*c[:2]) for c in l.coords],fill=(0,170,255,255),width=3)
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]):
    if l.distance(Point(cx,cy))<400: dr.line([Q(*c[:2]) for c in l.coords],fill=(255,255,255,230),width=2)
for bx,by in B:
  if x0<bx<x1 and y0<by<y1: c=Q(bx,by);dr.rectangle([c[0]-3,c[1]-3,c[0]+3,c[1]+3],fill=(255,80,80,255))
for lo,la,t in ((6.026558,45.447665,'N : croisement 4 voies'),(6.026721,45.447584,'')):
  c=Q(*T.transform(lo,la));dr.ellipse([c[0]-10,c[1]-10,c[0]+10,c[1]+10],outline=(255,0,255,255),width=4);dr.text((c[0]+12,c[1]-24),t,fill=(255,0,255,255),font=f15)
# direction de la tour
tx,ty=T.transform(6.03101275,45.4288723);a=math.atan2(tx-cx,ty-cy);c=Q(cx,cy)
dr.line([c,(c[0]+math.sin(a)*400,c[1]-math.cos(a)*400)],fill=(255,220,0,255),width=2);dr.text((c[0]+math.sin(a)*400-60,c[1]-math.cos(a)*400-20),'vers la tour (2,1 km)',fill=(255,220,0,255),font=f13)
dr.rectangle([0,0,W,60],fill=(0,0,0,175));dr.text((10,6),'Option N — croisement du Coisetan (Laissaud, limite Isère/Savoie), vu du sommet de la tour',fill=(255,255,255,255),font=f18)
dr.text((10,34),'vert = public (forêt communale de Saint-Maximin, parcelles des communes de Pontcharra / Saint-Maximin / Laissaud) ; bleu = eau ; rouge = bâti',fill=(255,255,255,255),font=f13)
s=Q(x0+20,y0+15);dr.line([s,(s[0]+50*S2,s[1])],fill=(255,255,255,255),width=4);dr.text((s[0],s[1]-22),'50 m',fill=(255,255,255,255),font=f13)
im.convert('RGB').save('t58_carte_N.jpg',quality=88)
