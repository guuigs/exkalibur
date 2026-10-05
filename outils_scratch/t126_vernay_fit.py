import json,math,numpy as np
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import Polygon
from shapely import affinity
exec(open('ring1068.py').read().split('out=[]')[0])
pts=[(25,12),(60,12),(100,18),(150,8),(200,10),(235,12),(270,5),(300,25),(325,55),(338,100),(343,150),(335,190),(320,215),(285,228),(245,228),(210,210),(180,190),(150,165),(125,152),(95,147),(70,130),(50,105),(35,75),(22,45)]
P0=Polygon([(x,-y) for x,y in pts]).buffer(0)
d=json.load(open('osm.json'));nodes=d['nodes']
for w in d['ways']:
    if (w[2].get('name') or '')=='Lac du Vernay':
        V=Polygon([T.transform(lo,la) for la,lo in [nodes[str(i)] for i in w[1] if str(i) in nodes]]).buffer(0)
def norm(p):
    p=affinity.translate(p,-p.centroid.x,-p.centroid.y);s=1/math.sqrt(p.area);return affinity.scale(p,s,s,origin=(0,0))
Vn=norm(V);best=[]
for f in (1.0,0.9,0.8,0.7,0.6,0.5):
    Pf=norm(affinity.scale(P0,1,f,origin=(P0.centroid.x,P0.centroid.y)))
    for mirror in (0,1):
        PP=affinity.scale(Pf,-1,1,origin=(0,0)) if mirror else Pf
        for a in np.arange(0,360,1.0):
            r=affinity.rotate(PP,a,origin=(0,0));i=Vn.intersection(r).area;u=Vn.union(r).area
            best.append((i/u,f,mirror,a))
best.sort(reverse=True)
for b in best[:8]: print('IoU %.3f  aplatissement %.1f  miroir %d  rotation %.0f°'%b)
print('meilleur sans aplatissement :',max(b for b in best if b[1]==1.0))
iou,f,mirror,a=best[0]
pickle=__import__('pickle');pickle.dump(best[0],open('run/vernay_fit.pkl','wb'))
# figure
W=1000;sc=330
Pf=norm(affinity.scale(P0,1,f,origin=(P0.centroid.x,P0.centroid.y)))
PP=affinity.rotate(affinity.scale(Pf,-1,1,origin=(0,0)) if mirror else Pf,a,origin=(0,0))
im=Image.new('RGB',(W,560),(255,255,255));dr=ImageDraw.Draw(im);ox,oy=500,290
dr.polygon([(ox+x*sc,oy-y*sc) for x,y in Vn.exterior.coords],fill=(180,200,255),outline=(0,0,200))
dr.line([(ox+x*sc,oy-y*sc) for x,y in PP.exterior.coords],fill=(255,0,0),width=3)
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)
dr.text((10,8),'Lac du Vernay (bleu) et étang peint de l\'enluminure 9 (rouge) : IoU %.2f, aplatissement %.1f, miroir %d, rotation %.0f°'%(iou,f,mirror,a),fill=(0,0,0),font=F)
im.save('/home/user/exkalibur/images_travail/t126_vernay_fit.png')
