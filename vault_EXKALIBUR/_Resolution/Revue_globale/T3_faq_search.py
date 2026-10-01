import sys,json,re
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
items=faq()
print(len(items),type(items))
kw=sys.argv[1:]
for it in items:
    t=(it.get('q','')+' '+str(it.get('a','')))
    if any(re.search(k,t,re.I) for k in kw):
        print(it.get('ref'),'|',it.get('theme'),'|Q:',it['q'][:200],'|A:',str(it['a'])[:250])
