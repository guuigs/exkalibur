import json, math, sys
sys.path.insert(0,'.')
from geo import inv, direct
C=tuple(map(float,sys.argv[1:3])) if len(sys.argv)>2 else (45.429083,6.030808)
R=1.85; TOL=0.0185
def lines(g):
    t=g['type']; c=g['coordinates']
    return [c] if t=='LineString' else (c if t=='MultiLineString' else [])
# densify streams and find points in ring
hyd=json.load(open('troncon_hydrographique.json'))
hits=[]
for f in hyd:
    p=f['properties']
    name=p.get('cpx_toponyme_de_cours_d_eau') or ''
    for l in lines(f['geometry']):
        for (a,b) in zip(l,l[1:]):
            n=max(1,int(inv((a[1],a[0]),(b[1],b[0]))[0]*1000/5))
            for k in range(n+1):
                lo=a[0]+(b[0]-a[0])*k/n; la=a[1]+(b[1]-a[1])*k/n
                d,az=inv(C,(la,lo))
                if abs(d-R)<=TOL: hits.append((round(az),name,p.get('persistance'),p.get('nature'),round(la,5),round(lo,5),round(d,3)))
# cluster by azimuth & name
seen={}
for h in hits:
    key=(h[0]//3,h[1])
    seen.setdefault(key,h)
for k,h in sorted(seen.items()):
    print('az %4d  %-35s %-12s %-18s %.5f %.5f d=%.3f'%h)
