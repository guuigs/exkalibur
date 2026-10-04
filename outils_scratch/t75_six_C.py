import math,itertools
from pyproj import Geod
g=Geod(ellps='WGS84')
C=[('Clairvaux',(4.7883,48.1467)),('Cîteaux',(5.0936,47.1289)),('Cluny',(4.6585012,46.4348054)),('Clermont',(3.0858573,45.7787583)),('Chartres',(1.4875,48.447778)),('Grande Chartreuse',(5.7936,45.3647))]
print('Segments (ordre de découverte) :')
segs=[]
for (n1,a),(n2,b) in zip(C,C[1:]+C[:1]):
  f,bk,d=g.inv(*a,*b);segs.append((n1,n2,f%360,d));print(f'  {n1:17s} → {n2:17s} cap {f%360:6.2f}°  {d/1000:6.1f} km')
print('Angles internes (ordre de découverte) :')
for i in range(6):
  n1,n2,f1,d1=segs[i-1];_,_,f2,_=segs[i]
  arr=(g.inv(*C[i][1],*C[i-1][1])[0])%360
  ang=(f2-arr)%360
  print(f'  en {C[i][0]:17s} : {ang:6.2f}°  (ou {360-ang:6.2f}°)')
# toutes les paires
print('Toutes les paires (cap, distance) :')
for (n1,a),(n2,b) in itertools.combinations(C,2):
  f,bk,d=g.inv(*a,*b);print(f'  {n1:17s} – {n2:17s} {f%360:6.2f}° / {(bk+180)%360:6.2f}°  {d/1000:6.1f} km')
