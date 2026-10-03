import sys,subprocess,json
from PIL import Image,ImageDraw
def get(layer,bbox,w,h,fmt,out):
    s,wl,n,e=bbox
    u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS={layer}&STYLES=&CRS=EPSG:4326&BBOX={s},{wl},{n},{e}&WIDTH={w}&HEIGHT={h}&FORMAT={fmt}"
    subprocess.run(['curl','-sS','-m','120','-o',out,u],check=True)
def annot(f,o,bbox,pts,w,h,scale=50):
    s,wl,n,e=bbox
    im=Image.open(f).convert('RGB');d=ImageDraw.Draw(im)
    for k,(la,lo) in pts.items():
        x=(lo-wl)/(e-wl)*w;y=(n-la)/(n-s)*h
        d.ellipse((x-6,y-6,x+6,y+6),outline=(255,0,0),width=3);d.text((x+8,y-6),k,fill=(255,255,0))
    import math
    px=scale/(111320*math.cos(math.radians((s+n)/2)))/(e-wl)*w
    d.line((15,h-15,15+px,h-15),fill=(255,255,255),width=4);d.text((15,h-32),f'{scale} m',fill=(255,255,255))
    im.save(o)
