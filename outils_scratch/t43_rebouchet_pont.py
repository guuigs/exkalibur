import json,math,numpy as np
from scipy import ndimage
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0].startswith(('1','2','3','4'))])
PUB=unary_union([NC,PU])
rd=[(shape(f['geometry']),f['properties'].get('nature')) for f in json.load(open('wfs_troncon_de_route.json'))['features']]
reb=unary_union([shape(f['geometry']) for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if (f['properties'].get('cpx_toponyme_de_cours_d_eau') or '')=='Ruisseau de Rebouchet'])
jx,jy=T.transform(6.03829,45.426344);J=Point(jx,jy)
s0=reb.project(J) if reb.geom_type=='LineString' else None
from shapely.ops import linemerge
L=linemerge(reb) if reb.geom_type!='LineString' else reb
lines=list(getattr(L,'geoms',[L]))
ln=min(lines,key=lambda g:g.distance(J));s0=ln.project(J)
print('ligne Rebouchet',round(ln.length),'m ; position du pont',round(s0))
z0=lambda q:mnt[int(YN-q.y),int(q.x-X0)]
# déterminer le sens amont
a=ln.interpolate(max(0,s0-50));b=ln.interpolate(min(ln.length,s0+50));up=1 if z0(b)>z0(a) else -1
print('amont = sens',up)
for k in range(-6,26):
  s=s0+up*k*20
  if s<0 or s>ln.length: continue
  q=ln.interpolate(s);R,C=int(YN-q.y),int(q.x-X0)
  D=mnt[R-8:R+9,C-8:C+9].astype(float);bump=float((D-ndimage.gaussian_filter(D,3)).max())
  q2=ln.interpolate(min(ln.length,max(0,s+up*10)));slope=(z0(q2)-z0(q))/10*100
  near=sorted((round(g.distance(q)),n) for g,n in rd if g.distance(q)<40)[:2]
  db=float(np.min(np.hypot(B[:,0]-q.x,B[:,1]-q.y)));lo,la=Ti.transform(q.x,q.y)
  print(f'{k*20:+5d} m | {la:.6f},{lo:.6f} | z {z0(q):.0f} | pente lit {slope:+.0f} % | saillie {bump:.1f} m | chemins {near} | maisons {db:.0f} m | vu pied ±10 {int(Vp[R-10:R+11,C-10:C+11].sum())} | public {PUB.distance(q):.0f} m | arbres {float(np.percentile(mnh[R-15:R+16,C-15:C+16],70)):.0f} m')
