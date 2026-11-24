# Section 2.3: Evidence-linked ecosystem map design record

This design record informed the completed [SVG](../figures/eclass_ecosystem_map.svg), [PNG](../figures/eclass_ecosystem_map.png), and [caption](../figures/eclass_ecosystem_map_caption.md). E5 was updated on 2026-11-23 after direct inspection of the public redacted DEL01 crop; no interface image was fabricated or substituted. The actual specification (page 3) requires a final labelled figure exported to docs/figures/ as PNG or SVG, embedded in the dossier with a caption and evidence identifiers; preserve editable source if practical. The figure files are present; they still need embedding in the final dossier.

## Focus and layout

Arrangement: course-information notification delivery and limited initial list visibility for a York eClass student. Avoid mapping the whole university or every LMS function. Use an outer context layer and a clearly highlighted inset labelled "Synthetic computational representation (E6-E7)". Status words must appear on nodes/edges, not only as colors.

## Proposed nodes

| Node | Role / proposed label | Evidence and status | Computational inclusion |
|---|---|---|---|
| Course staff and course activities | Originate course information/events | E1/E4 documented setting; particular workflow inferred | Outside; inputs stand in for notifications |
| Students | Recipients/users of information | E1/E4 documented role | Outside as actors; no student agents |
| York institutional support | UIT/LTS service context | E1-E3 documented | Outside; do not assign unverified control over ordering |
| eClass/Moodle notification processing | Event-to-notification context | E1/E4 documented at stated scope | Outside; generation/eligibility not simulated |
| Preferences/subscription controls | Delivery governance surrounding the list | E2-E3 documented York context; E4 upstream context | Outside |
| Web notification interface | Visible York dropdown, links and scrollbar | E5 observed public redacted DEL01 crop; E4 upstream context | Interface referent only; no actual algorithm or universal viewport inferred |
| Actual York ordering/filtering | Label "not established in this inquiry" | Unverified; no source proves it | Outside; not replaced silently by the baseline |
| Email/mobile routes | Surrounding channels | E2 documented email context; E4 upstream channels, deployment-dependent | Outside focal display investigation |
| Synthetic records and clock | 20 records, fixed deadlines, six-hour updates | E6-E7 synthetic | Inside |
| Experimental ranking policy | Recency or hybrid K=1,2,3 | E7 synthetic | Inside; policy-comparison input |
| Rank/visibility measurement | First five, urgent coverage/rank, nonurgent visibility | E7 synthetic definitions | Inside; outputs E10 |
| Attention, reading and educational consequences | Possible subsequent processes, not measured | Inferred/unobserved; no causal claim | Explicitly outside |
| Project team | Selects assumptions and policy conditions | E6-E7 project design | Design authority annotation, not a simulated agent |

## Proposed directed flows

1. Course activity/information -> notification processing: contextual event flow (E1/E4; specific pipeline inferred).
2. Preferences/subscriptions -> delivery eligibility: contextual governance (E2-E4), not rank priority.
3. Processing -> web interface and surrounding channels: documented at each source's scope (E2/E4); do not assert all channels are enabled at York.
4. Web interface -> opportunity to encounter information: inferred relationship, not measured attention.
5. Opportunity -> possible reading/action: outside the model, inferred/unverified, never drawn as a measured outcome.
6. In the inset only: E6 input -> time/urgency update -> E7 experimental policy -> assigned ranks -> first-five metrics -> E10 output evidence. These are synthetic/computational arrows, not an actual eClass pipeline.

Draw an explicit abstraction link from the contextual interface to the inset, labelled "selective representation; hypothetical policies". Do not draw recency/hybrid as the deployed real-world ordering node. E8 can appear as a technical-provenance note; E9/E11 support version/verification captions, not real-world actor flows. E12 governs the figure requirements, not the phenomenon.

## Evidence/status legend

- Documented: cite E1-E4 and distinguish York documentation from generic upstream behavior.
- Observed: E5 public redacted DEL01 crop, inspected directly; exact capture date unconfirmed.
- Inferred: use dashed relationships with the word inferred.
- Synthetic: visibly boxed input/rule assumptions E6-E7.
- Computationally derived: measurements/results E10; not empirical student observations.
- Unverified: actual York ordering, universal viewport capacity, and E5 capture metadata remain unconfirmed; the image itself is present.

Use text, shapes and line styles as well as color. A stylized node is an illustrative map symbol, not an authentic interface image. The inspected public redacted derivative is registered as E5; map symbols do not reproduce or replace it.

## Caption linkage

Figure 1. Ecosystem map of course-notification visibility in York eClass. E1-E4 support the documented institutional and notification context. The highlighted inset represents the synthetic input and hypothetical ordering comparison (E6-E7), with computational outputs recorded as E10. The inspected cropped DEL01 capture (E5) supports visible interface elements; its exact capture date, actual York ordering and student attention remain unverified. Preferences, delivery channels, and human outcomes lie outside the computational representation.

Use the saved caption alongside `docs/figures/eclass_ecosystem_map.svg` or `docs/figures/eclass_ecosystem_map.png`. E5 uses the actual filename `DEL01_eClass_notification_dropdown_E5_public_redacted.png`; no capture date is assigned from notification dates or the reported upload month.

## Remaining manual decisions

Keep recency/hybrid-2 as the main comparison and hybrid-1/3 as sensitivity checks; review the public redacted E5 derivative, add capture metadata only if independently established, and embed the existing reviewed figure in the dossier. The original crop is preserved unchanged privately outside the repository; the public derivative has disclosed opaque masks.
