# Prepare durable operations and recovery

Status: planned; implementation remains open.

Accountable owner: Chief of Staff.

## Outcome

Protect the running service and durable work with verified startup and recovery procedures.

## Execution

Task 1, save spec documentation, is complete in this change. Follow [tasks](tasks.md) in dependency order; keep checks open until their acceptance evidence exists.

## Acceptance

All implementation tasks below meet their recorded acceptance criteria. Planning or a successful agent turn alone does not satisfy them.

## Boundaries

No automatic publication, roster expansion, production deployment, paid service, or live infrastructure change follows from this spec. Historical evidence must be refreshed before operational changes.

## Tasks

### O1: Verify current launch mechanism, backup freshness, storage coverage, and Git preservation.

Owner: Chief of Staff. Depends on: None.

Acceptance: Redacted evidence with timestamps; distinguish database backup from files, secrets, and workspaces.

### O2: Complete the systemd template and rollback plan using the actual launch command.

Owner: Chief of Staff. Depends on: O1.

Acceptance: Syntax validation, ownership, environment paths, loopback binding, and rollback steps documented; no activation.

### O3: Design a full recovery plan and isolated restore rehearsal, including encrypted off-host coverage if approved.

Owner: Chief of Staff. Depends on: O1.

Acceptance: Coverage and key custody documented without secret values; rehearsal plan does not touch live DB.

### O4: Approve any cutover window, off-host destination, access changes, or cost.

Owner: Carlos. Depends on: O2, O3.

Acceptance: Explicit scope, maintenance window, and rollback owner recorded.

### O5: Execute the approved persistence and recovery work.

Owner: Chief of Staff. Depends on: O4.

Acceptance: Service restart/reboot behavior and isolated restore verified with evidence; rollback available.

### O6: Record ongoing maintenance ownership and recovery targets.

Owner: Chief of Staff. Depends on: O5.

Acceptance: Backup checks, retention, restore cadence, and agreed recovery targets documented.
