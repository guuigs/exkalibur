import json,gzip,csv,math,subprocess,time,os,collections
from PIL import Image,ImageDraw,ImageFont
from shapely.geometry import shape,box,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
tr=lambda g:stf(lambda x,y,z=None:T.transform(x,y),g)
x0,y0=T.transform(6.0455,45.4150);x1,y1=T.transform(6.0690,45.4325)
S=1.0;W=int((x1-x0)*S);H=int((y1-y0)*S)
BB=box(x0,y0,x1,y1)
def pm(fn):
  o={}
  for r in csv.reader(open(fn,encoding='latin-1'),delimiter=';'):
    if len(r)>23: o[(r[5].strip(),r[6].strip().zfill(4))]=(r[20],r[23])
  return o
own38426=json.load(open('cad/pm_38426.json'))
SRC=[('38426','cad/38426-parcelles.json',None),('38268','cad/38268-parcelles.json.gz','cad/pm_38268.csv'),('38006','cad/38006-parcelles.json.gz','cad/pm_38006.csv'),('38314','cad/38314-parcelles.json.gz','cad/pm_38314.csv')]
P=[]   # (id, geom, cat, owner)
for code,f,pmf in SRC:
  d=json.load(gzip.open(f) if f.endswith('gz') else open(f));o=pm(pmf) if pmf else None
  for ft in d['features']:
    g0=shape(ft['geometry'])
    if not g0.intersects(box(6.044,45.413,6.070,45.434)): continue
    g=tr(g0).buffer(0)
    if not g.intersects(BB): continue
    p=ft['properties']
    if o is None:
      v=own38426.get(p['id']);ow=(v[0],v[1]) if v else None
    else:
      ow=o.get((p['section'].lstrip('0') or p['section'],p['numero'].zfill(4))) or o.get((p['section'],p['numero'].zfill(4)))
    if ow is None: cat='part'
    elif ow[0][:1] in '1234': cat='pub'
    elif ow[0][:1]=='9': cat='pubetab'
    elif 'BND' in ow[1]: cat='bnd'
    else: cat='pm'
    P.append((p['id'],g,cat,ow[1] if ow else '',p.get('contenance'),code))
cnt=collections.Counter(c for _,_,c,_,_,_ in P);print('parcelles dans la carte :',dict(cnt))
allp=unary_union([g for _,g,_,_,_,_ in P])
FP=[(f['properties'].get('toponyme'),shape(f['geometry'])) for f in json.load(open('wfs_foret_publique.json'))['features'] if shape(f['geometry']).intersects(BB)]
roads=unary_union([shape(f['geometry']) for f in json.load(open('large/troncon_de_route.json'))['features'] if shape(f['geometry']).intersects(BB)])
EMP=allp.buffer(25).buffer(-25)
NC=EMP.intersection(BB).difference(allp.buffer(0.3)).buffer(-0.2)
NCv=NC.intersection(roads.buffer(6));NCo=NC.difference(roads.buffer(6))
u=f"https://data.geopf.fr/wms-r?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=HR.ORTHOIMAGERY.ORTHOPHOTOS&STYLES=&CRS=EPSG:2154&BBOX={x0},{y0},{x1},{y1}&WIDTH={W}&HEIGHT={H}&FORMAT=image/jpeg"
im=None
for i in range(12):
  if os.path.exists('tl.jpg'): os.remove('tl.jpg')
  subprocess.run(['curl','-sS','-m','150','-o','tl.jpg',u])
  try: im=Image.open('tl.jpg').convert('RGBA');break
  except Exception: time.sleep(2)
Q=lambda x,y:((x-x0)*S,(y1-y)*S)
ov=Image.new('RGBA',(W,H),(0,0,0,0));dd=ImageDraw.Draw(ov)
def poly(g,fill=None,outline=None,w=1):
  for gg in getattr(g,'geoms',[g]):
    if gg.geom_type=='Polygon' and not gg.is_empty:
      pts=[Q(*c[:2]) for c in gg.exterior.coords];dd.polygon(pts,fill=fill,outline=outline)
COL={'pub':(40,230,70,110),'pubetab':(0,200,255,100),'pm':(255,150,0,70),'bnd':(255,80,200,70)}
for pid,g,c,ow,ct,code in P:
  if c in COL: poly(g,fill=COL[c])
for t,g in FP: poly(g.intersection(BB),fill=None,outline=(0,255,100,255))
poly(NCv,fill=(200,255,120,140));poly(NCo,fill=(255,255,255,70))
for pid,g,c,ow,ct,code in P:
  for gg in getattr(g,'geoms',[g]):
    if gg.geom_type=='Polygon': dd.line([Q(*q[:2]) for q in gg.exterior.coords],fill=(255,255,255,120),width=1)
