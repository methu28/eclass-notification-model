# File-integrity fingerprints and reproducibility

Provenance clarification checked on 2026-11-23. This record distinguishes bytes from values without changing the dataset, simulation, saved outputs, metadata, Git configuration or DEL02 snapshot.

## What the fingerprints describe

| Record or field | Meaning and verification scope |
|---|---|
| E6 historical Windows input SHA-256 | Actual CRLF bytes consumed by the saved DEL03 execution; preserved as `input_sha256` in its metadata |
| E6 repository-content SHA-256 | Exact LF input content Git stores; also verified against the dataset at DEL02; not a retroactive execution fingerprint |
| E10 historical Windows artifact column | Exact bytes of the 18 saved local artifacts, including metadata; all 18 reproduced byte-for-byte in the same Windows environment |
| E10 repository-content column | SHA-256 of exact Git-clean-filtered content for the final candidates: 11 LF CSVs, LF JSON metadata and six unchanged PNGs |
| E9 Windows checkout column | Inspected local DEL02 checkout bytes, not independently established original execution bytes |
| E9 published DEL02 column | SHA-256 of `git show DEL02:<path>` content, unchanged in the current repository |
| E5 screenshot hashes | Binary PNG bytes; public derivative and private original have distinct fingerprints; no newline normalization applies |
| E12/E13 PDF hashes | Bytes of locally supplied course/DEL01 PDFs; these PDFs are not distributed in the repository |
| Git commit/tag identifiers | Git object identifiers for version provenance; these are not the SHA-256 content fingerprints used in the integrity tables |

Git's existing `core.autocrlf` handling removes CR bytes from CRLF text on storage and may restore CRLF on Windows checkout. Comparing each Windows file with its prospective repository content confirmed that every identified byte difference was exactly CRLF → LF. Input values, CSV fields, JSON values, UTF-8 readability and all PNGs are unchanged. No `.gitattributes` change is needed.

## Saved metadata semantics

`outputs/del03/run_metadata.json` remains the unedited historical run record. Its `input_sha256` is SHA-256 of `args.input.read_bytes()` during that run. Git normalizes the JSON file's newlines without changing this value. Thus an LF repository input does not have to match that historical CRLF runtime hash. E6 and E10 supply the repository hash separately; no schema or simulation change is necessary.

A new run reading LF input correctly records the LF input hash instead. Replacing that value solely to match an earlier run would falsify provenance. The metadata file's own SHA-256 is a separate quantity, listed in E10; it is not its `input_sha256` value.

## Verify the published version

Use the repository-content column for a raw repository file or an LF archive file. A Windows checkout can instead match the Windows column. For text files, hashing after replacing only CRLF with LF is a normalization-aware comparison with repository content; for PNGs, hash the original bytes. Do not alter fields, whitespace, encodings or numerical formatting.

The following portable Python example hashes raw Git content after the final commit. `HEAD` must identify the intended final version; use its verified full commit SHA when auditing a specific version. For preserved outputs, set `ref = "DEL02"` and select their original paths. These commands compute SHA-256 of returned file bytes, not Git's object identifier.

```python
import hashlib
import subprocess

ref = "HEAD"  # Use only after the final materials have been committed.
paths = ["data/notifications.csv", "outputs/del03/recency_raw_model.csv",
         "outputs/del03/run_metadata.json"]
for path in paths:
    content = subprocess.check_output(["git", "show", f"{ref}:{path}"])
    print(path, hashlib.sha256(content).hexdigest())
```

Without Git, use `Path(path).read_bytes()` and `hashlib.sha256(content).hexdigest()` for raw file bytes. For the repository-normalized comparison of CSV/JSON text only, hash `content.replace(b"\r\n", b"\n")`. A metadata file from a new execution is a new artifact: its runtime input fingerprint may legitimately differ even after newline normalization.

## Checks actually performed

- Recomputed both columns for the dataset, all 18 DEL03 artifacts and all nine DEL02 artifacts (28 files). Prospective repository bytes were read through an isolated Git index using existing clean-filter rules; the real staging index was not changed. DEL02 values were additionally checked against its tagged blobs.
- A fresh Windows CRLF-input execution reproduced all 18 saved artifacts byte-for-byte in the existing recorded dependency environment.
- Materialized LF Git content in an ignored checkout and executed the four conditions with that LF input on the same Windows runtime. All input records were equal; all 11 output CSVs matched the repository versions after CRLF/LF normalization, and all six PNGs matched byte-for-byte. Metadata differed from the saved record only in the correct runtime `input_sha256` for LF input.
- The full automated suite passed 18 tests, with no skips and 10 existing Mesa seed-deprecation warnings. Numerical results and experimental conditions remain unchanged.

This is a normalization-aware Windows check, not a Linux/macOS execution test. Cross-platform byte-identical rendering, exports or metadata reproduction has not been established. The earlier exact-reproduction statements in the results and verification records refer to same-environment Windows runs. The historical DEL02 verification account in `docs/validation_status.md` likewise describes its local runs, not universal cross-platform byte equality.

Records: [dataset E6](records/E6_synthetic_dataset.md), [DEL02 E9](records/E9_del02_snapshot.md), [DEL03 E10](records/E10_del03_computational_outputs.md), [implementation E11](records/E11_implementation_verification.md).
