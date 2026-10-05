import json,math,subprocess,os,time,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point
exec(open('ring1068.py').read().split('out=[]')[0])
LA,LO=45.418419,6.048904;x,y=T.transform(LO,LA);h=45;S=10;W=2*h*S
x0,x1,y0,y1=x-h,x+h,y-h,y+h
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
def wms(layer,fn):
  u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS={layer}&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
  for i in range(8):
    if os.path.exists(fn): os.remove(fn)
    subprocess.run(['curl','-sS','-m','90','-o',fn,u])
    try: return Image.open(fn).convert('RGB')
    except Exception: time.sleep(2)
  return None
Q=lambda px,py:((px-x0)*S,(y1-py)*S)
tiles=[]
orth=wms('HR.ORTHOIMAGERY.ORTHOPHOTOS','o0.jpg')
d=ImageDraw.Draw(orth)
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in l.coords],fill=(0,200,255),width=4)
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in l.coords],fill=(255,255,0),width=3)
q=Q(x,y);d.ellipse([q[0]-14,q[1]-14,q[0]+14,q[1]+14],outline=(255,0,255),width=4)
d.rectangle([0,0,W,34],fill=(0,0,0));d.text((8,6),'Photo aérienne IGN récente + eau (bleu) + chemins (jaune) — point 45.418419, 6.048904',fill=(255,255,255),font=F(17,True))
orth.save('t92_a_ortho.jpg',quality=90)
# MNT ombré
R,C=int(YN-y),int(x-X0)
Z=mnt[R-h:R+h,C-h:C+h].astype(float);gy,gx=np.gradient(Z)
sl=np.arctan(np.hypot(gx,gy));asp=np.arctan2(-gx,gy)
hs=np.clip(255*(np.cos(sl)*np.cos(np.radians(45))+np.sin(sl)*np.sin(np.radians(45))*np.cos(np.radians(315)-asp)),0,255).astype(np.uint8)
im=Image.fromarray(hs).resize((W,W),Image.BICUBIC).convert('RGB');d=ImageDraw.Draw(im)
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in l.coords],fill=(0,160,255),width=3)
for lvl in np.arange(np.floor(Z.min()),Z.max(),2):
  pass
d.ellipse([q[0]-14,q[1]-14,q[0]+14,q[1]+14],outline=(255,0,255),width=4)
d.rectangle([0,0,W,34],fill=(0,0,0));d.text((8,6),'Relief LiDAR 1 m ombré (sol seul, sans arbres)',fill=(255,255,255),font=F(17,True))
im.save('t92_b_mnt.jpg',quality=90)
# MNS (sol+arbres)
M2=(mnt[R-h:R+h,C-h:C+h]+mnh[R-h:R+h,C-h:C+h]).astype(float);gy,gx=np.gradient(M2)
sl=np.arctan(np.hypot(gx,gy));asp=np.arctan2(-gx,gy)
hs=np.clip(255*(np.cos(sl)*np.cos(np.radians(45))+np.sin(sl)*np.sin(np.radians(45))*np.cos(np.radians(315)-asp)),0,255).astype(np.uint8)
im=Image.fromarray(hs).resize((W,W),Image.BICUBIC).convert('RGB');d=ImageDraw.Draw(im)
d.ellipse([q[0]-14,q[1]-14,q[0]+14,q[1]+14],outline=(255,0,255),width=4)
d.rectangle([0,0,W,34],fill=(0,0,0));d.text((8,6),'Relief LiDAR avec la canopée (arbres)',fill=(255,255,255),font=F(17,True))
im.save('t92_c_mns.jpg',quality=90)
# profils : hauteur du sol le long du chemin (E-O et N-S) et canopée
print('profil Z sol (m) du centre : N-S tous les 5 m :',[round(float(mnt[R+k,C]),1) for k in range(-30,31,5)])
print('profil Z sol E-O :',[round(float(mnt[R,C+k]),1) for k in range(-30,31,5)])
print('canopée N-S :',[round(float(mnh[R+k,C]),0) for k in range(-30,31,5)])
# zone dégagée : taille
op=(mnh[R-30:R+31,C-30:C+31]<1.5);lab,n=__import__('scipy.ndimage',fromlist=['label']).label(op);cl=lab[30,30]
if cl: 
  ys,xs=np.where(lab==cl);print('trouée contenant le point : %d m², étendue %d m (N-S) x %d m (E-O)'%((lab==cl).sum(),np.ptp(ys)+1,np.ptp(xs)+1))
