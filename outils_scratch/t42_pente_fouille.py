import numpy as np,math
exec(open('ring1068.py').read().split('out=[]')[0])
def pente(la,lo,r=3):
  x,y=T.transform(lo,la);R,C=int(YN-y),int(x-X0)
  D=mnt[R-r-1:R+r+2,C-r-1:C+r+2].astype(float);gy,gx=np.gradient(D)
  return np.degrees(np.arctan(np.hypot(gx,gy)))[1:-1,1:-1]
for nm,la,lo in (('fouille A',45.42156,6.04558),('fouille B',45.42381,6.04168),('fouille C',45.424064,6.042013),('jonction',45.422426,6.040299),('rocher A',45.421452,6.045319)):
  p=pente(la,lo);print(f'{nm}: pente médiane {np.median(p):.0f}°, min {p.min():.0f}°, max {p.max():.0f}° ({math.tan(math.radians(np.median(p)))*100:.0f} %)')
# profil chemin de la jonction vers A (ligne droite) pente moyenne
x0,y0=T.transform(6.040299,45.422426);x1,y1=T.transform(6.045319,45.421452)
zs=[mnt[int(YN-(y0+(y1-y0)*t)),int(x0+(x1-x0)*t-X0)] for t in np.linspace(0,1,50)]
print('dénivelé jonction->A',round(zs[-1]-zs[0],1),'m sur',round(math.hypot(x1-x0,y1-y0)),'m')
