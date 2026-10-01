"""T4_04 : lecture 'Orient' = direction Est. Pour X (lieu très Sainte) et P (point de déroute), droite X->P prolongée (grand cercle) :
cap, et villes remarquables (Avallon, Reims...) dans 5 km de la droite du côté P. Déroutes: Varaville 1057, Mortemer 1054, Val-ès-Dunes, Hastings/Battle (Harold), Dol (Conan)."""
import sys; sys.path.insert(0,'.')
from solveurB_geo import *
X={"Ste-Chapelle":(48.85527778,2.345),"Notre-Dame":(48.85305556,2.35),"Vincennes":(48.8423,2.4364),"St-Denis":(48.93555556,2.35972222),
   "Dames Caen":(49.18638889,-0.35277778),"Hommes Caen":(49.18166667,-0.37277778),"Bayeux":(49.27555556,-0.70333333),"MSM":(48.636,-1.511),"Chartres":(48.4478,1.4878)}
P={"Varaville":(49.2542,-0.1569),"Mortemer":(49.7517,1.5511),"Battle":(50.915,0.4858),"Hastings":(50.855,0.5833),"Dol":(48.5506,-1.7497),"Rennes":(48.1147,-1.6794),"Dinan":(48.4564,-2.0489)}
cities=["Avallon","Vézelay","Reims","Troyes","Metz","Nancy, France","Strasbourg","Dijon","Langres","Auxerre","Alise-Sainte-Reine","Bibracte","Orléans","Sens","Chalon-sur-Saône","Besançon","Verdun","Épernay","Châlons-en-Champagne","Laon","Soissons","Cluny","Autun","Nevers","Bourges","Montbéliard","Lorient","Nantes","Saint-Malo","Brest, France","Quimper","Vannes","Redon","Ys"]
c=wiki_coords(cities,"fr")
c={k:v[:2] for k,v in c.items() if v}
print("villes sans coord:",[k for k in cities if k not in c])
for xn,x in X.items():
  for pn,p in P.items():
    cp=cap(x,p)
    if not(30<cp<150 or 200<cp<280): pass
    hits=[]
    for k,v in c.items():
        a=along(x,p,v); e=xtrack(x,p,v)
        if a>0 and abs(e)<=4: hits.append(f"{k}({e:+.1f}km @{a:.0f})")
    print(f"{xn:13s}->{pn:9s} cap {cp:6.1f} d={hav(x,p):6.1f} : "+", ".join(hits))
