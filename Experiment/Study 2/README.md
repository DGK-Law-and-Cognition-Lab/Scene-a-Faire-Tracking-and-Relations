# Study 2 (SAF_STUDY2): Where Did a Shared Story Feature Come From?

Rebuilt November 18, 2026. Study 2 is the experiment the design memo of November 17
called 3A, with a mouse-tracked condition added. The two-genre choice study that
used to be Study 2 is retired; its build is kept, unchanged, in
`../Archive/Study 2 two-genre choice (retired 2026-11-18)/`.

Plain-JavaScript Pavlovia experiment built on the Study 1 code (no build step, no
PsychoJS). Every participant judges the Study 1 items of two genres, one story
feature at a time. What they are asked varies between participants:

| Condition | Response | Question |
| --- | --- | --- |
| `COPY` | rating, 1 to 7 | Both a screenplay and a later film include the feature. How strongly does this suggest that the film was copied from the screenplay? |
| `GENRE` | rating, 1 to 7 | How much is this in the film because of the kind of film it is? |
| `STOCK` | rating, 1 to 7 | Is this a stock feature of the genre (the Restatement's five adjectives)? |
| `TRACK` | mouse-tracked choice | The copying question as a choice between two boxes, **Copied** and **Coincidence** |

A fifth condition, `PROTECT` (should the screenwriter be able to stop the film's
makers from using this?), is written and runs with `?cond=PROTECT`, but it is not in
the design unless it is added to `CONDITIONS`.

The design, hypotheses, wording and power analysis are in
`Docs/Memorandum/Studies2to5_Design_Memo_2026-11-18.md` (Section 8 and Appendix A).
Nothing is preregistered yet.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Page shell (title "Judgments About Films"). Loads `experiment.js`. |
| `experiment.js` | The whole experiment: constants, Pavlovia plumbing, pages, rating pages, trial engine, frequency block, data record. |
| `style.css` | Study 1 styles plus the trial stage (`#mtStage`, `.mt-*`) and the Study 2 rating and frequency pages (`.rate-lead`, `.freq-*`). |
| `captcha.png` | Image for the hidden-instruction captcha trap (identical to Study 1's). |
| `stimuli/stimuli_<genre>.json` | The Study 1 items, copied unchanged from `../Study 1/stimuli/`: per genre 48 stratified items (12 in each cell of high or low prevalence by high or low distinctiveness) and 8 foils. |
| `stimuli/stimuli_all.js` | The same items as `window.STIMULI`, used only when `fetch` fails (for example over `file://`). |
| `deploy_to_pavlovia.sh` | Pushes the page files and stimuli to `genres-and-themes/experiment-2` only. Not itself uploaded. |
| `README.md` | This file. |

There is no `config.json`: Pavlovia serves the correct one, and one committed to the
repository would override it.

## Session

1. Device check (desktop or laptop only), full screen, captcha trap, consent (same
   UCLA Box link as Study 1).
2. Reading task: the two moving-window sentences of Study 1.
3. Instructions for the participant's condition (Next enabled after 15 s) and a task
   check with one retry. The correct answer is always the third option and describes
   the participant's own task. Failing both attempts is recorded, not enforced on the
   spot.
4. `TRACK` only: a mouse-tracked Stroop task (8 practice trials with feedback, then
   32 scored trials) and 4 practice copying choices about two Romance films.
5. For each of the two genres: familiarity (1 to 7), then the judgments.
   Rating conditions: the condition's wording, then the 56 items and two
   instructed-response attention checks ("please select 2", "please select 6") on
   pages of 8, in random order. `TRACK`: the dispute wording on the stage, then 56
   item trials and two instructed-response trials ("Attention check: choose Copied",
   "choose Coincidence") in random order.
6. Frequency estimates, the same in every condition: for 16 items from each genre (4
   per cell), three questions in three short blocks: how many of 100 films of the
   genre include the item; how many of 100 films of all kinds include it; how many of
   100 films that include it are films of the genre. Each answer is given on a slider
   from 0 to 100 (see "Frequency sliders" below).
7. Demographics, a question on legal training, `TRACK` only "Your Setup" (input
   device, hand, color vision), AI use, final questions, feedback, debrief.
8. Save to Pavlovia, then the SONA credit redirect (or the completion page when no
   redirect is set).

About 25 to 30 minutes in every condition.

### Assignment

A design cell is a condition crossed with one of Study 1's twelve genre schedules
(six genre pairs, each in two orders): 48 cells with four conditions.

- design cell = the numeric SONA survey code modulo 48 (a non-numeric code gets a
  random cell)
- condition = design cell modulo 4, in the order of `CONDITIONS` (COPY, GENRE, STOCK,
  TRACK), so consecutive sign-ups rotate through the conditions
- genre schedule = floor(design cell / 4), numbered as in Study 1 (`cell_index` 0 to
  11: wave A pairs 0 to 2, then wave B pairs 0 to 2; order 1, then order 2)

Three things are drawn at random for each participant and recorded: the side of the
Copied box (`copied_side`, `TRACK` only, fixed for the whole session), the frequency
item set (`freq_set`, 0 to 2) and the order of the three frequency questions
(`freq_order`).

Changing the number of entries in `CONDITIONS` changes the modulus, so settle the
list of conditions before the first real session.

### One mouse-tracked trial

The two boxes sit in the top corners and a Start button at the bottom center. A line
above the center of the screen says what the trial is about ("Two Westerns both
include:"). The participant clicks Start (the base) and starts moving up. The item
appears once the cursor has moved 40 px above the Start click (`DYNAMIC_START_PX`, a
dynamic start after Scherbaum and Kieslich, 2018). If the cursor has not moved up
within 2 s (`INIT_TIMEOUT_MS`), the item appears anyway and the trial is flagged
`late_start`. The trial ends with a click on a box. A response slower than 4 s from
onset in the copying choice (`SLOW_MS_COPY`; 3 s in the Stroop task, `SLOW_MS_STROOP`)
shows a short "please answer a little faster" reminder and is flagged `slow`. Cursor
samples are kept at most once per 8 ms (`MIN_SAMPLE_MS`); the Start click and the
response click are always recorded. Trials need a window of at least 800 by 550
pixels; a smaller window gets a "make the window larger" panel before each block.

### Frequency item sets

Within each genre and cell the 12 stratified items are ordered by id and dealt into
three sets (items 1, 4, 7, 10 of the cell are set 0; items 2, 5, 8, 11 are set 1;
items 3, 6, 9, 12 are set 2). A participant estimates one set, so each item is
estimated by about a third of the participants who saw its genre. Only the first 12
ids of a cell are used (`FREQ_POOL_PER_CELL`), so an extended item file would leave
the frequency block on the Study 1 items.

### Frequency sliders

Each estimate is a slider from 0 to 100 in steps of 1 (`FREQ_INPUT = 'slider'`). The
line shows no handle until the participant clicks it, so no starting position can pull
the answer, and an untouched slider counts as unanswered. The chosen number is shown
beside the item ("12 of 100 Westerns") and can be adjusted by dragging or with the
left and right arrow keys. The sliders run the full width of the page (about 550
pixels, so about 5 pixels per unit), because most corpus values are below 10 in 100
and small numbers have to be settable. Setting `FREQ_INPUT = 'number'` brings back a
typed whole number.

## Settings to check before launch

| Constant | Now | Note |
| --- | --- | --- |
| `CONDITIONS` | COPY, GENRE, STOCK, TRACK | Decide whether PROTECT runs before the first real session. |
| `SONA_URL_BASE` | empty | Set to the Study 2 listing's credit URL ending in `survey_code=`. While empty, SONA sessions end on the completion page instead of granting credit. Blank the credit token in any public copy. |
| `CONSENT_URL` | Study 1's Box link | Confirm it is right for Study 2. |
| `TRACK.copied`, `TRACK.coincidence` | Copied, Coincidence | The two box labels. |
| `SLOW_MS_COPY` | 4000 | Adjust after the investigators' own piloting. |
| `FREQ_INPUT` | slider | `'number'` gives a typed whole number instead. Check in piloting that small values (1 to 10) are easy to set. |
| `ESTIMATED_MINUTES` | 25 to 30 | Shown on the instructions page. Adjust after piloting. |
| `WELCOME_TITLE` and the page title in `index.html` | Judgments About Films | Should match the SONA listing's name. |
| `COMPLETION_CODE` | SAFSTUDY2 | Shown only on the fallback completion page (test sessions, or no redirect set). |
| Stimuli | the 288 Study 1 items and 48 foils | The memo recommends an extended set of 432 stratified items. If it is drawn (Notebook 10's queues) and reviewed, replace the six JSON files and `stimuli_all.js`; the rating and tracked blocks follow the files. |

The quoted adjectives in the `STOCK` wording are the Restatement's as the law review
manuscript quotes them. If the manuscript's check of the black-letter text changes
them, change `QUESTIONS.STOCK.intro` to match.

## Data columns

One row per participant, saved as `data/SAF_STUDY2_<pid>_SESSION_<date>.csv`.
JSON-valued columns are strings; parse them in analysis. Checklists are joined with `;`.

Identity and session: `participant_id`, `is_test` (id begins PILOT or TEST),
`short_test`, `platform`, `platform_source`, `prolific_pid`, `pavlovia_session`,
`start_time`, `end_time`, `total_duration_ms`, `n_pages`, `page_timestamps`,
`user_agent`, `device_type`, `device_self_report`, `screen_width`, `screen_height`,
`window_width`, `window_height`, `fullscreen_entered`, `fullscreen_exits`,
`fullscreen_exits_during_judgments`, `atlas_detected`, `captcha_response`,
`captcha_pass`, `consent`, `consent_time`.

Assignment: `condition`, `condition_source`, `conditions_in_design`, `design_cell`
(0 to 47; -1 when a test link forces something outside the design), `cell_index`
(genre schedule, 0 to 11), `wave`, `pair_index`, `order`, `g1`, `g2`, `g1_display`,
`g2_display`, `genre_order`, `genre_source`, `assignment_source`
(`survey_code_mod` or `random`), `copied_side`, `freq_set`, `freq_order`,
`stimuli_source`, `stimuli_meta`.

Reading task: for each sentence `spr1_*` and `spr2_*` (`_rts`, `_mean_rt`,
`_median_rt`, `_fast`, `_min_rt`, `_repeat_presses`, `_done`, `_understood`), and
`spr_fast_any`.

Task check: `task_check`, `task_check_pass`, `task_check_retry`,
`task_check_retry_pass`, `task_check_failed_both`.

Per genre slot N (1 or 2), every condition: `genreN_familiarity`, `genreN_order`
(item ids in the order shown), `genreN_n_judged`, `genreN_attention` (JSON),
`genreN_attention_pass`, `genreN_attention_total`, `genreN_rating_time_ms`,
`genreN_time_ms`. Across both: `attention_pass`, `attention_total` (4).

Rating conditions: `genreN_ratings`, a JSON list with one object per item: `pos`,
`item_id`, `text`, `cell_code` (HH, HL, LH, LL, FOIL; first letter prevalence, second
distinctiveness), `is_foil`, `home_genre`, `response` (1 to 7), `rt_ms` (page render
to first answer), `rt_last_ms`, `n_changes`, `page`.

`TRACK`: `genreN_trials`, a JSON list with one object per trial, and
`genreN_copied_n` (item trials answered Copied); also `stroop_trials` and
`practice_trials`, and the browser-side summaries `stroop_practice_correct`,
`stroop_n`, `stroop_correct`, `stroop_rt_congruent_median`,
`stroop_rt_incongruent_median` (correct trials only), `late_start_n`, `slow_n`,
`resize_trials_n`, `pointer_types`. Each trial object has:

- `type` (`stroop_practice`, `stroop`, `copy_practice`, `copy`, `catch`), `trial`
  (position in its sequence), `block` (genre slot)
- `text`, `left`, `right` (box labels), `side` (`left` or `right`), `choice` (the
  chosen label)
- `rt` (ms from onset to the response click), `onset` (ms from the Start click to
  onset), `late_start`, `slow`, `resizes`, `pointer` (`mouse`, `pen`, `touch`),
  `fullscreen`
- `layout`: `stage` [width, height] and `left`, `right`, `start` as [x, y, width,
  height] in window pixels at trial start
- `t`, `x`, `y`: the cursor samples. `t` is ms since the Start click; `x` and `y` are
  window pixels (y grows downward). The first sample is the Start click and the last
  is the response click.
- Copy trials: `genre`, `item_id`, `cell_code`, `is_foil`, `home_genre`. Catch trials:
  `item_id` (`ATT_COPIED`, `ATT_COINCIDENCE`), `correct`. Stroop trials: `word`,
  `ink`, `congruent`, `correct`.

Before computing mousetrap measures, flip y, mirror the trials so that one response
is always on the same side (use `copied_side`), and align each trial's start and end
points; `layout` gives the box and Start positions needed for this.

Frequency block: `freq_estimates`, a JSON list with one object per estimate: `type`
(`genre` = of 100 films of the genre; `all` = of 100 films of all kinds; `cue` = of
100 films that include it, how many are of the genre), `block` (1 to 3), `genre`,
`item_id`, `text`, `cell_code`, `value` (0 to 100), `page`, `pos`, `page_ms`, `first_ms`
(ms from the page appearing to the first action on that slider) and `changes` (how
many times the slider was set); `freq_n` (96 in a full session); and `freq_input`
(`slider` or `number`).

Questionnaires: `age`, `gender`, `race`, `race_other`, `native_language`,
`english_proficiency`, `films_per_month`, `film_knowledge`, `legal_training`;
`TRACK` only `input_device`, `mouse_hand`, `color_vision`, `fullscreen_maintained`;
`ai_usage`; `seriousness`, `distractions`, `feedback_procedure`, `feedback_other`.

The trajectories make a `TRACK` row large. If the upload fails, the file is
downloaded to the participant's computer and the completion page asks them to email
it.

## Local test

1. Start a server: the `study2` entry in `.claude/launch.json` (port 8767), or

   ```bash
   cd "Experiment/Study 2" && python3 -m http.server 8767
   ```

2. Open `http://localhost:8767/index.html?participant=PILOT_DK1&cond=COPY`. On
   localhost the experiment does not contact Pavlovia; the final page prints
   `=== STUDY DATA ===` with the full record to the console and downloads the CSV.
3. On the captcha page press `q`; pressing `z` (the hidden trap instruction) ends the
   session.
4. Useful additions:
   - `&cond=COPY`, `GENRE`, `STOCK`, `TRACK` or `PROTECT` forces the condition
   - `&gcell=0` to `11` forces the genre schedule; `&g1=western&g2=horror` forces any
     two genres
   - `&side=left` or `right`, `&fset=0` to `2`, `&forder=0` to `5` force the random
     draws
   - `&short=1` shortens everything (6 items per genre, 2 practice and 4 scored
     Stroop trials, 2 frequency items per genre, 1-second waits); recorded as
     `short_test`
   - `?platform=sona&survey_code=12347` runs as a SONA session (design cell 11:
     TRACK, Crime then Science Fiction; it redirects to SONA only once
     `SONA_URL_BASE` is set)

Syntax check without a browser: `node --check experiment.js`.

Verified locally on November 18, 2026: full `short=1` sessions in COPY, STOCK and
TRACK to the saved record, the wording and page counts of GENRE and PROTECT,
assignment from a numeric code, the task-check retry, the minimum-window panel, the
four attention checks in both response formats, and the frequency sliders (real
clicks and arrow keys, and the refusal to continue with an untouched slider). Not yet run by a person with a real mouse, and not yet deployed.

## Deploying

Run `./deploy_to_pavlovia.sh` from this folder. It clones
`genres-and-themes/experiment-2`, stops if the clone points anywhere else, is empty,
or holds Study 1's experiment, copies `index.html`, `experiment.js`, `style.css`,
`captcha.png` and the seven stimuli files, removes the retired build's two item files
if they are there, creates `data/.gitkeep` if needed, shows the changes, and pushes
only after you type `experiment-2`. It never pushes `config.json`. Git asks for your
Pavlovia GitLab username and password or token.

Then run one pilot session per condition with the test links the script prints, and
check that each file appears in the project's data before opening the SONA listing.
Pilot ids (PILOT or TEST) are flagged `is_test`. The SONA listing should exclude
Study 1 participants, who have seen the items.
