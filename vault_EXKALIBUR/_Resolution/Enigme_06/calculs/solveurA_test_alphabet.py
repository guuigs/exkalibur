"""Piste 3 : position -> lettre (alphabet de 23/24/26 lettres), pions -> lettres, anagramme exacte d'un toponyme en C ?"""
import json,sys,random,unicodedata,collections
sys.stdout.reconfigure(encoding='utf-8')
from solveurA_board import *
def norm(s):
    s=unicodedata.normalize('NFD',s.upper()); s=''.join(c for c in s if c.isalpha() and unicodedata.category(c)[0]=='L' and ord(c)<128)
    return s
com=json.load(open('communes.json',encoding='utf-8'))
names=[(n,norm(n)) for n,_,_,_ in com if n.upper().startswith('C')]
extra=['Cluny','Clermont','Clermont-Ferrand','Cadouin','Conques','Cîteaux','Clairvaux','Chartres','Compostelle','Canterbury','Cantorbéry','Constantinople','Césarée','Chypre','Carcassonne','Cambrai','Corbie','Cordoue','Cologne','Chinon','Camelot','Carduel','Caerleon','Carlisle','Cardiff','Colchester','Chichester','Canterbury','Chester','Cambridge','Chelmsford','Crécy','Carnac','Chalon','Cahors','Chambord','Compiègne','Cesarea','Cantorbery','Cambria','Cornouailles','Cornwall','Cologne','Caen']
names+= [(n,norm(n)) for n in extra]
byk=collections.defaultdict(list)
for n,k in names: byk[''.join(sorted(k))].append(n)
maxlen=max(len(k) for _,k in names)
def exact(ms):
    return byk.get(''.join(sorted(ms)),[])
import functools
NC=[(n,k,collections.Counter(k)) for n,k in names]
@functools.lru_cache(None)
def contained_key(key,minlen):
    c=collections.Counter(key); return tuple(n for n,k,ck in NC if minlen<=len(k)<=len(key) and not (ck-c))
def contained(ms,minlen): return contained_key(''.join(sorted(ms)),minlen)
def letters(scheme,alph,pts):
    idx={p:i for i,p in enumerate(scheme)}
    return [alph[idx[p]] for p in pts if idx[p]<len(alph)]
S=schemes()
sets={'R7':lambda: RED,'B7':lambda: BLUE,'R7+B7':lambda: RED+BLUE}
extras={'R7':'S','B7':'T','R7+B7':'ST'}
def run(red,blue,report=True):
    hits_exact=0;hits_cont=0;det=[]
    for sn,sc in S.items():
        for an,al in ALPH.items():
            for rev in (False,True):
                a=al[::-1] if rev else al
                for setn,pts in (('R7',red),('B7',blue),('R7+B7',red+blue)):
                    L=letters(sc,a,pts)
                    for withx in (False,True):
                        M=L+(list(extras[setn]) if withx else [])
                        e=exact(M)
                        if e: hits_exact+=1; det.append(('EXACT',sn,an,rev,setn,withx,''.join(sorted(M)),e[:3]))
                        cnt=contained(M,len(M)-1) if len(M)>=7 else []
                        if cnt: hits_cont+=1
    return hits_exact,hits_cont,det
he,hc,det=run(RED,BLUE)
print('RÉEL : hits exacts',he,'; presque-exacts (nom de longueur >= n-1 contenu)',hc)
for d in det[:20]: print(d)
random.seed(1)
nulls=[]
for t in range(20):
    pts=random.sample(PTS,14); r=pts[:7]; b=pts[7:]
    h=run(r,b); nulls.append((h[0],h[1]))
print('NUL (20 placements aléatoires) exacts, presque:',nulls)
