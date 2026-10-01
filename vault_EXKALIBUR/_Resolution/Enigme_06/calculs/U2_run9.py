"""U2 run9 : titre / phrases courtes (Libera nos a malo ; Liber Pater ; HAROLD REX INTERFECTUS EST ; preux contre dieux ; Pater noster...) -> partition en 1..4 lieux en C ± S,T,10"""
from U2_run6c import *
P=build(["curated","communes","geo_big"],4,22); print(len(P),flush=True)
phr=["Libera nos a malo","Liber Pater","Libera nos a malo Liber Pater","preux contre dieux","preux contre dieux Pere cieux","Commencera le Pere et finiront les cieux","Pater noster qui es in caelis","Notre Pere qui etes aux cieux","Harold Rex Interfectus Est","Sub rosa","Dis Pater","Liber Pater Dionysos Bacchus","Sepulcre coupe de vie","Amen","Dieu le Pere"]
hits=[]
for ph in phr:
    for ex in ("","S","T","ST","TEN","DIX","STTEN"):
        s=norm(ph)+ex
        for k in (1,2,3,4):
            if k==1:
                r=[n for n in P if sorted(n)==sorted(s)]
            else: r=solve2(s,P,k,lim=20)
            if r: hits.append((ph,ex,k,len(r),r[:3])); print(ph,"|",ex,"|k",k,"|",len(r),r[:3],flush=True)
print("fini",len(hits))
