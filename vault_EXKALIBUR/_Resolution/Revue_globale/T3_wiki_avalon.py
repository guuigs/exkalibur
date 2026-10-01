import json,re,urllib.parse
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
def ext(lang,title,n=2500,intro=True):
    u=f'https://{lang}.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&redirects=1&titles='+urllib.parse.quote(title)+('&exintro=1' if intro else '')
    j=json.loads(get(u)); p=list(j['query']['pages'].values())[0]; return p.get('extract','')[:n]
for lang,t in (('fr','Hugues d\'Avalon'),('fr','Château d\'Avalon'),('fr','Tour d\'Avalon'),('en','Hugh of Avalon')):
    print('=====',lang,t); 
    try: print(ext(lang,t,1800))
    except Exception as e: print('ERR',e)
print('===== Bayard mort/ Rebec / arquebuse')
t=ext('fr','Pierre Terrail de Bayard',60000,False)
for k in ('30 avril','Sesia|Rebec|Robecco','arquebus','Bourbon','fille|descend','pitié','1476|naissance','Marignan|adoub','statue','rue '):
    for m in list(re.finditer(k,t))[:2]:
        print(f'[{k}]',t[max(0,m.start()-150):m.end()+220].replace('\n',' '))
