# Techniques (reusable)

## Geodesy
- Coordinates: OSM Nominatim `https://nominatim.openstreetmap.org/search?format=json&limit=1&q=...`,
  User-Agent header required, ≤1 req/s (`time.sleep(1.1)`), cache in `coords.json`.
  If a query returns nothing, simplify it ("Urquhart Castle, Highland" worked where a longer
  locality string did not). Guard `None` before computing.
- Named sites (castles, stone circles, cathedrals): the Wikipedia API gives coordinates by stdlib
  urllib, no key: `en.wikipedia.org/w/api.php?action=query&prop=coordinates|extracts&explaintext=1&titles=<T>&format=json`
  (the extract also lists sub-monuments, counts and local names).
- **Homonym communes** (Chambord exists in Eure AND Loir-et-Cher): select by department code, never by
  name alone. A name lookup silently takes the first match and shifts distances by 100+ km.
- Haversine R = 6371.0088 km; initial bearing via atan2; great-circle intersection and cross-track
  distance via 3D unit vectors (cross products). Print km, bearing, and the value in each unit.
- Script docstring states method, coordinate source, and the hypothesis being tested.
- Run as `python script.py > script.out.txt 2>&1; echo EXIT $?` — piping through `tee` hides the
  real exit code.
- On Windows add `sys.stdout.reconfigure(encoding="utf-8")` (accents); Pyright flags it — harmless.

## Chain search (« relie N lieux, même distance ») + control
- Precompute the haversine distance matrix once. Never loop `itertools.permutations(places, 4)` over
  100+ places with haversine inside: it exceeds the 420 s tool timeout. Iterate the middle segment
  (b, c), prune the end points a and d by ratio or length bounds, and keep one direction per chain
  (`name[a] < name[d]`).
- Shape tests (« the 4 bells draw a U »): use segment ratios with ±20 % and turn angles from a local
  equirectangular projection (atan2 of cross and dot products), same turn sign for a U.
- Control: count the chains within ±1 % for ~20 random D in the plausible range and print the sorted
  counts next to the real count. A real hit inside that spread is noise.
- Run long searches as `timeout 300 python x.py > x.out.txt 2>&1; echo EXIT $?`.

## Ring test (« go distance D toward X, you reach a place named … »)
- Candidate set: French communes with centroids (geo.api.gouv.fr `communes?fields=nom,centre,code`, cached as
  JSON). Keep those at D ± 1 % from the start, within a bearing window from the text (« vers l'Est » =
  45–135°), and matching the letter/name constraint. Print the whole list: its size is the null.
  A named target in that list proves nothing by itself. Promote it only if an independent clue picks it
  (e.g. labyrinth initial → Chartres among 29 C-communes).
- Lines that « cross » (garde × royaume): compute the great-circle intersection, check it lies on BOTH
  segments, and rerun the ring from the intersections of the alternative line readings. If the target
  survives only one reading, the result stands or falls with that reading, so say which one.
- Number × unit riddles (« multiplie… en mesure de pèlerin »): scan the plausible factors (e.g. petals
  5–24 × years 1–1400) × every historical unit, and report the share that lands ≤ 2 km of the target
  next to the real hit.

## Images (phone photos of parchments / illuminations; hand-drawn schemas)
- Copy originals to `_Resolution/Sources/`. Work from ONE base coordinate convention (e.g. the photo's
  960×1280) and crop zone by zone with PIL (LANCZOS ×2–4 for small zones) into scratch. One zone per
  `vision_analyze` call, strict « inventaire, sans interpréter » question.
- **Keep each crop ≤ ~800 px on its longest side**: the vision pipeline silently downscales larger images
  (a 756×1689 three-zone montage arrived halved and unreadable) — never send montages; view zones in
  separate calls.
- Map coordinates back before reusing them: `base = box_origin + crop_coord / zoom`; if a reply is marked
  « downscaled from W to w », multiply its coordinates by W/w first. Report each glyph's final position
  (base coords or %) to the owner so he can verify on the object.
- Ambiguous fine marks (a stroke next to a digit may be a radical, not a fleck; cursive R vs P; tiny
  figures): never settle from a single read — re-crop tighter, cross-check the known colours/positions
  from the official FAQ, park as « incertain » until confirmed.
- A hand-drawn schema from the owner is first-class data (his observations of the original): crop its
  quadrants at ~1.6–1.8×, transcribe every stone/square/letter into a coordinates map, post the
  reconstruction back (« dis-moi si j'ai bon ») and file it in the synthesis. His annotations override
  photo-based readings.

## Decode sanity checks
- Index ciphers (n.m = item n, letter m): test spaces counted vs ignored; the attested-word variant
  wins. Use name lists in the source object's original spelling (e.g. Wikipedia "Round Table"
  lists the Winchester table spellings).
