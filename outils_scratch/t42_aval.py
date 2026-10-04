import numpy as np,json,math
from shapely.geometry import shape,Point
exec(open('ring1068.py').read().split('out=[]')[0])
N=7000
Vp=np.unpackbits(np.load('vs_pied.npy'))[:N*N].reshape(N,N).astype(bool)
rd=[(shape(f['geometry']),f['properties']) for f in json.load(open('wfs_troncon_de_route.json'))['features']]
for nm,la,lo in (('aval1',45.422482,6.039049),('aval3',45.423909,6.037753),('jonction',45.422426,6.040299)):
  x,y=T.transform(lo,la);R,C=int(YN-y),int(x-X0)
  v10=int(Vp[R-10:R+11,C-10:C+11].sum());v30=int(Vp[R-30:R+31,C-30:C+31].sum())
  near=sorted((round(g.distance(Point(x,y))),p.get('nature'),p.get('nom_1_gauche') or '') for g,p in rd if g.distance(Point(x,y))<40)
  print(nm,'visible du pied: ±10 m',v10,'m², ±30 m',v30,'m² | tronçons <40 m:',near[:6])
