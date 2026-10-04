import json,math,subprocess,numpy as np
from PIL import Image,ImageDraw
from shapely.geometry import shape
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
NC=shape(json.load(open('cad/noncad.json')))
cx,cy=T.transform(6.04025,45.42205);h=110;S2=4;W=H=2*h*S2
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
for i in range(5):
  subprocess.run(['curl','-sS','-m','120','-o','o4.jpg',u])
  try: im=Image.open('o4.jpg').convert('RGBA');break
  except Exception: pass
P=lambda x,y:((x-x0)*S2,(y1-y)*S2)
R0,C0=int(YN-y1),int(x0-X0);V=Vp[R0:R0+2*h,C0:C0+2*h]
a=np.zeros(V.shape+(4,),np.uint8);a[V]=(255,255,0,80);im=Image.alpha_composite(im,Image.fromarray(a).resize((W,H),Image.NEAREST))
ov=Image.new('RGBA',(W,H),(0,0,0,0));d=ImageDraw.Draw(ov)
loc=NC.intersection(shape({'type':'Polygon','coordinates':[[(x0,y0),(x1,y0),(x1,y1),(x0,y1),(x0,y0)]]}))
for g in getattr(loc,'geoms',[loc]):
  if g.geom_type=='Polygon': d.polygon([P(*c[:2]) for c in g.exterior.coords],fill=(0,255,0,60),outline=(0,255,0,200))
im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
for f in json.load(open('wfs_troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': d.line([P(*c[:2]) for c in g.coords],fill=(255,255,255,255),width=2)
for o,col in ((91.4,(255,80,80,255)),(93.0,(255,170,0,255))):
  pts={}
  for k in (3,11):
    lo,la,_=G.fwd(6.03115,45.42887,(o-(k-0.5)*30)%360,1068);pts[k]=P(*T.transform(lo,la))
  d.line([pts[3],pts[11]],fill=col,width=2);q=pts[11];d.ellipse([q[0]-7,q[1]-7,q[0]+7,q[1]+7],outline=col,width=3);d.text((q[0]+9,q[1]),f'Simon {o}°',fill=col)
for nm,lo,la,col in (('jonction',6.040299,45.422426,(255,0,255,255)),('source 1',6.04019,45.42177,(0,255,255,255)),('source 2',6.039873,45.421003,(0,255,255,255))):
  q=P(*T.transform(lo,la));d.rectangle([q[0]-6,q[1]-6,q[0]+6,q[1]+6],outline=col,width=3);d.text((q[0]+9,q[1]-14),nm,fill=col)
for (la0,la1,lo0,lo1,col,nm) in ((45.42182,45.42194,6.04034,6.04054,(255,140,0,255),'fouille (roche = source)'),(45.42249,45.42266,6.04040,6.04060,(0,255,0,255),'fouille P-public')):
  a_=P(*T.transform(lo0,la1));b_=P(*T.transform(lo1,la0));d.rectangle([a_,b_],outline=col,width=3);d.text((b_[0]+5,b_[1]),nm,fill=col)
d.line([(15,H-20),(15+20*S2,H-20)],fill=(255,255,255,255),width=3);d.text((15,H-38),'20 m — vert : bande publique ; jaune : vu du pied du rempart',fill=(255,255,255,255))
im.convert('RGB').save('t47_detail_final.jpg',quality=90)
