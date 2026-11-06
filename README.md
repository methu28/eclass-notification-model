# eClass Notification Visibility: DEL02 Mesa Prototype

**Status:** Development prototype. Genuine Mesa execution is checked by GitHub Actions; the complete unchanged source example still needs to be retrieved and run before the DEL02 submission. Do not create the final DEL02 tag/release until validation and partner review are complete.

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

Requirements: **Python 3.12+**, an internet connection for the first installation, and Git when retrieving the original Mesa example.

**Windows PowerShell**, from the repository root:
```powershell
.\setup.ps1
```

**macOS/Linux:**
```bash
bash setup.sh
```

The scripts create a project-local `.venv`, install dependencies, execute tests and run the comparison.

**Manual alternative:**
```bash
python -m venv .venv
# Activate it: on macOS/Linux use source .venv/bin/activate
# On Windows PowerShell use .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python run.py
```

For a different parameter set:
```bash
python run.py --steps 6 --hours-per-step 6 --reserved 2 --seed 42
```

### Generated outputs

Running `python run.py` creates the following files in `outputs/`:

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

**GitHub Actions:** Every push to `main` and each pull request runs the project using installed Mesa and uploads computed output files as a workflow artifact. Downloading that artifact does **not** automatically commit the results to the repository. Review them and commit the actual generated outputs before submission.

## Original Mesa example required by DEL02

The specification asks for a **complete unchanged existing Mesa source example**, plus provenance and a working run command, alongside the separately adapted model. This repository currently contains a helper script, **not yet the upstream example**.

On a computer with Git and internet access, run:
```bash
python scripts/fetch_source_example.py
```

The script fetches the official Boltzmann Wealth Model example into `src/mesa_source/boltzmann_wealth_model/`, preserves the entire source directory unchanged, and records the upstream commit and attribution in `src/mesa_source/SOURCE.md`. Confirm the original example runs using its own instructions, and commit that complete source folder, SOURCE.md and license file.

Official documentation:
- https://mesa.readthedocs.io/stable/tutorials/0_first_model.html
- https://mesa.readthedocs.io/stable/tutorials/5_collecting_data.html

Our adapted project is in `src/project_model/`; its rules are different from the original wealth model. Notification agents update time-related attributes, while the model (not individual agents) implements the notification ranking policy. This avoids suggesting that individual notifications consciously decide where they appear.

## Validation and limitations

- Run `python -m pytest -q` with **Mesa genuinely installed**. Check that the integration tests are not skipped.
- Run `python run.py` twice and confirm both runs produce the same CSVs.
- Verify that recency and hybrid use the same 20 records and six-hour timeline.
- Run the original preserved Mesa example and document how to reproduce it.
- Include only genuinely generated and reviewed outputs in the final submission.

This model cannot reveal the internal eClass ranking algorithm, predict actual student behaviour, or establish whether students read alerts. The 72-hour definition of urgency and five visible positions are modelling assumptions.

See `docs/model_design.md`, `docs/validation_status.md`, and `docs/del02_submission_checklist.md`.

## Collaboration, AI assistance, and submission

The source code and synthetic dataset were created with AI assistance. Both students should review, understand, test and meaningfully contribute to the repository. Disclose AI use accurately in individual Accountability Records; GitHub commit attribution alone does not establish original authorship.

After passing genuine Mesa tests, confirming the unchanged Mesa example runs, committing outputs and documenting findings, create the prescribed **annotated** `DEL02` tag (message: `DEL02.2 - Submission - Initial Computational Prototype`) and GitHub release titled `DEL02 Release`. Do not tag an unverified prototype as the final submission.
