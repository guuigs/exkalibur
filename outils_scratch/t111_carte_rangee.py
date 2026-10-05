import json,math,subprocess,os,time,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51;tlo,tla=Ti.transform(TX,TY)
S=1850/8;az=126.35
cx,cy=TX+(0.06*1000)*0,TY;cx=TX+130;cy=TY-60;h=1650;W=2000;sc=W/(2*h)
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
for i in range(8):
    if os.path.exists('r0.jpg'): os.remove('r0.jpg')
    subprocess.run(['curl','-sS','-m','120','-o','r0.jpg',u])
    try: im=Image.open('r0.jpg').convert('RGB');break
    except Exception: time.sleep(2)
d=ImageDraw.Draw(im,'RGBA')
Q=lambda px,py:((px-x0)*sc,(y1-py)*sc)
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in l.coords],fill=(255,255,0,170),width=1)
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in l.coords],fill=(0,200,255,220),width=2)
mk=['1 Pierre','2 Jacques','3 Jean','4 André','5 Philippe','6 Barthélemy','7 Matthieu','8 Thomas','9 Jacques','10 Thaddée','11 Simon','12 Judas']
P=[];
for k in range(1,13):
    dd=(k-6.5)*S;a=az if dd>=0 else (az+180)%360
    lo,la=G.fwd(tlo,tla,a,abs(dd))[:2];P.append(Q(*T.transform(lo,la)))
d.line([P[0],P[-1]],fill=(255,0,255,230),width=3)
for k,(px,py) in enumerate(P,1):
    col=(255,255,255,255) if k not in (3,11) else (255,60,60,255)
    r=9 if k in (3,11) else 6
    d.ellipse([px-r,py-r,px+r,py+r],outline=col,width=3)
    d.text((px+12,py-24),mk[k-1],fill=col,font=F(17,True),stroke_width=3,stroke_fill=(0,0,0,255))
tq=Q(TX,TY);d.ellipse([tq[0]-12,tq[1]-12,tq[0]+12,tq[1]+12],outline=(0,255,0,255),width=4)
d.text((tq[0]+16,tq[1]+4),'Tour d\'Avalon = Christ = départ',fill=(0,255,0,255),font=F(17,True),stroke_width=3,stroke_fill=(0,0,0,255))
for nm,(la,lo) in {'Église Saint-Hugues (clocher)':(45.433376,6.023109),'J2 (jonction)':(45.42337,6.041663)}.items():
    q=Q(*T.transform(lo,la));d.rectangle([q[0]-5,q[1]-5,q[0]+5,q[1]+5],fill=(255,160,0,255))
    d.text((q[0]+12,q[1]+8),nm,fill=(255,200,0,255),font=F(17,True),stroke_width=3,stroke_fill=(0,0,0,255))
# échelle 500 m
bx,by=60,W-60;d.line([(bx,by),(bx+500*sc,by)],fill=(255,255,255,255),width=5);d.text((bx,by-26),'500 m',fill=(255,255,255,255),font=F(18,True),stroke_width=3,stroke_fill=(0,0,0,255))
d.rectangle([0,0,W,38],fill=(0,0,0,255));d.text((10,8),'Rangée de 12 apôtres (ordre de Marc), pas 231,25 m = 10 stades entre 3 et 11 ; axe = lever visible du 28/10 (126,6°)',fill=(255,255,255,255),font=F(18,True))
im.convert('RGB').save('/home/user/exkalibur/images_travail/t111_carte_rangee_apotres.jpg',quality=88)
print('ok')
