import json,gzip,math,pickle,numpy as np
from shapely.geometry import shape,Point,LineString
from shapely.ops import transform as stf
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51;tlo,tla=Ti.transform(TX,TY)
rows=pickle.load(open('run/rows_final.pkl','rb'))
j2=[r for r in rows if abs(r['la']-45.42337)<2e-5 and abs(r['lo']-6.04166)<2e-5][0]
print('J2',j2['la'],j2['lo'],'d',j2['d'],'az vrai',j2['az'],'az Lambert',j2['az']-2.2)
ld=json.load(gzip.open('ld.json.gz'));LDg=[(f['properties'].get('nom'),stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0)) for f in ld['features']]
def series(az,maxd=3400):
  line=LineString([T.transform(*G.fwd(tlo,tla,az,d)[:2]) for d in range(0,maxd,20)])
  seq=[]
  for n,g in LDg:
    it=g.intersection(line)
    if not it.is_empty and it.length>0:
      pts=[Point(c) for gg in getattr(it,'geoms',[it]) for c in gg.coords];seq.append((min(line.project(p) for p in pts),max(line.project(p) for p in pts),n))
  return sorted(seq)
az0=j2['az']
for az in (az0,):
  s=series(az);print('azimut',round(az,2))
  for i,(a,b,n) in enumerate(s,1): print(i,n,int(a),int(b))
