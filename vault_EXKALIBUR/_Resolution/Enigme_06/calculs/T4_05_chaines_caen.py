"""T4_05 : réutilise solveurB_08 (noyau restreint 19 lieux) avec D = valeurs des candidats Caen/Bayeux/MSM ; ±1 %. Chaînes ordre évident (= plus court chemin) marquées."""
import sys, itertools; sys.path.insert(0,'.')
import numpy as np
import solveurB_05_chaines as s5
s5.TARGETS.clear()
T={"Dames direct":258.90,"Dames via Battle":278.00,"Dames via Hastings":283.16,"Hommes direct":259.54,"Hommes via Battle":278.93,"Hommes via Hastings":284.15,
   "Bayeux direct":252.19,"Bayeux via Battle":277.75,"Bayeux via Hastings":284.12,"MSM direct":335.36,"MSM via Battle":367.83}
s5.TARGETS.update(T)
import solveurB_08_noyau as s8
s8.TARGETS=s5.TARGETS
names=[c for c in s8.CORE if c in ("Clermont","Cluny","Cadouin","Cîteaux","Clairvaux","Chartres","Conques","Compostelle","Canterbury","Caerleon","Cadbury Castle (Camelot)","Carcassonne","Caen","Chinon","Cahors","Carlisle","Colchester","Cologne","Constantinople (Sainte-Sophie)")]
out,names,M,P=s8.run(names,"noyau restreint 19 lieux, D des candidats Caen")
def best(ix):
    return min(sum(M[p[i],p[i+1]] for i in range(3)) for p in itertools.permutations(ix))
for tn in ("Dames via Battle","Hommes via Battle","Bayeux via Battle","Dames direct","Bayeux direct"):
    print("\n--",tn,T[tn])
    for L,a,b,c,d in sorted(out[tn],key=lambda r:abs(r[0]-T[tn]))[:10]:
        print(f"  {L:7.2f} ({100*(L/T[tn]-1):+.2f}%) "+" - ".join(names[i] for i in (a,b,c,d))," | plus court:",round(best((a,b,c,d)),2))
