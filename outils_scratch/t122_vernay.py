import json,math,subprocess,os,time
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,Polygon,Point
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51
d=json.load(open('osm.json'));nodes=d['nodes']
V=[]
for w in d['ways']:
    tags=w[2];ids=w[1]
    if 'vernay' in (tags.get('name') or '').lower() or ('water' in tags.get('natural','') and ids and ids[0]==ids[-1]):
        pts=[nodes[str(i)] for i in ids if str(i) in nodes]
        if len(pts)>=4:
            p=Polygon([T.transform(lo,la) for la,lo in pts]).buffer(0)
            if 'vernay' in (tags.get('name') or '').lower(): V.append((tags.get('name'),tags,p))
for n,t,p in V:
    lo,la=Ti.transform(p.centroid.x,p.centroid.y);print(n,t.get('water'),t.get('natural'),'aire %.0f m²'%p.area,'centre',round(la,5),round(lo,5),'dist tour %.0f'%p.centroid.distance(Point(TX,TY)))
vp=max(V,key=lambda v:v[2].area)[2]
bb=vp.bounds;cx,cy=(bb[0]+bb[2])/2,(bb[1]+bb[3])/2;h=max(bb[2]-bb[0],bb[3]-bb[1])/2+150;S=1800/(2*h)
x0,x1,y0,y1=cx-h,cx+h,cy-h,cy+h
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH=1800&HEIGHT=1800&FORMAT=image/jpeg"
for i in range(8):
    if os.path.exists('v0.jpg'): os.remove('v0.jpg')
    subprocess.run(['curl','-sS','-m','120','-o','v0.jpg',u])
    try: im=Image.open('v0.jpg').convert('RGB');break
    except Exception: time.sleep(2)
dr=ImageDraw.Draw(im,'RGBA');Q=lambda px,py:((px-x0)*S,(y1-py)*S)
dr.line([Q(*c) for c in vp.exterior.coords],fill=(255,0,255,255),width=3)
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',18)
dr.rectangle([0,0,1800,34],fill=(0,0,0,255));dr.text((8,6),'Lac du Vernay (OSM, contour magenta) — aire %.0f m² — orthophoto IGN'%vp.area,fill=(255,255,255,255),font=F)
im.save('/home/user/exkalibur/images_travail/t122_vernay.jpg',quality=88)
mr=vp.minimum_rotated_rectangle;e=[math.dist(mr.exterior.coords[i],mr.exterior.coords[i+1]) for i in range(2)]
print('rectangle englobant %.0f x %.0f m ; solidité %.2f'%(max(e),min(e),vp.area/vp.convex_hull.area))
