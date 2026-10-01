"""Piste géographique : où mène le rayon Tour de Londres -> Battle ? Lieux 'très saints' (îles ?) proches du rayon, et distance D nécessaire."""
import sys, math
sys.stdout.reconfigure(encoding='utf-8')
R=6371.0088
def hav(a,b):
    la1,lo1,la2,lo2=map(math.radians,(*a,*b)); h=math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
def cap(a,b):
    la1,lo1,la2,lo2=map(math.radians,(*a,*b)); y=math.sin(lo2-lo1)*math.cos(la2); x=math.cos(la1)*math.sin(la2)-math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return (math.degrees(math.atan2(y,x))+360)%360
def xt(a,b,p):
    d=hav(a,p)/R; return math.asin(math.sin(d)*math.sin(math.radians(cap(a,p)-cap(a,b))))*R
T=(51.5081124,-0.0759493); B=(50.9143,0.4870); H=(50.854259,0.573453)
sites={ # coordonnées approximatives Wikipedia (précision ~1 km)
'Sainte-Chapelle (Paris, Ile de la Cite)':(48.855375,2.3449609),
'Notre-Dame de Paris':(48.8530,2.3499),
'Ile Saint-Honorat (Lerins)':(43.5117,7.0467),
'Ile Sainte-Marguerite (Cannes)':(43.5183,7.0505),
'Reichenau (Ile, lac de Constance)':(47.6987,9.0625),
'Mont-Saint-Michel':(48.6361,-1.5115),
'Lindisfarne (Holy Island)':(55.669,-1.800),
'Iona':(56.3318,-6.3915),
'Chartres cathedrale':(48.4478,1.4875),
'Reims cathedrale':(49.2534,4.0340),
'Vezelay':(47.4663,3.7481),
'Cluny':(46.4348,4.6585),
'Taize':(46.5,4.667),
'Ars/Paray-le-Monial':(46.4536,4.1147),
'Lourdes':(43.0972,-0.0578),
'Assise':(43.0707,12.6196),
'Rome Vatican':(41.9022,12.4539),
'Saint-Denis basilique':(48.9354,2.3600),
'Saint-Germain-des-Pres':(48.8541,2.3335),
'Taize':(46.5,4.667),
'Ile Sainte-Helene / Ile Saint-Louis':(48.8518,2.3572),
'Isola San Giulio (Orta)':(45.7965,8.4142),
'Ile de Sein':(48.0378,-4.8519),
'Sainte-Baume':(43.3,5.7),
'Saintes-Maries-de-la-Mer':(43.4525,4.4281),
'Gniezno':(52.53,17.6),
}
print('cap Tour->Battle %.2f | Tour->Hastings %.2f'%(cap(T,B),cap(T,H)))
print(f"{'lieu':45s} {'D km':>8s} {'ecart lat km':>12s} {'cap':>7s}")
for n,p in sites.items():
    print(f"{n:45s} {hav(T,p):8.1f} {xt(T,B,p):12.1f} {cap(T,p):7.2f}")
