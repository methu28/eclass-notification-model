# DEL03.1 dossier quality review

Reviewed locally on 2026-11-23 against the actual `05_Deliverable3.1 - Final Integrated Dossier Report.pdf`, especially sections 1.3/1.4 and the section-specific requirements. This is a documentation/evidence review, not a new experiment or a claim of final submission. The dossier remains a team-review draft.

## Section-by-section completeness and evaluation fit

| Required section | Assessment | Evidence and remaining condition |
|---|---|---|
| 1 Final inquiry, context and boundary | Addressed | Specific 20-record list-placement inquiry, actors, mechanism and claim boundary; scope narrowing is explicit. Joint development by Adejumobi and Methunan Uthayakumar is identified; Adejumobi's preferred full submission name remains to confirm. |
| 2.1.1 Reference list | Addressed with bibliographic limits | Thirteen alphabetized source/input entries, consistent APA-style author–date citations and explicit published-source URLs; n.d./title-first where unknown; E5 capture date and personal authorship not invented. |
| 2.1.2 Evidence inventory | Addressed | Exact required four headings; observed, documented, inferred, synthetic and computational evidence distinguished. |
| 2.2.1 Overview | Addressed | Two sentences identify entities/process, primary/sensitivity conditions and omission. |
| 2.2.2 Representation ledger | Addressed | Exact required four headings; choices linked to E-records; actual York algorithm remains unknown. |
| 2.2.3 Assumptions | Addressed | Choices, analytical rationale and synthetic/evidence status explained; rationales require team endorsement. |
| 2.3 Ecosystem map | Addressed; final embedding must be retained | PNG embedded, SVG/caption linked; main alternative labelled hybrid-2, sensitivities 1/3; E5 is redacted observed evidence. |
| 3.1 Baseline and alternative | Addressed | Recency/hybrid-2 primary throughout; original urgency-class-first method accurately documented from DEL01 page 4 but explicitly unimplemented. |
| 3.2 Comparison setup | Addressed | Same input, threshold, clock, capacity, measures and changing urgent population stated. |
| 4.1 Outputs and reproducibility | Addressed with final-version follow-up | All 18 filenames, existing artifacts, fresh-directory command, dependency/README references and prior verification provided. Final submitted commit/CI remains to be checked after approval. |
| 4.2 Visible comparison | Addressed | Graph embedded; primary and sensitivity tables separated; all seven snapshots used; current vs initial-cohort nonurgent visibility distinguished. |
| 4.3 Outcome claim and boundary | Addressed | Separates computed result, mechanism investigated and claims not established for users/platform/populations. |
| 5 Consequences and trade-offs | Addressed | Connects changed ranking, mapped recipients/interface, actual output pattern, possible encounter consequence, displaced nonurgent information, nearest-deadline limitation and further evidence needs. |
| 6.1 Limits and claim effects | Addressed | Each material limitation explains what inference is restricted. |
| 6.2 Future work | Addressed | Specific robustness, mechanism and empirical checks; none is presented as completed. |
| 7 Repository and release | Partially complete by design | Actual repository and preserved DEL02 release identified. DEL03 tag/release URL/final commit are pending; do not submit the pending marker as a completed release. |

## Cross-section review

- Main comparison is recency versus hybrid-2 in the question, overview, setup, findings, interpretation and map. Hybrid-1/3 are sensitivity configurations, not the primary alternative.
- E6/E7 establish the synthetic representation; E10 supports numerical claims; E11 supports implementation checks; E1-E5 contextualize but do not validate ranking rules.
- Urgent coverage divides by all urgent items. Mean urgent rank uses all urgent items. Current nonurgent recency can age out; initial cohort membership stays fixed.
- The primary cohort difference is two at every snapshot, while the current recent difference is two, two, two, one, zero, zero, zero. The text does not conflate them.
- Closest-deadline example verified against final `hybrid_2_raw_agent_states.csv`: N01 rank 14/12 hours left; N05 rank 1/42; N06 rank 2/48.
- The draft defines the originally proposed urgency-only rule as urgent class first and recency within each class, not nearest-deadline sorting. It makes no urgency-only result claim.
- Supplied DEL01 grading feedback is accurately recorded: DEL01-4 was partially demonstrated because the three proposed methods were insufficiently explained. No other feedback or grade change is claimed. E13 records the actual earlier proposal and scope.
- The screenshot's October 2026 upload/work period is not assigned as capture date. Public masks/crop are disclosed; generic content and timestamps are preserved rather than generated.
- No statement identifies recency, hybrid reservations, 72-hour urgency or five positions as verified York behavior. No student reading, behavior, missed-deadline or learning improvement is claimed.

