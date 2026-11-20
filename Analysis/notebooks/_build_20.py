#!/usr/bin/env python3
# Builder for notebooks/20_extended_item_set.ipynb
# Run:  python3 notebooks/_build_20.py      (from the Analysis folder)
# Every cell is authored here as a string and written out with nbformat, so the
# notebook is reproducible from source. Edit this file, not the notebook.
import nbformat as nbf

OUTPATH = 'notebooks/20_extended_item_set.ipynb'
nb = nbf.v4.new_notebook()
cells = []
def md(s):   cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
def code(s): cells.append(nbf.v4.new_code_cell(s.strip("\n")))

# ----------------------------------------------------------------------
md(r"""
# Notebook 20. The extended item set for Study 1 of the tracking paper

Added November 19, 2026. Study 1 of the tracking paper reuses the items of the law review study and needs more of them: 18 story features per cell and genre instead of 12. This notebook adds 6 items to each of the four cells (HH, HL, LH, LL) in each of the six genres, 24 per genre and 144 in all. The law review study's 48 stratified items and 8 foils per genre stay exactly as they are. No new foils are drawn.

The new items come from the same draw that produced the old ones. Notebook 10 gave each genre a seeded random generator and a shuffled queue for each cell and grammatical type (noun or chunk), and walked those queues. This notebook rebuilds the same pool and the same queues, replays Notebook 10's draw, and checks that it gives the same 48 items per genre, with the same ids, text, cell and order, as the registered files. Only then does it keep walking the same queues to take the next items. If the replay does not match, the notebook stops before drawing anything.

Nothing in Notebook 10, its builder or its output folder is written. The constants (seed, genres, filters, `MANUAL_EXCLUDE`, `DISPLAY_OVERRIDES`, the franchise blocklist and so on) are read from `_build_10.py` itself, so the two notebooks cannot drift apart. Outputs go to `v4_rebuild/20_extended_item_set/`.
""")

# ----------------------------------------------------------------------
code(r"""
import ast, hashlib, json, re
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

try:
    from google.colab import drive  # type: ignore
    drive.mount('/content/drive')
except Exception:
    pass

_CANDS = [
    Path('/content/drive/MyDrive/DGK Lab/Reasoning Lab/'
         'DGK Lab - Scene A Faire Computational/Analysis/v4_rebuild'),
    Path('/Users/USER/Library/CloudStorage/GoogleDrive-ACCOUNT/'
         'My Drive/DGK Lab/Reasoning Lab/'
         'DGK Lab - Scene A Faire Computational/Analysis/v4_rebuild'),
    Path.cwd() / 'v4_rebuild',
    Path.cwd().parent / 'v4_rebuild',
]
V4 = next((c for c in _CANDS if c.exists()), None)
assert V4 is not None, 'Could not locate v4_rebuild; set V4 manually.'

# Inputs (read only)
PATH_BUILD10 = V4.parent / 'notebooks' / '_build_10.py'
PATH_CLASS   = V4 / '03b_classification' / 'stockiness_long_classified.parquet'
NB10         = V4 / '10_human_study_stimuli'
# Output (new folder)
OUT = V4 / '20_extended_item_set'
OUT.mkdir(parents=True, exist_ok=True)
print('V4  =', V4)
print('OUT =', OUT)

K_EXT = 18          # items per cell and genre in the extended set
""")

# ----------------------------------------------------------------------
md(r"""
## Read Notebook 10's constants from its builder

Notebook 10's builder holds its cells as strings. The cell below parses those strings and evaluates only plain assignments of the names listed, so the seed, the genres, the filters, the exclusion list and the display text fixes are exactly the registered ones.
""")
code(r"""
WANTED = ['GENRES', 'SEED', 'MIN_FILMS_IN_GENRE', 'K_PER_CELL', 'N_FOILS', 'ALLOWED_TYPES',
          'FOILS_UNIQUE_ACROSS_SET', 'MANUAL_EXCLUDE', 'DISPLAY_OVERRIDES', 'HIGH_CUT', 'LOW_CUT',
          'CELLS', 'CELL_CODES', 'TAXONOMY_TO_CATEGORY', 'FRANCHISE_BLOCKLIST']

def read_build10_constants(path):
    tree = ast.parse(path.read_text(encoding='utf-8'))
    srcs = [n.args[0].value for n in ast.walk(tree)
            if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == 'code'
            and n.args and isinstance(n.args[0], ast.Constant) and isinstance(n.args[0].value, str)]
    consts = {}
    for s in srcs:
        for node in ast.parse(s).body:
            if (isinstance(node, ast.Assign) and len(node.targets) == 1
                    and isinstance(node.targets[0], ast.Name) and node.targets[0].id in WANTED):
                name = node.targets[0].id
                assert name not in consts, f'{name} assigned twice in _build_10.py'
                consts[name] = eval(compile(ast.Expression(node.value), '<build10>', 'eval'),
                                    {'__builtins__': {}}, dict(consts))
    missing = [w for w in WANTED if w not in consts]
    assert not missing, f'not found in _build_10.py: {missing}'
    return consts

C10 = read_build10_constants(PATH_BUILD10)
globals().update(C10)
_excl = {s.lower().strip() for s in MANUAL_EXCLUDE}
print('build10 sha256 :', hashlib.sha256(PATH_BUILD10.read_bytes()).hexdigest())
print('GENRES         :', GENRES)
print('SEED           :', SEED, '  K_PER_CELL:', K_PER_CELL, '  N_FOILS:', N_FOILS, '  ALLOWED_TYPES:', ALLOWED_TYPES)
print('MANUAL_EXCLUDE :', len(MANUAL_EXCLUDE), 'strings;  DISPLAY_OVERRIDES:', len(DISPLAY_OVERRIDES))
assert K_PER_CELL == 12 and N_FOILS == 8 and len(GENRES) == 6

def genre_slug(g):
    return re.sub(r'[^a-z0-9]+', '_', g.lower()).strip('_')

def genre_code(g):
    return genre_slug(g).replace('_', '')[:3].upper()

def genre_rng(g):
    # Identical to Notebook 10: per-genre generator from SEED and the genre name.
    h = int.from_bytes(hashlib.sha256(g.encode('utf-8')).digest()[:4], 'little')
    return np.random.default_rng([SEED, h])
""")

