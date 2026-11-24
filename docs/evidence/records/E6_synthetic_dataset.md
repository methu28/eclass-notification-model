# E6: Synthetic notification dataset

- Record prepared/inspected: 2026-11-22; dataset creation date and full personal authorship not established here.
- Status: synthetic project input, not observed eClass records.
- Canonical file: [data/notifications.csv](../../../data/notifications.csv).
- Historical Windows execution-input SHA-256 (CRLF): `4ca083de76bc24d5bc6a69bfe3647ca88f1652c721c18deaf46d560d21df219d`. These are the actual bytes consumed by the saved DEL03 run.
- Repository-content SHA-256 (LF): `bf93f1889d199348d529197e2d5dda0d413fef321c81bcafc619f22aa24f1f2e`. Use this to verify raw repository content; it also matches the unchanged dataset blob at `DEL02`.
- The difference is exclusively CRLF versus LF; all 20 records and values are identical. `outputs/del03/run_metadata.json` retains the historical runtime hash rather than substituting a repository hash. See [file-integrity conventions](../file_integrity.md) for checkout-aware verification and the meaning of each fingerprint.
- Provisional author-date citation: (*Synthetic notification dataset*, n.d.). See [references](../references.md).

## Construction and model role

The CSV supplies 20 fictional records with ID, category, posting age in hours, and optional remaining deadline in hours. Eight have deadlines and twelve do not. Four are initially urgent at 72 hours; four more enter the urgent class during the 36-hour run. All conditions reuse the same records.

The distribution places newer nonurgent items ahead of older urgent items under recency, making the reservation trade-off inspectable. This is a description of the constructed contrast, not a measured distribution or a claim about the team's historical motives. There are no student identities or observed behavioral records. IDs are synthetic keys; categories are not asserted to map exactly to actual bell-notification types.

## Saved input record

This table transcribes the canonical CSV; it does not replace or modify it.

| ID | Synthetic category | Initial posting age (hours) | Initial deadline remaining (hours) |
|---|---|---:|---:|
| N01 | assignment_reminder | 48 | 48 |
| N02 | quiz_reminder | 60 | 54 |
| N03 | assignment_reminder | 72 | 60 |
| N04 | quiz_reminder | 96 | 66 |
| N05 | assignment_update | 36 | 78 |
| N06 | quiz_update | 42 | 84 |
| N07 | assignment_update | 50 | 90 |
| N08 | quiz_update | 54 | 96 |
| N09 | course_announcement | 1 | None |
| N10 | course_announcement | 2 | None |
| N11 | course_material | 4 | None |
| N12 | course_announcement | 6 | None |
| N13 | course_material | 9 | None |
| N14 | course_announcement | 12 | None |
| N15 | course_material | 16 | None |
| N16 | course_announcement | 20 | None |
| N17 | course_material | 25 | None |
| N18 | course_announcement | 30 | None |
| N19 | course_material | 40 | None |
| N20 | course_announcement | 65 | None |

## Limits and manual review

One intentionally constructed dataset cannot estimate real notification prevalence or student experience. Twelve missing deadlines mean absence of deadline metadata in this synthetic input, not evidence of unimportance. Confirm team authorship and creation history before adding names/dates to the final reference. Do not assign a publication date from filesystem timestamps.
