# Validation status

The initial local build environment lacked the genuine Mesa package and internet access for installing it. The project source compiled, and eight independent ordering/dataset tests passed there. An internal test substitute exercised the output-generation flow, but **that is not equivalent to successful execution with real Mesa**.

**GitHub Actions** now provides an independent workflow that installs the actual dependencies, runs pytest, executes the comparison and uploads output artifacts. Inspect the latest workflow run on GitHub; this document does not assert its result in advance.

Submission blockers until verified:
1. GitHub Actions genuine Mesa tests and comparison succeed, with no skipped integration tests.
2. Obtain, preserve, attribute, and independently run the complete upstream Mesa example.
3. Download and review the workflow outputs, then commit real generated files into `outputs/`.
4. Re-run setup from a clean checkout, document installation versions and any fixes.
5. Have both partners review and understand the code and record accurate contributions.
6. Create the annotated DEL02 tag and release only from the fully verified commit.
