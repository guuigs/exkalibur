# T1 tâche 2 et 4 : jonctions de chemins (troncon_de_route Sentier/Chemin/Route empierrée) cumulant trouée, ruisseau <150 m, domaine public, visibilité depuis l'origine (rempart), versant est
import sys, json, math, time, os
import numpy as np
from shapely.geometry import shape, Point, LineString
from shapely.ops import unary_union, nearest_points
from shapely.prepared import prep
from shapely.strtree import STRtree
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
OUT=r'C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/'
CACHE=r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/alti_cache.json'
alt_cache=json.load(open(CACHE)) if os.path.exists(CACHE) else {}
def key(lat,lon): return '%.5f,%.5f'%(lat,lon)
def alti(points):
    need=[p for p in points if key(*p) not in alt_cache]
    for i in range(0,len(need),150):
        b=need[i:i+150]
        u='https://data.geopf.fr/altimetrie/1.0/calcul/alti/rest/elevation.json?lon=%s&lat=%s&resource=ign_rge_alti_wld&zonly=true'%('|'.join('%.5f'%p[1] for p in b),'|'.join('%.5f'%p[0] for p in b))
        for t in range(3):
            try:
                j=json.loads(get(u,60)); z=j['elevations']; break
            except Exception as e:
                print('alti retry',e); time.sleep(2); z=None
        if z is None: continue
        for p,v in zip(b,z): alt_cache[key(*p)]=v if isinstance(v,(int,float)) else v.get('z')
    json.dump(alt_cache,open(CACHE,'w'))
    return [alt_cache.get(key(*p)) for p in points]
