# Scènes à Faire: Tracking and Relations

Working materials for the studies that follow Study 1 of the scènes à faire project.
Study 1, the corpus method and the law review article *Common or Characteristic? An
Empirical Method for Scènes à Faire* live in a separate repository,
`DGK-Law-and-Cognition-Lab/SceneAFaire`, which stays as it is for that article.

Study 1 asked what a genre leads people to expect. These studies ask the question a
copyright dispute poses: two works share a story feature, so where did the later work
get it? It might be there because films of every kind have it, because films of its
genre have it, or because it was copied. Each possibility is answered by a different
count from the corpus, and the studies test whether people's judgments follow the
count that answers the question they are asked.

**Status (November 18, 2026).** This is a working repository. Nothing here is
preregistered and no data have been collected. Study 2 is built and has been run
locally; Studies 3 to 5 are designs.

## The studies

| Study | What it does | Status |
|---|---|---|
| 2 | One shared story feature at a time. The question varies between participants: how strongly it suggests copying, how much it is there because of the genre, or whether it is a stock feature (ratings), and the copying judgment again as a mouse-tracked choice between "Copied" and "Coincidence" | Experiment built; not preregistered |
| 3 | Pairs of shared features in which one implies the other, or does not | Design |
| 4 | Two synopses in a copying dispute, after Spellman and Holyoak (1996): the kind of features they share, how those features are arranged, and the side the participant is on | Design |
| 5 | The same judgments when an expert's counts are shown, and which count is shown | Design |

A note on numbering. The first design memorandum (November 17, 2026) called these
Experiments 3A to 3D. An earlier Study 2, a mouse-tracked choice between two genres,
was retired on November 18, 2026 before it was preregistered or run, and is not in
this repository.

A note on words. The text calls the unit a *story feature*. Code, tables and file
names inherited from the corpus pipeline call it an `element`. They are the same
thing.

## What is in this repository

| Folder | Contents |
|---|---|
| `Docs/Memorandum/` | The design memorandum for Studies 2 to 5: the Markdown master, the Word version, its figures, and the script that builds the Word version. It sets out the causal model, the hypotheses (labeled S2-H1, S3-H1 and so on), the wording of every question, the power analysis and the open decisions. |
| `Experiment/Study 2/` | The Study 2 experiment for Pavlovia in plain JavaScript, with its own README (session, assignment, data columns, test links). The items are Study 1's. The SONA credit address is empty. |
| `Analysis/notebooks/` | `_build_18.py` and the notebook it generates, `18_studies2to5_design.ipynb`: the three corpus quantities for every story feature and genre, the Study 1 items under the model, what two unrelated films share, and candidate materials for Studies 3 and 4. |
| `Analysis/studies2to5_design/` | `design_inputs_from_study1.Rmd` (Study 1 item means, listing rates and variance components) and `studies2to5_power.Rmd` (power simulations for all four studies). |
| `Analysis/v4_rebuild/18_studies2to5_design/` | Small outputs of those files: summary tables, the text report, the power results and the figures. |

The folder layout mirrors the project's.

## What these files depend on

The notebook reads tables produced by the corpus pipeline of the law review
repository (`Analysis/v4_rebuild/01c_union/`, `02_elements/`, `03b_classification/`,
`03c_network/` and `10_human_study_stimuli/`), so it runs when this repository's
`Analysis` folder is laid over that one. `design_inputs_from_study1.Rmd` reads the
registered Study 1 analysis and the Study 1 session files, which are not public; its
outputs here are summaries only. `studies2to5_power.Rmd` needs nothing but
`study1_h2_variance_components.csv`, which is included, and can be knit as it stands:

```bash
Rscript -e "rmarkdown::render('Analysis/studies2to5_design/studies2to5_power.Rmd', params = list(sims = 200, workers = 8))"
```

## Running Study 2 on your own computer

```bash
cd "Experiment/Study 2" && python3 -m http.server 8767
```

Then open `http://localhost:8767/index.html?participant=PILOT_1&cond=COPY` (or
`GENRE`, `STOCK`, `TRACK`). On the page with the image, press `q`. A local run does
not contact Pavlovia and saves nothing to it. `Experiment/Study 2/README.md` lists
the other test options.

## Contact

David G. Kamper, UCLA (davidgkamper@ucla.edu).

## A note on paths

The memorandum's Appendix E and the Study 2 README name some project files that are
not in this repository (the retired two-genre build, the superseded memorandum, the
archive folders). Absolute paths in the notebook's builder and printed output have
been replaced by placeholders (`/Users/USER`, `GoogleDrive-ACCOUNT`).
