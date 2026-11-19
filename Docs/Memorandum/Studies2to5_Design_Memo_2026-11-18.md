---
title: "Design Memorandum for Studies 2 to 5: Where Did a Shared Story Feature Come From?"
subtitle: "Copying, genre and coincidence in judgments about two works"
author: "Prepared for David Kamper, Keith Holyoak and Mira Patel"
date: "November 18, 2026. Revises the memorandum of November 17. Draft for discussion; nothing here is preregistered."
---

*What changed on November 18.* The memorandum of November 17 proposed a Study 3 made of four experiments, 3A to 3D, to follow a Study 2 that was a mouse-tracked choice between two genres. David has retired the two-genre study. The experiment that was 3A is now Study 2 and gains a condition in which the copying judgment is made with the mouse. The experiments that were 3B, 3C and 3D are Studies 3, 4 and 5. Hypotheses are numbered within each study (S2-H1, S3-H1 and so on) so that they cannot be mistaken for Study 1's H1 to H3. The Study 2 experiment has been rebuilt to this design and verified locally, and the analysis files have been renamed. Section 2.5 gives the reasons, Section 8.9 the new condition, Section 16 the decisions made and still open, and Appendix E the files.

# 1. Summary

Study 1 asked people what a genre leads them to expect. Studies 2 to 5 ask the question a copyright dispute actually poses: two works share a story feature, so where did the later work get it? The later work might have it because films of every kind do, because films of its genre do, or because its makers took it from the earlier work. Keith's note of November 13 put the dispute in exactly these terms, as a question about how the disputed work was generated, and Spellman and Holyoak (1996) supply a tested experimental form for it: participants act as writers in a plagiarism dispute between two soap operas and must say which character corresponds to which.

The memo sets out a small causal model in which the three possible sources of a shared feature are separate causes. In that model prevalence, incremental category validity and distinctiveness stop being rival measures of one thing. Each is the correct answer to a different question: whether the shared feature is evidence of copying (prevalence), how much the genre adds (the increment), and whether a feature already in the work is there because of the genre (distinctiveness). The memo then states three accounts of what people do when asked these questions, reports what the corpus already says about the design, and specifies four studies.

Study 2 presents one shared feature at a time and varies the question between participants. It reuses the 288 items of Study 1, so every item already has an expectedness norm from other participants. Its central test has the form of Study 1's H2c with the predictions reversed: if people reason about copying as the model does, judged evidence of copying falls with prevalence and ignores distinctiveness; if one intuition about what is typical of a genre drives every judgment, it falls with distinctiveness instead. A fourth group of participants makes the copying judgment as a choice between two boxes, "Copied" and "Coincidence," while the path of the mouse is recorded. The path can show what a rating cannot: whether the sense of what is typical of the genre pulls at the answer while it is being made, even where it does not decide it. Study 3 moves to pairs of shared features and asks whether people see that a feature implied by another adds little, which is the corpus form of the necessity question set aside on November 1. Study 4 is the Spellman and Holyoak paradigm with corpus-calibrated materials: pairs of synopses that share common or rare, characteristic or uncharacteristic features, arranged alike or scattered, judged from the plaintiff's side, the defendant's side or neither. Study 5 shows participants the counts themselves and tests the paper's practical claim that which count a fact-finder is shown decides the answer for features on which the two counts disagree.