# ----------------------------------------------------------------------
md(r"""
## Rebuild the eligible pool and the cells

These steps copy Notebook 10's code: load the classified table, apply the franchise blocklist, keep narrative nouns and chunks with at least 20 films in the genre, collapse identical strings, compute within-genre percentiles of prevalence (`rel_freq_in_genre`) and distinctiveness (`posterior_smoothed`), and cut them into terciles. The rebuilt pool is then compared, row by row, with the frozen `eligible_pool_predictors.csv` that Notebook 10 wrote.
""")
code(r"""
stk = pd.read_parquet(PATH_CLASS)
_bl = {s.lower() for s in FRANCHISE_BLOCKLIST}
_mask = stk['element'].astype(str).str.lower().isin(_bl)
stk.loc[_mask, 'is_narrative_element'] = False
stk.loc[_mask, 'element_taxonomy'] = 'character_name'

_ratio = (stk['film_count'] / stk['rel_freq_in_genre']).round()
FILMS_IN_GENRE = _ratio.groupby(stk['genre']).agg(lambda s: int(s.mode().iloc[0])).to_dict()

elig = stk[
    stk['is_narrative_element']
    & stk['element_type'].isin(ALLOWED_TYPES)
    & stk['genre'].isin(GENRES)
    & (stk['film_count'] >= MIN_FILMS_IN_GENRE)
].copy()
elig['key'] = elig['element'].astype(str).str.lower().str.strip()
elig = (elig.sort_values(['genre', 'key', 'ensemble'], ascending=[True, True, False])
            .drop_duplicates(['genre', 'key'])
            .reset_index(drop=True))
elig['prevalence_pct']      = elig.groupby('genre')['rel_freq_in_genre'].rank(pct=True)
elig['distinctiveness_pct'] = elig.groupby('genre')['posterior_smoothed'].rank(pct=True)

def tercile(p):
    return 'high' if p > HIGH_CUT else ('low' if p <= LOW_CUT else 'mid')

elig['prev_tercile'] = elig['prevalence_pct'].map(tercile)
elig['dist_tercile'] = elig['distinctiveness_pct'].map(tercile)
elig['cell'] = elig['prev_tercile'] + '_prev_' + elig['dist_tercile'] + '_dist'
pool = elig[elig['cell'].isin(CELLS)].copy()

# Cross-check against the frozen pool export of Notebook 10.
frozen = pd.read_csv(NB10 / 'eligible_pool_predictors.csv', keep_default_na=False, na_values=[''])
chk = elig[['genre', 'key', 'element_type', 'prevalence_pct', 'distinctiveness_pct',
            'prev_tercile', 'dist_tercile']].merge(
    frozen[['genre', 'key', 'element_type', 'prevalence_pct', 'distinctiveness_pct',
            'prev_tercile', 'dist_tercile']],
    on=['genre', 'key'], how='outer', suffixes=('', '_frozen'), indicator=True)
assert (chk['_merge'] == 'both').all(), 'rebuilt pool and eligible_pool_predictors.csv hold different rows'
assert (chk['element_type'] == chk['element_type_frozen']).all()
assert np.allclose(chk['prevalence_pct'], chk['prevalence_pct_frozen'], rtol=0, atol=1e-12)
assert np.allclose(chk['distinctiveness_pct'], chk['distinctiveness_pct_frozen'], rtol=0, atol=1e-12)
assert (chk['prev_tercile'] == chk['prev_tercile_frozen']).all()
assert (chk['dist_tercile'] == chk['dist_tercile_frozen']).all()
print(f'rebuilt pool: {len(elig):,} rows, identical to eligible_pool_predictors.csv '
      f'(rows, types, percentiles, terciles)')
print(f'rows in the four cells: {len(pool):,}')
LG10CD_EXACT = dict(zip(frozen['subtlex_token'], frozen['Lg10CD'].where(frozen['subtlex_variant'].isna())))
""")

