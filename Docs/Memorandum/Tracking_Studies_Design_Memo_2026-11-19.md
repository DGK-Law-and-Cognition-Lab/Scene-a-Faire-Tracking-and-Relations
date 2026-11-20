---
title: "Design Memorandum for Studies 1 to 4 of the Tracking Paper: Where Did a Shared Story Feature Come From?"
subtitle: "Copying, genre and coincidence in judgments about two works"
author: "Prepared for David Kamper, Keith Holyoak and Mira Patel"
date: "November 19, 2026. Revises the memorandum of November 18. Draft for discussion; nothing here is preregistered."
---

*What changed on November 19.* The four studies are now numbered 1 to 4, because they belong to a paper of their own. The completed study that the law review article reports as its Study 1 is called the law review study throughout. Study 1 has three groups, one for each question, and every participant answers in two ways: one genre with ratings and the other with a mouse-tracked choice between two boxes. Its item pool grows from 288 to 432 stratified items, of which each participant rates 48 of one genre's 72 and judges all 72 of another genre with the mouse, the second box of the copying choice reads "Not copied," response time joins the bend of the path as a registered measure of conflict, and participants who answer the copying question are asked at the end how they read it. Study 2 gains a third kind of pair, a story feature together with what happens to it. Each study's section opens with a one-page statement of its design, and Section 15 lists what a reviewer is likely to press on. Study 1's experiment has been rebuilt to this design and run locally in all six of its versions.

# 1. Summary

The law review study asked people what a genre leads them to expect. The four studies planned here ask the question a copyright dispute actually poses: two works share a story feature, so where did the later work get it? The later work might have it because films of every kind do, because films of its genre do, or because its makers took it from the earlier work. Keith's note of November 13 put the dispute in exactly these terms, as a question about how the disputed work was generated, and Spellman and Holyoak (1996) supply a tested experimental form for it: participants act as writers in a plagiarism dispute between two soap operas and must say which character corresponds to which.

The memo sets out a small causal model in which the three possible sources of a shared feature are separate causes. In that model prevalence, incremental category validity and distinctiveness stop being rival measures of one thing. Each is the correct answer to a different question: whether the shared feature is evidence of copying (prevalence), how much the genre adds (the increment), and whether a feature already in the work is there because of the genre (distinctiveness). The memo then states three accounts of what people do when asked these questions, reports what the corpus already says about the design, and specifies four studies.

Study 1 presents one shared story feature at a time and varies the question between participants: whether the feature suggests copying, whether it is in the film because of the genre, or whether it is a stock feature. It uses the 288 items of the law review study, each of which has an expectedness norm from other participants, and 144 more drawn in the same way. Every participant answers the one question in two ways, rating the items of one genre from 1 to 7 and, for the items of another genre, choosing between two boxes with the mouse while the path of the pointer is recorded. The central test of the ratings has the form of the law review study's H2c with the predictions reversed: if people reason about copying as the model does, judged evidence of copying falls with prevalence and ignores distinctiveness; if one intuition about what is typical of a genre drives every judgment, it falls with distinctiveness instead. The path can show what a rating cannot: whether the statistic that does not decide the answer still pulls at it while it is being made. Study 2 moves to pairs of shared features and asks whether people see that a feature implied by another adds little, which is the corpus form of the necessity question set aside on November 1. A third kind of pair sets a feature beside what happens to it, a stagecoach and then a stagecoach robbed. Study 3 is the Spellman and Holyoak paradigm with corpus-calibrated materials: pairs of synopses that share common or rare, characteristic or uncharacteristic features, arranged alike or scattered, judged from the plaintiff's side, the defendant's side or neither. Study 4 shows participants the counts themselves and tests the law review article's practical claim that which count a fact-finder is shown decides the answer for features on which the two counts disagree.

The corpus work for this memo is in two notebooks (`Analysis/notebooks/18_tracking_studies_design.ipynb` and `19_event_pairs_design.ipynb`) and two R files (`Analysis/tracking_studies_design/`). Three of its results shape the design. The law review study's cells are almost perfectly matched for this purpose: high- and low-distinctiveness items have the same prevalence within each prevalence level, so the two accounts make nearly uncorrelated item-level predictions (Spearman −.03 between the model's copying weight and distinctiveness). Two unrelated Westerns share a median of two story features, but the closest other Western to a given Western shares a median of fourteen or fifteen, which is the baseline a plaintiff's list of similarities has to beat. And the law review study's variance components show that the number of items, not the number of participants, limits precision, which sets the sample sizes in Section 7.

Section 16 lists the decisions made so far and those still needed before any of this is preregistered.

# 2. Where the four studies come from

## 2.1 What the law review study established and what it could not ask

