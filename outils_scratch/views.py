import numpy as np, math
from pyproj import Transformer
X0,Y0,N=933000,6482000,7000
mnt=np.load('mnt.npy'); mnh=np.clip(np.nan_to_num(np.load('mnh.npy')),0,60)
# 2 m grid
g=2; M=mnt.reshape(N//g,g,N//g,g).mean((1,3)); H=mnh.reshape(N//g,g,N//g,g).max((1,3))
dsm=M+H; n=N//g
tr=Transformer.from_crs(4326,2154,always_xy=True)
def rc(lon,lat):
    x,y=tr.transform(lon,lat); return (Y0+N-y)/g,(x-X0)/g
obs={'tour_sommet':(6.03101275,45.4288723,None),'rue_rempart':(6.03118,45.42977,1.7)}
out={}
for name,(lon,lat,h) in obs.items():
    r0,c0=rc(lon,lat); z0=M[int(r0),int(c0)]
    z0= (mnt[int(r0*g),int(c0*g)]+33.0) if h is None else z0+h
    print(name,'z0',z0)
    nr=12000; L=int(4000/g)
    az=np.linspace(0,2*np.pi,nr,endpoint=False)
    s=np.arange(1,L)*1.0
    rr=r0-np.outer(np.cos(az),s); cc=c0+np.outer(np.sin(az),s)
    ok=(rr>=0)&(rr<n-1)&(cc>=0)&(cc<n-1)
    ri=np.clip(rr.astype(int),0,n-1); ci=np.clip(cc.astype(int),0,n-1)
    dist=s*g
    ang_obs=(dsm[ri,ci]-z0)/dist          # obstacle tangent
    tgt=(M[ri,ci]+1.5-z0)/dist            # ground target tangent
    maxprev=np.maximum.accumulate(np.concatenate([np.full((nr,1),-1e9),ang_obs[:,:-1]],1),axis=1)
    vis=(tgt>=maxprev)&ok
    V=np.zeros((n,n),bool); V[ri[vis],ci[vis]]=True
    out[name]=V; print(name,'visible cells',V.sum())
np.savez_compressed('viewsheds.npz',**out)
np.save('M2.npy',M); np.save('H2.npy',H)
