import json,math,subprocess,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
acc=np.load('acc.npy')
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
f12,f14,f16,f20,f24=F(12),F(14),F(16,True),F(20,True),F(26,True)
WHITE=(255,255,255,255);YEL=(255,220,0,255);RED=(255,70,70,255);CY=(0,230,255,255);MAG=(255,60,255,255);GRN=(60,255,90,255);ORA=(255,150,0,255)
def ortho(x0,y0,x1,y1,W,H,fn):
  u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
  for i in range(6):
    subprocess.run(['curl','-sS','-m','120','-o',fn,u])
    try: return Image.open(fn).convert('RGBA')
    except Exception: pass
def label(d,xy,txt,col,font,box=True):
  x,y=xy;b=d.textbbox((x,y),txt,font=font)
  if box: d.rectangle([b[0]-3,b[1]-2,b[2]+3,b[3]+2],fill=(0,0,0,170))
  d.text((x,y),txt,fill=col,font=font)
def num(d,xy,n,col):
  x,y=xy;d.ellipse([x-13,y-13,x+13,y+13],fill=(0,0,0,220),outline=col,width=3);b=d.textbbox((0,0),str(n),font=f16);d.text((x-(b[2]-b[0])/2,y-(b[3]-b[1])/2-3),str(n),fill=col,font=f16)
px,py=T.transform(6.03115,45.42887)
seat=lambda o,k,r=1068:T.transform(*G.fwd(6.03115,45.42887,(o-(k-0.5)*30)%360,r)[:2])
# ---------- Panneau A : vue d'ensemble
x0,x1,y0,y1=px-1350,px+1450,py-1400,py+1350;W=1100;H=int(W*(y1-y0)/(x1-x0));s=W/(x1-x0)
A=ortho(x0,y0,x1,y1,W,H,'oA.jpg');P=lambda x,y:((x-x0)*s,(y1-y)*s)
ov=Image.new('RGBA',(W,H));d=ImageDraw.Draw(ov)
# faisceau de l'aube de Pâques 91,3-93,6°
for o in np.arange(91.3,93.7,0.1):
  e=T.transform(*G.fwd(6.03115,45.42887,o,1400)[:2]);d.line([P(px,py),P(*e)],fill=(255,220,0,40),width=2)
A=Image.alpha_composite(A,ov);d=ImageDraw.Draw(A)
q=P(px,py);r=1068*s;d.ellipse([q[0]-r,q[1]-r,q[0]+r,q[1]+r],outline=WHITE,width=3)
o=92.4
for k in range(1,13):
  c=P(*seat(o,k));col=RED if k in (3,11) else WHITE
  d.ellipse([c[0]-7,c[1]-7,c[0]+7,c[1]+7],fill=col)
  if k not in (3,11): label(d,(c[0]+9,c[1]-9),str(k),WHITE,f12)
