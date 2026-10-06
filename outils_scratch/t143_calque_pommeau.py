exec(open('ring1068.py').read().split('out=[]')[0])
import re,sys
from PIL import Image,ImageDraw
TX,TY=936955.34,6485599.51
svg=open('/home/user/exkalibur/vault_EXKALIBUR/_Resolution/Revue_globale/rayure_epee_guilhem.svg').read()
d=re.search(r'd="([^"]+)"',svg).group(1);toks=re.findall(r'[MLVHC]|-?\d+\.?\d*',d)
paths=[];cur=None;cx=cy=0;i=0;cmd=None
while i<len(toks):
    t=toks[i]
    if t in 'MLVHC': cmd=t;i+=1;continue
    if cmd=='M': cx,cy=float(toks[i]),float(toks[i+1]);i+=2;cur=[(cx,cy)];paths.append(cur);cmd='L'
    elif cmd=='L': cx,cy=float(toks[i]),float(toks[i+1]);i+=2;cur.append((cx,cy))
    elif cmd=='V': cy=float(toks[i]);i+=1;cur.append((cx,cy))
    elif cmd=='H': cx=float(toks[i]);i+=1;cur.append((cx,cy))
    elif cmd=='C': cx,cy=float(toks[i+4]),float(toks[i+5]);i+=6;cur.append((cx,cy))
POM=np.array([523,368]);TIP=np.array([697,2184])
scale_m=float(sys.argv[1]) if len(sys.argv)>1 else 1850/1593
mirror=int(sys.argv[2]) if len(sys.argv)>2 else 1
bl=TIP-POM; blg=complex(bl[0]*mirror,-bl[1]); rot=complex(0,-1)/ (blg/abs(blg))  # blade -> due south
def to_xy(bx,by):
    v=complex((bx-POM[0])*mirror,-(by-POM[1]))*rot*scale_m
    return TX+v.real,TY+v.imag
def svgxy(sx,sy): return to_xy(631+0.335*sx,1490+0.335*sy)
cr=[[svgxy(*p) for p in pa] for pa in paths]
allp=np.array([q for pa in cr for q in pa]);cxm,cym=allp.mean(0)
print('fissure centre',Ti.transform(cxm,cym)[::-1],'dist',np.hypot(cxm-TX,cym-TY))
W=1600;x0,y0=cxm-W/2,cym+W/2
sub=mnt[int(YN-y0):int(YN-y0)+W,int(x0-X0):int(x0-X0)+W]
gy,gx=np.gradient(sub);hs=np.clip(128+(-gx+gy)*40,0,255).astype(np.uint8)
img=Image.fromarray(hs).convert('RGB');dr=ImageDraw.Draw(img)
def P(x,y): return (x-x0,y0-y)
for f in hyd['features']:
    g=f['geometry'];cs=g['coordinates'] if g['type']=='LineString' else [c for l in g['coordinates'] for c in l]
    dr.line([P(c[0],c[1]) for c in cs],fill=(0,120,255),width=3)
for f in r['features']:
    dr.line([P(c[0],c[1]) for c in f['geometry']['coordinates']],fill=(255,200,0),width=2)
for pa in cr: dr.line([P(*q) for q in pa],fill=(255,0,0),width=4)
dr.line([P(*to_xy(*POM)),P(*to_xy(*TIP))],fill=(255,0,255),width=2)
img.save(f'/home/user/exkalibur/images_travail/t143_calque_pommeau_s{scale_m:.3f}_m{mirror}.jpg',quality=85)
