#!/usr/bin/env python3
# Builder for notebooks/19_event_pairs_design.ipynb
# Run:  python3 notebooks/_build_19.py      (from the Analysis folder)
import nbformat as nbf

OUTPATH = 'notebooks/19_event_pairs_design.ipynb'
nb = nbf.v4.new_notebook()
cells = []
def md(s):   cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
def code(s): cells.append(nbf.v4.new_code_cell(s.strip("\n")))

md(r"""
# Notebook 19. Events as the second member of a pair: stability, counts and candidates

Added November 19, 2026, for Study 2 of the tracking paper (pairs of shared story features). That study shows people two things a screenplay and a later film share and asks how strongly the pair suggests copying. This notebook asks whether a new kind of pair can be built: a noun, then the same noun with what happens to it ("a stagecoach", then "a stagecoach is robbed"). Counting only. No language model is called and nothing upstream changes. Outputs go to `v4_rebuild/19_event_pairs_design/`.

The events are those of Notebook 13: a verb with its object ("rob stagecoach") or a verb with a preposition and its object ("ride into town"), found by a grammatical parser, counted once per film. The nouns are the noun story features of Notebook 03.

**Part 1** checks how stable the event scores are, with the split-half method Notebook 14 used for nouns. **Part 2** counts how many events each of the six study genres has at three floors. **Part 3** links each event to its object noun and computes, for each pair in each genre, how often the event goes with the noun and how much the event adds to the noun as evidence of copying.

The six genres are Western, Horror, Crime, Science Fiction, Comedy and Fantasy. The study's rule for noun pairs is that each member is in at least 20 of the genre's films.
""")

code(r"""
import shutil, tempfile, time
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import sparse
from scipy.stats import spearmanr

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
OUT = V4 / '19_event_pairs_design'
OUT.mkdir(parents=True, exist_ok=True)
TMP = Path(tempfile.mkdtemp())
def read_parquet(p, **kw):
    local = TMP / p.name          # Drive sometimes serves partial parquet files; read a local copy
    shutil.copy(p, local)
    return pd.read_parquet(local, **kw)

SEED = 20260219                   # the project seed; Notebook 14 drew its split with it
SIX = ['Western', 'Horror', 'Crime', 'Science Fiction', 'Comedy', 'Fantasy']
MIN_EVENT_FILMS = 10              # Notebook 13's rule: an event must be in at least 10 films
META_WORDS = {'film', 'movie', 'story', 'scene', 'cartoon', 'plot', 'audience', 'viewer', 'credit', 'credits',
              'narrator', 'flashback', 'episode', 'sequence', 'short', 'sequel', 'title'}   # copied from Notebook 13
NOUN_FLOOR = 20                   # the study's rule for single story features
EVENT_FLOORS = [10, 15, 20]
SPLITS = [(0.15, 0.05), (0.10, 0.05), (0.20, 0.05), (0.15, 0.02)]   # (common if above, rare if below); the first is the main one
report = []
def out(s=''):
    print(s); report.append(s)
print('V4 =', V4); print('OUT =', OUT)
""")

