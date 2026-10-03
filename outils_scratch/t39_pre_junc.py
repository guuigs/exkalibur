import numpy as np,json,math
from shapely.geometry import shape,Point,LineString
exec(open('ring1068.py').read().split('out=[]')[0])
PIED=(45.42887,6.03115);Xp,Yp=T.transform(PIED[1],PIED[0]);Zp=z(mnt,Xp,Yp)+1.7
X0t,Y0t=T.transform(6.03101275,45.4288723);Zs=z(mnt,X0t,Y0t)+33
rav=LineString([T.transform(*c) for c in json.load(open('ravin_B0071.json'))])
mx,my=T.transform(6.04751,45.42773)
for dd,m in sorted([(math.hypot(m[0]-mx,m[1]-my),m) for m in M],key=lambda t:t[0])[:8]:
  lo,la=Ti.transform(m[0],m[1]);db=float(np.min(np.hypot(B[:,0]-m[0],B[:,1]-m[1])))
  n=vp=vs=0
  for a in range(-40,41,5):
    for b in range(-40,41,5):
      if math.hypot(a,b)>40 or z(mnh,m[0]+a,m[1]+b)>=1.5: continue
      n+=1;vp+=los(Xp,Yp,Zp,m[0]+a,m[1]+b,True)<0;vs+=los(X0t,Y0t,Zs,m[0]+a,m[1]+b,True)<0
  print(f'{dd:4.0f} m du pré : {la:.6f},{lo:.6f} | {m[2]} br {m[4][:3]} | maisons {db:.0f} | ravin à {rav.distance(Point(m[0],m[1])):.0f} m | ouvert à 40 m : {n}, vus pied {vp}, sommet {vs} | relief pied {los(Xp,Yp,Zp,m[0],m[1],False):+.1f}')
