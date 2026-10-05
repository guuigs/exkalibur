import math,pickle,datetime,numpy as np
src=open('/home/user/exkalibur/outils_scratch/t108_dates_hugues.py').read().split("fetes={")[0]
exec(src)
rows=pickle.load(open('run/rows_final2.pkl','rb'))
Q=[r for r in rows if r['hb']>=100 and min(r['wd'],r['eauS'])<=150 or (r['hb']>=100 and r['ta']>=1)]
Q2=[r for r in Q if r['op']>=0.25 and max(r['vs'],r['vm'])>=100]
print('Q (maisons>=100+eau):',len(Q),' Q2 (+clairière vue):',len(Q2))
kQ=cKDTree(np.array([(r['x'],r['y']) for r in Q]));kQ2=cKDTree(np.array([(r['x'],r['y']) for r in Q2]))
fetes={'30/04':(4,30),'28/10 Simon-Jude':(10,28),'Pâques 2023 09/04':(4,9),'Pâques 2024 31/03':(3,31),'Pâques 2025 20/04':(4,20),'Pâques 2026 05/04':(4,5),'Pâques 1524 06/04':(4,6),'équinoxe 21/03':(3,21),'équinoxe 23/09':(9,23),'solstice hiver':(12,21),'solstice été':(6,21),'Jean 27/12':(12,27),'Jacques 25/07':(7,25),'André 30/11':(11,30),'Pierre 29/06':(6,29),'Hugues 17/11':(11,17),'Hugues 01/04':(4,1),'Noël':(12,25),'1er nov':(11,1)}
AZ=[]
for nm,(m,d) in fetes.items():
    doy=doy_of(m,d);av=lever_visible(doy)[0];af=sun_az(decl(doy),-0.83)
    for lab,a in (('vis',av),('plat',af)):
        if a is not None:
            for off in (0,90):
                AZ.append((nm,lab,off,(a+off)%360))
AZ.append(('est vrai','',0,90.0));AZ.append(('est vrai','',90,0.0))
print('axes a priori :',len(AZ))
s=S;res=[]
for p in range(1,14):
    for nm,lab,off,a in AZ:
        for k in (3,11):
            n=k-p
            for sg in (1,-1):
                if n==0: continue
                aa=(a+(0 if sg>0 else 180))%360
                lo,la=G.fwd(tlo,tla,aa,abs(n)*s)[:2] if sg*np.sign(n)>0 else G.fwd(tlo,tla,aa,abs(n)*s)[:2]
                # sens : le siège k est à n*s dans la direction aa si n>0 (sg=+1), sinon opposé
                dirn=aa if n>0 else (aa+180)%360
                lo,la=G.fwd(tlo,tla,dirn,abs(n)*s)[:2];x,y=T.transform(lo,la)
                d1=kQ.query([x,y])[0];d2=kQ2.query([x,y])[0]
                res.append((d1,d2,p,k,nm,lab,off,sg,round(a,1),round(la,5),round(lo,5)))
print('positions testées :',len(res))
r1=sorted(res)[:12];print('meilleures vs Q :')
for r in r1: print(' ',round(r[0]),'m (Q2 %.0f m)'%r[1],'T=siège',r[2],'siège',r[3],r[4],r[5],'axe+%d'%r[6],'sens',r[7],'az',r[8],r[9],r[10])
r2=sorted(res,key=lambda r:r[1])[:8];print('meilleures vs Q2 (clairière vue) :')
for r in r2: print(' ',round(r[1]),'m (Q %.0f m)'%r[0],'T=siège',r[2],'siège',r[3],r[4],r[5],'axe+%d'%r[6],'sens',r[7],'az',r[8],r[9],r[10])
# placebo : azimuts uniformes
rng=np.random.default_rng(5);K=40000;h1=0;h2=0;h1_20=0
for _ in range(K):
    a=rng.uniform(0,360);p=rng.integers(1,14);k=rng.choice([3,11]);n=k-p
    if n==0: continue
    lo,la=G.fwd(tlo,tla,a,abs(n)*s)[:2];x,y=T.transform(lo,la)
    h1+=(kQ.query([x,y])[0]<=10);h2+=(kQ2.query([x,y])[0]<=10);h1_20+=(kQ.query([x,y])[0]<=20)
print('placebo : P(<=10 m de Q)=%.4f ; P(<=10 m de Q2)=%.4f ; P(<=20 m de Q)=%.4f'%(h1/K,h2/K,h1_20/K))
print('attendu sur',len(res),'positions : <=10 m Q : %.2f ; Q2 : %.2f'%(len(res)*h1/K,len(res)*h2/K))
print('observé : <=10 m Q :',sum(1 for r in res if r[0]<=10),'; Q2 :',sum(1 for r in res if r[1]<=10),' ; <=20 m Q :',sum(1 for r in res if r[0]<=20))
print('\n--- meilleur résultat par position du départ T dans la rangée de 13 (Christ = place du départ si p indiqué) ---')
for p in range(1,14):
    sub=[r for r in res if r[2]==p]
    b=min(sub,key=lambda r:r[0]);print('T=siège',p,': meilleur %.0f m'%b[0],'(Q2 %.0f m)'%b[1],'siège',b[3],b[4],b[5],'axe+%d'%b[6],b[9],b[10])
