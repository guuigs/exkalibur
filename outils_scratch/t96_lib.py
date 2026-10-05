import pickle,math
def ok_cells(r,fr=0.0,ress=False): return [k for k in r['rocks'] if k['frac']>=fr and (k['ress'] or not ress)]
def lg(r):
  f=[]
  if r['P_reach']: f.append(f"TABLE(θ={r['theta']:.0f}°)")
  if r['dates']: f.append('date:'+'/'.join(r['dates']))
  if r['K']: f.append('axe-Lincoln')
  elif r['D10']: f.append('10stades')
  if r['ld']: f.append(f"lieux-dits {r['ld'][0]}m"+(' ✔' if r['ld'][3] else ''))
  return ' '.join(f)
def line(r):
  c=ok_cells(r);c5=ok_cells(r,0.5);cr=ok_cells(r,0.5,True)
  return f"{r['la']:.6f},{r['lo']:.6f} | {r['d']:.0f} m cap {r['az']:.0f}° | maisons {r['hb']:.0f} | vu sol {r['vs']}/mur {r['vm']} | ouvert {r['op']:.2f} forêt {r['fo']:.2f} | eau {r['wd']:.0f} tw {r['ta']:.1f} | pente {r['slope']:.0f}° | pts-eau+coffre {len(c)} (chemin≥50 %: {len(c5)}, ressaut: {len(cr)}) | {lg(r)}"
