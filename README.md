# eClass Notification Visibility: DEL02 Mesa Prototype

**Status:** Runnable DEL02 development prototype using genuine Mesa. The preserved original example and default simulation outputs are included and tracked. Local changes still require review before submission.

## Research question and scope

This is a selective computational representation of York University's eClass notification dropdown. We compare **hypothetical** ordering rules, not a verified eClass algorithm. We measure *opportunities for visibility* in the first five positions, **not** student attention or actual reading.

- 20 entirely fictional course notifications from `data/notifications.csv`
- Exactly four initially urgent notifications (deadline within the next 72 hours)
- **Baseline:** newest posted notification first
- **Alternative:** two newest urgent notifications first, followed by all remaining notifications in recency order, with no duplicates
- Six model steps of six hours each, plus step 0
- Time advances, deadline urgency can change, and all notifications are re-ranked each step
- No new arrivals, deletions, overdue notifications, human decisions, or private student records

## Setup and run

Requirements: **Python 3.12+** and an internet connection for the first installation. The notification model uses Mesa, pandas, matplotlib, and pytest from `requirements.txt`. The original example's visualization additionally requires `mesa[rec]` (see below). Dependency ranges are not a lockfile.

Run these commands from the repository root. Use a fresh output directory to preserve committed results; the runner overwrites matching filenames in its selected output directory.

