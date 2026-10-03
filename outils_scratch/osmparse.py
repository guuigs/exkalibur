import xml.etree.ElementTree as ET, math, json, glob
nodes={};ways=[];pois=[]
for f in glob.glob('osm_*.xml'):
    for ev,el in ET.iterparse(f):
        if el.tag=='node':
            nodes[el.get('id')]=(float(el.get('lat')),float(el.get('lon')))
            t={c.get('k'):c.get('v') for c in el.findall('tag')}
            if t: pois.append((el.get('id'),nodes[el.get('id')],t))
        elif el.tag=='way':
            t={c.get('k'):c.get('v') for c in el.findall('tag')}
            ways.append((el.get('id'),[n.get('ref') for n in el.findall('nd')],t))
        if el.tag in('node','way','relation'): el.clear()
json.dump({'nodes':nodes,'ways':ways,'pois':pois},open('osm.json','w'))
print(len(nodes),len(ways),len(pois))