# ----------------------------------------------------------------------
md(r"""
## Replay Notebook 10's draw and check it

The draw below is Notebook 10's `draw_genre()` with two additions that change nothing in what it picks: it remembers each candidate's position in its queue, and it returns the queues and the state so the draw can be continued. Notebook 10's three passes, with 12 per cell, are:

1. chunks, in each cell, up to half of 12 or the length of that cell's chunk queue, whichever is smaller;
2. nouns, in each cell, until the cell holds 12;
3. chunks again, in each cell still short of 12.

A candidate is skipped if it is in `MANUAL_EXCLUDE` or if it overlaps, as a whole-word sub-sequence in either direction, a string already taken in that genre. The replayed items are sorted and numbered as Notebook 10 numbered them (by cell, then by ensemble from high to low) and compared with `stimuli_long.csv` and the six JSON files. Every check is an assertion: if any fails, the notebook stops here.
""")
code(r"""
def overlaps(a, b):
    # Notebook 10's rule: whole-word containment in either direction.
    if a == b:
        return True
    ta, tb = a.split(), b.split()
    short, long_ = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
    n = len(short)
    return any(long_[i:i + n] == short for i in range(len(long_) - n + 1))

def build_queues(g):
    # Same calls to the same generator in the same order as Notebook 10.
    rng = genre_rng(g)
    sub = pool[pool['genre'] == g]
    queues, qpos, qlen = {}, {}, {}
    for c in CELLS:
        for t in ALLOWED_TYPES:
            idx = sub[(sub['cell'] == c) & (sub['element_type'] == t)].sort_values('key').index.to_numpy()
            q = list(rng.permutation(idx)) if len(idx) else []
            queues[(c, t)] = q
            qlen[(c, t)] = len(q)
            for pos, i in enumerate(q, start=1):
                qpos[int(i)] = pos
    return queues, qpos, qlen

def draw_original(g):
    queues, qpos, qlen = build_queues(g)
    st = {'accepted': [], 'accepted_keys': [], 'skipped': [],
          'per_cell': {c: 0 for c in CELLS},
          'per_cell_type': {c: {t: 0 for t in ALLOWED_TYPES} for c in CELLS}}

    def take(c, t, limit):
        q = queues[(c, t)]
        while q and st['per_cell'][c] < limit:
            i = q.pop(0)
            k = pool.at[i, 'key']
            if k in _excl:
                st['skipped'].append((c, t, k, qpos[int(i)], 'MANUAL_EXCLUDE', '')); continue
            blocker = next((ak for ak in st['accepted_keys'] if overlaps(k, ak)), None)
            if blocker is not None:
                st['skipped'].append((c, t, k, qpos[int(i)], 'overlaps a selected item', blocker)); continue
            st['accepted'].append((c, i)); st['accepted_keys'].append(k)
            st['per_cell'][c] += 1; st['per_cell_type'][c][t] += 1

    chunk_target = {c: min(K_PER_CELL // 2, len(queues[(c, 'chunk')])) for c in CELLS}
    for c in CELLS:
        take(c, 'chunk', chunk_target[c])
    for c in CELLS:
        for t in [t for t in ALLOWED_TYPES if t != 'chunk']:
            take(c, t, K_PER_CELL)
    for c in CELLS:
        take(c, 'chunk', K_PER_CELL)
    return queues, qpos, qlen, st

def numbered(g, accepted, start=1):
    rows = []
    for c, i in accepted:
        r = pool.loc[i].to_dict(); r['cell'] = c; r['pool_index'] = int(i)
        rows.append(r)
    sel = pd.DataFrame(rows)
    sel['cell'] = pd.Categorical(sel['cell'], categories=CELLS, ordered=True)
    sel = sel.sort_values(['cell', 'ensemble'], ascending=[True, False]).reset_index(drop=True)
    sel['cell'] = sel['cell'].astype(str)
    sel['cell_code'] = sel['cell'].map(CELL_CODES)
    sel['item_id'] = [f'{genre_code(g)}_{cc}_{n:02d}' for cc, n in
                      zip(sel['cell_code'], sel.groupby('cell_code').cumcount() + start)]
    sel['display_text'] = sel['element'].astype(str).map(
        lambda e: DISPLAY_OVERRIDES.get(e, EXTENSION_DISPLAY_OVERRIDES.get(e, e) if start > K_PER_CELL else e))
    return sel

long10 = pd.read_parquet(NB10 / 'stimuli_long.parquet')
long10_csv = pd.read_csv(NB10 / 'stimuli_long.csv', keep_default_na=False, na_values=[''])
assert long10['item_id'].tolist() == long10_csv['item_id'].tolist()
assert long10['display_text'].tolist() == long10_csv['display_text'].tolist()
json10 = {g: json.loads((NB10 / f'stimuli_{genre_slug(g)}.json').read_text(encoding='utf-8')) for g in GENRES}

STATE, QUEUES, QPOS, QLEN, ORIG = {}, {}, {}, {}, {}
for g in GENRES:
    queues, qpos, qlen, st = draw_original(g)
    sel = numbered(g, st['accepted'])
    ref = long10[(long10['genre'] == g) & ~long10['is_foil']].reset_index(drop=True)
    ref_json = [it for it in json10[g]['items'] if not it['is_foil']]
    assert len(sel) == len(ref) == len(ref_json) == 4 * K_PER_CELL, g
    for col in ['item_id', 'key', 'element', 'cell', 'cell_code', 'display_text', 'element_type', 'film_count']:
        assert sel[col].tolist() == ref[col].tolist(), f'{g}: replay differs from stimuli_long in {col}'
    assert np.allclose(sel['ensemble'], ref['ensemble'], rtol=0, atol=0)
    assert sel['item_id'].tolist() == [it['id'] for it in ref_json], f'{g}: ids differ from JSON'
    assert sel['display_text'].tolist() == [it['text'] for it in ref_json], f'{g}: text differs from JSON'
    assert sel['cell_code'].tolist() == [it['cell_code'] for it in ref_json], f'{g}: cells differ from JSON'
    assert sel['element'].tolist() == [it['element_string'] for it in ref_json], f'{g}: strings differ from JSON'
    STATE[g], QUEUES[g], QPOS[g], QLEN[g], ORIG[g] = st, queues, qpos, qlen, sel
    print(f'{g:<16} replay identical to the registered 48 items (ids, text, cell, order); '
          f'skips in the original draw: {len(st["skipped"])}')
REPRODUCED = True
print('\nAll six genres reproduced exactly. The extension may proceed.')
""")

# ----------------------------------------------------------------------
md(r"""
## Continue the draw to 18 per cell

**The continuation rule for the noun and chunk balance.** Notebook 10's passes aim at half of each cell as chunks, then fill with nouns, then fall back to chunks. Had the target been 18 from the start, pass 1 would have taken up to 9 chunks before any noun, which would change the first 12. So the 12 are left as drawn, and the same three passes are run again, in the same order over cells, from where the queues stopped, with the target raised to 18:

1. chunks, in each cell, until the cell holds 9 chunks (half of 18) or as many as its chunk queue held at the start, whichever is smaller;
2. nouns, in each cell, until the cell holds 18;
3. chunks again, in each cell still short of 18.

Pass 1 counts chunks rather than items because the cell already holds nouns. In Notebook 10's pass 1 the two counts are the same thing, since nothing else has been taken yet. The effect is that a cell with plenty of chunks ends with the half-and-half balance Notebook 10 aimed at, and a cell with few chunks is filled with nouns, as before.

**Skips.** A candidate is skipped if it is in `MANUAL_EXCLUDE`; if it overlaps, under Notebook 10's whole-word rule, any item already selected for the genre (the original 48 and the new items taken before it); if it overlaps one of the genre's 8 foils; or if it is the same string as a foil of any other genre. The last rule mirrors `FOILS_UNIQUE_ACROSS_SET` in Notebook 10, under which no foil string may also be a stimulus anywhere in the set. Notebook 10 enforced that by keeping foils away from stimuli; since the foils are now fixed, the new items are kept away from the foils instead. Nothing else is excluded.
""")
code(r"""
# Strings rejected in the review of the extension (November 19, 2026), by the standards of the law
# review study's review: idiom or summary residue, meta words, ambiguous nouns, fragments of compounds,
# and the genre's own name. They apply to the NEW items only, in every genre, so the replay of the
# registered items above is untouched. Each rejection hands the place to the next candidate in the
# cell's seeded queue. Add strings here and rerun; do not edit output files by hand.
EXTENSION_EXCLUDE = __EXTENSION_EXCLUDE__
_ext_excl = {s.lower().strip() for s in EXTENSION_EXCLUDE}
# Display text for new items, on the rule of DISPLAY_OVERRIDES (capitals for proper nouns, a plural
# where the singular is unnatural). The pipeline string is unchanged.
EXTENSION_DISPLAY_OVERRIDES = {'molotov cocktail': 'Molotov cocktail', 'ruin': 'ruins'}
print('EXTENSION_EXCLUDE:', len(_ext_excl), 'strings')

foils10 = long10[long10['is_foil']]
FOIL_KEYS = {g: foils10.loc[foils10['genre'] == g, 'key'].tolist() for g in GENRES}
ALL_FOIL_KEYS = set(foils10['key'])

REMAIN_BEFORE, NEW, EXT_SKIPS, EXT_MIX = {}, {}, {}, {}
for g in GENRES:
    st, queues, qpos = STATE[g], QUEUES[g], QPOS[g]
    REMAIN_BEFORE[g] = {(c, t): len(queues[(c, t)]) for c in CELLS for t in ALLOWED_TYPES}
    accepted_keys = list(st['accepted_keys'])
    per_cell = dict(st['per_cell'])
    per_type = {c: dict(st['per_cell_type'][c]) for c in CELLS}
    new, skips = [], []

    def take(c, t, done):
        q = queues[(c, t)]
        while q and per_cell[c] < K_EXT and not done(c):
            i = q.pop(0)
            k = pool.at[i, 'key']
            pos = qpos[int(i)]
            if k in _excl:
                skips.append((c, t, k, pos, 'MANUAL_EXCLUDE', '')); continue
            if k in _ext_excl:
                skips.append((c, t, k, pos, 'EXTENSION_EXCLUDE', '')); continue
            b = next((ak for ak in accepted_keys if overlaps(k, ak)), None)
            if b is not None:
                skips.append((c, t, k, pos, 'overlaps a selected item', b)); continue
            b = next((fk for fk in FOIL_KEYS[g] if overlaps(k, fk)), None)
            if b is not None:
                skips.append((c, t, k, pos, "overlaps one of the genre's foils", b)); continue
            if k in ALL_FOIL_KEYS:
                fg = foils10.loc[foils10['key'] == k, 'genre'].iloc[0]
                skips.append((c, t, k, pos, 'is a foil of another genre', fg)); continue
            new.append((c, i)); accepted_keys.append(k)
            per_cell[c] += 1; per_type[c][t] += 1

    chunk_target = {c: min(K_EXT // 2, QLEN[g][(c, 'chunk')]) for c in CELLS}
    for c in CELLS:                                     # pass 1: chunks to half of 18
        take(c, 'chunk', lambda c, tgt=chunk_target: per_type[c]['chunk'] >= tgt[c])
    for c in CELLS:                                     # pass 2: nouns to 18
        for t in [t for t in ALLOWED_TYPES if t != 'chunk']:
            take(c, t, lambda c: False)
    for c in CELLS:                                     # pass 3: chunks to 18
        take(c, 'chunk', lambda c: False)

    NEW[g], EXT_SKIPS[g], EXT_MIX[g] = new, skips, per_type
    print(f'{g:<16} ' + '  '.join(f"{CELL_CODES[c]}={per_cell[c]} ({per_type[c]['noun']}n+{per_type[c]['chunk']}c)"
                                  for c in CELLS) + f'   skipped={len(skips)}')

SHORT = [(g, c) for g in GENRES for c in CELLS
         if sum(1 for cc, _ in NEW[g] if cc == c) < K_EXT - K_PER_CELL]
print('\ncells short of 18:', SHORT if SHORT else 'none')
""")

