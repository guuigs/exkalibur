# Géoréférence le plan du dépliant « Parcours santé Pontcharra » (PDF Isère Outdoor/Pontcharra) sur la trace GPX officielle
# puis estime d(borne i, borne i+8). Les positions des numéros sont lues À L'ŒIL sur l'image (± ~10 px ≈ ± 30 m) : résultat indicatif.
import numpy as np, re, math, json
import PIL.Image as I
from scipy import ndimage as ndi
im=I.open('t18_sp_map.png').convert('RGB'); a=np.array(im).astype(int)
X0,Y0=540,40   # origine du crop affiché
sub=a[Y0:Y0+770,X0:X0+580]
m=(sub[:,:,0]>150)&(sub[:,:,1]<90)&(sub[:,:,2]>90)&(sub[:,:,0]-sub[:,:,1]>90)
lab,n=ndi.label(ndi.binary_dilation(m,iterations=3))
sizes=ndi.sum(m,lab,range(1,n+1)); k=1+int(np.argmax(sizes))
tr=(lab==k)&m
ys,xs=np.nonzero(tr)
print('(segmentation auto partielle, bbox ignorée)',xs.min(),xs.max(),ys.min(),ys.max())
# bbox visuelle de la trace complète dans le crop (lac/borne 7 en haut, borne 10 en bas)
xs=np.array([62,520]); ys=np.array([62,775])
gpx=open('pontch_gpx.gpx').read()
pts=np.array([(float(p),float(q)) for p,q in re.findall(r'lat="([\d.]+)" lon="([\d.]+)"',gpx)])
la0,la1,lo0,lo1=pts[:,0].min(),pts[:,0].max(),pts[:,1].min(),pts[:,1].max()
lat0=math.radians((la0+la1)/2); my=111132.; mx=111320*math.cos(lat0)
W=(lo1-lo0)*mx; Hh=(la1-la0)*my
pw=xs.max()-xs.min(); ph=ys.max()-ys.min()
sx=W/pw; sy=Hh/ph
print('GPX extent m',round(W),round(Hh),'px',pw,ph,'m/px',round(sx,2),round(sy,2))
s=(sx+sy)/2
def px2ll(px,py):  # px,py en coordonnées du crop ; ancrage centre bbox
    cx=(xs.min()+xs.max())/2; cy=(ys.min()+ys.max())/2
    lon=(lo0+lo1)/2+((px-cx)*s)/mx; lat=(la0+la1)/2-((py-cy)*s)/my; return lat,lon
def hav(a,b,c,d):
    R=6371008.8;p=math.pi/180
    x=math.sin((c-a)*p/2)**2+math.cos(a*p)*math.cos(c*p)*math.sin((d-b)*p/2)**2
    return 2*R*math.asin(math.sqrt(x))
# centres des carrés numérotés (lus sur t18_sp_crop.png)
V={1:(395,713),2:(361,577),3:(307,545),4:(188,437),5:(120,365),6:(94,335),7:(166,84),8:(283,268),9:(425,583),10:(483,775),11:(446,753)}
P={k:px2ll(*v) for k,v in V.items()}
out={}
for k,(la,lo) in P.items(): print(k,round(la,5),round(lo,5))
print('d(1,départ officiel 45.432275,6.020483)=',round(hav(*P[1],45.432275,6.020483)),'m')
TA=(45.429083,6.030808)
import itertools
for i in (1,2,3): print('paire',i,i+8,round(hav(*P[i],*P[i+8])),'m')
print('plus grande distance entre deux bornes:',max((round(hav(*P[i],*P[j])),i,j) for i,j in itertools.combinations(P,2)))
print('d(3,11)=',round(hav(*P[3],*P[11])),'-> dans 1850±18 ?',abs(hav(*P[3],*P[11])-1850)<=18)
for k in (3,11): print('d(borne',k,'-> tour)',round(hav(*P[k],*TA)))
