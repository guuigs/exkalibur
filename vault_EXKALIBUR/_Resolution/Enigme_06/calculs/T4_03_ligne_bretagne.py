"""T4_03 : la droite Dames(Caen)->Dol prolongée : lieux/forêts bretons proches (écart latéral, abscisse depuis Caen)."""
import sys; sys.path.insert(0,'.')
from solveurB_geo import *
A=(49.18638889,-0.35277778); Dol=(48.5506,-1.7497); Lor=(47.75,-3.36)
en=["Forêt de Lanouée","Forêt de Camors","Forêt de Quénécan","Forêt de Paimpont","Forêt de Villecartier","Forêt de Rennes","Forêt de Duault","Forêt de Coëtquidan","Forêt de Lorge","Forêt de Fougères","Forêt de Lanvaux","Port-Louis, Morbihan","Lorient","Hennebont","Pontivy","Josselin","Ploërmel","Camors","Auray","La Trinité-sur-Mer","Quiberon","Locminé","Baud, Morbihan","Château de Josselin","Trinité-Porhoët","Caulnes","Broons","Dinan","Combourg","Hédé-Bazouges","Saint-Malo","Landes de Lanvaux","Le Faouët, Morbihan","Guémené-sur-Scorff","Plouay","Forêt d'Hennebont"]
r=wiki_coords(en,"fr")
r2=wiki_coords(["Lorient","Port-Louis, Morbihan","Brocéliande","Paimpont Forest","Forêt de Brocéliande"],"en")
print("cap Caen(Dames)->Dol",round(cap(A,Dol),2)," d(Caen,Dol)",round(hav(A,Dol),1)," d(Caen,Lorient)",round(hav(A,Lor),1))
rows=[]
for d in (r,r2):
  for k,v in d.items():
    if v: rows.append((abs(xtrack(A,Dol,v[:2])),k,v,along(A,Dol,v[:2])))
    else: print("pas de coord:",k)
for e,k,v,a in sorted(rows)[:40]: print(f"{k:28s} ecart {xtrack(A,Dol,v[:2]):+7.2f} km  abscisse {a:6.1f} km ({v[0]:.4f},{v[1]:.4f})")
print("\nPoints de la droite (grand cercle Dames->Dol) :")
for dd in range(120,520,40):
    p=dest(A,cap(A,Dol),dd); print(dd,f"{p[0]:.3f},{p[1]:.3f}")
