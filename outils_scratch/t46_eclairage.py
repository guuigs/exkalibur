import numpy as np,math
exec(open('t45_horizon.py').read().split("hz={a:")[0])
def sun_alt_az_series(dec):
  # trajectoire du matin : pour h de -1 à 30°
  out=[]
  for h10 in range(-10,300):
    h=h10/10;out.append((h,sun_az(dec,h)))
  return out
def lit(lon,lat,h,az,eye=0.5):
  x,y=T.transform(lon,lat)
  try: z0=float(mnt[int(YN-y),int(x-X0)])+eye
  except Exception: z0=z(x,y)+eye
  azg=math.radians(az-2.2)
  for d in np.arange(30,24000,25):
    xx=x+d*math.sin(azg);yy=y+d*math.cos(azg)
    hh=z(xx,yy)
    if np.isnan(hh): break
    drop=d*d*(1-k)/(2*R)
    if math.degrees(math.atan2(hh-drop-z0,d))>h: return False
  return True
dec=decl(97)
traj=sun_alt_az_series(dec)
# instant où le soleil apparaît depuis le rempart
t_r=None
for i,(h,az) in enumerate(traj):
  if lit(6.03115,45.42887,h,az,eye=1.7): t_r=i;break
print('soleil visible du rempart : h',traj[t_r][0],'az',round(traj[t_r][1],1))
for nm,lo,la in (('pré visible du Mouret',6.039049,45.422482),('jonction du Mouret',6.040299,45.422426),('source / Simon',6.04019,45.42177),('pont du Rebouchet',6.03829,45.426344),('ruisseau vu du pied',6.038836,45.426236),('J5 (loup)',6.054780,45.426948)):
  t=None
  for i,(h,az) in enumerate(traj):
    if lit(lo,la,h,az): t=i;break
  dt=(traj[t][0]-traj[t_r][0]) if t is not None else None
  print(f'{nm:24s} éclairé à partir de h={traj[t][0] if t is not None else None}° (az {round(traj[t][1],1) if t is not None else None}) ; écart avec le rempart : {dt}° de hauteur (~{round(dt*60/11.5) if dt is not None else None} min)')