md(r"""
## Load the films, the events and the nouns

Genres come from the union corpus, as in Notebooks 13 and 14. The events are rebuilt from Notebook 13's event index with Notebook 13's own rules (events about the summary itself set aside, at least 10 films), and their counts are checked against Notebook 13's scores. Noun counts are taken from the film-level index of Notebook 02, restricted to the nouns in the scored table of Notebook 03, so that a noun and an event are both counted as distinct films.
""")
code(r"""
t0 = time.time()
cls = read_parquet(V4 / '03b_classification' / 'stockiness_long_classified.parquet')
GEN = sorted(cls['genre'].unique())
films = read_parquet(V4 / '01c_union' / 'movies_union.parquet', columns=['union_id', 'genres_canonical'])
films['genres'] = films['genres_canonical'].map(lambda g: [str(x) for x in list(g)] if g is not None else [])
fid = {u: i for i, u in enumerate(films['union_id'])}
NF = len(films)
G = np.zeros((NF, len(GEN)), dtype=np.float32)
for i, gs in enumerate(films['genres']):
    for g in gs:
        if g in GEN:
            G[i, GEN.index(g)] = 1
N_g = G.sum(0)
gi_of = {g: i for i, g in enumerate(GEN)}

def film_matrix(df, key, keys):
    # films x items, 1 if the film has the item
    pos = pd.Series(np.arange(len(keys)), index=pd.Index(keys))
    r = df['union_id'].map(fid).to_numpy(); c = pos.reindex(df[key]).to_numpy()
    X = sparse.csr_matrix((np.ones(len(df), dtype=np.float32), (r, c)), shape=(NF, len(keys)))
    X.data[:] = 1
    return X

# events, with Notebook 13's rules
ev_idx = read_parquet(V4 / '13_event_elements' / 'event_index.parquet')
is_meta = ev_idx['event'].map(lambda e: any(w in META_WORDS for w in e.split()))
ev_idx = ev_idx[~is_meta].drop_duplicates()
tot = ev_idx.groupby(['event', 'event_type'])['union_id'].nunique()
keep = tot[tot >= MIN_EVENT_FILMS].reset_index()[['event', 'event_type']]
keep['ekey'] = keep['event'] + '|' + keep['event_type']
ev_idx = ev_idx.merge(keep, on=['event', 'event_type'])
EV = keep.reset_index(drop=True)
XE = film_matrix(ev_idx, 'ekey', EV['ekey'].tolist())
nE_g = np.asarray(XE.T @ G); nE = np.asarray(XE.sum(0)).ravel()

# check against Notebook 13's scores
sc13 = read_parquet(V4 / '13_event_elements' / 'event_scores.parquet')
chk = sc13.assign(ekey=sc13['event'] + '|' + sc13['event_type'])
pos = pd.Series(np.arange(len(EV)), index=EV['ekey'])
mine = nE_g[pos.reindex(chk['ekey']).to_numpy(), chk['genre'].map(gi_of).to_numpy()]
assert len(EV) == chk['ekey'].nunique() == 18724, (len(EV), chk['ekey'].nunique())
assert np.array_equal(mine.astype(int), chk['film_count'].to_numpy()), 'event counts differ from Notebook 13'
print(f'{len(EV):,} events, counts identical to Notebook 13 event_scores.parquet')

# nouns of the scored table (Notebook 03), counted as distinct films from the Notebook 02 index
noun_tab = cls[cls['element_type'] == 'noun'][['element', 'is_narrative_element']].drop_duplicates('element').reset_index(drop=True)
el_idx = read_parquet(V4 / '02_elements' / 'element_index.parquet').drop_duplicates()
nidx = el_idx[(el_idx['element_type'] == 'noun') & el_idx['element'].isin(set(noun_tab['element']))]
XN = film_matrix(nidx, 'element', noun_tab['element'].tolist())
nO_g = np.asarray(XN.T @ G)
# compare with the film counts in the scored table
cn = cls[cls['element_type'] == 'noun']
npos = pd.Series(np.arange(len(noun_tab)), index=noun_tab['element'])
mine_n = nO_g[npos.reindex(cn['element']).to_numpy(), cn['genre'].map(gi_of).to_numpy()].astype(int)
agree_n = float((mine_n == cn['film_count'].to_numpy()).mean())
out('NOTEBOOK 19. EVENTS AS THE SECOND MEMBER OF A PAIR (counting only)')
out(f'{NF:,} films; {len(EV):,} events (counts identical to Notebook 13); {len(noun_tab):,} nouns in the scored table, {int(noun_tab["is_narrative_element"].sum()):,} kept as story features')
out(f'Noun film counts recounted from the Notebook 02 index equal the Notebook 03 film counts in {agree_n * 100:.2f}% of {len(cn):,} (noun, genre) cells')
print(f'{time.time() - t0:.0f} s')
""")

