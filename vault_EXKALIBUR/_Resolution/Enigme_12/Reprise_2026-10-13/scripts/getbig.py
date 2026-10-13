import numpy as np, subprocess, time, json
LA0,LA1,LO0,LO1=45.20,45.62,5.98,6.42
DLAT=20/111132.0; DLON=20/(111320*np.cos(np.radians(45.43)))
NY=int(round((LA1-LA0)/DLAT)); NX=int(round((LO1-LO0)/DLON)); print(NY,NX)
T=1000; Z=np.full((NY,NX),np.nan,np.float32)
for ty in range(0,NY,T):
  for tx in range(0,NX,T):
    h=min(T,NY-ty); w=min(T,NX-tx)
    lat_top=LA1-ty*DLAT; lat_bot=lat_top-h*DLAT; lon_l=LO0+tx*DLON; lon_r=lon_l+w*DLON
    u=('https://data.geopf.fr/wms-r/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=ELEVATION.ELEVATIONGRIDCOVERAGE.HIGHRES&CRS=EPSG:4326'
       '&BBOX=%.7f,%.7f,%.7f,%.7f&WIDTH=%d&HEIGHT=%d&FORMAT=image/x-bil;bits=32&STYLES='%(lat_bot,lon_l,lat_top,lon_r,w,h))
    for k in range(6):
      subprocess.run(['curl','-sS','-m','180',u,'-o','tileb.bil'],capture_output=True)
      a=np.fromfile('tileb.bil',dtype='<f4')
      if a.size==w*h: break
      time.sleep(4*(k+1))
    Z[ty:ty+h,tx:tx+w]=a.reshape(h,w); print(ty,tx,np.nanmin(a),np.nanmax(a),flush=True)
np.save('big20m.npy',Z); json.dump(dict(LA0=LA0,LA1=LA1,LO0=LO0,LO1=LO1,DLAT=DLAT,DLON=DLON,NY=NY,NX=NX),open('big20m.json','w'))
