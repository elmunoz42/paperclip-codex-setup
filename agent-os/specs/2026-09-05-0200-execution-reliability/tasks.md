# Make agent execution and handoffs reliable — tasks

- [x] DOC: Save plan, shaping notes, standards, references, and task checklist. Evidence: files in this spec folder.

- [ ] R1: Capture current agent model/adapter, wake settings, concurrency, timeout, permissions, and usage accounting in a redacted table.
  - Owner: Chief of Staff; depends on: None.
  - Acceptance: Timestamped live observations; historical backup settings clearly separated.
  - Evidence / Paperclip issue: Not yet recorded.

- [ ] R2: Diagnose recurring startup failures if still present and propose the smallest correction.
  - Owner: Chief of Staff; depends on: R1.
  - Acceptance: Successful bounded task or evidence issue resolved; no inference that old model errors still apply.
  - Evidence / Paperclip issue: Not yet recorded.

- [ ] R3: Propose low concurrency, finite task-appropriate timeouts, actionable wake rules, and enforceable access boundaries.
  - Owner: Chief of Staff; depends on: R1.
  - Acceptance: Proposal explains current versus recommended values and impact; no production/auth changes executed without authorization.
  - Evidence / Paperclip issue: Not yet recorded.

- [ ] R4: Approve changes that affect permissions, spend, authentication, or infrastructure.
  - Owner: Carlos; depends on: R2, R3.
  - Acceptance: Scoped decision recorded; existing authorization reused where applicable.
  - Evidence / Paperclip issue: Not yet recorded.

- [ ] R5: Apply approved corrections and verify one useful task handoff.
  - Owner: Chief of Staff; depends on: R4.
  - Acceptance: Artifact plus clear disposition; no startup failure or lost continuation in the validation task.
  - Evidence / Paperclip issue: Not yet recorded.

- [ ] R6: Observe the next five task-triggered runs and report outcomes.
  - Owner: Chief of Staff; depends on: R5.
  - Acceptance: Counts of useful, failed, and no-action runs; usage visibility limitations stated; no artificial wakes solely for metrics.
  - Evidence / Paperclip issue: Not yet recorded.
