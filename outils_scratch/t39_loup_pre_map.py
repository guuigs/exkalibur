import io,urllib.request,time,math,json,numpy as np
from shapely.geometry import shape
from shapely.ops import transform as stf
exec(open('ring1068.py').read().split('out=[]')[0])
from PIL import Image,ImageDraw,ImageFont
PIED=(45.42887,6.03115);Xp,Yp=T.transform(PIED[1],PIED[0]);Zp=z(mnt,Xp,Yp)+1.7
cx,cy=T.transform(6.0515,45.4273);H=520;W=1200;bb=(cx-H,cy-H,cx+H,cy+H)
s=W/(2*H);P=lambda x,y:((x-bb[0])*s,(bb[3]-y)*s)
u=f"https://data.geopf.fr/wms-r/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={bb[0]},{bb[1]},{bb[2]},{bb[3]}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
for k in range(8):
  try: ortho=Image.open(io.BytesIO(urllib.request.urlopen(u,timeout=90).read())).convert('RGBA');break
  except Exception as e: print(e);time.sleep(4)
# hillshade
c0,c1=int(bb[0]-X0),int(bb[2]-X0);r0,r1=int(YN-bb[3]),int(YN-bb[1])
D=mnt[r0:r1,c0:c1].astype(float);gy,gx=np.gradient(D);sl=np.arctan(np.hypot(gx,gy));asp=np.arctan2(-gx,gy)
hs=np.sin(math.radians(45))*np.cos(sl)+np.cos(math.radians(45))*np.sin(sl)*np.cos(math.radians(315)-asp)
hill=Image.fromarray((np.clip(hs,0,1)*255).astype(np.uint8)).convert('RGBA').resize((W,W))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
pubs=[stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0].startswith(('1','2','3','4'))]
r=json.load(open('wfs_troncon_de_route.json'));h=json.load(open('wfs_troncon_hydrographique.json'))
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',19)
outs=[]
for base,nm in [(ortho,'Photo aérienne'),(hill,'Relief LiDAR (chemins non cartographiés visibles)')]:
  im=base.copy();ov=Image.new('RGBA',im.size,(0,0,0,0));dr=ImageDraw.Draw(ov)
  for g in pubs:
    for p in (g.geoms if g.geom_type=='MultiPolygon' else [g]):
      cs=[P(*c) for c in p.exterior.coords]
      if any(-50<x<W+50 and -50<y<W+50 for x,y in cs): dr.polygon(cs,fill=(0,200,0,70),outline=(0,255,0,255))
  if nm.startswith('Photo'):
    for x in np.arange(bb[0]+4,bb[2],8):
      for y in np.arange(bb[1]+4,bb[3],8):
        if z(mnh,x,y)<1.5 and los(Xp,Yp,Zp,x,y,True)<0:
          X,Y=P(x,y);dr.rectangle((X-3,Y-3,X+3,Y+3),fill=(0,255,255,150))
  im=Image.alpha_composite(im,ov);dd=ImageDraw.Draw(im)
  for ft in h['features']:
    if ft['geometry']['type']=='LineString': dd.line([P(*c[:2]) for c in ft['geometry']['coordinates']],fill=(0,120,255),width=4)
  for ft in r['features']:
    cs=[P(*c[:2]) for c in ft['geometry']['coordinates']]
    if any(0<=x<=W and 0<=y<=W for x,y in cs): dd.line(cs,fill=(230,0,220),width=2)
  a=math.radians(95.78+2.2);dd.line([P(Xp+800*math.sin(a),Yp+800*math.cos(a)),P(Xp+2600*math.sin(a),Yp+2600*math.cos(a))],fill=(255,50,50),width=2)
  rv=[P(*T.transform(lo,la)) for lo,la in json.load(open('ravin_B0071.json'))];dd.line(rv,fill=(0,255,255),width=4)
  for t,la,lo,col in [('pré visible (1 287 m)',45.42773,6.04751,(0,255,255)),('J5',45.42696,6.05477,(255,80,80)),('gué du Tapon',45.42547,6.05785,(255,200,0)),('croisement (Ripellets)',45.428942,6.048785,(255,255,0)),('B0071 forêt communale (Pontcharra)',45.42597,6.05014,(0,255,0))]:
    X,Y=P(*T.transform(lo,la));dd.ellipse((X-9,Y-9,X+9,Y+9),outline=col,width=4);dd.text((X+11,Y-11),t,fill=col,font=f,stroke_width=3,stroke_fill=(0,0,0))
  dd.text((10,10),nm,fill=(255,255,255),font=f,stroke_width=3,stroke_fill=(0,0,0))
  dd.text((10,34),'rouge : axe du loup ; cyan : vu du PIED de la tour + ravin LiDAR (trait cyan) ; vert : terrain communal ; violet : chemins ; bleu : ruisseaux',fill=(255,255,255),font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15),stroke_width=3,stroke_fill=(0,0,0))
  dd.line((W-170,W-30,W-170+200*s,W-30),fill=(255,255,255),width=5);dd.text((W-170,W-58),'200 m',fill=(255,255,255),font=f,stroke_width=3,stroke_fill=(0,0,0))
  outs.append(im.convert('RGB'))
S=Image.new('RGB',(2*W+10,W),'white');S.paste(outs[0],(0,0));S.paste(outs[1],(W+10,0))
S.save('/home/user/exkalibur/images_travail/t39_loup_pre_visible_et_public.jpg',quality=85);print('ok')
