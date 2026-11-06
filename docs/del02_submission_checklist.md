# DEL02 submission checklist

- [ ] Verify the GitHub Actions Mesa test and comparison job succeeds.
- [ ] Install dependencies locally using `setup.ps1` (Windows) or `bash setup.sh` (macOS/Linux).
- [ ] Retrieve the complete unchanged upstream Mesa example with `python scripts/fetch_source_example.py`.
- [ ] Confirm the original example can run according to its own instructions.
- [ ] Confirm `src/mesa_source/SOURCE.md` contains the actual fetched commit, retrieval date, path, and license reference.
- [ ] Commit the source example, attribution, and generated output files to GitHub.
- [ ] Review `outputs/` plots and CSVs, and report observed—not invented—numbers.
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
