import re,numpy as np
from scipy import ndimage
acc=np.load('acc.npy')*4.0  # m2
GX0,GYT,g=933000,6489000,2
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
# densify in board px
pts=[]
for pa in paths:
    for (a,b),(c,e) in zip(pa,pa[1:]):
        n=max(2,int(np.hypot(c-a,e-b)/3))
        for t in np.linspace(0,1,n): pts.append((631+0.335*(a+(c-a)*t),1490+0.335*(b+(e-b)*t)))
pts=np.array(pts)
POM=np.array([523,368]);TIP=np.array([697,2184])
bl=TIP-POM
for A0 in (3000,10000):
    tal=acc>=A0
    dist=ndimage.distance_transform_edt(~tal)*g
    def score(theta,mirror,scale=1850/1593,anchor=(TX,TY)):
        blg=complex(bl[0]*mirror,-bl[1]);tgt=complex(np.sin(np.radians(theta)),np.cos(np.radians(theta)))
        rot=tgt/(blg/abs(blg))
        v=(( (pts[:,0]-POM[0])*mirror) + 1j*(-(pts[:,1]-POM[1])))*rot*scale
        X=anchor[0]+v.real;Y=anchor[1]+v.imag
        col=((X-GX0)/g).astype(int);row=((GYT-Y)/g).astype(int)
        ok=(col>=0)&(col<acc.shape[1])&(row>=0)&(row<acc.shape[0])
        if ok.mean()<1: return np.nan
        return dist[row,col].mean()
    obs={m:score(180,m) for m in (1,-1)}
    null=np.array([score(th,m) for th in np.arange(0,360,1) for m in (1,-1)])
    null=null[~np.isnan(null)]
    for m in (1,-1):
        print(f'seuil {A0} m2 miroir {m}: distance moyenne fissure->talweg {obs[m]:.1f} m ; rang parmi {len(null)} orientations : {(null<obs[m]).sum()+1} ; mediane null {np.median(null):.1f}')
    # random anchors within 2 km + random theta
    rng=np.random.default_rng(1);vals=[]
    for k in range(4000):
        ax=TX+rng.uniform(-2000,2000);ay=TY+rng.uniform(-2000,2000)
        s=score(rng.uniform(0,360),rng.choice([1,-1]),anchor=(ax,ay))
        if not np.isnan(s): vals.append(s)
    vals=np.array(vals);print('   ancre+cap aleatoires: P(score<=obs)=',(vals<=min(obs.values())).mean(),'n',len(vals))