## Public screenshot treatment

The unredacted supplied crop was not tracked by Git and has been preserved byte-identically outside the repository in a private local E5 folder, together with its treatment log. Its former repository path is ignored. Only `docs/evidence/DEL01_eClass_notification_dropdown_E5_public_redacted.png` remains as a public image.

The derivative is a 477 x 790 RGB PNG. Solid masks irreversibly replace course identifiers, activity titles and absolute schedule details. All unmasked pixels were checked equal to the original crop. A visual inspection confirmed generic content-change/quiz labels, relative timestamps, links, bell/header controls, scrollbar and See all remain. No course title/code, personal identifier or embedded image metadata was found in this public derivative. The private-original location is not linked in public documentation.

## Remaining factual/citation and submission inputs

1. Joint project development by Adejumobi and Methunan Uthayakumar is confirmed. Confirm Adejumobi's preferred full submission name and any document-specific author/date attribution before final typesetting; do not infer individual contributions or extra name components.
2. Original screenshot capture date/photographer and full viewport remain unconfirmed; preserve the stated limits unless new reliable evidence is supplied.
3. The supplied DEL01-4 assessment is acknowledged and addressed through explicit method definitions. No further feedback, quotation or revised grade is invented.
4. The original proposal referenced a different Moodle documentation version than the current E4 record. E4 explicitly uses the inspected Moodle 4.5 reference; no York version is inferred.
5. Review screenshot publication permissions and the finished redacted file, and review the shared interpretations and AI-assisted drafting before submission.
6. After approval only: commit/push the complete public package, verify final CI, create the annotated DEL03 tag and DEL03 Release, then replace the pending field with its verified URL. Complete individual Accountability Records and the other separately required presentation/submission materials.

## Checks performed

All required sections/subsections and exact inventory/ledger headers were checked. Local Markdown links and embedded figures resolve; CSV-derived numerical tables and a final-agent-state example were checked. Map SVG text fits existing boxes; PNG retains 4320 x 3240 dimensions and was visually inspected. Existing model, tests, dataset, verified outputs, HEAD and DEL02 tag are unchanged. No tests or simulations were rerun because the change is documentation/privacy treatment only. The initial 18-test/10-warning result in the dossier is prior recorded verification. The subsequent provenance check reran the full suite successfully and distinguished same-Windows byte-identical reproduction from LF-normalized repository-content verification; see [integrity conventions](evidence/file_integrity.md). The runtime input hash remains unchanged in saved metadata, with separate repository SHA-256 fingerprints documented in E6/E9/E10.

## eClass transfer and final formatting

Relative repository links resolve locally/on GitHub but will not resolve automatically in an eClass database entry. Preserve the captions and evidence identifiers when transferring the text.

| Item in the dossier | Required transfer handling |
|---|---|
| Figure 1: `figures/eclass_ecosystem_map.png` | Upload/embed the actual PNG in §2.3; inspect its labels at the displayed size. Keep the SVG as a repository link, using the final version once published. |
| Figure 2: `../outputs/del03/comparison_processed_overview.png` | Upload/embed the actual PNG in §4.2; retain the primary/sensitivity caption. |
| E5: `evidence/DEL01_eClass_notification_dropdown_E5_public_redacted.png` | If included or linked separately, use only this public redacted image. Never upload the private unredacted source. |
| Evidence records, dataset, README, results report and editable SVG | Replace relative links with verified links to the final released repository version, or attach permitted files. Do not substitute links to unpublished local paths. |
| Course specification and DEL01 PDF filenames | These identify local inputs, not public hyperlinks. Keep honest bibliographic descriptions; do not fabricate URLs or redistribute restricted course material. |
| References and tables | Apply hanging indents if supported; retain italics, author–date suffixes, all E1–E13 labels, the two exact four-column headers, and readable table widths. |
| §7 DEL03 Release URL | Leave pending until publication; then insert the verified release URL. Existing absolute GitHub and documentation links can remain hyperlinks. |

The draft is substantively complete across §§1–6. Final submission still requires the published DEL03 release, final team review/formatting and the separate required submission materials. Unknown capture dates and document-specific authorship remain disclosed evidence limits rather than details to invent.
