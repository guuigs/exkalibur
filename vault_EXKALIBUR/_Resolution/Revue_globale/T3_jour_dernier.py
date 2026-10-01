# T3 : azimut lever/coucher du soleil (jour dernier) - Meeus basse précision
import math
def jd_greg(y,m,d,h=12.0):
    if m<=2: y-=1; m+=12
    A=y//100; B=2-A+A//4
    return int(365.25*(y+4716))+int(30.6001*(m+1))+d+B-1524.5+h/24
def jd_jul(y,m,d,h=12.0):
    if m<=2: y-=1; m+=12
    return int(365.25*(y+4716))+int(30.6001*(m+1))+d-1524.5+h/24
def sun_dec_eot(jd):
    T=(jd-2451545.0)/36525
    L0=(280.46646+36000.76983*T+0.0003032*T*T)%360
    M=math.radians((357.52911+35999.05029*T-0.0001537*T*T)%360)
    C=(1.914602-0.004817*T-0.000014*T*T)*math.sin(M)+(0.019993-0.000101*T)*math.sin(2*M)+0.000289*math.sin(3*M)
    tl=L0+C; om=math.radians(125.04-1934.136*T)
    lam=math.radians(tl-0.00569-0.00478*math.sin(om))
    eps=math.radians(23.439291-0.0130042*T+0.00256*math.cos(om))
    dec=math.asin(math.sin(eps)*math.sin(lam))
    y=math.tan(eps/2)**2; L0r=math.radians(L0); e=0.016708634-0.000042037*T
    eot=4*math.degrees(y*math.sin(2*L0r)-2*e*math.sin(M)+4*e*y*math.sin(M)*math.cos(2*L0r))  # minutes
    return math.degrees(dec),eot
def rise_set_az(jd_noon,lat,lon,h0=-0.833):
    dec,_=sun_dec_eot(jd_noon)
    for _ in range(3):
        d=math.radians(dec); f=math.radians(lat); h=math.radians(h0)
        cosH=(math.sin(h)-math.sin(f)*math.sin(d))/(math.cos(f)*math.cos(d))
        if abs(cosH)>1: return dec,None,None
        H=math.degrees(math.acos(cosH))
        cosA=(math.sin(d)-math.sin(h)*math.sin(f))/(math.cos(h)*math.cos(f))
        A=math.degrees(math.acos(max(-1,min(1,cosA))))
        # lever à jd_noon - H/360 ; coucher à jd_noon + H/360
        dec=sun_dec_eot(jd_noon-H/360)[0]
    return dec,A,360-A
TA=(45.4288,6.0308); SP=(43.3283,-1.0347); CB=(45.42361,6.01889)
if __name__=='__main__':
    print('Vérif : 21 mars 2026 (équinoxe) et 21 juin 2026 : ')
    for nm,(y,m,d) in {'équinoxe 20/03/2026':(2026,3,20),'solstice 21/06/2026':(2026,6,21),'solstice 21/12/2026':(2026,12,21)}.items():
        dec,a,b=rise_set_az(jd_greg(y,m,d),*TA); print(f'  {nm}: dec {dec:+.2f} lever {a:.2f} coucher {b:.2f}')
    dates=[
     ('Bayard † 30/04/1524 JULIEN (=10/05 grég.)','jul',1524,4,30),
     ('30/04/1524 en grégorien proleptique','greg',1524,4,30),
     ('30/04 actuel (grég. 2026)','greg',2026,4,30),
     ('Marignan 13/09/1515 julien (jour gloire?)','jul',1515,9,13),
     ('Marignan 14/09/1515 julien','jul',1515,9,14),
     ('Colomb † 20/05/1506 julien','jul',1506,5,20),
     ('Jacques Cœur † 25/11/1456 julien','jul',1456,11,25),
     ('Tibère † 16/03/37 julien','jul',37,3,16),
     ('Hugues d\'Avalon † 16/11/1200 julien','jul',1200,11,16),
     ('Bayard né ~ 1476 (sans jour)','jul',1476,3,31),
     ('Jeanne d\'Arc / Vendredi 13 -> 13/10/1307 jul','jul',1307,10,13),
     ('Charlemagne † 28/01/814 jul','jul',814,1,28),
     ('Solstice été (21/06 grég.)','greg',2026,6,21),
     ('Solstice hiver (21/12)','greg',2026,12,21),
     ('Équinoxe (20/03)','greg',2026,3,20),
     ('31/12 (dernier jour de l\'an)','greg',2026,12,31),
     ('Vendredi saint / Consummatum est (~03/04/33 jul)','jul',33,4,3),
    ]
    print('\n%-52s | Avalon lever / coucher | Saint-Palais lever / coucher | ChâteauBayard lever/coucher'%'date')
    for nm,cal,y,m,d in dates:
        jd=(jd_jul if cal=='jul' else jd_greg)(y,m,d)
        row=[]
        for loc in (TA,SP,CB):
            dec,a,b=rise_set_az(jd,*loc); row.append(f'{a:6.2f}/{b:6.2f}')
        dec=sun_dec_eot(jd)[0]
        print(f'{nm:52s} | dec {dec:+6.2f} | '+' | '.join(row))
    # scan
    print('\n=== Scan année : jours où l\'azimut du LEVER à Saint-Palais est à ±0,35° de 64,99° (angle É11) — hasard')
    target=64.99; hits=[]
    for doy in range(365):
        jd=jd_greg(2026,1,1)+doy
        dec,a,b=rise_set_az(jd,*SP)
        if a is not None and abs(a-target)<=0.35: hits.append((doy+1,round(a,2)))
    print('  jours (n° du jour de l\'année 2026, tropical) :',hits)
    print('  soit',len(hits),'jours sur 365 (~',round(len(hits)/365*100,1),'%)')
    print('\n=== Bayard † : lever à Saint-Palais pour 30/04/1524 jul :', end=' ')
    dec,a,b=rise_set_az(jd_jul(1524,4,30),*SP); print(f'{a:.3f} (cible 64.99, écart {a-64.99:+.3f})')
    for h0,l in ((-0.833,'-0,833 (std)'),(0.0,'0° géom.'),(-0.5667,'-0,567'),(-1.0,'-1°')):
        dec,a,b=rise_set_az(jd_jul(1524,4,30),*SP,h0=h0); print(f'   horizon {l}: {a:.3f}')
    print('\n=== Fenêtre de dates julien 1524 (Saint-Palais lever) : 26/04..04/05')
    for d in range(26,31): 
        print('  ',d,'avril jul', round(rise_set_az(jd_jul(1524,4,d),*SP)[1],2))
    for d in range(1,5): print('  ',d,'mai jul', round(rise_set_az(jd_jul(1524,5,d),*SP)[1],2))
