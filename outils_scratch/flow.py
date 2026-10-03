import numpy as np
import numpy as np
np.in1d=np.isin
from pysheds.grid import Grid
from pysheds.sview import Raster, ViewFinder
from affine import Affine
M=np.load('M2.npy').astype(np.float64)
X0,Y0,N,g=933000,6482000,7000,2
aff=Affine(g,0,X0,0,-g,Y0+N)
vf=ViewFinder(affine=aff,shape=M.shape,crs='EPSG:2154',nodata=-9999.0)
dem=Raster(M,viewfinder=vf)
grid=Grid(viewfinder=vf)
pf=grid.fill_pits(dem); fl=grid.fill_depressions(pf); inf=grid.resolve_flats(fl)
fdir=grid.flowdir(inf)
acc=grid.accumulation(fdir)
np.save('acc.npy',np.asarray(acc,dtype=np.float32)); np.save('fdir.npy',np.asarray(fdir))
a=np.asarray(acc)*g*g
for th in (1e4,2e4,5e4,1e5): print(th, (a>th).sum())
