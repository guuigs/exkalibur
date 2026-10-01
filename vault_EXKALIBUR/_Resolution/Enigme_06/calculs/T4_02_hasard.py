"""T4_02 : test du hasard. Pour X aléatoire (Normandie/IdF/Bretagne nord), proba que Lorient soit à <=w km de la droite X->Dol, X->Rennes.
Comparer aux valeurs observées : Dames->Dol->Lorient -2.3 km ; Hommes -1.5 ; SC->Rennes->Lorient -0.7 ; Dol->Rennes."""
import sys,random; sys.path.insert(0,'.')
from solveurB_geo import *
random.seed(1)
Dol=(48.5506,-1.7497); Ren=(48.1147,-1.6794); Lor=(47.75,-3.36); Pai=(48.0189,-2.1697)
box=[(48.6,50.1,-1.6,3.0)]
N=200000
for name,Y in (("Dol",Dol),("Rennes",Ren)):
    for w in (1,2.3,5):
        k=0
        for _ in range(N):
            la=random.uniform(48.6,50.1); lo=random.uniform(-1.6,3.0)
            if hav((la,lo),Y)<60: continue
            if abs(xtrack((la,lo),Y,Lor))<=w: k+=1
        print(f"X uniforme (lat48.6-50.1, lon-1.6..3.0) ; droite X->{name} ; |ecart Lorient|<={w} km : {100*k/N:.2f} %")
# largeur angulaire: Lorient a distance d de X ; P(cap au hasard sur 360 deg) = 2w/(2 pi d)
import math
for d in (150,350): print("d",d,"P(|ecart|<=2.3 km | cap uniforme 360°)",round(100*2*2.3/(2*math.pi*d),3),"%  | cap dans secteur 90° :",round(100*2*2.3/(math.pi/2*d),3),"%")
# ecart de Paimpont / Rennes aux droites Dames->Dol->..
Dames=(49.18638889,-0.35277778)
print("Dames->Dol : ecart Paimpont",round(xtrack(Dames,Dol,Pai),1),"Rennes",round(xtrack(Dames,Dol,Ren),1),"Lorient",round(xtrack(Dames,Dol,Lor),1))
print("Dames->Lorient : ecart Dol",round(xtrack(Dames,Lor,Dol),2),"Paimpont",round(xtrack(Dames,Lor,Pai),1))
# meme test : avec Dol ET Lorient fixes, quelle proba qu'un X (aleatoire) soit sur la droite Dol-Lorient a <=2.3 km : largeur bande / surface
n=0;M=400000
for _ in range(M):
    x=(random.uniform(48.6,50.1),random.uniform(-1.6,3.0))
    if abs(xtrack(Dol,Lor,x))<=2.3 and along(Dol,Lor,x)<0: n+=1
print("P(X uniforme dans la boite est a <=2.3 km de la droite Dol-Lorient cote Caen) =",round(100*n/M,2),"%")
