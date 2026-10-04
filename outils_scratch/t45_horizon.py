import numpy as np,math
exec(open('ring1068.py').read().split('out=[]')[0])
A=np.fromfile('alti_large.bil','<f4').reshape(2000,2000);AX0,AYN,res=916000,6516000,25.0
def z(x,y):
  c=(x-AX0)/res-0.5;r=(AYN-y)/res-0.5
  if not(0<=c<1999 and 0<=r<1999): return np.nan
  c0,r0=int(c),int(r);fc,fr=c-c0,r-r0
  return (A[r0,c0]*(1-fc)*(1-fr)+A[r0,c0+1]*fc*(1-fr)+A[r0+1,c0]*(1-fc)*fr+A[r0+1,c0+1]*fc*fr)
ox,oy=T.transform(6.03115,45.42887);oz=float(mnt[int(YN-oy),int(ox-X0)])+1.7
print('oeil pied',round(oz,1),'m')
R=6371000;k=0.13
def horizon(az_true):
  azg=math.radians(az_true+2.2)  # cap grille
  best=-90;bd=0
  for d in np.arange(200,24000,25):
    x=ox+d*math.sin(azg);y=oy+d*math.cos(azg);h=z(x,y)
    if np.isnan(h): break
    drop=d*d*(1-k)/(2*R)
    ang=math.degrees(math.atan2(h-drop-oz,d))
    if ang>best: best,bd=ang,d
  return best,bd
phi=math.radians(45.42887)
def decl(doy):  # Spencer
  g=2*math.pi/365*(doy-1)
  return math.degrees(0.006918-0.399912*math.cos(g)+0.070257*math.sin(g)-0.006758*math.cos(2*g)+0.000907*math.sin(2*g)-0.002697*math.cos(3*g)+0.00148*math.sin(3*g))
def sun_az(dec,h):
  d=math.radians(dec);hh=math.radians(h)
  c=(math.sin(d)-math.sin(phi)*math.sin(hh))/(math.cos(phi)*math.cos(hh))
  return math.degrees(math.acos(max(-1,min(1,c))))
hz={a:horizon(a) for a in np.arange(40,140,0.5)}
for nm,doy in (('30/04/1524 julien = 10/05 grégorien',130),('30/04 grégorien',120),('équinoxe',80),('solstice d été',172)):
  dec=decl(doy)
  # trajectoire matinale : altitude h croissante, azimut sun_az(dec,h) ; premier h où h > horizon(az)
  for h10 in range(-10,400):
    h=h10/10;az=sun_az(dec,h+0.0)
    hb,dd=hz[round(az*2)/2] if 40<=az<140 else (-90,0)
    if h>=hb:
      print(f'{nm} : déclinaison {dec:.2f}° ; lever astronomique az {sun_az(dec,-0.83):.1f}° ; lever VISIBLE au-dessus du relief : az {az:.1f}°, hauteur {h:.1f}° (relief à {dd/1000:.1f} km)');break
for a in range(55,121,5): print('horizon',a,'°:',round(hz[a][0],2),'° à',round(hz[a][1]/1000,1),'km')
