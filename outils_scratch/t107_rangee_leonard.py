import numpy as np,math,pickle,json
from shapely.geometry import shape,Point
src=open('t45_horizon.py').read() if False else open('/home/user/exkalibur/outils_scratch/t45_horizon.py').read()
exec(src.split("hz={a:horizon")[0])
TX,TY=936955.34,6485599.51;tlo,tla=Ti.transform(TX,TY)
rows=pickle.load(open('run/rows_final.pkl','rb'))
J2=[r for r in rows if abs(r['la']-45.42337)<2e-5 and abs(r['lo']-6.04166)<2e-5][0]
S=1850/8
print('s=%.2f m ; 4,5 s = %.1f m ; 4 s = %.1f m ; J2 = %.1f m (%.2f %%)'%(S,4.5*S,4*S,J2['d'],100*(J2['d']/(4.5*S)-1)))
# 1) dates où le lever VISIBLE est à l'azimut de J2 (±1,7°)
hz={a:horizon(a) for a in np.arange(40,140.5,0.5)}
def lever_visible(doy):
  dec=decl(doy)
  for h10 in range(-10,400):
    h=h10/10;az=sun_az(dec,h)
    if 40<=az<=139.5:
      hb,dd=hz[round(az*2)/2]
      if h>=hb: return az,h
  return None,None
import datetime
tgt=J2['az'];out=[]
for doy in range(1,366):
  az,h=lever_visible(doy)
  if az is not None and abs(az-tgt)<=1.7: out.append((doy,round(az,1),round(h,1),(datetime.date(2026,1,1)+datetime.timedelta(doy-1)).strftime('%d/%m')))
print('cap J2 = %.2f° vrai ; dates (lever visible depuis le pied de la tour) à ±1,7° :'%tgt);print(out)
flat=[(doy,(datetime.date(2026,1,1)+datetime.timedelta(doy-1)).strftime('%d/%m'),round(sun_az(decl(doy),-0.83),1)) for doy in range(1,366) if abs(sun_az(decl(doy),-0.83)-tgt)<=1.7]
print('lever astronomique (horizon plat) à ±1,7° :',flat[:6],'... max flat az =',round(max(sun_az(decl(d),-0.83) for d in range(1,366)),2))
# 2) bande radiale 4,5 s pour les populations de croisements qualifiés
pops={'tous ≥3 voies 100 m-2,5 km':rows,
 'maisons≥100':[r for r in rows if r['hb']>=100],
 '+eau':[r for r in rows if r['hb']>=100 and (r['wd']<=150 or r['ta']>=1)],
 '+vu>=50':[r for r in rows if r['hb']>=100 and (r['wd']<=150 or r['ta']>=1) and max(r['vs'],r['vm'])>=50]}
for k,v in pops.items():
  n=[r for r in v if abs(r['d']-4.5*S)<=0.01*4.5*S]
  print(k,len(v),'dont dans 4,5 s ±1 % :',len(n),[ (round(r['la'],4),round(r['lo'],4),int(r['d'])) for r in n][:6])
# 3) où tombe la 3e (rangée de 12, T entre 6 et 7) : 3,5 s de l'autre côté
for sgn,nm in ((1,'3e opposée à J2'),):
  az3=(tgt+180)%360
  lo,la=G.fwd(tlo,tla,az3,3.5*S)[:2];print(nm,'-> %.5f,%.5f à %.0f m cap %.1f°'%(la,lo,3.5*S,az3))
  lo,la=G.fwd(tlo,tla,tgt,4.5*S)[:2];print('11e à',round(la,5),round(lo,5))
# toutes les places de la rangée de 12 le long de l'axe de J2
print('places (rangée de 12, axe cap %.2f°) :'%tgt)
for k in range(1,13):
  d=(k-6.5)*S;az=tgt if d>=0 else (tgt+180)%360
  lo,la=G.fwd(tlo,tla,az,abs(d))[:2];print(k,round(d),'m',round(la,5),round(lo,5))

# ===== 4) test de la famille : fêtes d'apôtres -> lever visible -> places 3/11 de la rangée =====
import datetime
fetes={'Pierre 29/06':(6,29),'Chaire de Pierre 22/02':(2,22),'André 30/11':(11,30),'Jacques le Majeur 25/07':(7,25),'Jean 27/12':(12,27),'Philippe et Jacques 03/05':(5,3),'Barthélemy 24/08':(8,24),'Thomas 03/07':(7,3),'Matthieu 21/09':(9,21),'Simon et Jude 28/10':(10,28),'Matthias 14/05':(5,14)}
def doy_of(m,d): return (datetime.date(2026,m,d)-datetime.date(2026,1,1)).days+1
JALL=np.array([(r['x'],r['y']) for r in rows]);QUAL=np.array([(r['x'],r['y']) for r in rows if r['hb']>=100 and (r['wd']<=150 or r['ta']>=1)])
from scipy.spatial import cKDTree
kA=cKDTree(JALL);kQ=cKDTree(QUAL)
pts=[]
for nm,(m,d) in fetes.items():
  doy=doy_of(m,d);azv,hv=lever_visible(doy);azf=sun_az(decl(doy),-0.83)
  for lab,az in (('visible',azv),('plat',azf)):
    if az is None: continue
    for ax_off in (0,90,-90):
      a=az+ax_off
      for dist,tag in ((4.5*S,'12:11e'),(3.5*S,'12:3e'),(4*S,'13:3e/11e')):
        for sg in (1,-1):
          lo,la=G.fwd(tlo,tla,(a+(0 if sg>0 else 180))%360,dist)[:2];x,y=T.transform(lo,la)
          pts.append((nm,lab,ax_off,tag,sg,az,x,y))
