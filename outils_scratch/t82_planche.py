import subprocess,json,time,pickle,numpy as np
from PIL import Image,ImageDraw,ImageFont
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vs=np.unpackbits(np.load('vs_muraille_sol.npy'))[:N*N].reshape(N,N).astype(bool)
cs=np.load('run/coffre_sur.npy')
L=[('A 45.419519, 6.020142 (passe tout)',6.020142,45.419519),('B Le Mouret 45.422426, 6.040299',6.040299,45.422426),('C 45.443603, 6.014493 (2,08 km)',6.014493,45.443603),('D 45.441043, 6.008715 (2,2 km)',6.008715,45.441043),('E 45.444902, 6.014473 (2,2 km)',6.014473,45.444902),('F 45.423829, 5.998057 (2,6 km)',5.998057,45.423829)]
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15)
tiles=[]
for name,lo,la in L:
  cx,cy=T.transform(lo,la);h=200;W=500
  u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={cx-h},{cy-h},{cx+h},{cy+h}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
  im=None
  for i in range(8):
    subprocess.run(['curl','-sS','-m','120','-o','tile.jpg',u])
    try: im=Image.open('tile.jpg').convert('RGBA');break
    except Exception: time.sleep(1)
  r0,c0=int(YN-(cy+h)),int(cx-h-X0)
  a=np.zeros((2*h,2*h,4),np.uint8);a[Vs[r0:r0+2*h,c0:c0+2*h]]=(255,255,0,90)
  R=5;rr,cc=int((YN-(cy+h))/R),int((cx-h-X0)/R);sub=cs[rr:rr+2*h//R,cc:cc+2*h//R]
  b=np.zeros((2*h//R,2*h//R,4),np.uint8);b[sub]=(0,255,120,110)
  ov=Image.alpha_composite(Image.fromarray(a).resize((W,W)),Image.fromarray(b).resize((W,W),Image.NEAREST))
  im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
  d.ellipse([W/2-10,W/2-10,W/2+10,W/2+10],outline=(255,0,255,255),width=4)
  d.rectangle([0,0,W,24],fill=(0,0,0,200));d.text((6,3),name,fill=(255,255,255,255),font=f)
  tiles.append(im.convert('RGB'))
out=Image.new('RGB',(3*510,2*510),(0,0,0))
for i,t in enumerate(tiles): out.paste(t,((i%3)*510,(i//3)*510))
out.save('t82_planche_pretendants.jpg',quality=85)
