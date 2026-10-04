import json,math,numpy as np
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
J=np.array(T.transform(6.054780,45.426948))
r0,c0=int((YN-J[1])/2),int((J[0]-X0)/2)
print('talweg LiDAR le plus proche de J5 :',end=' ')
w=acc[r0-60:r0+61,c0-60:c0+61];ys,xs=np.where(w>1500);dd=np.hypot(ys-60,xs-60)*2;k=np.argmin(dd);print(round(dd[k]),'m, bassin',round(w[ys[k],xs[k]]*4/1e4,1),'ha')
res=[];Rw=230
for r in range(r0-Rw,r0+Rw):
  for c in range(c0-Rw,c0+Rw):
    if acc[r,c]<1500: continue
    X=X0+c*2+1;Y=YN-r*2-1;dJ=math.hypot(X-J[0],Y-J[1])
    if dJ>450: continue
    lo,la=Ti.transform(X,Y)
    for pas in (0.65,0.75,1.48):
      lo1,la1,_=G.fwd(lo,la,0,10*pas);lo1,la1,_=G.fwd(lo1,la1,90,10*pas)
      ok=[]
      for jd in (90.0,91.4,93.0,67.7):
        lo2,la2,_=G.fwd(lo1,la1,jd,8*pas);x,y=T.transform(lo2,la2)
        ok.append(PUB.contains(Point(x,y)))
      if all(ok): res.append((round(dJ),round(la,6),round(lo,6),pas,int(acc[r,c]),round(float(np.min(np.hypot(B[:,0]-X,B[:,1]-Y))))))
print('positions de roche sur l eau à ≤450 m de J5 dont le coffre est public pour TOUTES les lectures du jour dernier :',len(res))
from collections import Counter
print('répartition par distance à J5 (tranches de 50 m) :',sorted(Counter(r[0]//50*50 for r in res).items()))
for r in sorted(res)[:12]: print(f'  roche à {r[0]} m de J5 : {r[1]},{r[2]} | pas {r[3]} | bassin {r[4]*4/1e4:.1f} ha | maisons {r[5]} m')
json.dump(res,open('t52_res.json','w'))
