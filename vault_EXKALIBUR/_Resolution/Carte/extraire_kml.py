"""Extrait les objets de la carte My Maps de Guilhem (KML) : points, lignes, polygones, avec dossiers et descriptions."""
import sys, re, xml.etree.ElementTree as ET, json, os
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ns = {"k": "http://www.opengis.net/kml/2.2"}
root = ET.parse(os.path.join(HERE, "carte_guilhem_mymaps.kml")).getroot()
out = []
def walk(node, path):
    for ch in node:
        tag = ch.tag.split("}")[1]
        if tag == "Folder":
            walk(ch, path + [ch.findtext("k:name", "", ns)])
        elif tag == "Placemark":
            name = ch.findtext("k:name", "", ns).strip()
            desc = re.sub("<[^>]+>", " ", ch.findtext("k:description", "", ns) or "").strip()
            for g in ("Point", "LineString", "Polygon"):
                e = ch.find(f".//k:{g}", ns)
                if e is not None:
                    coords = [tuple(map(float, c.split(",")[:2])) for c in e.find(".//k:coordinates", ns).text.split()]
                    out.append({"folder": "/".join(path), "name": name, "type": g, "desc": desc,
                                "coords_lonlat": coords})
        elif tag == "Document":
            walk(ch, path)
walk(root, [])
json.dump(out, open(os.path.join(HERE, "carte_guilhem_objets.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for o in out:
    c = o["coords_lonlat"]
    s = f"{c[0][1]:.5f},{c[0][0]:.5f}" if o["type"] == "Point" else f"{len(c)} pts: " + " -> ".join(f"({p[1]:.4f},{p[0]:.4f})" for p in c[:6])
    print(f"[{o['folder']}] {o['type']:10s} {o['name']!r}: {s}" + (f"  | desc: {o['desc'][:120]}" if o["desc"] else ""))
print(len(out), "objets")
