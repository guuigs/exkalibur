import subprocess,os,sys
from concurrent.futures import ThreadPoolExecutor
X0,Y0=933000,6482000   # SW corner ; 7 km x 7 km
L={'mnt':'IGNF_LIDAR-HD_MNT_ELEVATION.ELEVATIONGRIDCOVERAGE.LAMB93','mnh':'IGNF_LIDAR-HD_MNH_ELEVATION.ELEVATIONGRIDCOVERAGE.LAMB93'}
jobs=[]
for k,lay in L.items():
    for i in range(7):
        for j in range(7):
            x=X0+i*1000;y=Y0+j*1000;f=f'lid/{k}_{i}_{j}.bil'
            if os.path.exists(f) and os.path.getsize(f)==4000000: continue
            u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS={lay}&STYLES=&CRS=EPSG:2154&BBOX={x},{y},{x+1000},{y+1000}&WIDTH=1000&HEIGHT=1000&FORMAT=image/x-bil;bits=32"
            jobs.append((u,f))
def go(j):
    for t in range(4):
        r=subprocess.run(['curl','-sS','-m','180','-o',j[1],j[0]])
        if os.path.exists(j[1]) and os.path.getsize(j[1])==4000000: return 1
    return 0
with ThreadPoolExecutor(6) as ex: print(sum(ex.map(go,jobs)),'/',len(jobs))
