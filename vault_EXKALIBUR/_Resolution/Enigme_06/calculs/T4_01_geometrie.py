"""T4_01 : pour chaque candidat X (lieu très Sainte), D et alignements avec Bretagne (Dol/Rennes/Paimpont/Lorient).
Orthodromie haversine R=6371.0088 (solveurB_geo). Coordonnées: Wikipedia (cache solveurB_coords_cache.json)."""
import sys; sys.path.insert(0,'.')
from solveurB_geo import *
T=(51.50805556,-0.07611111); B=(50.915,0.4858); Hs=(50.855,0.58333333)
C={ # nom: coords (wikipedia en/fr)
 "Sainte-Chapelle":(48.85527778,2.345),"Notre-Dame Paris":(48.85305556,2.35),"Ste-Chap. Vincennes":(48.8423,2.4364),
 "Saint-Denis":(48.93555556,2.35972222),"Chartres":(48.4478,1.4878),"Abb. aux Hommes Caen":(49.18166667,-0.37277778),
 "Abb. aux Dames Caen":(49.18638889,-0.35277778),"Bayeux cath.":(49.27555556,-0.70333333),"Mont-St-Michel":(48.636,-1.511),
 "Canterbury":(51.2797,1.0831),"Rouen cath.":(49.4402,1.095),"Reims":(49.25388889,4.03416667)}
BR={"Dol":(48.5506,-1.7497),"Rennes":(48.1147,-1.6794),"Paimpont":(48.0189,-2.1697),"Lorient":(47.75,-3.36),"Dinan":(48.4564,-2.0489),"Carnac":(47.5847,-3.0794)}
print("== D par candidat: orthodromie directe T->X ; polyligne T->Battle->X ; T->Hastings->X ; ecart X a l'axe T-Battle")
for n,x in C.items():
    print(f"{n:22s} direct {hav(T,x):7.2f}  via Battle {hav(T,B)+hav(B,x):7.2f}  via Hastings {hav(T,Hs)+hav(Hs,x):7.2f}  ecart/axe T-B {xtrack(T,B,x):+7.2f} km")
print("\n== garde = grand cercle X -> Y prolonge : ecart lateral (km) des points bretons a la droite X->Y ; cap X->Y")
for n,x in C.items():
    for y in ("Dol","Rennes","Paimpont"):
        yy=BR[y]; c=cap(x,yy)
        offs={k:xtrack(x,yy,v) for k,v in BR.items() if k!=y}
        print(f"{n:22s}->{y:9s} cap {c:6.1f} d={hav(x,yy):6.1f} | "+" ".join(f"{k}:{v:+.1f}" for k,v in offs.items()))
print("\n== hypothèse 'Orient' = Lorient : droite Paimpont->Lorient, Dol->Lorient, Rennes->Lorient : X les plus proches (ecart lateral km)")
for y in ("Dol","Rennes","Paimpont"):
    print(y,"->Lorient cap",round(cap(BR[y],BR['Lorient']),1))
    for n,x in C.items(): print(f"   {n:22s} ecart de X a la droite {y}->Lorient : {xtrack(BR[y],BR['Lorient'],x):+8.1f} km")
