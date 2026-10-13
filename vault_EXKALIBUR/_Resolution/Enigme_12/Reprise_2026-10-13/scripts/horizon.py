"""Horizon réel vu du sommet de la tour d'Avalon (sol + 30 m) entre 50° et 130°, puis azimut du premier rayon de soleil selon la date."""
import json, math, subprocess, time, sys
sys.path.insert(0,'.')
from geo import direct
TA=(45.429083,6.030808); EYE=30.0
def prof(a,b,n):
    u=("https://data.geopf.fr/altimetrie/1.0/calcul/alti/rest/elevationLine.json?lon=%f|%f&lat=%f|%f&resource=ign_rge_alti_wld&sampling=%d&profil_mode=simple"%(a[1],b[1],a[0],b[0],n))
    for i in range(6):
        r=subprocess.run(['curl','-sS','-m','90',u],capture_output=True,text=True)
        try: return [p['z'] for p in json.loads(r.stdout)['elevations']]
        except Exception: time.sleep(3*(i+1))
    raise RuntimeError('alti')
H={}
z0=None
for az in range(50,131,2):
    end=direct(TA,az,25.0); zs=prof(TA,end,250)
    if z0 is None: z0=zs[0]+EYE
    best=-90
    for i,z in enumerate(zs[1:],1):
        d=25000*i/(len(zs)-1)
        ang=math.degrees(math.atan2(z-z0-(d*d)/(2*6371000)*0.87, d))
        best=max(best,ang)
    H[az]=best; print(az, round(best,2), flush=True)
json.dump(H,open('horizon_tour.json','w'))
