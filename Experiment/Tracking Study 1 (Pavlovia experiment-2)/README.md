# Tracking paper, Study 1 (SAF_TRACK1): Where Did a Shared Story Feature Come From?

Three-group build, November 19, 2026. This is Study 1 of the tracking paper. It runs on
Pavlovia at `genres-and-themes/experiment-2`. (The completed study in the law review
article, which that article calls its Study 1, is called **the law review study** here.
Its experiment is in `../Study 1/` and its Pavlovia project is `experiment-1`, which is
closed and is never deployed to from this folder.)

Until November 19 this experiment was called Study 2 and had four groups. That build was
deployed once and nobody took it. It is kept in
`../Archive/Four-group build (deployed 2026-11-19, replaced by the three-group build)/`.

## The design in brief

Every participant answers **one question** about the items of **two genres**, one story
feature at a time, and answers it **in two ways**, one genre each.

| Question (between participants) | Rated genre: 1 to 7 | Tracked genre: two boxes |
| --- | --- | --- |
| `COPY` | Both a screenplay and a later film include the feature. How strongly does this suggest that the film was copied from the screenplay? | **Copied** or **Not copied** |
| `GENRE` | How much is this in the film because the film is a Western? | **Because of the genre** or **Could be in any film** |
| `STOCK` | Is this a stock feature of Westerns (the Restatement's five adjectives)? | **Stock** or **Not stock** |

Half of the participants answer their first genre with the mouse and their second with
ratings (`first_mode = track`); half do the reverse (`first_mode = rate`). So there are
three groups of people and six versions of the session.

The design, hypotheses, wording and power analysis are in
`Docs/Memorandum/Tracking_Studies_Design_Memo_2026-11-19.md` (Section 8 and Appendix A).
Nothing is preregistered yet.

## Is it randomized?

Assigned from the sign-up code, which is unrelated to anything about the participant:

- design cell = the numeric SONA survey code modulo 72 (a non-numeric code, such as a
  pilot id, gets a random cell)
- question = `QUESTION_ORDER[cell modulo 3]` (COPY, GENRE, STOCK)
- the way the first genre is answered = `MODE_ORDER[floor(cell / 3) modulo 2]` (track,
  rate); the second genre is answered the other way
- genre schedule = `floor(cell / 6)`, the law review study's twelve schedules (`cell_index`
  0 to 11: six genre pairs, each in two orders)

Across the 72 cells, under every question, each genre is rated and tracked equally often,
in first and in second position. (Checked: 144 consecutive codes fill each of the 72
combinations of genre, way, position and question exactly four times.) A study's SONA codes
are not consecutive, though, so in practice the cells fill as under a random draw: the law
review study's twelve cells received 6 to 18 sessions each. The three question groups will be
about equal, not exactly equal, which is why more than 315 sessions are posted for 100 usable
per question (memo Section 8.8).

Drawn at random for each participant, and recorded:

- the order of the items in each genre
- the positions of the two attention checks in each genre (between positions 10 and 50 of
  the rated genre's 58 entries, and between 10 and 74 of the tracked genre's 82 trials)
- which box label is on the left (`yes_side`; fixed for the whole session)
- which 12 of a cell's 18 items they rate in the rated genre (`SHOW_PER_CELL`). In the
  tracked genre nothing is drawn: every item of the genre is shown
  (`SHOW_ALL_WHEN_TRACKED`)
- which 4 of the items they judged in each cell they then estimate in the frequency
  block, and the order of the three frequency questions (`freq_order`)
