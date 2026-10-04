import json,math,numpy as np
from shapely.geometry import shape,Point
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
Vs=np.unpackbits(np.load('vs_sommet.npy'))[:N*N].reshape(N,N).astype(bool)
px,py=T.transform(6.03115,45.42887)
res={}
for f in json.load(open('wfs_troncon_hydrographique.json'))['features']:
  g=shape(f['geometry']);p=f['properties']
  if g.geom_type!='LineString': continue
  n=(p.get('cpx_toponyme_de_cours_d_eau') or p.get('nature'))
  if n in ('Conduit forcé','Conduit buse','Canal'): continue
  for t in np.arange(0,g.length,3):
    q=g.interpolate(t);x,y=q.x,q.y
    if not(X0+20<x<X0+6980 and YN-6980<y<YN-20): continue
    R,C=int(YN-y),int(x-X0)
    vp=bool(Vp[R-2:R+3,C-2:C+3].any());vs=bool(Vs[R-2:R+3,C-2:C+3].any())
    if vp or vs:
      lo,la=Ti.transform(x,y);az,_,dd=G.inv(6.03115,45.42887,lo,la)
      k=(n,round(az%360/5)*5,round(dd/200)*200)
      e=res.setdefault(k,[0,0,la,lo,p.get('persistance'),1e9])
      e[0]+=vp;e[1]+=vs
      db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)));e[5]=min(e[5],db)
print('cours d eau | cap | dist | points vus pied | vus sommet | ex. lat,lon | persistance | maisons min')
for k,v in sorted(res.items(),key=lambda a:(a[0][2],a[0][1])):
  if v[0]>0: print(f'{k[0]} | {k[1]}° | {k[2]} m | {v[0]} | {v[1]} | {v[2]:.6f},{v[3]:.6f} | {v[4]} | {v[5]:.0f} m')
print('--- vus seulement du sommet (>=3 pts):')
for k,v in sorted(res.items(),key=lambda a:(a[0][2],a[0][1])):
  if v[0]==0 and v[1]>=3: print(f'{k[0]} | {k[1]}° | {k[2]} m | {v[1]} | {v[2]:.6f},{v[3]:.6f} | {v[4]} | {v[5]:.0f} m')
