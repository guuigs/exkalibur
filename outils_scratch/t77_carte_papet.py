import json,math,subprocess,pickle,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point
from shapely.ops import unary_union
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vm=np.unpackbits(np.load('vs_muraille.npy'))[:N*N].reshape(N,N).astype(bool)
PUB=unary_union([pickle.load(open('PUB_general.pkl','rb')),shape(json.load(open('cad/noncad.json')))]).buffer(0)
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
f13,f15,f18=F(13),F(15,True),F(18,True)
K=(6.023298,45.412208);cx,cy=T.transform(*K);h=230;S2=3;W=H=2*h*S2
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
im=None
for i in range(8):
  subprocess.run(['curl','-sS','-m','120','-o','oK.jpg',u])
  try: im=Image.open('oK.jpg').convert('RGBA');break
  except Exception: pass
Q=lambda x,y:((x-x0)*S2,(y1-y)*S2)
ov=Image.new('RGBA',(W,H));dd=ImageDraw.Draw(ov)
box=shape({'type':'Polygon','coordinates':[[(x0,y0),(x1,y0),(x1,y1),(x0,y1),(x0,y0)]]})
g_=PUB.intersection(box)
for g in getattr(g_,'geoms',[g_]):
  if g.geom_type=='Polygon': dd.polygon([Q(*c[:2]) for c in g.exterior.coords],fill=(60,255,90,70),outline=(60,255,90,220))
R0,C0=int(YN-y1),int(x0-X0)
a=np.zeros((2*h,2*h,4),np.uint8);a[Vm[R0:R0+2*h,C0:C0+2*h]]=(255,255,0,110)
ov=Image.alpha_composite(ov,Image.fromarray(a).resize((W,H),Image.NEAREST))
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
c=Q(cx,cy);dr.ellipse([c[0]-10,c[1]-10,c[0]+10,c[1]+10],outline=(255,0,255,255),width=4);dr.text((c[0]+12,c[1]+6),'croisement du Papet',fill=(255,0,255,255),font=f15)
tx,ty=T.transform(6.03101275,45.4288723);an=math.atan2(tx-cx,ty-cy)
dr.line([c,(c[0]+math.sin(an)*500,c[1]-math.cos(an)*500)],fill=(255,220,0,255),width=2);dr.text((c[0]+math.sin(an)*500,c[1]-math.cos(an)*500+6),'vers la tour (1,95 km)',fill=(255,220,0,255),font=f13)
dr.rectangle([0,0,W,60],fill=(0,0,0,175));dr.text((10,6),'Le Papet (Pontcharra) — croisement au cap 198° depuis la muraille (somme chimique 197)',fill=(255,255,255,255),font=f18)
dr.text((10,34),'jaune = sol vu depuis le chemin de la muraille ; vert = domaine public ; bleu = eau ; blanc = chemins ; rouge = bâti',fill=(255,255,255,255),font=f13)
s=Q(x0+20,y0+15);dr.line([s,(s[0]+50*S2,s[1])],fill=(255,255,255,255),width=4);dr.text((s[0],s[1]-22),'50 m',fill=(255,255,255,255),font=f13)
im.convert('RGB').save('t77_carte_papet.jpg',quality=88)
