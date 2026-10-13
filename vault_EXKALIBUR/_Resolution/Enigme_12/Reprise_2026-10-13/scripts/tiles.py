import math, os, subprocess, sys, io, time
from PIL import Image
def deg2num(lat, lon, z):
    n=2**z; x=(lon+180)/360*n
    y=(1-math.asinh(math.tan(math.radians(lat)))/math.pi)/2*n
    return x,y
def fetch(layer,tms,fmt,z,x,y,style='normal'):
    d='tiles/%s/%d'%(layer.replace('/','_'),z); os.makedirs(d,exist_ok=True)
    fn='%s/%d_%d.%s'%(d,x,y,'png' if 'png' in fmt else 'jpg')
    if os.path.exists(fn) and os.path.getsize(fn)>0: return fn
    u=('https://data.geopf.fr/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=%s&STYLE=%s&TILEMATRIXSET=%s&TILEMATRIX=%d&TILEROW=%d&TILECOL=%d&FORMAT=%s'%(layer,style,tms,z,y,x,fmt))
    for i in range(6):
        r=subprocess.run(['curl','-sS','-m','60','-o',fn,u],capture_output=True)
        try:
            Image.open(fn).load(); return fn
        except Exception:
            time.sleep(2*(i+1))
    return None
def mosaic(layer,tms,fmt,z,lat0,lon0,lat1,lon1,out,style='normal'):
    x0,y0=deg2num(lat1,lon0,z); x1,y1=deg2num(lat0,lon1,z)
    X0,Y0,X1,Y1=int(x0),int(y0),int(x1),int(y1)
    W=(X1-X0+1)*256; H=(Y1-Y0+1)*256
    im=Image.new('RGB',(W,H),(255,255,255))
    from concurrent.futures import ThreadPoolExecutor
    jobs=[(x,y) for x in range(X0,X1+1) for y in range(Y0,Y1+1)]
    with ThreadPoolExecutor(12) as ex:
        res=list(ex.map(lambda xy:(xy,fetch(layer,tms,fmt,z,xy[0],xy[1],style)),jobs))
    for (x,y),fn in res:
        if fn:
            t=Image.open(fn).convert('RGB'); im.paste(t,((x-X0)*256,(y-Y0)*256))
    # crop to bbox
    cx0=int((x0-X0)*256); cy0=int((y0-Y0)*256); cx1=int((x1-X0)*256); cy1=int((y1-Y0)*256)
    im=im.crop((cx0,cy0,cx1,cy1)); im.save(out,quality=90); return im
if __name__=='__main__':
    layer,tms,fmt,z=sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4])
    lat0,lon0,lat1,lon1=map(float,sys.argv[5:9]); out=sys.argv[9]
    im=mosaic(layer,tms,fmt,z,lat0,lon0,lat1,lon1,out); print(im.size)
