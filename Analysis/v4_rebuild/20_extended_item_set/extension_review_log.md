# Review of the extended item set (November 19, 2026)

Study 1 of the tracking paper uses 18 items per cell and genre in place of the law review
study's 12. Notebook 20 (`Analysis/notebooks/_build_20.py`) continues each genre's seeded
queues (seed 20260219) from where Notebook 10 stopped, after first reproducing the law
review study's 48 stratified items per genre exactly. The 288 registered items and the 48
foils are unchanged. 144 items are new, 6 per cell and genre.

## How the new items were reviewed

Claude, the AI assistant, reviewed the new items by the standards of the law review
study's review (`../10_human_study_stimuli/stimuli_rejection_log.md`): idiom or summary
residue, meta words, ambiguous nouns, fragments of compounds and the genre's own name are
rejected. Abstract but recognizable story features are kept, and so is sensitive content,
as the investigator decided in October (race labels and sexual content were kept then).
Each rejection hands its place to the next candidate in the cell's seeded queue. The
review ran until a round rejected nothing.

**Investigator's confirmation: November 19, 2026.** David Kamper read the list below, with the
sensitive and vague items pointed out to him, and confirmed all 144 new items ("All are fine.").

## Rejected strings (36), in `EXTENSION_EXCLUDE`

They apply to the new items only, in every genre.

| Round | Ground | Strings |
|---|---|---|
| 1 | Meta words, or the genre's own name | flashback, script, crime scene |
| 1 | Idiom or summary residue | return, surprise, wrath, hiding, new life, price, corner |
| 1 | Abstract discourse words | meaning, project, responsibility, comfort, energy, tension |
| 1 | Ambiguous, or possible parser errors | ring, burn, vessel, lie, sign, stage, violation, bill, base, shaft, switch, ball |
| 1 | Fragments of compounds | parlor, keeper, baron |
| 2 | Meta word | cinema |
| 2 | Idiom residue | respect, balance |
| 2 | Ambiguous | beauty |
| 3 | Idiom residue ("in danger") | danger |

Round 1 replaced 32 items ("violation" had been drawn in two genres), round 2 replaced 4
and round 3 replaced 1. Eight further candidates were skipped by rule and not by review:
they overlap an item already selected, are a foil, or were already in the law review
study's `MANUAL_EXCLUDE` (the report lists them).

## The 144 new items

| Genre | Common and characteristic (HH) | Common, not characteristic (HL) | Rare, characteristic (LH) | Rare, not characteristic (LL) |
|---|---|---|---|---|
| Western | horse, cattle, gold, land, robbery, stranger | officer, mother, village, agent, boss, country | hired gun, holdup, town sheriff, bull, trader, gang member | funeral, rival, priest, table, visit, affair |
| Horror | laboratory, barn, gate, research, motel, creation | officer, train, shop, land, cousin, crowd | parasite, holy water, Molotov cocktail, dead woman, biker, recorder | abortion, virginity, older brother, terrorist, wealth, ticket |
| Science Fiction | experiment, clone, explosion, vehicle, ruins, lair | house, wife, love, murder, suicide, witness | homeworld, test subject, autopsy, news report, firefight, outside world | pill, gold, market, punishment, palace, contest |
| Crime | diamond, gang member, police station, assassination, beating, hotel room | love, letter, gold, teenager, minister, promise | corrupt cop, defendant, strip club, cargo, poisoning, pregnant wife | posse, clan, small village, younger sister, inn, misunderstanding |
| Comedy | millionaire, speech, dollar, inheritance, publicity, heiress | fear, young man, shelter, little girl, dead body, fighter | coconut, senior year, gymnasium, mistaken identity, trustee, bank manager | database, social worker, firearm, locket, phone call, remote village |
| Fantasy | battle, spirit, cave, god, guardian, chamber | revenge, prison, office, gun, truck, agent | fountain, apple, helmet, amnesia, submarine, successor | nation, holiday, alarm, client, nightclub, younger brother |

Two display texts differ from the pipeline strings, on the rule of the law review study's
display overrides: "Molotov cocktail" (capital) and "ruins" (plural).

## Kept, but worth a look

- **Sensitive content, kept on the October precedent:** abortion, virginity, terrorist and
  dead woman (Horror); suicide (Science Fiction); strip club and pregnant wife (Crime).
- **Vague or abstract, kept as recognizable:** land (Western, Horror), visit (Western),
  research (Horror), punishment (Science Fiction), nation (Fantasy), wealth (Horror),
  promise and misunderstanding (Crime).
- **Two readings, kept:** officer and country (Western), creation and recorder (Horror),
  minister (Crime), spirit (Fantasy).
- **Close in meaning to another item of the same genre:** robbery and holdup (Western, with
  the registered "robber"); town sheriff (Western, with "new sheriff" and "local sheriff");
  dead woman (Horror, with "dead body"); young man (Comedy, with "young woman", "old man"
  and "young boy").
- **"gang member"** is now an item in two genres, Western and Crime. Notebook 10 allows
  that.

## Do the cells still match?

Yes. Pooled over genres, with all 18 items per cell, median prevalence is 3.0% in the
common-and-characteristic cell against 3.3% in the common-not-characteristic cell (it was
3.2% against 3.3% with the registered 12), and 0.75% against 0.75% in the two rare cells.
Neither difference approaches significance (Mann-Whitney p = .67 and p = 1.00). Median
distinctiveness is 28.7% and 34.4% in the characteristic cells against 6.3% and 5.9% in the
others. On within-genre percentiles the new items do not differ from the registered ones
in any cell. The full tables, by genre, are in `extended_items_report.txt`.

The new items have no ratings from the law review study. Their everyday word frequency
(SUBTLEX-US) is filled for one measure (`Lg10CD`, 143 of 144) and mostly missing for the
other (`Lg10WF`); the join to the SUBTLEX-US file has to be run before the analysis that
uses it.
