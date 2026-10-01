"""Piste 3 (étendue) : groupes naturels de cases (anneau, côté, couleur, illustré) -> lettres via alphabets/parcours -> anagramme exacte d'un lieu en C.
Compare au nul (placements aléatoires des 14 pions)."""
import sys, random, collections
sys.stdout.reconfigure(encoding='utf-8')
from solveurA_board import *
from solveurA_lists import norm, places, byk
CUR=[v[0] for k,v in places.items() if v[1]=='CUR']
curk=collections.defaultdict(list)
for n in CUR: curk[''.join(sorted(norm(n)))].append(n)
S=schemes()
def side(p):
    x,y=p; ring=min(x,y,6-x,6-y)
    return ring
def groups(red,blue):
    G={}
    for col,pts in (('R',red),('B',blue),('RB',red+blue)):
        G[col+':tous']=pts
        for r in range(3): G[f'{col}:anneau{r}']=[p for p in pts if side(p)==r]
        G[col+':haut']=[p for p in pts if p[1]<3]; G[col+':bas']=[p for p in pts if p[1]>3]
        G[col+':gauche']=[p for p in pts if p[0]<3]; G[col+':droite']=[p for p in pts if p[0]>3]
        G[col+':coins']=[p for p in pts if p[0] in (side(p),6-side(p)) and p[1] in (side(p),6-side(p))]
        G[col+':milieux']=[p for p in pts if 3 in p]
    return G
def scan(red,blue,cur_only):
    hits=[]
    D=curk if cur_only else byk
    for sn,sc in S.items():
        idx={p:i for i,p in enumerate(sc)}
        for an,al in ALPH.items():
            for rev in (0,1):
                a=al[::-1] if rev else al
                for gn,pts in groups(red,blue).items():
                    if len(pts)<4: continue
                    L=[a[idx[p]] for p in pts if idx[p]<len(a)]
                    for extra in ('','S','T','ST'):
                        key=''.join(sorted(L+list(extra)))
                        if key in D: hits.append((sn,an,rev,gn,extra,key,[x if isinstance(x,str) else x[0] for x in D[key]][:2]))
    return hits
h=scan(RED,BLUE,True)
print('REEL vs liste curée (%d noms):'%len(CUR),len(h))
for x in h[:15]: print(x)
h2=scan(RED,BLUE,False)
print('REEL vs 11 800 lieux en C:',len(h2))
for x in h2[:15]: print(x)
random.seed(11)
n1=[];n2=[]
for t in range(30):
    pts=random.sample(PTS,14)
    n1.append(len(scan(pts[:7],pts[7:],True))); n2.append(len(scan(pts[:7],pts[7:],False)))
print('NUL curé: ',n1,'\nNUL 11800:',n2)
