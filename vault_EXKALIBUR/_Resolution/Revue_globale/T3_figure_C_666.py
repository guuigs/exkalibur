# T3 : (a) figure des 6 C (6e = Château Bayard ?) (b) test 666/Tibère (c) E10 nombre -> E11 angle brute (d) parallèle Lincoln
import math,itertools
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
C={'Clairvaux':(48.1522,4.7822),'Cîteaux':(47.1375,5.0988),'Cluny':(46.4341,4.6590),'Clermont':(45.7797,3.0863),'Chartres':(48.4477,1.4876),'ChâteauBayard':CB}
LOMB=(42.8203,1.6206); URQ=(57.3243,-4.4419)
names=list(C)
d=[hav(C[a],C[b]) for a,b in zip(names,names[1:])]
print('== (a) chaîne 6 C :',' -> '.join(names)); print('   segments km',[round(x,1) for x in d],'| 4 premiers =',round(sum(d[:3]),1),'(attendu 340,9)')
# projection plane locale pour intersections
lat0,lon0=46.5,3.0
def xy(p): return ((p[1]-lon0)*math.cos(math.radians(lat0))*111.19,(p[0]-lat0)*111.19)
def inter(a,b,c,dd):
    (x1,y1),(x2,y2),(x3,y3),(x4,y4)=map(xy,(a,b,c,dd)); den=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if abs(den)<1e-9: return None
    t=((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den; u=-((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/den
    return (t,u) if 0<=t<=1 and 0<=u<=1 else None
segs=list(zip(names,names[1:]))
print('   auto-intersections des segments non adjacents :')
for i,j in itertools.combinations(range(len(segs)),2):
    if j==i+1: continue
    r=inter(C[segs[i][0]],C[segs[i][1]],C[segs[j][0]],C[segs[j][1]])
    print('    ',segs[i],'x',segs[j],'->',r if r else 'non')
r=[inter(C[a],C[b],LOMB,URQ) for a,b in segs]; print('   croisement avec la lame Lombrives-Urquhart :',r)
# distance de Cluny à la corde Chartres->Bayard
def xt(p,a,b):
    R=6371.0088; d13=hav(a,p)/R; t13=math.radians(brg(a,p)); t12=math.radians(brg(a,b)); return math.asin(math.sin(d13)*math.sin(t13-t12))*R
print('   distance de Cluny à la droite Chartres->Bayard : %.1f km ; Clermont : %.1f km'%(abs(xt(C['Cluny'],C['Chartres'],C['ChâteauBayard'])),abs(xt(C['Clermont'],C['Chartres'],C['ChâteauBayard']))))
print('   caps: Chartres->Bayard %.1f ; Bayard->Clairvaux %.1f'%(brg(C['Chartres'],CB),brg(CB,C['Clairvaux'])))
# (b) 666
print('\n== (b) 18 pétales × année de mort -> (18y)^2 pieds romains (0.296 m) ; distance et test du hasard')
PR=0.296
for y in (14,30,33,37,41,54,68,79):
    n=18*y; km=n*n*PR/1000; print(f'   y={y:3d} n={n:4d} -> {km:8.2f} km')
print('   nb d\'années 1..100 où 18*y ∈ [660,672] :',[y for y in range(1,101) if 660<=18*y<=672],'; n=666 exact seulement y=37 :',[y for y in range(1,101) if 18*y==666])
print('   pieds romains: 666^2 = %d ; ×0.296 = %.2f km'%(666**2,666**2*PR/1000))
# (c) E10 nombre N dans 1,3,5,? -> angle 64.99 ?
tgt=64.99; hits=[]
import itertools
for N in range(1,121):
    vals={'1':1,'3':3,'5':5,'N':N}
    for a,b in itertools.permutations(vals,2):
        for op,f in (('*',lambda x,y:x*y),('+',lambda x,y:x+y),('/',lambda x,y:x/y),('-',lambda x,y:x-y)):
            for k,kn in ((1,''),(math.pi,'π'),(1/math.pi,'/π')):
                v=f(vals[a],vals[b])*k
                if abs(v-tgt)<=0.03: hits.append((N,a+op+b+kn,round(v,3)))
print('\n== (c) formules 2 termes {1,3,5,N}, N<=120, ±0,03° de 64,99 :',hits[:12],'... total',len(hits),'| combinatoire testée ≈',120*12*4*3)
print('   somme 1+3+5=9 ; produit 15 ; 1·3·5·N=65 -> N=%.3f ; (1+3+5)·N·... N=%.3f'%(65/15,64.99/9))
print('   64.99/π = %.3f ; 64.99/23 = %.3f ; 64.99/193.13 = %.4f ; 606.72/193.13 = %.4f'%(64.99/math.pi,64.99/23,64.99/193.13,606.72/193.13))
# (d) Lincoln : distance Lincoln - Avalon, Payns
print('\n== (d) Lincoln Cathedral 53.2343,-0.5361 ; tour d\'Avalon %.2f km'%hav((53.2343,-0.5361),(45.4288,6.0308)))
