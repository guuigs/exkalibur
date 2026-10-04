exec(open('svg_route.py').read().split("res.sort()")[0])
import numpy as np
jx,jy=T.transform(6.040299,45.422426)
near=[x for x in res if math.hypot(x[2][0]-jx,x[2][1]-jy)<25]
allsc=np.array(sorted(x[0] for x in res))
for sc,sm,n,eu,ratio,k in sorted(near)[:3]:
  rank=(allsc<sc).mean()
  print(f'tour -> Mouret : score {sc:.3f} (miroir {sm:.3f}) ; meilleur que {100*(1-rank):.0f} % des itinéraires ; sinuosité {ratio:.2f} (rayure 1,62)')
