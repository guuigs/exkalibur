import json,math,numpy as np,networkx as nx
from shapely.geometry import LineString,Point
exec(open('ring1068.py').read().split('out=[]')[0])
r=json.load(open('wfs_troncon_de_route.json'));key=lambda c:(round(c[0]/3),round(c[1]/3))
Gr=nx.Graph()
for f in r['features']:
  cs=[c[:2] for c in f['geometry']['coordinates']];L=sum(math.dist(cs[i],cs[i+1]) for i in range(len(cs)-1))
  Gr.add_edge(key(cs[0]),key(cs[-1]),w=L,geom=cs,nat=f['properties']['nature'])
reb=[f for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if (f['properties'].get('cpx_toponyme_de_cours_d_eau') or '')=='Ruisseau de Rebouchet']
segs=[]
for f in reb:
  cs=f['geometry']['coordinates']
  if cs[0][2]<cs[-1][2]: cs=cs[::-1]
  segs+=list(zip(cs,cs[1:]))
def bank(x,y):
  best=None
  for a,b in segs:
    dx,dy=b[0]-a[0],b[1]-a[1];L=dx*dx+dy*dy;t=max(0,min(1,((x-a[0])*dx+(y-a[1])*dy)/L)) if L else 0
    px,py=a[0]+t*dx,a[1]+t*dy;d=math.hypot(x-px,y-py);cr=dx*(y-a[1])-dy*(x-a[0])
    if best is None or d<best[0]: best=(d,'G' if cr>0 else 'd')
  return best
jx,jy=T.transform(6.040299,45.422426);J=min(Gr.nodes,key=lambda n:math.hypot(n[0]*3-jx,n[1]*3-jy));print('nœud départ à',round(math.hypot(J[0]*3-jx,J[1]*3-jy)),'m')
for nm,(la,lo) in {'cul-de-sac A (roche 207 m²)':(45.414182,6.051137),'cul-de-sac B (sentier)':(45.416809,6.049903)}.items():
  tx,ty=T.transform(lo,la);tgt=min(Gr.nodes,key=lambda n:math.hypot(n[0]*3-tx,n[1]*3-ty))
  try:
    L,pth=nx.single_source_dijkstra(Gr,J,tgt,weight='w')
  except Exception as e: print(nm,'pas de chemin',e);continue
  geo=[]
  for a,b in zip(pth,pth[1:]):
    g=Gr[a][b]['geom'];g=g if key(g[0])==a else g[::-1];geo+=g
  line=LineString(geo);eu=math.dist(T.transform(6.040299,45.422426),T.transform(lo,la))
  print(f'\n{nm}: {L:.0f} m par les chemins (vol d\'oiseau {eu:.0f} m), z {z(mnt,*geo[0]):.0f} -> {z(mnt,*geo[-1]):.0f}')
  for s in range(0,int(line.length)+1,100):
    p=line.interpolate(s);d,side=bank(p.x,p.y);db=float(np.min(np.hypot(B[:,0]-p.x,B[:,1]-p.y)))
    print(f'   {s:5d} m : Rebouchet à {d:4.0f} m rive {side} | maisons {db:4.0f} m | z {z(mnt,p.x,p.y):.0f}')
  x,y=T.transform(lo,la);print('   bout du chemin : Rebouchet',bank(x,y))
