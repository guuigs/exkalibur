import io,urllib.request,time,math,json,numpy as np
from shapely.geometry import shape
from shapely.ops import transform as stf
from PIL import Image,ImageDraw,ImageFont
from pyproj import Transformer
T=Transformer.from_crs(4326,2154,always_xy=True)
X0,YN,N=933000,6489000,7000
mnh=np.clip(np.nan_to_num(np.load('mnh.npy')),0,60)
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
cx,cy=T.transform(6.0412,45.4228);H=330;W=1300;bb=(cx-H,cy-H,cx+H,cy+H);s=W/(2*H)
P=lambda x,y:((x-bb[0])*s,(bb[3]-y)*s)
u=f"https://data.geopf.fr/wms-r/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={bb[0]},{bb[1]},{bb[2]},{bb[3]}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
for k in range(8):
  try: im=Image.open(io.BytesIO(urllib.request.urlopen(u,timeout=90).read())).convert('RGBA');break
  except Exception as e: print(e);time.sleep(4)
ov=Image.new('RGBA',im.size,(0,0,0,0));dr=ImageDraw.Draw(ov)
# visible from foot (open ground)
r0,r1=int(YN-bb[3]),int(YN-bb[1]);c0,c1=int(bb[0]-X0),int(bb[2]-X0)
sub=Vp[r0:r1,c0:c1]&(mnh[r0:r1,c0:c1]<1.5)
ys,xs=np.where(sub)
for yy,xx in zip(ys[::3],xs[::3]):
  X,Y=P(X0+c0+xx,YN-(r0+yy));dr.rectangle((X-1,Y-1,X+1,Y+1),fill=(0,255,255,160))
# non cadastré
nc=shape(json.load(open('cad/noncad.json')))
mk=Image.new('L',im.size,0);dm=ImageDraw.Draw(mk)
for p in nc.geoms:
  if not p.intersects(__import__('shapely.geometry',fromlist=['box']).box(*bb)): continue
  dm.polygon([P(*c) for c in p.exterior.coords],fill=255)
  for h in p.interiors: dm.polygon([P(*c) for c in h.coords],fill=0)
wl=Image.new('RGBA',im.size,(255,255,255,0));wl.putalpha(mk.point(lambda v:150 if v else 0));ov=Image.alpha_composite(ov,wl)
im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im);f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',19)
for ft in json.load(open('wfs_troncon_hydrographique.json'))['features']:
  if ft['geometry']['type']=='LineString': d.line([P(*c[:2]) for c in ft['geometry']['coordinates']],fill=(0,120,255),width=4)
d.line([P(*T.transform(lo,la)) for lo,la in json.load(open('mouret_talweg.json'))],fill=(0,200,255),width=3)
for ft in json.load(open('wfs_troncon_de_route.json'))['features']:
  cs=[P(*c[:2]) for c in ft['geometry']['coordinates']]
  if any(0<=x<=W and 0<=y<=W for x,y in cs): d.line(cs,fill=(230,0,220),width=2)
def mk_(la,lo,t,col,sq=False):
  X,Y=P(*T.transform(lo,la));(d.rectangle if sq else d.ellipse)((X-9,Y-9,X+9,Y+9),outline=col,width=4);d.text((X+11,Y-11),t,fill=col,font=f,stroke_width=3,stroke_fill=(0,0,0))
mk_(45.422426,6.040299,'jonction 4 chemins',(255,255,0),True)
mk_(45.42337,6.041663,'jonction 2',(255,255,0),True)
mk_(45.423566,6.041667,'affleurement 48 m²',(255,120,0))
mk_(45.421767,6.040189,'source',(0,140,255));mk_(45.421003,6.039873,'source',(0,140,255))
mk_(45.42208,6.04066,'place de Simon',(255,60,60))
mk_(45.422555,6.041822,'tête du talweg',(0,220,255))
d.text((10,10),"Le Mouret — cyan : sol visible du PIED de la tour ; blanc : non cadastré (public) ; violet : chemins ; bleu : ruisseaux ; bleu clair : talweg LiDAR",fill=(255,255,255),font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15),stroke_width=3,stroke_fill=(0,0,0))
d.line((W-170,W-30,W-170+100*s,W-30),fill=(255,255,255),width=5);d.text((W-170,W-58),'100 m',fill=(255,255,255),font=f,stroke_width=3,stroke_fill=(0,0,0))
im.convert('RGB').save('/home/user/exkalibur/images_travail/t40_mouret_synthese.jpg',quality=86);print('ok')