im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
F=lambda s,b=False:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf'%('-Bold' if b else ''),s)
# eau
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
  g=shape(f['geometry']);nm=f['properties'].get('cpx_toponyme_de_cours_d_eau')
  for l in getattr(g,'geoms',[g]):
    if l.intersects(BB): d.line([Q(*c[:2]) for c in l.coords],fill=(0,170,255,255) if nm else (90,200,255,255),width=3 if nm else 2)
# chemins
for f in json.load(open('large/troncon_de_route.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]):
    if l.intersects(BB): d.line([Q(*c[:2]) for c in l.coords],fill=(255,255,255,235),width=1)
# Tire-Loup
ld=json.load(gzip.open('ld.json.gz'))
for f in ld['features']:
  if f['properties'].get('nom','').startswith('TIRE LOUP'):
    g=tr(shape(f['geometry'])).buffer(0)
    for gg in getattr(g,'geoms',[g]): d.line([Q(*c[:2]) for c in gg.exterior.coords],fill=(255,120,0,255),width=3)
    c=g.centroid;q=Q(c.x,c.y);d.text((q[0]-90,q[1]-60),'TIRE-LOUP (lieu-dit cadastral)',fill=(255,150,0,255),font=F(14,True))
f14=F(14,True);f12=F(12)
def lab(x,y,t,col=(255,255,255,255),dx=8,dy=-6,f=f14):
  q=Q(x,y);d.ellipse([q[0]-5,q[1]-5,q[0]+5,q[1]+5],outline=col,width=3);d.text((q[0]+dx,q[1]+dy),t,fill=col,font=f)
lab(*T.transform(6.054780,45.426948),'J5 (croisement à 5 voies)',(255,0,255,255))
lab(*T.transform(6.05785,45.42547),'gué du Tapon',(0,230,255,255))
lab(*T.transform(6.058280,45.418440),'Bois du Rechouchet',(255,255,120,255),f=f12)
lab(*T.transform(6.0417,45.4240),'',(255,255,255,0))
# noms de ruisseaux (milieu de tronçon)
done=set()
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
  nm=f['properties'].get('cpx_toponyme_de_cours_d_eau')
  if not nm or nm in done: continue
  g=shape(f['geometry']).intersection(BB)
  if g.is_empty: continue
  c=(g.geoms[0] if hasattr(g,'geoms') else g).interpolate(0.5,normalized=True);q=Q(c.x,c.y)
  d.rectangle([q[0]+4,q[1]-9,q[0]+4+len(nm)*8,q[1]+7],fill=(0,0,0,150));d.text((q[0]+6,q[1]-9),nm,fill=(120,220,255,255),font=f12);done.add(nm)
# étiquettes des parcelles publiques > 4000 m2
for pid,g,c,ow,ct,code in P:
  if c=='pub' and g.area>6000:
    cc=g.representative_point();q=Q(cc.x,cc.y);short=ow.replace('COMMUNE DE ','').replace('COMMUNE D ','').replace('COMMUNAUTE DE COMMUNES','CC')[:18]
    d.text((q[0]-30,q[1]-6),f'{short}',fill=(0,60,0,255),font=F(11,True))
# légende
LG=[((40,230,70),'parcelle publique (commune, CC, département…)'),((0,255,100),'contour : forêt publique (ONF)'),((200,255,120),'voirie non cadastrée (chemins : public sûr)'),((255,255,255),'autre non cadastré (lits de ruisseaux : douteux)'),((255,150,0),'personne morale privée'),((255,80,200),'indivision privée (« BND »)'),((255,255,255),'limites de parcelles = privé (particuliers) si non coloré')]
d.rectangle([0,0,W,60],fill=(0,0,0,185));d.text((10,6),'Forêt de Tire-Loup et ruisseaux (Tapon, Rebouchet) — domaine public et parcelles',fill=(255,255,255,255),font=F(18,True))
d.text((10,34),'cadastre Etalab 2025 + fichier DGFiP des personnes morales ; communes : Saint-Maximin, Le Moutaret, Allevard, Pontcharra',fill=(255,255,255,255),font=f12)
y=H-24*len(LG)-10;d.rectangle([8,y-6,420,H-6],fill=(0,0,0,170))
for col,t in LG:
  d.rectangle([14,y+2,34,y+16],fill=col+(255,));d.text((42,y),t,fill=(255,255,255,255),font=f12);y+=22
sb=Q(x1-260,y0+25);d.line([sb,(sb[0]+200*S,sb[1])],fill=(255,255,255,255),width=4);d.text((sb[0],sb[1]-20),'200 m',fill=(255,255,255,255),font=f12)
nx=Q(x1-40,y1-30);d.line([nx,(nx[0],nx[1]-40)],fill=(255,255,255,255),width=3);d.text((nx[0]-5,nx[1]-58),'N',fill=(255,255,255,255),font=f14)
im.convert('RGB').save('t91_carte_tireloup_public.jpg',quality=88)
print('ok',W,H)
