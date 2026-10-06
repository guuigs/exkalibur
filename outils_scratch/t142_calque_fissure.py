exec(open('ring1068.py').read().split('out=[]')[0])
import re
from PIL import Image,ImageDraw
TX,TY=936955.34,6485599.51
svg=open('/home/user/exkalibur/vault_EXKALIBUR/_Resolution/Revue_globale/rayure_epee_guilhem.svg').read()
d=re.search(r'd="([^"]+)"',svg).group(1)
# parse polylines (M/L/V/H/C approx)
toks=re.findall(r'[MLVHC]|-?\d+\.?\d*',d)
paths=[];cur=None;cx=cy=0;i=0;cmd=None
while i<len(toks):
    t=toks[i]
    if t in 'MLVHC': cmd=t;i+=1;continue
    if cmd=='M': cx,cy=float(toks[i]),float(toks[i+1]);i+=2;cur=[(cx,cy)];paths.append(cur);cmd='L'
    elif cmd=='L': cx,cy=float(toks[i]),float(toks[i+1]);i+=2;cur.append((cx,cy))
    elif cmd=='V': cy=float(toks[i]);i+=1;cur.append((cx,cy))
    elif cmd=='H': cx=float(toks[i]);i+=1;cur.append((cx,cy))
    elif cmd=='C': cx,cy=float(toks[i+4]),float(toks[i+5]);i+=6;cur.append((cx,cy))
tip=(697,2184);mpp=1850/1593
def to_xy(sx,sy,rot=0):
    bx,by=631+0.335*sx,1490+0.335*sy
    e=(bx-tip[0])*mpp; n=(tip[1]-by)*mpp
    a=np.radians(rot);E=e*np.cos(a)+n*np.sin(a);N=-e*np.sin(a)+n*np.cos(a)
    return TX+E,TY+N
import sys
rot=float(sys.argv[1]) if len(sys.argv)>1 else 0
W=1300;x0,y0=TX-650,TY+1000  # window
sub=mnt[int(YN-y0):int(YN-y0)+W,int(x0-X0):int(x0-X0)+W]
gy,gx=np.gradient(sub);hs=np.clip(128+ ( -gx*1.0 + gy*1.0)*40,0,255).astype(np.uint8)
img=Image.fromarray(hs).convert('RGB');dr=ImageDraw.Draw(img)
def P(x,y): return (x-x0,y0-y)
for f in hyd['features']:
    g=f['geometry'];cs=g['coordinates'] if g['type']=='LineString' else [c for l in g['coordinates'] for c in l]
    dr.line([P(c[0],c[1]) for c in cs],fill=(0,120,255),width=3)
for f in r['features']:
    cs=f['geometry']['coordinates'];dr.line([P(c[0],c[1]) for c in cs],fill=(255,200,0),width=2)
for p in paths:
    dr.line([P(*to_xy(sx,sy,rot)) for sx,sy in p],fill=(255,0,0),width=4)
dr.ellipse([P(TX,TY)[0]-8,P(TX,TY)[1]-8,P(TX,TY)[0]+8,P(TX,TY)[1]+8],outline=(255,0,255),width=3)
img.save(f'/home/user/exkalibur/images_travail/t142_calque_fissure_rot{int(rot)}.jpg',quality=88)
for p in paths:
    a=to_xy(*p[0],rot);b=to_xy(*p[-1],rot);print([ (round(v[1],5),round(v[0],5)) for v in (Ti.transform(*a)[::-1],Ti.transform(*b)[::-1])])
