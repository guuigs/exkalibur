"""T1_run1 : phrases Pater x parcours x sous-ensembles -> noms en C (anagramme exacte, 1 nom) + test du hasard."""
import sys, time, json
sys.path.insert(0, ".")
from T1_lib import *
t0 = time.time()
sets = load_names()
print({k: len(v) for k, v in sets.items()}, f"{time.time()-t0:.0f}s")
HS = name_hash_sets(sets, minlen=6)
HARR = {k: np.array(sorted(v.keys()), np.int64) for k, v in HS.items()}
print({k: len(v) for k, v in HS.items()})

PHRASES = {
 "lat_full": "Pater noster qui es in caelis",
 "lat_coelis": "Pater noster qui es in coelis",
 "lat_celis": "Pater noster qui es in celis",
 "lat_court": "Pater noster",
 "lat_pater_caelis": "Pater caelis",
 "lat_sanct": "Pater noster qui es in caelis sanctificetur nomen tuum",
 "lat_sanct2": "Pater noster qui es in caelis sanctificetur",
 "lat_long": "Pater noster qui es in caelis sanctificetur nomen tuum adveniat regnum tuum fiat voluntas tua sicut in caelo et in terra",
 "fr_es": "Notre Père qui es aux cieux",
 "fr_etes": "Notre Père qui êtes aux cieux",
 "fr_court": "Père cieux",
 "fr_long": "Notre Père qui es aux cieux que ton nom soit sanctifié",
 "en_which": "Our Father which art in heaven",
 "en_who": "Our Father who art in heaven",
 "en_hallowed": "Our Father which art in heaven hallowed be thy name",
 "es": "Padre nuestro que estás en el cielo",
 "it": "Padre nostro che sei nei cieli",
 "pt": "Pai nosso que estais nos céus",
 "en_father_heaven": "Father heaven",
 "cy": "Ein Tad yr hwn wyt yn y nefoedd",
 "br": "Hor Tad edod en env",
}
TRAV = all_traversals()
TN1 = list(TRAV.keys())
T2 = tier2_traversals()
ORD = [TRAV[k] for k in TN1] + T2
NAMES = TN1 + [f"t2_{i}" for i in range(len(T2))]
P = order_to_pos(ORD)          # (T,24)
NT1 = len(TN1)
print("parcours", len(ORD), "tier1", NT1)

def windows(letters):
    n = len(letters)
    if n <= 24: return [(0, letters)]
    return [(s, letters[s:s+24]) for s in range(0, n - 23)]

def run(R, Bi, Bp, phrases, want_hits=False, tiers=(True, False)):
    """retourne compteur {set: nb combos hit}, et liste hits"""
    subs = subsets(R, Bi, Bp)
    cnt = {k: 0 for k in HARR}; hits = []
    for pn, ph in phrases.items():
        L = norm(ph)
        for ws, w in windows(L):
            n = len(w)
            hl = np.zeros(24, np.int64); hl[:n] = hletters(w)
            valid = np.zeros(24, bool); valid[:n] = True
            # pour la cellule c du parcours t : lettre index P[t,c]
            HC = np.where(P < n, hl[np.minimum(P, 23)], 0)      # (T,24) hash de la lettre de chaque case
            LC = P  # position
            for sn, (m, s, t) in subs.items():
                size = int(m.sum()) + s + t
                if size < 6: continue
                mm = m.astype(bool)
                # sous-ensemble utilisable : toutes les cases masquées doivent avoir P<n
                ok = (P[:, mm] < n).all(1)
                if not ok.any(): continue
                hsum = (HC * m).sum(1)
                extra = 0
                lets = []
                if s: extra += int(HL[ord("S") - 65])
                if t: extra += int(HL[ord("T") - 65])
                hs = hsum + np.int64(extra)
                for k, arr in HARR.items():
                    sel = ok & np.isin(hs, arr)
                    if not tiers[1]: sel[NT1:] = False
                    if sel.any():
                        idxs = np.nonzero(sel)[0]
                        cnt[k] += len(idxs)
                        if want_hits:
                            for i in idxs[:50]:
                                hits.append((k, pn, ws, sn, NAMES[i], [d for _, d in HS[k][int(hs[i])]][:3]))
    return cnt, hits

R, Bi, Bp = board_masks()
cnt, hits = run(R, Bi, Bp, PHRASES, want_hits=True)
print("REEL comptes (combos hit) :", cnt, f"{time.time()-t0:.0f}s")
# hits distincts par nom
seen = {}
for k, pn, ws, sn, tn, dn in hits:
    seen.setdefault((k, tuple(dn)), []).append((pn, ws, sn, tn))
print("hits distincts (set, noms) :", len(seen))
for (k, dn), v in sorted(seen.items(), key=lambda x: (x[0][0] != "curated", x[0][0] != "communes", x[0][0])):
    if k in ("curated", "latin"):
        print(k, dn, len(v), v[:3])
json.dump([(a, b, c, d, e, f) for a, b, c, d, e, f in hits], open("T1_run1_hits.json", "w"), ensure_ascii=False)

# HASARD : plateaux aléatoires
rs = np.random.default_rng(1)
NB = int(sys.argv[1]) if len(sys.argv) > 1 else 40
rows = []
for i in range(NB):
    perm = rs.permutation(24)
    Rr = np.zeros(24, np.int64); Rr[perm[:7]] = 1
    Bii = np.zeros(24, np.int64); Bii[perm[7:10]] = 1
    Bpp = np.zeros(24, np.int64); Bpp[perm[10:14]] = 1
    c, _ = run(Rr, Bii, Bpp, PHRASES)
    rows.append(c)
print("HASARD plateaux aléatoires x", NB)
for k in HARR:
    a = np.array([r[k] for r in rows])
    print(f"  {k:9s} réel={cnt[k]:5d}  hasard moy={a.mean():8.1f} sd={a.std():7.1f} min={a.min()} max={a.max()}  rang: {(a>=cnt[k]).sum()}/{NB} >= réel", flush=True)
print(f"total {time.time()-t0:.0f}s")
