import json,math,numpy as np
exec(open('ring1068.py').read().split('out=[]')[0])
TOP=(45.4288723,6.03101275)
X0t,Y0t=T.transform(TOP[1],TOP[0]);Zs=z(mnt,X0t,Y0t)+33
Xp,Yp=T.transform(6.03115,45.42887);Zp=z(mnt,Xp,Yp)+1.7
L=json.load(open('wfs_lieu_dit_non_habite.json'))['features']+json.load(open('wfs_toponymie.json'))['features']
HS=np.array([c[:2] for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if f['geometry']['type']=='LineString' for c in f['geometry']['coordinates']])
def topo(x,y):
  b=[]
  for f in L:
    c=f['geometry']['coordinates']
    while isinstance(c[0],list): c=c[0]
    p=f['properties'];b.append((math.hypot(c[0]-x,c[1]-y),p.get('toponyme') or p.get('graphie_du_toponyme')))
  return min(b)
def ev(az,d):
  tl,ta,_=G.fwd(TOP[1],TOP[0],az%360,d);x,y=T.transform(tl,ta)
  if not(X0+130<x<X0+6870 and YN-6870<y<YN-130): return f'{ta:.5f},{tl:.5f} hors LiDAR ({topo(x,y)[1]})'
  js=sorted([(math.hypot(m[0]-x,m[1]-y),m) for m in M],key=lambda t:t[0])
  dj=js[0][0];deg=max([m[2] for dd,m in js if dd<=150] or [0])
  db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)));dw=float(np.min(np.hypot(HS[:,0]-x,HS[:,1]-y)))
  ring=np.mean([z(mnh,x+a,y+b)>5 for a in range(-120,121,8) for b in range(-120,121,8) if 60<=math.hypot(a,b)<=120])
  n=vs=vp=0
  for a in range(-80,81,10):
    for b in range(-80,81,10):
      if math.hypot(a,b)>80 or z(mnh,x+a,y+b)>=1.5: continue
      n+=1;vs+=los(X0t,Y0t,Zs,x+a,y+b,True)<0;vp+=los(Xp,Yp,Zp,x+a,y+b,True)<0
  t=topo(x,y)
  return f'{ta:.5f},{tl:.5f} | {t[1]} ({t[0]:.0f} m) | croist {dj:.0f} m (max {deg} br <150 m) | maisons {db:.0f} | eau {dw:.0f} | forêt autour {ring:.2f} | ouvert80 {n} vus sommet {vs} pied {vp}'
r=1068
az_comp=G.inv(TOP[1],TOP[0],-8.5446,42.8805)[0]%360
rules={
 'Cadran horaire (12 au nord)':(90,330),
 'Cadran inversé':(270,30),
 'Pierre (1) à l\'Orient, sens horaire':(150,30),
 'Pierre (1) à l\'Orient, sens inverse':(30,150),
 'Christ à l\'Orient (entre 12 et 1), horaire':(165,45),
 'Christ à l\'Orient, inverse':(15,135),
 'Pierre (1) sur la droite de l\'É11 (65°), horaire':(125,5),
 'Pierre (1) sur la droite de l\'É11, inverse':(5,125),
 f'Jacques vers Compostelle ({az_comp:.0f}°), Simon +120°':(az_comp,az_comp+120),
 f'Jacques vers Compostelle, Simon −120°':(az_comp,az_comp-120),
}
print('### TABLE RONDE (rayon 1 068 m, centre = sommet de la tour)')
for k,(a3,a11) in rules.items():
  print('\n'+k);print('  3e (Jacques) cap',round(a3%360),':',ev(a3,r));print('  11e (Simon)  cap',round(a11%360),':',ev(a11,r))
# plate model
print('\n### PLANCHE POSÉE SUR LE TERRAIN (nord en haut, gourde→scie = 1 850 m)')
gourde=(1175,1540);scie=(1175,2430);scale=1850/math.dist(gourde,scie)
refs={'pointe de l\'épée':(690,2175),'garde de l\'épée':(563,786),'pommeau':(534,367),'centre de la planche':(601,1308)}
for k,(rx,ry) in refs.items():
  print('\nRempart =',k)
  for nm,(px,py) in {'3e gourde':gourde,'11e scie':scie}.items():
    dx=(px-rx)*scale;dy=-(py-ry)*scale;az=math.degrees(math.atan2(dx,dy))%360;d=math.hypot(dx,dy)
    print(f'  {nm}: cap {az:.0f}°, {d:.0f} m :',ev(az,d))
print('\n### VECTEUR (comme le loup) : 3e au rempart, 11e à 1 850 m au cap gourde→scie = 180°')
print('  ',ev(180,1850))
