import json,math,subprocess,numpy as np
from PIL import Image,ImageDraw
from shapely.geometry import shape
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
# Panneau 1 : vue d'ensemble 2,6 km
px,py=T.transform(6.03115,45.42887)
def ortho(x0,y0,x1,y1,W,H,fn):
  u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
  for i in range(5):
    if subprocess.run(['curl','-sS','-m','120','-o',fn,u]).returncode==0:
      try: return Image.open(fn).convert('RGBA')
      except Exception: pass
x0,x1,y0,y1=px-1300,px+1300,py-1500,py+1300;W,H=900,int(900*2800/2600)
im=ortho(x0,y0,x1,y1,W,H,'o1.jpg');s=W/2600;P=lambda x,y:((x-x0)*s,(y1-y)*s)
d=ImageDraw.Draw(im)
r=1068;q=P(px,py);d.ellipse([q[0]-r*s,q[1]-r*s,q[0]+r*s,q[1]+r*s],outline=(255,255,255,255),width=2)
names={1:'Pierre',2:'André',3:'Jacques',4:'Jean',5:'Philippe',6:'Barth.',7:'Thomas',8:'Matthieu',9:'Jacques m.',10:'Thaddée',11:'Simon',12:'Judas'}
for k in range(1,13):
  az=(92.7-(k-0.5)*30)%360;lo,la,_=G.fwd(6.03115,45.42887,az,r);x,y=T.transform(lo,la);qq=P(x,y)
  col=(255,60,60,255) if k in (3,11) else (255,255,255,255)
  d.ellipse([qq[0]-5,qq[1]-5,qq[0]+5,qq[1]+5],fill=col);d.text((qq[0]+7,qq[1]-6),f'{k}',fill=col)
lo,la,_=G.fwd(6.03115,45.42887,92.7,r);x,y=T.transform(lo,la);qq=P(x,y);d.text((qq[0]-10,qq[1]-20),'Christ (Orient, 13e)',fill=(255,220,0,255))
lo,la,_=G.fwd(6.03115,45.42887,92.7,1300);x,y=T.transform(lo,la);d.line([q,P(x,y)],fill=(255,220,0,255),width=2)
d.text((q[0]+8,q[1]-14),'rempart',fill=(255,255,255,255))
for nm,lo,la in (('jonction',6.040299,45.422426),('source',6.04019,45.42177)):
  x,y=T.transform(lo,la);qq=P(x,y);d.rectangle([qq[0]-3,qq[1]-3,qq[0]+3,qq[1]+3],fill=(0,200,255,255))
d.text((10,10),'Table ronde, Christ à l\'Orient = lever visible de Pâques 1524 (92,7°) ; rayon 1 068 m',fill=(255,255,255,255))
im.convert('RGB').save('t46_panneau1.jpg',quality=88)
# Panneau 2 : zoom 300 m
cx,cy=T.transform(6.0402,45.4222);h=150;S2=3
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h;W=H=2*h*S2
im=ortho(x0,y0,x1,y1,W,H,'o2.jpg');P=lambda x,y:((x-x0)*S2,(y1-y)*S2)
R0,C0=int(YN-y1),int(x0-X0);V=Vp[R0:R0+2*h,C0:C0+2*h]
a=np.zeros((2*h,2*h,4),np.uint8);a[V]=(255,255,0,90);ov=Image.fromarray(a).resize((W,H),Image.NEAREST)
im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
acc=np.load('acc.npy');r0,c0=int((YN-y1)/2),int((x0-X0)/2);A=acc[r0:r0+h,c0:c0+h];yy,xx=np.where(A>1500)
for a_,b_ in zip(yy,xx):
  X=X0+(c0+b_)*2+1;Y=YN-(r0+a_)*2-1;qq=P(X,Y);d.ellipse([qq[0]-2,qq[1]-2,qq[0]+2,qq[1]+2],fill=(0,170,255,230))
for f in json.load(open('wfs_troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': d.line([P(*c[:2]) for c in g.coords],fill=(255,255,255,230),width=3)
for nm,lo,la,col in (('jonction (clairière)',6.040299,45.422426,(255,0,0,255)),('source = place de Simon (11 m)',6.04019,45.42177,(0,255,255,255)),('place 11 calculée',6.040335,45.421761,(255,0,255,255))):
  x,y=T.transform(lo,la);qq=P(x,y);d.ellipse([qq[0]-8,qq[1]-8,qq[0]+8,qq[1]+8],outline=col,width=3);d.text((qq[0]+10,qq[1]-6),nm,fill=col)
for lo,la in ((6.040366,45.421831),(6.040537,45.421890)):
  x,y=T.transform(lo,la);qq=P(x,y);d.line([qq[0]-6,qq[1]-6,qq[0]+6,qq[1]+6],fill=(255,140,0,255),width=3);d.line([qq[0]-6,qq[1]+6,qq[0]+6,qq[1]-6],fill=(255,140,0,255),width=3)
d.line([(15,H-20),(15+50*S2,H-20)],fill=(255,255,255,255),width=3);d.text((15,H-36),'50 m — jaune : vu du pied de la tour ; bleu : talwegs ; X orange : fouille',fill=(255,255,255,255))
im.convert('RGB').save('t46_panneau2.jpg',quality=88)
a=Image.open('t46_panneau1.jpg');b=Image.open('t46_panneau2.jpg');Hm=max(a.height,b.height)
out=Image.new('RGB',(a.width+b.width+10,Hm),(0,0,0));out.paste(a,(0,0));out.paste(b,(a.width+10,0));out.save('t46_paques_source_simon.jpg',quality=88)
