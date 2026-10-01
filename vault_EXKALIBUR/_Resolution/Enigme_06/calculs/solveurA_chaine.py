"""Contrainte D = 341.6 km +-1 % (Tour->Battle->Sainte-Chapelle) : quelles chaines de 4 C (ordre monotone) parmi des C 'thematiques' la satisfont ?
Puis taux de base : quelle proportion de 4-sous-ensembles aleatoires (villes en C, pop>5000) la satisfait par pur hasard ?"""
import sys, math, itertools, random, json
sys.stdout.reconfigure(encoding='utf-8')
R=6371.0088
def hav(a,b):
    la1,lo1,la2,lo2=map(math.radians,(*a,*b)); h=math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
P={ # lat, lon (Wikipedia approx.)
'Cluny':(46.4348,4.6585),'Clermont-Ferrand':(45.7788,3.0859),'Cadouin':(44.8115,0.8738),'Cîteaux':(47.1289,5.0936),
'Clairvaux':(48.1467,4.7883),'Chartres':(48.4478,1.4875),'Conques':(44.5992,2.3960),'Chalon-sur-Saône':(46.7806,4.8536),
'Cahors':(44.4475,1.4419),'Carcassonne':(43.2130,2.3491),'Cambrai':(50.1757,3.2350),'Compiègne':(49.4179,2.8261),
'Clichy':(48.9040,2.3060),'Charroux':(46.1428,0.4064),'Chinon':(47.1676,0.2400),'Caen':(49.1829,-0.3707),'Canterbury':(51.2802,1.0789),
'Carnac':(47.5836,-3.0787),'Cherbourg':(49.6337,-1.6221),'Chauvigny':(46.5688,0.6425),'Chaumont':(48.1113,5.1390),
'Corbie':(49.9095,2.5094),'Cousance':(46.5,5.4),'Château-Chalon':(46.7,5.63),'Châtillon-sur-Seine':(47.86,4.57)}
target=341.6
def chain(order): return sum(hav(P[a],P[b]) for a,b in zip(order,order[1:]))
def monotone(order):
    # pas d'aller-retour : les projections sur l'axe principal (1er->dernier) sont monotones
    a=P[order[0]];b=P[order[-1]]
    ax=(b[0]-a[0],(b[1]-a[1])*math.cos(math.radians((a[0]+b[0])/2)))
    pr=[(P[c][0]-a[0])*ax[0]+(P[c][1]-a[1])*math.cos(math.radians((a[0]+b[0])/2))*ax[1] for c in order]
    return all(x<y for x,y in zip(pr,pr[1:]))
names=list(P)
hits=[]
tot=0
for sub in itertools.combinations(names,4):
    best=None
    for perm in itertools.permutations(sub):
        if perm[0]>perm[-1]: continue
        if not monotone(perm): continue
        L=chain(perm); tot+=1
        if abs(L-target)/target<=0.01: hits.append((round(L,1),perm))
print('chaines monotones testees:',tot,'; dans +-1 %:',len(hits))
# cas 'Guilhem' avec 3 C
print('Cluny-Clermont-Cadouin', round(chain(('Cluny','Clermont-Ferrand','Cadouin')),1))
for L,p in sorted(hits)[:40]:
    if 'Cluny' in p and 'Clermont-Ferrand' in p: print('  contient Cluny+Clermont:',L,p)
print('quelques hits:',sorted(hits)[:8])
# taux de base sur communes aleatoires
com=json.load(open('communes.json',encoding='utf-8'))
C=[(n,la,lo) for n,la,lo,p in com if n.upper().startswith('C') and p>=5000]
print('villes C pop>=5000:',len(C))
random.seed(2); ok=0;N=20000
for _ in range(N):
    s=random.sample(C,4)
    good=False
    for perm in itertools.permutations(s):
        if perm[0][0]>perm[-1][0]: continue
        pts=[(c[1],c[2]) for c in perm]
        a,b=pts[0],pts[-1]; cl=math.cos(math.radians((a[0]+b[0])/2)); ax=(b[0]-a[0],(b[1]-a[1])*cl)
        pr=[(q[0]-a[0])*ax[0]+(q[1]-a[1])*cl*ax[1] for q in pts]
        if not all(x<y for x,y in zip(pr,pr[1:])): continue
        L=sum(hav(x,y) for x,y in zip(pts,pts[1:]))
        if abs(L-target)/target<=0.01: good=True;break
    ok+=good
print(f'taux de base: {ok}/{N} = {100*ok/N:.2f} % des 4-sous-ensembles de villes en C (FR) ont une chaine monotone de 341.6 km +-1 %')