- the Stroop trials and the order of the practice choices

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Page shell (title "Judgments About Films"). Loads `experiment.js`. |
| `experiment.js` | The whole experiment: constants, Pavlovia plumbing, pages, rating pages, trial engine, frequency block, data record. Plain JavaScript, no build step. |
| `style.css` | The law review study's styles plus the trial stage (`#mtStage`, `.mt-*`) and the rating and frequency pages. |
| `captcha.png` | Image for the hidden-instruction captcha trap (identical to the law review study's). |
| `stimuli/stimuli_<genre>.json` | The item pool: per genre the law review study's 56 items unchanged (48 stratified and 8 foils), followed by 24 new stratified items, so 18 in each cell of high or low prevalence by high or low distinctiveness. `in_law_review_study` marks which are which. Copied from `Analysis/v4_rebuild/20_extended_item_set/`. |
| `stimuli/stimuli_all.js` | The same items as `window.STIMULI`, used only when `fetch` fails. |
| `deploy_to_pavlovia.sh` | Pushes the page files and stimuli to `genres-and-themes/experiment-2` only. Not itself uploaded. |

There is no `config.json`: Pavlovia serves the correct one.

## Session

1. Device check (desktop or laptop with a mouse or trackpad), full screen, captcha trap,
   consent (the law review study's UCLA Box link).
2. Reading task: two moving-window sentences.
3. Instructions for the participant's question, which say that they will answer in two
   ways and in which order (Next after 15 s), and a task check with one retry. The correct
   answer is always the third option.
4. Genre 1, then a page saying that the genre and the way of answering change and the
   question stays the same, then genre 2.
   In the rated genre a participant judges 56 items: the 8 foils and 12 of the 18
   stratified items of each cell, drawn at random for that participant. In the tracked
   genre a participant judges all 80 items of the genre (72 stratified and 8 foils),
   because the measures taken from the pointer depend on the number of tracked trials
   each participant makes.
   - **Rated genre:** familiarity (1 to 7), the question's wording, then 56 items and two
     instructed-response attention checks ("please select 2", "please select 6") on pages
     of 8.
   - **Tracked genre:** a mouse-tracked Stroop task (8 practice trials with feedback, 32
     scored trials), 4 practice choices about Romance films with the participant's own two
     boxes, familiarity, the question's wording, then 80 item trials and two
     instructed-response trials (one naming each box).
5. Frequency estimates, the same for everyone: for 16 of the items they judged in each
   genre (4 per cell, drawn at random, the same items for all three questions), three
   questions in three short blocks, on sliders from 0 to 100 with no handle until clicked.
6. COPY group only: one closing question on how the participant read "copied" (as a
   question of fact, or as a question of what belongs to the screenwriter; the first two
   answers in random order).
7. Demographics, legal training, "Your Setup" (mouse or trackpad, hand, color vision), AI
   use, final questions, feedback, debrief (which says the pointer's path was recorded).
8. Save to Pavlovia, then the SONA credit redirect, or the completion page when no
   redirect is set. If the upload fails, the data file is downloaded and the participant
   sees a request to email it, with a button to go on for credit.

About 30 minutes for everyone, to be fixed after the investigators' own sessions.

### One mouse-tracked trial

The two boxes sit in the top corners and a Start button at the bottom center. A line above
the center says what the trial is about ("Two Westerns both include:", "A Western
includes:", "In Westerns:"). The participant clicks Start and starts moving up. The item
appears once the pointer has moved 40 px above the Start click (`DYNAMIC_START_PX`, a
dynamic start after Scherbaum and Kieslich, 2018). If the pointer has not moved up within
2 s (`INIT_TIMEOUT_MS`), the item appears anyway and the trial is flagged `late_start`.
The trial ends with a click on a box. A response slower than 4 s from onset
(`SLOW_MS_CHOICE`; 3 s in the Stroop task) shows a short "please answer a little faster"
reminder and is flagged `slow`. Pointer samples are kept at most once per 8 ms; the Start
click and the response click are always recorded.

Safeguards: the window must be at least 800 by 550 pixels, checked on every instruction
panel and again between trials (the trials pause until it is large enough; counted in
`size_prompts`). A click on Start within 250 ms of its appearing, or from the keyboard, is
ignored. A click on a box before the item appears is ignored. Instruction panels keep
their button disabled for 8 to 12 s, counted from when the text is actually shown.

A trackpad moves the same pointer and is recorded in the same way as a mouse. A touch
screen is not: touch drags produce no path (flagged by `pointer: touch` and `late_start`).

## Settings to check before launch

| Constant | Now | Note |
| --- | --- | --- |
| `SONA_URL_BASE` | the law review study's return link (SONA study 3298) | Set on November 19, 2026, because David said the SONA listing will have the same return link. It must match the completion URL shown on the listing (same `experiment_id` and `credit_token`); a new SONA listing has its own. When it is empty, SONA sessions end on the completion page and give no credit, and the deploy script warns. The public repository's copy keeps it empty. |
| `CONSENT_URL` | the law review study's Box link | Confirm it is right for this study. |
| Box labels (`QUESTIONS.<q>.yes`, `.no`) | Copied / Not copied; Because of the genre / Could be in any film; Stock / Not stock | "Not copied" replaced "Coincidence" on November 19 (David). |
| `SLOW_MS_CHOICE` | 4000 | Adjust after the investigators' own sessions. |
| `ESTIMATED_MINUTES` | 30 | Shown on the instructions page. Adjust after the investigators' own sessions. |
| `WELCOME_TITLE` and the page title | Judgments About Films | Should match the SONA listing's name. |
| Stimuli | 432 stratified items (18 per cell and genre: the law review study's 288 and 144 new ones) and 48 foils | In the rated genre each participant is shown 12 of a cell's 18 (`SHOW_PER_CELL`), drawn at random. In the tracked genre each participant is shown all 18 (`SHOW_ALL_WHEN_TRACKED`). The new items are drawn by `Analysis/notebooks/20_extended_item_set.ipynb`; the review and the list are in `Analysis/v4_rebuild/20_extended_item_set/extension_review_log.md`. David confirmed the new items on November 19, 2026. |

The quoted adjectives in the `STOCK` wording (`STOCK_RULE`) are the Restatement's as the
law review manuscript quotes them. If the manuscript's check changes them, change
`STOCK_RULE` to match.

## Data columns

One row per participant, saved as `data/SAF_TRACK1_<pid>_SESSION_<date>.csv`. JSON-valued
columns are strings; parse them in analysis with R or Python (Excel cuts a cell at 32,767
characters, and the trial columns are longer). Key items on `item_id`, never on the text:
a few texts ("best friend", "police officer") appear in both genres of a pair.

Identity and session: `participant_id`, `is_test` (id begins PILOT or TEST), `short_test`,
`platform`, `platform_source`, `prolific_pid`, `pavlovia_session`, `start_time`,
`end_time`, `total_duration_ms`, `n_pages`, `page_timestamps`, `user_agent`,
`device_type`, `device_self_report`, `screen_width`, `screen_height`, `window_width`,
`window_height`, `fullscreen_entered`, `fullscreen_exits` (whole session),
`fullscreen_exits_through_judgments` (page load to the end of both genres),
`atlas_detected`, `captcha_response`, `captcha_pass`, `consent`, `consent_time`.

Assignment: `question` (COPY, GENRE, STOCK), `first_mode` (track, rate), `condition`
(the two joined, for example `COPY_TRACK_FIRST`), `g1`, `g2`, `g1_display`, `g2_display`,
`genre_order`, `g1_mode`, `g2_mode` (track or rate for each genre slot), `tracked_genre`,
`rated_genre`, `design_cell` (0 to 71; -1 when a test link forces a genre pair outside
the design), `cell_index` (genre schedule, 0 to 11), `wave`, `pair_index`, `order`,
`assignment_source`, `question_source`, `first_mode_source`, `genre_source`
(`survey_code_mod`, `random` or `url...`), `questions_in_design`, `yes_side`, `box_yes`,
`box_no`, `box_left`, `box_right`, `items_per_cell_shown` (in the rated genre),
`tracked_genre_shows_all`, `freq_order`, `stimuli_source`,
`stimuli_meta`.

Reading task: `spr1_*`, `spr2_*` (`_rts`, `_mean_rt`, `_median_rt`, `_fast`, `_min_rt`,
`_repeat_presses`, `_done`, `_understood`), `spr_fast_any`.

Task check: `task_check`, `task_check_pass`, `task_check_retry`, `task_check_retry_pass`,
`task_check_failed_both`.

Per genre slot N (1 or 2), whichever way it was answered: `genreN_familiarity`,
`genreN_order` (item ids in the order shown), `genreN_n_judged`, `genreN_attention`
(JSON; `expected` is a number for a rated genre and a box label for a tracked one),
`genreN_attention_pass`, `genreN_attention_total`, `genreN_judgment_time_ms`,
`genreN_time_ms`. Across both: `attention_pass`, `attention_total` (4).

The rated genre: `genreN_ratings`, a JSON list with one object per item: `pos`, `item_id`,
`text`, `cell_code` (HH, HL, LH, LL, FOIL; first letter prevalence, second
distinctiveness), `is_foil`, `home_genre`, `response` (1 to 7), `rt_ms` (page render to
first answer), `rt_last_ms`, `n_changes`, `page`.

The tracked genre: `genreN_trials`, a JSON list with one object per trial, and
`genreN_yes_n` (item trials answered with the question's first label, `box_yes`). Also
`stroop_trials`, `practice_trials`, and the summaries `stroop_practice_correct`,
`stroop_n`, `stroop_correct`, `stroop_rt_congruent_median`,
`stroop_rt_incongruent_median` (correct trials only), `late_start_n`, `slow_n`,
`resize_trials_n`, `size_prompts`, `pointer_types`. Each trial object has:

- `type` (`stroop_practice`, `stroop`, `choice_practice`, `choice`, `catch`), `trial`
  (position in its sequence), `block` (genre slot)
- `text`, `left`, `right` (box labels), `side` (`left` or `right`), `choice` (the chosen
  label), and for item trials `chose_yes` (true when the choice is `box_yes`)
- `rt` (ms from onset to the response click), `onset` (ms from the Start click to onset),
  `late_start`, `slow`, `resizes`, `pointer` (`mouse`, `pen`, `touch`; a trackpad reports
  `mouse`, so use `input_device` to tell them apart), `fullscreen`
- `layout`: `stage` [width, height] and `left`, `right`, `start` as [x, y, width, height]
  in window pixels at trial start
- `t`, `x`, `y`: the pointer samples. `t` is ms since the Start click; `x` and `y` are
  window pixels (y grows downward). The first sample is the Start click and the last is
  the response click.
- Item trials: `genre`, `item_id`, `cell_code`, `is_foil`, `home_genre`. Catch trials:
  `item_id` (`ATT_YES`, `ATT_NO`), `correct`. Stroop trials: `word`, `ink`, `congruent`,
  `correct`.

Before computing mousetrap measures, flip y, mirror the trials so that one response is
always on the same side (use `yes_side`), and align each trial's start and end points;
`layout` gives the positions needed.

Frequency block: `freq_estimates`, a JSON list with one object per estimate: `type`
(`genre` = of 100 films of the genre; `all` = of 100 films of all kinds; `cue` = of 100
films that include it, how many are of the genre), `block` (1 to 3), `genre`, `item_id`,
`text`, `cell_code`, `value` (0 to 100), `page`, `pos`, `page_ms`, `first_ms`, `changes`;
`freq_n` (96 in a full session); `freq_input`.

Closing question, COPY group only: `copy_reading` (`fact` = how likely it is that the film's
makers took it from the screenplay; `own` = whether it fairly belongs to the screenwriter;
`both`; `other`) and `copy_reading_order` (the order in which the four answers were shown).

Response time in the tracked choices is `rt` in each trial object: ms from the appearance of
the item to the click on a box. It is a registered measure of conflict beside the path.

Questionnaires: `age`, `gender`, `race`, `race_other`, `native_language`,
`english_proficiency`, `films_per_month`, `film_knowledge`, `legal_training`,
`input_device`, `mouse_hand`, `color_vision`, `ai_usage`, `seriousness`,
`fullscreen_maintained`, `distractions`, `feedback_procedure`, `feedback_other`.

## Local test

1. Start a server: the `tracking-study1` entry in `.claude/launch.json` (port 8767), or

   ```bash
   cd "Experiment/Tracking Study 1 (Pavlovia experiment-2)" && python3 -m http.server 8767
   ```

2. Open `http://localhost:8767/index.html?participant=PILOT_DK1&cond=COPY&first=track`.
   On localhost the experiment does not contact Pavlovia; the final page prints
   `=== STUDY DATA ===` with the full record to the console and downloads the CSV.
3. On the captcha page press `q`; pressing `z` (the hidden trap instruction) ends the
   session.
4. Useful additions:
   - `&cond=COPY`, `GENRE` or `STOCK` forces the question; `&first=track` or `rate` forces
     which way comes first
   - `&gcell=0` to `11` forces the genre schedule; `&g1=western&g2=horror` forces any two
     genres
   - `&side=left` or `right` and `&forder=0` to `5` force two of the random draws
   - `&short=1` shortens everything (6 items per genre, 2 practice and 4 scored Stroop
     trials, 2 frequency items per genre, 1-second waits); recorded as `short_test`. In a
     short session the two attention checks are always the last two items.
   - `?platform=sona&survey_code=12347` runs as a SONA session (design cell 35: STOCK,
     ratings first, Fantasy then Comedy)

Syntax check without a browser: `node --check experiment.js`.

### What was checked on November 19, 2026

Full `short=1` sessions to the saved record in all six versions (three questions, two
orders), one of them assigned from a numeric code. The assignment over 144 codes. The
task-check retry. The counts of a full-length session (58 entries per genre, attention
checks between positions 10 and 50, 16 frequency items per genre, 4 per cell). The random
draws over 3,000 assignments. The small-window panel, before a block and between trials.
The guards on the Start button. The page a participant sees when the upload fails. An
independent read of the code found no serious defect. The smaller ones it found are
fixed: the wait on an instruction panel could run out behind the small-window message, the
window was not checked between trials, Start could be triggered from the keyboard or by a
double click, two columns had misleading names, and a failed upload was followed by an
immediate redirect.

Later on November 19, after the second copying box became "Not copied" and the item pool grew to
18 per cell: the item draw over 300 random participants (always 56 items per genre, 12 per cell,
every foil, each stratified item shown about two thirds of the time), the frequency items (4 per
cell, among the items judged, the same for all three questions), a load of the real 80-item files,
and one more full `short=1` session to the saved record.

The closing question of the COPY group was checked on its own page: it sits between the
frequency block and the questions about the participant, cannot be skipped, records the code
of the answer, and is absent for the other two groups.

After the tracked genre was set to show every item: with the real item files, the tracked
genre has 80 items (18 per cell and 8 foils) and 82 trials, the rated genre has 56 items and
58 entries, 200 redraws all gave those counts, the frequency items are among the items
judged, and the instructions say 30 minutes. The attention checks of the longer block were
moved to fall anywhere between trials 10 and 74 (20,000 draws; the rated genre's rule,
10 to 50, is unchanged). No full-length session has been run with 82 tracked trials.

These sessions were driven by a script in a hidden browser pane, so they check the logic
and the record, not the timing. **Nobody has yet taken the study by hand, on a laptop,
with a mouse or a trackpad.** That is the next check.

## Deploying

From a real terminal (the script asks you to type `experiment-2`, and git asks for your
Pavlovia username and password or token):

```bash
bash "Experiment/Tracking Study 1 (Pavlovia experiment-2)/deploy_to_pavlovia.sh"
```

That path is relative to the project's root folder. From any other folder, give the script's
full path.

It clones `genres-and-themes/experiment-2`, stops if the clone points anywhere else, is
empty, or holds the law review study's experiment, stops if `experiment.js` is not this
build or has a syntax error, copies `index.html`, `experiment.js`, `style.css`,
`captcha.png` and the seven stimuli files, shows the changes, and pushes only after you
type `experiment-2`. It never pushes `config.json`. It warns if `SONA_URL_BASE` is empty.

**Deployed by David**, three times on November 19, 2026 as the build changed and once more
after `SONA_URL_BASE` was set. On November 20 the eleven live files were downloaded and
compared with this folder and were identical: the 432-item pool, "Not copied", the closing
question, every item shown in the tracked genre, and the return link.

Then run one session per version with the six test links the script prints, and check
that each file appears in the project's data before opening the SONA listing. Pilot ids
(PILOT or TEST) are flagged `is_test`. The SONA listing should exclude participants of the
law review study, who have seen the items.
