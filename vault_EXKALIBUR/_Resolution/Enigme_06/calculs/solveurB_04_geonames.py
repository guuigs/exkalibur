"""Solveur B / É6 — télécharge geonames cities15000 (villes > 15 000 hab., tous pays) -> solveurB_cities15000.tsv (source: download.geonames.org, CC-BY)."""
import urllib.request, zipfile, io, sys
sys.stdout.reconfigure(encoding="utf-8")
try:
    data = urllib.request.urlopen(urllib.request.Request("https://download.geonames.org/export/dump/cities15000.zip", headers={"User-Agent": "hermes-solveurB/1.0"}), timeout=90).read()
    z = zipfile.ZipFile(io.BytesIO(data)); txt = z.read("cities15000.txt").decode("utf-8")
    open("solveurB_cities15000.tsv", "w", encoding="utf-8").write(txt)
    print("OK lignes", txt.count("\n"))
except Exception as e:
    print("ECHEC", e)
