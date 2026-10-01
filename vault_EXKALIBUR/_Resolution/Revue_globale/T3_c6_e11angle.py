# T3 : (a) 6e C « point de passage » (FAQ06-252) sur la droite É11 ? (b) origine de l'angle 64,99° (c) test hasard
import json,math,os,re
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
SP=(43.3283,-1.0347)  # Saint-Palais (approx.)
try:
    sp=json.loads(get('https://geo.api.gouv.fr/communes?nom=Saint-Palais&codeDepartement=64&fields=nom,centre&format=json'))
    SP=(sp[0]['centre']['coordinates'][1],sp[0]['centre']['coordinates'][0]); print('Saint-Palais geo.api',SP)
except Exception as e: print('SP fallback',e)
TA=(45.4288,6.03078); CBY=CB
print('cap SP->château Bayard %.3f  SP->tour Avalon %.3f  dist SP-CB %.2f SP-TA %.2f'%(brg(SP,CB),brg(SP,TA),hav(SP,CB),hav(SP,TA)))
def xtrack(p,a,b):
    R=6371.0088
    d13=hav(a,p)/R; t13=math.radians(brg(a,p)); t12=math.radians(brg(a,b))
    return math.asin(math.sin(d13)*math.sin(t13-t12))*R, math.acos(max(-1,min(1,math.cos(d13)/math.cos(math.asin(math.sin(d13)*math.sin(t13-t12))))))*R
cache=os.path.expanduser('~/AppData/Local/hermes/cache/scratch/exk_e12/communes_all.json')
if os.path.exists(cache): com=json.load(open(cache,encoding='utf-8'))
else:
    com=json.loads(get('https://geo.api.gouv.fr/communes?fields=nom,centre,population&format=json&geometry=centre',300)); json.dump(com,open(cache,'w',encoding='utf-8'))
print('communes',len(com))
L=hav(SP,TA)
print('\n=== (a) communes en C à moins de 2 km de la droite SP->Avalon (le long de la route, 0..L+5 km), pop>=500 puis toutes')
rows=[]
for c in com:
    if not c['nom'].upper().startswith('C') or 'centre' not in c: continue
    p=(c['centre']['coordinates'][1],c['centre']['coordinates'][0])
    x,a=xtrack(p,SP,TA)
    if abs(x)<=2 and 0<=a<=L+5: rows.append((abs(x),c['nom'],c.get('population',0),round(a,1),round(x,2)))
rows.sort()
print(len(rows),'communes en C dans le couloir ±2 km sur',round(L,1),'km  =>  densité attendue par hasard :',len(rows),'(hasard élevé : aucune preuve possible sans 2e indice)')
for r in rows: 
    if r[2]>=300: print('  ',r[1],'pop',r[2],'abscisse',r[3],'km  écart',r[4],'km')
# (b) angle
print('\n=== (b) dérivations numériques de 64,99° (test du hasard : combien de formules simples tombent à ±0,05°?)')
tgt=brg(SP,CB)
import itertools
nums={'1':1,'3':3,'5':5,'23':23,'12':12,'11':11,'8':8,'10':10,'13':13,'193.13':193.13,'606.6':606.6,'18':18,'37':37,'666':666,'14':14,'24':24,'52':52,'1524':1524,'1515':1515,'1476':1476,'30':30,'4':4,'6':6,'7':7,'9':9}
cons={'1':1,'pi':math.pi,'1/pi':1/math.pi,'e':math.e,'phi':(1+5**.5)/2,'sqrt2':2**.5,'sqrt3':3**.5}
hits=[]
for (n1,v1),(cn,cv) in itertools.product(nums.items(),cons.items()):
    for op,val in (('x',v1*cv),('/',v1/cv),('+',v1+cv)):
        for mod in (1,):
            v=val%360
            for tg,tn in ((tgt,'64.99'),(90-tgt,'90-a'),(tgt+90,'a+90')):
                if abs(v-tg)<=0.05 and tn=='64.99': hits.append((n1,op,cn,round(v,3)))
print('  formules simples (nombre×const) ±0,05° de 64,99 :',hits if hits else 'aucune')
print('  fenêtre ±0,05° = %.2f%% des 360° => hasard attendu pour ~%d formules : %.2f coups'%(0.1/360*100,len(nums)*len(cons)*3,len(nums)*len(cons)*3*0.1/360))
print('  Discord 23 pierres × π = %.3f° ; miss lateral at 606 km: %.1f km'%(23*math.pi,606*math.radians(abs(23*math.pi-tgt))))
# angle par rapport à l'axe lame É1 (Lombrives -> Urquhart)
LOMB=(42.8203,1.6206); URQ=(57.3243,-4.4419); VAL=(39.4753,-0.3753)
print('  axe lame Lombrives->Urquhart %.2f ; SP->CB relatif = %.2f'%(brg(LOMB,URQ),(tgt-brg(LOMB,URQ))%360))
GARDE=brg((42.5991,-5.5670),(42.9656,1.6053)); print('  cap garde León->Foix %.2f ; angle relatif %.2f'%(GARDE,(tgt-GARDE)%360))
NG=brg((48.8554,2.345),(47.7482,-3.3702)); print('  cap nouvelle garde SC->Lorient %.2f (inverse %.2f) ; relatif %.2f'%(NG,(NG+180)%360,(tgt-NG)%360))
print('  cap Sainte-Chapelle->Chartres %.2f  Camors->Chartres %.2f  Lorient->Chartres..'%(brg((48.8554,2.345),(48.4477,1.4876)),brg((47.8321,-3.005),(48.4477,1.4876))))
