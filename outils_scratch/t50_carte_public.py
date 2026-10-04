import json,math,subprocess,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point,LineString
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool);acc=np.load('acc.npy')
NC=shape(json.load(open('cad/noncad.json')))
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
f14,f16,f20=F(14),F(16,True),F(20,True)
cx,cy=T.transform(6.04028,45.42215);h=60;S2=9;W=H=int(2*h*S2)
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
for i in range(6):
  subprocess.run(['curl','-sS','-m','120','-o','oC.jpg',u])
  try: im=Image.open('oC.jpg').convert('RGBA');break
  except Exception: pass
Q=lambda x,y:((x-x0)*S2,(y1-y)*S2)
ov=Image.new('RGBA',(W,H));d=ImageDraw.Draw(ov)
loc=NC.intersection(shape({'type':'Polygon','coordinates':[[(x0,y0),(x1,y0),(x1,y1),(x0,y1),(x0,y0)]]}))
for g in getattr(loc,'geoms',[loc]):
  if g.geom_type=='Polygon': d.polygon([Q(*c[:2]) for c in g.exterior.coords],fill=(60,255,90,70),outline=(60,255,90,220))
im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
r0,c0=int((YN-y1)/2),int((x0-X0)/2);A=acc[r0:r0+h,c0:c0+h];yy,xx=np.where(A>1500)
for a,b in zip(yy,xx):
  X=X0+(c0+b)*2+1;Y=YN-(r0+a)*2-1;c=Q(X,Y);d.ellipse([c[0]-4,c[1]-4,c[0]+4,c[1]+4],fill=(0,170,255,230))
for f in json.load(open('wfs_troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': d.line([Q(*c[:2]) for c in g.coords],fill=(255,255,255,255),width=3)
def lab(xy,t,col,font=f16):
  b=d.textbbox(xy,t,font=font);d.rectangle([b[0]-3,b[1]-2,b[2]+3,b[3]+2],fill=(0,0,0,180));d.text(xy,t,fill=col,font=font)
P=lambda lo,la:Q(*T.transform(lo,la))
J=P(6.040299,45.422426)
# zone roche (11-24 m) et zone coffre
rocks=[(6.040377,45.422341),(6.040401,45.422323),(6.040426,45.422304),(6.040425,45.422286),(6.040424,45.422268),(6.040422,45.422232)]
chests=[(6.040526,45.4224),(6.040546,45.422399),(6.040593,45.422392),(6.040765,45.422417),(6.040764,45.422401),(6.040751,45.422406)]
for lo,la in rocks: c=P(lo,la);d.ellipse([c[0]-7,c[1]-7,c[0]+7,c[1]+7],outline=(0,240,255,255),width=3)
for lo,la in chests: c=P(lo,la);d.rectangle([c[0]-7,c[1]-7,c[0]+7,c[1]+7],outline=(255,60,60,255),width=4)
# exemple de parcours
r=P(6.040426,45.422304);s=P(*G.fwd(*G.fwd(6.040426,45.422304,0,7.5)[:2],90,7.5)[:2]);ch=P(6.040593,45.422392)
d.line([J,r],fill=(255,150,0,255),width=6);d.line([r,(r[0],s[1])],fill=(60,255,90,255),width=5);d.line([(r[0],s[1]),s],fill=(60,255,90,255),width=5);d.line([s,ch],fill=(255,60,60,255),width=5)
d.ellipse([J[0]-12,J[1]-12,J[0]+12,J[1]+12],outline=(255,60,255,255),width=4);lab((J[0]-260,J[1]-40),'① Jonction dans la clairière',(255,60,255,255))
lab((r[0]+14,r[1]+10),'② Grande roche au bord de l\'eau (11-24 m)',(0,240,255,255))
lab((s[0]-330,s[1]+14),'③ Souche (10 pas N + 10 pas E)',(60,255,90,255))
lab((ch[0]+30,ch[1]-46),'④ COFFRE sur la bande publique',(255,60,60,255))
src=P(6.04019,45.42177)
if 0<src[1]<H: d.ellipse([src[0]-9,src[1]-9,src[0]+9,src[1]+9],outline=(200,200,200,255),width=3);lab((src[0]+12,src[1]-8),'ancienne lecture : roche à la source (coffre en privé)',(200,200,200,255),f14)
lab((14,12),'Variante P-public : le coffre sur le chemin public',(255,255,255,255),f20)
lab((14,44),'vert = domaine public (bandes non cadastrées) ; bleu = eau ; blanc = chemins',(255,255,255,255),f14)
lab((14,68),'orange = on suit les eaux (sentier sud, eau à gauche)',(255,150,0,255),f14)
d.line([(20,H-25),(20+10*S2,H-25)],fill=(255,255,255,255),width=4);lab((20,H-52),'10 m',(255,255,255,255),f14)
im.convert('RGB').save('t50_variante_public.jpg',quality=90)
