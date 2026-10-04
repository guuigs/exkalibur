import json,math
from shapely.geometry import shape,Point,MultiPoint
from shapely.ops import linemerge,unary_union
from shapely.strtree import STRtree
H=json.load(open('large/troncon_hydrographique.json'))['features']
R=json.load(open('large/troncon_de_route.json'))['features']+json.load(open('large/troncon_de_voie_ferree.json'))['features']
rg=[shape(f['geometry']) for f in R];rn=[(f['properties'].get('nature') or 'voie ferrée') for f in R]
tree=STRtree(rg)
px,py=936966.13,6485597.76
by={}
for f in H:
  n=f['properties'].get('cpx_toponyme_de_cours_d_eau') or f['properties'].get('cpx_toponyme')
  if n: by.setdefault(n,[]).append(shape(f['geometry']))
def flat(g):
  return list(getattr(g,'geoms',[g]))
res=[]
for n,gs in by.items():
  from shapely.geometry import LineString,MultiLineString
  ls=[LineString([c[:2] for c in L.coords]) for g in gs for L in flat(g)]
  m=linemerge(MultiLineString(ls))
  for L in flat(m):
    if L.length<1500: continue
    pts=[]
    for i in tree.query(L):
      it=L.intersection(rg[i])
      for p in flat(it):
        if p.geom_type=='Point': pts.append((L.project(p),rn[i],p))
    pts.sort(key=lambda t:t[0])
    cl=[]
    for t in pts:
      if cl and t[0]-cl[-1][0]<15: continue
      cl.append(t)
    for order in (cl,cl[::-1]):
      if len(order)>=13:
        a,b=order[2],order[10];d=a[2].distance(b[2])
        res.append((abs(d-1850),n,len(order),d,a,b,order is cl,order[12]))
res.sort(key=lambda r:r[0])
for r in res[:25]:
  e,n,N,d,a,b,fw,c13=r
  print(f'{n[:30]:30s} N={N:3d} d3-11={d:6.0f} m | 3e {a[1]} ({a[2].x:.0f},{a[2].y:.0f}) à {math.hypot(a[2].x-px,a[2].y-py):.0f} m tour | 11e {b[1]} ({b[2].x:.0f},{b[2].y:.0f}) à {math.hypot(b[2].x-px,b[2].y-py):.0f} m | sens {"géom" if fw else "inverse"}')
print('cours d eau testés:',len(by),'combinaisons ≥13 franchissements:',len(res))
