# T1 tâche 1 : comparaison de forme entre le bassin de l'enluminure 9 et les surfaces d'eau IGN (<6 km de la tour)
import numpy as np, math, json
from PIL import Image, ImageDraw
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
W=r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/'
N=128
def norm_mask(m):
    ys,xs=np.nonzero(m); cy,cx=ys.mean(),xs.mean(); a=m.sum()
    return np.array([ (xs-cx)/math.sqrt(a),(ys-cy)/math.sqrt(a)]).T   # points normalisés aire=1
def raster(pts,ang=0,mirror=False):
    p=pts.copy()
    if mirror: p[:,0]*=-1
    c,s=math.cos(ang),math.sin(ang); p=p@np.array([[c,-s],[s,c]])
    return p
def rast_poly(polys,ang,mirror):
    # polys: liste d'anneaux (Nx2 en m), normalisés par l'aire totale -> masque NxN
    im=Image.new('L',(N,N),0); d=ImageDraw.Draw(im)
    for r in polys:
        q=raster(r,ang,mirror); d.polygon([(N/2+x*N*0.4,N/2+y*N*0.4) for x,y in q],fill=255)
    return np.array(im)>0
# --- masque du bassin peint : pixels bleus dans t1_pond.jpg
im=Image.open(W+'t1_pond.jpg').convert('RGB'); a=np.array(im).astype(int)
R,G,B=a[...,0],a[...,1],a[...,2]
mask=(B>R+35)&(B>G+5)&(B>110)
# garder la plus grosse composante (flood fill simple)
from collections import deque
lab=np.zeros(mask.shape,int); k=0; sizes={}
for y in range(0,mask.shape[0]):
    for x in range(0,mask.shape[1]):
        if mask[y,x] and not lab[y,x]:
            k+=1; q=deque([(y,x)]); lab[y,x]=k; n=0
            while q:
                cy,cx=q.popleft(); n+=1
                for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
                    yy,xx=cy+dy,cx+dx
                    if 0<=yy<mask.shape[0] and 0<=xx<mask.shape[1] and mask[yy,xx] and not lab[yy,xx]:
                        lab[yy,xx]=k; q.append((yy,xx))
            sizes[k]=n
kb=max(sizes,key=sizes.get); pm=lab==kb
# fermeture (les poissons et les reflets trouent le masque)
from PIL import ImageFilter
pmi=Image.fromarray((pm*255).astype('uint8')).filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.MinFilter(21))
pm=np.array(pmi)>0
Image.fromarray((pm*255).astype('uint8')).save(W+'t1/pond_mask.png')
ys,xs=np.nonzero(pm); print('masque bassin px',pm.sum(),'bbox',xs.min(),xs.max(),ys.min(),ys.max())
ptsP=[]
ph=Image.fromarray((pm*255).astype('uint8')).resize((N*2,N*2))
# anneau d'origine pour raster : on utilise directement le masque pour l'IoU
def norm_img_mask(m):
    ys,xs=np.nonzero(m); cy,cx=ys.mean(),xs.mean(); s=math.sqrt(m.sum())
    return np.array([(xs-cx)/s,(ys-cy)/s]).T
Pp=norm_img_mask(pm)
def mask_from_pts(P,ang,mirror):
    q=raster(P,ang,mirror); ix=np.round(N/2+q[:,0]*N*0.4).astype(int); iy=np.round(N/2+q[:,1]*N*0.4).astype(int)
    m=np.zeros((N,N),bool); ok=(ix>=0)&(ix<N)&(iy>=0)&(iy<N); m[iy[ok],ix[ok]]=True
    return np.array(Image.fromarray((m*255).astype('uint8')).filter(ImageFilter.MaxFilter(3)))>0
Mp={ (ang,mir):mask_from_pts(Pp,math.radians(ang),mir) for ang in range(0,360,10) for mir in (False,)}
# --- polygones IGN
lat0=TA[0]; kx=111320*math.cos(math.radians(lat0)); ky=110540
cands=[]
for L in ('surface_hydrographique','plan_d_eau'):
    for f in load(L):
        p=f['properties']; g=f['geometry']; nat=p.get('nature'); 
        if nat=='Ecoulement naturel': continue
        c=cen(g); d=hav(TA,c)
        if d>6.0: continue
        rings=[]; 
        for poly in g['coordinates']:
            rings.append([( (x-TA[1])*kx,(y-TA[0])*ky) for x,y in [(q[0],q[1]) for q in poly[0]]])
        # aire (m²)
        def area(r):
            return abs(sum(r[i][0]*r[(i+1)%len(r)][1]-r[(i+1)%len(r)][0]*r[i][1] for i in range(len(r)))/2)
        A=sum(area(r) for r in rings)
        cands.append(dict(id=p['cleabs'],layer=L,nom=p.get('toponyme'),nature=nat,pers=p.get('persistance'),d=d,cap=brg(TA,c),area=A,rings=rings,lat=c[0],lon=c[1]))
