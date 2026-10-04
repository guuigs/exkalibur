import json,math,subprocess,pickle,numpy as np,time
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point,LineString
from shapely.ops import unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
def wms(x0,y0,x1,y1,W,H,layer='HR.ORTHOIMAGERY.ORTHOPHOTOS'):
  u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS={layer}&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
  for i in range(8):
    subprocess.run(['curl','-sS','-m','120','-o','w.jpg',u])
    try: return Image.open('w.jpg').convert('RGBA')
    except Exception: time.sleep(2)
cr,ccn=3400.49,3955.34;TX,TY=X0+ccn,YN-cr;lo0,la0=Ti.transform(TX,TY)
J=T.transform(6.040299,45.422426);SRC=T.transform(6.04019,45.42177);PONT=T.transform(6.038836,45.426236)
ROCK=(6.040030,45.422117);RK=T.transform(*ROCK)
# ---------- A : vue d'ensemble ----------
x0,x1,y0,y1=TX-1250,TX+1350,TY-1250,TY+1250;W=1500;H=int(W*(y1-y0)/(x1-x0));s=W/(x1-x0)
im=wms(x0,y0,x1,y1,W,H);Q=lambda x,y:((x-x0)*s,(y1-y)*s);d=ImageDraw.Draw(im)
c=Q(TX,TY);r=1068*s;d.ellipse([c[0]-r,c[1]-r,c[0]+r,c[1]+r],outline=(255,255,255,200),width=2)
for O,col,lab in ((90.1,(120,220,255,255),'Pâques 2023'),(91.3,(255,220,0,255),'Pâques 1524'),(92.9,(255,150,0,255),'Pâques 2026')):
  e=Q(*T.transform(*G.fwd(lo0,la0,O,1250)[:2]));d.line([c,e],fill=col,width=2)
O=92.9;f15=F(15,True);f13=F(13)
for k in range(1,13):
  p=Q(*T.transform(*G.fwd(lo0,la0,(O-(k-0.5)*30)%360,1068)[:2]));col=(255,60,60,255) if k in (3,11) else (255,255,255,255)
  d.ellipse([p[0]-7,p[1]-7,p[0]+7,p[1]+7],fill=col);d.text((p[0]+9,p[1]-8),{3:'3 Jacques',11:'11 Simon'}.get(k,str(k)),fill=col,font=f15 if k in (3,11) else f13)
p=Q(*T.transform(*G.fwd(lo0,la0,O,1068)[:2]));d.ellipse([p[0]-8,p[1]-8,p[0]+8,p[1]+8],fill=(255,215,0,255));d.text((p[0]+10,p[1]-22),'Christ (13e) à l\'Orient = aube de Pâques',fill=(255,215,0,255),font=f15)
s3=Q(*T.transform(*G.fwd(lo0,la0,(O-2.5*30)%360,1068)[:2]));s11=Q(*T.transform(*G.fwd(lo0,la0,(O-10.5*30)%360,1068)[:2]))
d.line([s3,s11],fill=(255,60,60,255),width=3);d.text(((s3[0]+s11[0])/2+8,(s3[1]+s11[1])/2-10),'10 stades (1 850 m)',fill=(255,60,60,255),font=f15)
for (x,y),lab,col in ((PONT,'pont du Rebouchet (seul ruisseau vu du rempart)',(0,200,255,255)),(J,'jonction du Mouret',(255,0,255,255)),(SRC,'source',(0,255,200,255))):
  q=Q(x,y);d.ellipse([q[0]-7,q[1]-7,q[0]+7,q[1]+7],outline=col,width=3);d.text((q[0]+10,q[1]+(4 if 'source' in lab else -18)),lab,fill=col,font=f15)
d.ellipse([c[0]-8,c[1]-8,c[0]+8,c[1]+8],fill=(255,255,255,255));d.text((c[0]-120,c[1]+10),'tour d\'Avalon (muraille)',fill=(255,255,255,255),font=f15)
d.rectangle([0,0,W,58],fill=(0,0,0,180));d.text((10,6),'Schéma 1 — La Table de la Cène posée sur le rempart, orientée sur l\'aube de Pâques',fill=(255,255,255,255),font=F(18,True))
d.text((10,34),'cercle = table de rayon 1 068 m ; places à 30° ; numérotation depuis la droite du Christ (Mt 10) ; corde rouge = 3e → 11e',fill=(255,255,255,255),font=f13)
im.convert('RGB').save('t88_schema1_table.jpg',quality=88)
# ---------- B : zoom fin de parcours ----------
D=pickle.load(open('run/mouret_cad.pkl','rb'));NC=pickle.load(open('run/mouret_nc.pkl','rb'))
cx,cy=(J[0]+SRC[0])/2,(J[1]+SRC[1])/2+5;h=75;S2=8;W=H=2*h*S2;x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
im=wms(x0,y0,x1,y1,W,H);Q=lambda x,y:((x-x0)*S2,(y1-y)*S2)
ov=Image.new('RGBA',(W,H));dd=ImageDraw.Draw(ov)
for pid,g,o in D['P']:
  for gg in getattr(g,'geoms',[g]):
    if gg.geom_type=='Polygon': dd.polygon([Q(*c[:2]) for c in gg.exterior.coords],outline=(255,255,255,170))
