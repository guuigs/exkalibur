# T1 tâche 1 (v2) : contour peint tracé à la main (coordonnées du recadrage t1_pond.jpg 1353x993) vs polygones IGN, comparaison invariante (aire, centre, axes principaux, 4 symétries + rotation fine)
import numpy as np, math, json
from PIL import Image, ImageDraw
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
OUT=r'C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/'
W=r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/'
paint=[(140,230),(300,190),(560,195),(650,210),(760,190),(900,150),(960,170),(1010,250),(1080,340),(1100,500),(1110,650),(1080,730),(1000,790),(880,830),(760,800),(640,740),(520,680),(430,620),(330,580),(240,500),(170,380),(130,290)]
# contrôle visuel du tracé
im=Image.open(W+'t1_pond.jpg').convert('RGB'); d=ImageDraw.Draw(im); d.line(paint+[paint[0]],fill=(255,0,0),width=5); im.save(OUT+'T1_bassin_trace_controle.png')
N=160
def fill(rings,S=N):
    P=np.array([p for r in rings for p in r],float)
    m=(P.min(0)+P.max(0))/2; ext=(P.max(0)-P.min(0)).max()*1.02
    img=Image.new('L',(800,800),0); dd=ImageDraw.Draw(img)
    for r in rings: dd.polygon([(800*((x-m[0])/ext+.5),800*(-(y-m[1])/ext+.5)) for x,y in r],fill=255)
    a=np.array(img)>0
    ys,xs=np.nonzero(a); return np.array([xs,-ys],float).T  # points remplis (y vers le haut)
def normalize(pts):
    c=pts.mean(0); p=pts-c; s=math.sqrt(len(pts)); p=p/s   # aire unité
    cov=np.cov(p.T); w,v=np.linalg.eigh(cov); v=v[:,::-1]; q=p@v
    return q, math.sqrt(w[1]/w[0]) if False else math.sqrt(w[0]/w[1])  # elongation
def mask(q,S=N,sc=0.42):
    ix=np.round(S/2+q[:,0]*S*sc*1.0).astype(int); iy=np.round(S/2-q[:,1]*S*sc*1.0).astype(int)
    m=np.zeros((S,S),bool); ok=(ix>=0)&(ix<S)&(iy>=0)&(iy<S); m[iy[ok],ix[ok]]=True
    from PIL import ImageFilter
    return np.array(Image.fromarray(m.astype('uint8')*255).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(3)))>0
def iou_best(qa,qb):
    best=(0,0,0)
    for mir in (1,-1):
        for flip in (1,-1):
            for ang in range(-20,21,5):
                a=math.radians(ang); R=np.array([[math.cos(a),-math.sin(a)],[math.sin(a),math.cos(a)]])
                qq=(qb*np.array([flip,mir*flip]))@R.T
                A=mask(qa);B=mask(qq); i=(A&B).sum()/max(1,(A|B).sum())
                if i>best[0]: best=(i,mir*flip if False else (flip,mir),ang)
    return best
qp,ep=normalize(fill([paint]))
print('peint élongation (petit/grand axe) %.2f'%ep)
lat0=TA[0]; kx=111320*math.cos(math.radians(lat0)); ky=110540
res=[]
for L in ('surface_hydrographique','plan_d_eau'):
    for f in load(L):
        p=f['properties']; g=f['geometry']
        if p.get('nature')=='Ecoulement naturel': continue
        c=cen(g); dist=hav(TA,c)
        if dist>6.0: continue
        rings=[[((q[0]-TA[1])*kx,(q[1]-TA[0])*ky) for q in poly[0]] for poly in g['coordinates']]
        A=sum(abs(sum(r[i][0]*r[(i+1)%len(r)][1]-r[(i+1)%len(r)][0]*r[i][1] for i in range(len(r)))/2) for r in rings)
        if A<100: continue
        qi,ei=normalize(fill(rings)); b=iou_best(qp,qi)
        res.append(dict(id=p['cleabs'],layer=L,nom=p.get('toponyme'),nature=p.get('nature'),pers=p.get('persistance'),dist=dist,cap=brg(TA,c),aire=A,elong=ei,iou=b[0],flipmir=b[1],ang=b[2],lat=c[0],lon=c[1],rings=rings,qi=qi))
res.sort(key=lambda r:-r['iou'])
# doublons plan_d_eau / surface (même centroïde) signalés
print('n comparés',len(res))
print('IoU de contrôle (peint vs peint):',round(iou_best(qp,qp)[0],2))
for r in res[:15]: print('%.2f'%r['iou'],(r['nom'] or '-'),r['nature'],r['pers'],'%.2fkm cap%d aire%d m2 elong %.2f'%(r['dist'],r['cap'],r['aire'],r['elong']),r['id'])
for r in res:
    if r['nom']: print('NOMMÉ %-22s IoU %.2f elong %.2f aire %d dist %.2f'%(r['nom'],r['iou'],r['elong'],r['aire'],r['dist']))
ious=np.array([r['iou'] for r in res]); print('IoU médiane %.2f, max %.2f, nb>=0.80: %d, nb>=0.75: %d'%(np.median(ious),ious.max(),(ious>=.8).sum(),(ious>=.75).sum()))
json.dump([{k:v for k,v in r.items() if k not in('rings','qi')} for r in res],open(OUT+'T1_bassin_scores.json','w'),ensure_ascii=False,indent=1)
# planche : peint + 11 meilleurs + 3 nommés
sel=res[:9]+[r for r in res if r['nom']]
Wd=250; sheet=Image.new('RGB',(Wd*4,Wd*4),'white'); dr=ImageDraw.Draw(sheet)
def poly_img(q,flip=(1,1),ang=0,col=(80,120,220)):
    a=math.radians(ang); R=np.array([[math.cos(a),-math.sin(a)],[math.sin(a),math.cos(a)]])
    q=(q*np.array(flip))@R.T
    return q
def draw_pts(idx,q,label,label2):
    ox=(idx%4)*Wd; oy=(idx//4)*Wd
    tile=Image.new('RGB',(Wd-10,Wd-40),'white'); dd=ImageDraw.Draw(tile)
    for x,y in q: pass
    m=mask(q,S=Wd-40); tile=Image.fromarray(np.where(m[...,None],np.array([80,120,220],np.uint8),np.array([255,255,255],np.uint8)).astype(np.uint8)).resize((Wd-10,Wd-40))
    sheet.paste(tile,(ox+5,oy+5)); dr.text((ox+5,oy+Wd-32),label,fill='black'); dr.text((ox+5,oy+Wd-20),label2,fill='black')
draw_pts(0,qp,'ENLUMINURE 9 (trace)','contour peint')
for i,r in enumerate(sel[:12]):
    draw_pts(i+1,poly_img(r['qi'],r['flipmir'],r['ang']),'%s %.2f'%((r['nom'] or r['nature'])[:24],r['iou']),'%.1fkm cap%d %dm2 %s'%(r['dist'],r['cap'],r['aire'],r['id'][-6:]))
sheet.save(OUT+'T1_bassin_planche.png')
