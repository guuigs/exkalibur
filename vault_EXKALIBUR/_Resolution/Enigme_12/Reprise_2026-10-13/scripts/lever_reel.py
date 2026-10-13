"""Azimut du premier rayon de soleil vu du sommet de la tour d'Avalon, avec l'horizon réel (horizon_tour.json)."""
import json, math, datetime
H={int(k):v for k,v in json.load(open('horizon_tour.json')).items()}
def hz(az):
    ks=sorted(H); 
    if az<=ks[0]: return H[ks[0]]
    if az>=ks[-1]: return H[ks[-1]]
    for a,b in zip(ks,ks[1:]):
        if a<=az<=b: return H[a]+(H[b]-H[a])*(az-a)/(b-a)
LAT,LON=45.429083,6.030808
def sunpos(dt):  # dt UTC, NOAA algorithm
    jd=(dt-datetime.datetime(2000,1,1,12))/datetime.timedelta(days=1)+2451545.0
    T=(jd-2451545.0)/36525
    L0=(280.46646+T*(36000.76983+T*0.0003032))%360; M=357.52911+T*(35999.05029-0.0001537*T)
    e=0.016708634-T*(0.000042037+0.0000001267*T)
    C=math.sin(math.radians(M))*(1.914602-T*(0.004817+0.000014*T))+math.sin(math.radians(2*M))*(0.019993-0.000101*T)+math.sin(math.radians(3*M))*0.000289
    lam=L0+C-0.00569-0.00478*math.sin(math.radians(125.04-1934.136*T))
    eps=23+(26+((21.448-T*(46.815+T*(0.00059-T*0.001813))))/60)/60+0.00256*math.cos(math.radians(125.04-1934.136*T))
    dec=math.degrees(math.asin(math.sin(math.radians(eps))*math.sin(math.radians(lam))))
    y=math.tan(math.radians(eps/2))**2
    eqt=4*math.degrees(y*math.sin(2*math.radians(L0))-2*e*math.sin(math.radians(M))+4*e*y*math.sin(math.radians(M))*math.cos(2*math.radians(L0))-0.5*y*y*math.sin(4*math.radians(L0))-1.25*e*e*math.sin(2*math.radians(M)))
    tst=(dt.hour*60+dt.minute+dt.second/60+eqt+4*LON)%1440
    ha=tst/4-180
    phi=math.radians(LAT); d=math.radians(dec); h=math.radians(ha)
    alt=math.degrees(math.asin(math.sin(phi)*math.sin(d)+math.cos(phi)*math.cos(d)*math.cos(h)))
    az=(math.degrees(math.atan2(math.sin(h),math.cos(h)*math.sin(phi)-math.tan(d)*math.cos(phi)))+180)%360
    return alt,az
def first_light(date):
    t=datetime.datetime(date.year,date.month,date.day,2,0)
    while t.hour<12:
        alt,az=sunpos(t)
        if alt+0.27+0.5>=hz(az):   # bord supérieur + réfraction ~0,5°
            return t,az,alt
        t+=datetime.timedelta(minutes=1)
if __name__=='__main__':
    print('date (UTC)        az premier rayon  haut. soleil')
    for m,dd in [(3,21),(4,15),(4,30),(5,1),(5,10),(5,15),(5,20),(5,31),(6,21),(7,15),(8,1),(8,15),(8,31),(9,10),(9,23),(10,13)]:
        t,az,alt=first_light(datetime.date(2026,m,dd)); print('%02d/%02d  %s   %6.1f°   %5.1f°'%(dd,m,t.strftime('%H:%M'),az,alt))
    # dates où le premier rayon est à 77 ± 1,5°
    out=[]
    d=datetime.date(2026,1,1)
    while d.year==2026:
        t,az,alt=first_light(d)
        if abs(az-77)<=1.5: out.append((d.strftime('%d/%m'),round(az,1)))
        d+=datetime.timedelta(days=1)
    print('premier rayon à 77 ± 1,5° :', out)