# ----------------------------------------------------------------------
md(r"""
## Assemble the new items

Within each cell the 6 new items are numbered 13 to 18 by ensemble, high to low, the rule Notebook 10 used for 1 to 12. Their fields are built as Notebook 10 built them. The display text applies `DISPLAY_OVERRIDES`. The SUBTLEX-US values follow Notebook 10's join on the head token (the last word). `Lg10CD` comes from the frozen `eligible_pool_predictors.csv`, used only where that file matched the head token itself rather than a spelling variant, which is the rule Notebook 10 used for the JSON files. `Lg10WF` is not in that file, and this notebook does not open the SUBTLEX-US file, so `Lg10WF` is copied from the registered stimulus table when the same head token occurs there and is empty otherwise. The experiment does not read either value.
""")
code(r"""
WF_FROM_10 = (long10.dropna(subset=['Lg10WF']).drop_duplicates('subtlex_token')
                    .set_index('subtlex_token')['Lg10WF'].to_dict())

def to_py(v):
    if isinstance(v, (np.integer,)):  return int(v)
    if isinstance(v, (np.floating,)): return None if np.isnan(v) else float(v)
    if isinstance(v, (np.bool_,)):    return bool(v)
    if isinstance(v, float) and np.isnan(v): return None
    return v

new_frames = []
for g in GENRES:
    sel = numbered(g, NEW[g], start=K_PER_CELL + 1)
    sel['genre'] = g
    sel['home_genre'] = g
    sel['is_foil'] = False
    sel['film_count_in_target_genre'] = sel['film_count'].astype(int)
    sel['foil_rule'] = None
    sel['category_key'] = sel['element_taxonomy'].map(TAXONOMY_TO_CATEGORY)
    sel['subtlex_token'] = sel['key'].str.split().str[-1]
    sel['Lg10CD'] = sel['subtlex_token'].map(LG10CD_EXACT).astype(float)
    sel['Lg10WF'] = sel['subtlex_token'].map(WF_FROM_10).astype(float)
    sel['subtlex_matched'] = sel['Lg10CD'].notna()
    sel['queue_position'] = sel['pool_index'].map(QPOS[g]).astype(int)
    sel['in_law_review_study'] = False
    new_frames.append(sel)
new_items = pd.concat(new_frames, ignore_index=True)

# Original rows of the long table, with queue positions for the stratified ones.
orig_long = long10.copy()
orig_long['in_law_review_study'] = True
qp = {}
for g in GENRES:
    for iid, pi in zip(ORIG[g]['item_id'], ORIG[g]['pool_index']):
        qp[iid] = QPOS[g][pi]
orig_long['queue_position'] = orig_long['item_id'].map(qp).astype('Int64')

LONG_COLS = list(long10.columns) + ['in_law_review_study', 'queue_position']
parts = []
for g in GENRES:
    parts.append(orig_long[orig_long['genre'] == g])
    parts.append(new_items.loc[new_items['genre'] == g, [c for c in LONG_COLS]])
ext = pd.concat(parts, ignore_index=True)[LONG_COLS]
ext['queue_position'] = ext['queue_position'].astype('Int64')

# Integrity checks, Notebook 10's and the extension's.
assert len(ext) == 6 * (4 * K_EXT + N_FOILS) == 480
assert ext['item_id'].is_unique
assert not ext.duplicated(['genre', 'key']).any(), 'duplicate string within a genre'
_stim = set(ext.loc[~ext['is_foil'], 'key'])
assert not ext.loc[ext['is_foil'], 'key'].isin(_stim).any(), 'a foil coincides with a stimulus'
for g in GENRES:
    s = ext[(ext['genre'] == g)]
    ks = s.loc[~s['is_foil'], 'key'].tolist(); fk = s.loc[s['is_foil'], 'key'].tolist()
    for a_i, a in enumerate(ks):
        assert not any(overlaps(a, b) for b in ks[a_i + 1:]), f'overlap among {g} items'
        assert not any(overlaps(a, b) for b in fk), f'item overlaps a foil in {g}'
    assert (s[~s['is_foil']].groupby('cell_code').size() == K_EXT).all() or SHORT
    n = new_items[new_items['genre'] == g]
    assert (n['cell'].map(lambda c: c.split('_prev_')[0]) == n['prev_tercile']).all()
    assert (n['cell'].map(lambda c: c.split('_prev_')[1].replace('_dist', '')) == n['dist_tercile']).all()
assert not new_items['key'].isin(_excl).any()
print('extended long table:', ext.shape, '  new items:', len(new_items))
print(ext[~ext['is_foil']].groupby(['genre', 'cell_code']).size().unstack().reindex(GENRES).to_string())
print('new items with Lg10CD:', int(new_items['Lg10CD'].notna().sum()), 'of', len(new_items),
      '; with Lg10WF:', int(new_items['Lg10WF'].notna().sum()))
""")

