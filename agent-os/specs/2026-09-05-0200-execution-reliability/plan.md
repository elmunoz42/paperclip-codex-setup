# Make agent execution and handoffs reliable

Status: planned; implementation remains open.

Accountable owner: Chief of Staff.

## Outcome

Separate model/startup failures from legitimate review waits, and reduce runs that have no actionable work.

## Execution

Task 1, save spec documentation, is complete in this change. Follow [tasks](tasks.md) in dependency order; keep checks open until their acceptance evidence exists.

## Acceptance

All implementation tasks below meet their recorded acceptance criteria. Planning or a successful agent turn alone does not satisfy them.

## Boundaries

No automatic publication, roster expansion, production deployment, paid service, or live infrastructure change follows from this spec. Historical evidence must be refreshed before operational changes.

## Tasks

### R1: Capture current agent model/adapter, wake settings, concurrency, timeout, permissions, and usage accounting in a redacted table.

Owner: Chief of Staff. Depends on: None.

Acceptance: Timestamped live observations; historical backup settings clearly separated.

### R2: Diagnose recurring startup failures if still present and propose the smallest correction.

Owner: Chief of Staff. Depends on: R1.

Acceptance: Successful bounded task or evidence issue resolved; no inference that old model errors still apply.

### R3: Propose low concurrency, finite task-appropriate timeouts, actionable wake rules, and enforceable access boundaries.

Owner: Chief of Staff. Depends on: R1.

Acceptance: Proposal explains current versus recommended values and impact; no production/auth changes executed without authorization.

### R4: Approve changes that affect permissions, spend, authentication, or infrastructure.

Owner: Carlos. Depends on: R2, R3.

Acceptance: Scoped decision recorded; existing authorization reused where applicable.

### R5: Apply approved corrections and verify one useful task handoff.

Owner: Chief of Staff. Depends on: R4.

Acceptance: Artifact plus clear disposition; no startup failure or lost continuation in the validation task.

### R6: Observe the next five task-triggered runs and report outcomes.

Owner: Chief of Staff. Depends on: R5.

Acceptance: Counts of useful, failed, and no-action runs; usage visibility limitations stated; no artificial wakes solely for metrics.
