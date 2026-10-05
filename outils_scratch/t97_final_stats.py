import pickle,math
from t96_lib import *
rows=pickle.load(open('run/entonnoir4_rows.pkl','rb'))
def sure_cells(r,fr=0.0,ress=False): return [k for k in r['rocks'] if k['frac']>=fr and (k['ress'] or not ress) and any(t[6] for t in k['res'])]
stg=[
 ('S0  croisements ≥ 3 voies, 100 m – 2,5 km',lambda r:True),
 ('S1  + maisons ≥ 100 m du croisement (tous sommets)',lambda r:r['hb']>=100),
 ('S2  + eau : BD TOPO ≤ 150 m ou talweg ≥ 1 ha',lambda r:r['wd']<=150 or r['ta']>=1),
 ('S3  + clairière vue de la muraille (≥ 50 m² ouverts vus ; œil au sol OU sur le mur)',lambda r:r['vs']>=50 or r['vm']>=50),
 ('S4  + fin de parcours possible (eau reliée ≤ 450 m ; coffre public probable ou sûr, ≥ 100 m maisons, ≤ 30 m d\'un chemin)',lambda r:len(ok_cells(r))>=1),
 ('S5  + distance ≤ 2,0 km',lambda r:r['d']<=2000),
 ('S6  + chemin le long de l\'eau (≥ 50 % du parcours à ≤ 30 m d\'un chemin)',lambda r:len(ok_cells(r,0.5))>=1),
 ('S7  + coffre en public SÛR (parcelle/forêt publique/voirie cartographiée)',lambda r:len(sure_cells(r,0.5))>=1),
]
cur=rows
for nm,f in stg:
  cur=[r for r in cur if f(r)];print(f'{len(cur):5d}  {nm}')
S3=[r for r in rows if r['hb']>=100 and (r['wd']<=150 or r['ta']>=1) and (r['vs']>=50 or r['vm']>=50)]
print('\n=== S3 : %d croisements (clairière vue, eau, maisons ≥ 100 m) — fin de parcours ==='%len(S3))
for r in sorted(S3,key=lambda r:r['d']):
  c=ok_cells(r);c5=ok_cells(r,0.5);cs=sure_cells(r,0.5);cr=ok_cells(r,0.5,True)
  print(f"{r['la']:.6f},{r['lo']:.6f} | {r['d']:.0f} m cap {r['az']:.0f}° | pts {len(c)} (chemin≥50 %: {len(c5)}, sûr: {len(cs)}, ressaut: {len(cr)}) | {lg(r)}")
pickle.dump(rows,open('run/rows_final.pkl','wb'))
