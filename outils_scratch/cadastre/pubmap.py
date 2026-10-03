import json,io,urllib.request,time,math
from shapely.geometry import shape,Point,box,mapping
from shapely.ops import unary_union,transform
from pyproj import Transformer
from PIL import Image,ImageDraw,ImageFont
T=Transformer.from_crs(4326,2154,always_xy=True)
d=json.load(open('38426-parcelles.json'));own=json.load(open('pm_38426.json'))
def cat(pid):
  o=own.get(pid)
  if not o: return None
  g,n,c=o
  if 'SAINT MAXIMIN' in n and g.startswith('4'): return 'commune'
  if g.startswith(('1','2','3','4')) or 'SYND' in n or 'COMMUNAUTE' in n: return 'autre_public'
  if 'ELECTRICITE' in n or 'EDF' in n: return 'edf'
  return None
polys={'commune':[],'autre_public':[],'edf':[]};allp=[]
for f in d['features']:
  g=transform(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0);allp.append(g)
  c=cat(f['properties']['id'])
  if c: polys[c].append((g,f['properties']['id'],own[f['properties']['id']][1],own[f['properties']['id']][2]))
cadu=unary_union(allp)
tx,ty=T.transform(6.03101275,45.4288723)
cx,cy=tx+1500,ty-700;H=2200;W=1500;bb=(cx-H,cy-H,cx+H,cy+H)
u=f"https://data.geopf.fr/wms-r/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={bb[0]},{bb[1]},{bb[2]},{bb[3]}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
for k in range(8):
  try: im=Image.open(io.BytesIO(urllib.request.urlopen(u,timeout=90).read())).convert('RGBA');break
  except Exception as e: print(e);time.sleep(4)
s=W/(2*H);P=lambda x,y:((x-bb[0])*s,(bb[3]-y)*s)
ov=Image.new('RGBA',im.size,(0,0,0,0));dr=ImageDraw.Draw(ov)
def drawpoly(g,fill,outline):
  for p in (g.geoms if g.geom_type=='MultiPolygon' else [g]):
    dr.polygon([P(*c) for c in p.exterior.coords],fill=fill,outline=outline)
# non cadastré within saint-maximin bbox = bbox minus parcels (restricted to commune hull)
from shapely.geometry import MultiPolygon
hull=cadu.buffer(30).buffer(-30)
nonc=hull.difference(cadu)
nonc=unary_union([g for g in (nonc.geoms if hasattr(nonc,'geoms') else [nonc]) if g.area>30])
print('non cadastré (ha):',round(nonc.area/1e4,1));mk=Image.new('L',im.size,0);dm=ImageDraw.Draw(mk)
for p in (nonc.geoms if nonc.geom_type=='MultiPolygon' else [nonc]):
  dm.polygon([P(*c) for c in p.exterior.coords],fill=255)
  for h in p.interiors: dm.polygon([P(*c) for c in h.coords],fill=0)
wl=Image.new('RGBA',im.size,(255,255,255,0));wl.putalpha(mk.point(lambda v:200 if v else 0));ov=Image.alpha_composite(ov,wl);dr=ImageDraw.Draw(ov)
json.dump(mapping(nonc),open('noncad.json','w'))
for g,_,_,_ in polys['commune']: drawpoly(g,(0,200,0,120),(0,255,0,255))
for g,_,_,_ in polys['autre_public']: drawpoly(g,(0,120,255,120),(0,150,255,255))
for g,_,_,_ in polys['edf']: drawpoly(g,(255,160,0,110),(255,180,0,255))
im=Image.alpha_composite(im,ov);d2=ImageDraw.Draw(im);f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',20)
def mark(la,lo,t,col):
  X,Y=P(*T.transform(lo,la));d2.ellipse((X-9,Y-9,X+9,Y+9),outline=col,width=4);d2.text((X+11,Y-11),t,fill=col,font=f,stroke_width=3,stroke_fill=(0,0,0))
mark(45.4288723,6.03101275,'Tour',(255,255,255));mark(45.422426,6.040299,'Le Mouret',(255,80,80));mark(45.42696,6.05477,'J5',(255,80,80));mark(45.432042,6.043877,'Muraillat',(255,80,80))
d2.text((10,10),"Saint-Maximin — vert : parcelles de la COMMUNE ; bleu : autres publics ; orange : EDF ; blanc : non cadastré (chemins, ruisseaux)",fill=(255,255,255),font=f,stroke_width=3,stroke_fill=(0,0,0))
d2.line((W-170,W-30,W-170+500*s,W-30),fill=(255,255,255),width=5);d2.text((W-170,W-58),'500 m',fill=(255,255,255),font=f,stroke_width=3,stroke_fill=(0,0,0))
im.convert('RGB').save('/home/user/exkalibur/images_travail/t38_cadastre_public_saint_maximin.jpg',quality=85)
# summary of commune parcels: area, centroid, distance & bearing from tower
from pyproj import Geod;Gd=Geod(ellps='WGS84');Ti=Transformer.from_crs(2154,4326,always_xy=True)
rows=[]
for k in ('commune','autre_public'):
  for g,pid,n,c in polys[k]:
    p=g.representative_point();lo,la=Ti.transform(p.x,p.y);az,_,dd=Gd.inv(6.03101275,45.4288723,lo,la)
    rows.append((k,pid,round(g.area),c,n,round(dd),round(az%360),round(la,5),round(lo,5)))
json.dump(rows,open('public_parcels.json','w'),ensure_ascii=False)
print('surface communale totale (ha):',round(sum(g.area for g,*_ in polys['commune'])/1e4,1))
for r in sorted(rows,key=lambda r:-r[2])[:30]: print(r)
