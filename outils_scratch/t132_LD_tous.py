import json,gzip,math,pickle,numpy as np,glob
from shapely.geometry import shape,Point,LineString
from shapely.ops import transform as stf
from shapely.strtree import STRtree
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51;tlo,tla=Ti.transform(TX,TY)
LD=[]
for fn in ['ld.json.gz']+sorted(glob.glob('cad/ld_*.json.gz')):
    d=json.load(gzip.open(fn))
    for f in d['features']:
        g=stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0)
        if g.distance(Point(TX,TY))<=6000: LD.append((f['properties'].get('nom'),g,f['properties'].get('commune')))
print('lieux-dits utilisés (≤6 km) :',len(LD))
geoms=[g for n,g,c in LD];tree=STRtree(geoms)
def series(az,maxd=4500):
    line=LineString([T.transform(*G.fwd(tlo,tla,az,d)[:2]) for d in np.arange(0,maxd,5)])
    seq=[]
    for i in tree.query(line):
        it=geoms[i].intersection(line)
        if not it.is_empty and it.length>5:
            pts=[Point(c) for gg in getattr(it,'geoms',[it]) for c in gg.coords]
            seq.append((min(line.project(p) for p in pts),i))
    seq.sort();return seq
res=[]
for az in np.arange(0,360,0.25):
    s=series(az)
    if len(s)>=13:
        d=geoms[s[2][1]].centroid.distance(geoms[s[10][1]].centroid)
        res.append((az,d,LD[s[2][1]][0],LD[s[10][1]][0],len(s)))
ok=[r for r in res if abs(r[1]-1850)<=18.5]
print('caps avec >=13 lieux-dits :',len(res),'/ 1440 ; 3e→11e à 10 stades ±1 % :',len(ok),'(%.1f %%)'%(100*len(ok)/max(1,len(res))))
prev=None
for r in ok:
    if prev is None or r[0]-prev>0.6: print('  cap %.2f° : %.0f m  3e=%s  11e=%s (%d)'%r)
    prev=r[0]
pickle.dump(res,open('run/R_tous_LD.pkl','wb'))
