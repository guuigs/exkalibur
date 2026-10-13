"""Profil de visibilité depuis le sommet de la tour d'Avalon (sol + hauteur d'oeil) vers des cibles, via l'API altimétrie IGN (RGE ALTI)."""
import json, subprocess, sys, math, time
sys.path.insert(0,'.')
from geo import inv
TA=(45.429083,6.030808)
def profile(a,b,n=200):
    u=("https://data.geopf.fr/altimetrie/1.0/calcul/alti/rest/elevationLine.json?lon=%f|%f&lat=%f|%f&resource=ign_rge_alti_wld&sampling=%d&profil_mode=simple"%(a[1],b[1],a[0],b[0],n))
    for i in range(6):
        r=subprocess.run(['curl','-sS','-m','60',u],capture_output=True,text=True)
        try:
            j=json.loads(r.stdout); return [(p['lat'],p['lon'],p['z']) for p in j['elevations']]
        except Exception: time.sleep(3*(i+1))
    raise RuntimeError(r.stdout[:200]+r.stderr[:200])
def visible(target, eye=30.0, tgt=1.7):
    pr=profile(TA,target)
    z0=pr[0][2]+eye; D=inv(TA,target)[0]*1000; zt=pr[-1][2]+tgt
    worst=-1e9; block=None
    for la,lo,z in pr[1:-1]:
        d=inv(TA,(la,lo))[0]*1000
        if d<=0: continue
        # earth curvature+refraction negligible at 2 km (~0.27 m)
        h_line=z0+(zt-z0)*d/D
        m=z-h_line
        if m>worst: worst=m; block=(round(d),round(z,1))
    return pr[0][2], pr[-1][2], worst, block
if __name__=='__main__':
    targets=json.load(open(sys.argv[1])) if len(sys.argv)>1 else []
    for name,lat,lon in targets:
        try:
            z0,zt,w,b=visible((lat,lon))
            print('%-28s sol tour %.1f m  cible %.1f m  marge %.1f m (>0 = masqué) au point %s -> %s'%(name,z0,zt,w,b,'VISIBLE' if w<0 else 'masqué'))
        except Exception as e: print(name,'ERR',e)