# dédoublonnage plan_d_eau/surface (même polygone) : on garde tout, on marquera
print('candidats',len(cands))
res=[]
for c in cands:
    if c['area']<150: continue
    allp=np.array([pt for r in c['rings'] for pt in r]); 
    # points remplis : rasterisation fine
    xs_=allp[:,0]; ys_=allp[:,1]; sc=math.sqrt(c['area'])
    im=Image.new('L',(N,N),0); best=0;bang=0;bm=None
    # remplir polygone puis échantillonner
    S=400; mx,my=(xs_.min()+xs_.max())/2,(ys_.min()+ys_.max())/2
    ext=max(xs_.max()-xs_.min(),ys_.max()-ys_.min())*1.05
    big=Image.new('L',(S,S),0); d=ImageDraw.Draw(big)
    for r in c['rings']:
        d.polygon([((x-mx)/ext*S+S/2,-(y-my)/ext*S+S/2) for x,y in r],fill=255)
    m=np.array(big)>0
    if m.sum()<30: continue
    P=norm_img_mask(m)
    for mir in (False,True):
        for ang in range(0,360,10):
            mm=mask_from_pts(P,math.radians(ang),mir)
            # IoU contre le masque peint pour chaque rotation du peint : on tourne seulement l'IGN, le peint fixe
            pp=Mp[(0,False)]
            # léger décalage de recentrage
            iou=(mm&pp).sum()/max(1,(mm|pp).sum())
            if iou>best: best=iou;bang=ang;bmir=mir
    c['iou']=best;c['ang']=bang;c['mir']=bmir
    res.append(c)
res.sort(key=lambda c:-c['iou'])
# aussi : plusieurs polygones du même nom -> montrer
json.dump([{k:v for k,v in c.items() if k!='rings'} for c in res],open(r'C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/T1_bassin_scores.json','w'),ensure_ascii=False,indent=1)
print('n comparés',len(res))
for c in res[:15]:
    print('%.2f'%c['iou'],c['nom'] or '-',c['nature'],c['pers'],'%.2fkm cap%d aire%dm2'%(c['d'],c['cap'],c['area']),'rot',c['ang'],'mir',c['mir'],c['id'])
# planche PNG
top=res[:12]
Wd=260; sheet=Image.new('RGB',(Wd*4,Wd*4),'white'); d=ImageDraw.Draw(sheet)
pmi=Image.fromarray((pm*255).astype('uint8')).convert('RGB').resize((Wd-10,Wd-40)); sheet.paste(pmi,(5,5)); d.text((5,Wd-30),'ENLUMINURE 9 (masque bleu)',fill='red')
def draw_c(c,idx):
    ox=(idx%4)*Wd; oy=(idx//4)*Wd
    rings=c['rings']; allp=np.array([pt for r in rings for pt in r])
    mx,my=(allp[:,0].min()+allp[:,0].max())/2,(allp[:,1].min()+allp[:,1].max())/2
    ext=max(np.ptp(allp[:,0]),np.ptp(allp[:,1]))*1.1
    dd=Image.new('RGB',(Wd-10,Wd-40),'white'); d2=ImageDraw.Draw(dd)
    ang=math.radians(c['ang']); 
    for r in rings:
        pts=np.array([((x-mx)/ext,(y-my)/ext) for x,y in r])
        q=raster(pts,ang,c['mir'])
        d2.polygon([((Wd-10)/2+x*(Wd-40),(Wd-40)/2-(-y)*(Wd-40)) for x,y in q],fill=(80,120,220))
    sheet.paste(dd,(ox+5,oy+5)); d.text((ox+5,oy+Wd-30),'%s %.2f %s'%((c['nom'] or c['nature'])[:22],c['iou'],c['id'][-8:]),fill='black')
    d.text((ox+5,oy+Wd-18),'%.1fkm cap%d %dm2'%(c['d'],c['cap'],c['area']),fill='black')
for i,c in enumerate(top): draw_c(c,i+1)
sheet.save(r'C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/T1_bassin_planche.png')
# nommés
for c in res:
    if c['nom']: print('NOMMÉ',c['nom'],'%.2f'%c['iou'],c['pers'],c['id'])
