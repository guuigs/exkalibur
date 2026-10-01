"""U2 run4 : chaînes de 4 'C-boissons' (lieux en C donnant une boisson) de longueur 341,6 km ±1 % ; contrôle = 4 lieux C aléatoires parmi les communes FR pop>=..."""
from U2_common import *
import zipfile, math, itertools, unicodedata
FR_DR=["Cahors","Cassis","Chablis","Chinon","Cognac","Champagne","Cadillac","Condrieu","Cornas","Chénas","Chiroubles","Chassagne-Montrachet","Châteauneuf-du-Pape","Cheverny","Cérons","Crozes-Hermitage","Collioure","Condom","Cairanne","Chambolle-Musigny","Chambertin","Clos-Vougeot","Vougeot","Cramant","Cumières","Chouilly","Chigny-les-Roses","Corbières","Cluny","Cîteaux","Clairvaux-les-Lacs","Chaource","Cîteaux","Cavaillon","Carcassonne","Calvi","Cerdon","Crépy","Cour-Cheverny","Chusclan","Cabrières","Cuxac-Cabardès","Cabardès","Chablis","Charentay","Chatillon-en-Diois","Clairette","Cazouls-lès-Béziers","Coulommiers","Chavignol","Châteaumeillant","Chatus","Côte-Rôtie","Cotignac","Cucugnan","Cuers","Camarsac","Cubzac-les-Ponts","Chambéry","Crest","Cébazat","Clermont-Ferrand","Clermont","Chartres","Cadouin","Conques","Clairvaux","Charroux","Châteaubriant","Combourg"]
def load_fr():
    d={}
    for c in json.load(open(os.path.join(HERE,"T1data","communes.json"),encoding="utf-8")):
        d.setdefault(norm(c["nom"]),[]).append((c["nom"],c["centre"]["coordinates"][1],c["centre"]["coordinates"][0]))
    return d
FR=load_fr()
extra={"Calvados":(49.1,-0.4)}
def hav(a,b):
    R=6371.0088; p1,p2=math.radians(a[0]),math.radians(b[0]); dl=math.radians(b[1]-a[1]); dp=p2-p1
    x=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(x))
pts={}
for n in FR_DR:
    k=norm(n)
    if k in FR: pts[n]=FR[k][0][1:]
for k,v in extra.items(): pts[k]=v
# Ajouts hors France (coord approximatives 4 déc. connues)
pts.update({"Cork":(51.8985,-8.4756),"Clonmel":(52.355,-7.7033),"Campbeltown":(55.4247,-5.6053),"Cardhu":(57.47,-3.35),"Cádiz":(36.527,-6.288),"Cariñena":(41.3388,-1.2196),"Calatayud":(41.3536,-1.6433),"Carcavelos":(38.6924,-9.3364),"Colares":(38.7972,-9.4503),"Cava(Sant Sadurní)":(41.4287,1.7855),"Canterbury":(51.28,1.08),"Cornwall":(50.27,-5.05),"Chester":(53.19,-2.89)})
print(len(pts),"points boissons-C:",sorted(pts))
names=sorted(pts)
def minpath(S):
    best=1e9
    for perm in itertools.permutations(S[1:]):
        for first in [S[0]]:
            pass
    best=1e9
    for perm in itertools.permutations(S):
        if perm[0]>perm[-1]: continue
        d=sum(hav(pts[perm[i]],pts[perm[i+1]]) for i in range(3)); best=min(best,d)
    return best
D=341.6; lo,hi=D*0.99,D*1.01
res=[]
for S in itertools.combinations(names,4):
    m=minpath(list(S))
    if lo<=m<=hi: res.append((S,round(m,2)))
print("chaînes (plus court chemin) dans ±1 % :",len(res),"sur",math.comb(len(names),4))
for r in res[:60]: print(r)
# contrôle : proportion dans ±1% pour 4 lieux aléatoires tirés des communes FR+pts (même nombre de sous-ensembles)
pool=[v[0][1:] for v in FR.values()]
random.seed(3); cnt=0; N=20000
for _ in range(N):
    S=random.sample(pool,4); b=1e9
    for p in itertools.permutations(range(4)):
        if p[0]>p[-1]: continue
        b=min(b,sum(hav(S[p[i]],S[p[i+1]]) for i in range(3)))
    cnt+= lo<=b<=hi
print("contrôle 4 communes FR aléatoires: %.4f dans ±1%% ; attendu sur %d combi: %.1f"%(cnt/N,math.comb(len(names),4),cnt/N*math.comb(len(names),4)))
