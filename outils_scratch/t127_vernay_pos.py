import json,math,subprocess,os,time,pickle,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import Polygon,Point
from shapely import affinity
from scipy.spatial import cKDTree
exec(open('/home/user/exkalibur/outils_scratch/t126_vernay_fit.py').read().split('Vn=norm(V)')[0])
pts2=[(100,18),(150,8),(200,10),(235,12),(270,5),(300,25),(325,55),(338,100),(343,150),(335,190),(320,215),(285,228),(245,228),(210,210),(180,190),(150,165),(125,152),(100,147),(98,100),(100,50)]
P2=Polygon([(x,-y) for x,y in pts2]).buffer(0)
Vc=V.centroid;sV=math.sqrt(V.area);c2=P2.centroid;s2=1/math.sqrt(P2.area)
def tr(x,y,rot,mirror=0):
    X,Y=(x-c2.x)*s2,(y-c2.y)*s2
    if mirror: X=-X
    a=math.radians(rot);Xr=X*math.cos(a)-Y*math.sin(a);Yr=X*math.sin(a)+Y*math.cos(a)
    return Vc.x+Xr*sV,Vc.y+Yr*sV
import itertools
def poly_real(rot,mirror=0): return Polygon([tr(x,y,rot,mirror) for x,y in P2.exterior.coords])
best=None
for rot in range(0,360):
    q=poly_real(rot,0);i=q.intersection(V).area/q.union(V).area if False else None
# on réutilise l'ajustement normalisé (rot 110°, sans miroir)
rot,mirror=110,0
q=poly_real(rot,mirror)
# l'aire de q doit valoir celle de V (normalisation) ; IoU réel
print('IoU réel après placement sur le lac : %.3f'%(q.intersection(V).area/q.union(V).area))
# décalage éventuel du centroïde : recalage
q=affinity.translate(q,V.centroid.x-q.centroid.x,V.centroid.y-q.centroid.y)
print('IoU après recalage centroïde : %.3f'%(q.intersection(V).area/q.union(V).area))
fall=(205,5);cup=(130,41)   # chute d'eau (au bord haut de l'étang) et coupe, coordonnées (x,-y) du recadrage
fx,fy=tr(*fall,rot,mirror);cx,cy=tr(*cup,rot,mirror)
for nm,(x,y) in (('chute d eau',(fx,fy)),('coupe',(cx,cy))):
    lo,la=Ti.transform(x,y);print(nm,round(la,6),round(lo,6),'distance au bord du lac %.0f m'%Point(x,y).distance(V.exterior))
# rendu
bb=V.bounds;h=max(bb[2]-bb[0],bb[3]-bb[1])/2+200;cx0,cy0=(bb[0]+bb[2])/2,(bb[1]+bb[3])/2;S=1800/(2*h)
x0,x1,y0,y1=cx0-h,cx0+h,cy0-h,cy0+h
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH=1800&HEIGHT=1800&FORMAT=image/jpeg"
for i in range(8):
    if os.path.exists('v1.jpg'): os.remove('v1.jpg')
    subprocess.run(['curl','-sS','-m','120','-o','v1.jpg',u])
    try: im=Image.open('v1.jpg').convert('RGB');break
    except Exception: time.sleep(2)
dr=ImageDraw.Draw(im,'RGBA');Q=lambda px,py:((px-x0)*S,(y1-py)*S)
dr.line([Q(*c) for c in V.exterior.coords],fill=(255,0,255,255),width=4)
dr.line([Q(*c) for c in q.exterior.coords],fill=(255,255,0,255),width=4)
for (x,y),col,lab in (((fx,fy),(0,255,255,255),'chute'),((cx,cy),(255,60,60,255),'coupe')):
    p=Q(x,y);dr.ellipse([p[0]-12,p[1]-12,p[0]+12,p[1]+12],outline=col,width=4);dr.text((p[0]+16,p[1]-8),lab,fill=col,font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',20))
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',18)
dr.rectangle([0,0,1800,34],fill=(0,0,0,255));dr.text((8,6),'Vernay (magenta) et contour peint tourné de 110° (jaune) ; chute d\'eau et coupe de l\'enluminure 9',fill=(255,255,255,255),font=F)
im.save('/home/user/exkalibur/images_travail/t127_vernay_superposition.jpg',quality=88)
pickle.dump((fx,fy,cx,cy),open('run/vernay_pos.pkl','wb'))