**Windows PowerShell, with Python installed:**
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe run.py --output-dir .venv/results/run1
```

If `python` opens the Microsoft Store or is unavailable, install Python 3.12+ first. If `uv` is available, this alternative was verified locally:
```powershell
uv python install 3.12
uv venv --python 3.12 .venv
uv pip install --python .venv\Scripts\python.exe -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe run.py --output-dir .venv/results/run1
```

A uv-created environment may not include pip. Use `uv pip` for dependency management, or run `.\.venv\Scripts\python.exe -m ensurepip` before using `python -m pip`.

**macOS/Linux:**
```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q
.venv/bin/python run.py --output-dir .venv/results/run1
```

The convenience scripts `setup.ps1` and `setup.sh` install dependencies, run tests, and run the default comparison into `outputs/`, replacing matching files. Use them only when intentionally regenerating outputs. `setup.ps1` requires the Windows `py` launcher; the manual commands above avoid that dependency. The shell script requires `python3` version 3.12+.

The CLI supports `--input`, `--output-dir`, `--steps`, `--hours-per-step`, `--reserved`, and `--seed`. For example, with the environment's Python:
```bash
python run.py --steps 6 --hours-per-step 6 --reserved 2 --seed 42 --output-dir .venv/results/run2
```

The loader requires 20 records and four initially urgent items under the default 72-hour definition. The CLI always compares recency and hybrid, uses a 72-hour threshold and five visible positions, and rejects runs reaching the earliest deadline. A custom urgency threshold is available through `NotificationModel`, not a CLI option. It applies at initialization, to the initial recent nonurgent cohort, and on every step. No random draws are used by the notification process; changing the seed alone does not change its outputs.

### Generated outputs

The following default results are already tracked in `outputs/`. Running `python run.py` regenerates them; `--output-dir` redirects new files:

| File | Meaning |
|---|---|
| `baseline_raw_00_urgent_visibility.csv` | Recency model metrics at steps 0–6 |
| `alternative_raw_00_urgent_visibility.csv` | Hybrid model metrics at steps 0–6 |
| `baseline_raw_01_agent_states.csv` | Per-notification recency states |
| `alternative_raw_01_agent_states.csv` | Per-notification hybrid states |
| `baseline_processed_00_urgent_visibility.png` | Baseline visibility chart |
| `alternative_processed_00_urgent_visibility.png` | Alternative visibility chart |
| `comparison_processed_00_urgent_visibility.png` | Direct comparison chart |
| `comparison_processed_01_visibility_differences.csv` | Stepwise policy differences |
| `run_metadata.json` | Parameters and detected Mesa version |

The primary outcome is the number of urgent items in the first five positions. Supporting measurements include the share of all urgent items visible, average urgent ranking, recent nonurgent visibility, and how many initially recent nonurgent entries remain visible.

**GitHub Actions:** Every push to `main` and each pull request runs the project using installed Mesa and uploads computed output files as a workflow artifact. Downloading that artifact does **not** automatically commit the results to the repository. The default outputs are already committed. Review any newly generated artifacts before deciding whether to replace submission outputs.

## Original Mesa example required by DEL02

The complete unchanged Boltzmann Wealth example is preserved in `src/boltzmann_wealth_model/`. `src/boltzmann_wealth_model/SOURCE.md` records upstream commit `fe24c24ee34762de2ff85d487af14bfb5cd1dbb2` and its retrieval timestamp; `UPSTREAM_LICENSE` contains Apache License 2.0. All six example files were checked against that upstream commit during the audit.

From the repository root in PowerShell, install the preserved example's recommended extras and start its visualization:
```powershell
.\.venv\Scripts\python.exe -m pip install "mesa[rec]==3.5.2"
Set-Location src/boltzmann_wealth_model
..\..\.venv\Scripts\solara.exe run app.py
```

With uv, the equivalent installation is `uv pip install --python .venv\Scripts\python.exe "mesa[rec]==3.5.2"`. On macOS/Linux, install using `.venv/bin/python -m pip install "mesa[rec]==3.5.2"`, then run `../../.venv/bin/solara run app.py` from the example directory. Open the displayed local URL; stop the server with Ctrl+C. The example imports modules from installed Mesa as well as the preserved directory. Its optional Streamlit alternative has additional dependencies described in its unchanged `Readme.md` and was not verified in this audit.

`scripts/fetch_source_example.py` is retained for provenance/retrieval purposes. It is not a setup step for this checkout and deliberately refuses to overwrite the existing example. Do not rerun it expecting an update.

Official documentation:
- https://mesa.readthedocs.io/stable/tutorials/0_first_model.html
- https://mesa.readthedocs.io/stable/tutorials/5_collecting_data.html

Our adapted project is in `src/project_model/`; its rules are different from the original wealth model. Notification agents update time-related attributes, while the model (not individual agents) implements the notification ranking policy. This avoids suggesting that individual notifications consciously decide where they appear.

## Validation and limitations

- Run `python -m pytest -q` with **Mesa genuinely installed**. Check that the integration tests are not skipped.
- Run the comparison twice into different fresh `--output-dir` directories and compare their CSVs with each other and with the tracked default results.
- Verify that recency and hybrid use the same 20 records and six-hour timeline.
- The original model step, Solara page loading, and HTTP server startup were verified with Mesa 3.5.2 and its recommended extras; interactive browser controls were not exercised.
- Include only genuinely generated and reviewed outputs in the final submission.

This model cannot reveal the internal eClass ranking algorithm, predict actual student behaviour, or establish whether students read alerts. The 72-hour definition of urgency and five visible positions are modelling assumptions.

The default tracked results show 0 urgent items visible under recency and 2 under hybrid at every snapshot. Total urgent items increase from 4 to 8; hybrid urgent coverage falls from 50% to 25%. Initially recent nonurgent visibility is 5 versus 3. These are results of one intentionally constructed dataset.

Implemented: recency and hybrid ordering, volume 20, time-dependent urgency, and urgent/nonurgent visibility metrics. Deferred: a separate urgency-only policy, volumes 10 and 40, multiple datasets, arrivals/removals, and student behavior. Reserved-slot counts other than two are configurable but are not part of the tracked default experiment; the comparison plot legend currently hardcodes two reserved slots.

See `docs/model_design.md`, `docs/validation_status.md`, and `docs/del02_submission_checklist.md`.

## Collaboration, AI assistance, and submission

The source code and synthetic dataset were created with AI assistance. Partners must review the implementation, document their own genuine contributions, confirm repository write access, and complete individual Accountability Records. The DEL02 report, annotated submission tag, and GitHub release remain submission tasks; this local verification does not create or publish them.
