# Model design and assumptions

## Project phenomenon
The referent is York University's student-facing eClass bell-icon dropdown. The prototype compares *hypothetical* recency and hybrid ranking rules; it does not establish which algorithm eClass uses.

## DEL02 slice
- Fixed collection of 20 entirely synthetic notifications, initially four urgent (20%).
- A deadline is urgent only when `0 < hours_until_deadline <= 72`.
- Four other deadline-bearing items initially have 78, 84, 90, and 96 hours until deadline and cross the 72-hour threshold as time advances.
- Six 6-hour steps and one initial snapshot; notifications are neither created nor removed.
- First five list positions serve as the model's visibility proxy.

## Entities and rules
`NotificationAgent` is a Mesa agent carrying ID, category, posting age, optional deadline, urgency, rank, and top-five status. Its `step()` updates time-related states. It is a passive information item, not a human decision-maker.

`NotificationModel` is the ordering environment. Each model step activates every notification, applies the selected platform-level ranking policy, updates every rank, and collects data through `mesa.DataCollector`.

- **Recency:** sort by ascending posting age (newest first), breaking ties by notification ID.
- **Hybrid:** reserve the first two positions for the two newest currently urgent items, then sort *all remaining* items by recency. Never duplicate a notification.
- Both runs use the same dataset, clock, threshold, and parameters apart from ordering policy.
- The fixed initial synthetic distribution is intentionally designed to produce meaningful ranking contrasts.

## Measured outputs
- `urgent_total`: all currently urgent notifications
- `urgent_top5_count`: urgent notifications ranked 1 through 5
- `urgent_top5_share`: urgent top-five / all urgent
- `average_urgent_rank`: mean rank of currently urgent items
- `recent_nonurgent_top5`: currently nonurgent notifications posted within the past 24 hours in the top five
- `initial_recent_nonurgent_top5`: members of the initially recent nonurgent cohort remaining in the top five
- `top_five_ids`: auditable notification IDs by display rank

## Adaptation from Mesa example
The Boltzmann Wealth example provides a technical pattern for a Model managing multiple Agent entities, repeated activation, and data collection. This adaptation replaces money exchange with time-dependent notification states and centrally assigned rankings. It is **not** an analogy between wealth and message visibility.

The complete unchanged original example is included in `src/mesa_source/boltzmann_wealth_model/`, with commit/date provenance in `src/mesa_source/SOURCE.md` and Apache 2.0 license in `UPSTREAM_LICENSE`. The audit verified all six files against the recorded upstream commit, a model step, and Solara startup using Mesa 3.5.2 with recommended extras. Browser controls and the optional Streamlit interface were not verified. See the root README for installation and working-directory instructions.

## Limitations
No notification arrivals, dismissals, reader decisions, phone viewport measurements, or overdue alerts are modelled. The model cannot establish the actual eClass algorithm or what real students read. Recency rankings stay constant across steps without new arrivals; changes in hybrid ranking occur when deadlines become urgent.

Deferred experiments/features: a separate urgency-only policy, list sizes 10 and 40, multiple synthetic datasets, arrivals/removals, and student decisions. Hybrid reserved slots 1 and 3 are already configurable through `--reserved`, but have not been evaluated in the tracked default comparison. The comparison legend currently says two reserved slots even for other values.

## Parameter boundaries
The CLI runs both policies with a 72-hour threshold and five visible positions. It exposes input/output paths, steps, hours per step, reserved positions, and seed. The input loader requires 20 records and four initially urgent items using the default 72-hour definition. The model constructor additionally accepts a custom urgency threshold and visible-position count. The configured threshold applies to initial urgency, initial recent nonurgent cohort membership, and subsequent updates. Initial cohort membership stays fixed even if an item later becomes urgent or older than 24 hours. Metric names containing `top5` still refer to the configured capacity if changed through the constructor.

The notification process uses no random draws. The CLI prevents reaching a deadline; direct constructor/step use does not enforce that run-length restriction. Urgency excludes a deadline at zero or below.
