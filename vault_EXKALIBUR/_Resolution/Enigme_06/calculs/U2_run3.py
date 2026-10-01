"""U2 run3 : lieux en C qui SONT eux-mêmes une boisson (nom identique, ou exact anagramme) : liste + coordonnées."""
from U2_common import *
import warnings; warnings.filterwarnings("ignore")
import json
drinks=load_list("drinks")+DRINKS_CUR
dn={}
for d in drinks:
    n=norm(d)
    if n[:1]=="C" and len(n)>=4: dn.setdefault(n,d)
comm=json.load(open(os.path.join(HERE,"T1data","communes.json"),encoding="utf-8"))
print(type(comm[0]), comm[0])
cm={}
for c in comm:
    n=norm(c["nom"])
    if n in dn: cm.setdefault(n,[]).append(c)
print(len(dn),"boissons en C;",len(cm),"sont des communes FR")
for n,L in sorted(cm.items()): print(n,dn[n],[(c["nom"],round(c.get("pop",0) if isinstance(c,dict) else 0)) for c in L][:3])