# ----------------------------------------------------------------------
md(r"""
## Do the new items keep the cells matched?

In the law review study the high- and low-distinctiveness cells have nearly the same prevalence within each prevalence level. The table below gives, for each genre and cell, the median prevalence (share of the genre's films with the story feature, in percent) and the median distinctiveness (the smoothed share of the story feature's films that belong to the genre, in percent) of the original 12, the new 6 and all 18, and then the same pooled over genres. A second table compares the within-genre percentiles of new and original items in each cell, pooled over genres, with a Mann-Whitney test, to see whether the new items sit closer to the middle tercile than the originals.
""")
code(r"""
strat = ext[~ext['is_foil']].copy()
strat['prev_pc'] = 100 * strat['rel_freq_in_genre']
strat['dist_pc'] = 100 * strat['posterior_smoothed']
strat['set'] = np.where(strat['in_law_review_study'], 'original', 'new')

def med_table(df, by):
    rows = []
    for keys, s in df.groupby(by, sort=False, observed=True):
        keys = keys if isinstance(keys, tuple) else (keys,)
        r = dict(zip(by, keys))
        for lab, part in [('orig', s[s['set'] == 'original']), ('new', s[s['set'] == 'new']), ('all', s)]:
            r[f'prev_{lab}'] = part['prev_pc'].median()
            r[f'dist_{lab}'] = part['dist_pc'].median()
        rows.append(r)
    return pd.DataFrame(rows)

strat['genre'] = pd.Categorical(strat['genre'], categories=GENRES, ordered=True)
MED_GC = med_table(strat.sort_values(['genre', 'cell_code']), ['genre', 'cell_code'])
MED_POOLED = med_table(strat.sort_values('cell_code'), ['cell_code'])
pd.set_option('display.width', 200)
print('Medians by genre and cell (percent):')
print(MED_GC.round(3).to_string(index=False))
print('\nMedians pooled over genres (percent):')
print(MED_POOLED.round(3).to_string(index=False))

# Matching within prevalence level: HH vs HL and LH vs LL on prevalence.
MATCH = []
for hi, lo in [('HH', 'HL'), ('LH', 'LL')]:
    for lab in ['orig', 'new', 'all']:
        a = MED_POOLED.set_index('cell_code').loc[hi, f'prev_{lab}']
        b = MED_POOLED.set_index('cell_code').loc[lo, f'prev_{lab}']
        MATCH.append({'pair': f'{hi} vs {lo}', 'set': lab, 'prev_high_dist': a, 'prev_low_dist': b, 'ratio': a / b})
    s = strat[strat['cell_code'].isin([hi, lo])]
    p = stats.mannwhitneyu(s.loc[s['cell_code'] == hi, 'prev_pc'], s.loc[s['cell_code'] == lo, 'prev_pc']).pvalue
    MATCH.append({'pair': f'{hi} vs {lo}', 'set': 'all 18, Mann-Whitney p on prevalence', 'prev_high_dist': np.nan,
                  'prev_low_dist': np.nan, 'ratio': p})
MATCH = pd.DataFrame(MATCH)
print('\nPrevalence match within each prevalence level (pooled medians):')
print(MATCH.round(4).to_string(index=False))

# New vs original, within-genre percentiles, pooled over genres.
EXTREME = []
for cc in ['HH', 'HL', 'LH', 'LL']:
    s = strat[strat['cell_code'] == cc]
    o, n = s[s['set'] == 'original'], s[s['set'] == 'new']
    for col, lab in [('prevalence_pct', 'prevalence'), ('distinctiveness_pct', 'distinctiveness'),
                     ('prev_pc', 'prevalence %'), ('dist_pc', 'distinctiveness %')]:
        p = stats.mannwhitneyu(o[col], n[col]).pvalue
        EXTREME.append({'cell': cc, 'measure': lab, 'median_original': o[col].median(),
                        'median_new': n[col].median(), 'mann_whitney_p': p})
EXTREME = pd.DataFrame(EXTREME)
print('\nNew vs original items, pooled over genres:')
print(EXTREME.round(4).to_string(index=False))

# Plain statement, computed from the numbers above so it stays true on a rerun.
# A pair of cells counts as matched on prevalence when the pooled medians of all
# 18 differ by less than a quarter (ratio between 0.8 and 1.25) and the
# Mann-Whitney test of the two cells' prevalence is not significant at .05.
CONCLUSION = []
for hi, lo, level in [('HH', 'HL', 'high'), ('LH', 'LL', 'low')]:
    m = MATCH[MATCH['pair'] == f'{hi} vs {lo}'].set_index('set')
    r_o, r_n, r_a = m.loc['orig', 'ratio'], m.loc['new', 'ratio'], m.loc['all', 'ratio']
    p = m.loc['all 18, Mann-Whitney p on prevalence', 'ratio']
    ok = (0.8 <= r_a <= 1.25) and p > 0.05
    CONCLUSION.append(
        f'At {level} prevalence, the median prevalence of {hi} and {lo} is '
        f'{m.loc["all", "prev_high_dist"]:.2f}% and {m.loc["all", "prev_low_dist"]:.2f}% over all 18 items '
        f'(ratio {r_a:.2f}; {r_o:.2f} for the original 12, {r_n:.2f} for the new 6 alone; '
        f'Mann-Whitney p = {p:.2f}). '
        + ('The extension keeps the match.' if ok else 'The extension does NOT keep the match.'))
less, more = [], []
for r in EXTREME[EXTREME['measure'].isin(['prevalence', 'distinctiveness'])].itertuples(index=False):
    level = r.cell[0] if r.measure == 'prevalence' else r.cell[1]
    # In a high tercile, a lower median is less extreme; in a low tercile, a higher one.
    less_ext = (r.median_new < r.median_original) if level == 'H' else (r.median_new > r.median_original)
    if r.mann_whitney_p < 0.05:
        (less if less_ext else more).append(f'{r.cell} {r.measure} (p = {r.mann_whitney_p:.3f})')
if not less and not more:
    CONCLUSION.append('On within-genre percentiles, no cell shows a significant difference between new and '
                      'original items on either dimension (8 tests, each at .05): the new items are not '
                      'systematically less extreme than the originals.')
else:
    if less:
        CONCLUSION.append('The new items are significantly LESS extreme than the originals on: ' + ', '.join(less) + '.')
    if more:
        CONCLUSION.append('The new items are significantly MORE extreme than the originals on: ' + ', '.join(more) + '.')
    CONCLUSION.append('Eight tests were run at .05 with no correction, so one significant result is within chance.')
for line in CONCLUSION:
    print(line)
""")

