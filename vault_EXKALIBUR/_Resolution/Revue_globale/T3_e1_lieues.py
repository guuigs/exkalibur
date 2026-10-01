# T3 E1 : quelle lieue / quel point de mesure rend "près de 11 lieues" cohérent ? + parallélisme garde (E7)
import json,math
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
RLC={'village/Nominatim':(42.9272,2.2627),'église Ste-Marie-Madeleine':(42.92760,2.26330),'château (ruines)':(42.9278,2.2619)}
# points de mesure Foix
FOIX={'château (Nominatim)':(42.9656,1.6053),'centre-ville':(42.9647,1.6053),'Tour Ronde':(42.9655,1.6054)}
# autres châteaux cathares/citadelles proches de 11 lieues à l'ouest (coordonnées approximatives, OSM/Wikipedia)
CAND={'Foix':(42.9656,1.6053),'Montségur':(42.8737,1.8320),'Roquefixade':(42.9455,1.7830),'Lordat':(42.7997,1.7047),
'Puivert':(42.9098,2.0313),'Usson':(42.7717,2.0025),'Montréal-de-Sos':(42.7666,1.4970),'Gudanes':(42.8580,1.5130),'Termes':(43.0175,2.5920),
'Mirepoix(ville)':(43.0868,1.8700),'Saint-Girons':(42.9850,1.1450),'Pamiers':(43.1167,1.6100),'Tarascon-sur-Ariège':(42.8450,1.6060)}
LIEUES={'commune 4,444 (1/25°)':4.444,'poste 3,898':3.898,'métrique 4,0':4.0,'5,0 km (lieue "moderne")':5.0,'terrestre 4,828 (3 mi)':4.828,
'marine 5,556 (3 mn)':5.556,'legua castellana 5,573':5.573,'legua 4,19 (Alphonse X)':4.19,'Gascogne 5,847':5.847,'Bourbonnais 4,88':4.88,
'Bretagne/Anjou 4,5-4,6':4.55,'Beauce 3,2':3.2,'gauloise 2,2':2.222,'ancienne d\'Occitanie ~ 4,1':4.1,'Languedoc (lieue commune tol.) 4,44':4.44,'legua Portugal 6,17':6.17,'legua legal ES 5,5727':5.5727,'lieue Toulouse 4,5?':4.5}
print('=== 1) Foix : distance selon point de mesure RLC × Foix')
for kr,r in RLC.items():
    for kf,f in FOIX.items():
        print(f'  {kr:28s} -> Foix {kf:20s} {hav(r,f):6.2f} km  cap {brg(r,f):.1f}')
d=hav(RLC['village/Nominatim'],FOIX['château (Nominatim)'])
print('\n=== 2) Foix (%.2f km) exprimé en lieues, par lieue'%d)
ok=[]
for k,v in LIEUES.items():
    n=d/v; tag='  <-- "près de 11" (10.5-10.99)' if 10.5<=n<11 else ('  ~11 (>=11)' if 10.99<n<=11.3 else '')
    print(f'  {k:32s} {n:6.2f}{tag}')
print('\n=== 3) Test du hasard : pour chaque lieue, quels candidats (W, 240-300°) tombent à 10.5-10.99 lieues ?')
R=RLC['village/Nominatim']
for k,v in LIEUES.items():
    hits=[(n,hav(R,p)/v) for n,p in CAND.items() if 240<=brg(R,p)<=300 and 10.5<=hav(R,p)/v<11.0]
    print(f'  {k:32s}', ', '.join(f'{n} {x:.2f}' for n,x in hits) or '-')
print('\nAutre lecture : "près de 11" = 10.8-10.99 (très près) :')
for k,v in LIEUES.items():
    hits=[n for n,p in CAND.items() if 240<=brg(R,p)<=300 and 10.8<=hav(R,p)/v<11.0]
    if hits: print('  ',k,hits)
print('\n=== 4) Lieue implicite si Foix = 10.5..10.99 lieues :', round(d/10.99,3),'à',round(d/10.5,3),'km  (5,0 km dans la plage ? ',d/10.99<=5.0<=d/10.5,')')
print('   Lieue implicite Foix=11 exactement:',round(d/11,3))
# 5) Parallélisme nouvelle garde (SC->Lorient) avec garde León->quillon candidat
LEON=(42.5991,-5.5670); SC=(48.8554,2.3450); LOR=(47.7482,-3.3702)
b_new=brg(SC,LOR)
print('\n=== 5) Cap SC->Lorient %.2f ; cap inverse %.2f'%(b_new,(b_new+180)%360))
for n,p in CAND.items():
    if n in('Foix','Montségur','Roquefixade','Lordat','Puivert','Gudanes','Montréal-de-Sos','Usson'):
        b=brg(LEON,p); diff=((b-(b_new-180))+180)%360-180
        print(f'  León->{n:16s} cap {b:6.2f}  (garde vs nouvelle garde: écart {diff:+.2f}°)')
