# Section 2.2: Final computational representation (review draft)

## Section 2.2.1: Representation overview

This model represents 20 synthetic course notifications as they age, change urgency state, and receive display ranks under recency ordering and hybrid ordering with one, two, or three reserved urgent positions. It does not represent eClass's actual algorithm, student attention or reading, or notification arrivals and removals.

## Section 2.2.2: Representation ledger

The four headings match the actual specification, PDF pages 2-3. E-labels refer to [inventory.md](inventory.md) and its saved records. Inferred and synthetic entries are not field observations. Unsupported real-world values are explicitly identified as synthetic choices; their analytical rationale is proposed for team review in [modelling_assumptions.md](modelling_assumptions.md).

| Model component or assumption | What it does in the model | Evidence or input | Status and limit |
|---|---|---|---|
| Notification-list referent | Selects course-information display as the arrangement examined | E1 institutional context; E4 upstream menu; E5 observed redacted DEL01 crop | Observed interface elements support the referent; the model remains a selective abstraction, not the actual platform pipeline |
| Passive notification entities | Gives each record age, deadline, urgency, rank and visibility state | E6; E7; E8 technical pattern | Synthetic representation, not human decision-making |
| Same fixed population of 20 | Controls input volume across all four conditions | E6; E7 | Synthetic choice to isolate ordering; not measured traffic |
| Categories, posting ages and optional deadlines | Supplies heterogeneous information and temporal attributes | E6 | Synthetic inputs; no verified mapping of every category to a York bell event |
| Four initially urgent plus four later threshold crossings | Produces a changing urgency population within the fixed list | E6; E7 | Constructed contrast; not a population proportion |
| Urgency within 72 hours and strictly before deadline | Classifies items at initialization and each step | E7 | Synthetic operational definition; not a York policy or an urgency-only sorting condition |
| Newest-first recency | Assigns the baseline list order with ID tie-breaking | E7 | Hypothetical baseline; not verified platform behavior |
| Hybrid K=1,2,3 | Promotes K newest urgent items and fills the rest by recency without duplicates; K=2 primary, K=1/3 sensitivity | E7; E10 | Synthetic alternative family; newest urgent is not nearest deadline |
| Five visible positions | Limits the measured region to ranks 1-5 | E7 synthetic choice; E5 records one redacted cropped interface state | Synthetic fixed-capacity proxy; E5 shows four entries in this crop and does not establish a universal capacity |
| Six six-hour steps plus initial snapshot | Advances time over 36 hours and reranks | E7 | Synthetic discretization; no user checking schedule |
| Urgent visible count and coverage | Counts urgent items in ranks 1-5 and divides by all currently urgent items | E7; E10 | Computational measures, not attention or reading; denominator changes over time |
| Mean urgent rank | Averages positions of all currently urgent items | E7; E10 | Computational measure; cross-time changes can reflect changed membership |
| Current recent nonurgent age at most 24 hours | Measures recent nonurgent entries in ranks 1-5 | E7 | Synthetic recency window; zeros can reflect aging rather than displacement |
| Initial recent nonurgent cohort | Keeps initial cohort membership fixed and measures its visible count | E6; E7 | Synthetic analytical cohort, not a user group; separates aging from displacement |
| No arrivals, deletions, read-state changes or overdue items in default run | Isolates ranking and threshold transitions | E7 | Deliberate simplification; recency order stays fixed without arrivals |
| No delivery eligibility or preference simulation | Gives each condition identical available records | E7; E2-E4 provide omitted context | Synthetic boundary; surrounding channel governance is not implemented |
| No student behavior or educational outcomes | Ends the computational measurement at list position | E7 | Explicit omission; cannot infer noticing, reading, missed deadlines or grades |
| Deterministic repeated execution and shared inputs | Makes runs comparable and reproducible | E6; E7; E11 | Verified implementation property; repeated runs are not independent empirical samples |
| Original Mesa example preserved separately | Supplies implementation provenance without importing wealth dynamics into the inquiry | E8 | Technical lineage only; no wealth/attention analogy is validated |

The actual ordering of York's notification dropdown is unknown within this inquiry. Do not connect E1-E4 to the recency/hybrid rows as if those sources justified an implementation claim.
