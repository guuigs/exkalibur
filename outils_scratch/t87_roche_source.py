import pickle,math,numpy as np
from scipy import ndimage
from shapely.geometry import Point
from shapely.ops import unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy');B_=np.array(B)
D=pickle.load(open('run/mouret_cad.pkl','rb'));NC=unary_union(pickle.load(open('run/mouret_nc.pkl','rb')))
SRC=Point(*T.transform(6.04019,45.42177));J=Point(*T.transform(6.040299,45.422426));sud=D['sud']
res=[]
for dx in range(-60,61,2):
  for dy in range(-60,121,2):
    x,y=SRC.x+dx,SRC.y+dy;p=Point(x,y)
    if p.distance(J)<15: continue
    onwater=acc[int((YN-y)/2),int((x-X0)/2)]*4>=3000 or p.distance(SRC)<=8
    onpath=sud.distance(p)<=4
    if not (onwater or onpath): continue
    lo,la=Ti.transform(x,y);good={}
    for jd in (90.0,91.4,93.0):
      ok=True;cf=None
      for pas in (0.65,0.75):
        l1,a1,_=G.fwd(lo,la,0,10*pas);l1,a1,_=G.fwd(l1,a1,90,10*pas);l2,a2,_=G.fwd(l1,a1,jd,8*pas)
        q=Point(*T.transform(l2,a2));hb=float(np.min(np.hypot(B_[:,0]-q.x,B_[:,1]-q.y)))
        if not(NC.contains(q) and hb>=100): ok=False
        cf=(a2,l2,hb)
      good[jd]=(ok,cf)
    if all(v[0] for v in good.values()):
      R,C=int(YN-y),int(x-X0);Dm=mnt[R-6:R+7,C-6:C+7].astype(float);bump=float((Dm-ndimage.gaussian_filter(Dm,2.5)).max())
      res.append((p.distance(J),la,lo,'eau' if onwater else '',('sentier' if onpath else ''),p.distance(SRC),bump,good[90.0][1]))
print('positions de roche → coffre dans la bande publique (pas 0,65 et 0,75 ; jour dernier 90/91,4/93°) :',len(res))
for r in sorted(res)[:25]:
  print(f'roche à {r[0]:3.0f} m de la jonction, {r[5]:3.0f} m de la source : {r[1]:.6f},{r[2]:.6f} [{r[3]} {r[4]}] saillie +{r[6]:.1f} | coffre(0,75 ; 90°) {r[7][0]:.6f},{r[7][1]:.6f} maisons {r[7][2]:.0f} m')
pickle.dump(res,open('run/roches_pub.pkl','wb'))
