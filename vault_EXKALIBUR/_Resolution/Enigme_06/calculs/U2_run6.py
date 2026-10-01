"""U2 run6 : phrase (lettres) -> partition exacte en k noms de lieux commençant par C (k=3,4), ± S,T. Phrases: énoncé (4 C dans 'contre/Commencera/cieux').
Nul : phrases de même longueur aléatoires (lettres tirées de la phrase réelle, mélangées ; et phrases de la même énigme)."""
from U2_common import *
import warnings, sys; warnings.filterwarnings("ignore")
from collections import Counter
sets=load_names()
def build(setnames,minlen=4,maxlen=14):
    P={}
    for sn in setnames:
        for n,d in sets[sn].items():
            if minlen<=len(n)<=maxlen: P.setdefault(n,d[0])
    return P
def vec(s):
    v=[0]*26
    for ch in s: v[ord(ch)-65]+=1
    return tuple(v)
def solve(phrase,P,k,limit=2000,minlen=4):
    tot=vec(phrase); L=len(phrase)
    # les C de la phrase : chaque nom commence par C -> k <= nbC
    names=[(n,vec(n)) for n in P if all(a<=b for a,b in zip(vec(n),tot))]
    sols=[]
    def rec(rem,start,chosen,left):
        if len(sols)>=limit: return
        if left==0:
            if not any(rem): sols.append(tuple(chosen))
            return
        remL=sum(rem)
        if remL<minlen*left: return
        for i in range(start,len(names)):
            n,v=names[i]
            if all(a<=b for a,b in zip(v,rem)):
                r2=tuple(b-a for a,b in zip(v,rem))
                if left>1 and sum(r2)<minlen*(left-1): continue
                if left==1 and any(r2): continue
                rec(r2,i,chosen+[n],left-1)
    rec(tot,0,[],k)
    return sols
PH={
"A_partie+Pere":"Observe la partie, preux contre dieux. Commencera le Père, et finiront les cieux.",
"B_preux_dieux_Pere_cieux":"preux contre dieux commencera le Pere et finiront les cieux",
"C_pater_pointe":"Commencera le Père, et finiront les cieux.",
}
if __name__=="__main__":
    Pcur=build(["curated"],4,14)
    Pcom=build(["curated","communes"],4,13)
    print(len(Pcur),"curated;",len(Pcom),"curated+communes")
    for tag,ph in PH.items():
        for ex in ("","S","T","ST"):
            s=norm(ph)+ex; nC=s.count("C")
            for pn,P in (("cur",Pcur),):
                for k in (3,4):
                    if k>nC: continue
                    sol=solve(s,P,k,limit=500)
                    print(tag,ex,"len",len(s),"nC",nC,pn,"k",k,"sols",len(sol),sol[:6],flush=True)
