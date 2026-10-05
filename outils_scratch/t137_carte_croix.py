import json,math,subprocess,os,time
from PIL import Image,ImageDraw,ImageFont
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51
S=1850/8
Nx,Ny=T.transform(6.0320,45.42684)
brg=math.degrees(math.atan2(Nx-TX,Ny-TY))%360   # grille
# axe vertical (sud = vers J16 depuis la tour) en direction grille ; horizontal = +90 (est côté Orient)
ux,uy=math.sin(math.radians(brg)),math.cos(math.radians(brg))   # vecteur "bas" (de la tour vers J16)
hx,hy=-uy,ux   # perpendiculaire tournant de +90° ... à vérifier : bearing+90 -> (sin(b+90),cos(b+90))=(cos b,-sin b)=(uy,-ux)
hx,hy=-uy,ux
cx,cy=(TX+Nx)/2+0*hx,(TY+Ny)/2;h=1500;W=2000;sc=W/(2*h)
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={W}&FORMAT=image/jpeg"
for i in range(8):
    if os.path.exists('x0.jpg'): os.remove('x0.jpg')
    subprocess.run(['curl','-sS','-m','120','-o','x0.jpg',u])
    try: im=Image.open('x0.jpg').convert('RGB');break
    except Exception: time.sleep(2)
d=ImageDraw.Draw(im,'RGBA');Q=lambda px,py:((px-x0)*sc,(y1-py)*sc)
F=lambda s,b=True:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
L='PATERNOSTER'.replace('N','N')
word='PATERNOSTER'  # 11 lettres : P A T E R N O S T E R ; rang k de 1 à 11 ; N au rang 6
# bras vertical : rang 5 (R) = départ (tour) ; N = J16 ; haut = vers la tour (nord) donc rang k à (k-6)*S en "bas"
pts_v=[(k,word[k-1],Nx+(k-6)*S*ux,Ny+(k-6)*S*uy) for k in range(1,12)]
pts_h=[(k,word[k-1],Nx+(k-6)*S*hx,Ny+(k-6)*S*hy) for k in range(1,12)]
d.line([Q(pts_v[0][2],pts_v[0][3]),Q(pts_v[-1][2],pts_v[-1][3])],fill=(255,0,255,200),width=3)
d.line([Q(pts_h[0][2],pts_h[0][3]),Q(pts_h[-1][2],pts_h[-1][3])],fill=(0,255,255,200),width=3)
for arm,col in ((pts_v,(255,0,255,255)),(pts_h,(0,255,255,255))):
    for k,ch,x,y in arm:
        if k==6: continue
        p=Q(x,y);r=15 if ch in 'TR' else 11
        d.ellipse([p[0]-r,p[1]-r,p[0]+r,p[1]+r],outline=col,fill=(0,0,0,150),width=3);d.text((p[0]-7,p[1]-12),ch,fill=(255,255,255,255),font=F(20))
        if (arm is pts_v) and k in (3,5,11):
            lab={3:'3e (T)',5:'départ R5 = rempart',11:'11e (R)'}[k];d.text((p[0]+18,p[1]-10),lab,fill=(255,230,0,255),font=F(18),stroke_width=3,stroke_fill=(0,0,0,255))
p=Q(Nx,Ny);d.ellipse([p[0]-20,p[1]-20,p[0]+20,p[1]+20],outline=(255,60,60,255),width=5);d.text((p[0]+24,p[1]-12),'N = jonction = J16',fill=(255,90,90,255),font=F(20),stroke_width=3,stroke_fill=(0,0,0,255))
tq=Q(TX,TY);d.rectangle([tq[0]-8,tq[1]-8,tq[0]+8,tq[1]+8],outline=(0,255,0,255),width=4)
d.rectangle([0,0,W,36],fill=(0,0,0,255))
d.text((8,8),'Croix PATERNOSTER (enl. 11) posée sur la carte : pas 231,25 m (3e→11e = 10 stades), départ R5 au rempart, centre N = J16',fill=(255,255,255,255),font=F(17))
im.convert('RGB').save('/home/user/exkalibur/images_travail/t137_croix_paternoster_carte.jpg',quality=88)
lo,la=Ti.transform(*[v for v in (pts_v[2][2],pts_v[2][3])]);print('T3 ',round(la,5),round(lo,5))
lo,la=Ti.transform(pts_v[10][2],pts_v[10][3]);print('R11',round(la,5),round(lo,5))
lo,la=Ti.transform(pts_v[4][2],pts_v[4][3]);print('R5 ',round(la,5),round(lo,5),'(doit ≈ tour)')
print('axe vertical (grille) %.1f° ; vrai %.1f°'%(brg,brg+2.2))
