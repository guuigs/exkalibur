# T1 tâche 3 : toponymes (BD TOPO + cadastre lieux-dits) évoquant symboles du ciel + mots de l'énigme 12
import json, re, unicodedata, math
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
OUT=r'C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/'
def na(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
TERMS={'loup':r'\bloup|louve|tire.?loup|louvat|loubet','étoile':r'etoile|estelle|astre','arc-en-ciel':r'arc.?en.?ciel','âne':r'\bane\b|\banes\b|asne|anier|anerie|baudet|\bbourr','émeraude':r'emeraude','diamant':r'diamant','ancre':r'ancre|ancr','lune':r'\blune|lunaire|croissant',
'fée':r'\bfee|\bfees\b|fay\b|faye','dame':r'\bdame|damoiselle|demoiselle','fontaine':r'fontaine|fontan|font\b|\bfons?\b','roche':r'roche|rocher|\broc\b|\brocs\b|rochat|rocha','souche':r'souche|\bsouch|\bsouc','clairière':r'clairiere|claire\b|clairet|\bclair','chant':r'\bchant|chante|chanteperdrix|chantemerle','charpentier':r'charpent|\bcharpe','coupe':r'\bcoupe|coupet|la coupe','rempart':r'rempart|remparts|\bmur\b|muraille','avalon':r'avalon','bayard':r'bayard|bayart'}
O=TA; items=[]
for L in ('toponymie','lieu_dit_non_habite','cours_d_eau','detail_orographique','foret_publique','zone_d_activite_ou_d_interet','construction_ponctuelle','detail_hydrographique','construction_lineaire','construction_surfacique','batiment','zone_de_vegetation'):
    try: fs=load(L)
    except Exception as e: continue
    for f in fs:
        p=f['properties']
        names=[p.get(k) for k in ('toponyme','graphie_du_toponyme','nom_1','nom','nom_collaboratif') if p.get(k)]
        if L=='detail_hydrographique' and p.get('nature') in ('Fontaine','Source','Source captée','Lavoir'): names.append(p['nature']+' (nature, sans nom)')
        for n in names:
            c=cen(f['geometry']); items.append(('BDTOPO:'+L,n,c,p.get('nature') or p.get('nature_de_l_objet')))
# cadastre
import itertools
codes=set()
for dlat in (-.06,-.03,0,.03,.06):
    for dlon in (-.08,-.04,0,.04,.08):
        try:
            j=json.loads(get('https://geo.api.gouv.fr/communes?lat=%.4f&lon=%.4f&fields=code,nom'%(O[0]+dlat,O[1]+dlon)))
            for c in j: codes.add((c['code'],c['nom']))
        except Exception as e: print('geo err',e)
print('communes',sorted(codes))
for code,nom in sorted(codes):
    try:
        import subprocess
        j=json.loads(subprocess.run(['curl','-s','--compressed','-m','60','-A','Mozilla/5.0','https://cadastre.data.gouv.fr/bundler/cadastre-etalab/communes/%s/geojson/lieux_dits'%code],capture_output=True).stdout.decode('utf-8'))
    except Exception as e: print('cadastre err',code,e); continue
    for f in j['features']:
        n=f['properties'].get('nom'); 
        if n: items.append(('cadastre:'+nom,n,cen(f['geometry']),'lieu-dit'))
print('items',len(items))
seen=set(); rows=[]
for src,n,c,nat in items:
    d=hav(O,c)
    if d>6.5: continue
    for t,rx in TERMS.items():
        if re.search(rx,na(n)):
            k=(t,na(n),round(c[0],3),round(c[1],3))
            if k in seen: continue
            seen.add(k); rows.append(dict(terme=t,nom=n,src=src,nat=nat,d=d,cap=brg(O,c),lat=c[0],lon=c[1]))
rows.sort(key=lambda r:(r['terme'],r['d']))
json.dump(rows,open(OUT+'T1_toponymes.json','w'),ensure_ascii=False,indent=1)
cur=None
for r in rows:
    if r['terme']!=cur: cur=r['terme']; print('\n##',cur)
    print('  %-34s %-28s %4.2f km cap %3d° (%.5f,%.5f) %s'%(r['nom'][:34],r['src'][:28],r['d'],r['cap'],r['lat'],r['lon'],r['nat']))
