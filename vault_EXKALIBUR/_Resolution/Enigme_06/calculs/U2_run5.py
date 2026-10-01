"""U2 run5 : nom (preux/dieu/Liber…)+extras = LIEU en C  +  BOISSON (partition exacte des lettres)  -> 'pas forcément que le lieu'. Nul : noms mélangés."""
from U2_common import *
from collections import Counter
import warnings; warnings.filterwarnings("ignore")
sets=load_names()
places={}
for sn in ("curated","communes","geo_big"):
    for n,d in sets[sn].items():
        if len(n)>=4: places.setdefault(n,(d[0],sn))
pl=list(places)
dk=load_list("drinks"); DK={}
for d in dk+DRINKS_CUR:
    n=norm(d)
    if 3<=len(n)<=12: DK.setdefault(n,d)
DKc={n:d for n,d in DK.items() if n in set(norm(x) for x in DRINKS_CUR)}
print(len(pl),"lieux C;",len(DK),"boissons;",len(DKc),"boissons curées")
def cnt(s): c=[0]*26
def vec(s):
    v=np.zeros(26,np.int8)
    for ch in s: v[ord(ch)-65]+=1
    return v
PV=np.array([vec(p) for p in pl],np.int8); PL=np.array([len(p) for p in pl])
DKeys={"".join(sorted(n)):(n,d) for n,d in DK.items()}
DKcKeys={"".join(sorted(n)):(n,d) for n,d in DKc.items()}
def split(name,keys,minrest=3):
    out=[]
    for en,ex in (("",""),("S","S"),("T","T"),("ST","ST"),("TEN","TEN"),("DIX","DIX")):
        s=norm(name)+ex; v=vec(s); L=len(s)
        ok=np.all(PV<=v[None,:],axis=1)&(PL<=L-minrest)
        for i in np.nonzero(ok)[0]:
            rest=v-PV[i]; k="".join(chr(65+j)*int(rest[j]) for j in range(26) if rest[j])
            if k in keys: out.append((name,en,pl[i],places[pl[i]][0],keys[k][1]))
    return out
def shuffled(names,seed):
    r=random.Random(seed); pool=[c for n in names for c in norm(n)]; r.shuffle(pool); i=0; f=[]
    for n in names:
        L=len(norm(n)); f.append("".join(pool[i:i+L])); i+=L
    return f
names=list(hw(NINE+PREUX+BACCH+PLAN,3).values())
for tag,keys in (("boissons curées",DKcKeys),("boissons wikidata+curées",DKeys)):
    real=[]; 
    for n in names: real+=split(n,keys)
    nl=[]
    for t in range(6):
        c=0
        for n in shuffled(names,t): c+=len(split(n,keys))
        nl.append(c)
    print(f"\n== {tag}: réel={len(real)} nul={np.mean(nl):.1f}±{np.std(nl):.1f} {nl}")
    for r in real[:50]: print("  ",r)
