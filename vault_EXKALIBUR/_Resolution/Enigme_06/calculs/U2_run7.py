"""U2 run7 : ensembles entiers (9 preux, 7 planètes fr/lat/en, 7+9...) ± S,T,TEN/DIX -> partition en 2..4 lieux en C; + sous-ensembles (triplets/quadruplets) -> 1 lieu. Nul: lettres mélangées."""
from U2_run6c import *
import itertools
P=build(["curated","communes","geo_big"],4,22)
H=places_hashes()
W9=['Hector','Alexandre','Cesar','Josue','David','Judas','Arthur','Charlemagne','Godefroy']
W9b=['Hector','Alexandre','Cesar','Josue','David','Judas Maccabee','Arthur','Charlemagne','Godefroy de Bouillon']
PL={"fr":['Lune','Mercure','Venus','Soleil','Mars','Jupiter','Saturne'],"lat":['Luna','Mercurius','Venus','Sol','Mars','Iuppiter','Saturnus'],"en":['Moon','Mercury','Venus','Sun','Mars','Jupiter','Saturn'],"gr":['Selene','Hermes','Aphrodite','Helios','Ares','Zeus','Cronos']}
SETS={"9preux":W9,"9preux_b":W9b,**{"pl_"+k:v for k,v in PL.items()}}
t0=time.time()
for tag,S in SETS.items():
    base="".join(norm(x) for x in S)
    for ex in ("","S","T","ST","TEN","STTEN","DIX","STDIX"):
        s=base+ex
        out=[]
        for k in (2,3,4):
            r=solve2(s,P,k,lim=50); out.append((k,len(r),r[:2]))
        if any(o[1] for o in out): print(tag,ex,len(s),out,flush=True)
print("ensembles entiers terminés",round(time.time()-t0),flush=True)
# sous-ensembles 3-4 noms -> un seul lieu en C
def hs(s): return int(hword(s))
def sub(pool,tag,extras=("","S","T","ST","TEN","DIX")):
    res=[]
    for r in (3,4):
        for c in itertools.combinations(pool,r):
            b="".join(norm(x) for x in c)
            for ex in extras:
                h=hs(b+ex)
                if h in H: res.append((c,ex,H[h][0][1]))
    return res
pools={"9preux":W9,"pl_fr":PL["fr"],"pl_lat":PL["lat"],"pl_en":PL["en"],"preux+planetes_fr":W9+PL["fr"]}
for tag,pool in pools.items():
    real=sub(pool,tag)
    # nul : lettres mélangées
    nl=[]
    for t in range(10):
        r=random.Random(t); pl=[c for n in pool for c in norm(n)]; r.shuffle(pl); i=0; f=[]
        for n in pool: L=len(norm(n)); f.append("".join(pl[i:i+L])); i+=L
        nl.append(len(sub(f,tag)))
    print(tag,"réel",len(real),"nul",np.mean(nl),nl, real[:6],flush=True)
