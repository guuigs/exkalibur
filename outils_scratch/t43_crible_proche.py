import json,math,numpy as np
from scipy import ndimage
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
acc=np.load('acc.npy');fd=np.load('fdir.npy')
mv={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
px,py=T.transform(6.03115,45.42887)
# ressauts : cellule 2 m de cours d'eau (acc>2000 = 0,8 ha), chute sur 10 m aval > 4 m
ST=acc>2000
ys,xs=np.where(ST)
kp=[]
for r,c in zip(ys,xs):
  rr,cc,L=r,c,0
  for _ in range(5):
    d=mv.get(int(fd[rr,cc]))
    if d is None: break
    rr+=d[0];cc+=d[1];L+=2*(1.414 if d[0] and d[1] else 1)
  if L==0: continue
  X=X0+c*2+1;Y=YN-r*2-1;X2=X0+cc*2+1;Y2=YN-rr*2-1
  if not(X0+100<X<X0+6900 and YN-6900<Y<YN-100): continue
  dz=mnt[int(YN-Y),int(X-X0)]-mnt[int(YN-Y2),int(X2-X0)]
  if dz>=4: kp.append((X,Y,dz,int(acc[r,c])))
kp=np.array(kp);print('ressauts (chute ≥4 m sur ~10 m) :',len(kp))
out=[]
for m in M:
  x,y=m[0],m[1];R,C=int(YN-y),int(x-X0)
  if not(X0+200<x<X0+6800 and YN-6800<y<YN-200): continue
  # eau à moins de 30 m
  r2,c2=int((YN-y)/2),int((x-X0)/2)
  if not ST[r2-15:r2+16,c2-15:c2+16].any(): continue
  dk=np.hypot(kp[:,0]-x,kp[:,1]-y);sel=dk<150
  if not sel.any(): continue
  yy,xx=np.mgrid[-80:81,-80:81];disk=(xx**2+yy**2)<=6400
  vis=int((Vp[R-80:R+81,C-80:C+81]&(mnh[R-80:R+81,C-80:C+81]<1.5)&disk).sum())
  if vis<30: continue
  i=np.argmax(np.where(sel,kp[:,2],-1));kx,ky,kdz,ka=kp[i]
  dbk=float(np.min(np.hypot(B[:,0]-kx,B[:,1]-ky)));dbj=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))
  lo,la=Ti.transform(x,y);klo,kla=Ti.transform(kx,ky)
  out.append((round(math.hypot(x-px,y-py)),round(la,6),round(lo,6),vis,round(dbj),round(dk[i]),round(kla,6),round(klo,6),round(kdz,1),ka,round(dbk),m[2],','.join(sorted(set(m[4])))[:40]))
print('croisements : eau ≤30 m, ressaut ≤150 m, pré ouvert vu du pied ≥30 m² à ≤80 m :',len(out))
for o in sorted(out): print('tour %d m | J %s,%s | vu %d m² | maisons J %d m | ressaut à %d m : %s,%s chute %.1f m acc %d | maisons ressaut %d m | deg %d %s'%o)
