import numpy as np,math,datetime
src=open('t45_horizon.py').read().split("hz={a:horizon")[0]
exec(src)
from shapely.geometry import Point,LineString
from dateutil.easter import easter
J1=T.transform(6.040299,45.422426);J2=T.transform(6.041663,45.423370);SRC=T.transform(6.04019,45.42177);PONT=T.transform(6.038836,45.426236);RES=T.transform(6.0417,45.423957)
cr,ccn=3400.49,3955.34
def sunrise(doy,vx,vy,vz):
  global ox,oy,oz
  ox,oy,oz=vx,vy,vz;dec=decl(doy)
  for h10 in range(-10,400):
    h=h10/10;az=sun_az(dec,h);hb,_=horizon(az)
    if h>=hb: return az,h
pts=[('centre',X0+ccn,YN-cr)]
for a in (0,90,180,270):
  yy=cr-12*math.cos(math.radians(a));xx=ccn+12*math.sin(math.radians(a));pts.append((f'mur{a}',X0+xx,YN-yy))
print('année | date de Pâques | Orient | place 11 → J1 / J2 / source / ressaut | corde 3→11 : J1 / J2 / pont Rebouchet / ressaut')
for yr in (2023,2024,2025,2026):
  e=easter(yr);doy=e.timetuple().tm_yday
  rr_=[]
  for nm,vx,vy in pts:
    vz=float(mnt[int(YN-vy),int(vx-X0)])+1.7;lo0,la0=Ti.transform(vx,vy)
    O=sunrise(doy,vx,vy,vz)[0]
    s11=T.transform(*G.fwd(lo0,la0,(O-10.5*30)%360,1068)[:2]);s3=T.transform(*G.fwd(lo0,la0,(O-2.5*30)%360,1068)[:2]);ch=LineString([s3,s11])
    rr_.append((O,math.dist(s11,J1),math.dist(s11,J2),math.dist(s11,SRC),math.dist(s11,RES),ch.distance(Point(J1)),ch.distance(Point(J2)),ch.distance(Point(PONT)),ch.distance(Point(RES))))
  a=np.array(rr_)
  print(f'{yr} | {e} | {a[:,0].min():.1f}-{a[:,0].max():.1f}° | J1 {a[:,1].min():.0f}-{a[:,1].max():.0f} m / J2 {a[:,2].min():.0f}-{a[:,2].max():.0f} m / source {a[:,3].min():.0f}-{a[:,3].max():.0f} m / ressaut {a[:,4].min():.0f}-{a[:,4].max():.0f} m | corde : J1 {a[:,5].min():.0f}-{a[:,5].max():.0f} / J2 {a[:,6].min():.0f}-{a[:,6].max():.0f} / pont {a[:,7].min():.0f}-{a[:,7].max():.0f} / ressaut {a[:,8].min():.0f}-{a[:,8].max():.0f} m')
