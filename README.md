# Scènes à Faire: Tracking and Relations

Working materials for four planned studies on how people judge where a shared story
feature came from. They are Studies 1 to 4 of a paper of their own.

The corpus method, the completed study and the law review article *Common or
Characteristic? An Empirical Method for Scènes à Faire* live in a separate repository,
`DGK-Law-and-Cognition-Lab/SceneAFaire`, which stays as it is for that article. That
completed study is called **the law review study** here. (Inside the law review
repository it is "Study 1". It is not Study 1 of this repository.)

The law review study asked what a genre leads people to expect. These studies ask the
question a copyright dispute poses: two works share a story feature, so where did the
later work get it? It might be there because films of every kind have it, because films
of its genre have it, or because it was copied. Each possibility is answered by a
different count from the corpus, and the studies test whether people's judgments follow
the count that answers the question they are asked.

**Status (November 19, 2026).** This is a working repository. Nothing here is
preregistered and no data have been collected. Study 1 is built and has been run by
script in all six of its versions; nobody has yet taken it by hand. Studies 2 to 4 are
designs.

## The studies

| Study | What it does | Status |
|---|---|---|
| 1 | One shared story feature at a time. Three groups, one per question: does it suggest copying, is it in the film because of the genre, is it a stock feature. Every participant answers in two ways: ratings from 1 to 7 for one genre, and for another genre a choice between two boxes made with the mouse or trackpad while the pointer's path and the response time are recorded. The item pool has 432 stratified items, of which each participant is shown 48 per genre. | Experiment built; not preregistered |
| 2 | Pairs of shared features in which one implies the other, or does not; and a feature together with what happens to it (a stagecoach; a stagecoach is robbed). | Design |
| 3 | Two synopses in a copying dispute, after Spellman and Holyoak (1996): the kind of features they share, how those features are arranged, and the side the participant is on. | Design |
| 4 | The same judgments when an expert's counts are shown, and which count is shown. | Design |

A note on numbering. The first design memorandum (November 17, 2026) called these
Experiments 3A to 3D. On November 18 they became Studies 2 to 5, and the first of them
had four groups, only one of which used the mouse. On November 19 they became Studies 1
to 4 of their own paper, and Study 1 was redesigned as described above. The first commit
of this repository holds the November 18 version. An earlier and different "Study 2", a
mouse-tracked choice between two genres, was retired before it was preregistered or run
and is not in this repository.

A note on words. The text calls the unit a *story feature*. Code, tables and file names
inherited from the corpus pipeline call it an `element`. They are the same thing.

## What is in this repository

| Folder | Contents |
|---|---|
| `Docs/Memorandum/` | The design memorandum for Studies 1 to 4: the Markdown master, the Word version, its figures, and the script that builds the Word version. Each study's section opens with a one-page statement of its design. The memo sets out the causal model, the hypotheses (labeled S1-H1, S2-H1 and so on), the wording of every question, the power analysis and the open decisions. |
| `Experiment/Tracking Study 1 (Pavlovia experiment-2)/` | The Study 1 experiment for Pavlovia in plain JavaScript, with its own README (design, what is randomized, session, data columns, test links). The items are the law review study's. The SONA credit address is empty. |
| `Analysis/notebooks/` | `_build_18.py` and `18_tracking_studies_design.ipynb`: the three corpus quantities for every story feature and genre, the law review study's items under the model, what two unrelated films share, and candidate materials for Studies 2 and 3. `_build_19.py` and `19_event_pairs_design.ipynb`: events (a verb with its object) as material for Study 2, how stable their counts are, and the candidate pairs. `_build_20.py` and `20_extended_item_set.ipynb`: the 144 items added to Study 1's pool, drawn by continuing the law review study's seeded queues after reproducing its draw exactly. |
| `Analysis/tracking_studies_design/` | `design_inputs_from_law_review_study.Rmd` (item means, listing rates and variance components of the law review study) and `tracking_studies_power.Rmd` (power simulations for all four studies). |
| `Analysis/v4_rebuild/18_tracking_studies_design/`, `19_event_pairs_design/`, `20_extended_item_set/` | Small outputs of those files: summary tables, the text reports, the power results and the figures; and, for the item extension, the item files the experiment uses, the list of new items and the log of their review. |

The folder layout mirrors the project's. File and folder names carry no study number, so
that they do not have to change if the numbering does.

## What these files depend on

The notebooks read tables produced by the corpus pipeline of the law review repository
(`Analysis/v4_rebuild/01c_union/`, `02_elements/`, `03b_classification/`,
`03c_network/`, `10_human_study_stimuli/` and `13_event_elements/`; Notebook 20 also reads that
repository's `notebooks/_build_10.py`), so they run when this repository's `Analysis` folder is laid over
that one. `design_inputs_from_law_review_study.Rmd` reads the registered analysis and the
session files of the law review study, which are not public; its outputs here are
summaries only. `tracking_studies_power.Rmd` needs nothing but
`law_review_study_h2_variance_components.csv`, which is included. A full render takes
more than half an hour:

```bash
Rscript -e "rmarkdown::render('Analysis/tracking_studies_design/tracking_studies_power.Rmd', params = list(sims = 200, workers = 8))"
```

## Running Study 1 on your own computer

```bash
cd "Experiment/Tracking Study 1 (Pavlovia experiment-2)" && python3 -m http.server 8767
```

Then open `http://localhost:8767/index.html?participant=PILOT_1&cond=COPY&first=track`
(the question is `COPY`, `GENRE` or `STOCK`; `first` is `track` or `rate`). On the page
with the image, press `q`. A local run does not contact Pavlovia and saves nothing to it.
The README in that folder lists the other test options.

## Contact

David G. Kamper, UCLA (davidgkamper@ucla.edu).

## A note on paths

The memorandum's Appendix E and the Study 1 README name some project files that are not
in this repository (the retired builds, the superseded memoranda, the archive folders,
the law review study's experiment). Absolute paths in the notebooks' builders and printed
output have been replaced by placeholders (`/Users/USER`, `GoogleDrive-ACCOUNT`).
