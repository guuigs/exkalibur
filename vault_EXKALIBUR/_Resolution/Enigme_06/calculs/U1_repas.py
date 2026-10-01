"""U1 — ordre 'repas' fixé a priori : Cassis(apéritif) < Chablis < Cahors < Champagne(Châlons) < Cognac < Chartreuse (digestif). + Cidre(Cambremer) et Calvados(Caen)."""
import sys, itertools, random
sys.path.insert(0, ".")
import U1_chaines as U
from U1_chaines import hav
sys.stdout.reconfigure(encoding="utf-8")
rank = ["Cassis","Chablis","Chinon","Cahors","Champagne-Chalons","Cambremer","Chateauneuf-du-Pape","Cognac","Caen","Chartreuse"]
print("ordre repas :", rank)
def L(ch): return U.length(ch)
n = h = 0
for s in itertools.combinations(rank, 4):
    ch = list(s)  # ordre repas = ordre de rank
    l = L(ch); n += 1
    ok = abs(l/341.61-1) <= .01 or abs(l/342.01-1) <= .01
    h += ok
    if ok: print("HIT", ch, round(l,2), "croise lame:", U.crosses(ch))
print("sous-ensembles", n, "hits", h)
rnd = random.Random(2); Ds=[rnd.uniform(250,450) for _ in range(200)]
m = 0
for d in Ds:
    for s in itertools.combinations(rank, 4):
        m += abs(L(list(s))/d-1) <= .01
print(f"hasard : hits moyens à D aléatoire = {m/len(Ds):.2f} sur {n}")
# eau : ordre N>S
