---
name: puzzle-hunt-solving
description: "Use when solving treasure-hunt enigmas. Verified, filed."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Enigmes, Chasse au tresor, Puzzle, Geographie, Cryptographie, Obsidian, Exkalibur]
    related_skills: [obsidian, grounded-citations]
---

# Puzzle-hunt solving (chasses au trésor, énigmes)

Long multi-session projects where Guilhem has already worked on some riddles in his Obsidian vault.
The deliverable is **verified** solutions, not seductive ones. Designers plant traps for AI users,
so every "eureka" must survive a hostile verifier.

## When to Use
Treasure hunts, armchair enigmas, riddle chains with texts + illustrations + maps (e.g. Exkalibur),
especially multi-session work resuming from files in the vault.

## Standing rules (Guilhem's protocol)
- Guilhem's notes are **READ-ONLY**. All work goes in `<projet>/_Resolution/`.
- Never invent the content of a riddle. Missing text/image/map → stop and say exactly what is missing.
- Separate **fait / hypothèse / intuition** with a confidence level; cite sources; prefer
  "pas encore trouvé" to a fragile answer.
- Riddle N+1 is not validated before N. **Wait for Guilhem's confirmation after each validated riddle**
  (his standing choice); otherwise come back only for questions you can't answer or critical choices.
  **Autonomy mode overrides both**: when he grants autonomy and says not to come back before the conclusion,
  stop asking (no `clarify`, no photo requests, no « dis-moi si j'ai bon ») — keep working from the material
  already in the vault, and hold every question for the single closing reply.
- Community theories (Discord, forums) are allowed **as hypotheses only**, tagged [COMMUNAUTÉ] vs [OFFICIEL].
- **Organic reasoning (user requirement)**: keep one `GRAPHE_INDICES.md` for the whole hunt: cross-riddle
  threads, each riddle's inputs → outputs, rejected leads with reasons. Check each candidate with a 3-question
  filter: (a) contradicts the official FAQ? (b) contradicts an acquired node? (c) explains ≥ 2 independent
  elements? List the elements a solution does NOT consume: they feed later riddles.
- **Shark order of operations**: for each riddle, search its community channel (official Discord) and
  recompute the consensus by script BEFORE fanning out solver agents. Riddles already solved by the
  community are settled in minutes that way, whereas blind solver waves cost hours of budget.
- **Consensus weight falls on late riddles (Guilhem: « ne prends rien pour acquis »)**: the further into
  the hunt, the more the community guesses. For those riddles, use the Discord only to list candidate
  readings. Then (a) recompute the tracé yourself from acquired nodes, (b) enumerate EVERY candidate the
  rule allows (e.g. all C-named communes in the distance ring, see `references/techniques.md`), (c) keep a
  candidate only if an independent clue picks it out of that list (lettrine, text word), (d) control with
  the alternative readings of each line or term. Split the riddle into its **tracé part** (can reach 🟡)
  and its **narrative part** (narrator, dates, which the FAQ may say do not affect the tracé): mark the
  latter « ouvert » with the pistes, rather than adopting the dominant community story. The same goes for
  under-specified sub-steps (« compte-les », « mesure… »): list the candidate values, mark them ouvert, and
  let a later riddle pick one.
- **Every equation « term = earlier element » ships with its derivation** (Guilhem asks « comment on
  l'explique dans le lore ? » otherwise). Give three things in the solution file and in the reply:
  (1) every occurrence of the term across ALL the hunt's texts and the author's FAQ answers (grep them);
  (2) the lore or history link;
  (3) the fragile points (unanswered FAQ questions, other readings).
  Also run a **variant calculation** that drops the equation (other readings of the term) and report what
  emerges. Word it honestly: such a control only rules out the variants you tested, so « renforcée » is
  too strong when the target was in your candidate list from the start.
- **Mode « shark agressif »** (Guilhem's standing choice): if a resolution is **officially validated**
  (author, official FAQ, organiser), take it and move on, with no re-derivation. **Rumours of validation** go
  in `hypotheses.md` as approach leads, tagged [RUMEUR], never as facts. Riddles Guilhem declares
  « acquises » are facts: do not re-verify them.
- Subagents: Sonnet 5.5 first (`delegation.*`), auto-switch to DeepSeek at 90 % usage (skill
  subagent-model-guard). Check `hermes config get delegation.model` before a heavy batch.
- No action outside read/write in the project folder + web research without his OK.
- Replies: French, compact tables, lead with what is confirmed / what to fix; ask decisions with one
  `clarify` call holding several questions. Close with the ≤3 checks only he can run on the physical
  original (panel, stone, sketch) — his eye on the object outranks any photo read.
- **Recap note in the vault (standing deliverable)**: `<projet>/00 - Solutions validées.md` (project root,
  so Obsidian shows it): per riddle, the **full base text** as a quote + a **TL;DR** of the resolution;
  summary table on top; riddles not yet confirmed marked 🟡 « probable, à confirmer ». Update it at each
  validation. Text source order: HD photos → `releve.md` → web / Discord channel of the riddle → only then
  ask Guilhem for new photos. Never paste his partial notes as the text.
- **Own map (standing deliverable)**: keep `_Resolution/Carte/<hunt>_traces_valides.kml` (importable in
  Google My Maps: every validated point and line, tagged per riddle, `[probable]` when unconfirmed) +
  an SVG sketch for Obsidian, regenerated from the KML by a script kept next to it (`Carte/gen_svg.py`,
  dashed = probable) so the two never drift. Add each riddle's tracé as soon as it is computed; geometric links between
  riddles (parallel guard, shared endpoints) show up on the map before they show up in text.

## File harness (state lives in files, not context)
```
_Resolution/
  00_ETAT.md            tableau de bord — READ FIRST on resume; update before/after each long step
  01_Contexte.md        règlement, infos officielles, sources ([OFF]/[PRESSE]/[NON-OFF])
  02_Audit.md           audit of Guilhem's pistes: solide/plausible/fragile/invalidée + raison
  02_Audit_calculs/     scripts + .out.txt + coords.json cache
  03_Correspondance_illustrations.md   (when texts and illustrations are shuffled)
  Enigme_XX/ releve.md, hypotheses.md, calculs/, solution.md, verification.md, solveur_notes.md
  Journal.md            timestamped decisions / changes of course
  Pistes_transverses.md recurring symbols/places/units across riddles
  Sources/              original photos only
  Communaute/           veille files
```
Keep heavy derived images (zoom crops, tens of MB) in the Hermes scratch dir, **not** the vault — the
vault is git-synced to the VPS every 5 min. Only small per-riddle crops go in `Enigme_XX/`.

## Procedure
1. **Phase 0 — cadrage, then STOP for validation**: official rules/FAQ (organiser site first), form of
   the final answer, allowed countries, author interviews in the press; inventory; audit each existing
   piste **with code** (a quick check often upgrades or kills a piste); report + plan + `clarify` for
   decisions (community yes/no, map available?, checkpoint mode, starting point).
2. **Relevé** per riddle: exact transcription from the photo (the user's notes are often partial —
   re-transcribe the full text), anomalies (capitals, odd spellings, the only number, cardinal points
   present/absent), illustration zone by zone. Pure observation.
3. **Hypothèses**: ≥3 live pistes, registre with a written reason for each abandon.
4. **Calculs**: always by script, archived with output. See `references/techniques.md`.
5. **Solution candidate**: full chain, role of every relevé element.
6. **Vérification**: a *separate* subagent with fresh context gets riddle + relevé + solution, NOT
   `solveur_notes.md`. Criteria: couverture, pas d'ad hoc, test du hasard, unicité, cohérence,
   plausibilité de conception. Verdict VALIDÉE / PROBABLE (manque X) / REJETÉE.
7. **Blocage** after ~5 cycles: status BLOQUÉE, document tested/rejected/missing, propose angles.
8. **Final zone / terrain phase** (once the chain lands on a small area): pull public terrain data for a
   ~5-12 km box (France: IGN BD TOPO WFS, altimetry, cadastre lieux-dits; recipe in
   `references/techniques.md`). Guilhem expects IGN/Géoportail to be used for paths, streams and clearings.
   Turn each text element into a filter (clearing = path junction in a gap in the forest, stream ≤ 150 m, public
   forest, line of sight from the start point, east-facing slope) and print how many candidates pass each
   filter and each combination. That count is the null. Filters that pass 25-50 % of junctions tell you nothing.
   BD TOPO misses small clearings and short streams, so when nothing passes, say that the desk ceiling is
   reached. Then propose LiDAR HD / orthophoto or a field-visit prep, not a forced candidate.
   When the stake is water (« eaux », « ruisseau », « l'eau s'écoule sous le chemin ») or « visible depuis le
   départ », move to the stitched LiDAR grid and compute a real viewshed + visible-stream clusters rather than
   judging the line of sight from the map (recipes and the orientation trap in `references/techniques.md`).
   The surviving clusters are the shortlist.
- **Closing a final zone that will not close**: never hand over one unhedged point. Deliver a ranked shortlist
  — per candidate a 50 m box (lat/lon bounds + centre + map link), a confidence level, the text element that would
  confirm it, and an on-site protocol in order (what to look at, from where, at which hour). **Before sending,
  audit the shortlist**: (1) every phrase you attribute to the riddle text must be found verbatim in the base
  text (grep it), because a paraphrase slipped in as a quote invalidates the whole argument; (2) for every
  FAQ item, check whether your wording sits in the player's QUESTION or the author's ANSWER: an answer like
  « folie ou génie » validates nothing; (3) a candidate built on a place-name coincidence (lieu-dit with
  oak/rock/pond words) needs an independent clue, and must pass the author's hard constraints (e.g. distance to
  buildings) — test that in code; (4) give percentages only when they come from a count or control, otherwise
  say « moyenne / faible ». If a later critique retracts the shortlist, write the retractions into the riddle's
  `solution.md` so the next session does not revive it. Say plainly which
  sub-step is still unidentified and what only he can unblock (physical panel check, Discord channel access,
  a field visit). A labelled 45 % candidate beats a confident invention.
- Load the vault's texts + FAQ slices with the analysis script itself (`open(p, encoding="utf-8").read()`
  inside one `execute_code` call, several files per call) instead of one read per turn: the text then sits in
  the same context as the numbers it must explain, and a harness that returns only a « read <path> (N chars) »
  stub for a file cannot silently cost you its content.
9. **Global review after the last riddle** (Guilhem asks to revisit every zone d'ombre with the whole picture):
   write `Revue_globale/BRIEF_sous_agents.md` and fan out three agents: terrain/IGN, the unsolved final step,
   and the zones d'ombre of the earlier riddles. The orchestrator keeps the final illustration, the Discord
   and the synthesis (`Revue_globale/00_SYNTHESE.md`: a before/after table per point). Re-read the late
   illustrations at full HD and cross them with EARLY riddles: late clues often confirm an early unused lead.

### Delegation pattern
Guilhem's standing choice: **one riddle = a sub-team**. The orchestrator writes `Enigme_XX/BRIEF_sous_agents.md`
(exact text, relevé, official constraints, what is already done or ruled out, rules, budget), then fans out
4 to 6 Sonnet agents with **distinct angles**: mechanism/cipher, iconography HD, history/theme, geometry,
rumours + transverse FAQ. Each agent uses its own file prefix (`T1_` …) and notes file, has a ~40-call budget, and
returns a 12-line summary. Check `subagent_model_guard.py --status` before each fan-out; above ~70 %, use
fewer agents. Then synthesise and run the verifier (fresh context, no solver notes).

### Persistence against usage limits (Guilhem's hard rule)
The 5-hour Claude limit WILL cut sessions mid-work; subagent context is lost unless it is on disk.
- Put a **« Sauvegarde continue »** section in every BRIEF: create `<prefix>_notes.md` on the first call and
  update it after **each** piste, with a `## REPRISE` header (Fait / En cours / Prochaines étapes / Écarté).
  If the file already exists, the agent is a resume: read REPRISE, skip what is done.
- The orchestrator writes `Enigme_XX/REPRISE.md` (agents × angle × notes file × prefix + resume
  procedure) **before** ending the turn after a fan-out, and points to it from `00_ETAT.md`.
- If agents are already running without the rule, `steer` each one immediately (they get it on their next tool result).
- On resume: relaunch only the unfinished angles, with the context « Lis BRIEF puis Tn_notes.md ; tu es une REPRISE ».
- If a fan-out dies within seconds (user interrupt, Esc), relaunch the same angles as REPRISE right away:
  the notes files already exist, and an agent whose notes say TERMINÉ just re-reads its report and returns.
  If the brief used per-task **output dirs** instead of notes files, harvest them (and the batch's `live/`
  transcripts) into the vault first, then relaunch with « lis d'abord tes fichiers existants — tu reprends, ne
  recommence pas ». Tell Guilhem where the recovered work now lives: he follows the agents in the chat and
  worries when they seem to vanish.
- Steer only goes to agents that are still live (`action=list` first); an agent that already finished
  returns an error, so fold that lead into your own work or into a new small wave.

### Waves, not one big batch
- After a wave returns: write a « Synthèse vague N » table in `hypotheses.md` (piste / result / statut),
  update `REPRISE.md` + `Journal.md`, **then** launch a smaller wave (2-3 agents) aimed only at the new
  leads. Size each wave from `--status`: past ~50 % of the 5-hour window, use 2 agents and do cheap
  tests yourself.
- Background-process completion notices from subagents need no action: reply in one line and wait.
- If a detail is unreadable (tokens, tiny figures ≈ 40 px), ask Guilhem for a **macro photo** at once
  rather than spending agent budget on guessing; mark the angle « bloqué : source ».
- User photo drops may arrive as a zip in `Downloads` even when he gives a folder path: search
  `Downloads` for the name, extract to `Sources/<lot>/` + `INDEX.md` (file → content), and make contact
  sheets in scratch to sort them.

## Pitfalls
- **Test the method on a control input** before believing a decode: the same rule applied to other
  constants or random text must give garbage — that is the "test du hasard" in code.
- **Distances: check the unit before the place.** Try every historical unit (lieue commune 4.444,
  Paris/poste 3.898, gauloise 2.222, marine 5.556 km; mille romain 1.4786 km). A <1 % match with a
  period-appropriate unit is strong; having to shop for a unit is ad hoc.
- Geocode the **historical site**, not the modern namesake town (battlefield ≠ town of the same name).
- **« Visible à l'œil nu depuis X » is a testable claim**: run an altimetry profile along the segment before
  adopting (or defending) a distant landmark — a 1 100 m ridge 3 km out hides a target 6 km out (recipe in
  `references/techniques.md`). Eliminate, or keep with the tested reason written down.
- **Ordinals in a source (« le 10e père », « le 3e roi »): count in the primary text itself** (prologue,
  charter, chronicle), not in an encyclopedia list, whose order often differs. If you only have a
  translation, say so, because the whole letter or place rests on that order.
- **Saints and figures on an illumination: identify them by their attribute** (saw = Simon the Zealot,
  keys = Peter, swan = Hugh of Lincoln…), then check ordinal lists that contain them (apostle lists differ:
  Mt 10 / Mc 3 / Lc 6). A « lone Christ at table, incomplete scene » means the missing figures are placed
  elsewhere. Rotate phone photos so the sky is up before any vision pass: sideways crops get misread, and hand-held
  shots of panels often arrive **flipped 180°** (the tell: a banderole or inscription that reads upside-down) —
  fix the orientation and re-crop before reading any sign.
- **Guilhem's own convictions and sketches (SVG of a scratch, a river-like line, « maybe a sawmill »)**: he
  wants you to test them yourself, not just discuss them. First grep the FAQ for what may vary (orientation,
  position). Then test by script against the zone's data with a control (mirror for shapes, base rate for
  distances; `references/techniques.md`). Report the null result plainly but keep the lead alive when the data
  is coarser than the clue (the sketch becomes a field-recognition aid). Record his validations (a date, a
  reading) as facts in the recap and project note at once.
- **The physical material is his, the pixels are yours**: give the owner the exact position (base-image
  coords or % width/height) of every glyph you report from a photo so he can check it on the object; when
  a mark's status is unclear, ask ONE decisive check (same paint/ink as its neighbours — deliberate or
  artifact?). When he corrects a reading, his observation wins: append the correction to the synthesis file
  immediately, lead the next reply with it, and re-anchor hypotheses instead of defending the old read.
