"""U2 run6c : partition exacte d'une phrase en k lieux en C (meet-in-the-middle), nul par perturbation de lettres."""
from U2_common import *
import warnings, time; warnings.filterwarnings("ignore")
from collections import defaultdict
sets=load_names()
def build(setnames,minlen=4,maxlen=16):
    P={}
    for sn in setnames:
        for n,d in sets[sn].items():
            if minlen<=len(n)<=maxlen: P.setdefault(n,d[0])
    return P
def vec(s):
    v=np.zeros(26,np.int16)
    for ch in s: v[ord(ch)-65]+=1
    return v
def solve2(s,P,k,lim=200):
    tot=vec(s); nm=[n for n in P if np.all(vec(n)<=tot)]
    if len(nm)<k: return []
    V=np.array([vec(n) for n in nm]); L=V.sum(1)
    sols=set()
    if k==2: pairs=[(i,j) for i in range(len(nm)) for j in range(i,len(nm)) if np.array_equal(V[i]+V[j],tot)]
    else:
        # k=3: boucle sur i<=j, cherche troisième par dict ; k=4: paires <-> paires
        key=lambda v: v.tobytes()
        if k==3:
            D={key(V[i]):i for i in range(len(nm))}
            for i in range(len(nm)):
                for j in range(i,len(nm)):
                    r=tot-V[i]-V[j]
                    if r.min()<0: continue
                    t=D.get(key(r))
                    if t is not None and t>=j: sols.add(tuple(sorted((nm[i],nm[j],nm[t]))))
                    if len(sols)>=lim: return sorted(sols)
            return sorted(sols)
        if k==4:
            PD=defaultdict(list)
            for i in range(len(nm)):
                for j in range(i,len(nm)):
                    sv=V[i]+V[j]
                    if np.all(sv<=tot): PD[key(sv)].append((i,j))
            for kk,lst in PD.items():
                r=tot-np.frombuffer(kk,dtype=np.int16)
                for a in lst:
                    for b in PD.get(key(r),[]):
                        sols.add(tuple(sorted((nm[a[0]],nm[a[1]],nm[b[0]],nm[b[1]]))))
                if len(sols)>=lim: break
            return sorted(sols)
    return pairs
PH={"A":"Observe la partie, preux contre dieux. Commencera le Père, et finiront les cieux.","B":"preux contre dieux commencera le Pere et finiront les cieux"}
if __name__=="__main__":
    t0=time.time()
    P=build(["curated","communes","geo_big"],4,16); print(len(P),"noms",flush=True)
    for tag in PH:
        for ex in ("","S","T","ST"):
            s=norm(PH[tag])+ex
            for k in (3,4):
                r=solve2(s,P,k); print(tag,ex,"k",k,"n=",len(r),r[:5],round(time.time()-t0),flush=True)
    base=norm(PH["B"]); r=random.Random(11); nl=[]
    pool="EEEEEEEAAAIIINNNRRRSSSTTTOOOLLUUDDMP"
    for t in range(8):
        L=list(base)
        for j in r.sample(range(len(L)),10): L[j]=r.choice(pool)
        for j in r.sample([i for i,c in enumerate(L) if c!="C"],max(0,4-L.count("C"))): L[j]="C"
        nl.append(len(solve2("".join(L),P,4)))
    print("NUL k=4:",nl,round(time.time()-t0))
