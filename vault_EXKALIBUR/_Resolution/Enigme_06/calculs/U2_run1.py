"""U2 run1 : anagramme d'UN nom (preux/dieu/boisson/planète) ± S,T,ST (,10=TEN/DIX) = lieu en C ? Contre hasard (lettres permutées entre noms)."""
from U2_common import *
H=places_hashes(); PH=np.array(sorted(H),np.int64); print("lieux en C (hash distincts):",len(PH))
deit=load_list("deities"); drinks=load_list("drinks")
SETS={"preux":PREUX,"bacch":BACCH,"planetes":PLAN,"dieux_wd":deit,"boissons_wd":drinks,"boissons_cur":DRINKS_CUR}
EXTRA={"":"","S":"S","T":"T","ST":"ST","TEN":"TEN","DIX":"DIX","STTEN":"STTEN"}
def count(names,extras,minlen=4):
    hits=[]
    for n in names:
        nn=norm(n)
        if len(nn)<3: continue
        for en,ex in extras.items():
            h=hword(nn+ex); 
            if len(nn+ex)<minlen: continue
            if int(h) in H: hits.append((n,en,H[int(h)][0][1],H[int(h)][0][2]))
    return hits
random.seed(1)
def null(names,extras,T=20):
    pool=[c for n in names for c in norm(n)]; res=[]
    for t in range(T):
        random.shuffle(pool); i=0; fake=[]
        for n in names:
            L=len(norm(n)); fake.append("".join(pool[i:i+L])); i+=L
        res.append(len(count(fake,extras)))
    return res
for sn,names in SETS.items():
    hs=count(names,EXTRA); nl=null(names,EXTRA)
    print(f"\n== {sn} ({len(names)} noms) réel={len(hs)} nul={np.mean(nl):.1f}±{np.std(nl):.1f}")
    for h in hs[:40]: print("  ",h)