The law review study (131 usable participants, preregistered) had people list what they expect in a typical film of a genre and rate 48 items per genre for expectedness. Ratings followed distinctiveness about four times as strongly as prevalence (1.49 against 0.36 points on the seven-point scale; the difference, H2c, was −1.13 with a 95% interval from −1.50 to −0.76). Listing followed both (odds ratios of about 25 and 11 from the bottom to the top of a genre's ranking). Prevalence and distinctiveness kept apart predicted both tasks better than the composite (H3), and, in an exploratory analysis, better than incremental category validity.

The law review study's question was a category-to-feature question: given the genre, what do you expect? People answered it largely with feature-to-category information. That result is about expectation. It says nothing direct about the two judgments a court makes about a shared feature, which are whether the defendant took it and whether it is free for anyone to take.

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

The one earlier candidate for a later study was a rating of how necessary a feature is given a story premise, dropped from the plan on November 1. Its corpus measure was to be how often features occur together within a genre, which Notebook 03c already counts. That study is not replaced here. It becomes Study 2, because in the model of Section 4 necessity is the conditional form of prevalence, and its legal role, discounting similarities that follow from a shared premise, is a prediction about judged evidence of copying.

## 2.5 Why mouse tracking

Until November 18 the plan held a different mouse-tracked experiment, a choice between two genres for each of 555 items, built and verified but never preregistered or run. David retired it. Its one new quantity, the weight people give to the size of a genre, could not be separated from their liking for particular genres. Within a pair of genres prevalence and distinctiveness order the items identically, so it could not set a common feature against a characteristic one. And which of two genres a feature belongs to is none of the three questions of Table 2. Its files are kept in `Experiment/Archive/`.

The method is worth keeping. When a person chooses between two answers by moving a mouse from a common start, the path bends toward the answer that loses, and bends more the more strongly that answer competed (Dale, Kehoe and Spivey, 2007; Freeman and Ambady, 2010). Each of the three questions may be such a case. A rare but characteristic feature has two candidate answers to the copying question: its typicality says the genre explains it, and its prevalence says an independent author was unlikely to arrive at it. A common but uncharacteristic feature, a father in a Western, has two candidate answers to the other two questions: it is in many of the genre's films, and it belongs to no genre in particular. In Study 1 every participant therefore answers one genre with the mouse (Section 8.9), using the trial procedure and the Stroop practice built for the retired experiment.

The studies are intended for one paper for a cognitive science journal, separate from the law review. Its repository is `DGK-Law-and-Cognition-Lab/Scene-a-Faire-Tracking-and-Relations`.

# 3. The legal questions the studies map onto

A copyright plaintiff must show two things about copying, and the cases keep them apart. In *Arnstein v. Porter* the Second Circuit required proof "(a) that defendant copied from plaintiff's copyrighted work and (b) that the copying (assuming it to be proved) went so far as to constitute improper appropriation" (154 F.2d 464 (2d Cir. 1946)). The Ninth Circuit uses the same division: the infringement element "has two distinct components: 'copying' and 'unlawful appropriation'" (*Rentmeester v. Nike, Inc.*, 883 F.3d 1111 (9th Cir. 2018)). Similarity that bears on the first question is often called probative similarity, after Latman (1990), to keep it distinct from the substantial similarity of protected expression that the second question requires.

The first question is a factual inference from similarity to its cause, and courts have long said that the inference depends on what else could explain the similarity. Judge Posner's formulation in *Ty, Inc. v. GMA Accessories* is that copying may be inferred when two works are "so similar to each other and not to anything in the public domain that it is likely that the creator of the second work copied the first" (132 F.3d 1167 (7th Cir. 1997)). The phrase "and not to anything in the public domain" is a base-rate condition. A genre's conventions are the nearest thing a film has to a public-domain source, and prevalence within the genre measures how likely an independent author was to arrive at the feature.

The second question is where scènes à faire formally sits. Material that is stock for the kind of work is filtered out before the works are compared. Two refinements matter for the design. A selection and arrangement of stock material can itself be protected: "[t]he particular sequence in which an author strings a significant number of unprotectable elements can itself be a protectable element" (*Metcalf v. Bochco*, 294 F.3d 1069 (9th Cir. 2002)). And courts distrust lists of similarities, which "are inherently subjective and unreliable," particularly where "the list emphasizes random similarities scattered throughout the works" (*Litchfield v. Spielberg*, 736 F.2d 1352 (9th Cir. 1984)). The *Metcalf* rule is a claim that relational structure counts apart from the features it relates. The *Litchfield* caution is a claim that features without shared structure count for little, and that advocates compile them selectively. Both are claims about analogical mapping, and both are testable.

The original formulation of the doctrine was about necessity, "sequences of events which necessarily follow from a common theme" (*Reyher v. Children's Television Workshop*, 533 F.2d 87, 91 (2d Cir. 1976)). A feature that follows from another shared feature is, on that formulation, no additional similarity at all.

What is known empirically about how lay fact-finders handle these questions is limited. Balganesh, Manta and Wilkinson-Ryan (2014) found that mock jurors largely cannot set aside material they are told is unprotectable. Lee and Moshirnia (2022) found that expert musicologists change mock jurors' verdicts. Mandel, Fast and Olson (2015) found that lay people take intellectual property law to be about preventing plagiarism. None of these studies had a measure of how common the disputed material is, so none could ask whether lay judgments of copying or of stock material track the facts those judgments are about.

Table 1 maps the legal questions onto the studies.

| Legal question | What the fact-finder must judge | Study |
|------------------------------|----------------------------------------------------|------------------|
| Copying in fact (probative similarity) | How strongly a shared feature favors copying over independent creation | 1, 3, 4 |
| Is the feature stock for the genre? | Whether the feature belongs to the genre, under the Restatement's words or in plain causal terms | 1, 4 |
| Does it follow from something else the works share? | Whether a second shared feature adds anything to a first | 2 |
| Selection and arrangement | Whether shared structure counts beyond the features it arranges | 3 |
| Adversarial presentation | Whether the side one is on changes the similarities one finds and the features one filters | 3 |
| Expert evidence of commonness | Whether being shown a count changes the judgment, and which count | 4 |

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

The copying ratio $1/p$ assumes a copier reproduces the feature for certain; with lower fidelity the ratio shrinks toward 1 but still depends only on $p$. It treats the pair of works as given. A plaintiff who searches thousands of later works for the one most like her own will find more shared features than a random pair shares, and Section 6.2 puts numbers on that. It treats features as independent, which Study 2 relaxes. It takes the feature's level of description as fixed, when the same similarity can be stated broadly ("a lawman") or narrowly ("a newly appointed sheriff"), with different counts. And its counts come from plot summaries of films, so it describes the summaries. None of this affects the studies, which use the model as a benchmark for judgment and do not apply it to a real dispute.

# 5. Three accounts of what people do

The studies are built to separate three accounts of how lay reasoners answer the questions of Table 2.

*The query-sensitive account.* People answer each question with the statistic that answers it. Asked about copying, they consider how likely an independent work of the genre was to have the feature, so judged evidence of copying falls with prevalence and does not depend on distinctiveness. Asked whether a feature is there because of the genre, they use distinctiveness. This is what the causal model prescribes, and there is evidence that people reason well about probabilities when a problem has a causal structure they can use: base-rate neglect shrinks when the statistics map onto a causal model (Krynski and Tenenbaum, 2007), diagnostic judgments from an effect to a cause are sensitive to alternative causes (Fernbach, Darlow and Sloman, 2010), and judgments of coincidence behave like comparisons of a causal against a chance explanation (Griffiths and Tenenbaum, 2007). Keith's framing predicts this account. So does the category-learning literature in a general way: people who learn categories by inferring features attend to what is characteristic, and people who learn by classifying attend to what is diagnostic (Yamauchi and Markman, 1998; Chin-Parker and Ross, 2004), so the question asked can change the statistic used.

*The one-intuition account.* People have a single sense of how typical a feature is of a genre, the sense the law review study measured, and they use it for every question. A feature that feels typical of Westerns is judged stock, judged to be there because of the genre, and discounted as evidence of copying. Since that sense follows distinctiveness about four times as strongly as prevalence, judged evidence of copying would fall with distinctiveness, which the model says is irrelevant, and would barely respond to prevalence, which the model says is the only thing that matters. This is the representativeness account of probability judgment (Kahneman and Tversky, 1972), in the form given it by Bordalo, Coffman, Gennaioli and Shleifer (2016), for whom a trait is representative of a group when it is more frequent there than in a comparison group. It also fits the inverse fallacy, the substitution of $P(C \mid F)$ for $P(F \mid C)$ (Villejoubert and Mandel, 2002). Its legal consequence would be serious: rare but characteristic features such as the bounty hunter are the strongest evidence of copying the model recognizes, and this account says they are exactly what an intuitive fact-finder discounts.

*The overall-frequency account.* People judge copying by how common the feature is in stories generally, without conditioning on the genre. Ordinary things are coincidences and unusual things are evidence. Within a level of prevalence, a more distinctive feature is rarer in film at large, so on this account judged evidence of copying rises with distinctiveness.

The three accounts predict three different signs for the effect of distinctiveness on judged evidence of copying, with prevalence held fixed: zero, negative and positive. That one coefficient is the most diagnostic quantity in the design, and Study 1 is built around it.

| | Query-sensitive | One intuition | Overall frequency |
|---|---|---|---|
| Copying: effect of prevalence | Negative | Weakly negative | Negative |
| Copying: effect of distinctiveness | Zero | Negative | Positive |
| Copying: rare-but-characteristic against common-but-uncharacteristic (LH minus HL) | Positive | Negative | Positive |
| "Because of the genre" and "stock": effect of distinctiveness | Positive, larger than prevalence | Positive, larger than prevalence | Not specified |
| Does the question change the weights? | Yes | No: one profile, reversed for copying | Partly |

: Table 4. Predictions of the three accounts for Study 1.

The three accounts are about the answer a person gives. A fourth possibility is about how the answer forms. The sense of what is typical of a genre may come to mind first whatever the question, and be set aside when the question calls for something else. Kahneman and Frederick (2002) describe intuitive judgment in this way, as the substitution of an easily assessed attribute for the one asked about, which slower reasoning sometimes corrects. On this reading, which this memo calls corrected intuition, ratings of copying could follow prevalence, as the query-sensitive account says, and the feature's typicality would still pull at the response while it was being made. Ratings cannot show such a pull. The mouse-tracked genre of Study 1 is there to look for it, and to look for the matching pull of plain commonness under the other two questions.

# 6. What the corpus already says

## 6.1 The law review study's items are matched for this test

Table 5 gives the law review study's rated items by cell. Within each level of prevalence the high- and low-distinctiveness cells have almost the same prevalence (3.2% and 3.3% in the high cells; 0.75% and 0.77% in the low cells), so the model's copying ratio is the same across distinctiveness, about 31 to 1 in the high-prevalence cells and about 130 to 1 in the low ones. The prevalence manipulation is worth two bits, a factor of four in the odds. The distinctiveness manipulation moves cue validity from about 6% to about 33% and moves the share due to the genre from zero to about three quarters.

| Cell (prevalence, distinctiveness) | Items | Median prevalence | Median copying ratio | Median weight (bits) | Median cue validity | Median share due to the genre | Mean rating in the law review study |
|----------------------|-------|-----------|-----------|---------|----------|------------|----------|
| High, high | 72 | 3.2% | 31 to 1 | 5.0 | 31.7% | .77 | 5.65 |
| High, low | 72 | 3.3% | 31 to 1 | 4.9 | 6.2% | 0 | 4.38 |
| Low, high | 72 | 0.75% | 130 to 1 | 7.0 | 35.3% | .78 | 5.17 |
| Low, low | 72 | 0.77% | 129 to 1 | 7.0 | 5.9% | 0 | 3.95 |
| Foils (from other genres) | 48 | 0.10% | 824 to 1 | 9.7 | 1.5% | 0 | 2.79 |

: Table 5. The law review study's rated items under the model. Ratings are means of item means. Source: Notebook 18, Part B, and `design_inputs_from_law_review_study.Rmd`.

Across the 288 stratified items, with each variable centered within genre, the model's copying weight correlates −.03 with distinctiveness and −.23 with the law review study's rating, while the law review study's rating correlates .60 with distinctiveness (Spearman). The two main accounts therefore make nearly uncorrelated predictions item by item, which is the condition under which a single study can tell them apart. Figure 1 shows every item.

![Figure 1. Mean expectedness of each rated item in the law review study against its prevalence in the genre, by distinctiveness. The model's evidence of copying depends only on horizontal position; the law review study's ratings depend mostly on color. Bars are 95% intervals. Source: Notebook 18.](figures/law_review_study_items_expected_by_prevalence.png)

The cells differ in absolute prevalence across genres, because the genres differ in size and the cells are thirds within genre. The median high-prevalence item is in 5% to 11% of Westerns and about 1% of comedies. The analysis uses within-genre predictors, as the law review study did, and adds the copying weight in bits as a continuous predictor so that the absolute differences are used and not hidden.

## 6.2 What two unrelated films share

A list of similarities means something only against what two unrelated films of the genre share. For each of the law review study's six genres, Notebook 18 drew 20,000 random pairs of films and counted the story features both summaries contain. Table 6 gives the result. Two random Westerns share a median of 2 story features and 11 at the 95th percentile. The closest other Western to a given Western, found by searching all 1,362, shares a median of 14.5. A plaintiff who looks across a genre for the work most like hers can therefore expect about as many shared features by chance as the 95th to 99th percentile of random pairs, with summed model weights of about 50 to 80 bits depending on the genre.

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

Notebook 18 also confirms that the materials for Studies 2 and 3 exist. Among concrete story features in at least 20 of a genre's films, each genre has between 220 (Western) and 1,476 (comedy) ordered pairs in which the second feature is at least three times as likely given the first as in the genre at large and present in at least 30% of the films with the first. In Westerns, 77% of films with a Confederate have a war, against 14% of Westerns overall; 66% of films with a foreman have a ranch, against 18%. In horror, 82% of films with a transfusion have blood, against 16%. Each genre also has thousands of pairs whose members are statistically unrelated. And every genre has enough concrete characters, settings, objects and events in each of the four cells to fill two story shells: the smallest supply is the Western's common-but-uncharacteristic cell, with 11 kinds of character, 8 settings, 2 objects and 3 events.

# 7. The four studies at a glance

| | Study 1. One shared story feature | Study 2. Pairs and events | Study 3. Two works | Study 4. Showing the counts |
|----------------|---------------------|---------------------|---------------------|---------------------|
| Question | Which statistic answers which question, and does the other statistic pull at the answer as it forms? | Do people see that one shared feature can imply another, and does what happens to a feature add evidence? | Do arrangement and one's side change the judgment? | Does a count change the judgment, and which count? |
| Unit judged | One feature shared by two unseen works | A pair of shared features, or a feature and what happens to it | Two synopses | Features in a dispute, with expert counts |
| Varied between participants | The question (copying; because of the genre; stock) | The question (copying; necessity) | Role (plaintiff's side; defendant's side; juror) | Count format (none; prevalence; distinctiveness; both; increment) |
| Varied within participants | The way of answering (ratings for one genre, mouse-tracked choice for the other); prevalence × distinctiveness of the feature | Kind of pair (implied; unrelated; event) | Kind of shared features (2 × 2) × arrangement (aligned, scattered) | Prevalence × distinctiveness of the feature |
| Materials | 432 stratified items and 48 foils; a participant rates 48 of one genre's 72 and tracks all 72 of another | 144 pairs in 72 matched sets and 48 event pairs, drawn from corpus counts | 12 story shells, 96 synopsis pairs | 48 items of the law review study with their corpus counts |
| Main measures | Rating, 1 to 7; choice and pointer path; frequency estimates | Rating, 1 to 7; conditional frequency estimates | Probability of copying; similarity; character mapping; feature checklist | Stock rating; copying rating |
| Usable participants | 300 (100 per question), decided | 120 (60 per question), proposed | 210 (70 per role), proposed | 300 (60 per format), proposed |
| Session | About 30 minutes | About 30 minutes | About 45 minutes | About 20 minutes |
| New materials work | Done: 144 items drawn and reviewed | Moderate: the pairs are drawn and reviewed | Large: the story shells are written by hand | Small |
| State | Built and run locally in all six versions | Not built | Not built | Not built |

: Table 7. Overview of the studies.

The four studies together call for 930 usable participants. Sections 8 to 11 each open with the design of one study on a single page.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# 8. Study 1: one shared story feature, three questions, answered two ways

| | |
|------------------|--------------------------------------------------------------|
| The question it answers | When people judge a shared story feature, which fact do they use: how common it is in the genre, or how much it belongs to the genre? Does that depend on what they are asked? And does the fact they do not use still pull at the answer while it forms? |
| Who takes part | 300 usable participants from the UCLA subject pool, 100 for each question, on a desktop or laptop with a mouse or a trackpad. |
| What a participant does | Answers one question about the items of two genres. For one genre, rates 56 items from 1 to 7. For the other, chooses between two boxes by moving the pointer, one item at a time, for all 80 items of the genre. Then estimates how often 32 of the items occur in films. |
| What differs between participants | The question: does this shared feature suggest copying (COPY); is it in the film because of the genre (GENRE); is it a stock feature of the genre (STOCK). Also which way of answering comes first, and which two genres. |
| What differs within a participant | The way of answering: ratings for one genre, the mouse for the other. Within each genre, prevalence (high, low) by distinctiveness (high, low): the pool has 18 items in each of the four cells. In the rated genre a participant is shown 12 of the 18, and in the tracked genre all 18. Both have 8 foils from another genre. |
| How people are assigned | By the numeric sign-up code. The code modulo 72 picks one of 72 cells: 3 questions by 2 orders of answering by 12 genre schedules. The code does not depend on anything about the person. A study's codes are not consecutive, so the groups come out about equal and not exactly equal. Across the 72 cells, under every question, each genre is rated and tracked equally often, in first and in second position. |
| What is drawn at random for each person | Which 12 of the 18 items of each cell they rate, and the order of the items in both genres. The positions of the attention checks. Which box is on the left. Which of the items they judged they then estimate, and the order of the three frequency questions. |
| What is recorded | Each rating and its response time. Each choice, its response time and the position of the pointer up to 125 times a second. Three frequency estimates for each of 32 items. Familiarity with each genre, the pointing device, and the closing questions. In the COPY group, one closing question on how the participant read "copied." |
| The main tests | Primary, in ratings of copying: the sign of prevalence minus distinctiveness (S1-H2), and whether distinctiveness has no effect, within ±0.40 points (S1-H3). Secondary, across the three questions: whether the two facts are weighted differently. In the tracked choices, on two measures, the bend of the path and the response time: whether the answer that typicality favors, and the answer that prevalence favors, pulls at the response. |
| Length | About 30 minutes. |
| State | Built, and run locally in all six versions (three questions, two orders of answering). Not yet taken by a person. Not preregistered. |

: Study 1 on one page.

## 8.1 Purpose

Study 1 tests whether the statistic people use depends on the question they are asked. It holds the materials constant, the law review study's items, and changes the question between participants. Within each participant it also changes how the question is answered: with a rating for one genre, and for the other with a choice made with the mouse, which shows how the judgment forms.

## 8.2 Design

The question varies between participants, in three groups. In the COPY group participants judge whether a feature shared by an earlier screenplay and a later film suggests that the film was copied. In the GENRE group they judge whether a feature is in a film because of the film's genre. In the STOCK group they are given the Restatement's five adjectives and judge whether the feature is a stock feature of the genre. COPY corresponds to the first question of Table 2 and GENRE to the third. STOCK is the legal classification in the law's own words, included because the law review article's argument is that those words do not settle which property is meant.

The way of answering varies within participants. Each participant judges the items of two genres: one genre by rating each item from 1 to 7, and the other by choosing between two boxes with the mouse while the path of the pointer is recorded (Section 8.9). The boxes carry the two ends of the participant's question: "Copied" and "Not copied" for COPY, "Because of the genre" and "Could be in any film" for GENRE, "Stock" and "Not stock" for STOCK. Half of the participants answer their first genre with the mouse and their second with ratings, and half do the reverse.

Each question is therefore answered both ways, by the same people, on different genres. Three things follow. The rated and the tracked results can be compared within each question. One question can serve as the control for another: on the genre question typicality and the right answer agree, so the pull of typicality that the copying question is expected to show should be absent there, and a pull of plain commonness may appear in its place. And the first genre of every session, taken alone, is a comparison between separate groups of participants, free of any influence of one way of answering on the other.

The two genres come from the twelve-cell schedule of the law review study (six genre pairs in two orders). Crossed with the three questions and the two orders of answering, that gives 72 cells, in which every genre is rated and tracked equally often, in first and in second position, under every question. The item pool of a genre has 72 stratified items, 18 in each cell of high or low prevalence crossed with high or low distinctiveness, and 8 foils. In the rated genre each participant is shown 12 of the 18 items of every cell, drawn at random for that participant, and all 8 foils: 56 items, as in the law review study, with different participants rating different items. In the tracked genre each participant judges all 72 items and the 8 foils, because the measures taken from the pointer depend on the number of tracked trials each participant makes (Section 8.9). The order of the items is random in both.

An earlier draft carried a fourth question, whether the screenwriter should be able to stop the film's makers from using the feature. It is set aside. It would add a third to the sample and is not needed to tell the three accounts apart.

## 8.3 Materials

The pool is the 336 rated items of the law review study, with their display text unchanged, and 144 new stratified items. Every one of the law review study's items has an expectedness rating given by 36 to 49 other participants, so the one-intuition account can be tested with a predictor measured on different people. The new items have no such rating.

The pool was enlarged because the law review study's variance components show that the item set, not the sample, limits precision. The item standard deviation was 0.99 rating points, against 0.61 for participants and 1.30 for the residual, so the standard error of a cell contrast across 288 items has a floor of about 0.12 to 0.14 however many participants are run, and 432 items lower that floor by about a fifth. Showing every participant all 72 items of both genres would lengthen the session by about ten minutes, so the design shows all 72 only where the number of trials matters. In the rated genre each participant is shown 48 of the 72, which keeps most of the gain for the ratings, because there the items and not the number of answers per item are the limit (Section 8.8). In the tracked genre each participant judges all 72, because the precision of the measures taken from the pointer depends on the number of tracked trials each participant makes (Section 8.9). That adds 24 tracked trials, a few minutes, to the session.

The 144 new items, 6 in each cell of each genre, were drawn by Notebook 20. It first reproduces the law review study's draw exactly from that study's seeded queues, and then continues each queue from where it stopped, with the same pool, filters, exclusions and overlap rule. The new items were reviewed by the standards of the law review study's review: 36 strings were rejected as idiom residue, meta words, ambiguous nouns or fragments, each replaced by the next candidate in its queue, in three rounds. The cells stay matched. With all 18 items per cell and the genres pooled, median prevalence is 3.0% in the common-and-characteristic cell against 3.3% in the common-but-uncharacteristic cell, and 0.75% against 0.75% in the two rare cells, and on within-genre percentiles the new items do not differ from the old in any cell. David confirmed the 144 new items on November 19. The list of new items, the rejected strings and the tables are in `Analysis/v4_rebuild/20_extended_item_set/`.

## 8.4 Procedure

The session follows the law review study's structure with the listing task removed. After consent and the two-sentence reading task, participants read the instructions for their question, which say that they will answer in two ways and in which order, and answer the task check ("What is your task in this study?"), with one retry after re-reading.

For the rated genre participants rate their familiarity with the genre, read the question's wording, and rate their 56 items of the genre eight to a page, with two instructed-response attention checks among them. For the tracked genre they first learn the mouse procedure on a color-word Stroop task and make four practice choices (Section 8.9). They then rate their familiarity with the genre, read the same question in its two-box form, and judge all 80 items of the genre one at a time, with two instructed-response trials among them. A page between the two genres says that the genre changes, that the question stays the same, and that the way of answering changes.

A final block, the same for everyone, collects frequency estimates. Participants in the COPY group then answer one closing question on how they read the copying question (Section 8.11). The session ends with demographics, a question on legal training, three questions about the participant's setup (mouse or trackpad, which hand, color vision), the law review study's closing questions (seriousness, distraction, use of AI tools) and the debriefing, which says that the path of the pointer was recorded. The expected length is about 30 minutes, to be fixed after the investigators' own sessions.

In the frequency block each participant gives three estimates for 16 of the items they judged in each of their two genres (4 of the items they judged in each cell, drawn at random, and the same items for all three estimates, so every item of the pool is estimated by about two ninths of the participants who had its genre). The three estimates are the number, out of 100 films of the genre, that include the feature; the number, out of 100 films of all kinds, that include it; and the number, out of 100 films that include it, that are films of the genre. They are collected in three short blocks whose order is drawn at random for each participant, on sliders from 0 to 100 that show no handle until they are clicked. They give each item a subjective prevalence, a subjective base rate and a subjective cue validity, from which a subjective copying ratio and a subjective share due to the genre follow. The block comes last so that it cannot affect the main judgments; whether the question a participant answered affects the estimates is checked.

The exact wording of every instruction and question is in Appendix A. It is the wording of the experiment as built (`Experiment/Tracking Study 1 (Pavlovia experiment-2)/`).

## 8.5 Hypotheses and registered tests for the ratings

S1-H2 and S1-H3 are the primary tests of Study 1, and the preregistration will name them so. Every other hypothesis of Study 1 is secondary. These tests use each participant's rated genre; the tests of the tracked genre are in Section 8.9. All tests use the stratified items. Prevalence (P) and distinctiveness (D) are coded +0.5 for the top third and −0.5 for the bottom third of the genre, as in the law review study.

S1-H1. *Prevalence lowers judged evidence of copying.* In the COPY group the coefficient of P is below zero. All three accounts predict the sign; the query-sensitive account predicts the largest effect.

S1-H2. *The diagnostic contrast.* In the COPY group, the contrast P minus D, which equals the common-but-uncharacteristic cell minus the rare-but-characteristic cell (HL minus LH), separates the accounts. Below zero favors the query-sensitive and overall-frequency accounts: the rarer feature is the stronger evidence. Above zero favors the one-intuition account: the more characteristic feature is discounted. This is the law review study's H2c with the question changed.

S1-H3. *Distinctiveness and copying.* In the COPY group the coefficient of D is negative under the one-intuition account, positive under the overall-frequency account, and zero under the query-sensitive account. A zero cannot be shown by a non-significant test, so the query-sensitive prediction is tested as an equivalence: the 90% interval for the coefficient lies within ±0.40 rating points. That bound is about a quarter of distinctiveness's effect on expectedness in the law review study and slightly more than prevalence's effect there (0.36).

S1-H4. *The question changes the weights.* The effect of D differs between the COPY group and the GENRE and STOCK groups, and so does the effect of P (question-by-predictor interactions in a model of all three groups). Under the one-intuition account the COPY profile is the GENRE profile reversed, so the sum of the two D coefficients is near zero; under the query-sensitive account the COPY group has no D effect at all.

S1-H5. *GENRE and STOCK replicate the law review study.* In both groups D has a larger effect than P.

S1-H6. *The Restatement's words.* The effect of P is larger in the STOCK group than in the GENRE group. The Restatement's list includes "common" and "customary," which name prevalence. If the words matter, they should pull the classification toward prevalence. This test is two-sided.

S1-H7. *Beliefs about frequency.* Estimates of how many films of the genre include a feature rise with corpus prevalence, and also rise with corpus distinctiveness at a given prevalence. The second effect is the inverse fallacy in this domain and would mean that part of any distinctiveness effect on judged copying comes from mistaken beliefs about prevalence.

S1-H8. *Belief or inference.* In the COPY group, when the subjective copying weight ($-\log_2$ of the item's mean estimated prevalence) is entered, does corpus distinctiveness still predict the rating? If not, people reason as the model does from wrong beliefs. If so, they reason differently.

S1-H9. *One score or several.* For each group, models that know a single item-level predictor (the law review study's expectedness rating, for the 288 items that have one; the copying weight; the increment) are compared with each other and with the two-predictor model by AIC and by held-out log-likelihood in ten folds by participant, as in the law review study's H3.

## 8.6 Decision rule

The three accounts are distinguished by S1-H2 and S1-H3 together, read as in Table 8.

| P minus D (S1-H2) | D (S1-H3) | Reading |
|---|---|---|
| Below zero | Equivalent to zero | Query-sensitive: copying judged by prevalence alone |
| Below zero | Above zero | Overall frequency: copying judged by rarity in film generally |
| Above zero | Below zero | One intuition: characteristic features discounted |
| Below zero or not different from zero | Below zero | Mixed: prevalence is used and characteristic features are also discounted |
| Any other pattern | | No account supported as stated |

: Table 8. Reading the two tests of the COPY ratings.

## 8.7 Analysis

The registered model for each group is the law review study's ratings model: the rating regressed on P, D, their interaction, everyday word frequency (SUBTLEX-US log contextual diversity, centered) and genre (sum-to-zero contrasts), with random intercepts for participants and items and random slopes for P and D by participant, fit by restricted maximum likelihood with `lmer`. Each participant contributes the ratings of one genre. A model that fails the law review study's convergence check is reduced by that study's rule: the correlations among the participant effects are removed, then the slope with the smaller variance. Intervals and p-values use Satterthwaite degrees of freedom.

The combined model for S1-H4 to S1-H6 adds question and its interactions with P and D, and gives items a random slope for question, since the same items appear under every question. The continuous form of each model replaces P and D by centered within-genre percentiles and, separately, by the copying weight in bits and the share due to the genre, to use the absolute differences among genres that the coding by thirds removes.

Robustness checks follow the law review study: the model without word frequency; a cumulative-link mixed model; each genre left out in turn; and familiarity with the genre as a moderator. Two checks are specific to this design. Every test is repeated on the sessions in which the ratings came first, which are free of any influence of the tracked choice. And the order of answering, with its interactions with P and D, is added to the models to see whether having chosen with the mouse first changes the ratings. The foils are analyzed separately, as in the law review study; under the copying question they should be the strongest evidence of all on both the query-sensitive and overall-frequency accounts, since a feature from another genre is rare in this one.

An item-level analysis uses the law review study's norms directly, for the 288 items that have them. The mean COPY rating of each item is regressed on its copying weight and its expectedness rating from the law review study, with genre. Because the two predictors correlate only −.23, their coefficients are well separated.

## 8.8 Sample size

*The ratings.* The simulations (Appendix C) varied the number of participants per question (60, 80, 100 or 120) under each account, for the design as built: a pool of 432 items, of which each participant rates 48 of one genre's 72. With 100 participants per question every item is then rated by about 11 of them. If copying judgments follow prevalence alone, with an effect of 0.60 points, the contrast of S1-H2 is significantly below zero in 95% of simulations with 100 participants, and the equivalence test of S1-H3 at ±0.40 succeeds in 92%. At ±0.30 it succeeds in 61%, so a zero cannot be established that tightly. If the one-intuition account holds at seven tenths of the size of the law review study's effects, or the overall-frequency account at the size assumed, the contrast and the distinctiveness effect are detected in 99% to 100% of simulations. A prevalence effect as small as 0.25 points, which the one-intuition account implies, is detected in 68%.

The larger pool is what buys this, and showing each participant only part of it costs little. With the law review study's 288 items alone the two tests succeed in 90% and 79% of simulations. With all 72 items of the genre rated by everyone they would succeed in 97% and 95%. The reason is that the differences among items, and not the number of ratings each item receives, limit precision.

Having each participant answer both ways also costs nothing against separate groups. If 100 participants per question were split into 50 who rate two genres and 50 who answer two genres with the mouse, all items shown, the two tests would succeed in 95% and 81% of simulations. People differ a good deal in the weight they give distinctiveness, so 100 people rating one genre each say more than 50 people rating two. The check on first genres alone, about 50 participants with one genre each, was simulated with all items shown and succeeds in 95% and 81%; with 48 of 72 rated it will be somewhat lower.

*How many participants.* The table below gives the main tests by the number of participants per question, for the design as built: 48 of a genre's 72 items rated, and all 72 of another genre judged with the mouse. The two primary tests, which use the ratings, are at 86% or more with 60 participants per question, because the items and not the participants limit them. The tests on the pointer's path are the ones that need people: a pull of 0.10 is detected in 76% of simulations with 60 participants per question, 85% with 80, 94% with 100 and 97% with 120 (Section 8.9).

| Participants per question | Ratings: P minus D below zero (S1-H2) | Ratings: D within ±0.40 (S1-H3) | Choice: P minus D below zero | Choice: D within the bound | Path: pull of 0.10 detected | Path: pull of 0.20 told apart from 0.10 |
|---|---|---|---|---|---|---|
| 60 | 95% | 86% | 92% | 88% | 76% | 58% |
| 80 | 96% | 91% | 96% | 93% | 85% | 60% |
| 100 | 95% | 92% | 97% | 95% | 94% | 77% |
| 120 | 98% | 92% | 96% | 97% | 97% | 75% |

: Study 1 as built: share of simulations in which each main test succeeds, by the number of participants per question, when judgments follow prevalence alone.

Study 1 will have 100 usable participants per question, 300 in all, as David decided on November 19. Under these assumptions that puts five tests at 92% or more: the two primary tests, the same two tests in the tracked choice, and the detection of a pull of 0.10. With 80 per question, 240 in all, the same five would be at 85% or more. Telling two pulls apart stays uncertain at every size simulated. The law review study lost 6 of 137 sessions to its exclusion rules, so 300 usable sessions need about 315. The three groups will not be exactly equal, however. Assignment is by the sign-up code, and a study's codes are not consecutive: in the law review study the twelve cells received between 6 and 18 sessions each, as a random draw would give. With 315 sessions the smallest of the three groups would have 92 usable participants on average. With 345 it has 101 on average, and all three groups reach 90 in 97% of simulated recruitments and 100 in 66%. The recommendation is therefore to post 345 sessions, and to register a stopping rule that uses counts alone: recruitment stops when every question has 100 usable sessions or when 375 sessions have been run, whichever comes first. The figures rest on the assumed sizes of the effects. If the effect of prevalence on judged copying is smaller than 0.60 points, more items would be needed, and more participants would not make up for them. Figure 2 shows the two rating tests.

![Figure 2. Study 1, ratings of copying: share of simulations in which each test succeeds if copying judgments follow prevalence alone, by number of participants per question and item set. The black line, in the right-hand panels, is the design as built, in which each participant rates 48 of a genre's 72 items. The blue line is the design in which every item is rated; the gray line splits the same participants into separate groups for the two ways; the red line uses first genres only. The dashed line is 80%. Source: `tracking_studies_power.Rmd`.](figures/power_one_feature_ratings.png)

## 8.9 The mouse-tracked genre

*Why it is there.* The ratings say which statistic the answer follows. They cannot say whether the other statistic was in play. Under the query-sensitive account a person asked about copying consults how common the feature is in the genre, and nothing else comes into it. Under the corrected-intuition reading of Section 5 the feature's typicality comes to mind first and is overruled. Both predict the same ratings. They predict different paths. If typicality is overruled, then on the way to "Copied" for a rare but characteristic feature the hand should lean toward "Not copied," and it should lean less for a rare feature that is not characteristic. If the one-intuition account holds and typicality decides the choice, the same measure shows which of the two statistics the response was working against.

The other two questions put the same test the other way round. There typicality is expected to decide the answer, as it decided expectedness in the law review study, and the open matter is whether plain commonness is in play. A father is in about a fifth of Westerns and in films of every kind. If commonness pulls, then on the way to "Could be in any film" or "Not stock" for such a feature the hand should lean toward the other box, and it should lean less for a feature that is rare in the genre as well. The Restatement's words predict a stronger lean under the stock question than under the genre question, since "common" and "customary" are on its list.

*The task.* The task is the participant's own question with two answers. For COPY the instructions give the same dispute as for the ratings (a screenplay, a later film by different people, a claim of copying and a denial) and ask, for each thing the two works share, which is more likely: that the film's makers copied it, or that they did not copy it, meaning that they came up with it on their own. For GENRE they ask which fits better: that the thing is in the film because of the genre, or that it could be in any film. For STOCK they give the Restatement's sentence and ask whether the thing is a stock feature in that sense, or not stock. The two boxes sit in the top corners of the screen and a Start button at the bottom center. A line above the center states the frame ("Two Westerns both include:", "A Western includes:", "In Westerns:"). The participant clicks Start and begins to move upward, and the item appears once the pointer has risen 40 pixels, so that the decision is made while the hand is moving (the dynamic start of Scherbaum and Kieslich, 2018). The trial ends with a click on a box. The pointer's position is recorded throughout, at up to 125 samples a second. Each label stays on one side for the whole session, left or right by a random draw for each participant.

For COPY the choice asks which explanation is more likely, where the rating asks how strongly the feature suggests copying. Under the model the two differ by the participant's prior belief that a film in such a dispute was copied, which moves every item alike. The order of the items by prevalence is the same for both, and a participant's own threshold absorbs the rest. The same holds for the other two questions, whose ratings ask how much and whose choices ask which.

*Practice and control.* Before the tracked genre, participants complete a mouse-tracked color-word Stroop task: 8 practice trials with feedback and 32 scored trials, half of them incongruent. It teaches the procedure, and it is a positive control. Mouse-tracked Stroop tasks show a reliable effect of congruency on the movement toward the response (Bundt, Ruitenberg, Abrahamse and Notebaert, 2018; Yamamoto, Incera and McLennan, 2016), so a session's own Stroop trials show whether its paths register a conflict whose existence is not in doubt, and how large such a conflict is on the measure used here. Four practice choices about Romance films follow, with the participant's own two boxes.

*Trials.* The tracked genre has all 80 items of the genre, in random order, and two instructed-response trials, one naming each box, which take the place of the two attention checks. A response slower than four seconds from the item's onset brings a short reminder to answer a little faster. That limit is a first setting, to be fixed after the investigators' own sessions.

*Measures.* The choice is one measure. Conflict between the two candidate answers is measured in two ways, and both are registered.

The first is the curvature of the path. The paths are mirrored so that the chosen box is always on the same side, aligned to a common start, and resampled to 101 steps of equal time; the curvature is the area between the path and the straight line from start to response, positive when the path bends toward the box that was not chosen. The maximum deviation from the straight line is the robustness measure. Both are computed with the mousetrap package (Kieslich and Henninger, 2017; Kieslich, Henninger, Wulff, Haslbeck and Schulte-Mecklenbeck, 2019).

The second is the response time: the time from the appearance of the item to the click on a box, analyzed as its logarithm. A response made against a competing answer should be slower as well as more bent. Response time does not depend on the shape of the path, so it can show a conflict that was settled before the hand turned, which is the case the curvature would miss (Section 15). The time from the click on Start to the appearance of the item is recorded separately and is not part of it.

A further measure, the direction of movement at each step, gives the time at which a predictor begins to steer the path.

S1-H10. *The choice repeats the rating tests.* In a logistic mixed model of choosing the first-named box ("Copied," "Because of the genre," "Stock"), the rating tests are repeated for each question. For COPY: prevalence lowers the rate of "Copied"; the sign of P minus D separates the accounts; and the effect of D is negative, positive or equivalent to zero (S1-H1 to S1-H3). For GENRE and STOCK: D has the larger effect, and P has a larger effect under STOCK than under GENRE (S1-H5 and S1-H6). Across items, the share choosing the first-named box rises with the mean rating that other participants gave the item under the same question.

S1-H11. *The pull of typicality on the copying choice.* In the COPY group, curvature is greater when the response goes against the feature's distinctiveness, that is, when "Copied" is chosen for a characteristic feature or "Not copied" for an uncharacteristic one, than when it goes with it. This is the interaction of the response with D in a model of curvature. Under the query-sensitive account it is zero. Under corrected intuition it is positive although D does not affect the choice. Under the one-intuition account it is positive and D decides the choice as well.

S1-H12. *The pull of prevalence on the copying choice.* The same for prevalence: curvature is greater when "Copied" is chosen for a common feature or "Not copied" for a rare one. Every account on which prevalence affects the choice predicts this, and the comparison of the two pulls says which statistic the hand resists more.

S1-H13. *The pull of commonness on the genre and stock choices.* In the GENRE and STOCK groups, curvature is greater when the response goes against the feature's prevalence, that is, when "Could be in any film" or "Not stock" is chosen for a feature common in the genre, or the other box for a rare one. If typicality alone answers these questions, the pull is zero at a given distinctiveness. The Restatement's words predict a larger pull in the STOCK group than in the GENRE group. The pull of distinctiveness in these two groups is reported beside it. Since distinctiveness is expected to decide these choices, its pull shows how large a pull is when the statistic is known to be in use.

*Two measures, one claim.* Each of S1-H11, S1-H12 and S1-H13 is tested twice, on curvature and on response time. A pull predicts both a path that bends toward the box not chosen and a slower response. The two p-values of a hypothesis are corrected by Holm's method, and the pull counts as shown if either corrected test is significant. Both estimates are reported whatever the outcome. If only the path shows the pull, the conflict was still open while the hand moved. If only the response time shows it, the conflict was settled before the hand turned.

S1-H14. *Which comes first.* In a regression of the direction of movement on P and D at each time step, in the COPY group the effect of D begins earlier than the effect of P. This is corrected intuition in its sharpest form. The method is that of Scherbaum, Dshemuchadse, Fischer and Goschke (2010) and of Sullivan, Hutcherson, Harris and Rangel (2015), who found with it that the tastiness of a food begins to steer a choice about 195 ms before its healthfulness does. The onset of each effect is estimated from the pooled paths, and the difference between the two onsets is tested by jackknifing over participants (Miller, Patterson and Ulrich, 1998). The same onsets are reported for the other two groups.

S1-H15. *The same people.* A participant's weight on distinctiveness in their ratings is related to the pull of typicality in their paths. This is reported and is not a registered test: each person's two estimates rest on 48 items apiece and on different genres, so the correlation between them will be weakened by noise.

*Analysis.* The choice model is the rating model of Section 8.7 with a logit link. The curvature model is linear, with the response, P, D, the interactions of the response with P and with D, word frequency and genre as fixed effects, random intercepts for participants and items, and participant slopes for the two interactions, reduced by the law review study's rule if it fails the convergence check. The response-time model has the same form, with the logarithm of the response time as the outcome. It is fitted to each group, and to the three groups together with question as a factor for the comparisons among questions. The Stroop effect on curvature is reported first, from a model of the same form. A mean curvature can come from a mixture of straight paths and paths that change direction (Kieslich et al., 2019), so the distribution of curvature is reported for each cell and the tests are repeated on the share of paths that cross toward the box not chosen. As for the ratings, every test is repeated on the sessions in which the tracked genre came first.

*Laptops and trackpads.* Most participants will use a laptop, and many of those a trackpad. A trackpad moves the same pointer as a mouse and the page records it in the same way. Paths made on a trackpad are expected to be noisier, with pauses where the finger is lifted. The tests compare trials within a participant, so the device adds noise without favoring a hypothesis. Each participant reports the device used, the browser records the kind of pointer, and the device enters the curvature models as a covariate in a robustness check, with the tests also reported for mouse and for trackpad sessions apart.

*Trials and sessions left out.* The proposal, to be settled before preregistration, is to drop tracked trials on which the item appeared only after the two-second limit for starting to move, trials during which the window was resized, and trials slower than six seconds; and to leave out the tracked genre, but keep the ratings, of sessions answered with a touch screen and of sessions with fewer than three quarters of the scored Stroop trials correct. The common rules of Section 12 remove whole sessions.

*Power.* Appendix C has the simulations. In the tracked genre every participant judges all 72 items of the genre. The choice loses little against the rating, because the differences among items, and not the noise in a single response, limit precision. If choices of copying follow prevalence alone, then with 100 participants per question the contrast P minus D is below zero in 97% of simulations, and the effect of D is shown to be equivalent to zero, within the logit equivalent of ±0.40 rating points, in 95%. If the one-intuition or the overall-frequency account holds, the contrast and the effect of D are detected in 100% of simulations. These figures assume that a choice is the rating cut at a threshold, with the same noise. A noisier choice would lower them. If only a quarter of the choices are "Copied," the two figures are 92% and 93%.

For the path no quantity has an earlier estimate, so the simulation states its assumptions (Appendix C) and asks how small a pull could be found. With choices following prevalence alone and 100 participants each answering one genre with the mouse, a pull of typicality of 0.10 trial standard deviations is detected in 94% of simulations, and a pull of 0.15 or 0.20 in 100%. A pull of prevalence of 0.10 is detected in 96% to 98%. Telling the two pulls apart is harder. A pull of typicality twice the size of the pull of prevalence (0.20 against 0.10) is distinguished from it in 77% of simulations, and a pull half again as large (0.15 against 0.10) in 23%.

Showing every item of the tracked genre is what gives these figures. The precision of the measures taken from the pointer depends on how many tracked trials each participant makes and not on how many items there are. With 48 of the 72 items shown, as in the rated genre, the smallest pull would be detected in 85% of simulations, and with the law review study's 288 items alone in 83%. Fifty participants each answering two genres with the mouse would give 88%, and the check on first genres alone gives 79%. Only the copying question was simulated. The other two groups have the same structure, so the same figures apply to pulls of the same size there. Response time, the second registered measure, was not simulated separately; a pull of the same size in standard deviations of the logarithm of response time has the same power.

The sample of 100 usable participants per question is, under these assumptions, enough for S1-H11, S1-H12 and S1-H13. It tells two pulls apart only when one is at least twice the other, and then in about three simulations of four. S1-H14 was not simulated: its power depends on how far apart in time the two effects begin and on the shape of the noise in the paths, and nothing yet gives either. The investigators' own sessions and the Stroop trials will give the first real numbers. Figure 3 shows the test of S1-H11.

![Figure 3. Study 1, tracked choice of copying: share of simulations in which a pull toward the typical answer is detected in the curvature of the paths when choices follow prevalence alone, by its assumed size and the number of participants per question, with every item of the tracked genre shown. The right-hand panel is the design as built. The dashed line is 80%. Source: `tracking_studies_power.Rmd`.](figures/power_one_feature_tracking.png)

*What it costs.* A choice carries less information than a rating, which is why each question is answered both ways and neither way replaces the other. The tracked genre needs a mouse or trackpad and a window of at least 800 by 550 pixels, which the page checks. Because everyone answers both ways, every session has the same length and one listing and one credit value serve all participants.

## 8.10 What Study 1 cannot show

Each trial gives one shared feature and no works. The judgment is stripped of everything a real comparison involves, which is the point of the design and also its limit. A participant may reasonably think one shared feature proves nothing and use only the bottom of the scale; the instructions ask for relative judgments and the foils and rare items give the scale a top. If ratings of copying sit at the floor when the investigators take the study themselves, the question would be changed to a comparative one before preregistration. The undergraduates of the subject pool are not jurors, and Study 4 is the place for a broader sample.

Each participant answers in both ways, so one way may color the other. Rating a genre first may make the later choices more deliberate, and choosing quickly first may change how the scale is then used. The design meets this by counterbalancing the order, by giving the two ways different genres, and by repeating every test on first genres alone. It cannot rule out that the ratings and choices of a second genre differ a little from what separate groups would have given.

The tracked genre adds a view of the judgment forming. It does not say what the pull, if there is one, would do to a decision made under load or in a hurry, which is where an overruled intuition would matter in practice. That is a question for a later study.

## 8.11 The closing question on how "copied" was read

*Why it is there.* The copying question can be read as a question of fact (did the film's makers take this from the screenplay?) or as a question of what belongs to the screenwriter. On the second reading a feature that belongs to the genre is fair game and is rated low, which would look like the one-intuition account for a different reason (Section 15). The design cannot separate the two readings, so participants are asked.

*The question.* After the frequency block, participants in the COPY group see one page: "In this study you judged whether things that a screenplay and a later film both include suggest that the film was copied from the screenplay. People understand that question in different ways. Which of these is closest to what you had in mind when you answered?" The answers are "How likely it is that the film's makers took it from the screenplay, and did not come up with it on their own" (the factual reading); "Whether it is something that fairly belongs to the screenwriter" (the ownership reading); "Both of these about equally"; and "Something else." The first two are shown in an order drawn at random for each participant. The other two groups are not asked.

*What is done with it.* The shares of the four answers are reported. The tests of S1-H2 and S1-H3 are repeated on the participants who give the factual reading.

S1-H16. *The reading of the question.* If the discounting of characteristic features comes from the ownership reading, the effect of D on the copying ratings is more negative among participants who give that reading than among those who give the factual reading. This is the interaction of the reported reading with D in the model of the COPY ratings, tested two-sided.

*Its limits.* The answer is one report made after the judgments. Participants may not know how they read the question, or may choose the answer that sounds right. The question cannot turn one reading into the other. It shows how far the main result depends on the reading people report. Its power was not simulated, because it depends on how the group divides among the answers.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# 9. Study 2: pairs of shared features, and what happens to a feature

| | |
|------------------|--------------------------------------------------------------|
| The question it answers | Do people see that one shared story feature can follow from another, so that the pair is one piece of evidence and not two? And when a shared feature comes with what happens to it, does that add evidence of copying? |
| Who takes part | 120 usable participants from the UCLA subject pool, 60 for each question. |
| What a participant does | Judges pairs from two genres, 32 pairs per genre: 12 implied pairs (a foreman; a ranch), 12 unrelated pairs that end in the same second feature (a lady; a ranch), and 8 event pairs (a stagecoach; a stagecoach is robbed). |
| What differs between participants | The question: how strongly the pair suggests copying (COPY), or how necessary the second member is given the first (NECESSITY). Also which two genres. |
| What differs within a participant | The kind of pair: implied, unrelated, or event. |
| How people are assigned | By the numeric sign-up code, as in Study 1. The code modulo 24 picks one of 24 cells: 2 questions by 12 genre schedules. |
| What is drawn at random for each person | The order of the pairs within each genre, the order of the single features in the second block, and the positions of the attention checks. |
| What is recorded | COPY group: a rating from 1 to 7 for each pair and event, then for each feature alone. NECESSITY group: a rating from 1 to 7 for each pair, then two frequency estimates for each pair. |
| The main tests | Whether necessity ratings follow the conditional counts. Whether implied pairs are rated as weaker evidence of copying than unrelated pairs. Whether an event is rated as stronger evidence than its feature alone. |
| Length | About 30 minutes. |
| State | Not built. The pairs and events have to be drawn and reviewed. |

: Study 2 on one page.

## 9.1 Purpose

Two shared features are not always two pieces of evidence. If nearly every Western with a foreman has a ranch, a second work that has both tells little more than one that has a foreman. In the model the weight of a pair is the surprisal of the pair,

$$-\log P(F_1, F_2 \mid g) = -\log P(F_1 \mid g) - \log P(F_2 \mid F_1, g),$$

and the second term is small when the first feature implies the second. That conditional probability is what the corpus can say about necessity, and discounting features that follow from other shared features is what the *Reyher* formulation asks a court to do. Study 2 tests whether people's necessity judgments follow the conditional counts and whether their judgments of copying discount implied features.

People often fail to discount correlated evidence (Enke and Zimmermann, 2019). There is also a reason to expect the opposite of discounting: a pair that hangs together may feel like more of a shared story than two unrelated features, as coherent conjunctions feel more probable than their parts (Tversky and Kahneman, 1983).

The same question arises inside a single feature. The corpus counts events as well as things: a verb with its object, such as robbing a stagecoach or turning into a vampire (Notebook 13). An event is rarer than the thing it happens to, so in the model sharing the event is stronger evidence than sharing the thing. A stagecoach is in 96 of the 1,362 Westerns and a stagecoach robbery in 18, which makes 3.8 bits against 6.2. The difference, 2.4 bits, is the surprisal of the event given the thing, and it is small when the event is the usual thing to happen: about 18% of the Westerns with a stagecoach have it robbed. Events are also what the *Reyher* definition speaks of, sequences of events that follow from a common theme. Study 2 therefore adds pairs made of a feature and an event that happens to it, and asks whether people count the event as more than the feature.

## 9.2 Design

The question varies between participants: COPY (how strongly do these two shared features together suggest copying?) or NECESSITY (given that a film of the genre has the first feature, how necessary is the second?). Pair type varies within participants: in implied pairs the second feature is much more likely given the first than in the genre at large; in unrelated pairs the conditional and the plain rate are about equal. Each participant sees the pairs of two genres, assigned as in the law review study. Pairs come in matched sets, an implied pair and an unrelated pair that share their second feature, so that the two types are compared on the same feature.

A third kind of pair, the event pair, sets a feature beside an event that happens to it: a stagecoach, and a stagecoach is robbed. Within each genre half of the event pairs are those in which the event is the usual thing to happen to the feature (the upper half of the conditional rate among the genre's candidates) and half those in which it is not. In the COPY group the event is rated in the block of pairs and its feature in the block of single features, so each event can be compared with its own feature.

## 9.3 Materials

A new notebook draws 12 matched sets per genre, 24 pairs, from the counts of Notebook 03c, by a seeded rule with a reviewed exclusion list, as Notebook 10 did. Both members of a pair are concrete nouns or noun phrases (kinds of character, settings, objects, events) found in at least 20 of the genre's films. An implied pair requires $P(F_2 \mid F_1, g) \ge .30$, at least three times $P(F_2 \mid g)$, and at least 10 films with both. An unrelated pair requires the two rates to differ by less than a quarter. A matched set is an implied pair and an unrelated pair with the same second feature, whose first features are about equally common in the genre (within a factor of 1.5). The two pairs then have nearly the same single-feature weights and differ in dependence. Every genre has enough of them: between 165 (Western) and 866 (comedy) implied pairs have such a partner, covering 41 to 73 different second features. Pairs whose members share a word or a stem, or stand as part to whole (sheriff and new sheriff; starship and ship; townspeople and town), are excluded by rule and by review.

For the pair of a foreman and a ranch in Westerns, 41 Westerns have a foreman, 241 have a ranch and 27 have both. The pair's weight is $-\log_2(27/1362) = 5.7$ bits. If the two were independent it would be 7.6 bits. The dependence removes about two bits, a factor of nearly four in the odds. Its matched partner is a lady and a ranch: 18% of Westerns with a lady have a ranch, the same as Westerns overall.

The event pairs are drawn by Notebook 19 from the events of Notebook 13. An event is linked to a story feature when the feature is the event's object. A candidate pair has the feature in at least 20 of the genre's films and the event in at least 10, with at least four fifths of the event's films also having the feature (the two were extracted in separate passes). Before review there are 95 such pairs in the Western, 291 in fantasy, 301 in science fiction, 829 in horror, 897 in crime and 2,256 in comedy. Requiring the event in 20 films would leave 18 in the Western, which is why the floor for events is 10. Eight are drawn per genre, 48 in all, four from the upper half and four from the lower half of the conditional rate. Set phrases in which the object is not a thing in the story (commit suicide, fall in love) are excluded by rule and by review, and each event is given a display phrase written by hand from the verb and its object ("a stagecoach is robbed") and reviewed.

How well are events measured? Notebook 19 split the corpus in half at random, as Notebook 14 did for story features, and compared the two halves. For events in at least 20 of a genre's films, the ranking by distinctiveness agrees between the halves nearly as well as it does for nouns (.78 against .84, averaged over genres), and the ranking by prevalence agrees less well (.55 against .88). For events in at least 10 films the figures are .67 and .42, against .76 and .85 for nouns. So which genre an event belongs to is measured about as well as for a noun, and how common the event is within the genre is measured more coarsely. The study therefore uses an event's rate only as a coarse contrast, the upper against the lower half within a genre, and reports each event's counts with their intervals.

A design in which one feature is paired with two events, one usual for it and one unusual, would be cleaner, and the corpus cannot support it. With the usual event above 15% and the unusual one below 5%, no story feature in the Western qualifies, and only two do in fantasy and three in science fiction.

## 9.4 Procedure and measures

In the COPY group, participants use the dispute frame of Study 1 and rate each pair ("Both the screenplay and the film include: a foreman; a ranch") and each event ("Both the screenplay and the film include: a stagecoach is robbed") on the same seven-point scale. After the pairs and events of both genres, a second block presents the features one at a time for the same rating: the members of the pairs and the features of the events. Each pair's rating can then be compared with its members', and each event's with its feature's. The pairs and events come first so that the single ratings cannot affect them.

In the NECESSITY group, participants rate for each pair how necessary the second feature is in a film of the genre that has the first (1, it could easily be left out, to 7, the story could not do without it), and for each event pair how necessary it is that the event happens in a film of the genre that has the feature. They then estimate, for each pair, how many of 100 films of the genre with the first also have the second, and how many of 100 films of the genre have the second.

## 9.5 Hypotheses

S2-H1. *Necessity follows conditional prevalence.* Necessity ratings are higher for implied than for unrelated pairs, and across pairs they rise with $P(F_2 \mid F_1, g)$ with $P(F_2 \mid g)$ held fixed.

S2-H2. *Packages as evidence.* In the COPY group the model predicts lower ratings for implied than for unrelated pairs. Neglect of the dependence predicts no difference. Coherence predicts higher ratings for implied pairs. The test is two-sided and the direction is the finding.

S2-H3. *Adding up.* The difference between a pair's rating and the mean of its members' ratings is smaller for implied than for unrelated pairs (model), equal (neglect) or larger (coherence).

S2-H4. *Beliefs.* Estimated conditional frequencies track the corpus values, and the COPY ratings of pairs are better predicted by the pair's weight computed from estimated frequencies than from corpus frequencies.

S2-H5. *What happens adds evidence.* In the COPY group an event is rated as stronger evidence of copying than its feature alone, and the difference is larger for events that are unusual for the feature than for events that are usual for it. That is the model's prediction, since the event is always the rarer of the two and adds more bits when it is unusual. On the one-intuition account an event that is the usual thing to happen to a feature in the genre is itself typical of the genre, and adds nothing or is discounted. The test is two-sided.

S2-H6. *The necessity of events.* In the NECESSITY group, ratings of how necessary the event is, and estimates of how often it happens given the feature, are higher for the usual events than for the unusual ones.

## 9.6 Analysis and sample size

The models have the form of Study 1's, with pair type in place of P and D, pairs and matched sets as random factors, and the continuous predictors (the members' single weights and the log of the dependence ratio) in the continuous form.

A first simulation used unmatched pairs and showed the limit met in Study 1 more sharply. With 96 pairs, a difference of 0.5 points between the pair types was detected in 60% to 69% of simulations; with 144 pairs, in 74% to 82%. That is why the design uses matched sets. How much of the variation among pairs the two members of a set share is not known. If half is shared, 144 pairs in 72 sets and 60 participants per question detect a difference of 0.5 points in 94% of simulations and a difference of 0.4 in 76%. If a quarter is shared the figures are 86% and 70%. For scale, the dependence in an implied pair is worth about two bits, the size of the prevalence manipulation in Study 1, for which the Study 1 simulations assumed 0.6 points; a difference of 0.6 is detected in 93% to 98%. The proposal is 12 matched sets and 8 event pairs per genre, and 60 usable participants per question, 120 in all. An effect smaller than about 0.4 points would need more sets, which the corpus can supply.

The event pairs have not been simulated. Each event is compared with its own feature within a participant, across 48 events, so the comparison has fewer items than the matched sets and a difference on which nothing yet gives a size. A simulation with the variance components of the pairs is needed before preregistration, and it will say whether 8 events per genre are enough or whether 12 are needed, at the cost of a longer session.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# 10. Study 3: two works, their arrangement, and the side one is on

| | |
|------------------|--------------------------------------------------------------|
| The question it answers | When two whole stories are compared, do the kind of shared features and their arrangement change the judgment of copying? Does the side a person is on change what they see? |
| Who takes part | 210 usable participants from the UCLA subject pool, 70 in each role. |
| What a participant does | Reads eight cases. Each shows two short synopses side by side, a screenplay and a later film, that share four story features. For each case gives the probability that the film was copied, the similarity of the two works, which character corresponds to which, which of six listed features count toward copying, and who should win. |
| What differs between participants | The role: working with the screenwriter's lawyers, working with the film makers' lawyers, or serving as a juror. |
| What differs within a participant | The kind of shared features (common or rare in the genre, characteristic of it or not: four kinds) by their arrangement (aligned: the same parts in the same order; scattered: the same four features in an unrelated plot). Eight cases, one of each combination. |
| How people are assigned | By the numeric sign-up code: the role, and a row of a Latin square that gives each participant 8 of the 12 story shells, one in each combination, so that across participants every shell appears in every combination. |
| What is drawn at random for each person | The order of the eight cases. |
| What is recorded | A short written statement of what they will look for. For each case: probability of copying (0 to 100); similarity (1 to 7); the corresponding character for each of two characters; a mark for each of six features (counts, standard for the genre, not in both); who should win and confidence. On a side, a prediction of what a jury would decide. |
| The main tests | Whether aligned cases are judged more likely copied than scattered ones. Whether the kind of shared features matters as in Study 1. Whether arrangement counts for less when the features are the genre's stock. Whether the roles differ. |
| Length | About 45 minutes. |
| State | Not built. Twelve story shells have to be written by hand and reviewed. |

: Study 3 on one page.

## 10.1 Purpose

Study 3 returns to the Spellman and Holyoak paradigm: participants compare two narrative works in a copying dispute. It asks what single features cannot. Do the effects of Study 1 hold when the shared features sit inside stories? Does shared arrangement count beyond the shared features, as *Metcalf* holds, and does that depend on whether the features are stock? Does the side a person is on change the judgment, the correspondences found, and the features filtered out, as their pragmatic account of mapping predicts and as *Litchfield* suspects?

## 10.2 Design

Role varies between participants: working with the plaintiff's lawyers, working with the defendant's lawyers, or serving as a juror. Two factors vary within participants across eight cases. The kind of shared features has the four cells of the law review study: the four features the works share are all from one cell of the genre. Arrangement has two levels. In aligned cases the shared features play the same parts in both stories and the events run in the same order. In scattered cases the same four features appear in both works but in different parts of unrelated plots.

## 10.3 Materials

Each case is built on a story shell. A shell is a plot skeleton for one genre with four slots, two kinds of character, a setting or object, and an event, together with fixed material that the two works do not share. Filling the slots from one cell of the genre gives the screenplay's synopsis and the aligned film's synopsis, which tell the same sequence in different words and with different unshared detail. The scattered film's synopsis uses the same four features in a plot with a different skeleton. Each synopsis is five or six sentences, about 110 to 130 words. Unshared detail comes from the middle third of the genre on both measures, so that it is neutral.

There are 12 shells, two per genre, and each can be filled from any of the four cells and paired with either arrangement, which gives 96 versions. Each participant sees 8 different shells, one in each combination of cell and arrangement, by a Latin square, so that across participants every shell appears in every combination. Shells are the random item factor.

The slot fillers are drawn by a seeded rule from the law review study's pool (story features in at least 20 of the genre's films) and reviewed, and the shells are written by hand and reviewed for whether each filled version reads as a plausible story. Appendix B gives a complete example. A pair that shares four listed features is inside the range of chance for every genre (Table 6), so no case is decided by the count of similarities alone.

The model's benchmark for each version is the sum of its four features' weights. It is the same for both arrangements and differs by about eight bits between cells of high and low prevalence. The model as specified has no term for arrangement. It says only that shared structure is further evidence, by an amount the corpus cannot yet supply.

## 10.4 Procedure

After consent, the reading task and general instructions, participants read their role. As in Spellman and Holyoak, the role is given a purpose: participants on a side are asked to write, before the cases, two or three sentences on what they will look for on behalf of their side, and jurors on what they will want to know. Every participant is then told that for each case they should give their honest judgment, whatever their side.

For each case the two synopses appear side by side, the screenplay labeled as written first. The participant then gives, in order: the probability that the film's makers copied from the screenplay (0 to 100); the similarity of the two works (1 to 7); for each of the screenplay's two main characters, which character in the film corresponds to it, with "no one" as an option; a checklist of six features, the four shared ones and two that only one work has, each to be marked as in both works and counting toward copying, in both works but standard for the genre and so not counting, or not in both works; and which side should win, with confidence. Participants on a side also predict what a jury would decide. The session is planned for 45 minutes.

## 10.5 Hypotheses

S3-H1. *Arrangement.* Aligned cases receive higher probabilities of copying and higher similarity than scattered cases. Structure-mapping accounts of similarity predict a large effect (Gentner, 1983; Markman and Gentner, 1993), and *Metcalf* requires one.

S3-H2. *The kind of shared features.* The accounts make the predictions of Table 4 at the level of works: the probability of copying is higher when the shared features are rare in the genre (query-sensitive), lower when they are characteristic of it (one intuition), or higher when they are characteristic (overall frequency).

S3-H3. *Do stock parts spoil the arrangement?* In the model, shared features and shared arrangement are separate evidence and add on the log-odds scale. The alternative of legal interest is an interaction: arrangement counts for less when the arranged features are the genre's stock, which would mean that lay judgment does not give selection and arrangement the independent weight the doctrine gives it.

S3-H4. *Sides.* Probabilities of copying are highest on the plaintiff's side and lowest on the defendant's, despite the instruction to judge honestly, and each side's prediction of the jury leans its own way, the self-serving bias of Babcock and Loewenstein (1997).

S3-H5. *Filtering.* The share of shared features marked standard for the genre rises with distinctiveness more than with prevalence in every role, and is higher on the defendant's side.

S3-H6. *Mapping.* In scattered cases, participants on the plaintiff's side report a corresponding character more often than participants on the defendant's side, who more often answer "no one." In aligned cases the roles do not differ. This is the pragmatic effect of Spellman and Holyoak transferred to adversaries.

## 10.6 Analysis and sample size

Probabilities are analyzed as log-odds after the usual adjustment for 0 and 100, in a linear mixed model with arrangement, P, D, their interactions with arrangement, and role, random intercepts for participants and shells, a random intercept for each shell-by-condition version, and a participant slope for arrangement. The raw scale and an ordinal model are robustness checks. Checklist responses and mapping responses are analyzed with logistic mixed models. The slope of the log-odds on the model's summed weight estimates how conservative participants are relative to the model (Edwards, 1968).

The free-text statements of purpose are coded for which features they mention by the method of the law review study: three language models with a two-of-three rule, validated against two human coders on a sample, with the registered agreement threshold.

No earlier study gives variance components for this task, so the simulation rests on assumed values, stated in Appendix C, and its results hold only under them. With 12 shells and 50 participants per role, the assumed effects of arrangement (12 points on the 0-to-100 scale), prevalence (8), distinctiveness (8, where present) and role (6 on each side of neutral) are each detected in 96% of simulations or more. When distinctiveness has no effect, the test rejects in 2% to 10% of simulations, around the nominal 5%. The interaction of arrangement with the kind of shared features (S3-H3) is the weak point. An interaction of 6 points is detected in 52% to 65% of simulations with 12 shells and in 60% to 74% with 18. An interaction of 9 points is detected in 87% to 96% with 12 shells and in 92% to 98% with 18. The proposal is 12 shells and 70 usable participants per role, 210 in all, on the understanding that S3-H3 has good power only for an interaction about three quarters the size of the arrangement effect. Six more shells would raise that power and cost half again as much writing and review.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# 11. Study 4: showing the counts

| | |
|------------------|--------------------------------------------------------------|
| The question it answers | Does showing a count change whether a feature is called stock, and does it matter which count is shown? |
| Who takes part | 300 usable participants, 60 for each format. The subject pool, or a paid panel of jury-eligible adults (open). |
| What a participant does | Judges three disputes, each in a different genre and each with eight claimed similarities. Every similarity comes with an expert's report in the participant's format. Rates each similarity twice, in two passes: is it a stock feature (1 to 7), and how strongly does it suggest copying (1 to 7). Gives a probability of copying for each dispute. Answers a short numeracy scale. |
| What differs between participants | The format of the report: no count; how common the feature is in the genre ("26 of 1,362 Westerns include a bounty hunter"); how much it belongs to the genre ("26 of the 76 films with a bounty hunter are Westerns"); both; or its rate in the genre beside its rate in all films. Also which of the two passes comes first. |
| What differs within a participant | The kind of feature: the four cells of the law review study, two features from each cell in every dispute. |
| How people are assigned | By the numeric sign-up code: the format, the order of the two passes, and the three genres. |
| What is drawn at random for each person | The order of the similarities within each dispute. |
| What is recorded | The stock rating and the copying rating for each of 24 features, a probability of copying for each of three disputes, and the numeracy score. |
| The main test | The gap in stock ratings between rare-but-characteristic and common-but-uncharacteristic features, compared between the prevalence format and the distinctiveness format. |
| Length | About 20 minutes. |
| State | Not built. It uses 48 items of the law review study with their corpus counts. |

: Study 4 on one page.

## 11.1 Purpose

The law review article proposes that courts be given counts. Study 4 tests what counts do to judgment. Its sharpest prediction comes from the paper's central claim: for features on which prevalence and distinctiveness disagree, the count a fact-finder is shown should decide whether the feature is called stock. If so, an expert's choice of statistic is not a neutral act, which is the behavioral form of the paper's argument that the doctrine must say which property it means.

## 11.2 Design

The format of the expert's report varies between participants: no count; prevalence only; distinctiveness only; both; and the increment (the feature's rate in the genre beside its rate in all films). Within participants, the features come from the four cells of the law review study. Each participant judges three disputes, one in each of three genres, with eight claimed similarities each, two from each cell.

## 11.3 Materials

The 48 features are rated items of the law review study, two per cell per genre, chosen for concreteness and for narrow rating intervals in the law review study. The counts are the corpus's own and are described truthfully as counts from summaries of 45,958 films. They are given as natural frequencies with a rounded rate, which people handle better than bare probabilities (Gigerenzer and Hoffrage, 1995). For the bounty hunter the prevalence report reads: "A researcher counted 1,362 Westerns. 26 of them include a bounty hunter: about 2 in every 100." The distinctiveness report reads: "A researcher counted 76 films of all kinds that include a bounty hunter. 26 of them are Westerns: about 34 in every 100." For the hero's father the two reports are 288 of 1,362 Westerns, about 21 in every 100, and 288 of 11,207 films with a father, about 3 in every 100.

## 11.4 Procedure and measures

For each dispute participants read the frame (a screenplay, a later film, a claim of copying) and then, for each claimed similarity with its report, rate whether it is a stock feature of the genre (1 to 7, with the Restatement's words as in Study 1) and how strongly it suggests copying (1 to 7). The two ratings are collected in separate passes through the features, in an order counterbalanced between participants. After each dispute they give an overall probability of copying. A short numeracy scale and the closing questions follow.

## 11.5 Hypotheses

S4-H1. *The count shown decides the classification.* The gap in stock ratings between rare-but-characteristic and common-but-uncharacteristic features (LH minus HL) is more positive in the distinctiveness format than in the prevalence format. The law review study puts the gap at about +0.8 with no count. A reversal of its sign in the prevalence format is the strong form of the prediction.

S4-H2. *Counts and copying.* The correlation between copying ratings and the model's weight is higher in the prevalence format than with no count. In the distinctiveness format it is no higher, and may be lower, because a high share of a feature's films being Westerns reads as a reason to discount a feature that few Westerns have.

S4-H3. *Both counts.* With both shown, stock ratings weight distinctiveness more than prevalence, as unaided ratings do. This test is two-sided.

S4-H4. *The increment.* With the increment format, stock ratings follow the increment, which at the top of a genre means following prevalence among characteristic features.

S4-H5. *Numeracy.* The effects of format are larger for participants with higher numeracy.

## 11.6 Analysis, sample and sample size

Ratings are analyzed with the mixed models of Study 1, with format and its interactions with P and D, and a random slope for format by item. Because this study is about fact-finders, a sample of jury-eligible adults from an online panel would suit it better than the subject pool; Section 16 leaves the choice open.

The test of S4-H1 compares two formats. With 60 participants per format, a shift of 0.6 points between the formats in the gap is detected in 84% of simulations, a shift of 0.8 in 94%, and a shift of 1.0 in 100%. With 40 per format the figures are 84%, 94% and 98%. A reversal of the gap the law review study found would be a shift of well over a point. The proposal is 60 usable participants per format, 300 in all, which leaves the other three formats enough participants for their own comparisons. Forty per format, 200 in all, would lose little for S4-H1.

# 12. Methods common to the four studies

*Participants.* Studies 1 to 3 are planned for the UCLA psychology subject pool, with course credit, under the conditions of the law review study. Anyone who took part in the law review study, or in an earlier study of this series, is excluded through the pool's prerequisite settings, because all of them expose participants to the items.

*Platform.* Each study is a plain-JavaScript page hosted on Pavlovia, built from the law review study's code: the consent page, the device check, the reading task, the hidden-instruction check, the task check, the instructed-response attention checks, the closing questions and the credit redirect are reused unchanged. Each study gets its own Pavlovia project and its own deployment script fixed to that project. Study 1's page is built in `Experiment/Tracking Study 1 (Pavlovia experiment-2)/` for the project `genres-and-themes/experiment-2`, and has been run locally in all six versions. The law review study's project, `genres-and-themes/experiment-1`, is closed and is never deployed to. David does the pushes.

*Assignment.* Participants are assigned from the numeric survey code, as in the law review study: the code modulo the number of cells picks the cell. Study 1 has 72 cells, three questions by two orders of answering by the twelve genre schedules. The cell modulo three is the question, and the order of answering and the genre schedule follow from the rest of the code. The assignment does not depend on anything about the participant. It would be an exact rotation if a study's codes were consecutive. They are not, so the cells fill as they would under a random draw (the twelve cells of the law review study received between 6 and 18 sessions each), and the groups are about equal and not exactly equal. Within a session, the order of the items, the positions of the attention checks, the side of each box and the frequency items are drawn at random.

*Exclusions.* The law review study's rules apply in their registered order, without the rule about the quality of listed responses, which has no counterpart: failing the hidden-instruction check; a median reading time under 150 ms per word on either reading sentence; failing the task check twice; passing fewer than all four attention checks; an incomplete session; reported use of an AI tool; a repeated identifier; and a self-report of not taking part seriously. The tracked genre of Study 1 adds the rules proposed in Section 8.9.

*Stopping.* Each study has a fixed target of usable participants per group and stops when it is met or the term ends. There are no interim analyses.

*Preregistration and materials.* Each study is preregistered as one document in the format of the law review study's, with the materials in a release of a GitHub repository cited by commit.

*Ethics.* The tasks are judgments about fictional disputes and carry the same minimal risk as the law review study's. Whether the existing exemption (IRB-25-2264) describes these tasks, and whether it covers an online panel if Study 4 uses one, should be confirmed before preregistration.

# 13. Modeling

The studies are designed so that every judgment has a model prediction computed before the data exist.

*The causal model with corpus statistics.* For each item, pair or set, the copying weight, the increment, the genre's strength and the share due to the genre come from the corpus counts. The model has two free parameters when fit to ratings, the fidelity of copying $\kappa$ and the prior probability of copying, plus a linear map from log-odds to the response scale.

*The causal model with subjective statistics.* The same model with each item's estimated frequencies from the frequency block in place of corpus counts. Comparing it with the corpus version separates errors of belief from errors of inference (S1-H8).

*The one-intuition model.* Every judgment is a linear function of a single item-level typicality value, taken from the law review study's ratings or from the GENRE group of Study 1, with a sign that depends on the question.

*Comparison.* Models are compared by held-out log-likelihood in ten folds by participant and by AIC, the criteria registered for the law review study's H3.

*Mapping.* For Study 3, the synopses can be given to a model of analogical mapping to predict the correspondences participants report. Two candidates fit the lineage of the paradigm: ACME (Holyoak and Thagard, 1989), which Spellman and Holyoak used and in which a goal acts by inhibiting attention to irrelevant relations, and Probabilistic Analogical Mapping (Lu, Ichien and Holyoak, 2022), which builds semantic relation networks from distributed representations of words and relations and so would not need hand-coded propositions. Either would give a principled measure of how much relational structure two synopses share, which is the quantity the model of Section 4 lacks. Whether to include this is a decision for Keith (Section 16).

# 14. What each result would mean

| Result | For the theory | For the law |
|--------------------------|-------------------------------------|-------------------------------------|
| Copying judged by prevalence alone (Study 1) | People reason about the source of a feature as a causal model prescribes; the law review study's reliance on distinctiveness was specific to its question | Lay fact-finders can use the right fact for copying in fact; the difficulty is that they are rarely given it |
| Copying judged by typicality (Study 1) | One representativeness-based sense of the genre answers every question | Intuitive fact-finding discounts rare-but-characteristic features, which are the strongest evidence of copying, and credits common ones; counts are needed most where intuition is most confident |
| The question does not change the weights (Study 1) | The distinction between category validity and cue validity is not one people draw unaided | The two steps of the infringement test collapse into one impression in lay judgment |
| Paths bend toward "Not copied" for characteristic features although choices follow prevalence (Study 1, tracked choice of copying) | The sense of what is typical is active and is overruled: intuition corrected by the question | Fact-finders can reach the right answer on copying, but against a live intuition, which haste or load might let through |
| Choices follow prevalence and paths show no such bend (Study 1, tracked choice of copying) | The question selects the statistic from the start | The obstacle to accurate fact-finding on copying is the missing count, with no competing intuition to overcome |
| Paths bend toward "Stock" or "Because of the genre" for features that are merely common in the genre (Study 1, tracked choice under the other two questions) | Commonness is registered even where typicality decides the answer | The Restatement's "common" and "customary" name a property that fact-finders notice and set aside; an instruction or a count could bring it forward |
| Necessity ratings follow conditional counts (Study 2) | The corpus has a usable measure of necessity | The *Reyher* formulation can be given the same kind of evidence as the Restatement's |
| Implied pairs counted as much as unrelated pairs, or more (Study 2) | Correlation neglect, or coherence, in judgments of similarity | Lists of similarities overstate the evidence when their items come as a package |
| Arrangement counts regardless of the parts (Study 3) | Relational structure drives similarity, as structure-mapping holds | Lay judgment matches *Metcalf* |
| Arrangement counts less for stock parts (Study 3) | Feature typicality and structure interact | Lay judgment gives selection and arrangement less protection than doctrine does |
| Sides differ in mapping and filtering (Study 3) | Pragmatic control of mapping extends to adversarial goals | Party-compiled lists of similarities and party experts' accounts of what is stock are shaped by purpose, as *Litchfield* suspects |
| The count shown decides the classification (Study 4) | Explicit statistics override the intuitive weighting | An expert's choice between prevalence and distinctiveness decides outcomes for divergent features; courts must say which property they mean |

: Table 9. Possible results and their meaning.

# 15. Threats, and corpus work alongside the studies

*How the copying question is read.* "Copied" can be heard as a question of fact (did the film's makers take this from the screenplay?) or as a moral one (was something taken that should not have been?). On the second reading a feature that belongs to the genre is fair game and gets a low rating, which would look like the one-intuition account for a different reason. The instructions describe a dispute of fact, and the stock question, put to other participants, shows what a normative reading looks like on the same items. The design of Study 1 cannot separate the two readings. A closing question therefore asks participants in the COPY group which they had in mind, and the main tests are repeated on those who report the factual reading (Section 8.11).

*The size of the prevalence difference.* The items contrast the top and the bottom third of each genre's features. That is a ratio of about four to one and a small difference in absolute terms: the median common item is in about 3% of the genre's films and the median rare item in under 1%. If participants do not perceive the difference, the absence of a prevalence effect on judged copying would say little about how they reason. The frequency estimates measure what they perceive, and S1-H8 separates a failure of belief from a failure of inference.

*A prediction of no effect.* On the query-sensitive account distinctiveness has no effect on judged copying. That is tested as an equivalence within ±0.40 points, and a reader has to accept the bound. The larger item pool is what gives the test its power (Section 8.8).

*A slow judgment and a fast hand.* Mouse tracking shows a competing answer only if the decision is still being made while the hand moves. Judging whether a shared feature suggests copying may take long enough that participants stop, decide, and then move in a straight line, which would leave no bend even where there was a conflict. Showing the item only once the hand is moving works against this, and the Stroop trials show that the setup registers a conflict, though a fast perceptual one. Response time is recorded for every choice and does not depend on the shape of the path, which is why it is the second registered measure of conflict (Section 8.9). The tracked choices are also made under a prompt to answer quickly and the ratings are not, so a difference between the two ways of answering may reflect time pressure and not the format of the response.

*What the choice asks.* The rating asks how strongly a feature suggests copying, and the choice asks which is more likely. If nearly every feature is answered "Not copied," the choices carry little information and the paths toward "Copied" are few. The investigators' own sessions will show the rate. If it is extreme, the choice can be reworded to ask whether the feature points toward copying.

*Two groups in which the accounts agree.* Under the genre and stock questions every account predicts that distinctiveness outweighs prevalence. Those two groups are not there to separate the accounts. They are there so that a flat result under the copying question cannot be put down to noise: the same items must give a different profile when the question changes.

*Incremental category validity.* Keith's proposal, the feature's rate in the genre minus its rate elsewhere, is not a factor of the design. Within a genre it cannot be: the increment is fixed once prevalence and distinctiveness are, so it is a third summary of the same two numbers and enters only as one of the single-predictor models of S1-H9.

*Many hypotheses.* Study 1 states sixteen. S1-H2 and S1-H3 are the primary tests and the rest are secondary (Section 8.5).

*Demand.* Participants in the COPY group might guess that rare things are meant to count. The instructions do not say so, the items are not labeled, and the frequency block comes last. The one-intuition account predicts a result that no demand explanation produces.

*Word frequency and familiarity.* A rare word may seem a rare feature. Everyday word frequency is a covariate in every model, as in the law review study, and familiarity with each genre is measured.

*The scale.* Ratings of evidence are not probabilities. The analysis treats them as monotone in the log-odds, tests ordinal versions, and in Studies 3 and 4 collects probabilities directly.

*Item sets.* Abstract items such as "fate" or "truth" are odd as claimed similarities. They are kept in Study 1 for comparability with the law review study and analyzed with and without them; Studies 2 to 4 use concrete features only.

*The corpus as ground truth.* Prevalence in plot summaries is not prevalence in films, and neither is what an author would have written. The studies compare judgments with the counts and with participants' own estimates; they do not assume the counts are right about the world.

*Mouse tracking outside the laboratory.* Participants use their own laptops, mostly with trackpads, on their own screens, and paths differ with the device. The design answers this in four ways: every trial begins from the same place and the item appears only once the hand is moving; the window must be large enough before a block starts; the Stroop trials give each session a conflict effect of known direction against which its paths can be judged; and the device is recorded and used as a covariate, with the tests also reported for mouse and trackpad sessions apart. The tests compare trials within a participant, so differences between devices add noise without favoring a hypothesis.

*One way of answering coloring the other.* In Study 1 each participant answers in both ways. The order is counterbalanced, the two ways are given different genres, every test is repeated on first genres alone, and the order of answering enters the models as a check (Sections 8.7 and 8.10).

*Events.* The counts of events are less stable than the counts of nouns, above all for how common an event is within a genre (Section 9.3), and the parser's verbs and objects have not been checked by hand. Study 2 uses events only as a coarse contrast and reviews every event it shows.

*Generality.* Six genres, film only, undergraduates in three of the four studies.

Some corpus work would strengthen the next paper and needs no participants. A curated set of remakes and adaptations, from a public source that records which film is a remake of which, would replace the shared-title stand-in of Section 6.3 and test properly whether weighting shared features by surprisal detects derivation better than counting them or weighting them by distinctiveness. The baseline of Section 6.2 could also be extended to events (Notebook 13) and to pairs, so that shared structure can be given a count.

# 16. Sequence and decisions

## 16.1 A proposed order

Study 1 can be preregistered first: its items exist, its experiment is built, and the analysis of its ratings is the law review study's. What it still needs is listed below. Study 4 reuses Study 1's items and adds only the display of counts, so it can be built alongside Study 1 and run on a different sample. Study 2 needs a stimulus notebook and a review of the drawn pairs and events. Study 3 needs the most work: the shells have to be written and reviewed, and the page for comparing two synopses is new. For the cognitive science paper, Studies 1 and 3 would make a complete argument, with Studies 2 and 4 either in the same paper or held for the next.

## 16.2 Decisions made

On November 18 David retired the two-genre choice study and moved mouse tracking to the judgments of what is now Study 1.

On November 19 David decided eleven things. Study 1 has three groups, one for each question, and every participant answers one genre with ratings and the other with the mouse; a design with only the copying question tracked is dropped. Laptops and trackpads are acceptable for the tracked genre. The four studies are numbered 1 to 4, as the studies of their own paper. Events, a feature with what happens to it, join Study 2. The second box of the copying choice reads "Not copied" and not "Coincidence," because a feature the genre explains is not a coincidence and the label would have sat badly on exactly the common items. Study 1 uses the pool of 432 items, and David confirmed the 144 new items. Response time is a second registered measure of conflict in the tracked choices, beside the bend of the path. Participants who answer the copying question are asked at the end how they read it. In the tracked genre every participant judges all 72 items, and in the rated genre 48 of the 72. S1-H2 and S1-H3 are the primary tests. And Study 1 will have 100 usable participants for each question, 300 in all.

## 16.3 Decisions still needed

1. One more push to Pavlovia by David. The build with the 432 items, the "Not copied" box, the closing question and every item shown in the tracked genre is live, checked file by file on the evening of November 19. The return link was added after that check and is not yet live.
2. Which of Studies 2 to 4 to run, and in what order. The recommendation is Study 1 first, then Study 3, with Study 4 alongside Study 1 if a panel sample can be paid for.
3. For Study 1, the number of sessions to post and the stopping rule. The recommendation is 345 sessions, stopping when every question has 100 usable sessions or at 375 (Section 8.8).
4. For Study 1, the wording of the COPY question and whether the equivalence bound of ±0.40 is the right smallest effect of interest.
5. For Study 1, the labels "Because of the genre" and "Could be in any film," and "Stock" and "Not stock," which are as built, and the rules of Section 8.9 for leaving out tracked trials and tracked genres.
6. Whether necessity (Study 2) should stay in this series, as proposed, or be run separately as first planned, and whether Study 2 has 8 event pairs per genre or 12.
7. For Study 3, who writes the story shells, how many (12 or 18), and whether the roles should be lawyers' assistants, as proposed, or the writers themselves, as in Spellman and Holyoak.
8. For Study 4, the subject pool or a paid online panel of jury-eligible adults, and the budget for the latter.
9. Whether Keith's lab would model the Study 3 mappings with ACME or with Probabilistic Analogical Mapping.
10. Whether to write to Barbara Spellman for the 1996 story materials and her comments on the design.
11. Whether each study gets its own preregistration or Studies 1 and 2 share one.
12. Confirmation that the existing exemption covers these tasks.
13. Whether the corpus work of Section 15 should start now.
14. Before Study 1 can launch: the SONA listing, whose return link David said on November 19 is the law review study's and which the build now carries; a deploy of that build; a session in each of the six versions taken by the investigators on a laptop, after which the time limit and the estimated length are fixed; and the preregistration.

# Appendix A. Instructions and questions

Bracketed words change with the genre: [Westerns] stands for Westerns, Horror films, Crime films, Science Fiction films, Comedies or Fantasy films, and [a Western] for a Western, a Horror film, a Crime film, a Science Fiction film, a Comedy or a Fantasy film. All ratings use a row of seven buttons with the end labels shown. The wording of Study 1 (A.1 to A.6) is that of the experiment as built.

## A.1 Study 1, the instructions every participant reads

"In this study you will be asked about two film genres. For each genre there are two short parts. Part 1: Familiarity. You will rate how familiar you are with the genre. Part 2: Judgments. [The sentence for the participant's question, below.] The question is the same for both genres, but you will answer it in two different ways. For your first genre you will choose between two answers by moving the pointer to one of two boxes, with your mouse or trackpad. A short practice with colors shows you how this works. For your second genre you will give each item a rating from 1 to 7. [For half of the participants the two sentences are in the other order.] There are no right or wrong answers. We are interested in your own judgment. A few items will instead ask you to select a specific number or to choose a specific box. Please read every item carefully."

The sentence for COPY: "You will read about a disagreement between a screenwriter and the makers of a later film of that genre. You will then see things that the screenplay and the film both include, and judge whether each one suggests that the film was copied from the screenplay." For GENRE: "You will see things that a film of that genre includes, and judge whether each one is in the film because of the kind of film it is." For STOCK: "You will read a short description of a rule of copyright law. You will then see things that a film of that genre might include, and judge whether each one is a stock feature of the genre."

Between the genres: "You have finished [Western]. Next is a different genre: [Horror]. The question stays the same. For [Horror] you will answer in a different way. Instead of choosing between two boxes, you will give each item a rating from 1 to 7." (Or, in the other order: "Instead of giving ratings, you will choose between two boxes with your mouse or trackpad. A short practice with colors comes first and shows you how this works.")

## A.2 Study 1, COPY

Rated genre, instructions: "In this part you will think about two [Westerns]. One is a screenplay. The other is a film that was made a few years later by different people. The screenwriter says that the people who made the film copied from the screenplay. The people who made the film say they never saw the screenplay and came up with the film on their own. You will not read the screenplay or see the film. We will show you, a few at a time, things that both of them include. For each one, tell us how strongly it suggests that the film was copied from the screenplay. Some things that two [Westerns] have in common say very little about whether one was copied from the other. Others say a lot. Please use the whole scale."

Each rated item: "Both the screenplay and the film include: **[item]**. How strongly does this suggest that the film was copied from the screenplay?" 1 = Not at all; 7 = Very strongly.

Tracked genre, instructions: the same five sentences that set out the dispute, then: "You will not read the screenplay or see the film. We will show you, one at a time, things that both of them include. For each one, choose what is more likely: that the film's makers copied it from the screenplay, or that they did not copy it, meaning that they came up with it on their own. Some things that two [Westerns] have in common say very little about whether one was copied from the other. Others say a lot. There are no right or wrong answers."

Each tracked trial: the line "Two [Westerns] both include:" and, once the pointer is moving, **[item]**. The boxes read "Copied" and "Not copied."

Closing question, after the frequency block, COPY group only: "In this study you judged whether things that a screenplay and a later film both include suggest that the film was copied from the screenplay. People understand that question in different ways. Which of these is closest to what you had in mind when you answered?" The answers: "How likely it is that the film's makers took it from the screenplay, and did not come up with it on their own"; "Whether it is something that fairly belongs to the screenwriter"; "Both of these about equally"; "Something else." The first two are in random order.

## A.3 Study 1, GENRE

Rated genre, instructions: "In this part you will think about [Westerns]. We will show you, a few at a time, things that [a Western] includes. Films include things for different reasons. Some things are in a film because of the kind of film it is. Others would be just as likely in a film of any kind. For each one, tell us how much it is in the film because the film is [a Western]. Please use the whole scale."

Each rated item: "[A Western] includes: **[item]**. How much is this in the film because the film is [a Western]?" 1 = Not at all (it could be in any kind of film); 7 = Entirely (it is there because the film is [a Western]).

Tracked genre, instructions: "In this part you will think about [Westerns]. We will show you, one at a time, things that [a Western] includes. Films include things for different reasons. Some things are in a film because of the kind of film it is. Others would be just as likely in a film of any kind. For each one, choose what fits better: that it is in the film because of the genre, meaning because the film is [a Western], or that it could be in any film, meaning that it would be just as likely in a film of any kind. There are no right or wrong answers."

Each tracked trial: the line "[A Western] includes:" and, once the pointer is moving, **[item]**. The boxes read "Because of the genre" and "Could be in any film."

## A.4 Study 1, STOCK

Rated genre, instructions: "Copyright law lets a writer own the particular way a story is told. It does not let anyone own the stock features of a kind of story. A standard legal reference describes these as features that are 'standard, stock, customary, stereotypical, or common' in stories of that kind. Anyone may use them. We will show you, a few at a time, things that [a Western] might include. For each one, tell us whether it is a stock feature of [Westerns] in this sense. Please use the whole scale."

Each rated item: "In [Westerns]: **[item]**. Is this a stock feature of [Westerns]?" 1 = Definitely not; 7 = Definitely.

Tracked genre, instructions: the same four sentences about the rule, then: "We will show you, one at a time, things that [a Western] might include. For each one, choose whether it is a stock feature of [Westerns] in this sense, or not stock. There are no right or wrong answers."

Each tracked trial: the line "In [Westerns]:" and, once the pointer is moving, **[item]**. The boxes read "Stock" and "Not stock."

The quoted adjectives are the Restatement's as the law review manuscript quotes them; the manuscript's check of the black-letter text is still open and this wording should follow it.

## A.5 Study 1, the mouse procedure

Stroop practice: "Each trial starts when you click Start at the bottom of the screen. As soon as you click it, start moving the pointer upward with your mouse or trackpad. A word will appear once you move. Move to the box that names the color of the ink the word is printed in, and click it. Ignore what the word says. For example, if the word BLUE is printed in red ink, choose Red. Keep the pointer moving from the moment you click Start, and answer as quickly and accurately as you can."

Practice choices, COPY: "The boxes now say Copied and Not copied. Imagine a screenplay and a later film made by different people. The screenwriter says the film was copied from the screenplay; the film's makers say they came up with it on their own. Each trial shows one thing that the screenplay and the film both include. Choose Copied if you think the film's makers more likely copied it, and Not copied if you think they more likely came up with it on their own." GENRE: "The boxes now say Because of the genre and Could be in any film. Films include things for different reasons. Some things are in a film because of the kind of film it is. Others would be just as likely in a film of any kind. Each trial shows one thing that a Romance includes. Choose Because of the genre if you think it is in the film because the film is a Romance, and Could be in any film if you think it would be just as likely in a film of any kind." STOCK: "The boxes now say Stock and Not stock. [The four sentences about the rule.] Each trial shows one thing that a Romance might include. Choose Stock if you think it is a stock feature of Romance films in this sense, and Not stock if you think it is not."

Before the tracked genre, after the question's instructions: "Click Start, keep the pointer moving upward, and click your choice as quickly as you can while still choosing carefully. [The first label] is on the left and [the second] on the right, in every trial. There are 82 trials. A few will instead tell you which box to choose." An instructed-response trial reads "Attention check: choose 'Copied'" (or the other label).

## A.6 Frequency estimates (Study 1, every participant)

Each answer is given on a slider from 0 to 100 in steps of 1. The slider shows no handle until the participant clicks it, so that no starting position can pull the answer, and the number chosen is displayed beside the item.

"Think of 100 [Westerns] chosen at random. How many of them include each of the following?"

"Think of 100 films of all kinds chosen at random. How many of them include each of the following?"

"For each of the following, think of 100 films of any kind that include it. How many of those 100 films are [Westerns]?"

## A.7 Study 2

COPY group, pairs: the instructions of A.2 for the rated genre with "things" replaced by "pairs of things." Each trial: "Both the screenplay and the film include: **[first]** and **[second]**. How strongly does this suggest that the film was copied from the screenplay?" An event trial: "Both the screenplay and the film include: **[a stagecoach is robbed]**. How strongly does this suggest that the film was copied from the screenplay?"

NECESSITY group: "In this part you will think about [Westerns]. We will tell you one thing a [Western] includes and ask about a second thing. For each pair, tell us how necessary the second thing is in a [Western] that has the first." Each trial: "A [Western] includes **[first]**. How necessary is it that it also includes **[second]**?" 1 = Not at all (it could easily be left out); 7 = Completely (the story could not do without it). An event trial: "A [Western] includes **[a stagecoach]**. How necessary is it that **[a stagecoach is robbed]**?" Estimates: "Think of 100 [Westerns] that include **[first]**. How many of them also include **[second]**?" and "Think of 100 [Westerns] chosen at random. How many of them include **[second]**?"

## A.8 Study 3

Role, plaintiff's side: "A screenwriter believes that a film was copied from her screenplay and has gone to court. You are working with her lawyers. Your job is to help them prepare by looking closely at the screenplay and the film." Defendant's side: "A screenwriter believes that a film was copied from her screenplay and has gone to court. The people who made the film say they never saw it. You are working with their lawyers. Your job is to help them prepare by looking closely at the screenplay and the film." Juror: "A screenwriter believes that a film was copied from her screenplay and has gone to court. The people who made the film say they never saw it. You are a member of the jury."

Statement of purpose: "Before you read the cases, tell us in two or three sentences what you will look for [on behalf of the screenwriter / on behalf of the film's makers / in deciding the case]."

To all: "You will read eight cases like this one, each about a different screenplay and film. For every case, whatever your role, please give your honest judgment."

Per case: "How likely is it that the makers of the film copied from the screenplay?" (0 = certainly did not, 100 = certainly did). "How similar are the screenplay and the film?" 1 = Not at all similar; 7 = Extremely similar. "Which character in the film corresponds to the screenplay's **[character]**?" (the film's characters, and "no one"). For each listed feature: "In both, and it counts toward copying" / "In both, but it is standard for [Westerns], so it should not count" / "Not in both." "Who should win?" (the screenwriter; the film's makers) and "How confident are you?" 1 to 7. On a side only: "What do you think a jury would decide?"

## A.9 Study 4

Frame, per dispute: "A screenwriter says a later [Western] film was copied from her [Western] screenplay. Her lawyers have listed things the two have in common. [In the count formats: An expert who counted the features of 45,958 film plot summaries has reported on each one.]" Per feature: the report in the participant's format, then, in one pass, "Is this a stock feature of [Westerns]?" 1 = Definitely not; 7 = Definitely (with the definition of A.3), and in the other pass, "How strongly does this suggest that the film was copied from the screenplay?" 1 = Not at all; 7 = Very strongly.

Increment format, bounty hunter: "About 2 in every 100 Westerns include a bounty hunter. About 2 in every 1,000 films of all kinds do."

# Appendix B. An example case for Study 3

The example is a Western shell filled from the rare-but-characteristic cell. The four shared features are a bounty hunter and a ranch hand (kinds of character), a barn (setting) and a stampede (event). In the corpus they are in 1.9%, 2.0%, 1.6% and 1.8% of Westerns. The unshared detail in this example is illustrative; in the experiment it is drawn from the middle third of the genre.

*The screenplay.* A bounty hunter rides into a mining valley looking for a man wanted for a killing back east. The man has been working as a ranch hand under another name and is well liked. The bounty hunter learns who he is and corners him one night in a barn. Before he can take him in, a stampede scatters the herd, and the two men have to ride together until dawn to turn it. By morning the bounty hunter has to decide whether to collect.

*The film, aligned.* A bounty hunter arrives in a river town on the trail of a fugitive. The fugitive has hired on as a ranch hand at a spread outside town, and the owner trusts him. The bounty hunter catches up with him in a barn after dark. A stampede breaks out before he can bring him in, and the two must work side by side to save the cattle. In the end the bounty hunter must choose whether to turn him over.

*The film, scattered.* A widow hires a bounty hunter to find her brother, who went west ten years ago and stopped writing. On the road the bounty hunter is robbed and left for dead, and a ranch hand takes him in until he can ride. The brother, it turns out, died years ago in a stampede. The widow sells what he left her, and the film ends at the auction, held in a barn.

The same shell filled from the common-and-characteristic cell would share a sheriff, an outlaw, a saloon and a gunfight; from the common-but-uncharacteristic cell, a father, a daughter, a house and a death; and from the rare-and-uncharacteristic cell, a lawyer, a lady, a bridge and a funeral.

# Appendix C. Power simulations

The simulations are in `Analysis/tracking_studies_design/tracking_studies_power.Rmd`. Each scenario was simulated 200 times, and each simulated data set was analyzed with the mixed model proposed for the study and a Wald test at the .05 level. For the rating tasks the standard deviations are the law review study's (items 0.99, participants 0.61, the participant slope for distinctiveness 0.59, the participant slope for prevalence 0.09, residual 1.30). For the tracked choices of Study 1 the same values are converted to logits on the assumption that a choice is the rating cut at a threshold, which makes one rating point 1.31 logits and the equivalence bound ±0.52 logits. For the curvature of mouse paths no estimates exist: the simulation works in units of the trial-to-trial standard deviation of curvature and assumes a participant standard deviation of 0.6, participant slopes of 0.15 for each pull, and an item standard deviation of 0.15. In Study 1 each simulated participant rates one genre and answers another with the mouse, by the schedule of Section 8.2. In the design as built the pool has 18 items in each cell of each genre. In the rated genre a simulated participant is shown 12 of them, drawn at random, and in the tracked genre all 18. The ratings and the choices are analyzed in separate models, so nothing has to be assumed about how a person's two sets of answers are related. Only the copying question is simulated; the other two groups have the same structure. For Study 3 no estimates exist either, and the simulation assumes a participant standard deviation of 14 points on the 0-to-100 scale, a participant slope for arrangement of 8, a shell standard deviation of 6, a further deviation of 5 for each shell-by-condition version, and a residual of 18. For Study 4 each item is given a further deviation of 0.5 points in each format. These are assumptions, not data.

| Account simulated | Participants per question | P minus D below zero | P minus D above zero | D differs from zero | D within ±0.40 | D within ±0.30 | P differs from zero |
|---|---|---|---|---|---|---|---|
| one intuition | 60 | 0% | 100% | 100% | 0% | 0% | 65% |
| one intuition | 80 | 0% | 100% | 100% | 0% | 0% | 67% |
| one intuition | 100 | 0% | 99% | 100% | 0% | 0% | 68% |
| one intuition | 120 | 0% | 100% | 100% | 0% | 0% | 69% |
| overall frequency | 60 | 100% | 0% | 100% | 0% | 0% | 100% |
| overall frequency | 80 | 100% | 0% | 100% | 0% | 0% | 100% |
| overall frequency | 100 | 100% | 0% | 100% | 0% | 0% | 100% |
| overall frequency | 120 | 100% | 0% | 100% | 0% | 0% | 100% |
| query-sensitive | 60 | 95% | 0% | 6% | 86% | 57% | 100% |
| query-sensitive | 80 | 96% | 0% | 3% | 91% | 60% | 100% |
| query-sensitive | 100 | 95% | 0% | 6% | 92% | 61% | 100% |
| query-sensitive | 120 | 98% | 0% | 6% | 92% | 69% | 100% |

: Table C1. Study 1 as built, ratings of copying (each participant rates 48 of a genre's 72 items): share of simulations in which each test gives the stated result.

| Account simulated | Participants per question | Share choosing "Copied" | P minus D below zero | P minus D above zero | D differs from zero | D within the bound | P differs from zero |
|---|---|---|---|---|---|---|---|
| one intuition | 60 | 50% | 0% | 98% | 100% | 0% | 58% |
| one intuition | 80 | 50% | 0% | 99% | 100% | 0% | 63% |
| one intuition | 100 | 50% | 0% | 100% | 100% | 0% | 58% |
| one intuition | 120 | 50% | 0% | 100% | 100% | 0% | 64% |
| overall frequency | 60 | 50% | 100% | 0% | 99% | 0% | 100% |
| overall frequency | 80 | 50% | 100% | 0% | 100% | 0% | 100% |
| overall frequency | 100 | 50% | 100% | 0% | 100% | 0% | 100% |
| overall frequency | 120 | 50% | 100% | 0% | 100% | 0% | 100% |
| query-sensitive | 60 | 50% | 92% | 0% | 4% | 88% | 100% |
| query-sensitive | 80 | 50% | 96% | 0% | 4% | 93% | 100% |
| query-sensitive | 100 | 50% | 97% | 0% | 4% | 95% | 100% |
| query-sensitive | 120 | 51% | 96% | 0% | 2% | 97% | 100% |
| query-sensitive, a quarter "Copied" | 100 | 32% | 92% | 0% | 4% | 93% | 100% |

: Table C2. Study 1 as built, tracked choice of copying (each participant judges all 72 items of the tracked genre): share of simulations in which each test gives the stated result. The bound for D is the logit equivalent of ±0.40 rating points.

| Pull of typicality (trial SDs) | Participants per question | Item trials per participant | Pull of typicality detected | Pull of prevalence (0.10) detected | The two pulls told apart |
|---|---|---|---|---|---|
| 0.10 | 60 | 72 | 76% | 84% | 7% |
| 0.10 | 80 | 72 | 85% | 88% | 6% |
| 0.10 | 100 | 72 | 94% | 96% | 9% |
| 0.10 | 120 | 72 | 97% | 98% | 6% |
| 0.15 | 60 | 72 | 99% | 87% | 21% |
| 0.15 | 80 | 72 | 100% | 92% | 27% |
| 0.15 | 100 | 72 | 100% | 98% | 23% |
| 0.15 | 120 | 72 | 100% | 100% | 35% |
| 0.20 | 60 | 72 | 100% | 86% | 58% |
| 0.20 | 80 | 72 | 100% | 89% | 60% |
| 0.20 | 100 | 72 | 100% | 97% | 77% |
| 0.20 | 120 | 72 | 100% | 98% | 75% |

: Table C3. Study 1 as built, tracked choice of copying, curvature (all 72 items of the tracked genre): share of simulations in which each pull is detected, and in which the two are distinguished, when choices follow prevalence alone. Where the two pulls are equal (0.10), the last column is the false-positive rate.

| Design | Participants rating and tracking | Items each rates and tracks | Ratings: P minus D below zero | Ratings: D within ±0.40 | Choice: P minus D below zero | Choice: D within the bound | Pull of 0.10 detected | Pull of 0.20 told apart from 0.10 |
|---|---|---|---|---|---|---|---|---|
| As built: 48 of 72 rated, all 72 tracked | 100 and 100 | 48 and 72 | 95% | 92% | 97% | 95% | 94% | 77% |
| 48 of 72 shown in both genres | 100 and 100 | 48 and 48 | 95% | 92% | 93% | 92% | 85% | 63% |
| All 72 shown in both genres | 100 and 100 | 72 and 72 | 97% | 95% | 97% | 95% | 94% | 77% |
| The 288 items only | 100 and 100 | 48 and 48 | 90% | 79% | 88% | 80% | 83% | 55% |
| Separate groups for the two ways, all 432 shown | 50 and 50 | 144 and 144 | 95% | 81% | 94% | 87% | 88% | 62% |
| First genres only, all 432 shown | 52 and 48 | 72 and 72 | 95% | 81% | 87% | 84% | 79% | 45% |

: Table C4. Study 1, ways of using 100 participants per question, when judgments follow prevalence alone: share of simulations in which each test succeeds.

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

: Table C5. Study 2 with unmatched pairs.

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

: Table C6. Study 2 with matched sets.

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

: Table C7. Study 3: share of simulations in which each effect is detected. Where the distinctiveness effect is 0, the distinctiveness column is the false-positive rate.

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

: Table C8. Study 4: the difference between two count formats in the LH-minus-HL gap.

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
| `Experiment/Tracking Study 1 (Pavlovia experiment-2)/` | The Study 1 experiment as rebuilt on November 19: `experiment.js`, `index.html`, `style.css`, the law review study's item files, a README with the data columns and test links, and the deployment script for `genres-and-themes/experiment-2` |
| `Experiment/Archive/Four-group build (deployed 2026-11-19, replaced by the three-group build)/` | The build this one replaces, for the record |
| `Experiment/Archive/Study 2 two-genre choice (retired 2026-11-18)/` | The retired two-genre build, unchanged |
| `Experiment/Study 1/` | The law review study's experiment (`genres-and-themes/experiment-1`, closed) |
| `Analysis/notebooks/_build_18.py`, `18_tracking_studies_design.ipynb` | Corpus inputs: the three quantities for every story feature and genre; the law review study's items under the model; chance overlap; the shared-title check; candidate pairs; concrete features by cell |
| `Analysis/notebooks/_build_19.py`, `19_event_pairs_design.ipynb` | Events for Study 2: how stable their counts are, how many there are, and the candidate pairs of a feature and an event |
| `Analysis/notebooks/_build_20.py`, `20_extended_item_set.ipynb` | The 144 new items of Study 1: the law review study's draw reproduced and continued, the review, and the check that the cells stay matched. Outputs, with the review log, in `Analysis/v4_rebuild/20_extended_item_set/` |
| `Analysis/tracking_studies_design/design_inputs_from_law_review_study.Rmd` | Item means, listing rates and the variance components of the law review study's registered ratings model, using the registered exclusions and tables |
| `Analysis/tracking_studies_design/tracking_studies_power.Rmd` | Power simulations for the four studies, including the choices and pointer paths of Study 1 |
| `Analysis/v4_rebuild/18_tracking_studies_design/`, `19_event_pairs_design/` | Outputs of the files above, including the tables and figures in this memo |
| `Analysis/notebooks/17_category_utility.ipynb` | Incremental category validity and the identity linking the two increments (Part F) |
| `Analysis/notebooks/archive/12_study2_stimuli.ipynb`, `Analysis/Archive/study2_two_genre_power_retired_2026-11-18/` | The item draw and power simulations of the retired two-genre study |
| `Docs/Memorandum/Superseded/` | The memoranda of November 17 and November 18, which this one revises |
