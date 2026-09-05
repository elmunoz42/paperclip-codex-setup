# Proposal 003 — Technical content agent responsibilities

**Status:** proposed September 5, 2026; not installed or sent to agents. Carlos requested review and proposals for Content Strategist and Content Creator.

## Review findings

Reviewed the repository's [content engine](../docs/content-engine.md), [existing task briefs](prompts/implementation.md), and [role additions](prompts/role-additions.md). This is a review of saved guidance, not an audit of current runtime system prompts or agent performance.

The saved Strategist remit favors breadth across many content pillars. It needs a stronger selection rule for the new ML-technical audience. The workflow also allows a companion outline to count as the final deliverable; the new technical lesson needs a working experiment and validation evidence.

The saved roster calls the production role **Research & Editorial Producer**, while Carlos now calls it **Content Creator**. Chief of Staff should verify which existing agent fills that role and use it. This proposal does not create a fourth agent or assume a runtime rename. If the roles are separate, assign one accountable creator and one research contributor per artifact to prevent duplicate drafts.

## Proposed responsibility split

| Role | Owns | Handoff |
| --- | --- | --- |
| Content Strategist | Learning question, audience prerequisites, episode sequence, source feasibility, scope and success criteria | A decision-ready brief to Carlos through Chief of Staff |
| Content Creator | Source-backed explanation, script, visual sequence, companion narrative, artifact integration | One coherent draft package with reproducible demonstration evidence |
| Designated implementer | Notebook or interactive code and correctness checks | Tested artifact and technical limitations to Creator |
| Chief of Staff | Assignment mapping, dependencies, independent QA and consolidated review | One accept/revise/reject request to Carlos |

The Creator can also implement if qualified and assigned; a separate new role is not required. Creator self-checking does not replace Chief of Staff independent QA. Carlos remains presenter and final editor.

## Content Strategist proposal

Optimize for a question a viewer can answer and an experiment they can change. Recommend one principal algorithm or mathematical mechanism per episode. Identify why that knowledge transfers to an ML practitioner's work without relabeling all controls or robotics as ML.

Each brief contains: audience and prerequisites; one-sentence learning promise; primary-source pointers and evidence gaps; actual mission component and execution location; proposed equation with assumptions; executable experiment; expected result and failure case; format; implementation dependencies; explicit exclusions; and Carlos's decision.

Use a transparent comparison with 0–2 points each for primary evidence, mathematical depth, executable experiment, audience relevance, and bounded implementation effort. Explain every score; this is editorial judgment, not measured audience demand. Unresolved source feasibility blocks a mission-specific claim regardless of total score. Do not invent estimated views, timelines, or agent capacity.

Initial sequence: Perseverance uncertainty/path planning first; Apollo source-to-calculation feasibility second; thermal scheduling as a later candidate. Preserve the existing matrix as history and annotate changed priorities. Do not map Apollo to SPA-13/14 without checking their actual briefs and dependencies.

## Content Creator proposal

Build the explanation around **question → equation → code → observable result → limitation**. In the opening minute, show the result viewers will reproduce. Then explain variables and units, connect code to the equation, and change one parameter to expose a failure or boundary case.

Deliver one package: spoken script with visual/cell cues; claim ledger with primary-source locations and dates; companion narrative; executable artifact link and run instructions; actual validation results; and a short note on what Carlos can now explain and what remains unresolved. If implementation is pending, label the package incomplete rather than using mock results as evidence.

For Perseverance, retain prior source corrections and satisfy the existing notebook contract. For Apollo, request the verified routine mapping before claiming the interactive reproduces historical guidance. Use placeholder narration clearly marked as such when evidence is missing. Synthetic parameters and educational approximations must be visible where readers encounter them.

## Review gates and measures

Chief of Staff checks the shared [editorial rubric](README.md), source-to-equation support, units, code/figure consistency, an independent correctness check, and reproducibility. Return failed criteria with a specific repair action. Capture accepted packages, review minutes, revision requests, and factual corrections when available; leave missing values unknown.

Ready-to-forward messages: [Content Strategist](prompts/content-strategist.md) and [Content Creator](prompts/content-creator.md). Optional role additions are in the same files and remain proposals until Carlos chooses to adopt them.
