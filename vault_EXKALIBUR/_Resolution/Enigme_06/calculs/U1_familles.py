"""U1 — familles CURÉES (petites), ordres a priori {N>S,O>E,alpha}. Hasard: même procédure, D tirés dans [250,450] (pas 5 km), taux moyen de sous-ensembles à ±1 %."""
import sys, json, itertools, random
sys.path.insert(0, ".")
from solveurB_geo import hav, wiki_coords
import U1_chaines as U
from U1_chaines import ORD, seg_cross, URQ, VAL
sys.stdout.reconfigure(encoding="utf-8")
extra = {"Cariñena":"Cariñena","Calatayud":"Calatayud","Cigales":"Cigales","Colares":"Colares (Sintra)","Corbières":"Corbières AOC",
 "Chalice Well":"Chalice Well","Nanteos":"Nanteos Mansion","Cava-SantSadurni":"Sant Sadurní d'Anoia","Cangas":"Cangas de Onís",
 "Clos-Vougeot":"Clos de Vougeot","Cambus":"Cambus distillery","Cooley":"Cooley Distillery","Cambados":"Cambados","Calvados-Pays-Auge":"Pays d'Auge",
 "Cabrach":"Cabrach","Cushendall":"Cushendall","Coruña":"A Coruña","Cintra":"Cinfães","Cantavieja":"Cantavieja"}
r = wiki_coords(list(extra.values()), "en")
P = dict(U.P)
for k, t in extra.items():
    if r[t]: P[k] = (r[t][0], r[t][1])
    else: print("sans coord:", k)
U.P.update(P)
FAM = {
 "F1 vins/spiritueux France (célèbres)": ["Cognac","Chablis","Cahors","Cassis","Chinon","Chateauneuf-du-Pape","Condrieu","Cornas","Chartreuse","Cadillac","Collioure","Cambremer","Chambolle","Chassagne","Champagne-Chalons","Corbieres"],
 "F2 eaux/thermes France": ["Contrexeville","Cauterets","Chatel-Guyon","Chateldon","Cransac","Capvern","Chaudes-Aigues","Cambo"],
 "F3 whisky/bière UK-IE": ["Campbeltown","Cardhu","Cragganmore","Clynelish","Caol Ila","Coleraine","Cork","Carlow","Clonmel"],
 "F4 Graal/coupe/calice": ["Cebreiro","Compostelle","Cashel","Cadouin","Chalice Well","Nanteos","Cluny","Chartres"],
 "F5 Ibérie vin/spiritueux": ["Carinena","Calatayud","Cebreros","Cadiz","Carcavelos","Cartaxo","Chinchon","Cazalla","Cebreiro"],
 "F6 moines-boisson (Cluny/Cîteaux/Clairvaux/Chartreuse/Clermont/Cahors/Cassis/Cognac/Champagne)": ["Cluny","Citeaux","Clairvaux","Chartreuse","Cahors","Cognac","Chablis","Chinon","Cassis","Champagne-Chalons"],
 "F7 emblématiques multi-pays": ["Cognac","Chartreuse","Cork","Campbeltown","Carinena","Carcavelos","Cahors","Chablis","Cebreiro","Cassis","Calvados","Cadiz"],
}
for k, v in {"Clermont": (45.7787583, 3.0858573)}.items(): U.P[k] = v; P[k] = v
FAM["F6 moines-boisson (Cluny/Cîteaux/Clairvaux/Chartreuse/Clermont/Cahors/Cassis/Cognac/Champagne)"].append("Clermont")
def stats(names, D, tol=.01):
    tot = h = 0
    for s in itertools.combinations(names, 4):
        for on in ("N>S","O>E","alpha"):
            tot += 1; h += abs(U.length(ORD[on](s))/D-1) <= tol
    return h, tot
rnd = random.Random(7)
Ds = [rnd.uniform(250, 450) for _ in range(60)]
for name, lst in FAM.items():
    lst = [n for n in lst if n in U.P]
    h0, t = stats(lst, 341.61); h1, _ = stats(lst, 342.01)
    hr = sum(stats(lst, d)[0] for d in Ds)/len(Ds)
    print(f"\n== {name} : n={len(lst)} tot={t}  hits D=341,61: {h0}  D=342,01: {h1}  | hits moyens à D aléatoire [250,450]: {hr:.1f}")
    for s in itertools.combinations(lst, 4):
        for on in ("N>S","O>E","alpha"):
            ch = ORD[on](s); L = U.length(ch)
            if abs(L/341.61-1) <= .01 or abs(L/342.01-1) <= .01:
                print(f"   {on:6s} {' > '.join(ch)}  L={L:.2f}  croise lame={U.crosses(ch)}")
