import json,math,itertools,random,numpy as np
from shapely.geometry import shape,Point,LineString
exec(open('ring1068.py').read().split('out=[]')[0])
cr,ccn=3400.49,3955.34;TX,TY=X0+ccn,YN-cr
KEY=[]
for lay in ['zone_d_habitation','construction_ponctuelle','detail_hydrographique','cimetiere','detail_orographique']:
  for f in json.load(open(f'large/{lay}.json'))['features']:
    nat=f['properties'].get('nature') or '';top=f['properties'].get('toponyme') or ''
    if nat in ('Château','Croix','Clocher','Ruines','Source captée','Lavoir','Fontaine','Source','Sommet','Civil','Gorge') or 'Avallon' in top:
      c=shape(f['geometry']).centroid
      if math.hypot(c.x-TX,c.y-TY)<3500: KEY.append((nat,top or nat,c.x,c.y))
KEY.append(('Tour','Tour d Avalon (muraille)',TX,TY))
print(len(KEY),'lieux clés')
M0=T.transform(6.040299,45.422426);S0=T.transform(6.04019,45.42177)
# 1) lieux clés à 10 stades (±1 %) / 5 stades / 1068 m de la jonction ou de la source du Mouret
for nm,P in (('jonction Mouret',M0),('source',S0)):
  for tag,Dm in (('10 stades',1850),('5 stades',925),('1 stade',185),('rayon 1068',1068)):
    L=[(k[1],round(math.hypot(k[2]-P[0],k[3]-P[1]))) for k in KEY if abs(math.hypot(k[2]-P[0],k[3]-P[1])-Dm)<=Dm*0.01]
    print(f'  {nm} ↔ lieux clés à {tag} ±1 % : {L}')
# 2) paires de lieux clés à 1850 ±1 %
pairs=[(a,b,math.hypot(a[2]-b[2],a[3]-b[3])) for a,b in itertools.combinations(KEY,2) if abs(math.hypot(a[2]-b[2],a[3]-b[3])-1850)<=18.5]
print('paires à 10 stades ±1 % :',len(pairs))
for a,b,d in pairs:
  L=LineString([(a[2],a[3]),(b[2],b[3])])
  print(f'  {a[1][:28]:28s} – {b[1][:28]:28s} {d:.0f} m | droite à {L.distance(Point(*M0)):.0f} m de la jonction du Mouret, {L.distance(Point(*S0)):.0f} m de la source')
# nul : même nombre de points tirés au hasard dans la même emprise
xs=[k[2] for k in KEY];ys=[k[3] for k in KEY];random.seed(1);cnt=[]
for _ in range(2000):
  P=[(random.uniform(min(xs),max(xs)),random.uniform(min(ys),max(ys))) for _ in KEY]
  cnt.append(sum(1 for a,b in itertools.combinations(P,2) if abs(math.hypot(a[0]-b[0],a[1]-b[1])-1850)<=18.5))
print('nombre de paires à 10 stades +-1 pct attendu au hasard : moyenne',round(float(np.mean(cnt)),1),', 95e centile',int(np.percentile(cnt,95)))
# 3) caps et distances des lieux clés proches vers la jonction
print('\nDepuis les lieux clés proches du Mouret :')
for k in sorted(KEY,key=lambda k:math.hypot(k[2]-M0[0],k[3]-M0[1]))[:14]:
  lo,la=Ti.transform(k[2],k[3]);az,_,d=G.inv(lo,la,6.040299,45.422426)
  print(f'  {k[1][:30]:30s} ({k[0]}) → jonction : {d:5.0f} m cap {az%360:5.1f}°')