# ----------------------------------------------------------------------
md(r"""
## Flags for the reviewer

The new items were reviewed on November 19, 2026 by Claude, the AI assistant, by the standards of the law review study's review (`stimuli_rejection_log.md` and `stimuli_rejects_for_confirmation.md` in Notebook 10's folder): idiom or summary residue, meta words, ambiguous nouns, fragments of compounds and the genre's own name are rejected; abstract but recognizable features and sensitive content are kept, as the investigator decided in October. The review ran in three rounds, each rejection handing its place to the next candidate in the cell's seeded queue, until no new item was rejected. The rejected strings are in `EXTENSION_EXCLUDE`. The investigator's confirmation of the final list is recorded in `extension_review_log.md` in the output folder. The `flag` column of the review sheet notes what a reader of the final list may still want to look at; a flag is not a rejection.
""")
code(r"""
# (genre, pipeline string) -> note. Written by hand after reading the draw.
FLAGS = __FLAGS__

def shared_word_note(g, k, item_id):
    words = set(k.split())
    others = ext[(ext['genre'] == g) & (ext['item_id'] != item_id)]
    hits = [f"{o} ({iid})" for o, iid in zip(others['display_text'], others['item_id'])
            if words & set(str(o).lower().split()) and len(words | set(str(o).lower().split())) > 1]
    return ('shares a word with ' + ', '.join(hits)) if hits else ''

unknown = [gk for gk in FLAGS if not ((new_items['genre'] == gk[0]) & (new_items['key'] == gk[1])).any()]
if unknown: print('flags for items no longer drawn (ignored):', len(unknown))

rev = new_items.copy()
rev['films_in_genre'] = rev['genre'].map(FILMS_IN_GENRE)
rev['prevalence_percent'] = (100 * rev['rel_freq_in_genre']).round(3)
rev['distinctiveness_percent'] = (100 * rev['posterior_smoothed']).round(2)
rev['prevalence_percentile'] = rev['prevalence_pct'].round(3)
rev['distinctiveness_percentile'] = rev['distinctiveness_pct'].round(3)
def _flag(r):
    parts = [FLAGS.get((r['genre'], r['key']), ''), shared_word_note(r['genre'], r['key'], r['item_id'])]
    return '; '.join(p for p in parts if p)
rev['flag'] = rev.apply(_flag, axis=1)
REVIEW_COLS = ['genre', 'cell_code', 'item_id', 'display_text', 'element', 'element_type', 'element_taxonomy',
               'film_count', 'films_in_genre', 'prevalence_percent', 'distinctiveness_percent',
               'prevalence_percentile', 'distinctiveness_percentile', 'queue_position', 'flag']
rev = rev[REVIEW_COLS]
print(f'{(rev["flag"] != "").sum()} of {len(rev)} new items carry a flag')
for g in GENRES:
    print(f'\n{g}')
    for r in rev[rev['genre'] == g].itertuples(index=False):
        print(f'  {r.item_id:<10} {r.display_text:<24} {r.element_type:<5} n={r.film_count:<4} '
              f'P={r.prevalence_percent:6.3f}% D={r.distinctiveness_percent:6.2f}% q={r.queue_position:<3} {r.flag}')
""")

# ----------------------------------------------------------------------
md(r"""
## Write the outputs

Five files go to `v4_rebuild/20_extended_item_set/`. The six JSON files keep the registered files' top-level keys and per-item fields; `k_per_cell` becomes 18 and `n_items` becomes 80, and each item gains `in_law_review_study`. The original 56 items are copied from the registered JSON files unchanged, in their order, and the 24 new items follow, by cell and then by id. `stimuli_all.js` is built from the six new JSON files exactly as the experiment's copy is built from the registered ones (checked below by rebuilding the experiment's copy from the registered JSON files byte for byte).
""")
code(r"""
written = []
JSON_FIELDS = ['item_id', 'display_text', 'cell', 'cell_code', 'is_foil', 'home_genre',
               'element_type', 'element_taxonomy', 'category_key',
               'film_count', 'film_count_in_target_genre', 'foil_rule',
               'prevalence_pct', 'distinctiveness_pct', 'ensemble',
               'subtlex_token', 'Lg10WF', 'Lg10CD']
GENRE_KEYS_JS = ['western', 'horror', 'science_fiction', 'crime', 'comedy', 'fantasy']

new_json = {}
for g in GENRES:
    payload = json.loads((NB10 / f'stimuli_{genre_slug(g)}.json').read_text(encoding='utf-8'))
    item_keys = list(payload['items'][0].keys())
    for it in payload['items']:
        assert list(it.keys()) == item_keys
        it['in_law_review_study'] = True
    for _, r in new_items[new_items['genre'] == g].iterrows():
        d = {'id': r['item_id'], 'text': r['display_text'], 'element_string': r['element']}
        d.update({k: to_py(r[k]) for k in JSON_FIELDS if k not in ('item_id', 'display_text')})
        assert list(d.keys()) == item_keys
        d['in_law_review_study'] = False
        payload['items'].append(d)
    payload['k_per_cell'] = K_EXT
    payload['n_items'] = len(payload['items'])
    assert payload['n_items'] == 80
    new_json[genre_slug(g)] = payload
    p = OUT / f'stimuli_{genre_slug(g)}.json'
    p.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    written.append(p)

def make_all_js(d):
    return ('// stimuli_all.js (GENERATED FILE; do not edit by hand)\n'
            '// Inline fallback for the six stimuli_<genre>.json files in this folder.\n'
            'window.STIMULI = ' + json.dumps({k: d[k] for k in GENRE_KEYS_JS}, ensure_ascii=False, indent=1) + ';\n')

# Check the format against the experiment's file, rebuilt from the registered JSON.
EXP_JS = V4.parent.parent / 'Experiment' / 'Tracking Study 1 (Pavlovia experiment-2)' / 'stimuli' / 'stimuli_all.js'
if EXP_JS.exists():
    reg = {genre_slug(g): json.loads((NB10 / f'stimuli_{genre_slug(g)}.json').read_text(encoding='utf-8')) for g in GENRES}
    assert make_all_js(reg) == EXP_JS.read_text(encoding='utf-8'), 'stimuli_all.js format not reproduced'
    JS_FORMAT_CHECK = 'the experiment copy is rebuilt byte for byte from the registered JSON files'
else:
    JS_FORMAT_CHECK = 'experiment copy not found; format check skipped'
print('stimuli_all.js format check:', JS_FORMAT_CHECK)
p = OUT / 'stimuli_all.js'; p.write_text(make_all_js(new_json), encoding='utf-8'); written.append(p)

# Round trip: the JSON files and the long table agree.
for g in GENRES:
    items = new_json[genre_slug(g)]['items']
    s = ext[ext['genre'] == g]
    assert [it['id'] for it in items] == s['item_id'].tolist()
    assert [it['text'] for it in items] == s['display_text'].tolist()
    assert [it['in_law_review_study'] for it in items] == s['in_law_review_study'].tolist()
    old = json10[g]['items']
    for a, b in zip(old, items[:56]):
        assert {k: v for k, v in b.items() if k != 'in_law_review_study'} == a

p = OUT / 'extended_items_long.csv'; ext.to_csv(p, index=False, encoding='utf-8'); written.append(p)
p = OUT / 'review_sheet_new_items.csv'; rev.to_csv(p, index=False, encoding='utf-8'); written.append(p)
""")

