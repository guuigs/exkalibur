"""Piste 2/4 : anagrammes exactes de phrases/mots-clés du texte -> 1 ou 2 toponymes en C (11 800 lieux). + test du hasard."""
from solveurA_lists import *
import random, itertools
NCn=[(k,n,collections.Counter(k)) for k,(n,cc,p) in places.items() if len(k)>=4]
def sub(ph):
    c=collections.Counter(norm(ph)); return [(k,n,ck) for k,n,ck in NCn if not (ck-c)]
def exact1(ph):
    key=''.join(sorted(norm(ph))); return [places[k][0] for k in {norm(n) for n in [x[1] for x in []]}] or [v[0] for v in byk.get(key,[])]
def exact2(ph, cand):
    tot=collections.Counter(norm(ph)); res=[]
    for i,(k1,n1,c1) in enumerate(cand):
        rest=tot-c1
        if sum(c1.values())+sum(rest.values())!=sum(tot.values()): continue
        key=''.join(sorted(rest.elements()))
        for v in byk.get(key,[]):
            if norm(v[0])>=k1: res.append((n1,v[0]))
    return res
PH=['Libera nos a malo','Pater noster','Notre Pere qui es aux cieux','Preux contre dieux','Observe la partie',
    'Commencera le Pere et finiront les cieux','Harold rex interfectus est','Rex interfectus est','MLXVI','Sepulcre','coupe de Vie',
    'Tour de Londres','Battle Abbey','Sainte Chapelle','Nine worthies','Neuf preux','pauvres chevaliers','jeu du moulin','marelle',
    'Urbain deux','Concile de Clermont','Pere Cieux S T dix','Saint Sepulcre','Godefroy de Bouillon','Jerusalem','Hastings','Guillaume le Conquerant','Senlac',
    'Harold','Annonciation','Gabriel Marie']
out=[]
for ph in PH:
    cand=sub(ph)
    e1=[v[0] for v in byk.get(''.join(sorted(norm(ph))),[])]
    e2=exact2(ph,cand) if len(norm(ph))<=40 else []
    e2=[x for x in e2 if len(norm(x[0]))>=4 and len(norm(x[1]))>=4]
    print(f'{ph!r} ({len(norm(ph))} lettres): C-lieux contenus={len(cand)} ; anagramme exacte 1 lieu={e1[:5]} ; 2 lieux={e2[:8]} (n={len(e2)})')
# NUL : phrases aléatoires de même longueur tirées de lettres françaises fréquentes
random.seed(3)
alph=list('EEEEEEEEEEEEEEEAAAAAAAAIIIIIIIINNNNNNNSSSSSSSRRRRRRTTTTTTOOOOOOLLLLLUUUUUDDDCCCMMMPPVVFHGBQXY')
lens=[len(norm(p)) for p in PH if 7<=len(norm(p))<=30]
n1=n2=0;N=0
for t in range(300):
    L=random.choice(lens); ph=''.join(random.choice(alph) for _ in range(L)); N+=1
    if byk.get(''.join(sorted(ph))): n1+=1
    cand=sub(ph)
    if exact2(ph,cand): n2+=1
print(f'NUL {N} phrases aléatoires (longueurs 7-30) : anagramme exacte 1 lieu={n1}, 2 lieux={n2}')
