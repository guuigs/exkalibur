import json,math,numpy as np,datetime as dt
exec(open('table_orient.py').read().split('r=1068')[0])
J=(45.422426,6.040299);jx,jy=T.transform(J[1],J[0])
Xr,Yr=T.transform(6.03118,45.42977);Zr=z(mnt,Xr,Yr)+1.7
obs={'sommet tour (+33 m)':(X0t,Y0t,Zs),'pied tour (1,7 m)':(Xp,Yp,Zp),'Rue du Rempart (1,7 m)':(Xr,Yr,Zr)}
print('== 1. VISIBILITÉ du croisement (point au sol +1,5 m)')
for k,(a,b,c) in obs.items():
  print(f'  {k}: relief {los(a,b,c,jx,jy,False):+.1f} m | avec arbres {los(a,b,c,jx,jy,True):+.1f} m (négatif = visible)')
print('  zones ouvertes (sans arbre) visibles, par rayon autour du croisement :')
for R in (30,60,100,150):
  n=0;v={k:0 for k in obs}
  for dx in range(-R,R+1,6):
    for dy in range(-R,R+1,6):
      if math.hypot(dx,dy)>R or z(mnh,jx+dx,jy+dy)>=1.5: continue
      n+=1
      for k,(a,b,c) in obs.items(): v[k]+= los(a,b,c,jx+dx,jy+dy,True)<0
  print(f'   ≤{R} m : {n} cellules ouvertes ; visibles : '+', '.join(f'{k.split(" (")[0]} {v[k]}' for k in obs))
# nearest visible open cell from foot
best=None
for dx in range(-200,201,4):
  for dy in range(-200,201,4):
    if z(mnh,jx+dx,jy+dy)>=1.5: continue
    d=math.hypot(dx,dy)
    if best and d>=best: continue
    if los(Xp,Yp,Zp,jx+dx,jy+dy,True)<0: best=d
print(f'  zone ouverte visible du PIED la plus proche du croisement : {best:.0f} m')
print('\n== 2. CROISEMENT réel')
for dd,m in sorted([(math.hypot(m[0]-jx,m[1]-jy),m) for m in M],key=lambda t:t[0])[:2]: print(f'  {dd:.0f} m : {m[2]} branches, source {m[3]}, {m[4]}')
print('\n== 3. CLAIRIÈRE')
for R in (15,30,50):
  print(f'  part sans arbre ≤{R} m : {np.mean([z(mnh,jx+a,jy+b)<2 for a in range(-R,R+1,2) for b in range(-R,R+1,2) if math.hypot(a,b)<=R]):.2f}')
print(f'  forêt entre 60 et 150 m : {np.mean([z(mnh,jx+a,jy+b)>5 for a in range(-150,151,6) for b in range(-150,151,6) if 60<=math.hypot(a,b)<=150]):.2f}')
print('\n== 4. MAISONS',f'{float(np.min(np.hypot(B[:,0]-jx,B[:,1]-jy))):.0f} m du croisement')
for nm,(la,lo) in {'affleurement 45.423544,6.04383':(45.423544,6.04383),'affleurement 45.42252,6.044485':(45.42252,6.044485),'affleurement 45.421319,6.045054':(45.421319,6.045054)}.items():
  x,y=T.transform(lo,la);print(f'  {nm} : maisons à {float(np.min(np.hypot(B[:,0]-x,B[:,1]-y))):.0f} m')
print('\n== 5. FORÊT PUBLIQUE / statut')
fp=json.load(open('wfs_foret_publique.json'))
from shapely.geometry import shape,Point
pt=Point(jx,jy);hit=[f['properties'] for f in fp['features'] if shape(f['geometry']).buffer(0).distance(pt)<300]
print('  forêts publiques à < 300 m :',[(p.get('toponyme') or p.get('nom'),p.get('nature')) for p in hit][:5] or 'aucune')
print('\n== 6. SOLEIL DU MATIN (horizon LiDAR vu du croisement et du ruisseau)')
src=open('/home/user/exkalibur/outils_scratch/t21_lever_soleil.py').read()
exec(src.split("hz=json.load")[0]);exec('lat,lon=45.42,6.04\n'+src.split("lat,lon=45.4288723,6.03101275")[1].split('res=[]')[0])
def horizon(x,y,zh):
  hz={}
  for az in range(40,181,2):
    a=math.radians(az+2.2);best=-90
    for s in range(20,6900,6):
      X=x+s*math.sin(a);Y=y+s*math.cos(a)
      if not(X0<X<X0+7000 and YN-7000<Y<YN): break
      best=max(best,math.degrees(math.atan2(z(mnt,X,Y)-zh-s*s/(2*6371000)*0.87,s)))
    hz[az]=best
  return hz
def sunreach(x,y,label):
  zh=z(mnt,x,y)+1.5;hz=horizon(x,y,zh);A=np.array(sorted(hz));Hh=np.array([hz[a] for a in A])
  for lab,day in [('30 avril',dt.date(2026,4,30)),('10 mai',dt.date(2026,5,10)),('21 juin',dt.date(2026,6,21))]:
    jd0=2451544.5+(day-dt.date(2000,1,1)).days;res=None
    for m in range(3*60,12*60):
      alt,az,dec=sunpos(jd0+m/1440)
      if az<40 or az>180: continue
      if alt+refr(alt)>=np.interp(az,A,Hh): res=(m,az);break
    t=f'{(res[0]//60+2)%24}h{res[0]%60:02d} (heure légale), soleil au cap {res[1]:.0f}°' if res else 'pas avant midi'
    print(f'  {label} — {lab} : soleil au sol à {t}')
sunreach(jx,jy,'croisement')
x,y=T.transform(6.04383,45.423544);sunreach(x,y,'ruisseau (rive gauche, 45.4235,6.0438)')
print('\n== 7. RUISSEAU visible depuis le rempart ?')
for la,lo in [(45.423544,6.04383),(45.4240,6.04245),(45.4227,6.0447)]:
  x,y=T.transform(lo,la)
  print(f'  {la},{lo} : '+', '.join(f'{k.split(" (")[0]} relief {los(a,b,c,x,y,False):+.1f} arbres {los(a,b,c,x,y,True):+.1f}' for k,(a,b,c) in obs.items()))