print('points prédits (famille) :',len(pts))
P=np.array([(p[6],p[7]) for p in pts])
dA=kA.query(P)[0];dQ=kQ.query(P)[0]
for thr in (10,20,30,50):
  print('<=%d m : junction quelconque %d ; qualifiée (maisons>=100+eau) %d'%(thr,(dA<=thr).sum(),(dQ<=thr).sum()))
for i in np.argsort(dQ)[:8]:
  p=pts[i];print('  ',p[0],p[1],'axe+%d'%p[2],p[3],'az %.1f'%p[5],'-> junction qualifiée à %.0f m ; quelconque %.0f m'%(dQ[i],dA[i]))
# espérance sous hasard : points uniformes dans la couronne 700-1300 m
rng=np.random.default_rng(1);N0=200000
rr=np.sqrt(rng.uniform(700**2,1300**2,N0));th=rng.uniform(0,2*np.pi,N0);R=np.column_stack([TX+rr*np.sin(th),TY+rr*np.cos(th)])
for thr in (10,20,30):
  pA=(kA.query(R)[0]<=thr).mean();pQ=(kQ.query(R)[0]<=thr).mean()
  print('hasard <=%d m : P(junction)=%.4f  P(qualifiée)=%.4f -> attendu sur %d points : %.2f / %.2f'%(thr,pA,pQ,len(pts),pA*len(pts),pQ*len(pts)))

# ===== 5) test joint : 11e sur un croisement qualifié ET 3e sur une église =====
from shapely.geometry import shape as shp
egl=[shp(f['geometry']).centroid for f in json.load(open('wfs_batiment.json'))['features'] if f['properties']['nature'] in ('Eglise','Chapelle')]
EG=np.array([(p.x,p.y) for p in egl]);kE=cKDTree(EG);print('églises/chapelles dans la zone :',len(EG))
hugues=Point(*T.transform(6.02268,45.43321)).buffer(0)  # point de contrôle seulement
cfg=[]
for nm,(m,d) in fetes.items():
  doy=doy_of(m,d);azv,hv=lever_visible(doy);azf=sun_az(decl(doy),-0.83)
  for lab,az in (('visible',azv),('plat',azf)):
    if az is None: continue
    for ax_off in (0,90,-90):
      for sg in (1,-1):
        a=(az+ax_off+(0 if sg>0 else 180))%360
        for var,(d11,d3) in (('12',(4.5*S,3.5*S)),('13',(4*S,4*S))):
          lo,la=G.fwd(tlo,tla,a,d11)[:2];x11=T.transform(lo,la)
          lo,la=G.fwd(tlo,tla,(a+180)%360,d3)[:2];x3=T.transform(lo,la)
          cfg.append((nm,lab,ax_off,sg,var,az,x11,x3))
print('configurations :',len(cfg))
c11=np.array([c[6] for c in cfg]);c3=np.array([c[7] for c in cfg])
d11=kQ.query(c11)[0];d3=kE.query(c3)[0]
for t1,t3 in ((30,40),(20,30),(10,30)):
  both=((d11<=t1)&(d3<=t3));print('11e<=%d m d une jonction qualifiée ET 3e<=%d m d une église : %d configs'%(t1,t3,both.sum()),[ (cfg[i][0],cfg[i][1],cfg[i][4]) for i in np.where(both)[0]])
print('3e<=40 m d une église (toutes configs) :',(d3<=40).sum(),'/',len(cfg),' ; 11e<=30 m d une jonction qualifiée :',(d11<=30).sum())
# hasard Monte-Carlo : même taille de famille, axes aléatoires
rng=np.random.default_rng(3);K=20000;hit=0;h3=0;h11=0
for _ in range(K):
  a=rng.uniform(0,360)
  lo,la=G.fwd(tlo,tla,a,4.5*S)[:2];p11=T.transform(lo,la)
  lo,la=G.fwd(tlo,tla,(a+180)%360,3.5*S)[:2];p3=T.transform(lo,la)
  q=kQ.query(p11)[0]<=30;e=kE.query(p3)[0]<=40;h11+=q;h3+=e;hit+=(q and e)
print('hasard (axe aléatoire) : P(11e<=30 m jonction qualifiée)=%.4f ; P(3e<=40 m église)=%.4f ; P(joint)=%.5f (%d sur %d)'%(h11/K,h3/K,hit/K,hit,K))
