"""Modèle du plateau (7x7, 24 points) + pions lus sur R4G (coordonnées col,row ; row 0 = haut)."""
import itertools
PTS=[(x,y) for r in range(3) for (x,y) in
     [(a,b) for a in (r,3,6-r) for b in (r,3,6-r) if not (a==3 and b==3)]]
PTS=sorted(set(PTS), key=lambda p:(p[1],p[0]))
assert len(PTS)==24
RED=[(3,0),(1,3),(1,5),(3,5),(0,6),(3,6),(4,3)]
BLUE=[(0,0),(6,0),(1,1),(3,1),(5,3),(5,5),(4,2)]
BLUE_ILLUS=[(0,0),(6,0),(1,1)]
BLUE_PLAIN=[p for p in BLUE if p not in BLUE_ILLUS]
def ring_seq(r, start, cw=True):
    c=[(r,r),(3,r),(6-r,r),(6-r,3),(6-r,6-r),(3,6-r),(r,6-r),(r,3)]  # horaire depuis coin haut-gauche
    if not cw: c=[c[0]]+c[:0:-1]
    k=start%8
    return c[k:]+c[:k]
def schemes():
    S={}
    S['ligne']=sorted(PTS,key=lambda p:(p[1],p[0]))
    S['colonne']=sorted(PTS,key=lambda p:(p[0],p[1]))
    for order in ('ext-int','int-ext'):
        rs=[0,1,2] if order=='ext-int' else [2,1,0]
        for cw in (True,False):
            for st in range(8):
                S[f'anneaux {order} {"cw" if cw else "ccw"} d{st}']=[p for r in rs for p in ring_seq(r,st,cw)]
    # spirale : un seul parcours ext->int, l'anneau suivant démarre là où finit le précédent
    return S
ALPH={'A-X':'ABCDEFGHIJKLMNOPQRSTUVWX',
      'L24(sans J,W)':'ABCDEFGHIKLMNOPQRSTUVXYZ',
      'L23(sans J,U,W)':'ABCDEFGHIKLMNOPQRSTVXYZ',
      'A-Z(26)':'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