md(r"""
## Part 1. How stable are the event scores?

This repeats Notebook 14's Part B3 exactly. The films are split in half once at random: a random permutation of the films from `np.random.default_rng(20260219)`, the first half of it is half A and the rest is half B. Notebook 14 used one split, not several, and reported the raw Spearman correlation between halves with no correction for halving; the same is done here. On each half, prevalence is the genre's films with the event divided by the genre's films, and distinctiveness is (the genre's films with the event + α·P(genre)) divided by (films with the event + α), α = 1. Inside each genre the two halves are correlated across events (Spearman), and the correlation is averaged over the genres with at least 30 events at that level. Events are grouped by how many of the genre's films in the whole corpus have them.

Notebook 14 grouped story features in bands (5 to 19, 20 to 99, 100 or more films of the genre). The study needs floors (at least 5, 10, 20). Both are given. To put events and nouns on the same footing, the noun figures are also recomputed here on the same split: for Notebook 14's set (all story features of every grammatical type, which reproduces its report) and for single-word nouns kept as story features. A column with the Spearman-Brown value 2r ÷ (1 + r), the expected agreement for the full corpus rather than half of it, is added for reference; Notebook 14 did not report it.
""")
code(r"""
rng = np.random.default_rng(SEED)
perm = rng.permutation(NF)
A = np.zeros(NF, bool); A[perm[:NF // 2]] = True
B = ~A

def halves(X):
    res = []
    for m in (A, B):
        n_eg = np.asarray(X[m].T @ G[m]); n_e = np.asarray(X[m].sum(0)).ravel(); Ng = G[m].sum(0)
        res.append((n_eg / Ng, (n_eg + Ng / Ng.sum()) / (n_e[:, None] + 1.0)))
    return res, np.asarray(X.T @ G)

# Notebook 14's set: every story feature of every type
narr_pairs = cls[cls['is_narrative_element']][['element', 'element_type']].drop_duplicates().reset_index(drop=True)
narr_pairs['k'] = narr_pairs['element'] + '|' + narr_pairs['element_type']
ix = el_idx.merge(narr_pairs, on=['element', 'element_type'])
XS = film_matrix(ix, 'k', narr_pairs['k'].tolist())
XNn = XN[:, np.where(noun_tab['is_narrative_element'].to_numpy())[0]]
UNITS = {'events': XE, 'story features, all types (Notebook 14 set)': XS, 'nouns kept as story features': XNn}
H = {u: halves(X) for u, X in UNITS.items()}

LEVELS = [('band', '5 to 19', 5, 20), ('band', '20 to 99', 20, 100), ('band', '100 or more', 100, 10**9),
          ('floor', 'at least 5', 5, 10**9), ('floor', 'at least 10', 10, 10**9), ('floor', 'at least 20', 20, 10**9)]
NB14 = {'5 to 19': (0.222, 0.521), '20 to 99': (0.757, 0.803), '100 or more': (0.938, 0.934)}
sb = lambda r: 2 * r / (1 + r)
rows = []
for u, (((pA, dA), (pB, dB)), full) in H.items():
    for scheme, lab, lo, hi in LEVELS:
        rp, rd, n = [], [], 0
        per = {}
        for gi, g in enumerate(GEN):
            m = (full[:, gi] >= lo) & (full[:, gi] < hi)
            k = int(m.sum())
            if k >= 3:
                per[g] = (k, spearmanr(pA[m, gi], pB[m, gi])[0], spearmanr(dA[m, gi], dB[m, gi])[0])
            if k >= 30:
                rp.append(per[g][1]); rd.append(per[g][2]); n += k
        r = {'unit': u, 'scheme': scheme, 'films_in_genre': lab, 'genre': 'all genres (mean)', 'n_cells': n, 'n_genres': len(rp),
             'prevalence_r': np.mean(rp) if rp else np.nan, 'distinctiveness_r': np.mean(rd) if rd else np.nan}
        if scheme == 'band' and u.startswith('story features'):
            r['nb14_report_prevalence'], r['nb14_report_distinctiveness'] = NB14[lab]
        rows.append(r)
        for g in SIX:
            if g in per:
                k, a, b = per[g]
                rows.append({'unit': u, 'scheme': scheme, 'films_in_genre': lab, 'genre': g, 'n_cells': k, 'n_genres': 1,
                             'prevalence_r': a, 'distinctiveness_r': b})
            else:
                rows.append({'unit': u, 'scheme': scheme, 'films_in_genre': lab, 'genre': g, 'n_cells': int(((full[:, gi_of[g]] >= lo) & (full[:, gi_of[g]] < hi)).sum()), 'n_genres': 1})
rel = pd.DataFrame(rows)
rel['prevalence_r_spearman_brown'] = sb(rel['prevalence_r']); rel['distinctiveness_r_spearman_brown'] = sb(rel['distinctiveness_r'])
rel.to_csv(OUT / 'event_split_half.csv', index=False)

# Notebook 14 must be reproduced on its own set
chk14 = rel[(rel['scheme'] == 'band') & rel['unit'].str.startswith('story features') & (rel['genre'] == 'all genres (mean)')]
for r in chk14.itertuples():
    assert abs(r.prevalence_r - r.nb14_report_prevalence) < 0.0015 and abs(r.distinctiveness_r - r.nb14_report_distinctiveness) < 0.0015, r
out(''); out(f'PART 1. SPLIT-HALF STABILITY (one random half split, seed {SEED}, as in Notebook 14; raw Spearman between halves, mean over genres with 30+ cells)')
out("Notebook 14's band figures for story features are reproduced to three decimals on the same split.")
allg = rel[rel['genre'] == 'all genres (mean)']
for scheme in ['band', 'floor']:
    t = allg[allg['scheme'] == scheme].pivot_table(index='films_in_genre', columns='unit', values=['prevalence_r', 'distinctiveness_r'], sort=False)
    out(''); out(f'All genres, by {scheme} of films of the genre with the feature (prevalence r, distinctiveness r)')
    for lab in t.index:
        out(f'  {lab:<13}' + '   '.join(f"{u.split(',')[0].split(' (')[0][:22]:<22} {t.loc[lab, ('prevalence_r', u)]:.3f} / {t.loc[lab, ('distinctiveness_r', u)]:.3f}" for u in UNITS))
    cells_ = allg[allg['scheme'] == scheme].pivot_table(index='films_in_genre', columns='unit', values='n_cells', sort=False)
    out('  cells: ' + '; '.join(f"{lab}: " + ', '.join(f"{int(cells_.loc[lab, u]):,}" for u in UNITS) for lab in cells_.index))
out(''); out('Six study genres, floors (events | nouns kept as story features): n cells, prevalence r, distinctiveness r')
for g in SIX:
    parts = []
    for lab in ['at least 5', 'at least 10', 'at least 20']:
        e = rel[(rel['unit'] == 'events') & (rel['genre'] == g) & (rel['films_in_genre'] == lab)].iloc[0]
        nn = rel[(rel['unit'] == 'nouns kept as story features') & (rel['genre'] == g) & (rel['films_in_genre'] == lab)].iloc[0]
        parts.append(f"{lab[9:]}+: ev {e.n_cells} {e.prevalence_r:.2f}/{e.distinctiveness_r:.2f} | nn {nn.n_cells} {nn.prevalence_r:.2f}/{nn.distinctiveness_r:.2f}")
    out(f'  {g:<16} ' + ';  '.join(parts))
allg.round(3)
""")

