import json,math,subprocess,os,time,pickle,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,box
from scipy import ndimage
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vm=np.unpackbits(np.load('vs_muraille.npy'))[:N*N].reshape(N,N).astype(bool)
Vs=np.unpackbits(np.load('vs_muraille_sol.npy'))[:N*N].reshape(N,N).astype(bool)
c=T.transform(6.0410,45.4229);h=260;S=4;W=2*h*S
x0,x1,y0,y1=c[0]-h,c[0]+h,c[1]-h,c[1]+h
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
Q=lambda px,py:((px-x0)*S,(y1-py)*S)
def wms(layer,fn):
  u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS={layer}&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
  for i in range(8):
    if os.path.exists(fn): os.remove(fn)
    subprocess.run(['curl','-sS','-m','90','-o',fn,u])
    try: return Image.open(fn).convert('RGB')
    except Exception: time.sleep(2)
im=wms('HR.ORTHOIMAGERY.ORTHOPHOTOS','m0.jpg');d=ImageDraw.Draw(im,'RGBA')
R0,C0=int(YN-y1),int(x0-X0);n=2*h
op=(mnh[R0:R0+n,C0:C0+n]<1.5);vm=Vm[R0:R0+n,C0:C0+n];vs=Vs[R0:R0+n,C0:C0+n]
ov=np.zeros((n,n,4),np.uint8)
ov[op]=(255,255,0,60);ov[op&(vm|vs)]=(255,0,255,170)
im.paste(Image.fromarray(ov).resize((W,W),Image.NEAREST),(0,0),Image.fromarray(ov).resize((W,W),Image.NEAREST))
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*c_[:2]) for c_ in l.coords],fill=(0,200,255,255),width=3)
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*c_[:2]) for c_ in l.coords],fill=(255,160,0,255),width=2)
for la,lo,t in ((45.42243,6.0403,'J1'),(45.42337,6.04166,'J2'),(45.423957,6.0417,'ressaut')):
  q=Q(*T.transform(lo,la));d.ellipse([q[0]-12,q[1]-12,q[0]+12,q[1]+12],outline=(255,255,255,255),width=3);d.text((q[0]+14,q[1]-8),t,fill=(255,255,255,255),font=F(16,True))
d.rectangle([0,0,W,30],fill=(0,0,0,255))
d.text((8,5),'Mouret : jaune = sol dégagé (<1,5 m), magenta = dégagé ET vu depuis la muraille ; bleu eau, orange chemins',fill=(255,255,255,255),font=F(14,True))
im.convert('RGB').save('/home/user/exkalibur/images_travail/t102_mouret_ouvert_vu.jpg',quality=88)
lab,k=ndimage.label(op&(vm|vs))
print('plages dégagées+vues:',k)
for i in range(1,k+1):
  ys,xs=np.where(lab==i)
  if len(ys)<15: continue
  X=x0+xs.mean();Y=y1-ys.mean();lo,la=Ti.transform(X,Y);print(round(la,5),round(lo,5),len(ys),'m²')