ch=P(*T.transform(*G.fwd(6.03115,45.42887,o,1068)[:2]));d.ellipse([ch[0]-9,ch[1]-9,ch[0]+9,ch[1]+9],fill=YEL)
label(d,(ch[0]-150,ch[1]+12),'Christ à l\'Orient (13e)',YEL,f14)
s3,s11=P(*seat(o,3)),P(*seat(o,11))
d.line([s3,s11],fill=RED,width=4)
label(d,(s3[0]+12,s3[1]-8),'3e place : Jacques (gourde)',RED,f14)
label(d,(s11[0]+12,s11[1]+4),'11e place : Simon (scie)',RED,f14)
d.ellipse([q[0]-9,q[1]-9,q[0]+9,q[1]+9],fill=WHITE);label(d,(q[0]-150,q[1]+10),'Rempart (tour d\'Avalon)',WHITE,f14)
e=P(*T.transform(*G.fwd(6.03115,45.42887,92.4,1400)[:2]));label(d,(e[0]-250,e[1]-40),'Soleil de Pâques vu du rempart',YEL,f14)
vs=P(*T.transform(6.038836,45.426236));d.rectangle([vs[0]-7,vs[1]-7,vs[0]+7,vs[1]+7],outline=CY,width=3);label(d,(vs[0]+12,vs[1]-8),'seul ruisseau visible du rempart',CY,f14)
jj=P(*T.transform(6.040299,45.422426));d.rectangle([jj[0]-7,jj[1]-7,jj[0]+7,jj[1]+7],outline=MAG,width=3);label(d,(jj[0]-175,jj[1]-26),'jonction / clairière',MAG,f14)
num(d,(q[0]-25,q[1]-30),1,WHITE);num(d,(e[0]-280,e[1]-30),2,YEL);num(d,(q[0]+r*0.70,q[1]-r*0.72),3,WHITE)
num(d,(s3[0]-20,s3[1]-20),4,RED);num(d,(vs[0]-25,vs[1]-22),5,CY);num(d,(jj[0]-195,jj[1]-18),6,MAG)
d.line([(20,H-25),(20+500*s,H-25)],fill=WHITE,width=4);label(d,(20,H-50),'500 m',WHITE,f14)
label(d,(15,12),'A. Le raisonnement : du rempart à la clairière',WHITE,f20)
# ---------- Panneau B : zoom
cx,cy=T.transform(6.04020,45.42210);h=95;S2=6;WB=HB=int(2*h*S2)
bx0,bx1,by0,by1=cx-h,cx+h,cy-h,cy+h
B_=ortho(bx0,by0,bx1,by1,WB,HB,'oB.jpg');Q=lambda x,y:((x-bx0)*S2,(by1-y)*S2)
R0,C0=int(YN-by1),int(bx0-X0);V=Vp[R0:R0+2*h,C0:C0+2*h];a=np.zeros(V.shape+(4,),np.uint8);a[V]=(255,255,0,85)
B_=Image.alpha_composite(B_,Image.fromarray(a).resize((WB,HB),Image.NEAREST));d=ImageDraw.Draw(B_)
r0,c0=int((YN-by1)/2),int((bx0-X0)/2);Aw=acc[r0:r0+h,c0:c0+h];yy,xx=np.where(Aw>1500)
for a_,b_ in zip(yy,xx):
  X=X0+(c0+b_)*2+1;Y=YN-(r0+a_)*2-1;c=Q(X,Y);d.ellipse([c[0]-3,c[1]-3,c[0]+3,c[1]+3],fill=(0,170,255,230))
