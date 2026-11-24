# E7: Synthetic rules, operational definitions, and representation choices

- Record prepared/inspected: 2026-11-22.
- Status: synthetic modelling choices; implementation is inspectable. No rule below is identified as York eClass's actual algorithm.
- Canonical definitions: [ordering.py](../../../src/project_model/ordering.py), [notification_model.py](../../../src/project_model/notification_model.py), [notification_agent.py](../../../src/project_model/notification_agent.py).
- Experiment configuration: [run_del03.py](../../../src/project_model/run_del03.py).
- Existing design account: [model_design.md](../../model_design.md); its DEL02 default-comparison scope must be distinguished from DEL03 sensitivity work.
- Provisional citation: (*Model design and assumptions*, n.d.). See [references](../references.md).

## Rules represented

1. Recency sorts by ascending posting age, with notification ID breaking ties.
2. Urgency is a Boolean classification: remaining deadline exists and is greater than zero and at most 72 hours. This is not a separate urgency-only ordering policy.
3. Hybrid selects the K newest currently urgent notifications, where K is 1, 2, or 3, then appends every remaining notification in recency order without duplication. It does not select urgent items by closest deadline.
4. Mesa activates all 20 passive notification agents each step. Posting age increases and remaining deadline decreases by six hours; urgency and ranks are recomputed. No notifications arrive or disappear.
5. Step 0 plus six steps yields seven snapshots over 36 hours. The CLI rejects reaching an overdue deadline.
6. Visibility is rank 1-5. Coverage is visible urgent/all urgent. Mean urgent rank uses all currently urgent items. Current recent nonurgent visibility uses age at most 24 hours; the initially recent nonurgent cohort retains its step-0 membership.

## Why use these choices?

They create a controlled comparison of display-capacity allocation without changing the input population. These are proposed analytical justifications for the dossier, subject to team review, not empirical claims. See the choice/rationale/status list in [modelling_assumptions.md](../modelling_assumptions.md).

## Boundary

The model does not implement actual eClass internals, channel eligibility, preferences, arrivals, human attention, or educational outcomes. The external documentation supplies context, not the numerical thresholds or ranking rules. No urgency-only policy or extra volume has been added.

## Dossier comparison roles and earlier proposal

Recency is the primary baseline and hybrid K=2 the primary alternative; K=1 and K=3 are sensitivity conditions. [E13](E13_del01_inquiry_plan.md) verifies the earlier urgency-only proposal (urgent class before nonurgent class, newest-first within each). It was not implemented, and no results are attributed to it.
