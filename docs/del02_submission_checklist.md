# DEL02 submission checklist

- [x] Audit confirmed successful GitHub Actions execution at commit `8235432c45cd1df7e495686b7428862586902a52`.
- [ ] Verify CI again after the reviewed local fixes are committed and pushed by the partners.
- [x] Install dependencies and run the full test suite locally using the README manual/uv workflow.
- [ ] Verify installation from a fresh clone on a partner machine; setup scripts regenerate `outputs/`.
- [x] Preserve the complete unchanged upstream Mesa example; all six files matched the recorded upstream commit.
- [x] Verify the original model step and Solara startup with `mesa[rec]==3.5.2`.
- [ ] Exercise the original visualization controls in a browser before final submission.
- [x] Confirm `src/mesa_source/SOURCE.md` contains the actual fetched commit, retrieval date, path, and license reference.
- [x] Source example, attribution, and default generated output files are tracked at the audited commit.
- [ ] Review local fixes before committing; do not replace existing outputs without reviewing regenerated results.
- [x] Audit reviewed all three tracked plots and reconciled CSV values; default results were reproduced.
- [ ] Use only observed numbers in the submitted report.
- [ ] Confirm both partners have repository write access.
- [ ] Write DEL02.1 report sections 1–5 linked to actual outputs and the source code repository.
- [ ] Both partners make genuine and attributable contributions; document responsibilities under report sections 1–5.
- [ ] Review and disclose AI assistance in each student's Accountability Record.
- [ ] Verify the README instructions work from a clean checkout.
- [ ] Create annotated tag `DEL02` with message `DEL02.2 - Submission - Initial Computational Prototype`.
- [ ] Create GitHub release `DEL02 Release` based on that tag, documenting how to run the model and known limitations.
- [ ] Submit the shared DEL02.1 report, DEL02.2 release URL, and two individual Accountability Records.

## Tag command after final verification
```bash
git tag -a DEL02 -m "DEL02.2 - Submission - Initial Computational Prototype"
git push origin DEL02
```

The current repository is a **development prototype**, not a final DEL02 submission.
