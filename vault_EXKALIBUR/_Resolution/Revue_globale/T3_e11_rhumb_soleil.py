# T3 : angle É11 en loxodromie (My Maps = Mercator + rapporteur) vs azimut solaire ; solveur de date
import math
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
exec(open('T3_jour_dernier.py',encoding='utf-8').read().split("if __name__")[0])
def rhumb(a,b):
    p1,p2=math.radians(a[0]),math.radians(b[0]); dl=math.radians(b[1]-a[1])
    dpsi=math.log(math.tan(math.pi/4+p2/2)/math.tan(math.pi/4+p1/2))
    return (math.degrees(math.atan2(dl,dpsi))+360)%360
SPs={'geo.api centre 43.3173,-1.041':(43.3173,-1.0410),'43.3283,-1.0347 (exk)':(43.3283,-1.0347),'mairie ~43.3290,-1.0360':(43.3290,-1.0360)}
TAs={'tour Avalon 45.4288,6.0308':TA,'château Bayard':CB}
print('== cap géodésique / loxodromique SP -> cibles')
for ks,s in SPs.items():
    for kt,t in TAs.items():
        print(f'  {ks:32s} -> {kt:28s} géod {brg(s,t):.3f}  loxo {rhumb(s,t):.3f}  dist {hav(s,t):.2f}')
tg=[brg(SP:=SPs['43.3283,-1.0347 (exk)'],CB),rhumb(SP,CB)]
print('\n== Azimut lever soleil à Saint-Palais, 30/04/1524 julien, selon horizon h0 :')
for h0 in (-0.833,-0.6,-0.567,-0.5,0.0):
    print('  h0',h0,round(rise_set_az(jd_jul(1524,4,30),*SP,h0=h0)[1],3))
print('\n== Date (julien 1524) où lever SP = cap loxodromique / géodésique (h0=-0.833) :')
for tgt,nm in ((tg[0],'géod'),(tg[1],'loxo')):
    best=min(((abs(rise_set_az(jd_jul(1524,4,1)+x/10,*SP)[1]-tgt),x/10) for x in range(0,600)))
    jd=jd_jul(1524,4,1)+best[1]; print(f'  {nm} {tgt:.3f} -> jour {1+best[1]:.1f} avril julien (résidu {best[0]:.3f})')
# jours à ±0,3° dans l'année, avec horizon -0.833 : combien ?
print('\n== Combien de jours/an (tropical, h0=-0.833) ont lever SP à ±0,3° de 64,90 / 64,99 ? (test du hasard)')
for tgt in (64.90,64.99):
    n=sum(1 for d in range(365) if abs(rise_set_az(jd_greg(2026,1,1)+d,*SP)[1]-tgt)<=0.3)
    print('  cible',tgt,':',n,'jours /365 =',round(n/3.65,2),'%')
print('\n== Coucher : azimut coucher Avalon le 30/04/1524 jul = %.2f ; angle "opposé" SP->CB+180 = %.2f'%(rise_set_az(jd_jul(1524,4,30),*TA)[2],(brg(SP,CB)+180)%360))
# Bayard : dates clés (julien)
print('\n== Autres dates de la vie de Bayard (lever à Avalon / SP)')
for nm,y,m,d in (('Marignan 13/09/1515',1515,9,13),('Marignan 14/09/1515',1515,9,14),('Brescia 19/02/1512',1512,2,19),('Garigliano 29/12/1503',1503,12,29),('Mézières 1521 (~27/09)',1521,9,27),('Rebec = † 30/04/1524',1524,4,30)):
    jd=jd_jul(y,m,d); print(f'  {nm:26s} Avalon lever {rise_set_az(jd,*TA)[1]:.2f}  coucher {rise_set_az(jd,*TA)[2]:.2f} | SP lever {rise_set_az(jd,*SP)[1]:.2f}')
