import numpy as np,json,math
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0].startswith(('1','2','3','4'))])
PUB=unary_union([NC,PU])
x,y=T.transform(6.041837,45.424003)
print('roche C dans domaine public :',PUB.contains(Point(x,y)),' dist public',round(PUB.distance(Point(x,y)),1),'m')
for pas in (0.75,1.48):
  for nm,brg in (('90',90),('67.6',67.6),('72.4',72.4)):
    dx=10*pas+8*pas*math.sin(math.radians(brg+2.2));dy=10*pas+8*pas*math.cos(math.radians(brg+2.2))
    p=Point(x+dx,y+dy);lo,la=Ti.transform(p.x,p.y)
    db=float(np.min(np.hypot(B[:,0]-p.x,B[:,1]-p.y)))
    print(f'pas {pas} cap {nm}: {la:.6f},{lo:.6f} public={PUB.contains(p)} (dist bande {PUB.distance(p):.1f} m) maisons {db:.0f} m')
