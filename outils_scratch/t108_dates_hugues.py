import re
src=open('/home/user/exkalibur/outils_scratch/t107_rangee_leonard.py').read().split('# 1) dates')[0]
exec(src)
hz={a:horizon(a) for a in np.arange(40,140.5,0.5)}
import datetime
def lever_visible(doy):
  dec=decl(doy)
  for h10 in range(-10,400):
    h=h10/10;az=sun_az(dec,h)
    if 40<=az<=139.5:
      hb,dd=hz[round(az*2)/2]
      if h>=hb: return az,h
  return None,None
def doy_of(m,d): return (datetime.date(2026,m,d)-datetime.date(2026,1,1)).days+1
from scipy.spatial import cKDTree
rows=pickle.load(open('run/rows_final.pkl','rb'))
QUAL=np.array([(r['x'],r['y'],r['la'],r['lo']) for r in rows if r['hb']>=100 and (r['wd']<=150 or r['ta']>=1)]);kQ=cKDTree(QUAL[:,:2]);kA=cKDTree(np.array([(r['x'],r['y']) for r in rows]))
fetes={'Hugues de Grenoble 01/04':(4,1),'Hugues de Cluny 29/04':(4,29),'Hugues de Rouen 09/04':(4,9),'Hugues de Lincoln 17/11':(11,17),'Hugues (Bonnevaux) 01/04':(4,1),'Pâques ex. 05/04':(4,5),'Pâques 20/04':(4,20),'Pâques 31/03':(3,31),'Pâques 09/04':(4,9),'Pâques 27/03 (1524 jul)':(3,27),'Simon et Jude 28/10':(10,28)}
print('date | az lever visible | az astronomique')
for nm,(m,d) in fetes.items():
  doy=doy_of(m,d);az,h=lever_visible(doy);print(nm,'|',None if az is None else round(az,1),'|',round(sun_az(decl(doy),-0.83),1))
# Pâques : positions 3e/11e pour les 2 sens, axes le long du soleil
print('\nPâques (rangée de 12) : place 11 à 1040,6 m côté soleil / côté opposé ; place 3 à 809 m')
for nm,(m,d) in [('Pâques 2023 (09/04)',(4,9)),('Pâques 2024 (31/03)',(3,31)),('Pâques 2025 (20/04)',(4,20)),('Pâques 2026 (05/04)',(4,5)),('Pâques 1524 grég (06/04)',(4,6))]:
  doy=doy_of(m,d);az,h=lever_visible(doy)
  for sg,lab in ((1,'11e côté soleil'),(-1,'11e côté opposé')):
    a=(az+(0 if sg>0 else 180))%360
    lo,la=G.fwd(tlo,tla,a,4.5*S)[:2];x11=T.transform(lo,la)
    lo3,la3=G.fwd(tlo,tla,(a+180)%360,3.5*S)[:2];x3=T.transform(lo3,la3)
    dq=kQ.query(x11);da=kA.query(x11)
    print(nm,'az %.1f'%az,lab,'-> 11e %.5f,%.5f ; croisement qualifié le + proche %.0f m ; quelconque %.0f m ; 3e %.5f,%.5f'%(la,lo,dq[0],da[0],la3,lo3))
print('\nPâques, rangée PERPENDICULAIRE au lever (axe = lever ±90°) : meilleure distance 11e -> croisement qualifié (toutes places 3 et 11, 12 et 13 places)')
best=[]
for nm,(m,d) in [('2023 09/04',(4,9)),('2024 31/03',(3,31)),('2025 20/04',(4,20)),('2026 05/04',(4,5)),('1524 06/04',(4,6)),('1524 jul 27/03',(3,27))]:
  doy=doy_of(m,d);az,h=lever_visible(doy)
  for off in (90,-90):
    for var,(a11,a3) in (('12',(4.5*S,3.5*S)),('13',(4*S,4*S))):
      for sgn in (1,-1):
        a=(az+off+(0 if sgn>0 else 180))%360
        lo,la=G.fwd(tlo,tla,a,a11)[:2];x11=T.transform(lo,la);lo3,la3=G.fwd(tlo,tla,(a+180)%360,a3)[:2];x3=T.transform(lo3,la3)
        best.append((kQ.query(x11)[0],nm,off,var,sgn,round(la,5),round(lo,5)));best.append((kQ.query(x3)[0],nm+' (3e)',off,var,sgn,round(la3,5),round(lo3,5)))
best.sort();print(best[:6])
