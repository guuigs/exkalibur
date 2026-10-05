import json,gzip,math,pickle,numpy as np,glob
from shapely.geometry import shape,Point,LineString
from shapely.ops import transform as stf
from shapely.strtree import STRtree
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51
LD=[]
for fn in ['ld.json.gz']+sorted(glob.glob('cad/ld_*.json.gz')):
    d=json.load(gzip.open(fn))
    for f in d['features']:
        g=stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0)
        if g.distance(Point(TX,TY))<=6000: LD.append((f['properties'].get('nom'),g))
geoms=[g for n,g in LD];tree=STRtree(geoms)
def series(x,y,az,maxd=4500):
    lo0,la0=Ti.transform(x,y)
    line=LineString([T.transform(*G.fwd(lo0,la0,az,d)[:2]) for d in np.arange(0,maxd,5)])
    seq=[]
    for i in tree.query(line):
        it=geoms[i].intersection(line)
        if not it.is_empty and it.length>5:
            pts=[Point(c) for gg in getattr(it,'geoms',[it]) for c in gg.coords]
            seq.append((min(line.project(p) for p in pts),i))
    seq.sort();return seq
starts={'centre tour':(TX,TY)}
for k in range(8):
    a=math.radians(k*45);starts['mur %d°'%(k*45)]=(TX+14*math.sin(a),TY+14*math.cos(a))
rr=[(45.42976,6.03176),(45.42972,6.03139),(45.42964,6.03107),(45.42951,6.03100),(45.42938,6.03101),(45.42908,6.03081)]
for i,(la,lo) in enumerate(rr): starts['Rue du Rempart %d'%(i+1)]=T.transform(lo,la)
AZ={'30/04 plat 68.6':68.6,'30/04 vis 73.9':73.9,'Pâques 2023 vis 90.2':90.2,'Pâques 2025 vis 81.7':81.7,'équinoxe vis 104':104.0,'1524 jul 27/03 vis 99.4':99.4}
for an,az in AZ.items():
    print('\n== azimut',an)
    for sn,(x,y) in starts.items():
        s=series(x,y,az)
        if len(s)<11: print('  ',sn,'<11');continue
        g3,g11=geoms[s[2][1]],geoms[s[10][1]]
        dd=g3.centroid.distance(g11.centroid)
        print('  %-18s 3e=%-26s 11e=%-26s %5.0f m (%+.1f %%) %s'%(sn,LD[s[2][1]][0],LD[s[10][1]][0],dd,100*(dd/1850-1),'<<<' if abs(dd-1850)<=18.5 else ''))
