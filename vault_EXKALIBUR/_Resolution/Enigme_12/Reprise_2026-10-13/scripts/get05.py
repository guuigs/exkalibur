import numpy as np, subprocess, time, json, sys, os
layer, out, lat0, lon0, half = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
RES=0.5
DLAT=RES/111132.0; DLON=RES/(111320*np.cos(np.radians(lat0)))
LA1=lat0+half/111132.0; LO0=lon0-half/(111320*np.cos(np.radians(lat0)))
N=int(2*half/RES)
T=1000; Z=np.full((N,N),np.nan,np.float32)
for ty in range(0,N,T):
  for tx in range(0,N,T):
    h=min(T,N-ty); w=min(T,N-tx)
    lat_top=LA1-ty*DLAT; lat_bot=lat_top-h*DLAT; lon_l=LO0+tx*DLON; lon_r=lon_l+w*DLON
    u=('https://data.geopf.fr/wms-r/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=%s&CRS=EPSG:4326'
       '&BBOX=%.8f,%.8f,%.8f,%.8f&WIDTH=%d&HEIGHT=%d&FORMAT=image/x-bil;bits=32&STYLES='%(layer,lat_bot,lon_l,lat_top,lon_r,w,h))
    for k in range(6):
      if os.path.exists('t.bil'): os.remove('t.bil')  # sinon une réponse ratée réutilise la dalle précédente
      subprocess.run(['curl','-sS','-m','180',u,'-o','t.bil'],capture_output=True)
      a=np.fromfile('t.bil',dtype='<f4') if os.path.exists('t.bil') else np.zeros(0)
      if a.size==w*h: break
      time.sleep(4*(k+1))
    Z[ty:ty+h,tx:tx+w]=a.reshape(h,w); print(ty,tx,np.nanmin(a),np.nanmax(a),flush=True)
np.save(out+'.npy',Z); json.dump(dict(LA1=LA1,LO0=LO0,DLAT=DLAT,DLON=DLON,N=N,RES=RES),open(out+'.json','w'))
