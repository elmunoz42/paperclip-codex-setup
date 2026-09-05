# SPA-12 independent QA — E2

**Status: revised draft suitable for Carlos review, with the evidence limits below. Not publication approval.**

Reviewer: Codex collaborator, independently checking the producer’s source records under the user’s instruction to continue the spec. Review date: 2026-09-05. Input: live Paperclip revision 1, matched to repository commit `b158edc`; output: repository revision 2. This is not a claim that the Paperclip Chief of Staff has accepted its pending interaction.

## Findings and dispositions

| ID | Finding in original | Revision 2 treatment |
| --- | --- | --- |
| QA-01 | C-04 publication date was July 19, 2023. JPL author bibliography lists July 26. | Corrected to July 26; added title, author-bibliography verification, and access limit. |
| QA-02 | C-05 gave March 4 as a publication date, conflating conference timing with publication. | Uses 2023 and JPL’s March 7 conference listing; exact online-publication date explicitly unverified. |
| QA-03 | C-07 asserted January 30 as publication date, but the retrieved vendor article displays no publication date. | Marked not displayed; retained access date. |
| QA-04 | C-04 could suggest OBP was already operational when the 2023 paper appeared. | Ledger states it was then planned for operational use; removed the broad paper summary from narration. |
| QA-05 | “Current” ENav wording and a historical percentage were unnecessary to the pilot argument. | Removed the percentage and current-state wording from narration; preserved qualified background record. |
| QA-06 | Planning-time benefit estimate added vendor framing without a comparative study in the reviewed releases. | Removed numeric estimate from narration; retained the evidence gap in notes. |
| QA-07 | The claimed 945 words included cues rather than spoken-only text. | Original narration was 834 whitespace-delimited words after stripping bracketed cues. Revised count is documented in the package using the same method. |
| QA-08 | Review instructions and technical caveats interrupted spoken flow. | Source cues remain in the annotated package; clean narration and consolidated choices appear in the review packet. |

## Source-by-source verification

Access date for all checks: **2026-09-05**. Titles and original publishers identify the seven sources; auxiliary author records verify metadata and are not counted as extra sources.

| Claim record / source | Evidence inspected | Scope and result |
| --- | --- | --- |
| C-01 — NASA/JPL, [NASA’s Perseverance Rover Completes First AI-Planned Drive on Mars](https://www.jpl.nasa.gov/news/nasas-perseverance-rover-completes-first-ai-planned-drive-on-mars/), Jan. 30, 2026 | Full release: demonstration description; “Progress for Mars, beyond”; drive-distance paragraph. | Supports dates, distances, vision-language inputs, waypoint output, Claude identity, and digital-twin checks. Does not establish independent command authority or comparative safety. |
| C-02 — NASA/JPL, [NASA’s Self-Driving Perseverance Mars Rover ‘Takes the Wheel’](https://www.jpl.nasa.gov/news/nasas-self-driving-perseverance-mars-rover-takes-the-wheel/), July 1, 2021 | Full release: AutoNav description and “The Human Element.” | Supports camera-based 3D mapping, hazard avoidance, and ground planning/sign-off/uplink. Historical context; not a complete record of the 2025 demonstration. |
| C-03 — NASA/JPL, [Autonomous Systems Help NASA’s Perseverance Do More Science on Mars](https://www.jpl.nasa.gov/news/autonomous-systems-help-nasas-perseverance-do-more-science-on-mars/), Sept. 21, 2023 | Mission release opening and Snowdrift Peak traverse paragraph. | Supports human general-route planning and local AutoNav detours around rocks absent from orbital imagery. No generalized speed advantage asserted. |
| C-04 — Verma et al., [Autonomous robotics is driving Perseverance rover’s progress on Mars](https://doi.org/10.1126/scirobotics.adi3099), Science Robotics 8(80), July 26, 2023 | [JPL coauthor bibliography](https://www-robotics.jpl.nasa.gov/who-we-are/people/michael_mchenry/) and the paper’s indexed abstract in [PubMed](https://pubmed.ncbi.nlm.nih.gov/37494463/). Publisher full text returned 403; PubMed direct reader did not expose text, so abstract check used its indexed record. | Identity/date and the limited AutoNav/AEGIS/then-planned-OBP summary checked. Not a full-paper review. Removed from narrated technical evidence. |
| C-05 — Rankin et al., [Perseverance Rapid Traverse Campaign](https://doi.org/10.1109/AERO55745.2023.10115835), 2023 IEEE Aerospace Conference | [JPL author bibliography](https://www-robotics.jpl.nasa.gov/who-we-are/people/tyler_del-sesto/) and indexed text from [JPL-hosted paper](https://robotics.jpl.nasa.gov/media/documents/2023-rapid-traverse.pdf), section 7, p. 7. | Supports directed-drive start, intermediate waypoints, and real-time AutoNav avoidance. JPL lists March 7; online-publication date not established. Full PDF exceeded web-reader size; relevant primary-source passage was inspected through its indexed text. |
| C-06 — Toupet et al., [Enhanced Autonomous Navigation on the Perseverance Mars Rover](https://doi.org/10.1109/TFR.2025.3636366), IEEE Transactions on Field Robotics, Nov. 24, 2025 | [IEEE-indexed abstract and metadata](https://ieeexplore.ieee.org/document/11265757), plus [JPL author bibliography](https://www-robotics.jpl.nasa.gov/who-we-are/people/michael_mchenry/). Direct IEEE page requires JavaScript verification. | Indexed abstract supports the dated 90% / 32.1 km figure through Oct. 28, 2024; author record corroborates date. Full text not reviewed; statistic removed from narration. |
| C-07 — Anthropic, [Claude AI Powers NASA’s First AI-Planned Mars Rover Drive](https://www.anthropic.com/features/claude-on-mars), publication date not displayed | Full article: waypoint workflow, simulation, engineer review, route adjustment, and estimated benefit. | Ten-meter segments and minor edits are vendor-attributed details. Claude identity also has independent JPL attribution. No independently validated savings claim retained. |

## Material-claim coverage

- Topic brief, ledger and outline: C-01 supplies demonstration details; C-02/C-03 supply historical onboard context; C-05 supplies the driving-mode distinction. C-08 labels interpretation, and C-09 labels the comparative-evidence gap.
- Spoken paragraph cues preserve the mapping for dates/distances, waypoints, terrain inputs, engineering checks, ground actions, AutoNav, Snowdrift Peak, and directed/Autonav drive modes. Analogies and conclusions are labeled analysis in the annotated package.
- Both companion outlines reuse those claims. The notebook remains a proposal using a synthetic grid and A*, explicitly not generative AI or rover flight software.
- No new mission-performance claim or quotation was introduced. The absence of a comparative study in these checked releases is not a claim that no such study exists anywhere.

## Remaining limits

Carlos must decide tone and companion format. Exact C-05 online-publication date and C-07 publication date remain unverified rather than guessed. Full scholarly texts were not all accessible; narration avoids relying on inaccessible detail. The diagram is conceptual and does not claim to document every flight-software interface. Any later production assets require their own review.

## Review outcome

E2 is complete as a claim check with corrections and explicit unresolved items. E3 incorporates those corrections. E4 editorial acceptance and E5 feedback capture remain open. [Read the consolidated packet](SPA-12-review.md).
