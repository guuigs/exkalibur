import numpy as np, subprocess, time, json, sys
LA0,LA1,LO0,LO1=45.4040,45.4540,5.9980,6.0640
DLAT=1.8e-5; DLON=2.56e-5
NY=int(round((LA1-LA0)/DLAT)); NX=int(round((LO1-LO0)/DLON))
print(NY,NX)
T=1000
Z=np.full((NY,NX),np.nan,np.float32)
for ty in range(0,NY,T):
  for tx in range(0,NX,T):
    h=min(T,NY-ty); w=min(T,NX-tx)
    lat_top=LA1-ty*DLAT; lat_bot=lat_top-h*DLAT
    lon_l=LO0+tx*DLON; lon_r=lon_l+w*DLON
    u=('https://data.geopf.fr/wms-r/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=ELEVATION.ELEVATIONGRIDCOVERAGE.HIGHRES&CRS=EPSG:4326'
       '&BBOX=%.7f,%.7f,%.7f,%.7f&WIDTH=%d&HEIGHT=%d&FORMAT=image/x-bil;bits=32&STYLES='%(lat_bot,lon_l,lat_top,lon_r,w,h))
    for k in range(6):
      r=subprocess.run(['curl','-sS','-m','120',u,'-o','tile.bil'],capture_output=True)
      try:
        a=np.fromfile('tile.bil',dtype='<f4')
        if a.size==w*h: break
      except Exception: pass
      time.sleep(3*(k+1))
    Z[ty:ty+h,tx:tx+w]=a.reshape(h,w)
    print(ty,tx,np.nanmin(a),np.nanmax(a),flush=True)
np.save('dem2m.npy',Z)
json.dump(dict(LA0=LA0,LA1=LA1,LO0=LO0,LO1=LO1,DLAT=DLAT,DLON=DLON,NY=NY,NX=NX,note='row0 = LA1 (north), pixel-edge grid, WMS EPSG:4326 RGE ALTI HIGHRES'),open('dem2m.json','w'))