md(r"""
## Part 2. How many events each genre has

The number of events in at least 10, 15 and 20 of the genre's films, for all events and for the two kinds that have an object noun (verb with object, verb with preposition and object). The earlier count at 20 films (Western 32, Fantasy 104, Science Fiction 124, Horror 444, Crime 509, Comedy 1,504) is checked against the first column.
""")
code(r"""
EARLIER = {'Western': 32, 'Fantasy': 104, 'Science Fiction': 124, 'Horror': 444, 'Crime': 509, 'Comedy': 1504}
has_obj = EV['event_type'].isin(['verb_object', 'verb_prep_object']).to_numpy()
rows = []
for g in SIX:
    c = nE_g[:, gi_of[g]]
    r = {'genre': g, 'films_in_genre': int(N_g[gi_of[g]])}
    for f in EVENT_FLOORS:
        r[f'events_at_least_{f}'] = int((c >= f).sum())
        r[f'object_events_at_least_{f}'] = int(((c >= f) & has_obj).sum())
    r['earlier_count_at_20'] = EARLIER[g]
    r['reproduced'] = r['events_at_least_20'] == EARLIER[g]
    rows.append(r)
counts = pd.DataFrame(rows)
counts.to_csv(OUT / 'event_counts_by_genre.csv', index=False)
out(''); out('PART 2. EVENTS PER GENRE (all kinds; in brackets, the kinds with an object noun)')
for r in counts.itertuples():
    out(f'  {r.genre:<16} {r.films_in_genre:>6,} films   10+: {r.events_at_least_10:>5,} ({r.object_events_at_least_10:,})   15+: {r.events_at_least_15:>5,} ({r.object_events_at_least_15:,})   20+: {r.events_at_least_20:>5,} ({r.object_events_at_least_20:,})   earlier 20+: {r.earlier_count_at_20:,} {"reproduced" if r.reproduced else "NOT reproduced"}')
counts
""")

