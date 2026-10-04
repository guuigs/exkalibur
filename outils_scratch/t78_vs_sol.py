import numpy as np,math
X0,YN,N=933000,6489000,7000
mnt=np.load('mnt.npy').astype(np.float32);mnh=np.clip(np.nan_to_num(np.load('mnh.npy')),0,60).astype(np.float32)
dsm=mnt+mnh
tx,ty=936966.13,6485597.76;r0,c0=int(YN-ty),int(tx-X0)
w=mnh[r0-20:r0+21,c0-20:c0+21];rr,cc=np.where(w>20);cr=r0-20+rr.mean();ccn=c0-20+cc.mean()
print('centre tour (ligne,col)',cr,ccn,'x,y',X0+ccn,YN-cr)
# muraille : pour chaque azimut, rayon (6-18 m) où mnh 1.5-4 m est maximal le plus à l'extérieur
pts=[]
for a in range(0,360,22):
  best=None
  for r in np.arange(6,18,0.5):
    y=cr-r*math.cos(math.radians(a));x=ccn+r*math.sin(math.radians(a))
    h=mnh[int(round(y)),int(round(x))]
    if 1.2<=h<=4.5: best=(r,y,x,h)
  if best: pts.append((a,)+best)
print('points de muraille trouvés',len(pts))
V=np.zeros((N,N),bool)
for a,r,y,x,h in pts:
  z0=mnt[int(y),int(x)]+1.7
  nr=12000;L=4300
  for k0 in range(0,nr,1000):
    az=np.linspace(0,2*np.pi,nr,endpoint=False)[k0:k0+1000];s=np.arange(3,L,1.0)
    R=(y-np.outer(np.cos(az),s));C=(x+np.outer(np.sin(az),s))
    ok=(R>=0)&(R<N-1)&(C>=0)&(C<N-1);ri=np.clip(R.astype(int),0,N-1);ci=np.clip(C.astype(int),0,N-1)
    ang=(dsm[ri,ci]-z0)/s;tg=(mnt[ri,ci]+1.5-z0)/s
    mp=np.maximum.accumulate(np.concatenate([np.full((len(az),1),-1e9),ang[:,:-1]],1),axis=1)
    vis=(tg>=mp)&ok&(s>=12);V[ri[vis],ci[vis]]=True
  print(f'az {a:3d}° r {r:.1f} m mur {h:.1f} m oeil {z0:.1f} -> cumul {int(V.sum())}',flush=True)
np.save('vs_muraille_sol.npy',np.packbits(V))
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
print('pied seul',int(Vp.sum()),' muraille (union)',int(V.sum()),' nouveau (vu de la muraille, pas du pied)',int((V&~Vp).sum()))
