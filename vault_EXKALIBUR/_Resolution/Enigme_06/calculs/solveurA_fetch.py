import urllib.request, json, sys
sys.stdout.reconfigure(encoding='utf-8')
u='https://geo.api.gouv.fr/communes?fields=nom,centre,population&format=json&geometry=centre'
data=json.load(urllib.request.urlopen(u,timeout=120))
out=[(c['nom'],c['centre']['coordinates'][1],c['centre']['coordinates'][0],c.get('population',0)) for c in data if c.get('centre')]
json.dump(out,open('communes.json','w',encoding='utf-8'),ensure_ascii=False)
print(len(out), sum(1 for o in out if o[0].upper().startswith('C')))
