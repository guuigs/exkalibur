import json,math,numpy as np
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0].startswith(('1','2','3','4'))])
PUB=unary_union([NC,PU])
H=[shape(f['geometry']) for f in json.load(open('wfs_troncon_hydrographique.json'))['features']]
def info(lo,la,tag):
  x,y=T.transform(lo,la);P=Point(x,y)
  inside=X0+100<x<X0+6900 and YN-6900<y<YN-100
  db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))
  dw=min(g.distance(P) for g in H)
  js=sorted((math.hypot(m[0]-x,m[1]-y),m) for m in M)[:2]
  s=f'{tag}: {la:.6f},{lo:.6f} | maisons {db:.0f} m | eau {dw:.0f} m'
  if inside:
    R,C=int(YN-y),int(x-X0)
    yy,xx=np.mgrid[-80:81,-80:81];dk=(xx**2+yy**2)<=6400
    s+=f' | ouvert ±30 {float((mnh[R-30:R+31,C-30:C+31]<1.5).mean()):.2f} | forêt anneau {float((mnh[R-150:R+151,C-150:C+151]>5).mean()):.2f} | vu pied r80 {int((Vp[R-80:R+81,C-80:C+81]&dk).sum())} m²'
  for dj,m in js:
    lo2,la2=Ti.transform(m[0],m[1]);s+=f'\n      croisement à {dj:.0f} m : {la2:.6f},{lo2:.6f} deg {m[2]} {",".join(sorted(set(m[4])))[:45]}'
  return s
starts={'pied':(6.03115,45.42887),'sommet':(6.03101275,45.4288723)}
for sn,(slo,sla) in starts.items():
  for A in (63.7,67.6,72.4,90.0):
    print(f'=== départ {sn}, soleil {A}° (dos du Christ) ; rangée {(A-90)%360:.1f}° / {(A+90)%360:.1f}°')
    for seat,sgn,dist in ((3,-1,925),(11,+1,925),(13,+1,1387.5)):
      az=(A+sgn*90)%360;lo,la,_=G.fwd(slo,sla,az,dist)
      print('  ',info(lo,la,f'place {seat} (cap {az:.1f}°, {dist:.0f} m)'))
