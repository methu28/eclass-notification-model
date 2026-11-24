# DEL03 section 2 evidence package

Prepared 2026-11-22; status updated 2026-11-23 using the actual local EECS 4461 F26 DEL03.1 specification. Its identity, page/section mapping and fingerprint are recorded in [E12_del03_specification.md](records/E12_del03_specification.md). The evidence inventory, representation ledger, assumptions, E1–E13 records, privacy-safe E5 registration and ecosystem map are prepared and incorporated in the [final dossier draft](../del03_final_dossier_draft.md). Existing model code, DEL02 materials and DEL03 results are preserved. DEL03 publication remains pending.

## Dossier assembly crosswalk

| Dossier section | Saved package file | Review status |
|---|---|---|
| 2.1.1 Reference list and saved inputs | [references.md](references.md); [records/](records/) | Source details checked; E5 public redaction inspected; capture metadata and internal authorship review remain |
| 2.1.2 Four-column evidence inventory | [inventory.md](inventory.md) | Prepared and incorporated; exact specification headings |
| 2.2.1 One/two-sentence overview | Opening of [representation_ledger.md](representation_ledger.md) | Incorporated in dossier §2.2.1 |
| 2.2.2 Four-column representation ledger | [representation_ledger.md](representation_ledger.md) | Prepared and incorporated; exact specification headings |
| 2.2.3 Choices, reasons and status | [modelling_assumptions.md](modelling_assumptions.md) | Choices, rationales and statuses incorporated in dossier §2.2.3 |
| 2.3 Evidence-linked map | [SVG](../figures/eclass_ecosystem_map.svg), [PNG](../figures/eclass_ecosystem_map.png), [caption](../figures/eclass_ecosystem_map_caption.md); [plan](ecosystem_map_plan.md) | Completed; PNG and caption incorporated in dossier §2.3; editable source and plan retained |

The dossier names the saved evidence records. E-labels supplement, rather than replace, author-date citations. The records distinguish supported context from assumptions and measurements; not all E-items are empirical evidence about the platform.

## Stable identifiers

| ID | Record | Kind |
|---|---|---|
| E1 | [E1_york_context.md](records/E1_york_context.md) | Documented institutional context |
| E2 | [E2_york_notification_preferences.md](records/E2_york_notification_preferences.md) | Documented delivery preferences |
| E3 | [E3_york_forum_governance.md](records/E3_york_forum_governance.md) | Documented subscription governance |
| E4 | [E4_moodle_notifications.md](records/E4_moodle_notifications.md) | Documented upstream reference |
| E5 | [E5_observed_del01_screenshot.md](records/E5_observed_del01_screenshot.md) | Observed redacted DEL01 crop; exact capture date unconfirmed |
| E13 | [E13_del01_inquiry_plan.md](records/E13_del01_inquiry_plan.md) | Earlier proposed ordering definitions and scope |
| E6 | [E6_synthetic_dataset.md](records/E6_synthetic_dataset.md) | Synthetic input record and canonical data hash |
| E7 | [E7_synthetic_rules.md](records/E7_synthetic_rules.md) | Synthetic rules/assumptions record |
| E8 | [E8_mesa_provenance.md](records/E8_mesa_provenance.md) | Technical provenance |
| E9 | [E9_del02_snapshot.md](records/E9_del02_snapshot.md) | Preserved computational snapshot |
| E10 | [E10_del03_computational_outputs.md](records/E10_del03_computational_outputs.md) | Computationally derived outputs |
| E11 | [E11_implementation_verification.md](records/E11_implementation_verification.md) | Prior implementation verification |
| E12 | [E12_del03_specification.md](records/E12_del03_specification.md) | Course requirement record |

## Status conventions

- Observed: directly inspected real-world interface evidence; E5 is the supplied DEL01 crop, with user-reported provenance and unconfirmed exact capture date.
- Documented: stated by an identifiable source; upstream claims are not automatically York-specific.
- Inferred: qualified interpretive connection; not an observation.
- Synthetic: constructed dataset, condition, parameter or representation choice.
- Computationally derived: result of executing the synthetic representation, not field data.
- Pending/unverified: a specific fact remains unavailable/not checked. E5 is present and inspected; its exact capture date, original viewport, and capture authorship remain unconfirmed.
- Illustrative: diagram symbols only, never a substitute screenshot.

The project's recency baseline, urgency classification, hybrid policies, 72-hour threshold, 24-hour recent window and five-position visibility boundary are synthetic operational choices. No reviewed source establishes them as York's actual algorithm or configuration. There is no separate urgency-only sorting condition.

## Manual inputs and remaining work

1. E5 is now registered as `DEL01_eClass_notification_dropdown_E5_public_redacted.png`. Confirm capture author/date/context if recoverable. Course-identifying content is now opaquely masked, and the unredacted original is private outside the repository. Do not infer a capture date from the October 2026 upload/work period.
2. Review provisional author-date references for team-created inputs; add verified names/dates if available. n.d. and title-first entries intentionally avoid invented details.
3. Retain the confirmed primary recency/hybrid-2 comparison, with hybrid-1 and hybrid-3 as sensitivity conditions, during final typesetting and submission.
4. When transferring the completed dossier to eClass, upload/embed the map PNG and comparison figure directly and preserve their captions. Repository-relative links need final published URLs or permitted attachments; see the [transfer checklist](../del03_dossier_quality_review.md#eclass-transfer-and-final-formatting).
5. Complete final team review and individual AI-assistance/accountability disclosures. Dossier assembly is complete; publication and eClass transfer remain separate steps.

## Verification boundary

External pages E1-E4 were rechecked on 2026-11-22, which is the source-note access date, not a retrospectively assigned DEL01 date. Record dates are separate from source creation/publication dates. Dataset/output fingerprints support traceability. Initial evidence-package preparation did not rerun the simulation; the subsequent pre-release audit passed all 18 tests and reproduced all 18 DEL03 artifacts byte-for-byte on the same Windows runtime. Existing saved results remain the authority for numerical findings, with E11 documenting implementation checks. [File-integrity conventions](file_integrity.md) distinguish historical runtime/Windows hashes from Git-normalized repository fingerprints; E6, E9 and E10 preserve both meanings. LF-input normalization-aware verification does not establish cross-platform byte-identical reproduction.

No commit, push, tag or release is authorized by this package. E12 describes final assignment requirements, not actions to execute now. Do not redistribute the locally supplied course PDFs or private unredacted screenshot. Only the registered public redacted E5 derivative belongs in the final public commit.
