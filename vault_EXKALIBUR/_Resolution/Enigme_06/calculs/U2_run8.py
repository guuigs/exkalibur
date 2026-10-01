"""U2 run8 : (a) sous-ensembles de 3-4 noms (preux / planètes / preux+planètes) ± S,T,TEN -> 1 lieu en C, vs nul ; (b) Liber Pater & variantes -> lieux C ; (c) 7 planètes entières, partition k=2,3 (petites listes)."""
from U2_common import *
import itertools, warnings; warnings.filterwarnings("ignore")
H=places_hashes()
W9=['Hector','Alexandre','Cesar','Josue','David','Judas','Arthur','Charlemagne','Godefroy']
PL={"fr":['Lune','Mercure','Venus','Soleil','Mars','Jupiter','Saturne'],"lat":['Luna','Mercurius','Venus','Sol','Mars','Iuppiter','Saturnus'],"en":['Moon','Mercury','Venus','Sun','Mars','Jupiter','Saturn']}
def sub(pool,rs=(2,3,4),extras=("","S","T","ST","TEN","DIX")):
    res=[]
    for r in rs:
        for c in itertools.combinations(pool,r):
            b="".join(norm(x) for x in c)
            for ex in extras:
                h=int(hword(b+ex))
                if h in H: res.append((c,ex,H[h][0][1]))
    return res
def nullf(pool,t):
    r=random.Random(t); pl=[c for n in pool for c in norm(n)]; r.shuffle(pl); i=0; f=[]
    for n in pool: L=len(norm(n)); f.append("".join(pl[i:i+L])); i+=L
    return f
pools={"9preux":W9,"pl_fr":PL["fr"],"pl_lat":PL["lat"],"pl_en":PL["en"],"preux+pl_fr":W9+PL["fr"]}
for tag,pool in pools.items():
    real=sub(pool); nl=[len(sub(nullf(pool,t))) for t in range(10)]
    print(tag,"réel",len(real),"nul %.1f±%.1f"%(np.mean(nl),np.std(nl)),nl)
    for x in real[:12]: print("   ",x)
print("\n-- Liber Pater & co")
for w in ["Liber Pater","Liber","Liber Pater Libera","Pater","Libera","Libera Liber Ceres","Bacchus","Dionysos","Dionysus","Dionysos Bacchus","Bacchus Liber"]:
    for ex in ("","S","T","ST","TEN","DIX","STTEN"):
        s=norm(w)+ex
        if int(hword(s)) in H: print(w,ex,"->",H[int(hword(s))])
