import numpy as np,math
from pyproj import Transformer
T=Transformer.from_crs(4326,2154,always_xy=True)
X0,YN,N=933000,6489000,7000
mnt=np.load('mnt.npy').astype(np.float32);mnh=np.clip(np.nan_to_num(np.load('mnh.npy')),0,60).astype(np.float32)
dsm=mnt+mnh
def vs(lat,lon,eye,name):
  x0,y0=T.transform(lon,lat);r0,c0=YN-y0,x0-X0;z0=mnt[int(r0),int(c0)]+eye
  nr=14000;L=4300
  V=np.zeros((N,N),bool);VG=np.zeros((N,N),bool)
  for k0 in range(0,nr,1000):
    az=np.linspace(0,2*np.pi,nr,endpoint=False)[k0:k0+1000];s=np.arange(15,L,1.0)
    rr=(r0-np.outer(np.cos(az),s));cc=(c0+np.outer(np.sin(az),s))
    ok=(rr>=0)&(rr<N-1)&(cc>=0)&(cc<N-1);ri=np.clip(rr.astype(int),0,N-1);ci=np.clip(cc.astype(int),0,N-1)
    ang_obs=(dsm[ri,ci]-z0)/s;tg=(mnt[ri,ci]+1.5-z0)/s;tgT=(dsm[ri,ci]-z0)/s
    mp=np.maximum.accumulate(np.concatenate([np.full((len(az),1),-1e9),ang_obs[:,:-1]],1),axis=1)
    vis=(tg>=mp)&ok;V[ri[vis],ci[vis]]=True
  np.save(f'vs_{name}.npy',np.packbits(V))
  print(name,'cellules (1 m) au sol visibles :',int(V.sum()))
vs(45.42887,6.03115,1.7,'pied')
vs(45.4288723,6.03101275,33.0,'sommet')