def run(name,O,maxd,hobs):
    lat0=O[0]; kx=111320*math.cos(math.radians(lat0)); ky=110540
    P=lambda lon,lat:((lon-O[1])*kx,(lat-O[0])*ky)
    inv=lambda x,y:(O[0]+y/ky,O[1]+x/kx)
    def sh(g):
        from shapely.ops import transform
        return transform(lambda x,y,z=None:P(x,y),shape(g))
    roads=[f for f in load('troncon_de_route') if f['properties']['nature'] in('Sentier','Chemin','Route empierrée')]
    allroads=load('troncon_de_route')
    # noeuds
    from collections import defaultdict
    deg=defaultdict(list); degall=defaultdict(int)
    kk=lambda c:(round(c[0],5),round(c[1],5))
    for f in roads:
        g=f['geometry']; lines=[g['coordinates']] if g['type']=='LineString' else g['coordinates']
        for L in lines:
            deg[kk(L[0])].append(f); deg[kk(L[-1])].append(f)
    for f in allroads:
        g=f['geometry']; lines=[g['coordinates']] if g['type']=='LineString' else g['coordinates']
        for L in lines: degall[kk(L[0])]+=1; degall[kk(L[-1])]+=1
    nodes=[(k,v) for k,v in deg.items() if len(v)>=3]
    # végétation
    veg=[sh(f['geometry']) for f in load('zone_de_vegetation') if f['properties']['nature'] in('Forêt fermée de feuillus','Forêt fermée mixte','Forêt fermée de conifères','Bois','Forêt ouverte','Lande ligneuse')]
    forest=unary_union([g.buffer(0) for g in veg]); pforest=prep(forest)
    fp=unary_union([sh(f['geometry']).buffer(0) for f in load('foret_publique')]); pfp=prep(fp)
    hyd=[f for f in load('troncon_hydrographique') if f['properties']['nature']=='Ecoulement naturel']
    hg=[sh(f['geometry']) for f in hyd]; tree=STRtree(hg)
    cdeau={f['properties']['cleabs']:f['properties'].get('toponyme') for f in load('cours_d_eau')}
    rows=[]
    for k,fs in nodes:
        lat,lon=k[1],k[0]; x,y=P(lon,lat); d=math.hypot(x,y)
        if d>maxd*1000: continue
        pt=Point(x,y)
        infor=pforest.contains(pt)
        ring=pt.buffer(90).difference(pt.buffer(25)); frac=ring.intersection(forest).area/ring.area
        near=pt.buffer(20).intersection(forest).area/pt.buffer(20).area
        trouee=(not infor) and near<0.15 and frac>=0.35
        ii=tree.nearest(pt); dh=hg[ii].distance(pt)
        pub=pfp.contains(pt)
        prive=any((f['properties'].get('prive') in(True,'true','Oui')) for f in fs)
        rows.append(dict(lat=lat,lon=lon,x=x,y=y,d=d,cap=brg(O,(lat,lon)),deg=len(fs),degall=degall[k],nat=sorted(set(f['properties']['nature'] for f in fs)),infor=infor,frac=frac,near=near,trouee=trouee,dh=dh,ih=int(ii),pub=pub,prive=prive))
    print(name,'jonctions >=3 branches dans %.1f km: %d'%(maxd,len(rows)))
    # filtres
    for r in rows: r['eau']=r['dh']<=150
    base=[r for r in rows if r['trouee'] and r['eau']]
    print('  trouée:',sum(r['trouee'] for r in rows),' eau<=150m:',sum(r['eau'] for r in rows),' trouée+eau:',len(base))
    # altitudes: origine + vue + versant, seulement pour les rows trouée ou eau (pour le test du hasard sur les 2 filtres suivants on calcule pour tous ceux de 'rows' si <= 300)
    sel=[r for r in rows if r['trouee'] or r['eau']]
    O_alt=alti([O])[0]
    print('  altitude origine',O_alt)
    for r in sel:
        # versant : 4 points à 40 m
        pts=[inv(r['x'],r['y']),inv(r['x']+40,r['y']),inv(r['x']-40,r['y']),inv(r['x'],r['y']+40),inv(r['x'],r['y']-40)]
        r['_pts']=pts
        n=max(3,int(r['d']/60)); r['_prof']=[inv(r['x']*t/n,r['y']*t/n) for t in range(1,n)]
    allp=[]
    for r in sel: allp+=r['_pts']+r['_prof']
    alti(allp)
    for r in sel:
        z=alti(r['_pts']); zc,ze,zw,zn,zs=z
        if None in z: r['aspect']=None; continue
        gx=(zw-ze)/80; gy=(zs-zn)/80   # pente vers l'est si zw>ze ; vers le nord si zs>zn
        slope=math.hypot(gx,gy)
        aspect=(math.degrees(math.atan2(gx,gy))+360)%360   # direction de la descente (0=N, 90=E)
        r['z']=zc; r['slope']=slope*100; r['aspect']=aspect
        r['est']=slope>=0.04 and 45<=aspect<=135
        # visibilité
        prof=alti(r['_prof']); n=len(prof)+1
        za=O_alt+hobs; zb=zc+1.7; vis=True; clear=1e9
        for i,zp in enumerate(prof,1):
            if zp is None: continue
            t=i/n; zl=za+(zb-za)*t; c=zl-zp; clear=min(clear,c)
            if c<0: vis=False
        r['vis']=vis; r['clear']=clear if clear<1e8 else None
    for r in sel:
        r.setdefault('est',False); r.setdefault('vis',False)
    for r in rows:
        r.setdefault('est',False); r.setdefault('vis',False)
    # hasard : compteurs
    flt=['trouee','eau','pub','vis','est']
    print('  compte par filtre (sur',len(rows),'jonctions): trouée %d, eau %d, public %d, vue %d, est %d'%tuple(sum(bool(r[f]) for r in rows) for f in flt))
    # NB : vis/est ne sont calculés que pour trouée ou eau
    from itertools import combinations
    print('  combinaisons:')
    for n in range(2,6):
        for c in combinations(flt,n):
            print('    ',c,sum(all(r[f] for f in c) for r in rows))
    for r in rows: r['score']=sum(bool(r[f]) for f in flt)+ (0.5 if r['dh']<=60 else 0) + (0.5 if r['near']<0.02 else 0) - r['d']/10000
    rows.sort(key=lambda r:-r['score'])
    # ruisseau : nom + sens d'écoulement au point le plus proche
    top=rows[:10]
    for r in top:
        f=hyd[r['ih']]; g=hg[r['ih']]; pt=Point(r['x'],r['y'])
        s=g.project(pt); s2=min(g.length,s+15); s1=max(0,s-15)
        a=g.interpolate(s1); b=g.interpolate(s2)
        sens=f['properties'].get('sens_de_l_ecoulement')
        bx,by=b.x-a.x,b.y-a.y
        cap=(math.degrees(math.atan2(bx,by))+360)%360
        if sens and 'inverse' in str(sens).lower(): cap=(cap+180)%360
        r['flow_cap']=cap; r['sens']=sens
        r['ruis']=f['properties'].get('code_hydrographique'); lk=f['properties'].get('liens_vers_cours_d_eau')
        r['ruis_nom']=cdeau.get(lk if isinstance(lk,str) else (lk[0] if lk else None)) if lk else None
        # à gauche de qui ? on donne le côté du ruisseau par rapport au cap d'arrivée depuis l'origine (visiteur venant du rempart)
        cl=nearest_points(pt,g)[1]; rel=(math.degrees(math.atan2(cl.x-r['x'],cl.y-r['y']))+360)%360
        r['ruis_dir_depuis_jonction']=rel
    out=[{k:v for k,v in r.items() if not k.startswith('_')} for r in rows]
    json.dump(out,open(OUT+'T1_%s_jonctions.json'%name,'w'),ensure_ascii=False,indent=1)
    print('  TOP 10 :')
    for i,r in enumerate(top,1):
        print('  %2d sc=%.2f %.5f,%.5f d=%.0fm cap=%.0f %s deg%d trouee=%s eau=%dm pub=%s vue=%s(degag %s m) est=%s(asp %s, pente %s%%) ruisseau=%s/%s flux vers %.0f (ruisseau a %.0f de la jonction) alt=%s'%(i,r['score'],r['lat'],r['lon'],r['d'],r['cap'],r['nat'],r['deg'],r['trouee'],r['dh'],r['pub'],r['vis'],None if r.get('clear') is None else round(r['clear']),r['est'],None if r.get('aspect') is None else round(r['aspect']),None if r.get('slope') is None else round(r['slope']),r['ruis'],r['ruis_nom'],r['flow_cap'],r['ruis_dir_depuis_jonction'],r.get('z')))
    return rows
if __name__=='__main__':
    run('tour',TA,2.5,8)
    run('fort',(45.4358,5.98723),1.5,8)
