import json,math,numpy as np
from pyproj import Transformer
exec(open('ring1068.py').read().split('out=[]')[0])
BNG=Transformer.from_crs(27700,4326,always_xy=True)
ngr={'3':(191006,632457),'11':(191213,632426),'4':(191000,632350),'5':(190870,632340),'6':(190730,632370),'7':(190630,632530),
     '8':(190570,632370),'9':(190500,632400),'10':(190050,632650),'12':(191000,632400)}
prec={'3':1,'11':1,'4':10,'5':10,'6':10,'7':10,'8':10,'9':100,'10':10,'12':10}
mm={k:BNG.transform(*v) for k,v in ngr.items()}
vec={k:G.inv(mm['3'][0],mm['3'][1],*mm[k]) for k in mm if k!='3'}
sc=1850/vec['11'][2]
for k in ['4','5','6','7','8','9','10','12']:
  print(f'MM{k}: cap {vec[k][0]%360:6.1f}°, {vec[k][2]:5.0f} m sur Arran -> {vec[k][2]*sc:6.0f} m projeté (incertitude ±{prec[k]*sc*0.7:.0f} m)')
X0t,Y0t=T.transform(6.03101275,45.4288723);Zs=z(mnt,X0t,Y0t)+33
Xp,Yp=T.transform(6.03115,45.42887);Zp=z(mnt,Xp,Yp)+1.7
L=json.load(open('wfs_lieu_dit_non_habite.json'))['features']+json.load(open('wfs_toponymie.json'))['features']
def topo(x,y):
  b=[]
  for f in L:
    c=f['geometry']['coordinates']
    while isinstance(c[0],list): c=c[0]
    p=f['properties'];b.append((math.hypot(c[0]-x,c[1]-y),p.get('toponyme') or p.get('graphie_du_toponyme')))
  return min(b)
print()
for sn,(la,lo) in {'sommet':(45.4288723,6.03101275),'Rue du Rempart':(45.42977,6.03118)}.items():
  for k in ['4','5','6','7','8','9','10','12']:
    tl,ta,_=G.fwd(lo,la,vec[k][0],vec[k][2]*sc);x,y=T.transform(tl,ta)
    inside=X0+130<x<X0+6870 and YN-6870<y<YN-130
    t=topo(x,y) if inside or True else None
    if not inside:
      print(f'{sn:15s} MM{k}: {ta:.5f},{tl:.5f} hors zone LiDAR | lieu-dit le plus proche : {t[1]} ({t[0]:.0f} m)');continue
    j=min(M,key=lambda m:math.hypot(m[0]-x,m[1]-y));dj=math.hypot(j[0]-x,j[1]-y)
    db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))
    op=np.mean([z(mnh,x+a,y+b)<2 for a in range(-30,31,3) for b in range(-30,31,3) if math.hypot(a,b)<=30])
    ring=np.mean([z(mnh,x+a,y+b)>5 for a in range(-120,121,8) for b in range(-120,121,8) if 60<=math.hypot(a,b)<=120])
    vs=vp=n=0
    for a in range(-80,81,10):
      for b in range(-80,81,10):
        if math.hypot(a,b)>80 or z(mnh,x+a,y+b)>=1.5: continue
        n+=1;vs+=los(X0t,Y0t,Zs,x+a,y+b,True)<0;vp+=los(Xp,Yp,Zp,x+a,y+b,True)<0
    print(f'{sn:15s} MM{k}: {ta:.5f},{tl:.5f} | {t[1]} ({t[0]:.0f} m) | croisement {dj:.0f} m ({j[2]} br) | maisons {db:.0f} m | ouvert {op:.2f} forêt autour {ring:.2f} | zones ouvertes à 80 m : {n}, vues sommet {vs}, pied {vp}')