# ----------------------------------------------------------------------
code(r"""
L = []
def out(s=''):
    L.append(s)
out('=' * 78)
out('NOTEBOOK 20: THE EXTENDED ITEM SET FOR STUDY 1 OF THE TRACKING PAPER')
out('=' * 78)
out('Six genres, four cells, 18 story features per cell: the 12 of the law review study')
out('plus 6 new ones taken from further down the same seeded queues. Foils unchanged (8 per genre).')
out(f'seed {SEED}; constants read from notebooks/_build_10.py; {len(MANUAL_EXCLUDE)} strings in MANUAL_EXCLUDE.')
out()
out('1. REPRODUCTION OF THE LAW REVIEW STUDY ITEMS')
out('-' * 78)
out('The pool was rebuilt and matches eligible_pool_predictors.csv row for row (types,')
out('percentiles, terciles). The replayed draw gives, for every genre, the same 48 stratified')
out('items as stimuli_long.csv and the JSON files: same ids, pipeline strings, display text,')
out('cells, types, film counts and ensemble values, in the same order. Result: '
    + ('reproduced exactly.' if REPRODUCED else 'NOT reproduced.'))
out()
out('2. THE CONTINUATION RULE FOR THE NOUN AND CHUNK BALANCE')
out('-' * 78)
out('The first 12 are left as drawn. Notebook 10\'s three passes are then run again from where')
out('the queues stopped, with the target raised from 12 to 18: (1) chunks until the cell holds')
out('9 chunks, or as many as its chunk queue held at the start if that is fewer; (2) nouns until')
out('the cell holds 18; (3) chunks again for any cell still short of 18.')
out()
out('3. QUEUES, TAKES AND SKIPS PER GENRE AND CELL')
out('-' * 78)
out('"left" is what the queue still held when Notebook 10 stopped (nouns + chunks); "taken" is')
out('the number of new items (nouns + chunks); "skipped" lists each skipped candidate.')
for g in GENRES:
    out(g)
    for c in CELLS:
        cc = CELL_CODES[c]
        left_n = REMAIN_BEFORE[g][(c, 'noun')]; left_c = REMAIN_BEFORE[g][(c, 'chunk')]
        took = [(cc2, i) for cc2, i in NEW[g] if cc2 == c]
        tn = sum(1 for _, i in took if pool.at[i, 'element_type'] == 'noun')
        tc = len(took) - tn
        sk = [s for s in EXT_SKIPS[g] if s[0] == c]
        out(f'  {cc}: left {left_n + left_c:4d} ({left_n}n + {left_c}c)  taken {len(took)} ({tn}n + {tc}c)  '
            f'skipped {len(sk)}  final {EXT_MIX[g][c]["noun"]}n + {EXT_MIX[g][c]["chunk"]}c'
            + ('' if len(took) == K_EXT - K_PER_CELL else '   SHORT OF 18'))
        for (_, t, k, pos, why, b) in sk:
            out(f'      skipped {k!r} ({t}, queue position {pos}): {why}' + (f' ({b!r})' if b else ''))
out('cells short of 18: ' + ('none' if not SHORT else ', '.join(f'{g}/{CELL_CODES[c]}' for g, c in SHORT)))
nsk = pd.Series([s[4] for g in GENRES for s in EXT_SKIPS[g]]).value_counts()
out('skips by reason: ' + (', '.join(f'{k}: {v}' for k, v in nsk.items()) if len(nsk) else 'none'))
out()
out('4. MEDIAN PREVALENCE AND DISTINCTIVENESS (percent)')
out('-' * 78)
out('Prevalence = share of the genre\'s films with the story feature (rel_freq_in_genre).')
out('Distinctiveness = smoothed share of the story feature\'s films in the genre (posterior_smoothed).')
out(f'{"genre":<16}{"cell":<5}{"P orig":>8}{"P new":>8}{"P all":>8}{"D orig":>9}{"D new":>8}{"D all":>8}')
for r in MED_GC.itertuples(index=False):
    out(f'{r.genre:<16}{r.cell_code:<5}{r.prev_orig:8.3f}{r.prev_new:8.3f}{r.prev_all:8.3f}'
        f'{r.dist_orig:9.2f}{r.dist_new:8.2f}{r.dist_all:8.2f}')
out('pooled over genres')
for r in MED_POOLED.itertuples(index=False):
    out(f'{"all genres":<16}{r.cell_code:<5}{r.prev_orig:8.3f}{r.prev_new:8.3f}{r.prev_all:8.3f}'
        f'{r.dist_orig:9.2f}{r.dist_new:8.2f}{r.dist_all:8.2f}')
out()
out('Prevalence match within each prevalence level (pooled medians, percent):')
for r in MATCH.itertuples(index=False):
    if 'Mann' in r.set:
        out(f'  {r.pair}: {r.set} = {r.ratio:.3f}')
    else:
        out(f'  {r.pair}, {r.set:<5}: {r.prev_high_dist:.3f} vs {r.prev_low_dist:.3f} (ratio {r.ratio:.3f})')
out()
out('New against original items, pooled over genres (within-genre percentiles and percents):')
for r in EXTREME.itertuples(index=False):
    out(f'  {r.cell} {r.measure:<18} original {r.median_original:8.3f}  new {r.median_new:8.3f}  '
        f'Mann-Whitney p = {r.mann_whitney_p:.3f}')
out()
out('In plain words:')
for line in CONCLUSION:
    out('  ' + line)
out()
out('5. FILES')
out('-' * 78)
out('stimuli_<genre>.json x 6 : 80 items each (56 registered, unchanged and in order, then 24 new);')
out('                           every registered field kept; in_law_review_study added; k_per_cell 18.')
out('stimuli_all.js           : window.STIMULI built from the six new JSON files (' + JS_FORMAT_CHECK + ').')
out('extended_items_long.csv  : 480 rows, the columns of stimuli_long.csv plus in_law_review_study and')
out('                           queue_position (position in its cell-and-type queue; empty for foils).')
out('review_sheet_new_items.csv: the 144 new items with a flag column for the reviewer.')
out()
out('6. NOTES')
out('-' * 78)
out(f'SUBTLEX-US: Lg10CD is filled for {int(new_items["Lg10CD"].notna().sum())} of 144 new items (exact head-token')
out(f'match from eligible_pool_predictors.csv); Lg10WF for {int(new_items["Lg10WF"].notna().sum())} of 144 (copied from the')
out('registered stimulus table where the same head token occurs). The SUBTLEX-US file was not opened.')
out('The experiment does not read either value.')
out(f'{int((rev["flag"] != "").sum())} of 144 new items in the final list carry a note in the flag column; a note is not a rejection.')
out(f'Reviewed on November 19, 2026 by the standards of the law review study\'s review; {len(_ext_excl)} strings rejected (EXTENSION_EXCLUDE); see extension_review_log.md.')
p = OUT / 'extended_items_report.txt'; p.write_text('\n'.join(L) + '\n', encoding='utf-8'); written.append(p)
print('\n'.join(L))
print()
for p in written:
    print('wrote', p.name, f'({p.stat().st_size:,} bytes)')
""")