- Constant-digit ciphers (π decimals): run the identical rule on e and √2 as controls.
- Anagram pools: compare `collections.Counter`s in code, never by eye. « Word X is formable from the letters » is
  weak evidence alone: run the same test on ~300 random same-length windows of French text and report the share (a
  vowel-rich pool lets thousands of words through). For « letters → word square », search exhaustively with
  prefix-pruned backtracking over a word list pre-filtered by the pool (symmetric squares finish in seconds;
  unrestricted double squares need a time cap).
- Board or grid → letters (fill a phrase along a traversal, read the letters under the tokens): test many
  traversals × phrases, then run the identical pipeline on randomly placed tokens. Report real vs
  mean ± sd; only a clear outlier counts.

## Terrain data for a final zone (France, public, no key)
- **IGN BD TOPO v3 WFS**: `https://data.geopf.fr/wfs/ows?SERVICE=WFS&VERSION=2.0.0&REQUEST=GetFeature&TYPENAMES=BDTOPO_V3:<layer>&OUTPUTFORMAT=application/json&SRSNAME=EPSG:4326&COUNT=5000&STARTINDEX=<n>&BBOX=<latmin>,<lonmin>,<latmax>,<lonmax>,urn:ogc:def:crs:EPSG::4326`
  (page by STARTINDEX while a page returns 5000). Useful layers: `troncon_de_route` (field `nature`:
  Sentier / Chemin / Route empierrée), `troncon_hydrographique` (`sens_de_l_ecoulement`,
  `cpx_toponyme_de_cours_d_eau`), `cours_d_eau`, `plan_d_eau`, `surface_hydrographique`,
  `detail_hydrographique` (sources, fountains), `detail_orographique`, `zone_de_vegetation`, `foret_publique`,
  `construction_ponctuelle` (crosses, bell towers), `toponymie` (field `graphie_du_toponyme`),
  `lieu_dit_non_habite`. List all layers with `REQUEST=GetCapabilities`.
- Altitude: single point via `.../elevation.json?lon=..&lat=..&resource=ign_rge_alti_wld`; a full segment in one
  call via `.../elevationLine.json?lon=<l1|l2|…>&lat=<la1|…>&resource=ign_rge_alti_wld&delimiter=|` (~64 samples
  for 6 km). Visibility test: apparent angle of each sample from the observer (first sample z + real observer
  height — tower terrace, rampart) vs the target's angle; any sample above it masks the target. Terrain only
  (no trees/buildings): a pass is optimistic, a fail is decisive — it eliminated a candidate cascade 5.7 km out
  (1 111 m ridge at 2.9 km).
- **Stitched raster grid (numpy MNT): fix the axis convention BEFORE any analysis.** Sample a known FLAT
  feature — a reservoir, pond or river polygon from `surface_hydrographique`, several dozen vertices — under
  both `row0 = north` and `row0 = south`, and keep the convention with the smallest elevation spread (≤ 2 m vs
  20-30 m). Single-point checks (a station, a river bend) are ambiguous and can point the wrong way; a water
  polygon is decisive. A mirrored grid silently returns plausible-looking garbage for every distance, bearing
  and viewshed.
- **Full viewshed mask** (save it with `np.save`, the run costs 1-2 min): for every azimuth (0.25° step) walk
  the ray at the grid step, take the elevation angle of each sample relative to the observer and mark a cell
  visible when its angle ≥ the running maximum (`np.maximum.accumulate`) of the samples before it. Run it at
  BOTH observer heights — ground + 1.7 m and vantage (+ 25-30 m for a tower, terrace or rampart): a 4 m bump
  50 m away hides a spot from the ground but not from the wall, so « on la voit depuis le rempart » flips on
  exactly this choice.
- Intersect the viewshed with the stream mask (LiDAR catchment ≥ ~2-5 ha **or** the vertices of
  `troncon_hydrographique`), label the connected components (`scipy.ndimage.label`), and rank the clusters of
  ≥ 4-6 cells by distance, bearing and elevation from the start, plus distance to the nearest NAMED junction
  and to the nearest building polygon. Visible water is rare — a valley-bottom stream is usually hidden, so
  expect a handful of clusters, and treat their count as the null.
