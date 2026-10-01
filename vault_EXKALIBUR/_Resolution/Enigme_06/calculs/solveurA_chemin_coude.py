"""Chemin Tour -> Battle -> lieu (coude libre) : longueur totale, pour lieux 'saints' insulaires ; compare a la chaine des C de Guilhem (345.2 km) et a 341.6."""
import sys; sys.stdout.reconfigure(encoding='utf-8')
from solveurA_geo_rayon import hav,T,B
import io
L={'Sainte-Chapelle':(48.855375,2.3449609),'Mont-Saint-Michel':(48.6361,-1.5115),'Lindisfarne':(55.669,-1.800),'Iona':(56.3318,-6.3915),
'Ile Saint-Honorat':(43.5117,7.0467),'Skellig Michael':(51.7715,-10.5406),'Saint Michael s Mount (Cornouailles)':(50.1160,-5.4785),'Glastonbury Tor':(51.1441,-2.6987),
'Ile de Sein':(48.0378,-4.8519),'Bardsey':(52.7627,-4.7930),'Holy Island Anglesey':(53.2993,-4.6383),'Ile-Tudy/Belle-Ile':(47.3376,-3.1620),'Reichenau':(47.6987,9.0625)}
for n,p in L.items(): print(f'{n:40s} T->B->lieu = {hav(T,B)+hav(B,p):7.1f} km ; direct T->lieu {hav(T,p):7.1f}')
