import json, sys, math
from PIL import Image, ImageDraw
sys.path.insert(0,'.')
from tiles import deg2num
from geo import direct
def make(img, z, lat0,lon0,lat1,lon1, out, rings=(), pts=(), streams=True, paths=True, scale=1.0, crop=None):
    im=Image.open(img).convert('RGB'); d=ImageDraw.Draw(im)
    x0,y0=deg2num(lat1,lon0,z)
    def P(lon,lat):
        x,y=deg2num(lat,lon,z); return ((x-x0)*256,(y-y0)*256)
    def lines(g):
        t=g['type']; c=g['coordinates']
        return [c] if t=='LineString' else (c if t=='MultiLineString' else [])
    if paths:
        for f in json.load(open('troncon_de_route.json')):
            n=f['properties']['nature']
            colr={'Sentier':(255,90,0),'Chemin':(255,170,0),'Route empierrée':(200,200,0)}.get(n,(120,120,120))
            for l in lines(f['geometry']):
                d.line([P(*p[:2]) for p in l],fill=colr,width=2)
    if streams:
        for f in json.load(open('troncon_hydrographique.json')):
            for l in lines(f['geometry']):
                d.line([P(*p[:2]) for p in l],fill=(0,120,255),width=2)
    for (c,r,col) in rings:
        ring=[P(*direct(c,a,r)[::-1]) for a in range(0,361,1)]
        d.line(ring,fill=col,width=2)
    for (la,lo,lab) in pts:
        x,y=P(lo,la); d.ellipse((x-6,y-6,x+6,y+6),outline=(255,0,0),width=3); d.text((x+8,y-6),lab,fill=(255,0,0))
    if crop:
        a=P(crop[1],crop[2]); b=P(crop[3],crop[0]); im=im.crop((int(a[0]),int(a[1]),int(b[0]),int(b[1])))
    if scale!=1.0: im=im.resize((int(im.width*scale),int(im.height*scale)),Image.LANCZOS)
    im.save(out,quality=88); return im.size
if __name__=='__main__':
    TA=(45.429083,6.030808); CB=(45.423611,6.018889)
    print(make('lidar_z16.jpg',16,45.405,6.015,45.450,6.075,'lidar_overlay.jpg',
         rings=[(TA,1.85,(255,0,0)),(TA,1.8315,(255,150,150)),(TA,1.8685,(255,150,150)),(CB,1.85,(160,0,200))],
         pts=[(TA[0],TA[1],'TA'),(CB[0],CB[1],'CB')], scale=0.5))
