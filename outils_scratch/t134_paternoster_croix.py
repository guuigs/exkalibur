import json,gzip,math,pickle,glob,numpy as np
from shapely.geometry import shape,Point
from shapely.ops import transform as stf
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51;tlo,tla=Ti.transform(TX,TY)
S=1850/8
rows=pickle.load(open('run/rows_final2.pkl','rb'))
d=json.load(open('osm.json'));nodes=d['nodes']
names=[]
for pid,(la,lo),tags in d['pois']:
    if tags.get('name'): x,y=T.transform(lo,la);names.append((x,y,tags['name'],'osm'))
for w in d['ways']:
    n=w[2].get('name')
    if n:
        pts=[nodes[str(i)] for i in w[1] if str(i) in nodes]
        if pts: la=sum(p[0] for p in pts)/len(pts);lo=sum(p[1] for p in pts)/len(pts);x,y=T.transform(lo,la);names.append((x,y,n,'voie'))
for fn in ['ld.json.gz']+sorted(glob.glob('cad/ld_*.json.gz')):
    for f in json.load(gzip.open(fn))['features']:
        g=stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).centroid;names.append((g.x,g.y,f['properties']['nom'],'ld'))
def near(x,y,R=150):
    L=sorted((math.hypot(x-a,y-b),n,s) for a,b,n,s in names if math.hypot(x-a,y-b)<=R)
    seen=set();o=[]
    for dd,n,s in L:
        if n.lower() in seen: continue
        seen.add(n.lower());o.append('%s(%d)'%(n,dd))
    return ', '.join(o[:7])
print('pas s = %.2f m'%S)
for lab,az_s in (('30/04 plat 68.6',68.6),('30/04 visible 73.9',73.9),('Pâques 2025 plat 73.0',73.0)):
    axis=az_s+90
    print('\n== orientation',lab,': axe de la croix %.1f° / %.1f°'%(axis%360,(axis+180)%360))
    for k,nm in ((1,'N (jonction, 1 pas)'),(-2,'T3 (3e, 2 pas au nord)'),(6,'R11 (11e, 6 pas au sud)'),(2,'S8'),(-4,'P1')):
        dd=k*S;a=axis if dd>0 else axis+180
        lo,la=G.fwd(tlo,tla,a%360,abs(dd))[:2];x,y=T.transform(lo,la)
        J=min(rows,key=lambda r:math.hypot(r['x']-x,r['y']-y));dj=math.hypot(J['x']-x,J['y']-y)
        print('  %-26s %5.0f m cap %.1f° : %.5f,%.5f | jonction ≥3 voies la + proche %.0f m (%.5f,%.5f) | %s'%(nm,abs(dd),a%360,la,lo,dj,J['la'],J['lo'],near(x,y)))
