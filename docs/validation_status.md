# Validation status — 2026-11-06

## Verified with genuine Mesa on GitHub Actions

The first successful GitHub Actions run on the `main` branch installed the project dependencies and executed the actual Mesa library on Python 3.12.

- GitHub Actions run: https://github.com/methu28/eclass-notification-model/actions/runs/42297387338
- Installed Mesa version: **3.5.2**
- Test result: **10 passed, 2 warnings**, with **no skipped integration tests**
- `python run.py` completed successfully under genuine Mesa
- Both runs initialized 20 notification agents, advanced through six simulated 6-hour steps, and generated output files
- The workflow uploaded the output files as artifact `mesa-comparison-outputs` (artifact must be downloaded/reviewed and final files committed to `outputs/` before submission)

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

## Still required before DEL02 submission

1. Retrieve the **complete unchanged original Mesa example**, record provenance and attribution in SOURCE.md, and verify it runs independently.
2. Download the GitHub Actions artifact and review the generated CSVs and PNGs. Commit the actual reviewed outputs to `outputs/`.
3. Verify the README from a fresh clone and confirm reproducibility on a partner's machine.
4. Have both partners review the AI-generated source, contribute meaningfully, and record accurate, independent Accountability Records.
5. Finish DEL02.1 §§1–5 using the actual outputs.
6. Create the required annotated `DEL02` tag and `DEL02 Release` only from a tested complete submission commit.

The initial build sandbox did **not** install Mesa, but the later GitHub Actions run **did** and passed successfully.
