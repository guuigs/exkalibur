import json,math,numpy as np,networkx as nx
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
Vs=np.unpackbits(np.load('vs_sommet.npy'))[:N*N].reshape(N,N).astype(bool)
r=json.load(open('wfs_troncon_de_route.json'));key=lambda c:(round(c[0]/3),round(c[1]/3))
Gr=nx.Graph()
for f in r['features']:
  cs=[c[:2] for c in f['geometry']['coordinates']];L=sum(math.dist(cs[i],cs[i+1]) for i in range(len(cs)-1))
  Gr.add_edge(key(cs[0]),key(cs[-1]),w=L,geom=cs)
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
pubs=[(stf(lambda a,b,c=None:T.transform(a,b),shape(f['geometry'])).buffer(0),own[f['properties']['id']][1]) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0].startswith(('1','2','3','4'))]
hyd=[(shape(f['geometry']),f['properties'].get('cpx_toponyme_de_cours_d_eau'),f['properties'].get('persistance')) for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if f['geometry']['type']=='LineString']
res=json.load(open('deadend_rock.json'))
for steep,la,lo,nat,dw,db,dd,az in res[:13]:
  x,y=T.transform(lo,la);n0=key((x,y))
  if n0 not in Gr: print('nœud absent',la,lo);continue
  dist,paths=nx.single_source_dijkstra(Gr,n0,weight='w',cutoff=1500)
  js=sorted([(dist[n],n) for n in paths if Gr.degree(n)>=3],key=lambda t:t[0])[:3]
  p=Point(x,y);pub=[nm for g,nm in pubs if g.distance(p)<5]
  hn=min(hyd,key=lambda t:t[0].distance(p))
  print(f'\nCUL-DE-SAC {la},{lo} ({nat}) | roche {steep} m² | eau {dw} m : {hn[1]} ({hn[2]}) | public : {pub[0] if pub else "non"} | tour {dd} m cap {az}°')
  for dl,n in js:
    jx,jy=n[0]*3,n[1]*3;r0,c0=int(YN-jy),int(jx-X0)
    yy,xx=np.mgrid[-60:61,-60:61];disk=(xx**2+yy**2)<=3600;op=mnh[r0-60:r0+61,c0-60:c0+61]<1.5
    vp=int((Vp[r0-60:r0+61,c0-60:c0+61]&op&disk).sum());vs=int((Vs[r0-60:r0+61,c0-60:c0+61]&op&disk).sum())
    jlo,jla=Ti.transform(jx,jy);dbj=float(np.min(np.hypot(B[:,0]-jx,B[:,1]-jy)))
    print(f'   croisement à {dl:.0f} m par le chemin : {jla:.6f},{jlo:.6f} deg {Gr.degree(n)} | ouvert 60 m {int((op&disk).sum())} m², vu sommet {vs}, pied {vp} | maisons {dbj:.0f} m')
