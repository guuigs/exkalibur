from U2_run6 import *
import time
Pcom=build(["curated","communes"],4,13)
Pall=build(["curated","communes","geo_big"],4,13)
print(len(Pcom),len(Pall))
def nsol(ph,P,k,ex="",limit=300):
    return solve(norm(ph)+ex,P,k,limit=limit)
t0=time.time()
for tag in ("A_partie+Pere","B_preux_dieux_Pere_cieux"):
    for ex in ("","S","T","ST"):
        sol=nsol(PH[tag],Pcom,4,ex,limit=500)
        print(tag,ex,"communes k4:",len(sol),sol[:4],round(time.time()-t0),flush=True)
# nul : 10 phrases aléatoires de même longueur avec exactement 4 C (lettres tirées de la distribution de lettres du français d'une phrase quelconque), k=4
base=norm(PH["B_preux_dieux_Pere_cieux"]); r=random.Random(11); nl=[]
for t in range(10):
    L=list(base); r.shuffle(L); 
    # garantit 4 C : on garde multiset du réel mais échange 4 lettres avec aléatoires -> nul 'doux' : on permute 12 lettres avec des lettres fréquentes
    pool="EEEEEEEAAAIIINNNRRRSSSTTTOOOLLUUDDCMP"
    for j in r.sample(range(len(L)),10): L[j]=r.choice(pool)
    s="".join(L); 
    if s.count("C")<4: 
        for j in r.sample([i for i,c in enumerate(L) if c!="C"],4-s.count("C")): L[j]="C"
        s="".join(L)
    nl.append(len(solve(s,Pcom,4,limit=500)))
print("NUL (perturbation de 10 lettres, >=4 C):",nl,round(time.time()-t0))
