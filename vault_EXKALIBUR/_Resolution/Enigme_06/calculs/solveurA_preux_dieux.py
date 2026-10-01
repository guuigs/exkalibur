"""Piste 1 : paires/triplets (preux, dieu) -> concaténation anagrammée = lieu en C ? (avec ou sans S/T). Nul : mêmes tests avec des noms mélangés."""
import sys, itertools, random, collections
sys.stdout.reconfigure(encoding='utf-8')
from solveurA_lists import *
preux=['Hector','Alexandre','Cesar','Josue','David','Judas Maccabee','Arthur','Charlemagne','Godefroy de Bouillon']
gods=sorted({w for c in ('grec','romain','nordique','egypte','celte') for w in LISTS[c]})
def hits(A,B,tag):
    res=[]
    for a in A:
        for b in B:
            for ex in ('','S','T','ST'):
                k=''.join(sorted(norm(a)+norm(b)+ex))
                for v in byk.get(k,[]):
                    res.append((a,b,ex,v[0],v[1]))
    return res
h=hits(preux,gods,'pd')
print('REEL preux x dieux (%d x %d paires):'%(len(preux),len(gods)),len(h))
for x in h[:20]: print(x)
# nul : dieux remplacés par mots aléatoires de même longueur (lettres mélangées de vrais dieux)
random.seed(5); cnt=[]
for t in range(20):
    G=[]
    for g in gods:
        L=list(norm(g)); random.shuffle(L); G.append(''.join(L))
    cnt.append(len(hits(preux,G,'n')))
print('NUL (20 tirages, dieux mélangés):',cnt)
# triplets preux+preux (sans dieux)
h2=[]
for a,b in itertools.combinations(preux,2):
    for ex in ('','S','T','ST'):
        k=''.join(sorted(norm(a)+norm(b)+ex))
        for v in byk.get(k,[]): h2.append((a,b,ex,v[0]))
print('preux+preux:',h2)
