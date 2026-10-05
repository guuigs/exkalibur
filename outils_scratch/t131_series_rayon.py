import json,math,numpy as np,pickle
from shapely.geometry import shape,LineString,Point
from shapely.ops import unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51;tlo,tla=Ti.transform(TX,TY)
def load(fn,filt=None):
    L=[]
    for f in json.load(open(fn))['features']:
        if filt and not filt(f['properties']): continue
        g=shape(f['geometry']);L+=list(getattr(g,'geoms',[g]))
    return unary_union(L)
ROADS=load('large/troncon_de_route.json')
HYD=load('large/troncon_hydrographique.json')
try:
    ROADS_NAT=json.load(open('large/troncon_de_route.json'))['features'][0]['properties']
    print(ROADS_NAT)
except Exception as e: print(e)
def cross(geom,az,maxd=3500,merge=15):
    line=LineString([T.transform(*G.fwd(tlo,tla,az,d)[:2]) for d in range(0,maxd,25)])
    it=geom.intersection(line)
    pts=[]
    for g in getattr(it,'geoms',[it]):
        if g.is_empty: continue
        for c in (g.coords if g.geom_type in('Point','LineString') else []):
            pts.append(line.project(Point(c)))
    pts=sorted(pts);out=[]
    for p in pts:
        if not out or p-out[-1]>merge: out.append(p)
    return out
res={}
for nm,geom in (('routes',ROADS),('hydro',HYD)):
    ok=[]
    for az in np.arange(0,360,0.25):
        c=cross(geom,az)
        if len(c)>=11:
            d=c[10]-c[2]
            if abs(d-1850)<=18.5: ok.append((az,round(d),len(c),round(c[2]),round(c[10])))
    res[nm]=ok;print(nm,'caps (pas 0,25°) avec 3e→11e à 10 stades ±1 % :',len(ok))
    # regroupe
    prev=None
    for r in ok:
        if prev is None or r[0]-prev>0.6: print('   ',r)
        prev=r[0]
pickle.dump(res,open('run/series_rayon.pkl','wb'))

print('\n=== détail des fenêtres (routes) : 3e et 11e croisements et croisement ≥3 voies le plus proche ===')
rows=pickle.load(open('run/rows_final2.pkl','rb'))
from scipy.spatial import cKDTree
kJ=cKDTree(np.array([(r['x'],r['y']) for r in rows]))
src=open('/home/user/exkalibur/outils_scratch/t108_dates_hugues.py').read().split("fetes={")[0]
for az in (38.5,56.5,78.75,80.25,126.5,187.25,190.0,236.5,237.75):
    c=cross(ROADS,az)
    for k in (2,10):
        d=c[k];lo,la=G.fwd(tlo,tla,az,d)[:2];x,y=T.transform(lo,la);dd,i=kJ.query([x,y]);r=rows[i]
        print('az %.2f crossing n°%d à %.0f m (%.5f,%.5f) ; jonction ≥3 voies la + proche %.0f m : maison %d eauS %d open %.2f vu %d pub2 %s'%(az,k+1,d,la,lo,dd,r['hb'],r['eauS'],r['op'],max(r['vs'],r['vm']),r['pub2']))
