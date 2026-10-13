import json, subprocess, time, sys
def wfs(layer, bb, maxf=50000):
    feats=[]; start=0
    while True:
        u=("https://data.geopf.fr/wfs/ows?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES="+layer+
           "&OUTPUTFORMAT=application/json&SRSNAME=EPSG:4326&COUNT=5000&STARTINDEX=%d&BBOX=%f,%f,%f,%f,urn:ogc:def:crs:EPSG::4326"%(start,*bb))
        for i in range(6):
            r=subprocess.run(['curl','-sS','-m','180',u],capture_output=True,text=True)
            try:
                j=json.loads(r.stdout); break
            except Exception:
                time.sleep(3*(i+1))
        else:
            raise RuntimeError('fail '+layer+r.stderr[:200])
        f=j.get('features',[]); feats+=f
        if len(f)<5000 or len(feats)>=maxf: break
        start+=5000
    return feats
if __name__=='__main__':
    layer=sys.argv[1]; bb=tuple(map(float,sys.argv[2:6])); out=sys.argv[6]
    f=wfs(layer,bb); json.dump(f,open(out,'w')); print(layer,len(f))
