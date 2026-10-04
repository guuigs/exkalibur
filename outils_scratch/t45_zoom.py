import json,math,subprocess,numpy as np
from PIL import Image,ImageDraw
from shapely.geometry import shape,Point
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
acc=np.load('acc.npy')
cx,cy=T.transform(6.036386,45.421409);S=2;half=200
x0,x1,y0,y1=cx-half,cx+half,cy-half,cy+half;W=Hh=2*half*S
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={Hh}&FORMAT=image/jpeg"
for i in range(4):
  if subprocess.run(['curl','-sS','-m','120','-o','ortho_p11.jpg',u]).returncode==0: break
im=Image.open('ortho_p11.jpg').convert('RGBA')
P=lambda x,y:((x-x0)*S,(y1-y)*S)
R0,C0=int(YN-y1),int(x0-X0);V=Vp[R0:R0+2*half,C0:C0+2*half]
a=np.zeros((2*half,2*half,4),np.uint8);a[V]=(255,255,0,80)
ov=Image.fromarray(a).resize((W,Hh),Image.NEAREST);d=ImageDraw.Draw(ov)
# talwegs acc (2 m grid) > 150 cellules (600 m²)
r0,c0=int((YN-y1)/2),int((x0-X0)/2)
A=acc[r0:r0+half,c0:c0+half]
ys,xs=np.where(A>3000)
for yy,xx in zip(ys,xs):
  X=X0+(c0+xx)*2+1;Y=YN-(r0+yy)*2-1;q=P(X,Y);s=1+min(3,int(math.log10(A[yy,xx])-1))
  d.ellipse([q[0]-s,q[1]-s,q[0]+s,q[1]+s],fill=(0,200,255,220))
for f in json.load(open('wfs_troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': d.line([P(*c[:2]) for c in g.coords],fill=(0,80,255,255),width=3)
for f in json.load(open('wfs_troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': d.line([P(*c[:2]) for c in g.coords],fill=(255,255,255,200),width=2)
for m in M:
  if x0<m[0]<x1 and y0<m[1]<y1:
    q=P(m[0],m[1]);d.ellipse([q[0]-7,q[1]-7,q[0]+7,q[1]+7],outline=(255,0,0,255),width=3)
for bx,by in B:
  if x0<bx<x1 and y0<by<y1: q=P(bx,by);d.rectangle([q[0]-2,q[1]-2,q[0]+2,q[1]+2],fill=(255,0,255,255))
q=P(*T.transform(6.036386,45.421409));d.line([q[0]-12,q[1],q[0]+12,q[1]],fill=(255,0,0,255),width=3);d.line([q[0],q[1]-12,q[0],q[1]+12],fill=(255,0,0,255),width=3);d.text((q[0]+10,q[1]+6),'place 11',fill=(255,255,255,255))
d.line([(20,Hh-20),(20+100*S,Hh-20)],fill=(255,255,255,255),width=3);d.text((20,Hh-36),'100 m  (N en haut)',fill=(255,255,255,255))
Image.alpha_composite(im,ov).convert('RGB').save('t45_place11_lever1524.jpg',quality=88)
