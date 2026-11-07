# Validation status — 2026-11-06

## Historical GitHub Actions verification

The first successful GitHub Actions run on the `main` branch installed the project dependencies and executed the actual Mesa library on Python 3.12.

- GitHub Actions run: https://github.com/methu28/eclass-notification-model/actions/runs/42297387338
- Installed Mesa version: **3.5.2**
- Test result: **10 passed, 2 warnings**, with **no skipped integration tests**
- `python run.py` completed successfully under genuine Mesa
- Both runs initialized 20 notification agents, advanced through six simulated 6-hour steps, and generated output files
- The workflow uploaded artifact `mesa-comparison-outputs`. The default CSVs, figures, and metadata are now tracked in `outputs/` at audited commit `8235432c45cd1df7e495686b7428862586902a52`. The audit also confirmed a successful workflow run for that commit: https://github.com/methu28/eclass-notification-model/actions/runs/42303794757 . This is historical CI evidence, not CI verification of the current uncommitted fixes.

### Recorded example results from the run logs

| Step | Urgent total | Recency urgent in top five | Hybrid urgent in top five |
|---|---:|---:|---:|
| 0 | 4 | 0 | 2 |
| 1 | 5 | 0 | 2 |
| 2 | 6 | 0 | 2 |
| 3 | 7 | 0 | 2 |
| 4 | 8 | 0 | 2 |
| 5 | 8 | 0 | 2 |
| 6 | 8 | 0 | 2 |

These are results of **one fixed synthetic scenario**, not measurements of actual eClass.

The two warnings report that Mesa's `seed` constructor argument is deprecated in favor of `rng`. This does not invalidate the successful run, but the project can migrate to the newer argument in a reviewed update.

## Local targeted-fix verification

Environment: Python 3.12.14, Mesa 3.5.2, pandas 2.3.3, matplotlib 3.11.2, pytest 9.2.0. The root README documents both standard Python and the uv installation route used locally. The original example additionally used `mesa[rec]==3.5.2`.

The configured model urgency threshold now applies consistently to initial urgency, initial recent nonurgent cohort membership, and later steps. The cohort remains fixed after initialization. The default CLI continues to use 72 hours; custom thresholds are constructor parameters only. The input loader still validates its fixed dataset using the default 72-hour definition.

Executed from the repository root:
```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe run.py --output-dir .venv/audit/targeted_fixes_qlu5uckf/run1
.\.venv\Scripts\python.exe run.py --output-dir .venv/audit/targeted_fixes_qlu5uckf/run2
```

- Complete suite: **14 passed, 6 warnings, no skips**. Warnings are the existing Mesa `seed` deprecation; the four extra warning entries accompany four new parameterized test cases.
- New regression cases cover both policies with the repository dataset at a 24-hour threshold: urgent totals at steps 0-6 are `0, 0, 0, 0, 1, 2, 3`.
- Additional 20-record in-memory fixtures check a deadline exactly at 24 hours, a later threshold crossing, a missing deadline, posting age outside the recent cohort, cohort retention after urgency changes, and urgency exclusion at deadline zero. These fixtures exercise the constructor directly without changing the fixed input CSV or CLI scope.
- Both default comparison runs completed. All five fresh CSV tables matched the tracked CSVs exactly using pandas frame comparisons, including both 140-row agent exports.
- All nine generated files were byte-identical between the two fresh runs. Metadata uses the local input path, so it is not claimed byte-identical to the partner's committed metadata.
- File hashes confirmed that existing outputs and the preserved original example were unchanged during execution. Fresh results are in ignored `.venv/audit/`; no source-example files or existing outputs were rewritten.
- Default numerical findings remain the table above: urgent visibility 0 versus 2 throughout, urgent totals rising from 4 to 8, and initial recent nonurgent visibility 5 versus 3. Hybrid urgent coverage declines from 50% to 25%.

## Preserved example and output audit

All six files in `src/mesa_source/boltzmann_wealth_model/` matched the upstream Git blobs at the commit recorded in `SOURCE.md`. Provenance and the Apache 2.0 license are included. A 50-agent original model completed a step; its Solara app module loaded and server responded with HTTP 200 after installing recommended extras. Interactive browser controls and the optional Streamlit app were not exercised.

The audit visually reviewed all three committed PNGs and reconciled all seven model snapshots against the 140 agent rows per condition. It independently reconstructed top-five membership and average urgent rank from the input CSV. Both policies use identical input/time/urgency trajectories. These are computational checks of one synthetic scenario, not validation against real eClass or students.

## Remaining work and known limitations

1. Review the local changes before committing. No commit, push, tag, release, or publication was performed by the local fixes.
2. Verify the README workflow from a fresh clone on a partner's machine and exercise the original visualization controls.
3. Confirm partner write access, genuine contributions, and individual Accountability Records, including AI assistance disclosure.
4. Finish DEL02.1 sections 1-5 using the actual outputs.
5. Create the required annotated `DEL02` tag and `DEL02 Release` only after final review; they were absent at the audit.
6. Optional follow-ups: migrate deprecated `seed`, lock dependency versions, add input hashes, and make the hardcoded comparison legend reflect nondefault reserved slots. Metric names containing `top5` also remain fixed if constructor-level capacity changes. These were left outside the targeted fixes.

A separate urgency-only policy, notification volumes 10 and 40, multiple synthetic datasets, notification arrivals/removals, and student behavior remain deferred. Reserved-slot counts other than two are already configurable, but are not part of the tracked default experiment.
