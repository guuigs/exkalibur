import numpy as np,math,json,pickle
src=open('t45_horizon.py').read().split("hz={a:horizon")[0]
exec(src)
from shapely.geometry import shape,Point
from shapely.ops import unary_union
PUB=unary_union([pickle.load(open('PUB_general.pkl','rb')),shape(json.load(open('cad/noncad.json')))]).buffer(0)
cr,ccn=3400.49,3955.34
K=(6.059095,45.434748);kx,ky=T.transform(*K)
def sunrise(doy,vx,vy,vz):
  global ox,oy,oz
  ox,oy,oz=vx,vy,vz;dec=decl(doy)
  for h10 in range(-10,400):
    h=h10/10;az=sun_az(dec,h);hb,_=horizon(az)
    if h>=hb: return az,h
S=1850/8
print('pas de la rangée',round(S,2),'m ; 11e à',10*S,'m ; 13e à',12*S,'m ; 3e à',2*S,'m')
for a in (0,44,88,132,176,220,264,308):
  r=12
  y=cr-r*math.cos(math.radians(a));x=ccn+r*math.sin(math.radians(a));vx,vy=X0+x,YN-y;vz=float(mnt[int(y),int(x)])+1.7
  lo,la=Ti.transform(vx,vy)
  out=[]
  for doy in (119,120,121):
    az,h=sunrise(doy,vx,vy,vz)
    l11,a11,_=G.fwd(lo,la,az,10*S);x11,y11=T.transform(l11,a11)
    out.append(f'{doy}: az {az:.2f} 11e à {math.hypot(x11-kx,y11-ky):.0f} m du Couvet')
  print(f'muraille az {a:3d}° :',' | '.join(out))
