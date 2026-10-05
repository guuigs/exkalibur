import json,gzip,math,pickle,numpy as np
from shapely.geometry import shape,Point,LineString
from shapely.ops import transform as stf
exec(open('ring1068.py').read().split('out=[]')[0])
rows=pickle.load(open('run/rows_final.pkl','rb'))
ld=json.load(gzip.open('ld.json.gz'))
LD=[(f['properties'].get('nom'),stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0)) for f in ld['features']]
TX,TY=936955.34,6485599.51;tlo,tla=Ti.transform(TX,TY)
def series(az):
  line=LineString([T.transform(*G.fwd(tlo,tla,az,d)[:2]) for d in np.arange(0,4000,5)])
  seq=[]
  for n,g in LD:
    it=g.intersection(line)
    if not it.is_empty and it.length>5:
      pts=[Point(c) for gg in getattr(it,'geoms',[it]) for c in gg.coords]
      seq.append((min(line.project(p) for p in pts),n,g,it.length))
  seq.sort();return seq
for az in (73.9,75.0,90.2,91.4,103.0,104.0):
  s=series(az)
  if len(s)<11: print(az,'<11');continue
  g3,g11=s[2][2],s[10][2];d=g3.centroid.distance(g11.centroid)
  print('\n=== az %.1f : 3e=%s, 11e=%s, centroïdes %.0f m (%+.1f %%) ; 13e=%s'%(az,s[2][1],s[10][1],d,100*(d/1850-1),s[12][1] if len(s)>12 else None))
  print('   série :',' · '.join('%d %s'%(i+1,n) for i,(a,n,g,l) in enumerate(s[:14])))
  poly=g11.buffer(60)
  J=[r for r in rows if poly.contains(Point(r['x'],r['y']))]
  for r in sorted(J,key=lambda r:r['d']):
    print('   jonction %.5f,%.5f %dm cap %.0f deg %d | maison %d eau %d ta %.1f open %.2f for %.2f vu %d cs %d'%(r['la'],r['lo'],r['d'],r['az'],r['deg'],r['hb'],r['wd'],r['ta'],r['op'],r['fo'],max(r['vs'],r['vm']),r['cs']))
