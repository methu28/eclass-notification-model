# E10: DEL03 computationally derived evidence

- Record prepared/inspected: 2026-11-22; no execution/publication date is inferred from artifact timestamps.
- Status: computationally derived from E6 under E7; present locally and not yet committed/published as DEL03.
- Results account: [docs/del03_results.md](../../del03_results.md).
- Canonical artifacts: [outputs/del03/](../../../outputs/del03/); 18 result files.
- Metadata: [run_metadata.json](../../../outputs/del03/run_metadata.json).
- Saved metadata `input_sha256`: `4ca083de76bc24d5bc6a69bfe3647ca88f1652c721c18deaf46d560d21df219d`; historical CRLF execution-input bytes, as distinguished in E6.
- LF repository-input SHA-256: `bf93f1889d199348d529197e2d5dda0d413fef321c81bcafc619f22aa24f1f2e`; not substituted into the saved run record.
- Citation: (*DEL03: Reserved urgent position comparison*, n.d.).

There are four conditions, seven snapshots each, and 140 agent-state rows per condition (560 total). Urgent visibility is 0/1/2/3; initial recent nonurgent cohort visibility is 5/4/3/2 in recency/hybrid-1/hybrid-2/hybrid-3. These findings are model outputs, not field observations. Prefer reporting detailed findings in dossier section 4; this record establishes their origin and limits.

The table preserves the original Windows fingerprints and adds SHA-256 fingerprints of the exact content Git would store. Twelve text artifacts differ only in CRLF/LF line endings; six PNGs are byte-identical. The metadata file itself has both fingerprints, while its JSON `input_sha256` value continues to describe the input consumed during execution. No metadata or saved output bytes were edited. Verify published/raw content using the repository column; Windows checkouts may match the historical column. See [file-integrity conventions and commands](../file_integrity.md).

Snapshot means include step 0 and are not independent replications or continuous-time averages. The metadata documents 72-hour urgency, five visible positions, six six-hour steps, and one unchanged input dataset. No student response was measured.

| Existing file | Historical Windows artifact SHA-256 | Repository-content SHA-256 (LF text; unchanged PNG bytes) |
|---|---|---|
| `outputs/del03/comparison_processed_average_urgent_rank.png` | `52cfa402e36e0ac76441d93dd09ae995dde8b02bbf986c1970269c9a0e39f73e` | `52cfa402e36e0ac76441d93dd09ae995dde8b02bbf986c1970269c9a0e39f73e` |
| `outputs/del03/comparison_processed_initial_recent_nonurgent_top5.png` | `a3c50b4938ac922dc7705a5427baf13b822d9832b063b13e0f0437fb66bea75b` | `a3c50b4938ac922dc7705a5427baf13b822d9832b063b13e0f0437fb66bea75b` |
| `outputs/del03/comparison_processed_metrics_wide.csv` | `d10b4f57b704a197693c7ed551c1cf7c53f03cc41afd30ee8b0078406bff5e41` | `971d81b227ea2b328e20568300822d72d74000173539771d1ce74362cbe16367` |
| `outputs/del03/comparison_processed_overview.png` | `e26425b9a0277fbc016ea18fe89d951d4a3b04b04a48cb1ac952220ce114f185` | `e26425b9a0277fbc016ea18fe89d951d4a3b04b04a48cb1ac952220ce114f185` |
| `outputs/del03/comparison_processed_recent_nonurgent_top5.png` | `03e0e2421df025e0770b48575ba22de0b339df512c65dc90e32eaf32f154cc1d` | `03e0e2421df025e0770b48575ba22de0b339df512c65dc90e32eaf32f154cc1d` |
| `outputs/del03/comparison_processed_summary.csv` | `45f1198571e41b9715d1115f088345fa106f3c3d52ac3a0977c9b9da3a3b9bac` | `074bdf9715c29f697e3ab90056ef29d37562c08e44358c466968b890ea26c54a` |
| `outputs/del03/comparison_processed_urgent_top5_count.png` | `d35a31b079ca9a9a6a2c8c6fd98506201112d7c84b17ccc13042109290327b0b` | `d35a31b079ca9a9a6a2c8c6fd98506201112d7c84b17ccc13042109290327b0b` |
| `outputs/del03/comparison_processed_urgent_top5_share.png` | `1158f49b079108312b9fa03c3b95fe7173d0109dda1c1b628018333c7737fa80` | `1158f49b079108312b9fa03c3b95fe7173d0109dda1c1b628018333c7737fa80` |
| `outputs/del03/comparison_raw_model_metrics.csv` | `44062d7cbadd7f01c2d8fd5bae06c620bd25fcaac84546acd4759183e1327050` | `f1b382106c539e43a5fe6c70b15961e7899cffaf140eb5f90f45a7d2e12926ad` |
| `outputs/del03/hybrid_1_raw_agent_states.csv` | `9c1b3ef785c2bab769d44e04976100c01201c64056b6c14301d869fce7ff6116` | `c8b981a33f35719db9e44e5a4dc00ec295bef1aea544a7833bf358e6dae274b4` |
| `outputs/del03/hybrid_1_raw_model.csv` | `6fe425d95fa743a40bda6a152c6cd14088f1cf0bc2bf5c43debae0ef92664b14` | `2f813c8eae532733fc57dff78400879d7f94bc62980aa8a12b9c7703a9057060` |
| `outputs/del03/hybrid_2_raw_agent_states.csv` | `2923aa3e84f0be6f9ebc5e52f139430403e47a2edde953a355867073c142e205` | `7a7e295becd73f0d35c23691097e798ec778c18b42e713641e0e61b965694e7e` |
| `outputs/del03/hybrid_2_raw_model.csv` | `70bf9eee01ef897ae2a00c16f203ec0bb11b0969027010413f2d8eecd39bd0ab` | `4e5c6f76e62d90f726a43b63d7991f6afe97050b497a2b751250118c291ce5b8` |
| `outputs/del03/hybrid_3_raw_agent_states.csv` | `78a31ac09a9ae199d2a6667377beef4774b2ae885b25d1014b621693876a4c55` | `1bae87ae58640f3507afc1394028e138edb8d4bc046ae8a8930c9cc03b9a5d05` |
| `outputs/del03/hybrid_3_raw_model.csv` | `d835d49d491b5bacd99252a6d20c61ca8919e3c3978e7d34ee53a9ca8fcb918b` | `8d668aea31c00b9d01f3bf1d138efd1823795b8aa1bbbab738f8aeb5e8d4db97` |
| `outputs/del03/recency_raw_agent_states.csv` | `35c1bb29f472a4167f9f0cea288e293f0d5e75dc34be48bcfee98ebcc65e4a13` | `9417dada54cc90f52979b4b87a39b250417477cc38110e486c567f28f0c505b3` |
| `outputs/del03/recency_raw_model.csv` | `e9bd1ad78c451c46af31425e13947169842331f8a624422b27519c4254d7efaf` | `b4c1c9eaf8b428cbee63fc28125d967a2c2f4f9e403eae1998f924a5f4350bb6` |
| `outputs/del03/run_metadata.json` | `0bfdf6de52244b55864564f0baf3c501621310a6afe0ce52b70a353cafbe30e3` | `559044088c02d326ab342ab2f76880604e355d70730136c36222e0f55db96132` |

Dossier comparison roles: recency versus hybrid-2 is primary; hybrid-1 and hybrid-3 are sensitivity conditions. This interpretive designation does not alter any run, parameter or saved result.
