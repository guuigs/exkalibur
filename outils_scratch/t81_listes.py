import pickle
rows=pickle.load(open('run/crible_rows.pkl','rb'))
crit={'proche ≤2 km':lambda r:r['d']<=2000,
 'clairière vue (≥100 m² au sol, œil au sol)':lambda r:r['vs']>=100,
 'maisons ≥100 m du croisement':lambda r:r['hb']>=100,
 'eau ≤100 m (ou talweg ≥2 ha)':lambda r:r['wd']<=100 or r['ta']>=2,
 'coffre public sûr possible (≥200 m², ≥100 m maisons, ≤30 m chemin, ≤300 m)':lambda r:r['cs']>=200,
 'clairière (ouvert ≥30 %, forêt ≥20 %)':lambda r:r['op']>=0.3 and r['fo']>=0.2}
names=list(crit)
def show(r,miss=''):
  return f"{r['la']:.6f},{r['lo']:.6f} | {r['d']:.0f} m cap {r['az']:.0f}° | {r['deg']} voies | maisons {r['hb']:.0f} | vu {r['vs']}/{r['vm']} m² | eau {r['wd']:.0f} m talweg {r['ta']:.1f} ha | ouvert {r['op']:.2f} forêt {r['fo']:.2f} | coffre sûr {r['cs']} m² (douteux {r['cd']}) {miss}"
ok=[r for r in rows if all(f(r) for f in crit.values())]
print('=== PASSENT TOUT :',len(ok))
for r in sorted(ok,key=lambda r:r['d']): print(' ',show(r))
print('\n=== RATENT UN SEUL CRITÈRE ===')
for nm in names:
  L=[r for r in rows if not crit[nm](r) and all(f(r) for k,f in crit.items() if k!=nm)]
  print(f'-- sauf « {nm} » : {len(L)}')
  for r in sorted(L,key=lambda r:r['d'])[:8]: print('   ',show(r))
print('\n=== effectif par critère ===')
for nm in names: print(f'{sum(crit[nm](r) for r in rows):5d}  {nm}')
