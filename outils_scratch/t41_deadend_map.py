import json,math,numpy as np
from shapely.geometry import shape
from shapely.ops import transform as stf
from PIL import Image,ImageDraw,ImageFont
from pyproj import Transformer
T=Transformer.from_crs(4326,2154,always_xy=True)
mnt=np.load('mnt.npy');X0,YN=933000,6489000
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
pubs=[stf(lambda a,b,c=None:T.transform(a,b),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0].startswith(('1','2','3','4'))]
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',18)
outs=[]
for nm,(la,lo),H in [('Vue d\'ensemble Le Mouret -> Rebouchet amont',(45.4185,6.0455),850),('Cul-de-sac B (sentier, Pontcharra)',(45.416809,6.049903),120),('Cul-de-sac A (roche 207 m², Pontcharra)',(45.414182,6.051137),120)]:
  cx,cy=T.transform(lo,la);W=900;bb=(cx-H,cy-H,cx+H,cy+H);s=W/(2*H);P=lambda x,y:((x-bb[0])*s,(bb[3]-y)*s)
  c0,c1=int(bb[0]-X0),int(bb[2]-X0);r0,r1=int(YN-bb[3]),int(YN-bb[1]);D=mnt[r0:r1,c0:c1].astype(float)
  gy,gx=np.gradient(D);sl=np.arctan(np.hypot(gx,gy));asp=np.arctan2(-gx,gy)
  hs=np.sin(math.radians(40))*np.cos(sl)+np.cos(math.radians(40))*np.sin(sl)*np.cos(math.radians(315)-asp)
  im=Image.fromarray((np.clip(hs,0,1)*255).astype(np.uint8)).convert('RGBA').resize((W,W));ov=Image.new('RGBA',im.size,(0,0,0,0));dr=ImageDraw.Draw(ov)
  for g in pubs:
    for p in (g.geoms if g.geom_type=='MultiPolygon' else [g]):
      cs=[P(*c) for c in p.exterior.coords]
      if any(-100<x<W+100 and -100<y<W+100 for x,y in cs): dr.polygon(cs,fill=(0,200,0,60),outline=(0,160,0,255))
  im=Image.alpha_composite(im,ov);dd=ImageDraw.Draw(im)
  for ft in json.load(open('wfs_troncon_hydrographique.json'))['features']:
    if ft['geometry']['type']=='LineString': dd.line([P(*c[:2]) for c in ft['geometry']['coordinates']],fill=(0,110,255),width=4)
  for ft in json.load(open('wfs_troncon_de_route.json'))['features']:
    cs=[P(*c[:2]) for c in ft['geometry']['coordinates']]
    if any(0<=x<=W and 0<=y<=W for x,y in cs): dd.line(cs,fill=(220,0,200),width=3)
  for t,a,b,col in [('jonction Le Mouret',45.422426,6.040299,(200,150,0)),('cul-de-sac B',45.416809,6.049903,(255,60,0)),('cul-de-sac A',45.414182,6.051137,(255,60,0)),('tour',45.4288723,6.03101275,(0,0,0))]:
    X,Y=P(*T.transform(b,a))
    if -20<X<W+20 and -20<Y<W+20: dd.ellipse((X-9,Y-9,X+9,Y+9),outline=col,width=4);dd.text((X+11,Y-11),t,fill=col,font=f,stroke_width=3,stroke_fill=(255,255,255))
  dd.text((8,8),nm,fill=(0,0,0),font=f,stroke_width=3,stroke_fill=(255,255,255))
  sc=100 if H>300 else 20;dd.line((W-150,W-25,W-150+sc*s,W-25),fill=(0,0,0),width=5);dd.text((W-150,W-52),f'{sc} m',fill=(0,0,0),font=f,stroke_width=3,stroke_fill=(255,255,255))
  outs.append(im.convert('RGB'))
S=Image.new('RGB',(3*900+20,900),'white')
for i,o in enumerate(outs): S.paste(o,(i*910,0))
S.save('/home/user/exkalibur/images_travail/t41_rebouchet_amont_culs_de_sac.jpg',quality=86);print('ok')
