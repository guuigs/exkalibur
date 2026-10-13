import json, math, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0,'.')
from geo import direct
LAT0,LAT1,LON0,LON1=45.39,45.47,5.97,6.09
if len(sys.argv)>1: LAT0,LAT1,LON0,LON1=map(float,sys.argv[1:5])
MPP=float(sys.argv[5]) if len(sys.argv)>5 else 5.0
out=sys.argv[6] if len(sys.argv)>6 else 'map.png'
ky=111132.0; kx=111320*math.cos(math.radians((LAT0+LAT1)/2))
W=int((LON1-LON0)*kx/MPP); H=int((LAT1-LAT0)*ky/MPP)
def P(lon,lat): return ((lon-LON0)*kx/MPP, (LAT1-lat)*ky/MPP)
im=Image.new('RGB',(W,H),(250,250,245)); d=ImageDraw.Draw(im)
def rings(g):
    t=g['type']; c=g['coordinates']
    if t=='Polygon': return [c[0]]
    if t=='MultiPolygon': return [p[0] for p in c]
    return []
def lines(g):
    t=g['type']; c=g['coordinates']
    if t=='LineString': return [c]
    if t=='MultiLineString': return c
    return []
col={'Bois':(170,215,150),'Forêt fermée de feuillus':(150,205,130),'Forêt fermée mixte':(130,190,120),'Forêt fermée de conifères':(110,170,110),'Verger':(225,240,180),'Vigne':(235,215,235),'Forêt ouverte':(190,225,170),'Lande ligneuse':(210,220,170),'Peupleraie':(190,230,190)}
for f in json.load(open('zone_de_vegetation.json')):
    n=f['properties'].get('nature')
    if n in col:
        for r in rings(f['geometry']):
            d.polygon([P(*p[:2]) for p in r],fill=col[n])
for f in json.load(open('troncon_de_route.json')):
    n=f['properties']['nature']
    for l in lines(f['geometry']):
        pts=[P(*p[:2]) for p in l]
        if n=='Sentier': d.line(pts,fill=(160,80,20),width=2)
        elif n=='Chemin': d.line(pts,fill=(200,120,40),width=2)
        elif n=='Route empierrée': d.line(pts,fill=(170,170,120),width=2)
        else: d.line(pts,fill=(150,150,150),width=3)
for f in json.load(open('troncon_hydrographique.json')):
    p=f['properties']
    for l in lines(f['geometry']):
        pts=[P(*q[:2]) for q in l]
        d.line(pts,fill=(30,90,230) if p.get('persistance')=='Permanent' else (100,160,255),width=3 if p.get('persistance')=='Permanent' else 2)
for f in json.load(open('detail_hydrographique.json')):
    n=f['properties'].get('nature'); x,y=P(*f['geometry']['coordinates'][:2])
    if n in ('Source','Source captée'): d.ellipse((x-5,y-5,x+5,y+5),outline=(0,0,200),width=2)
for f in json.load(open('construction_ponctuelle.json')):
    if f['properties'].get('nature')=='Croix':
        x,y=P(*f['geometry']['coordinates'][:2]); d.line((x-5,y,x+5,y),fill=(0,0,0),width=2); d.line((x,y-5,x,y+5),fill=(0,0,0),width=2)
pts={'TA':(45.429083,6.030808),'CB':(45.423611,6.018889),'FB':(45.43564,5.98710)}
for k,(la,lo) in pts.items():
    x,y=P(lo,la); d.ellipse((x-6,y-6,x+6,y+6),fill=(220,0,0)); d.text((x+8,y-8),k,fill=(200,0,0))
for k in ('TA','CB'):
    la,lo=pts[k]
    ring=[P(*direct((la,lo),a,1.85)[::-1]) for a in range(0,361,2)]
    d.line(ring,fill=(220,0,0) if k=='TA' else (240,120,0),width=2)
# scale bar 500 m
d.line((20,H-20,20+500/MPP,H-20),fill=(0,0,0),width=4); d.text((20,H-40),'500 m',fill=(0,0,0))
im.save(out); print(W,H)
