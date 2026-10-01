"""U1 — (i) lecture 'exception': 2 premiers C = boisson (vin/spiritueux), 2 derniers = pommes/cidre (Normandie) ; (ii) bloc ibérique nord-ouest (Graal de Galice + albariño/cidre).
Ordres a priori N>S, O>E, alpha. Hasard = D aléatoire dans [250,450] (moyenne de hits)."""
import sys, itertools, random
sys.path.insert(0, ".")
import U1_chaines as U
from U1_chaines import ORD
from solveurB_geo import wiki_coords
sys.stdout.reconfigure(encoding="utf-8")
ex = {"Cambados":"Cambados","Covadonga":"Covadonga","CangasOnis":"Cangas de Onís","Cabranes":"Cabranes","Cerisy-la-Salle":"Cerisy-la-Salle",
      "Condé":"Condé-en-Normandie","Carentan":"Carentan-les-Marais","Cabourg":"Cabourg","Coutances":"Coutances","Cherbourg":"Cherbourg-en-Cotentin","Caudebec":"Caudebec-en-Caux","Cormeilles":"Cormeilles, Eure","Camembert":"Camembert, Orne"}
r = wiki_coords(list(ex.values()), "en")
for k, t in ex.items():
    if r[t]: U.P[k] = (r[t][0], r[t][1])
    else: print("sans coord", k)
def stats(lst, D):
    h = 0; tot = 0; L = []
    for s in itertools.combinations(lst, 4):
        for on in ("N>S","O>E","alpha"):
            ch = ORD[on](s); l = U.length(ch); tot += 1
            if abs(l/D-1) <= .01: h += 1; L.append((on, ch, l))
    return h, tot, L
rnd = random.Random(11); Ds = [rnd.uniform(250,450) for _ in range(80)]
def run(name, lst):
    lst = [n for n in lst if n in U.P]
    h, tot, L = stats(lst, 341.61); h2, _, L2 = stats(lst, 342.01)
    hr = sum(stats(lst, d)[0] for d in Ds)/len(Ds)
    print(f"\n== {name}: n={len(lst)} tot={tot} hits(341,61)={h} hits(342,01)={h2} ; hasard moyen={hr:.2f}")
    for on, ch, l in L + L2: print(f"   {on} {' > '.join(ch)} L={l:.2f} croise lame={U.crosses(ch)}")
run("Iberie NO (Graal Galice, vin/cidre)", ["Cebreiro","Compostelle","Cambados","Covadonga","CangasOnis","Cudillero","Cabranes","Cebreros","Chaves","Coimbra","Carinena"])
# (i) 2 boissons célèbres + 2 Normandie cidre : ordre fixe (2 premiers = ordre N>S dans leur paire ; 2 derniers idem)
drink = ["Cognac","Chablis","Cahors","Cassis","Chinon","Cornas","Condrieu","Chartreuse","Cadillac","Champagne-Chalons","Cluny","Citeaux","Clairvaux","Chateauneuf-du-Pape"]
norm = ["Caen","Cambremer","Cerisy","Cerisy-la-Salle","Condé","Carentan","Cabourg","Coutances","Cherbourg","Caudebec","Cormeilles","Camembert"]
def hits2(D):
    out = []
    for a in itertools.combinations(drink, 2):
        for b in itertools.combinations(norm, 2):
            for oa in (a, a[::-1]):
                for ob in (b, b[::-1]):
                    ch = list(oa)+list(ob)
                    if abs(U.length(ch)/D-1) <= .01: out.append(ch)
    return out
H = hits2(341.61)+hits2(342.01)
n = len(list(itertools.combinations(drink,2)))*len(list(itertools.combinations(norm,2)))*4
print(f"\n== (i) 2 boissons + 2 Normandie : {len(H)} hits / {n} chaînes ({100*len(H)/n:.2f} %) ; hasard (D aléatoire, 15 tirages) : ", end="")
hh = [len(hits2(d)) for d in Ds[:15]]; print(f"{sum(hh)/len(hh):.1f} hits moyens")
for c in H[:20]: print("   ", " > ".join(c), round(U.length(c),2), "croise:", U.crosses(c))