md(r"""
## Part 3. Linking each event to its noun

An event of the kind verb with object is written verb, then noun ("rob stagecoach", "blow up bridge"); an event of the kind verb with preposition and object is written verb, preposition, noun ("ride into town"). In both, the object noun is the last word. It is linked to the noun story feature with exactly the same spelling in the scored table of Notebook 03 (grammatical type noun). Events of the kind subject with verb ("sheriff arrest") say what a noun does, not what happens to it, and are not linked. Both sides are dictionary forms, but they come from different passes: the events from spaCy's small English model (Notebook 13), the nouns from its large model (Notebook 02). So the films with an event need not all be among the films with its noun. For that reason P(E | O, g) below is computed from the films of the genre that have both the event and the noun, n(E and O), not from n(E).
""")
code(r"""
EV['noun'] = np.where(has_obj, EV['event'].str.split().str[-1], None)
EV['verb_part'] = np.where(has_obj, EV['event'].str.rsplit(n=1).str[0], None)
EV['linked'] = EV['noun'].isin(set(noun_tab['element']))
narr_set = set(noun_tab.loc[noun_tab['is_narrative_element'], 'element'])
EV['linked_story_feature'] = EV['noun'].isin(narr_set)
out(''); out('PART 3. LINKING EVENTS TO NOUNS')
for kind in ['verb_object', 'verb_prep_object']:
    d = EV[EV['event_type'] == kind]
    out(f'  {kind:<17} {len(d):>6,} events; linked to a noun in the scored table {d["linked"].mean() * 100:.1f}%; to a noun kept as a story feature {d["linked_story_feature"].mean() * 100:.1f}%')
d = EV[has_obj]
out(f'  both kinds        {len(d):>6,} events; linked {d["linked"].mean() * 100:.1f}%; to a story feature {d["linked_story_feature"].mean() * 100:.1f}%')
out(f'  all {len(EV):,} events (subject-verb events are not linked by design): linked {EV["linked"].mean() * 100:.1f}%')
# weighted by genre cells in the six genres at 10+ films
six_cells = np.stack([nE_g[:, gi_of[g]] >= 10 for g in SIX], 1)
w = six_cells[has_obj].sum(1)
out(f'  object events weighted by their (genre, event) cells with 10+ films in the six genres: linked {np.average(d["linked"], weights=w) * 100:.1f}%, to a story feature {np.average(d["linked_story_feature"], weights=w) * 100:.1f}%')
unl = d[~d['linked']]
out('  most frequent unlinked object nouns: ' + ', '.join(f'{n} ({c})' for n, c in unl['noun'].value_counts().head(12).items()))
non_story = d[d['linked'] & ~d['linked_story_feature']]
out('  most frequent linked nouns NOT kept as story features by the Notebook 03b classifier: ' + ', '.join(f'{n} ({c})' for n, c in non_story['noun'].value_counts().head(15).items()))
""")

