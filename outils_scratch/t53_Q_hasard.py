import math,numpy as np
exec(open('ring1068.py').read().split('out=[]')[0])
st=(6.03115,45.42887)
Ma=np.array([[m[0],m[1],m[2]] for m in M],float)
def hit(o,dmax,deg):
  lo,la,_=G.fwd(st[0],st[1],o,1850);x,y=T.transform(lo,la)
  s=Ma[Ma[:,2]>=deg];d=np.hypot(s[:,0]-x,s[:,1]-y);return d.min()
for deg in (3,4,5):
  for dm in (33,50):
    a=np.array([hit(o,dm,deg) for o in np.arange(0,360,0.1)])
    b=np.array([hit(o,dm,deg) for o in np.arange(85,100.01,0.1)])
    print(f'deg>={deg} ≤{dm} m : tour complet {(a<=dm).mean()*100:.1f} % | secteur 85-100° {(b<=dm).mean()*100:.1f} %')
print('nb jonctions deg>=5 :',int((Ma[:,2]>=5).sum()),' entre 1700-2000 m :',sum(1 for m in M if m[2]>=5 and 1700<math.hypot(m[0]-T.transform(*st)[0],m[1]-T.transform(*st)[1])<2000))