The corpus work for this memo is in a notebook (`Analysis/notebooks/18_studies2to5_design.ipynb`) and two R files (`Analysis/studies2to5_design/`). Three of its results shape the design. The Study 1 cells are almost perfectly matched for this purpose: high- and low-distinctiveness items have the same prevalence within each prevalence level, so the two accounts make nearly uncorrelated item-level predictions (Spearman −.03 between the model's copying weight and distinctiveness). Two unrelated Westerns share a median of two story features, but the closest other Western to a given Western shares a median of fourteen or fifteen, which is the baseline a plaintiff's list of similarities has to beat. And Study 1's variance components show that the number of items, not the number of participants, limits precision, which sets the sample sizes in Section 7.

Section 16 lists the decisions made on November 18 and those still needed before any of this is preregistered.

# 2. Where Studies 2 to 5 come from

## 2.1 What Study 1 established and what it could not ask

Study 1 (131 usable participants, preregistered) had people list what they expect in a typical film of a genre and rate 48 items per genre for expectedness. Ratings followed distinctiveness about four times as strongly as prevalence (1.49 against 0.36 points on the seven-point scale; the difference, H2c, was −1.13 with a 95% interval from −1.50 to −0.76). Listing followed both (odds ratios of about 25 and 11 from the bottom to the top of a genre's ranking). Prevalence and distinctiveness kept apart predicted both tasks better than the composite (H3), and, in an exploratory analysis, better than incremental category validity.

Study 1's question was a category-to-feature question: given the genre, what do you expect? People answered it largely with feature-to-category information. That result is about expectation. It says nothing direct about the two judgments a court makes about a shared feature, which are whether the defendant took it and whether it is free for anyone to take.

## 2.2 Keith's two notes

Keith's first note (November 12) proposed correcting prevalence for the feature's base rate, $P(F \mid C) - P(F \mid S)$, with $S$ the superordinate category. His second (November 13) named it incremental category validity and gave the reason he likes it: it fits the causal direction the law implies. The dispute asks how the disputed work D was generated. The defendant answers that D's features came from the pressures of its genre; the plaintiff answers that they came from the earlier work W. Both answers reason from a cause to the features of D. He added that the increment is proportional to incremental cue validity and so may be the common core of prevalence and distinctiveness.

The corpus check of that note (Notebook 17, Part F) found the precise form of the claim. The two increments are one quantity, the excess of the joint rate over chance, divided by different base rates:

$$P(C)\,[P(F \mid C) - P(F)] = P(F)\,[P(C \mid F) - P(C)] = P(F, C) - P(F)P(C).$$

Within a genre the first increment orders features exactly by that excess and the second orders them as distinctiveness does. The law review now carries this, with a passage separating copying in fact from the filtering of a genre's stock. Section 4 below extends the same idea into a model with three causes, and the studies test it.

## 2.3 Spellman and Holyoak (1996)

The paradigm Keith pointed to is Experiment 3 of Spellman and Holyoak, "Pragmatics in Analogical Mapping," *Cognitive Psychology* 31, 307 to 346 (1996), whose materials are slightly modified from their 1993 Cognitive Science Society paper. Participants (128 University of Texas undergraduates) were told to pretend they were the writers of a successful soap opera, *Soap Opera University*, who were in court trying to prove that the writers of another soap opera, *Soap Opera City*, had stolen their ideas. Their own show had a professor, Peter, who was his research assistant Mary's boss, was in love with her, and had cheated his brother out of an inheritance. The other show had two sets of characters, lawyers and doctors, each of which partly matched Peter and Mary, so that on structure alone it was ambiguous who corresponded to whom.

Participants were told that a judge had seen a tape of the other show's next episode and found it "just like" one of two recent episodes of their own show, one about the professional relation and one about the romantic relation. They wrote what they thought happened on the tape (predicting it correctly "would be the strongest possible evidence" of stealing) and then mapped four characters of their show onto characters of the other. The goal set by the judge's tape decided the mappings: 88% wrote an analogous continuation and 97% of those followed the cued relation; on the mapping task 72% mapped in line with the cued relation. Information irrelevant to the goal, the inheritance relation, did not affect the plot extension (53% against 47%) but did resolve the mapping (65% against 35%). The authors simulated the pattern with ACME, treating the goal as an inhibitory filter on attention.

Much of this carries over. The cover story is a copying dispute between two narrative works, already validated as a task undergraduates can do. The dependent measures, predicting the other work and mapping its characters, are measures of analogical correspondence that the law's "substantial similarity" presupposes and never defines. The main finding, that the purpose for which two works are compared changes which correspondences people find, bears directly on a litigation setting in which the two sides have opposite purposes. What their materials lack, and what the corpus supplies, is any measure of how common or how characteristic the shared material is in its genre. Their soap operas share a professor, a boss, a romance and an inheritance; nothing in the study says whether sharing those is surprising.

Barbara Spellman, who took her doctorate at UCLA in 1993 and wrote these papers with Keith, is now Professor of Law at the University of Virginia, where she works on the psychology of evidence. The 1996 paper directs requests for the story materials to her. Section 16 proposes asking her for them and for her view of the design.

## 2.4 The necessity study set aside earlier

The one earlier candidate for a later study was a rating of how necessary a feature is given a story premise, dropped from the plan on November 1. Its corpus measure was to be how often features occur together within a genre, which Notebook 03c already counts. That study is not replaced here. It becomes Study 3, because in the model of Section 4 necessity is the conditional form of prevalence, and its legal role, discounting similarities that follow from a shared premise, is a prediction about judged evidence of copying.

## 2.5 The two-genre study, retired, and where mouse tracking went

From November 1 to November 18 Study 2 was a different experiment: a mouse-tracked choice between two genres for each of 555 items, built and verified but never preregistered or run. David retired it on November 18. Three things found while planning it and this program count against it. Its one new quantity, the weight people give to the size of a genre, cannot be separated from their liking for particular genres; in its power simulations the estimate had a standard deviation of about 0.45 to 0.5 however many participants were run. Within a pair of genres prevalence and distinctiveness order the items identically, so the design could not set a common feature against a characteristic one, which is the contrast the rest of this program turns on. And which of two genres a feature belongs to is none of the three questions of Table 2.

The method is worth keeping. When a person chooses between two answers by moving a mouse from a common start, the path bends toward the answer that loses, and bends more the more strongly that answer competed (Dale, Kehoe and Spivey, 2007; Freeman and Ambady, 2010). The copying judgment may be such a case. A rare but characteristic feature has two candidate answers: its typicality says the genre explains it, and its prevalence says an independent author was unlikely to arrive at it. Study 2 therefore has a fourth condition in which the copying judgment is made with the mouse (Section 8.9). It reuses the trial procedure and the Stroop practice built for the retired study, whose files are kept in `Experiment/Archive/`.

The studies are intended for one paper for a cognitive science journal, separate from the law review.

# 3. The legal questions the studies map onto

A copyright plaintiff must show two things about copying, and the cases keep them apart. In *Arnstein v. Porter* the Second Circuit required proof "(a) that defendant copied from plaintiff's copyrighted work and (b) that the copying (assuming it to be proved) went so far as to constitute improper appropriation" (154 F.2d 464 (2d Cir. 1946)). The Ninth Circuit uses the same division: the infringement element "has two distinct components: 'copying' and 'unlawful appropriation'" (*Rentmeester v. Nike, Inc.*, 883 F.3d 1111 (9th Cir. 2018)). Similarity that bears on the first question is often called probative similarity, after Latman (1990), to keep it distinct from the substantial similarity of protected expression that the second question requires.

The first question is a factual inference from similarity to its cause, and courts have long said that the inference depends on what else could explain the similarity. Judge Posner's formulation in *Ty, Inc. v. GMA Accessories* is that copying may be inferred when two works are "so similar to each other and not to anything in the public domain that it is likely that the creator of the second work copied the first" (132 F.3d 1167 (7th Cir. 1997)). The phrase "and not to anything in the public domain" is a base-rate condition. A genre's conventions are the nearest thing a film has to a public-domain source, and prevalence within the genre measures how likely an independent author was to arrive at the feature.

The second question is where scènes à faire formally sits. Material that is stock for the kind of work is filtered out before the works are compared. Two refinements matter for the design. A selection and arrangement of stock material can itself be protected: "[t]he particular sequence in which an author strings a significant number of unprotectable elements can itself be a protectable element" (*Metcalf v. Bochco*, 294 F.3d 1069 (9th Cir. 2002)). And courts distrust lists of similarities, which "are inherently subjective and unreliable," particularly where "the list emphasizes random similarities scattered throughout the works" (*Litchfield v. Spielberg*, 736 F.2d 1352 (9th Cir. 1984)). The *Metcalf* rule is a claim that relational structure counts apart from the features it relates. The *Litchfield* caution is a claim that features without shared structure count for little, and that advocates compile them selectively. Both are claims about analogical mapping, and both are testable.

The original formulation of the doctrine was about necessity, "sequences of events which necessarily follow from a common theme" (*Reyher v. Children's Television Workshop*, 533 F.2d 87, 91 (2d Cir. 1976)). A feature that follows from another shared feature is, on that formulation, no additional similarity at all.

What is known empirically about how lay fact-finders handle these questions is limited. Balganesh, Manta and Wilkinson-Ryan (2014) found that mock jurors largely cannot set aside material they are told is unprotectable. Lee and Moshirnia (2022) found that expert musicologists change mock jurors' verdicts. Mandel, Fast and Olson (2015) found that lay people take intellectual property law to be about preventing plagiarism. None of these studies had a measure of how common the disputed material is, so none could ask whether lay judgments of copying or of stock material track the facts those judgments are about.

Table 1 maps the legal questions onto the studies.

| Legal question | What the fact-finder must judge | Study |
|------------------------------|----------------------------------------------------|------------------|
| Copying in fact (probative similarity) | How strongly a shared feature favors copying over independent creation | 2, 4, 5 |
| Is the feature stock for the genre? | Whether the feature belongs to the genre, under the Restatement's words or in plain causal terms | 2, 5 |
| Does it follow from something else the works share? | Whether a second shared feature adds anything to a first | 3 |
| Selection and arrangement | Whether shared structure counts beyond the features it arranges | 4 |
| Adversarial presentation | Whether the side one is on changes the similarities one finds and the features one filters | 4 |
| Expert evidence of commonness | Whether being shown a count changes the judgment, and which count | 5 |

: Table 1. Legal questions and the studies that address them.

# 4. A causal model of a shared feature

## 4.1 Three causes

Let D be the disputed work, of genre $g$, made after an earlier work W. Let $F$ be a story feature that W has. $F$ can be in D because films of every kind sometimes have it (the background), because being a film of genre $g$ makes it more likely (the genre), or because D's makers took it from W (copying).

Write $b$ for the feature's rate in films outside the genre and $p = P(F \mid g)$ for its prevalence in the genre. If the background and the genre act independently (a noisy-OR), the genre has its own strength $q$, and $p = b + q - bq$. If D's makers copied, they reproduce the feature with some fidelity $\kappa$; otherwise D has it with probability $p$.

## 4.2 Three questions and their answers

*Is the shared feature evidence of copying?* Under independent creation D has the feature with probability $p$. Under copying it has it with probability $\kappa + (1 - \kappa)p$. Sharing the feature therefore multiplies the odds of copying by $[\kappa + (1-\kappa)p]/p$, which is $1/p$ when the copier reproduces the feature for certain. The weight of the evidence is $-\log p$, the surprisal of the feature in the genre. It depends on prevalence and on nothing else. In particular, once it is given that D is a work of the genre, the feature's rate in other genres is irrelevant to whether D copied.

*How much does the genre add?* The absolute amount is the increment $p - b$, which is incremental category validity with films outside the genre as the baseline (with all films as the baseline it is $p - P(F)$, and within a genre the two order features identically). Expressed as a strength it is $q = (p - b)/(1 - b)$, which is Cheng's (1997) generative causal power and has the form of Pearl's (1999) probability of sufficiency.

*Given that the feature is in this work, and was not copied, is it there because of the genre?* Of the genre's films that have the feature, the share that would lack it but for the genre is $(p - b)/p$, which equals $1 - 1/L$, where $L = p/b$ is the feature's lift. It has the form of Pearl's probability of necessity and is the attributable fraction of epidemiology. Lift is cue validity divided by the genre's share of films, so within a genre this quantity orders features as distinctiveness does.

The three answers are built from the one excess $p - b$ that Keith's note identified. They differ in what the excess is divided by: nothing, the room the background leaves ($1 - b$), or the feature's prevalence ($p$). That is why the three measures can disagree about the same feature without any of them being wrong.

| Question | Quantity | Formula | Orders a genre's features like |
|---|---|---|---|
| Is sharing it evidence of copying? | Copying ratio; weight in bits | $1/p$; $-\log_2 p$ | Prevalence, reversed |
| How much does the genre add? | Increment; genre strength | $p - b$; $(p-b)/(1-b)$ | Incremental category validity |
| Given that it is here and not copied, is it here because of the genre? | Share due to the genre | $(p-b)/p$ | Distinctiveness |

: Table 2. Three questions about a shared feature and the quantity that answers each.

Notebook 18 confirms the orderings on the corpus. Across the 17 genres, the share due to the genre correlates .96 with distinctiveness within genre (Spearman; range .89 to .99) and .26 with prevalence, and the genre's strength correlates .96 with incremental category validity. The correlations fall short of 1 for one reason: in 42% of story-feature cells the genre lowers the feature's rate ($p < b$), and for those the share due to the genre is zero and the features tie.

## 4.3 The worked example

Table 3 gives the quantities for nine of the features in the paper's Western example (Part VI). The pattern is easiest to see in four of them. The bounty hunter and the lawyer are equally rare in Westerns, about 2%, so sharing either is equally strong evidence of copying, about 50 to 1. They are opposite in what the genre contributes: of Westerns with a bounty hunter, 94% have one because they are Westerns, while a lawyer is slightly less likely in a Western than elsewhere. The sheriff and the hero's father are equally common in Westerns, 18% and 21%, so sharing either is weak evidence, about 5 to 1. The sheriff is there because of the genre (95%); the father is not.

| Feature | Westerns with it (of 1,362) | All films with it | Prevalence $p$ | Rate outside the genre $b$ | Cue validity | Increment $p - P(F)$ | Share due to the genre | Copying ratio $1/p$ |
|----------------|-----------|----------|-----------|-----------|----------|-----------|----------|-----------|
| outlaw | 195 | 289 | 14.3% | 0.2% | 67.5% | +13.7 | .99 | 7 to 1 |
| saloon | 150 | 226 | 11.0% | 0.2% | 66.4% | +10.5 | .99 | 9 to 1 |
| sheriff | 248 | 697 | 18.2% | 1.0% | 35.6% | +16.7 | .95 | 5 to 1 |
| stagecoach | 96 | 111 | 7.0% | under 0.1% | 86.5% | +6.8 | .99 | 14 to 1 |
| wagon train | 45 | 51 | 3.3% | under 0.1% | 88.2% | +3.2 | 1.00 | 30 to 1 |
| bounty hunter | 26 | 76 | 1.9% | 0.1% | 34.2% | +1.7 | .94 | 52 to 1 |
| father | 288 | 11,207 | 21.1% | 24.5% | 2.6% | −3.2 | 0 | 5 to 1 |
| lawyer | 27 | 1,172 | 2.0% | 2.6% | 2.3% | −0.6 | 0 | 50 to 1 |
| chair | 10 | 656 | 0.7% | 1.4% | 1.5% | −0.7 | 0 | 136 to 1 |

: Table 3. The paper's Western example under the three questions. The increment is in percentage points. Source: Notebook 18, Part A.

## 4.4 What the model leaves out

The copying ratio $1/p$ assumes a copier reproduces the feature for certain; with lower fidelity the ratio shrinks toward 1 but still depends only on $p$. It treats the pair of works as given. A plaintiff who searches thousands of later works for the one most like her own will find more shared features than a random pair shares, and Section 6.2 puts numbers on that. It treats features as independent, which Study 3 relaxes. It takes the feature's level of description as fixed, when the same similarity can be stated broadly ("a lawman") or narrowly ("a newly appointed sheriff"), with different counts. And its counts come from plot summaries of films, so it describes the summaries. None of this affects the studies, which use the model as a benchmark for judgment and do not apply it to a real dispute.

# 5. Three accounts of what people do

The studies are built to separate three accounts of how lay reasoners answer the questions of Table 2.

*The query-sensitive account.* People answer each question with the statistic that answers it. Asked about copying, they consider how likely an independent work of the genre was to have the feature, so judged evidence of copying falls with prevalence and does not depend on distinctiveness. Asked whether a feature is there because of the genre, they use distinctiveness. This is what the causal model prescribes, and there is evidence that people reason well about probabilities when a problem has a causal structure they can use: base-rate neglect shrinks when the statistics map onto a causal model (Krynski and Tenenbaum, 2007), diagnostic judgments from an effect to a cause are sensitive to alternative causes (Fernbach, Darlow and Sloman, 2010), and judgments of coincidence behave like comparisons of a causal against a chance explanation (Griffiths and Tenenbaum, 2007). Keith's framing predicts this account. So does the category-learning literature in a general way: people who learn categories by inferring features attend to what is characteristic, and people who learn by classifying attend to what is diagnostic (Yamauchi and Markman, 1998; Chin-Parker and Ross, 2004), so the question asked can change the statistic used.

*The one-intuition account.* People have a single sense of how typical a feature is of a genre, the sense Study 1 measured, and they use it for every question. A feature that feels typical of Westerns is judged stock, judged to be there because of the genre, and discounted as evidence of copying. Since that sense follows distinctiveness about four times as strongly as prevalence, judged evidence of copying would fall with distinctiveness, which the model says is irrelevant, and would barely respond to prevalence, which the model says is the only thing that matters. This is the representativeness account of probability judgment (Kahneman and Tversky, 1972), in the form given it by Bordalo, Coffman, Gennaioli and Shleifer (2016), for whom a trait is representative of a group when it is more frequent there than in a comparison group. It also fits the inverse fallacy, the substitution of $P(C \mid F)$ for $P(F \mid C)$ (Villejoubert and Mandel, 2002). Its legal consequence would be serious: rare but characteristic features such as the bounty hunter are the strongest evidence of copying the model recognizes, and this account says they are exactly what an intuitive fact-finder discounts.

*The overall-frequency account.* People judge copying by how common the feature is in stories generally, without conditioning on the genre. Ordinary things are coincidences and unusual things are evidence. Within a level of prevalence, a more distinctive feature is rarer in film at large, so on this account judged evidence of copying rises with distinctiveness.

The three accounts predict three different signs for the effect of distinctiveness on judged evidence of copying, with prevalence held fixed: zero, negative and positive. That one coefficient is the most diagnostic quantity in the design, and Study 2 is built around it.

| | Query-sensitive | One intuition | Overall frequency |
|---|---|---|---|
| Copying: effect of prevalence | Negative | Weakly negative | Negative |
| Copying: effect of distinctiveness | Zero | Negative | Positive |
| Copying: rare-but-characteristic against common-but-uncharacteristic (LH minus HL) | Positive | Negative | Positive |
| "Because of the genre" and "stock": effect of distinctiveness | Positive, larger than prevalence | Positive, larger than prevalence | Not specified |
| Does the question change the weights? | Yes | No: one profile, reversed for copying | Partly |

: Table 4. Predictions of the three accounts for Study 2.

The three accounts are about the answer a person gives. A fourth possibility is about how the answer forms. The sense of what is typical of a genre may come to mind first whatever the question, and be set aside when the question calls for something else. Kahneman and Frederick (2002) describe intuitive judgment in this way, as the substitution of an easily assessed attribute for the one asked about, which slower reasoning sometimes corrects. On this reading, which this memo calls corrected intuition, ratings of copying could follow prevalence, as the query-sensitive account says, and the feature's typicality would still pull at the response while it was being made. Ratings cannot show such a pull. The mouse-tracked condition of Study 2 is there to look for it.

# 6. What the corpus already says

## 6.1 The Study 1 items are matched for this test

Table 5 gives the Study 1 rated items by cell. Within each level of prevalence the high- and low-distinctiveness cells have almost the same prevalence (3.2% and 3.3% in the high cells; 0.75% and 0.77% in the low cells), so the model's copying ratio is the same across distinctiveness, about 31 to 1 in the high-prevalence cells and about 130 to 1 in the low ones. The prevalence manipulation is worth two bits, a factor of four in the odds. The distinctiveness manipulation moves cue validity from about 6% to about 33% and moves the share due to the genre from zero to about three quarters.

| Cell (prevalence, distinctiveness) | Items | Median prevalence | Median copying ratio | Median weight (bits) | Median cue validity | Median share due to the genre | Study 1 mean rating |
|----------------------|-------|-----------|-----------|---------|----------|------------|----------|
| High, high | 72 | 3.2% | 31 to 1 | 5.0 | 31.7% | .77 | 5.65 |
| High, low | 72 | 3.3% | 31 to 1 | 4.9 | 6.2% | 0 | 4.38 |
| Low, high | 72 | 0.75% | 130 to 1 | 7.0 | 35.3% | .78 | 5.17 |
| Low, low | 72 | 0.77% | 129 to 1 | 7.0 | 5.9% | 0 | 3.95 |
| Foils (from other genres) | 48 | 0.10% | 824 to 1 | 9.7 | 1.5% | 0 | 2.79 |

: Table 5. The Study 1 rated items under the model. Ratings are means of item means. Source: Notebook 18, Part B, and `design_inputs_from_study1.Rmd`.

Across the 288 stratified items, with each variable centered within genre, the model's copying weight correlates −.03 with distinctiveness and −.23 with the Study 1 rating, while the Study 1 rating correlates .60 with distinctiveness (Spearman). The two main accounts therefore make nearly uncorrelated predictions item by item, which is the condition under which a single study can tell them apart. Figure 1 shows every item.

![Figure 1. Study 1 mean expectedness of each rated item against its prevalence in the genre, by distinctiveness. The model's evidence of copying depends only on horizontal position; the Study 1 ratings depend mostly on color. Bars are 95% intervals. Source: Notebook 18.](figures/study1_items_expected_by_prevalence.png)

The cells differ in absolute prevalence across genres, because the genres differ in size and the cells are thirds within genre. The median high-prevalence item is in 5% to 11% of Westerns and about 1% of comedies. The analysis uses within-genre predictors, as Study 1 did, and adds the copying weight in bits as a continuous predictor so that the absolute differences are used and not hidden.

## 6.2 What two unrelated films share

A list of similarities means something only against what two unrelated films of the genre share. For each of the six Study 1 genres, Notebook 18 drew 20,000 random pairs of films and counted the story features both summaries contain. Table 6 gives the result. Two random Westerns share a median of 2 story features and 11 at the 95th percentile. The closest other Western to a given Western, found by searching all 1,362, shares a median of 14.5. A plaintiff who looks across a genre for the work most like hers can therefore expect about as many shared features by chance as the 95th to 99th percentile of random pairs, with summed model weights of about 50 to 80 bits depending on the genre.

| | Western | Horror | Science fiction | Crime | Fantasy | Comedy |
|---|---|---|---|---|---|---|
| Films of the genre | 1,362 | 4,363 | 2,590 | 5,564 | 2,429 | 14,724 |
| Story features per summary (median) | 39 | 58 | 69 | 44 | 70 | 37 |
| Shared by a random pair: median | 2 | 3 | 3 | 2 | 3 | 1 |
| Shared by a random pair: 95th percentile | 11 | 16 | 16 | 13 | 16 | 8 |
| Shared by a random pair: 99th percentile | 19 | 24 | 23 | 20 | 23 | 14 |
| Shared with the closest other film (median) | 14.5 | 16 | 23 | 17 | 23 | 13 |
| Weight of a random pair's shared features, bits (median) | 5.9 | 6.8 | 8.6 | 5.8 | 8.6 | 4.2 |
| Weight shared with the closest other film, bits (median) | 50 | 57 | 80 | 63 | 78 | 59 |

: Table 6. Shared story features between unrelated films of a genre. Counts depend on the length of the summaries. Source: Notebook 18, Part C.

These numbers size the materials: a pair of synopses that shares four listed features is within the range of chance for the genre, which is where a judgment task should sit. They are also a result the next paper could report in its own right, since they are the baseline that *Ty* asks for and that no court has had.

## 6.3 A first check of the copying weight on real films

The corpus has no record of which films derive from which. As a rough stand-in, Notebook 18 took the 3,204 pairs of films that share a title and were released at least three years apart, many of them remakes or adaptations of one source, and asked how well three scoring rules tell them from random pairs of the same genre. After adjusting for summary length, the mean AUC across 17 genres was .79 for the plain number of shared features, .80 for shared features weighted by the model's copying weight, and .79 for shared features weighted by distinctiveness. The copying weight was ahead of the plain count in 15 genres and ahead of distinctiveness weighting in 13, but the differences are a point or two and this check is too coarse to separate the rules. Shared titles include unrelated films, and remakes share a source more than they share incidental features. A cleaner test needs a curated list of remakes and adaptations, which is proposed in Section 15 as corpus work alongside the studies.

## 6.4 Material for packages and for synopses

Notebook 18 also confirms that the materials for Studies 3 and 4 exist. Among concrete story features in at least 20 of a genre's films, each genre has between 220 (Western) and 1,476 (comedy) ordered pairs in which the second feature is at least three times as likely given the first as in the genre at large and present in at least 30% of the films with the first. In Westerns, 77% of films with a Confederate have a war, against 14% of Westerns overall; 66% of films with a foreman have a ranch, against 18%. In horror, 82% of films with a transfusion have blood, against 16%. Each genre also has thousands of pairs whose members are statistically unrelated. And every genre has enough concrete characters, settings, objects and events in each of the four cells to fill two story shells: the smallest supply is the Western's common-but-uncharacteristic cell, with 11 kinds of character, 8 settings, 2 objects and 3 events.

# 7. The four studies at a glance

| | Study 2. One shared feature: three questions and a tracked choice | Study 3. Packages | Study 4. Two works | Study 5. Showing the counts |
|----------------|---------------------|---------------------|---------------------|---------------------|
| Question | Which statistic answers which question, and does typicality pull at the copying judgment as it forms? | Do people see that one shared feature can imply another? | Do arrangement and one's side change the judgment? | Does a count change the judgment, and which count? |
| Unit judged | One feature shared by two unseen works | A pair of shared features | Two synopses | Features in a dispute, with expert counts |
| Varied between participants | The question and how it is answered (copying, rated; because of the genre; stock; copying, chosen with the mouse) | The question (copying; necessity) | Role (plaintiff's side; defendant's side; neutral) | Count format (none; prevalence; distinctiveness; both; increment) |
| Varied within participants | Prevalence × distinctiveness of the feature | Implied or unrelated pair | Kind of shared features (2 × 2) × arrangement (aligned, scattered) | Prevalence × distinctiveness of the feature |
| Materials | The 336 Study 1 items; 480 with the recommended extension | 144 pairs in 72 matched sets, drawn from Notebook 03c counts | 12 story shells, 96 synopsis pairs | 48 Study 1 items with their corpus counts |
| Main measures | Rating, 1 to 7; choice and mouse path; frequency estimates | Rating, 1 to 7; conditional frequency estimates | Probability of copying; similarity; character mapping; feature checklist | Stock rating; copying weight |
| Usable participants proposed | 280 (70 per condition) | 120 (60 per question) | 210 (70 per role) | 300 (60 per format) |
| Session | 25 to 30 minutes | About 25 minutes | About 45 minutes | About 20 minutes |
| New materials work | None with the Study 1 items; the experiment is built | Moderate | Large | Small |

: Table 7. Overview of the studies.

# 8. Study 2: one shared feature, three questions and a tracked choice

## 8.1 Purpose

Study 2 tests whether the statistic people use depends on the question they are asked. It holds the materials constant, the Study 1 items, and changes only the question. One further condition changes how the copying question is answered, from a rating to a choice made with the mouse, to see how that judgment forms.

## 8.2 Design

Four conditions vary between participants. In three of them participants give ratings. In the COPY condition they judge how strongly a feature shared by an earlier screenplay and a later film suggests that the film was copied. In the GENRE condition they judge how much a feature is in a film because of the film's genre. In the STOCK condition they are given the Restatement's five adjectives and judge whether the feature is a stock feature of the genre. COPY corresponds to the first question of Table 2 and GENRE to the third. STOCK is the legal classification in the law's own words, included because the paper's argument is that those words do not settle which property is meant. In the fourth condition, TRACK, participants answer the COPY question as a choice between two boxes, "Copied" and "Coincidence," and the path of the mouse is recorded (Section 8.9).

Within participants the design is Study 1's in every condition: two genres per participant, assigned by the twelve-cell schedule of Study 1 (six genre pairs in two orders), and for each genre the 48 stratified items (12 in each cell of high or low prevalence crossed with high or low distinctiveness) and the 8 foils, in random order with two instructed-response attention checks. With the extended item set recommended in Section 8.8 there are 72 stratified items per genre.

A fifth condition is possible and is left as a decision (Section 16). In a PROTECT condition participants would judge whether the screenwriter should be able to stop the film's makers from using the feature. It measures the normative intuition directly and would connect to Mandel, Fast and Olson's finding that lay people read intellectual property law as a rule against plagiarism. It adds a quarter to the sample and is not needed for the test of the three accounts. The experiment as built contains its wording, switched off.

## 8.3 Materials

The items are the 336 rated items of Study 1 with their display text unchanged. Using them has advantages. Every item has a Study 1 expectedness rating from 36 to 49 other participants, so the one-intuition account can be tested with a predictor measured on different people. The cells are matched on prevalence across distinctiveness (Table 5). The Study 1 experiment code already presents them.

Study 1's variance components show that the item set, not the sample, limits precision. The item standard deviation was 0.99 rating points, against 0.61 for participants and 1.30 for the residual, so the standard error of a cell contrast across 288 items has a floor of about 0.12 to 0.14 however many participants are run. An extended set of 432 items (18 per cell per genre) would lower that floor by about a fifth. The extra items would come from the same seeded queues that Notebook 10 used, so the draw stays reproducible, but they would have no Study 1 norms. Section 8.8 gives the power for both sets.

## 8.4 Procedure

The session follows Study 1's structure with the listing task removed. After consent and the two-sentence reading task, participants read the instructions for their condition and answer the task check ("What is your task in this study?"), with one retry after re-reading. Participants in the TRACK condition then learn the mouse procedure (Section 8.9). For each of their two genres participants rate their familiarity with the genre and then make the judgments for that genre, 56 with the Study 1 items and 80 with the extended set. In the rating conditions the items appear eight to a page, as in Study 1. In the TRACK condition they appear one at a time. A final block, the same in every condition, collects frequency estimates. The session ends with demographics, a question on legal training, the Study 1 closing questions (seriousness, distraction, use of AI tools) and the debriefing. The expected length with the Study 1 items is 25 to 30 minutes in every condition.

In the frequency block each participant gives three estimates for 16 of the Study 1 items from each of their two genres (4 per cell; the 12 Study 1 items of each cell are divided into three fixed sets and each participant is given one set at random, so every item is estimated by about a third of the participants who saw its genre). The three estimates are the number, out of 100 films of the genre, that include the feature; the number, out of 100 films of all kinds, that include it; and the number, out of 100 films that include it, that are films of the genre. They are collected in three short blocks whose order is drawn at random for each participant, on sliders from 0 to 100 that show no handle until they are clicked. They give each item a subjective prevalence, a subjective base rate and a subjective cue validity, from which a subjective copying ratio and a subjective share due to the genre follow. The block comes last so that it cannot affect the main judgments; whether the preceding condition affects the estimates is checked.

The exact wording of every instruction and question is in Appendix A. It is the wording of the experiment as built (`Experiment/Study 2/`).

## 8.5 Hypotheses and registered tests for the ratings

These tests concern the three rating conditions; the tests of the TRACK condition are in Section 8.9. All tests use the 48 stratified items. Prevalence (P) and distinctiveness (D) are coded +0.5 for the top third and −0.5 for the bottom third of the genre, as in Study 1.

S2-H1. *Prevalence lowers judged evidence of copying.* In the COPY condition the coefficient of P is below zero. All three accounts predict the sign; the query-sensitive account predicts the largest effect.

S2-H2. *The diagnostic contrast.* In the COPY condition, the contrast P minus D, which equals the common-but-uncharacteristic cell minus the rare-but-characteristic cell (HL minus LH), separates the accounts. Below zero favors the query-sensitive and overall-frequency accounts: the rarer feature is the stronger evidence. Above zero favors the one-intuition account: the more characteristic feature is discounted. This is Study 1's H2c with the question changed.

S2-H3. *Distinctiveness and copying.* In the COPY condition the coefficient of D is negative under the one-intuition account, positive under the overall-frequency account, and zero under the query-sensitive account. A zero cannot be shown by a non-significant test, so the query-sensitive prediction is tested as an equivalence: the 90% interval for the coefficient lies within ±0.40 rating points. That bound is about a quarter of distinctiveness's effect on expectedness in Study 1 and slightly more than prevalence's effect there (0.36).

S2-H4. *The question changes the weights.* The effect of D differs between the COPY condition and the GENRE and STOCK conditions, and so does the effect of P (question-by-predictor interactions in a model of all three conditions). Under the one-intuition account the COPY profile is the GENRE profile reversed, so the sum of the two D coefficients is near zero; under the query-sensitive account the COPY condition has no D effect at all.

S2-H5. *GENRE and STOCK replicate Study 1.* In both conditions D has a larger effect than P.

S2-H6. *The Restatement's words.* The effect of P is larger in the STOCK condition than in the GENRE condition. The Restatement's list includes "common" and "customary," which name prevalence. If the words matter, they should pull the classification toward prevalence. This test is two-sided.

S2-H7. *Beliefs about frequency.* Estimates of how many films of the genre include a feature rise with corpus prevalence, and also rise with corpus distinctiveness at a given prevalence. The second effect is the inverse fallacy in this domain and would mean that part of any distinctiveness effect on judged copying comes from mistaken beliefs about prevalence.

S2-H8. *Belief or inference.* In the COPY condition, when the subjective copying weight ($-\log_2$ of the item's mean estimated prevalence) is entered, does corpus distinctiveness still predict the rating? If not, people reason as the model does from wrong beliefs. If so, they reason differently.

S2-H9. *One score or several.* For each condition, models that know a single item-level predictor (the Study 1 expectedness rating; the copying weight; the increment) are compared with each other and with the two-predictor model by AIC and by held-out log-likelihood in ten folds by participant, as in Study 1's H3.

## 8.6 Decision rule

The three accounts are distinguished by S2-H2 and S2-H3 together, read as in Table 8.

| P minus D (S2-H2) | D (S2-H3) | Reading |
|---|---|---|
| Below zero | Equivalent to zero | Query-sensitive: copying judged by prevalence alone |
| Below zero | Above zero | Overall frequency: copying judged by rarity in film generally |
| Above zero | Below zero | One intuition: characteristic features discounted |
| Below zero or not different from zero | Below zero | Mixed: prevalence is used and characteristic features are also discounted |
| Any other pattern | | No account supported as stated |

: Table 8. Reading the two tests of the COPY condition.

## 8.7 Analysis

The registered model in each condition is Study 1's ratings model: the rating regressed on P, D, their interaction, everyday word frequency (SUBTLEX-US log contextual diversity, centered) and genre (sum-to-zero contrasts), with random intercepts for participants and items and random slopes for P and D by participant, fit by restricted maximum likelihood with `lmer`. A model that fails Study 1's convergence check is reduced by Study 1's rule: the correlations among the participant effects are removed, then the slope with the smaller variance. Intervals and p-values use Satterthwaite degrees of freedom.

The combined model for S2-H4 to S2-H6 adds question and its interactions with P and D, and gives items a random slope for question, since the same items appear in every condition. The continuous form of each model replaces P and D by centered within-genre percentiles and, separately, by the copying weight in bits and the share due to the genre, to use the absolute differences among genres that the coding by thirds removes.

Robustness checks follow Study 1: the model without word frequency; a cumulative-link mixed model; each genre left out in turn; the first genre block only, which is free of any carry-over between genres; and familiarity with the genre as a moderator. The foils are analyzed separately, as in Study 1; in the COPY condition they should be the strongest evidence of all on both the query-sensitive and overall-frequency accounts, since a feature from another genre is rare in this one.

An item-level analysis uses the Study 1 norms directly. The mean COPY rating of each item is regressed on its copying weight and its Study 1 expectedness rating, with genre. Because the two predictors correlate only −.23, their coefficients are well separated.

## 8.8 Sample size for the ratings

The simulations (Appendix C) varied the number of participants per condition (50, 70 or 90) and the item set (288 or 432 stratified items) under each account. The number of participants hardly matters, because every item is rated by a third of them and the differences among items dominate. The item set matters. If copying judgments follow prevalence alone, with an effect of 0.60 points, the contrast of S2-H2 is significantly below zero in 91% of simulations with 288 items and 70 participants, and in 98% with 432 items. The equivalence test of S2-H3 at ±0.40 succeeds in 71% of simulations with 288 items and in 90% with 432. At ±0.30 it succeeds in 32% and 58%, so neither set can establish a zero that tightly. If the one-intuition account holds at seven tenths of the size of Study 1's effects, or the overall-frequency account at the size assumed, the contrast and the distinctiveness effect are detected in 98% to 100% of simulations with either set. A prevalence effect as small as 0.25 points, which the one-intuition account implies, is detected in 60% of simulations with 288 items and 71% with 432.

The proposal is 70 usable participants per condition and the extended set of 432 items. With the TRACK condition, whose own power is in Section 8.9, that is 280 usable participants. Study 1 lost 6 of 137 sessions to its exclusion rules, so about 295 would be recruited, and somewhat more if the tracked condition loses more sessions to its own rules. Figure 2 shows the two tests on which the choice of item set turns.

![Figure 2. Study 2, rating conditions: share of simulations in which each test succeeds if copying judgments follow prevalence alone, by number of participants and item set. The dashed line is 80%. Source: `studies2to5_power.Rmd`.](figures/power_study2_ratings.png)

## 8.9 The mouse-tracked condition

*Why it is there.* The ratings say which statistic the answer follows. They cannot say whether the other statistic was in play. Under the query-sensitive account a person asked about copying consults how common the feature is in the genre, and nothing else comes into it. Under the corrected-intuition reading of Section 5 the feature's typicality comes to mind first and is overruled. Both predict the same ratings. They predict different paths. If typicality is overruled, then on the way to "Copied" for a rare but characteristic feature the hand should lean toward "Coincidence," and it should lean less for a rare feature that is not characteristic. If the one-intuition account holds and typicality decides the choice, the same measure shows which of the two statistics the response was working against.

*The task.* The task is the COPY question with two answers. The instructions give the same dispute (a screenplay, a later film by different people, a claim of copying and a denial) and ask, for each thing the two works share, which is more likely: that the film's makers copied it, or that it is a coincidence, meaning that they came up with it on their own. The two boxes sit in the top corners of the screen and a Start button at the bottom center. A line above the center states the frame for the block ("Two Westerns both include:"). The participant clicks Start and begins to move upward, and the item appears once the cursor has risen 40 pixels, so that the decision is made while the hand is moving (the dynamic start of Scherbaum and Kieslich, 2018). The trial ends with a click on a box. The cursor's position is recorded throughout, at up to 125 samples a second. The box for "Copied" stays on one side for the whole session, left or right by a random draw for each participant.

The choice asks which explanation is more likely, where the rating asks how strongly the feature suggests copying. Under the model the two differ by the participant's prior belief that a film in such a dispute was copied, which moves every item alike. The order of the items by prevalence is the same for both, and a participant's own threshold absorbs the rest.

*Practice and control.* Before the genres, participants complete a mouse-tracked color-word Stroop task: 8 practice trials with feedback and 32 scored trials, half of them incongruent. It teaches the procedure, and it is a positive control. Mouse-tracked Stroop tasks show a reliable effect of congruency on the movement toward the response (Bundt, Ruitenberg, Abrahamse and Notebaert, 2018; Yamamoto, Incera and McLennan, 2016), so a session's own Stroop trials show whether its paths register a conflict whose existence is not in doubt, and how large such a conflict is on the measure used here. Four practice choices about two Romance films follow.

*Trials.* Each genre block has the same 56 items as the rating conditions, in random order, and two instructed-response trials ("Attention check: choose Copied" and "Attention check: choose Coincidence"), which take the place of the two attention checks. A response slower than four seconds from the item's onset brings a short reminder to answer a little faster. That limit is a first setting, to be fixed after the investigators' own piloting.

*Measures.* The choice is one measure. From each path the analysis takes its curvature. The paths are mirrored so that the chosen box is always on the same side, aligned to a common start, and resampled to 101 steps of equal time; the curvature is the area between the path and the straight line from start to response, positive when the path bends toward the box that was not chosen. The maximum deviation from the straight line is the robustness measure. Both are computed with the mousetrap package (Kieslich and Henninger, 2017; Kieslich, Henninger, Wulff, Haslbeck and Schulte-Mecklenbeck, 2019). The third measure is the direction of movement at each step, from which the time at which a predictor begins to steer the path can be estimated.

S2-H10. *The choice repeats the rating tests.* In a logistic mixed model of choosing "Copied," the tests of S2-H1 to S2-H3 are repeated: prevalence lowers the rate of "Copied"; the sign of P minus D separates the accounts; and the effect of D is negative, positive or equivalent to zero. Across items, the share choosing "Copied" rises with the mean rating of the COPY condition.

S2-H11. *The pull of typicality.* Curvature is greater when the response goes against the feature's distinctiveness, that is, when "Copied" is chosen for a characteristic feature or "Coincidence" for an uncharacteristic one, than when it goes with it. This is the interaction of the response with D in a model of curvature. Under the query-sensitive account it is zero. Under corrected intuition it is positive although D does not affect the choice. Under the one-intuition account it is positive and D decides the choice as well.

S2-H12. *The pull of prevalence.* The same for prevalence: curvature is greater when "Copied" is chosen for a common feature or "Coincidence" for a rare one. Every account on which prevalence affects the choice predicts this, and the comparison of the two pulls says which statistic the hand resists more.

S2-H13. *Which comes first.* In a regression of the direction of movement on P and D at each time step, the effect of D begins earlier than the effect of P. This is corrected intuition in its sharpest form. The method is that of Scherbaum, Dshemuchadse, Fischer and Goschke (2010) and of Sullivan, Hutcherson, Harris and Rangel (2015), who found with it that the tastiness of a food begins to steer a choice about 195 ms before its healthfulness does. The onset of each effect is estimated from the pooled paths, and the difference between the two onsets is tested by jackknifing over participants (Miller, Patterson and Ulrich, 1998).

*Analysis.* The choice model is the rating model of Section 8.7 with a logit link. The curvature model is linear, with the response, P, D, the interactions of the response with P and with D, word frequency and genre as fixed effects, random intercepts for participants and items, and participant slopes for the two interactions, reduced by Study 1's rule if it fails the convergence check. The Stroop effect on curvature is reported first, from a model of the same form. A mean curvature can come from a mixture of straight paths and paths that change direction (Kieslich et al., 2019), so the distribution of curvature is reported for each cell and the tests are repeated on the share of paths that cross toward the box not chosen. The kind of pointing device, as reported by the participant and as recorded by the browser, enters as a covariate in a robustness check.

*Trials and sessions left out.* The proposal, to be settled before preregistration, is to drop trials on which the item appeared only after the two-second limit for starting to move, trials during which the window was resized, and trials slower than six seconds; and, beyond the common rules of Section 12, to exclude sessions answered with a touch screen and sessions with fewer than three quarters of the scored Stroop trials correct.

*Power.* Appendix C has the simulations. The choice loses little against the rating, because the differences among items, and not the noise in a single response, limit precision. If choices follow prevalence alone, the contrast P minus D is below zero in 83% of simulations with 288 items and 70 participants and in 98% with 432 items (the ratings: 91% and 98%), and the effect of D is shown to be equivalent to zero, within the logit equivalent of ±0.40 rating points, in 74% and 94% (the ratings: 71% and 90%). If the one-intuition or the overall-frequency account holds, the contrast and the effect of D are detected in 96% of simulations or more. These figures assume that a choice is the rating cut at a threshold, with the same noise. A noisier choice would lower them.

For the path no quantity has an earlier estimate, so the simulation states its assumptions (Appendix C) and asks how small a pull could be found. With choices following prevalence alone, 70 participants and two genres each, a pull of typicality of 0.10 trial standard deviations is detected in 89% of simulations with 288 items and in 96% with 432, and a pull of 0.15 or 0.20 in every simulation. With 50 participants the first two figures are 79% and 92%. Telling the two pulls apart is harder. A pull of typicality twice the size of the pull of prevalence (0.20 against 0.10) is distinguished from it in 63% of simulations with 288 items and in 79% with 432; a pull half again as large (0.15 against 0.10) in 23% and 40%. Giving each tracked participant all six genres, 288 item trials in place of 96, raises the 63% to 93%.

The proposal is 70 usable participants and two genres each, which under these assumptions is enough for S2-H11 and S2-H12. The number of genres is left open (Section 16), because the comparison of the two pulls and the test of S2-H13 would gain from more trials. S2-H13 was not simulated: its power depends on how far apart in time the two effects begin and on the shape of the noise in the paths, and nothing yet gives either. The investigators' own sessions and the Stroop trials will give the first real numbers. Figure 3 shows the test of S2-H11.

![Figure 3. Study 2, tracked condition: share of simulations in which a pull toward the typical answer is detected in the curvature of the paths when choices follow prevalence alone, by its assumed size, the number of participants and the item set. The dashed line is 80%. Source: `studies2to5_power.Rmd`.](figures/power_study2_tracking.png)

*What it costs.* A choice carries less information than a rating, which is why the tracked condition stands beside the COPY ratings and does not replace them. It needs a mouse or trackpad and a window of at least 800 by 550 pixels, which the page checks. Its sessions are the same length as the others, so one listing and one credit value serve all four conditions.

## 8.10 What Study 2 cannot show

Each trial gives one shared feature and no works. The judgment is stripped of everything a real comparison involves, which is the point of the design and also its limit. A participant may reasonably think one shared feature proves nothing and use only the bottom of the scale; the instructions ask for relative judgments and the foils and rare items give the scale a top. If ratings in the COPY condition sit at the floor in piloting by the investigators, the question would be changed to a comparative one before preregistration. The undergraduates of the subject pool are not jurors, and Study 5 is the place for a broader sample.

The tracked condition adds a view of the judgment forming. It does not say what the pull, if there is one, would do to a decision made under load or in a hurry, which is where an overruled intuition would matter in practice. That is a question for a later study.

# 9. Study 3: packages of shared features

## 9.1 Purpose

Two shared features are not always two pieces of evidence. If nearly every Western with a foreman has a ranch, a second work that has both tells little more than one that has a foreman. In the model the weight of a pair is the surprisal of the pair,

$$-\log P(F_1, F_2 \mid g) = -\log P(F_1 \mid g) - \log P(F_2 \mid F_1, g),$$

and the second term is small when the first feature implies the second. That conditional probability is what the corpus can say about necessity, and discounting features that follow from other shared features is what the *Reyher* formulation asks a court to do. Study 3 tests whether people's necessity judgments follow the conditional counts and whether their judgments of copying discount implied features.

People often fail to discount correlated evidence (Enke and Zimmermann, 2019). There is also a reason to expect the opposite of discounting: a pair that hangs together may feel like more of a shared story than two unrelated features, as coherent conjunctions feel more probable than their parts (Tversky and Kahneman, 1983).

## 9.2 Design

The question varies between participants: COPY (how strongly do these two shared features together suggest copying?) or NECESSITY (given that a film of the genre has the first feature, how necessary is the second?). Pair type varies within participants: in implied pairs the second feature is much more likely given the first than in the genre at large; in unrelated pairs the conditional and the plain rate are about equal. Each participant sees the pairs of two genres, assigned as in Study 1. Pairs come in matched sets, an implied pair and an unrelated pair that share their second feature, so that the two types are compared on the same feature.

## 9.3 Materials

A new notebook draws 12 matched sets per genre, 24 pairs, from the counts of Notebook 03c, by a seeded rule with a reviewed exclusion list, as Notebook 10 did. Both members of a pair are concrete nouns or noun phrases (kinds of character, settings, objects, events) found in at least 20 of the genre's films. An implied pair requires $P(F_2 \mid F_1, g) \ge .30$, at least three times $P(F_2 \mid g)$, and at least 10 films with both. An unrelated pair requires the two rates to differ by less than a quarter. A matched set is an implied pair and an unrelated pair with the same second feature, whose first features are about equally common in the genre (within a factor of 1.5). The two pairs then have nearly the same single-feature weights and differ in dependence. Every genre has enough of them: between 165 (Western) and 866 (comedy) implied pairs have such a partner, covering 41 to 73 different second features. Pairs whose members share a word or a stem, or stand as part to whole (sheriff and new sheriff; starship and ship; townspeople and town), are excluded by rule and by review.

For the pair of a foreman and a ranch in Westerns, 41 Westerns have a foreman, 241 have a ranch and 27 have both. The pair's weight is $-\log_2(27/1362) = 5.7$ bits. If the two were independent it would be 7.6 bits. The dependence removes about two bits, a factor of nearly four in the odds. Its matched partner is a lady and a ranch: 18% of Westerns with a lady have a ranch, the same as Westerns overall.

## 9.4 Procedure and measures

In the COPY condition, participants use the dispute frame of Study 2 and rate each pair ("Both the screenplay and the film include: a foreman; a ranch") on the same seven-point scale. After the pairs of both genres, a second block presents the members of the pairs one at a time for the same rating, so that each pair's rating can be compared with its members'. The pairs come first so that the single ratings cannot affect them.

In the NECESSITY condition, participants rate for each pair how necessary the second feature is in a film of the genre that has the first (1, it could easily be left out, to 7, the story could not do without it), and then estimate, for each pair, how many of 100 films of the genre with the first feature also have the second, and how many of 100 films of the genre have the second.

## 9.5 Hypotheses

S3-H1. *Necessity follows conditional prevalence.* Necessity ratings are higher for implied than for unrelated pairs, and across pairs they rise with $P(F_2 \mid F_1, g)$ with $P(F_2 \mid g)$ held fixed.

S3-H2. *Packages as evidence.* In the COPY condition the model predicts lower ratings for implied than for unrelated pairs. Neglect of the dependence predicts no difference. Coherence predicts higher ratings for implied pairs. The test is two-sided and the direction is the finding.

S3-H3. *Adding up.* The difference between a pair's rating and the mean of its members' ratings is smaller for implied than for unrelated pairs (model), equal (neglect) or larger (coherence).

S3-H4. *Beliefs.* Estimated conditional frequencies track the corpus values, and the COPY ratings of pairs are better predicted by the pair's weight computed from estimated frequencies than from corpus frequencies.

## 9.6 Analysis and sample size

The models have the form of Study 2's, with pair type in place of P and D, pairs and matched sets as random factors, and the continuous predictors (the members' single weights and the log of the dependence ratio) in the continuous form.

A first simulation used unmatched pairs and showed the limit met in Study 2 more sharply. With 96 pairs, a difference of 0.5 points between the pair types was detected in 60% to 69% of simulations; with 144 pairs, in 74% to 82%. That is why the design uses matched sets. How much of the variation among pairs the two members of a set share is not known. If half is shared, 144 pairs in 72 sets and 60 participants per question detect a difference of 0.5 points in 94% of simulations and a difference of 0.4 in 76%. If a quarter is shared the figures are 86% and 70%. For scale, the dependence in an implied pair is worth about two bits, the size of the prevalence manipulation in Study 2, for which the Study 2 simulations assumed 0.6 points; a difference of 0.6 is detected in 93% to 98%. The proposal is 12 matched sets per genre and 60 usable participants per question, 120 in all. An effect smaller than about 0.4 points would need more sets, which the corpus can supply.

# 10. Study 4: two works, their arrangement, and the side one is on

## 10.1 Purpose

Study 4 returns to the Spellman and Holyoak paradigm: participants compare two narrative works in a copying dispute. It asks what single features cannot. Do the effects of Study 2 hold when the shared features sit inside stories? Does shared arrangement count beyond the shared features, as *Metcalf* holds, and does that depend on whether the features are stock? Does the side a person is on change the judgment, the correspondences found, and the features filtered out, as their pragmatic account of mapping predicts and as *Litchfield* suspects?

## 10.2 Design

Role varies between participants: working with the plaintiff's lawyers, working with the defendant's lawyers, or serving as a juror. Two factors vary within participants across eight cases. The kind of shared features has the four cells of Study 1: the four features the works share are all from one cell of the genre. Arrangement has two levels. In aligned cases the shared features play the same parts in both stories and the events run in the same order. In scattered cases the same four features appear in both works but in different parts of unrelated plots.

## 10.3 Materials

Each case is built on a story shell. A shell is a plot skeleton for one genre with four slots, two kinds of character, a setting or object, and an event, together with fixed material that the two works do not share. Filling the slots from one cell of the genre gives the screenplay's synopsis and the aligned film's synopsis, which tell the same sequence in different words and with different unshared detail. The scattered film's synopsis uses the same four features in a plot with a different skeleton. Each synopsis is five or six sentences, about 110 to 130 words. Unshared detail comes from the middle third of the genre on both measures, so that it is neutral.

There are 12 shells, two per genre, and each can be filled from any of the four cells and paired with either arrangement, which gives 96 versions. Each participant sees 8 different shells, one in each combination of cell and arrangement, by a Latin square, so that across participants every shell appears in every combination. Shells are the random item factor.

The slot fillers are drawn by a seeded rule from the Study 1 pool (story features in at least 20 of the genre's films) and reviewed, and the shells are written by hand and reviewed for whether each filled version reads as a plausible story. Appendix B gives a complete example. A pair that shares four listed features is inside the range of chance for every genre (Table 6), so no case is decided by the count of similarities alone.

The model's benchmark for each version is the sum of its four features' weights. It is the same for both arrangements and differs by about eight bits between cells of high and low prevalence. The model as specified has no term for arrangement. It says only that shared structure is further evidence, by an amount the corpus cannot yet supply.

## 10.4 Procedure

After consent, the reading task and general instructions, participants read their role. As in Spellman and Holyoak, the role is given a purpose: participants on a side are asked to write, before the cases, two or three sentences on what they will look for on behalf of their side, and jurors on what they will want to know. Every participant is then told that for each case they should give their honest judgment, whatever their side.

For each case the two synopses appear side by side, the screenplay labeled as written first. The participant then gives, in order: the probability that the film's makers copied from the screenplay (0 to 100); the similarity of the two works (1 to 7); for each of the screenplay's two main characters, which character in the film corresponds to it, with "no one" as an option; a checklist of six features, the four shared ones and two that only one work has, each to be marked as in both works and counting toward copying, in both works but standard for the genre and so not counting, or not in both works; and which side should win, with confidence. Participants on a side also predict what a jury would decide. The session is planned for 45 minutes.

## 10.5 Hypotheses

S4-H1. *Arrangement.* Aligned cases receive higher probabilities of copying and higher similarity than scattered cases. Structure-mapping accounts of similarity predict a large effect (Gentner, 1983; Markman and Gentner, 1993), and *Metcalf* requires one.

S4-H2. *The kind of shared features.* The accounts make the predictions of Table 4 at the level of works: the probability of copying is higher when the shared features are rare in the genre (query-sensitive), lower when they are characteristic of it (one intuition), or higher when they are characteristic (overall frequency).

S4-H3. *Do stock parts spoil the arrangement?* In the model, shared features and shared arrangement are separate evidence and add on the log-odds scale. The alternative of legal interest is an interaction: arrangement counts for less when the arranged features are the genre's stock, which would mean that lay judgment does not give selection and arrangement the independent weight the doctrine gives it.

S4-H4. *Sides.* Probabilities of copying are highest on the plaintiff's side and lowest on the defendant's, despite the instruction to judge honestly, and each side's prediction of the jury leans its own way, the self-serving bias of Babcock and Loewenstein (1997).

S4-H5. *Filtering.* The share of shared features marked standard for the genre rises with distinctiveness more than with prevalence in every role, and is higher on the defendant's side.

S4-H6. *Mapping.* In scattered cases, participants on the plaintiff's side report a corresponding character more often than participants on the defendant's side, who more often answer "no one." In aligned cases the roles do not differ. This is the pragmatic effect of Spellman and Holyoak transferred to adversaries.

## 10.6 Analysis and sample size

Probabilities are analyzed as log-odds after the usual adjustment for 0 and 100, in a linear mixed model with arrangement, P, D, their interactions with arrangement, and role, random intercepts for participants and shells, a random intercept for each shell-by-condition version, and a participant slope for arrangement. The raw scale and an ordinal model are robustness checks. Checklist responses and mapping responses are analyzed with logistic mixed models. The slope of the log-odds on the model's summed weight estimates how conservative participants are relative to the model (Edwards, 1968).

The free-text statements of purpose are coded for which features they mention by the method of Study 1: three language models with a two-of-three rule, validated against two human coders on a sample, with the registered agreement threshold.

No earlier study gives variance components for this task, so the simulation rests on assumed values, stated in Appendix C, and its results hold only under them. With 12 shells and 50 participants per role, the assumed effects of arrangement (12 points on the 0-to-100 scale), prevalence (8), distinctiveness (8, where present) and role (6 on each side of neutral) are each detected in 96% of simulations or more. When distinctiveness has no effect, the test rejects in 2% to 10% of simulations, around the nominal 5%. The interaction of arrangement with the kind of shared features (S4-H3) is the weak point. An interaction of 6 points is detected in 52% to 65% of simulations with 12 shells and in 60% to 74% with 18. An interaction of 9 points is detected in 87% to 96% with 12 shells and in 92% to 98% with 18. The proposal is 12 shells and 70 usable participants per role, 210 in all, on the understanding that S4-H3 has good power only for an interaction about three quarters the size of the arrangement effect. Six more shells would raise that power and cost half again as much writing and review.

# 11. Study 5: showing the counts

## 11.1 Purpose

The law review proposes that courts be given counts. Study 5 tests what counts do to judgment. Its sharpest prediction comes from the paper's central claim: for features on which prevalence and distinctiveness disagree, the count a fact-finder is shown should decide whether the feature is called stock. If so, an expert's choice of statistic is not a neutral act, which is the behavioral form of the paper's argument that the doctrine must say which property it means.

## 11.2 Design

The format of the expert's report varies between participants: no count; prevalence only; distinctiveness only; both; and the increment (the feature's rate in the genre beside its rate in all films). Within participants, the features come from the four Study 1 cells. Each participant judges three disputes, one in each of three genres, with eight claimed similarities each, two from each cell.

## 11.3 Materials

The 48 features are Study 1 rated items, two per cell per genre, chosen for concreteness and for narrow rating intervals in Study 1. The counts are the corpus's own and are described truthfully as counts from summaries of 45,958 films. They are given as natural frequencies with a rounded rate, which people handle better than bare probabilities (Gigerenzer and Hoffrage, 1995). For the bounty hunter the prevalence report reads: "A researcher counted 1,362 Westerns. 26 of them include a bounty hunter: about 2 in every 100." The distinctiveness report reads: "A researcher counted 76 films of all kinds that include a bounty hunter. 26 of them are Westerns: about 34 in every 100." For the hero's father the two reports are 288 of 1,362 Westerns, about 21 in every 100, and 288 of 11,207 films with a father, about 3 in every 100.

## 11.4 Procedure and measures

For each dispute participants read the frame (a screenplay, a later film, a claim of copying) and then, for each claimed similarity with its report, rate whether it is a stock feature of the genre (1 to 7, with the Restatement's words as in Study 2) and how strongly it suggests copying (1 to 7). The two ratings are collected in separate passes through the features, in an order counterbalanced between participants. After each dispute they give an overall probability of copying. A short numeracy scale and the closing questions follow.

## 11.5 Hypotheses

S5-H1. *The count shown decides the classification.* The gap in stock ratings between rare-but-characteristic and common-but-uncharacteristic features (LH minus HL) is more positive in the distinctiveness format than in the prevalence format. Study 1 puts the gap at about +0.8 with no count. A reversal of its sign in the prevalence format is the strong form of the prediction.

S5-H2. *Counts and copying.* The correlation between copying ratings and the model's weight is higher in the prevalence format than with no count. In the distinctiveness format it is no higher, and may be lower, because a high share of a feature's films being Westerns reads as a reason to discount a feature that few Westerns have.

S5-H3. *Both counts.* With both shown, stock ratings weight distinctiveness more than prevalence, as unaided ratings do. This test is two-sided.

S5-H4. *The increment.* With the increment format, stock ratings follow the increment, which at the top of a genre means following prevalence among characteristic features.

S5-H5. *Numeracy.* The effects of format are larger for participants with higher numeracy.

## 11.6 Analysis, sample and sample size

Ratings are analyzed with the mixed models of Study 2, with format and its interactions with P and D, and a random slope for format by item. Because this study is about fact-finders, a sample of jury-eligible adults from an online panel would suit it better than the subject pool; Section 16 leaves the choice open.

The test of S5-H1 compares two formats. With 60 participants per format, a shift of 0.6 points between the formats in the gap is detected in 84% of simulations, a shift of 0.8 in 94%, and a shift of 1.0 in 100%. With 40 per format the figures are 84%, 94% and 98%. A reversal of the gap Study 1 found would be a shift of well over a point. The proposal is 60 usable participants per format, 300 in all, which leaves the other three formats enough participants for their own comparisons. Forty per format, 200 in all, would lose little for S5-H1.

# 12. Methods common to the four studies

*Participants.* Studies 2 to 4 are planned for the UCLA psychology subject pool, with course credit, under the conditions of Study 1. Anyone who took part in Study 1, or in an earlier study of this series, is excluded through the pool's prerequisite settings, because all of them expose participants to the items.

*Platform.* Each study is a plain-JavaScript page hosted on Pavlovia, built from the Study 1 code: the consent page, the device check, the reading task, the hidden-instruction check, the task check, the instructed-response attention checks, the closing questions and the credit redirect are reused unchanged. Each study gets its own Pavlovia project and its own deployment script fixed to that project. Study 2's page is built in `Experiment/Study 2/` for the project `genres-and-themes/experiment-2`, and has been run locally in every condition. David does the pushes.

*Assignment.* Conditions are assigned from the numeric survey code, as in Study 1: the code modulo the number of cells picks the cell. Study 2 has 48 cells, four conditions by the twelve genre schedules, and the cell modulo four is the condition, so consecutive sign-ups rotate through the conditions.

*Exclusions.* Study 1's rules apply in their registered order, without the rule about the quality of listed responses, which has no counterpart: failing the hidden-instruction check; a median reading time under 150 ms per word on either reading sentence; failing the task check twice; passing fewer than all four attention checks; an incomplete session; reported use of an AI tool; a repeated identifier; and a self-report of not taking part seriously. The tracked condition of Study 2 adds the rules proposed in Section 8.9.

*Stopping.* Each study has a fixed target of usable participants per condition and stops when it is met or the term ends. There are no interim analyses.

*Preregistration and materials.* Each study is preregistered as one document in the format of Study 1's, with the materials in a release of a GitHub repository cited by commit.

*Ethics.* The tasks are judgments about fictional disputes and carry the same minimal risk as Study 1's. Whether the existing exemption (IRB-25-2264) describes these tasks, and whether it covers an online panel if Study 5 uses one, should be confirmed before preregistration.

# 13. Modeling

The studies are designed so that every judgment has a model prediction computed before the data exist.

*The causal model with corpus statistics.* For each item, pair or set, the copying weight, the increment, the genre's strength and the share due to the genre come from the corpus counts. The model has two free parameters when fit to ratings, the fidelity of copying $\kappa$ and the prior probability of copying, plus a linear map from log-odds to the response scale.

*The causal model with subjective statistics.* The same model with each item's estimated frequencies from the frequency block in place of corpus counts. Comparing it with the corpus version separates errors of belief from errors of inference (S2-H8).

*The one-intuition model.* Every judgment is a linear function of a single item-level typicality value, taken from Study 1's ratings or from the GENRE condition of Study 2, with a sign that depends on the question.

*Comparison.* Models are compared by held-out log-likelihood in ten folds by participant and by AIC, the criteria registered for Study 1's H3.

*Mapping.* For Study 4, the synopses can be given to a model of analogical mapping to predict the correspondences participants report. Two candidates fit the lineage of the paradigm: ACME (Holyoak and Thagard, 1989), which Spellman and Holyoak used and in which a goal acts by inhibiting attention to irrelevant relations, and Probabilistic Analogical Mapping (Lu, Ichien and Holyoak, 2022), which builds semantic relation networks from distributed representations of words and relations and so would not need hand-coded propositions. Either would give a principled measure of how much relational structure two synopses share, which is the quantity the model of Section 4 lacks. Whether to include this is a decision for Keith (Section 16).

# 14. What each result would mean

| Result | For the theory | For the law |
|--------------------------|-------------------------------------|-------------------------------------|
| Copying judged by prevalence alone (Study 2) | People reason about the source of a feature as a causal model prescribes; Study 1's reliance on distinctiveness was specific to its question | Lay fact-finders can use the right fact for copying in fact; the difficulty is that they are rarely given it |
| Copying judged by typicality (Study 2) | One representativeness-based sense of the genre answers every question | Intuitive fact-finding discounts rare-but-characteristic features, which are the strongest evidence of copying, and credits common ones; counts are needed most where intuition is most confident |
| The question does not change the weights (Study 2) | The distinction between category validity and cue validity is not one people draw unaided | The two steps of the infringement test collapse into one impression in lay judgment |
| Paths bend toward "Coincidence" for characteristic features although choices follow prevalence (Study 2, tracked) | The sense of what is typical is active and is overruled: intuition corrected by the question | Fact-finders can reach the right answer on copying, but against a live intuition, which haste or load might let through |
| Choices follow prevalence and paths show no such bend (Study 2, tracked) | The question selects the statistic from the start | The obstacle to accurate fact-finding on copying is the missing count, with no competing intuition to overcome |
| Necessity ratings follow conditional counts (Study 3) | The corpus has a usable measure of necessity | The *Reyher* formulation can be given the same kind of evidence as the Restatement's |
| Implied pairs counted as much as unrelated pairs, or more (Study 3) | Correlation neglect, or coherence, in judgments of similarity | Lists of similarities overstate the evidence when their items come as a package |
| Arrangement counts regardless of the parts (Study 4) | Relational structure drives similarity, as structure-mapping holds | Lay judgment matches *Metcalf* |
| Arrangement counts less for stock parts (Study 4) | Feature typicality and structure interact | Lay judgment gives selection and arrangement less protection than doctrine does |
| Sides differ in mapping and filtering (Study 4) | Pragmatic control of mapping extends to adversarial goals | Party-compiled lists of similarities and party experts' accounts of what is stock are shaped by purpose, as *Litchfield* suspects |
| The count shown decides the classification (Study 5) | Explicit statistics override the intuitive weighting | An expert's choice between prevalence and distinctiveness decides outcomes for divergent features; courts must say which property they mean |

: Table 9. Possible results and their meaning.

# 15. Threats, and corpus work alongside the studies

*Demand.* Participants in the COPY condition might guess that rare things are meant to count. The instructions do not say so, the items are not labeled, and the frequency block comes last. The one-intuition account predicts a result that no demand explanation produces.

*Word frequency and familiarity.* A rare word may seem a rare feature. Everyday word frequency is a covariate in every model, as in Study 1, and familiarity with each genre is measured.

*The scale.* Ratings of evidence are not probabilities. The analysis treats them as monotone in the log-odds, tests ordinal versions, and in Studies 4 and 5 collects probabilities directly.

*Item sets.* Abstract items such as "fate" or "truth" are odd as claimed similarities. They are kept in Study 2 for comparability with Study 1 and analyzed with and without them; Studies 3 to 5 use concrete features only.

*The corpus as ground truth.* Prevalence in plot summaries is not prevalence in films, and neither is what an author would have written. The studies compare judgments with the counts and with participants' own estimates; they do not assume the counts are right about the world.

*Mouse tracking outside the laboratory.* Participants in the tracked condition use their own mice and trackpads on their own screens, and paths differ with the device. The design answers this in four ways: every trial begins from the same place and the item appears only once the hand is moving; the window must be large enough before a block starts; the Stroop trials give each session a conflict effect of known direction against which its paths can be judged; and the device is recorded and used as a covariate. The tests compare trials within a participant, so differences between devices add noise without favoring a hypothesis.

*Generality.* Six genres, film only, undergraduates in three of the four studies.

Some corpus work would strengthen the next paper and needs no participants. A curated set of remakes and adaptations, from a public source that records which film is a remake of which, would replace the shared-title stand-in of Section 6.3 and test properly whether weighting shared features by surprisal detects derivation better than counting them or weighting them by distinctiveness. The baseline of Section 6.2 could also be extended to events (Notebook 13) and to pairs, so that shared structure can be given a count.

# 16. Sequence and decisions

## 16.1 A proposed order

Study 2 can be preregistered first: its items exist, its experiment is built, and the analysis of its ratings is Study 1's. What it still needs is listed below. Study 5 reuses Study 2's items and adds only the display of counts, so it can be built alongside Study 2 and run on a different sample. Study 3 needs a stimulus notebook and a review of the drawn pairs. Study 4 needs the most work: the shells have to be written and reviewed, and the page for comparing two synopses is new. For the cognitive science paper, Studies 2 and 4 would make a complete argument, with Studies 3 and 5 either in the same paper or held for the next.

## 16.2 Decisions made on November 18

David decided three things on November 18. The two-genre choice study is retired. Mouse tracking moves to the copying judgment, as a fourth condition of what was Experiment 3A. And the experiments are numbered as studies: 3A is Study 2, 3B is Study 3, 3C is Study 4 and 3D is Study 5.

## 16.3 Decisions still needed

1. Which of Studies 3 to 5 to run, and in what order. The recommendation is Study 2 first, then Study 4, with Study 5 alongside Study 2 if a panel sample can be paid for.
2. For Study 2, whether to add PROTECT as a fifth condition, and whether to use the 288 normed items or the extended set of 432. The power analysis favors the extended set, which would have to be drawn from Notebook 10's queues and reviewed before the experiment's item files are replaced. The number of conditions fixes the assignment rule, so it has to be settled before the first session.
3. For Study 2, the wording of the COPY question and whether the equivalence bound of ±0.40 is the right smallest effect of interest.
4. For the tracked condition of Study 2: whether the second box should read "Coincidence," as built, or "Not copied," since a feature the genre explains is not quite a coincidence; whether tracked participants should judge two genres, as built, or more, which Section 8.9 shows would help most in telling the two pulls apart; and the rules of Section 8.9 for leaving out trials and sessions.
5. Whether necessity (Study 3) should stay in this series, as proposed, or be run separately as first planned.
6. For Study 4, who writes the story shells, how many (12 or 18), and whether the roles should be lawyers' assistants, as proposed, or the writers themselves, as in Spellman and Holyoak.
7. For Study 5, the subject pool or a paid online panel of jury-eligible adults, and the budget for the latter.
8. Whether Keith's lab would model the Study 4 mappings with ACME or with Probabilistic Analogical Mapping.
9. Whether to write to Barbara Spellman for the 1996 story materials and her comments on the design.
10. Whether each study gets its own preregistration or Studies 2 and 3 share one.
11. Confirmation that the existing exemption covers these tasks.
12. Whether the corpus work of Section 15 should start now.
13. Before Study 2 can launch: the SONA listing and its credit address; a session in each condition run by the investigators with a real mouse, after which the time limit and the estimated length are fixed; David's push to Pavlovia; and the preregistration. The GitHub repository made for this paper is public and empty, and whether it should be private until the preregistrations are filed is David's call.

# Appendix A. Instructions and questions

Bracketed words change with the genre: [Westerns] stands for Westerns, Horror films, Crime films, Science Fiction films, Comedies or Fantasy films, and [a Western] for a Western, a Horror film, a Crime film, a Science Fiction film, a Comedy or a Fantasy film. All ratings use a row of seven buttons with the end labels shown. The wording of Study 2 (A.1 to A.6) is that of the experiment as built.

## A.1 Study 2, COPY condition

Instructions: "In this part you will think about two [Westerns]. One is a screenplay. The other is a film that was made a few years later by different people. The screenwriter says that the people who made the film copied from the screenplay. The people who made the film say they never saw the screenplay and came up with the film on their own. You will not read the screenplay or see the film. We will show you, a few at a time, things that both of them include. For each one, tell us how strongly it suggests that the film was copied from the screenplay. Some things that two [Westerns] have in common say very little about whether one was copied from the other. Others say a lot. Please use the whole scale."

Each item: "Both the screenplay and the film include: **[item]**. How strongly does this suggest that the film was copied from the screenplay?" 1 = Not at all; 7 = Very strongly.

## A.2 Study 2, GENRE condition

Instructions: "In this part you will think about [Westerns]. We will show you, a few at a time, things that [a Western] includes. Films include things for different reasons. Some things are in a film because of the kind of film it is. Others would be just as likely in a film of any kind. For each one, tell us how much it is in the film because the film is [a Western]. Please use the whole scale."

Each item: "[A Western] includes: **[item]**. How much is this in the film because the film is [a Western]?" 1 = Not at all (it could be in any kind of film); 7 = Entirely (it is there because the film is [a Western]).

## A.3 Study 2, STOCK condition

Instructions: "Copyright law lets a writer own the particular way a story is told. It does not let anyone own the stock features of a kind of story. A standard legal reference describes these as features that are 'standard, stock, customary, stereotypical, or common' in stories of that kind. Anyone may use them. We will show you, a few at a time, things that [a Western] might include. For each one, tell us whether it is a stock feature of [Westerns] in this sense. Please use the whole scale."

Each item: "In [Westerns]: **[item]**. Is this a stock feature of [Westerns]?" 1 = Definitely not; 7 = Definitely.

The quoted adjectives are the Restatement's as the manuscript quotes them; the manuscript's check of the black-letter text is still open and this wording should follow it.

## A.4 Study 2, PROTECT condition (if run)

The five sentences of A.1 that set out the dispute, then: "You will not read the screenplay or see the film. We will show you, a few at a time, things that both of them include. For each one, tell us whether the screenwriter should be able to stop the film's makers from using it. Please use the whole scale." Each item: "Both the screenplay and the film include: **[item]**. Should the screenwriter be able to stop the film's makers from using this?" 1 = Definitely not; 7 = Definitely.

## A.5 Study 2, TRACK condition

Before each genre: "In this part you will think about two [Westerns]. One is a screenplay. The other is a film that was made a few years later by different people. The screenwriter says that the people who made the film copied from the screenplay. The people who made the film say they never saw the screenplay and came up with the film on their own. You will not read the screenplay or see the film. We will show you, one at a time, things that both of them include. For each one, choose what is more likely: that the film's makers copied it from the screenplay, or that it is a coincidence, meaning that they came up with it on their own. Some things that two [Westerns] have in common say very little about whether one was copied from the other. Others say a lot. There are no right or wrong answers. Click Start, keep the mouse moving upward, and click your choice as quickly as you can while still choosing carefully."

Each trial: the line "Two [Westerns] both include:" and, once the mouse is moving, **[item]**. The boxes read "Copied" and "Coincidence."

Stroop practice: "Each trial starts when you click Start at the bottom of the screen. As soon as you click it, start moving the mouse upward. A word will appear once you move. Move to the box that names the color of the ink the word is printed in, and click it. Ignore what the word says. For example, if the word BLUE is printed in red ink, choose Red. Keep the mouse moving from the moment you click Start, and answer as quickly and accurately as you can."

Practice choices: "The boxes now say Copied and Coincidence. Imagine a screenplay and a later film made by different people. The screenwriter says the film was copied from the screenplay; the film's makers say they came up with it on their own. Each trial shows one thing that the screenplay and the film both include. Choose Copied if you think the film's makers more likely copied it, and Coincidence if you think they more likely came up with it on their own."

## A.6 Frequency estimates (Study 2, all conditions)

Each answer is given on a slider from 0 to 100 in steps of 1. The slider shows no handle until the participant clicks it, so that no starting position can pull the answer, and the number chosen is displayed beside the item.

"Think of 100 [Westerns] chosen at random. How many of them include each of the following?"

"Think of 100 films of all kinds chosen at random. How many of them include each of the following?"

"For each of the following, think of 100 films of any kind that include it. How many of those 100 films are [Westerns]?"

## A.7 Study 3

COPY condition, pairs: the instructions of A.1 with "things" replaced by "pairs of things." Each trial: "Both the screenplay and the film include: **[first]** and **[second]**. How strongly does this suggest that the film was copied from the screenplay?"

NECESSITY condition: "In this part you will think about [Westerns]. We will tell you one thing a [Western] includes and ask about a second thing. For each pair, tell us how necessary the second thing is in a [Western] that has the first." Each trial: "A [Western] includes **[first]**. How necessary is it that it also includes **[second]**?" 1 = Not at all (it could easily be left out); 7 = Completely (the story could not do without it). Estimates: "Think of 100 [Westerns] that include **[first]**. How many of them also include **[second]**?" and "Think of 100 [Westerns] chosen at random. How many of them include **[second]**?"

## A.8 Study 4

Role, plaintiff's side: "A screenwriter believes that a film was copied from her screenplay and has gone to court. You are working with her lawyers. Your job is to help them prepare by looking closely at the screenplay and the film." Defendant's side: "A screenwriter believes that a film was copied from her screenplay and has gone to court. The people who made the film say they never saw it. You are working with their lawyers. Your job is to help them prepare by looking closely at the screenplay and the film." Juror: "A screenwriter believes that a film was copied from her screenplay and has gone to court. The people who made the film say they never saw it. You are a member of the jury."

Statement of purpose: "Before you read the cases, tell us in two or three sentences what you will look for [on behalf of the screenwriter / on behalf of the film's makers / in deciding the case]."

To all: "You will read eight cases like this one, each about a different screenplay and film. For every case, whatever your role, please give your honest judgment."

Per case: "How likely is it that the makers of the film copied from the screenplay?" (0 = certainly did not, 100 = certainly did). "How similar are the screenplay and the film?" 1 = Not at all similar; 7 = Extremely similar. "Which character in the film corresponds to the screenplay's **[character]**?" (the film's characters, and "no one"). For each listed feature: "In both, and it counts toward copying" / "In both, but it is standard for [Westerns], so it should not count" / "Not in both." "Who should win?" (the screenwriter; the film's makers) and "How confident are you?" 1 to 7. On a side only: "What do you think a jury would decide?"

## A.9 Study 5

Frame, per dispute: "A screenwriter says a later [Western] film was copied from her [Western] screenplay. Her lawyers have listed things the two have in common. [In the count formats: An expert who counted the features of 45,958 film plot summaries has reported on each one.]" Per feature: the report in the participant's format, then, in one pass, "Is this a stock feature of [Westerns]?" 1 = Definitely not; 7 = Definitely (with the definition of A.3), and in the other pass, "How strongly does this suggest that the film was copied from the screenplay?" 1 = Not at all; 7 = Very strongly.

Increment format, bounty hunter: "About 2 in every 100 Westerns include a bounty hunter. About 2 in every 1,000 films of all kinds do."

# Appendix B. An example case for Study 4

The example is a Western shell filled from the rare-but-characteristic cell. The four shared features are a bounty hunter and a ranch hand (kinds of character), a barn (setting) and a stampede (event). In the corpus they are in 1.9%, 2.0%, 1.6% and 1.8% of Westerns. The unshared detail in this example is illustrative; in the experiment it is drawn from the middle third of the genre.

*The screenplay.* A bounty hunter rides into a mining valley looking for a man wanted for a killing back east. The man has been working as a ranch hand under another name and is well liked. The bounty hunter learns who he is and corners him one night in a barn. Before he can take him in, a stampede scatters the herd, and the two men have to ride together until dawn to turn it. By morning the bounty hunter has to decide whether to collect.

*The film, aligned.* A bounty hunter arrives in a river town on the trail of a fugitive. The fugitive has hired on as a ranch hand at a spread outside town, and the owner trusts him. The bounty hunter catches up with him in a barn after dark. A stampede breaks out before he can bring him in, and the two must work side by side to save the cattle. In the end the bounty hunter must choose whether to turn him over.

*The film, scattered.* A widow hires a bounty hunter to find her brother, who went west ten years ago and stopped writing. On the road the bounty hunter is robbed and left for dead, and a ranch hand takes him in until he can ride. The brother, it turns out, died years ago in a stampede. The widow sells what he left her, and the film ends at the auction, held in a barn.

The same shell filled from the common-and-characteristic cell would share a sheriff, an outlaw, a saloon and a gunfight; from the common-but-uncharacteristic cell, a father, a daughter, a house and a death; and from the rare-and-uncharacteristic cell, a lawyer, a lady, a bridge and a funeral.

# Appendix C. Power simulations

The simulations are in `Analysis/studies2to5_design/studies2to5_power.Rmd`. Each scenario was simulated 200 times, and each simulated data set was analyzed with the mixed model proposed for the study and a Wald test at the .05 level. For the rating tasks the standard deviations are Study 1's (items 0.99, participants 0.61, the participant slope for distinctiveness 0.59, the participant slope for prevalence 0.09, residual 1.30). For the choices of the tracked condition the same values are converted to logits on the assumption that a choice is the rating cut at a threshold, which makes one rating point 1.31 logits and the equivalence bound ±0.52 logits. For the curvature of mouse paths no estimates exist: the simulation works in units of the trial-to-trial standard deviation of curvature and assumes a participant standard deviation of 0.6, participant slopes of 0.15 for each pull, and an item standard deviation of 0.15. For Study 4 no estimates exist either, and the simulation assumes a participant standard deviation of 14 points on the 0-to-100 scale, a participant slope for arrangement of 8, a shell standard deviation of 6, a further deviation of 5 for each shell-by-condition version, and a residual of 18. For Study 5 each item is given a further deviation of 0.5 points in each format. These are assumptions, not data.

| Account simulated | Items | Participants per condition | P minus D below zero | P minus D above zero | D differs from zero | D within ±0.40 | D within ±0.30 | P differs from zero |
|------------------|-------|-------------|----------|----------|----------|---------|---------|----------|
| one intuition | 288 | 50 | 0% | 98% | 100% | 0% | 0% | 54% |
| one intuition | 288 | 70 | 0% | 100% | 100% | 0% | 0% | 60% |
| one intuition | 288 | 90 | 0% | 99% | 100% | 0% | 0% | 56% |
| one intuition | 432 | 50 | 0% | 100% | 100% | 0% | 0% | 70% |
| one intuition | 432 | 70 | 0% | 100% | 100% | 0% | 0% | 71% |
| one intuition | 432 | 90 | 0% | 100% | 100% | 0% | 0% | 76% |
| overall frequency | 288 | 50 | 100% | 0% | 98% | 0% | 0% | 100% |
| overall frequency | 288 | 70 | 100% | 0% | 98% | 0% | 0% | 100% |
| overall frequency | 288 | 90 | 100% | 0% | 99% | 0% | 0% | 100% |
| overall frequency | 432 | 50 | 100% | 0% | 100% | 0% | 0% | 100% |
| overall frequency | 432 | 70 | 100% | 0% | 100% | 0% | 0% | 100% |
| overall frequency | 432 | 90 | 100% | 0% | 100% | 0% | 0% | 100% |
| query-sensitive | 288 | 50 | 86% | 0% | 4% | 74% | 27% | 100% |
| query-sensitive | 288 | 70 | 91% | 0% | 6% | 71% | 32% | 100% |
| query-sensitive | 288 | 90 | 90% | 0% | 5% | 79% | 42% | 99% |
| query-sensitive | 432 | 50 | 94% | 0% | 6% | 83% | 45% | 100% |
| query-sensitive | 432 | 70 | 98% | 0% | 5% | 90% | 58% | 100% |
| query-sensitive | 432 | 90 | 98% | 0% | 4% | 92% | 65% | 100% |

: Table C1. Study 2, COPY rating: share of simulations in which each test gives the stated result.

| Account simulated | Items | Participants in the tracked condition | Share choosing Copied | P minus D below zero | P minus D above zero | D differs from zero | D within the bound | P differs from zero |
|----------------------|-------|-------------|---------|----------|----------|----------|---------|----------|
| one intuition | 288 | 50 | 50% | 0% | 96% | 100% | 0% | 47% |
| one intuition | 288 | 70 | 50% | 0% | 98% | 100% | 0% | 48% |
| one intuition | 288 | 90 | 50% | 0% | 98% | 100% | 0% | 49% |
| one intuition | 432 | 50 | 50% | 0% | 100% | 100% | 0% | 62% |
| one intuition | 432 | 70 | 50% | 0% | 100% | 100% | 0% | 68% |
| one intuition | 432 | 90 | 50% | 0% | 100% | 100% | 0% | 68% |
| overall frequency | 288 | 50 | 50% | 100% | 0% | 97% | 0% | 100% |
| overall frequency | 288 | 70 | 50% | 100% | 0% | 98% | 0% | 100% |
| overall frequency | 288 | 90 | 50% | 100% | 0% | 98% | 0% | 100% |
| overall frequency | 432 | 50 | 50% | 100% | 0% | 100% | 0% | 100% |
| overall frequency | 432 | 70 | 50% | 100% | 0% | 99% | 0% | 100% |
| overall frequency | 432 | 90 | 50% | 100% | 0% | 100% | 0% | 100% |
| query-sensitive | 288 | 50 | 50% | 80% | 0% | 5% | 70% | 100% |
| query-sensitive | 288 | 70 | 50% | 83% | 0% | 8% | 74% | 100% |
| query-sensitive | 288 | 90 | 50% | 86% | 0% | 4% | 81% | 100% |
| query-sensitive | 432 | 50 | 50% | 89% | 0% | 5% | 86% | 100% |
| query-sensitive | 432 | 70 | 50% | 98% | 0% | 4% | 94% | 100% |
| query-sensitive | 432 | 90 | 50% | 97% | 0% | 5% | 94% | 100% |
| query-sensitive, a quarter Copied | 288 | 70 | 32% | 86% | 0% | 2% | 80% | 99% |
| query-sensitive, a quarter Copied | 432 | 70 | 32% | 96% | 0% | 2% | 90% | 100% |

: Table C2. Study 2, TRACK condition, choice of "Copied": share of simulations in which each test gives the stated result. The bound for D is the logit equivalent of ±0.40 rating points.

| Genres per participant | Pull of typicality (trial SDs) | Items | Participants | Item trials per participant | Pull of typicality detected | Pull of prevalence (0.10) detected | The two pulls told apart |
|----------|------------|-------|------------|------------|------------|--------------|------------|
| 2 | 0.10 | 288 | 50 | 96 | 79% | 84% | 6% |
| 2 | 0.10 | 288 | 70 | 96 | 89% | 94% | 6% |
| 2 | 0.10 | 288 | 90 | 96 | 97% | 99% | 6% |
| 2 | 0.10 | 432 | 50 | 144 | 92% | 94% | 7% |
| 2 | 0.10 | 432 | 70 | 144 | 96% | 99% | 6% |
| 2 | 0.10 | 432 | 90 | 144 | 98% | 100% | 7% |
| 2 | 0.15 | 288 | 50 | 96 | 100% | 84% | 25% |
| 2 | 0.15 | 288 | 70 | 96 | 100% | 96% | 23% |
| 2 | 0.15 | 288 | 90 | 96 | 100% | 96% | 30% |
| 2 | 0.15 | 432 | 50 | 144 | 98% | 93% | 26% |
| 2 | 0.15 | 432 | 70 | 144 | 100% | 98% | 40% |
| 2 | 0.15 | 432 | 90 | 144 | 100% | 100% | 40% |
| 2 | 0.20 | 288 | 50 | 96 | 100% | 83% | 52% |
| 2 | 0.20 | 288 | 70 | 96 | 100% | 94% | 63% |
| 2 | 0.20 | 288 | 90 | 96 | 100% | 98% | 72% |
| 2 | 0.20 | 432 | 50 | 144 | 100% | 94% | 66% |
| 2 | 0.20 | 432 | 70 | 144 | 100% | 98% | 79% |
| 2 | 0.20 | 432 | 90 | 144 | 100% | 100% | 86% |
| 6 | 0.10 | 288 | 70 | 288 | 100% | 99% | 13% |
| 6 | 0.15 | 288 | 70 | 288 | 100% | 100% | 44% |
| 6 | 0.20 | 288 | 70 | 288 | 100% | 100% | 93% |

: Table C3. Study 2, TRACK condition, curvature: share of simulations in which each pull is detected, and in which the two are distinguished, when choices follow prevalence alone. Where the two pulls are equal (0.10), the last column is the false-positive rate.

| Difference (points) | Pairs | Participants per question | Detected |
|---|---|---|---|
| 0.3 | 96 | 60 | 28% |
| 0.3 | 96 | 80 | 26% |
| 0.3 | 96 | 100 | 30% |
| 0.3 | 144 | 60 | 40% |
| 0.3 | 144 | 80 | 32% |
| 0.3 | 144 | 100 | 38% |
| 0.4 | 96 | 60 | 38% |
| 0.4 | 96 | 80 | 46% |
| 0.4 | 96 | 100 | 47% |
| 0.4 | 144 | 60 | 52% |
| 0.4 | 144 | 80 | 56% |
| 0.4 | 144 | 100 | 57% |
| 0.5 | 96 | 60 | 60% |
| 0.5 | 96 | 80 | 69% |
| 0.5 | 96 | 100 | 63% |
| 0.5 | 144 | 60 | 74% |
| 0.5 | 144 | 80 | 78% |
| 0.5 | 144 | 100 | 82% |
| 0.6 | 96 | 60 | 76% |
| 0.6 | 96 | 80 | 80% |
| 0.6 | 96 | 100 | 80% |
| 0.6 | 144 | 60 | 90% |
| 0.6 | 144 | 80 | 88% |
| 0.6 | 144 | 100 | 86% |

: Table C4. Study 3 with unmatched pairs.

| Share of pair variance common to a set | Difference (points) | Pairs | Participants per question | Detected |
|--------------------|------------|--------|--------------|----------|
| 0.25 | 0.3 | 96 | 60 | 30% |
| 0.25 | 0.3 | 96 | 80 | 40% |
| 0.25 | 0.3 | 144 | 60 | 41% |
| 0.25 | 0.3 | 144 | 80 | 44% |
| 0.25 | 0.4 | 96 | 60 | 51% |
| 0.25 | 0.4 | 96 | 80 | 59% |
| 0.25 | 0.4 | 144 | 60 | 70% |
| 0.25 | 0.4 | 144 | 80 | 68% |
| 0.25 | 0.5 | 96 | 60 | 65% |
| 0.25 | 0.5 | 96 | 80 | 72% |
| 0.25 | 0.5 | 144 | 60 | 86% |
| 0.25 | 0.5 | 144 | 80 | 88% |
| 0.25 | 0.6 | 96 | 60 | 84% |
| 0.25 | 0.6 | 96 | 80 | 91% |
| 0.25 | 0.6 | 144 | 60 | 93% |
| 0.25 | 0.6 | 144 | 80 | 95% |
| 0.5 | 0.3 | 96 | 60 | 38% |
| 0.5 | 0.3 | 96 | 80 | 46% |
| 0.5 | 0.3 | 144 | 60 | 59% |
| 0.5 | 0.3 | 144 | 80 | 60% |
| 0.5 | 0.4 | 96 | 60 | 64% |
| 0.5 | 0.4 | 96 | 80 | 71% |
| 0.5 | 0.4 | 144 | 60 | 76% |
| 0.5 | 0.4 | 144 | 80 | 76% |
| 0.5 | 0.5 | 96 | 60 | 84% |
| 0.5 | 0.5 | 96 | 80 | 86% |
| 0.5 | 0.5 | 144 | 60 | 94% |
| 0.5 | 0.5 | 144 | 80 | 96% |
| 0.5 | 0.6 | 96 | 60 | 93% |
| 0.5 | 0.6 | 96 | 80 | 94% |
| 0.5 | 0.6 | 144 | 60 | 98% |
| 0.5 | 0.6 | 144 | 80 | 100% |

: Table C5. Study 3 with matched sets.

| Interaction assumed (points) | Distinctiveness effect assumed | Shells | Participants per role | Arrangement | Prevalence | Distinctiveness | Role | Arrangement by prevalence |
|------------|--------------|--------|-------------|------------|-----------|--------------|-------|-------------|
| 6 | -8 | 12 | 50 | 100% | 100% | 100% | 98% | 57% |
| 6 | -8 | 12 | 70 | 100% | 100% | 100% | 100% | 52% |
| 6 | -8 | 12 | 90 | 100% | 100% | 100% | 100% | 61% |
| 6 | -8 | 18 | 50 | 100% | 100% | 100% | 96% | 60% |
| 6 | -8 | 18 | 70 | 100% | 100% | 100% | 100% | 70% |
| 6 | -8 | 18 | 90 | 100% | 100% | 100% | 100% | 73% |
| 6 | 0 | 12 | 50 | 100% | 100% | 5% | 98% | 56% |
| 6 | 0 | 12 | 70 | 100% | 100% | 6% | 100% | 56% |
| 6 | 0 | 12 | 90 | 100% | 100% | 3% | 100% | 65% |
| 6 | 0 | 18 | 50 | 100% | 100% | 3% | 98% | 62% |
| 6 | 0 | 18 | 70 | 100% | 100% | 5% | 100% | 70% |
| 6 | 0 | 18 | 90 | 100% | 100% | 3% | 100% | 74% |
| 9 | -8 | 12 | 50 | 100% | 100% | 100% | 98% | 87% |
| 9 | -8 | 12 | 70 | 100% | 100% | 100% | 100% | 90% |
| 9 | -8 | 12 | 90 | 100% | 100% | 100% | 100% | 96% |
| 9 | -8 | 18 | 50 | 100% | 100% | 100% | 98% | 92% |
| 9 | -8 | 18 | 70 | 100% | 100% | 100% | 100% | 95% |
| 9 | -8 | 18 | 90 | 100% | 100% | 100% | 100% | 96% |
| 9 | 0 | 12 | 50 | 100% | 100% | 2% | 98% | 88% |
| 9 | 0 | 12 | 70 | 100% | 100% | 8% | 100% | 88% |
| 9 | 0 | 12 | 90 | 100% | 100% | 6% | 100% | 93% |
| 9 | 0 | 18 | 50 | 100% | 100% | 10% | 97% | 92% |
| 9 | 0 | 18 | 70 | 100% | 100% | 6% | 100% | 98% |
| 9 | 0 | 18 | 90 | 100% | 100% | 4% | 100% | 98% |

: Table C6. Study 4: share of simulations in which each effect is detected. Where the distinctiveness effect is 0, the distinctiveness column is the false-positive rate.

| Shift between formats (points) | Participants per format | Detected |
|---|---|---|
| 0.6 | 40 | 84% |
| 0.6 | 60 | 84% |
| 0.6 | 80 | 88% |
| 0.8 | 40 | 94% |
| 0.8 | 60 | 94% |
| 0.8 | 80 | 98% |
| 1 | 40 | 98% |
| 1 | 60 | 100% |
| 1 | 80 | 99% |

: Table C7. Study 5: the difference between two count formats in the LH-minus-HL gap.


# Appendix D. Sources and their verification

The legal quotations in Section 3 were checked against the opinions in Descrybe on November 17, 2026: *Arnstein*, *Rentmeester*, *Ty* and *Litchfield* matched exactly (Descrybe's text of *Ty* has a scanning error in a different sentence); the *Metcalf* quotation was checked for the CogForum deck; the *Reyher* quotation and pin cite were checked on November 6. Pin cites for *Arnstein*, *Rentmeester*, *Ty*, *Litchfield* and *Metcalf* have not been added and should be taken from the reporters. Bibliographic details of the articles below were confirmed from publisher or index listings on November 17, 2026, unless marked. The mouse-tracking sources and Kahneman and Frederick (2002) were confirmed in the same way on November 1 and November 18. None of them was read in full, and what the text says of their findings rests on their abstracts and index summaries.

Babcock, L., & Loewenstein, G. (1997). Explaining bargaining impasse: The role of self-serving biases. *Journal of Economic Perspectives, 11*(1), 109–126.

Balganesh, S., Manta, I. D., & Wilkinson-Ryan, T. (2014). Judging similarity. *Iowa Law Review, 100*, 267. (As cited in the manuscript.)

Bordalo, P., Coffman, K., Gennaioli, N., & Shleifer, A. (2016). Stereotypes. *Quarterly Journal of Economics, 131*(4), 1753–1794.

Bundt, C., Ruitenberg, M. F. L., Abrahamse, E. L., & Notebaert, W. (2018). Early and late indications of item-specific control in a Stroop mouse tracking study. *PLOS ONE, 13*(5), e0197278.

Cheng, P. W. (1997). From covariation to causation: A causal power theory. *Psychological Review, 104*(2), 367–405.

Chin-Parker, S., & Ross, B. H. (2004). Diagnosticity and prototypicality in category learning: A comparison of inference learning and classification learning. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 30*(1), 216–226.

Dale, R., Kehoe, C., & Spivey, M. J. (2007). Graded motor responses in the time course of categorizing atypical exemplars. *Memory & Cognition, 35*(1), 15–28.

Edwards, W. (1968). Conservatism in human information processing. In B. Kleinmuntz (Ed.), *Formal representation of human judgment*. Wiley. (Not rechecked.)

Enke, B., & Zimmermann, F. (2019). Correlation neglect in belief formation. *Review of Economic Studies, 86*(1), 313–332.

Fernbach, P. M., Darlow, A., & Sloman, S. A. (2010). Neglect of alternative causes in predictive but not diagnostic reasoning. *Psychological Science, 21*(3), 329–336. (Title and DOI confirmed; volume and pages not rechecked.)

Freeman, J. B., & Ambady, N. (2010). MouseTracker: Software for studying real-time mental processing using a computer mouse-tracking method. *Behavior Research Methods, 42*(1), 226–241.

Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science, 7*(2), 155–170.

Gigerenzer, G., & Hoffrage, U. (1995). How to improve Bayesian reasoning without instruction: Frequency formats. *Psychological Review, 102*(4), 684–704. (Not rechecked.)

Griffiths, T. L., & Tenenbaum, J. B. (2007). From mere coincidences to meaningful discoveries. *Cognition, 103*(2), 180–226.

Holyoak, K. J., & Thagard, P. (1989). Analogical mapping by constraint satisfaction. *Cognitive Science, 13*(3), 295–355. (Not rechecked.)

Kahneman, D., & Tversky, A. (1972). Subjective probability: A judgment of representativeness. *Cognitive Psychology, 3*(3), 430–454. (Not rechecked.)

Kahneman, D., & Frederick, S. (2002). Representativeness revisited: Attribute substitution in intuitive judgment. In T. Gilovich, D. Griffin, & D. Kahneman (Eds.), *Heuristics and biases: The psychology of intuitive judgment* (pp. 49–81). Cambridge University Press.

Kieslich, P. J., & Henninger, F. (2017). Mousetrap: An integrated, open-source mouse-tracking package. *Behavior Research Methods, 49*(5), 1652–1667.

Kieslich, P. J., Henninger, F., Wulff, D. U., Haslbeck, J. M. B., & Schulte-Mecklenbeck, M. (2019). Mouse-tracking: A practical guide to implementation and analysis. In M. Schulte-Mecklenbeck, A. Kühberger, & J. G. Johnson (Eds.), *A handbook of process tracing methods* (pp. 111–130). Routledge.

Krynski, T. R., & Tenenbaum, J. B. (2007). The role of causality in judgment under uncertainty. *Journal of Experimental Psychology: General, 136*(3), 430–450. (Volume and first page confirmed.)

Latman, A. (1990). "Probative similarity" as proof of copying: Toward dispelling some myths in copyright infringement. *Columbia Law Review, 90*, 1187.

Lee, E., & Moshirnia, A. (2022). Do experts matter? A study of the effect of musicologist testimony in music cases. *University of Illinois Law Review, 2022*, 707. (As cited in the manuscript.)

Lu, H., Ichien, N., & Holyoak, K. J. (2022). Probabilistic analogical mapping with semantic relation networks. *Psychological Review, 129*(5), 1078–1103.

Mandel, G. N., Fast, A. A., & Olson, K. R. (2015). Intellectual property law's plagiarism fallacy. *BYU Law Review, 2015*, 915.

Markman, A. B., & Gentner, D. (1993). Structural alignment during similarity comparisons. *Cognitive Psychology, 25*(4), 431–467.

Miller, J., Patterson, T., & Ulrich, R. (1998). Jackknife-based method for measuring LRP onset latency differences. *Psychophysiology, 35*(1), 99–115.

Pearl, J. (1999). Probabilities of causation: Three counterfactual interpretations and their identification. *Synthese, 121*, 93–149. (The formulas for the probabilities of necessity and sufficiency in Section 4 are given from memory of this source and should be checked against it.)

Scherbaum, S., Dshemuchadse, M., Fischer, R., & Goschke, T. (2010). How decisions evolve: The temporal dynamics of action selection. *Cognition, 115*(3), 407–416.

Scherbaum, S., & Kieslich, P. J. (2018). Stuck at the starting line: How the starting procedure influences mouse-tracking data. *Behavior Research Methods, 50*(5), 2097–2110.

Spellman, B. A., & Holyoak, K. J. (1993). An inhibitory mechanism for goal-directed analogical mapping. *Proceedings of the Fifteenth Annual Conference of the Cognitive Science Society*. (Pages not confirmed.)

Spellman, B. A., & Holyoak, K. J. (1996). Pragmatics in analogical mapping. *Cognitive Psychology, 31*, 307–346. (Read in full.)

Sullivan, N., Hutcherson, C., Harris, A., & Rangel, A. (2015). Dietary self-control is related to the speed with which attributes of healthfulness and tastiness are processed. *Psychological Science, 26*(2), 122–134.

Tversky, A., & Kahneman, D. (1983). Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment. *Psychological Review, 90*(4), 293–315. (Not rechecked.)

Villejoubert, G., & Mandel, D. R. (2002). The inverse fallacy: An account of deviations from Bayes's theorem and the additivity principle. *Memory & Cognition, 30*(2), 171–178.

Yamamoto, N., Incera, S., & McLennan, C. T. (2016). A reverse Stroop task with mouse tracking. *Frontiers in Psychology, 7*, 670.

Yamauchi, T., & Markman, A. B. (1998). Category learning by inference and classification. *Journal of Memory and Language, 39*(1), 124–148.

# Appendix E. Files

| File | What it is |
|---|---|
| `Experiment/Study 2/` | The Study 2 experiment as rebuilt on November 18: `experiment.js`, `index.html`, `style.css`, the Study 1 item files, a README with the data columns and test links, and the deployment script for `genres-and-themes/experiment-2` |
| `Experiment/Archive/Study 2 two-genre choice (retired 2026-11-18)/` | The retired two-genre build, unchanged |
| `Analysis/notebooks/_build_18.py`, `18_studies2to5_design.ipynb` | Corpus inputs: the three quantities for every story feature and genre; the Study 1 items under the model; chance overlap; the shared-title check; candidate pairs; concrete features by cell |
| `Analysis/studies2to5_design/design_inputs_from_study1.Rmd` | Study 1 item means, listing rates and the variance components of the registered ratings model, using the registered exclusions and tables |
| `Analysis/studies2to5_design/studies2to5_power.Rmd` | Power simulations for the four studies, including the choices and mouse paths of Study 2's tracked condition |
| `Analysis/v4_rebuild/18_studies2to5_design/` | Outputs of the three files above, including the tables and figures in this memo |
| `Analysis/notebooks/17_category_utility.ipynb` | Incremental category validity and the identity linking the two increments (Part F) |
| `Analysis/notebooks/archive/12_study2_stimuli.ipynb`, `Analysis/Archive/study2_two_genre_power_retired_2026-11-18/` | The item draw and power simulations of the retired two-genre study |
| `Docs/Memorandum/Superseded/Study3_Design_Memo_2026-11-17.md` | The memorandum this one revises |
