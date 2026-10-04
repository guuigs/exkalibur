import json,math,pickle,numpy as np,os
from scipy import ndimage
from shapely.geometry import shape
from shapely import contains_xy
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
Vm=np.unpackbits(np.load('vs_muraille.npy'))[:N*N].reshape(N,N).astype(bool)
Vs=np.unpackbits(np.load('vs_muraille_sol.npy'))[:N*N].reshape(N,N).astype(bool)
acc=np.load('acc.npy')
C=pickle.load(open('PUB_cat.pkl','rb'))
R=5;n=N//R
xs=X0+(np.arange(n)+0.5)*R;ys=YN-(np.arange(n)+0.5)*R;XX,YY=np.meshgrid(xs,ys)
pub=contains_xy(C['PUBSUR'],XX,YY);dou=contains_xy(C['NC_autre'],XX,YY)
def rast_pts(P):
  m=np.zeros((n,n),bool);c=((P[:,0]-X0)/R).astype(int);r=((YN-P[:,1])/R).astype(int);k=(c>=0)&(c<n)&(r>=0)&(r<n);m[r[k],c[k]]=True;return m
bm=rast_pts(np.array(B));bdist=ndimage.distance_transform_edt(~bm)*R
def line_pts(fn):
  pts=[]
  for f in json.load(open(fn))['features']:
    g=shape(f['geometry'])
    for l in getattr(g,'geoms',[g]):
      L=l.length
      for s in np.arange(0,L,2): p=l.interpolate(s);pts.append((p.x,p.y))
  return np.array(pts)
rdist=ndimage.distance_transform_edt(~rast_pts(line_pts('large/troncon_de_route.json')))*R
wdist=ndimage.distance_transform_edt(~rast_pts(line_pts('large/troncon_hydrographique.json')))*R
coffre_sur=pub&(bdist>=100)&(rdist<=30)
coffre_dou=(pub|dou)&(bdist>=100)&(rdist<=30)
np.save('run/coffre_sur.npy',coffre_sur)
Pd=60
coffre_sur_p=np.pad(coffre_sur,Pd);coffre_dou_p=np.pad(coffre_dou,Pd)
px,py=936955.34,6485599.51
yy,xx=np.mgrid[-60:61,-60:61];disk60=(xx**2+yy**2)<=60**2
yr,xr=np.mgrid[-200:201,-200:201];ring=((xr**2+yr**2)>=60**2)&((xr**2+yr**2)<=200**2)
d5=int(300/R);yk,xk=np.mgrid[-d5:d5+1,-d5:d5+1];disk300=(xk**2+yk**2)<=d5**2
rows=[]
for m in M:
  x,y,deg=m[0],m[1],m[2]
  if deg<3: continue
  d=math.hypot(x-px,y-py)
  if d<200 or d>3000: continue
  r1,c1=int(YN-y),int(x-X0)
  if r1<210 or c1<210 or r1>N-210 or c1>N-210: continue
  H=mnh[r1-60:r1+61,c1-60:c1+61];op=(H<1.5)&disk60
  vm=int((Vm[r1-60:r1+61,c1-60:c1+61]&op).sum());vs=int((Vs[r1-60:r1+61,c1-60:c1+61]&op).sum())
  vpt=int(Vm[r1-10:r1+11,c1-10:c1+11].sum())
  op30=float((mnh[r1-30:r1+31,c1-30:c1+31]<1.5).mean());fo=float((mnh[r1-200:r1+201,c1-200:c1+201][ring]>5).mean())
  r5,c5=int((YN-y)/R),int((x-X0)/R)
  hb=float(bdist[r5,c5]);wd=float(wdist[r5,c5])
  ta=float(acc[r1//2-20:r1//2+21,c1//2-20:c1//2+21].max())*4/1e4
  cs=int((coffre_sur_p[r5+Pd-d5:r5+Pd+d5+1,c5+Pd-d5:c5+Pd+d5+1][disk300]).sum())*R*R
  cd=int((coffre_dou_p[r5+Pd-d5:r5+Pd+d5+1,c5+Pd-d5:c5+Pd+d5+1][disk300]).sum())*R*R
  lo,la=Ti.transform(x,y);az=G.inv(6.03101,45.42887,lo,la)[0]%360
  rows.append(dict(la=la,lo=lo,d=d,az=az,deg=deg,nat=sorted(set(m[4])),hb=hb,vm=vm,vs=vs,vpt=vpt,op=op30,fo=fo,wd=wd,ta=ta,cs=cs,cd=cd))
pickle.dump(rows,open('run/crible_rows.pkl','wb'))
print('croisements analysés :',len(rows))
