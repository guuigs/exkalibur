import numpy as np,math
src=open('t45_horizon.py').read().split("hz={a:horizon")[0]
exec(src)
from shapely.geometry import Point,LineString
J=T.transform(6.040299,45.422426);SRC=T.transform(6.04019,45.42177);PONT=T.transform(6.038836,45.426236)
cr,ccn=3400.49,3955.34
def sunrise(doy,vx,vy,vz):
  global ox,oy,oz
  ox,oy,oz=vx,vy,vz;dec=decl(doy)
  for h10 in range(-10,400):
    h=h10/10;az=sun_az(dec,h);hb,_=horizon(az)
    if h>=hb: return az
pts=[('centre de la tour',X0+ccn,YN-cr)]
for a in (0,90,180,270):
  y=cr-12*math.cos(math.radians(a));x=ccn+12*math.sin(math.radians(a));pts.append((f'muraille {a}°',X0+x,YN-y))
for nm,vx,vy in pts:
  vz=float(mnt[int(YN-vy),int(vx-X0)])+1.7;lo0,la0=Ti.transform(vx,vy)
  for dn,doy in (('Pâques 1524',97),('Pâques 2026',95)):
    O=sunrise(doy,vx,vy,vz)
    s11=T.transform(*G.fwd(lo0,la0,(O-(11-0.5)*30)%360,1068)[:2]);s3=T.transform(*G.fwd(lo0,la0,(O-(3-0.5)*30)%360,1068)[:2])
    ch=LineString([s3,s11])
    print(f'{nm:18s} {dn}: Orient {O:.1f}° | Simon → source {math.dist(s11,SRC):3.0f} m, jonction {math.dist(s11,J):3.0f} m | corde 3→11 : jonction à {ch.distance(Point(J)):3.0f} m, pont du Rebouchet à {ch.distance(Point(PONT)):3.0f} m')