- **Artificial ≠ natural water**: `troncon_hydrographique`'s `nature` separates `Ecoulement naturel` from
  `Canal`, `Conduit forcé` and `Conduit buse` (a hydro scheme's canal, penstock, culvert). When the text says
  « ruisseau / eaux », drop the artificial ones before reasoning. A `Conduit buse` is a culvert — the exact
  case of « l'eau s'écoule sous le chemin » — so use it as a marker of the crossing, not as the stream itself.
- **Clearings never come from the MNT** (LiDAR is bare-earth): take them from `zone_de_vegetation` /
  `foret_publique`, and ignore the `Haie` (hedge) and `Verger` polygons — they sit on every plot and make any
  « clearing » test pass 100 %.
- Street names: BAN `https://api-adresse.data.gouv.fr/search/?type=street&limit=20&q=<rue du X> <postcode>` returns a
  public street's centroid in one call; the local form finds streets a generic France-wide query never lists.
- Cadastral lieux-dits (finer names than BD TOPO): `https://cadastre.data.gouv.fr/bundler/cadastre-etalab/communes/<INSEE>/geojson/lieux_dits`.
- Historic basemaps, same WMS GetMap (`FORMAT=image/jpeg`): GetCapabilities once, grep the LAYER names —
  `GEOGRAPHICALGRIDSYSTEMS.ETATMAJOR10/40` (XIXe), `GEOGRAPHICALGRIDSYSTEMS.MAPS.SCAN50.1950`,
  `ORTHOIMAGERY.ORTHOPHOTOS.1950-1965`, `GEOGRAPHICALGRIDSYSTEMS.CASSINI`. Use `CRS=CRS:84` with
  `BBOX=lonmin,latmin,lonmax,latmax` to avoid the WMS 1.3.0 lat/lon axis order. Old sheets keep toponyms, hamlets
  and paths that modern layers dropped.
- OSM Overpass (`overpass-api.de/api/interpreter`, POST `data=`): send an `Accept: */*` header, otherwise
  HTTP 406. It often times out on large radii: keep ≤ 10 km or split. When the main instance and
  `overpass.kumi.systems` keep answering 406/000, the mirror `https://overpass.openstreetmap.fr/api/interpreter`
  (curl `--data-urlencode "data=<query>"`) returned full JSON: loop over the endpoints and stop at the first
  body containing `"elements"`. One-shot query for religious / roadside objects:
  `nwr["historic"~"wayside_cross|wayside_shrine|calvary|memorial"](around:4000,lat,lon);nwr["amenity"="place_of_worship"](around:4000,lat,lon);`.
  Wikimedia Commons `list=geosearch&gsnamespace=6&gsradius=2500` (geotagged photos) is a keyless cross-check
  for « does this object exist on the ground ».
- For one relation and all its members (routes, hiking node networks), the direct API is lighter than Overpass:
  `https://api.openstreetmap.org/api/0.6/relation/<id>/full.json` (`.../node/<id>.json` gives a node's full tags).
  « Réseaux de carrefours » (`network:type=node_network`) list named junctions — prime suspects for « la jonction
  des chemins » clues; compute junction-to-junction distances for claimed spacings.
- Cache everything as GeoJSON in scratch and share one helper file (hav, bearing, centroid, wfs, faq loader)
  with subagents by path.
- **Toponym hunts**: 3 000+ names sit within 6 km, so « roche » or « loup » hits are banal. Only a name
  that is independent of the chain (not already in the text) counts. The shape that IS discriminating is a
  **multi-noun name**: a lieu-dit or a junction whose name concatenates two or more independent nouns of the
  riddle (« le Chêne la Roche et le Vivier » for wood + rock + water) is rare enough to be a real lead. Cross
  the riddle's concrete nouns against the name lists, and weigh names that literally render a phrase of the
  text (« PIERRE GROS » for « la grande roche »). **Named junction nodes of a hiking network are first-class
  material**: a junction whose NAME matches a riddle noun is a prime candidate for « la jonction des chemins »,
  and its distance to the previous point is testable at once.
- **Shape of a lake vs an illustration**: IoU over rotations gives ~0.7 for any blob (the median of the
  null distribution). Report how many water bodies exceed the best score; a contour alone rarely discriminates.

## Sketch vs network (a drawn line = a stream?)
- Parse the SVG path into sub-paths; flip y (SVG y points down). Resample the main stem to ~64 points.
- Build a graph from BD TOPO hydro segments (skip buried conduits). At every confluence, for each
  upstream/downstream pair and ~25 lengths (150 m → 14 km, ×1.2 steps), walk the network and compare by
  Procrustes (similarity, proper rotation only).
- Control: rerun with the mirrored sketch. Equal best scores and equal quantiles mean no real match. The
  full scan over a 12 km box runs > 5 min: launch it in the background and wait on the process.
- Finer streams from **LiDAR HD** (IGN, public, no key): WMS `https://data.geopf.fr/wms-r` GetMap with
  `LAYERS=IGNF_LIDAR-HD_MNT_ELEVATION.ELEVATIONGRIDCOVERAGE.WGS84G`, `CRS=EPSG:4326`, `BBOX=latmin,lonmin,latmax,lonmax`,
  `FORMAT=image/x-bil;bits=32` → raw little-endian float32 grid. Fetch tiles of 1000 × 1000 px at 2 m and stitch.
  Fill depressions (priority-flood + epsilon) **before** D8 flow direction: a raw LiDAR MNT has countless
  micro-pits, so without filling the accumulation stays tiny and zero cells reach a stream threshold. Threshold
  ~2-5 ha of catchment. Save a hillshade with streams overlaid for the user: the relief reading (isolated
  hill, parallel valleys) is useful by itself.
- D8 paths are 8-direction staircases, so at a scale of a few hundred metres they cannot match a hand-drawn
  meander. When the author says the feature is seen only on site, one controlled desk test (BD TOPO, then LiDAR)
  is the ceiling: keep the sketch as a field-recognition aid rather than scanning further.

## Ordinals along a line (« les troisième et onzième »)
- Test ordered objects of one kind along a linear feature: k-th bridges, crosses or mills along one river,
  counted from the mouth AND from the source (project each object onto the river graph, distance to the mouth
  by Dijkstra over flow-directed segments, dedupe objects < 20 m apart). Check the pair (3, 11) against the
  distance window for every plausible unit value.
- Base rate: the share of ALL pairs (k, k+8) that fall in the window. A hit at that rate (~1-2 %) is noise.
- Same for unordered same-kind sets (sawmills, chapels): count pairs in the window over all pairs.

## Sun azimuth for dated directions (« ma boussole suivait le jour dernier »)
- Compute sunrise/sunset azimuth from solar declination at the site (horizon −0.833°), and validate on
  equinox/solstice values first.
- For pre-1582 dates, compute both the Julian date and the proleptic Gregorian one: they differ by about
  4° in spring. An author using an online tool with the historical date likely got the proleptic value.
  A compass reads magnetic north: note the local declination (~+2° in the French Alps).
- Test the date as the source of a known bearing too: count the days per year that fall within the
  tolerance, and the false-alarm rate for « at least one of the k dates tried ».

## Official FAQ harvesting
- If the organiser runs a searchable FAQ page, scrape it by many search terms into one JSON
  (`ref, theme, q, a`), dedupe on ref, and store it in `Communaute/`. Then write per-riddle extracts
  (`Enigme_XX/faq_eXX.md`) with regex over q+a, and a transverse extract for recurring objects.

## Rumour / published-solution search (Google via Firecrawl, browser_exec as fallback)
- Preferred: `terminal(command="firecrawl scrape 'https://www.google.com/search?hl=fr&num=20&udm=14&q=<quoted query>' -o .firecrawl/google.md")` then `read_file` — verified working, and Firecrawl follows the `google.com/goto` redirects itself. Skill: `firecrawl`.
- Fallback, only when Firecrawl is down: `browser_exec`. If it reports `chrome-not-running`, start Chrome yourself (see skill
  hermes-browser-exec-backend); the user clicks « Allow » once on the remote-debugging popup.
- URL: `https://www.google.com/search?hl=fr&num=20&udm=14&q=<quoted query>`. `udm=14` = « Web »
  results only, without the « Aperçu IA ». AI overview text is unsourced and never counts, even when it
  echoes your own hypothesis.
- Extract results in one `js()` call: `[...document.querySelectorAll('a h3')]` → h3 text + closest
  `div[data-hveid]` innerText (snippet). The hrefs are `google.com/goto?...` redirects: open them with
  `goto_url(href)` and read `document.body.innerText`.
- Public Facebook group posts indexed by Google open **without login**, comments included (cut the text
  at the cookie banner « Autoriser l… »). Find the group id once, then use
  `site:facebook.com/groups/<id> <mot>`.
- Batch 5-10 queries per batch (one Firecrawl scrape each — or `firecrawl search` for plain queries; keep ~1.5 s apart on the browser fallback); archive the conclusion in
  `Communaute/recherche_solutions_<date>.md` (source / access / useful content, leads as [RUMEUR]).

## Web research fallback (no browser)
For official pages and press, a stdlib urllib fetcher (strip script/style, unescape) or `curl` with a
desktop User-Agent is enough; YouTube search result pages also parse via curl. Scripted search engines
(DuckDuckGo HTML, Bing, Brave, Qwant lite, Mojeek) often return empty or 403/429 pages: do not read an
empty result as « nothing exists ». Keep helper scripts in scratch and pass their paths to subagents.