nb['cells'] = cells
nb['metadata'] = {'kernelspec': {'name': 'python3', 'display_name': 'Python 3', 'language': 'python'},
                  'language_info': {'name': 'python'}}

# The hand-written flags are kept in a separate block below so they are easy to find.
FLAGS_SRC = r'''{
    # Western
    ('Western', 'land'): 'vague: land as property, territory or terrain',
    ('Western', 'robbery'): 'near-synonym of robber (WES_HH_10) and of the new holdup (WES_LH_14)',
    ('Western', 'officer'): 'ambiguous: army officer or police officer; close to the Western foil policeman',
    ('Western', 'country'): 'ambiguous: nation or countryside (the same string was accepted in Horror and Fantasy)',
    ('Western', 'holdup'): 'near-synonym of the new robbery (WES_HH_17) and of robber (WES_HH_10)',
    ('Western', 'town sheriff'): 'near-synonym of new sheriff (WES_LH_03) and local sheriff (WES_LH_08)',
    ('Western', 'visit'): 'vague event word, hard to picture as a thing two films share',
    # Horror
    ('Horror', 'research'): 'abstract activity word',
    ('Horror', 'creation'): 'ambiguous: a created creature ("his creation") or the act of creating',
    ('Horror', 'land'): 'vague: land as property, territory or terrain',
    ('Horror', 'dead woman'): 'close to dead body (HOR_HH_07)',
    ('Horror', 'recorder'): 'ambiguous: tape recorder or the flute (the same string was accepted in Crime)',
    ('Horror', 'abortion'): 'sensitive topic that some participants may find upsetting',
    ('Horror', 'terrorist'): 'sensitive label; check it reads as a character type',
    # Science Fiction
    ('Science Fiction', 'suicide'): 'sensitive topic that some participants may find upsetting',
    ('Science Fiction', 'punishment'): 'abstract',
    # Crime
    ('Crime', 'minister'): 'ambiguous: clergy or government minister',
    # Comedy
    ('Comedy', 'young man'): 'close to young woman (COM_HL_02), old man (COM_HL_05) and young boy (COM_HL_10)',
    # Fantasy
    ('Fantasy', 'spirit'): 'ambiguous: a ghost or a mood ("in good spirits")',
    ('Fantasy', 'nation'): 'abstract or vague',
}'''
# Strings rejected in the review of the extension. See the note where EXTENSION_EXCLUDE is used.
EXTENSION_EXCLUDE_SRC = r'''{
    # round 1
    'flashback', 'script', 'crime scene',                                   # meta words, or the genre's own name
    'return', 'surprise', 'wrath', 'hiding', 'new life', 'price', 'corner', # idiom or summary residue
    'meaning', 'project', 'responsibility', 'comfort', 'energy', 'tension', # abstract discourse words
    'ring', 'burn', 'vessel', 'lie', 'sign', 'stage', 'violation', 'bill',  # ambiguous or possible parser errors
    'base', 'shaft', 'switch', 'ball',
    'parlor', 'keeper', 'baron',                                            # fragments of compounds
    # round 2 (replacements for round 1)
    'cinema',                                                               # meta word
    'respect', 'balance',                                                   # idiom residue
    'beauty',                                                               # ambiguous
    # round 3 (replacement for round 2)
    'danger',                                                               # idiom residue ("in danger")
}'''
for c in nb['cells']:
    if c['cell_type'] == 'code' and '__FLAGS__' in c['source']:
        c['source'] = c['source'].replace('__FLAGS__', FLAGS_SRC)
    if c['cell_type'] == 'code' and '__EXTENSION_EXCLUDE__' in c['source']:
        c['source'] = c['source'].replace('__EXTENSION_EXCLUDE__', EXTENSION_EXCLUDE_SRC)
nbf.write(nb, OUTPATH)
print(f'wrote {OUTPATH} with {len(cells)} cells')
