import json,gzip,math,numpy as np
from shapely.geometry import shape,Point,LineString
from shapely.ops import transform as stf
from shapely.strtree import STRtree
exec(open('ring1068.py').read().split('out=[]')[0])
ld=json.load(gzip.open('ld.json.gz'))
LD=[(f['properties'].get('nom'),stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0)) for f in ld['features']]
geoms=[g for n,g in LD];tree=STRtree(geoms)
cr,ccn=3400.49,3955.34;lo0,la0=Ti.transform(X0+ccn,YN-cr)
res=[]
for AZ in np.arange(0,360,0.5):
  line=LineString([T.transform(*G.fwd(lo0,la0,AZ,d)[:2]) for d in np.arange(0,4000,5)])
  seq=[]
  for i in tree.query(line):
    it=geoms[i].intersection(line)
    if not it.is_empty and it.length>5:
      pts=[Point(c) for gg in getattr(it,'geoms',[it]) for c in gg.coords]
      seq.append((min(line.project(p) for p in pts),i))
  seq.sort()
  if len(seq)>=13:
    d=geoms[seq[2][1]].centroid.distance(geoms[seq[10][1]].centroid)
    res.append((AZ,d,LD[seq[2][1]][0],LD[seq[10][1]][0],len(seq)))
ok=[r for r in res if abs(r[1]-1850)<=18.5]
print('caps avec ≥13 lieux-dits traversés :',len(res),'/ 720 ; dont 3e→11e à 10 stades ±1 % :',len(ok))
for r in ok: print('  cap %.1f° : %.0f m  3e %s  11e %s  (%d traversés)'%r)
