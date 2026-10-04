import numpy as np,math
src=open('t45_horizon.py').read().split("hz={a:horizon")[0]
exec(src)
cr,ccn=3400.49,3955.34
pts={}
for a in range(0,360,11):
  best=None
  for r in np.arange(6,18,0.5):
    y=cr-r*math.cos(math.radians(a));x=ccn+r*math.sin(math.radians(a))
    h=mnh[int(round(y)),int(round(x))]
    if 1.2<=h<=4.5: best=(X0+x,YN-y,float(mnt[int(y),int(x)]+h+1.7))
  if best: pts[a]=best
K=(6.059095,45.434748);kx,ky=T.transform(*K)
def sunrise(doy,vx,vy,vz):
  global ox,oy,oz
  ox,oy,oz=vx,vy,vz
  dec=decl(doy)
  for h10 in range(-10,400):
    h=h10/10;az=sun_az(dec,h);hb,_=horizon(az)
    if h>=hb: return az,h
cases=[('centre tour',(X0+ccn,YN-cr,float(mnt[int(cr),int(ccn)])+1.7)),('muraille NO (az 308, point qui voit le Couvet)',pts[308])]
dates=[('30/04 grégorien (2026)',120),('30/04/1524 julien = 10/05 grég.',130),('Pâques 2026 05/04',95),('Pâques 1524 06/04 grég.',97),('1er mai',121),('29/04',119)]
for nm,(vx,vy,vz) in cases:
  lo,la=Ti.transform(vx,vy);azK=G.inv(lo,la,*K)[0]%360;dK=G.inv(lo,la,*K)[2]
  print(f'== {nm} : Couvet au cap vrai {azK:.2f}°, {dK:.0f} m')
  for dn,doy in dates:
    az,h=sunrise(doy,vx,vy,vz);print(f'   lever visible {dn}: az {az:.1f}°, h {h:.1f}° -> écart avec le Couvet {az-azK:+.1f}°')
# quel jour le soleil se lève-t-il pile derrière le Couvet ?
vx,vy,vz=pts[308];lo,la=Ti.transform(vx,vy);azK=G.inv(lo,la,*K)[0]%360
for doy in range(100,140):
  az,h=sunrise(doy,vx,vy,vz)
  if abs(az-azK)<0.8: print('jour (n° dans l année)',doy,'az',round(az,2),'h',round(h,1))
