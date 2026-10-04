import json,math,subprocess,pickle,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point,LineString
from shapely.ops import unary_union,linemerge
exec(open('ring1068.py').read().split('out=[]')[0])
PUB=unary_union([pickle.load(open('PUB_general.pkl','rb')),shape(json.load(open('cad/noncad.json')))]).buffer(0)
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
f13,f15,f18=F(13),F(15,True),F(18,True)
cr,ccn=3400.49,3955.34;vx,vy=X0+ccn,YN-cr;lo0,la0=Ti.transform(vx,vy);AZ=73.9;S=1850/8
def wms(x0,y0,x1,y1,W,H,fn):
  u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
  for i in range(8):
    subprocess.run(['curl','-sS','-m','120','-o',fn,u])
    try: return Image.open(fn).convert('RGBA')
    except Exception: pass
P=lambda k:T.transform(*G.fwd(lo0,la0,AZ,k*S)[:2])
K=T.transform(6.059095,45.434748)
# carte 1 : la ligne
x0,x1=vx-150,K[0]+700;y0,y1=vy-500,K[1]+400;W=1600;H=int(W*(y1-y0)/(x1-x0))
im=wms(x0,y0,x1,y1,W,H,'oR1.jpg');sc=W/(x1-x0);Q=lambda x,y:((x-x0)*sc,(y1-y)*sc)
dr=ImageDraw.Draw(im)
dr.line([Q(vx,vy),Q(*P(12.6))],fill=(255,210,0,255),width=3)
for k in range(13):
  x,y=P(k);c=Q(x,y);col=(255,60,60,255) if k in (2,10) else (255,255,255,255) if k!=12 else (160,160,160,255)
  r=9 if k in (0,2,10,12) else 5;dr.ellipse([c[0]-r,c[1]-r,c[0]+r,c[1]+r],outline=col,width=3)
  if k in (0,2,10,12): dr.text((c[0]-30,c[1]+12),{0:'1re = muraille',2:'3e (Le Chapela)',10:'11e',12:'13e (ne mène pas au bon endroit)'}[k],fill=col,font=f15)
c=Q(*K);dr.ellipse([c[0]-7,c[1]-7,c[0]+7,c[1]+7],fill=(255,0,255,255));dr.text((c[0]+10,c[1]-26),'croisement du Couvet',fill=(255,0,255,255),font=f15)
dr.rectangle([0,0,W,62],fill=(0,0,0,175));dr.text((10,6),'Hypothèse R — le soleil du 30 avril se lève derrière le Couvet ; rangée : 1re au rempart, 3e→11e = 10 stades',fill=(255,255,255,255),font=f18)
dr.text((10,36),'jaune = direction du lever visible le 30/04 depuis la muraille (73,9°) ; cercles = places de la rangée tous les 231 m (10 stades / 8)',fill=(255,255,255,255),font=f13)
s=Q(x0+40,y0+40);dr.line([s,(s[0]+500*sc,s[1])],fill=(255,255,255,255),width=4);dr.text((s[0],s[1]-22),'500 m',fill=(255,255,255,255),font=f13)
im.convert('RGB').save('t70_carte_R_ligne.jpg',quality=88)
# carte 2 : fin de parcours
segs=[shape(f['geometry']) for f in json.load(open('large/troncon_hydrographique.json'))['features'] if 'Burge' in str(f['properties'].get('cpx_toponyme_de_cours_d_eau'))]
L=linemerge([LineString([c[:2] for c in s.coords]) for s in segs]);L=max(getattr(L,'geoms',[L]),key=lambda l:l.length)
cx,cy=K[0]+120,K[1]-170;h=260;S2=3;W=H=2*h*S2;x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
im=wms(x0,y0,x1,y1,W,H,'oR2.jpg');Q=lambda x,y:((x-x0)*S2,(y1-y)*S2)
ov=Image.new('RGBA',(W,H));dd=ImageDraw.Draw(ov)
from shapely.geometry import box
g_=PUB.intersection(box(x0,y0,x1,y1))
for g in getattr(g_,'geoms',[g_]):
  if g.geom_type=='Polygon': dd.polygon([Q(*c[:2]) for c in g.exterior.coords],fill=(60,255,90,60),outline=(60,255,90,200))
im=Image.alpha_composite(im,ov);dr=ImageDraw.Draw(im)
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]):
    if l.distance(Point(cx,cy))<500: dr.line([Q(*c[:2]) for c in l.coords],fill=(255,255,255,230),width=2)
dr.line([Q(*c[:2]) for c in L.coords],fill=(0,170,255,255),width=3)
s0=L.project(Point(*K));pts=[Q(*L.interpolate(s0-d).coords[0]) for d in range(0,411,5)]
dr.line(pts,fill=(0,255,255,255),width=5)
for bx,by in B:
  if x0<bx<x1 and y0<by<y1: c=Q(bx,by);dr.rectangle([c[0]-3,c[1]-3,c[0]+3,c[1]+3],fill=(255,80,80,255))
c=Q(*K);dr.ellipse([c[0]-10,c[1]-10,c[0]+10,c[1]+10],outline=(255,0,255,255),width=4);dr.text((c[0]+12,c[1]-24),'Couvet (11e)',fill=(255,0,255,255),font=f15)
rk=L.interpolate(s0-405);lo,la=Ti.transform(rk.x,rk.y);c=Q(rk.x,rk.y);dr.ellipse([c[0]-9,c[1]-9,c[0]+9,c[1]+9],fill=(255,140,0,255));dr.text((c[0]+12,c[1]-8),'ressaut de 4-7 m (grande roche ?)',fill=(255,140,0,255),font=f15)
for pas,col in ((0.65,(255,255,255,255)),(0.75,(255,60,60,255))):
  for d in (390,410):
    q=L.interpolate(s0-d);lo,la=Ti.transform(q.x,q.y);l1,a1,_=G.fwd(lo,la,0,10*pas);l1,a1,_=G.fwd(l1,a1,90,10*pas);l2,a2,_=G.fwd(l1,a1,74,8*pas)
    E=Q(*T.transform(l2,a2));dr.line([(E[0]-6,E[1]-6),(E[0]+6,E[1]+6)],fill=col,width=3);dr.line([(E[0]-6,E[1]+6),(E[0]+6,E[1]-6)],fill=col,width=3)
    print('coffre',pas,d,round(a2,6),round(l2,6),PUB.contains(Point(*T.transform(l2,a2))))
dr.rectangle([0,0,W,60],fill=(0,0,0,175));dr.text((10,6),'Hypothèse R — fin de parcours : remonter la Burge (eau à gauche) jusqu au ressaut',fill=(255,255,255,255),font=f18)
dr.text((10,34),'cyan = eau suivie depuis le croisement ; vert = public ; X = coffre (pas 0,65 blanc / 0,75 rouge ; 8 pas vers le lever du 30/04)',fill=(255,255,255,255),font=f13)
s=Q(x0+20,y0+15);dr.line([s,(s[0]+50*S2,s[1])],fill=(255,255,255,255),width=4);dr.text((s[0],s[1]-22),'50 m',fill=(255,255,255,255),font=f13)
im.convert('RGB').save('t70_carte_R_fin.jpg',quality=88)
