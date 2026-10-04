import json,gzip,math,numpy as np
from shapely.geometry import shape,Point,LineString
from shapely.ops import transform as stf
exec(open('ring1068.py').read().split('out=[]')[0])
ld=json.load(gzip.open('ld.json.gz'))
LD=[(f['properties'].get('nom'),stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0)) for f in ld['features']]
K=Point(*T.transform(6.059095,45.434748))
print('Couvet dans :',[n for n,g in LD if g.contains(K)],' le plus proche :',min(((g.distance(K),n) for n,g in LD))[1])
cr,ccn=3400.49,3955.34
for a in (308,0,132,220):
  r=12;y=cr-r*math.cos(math.radians(a));x=ccn+r*math.sin(math.radians(a));lo0,la0=Ti.transform(X0+x,YN-y)
  for AZ in (73.9,):
    line=LineString([T.transform(*G.fwd(lo0,la0,AZ,d)[:2]) for d in np.arange(0,3200,2)])
    seq=[]
    for n,g in LD:
      it=g.intersection(line)
      if not it.is_empty and it.length>0:
        seq.append((line.project(Point(it.coords[0]) if it.geom_type=='LineString' else Point(list(it.geoms)[0].coords[0])),n,it.length,g))
    seq.sort()
    print(f'-- muraille az {a}° :')
    for i,(d0,n,l,g) in enumerate(seq,1): print(f'  {i:2d}. {n:35s} entrée {d0:6.0f} m, traversée {l:5.0f} m')
    if len(seq)>=11:
      g3,g11=seq[2][3],seq[10][3];print('  centroïdes 3e→11e :',round(g3.centroid.distance(g11.centroid)),'m ; milieux des traversées 3e→11e :',round((seq[10][0]+seq[10][2]/2)-(seq[2][0]+seq[2][2]/2)),'m')
