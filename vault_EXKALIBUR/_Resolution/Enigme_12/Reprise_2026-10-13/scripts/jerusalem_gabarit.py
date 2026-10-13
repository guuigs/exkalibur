import sys, json, math, numpy as np
sys.path.insert(0,'.')
from tiles import mosaic, deg2num
from PIL import Image, ImageDraw
from geographiclib.geodesic import Geodesic
G=Geodesic.WGS84
TA=(45.428888,6.031015)
KX=math.cos(math.radians(TA[0]))*111320.0; KY=111132.0
L=1850/math.hypot(1,0.25)
def ll(x,y): return (TA[0]+y/KY, TA[1]+x/KX)
# portes (Ap 21,13 : orient 1-3, nord 4-6, midi 7-9, occident 10-12)
gates={1:(L,-L/4),2:(L,0),3:(L,L/4),4:(3*L/4,L/2),5:(L/2,L/2),6:(L/4,L/2),7:(3*L/4,-L/2),8:(L/2,-L/2),9:(L/4,-L/2),10:(0,-L/4),11:(0,0),12:(0,L/4)}
corners=[(0,-L/2),(L,-L/2),(L,L/2),(0,L/2),(0,-L/2)]
lat0,lon0=ll(-150,-L/2-150); lat1,lon1=ll(L+150,L/2+150)
z=16
fn='jer_base.jpg'; mosaic('IGNF_LIDAR-HD_MNT_ELEVATION.ELEVATIONGRIDCOVERAGE.SHADOW','PM_0_18','image/png',z,lat0,lon0,lat1,lon1,fn)
im=Image.open(fn).convert('RGB'); d=ImageDraw.Draw(im)
x0,y0=deg2num(lat1,lon0,z)
def P(la,lo):
    x,y=deg2num(la,lo,z); return ((x-x0)*256,(y-y0)*256)
for f in json.load(open('troncon_hydrographique.json')):
    g=f['geometry']; ls=[g['coordinates']] if g['type']=='LineString' else g['coordinates']
    for l in ls: d.line([P(p[1],p[0]) for p in l],fill=(0,110,255),width=2)
d.line([P(*ll(*c)) for c in corners],fill=(200,0,0),width=3)
ring=[P(*(lambda q:(q['lat2'],q['lon2']))(G.Direct(*TA,a,1850))) for a in range(0,361)]
d.line(ring,fill=(255,140,0),width=2)
for k,(x,y) in gates.items():
    px,py=P(*ll(x,y)); r=7 if k in (3,11) else 4
    d.ellipse([px-r,py-r,px+r,py+r],fill=(255,0,0) if k in (3,11) else (120,0,0)); d.text((px+8,py-8),str(k),fill=(0,0,0))
for la,lo,lab in [(45.432881,6.054064,'jonction du Couvat'),(45.43360,6.04491,'Muraillat')]:
    px,py=P(la,lo); d.rectangle([px-5,py-5,px+5,py+5],outline=(0,150,0),width=3); d.text((px+8,py+4),lab,fill=(0,120,0))
im.save('jerusalem_celeste_terrain.jpg',quality=85); print(im.size)
