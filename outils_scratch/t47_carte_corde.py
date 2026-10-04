import json,math,subprocess,numpy as np
from PIL import Image,ImageDraw
from shapely.geometry import shape
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
px,py=T.transform(6.03115,45.42887)
x0,x1,y0,y1=px-700,px+1500,py-1150,py+1250;W=1000;H=int(W*(y1-y0)/(x1-x0));s=W/(x1-x0)
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
for i in range(5):
  subprocess.run(['curl','-sS','-m','120','-o','o3.jpg',u])
  try: im=Image.open('o3.jpg').convert('RGBA');break
  except Exception: pass
P=lambda x,y:((x-x0)*s,(y1-y)*s)
R0,C0=int(YN-y1),int(x0-X0);V=Vp[R0:R0+int(y1-y0),C0:C0+int(x1-x0)]
a=np.zeros(V.shape+(4,),np.uint8);a[V]=(255,255,0,110);im=Image.alpha_composite(im,Image.fromarray(a).resize((W,H),Image.NEAREST));d=ImageDraw.Draw(im)
for f in json.load(open('wfs_troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  if g.geom_type=='LineString': d.line([P(*c[:2]) for c in g.coords],fill=(0,160,255,255),width=2)
cols={91.4:(255,80,80,255),93.0:(255,170,0,255)}
for o,col in cols.items():
  pts={}
  for k in (3,11):
    lo,la,_=G.fwd(6.03115,45.42887,(o-(k-0.5)*30)%360,1068);pts[k]=P(*T.transform(lo,la))
  d.line([pts[3],pts[11]],fill=col,width=3)
  for k,q in pts.items(): d.ellipse([q[0]-6,q[1]-6,q[0]+6,q[1]+6],fill=col);d.text((q[0]+8,q[1]-4),f'{k} ({o}°)',fill=col)
  lo,la,_=G.fwd(6.03115,45.42887,o,1300);d.line([P(px,py),P(*T.transform(lo,la))],fill=col,width=1)
q=P(px,py);d.ellipse([q[0]-6,q[1]-6,q[0]+6,q[1]+6],fill=(255,255,255,255));d.text((q[0]-60,q[1]-18),'rempart (centre)',fill=(255,255,255,255))
for nm,lo,la,col in (('ruisseau vu du rempart',6.038836,45.426236,(0,255,255,255)),('jonction du Mouret',6.040299,45.422426,(255,0,255,255)),('source',6.04019,45.42177,(0,255,0,255))):
  q=P(*T.transform(lo,la));d.rectangle([q[0]-5,q[1]-5,q[0]+5,q[1]+5],outline=col,width=3);d.text((q[0]+9,q[1]+2),nm,fill=col)
d.text((10,10),"Table de la Cène (Table ronde), Christ à l'Orient = lever visible de Pâques ; corde 3→11 (Jacques→Simon)",fill=(255,255,255,255))
d.text((10,26),'jaune = vu du pied du rempart ; rouge = Pâques 1524 (91,4°) ; orange = Pâques 2026 (93,0°)',fill=(255,255,255,255))
im.convert('RGB').save('t47_corde_3_11.jpg',quality=88)