for f in json.load(open('wfs_troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': d.line([Q(*c[:2]) for c in g.coords],fill=WHITE,width=3)
pts={'J':(6.040299,45.422426),'R':(6.04019,45.42177),'S':(6.040286,45.421837),'C':(6.040362,45.421836)}
pq={k:Q(*T.transform(*v)) for k,v in pts.items()}
# parcours : jonction -> long du sentier (eau à gauche) -> roche
sent=[shape(f['geometry']) for f in json.load(open('wfs_troncon_de_route.json'))['features'] if f['properties'].get('nature')=='Sentier' and round(shape(f['geometry']).length)==479][0]
from shapely.geometry import Point
J0=Point(*T.transform(*pts['J']));c=[p[:2] for p in sent.coords]
if Point(c[0]).distance(J0)>Point(c[-1]).distance(J0): c=c[::-1]
from shapely.geometry import LineString
L=LineString(c);path=[Q(*L.interpolate(t).coords[0]) for t in range(0,75,3)]
d.line(path,fill=ORA,width=6);d.line([path[-1],pq['R']],fill=ORA,width=6)
d.line([pq['R'],(pq['R'][0],pq['S'][1])],fill=GRN,width=5);d.line([(pq['R'][0],pq['S'][1]),pq['S']],fill=GRN,width=5);d.line([pq['S'],pq['C']],fill=RED,width=5)
for k,col,t,dx,dy in (('J',MAG,'Jonction dans la clairière',14,-34),('R',CY,'Grande roche = source (eaux enchantées)',-430,8),('S',GRN,'Souche-majesté (10 pas N + 10 pas E)',-420,-40),('C',RED,'COFFRE (8 pas vers le jour dernier)',16,-6)):
  c=pq[k];d.ellipse([c[0]-11,c[1]-11,c[0]+11,c[1]+11],fill=(0,0,0,200),outline=col,width=4);label(d,(c[0]+dx,c[1]+dy),t,col,f16)
mid=path[len(path)//2];label(d,(mid[0]-330,mid[1]-10),'sentier : eau à gauche en montant',ORA,f16)
for n,k,col,dx,dy in ((7,'J',MAG,-38,-38),(8,'R',CY,-38,-38),(9,'S',GRN,28,28),(10,'C',RED,30,28)): c=pq[k];num(d,(c[0]+dx,c[1]+dy),n,col)
d.line([(20,HB-25),(20+20*S2,HB-25)],fill=WHITE,width=4);label(d,(20,HB-50),'20 m',WHITE,f14)
label(d,(15,12),'B. Le parcours final (zoom)',WHITE,f20)
label(d,(15,44),'jaune = visible du pied du rempart ; bleu = eau (talwegs LiDAR)',WHITE,f14)
# ---------- Assemblage + légende
LW=760;Ht=max(H,HB)
out=Image.new('RGB',(W+WB+LW+20,Ht),(18,18,24));out.paste(A.convert('RGB'),(0,0));out.paste(B_.convert('RGB'),(W+10,0))
d=ImageDraw.Draw(out);x=W+WB+30;y=20
lines=[('Hypothèse P : « l\'aube de Pâques »',f24,WHITE),('',f14,WHITE),
('1  Départ : chemin de rempart de la tour d\'Avalon',f16,WHITE),('   (arrivée de l\'É11 ; Hugues de Lincoln = Hugues d\'Avalon)',f14,(200,200,200)),
('2  Le ciel donne l\'Orient : soleil de l\'aube de Pâques',f16,YEL),('   vu du rempart (91-94°). Ligne 2 = veillée pascale :',f14,(200,200,200)),('   Alpha-Oméga, Exsultet, « astre du matin »',f14,(200,200,200)),
('3  Table ronde (fondée en souvenir de la Cène),',f16,WHITE),('   centrée au rempart, le Christ à l\'Orient',f14,(200,200,200)),
('4  3e et 11e = Jacques et Simon (Matthieu 10),',f16,RED),('   10 stades entre eux -> rayon 1 068 m',f14,(200,200,200)),('   3e en prés (pas d\'écharde), 11e en forêt (écharde)',f14,(200,200,200)),('   13e = le Christ : champs, « pas le bon endroit »',f14,(200,200,200)),
('5  En allant « directement de la 3e à la 11e »,',f16,CY),('   la ligne traverse le seul ruisseau visible',f14,(200,200,200)),('   du rempart (« magnifiait le ruisseau »)...',f14,(200,200,200)),
('6  ...puis la jonction de 4 chemins, en lisière',f16,MAG),('   d\'une clairière visible du rempart',f14,(200,200,200)),
('7  « Dans la clairière, à la jonction des chemins »',f16,MAG),
('8  « suivi à senestre les eaux enchantées » : sentier',f16,CY),('   sud, l\'eau à gauche, jusqu\'à la source (73 m)',f14,(200,200,200)),('   = la grande roche (enl. 9 : source dans un rocher)',f14,(200,200,200)),
('9  10 pas au nord, autant à l\'est : la souche',f16,GRN),
('10 8 pas vers le jour dernier : le coffre',f16,RED),('   à 13-32 m après la roche, ~60 m de la jonction',f14,(200,200,200)),
('',f14,WHITE),('Contrôles',f16,WHITE),('- autres dates, miroir, lever astronomique : moins bons',f14,(200,200,200)),('- corde par ruisseau + jonction : 0,44 % des orientations',f14,(200,200,200)),
('',f14,WHITE),('Points faibles',f16,ORA),('- coffre en bois privé : domaine public NON tenu',f14,ORA),('- roche non visible en ligne (inconnue acceptée)',f14,ORA)]
for t,fnt,col in lines:
  d.text((x,y),t,fill=col,font=fnt);y+=fnt.size+8
out.save('t49_carte_raisonnement_P.jpg',quality=90);print(out.size)