for g in NC:
  for gg in getattr(g,'geoms',[g]):
    if gg.geom_type=='Polygon': dd.polygon([Q(*c[:2]) for c in gg.exterior.coords],fill=(60,255,90,110),outline=(60,255,90,255))
im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
for g,n,c in D['rd']:
  for l in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in l.coords],fill=(255,255,255,255),width=3)
acc=np.load('acc.npy');fdir=np.load('fdir.npy')
mv={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
def flow(x,y,L):
  r,c=int((YN-y)/2),int((x-X0)/2);pts=[];dd_=0
  while dd_<L:
    pts.append((X0+c*2+1,YN-r*2-1));m=mv.get(int(fdir[r,c]))
    if not m: break
    r+=m[0];c+=m[1];dd_+=2
  return pts
w=flow(*SRC,120);d.line([Q(*p) for p in w],fill=(0,200,255,255),width=5)
for p in w[::8][1:]:
  q=Q(*p);d.ellipse([q[0]-4,q[1]-4,q[0]+4,q[1]+4],fill=(0,200,255,255))
f16=F(16,True);f13=F(14)
q=Q(*J);d.ellipse([q[0]-12,q[1]-12,q[0]+12,q[1]+12],outline=(255,0,255,255),width=5);d.text((q[0]+14,q[1]-10),'JONCTION (clairière)',fill=(255,0,255,255),font=f16)
q=Q(*SRC);d.ellipse([q[0]-10,q[1]-10,q[0]+10,q[1]+10],outline=(0,255,200,255),width=4);d.text((q[0]+12,q[1]),'source (roche-source, coffre en privé)',fill=(0,255,200,255),font=f13)
q=Q(*RK);d.ellipse([q[0]-11,q[1]-11,q[0]+11,q[1]+11],fill=(255,140,0,255));d.text((q[0]-235,q[1]-8),'GRANDE ROCHE ? (≈40 m)',fill=(255,140,0,255),font=f16)
lo,la=ROCK;pas=0.75
l1,a1,_=G.fwd(lo,la,0,10*pas);n1=Q(*T.transform(l1,a1));l2,a2,_=G.fwd(l1,a1,90,10*pas);n2=Q(*T.transform(l2,a2))
d.line([Q(*RK),n1],fill=(255,255,0,255),width=4);d.line([n1,n2],fill=(255,255,0,255),width=4)
d.text((n1[0]-120,n1[1]-22),'10 pas N',fill=(255,255,0,255),font=f13);d.text(((n1[0]+n2[0])/2-30,n1[1]-24),'10 pas E',fill=(255,255,0,255),font=f13)
d.ellipse([n2[0]-9,n2[1]-9,n2[0]+9,n2[1]+9],fill=(140,90,40,255),outline=(255,255,255,255));d.text((n2[0]-10,n2[1]+10),'souche-majesté',fill=(255,255,255,255),font=f13)
for jd in (67.7,90.0,93.0):
  l3,a3,_=G.fwd(l2,a2,jd,8*pas);e=Q(*T.transform(l3,a3));d.line([n2,e],fill=(255,60,60,255),width=3)
d.line([(e[0]-9,e[1]-9),(e[0]+9,e[1]+9)],fill=(255,0,0,255),width=5);d.line([(e[0]-9,e[1]+9),(e[0]+9,e[1]-9)],fill=(255,0,0,255),width=5)
d.text((e[0]+12,e[1]-8),'COFFRE (8 pas vers le jour dernier)',fill=(255,80,80,255),font=f16)
d.rectangle([0,0,W,60],fill=(0,0,0,185));d.text((10,6),'Schéma 2 — Le Mouret : de la jonction à la roche, puis au coffre (variante « roche à mi-chemin »)',fill=(255,255,255,255),font=F(18,True))
d.text((10,34),'vert = bande non cadastrée (publique) ; traits blancs = limites de parcelles privées ; bleu = l\'eau qu\'on remonte (à gauche) ; pas de 0,75 m',fill=(255,255,255,255),font=f13)
sb=Q(x0+8,y0+8);d.line([sb,(sb[0]+20*S2,sb[1])],fill=(255,255,255,255),width=4);d.text((sb[0],sb[1]-22),'20 m',fill=(255,255,255,255),font=f13)
im.convert('RGB').save('t88_schema2_fin.jpg',quality=88)
print('ok')