md(r"""
## Part 3, continued. The quantities for every pair

For each linked pair (event E, noun O) and each of the six genres g, with N(g) the films of the genre:

n(O) is the films of g with the noun; n(E) the films of g with the event; n(E and O) the films of g with both. P(E | O, g) = n(E and O) ÷ n(O), the chance that a film of the genre that has the noun also has this event. P(O | g) = n(O) ÷ N(g) and P(E | g) = n(E) ÷ N(g). The weight of sharing the noun, in bits, is −log2 P(O | g); of sharing the event, −log2 P(E | g); the bits the event adds are the difference. Because a film with the event can lack the noun (different parses), the difference is also given in the strict form −log2 P(E | O, g), which is what the event adds to a noun already shared.

A pair qualifies when the noun is in at least 20 of the genre's films (the study's rule) and the event in at least 10. Flags mark the pairs whose event is in at least 15 and at least 20. The primary set uses nouns kept as story features by Notebook 03b; the counts are also given with every noun of the scored table, because the classifier set aside some nouns that matter here ("body", "life").
""")
code(r"""
L = EV[EV['linked']].reset_index()          # 'index' is the event's column in XE
ncol = npos.reindex(L['noun']).to_numpy()
XEl = XE[:, L['index'].to_numpy()]
XOl = XN[:, ncol]
XB = XEl.multiply(XOl).tocsr()               # films with both the event and its noun
nB_g = np.asarray(XB.T @ G)
nEl_g = nE_g[L['index'].to_numpy()]
nOl_g = nO_g[ncol]
nE_all = nE[L['index'].to_numpy()]
nO_all = np.asarray(XN.sum(0)).ravel()[ncol]
prior = N_g / N_g.sum()
rows = []
for g in SIX:
    gi = gi_of[g]
    t = pd.DataFrame({'genre': g, 'event': L['event'], 'event_type': L['event_type'], 'noun': L['noun'], 'verb_part': L['verb_part'],
                      'noun_is_story_feature': L['linked_story_feature'], 'N_g': int(N_g[gi]),
                      'n_O': nOl_g[:, gi].astype(int), 'n_E': nEl_g[:, gi].astype(int), 'n_E_and_O': nB_g[:, gi].astype(int),
                      'n_E_all_films': nE_all.astype(int), 'n_O_all_films': nO_all.astype(int)})
    t = t[(t['n_O'] >= NOUN_FLOOR) & (t['n_E'] >= 10)].copy()
    rows.append(t)
cand = pd.concat(rows, ignore_index=True)
cand['event_subset_of_noun'] = cand['n_E_and_O'] == cand['n_E']
cand['share_of_event_films_with_noun'] = cand['n_E_and_O'] / cand['n_E']
cand['P_E_given_O'] = cand['n_E_and_O'] / cand['n_O']
cand['P_E_given_O_from_nE'] = cand['n_E'] / cand['n_O']
cand['P_O_given_g'] = cand['n_O'] / cand['N_g']
cand['P_E_given_g'] = cand['n_E'] / cand['N_g']
cand['bits_noun'] = -np.log2(cand['P_O_given_g'])
cand['bits_event'] = -np.log2(cand['P_E_given_g'])
cand['bits_added'] = cand['bits_event'] - cand['bits_noun']
cand['bits_added_strict'] = -np.log2(cand['P_E_given_O'].clip(lower=1e-12))
cand['event_distinctiveness'] = (cand['n_E'] + cand['genre'].map(dict(zip(GEN, prior)))) / (cand['n_E_all_films'] + 1.0)
cand['noun_distinctiveness'] = (cand['n_O'] + cand['genre'].map(dict(zip(GEN, prior)))) / (cand['n_O_all_films'] + 1.0)
for f in EVENT_FLOORS:
    cand[f'event_at_least_{f}'] = cand['n_E'] >= f
cand = cand.sort_values(['genre', 'noun', 'P_E_given_O'], ascending=[True, True, False])
cand.to_csv(OUT / 'event_pair_candidates.csv', index=False)

out(''); out(f'PART 3. QUALIFYING PAIRS (noun in {NOUN_FLOOR}+ films of the genre, event in 10+), {len(cand):,} rows over the six genres')
out(f"  event films that also have the noun: {cand['event_subset_of_noun'].mean() * 100:.1f}% of pairs are a full subset; "
    f"{cand['n_E_and_O'].sum() / cand['n_E'].sum() * 100:.1f}% of all event films (pooled); median share per pair {cand['share_of_event_films_with_noun'].median():.3f}; "
    f"pairs below 80%: {(cand['share_of_event_films_with_noun'] < 0.8).sum():,}")
""")

