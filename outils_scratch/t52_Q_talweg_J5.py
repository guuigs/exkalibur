import json,math,numpy as np
from scipy import ndimage
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy');fd=np.load('fdir.npy')
mv={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0][:1] in '1234'])
FP=unary_union([shape(f['geometry']) for f in json.load(open('wfs_foret_publique.json'))['features']])
PUB=unary_union([NC,PU,FP]).buffer(0)
rd=[(shape(f['geometry']),f['properties'].get('nature'),round(shape(f['geometry']).length)) for f in json.load(open('wfs_troncon_de_route.json'))['features']]
tap=unary_union([shape(f['geometry']) for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if 'Tapon' in (f['properties'].get('cpx_toponyme_de_cours_d_eau') or '')])
J=np.array(T.transform(6.054780,45.426948))
r0,c0=int((YN-J[1])/2),int((J[0]-X0)/2);w=acc[r0-10:r0+11,c0-10:c0+11];ys,xs=np.where(w>1500);k=np.argmin(np.hypot(ys-10,xs-10));r,c=r0-10+ys[k],c0-10+xs[k]
L=0;last=-99
print(' m aval | position | z | pente lit | saillie | chemin (côté en descendant) | Tapon | coffre public (4 lectures, pas 0,65/0,75/1,48) | maisons')
prev=None
while L<420:
  X=X0+c*2+1;Y=YN-r*2-1
  if L-last>=12:
    last=L;lo,la=Ti.transform(X,Y);P=Point(X,Y);R,C=int(YN-Y),int(X-X0)
    D=mnt[R-6:R+7,C-6:C+7].astype(float);bump=float((D-ndimage.gaussian_filter(D,2.5)).max())
    d2=mv.get(int(fd[r,c]));
    ok=[]
    for pas in (0.65,0.75,1.48):
      lo1,la1,_=G.fwd(lo,la,0,10*pas);lo1,la1,_=G.fwd(lo1,la1,90,10*pas)
      ok.append(all(PUB.contains(Point(*T.transform(*G.fwd(lo1,la1,jd,8*pas)[:2]))) for jd in (67.7,90,91.4,93)))
    g,n,ln=min(rd,key=lambda t:t[0].distance(P));q=g.interpolate(g.project(P))
    # côté du chemin par rapport au sens de l'eau
    if d2: ux,uy=d2[1],-d2[0]; cr=ux*(q.y-Y)-uy*(q.x-X); side='chemin à GAUCHE de l eau' if cr>0 else 'chemin à droite de l eau'
    else: side='?'
    zz=mnt[R,C]
    print(f'{L:5.0f} | {la:.6f},{lo:.6f} | {zz:.0f} | {"":3s} | +{bump:.1f} m | {n} {ln} m à {g.distance(P):.0f} m ({side}) | {tap.distance(P):.0f} m | {"".join("✓" if o else "·" for o in ok)} | {float(np.min(np.hypot(B[:,0]-X,B[:,1]-Y))):.0f} m')
  d2=mv.get(int(fd[r,c]))
  if d2 is None: break
  r+=d2[0];c+=d2[1];L+=2*(1.414 if d2[0] and d2[1] else 1)
