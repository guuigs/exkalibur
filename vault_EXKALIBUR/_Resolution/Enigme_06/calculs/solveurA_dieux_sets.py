"""Piste 2/9 : sous-ensembles de noms de dieux (planetes / jours / Olympiens / Titans / Ciel) +/- S,T -> anagramme exacte d'un lieu en C.
Avec test du hasard : memes noms aux lettres melangees."""
import sys, itertools, random, collections
sys.stdout.reconfigure(encoding='utf-8')
from solveurA_lists import *
SETS={
 'planetes_lat':['Sol','Luna','Mars','Mercurius','Iuppiter','Venus','Saturnus'],
 'planetes_fr':['Soleil','Lune','Mars','Mercure','Jupiter','Venus','Saturne'],
 'planetes_gr':['Helios','Selene','Ares','Hermes','Zeus','Aphrodite','Cronos'],
 'jours_fr':['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche'],
 'olympiens_gr':['Zeus','Hera','Poseidon','Demeter','Athena','Apollon','Artemis','Ares','Aphrodite','Hephaistos','Hermes','Hestia','Dionysos'],
 'olympiens_lat':['Jupiter','Junon','Neptune','Ceres','Minerve','Apollon','Diane','Mars','Venus','Vulcain','Mercure','Vesta','Bacchus'],
 'titans':['Cronos','Rhea','Ouranos','Gaia','Oceanos','Tethys','Hyperion','Theia','Coeos','Phoebe','Crios','Japet','Themis','Mnemosyne','Atlas'],
 'ciel_pere':['Caelus','Coelus','Uranus','Ouranos','Saturne','Saturnus','Cronos','Kronos','Jupiter','Iuppiter','Diespiter','Dyaus','Zeus','Pater','Pere','Ciel','Cieux','Odin','Tyr'],
}
def norm2(w): return norm(w)
def run(names,src=None):
    L=[norm(w) for w in names]; out=[]
    for r in (1,2,3):
        for comb in itertools.combinations(range(len(L)),r):
            base=''.join(L[i] for i in comb)
            for ex in ('','S','T','ST'):
                k=''.join(sorted(base+ex))
                if len(k)<4: continue
                for v in byk.get(k,[]):
                    if norm(v[0]) not in [L[i] for i in comb]:
                        out.append(([names[i] for i in comb],ex,v[0],v[1]))
    return out
random.seed(9)
for sn,names in SETS.items():
    real=run(names)
    nulls=[]
    for t in range(15):
        sh=[]
        for w in names:
            l=list(norm(w)); random.shuffle(l); sh.append(''.join(l))
        nulls.append(len(run(sh)))
    print(f'{sn}: reel={len(real)}  nul(15)={nulls}')
    for x in real[:12]: print('   ',x)
