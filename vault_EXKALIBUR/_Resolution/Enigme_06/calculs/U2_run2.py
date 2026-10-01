"""U2 run2 : paires/triplets de noms (preux, dieux, boissons) + extras (S,T,ST) = lieu en C ? vs hasard."""
from U2_common import *
import itertools, warnings
warnings.filterwarnings("ignore")
H=places_hashes(); PHs=np.array(sorted(H),np.int64)
exec(open(os.path.join(D,"lists_A.py"),encoding="utf-8").read())
GODS=set(load_list("deities"))|set(BACCH)|set(PLAN)
for c in ('grec','romain','nordique','egypte','celte'): GODS|=set(LISTS[c])
GODS=list(hw(GODS,3).values()); P=list(hw(NINE+PREUX,3).values()); DK=list(hw(load_list("drinks")+DRINKS_CUR,3).values())
# boissons dont le nom commence par C exclues (trivial) pour les combinaisons
EX={"":"","S":"S","T":"T","ST":"ST"}
def hv(names): return np.array([int(hword(norm(n))) for n in names],np.int64), np.array([len(norm(n)) for n in names])
def pairs(A,B,ex_h,chunk=2000,minlen=6):
    ha,la=hv(A); hb,lb=hv(B); out=[]
    for i in range(0,len(A),chunk):
        S=ha[i:i+chunk,None]+hb[None,:]
        for en,eh in ex_h.items():
            T=S+eh
            m=np.isin(T,PHs)
            for a,b in zip(*np.nonzero(m)):
                if la[i+a]+lb[b]+len(en)>=minlen: out.append((A[i+a],B[b],en,H[int(T[a,b])][0][1],H[int(T[a,b])][0][2]))
    return out
ex_h={k:np.int64(hword(v)) if v else np.int64(0) for k,v in EX.items()}
def shuffled(names,seed):
    r=random.Random(seed); pool=[c for n in names for c in norm(n)]; r.shuffle(pool); i=0; f=[]
    for n in names:
        L=len(norm(n)); f.append("".join(pool[i:i+L])); i+=L
    return f
def run(tag,A,B,T=8):
    real=pairs(A,B,ex_h); nl=[]
    for t in range(T): nl.append(len(pairs(shuffled(A,t),shuffled(B,100+t),ex_h)))
    print(f"\n== {tag} ({len(A)}x{len(B)}) réel={len(real)} nul={np.mean(nl):.1f}±{np.std(nl):.1f} {nl}",flush=True)
    return real
rp=run("preux x dieux",P,GODS)
for x in rp[:60]: print("  ",x)
json.dump(rp,open("U2_run2_preuxdieux.json","w",encoding="utf-8"),ensure_ascii=False)
DKn=[d for d in DK if norm(d)[0]!="C"]
rb=run("preux x boissons(non-C)",P,DKn)
for x in rb[:40]: print("  ",x)
rg=run("dieux x boissons(non-C)",GODS,DKn,T=3)
print(" sample",rg[:15])
