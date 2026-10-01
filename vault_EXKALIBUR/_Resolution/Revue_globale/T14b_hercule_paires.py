import json, math, itertools
exec(open('T14_inverse_toponymes.py').read().split("S={")[0].split("D=json")[0])  # imports only
D=json.load(open('T11_roches_web/lieux_dits_bruts.json'))
def hav(a,b):
    R=6371000;p1,p2=math.radians(a[0]),math.radians(b[0]);dl=math.radians(b[1]-a[1]);dp=p2-p1
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(h))
def brg(a,b):
    p1,p2=math.radians(a[0]),math.radians(b[0]);dl=math.radians(b[1]-a[1])
    return math.degrees(math.atan2(math.sin(dl)*math.cos(p2),math.cos(p1)*math.sin(p2)-math.sin(p1)*math.cos(p2)*math.cos(dl)))%360
P={x['nom']+'|'+x['commune']:(x['lat'],x['lon']) for x in D}
X={'tour':(45.4288,6.03078),'rue_rempart':(45.42977,6.03118),'avalon_ld':(45.42956,6.03126),'bayard':(45.42337,6.01894),'pierre_gros':P['PIERRE GROS|Saint-Maximin'],'chene_roche_vivier':P['LE CHENE LA ROCHE ET LE VIVIER|Saint-Maximin'],
 'HERCULEE':P['HERCULEE|Pontcharra'],'HERCULER':P['HERCULER|Pontcharra'],'BRAME_FARINE':P['BRAME FARINE|Pontcharra'],'CHANTE_MERLE':P['CHANTE-MERLE|Saint-Maximin'],'VERGER_BAYARD':P['VERGER DE BAYARD|Pontcharra']}
names=list(X)
print('%-20s'%''+''.join('%11s'%n[:10] for n in names))
for a in names:
    print('%-20s'%a+''.join('%11.0f'%hav(X[a],X[b]) for b in names))
print()
for a,b in [('HERCULEE','avalon_ld'),('HERCULEE','tour'),('HERCULEE','rue_rempart'),('HERCULEE','bayard'),('HERCULER','tour'),('CHANTE_MERLE','tour')]:
    print('%s -> %s : %.0f m, cap %.1f°, écart à 1850 : %+.2f %%'%(a,b,hav(X[a],X[b]),brg(X[b],X[a]),(hav(X[a],X[b])/1850-1)*100))
# toutes les paires de lieux-dits à 1850 m ±1 % dans 4 km de la tour, contenant un toponyme thématique
import re,unicodedata
def na(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
near=[(k,v) for k,v in P.items() if hav(X['tour'],v)<5000]
print('\nlieux-dits <5 km de la tour:',len(near))
th=re.compile(r'hercul|biche|cerf|daim|brame|diane|pomm|verger|avalon|chant|merle|dragon|serpent')
for (a,va),(b,vb) in itertools.combinations(near,2):
    d=hav(va,vb)
    if 1831<=d<=1869 and (th.search(na(a)) or th.search(na(b))): print('PAIRE 1850±1%%  %s <-> %s : %.0f m'%(a,b,d))
print('--- paires thématiques <-> thématiques (toutes distances)')
tt=[(k,v) for k,v in near if th.search(na(k))]
for (a,va),(b,vb) in itertools.combinations(tt,2): print('  %-40s %-40s %.0f m'%(a,b,hav(va,vb)))
