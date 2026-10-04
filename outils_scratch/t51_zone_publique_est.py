import json,math,subprocess,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
Vs=np.unpackbits(np.load('vs_sommet.npy'))[:N*N].reshape(N,N).astype(bool)
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0][:1] in '1234'])
FP=unary_union([shape(f['geometry']) for f in json.load(open('wfs_foret_publique.json'))['features']])
PUBL=unary_union([PU,FP])
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
f13,f15,f18=F(13),F(15,True),F(18,True)
px,py=T.transform(6.03115,45.42887)
cx,cy=T.transform(*G.fwd(6.03115,45.42887,93,1850)[:2]);h=450;S2=2;W=H=2*h*S2
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
for i in range(6):
  subprocess.run(['curl','-sS','-m','120','-o','oE.jpg',u])
  try: im=Image.open('oE.jpg').convert('RGBA');break
  except Exception: pass
Q=lambda x,y:((x-x0)*S2,(y1-y)*S2)
ov=Image.new('RGBA',(W,H));dd=ImageDraw.Draw(ov)
box=shape({'type':'Polygon','coordinates':[[(x0,y0),(x1,y0),(x1,y1),(x0,y1),(x0,y0)]]})
for G_,col in ((PUBL.intersection(box),(60,255,90,70)),(NC.intersection(box),(60,255,90,120))):
  for g in getattr(G_,'geoms',[G_]):
    if g.geom_type=='Polygon': dd.polygon([Q(*c[:2]) for c in g.exterior.coords],fill=col,outline=(60,255,90,200))
R0,C0=int(YN-y1),int(x0-X0)
a=np.zeros((2*h,2*h,4),np.uint8);a[Vs[R0:R0+2*h,C0:C0+2*h]]=(80,160,255,70);a[Vp[R0:R0+2*h,C0:C0+2*h]]=(255,255,0,120)
ov=Image.alpha_composite(ov,Image.fromarray(a).resize((W,H),Image.NEAREST))
im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
for f in json.load(open('wfs_troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': d.line([Q(*c[:2]) for c in g.coords],fill=(0,170,255,255),width=3)
for f in json.load(open('wfs_troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': d.line([Q(*c[:2]) for c in g.coords],fill=(255,255,255,220),width=2)
for m in M:
  if x0<m[0]<x1 and y0<m[1]<y1: c=Q(m[0],m[1]);d.ellipse([c[0]-5,c[1]-5,c[0]+5,c[1]+5],outline=(255,0,255,255),width=2)
for bx,by in B:
  if x0<bx<x1 and y0<by<y1: c=Q(bx,by);d.rectangle([c[0]-2,c[1]-2,c[0]+2,c[1]+2],fill=(255,80,80,255))
for o,col,t in ((91.4,(255,220,0,255),'Pâques 1524'),(93.0,(255,170,0,255),'Pâques 2026'),(95.78,(255,80,80,255),'axe Machrie 3→11')):
  e=Q(*T.transform(*G.fwd(6.03115,45.42887,o,2400)[:2]));s_=Q(*T.transform(*G.fwd(6.03115,45.42887,o,1300)[:2]))
  d.line([s_,e],fill=col,width=2);p=Q(*T.transform(*G.fwd(6.03115,45.42887,o,1850)[:2]));d.ellipse([p[0]-8,p[1]-8,p[0]+8,p[1]+8],outline=col,width=3)
  d.text((p[0]+10,p[1]+(-22 if o<92 else 6 if o<94 else 22)),f'1 850 m — {t}',fill=col,font=f13)
J5=Q(*T.transform(6.054780,45.426948));d.text((J5[0]+8,J5[1]+6),'J5',fill=(255,0,255,255),font=f15)
gue=Q(*T.transform(6.05785,45.42547));d.text((gue[0]+8,gue[1]),'gué du Tapon',fill=(0,220,255,255),font=f15)
d.rectangle([0,0,W,58],fill=(0,0,0,170));d.text((10,6),'Secteur est à ~10 stades : domaine public et visibilité',fill=(255,255,255,255),font=f18)
d.text((10,34),'vert = public (forêts communales, parcelles communales, bandes) ; jaune = vu du pied ; bleu clair = vu du sommet ; violet = croisements',fill=(255,255,255,255),font=f13)
d.line([(20,H-25),(220,H-25)],fill=(255,255,255,255),width=4);d.text((20,H-48),'100 m',fill=(255,255,255,255),font=f13)
im.convert('RGB').save('t51_zone_est.jpg',quality=88)