md(r"""
### Counts per genre, the spread of P(E | O, g), and nouns with a common and a rare event

For the "same noun, two different events" design, a noun counts when, among its qualifying events, at least one has P(E | O, g) above the upper cut (common given the noun) and at least one has it below the lower cut (rare given the noun). The main split is above .15 against below .05. Three other splits are shown so the choice can be judged. A rare event needs the noun to be frequent: with the event in at least 10 films and P(E | O, g) below .05, the noun must be in more than 200 films of the genre.
""")
code(r"""
def common_rare(d, hi, lo):
    gb = d.groupby('noun')['P_E_given_O']
    ok = (gb.max() > hi) & (gb.min() < lo)
    return ok[ok].index.tolist()

rows, qrows = [], []
for g in SIX:
    for nounset in ['story features', 'all nouns']:
        dg = cand[cand['genre'] == g]
        if nounset == 'story features':
            dg = dg[dg['noun_is_story_feature']]
        for f in EVENT_FLOORS:
            d = dg[dg['n_E'] >= f]
            q = d['P_E_given_O'].quantile([0.25, 0.5, 0.75]) if len(d) else pd.Series([np.nan] * 3, index=[0.25, 0.5, 0.75])
            r = {'genre': g, 'nouns': nounset, 'event_floor': f, 'pairs': len(d), 'distinct_nouns': d['noun'].nunique(),
                 'distinct_events': d['event'].nunique(), 'nouns_with_2plus_events': int((d.groupby('noun').size() >= 2).sum()),
                 'P_E_given_O_q1': q[0.25], 'P_E_given_O_median': q[0.5], 'P_E_given_O_q3': q[0.75],
                 'bits_added_median': d['bits_added'].median()}
            for hi, lo in SPLITS:
                r[f'nouns_common_gt{hi:.2f}_rare_lt{lo:.2f}'] = len(common_rare(d, hi, lo))
            rows.append(r)
summary = pd.DataFrame(rows)
summary.to_csv(OUT / 'event_pair_counts_by_genre.csv', index=False)

out(''); out('Pairs per genre (nouns kept as story features; in brackets with all nouns), by the event floor')
for g in SIX:
    s = summary[summary['genre'] == g].set_index(['nouns', 'event_floor'])
    out(f'  {g:<16} ' + '   '.join(f"event {f}+: {s.loc[("story features", f), "pairs"]:,} ({s.loc[("all nouns", f), "pairs"]:,})" for f in EVENT_FLOORS))
out(''); out('P(E | O, g) among qualifying pairs, event 10+ (story-feature nouns): quartiles; median bits the event adds')
for g in SIX:
    s = summary[(summary['genre'] == g) & (summary['nouns'] == 'story features') & (summary['event_floor'] == 10)].iloc[0]
    out(f'  {g:<16} {s.pairs:>5,} pairs, {s.distinct_nouns:>4,} nouns   Q1 {s.P_E_given_O_q1:.3f}   median {s.P_E_given_O_median:.3f}   Q3 {s.P_E_given_O_q3:.3f}   median bits added {s.bits_added_median:.2f}')
out(''); out('Nouns with at least one common and one rare event (story-feature nouns; in brackets with all nouns)')
for hi, lo in SPLITS:
    col = f'nouns_common_gt{hi:.2f}_rare_lt{lo:.2f}'
    out(f'  split: common above {hi:.2f}, rare below {lo:.2f}')
    for g in SIX:
        s = summary[summary['genre'] == g].set_index(['nouns', 'event_floor'])
        out(f'    {g:<16} ' + '   '.join(f"event {f}+: {s.loc[('story features', f), col]} ({s.loc[('all nouns', f), col]})" for f in EVENT_FLOORS))
summary[summary['nouns'] == 'story features'].round(3)
""")

