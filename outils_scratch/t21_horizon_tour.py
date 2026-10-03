import numpy as np,subprocess,json,math,time
from pyproj import Geod
g=Geod(ellps='WGS84')
T=(45.4288723,6.03101275); eye=440.46
az=np.arange(40,80.01,0.5)
ds=np.concatenate([np.arange(300,3000,100),np.arange(3000,15000,250),np.arange(15000,80001,750)])
pts=[]
for a in az:
    lo,la,_=g.fwd(np.full(len(ds),T[1]),np.full(len(ds),T[0]),np.full(len(ds),a),ds)
    pts+= [(a,d,x,y) for d,x,y in zip(ds,lo,la)]
Z=[]
B=120
for i in range(0,len(pts),B):
    ch=pts[i:i+B]
    u="https://data.geopf.fr/altimetrie/1.0/calcul/alti/rest/elevation.json?lon="+"|".join(f"{p[2]:.6f}" for p in ch)+"&lat="+"|".join(f"{p[3]:.6f}" for p in ch)+"&resource=ign_rge_alti_wld&zonly=true"
    for t in range(5):
        r=subprocess.run(['curl','-sS','-m','60',u],capture_output=True,text=True)
        try: z=json.loads(r.stdout)['elevations'];break
        except Exception: time.sleep(2)
    else: z=[np.nan]*len(ch)
    Z+=z
pts=np.array([(p[0],p[1]) for p in pts]);Z=np.array(Z,float);Z[Z<-1000]=np.nan
np.savez('hz.npz',pts=pts,Z=Z)
R=6371000;k=0.13
out={}
for a in az:
    m=pts[:,0]==a; d=pts[m,1]; z=Z[m]
    el=np.degrees(np.arctan((z-eye-d**2/(2*R)*(1-k))/d))
    j=np.nanargmax(el); out[float(a)]=(float(el[j]),float(d[j]),float(z[j]))
json.dump(out,open('hz.json','w'))
for a,v in out.items(): print(a,[round(x,2) for x in v])
