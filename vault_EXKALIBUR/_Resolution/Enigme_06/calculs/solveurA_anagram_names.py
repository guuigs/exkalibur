from solveurA_lists import *
import random
rows=[]
for cat,lst in LISTS.items():
    for w in lst:
        k=''.join(sorted(norm(w)))
        if len(k)<4: continue
        for (n,cc,p) in byk.get(k,[]):
            if norm(n)!=norm(w): rows.append((cat,w,n,cc,p))
print('== anagrammes exactes mot -> lieu en C (hors identité)')
for r in rows: print(r)
allw=[w for l in LISTS.values() for w in l if len(norm(w))>=4]
random.seed(7)
T=100;hits=[]
for t in range(T):
    h=0
    for w in allw:
        L=list(norm(w)); random.shuffle(L)
        k=''.join(sorted(L))
        for (n,cc,p) in byk.get(k,[]):
            if norm(n)!=norm(w): h+=1
    hits.append(h)
print('NUL: hits sur',len(allw),'mots aux lettres permutées, moyenne',sum(hits)/T,'min',min(hits),'max',max(hits))
print('REEL:',len(rows))
