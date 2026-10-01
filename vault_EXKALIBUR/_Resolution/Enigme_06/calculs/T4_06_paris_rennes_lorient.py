"""T4_06 : hypothèse « déroute » = fuite de Conan Dol -> Rennes -> Dinan (tapisserie: 'Et venerunt ad Dol et Conan fuga vertit. Rednes. Dinant').
Garde = droite X->Rennes (ou X->Dol) prolongée. Ecarts de Paimpont (Brocéliande) et Lorient (L'Orient) ; test du hasard sur X quelconque dans Paris intra-muros et dans l'IdF/Normandie."""
import sys,random; sys.path.insert(0,'.')
from solveurB_geo import *
Ren=(48.1147,-1.6794); Dol=(48.5506,-1.7497); Pai=(48.0189,-2.1697); Lor=(47.75,-3.36); Din=(48.4564,-2.0489)
SC=(48.85527778,2.345)
print("SC->Rennes: Paimpont %+.2f Lorient %+.2f | SC->Dol: Dinan %+.2f Lorient %+.2f | SC->Dinan: Lorient %+.2f Paimpont %+.2f"%(xtrack(SC,Ren,Pai),xtrack(SC,Ren,Lor),xtrack(SC,Dol,Din),xtrack(SC,Dol,Lor),xtrack(SC,Din,Lor),xtrack(SC,Din,Pai)))
print("Rennes->Paimpont cap",round(cap(Ren,Pai),1)," Rennes->Lorient cap",round(cap(Ren,Lor),1)," Dol->Rennes cap",round(cap(Dol,Ren),1)," Rennes->Dinan cap",round(cap(Ren,Din),1))
# Paris intra-muros ~ boite 48.815-48.902, 2.224-2.470 (approx, ellipse ignorée)
random.seed(4); N=100000
def frac(box,w,Y,Z):
    k=0
    for _ in range(N):
        x=(random.uniform(box[0],box[1]),random.uniform(box[2],box[3]))
        if abs(xtrack(x,Y,Z))<=w: k+=1
    return 100*k/N
paris=(48.815,48.902,2.224,2.470); big=(48.6,50.1,-1.6,3.0)
for w in (0.7,1.15,2.3):
    print(f"w={w} km : P(Lorient a <=w de X->Rennes) X~Paris {frac(paris,w,Ren,Lor):.1f} % ; X~grande boite {frac(big,w,Ren,Lor):.1f} %")
# meme alignement pour d'autres 'villes de la deroute' : Lorient a <=0.7 km de X->Y (Y aleatoire pres de Rennes rayon 40 km) pour X=SC
k=0
for _ in range(N):
    y=(random.uniform(47.9,48.4),random.uniform(-2.4,-1.3))
    if abs(xtrack(SC,y,Lor))<=0.7: k+=1
print("SC fixe, Y aleatoire (Bretagne est 47.9-48.4N,-2.4..-1.3) : P(|ecart Lorient|<=0.7)= %.1f %%"%(100*k/N))
# D : marges
T=(51.50805556,-0.07611111)
pts={"Battle Abbey":(50.915,0.4858),"Battle ville":(50.92,0.48),"Hastings":(50.855,0.5833),"Senlac (Caldbec Hill)":(50.9166,0.4917),"Telham Hill":(50.9,0.5)}
for n,p in pts.items(): print(f"{n:24s} T->champ {hav(T,p):6.2f} champ->SC {hav(p,SC):7.2f} D={hav(T,p)+hav(p,SC):.2f}  droit={hav(T,SC):.2f}")
print("Point à D=341.61 sur la droite prolongée T->Battle:",dest(T,cap(T,pts['Battle Abbey']),341.61), " ecart à SC:",hav(dest(T,cap(T,pts['Battle Abbey']),341.61),SC))
print("1 % de D =",round(3.4161,2),"km ; ecart D Vincennes/ND/StDenis vs SC :",[round(x-341.61,2) for x in (346.19,342.01,334.40)])
