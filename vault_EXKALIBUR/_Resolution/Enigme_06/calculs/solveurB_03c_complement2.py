"""Solveur B / É6 — complément 2 de géocodage (Conques, Carnac, Château-Gaillard, Cîteaux… titres Wikipedia alternatifs)."""
import sys
sys.path.insert(0, "."); from solveurB_geo import *
for lang, tl in (("en", ["Conques-en-Rouergue", "Conques, Aveyron", "Carnac", "Carnac stones", "Temple Church", "Cambridge", "Château Gaillard"]),
                 ("fr", ["Conques-en-Rouergue", "Abbatiale Sainte-Foy de Conques", "Château Gaillard", "Camlann", "Abbaye de Cadouin", "Temple de Paris", "Commanderie de Cressing Temple"])):
    r = wiki_coords(tl, lang)
    for k, v in r.items(): print(lang, k, v)
