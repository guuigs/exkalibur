# T14 : recherche INVERSE — lieux-dits (cadastre, 671) à ~10 stades (1850 m) des départs candidats,
# puis filtre sémantique (Dieu favorable / biche-Hercule / chant / roche / eau).  Local, sans réseau.
import json, math, re, unicodedata
D=json.load(open('T11_roches_web/lieux_dits_bruts.json'))
def na(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
def hav(a,b):
    R=6371000;p1,p2=math.radians(a[0]),math.radians(b[0]);dl=math.radians(b[1]-a[1]);dp=p2-p1
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(h))
def brg(a,b):
    p1,p2=math.radians(a[0]),math.radians(b[0]);dl=math.radians(b[1]-a[1])
    return math.degrees(math.atan2(math.sin(dl)*math.cos(p2),math.cos(p1)*math.sin(p2)-math.sin(p1)*math.cos(p2)*math.cos(dl)))%360
S={'tour':(45.4288,6.03078),'rue_rempart':(45.42977,6.03118),'avalon_lieudit':(45.42956,6.03126),'bayard':(45.42337,6.01894)}
pts=[(x['nom'],x['commune'],(x['lat'],x['lon'])) for x in D]
print('lieux-dits',len(pts),'| dist max à la tour km',max(hav(S['tour'],p[2]) for p in pts)/1000)
SEM={'dieu/grâce':r'dieu|jean\b|jehan|\bjan\b|anne\b|\bsainte? ?anne|grace|bon\b|beni|favor|theo|dieudonne|mathieu|donat',
 'biche/Hercule':r'biche|cerf|daim|chevrette|brame|diane|artemis|ladon|cerynie|hercule|verger|pomm|hesper|dragon|serpent|vouivre',
 'chant/oiseau':r'chant|merle|rossignol|\bcoucou|pinson',
 'roche':r'roche|rocher|\broc\b|pierre|perr|rochat|blocs?|erratique|\bpeyr',
 'eau':r'ruisseau|\bnant\b|source|fontaine|\bfont\b|etang|mare|vivier|\bbief|lavoir|\bgour|cascade',
 'souche/bois':r'souche|chene|chesne|fouteau|\bfau\b|hetre|charpent|\bbois\b|vieux',
 'clairiere':r'clairiere|clair\b|\bclos\b|\bplan\b|champ|pre\b|\bpres\b|\blayat|essart|\bchamp'}
for sn,s in S.items():
    print('\n=== départ',sn,s)
    ring=[(hav(s,c),brg(s,c),n,com,c) for n,com,c in pts if 1750<=hav(s,c)<=1950]
    ring.sort()
    print(' anneau 1750-1950 m : %d lieux-dits'%len(ring))
    for d,b,n,com,c in ring:
        tags=[k for k,r in SEM.items() if re.search(r,na(n))]
        print('  %5.0f m cap %3.0f° %-38s %-22s %s %s'%(d,b,n,com,'(%.5f,%.5f)'%c,'|'.join(tags)))
print('\n=== SEMANTIQUE GLOBALE (tous lieux-dits, dist à la tour) ===')
for k,r in SEM.items():
    if k in('clairiere',): continue
    print('--',k)
    for d,b,n,com,c in sorted((hav(S['tour'],c),brg(S['tour'],c),n,com,c) for n,com,c in pts if re.search(r,na(n)))[:25]:
        print('   %5.2f km cap %3.0f° %-40s %-20s (%.5f,%.5f)'%(d/1000,b,n,com,*c))
