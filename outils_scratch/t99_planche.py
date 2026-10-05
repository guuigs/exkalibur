import json,math,subprocess,os,time,pickle,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Point,box
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vs=np.unpackbits(np.load('vs_muraille_sol.npy'))[:N*N].reshape(N,N).astype(bool)
Vm=np.unpackbits(np.load('vs_muraille.npy'))[:N*N].reshape(N,N).astype(bool)
PUB2=pickle.load(open('run/PUB2.pkl','rb'));PUB3=pickle.load(open('run/PUB3.pkl','rb'))
rows=pickle.load(open('run/rows_final.pkl','rb'))
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
L=[('1  Le Mouret, jonction 1 (1,02 km)',6.040299,45.422426),('2  Le Mouret, jonction 2 (1,03 km)',6.041663,45.423370),('3  prairie près de la tour (240 m)',6.031995,45.426839),('4  Pontcharra sud « A » (1,34 km)',6.020142,45.419519),('5  plaine NO (2,1 km)',6.026558,45.447665),('6  plaine NO (2,1 km)',6.014139,45.443726)]
h=200;W=520;tiles=[]
def wms(x0,y0,x1,y1):
  u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
  for i in range(12):
    if os.path.exists('pl.jpg'): os.remove('pl.jpg')
    subprocess.run(['curl','-sS','-m','90','-o','pl.jpg',u],capture_output=True)
    try: return Image.open('pl.jpg').convert('RGBA')
    except Exception: time.sleep(2)
  return Image.new('RGBA',(W,W),(60,60,60,255))
roads=[shape(f['geometry']) for f in json.load(open('large/troncon_de_route.json'))['features']]
hyd=[shape(f['geometry']) for f in json.load(open('large/troncon_hydrographique.json'))['features']]
for nm,lo,la in L:
  cx,cy=T.transform(lo,la);x0,y0,x1,y1=cx-h,cy-h,cx+h,cy+h;S=W/(2*h)
  im=wms(x0,y0,x1,y1);Q=lambda x,y:((x-x0)*S,(y1-y)*S);bb=box(x0,y0,x1,y1)
  ov=Image.new('RGBA',(W,W));dd=ImageDraw.Draw(ov)
  for G_,col in ((PUB3.intersection(bb),(140,255,140,70)),(PUB2.intersection(bb),(40,230,70,110))):
    for g in getattr(G_,'geoms',[G_]):
      if g.geom_type=='Polygon': dd.polygon([Q(*c[:2]) for c in g.exterior.coords],fill=col)
  R0,C0=int(YN-y1),int(x0-X0);a=np.zeros((2*h,2*h,4),np.uint8);a[Vs[R0:R0+2*h,C0:C0+2*h]]=(255,255,0,110)
  ov=Image.alpha_composite(ov,Image.fromarray(a).resize((W,W),Image.NEAREST));im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
  for g in hyd:
    if g.intersects(bb):
      for l in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in l.coords],fill=(0,170,255,255),width=2)
  for g in roads:
    if g.intersects(bb):
      for l in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in l.coords],fill=(255,255,255,230),width=1)
  for bx,by in B:
    if x0<bx<x1 and y0<by<y1: c=Q(bx,by);d.rectangle([c[0]-2,c[1]-2,c[0]+2,c[1]+2],fill=(255,70,70,255))
  r=[r for r in rows if abs(r['la']-la)<2e-4 and abs(r['lo']-lo)<2e-4]
  c=Q(cx,cy);d.ellipse([c[0]-9,c[1]-9,c[0]+9,c[1]+9],outline=(255,0,255,255),width=3)
  if r:
    for k in sorted(r[0]['rocks'],key=lambda k:-k['frac'])[:60]:
      e=Q(k['cx'],k['cy']);d.ellipse([e[0]-2,e[1]-2,e[0]+2,e[1]+2],fill=(255,150,0,255))
      for t in k['res'][:1]: q=Q(t[2],t[3]);d.line([(q[0]-3,q[1]-3),(q[0]+3,q[1]+3)],fill=(255,255,255,255),width=1);d.line([(q[0]-3,q[1]+3),(q[0]+3,q[1]-3)],fill=(255,255,255,255),width=1)
  d.rectangle([0,0,W,22],fill=(0,0,0,200));d.text((5,3),nm,fill=(255,255,255,255),font=F(13,True))
  tiles.append(im.convert('RGB'))
out=Image.new('RGB',(3*W+20,2*W+10),(0,0,0))
for i,t in enumerate(tiles): out.paste(t,((i%3)*(W+10),(i//3)*(W+10)))
out.save('t99_planche_entonnoir.jpg',quality=86)