- **A unique mark inside a parallel series** (one radical among four identical digits, one letter unlike
  its twins) is a lead, not a result: file it as a variant under surveillance with the check that would
  settle it, build nothing on it, and state plainly that the mainline reading is unaffected. Authors plant
  « des choses à corriger »: a lone anomaly is as likely a deliberate trap or correction target as a clue.
- **Banners, mottos and heraldry on an illumination are cryptos**: search the motto, find the family or
  clan it belongs to, then their seat (e.g. a clan motto leads to that clan's castle). Wikipedia pages of
  clans and castles state it.
- Grammar is a clue: a feminine ("ma septième, épopée") points to a work, not an author; titles have
  dates (Octave before "Auguste"). Re-check charade answers against the acrostic they should produce.
- Letter grids with holes: test known squares (SATOR) and use the missing letters as an anagram pool;
  check the observed marks against the square's skeleton (five-letter words, the four R positions
  (1,5)(2,2)(4,4)(5,1), the middle cell) before hunting exotic variants.
- Illustrations shuffled vs texts: pair by **specific** discriminators (inscriptions, grids, named
  monuments), not generic theme; record any ordering structure found.
- Without the official map, flag every geometric result that depends on projection.
- **Official author FAQs are gold**: harvest them exhaustively first (script + JSON in `Communaute/`),
  then grep per riddle **and re-grep the whole corpus after every new hypothesis** (query the words of the
  theory, not the riddle title). Author answers constrain mechanisms ("anagrammes parfaites", "même distance
  QUE", "ordre évident") and settle readings faster than any solver. Quote the **full verbatim** in the notes,
  and keep the dodges (NRP, « très bonne question », « je ne pourrais pas répondre ») as entries too: a dodge
  marks a live question and narrows the mechanism by what the author declines to deny.
- **Author's illumination numbering ≠ riddle numbering**: the author numbers panels in reading order;
  map FAQ "enluminure N" to the panel before using it (Exkalibur: plateau de jeu = enl. 7 → É6).
- **Grep the author FAQ by concrete words, not just by riddle tags**: playful answers under unrelated
  tags carry real hints (e.g. « non, mais vous pouvez sûrement boire à chaque fois » about the C
  places). Search nouns/verbs of the text and image (boire, pomme, cloche, casque…) across the whole base.
- **When the user says the crux is unidentified, do not stop at « je ne peux pas »**: the unknown (e.g. the
  3rd/11th elements) is exactly where he wants creativity. Build structured hypotheses from the hunt's OWN
  material (letter grids read row by row, card ranks, apostle lists, numbered sets), tabulate which FAQ
  constraints each one explains and which it does not (same nature, rank counts, « intermediate steps »,
  physical contact), keep the strongest two with their weak point, and name the missing bridge (often an
  orientation/placement step) instead of forcing a site.
- **Every idea the user throws in (a phrase of the text, a liturgical series, a village-name theory, knights →
  cards) gets the same treatment in the same reply**: (1) grep the exact phrase and the concrete nouns across
  the whole FAQ base and the riddle texts, (2) compute what is computable (units, pair distances, counts vs a
  random-D control), (3) say what the idea explains AND what it leaves unexplained, (4) check that the
  real-world object exists near the zone before building on it (church, calvary, cross series in OSM/BD TOPO).
  An idea that explains the text but has no object on the ground is demoted, not dropped.
- **For every constraint you lean on, say where it lives**: riddle text, author's FAQ answer, or a player's
  question that the author merely answered. The user checks (« je ne la vois pas dans l'énigme ») and loses
  trust when an FAQ-derived detail (e.g. a wood splinter on the 11th) is presented as if it were in the text.
- **Recompute the exact endpoint of the previous riddle and compare every candidate start to it**: when a
  community consensus start (a tower) sits ~1 km past the computed point (a castle at 50 m), the consensus
  is weaker than it looks. Report both with their offsets; keep the exact point as the defensible one.
- **Before saying « X is not mapped / does not exist near the zone », query the exact local form**: geocode with
  singular/plural, article and postcode (`rue du rempart 38530`), then confirm with a second source (OSM, Commons
  geosearch). A France-wide generic query returns only the top ~50 hits and silently misses the local street; a
  wrong negative that reached the user had to be retracted. State a negative as « not found in A and B », never as
  a fact about the world.
- **Size the procedural tail before choosing where to spend effort**: add up the final walking steps (e.g. 10 + 10 +
  8 paces ≈ 35 m). If that span is small against the target zone (50 m), the tail (date, compass, pace length,
  grids) is annex for a zone answer, and the whole problem is the anchor that places the first step. Say so in the
  plan and give the anchor the budget.
- **Plan for « no initial intuition »** (user grants autonomy, cannot supply the first move): write
  `Enigme_XX/PLAN_ACTION.md` (recadrage, one table of parallel pistes each with its decisive kill test, sorting
  rules, what only the user can unblock) + ONE shared `BRIEF` file (verbatim riddle text, the author's ANSWERS tagged
  by FAQ id, data paths, already-dead list). Fan out 3-4 agents on DIFFERENT hypothesis families (ontology of the
  unknown objects, a decoding source named by the author, terrain simulation, text/author habits), and run cheap
  orthogonal tests yourself while they work. The next wave = survivors plus any fact the first wave surfaced.
  Re-verify any agent claim that contradicts an earlier statement of yours before relaying it, and write the
  correction into `solution.md`.
- **Video-FAQ transcripts hold answers absent from the FAQ JSON base**: read the whole transcript (in
  `execute_code`, loop `hermes_tools.read_file` with offset/limit, strip timestamps, save plain text to scratch),
  then grep normalised keywords with context. PDF libs (fitz, pypdf) may be missing; `read_file` extracts text.
- **A chain whose length « tombe juste » is not evidence** unless the places AND their order were fixed
  before measuring: with ±1 % tolerance, dozens of 4-place chains hit any D. Always report the count
  for random D values (control) next to the real hit.
- **Shark mode starts with a real Google pass**, not only scripted engines: DuckDuckGo, Bing and other HTML
  scrapers return empty pages, so an empty result proves nothing. Drive Google through Firecrawl — `terminal(command="firecrawl scrape 'https://www.google.com/search?hl=fr&num=20&udm=14&q=<quoted query>' -o .firecrawl/google.md")` then `read_file` it (verified: ~22 KB of real result blocks; the consent/cookie header at the top is normal). `browser_exec` is the fallback only
  (recipe in `references/techniques.md`). Before telling Guilhem « rien en ligne », run it for: the riddle
  title, key objects (« 4 C »), candidate places, and `site:` queries on the hunt's Facebook groups and
  forums. Report the leads as [RUMEUR].
- Communities of live hunts sit on the official Discord (buyers only). When public search is dry, ask
  Guilhem to log his account into the harness Chrome (Discord QR code screenshot, never a password), then
  read **only through the UI**, never post/react, no token/API helper. The channel list is virtualised:
  scroll the sidebar before claiming a channel is hidden. Search with `scripts/discord_search_safe.py`
  (`srch(q)`), never with fixed-coordinate clicks: the search box is also a Slate editor, so a layout
  shift can route keystrokes into the message composer. Search by concrete nouns of the riddle (places,
  people, units), not by the riddle title.

## References
- `references/techniques.md` — geodesy recipe, Nominatim, chain search + random-D control, image zoom
  crops, decode checks, Google-via-browser rumour search, web fallback.
- `references/exkalibur.md` — Exkalibur project: paths, official facts, decisions, state pointer.
- `scripts/discord_search_safe.py` — read-only Discord UI search with focus guards (`srch(q)`).
