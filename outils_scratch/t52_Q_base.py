import json,math,numpy as np
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vs=np.unpackbits(np.load('vs_sommet.npy'))[:N*N].reshape(N,N).astype(bool)
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0][:1] in '1234'])
FP=unary_union([shape(f['geometry']) for f in json.load(open('wfs_foret_publique.json'))['features']])
PUB=unary_union([NC,PU,FP])
tap=unary_union([shape(f['geometry']) for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if 'Tapon' in (f['properties'].get('cpx_toponyme_de_cours_d_eau') or '')])
Hy=unary_union([shape(f['geometry']) for f in json.load(open('wfs_troncon_hydrographique.json'))['features']])
J={'J5':(6.054780,45.426948),'E2a':(6.055758,45.429069),'E2b':(6.055896,45.428916)}
for o,lab in ((91.4,'Pâques 1524'),(93.0,'Pâques 2026'),(95.78,'axe Machrie')):
  for sn,st in (('pied',(6.03115,45.42887)),('sommet',(6.03101275,45.4288723))):
    lo,la,_=G.fwd(st[0],st[1],o,1850);x,y=T.transform(lo,la)
    print(f'{lab:12s} {sn:6s} 1 850 m -> {la:.6f},{lo:.6f} | '+' | '.join(f'{k} {math.hypot(x-T.transform(*v)[0],y-T.transform(*v)[1]):.0f} m' for k,v in J.items()))
print()
for k,(lo,la) in J.items():
  x,y=T.transform(lo,la);P=Point(x,y);R,C=int(YN-y),int(x-X0)
  m=min(M,key=lambda m:math.hypot(m[0]-x,m[1]-y))
  print(f'{k}: deg {m[2]} {sorted(set(m[4]))} | ouvert ±15 {float((mnh[R-15:R+16,C-15:C+16]<1.5).mean()):.2f} ±30 {float((mnh[R-30:R+31,C-30:C+31]<1.5).mean()):.2f} | forêt anneau {float((mnh[R-150:R+151,C-150:C+151]>5).mean()):.2f} | Tapon {tap.distance(P):.0f} m, eau {Hy.distance(P):.0f} m | maisons {float(np.min(np.hypot(B[:,0]-x,B[:,1]-y))):.0f} m | public : dedans={PUB.contains(P)}, à {PUB.distance(P):.0f} m, {PUB.intersection(P.buffer(30)).area:.0f} m² à ≤30 m | vu sommet ±30 {int(Vs[R-30:R+31,C-30:C+31].sum())} pied {int(Vp[R-30:R+31,C-30:C+31].sum())}')
