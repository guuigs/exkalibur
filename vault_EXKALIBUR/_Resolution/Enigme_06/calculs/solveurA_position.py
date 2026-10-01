"""Analyse de la position (lecture des pions de releve.md) : cases vides, moulins, menaces. Sert a verifier la coincidence '10' = cases vides."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from solveurA_board import *
LINES=[]
for r in range(3):
    a,b=r,6-r
    LINES+= [[(a,r),(3,r),(b,r)],[(a,b),(3,b),(b,b)],[(r,a),(r,3),(r,b)],[(b,a),(b,3),(b,b)]]
for y in (3,):
    LINES+= [[(0,3),(1,3),(2,3)],[(4,3),(5,3),(6,3)]]
LINES+= [[(3,0),(3,1),(3,2)],[(3,4),(3,5),(3,6)]]
LINES=[l for l in LINES if all(p in PTS for p in l)]
LINES=[list(x) for x in {tuple(l) for l in LINES}]
print('points',len(PTS),'lignes',len(LINES))
R=set(RED);B=set(BLUE)
empty=[p for p in PTS if p not in R and p not in B]
print('rouges',len(R),'bleus',len(B),'vides',len(empty),empty)
for l in LINES:
    r=sum(p in R for p in l); b=sum(p in B for p in l); e=sum(p in empty for p in l)
    if (r==3) or (b==3): print('MOULIN',l,'R' if r==3 else 'B')
    elif e==1 and (r==2 or b==2): print('menace',('R' if r==2 else 'B'),'sur',[p for p in l if p in empty][0],l)
