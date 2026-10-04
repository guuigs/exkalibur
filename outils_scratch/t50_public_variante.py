import json,math,numpy as np
from shapely.geometry import shape,Point
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy');fd=np.load('fdir.npy')
mv={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
NC=shape(json.load(open('cad/noncad.json'))).buffer(0.5)
rd=[(shape(f['geometry']),f['properties'].get('nature')) for f in json.load(open('wfs_troncon_de_route.json'))['features']]
J=np.array(T.transform(6.040299,45.422426))
r0,c0=int((YN-J[1])/2),int((J[0]-X0)/2);Rw=220  # fenêtre ±440 m (cellules 2 m)
cells={}
# eau reliée : (a) cellules dont l'écoulement passe à ≤15 m de la jonction (amont) ; (b) aval de la jonction sur 400 m
def walk(r,c,maxL=900):
  L=0;out=[(r,c,0)]
  while L<maxL:
    d=mv.get(int(fd[r,c]))
    if d is None: break
    r+=d[0];c+=d[1];L+=2*(1.414 if d[0] and d[1] else 1);out.append((r,c,L))
  return out
for r in range(r0-Rw,r0+Rw):
  for c in range(c0-Rw,c0+Rw):
    if acc[r,c]<1500: continue
    path=walk(r,c,700)
    for (rr,cc,L) in path:
      X=X0+cc*2+1;Y=YN-rr*2-1
      if math.hypot(X-J[0],Y-J[1])<=15: cells[(r,c)]=('amont',L);break
# aval
w=acc[r0-8:r0+9,c0-8:c0+9];ys,xs=np.where(w>=1500)
if len(ys):
  k=np.argmin(np.hypot(ys-8,xs-8));for_r,for_c=r0-8+ys[k],c0-8+xs[k]
  for (rr,cc,L) in walk(for_r,for_c,400): cells.setdefault((rr,cc),('aval',L))
print('cellules d eau reliées à la jonction :',len(cells))
res=[]
for (r,c),(sens,L) in cells.items():
  X=X0+c*2+1;Y=YN-r*2-1;lo,la=Ti.transform(X,Y)
  for pas in (0.65,0.75,1.48):
    lo1,la1,_=G.fwd(lo,la,0,10*pas);lo1,la1,_=G.fwd(lo1,la1,90,10*pas)
    for jd in (90.0,91.4,93.0,67.7):
      lo2,la2,_=G.fwd(lo1,la1,jd,8*pas);x,y=T.transform(lo2,la2);P=Point(x,y)
      if NC.contains(P):
        db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))
        res.append((sens,round(L),round(math.hypot(X-J[0],Y-J[1])),round(la,6),round(lo,6),pas,jd,round(la2,6),round(lo2,6),round(db),int(acc[r,c])))
print('combinaisons roche (sur l eau reliée) -> coffre en bande publique :',len(res))
seen={}
for r_ in sorted(res,key=lambda t:(t[0],t[2])):
  key=(r_[0],r_[2]//15)
  if key in seen: continue
  seen[key]=1
  print(f'{r_[0]:5s} | roche à {r_[2]:3d} m de la jonction ({r_[3]},{r_[4]}, bassin {r_[10]*4/10000:.1f} ha) | pas {r_[5]} jour {r_[6]} -> COFFRE {r_[7]},{r_[8]} | maisons {r_[9]} m')
json.dump(res,open('t50_res.json','w'))
