import pandas as pd,numpy as np,pickle
from pyproj import Transformer
from scipy.spatial import cKDTree
Tf=Transformer.from_crs(4326,2154,always_xy=True)
TX,TY=936955.34,6485599.51
J16=np.array(Tf.transform(6.0319955,45.4268394))
rows=pickle.load(open('run/rows_final2.pkl','rb'))
Q=np.array([(x['x'],x['y']) for x in rows if x['deg']>=3 and x['hb']>=100 and x['eauS']<=150 and x['op']>=0.25 and max(x['vs'],x['vm'])>=100])
A=np.array([(x['x'],x['y']) for x in rows if x['deg']>=3]);kA=cKDTree(A)
d=pd.read_csv('hyg38.csv.gz',low_memory=False)
d=d[d.bayer.notna()].copy();d['b']=d.bayer.str.split('-').str[0]
d=d.sort_values('mag').drop_duplicates(['con','b'])
GR=['Alp','Bet','Gam','Del','Eps','Zet','Eta','The','Iot','Kap','Lam','Mu','Nu','Xi','Omi','Pi','Rho','Sig','Tau','Ups','Phi','Chi','Psi','Ome']
res=[]
for con,g in d.groupby('con'):
    s={r.b:(r.ra*15,r.dec) for r in g.itertuples()}
    if not all(k in s for k in ('Alp','Gam','Lam')): continue
    ra0,de0=np.radians(s['Alp'])
    def proj(ra,de):
        ra,de=np.radians(ra),np.radians(de)
        c=np.sin(de0)*np.sin(de)+np.cos(de0)*np.cos(de)*np.cos(ra-ra0)
        xi=np.cos(de)*np.sin(ra-ra0)/c; eta=(np.cos(de0)*np.sin(de)-np.sin(de0)*np.cos(de)*np.cos(ra-ra0))/c
        return np.array([xi,eta])
    P={k:proj(*v) for k,v in s.items()}
    sc=1850/np.linalg.norm(P['Gam']-P['Lam'])
    for anchor in ('Alp','Gam','Lam'):
      for m in (1,-1):
        pos={k:np.array([TX,TY])+sc*np.array([m*(p[0]-P[anchor][0]),p[1]-P[anchor][1]]) for k,p in P.items()}
        for k,p in pos.items():
            if k==anchor: continue
            dj=np.linalg.norm(p-J16);dq=np.min(np.linalg.norm(Q-p,axis=1));da=kA.query(p)[0]
            res.append((con,anchor,m,k,round(dj),round(dq),round(da),round(np.linalg.norm(p-[TX,TY]))))
R=pd.DataFrame(res,columns=['con','anchor','mir','star','dJ16','dQ','dAny','dTour'])
print('constellations testées:',R.con.nunique(),'placements:',len(R))
print(R.sort_values('dQ').head(15).to_string())
# base rate: fraction of star positions within 1300 m of tower; expected hits within 15 m of J16
near=R[R.dTour<1300];print('positions à <1,3 km de la tour:',len(near))
print('attendu au hasard à <=15 m de J16 ~', round(len(near)*(15**2)/(1300**2),2))