md(r"""
## Examples

**The clearest pairs.** For each genre, 15 pairs chosen by a fixed rule: the noun is kept as a story feature and is not on a short list of nouns that mostly appear in set phrases ("take place", "make way", "take care"); at least 80% of the event's films in the genre also have the noun, so the link is real; at most two events per noun; ranked by the event's distinctiveness in the genre, so that events tied to the genre come first. The list of set-phrase nouns is in the code below.

**Same noun, common and rare event.** For each genre, up to 10 nouns that pass the main split (above .15 and below .05, event in at least 10 films), ranked by the noun's distinctiveness in the genre. For each, the common event with the highest P(E | O, g) and the rare event with the most films are shown side by side, with the same filters as above.
""")
code(r"""
SET_PHRASE_NOUNS = {'place', 'way', 'care', 'advantage', 'part', 'time', 'turn', 'end', 'sight', 'attention', 'interest',
                    'note', 'fun', 'charge', 'hold', 'touch', 'control', 'sense', 'chance', 'look', 'mind', 'effect',
                    'action', 'use', 'notice', 'step', 'stand', 'pity', 'liking', 'offense', 'matter', 'thing', 'lot',
                    'rest', 'fact', 'point', 'side', 'order', 'course', 'trouble', 'decision', 'attempt', 'effort', 'idea'}
ok = cand[cand['noun_is_story_feature'] & ~cand['noun'].isin(SET_PHRASE_NOUNS) & (cand['share_of_event_films_with_noun'] >= 0.8)]
COLS = ['genre', 'noun', 'event', 'event_type', 'n_O', 'n_E', 'n_E_and_O', 'P_E_given_O', 'P_O_given_g', 'P_E_given_g',
        'bits_noun', 'bits_event', 'bits_added', 'bits_added_strict', 'event_distinctiveness', 'noun_distinctiveness']
ex_rows = []
for g in SIX:
    d = ok[ok['genre'] == g].sort_values(['event_distinctiveness', 'n_E'], ascending=False)
    d = d.groupby('noun', sort=False).head(2).head(15)
    ex_rows.append(d[COLS].assign(example_kind='clearest', rank=range(1, len(d) + 1)))
ex = pd.concat(ex_rows, ignore_index=True)

side = []
hi, lo = SPLITS[0]
for g in SIX:
    d = ok[ok['genre'] == g]
    nouns = common_rare(d, hi, lo)
    nd = d[d['noun'].isin(nouns)].groupby('noun')['noun_distinctiveness'].first().sort_values(ascending=False).head(10)
    for rank, noun in enumerate(nd.index, 1):
        dn = d[d['noun'] == noun]
        com = dn[dn['P_E_given_O'] > hi].sort_values('P_E_given_O', ascending=False).iloc[0]
        rar = dn[dn['P_E_given_O'] < lo].sort_values('n_E', ascending=False).iloc[0]
        side.append({'genre': g, 'example_kind': 'common_and_rare', 'rank': rank, 'noun': noun, 'n_O': int(com['n_O']),
                     'noun_distinctiveness': com['noun_distinctiveness'], 'bits_noun': com['bits_noun'],
                     'common_event': com['event'], 'common_n_E': int(com['n_E']), 'common_n_E_and_O': int(com['n_E_and_O']),
                     'common_P_E_given_O': com['P_E_given_O'], 'common_bits_added': com['bits_added'],
                     'rare_event': rar['event'], 'rare_n_E': int(rar['n_E']), 'rare_n_E_and_O': int(rar['n_E_and_O']),
                     'rare_P_E_given_O': rar['P_E_given_O'], 'rare_bits_added': rar['bits_added']})
side = pd.DataFrame(side)
pd.concat([ex, side], ignore_index=True).to_csv(OUT / 'event_pair_examples.csv', index=False)

out(''); out('CLEAREST PAIRS (noun ; event : n(O), n(E), n(E and O), P(E | O, g), bits added)')
for g in SIX:
    out(f'  {g}')
    for r in ex[ex['genre'] == g].itertuples():
        out(f'    {r.noun:<12} ; {r.event:<24} n(O) {r.n_O:>5}  n(E) {r.n_E:>4}  both {r.n_E_and_O:>4}  P(E|O) {r.P_E_given_O:.3f}  +{r.bits_added:.2f} bits')
out(''); out(f'SAME NOUN, COMMON AND RARE EVENT (common above {hi}, rare below {lo}; event 10+ films; filters as above)')
for g in SIX:
    d = side[side['genre'] == g] if len(side) else side
    out(f'  {g}: {len(d)} nouns shown')
    for r in d.itertuples():
        out(f'    {r.noun:<12} n(O) {r.n_O:>5}   common: {r.common_event:<22} {r.common_n_E_and_O:>4}/{r.n_O} = {r.common_P_E_given_O:.3f}   rare: {r.rare_event:<22} {r.rare_n_E_and_O:>3}/{r.n_O} = {r.rare_P_E_given_O:.3f}')
""")

md(r"""
## Outputs

In `v4_rebuild/19_event_pairs_design/`: `event_split_half.csv` (Part 1), `event_counts_by_genre.csv` (Part 2), `event_pair_candidates.csv` (every qualifying pair with its counts, probabilities and bits), `event_pair_counts_by_genre.csv` (pairs, quartiles and noun counts per genre, floor and split), `event_pair_examples.csv` (15 clearest pairs per genre and up to 10 nouns per genre with a common and a rare event), and `event_pairs_report.txt`.

The events come from a parser and have not been checked by hand. Some pairs will be parse errors or set phrases, and the examples should be read before any are used as stimuli.
""")
code(r"""
(OUT / 'event_pairs_report.txt').write_text('\n'.join(report) + '\n')
print(sorted(p.name for p in OUT.rglob('*') if p.is_file()))
""")

nb['cells'] = cells
nb['metadata'] = {'kernelspec': {'name': 'python3', 'display_name': 'Python 3', 'language': 'python'},
                  'language_info': {'name': 'python'}}
nbf.write(nb, OUTPATH)
print(f'wrote {OUTPATH} with {len(cells)} cells')
