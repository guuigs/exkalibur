import numpy as np,math
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy');fd=np.load('fdir.npy')
jx,jy=T.transform(6.040299,45.422426)
# cellules 2 m de cours d'eau (acc>2000 cellules ~0.8 ha) dans 700 m
ny,nx=acc.shape
r=int((YN-jy)/2);c=int((jx-X0)/2);R=350
sub=acc[r-R:r+R,c-R:c+R]
ys,xs=np.where(sub>3000)
mv={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
out=[]
for yy,xx in zip(ys,xs):
  R0,C0=yy+r-R,xx+c-R
  # descendre 6 cellules (12 m)
  rr,cc=R0,C0;L=0
  for _ in range(5):
    d=mv.get(int(fd[rr,cc]));
    if d is None: break
    rr+=d[0];cc+=d[1];L+=2*(1.414 if d[0] and d[1] else 1)
  X=X0+C0*2+1;Y=YN-R0*2-1;X2=X0+cc*2+1;Y2=YN-rr*2-1
  z1=mnt[int(YN-Y),int(X-X0)];z2=mnt[int(YN-Y2),int(X2-X0)]
  if L>0 and (z1-z2)/L>0.45: out.append((round((z1-z2)/L,2),round(z1-z2,1),X,Y,int(acc[R0,C0])))
out.sort(reverse=True)
seen=[]
for s,dz,X,Y,a in out:
  if any(math.hypot(X-p,Y-q)<25 for p,q in seen): continue
  seen.append((X,Y));lo,la=Ti.transform(X,Y)
  db=float(np.min(np.hypot(B[:,0]-X,B[:,1]-Y)))
  print(f'{la:.6f},{lo:.6f} pente {s} chute {dz} m /~10 m, acc {a}, jonction {math.hypot(X-jx,Y-jy):.0f} m, maisons {db:.0f} m')
  if len(seen)>=15: break
