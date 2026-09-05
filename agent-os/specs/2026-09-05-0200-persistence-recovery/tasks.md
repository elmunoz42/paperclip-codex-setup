# Prepare durable operations and recovery — tasks

- [x] DOC: Save plan, shaping notes, standards, references, and task checklist. Evidence: files in this spec folder.

- [ ] O1: Verify current launch mechanism, backup freshness, storage coverage, and Git preservation.
  - Owner: Chief of Staff; depends on: None.
  - Acceptance: Redacted evidence with timestamps; distinguish database backup from files, secrets, and workspaces.
  - Evidence / Paperclip issue: Not yet recorded.

- [ ] O2: Complete the systemd template and rollback plan using the actual launch command.
  - Owner: Chief of Staff; depends on: O1.
  - Acceptance: Syntax validation, ownership, environment paths, loopback binding, and rollback steps documented; no activation.
  - Evidence / Paperclip issue: Not yet recorded.

- [ ] O3: Design a full recovery plan and isolated restore rehearsal, including encrypted off-host coverage if approved.
  - Owner: Chief of Staff; depends on: O1.
  - Acceptance: Coverage and key custody documented without secret values; rehearsal plan does not touch live DB.
  - Evidence / Paperclip issue: Not yet recorded.

- [ ] O4: Approve any cutover window, off-host destination, access changes, or cost.
  - Owner: Carlos; depends on: O2, O3.
  - Acceptance: Explicit scope, maintenance window, and rollback owner recorded.
  - Evidence / Paperclip issue: Not yet recorded.

- [ ] O5: Execute the approved persistence and recovery work.
  - Owner: Chief of Staff; depends on: O4.
  - Acceptance: Service restart/reboot behavior and isolated restore verified with evidence; rollback available.
  - Evidence / Paperclip issue: Not yet recorded.

- [ ] O6: Record ongoing maintenance ownership and recovery targets.
  - Owner: Chief of Staff; depends on: O5.
  - Acceptance: Backup checks, retention, restore cadence, and agreed recovery targets documented.
  - Evidence / Paperclip issue: Not yet recorded.
