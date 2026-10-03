import numpy as np,json,math,datetime as dt
hz=json.load(open('hz.json'));A=np.array(sorted(map(float,hz)));H=np.array([hz[str(a)][0] if str(a) in hz else hz[repr(a)][0] for a in A])
lat,lon=45.4288723,6.03101275
def sunpos(jd):
    n=jd-2451545.0;L=(280.460+0.9856474*n)%360;gm=math.radians((357.528+0.9856003*n)%360)
    lam=math.radians(L+1.915*math.sin(gm)+0.020*math.sin(2*gm));eps=math.radians(23.439-0.0000004*n)
    ra=math.atan2(math.cos(eps)*math.sin(lam),math.cos(lam));dec=math.asin(math.sin(eps)*math.sin(lam))
    gmst=(280.46061837+360.98564736629*n)%360;ha=math.radians(gmst+lon)-ra
    la=math.radians(lat)
    alt=math.asin(math.sin(la)*math.sin(dec)+math.cos(la)*math.cos(dec)*math.cos(ha))
    az=math.atan2(-math.sin(ha)*math.cos(dec),math.cos(la)*math.sin(dec)-math.sin(la)*math.cos(dec)*math.cos(ha))
    return math.degrees(alt),math.degrees(az)%360,math.degrees(dec)
def refr(h): return 1.02/math.tan(math.radians(h+10.3/(h+5.11)))/60
res=[]
for doy in range(1,366):
    d0=dt.datetime(2026,1,1)+dt.timedelta(days=doy-1)
    jd0=2461041.5+doy-1  # 2026-01-01 0h UT
    flat=real=None
    for m in range(2*60,9*60):
        jd=jd0+m/1440;alt,az,dec=sunpos(jd)
        app=alt+refr(alt)
        if flat is None and app+0.27>=0: flat=(az,m)  # upper limb on flat horizon
        if 40<=az<=80:
            h=np.interp(az,A,H)
            if real is None and app+0.27>=h: real=(az,m)
        if flat and real: break
    res.append((d0.strftime('%m-%d'),flat[0] if flat else None,real[0] if real else None,dec))
json.dump(res,open('sunrise.json','w'))
for r in res:
    if r[0][-2:] in('01','10','20') or r[0] in('06-21','06-24','05-10','04-30'): print(r[0],round(r[1],2),r[2] and round(r[2],2),round(r[3],2))
print('min flat',min(res,key=lambda r:r[1]));print('min real',min([r for r in res if r[2]],key=lambda r:r[2]))
