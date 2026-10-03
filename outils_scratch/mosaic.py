import numpy as np
X0,Y0,N=933000,6482000,7000
for k in ('mnt','mnh'):
    A=np.zeros((N,N),np.float32)
    for i in range(7):
        for j in range(7):
            t=np.fromfile(f'lid/{k}_{i}_{j}.bil','<f4').reshape(1000,1000)
            A[(6-j)*1000:(7-j)*1000, i*1000:(i+1)*1000]=t
    A[A<-1000]=np.nan
    np.save(f'{k}.npy',A); print(k,np.nanmin(A),np.nanmax(A),np.isnan(A).sum())
