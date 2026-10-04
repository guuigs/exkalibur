import json,math,subprocess,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy');fd=np.load('fdir.npy')
mv={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0][:1] in '1234'])
FP=unary_union([shape(f['geometry']) for f in json.load(open('wfs_foret_publique.json'))['features']])
PUB=unary_union([NC,PU,FP]).buffer(0)
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
f13,f15,f18=F(13),F(15,True),F(18,True)
J5=T.transform(6.054780,45.426948)
cx,cy=J5[0]+80,J5[1]+20;h=230;S2=3;W=H=2*h*S2
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
for i in range(6):
  subprocess.run(['curl','-sS','-m','120','-o','oQ.jpg',u])
  try: im=Image.open('oQ.jpg').convert('RGBA');break
  except Exception: pass
Q=lambda x,y:((x-x0)*S2,(y1-y)*S2)
ov=Image.new('RGBA',(W,H));dd=ImageDraw.Draw(ov)
box=shape({'type':'Polygon','coordinates':[[(x0,y0),(x1,y0),(x1,y1),(x0,y1),(x0,y0)]]})
g_=PUB.intersection(box)
for g in getattr(g_,'geoms',[g_]):
  if g.geom_type=='Polygon': dd.polygon([Q(*c[:2]) for c in g.exterior.coords],fill=(60,255,90,85),outline=(60,255,90,220))
im=Image.alpha_composite(im,ov);dr=ImageDraw.Draw(im)
for f in json.load(open('wfs_troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': dr.line([Q(*c[:2]) for c in g.coords],fill=(0,170,255,255),width=3)
for f in json.load(open('wfs_troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': dr.line([Q(*c[:2]) for c in g.coords],fill=(255,255,255,230),width=2)
for bx,by in B:
  if x0<bx<x1 and y0<by<y1: c=Q(bx,by);dr.rectangle([c[0]-3,c[1]-3,c[0]+3,c[1]+3],fill=(255,80,80,255))
# talweg de J5
r0,c0=int((YN-J5[1])/2),int((J5[0]-X0)/2);w=acc[r0-10:r0+11,c0-10:c0+11];ys,xs=np.where(w>1500);k=np.argmin(np.hypot(ys-10,xs-10));r,c=r0-10+ys[k],c0-10+xs[k]
pts=[];L=0
while L<150:
  pts.append(Q(X0+c*2+1,YN-r*2-1));d2=mv.get(int(fd[r,c]))
  if d2 is None: break
  r+=d2[0];c+=d2[1];L+=2*(1.414 if d2[0] and d2[1] else 1)
dr.line(pts,fill=(0,255,255,255),width=4)
for p in pts[::8]: dr.polygon([(p[0]-4,p[1]-4),(p[0]+4,p[1]-4),(p[0],p[1]+4)],fill=(0,255,255,255))
# axe Machrie + point 1850
for o,col,t in ((95.78,(255,80,80,255),'axe Machrie 3→11 (95,78°)'),(91.4,(255,220,0,255),'aube de Pâques 1524 (91,4°)'),(93.0,(255,170,0,255),'aube de Pâques 2026 (93,0°)')):
  a=Q(*T.transform(*G.fwd(6.03115,45.42887,o,1600)[:2]));b=Q(*T.transform(*G.fwd(6.03115,45.42887,o,2100)[:2]))
  dr.line([a,b],fill=col,width=2);p=Q(*T.transform(*G.fwd(6.03115,45.42887,o,1850)[:2]));dr.ellipse([p[0]-9,p[1]-9,p[0]+9,p[1]+9],outline=col,width=3)
  dr.text((p[0]-300,p[1]+(-26 if o<92 else -22 if o<94 else 12)),t+' — 10 stades',fill=col,font=f13)
c=Q(*J5);dr.ellipse([c[0]-10,c[1]-10,c[0]+10,c[1]+10],outline=(255,0,255,255),width=4);dr.text((c[0]+12,c[1]+8),'J5 : croisement à 5 voies, clairière',fill=(255,0,255,255),font=f15)
rock=(6.055680,45.427909);rk=Q(*T.transform(*rock));dr.ellipse([rk[0]-9,rk[1]-9,rk[0]+9,rk[1]+9],fill=(255,140,0,255));dr.text((rk[0]-245,rk[1]+12),'grande roche ? (+2,4 m)',fill=(255,140,0,255),font=f15)
for pas,col in ((0.65,(255,255,255,255)),(0.75,(255,60,60,255))):
  lo,la,_=G.fwd(*rock,0,10*pas);s1=Q(*T.transform(lo,la));lo,la,_=G.fwd(lo,la,90,10*pas);s2=Q(*T.transform(lo,la))
  dr.line([rk,s1,s2],fill=col,width=2)
  for jd in (67.7,91.4,93):
    e=T.transform(*G.fwd(lo,la,jd,8*pas)[:2]);E=Q(*e);dr.line([s2,E],fill=col,width=1);dr.line([(E[0]-6,E[1]-6),(E[0]+6,E[1]+6)],fill=col,width=3);dr.line([(E[0]-6,E[1]+6),(E[0]+6,E[1]-6)],fill=col,width=3)
    print(pas,jd,Ti.transform(*e)[::-1],PUB.contains(Point(*e)))
dr.text((rk[0]+14,rk[1]-6),'souche → coffre (X)',fill=(255,255,255,255),font=f13)
dr.rectangle([0,0,W,60],fill=(0,0,0,175));dr.text((10,6),'Hypothèse Q — J5 et le ravin du Tapon (chemin de pensée)',fill=(255,255,255,255),font=f18)
dr.text((10,34),'vert = domaine public ; cyan = eau qui part de J5 (vers le Tapon) ; blanc = chemins ; rouge = maisons ; X = coffre (pas 0,65 blanc / 0,75 rouge)',fill=(255,255,255,255),font=f13)
s=Q(x0+20,y0+15);dr.line([s,(s[0]+50*S2,s[1])],fill=(255,255,255,255),width=4);dr.text((s[0],s[1]-22),'50 m',fill=(255,255,255,255),font=f13)
im.convert('RGB').save('t54_carte_Q.jpg',quality=88)
