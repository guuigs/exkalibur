import pickle,numpy as np
from scipy import ndimage
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vm=np.unpackbits(np.load('vs_muraille.npy'))[:N*N].reshape(N,N).astype(bool)
Vs=np.unpackbits(np.load('vs_muraille_sol.npy'))[:N*N].reshape(N,N).astype(bool)
op=(mnh[:N,:N]<1.5)&(Vm|Vs)
lab,k=ndimage.label(op);ar=np.bincount(lab.ravel());big=np.isin(lab,np.where(ar>=5000)[0][1:])
dt=ndimage.distance_transform_edt(~big)
rows=pickle.load(open('run/rows_final.pkl','rb'))
import math
res=[]
for r in rows:
    r1,c1=int(YN-r['y']),int(r['x']-X0);r['dl']=float(dt[r1,c1]) if 0<=r1<N and 0<=c1<N else 999;res.append(r)
sel=lambda f:[r for r in res if f(r)]
import itertools
for amin in (2000,5000,10000):
  big=np.isin(lab,np.where(ar>=amin)[0][1:]);dt=ndimage.distance_transform_edt(~big)
  for r in res:
    r1,c1=int(YN-r['y']),int(r['x']-X0);r['dl']=float(dt[r1,c1]) if 0<=r1<N and 0<=c1<N else 999
  for dmax in (40,60,100):
    for fmin in (0.2,0.3,0.5):
      S=[r for r in res if r['d']<=2000 and r['dl']<=dmax and r['hb']>=100 and (r['wd']<=150 or r['ta']>=1) and r['fo']>=fmin]
      print(amin,dmax,fmin,len(S),[ (round(r['la'],4),round(r['lo'],4)) for r in S][:6])
