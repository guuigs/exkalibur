import json,math,numpy as np
exec(open('ring1068.py').read().split('hyd=json.load')[0])   # builds merged real junctions M (x,y,deg,src,nat)
P=np.array([[m[0],m[1],m[2]] for m in M])
ox,oy=T.transform(6.03101275,45.4288723)
def hits(R,degmin,rad):
  az=np.radians(np.arange(0,360,0.1));tx=ox+R*np.sin(az);ty=oy+R*np.cos(az)
  sel=P[P[:,2]>=degmin]
  d=np.min(np.hypot(sel[:,0][None,:]-tx[:,None],sel[:,1][None,:]-ty[:,None]),axis=1)
  return np.mean(d<=rad)
for dm in (3,4,5):
  print('deg>=',dm,'nb',int((P[:,2]>=dm).sum()),' P(croisement à <=32 m sur le cercle 1850 m) =',round(hits(1850,dm,32),3),'| secteur 30-150° :',end=' ')
  az=np.radians(np.arange(30,150,0.1));tx=ox+1850*np.sin(az);ty=oy+1850*np.cos(az);sel=P[P[:,2]>=dm]
  d=np.min(np.hypot(sel[:,0][None,:]-tx[:,None],sel[:,1][None,:]-ty[:,None]),axis=1);print(round(np.mean(d<=32),3))
# J5 degree check
j=(45.42696,6.05477);jx,jy=T.transform(j[1],j[0])
near=P[np.hypot(P[:,0]-jx,P[:,1]-jy)<40];print('J5 voisins:',near)
for m in M:
  if math.hypot(m[0]-jx,m[1]-jy)<40: print(m)
