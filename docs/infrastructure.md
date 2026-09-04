# Infrastructure

## Current verified posture

Paperclip is running and listening on `127.0.0.1:3100`. The host has 3.7 GiB RAM and a 4 GiB unused swap file. Do not stop/restart Paperclip or remove swap during this initial setup.

## Safe tmux-to-systemd migration path (documented only)

### Preconditions

1. Confirm the exact command, working directory, Node path, user, and required non-secret environment variables from the current live process.
2. Confirm how Paperclip currently receives secrets; place no secret values in a unit file or repository.
3. Review [the example unit](../ops/systemd/paperclip.service.example) locally and have Carlos approve a maintenance window.
4. Capture baseline health: process PID/command, `ss` listener on 127.0.0.1:3100, Paperclip health endpoint if available, `free -h`, `swapon --show`, and recent logs.
5. Install the unit outside this repository only after review, using a root-owned environment file with restrictive permissions if one is required.

### Controlled cutover

1. Validate the unit syntax with `systemd-analyze verify` before enabling it.
2. Do not enable/start it while the tmux-managed process owns port 3100.
3. During the approved window, stop the old process once, start the unit, then verify service status, listener binding, health endpoint, logs, and a fresh Paperclip interaction.
4. Observe memory and swap use for a normal workload before considering any swap change.

### Rollback

If startup, health, authentication, binding, or behavior is degraded: stop and disable the new unit; restore the prior tmux launch command; verify the same baseline checks; retain logs and the unit for diagnosis. Do not delete the swap file.

### Verification criteria

- The service runs as the intended non-root user.
- It binds only to `127.0.0.1:3100` unless an approved architecture changes that.
- Restart policy works on a safe test only after functional health is confirmed.
- Logs are available through `journalctl -u paperclip`.
- No secrets appear in the unit, repository, process list, or logs.

## Model pinning

The original `gpt-5.6-sol` pin failed in this ChatGPT-backed runtime. The current board instruction is to use `gpt-5.6-terra`. Keep model selection explicit in Paperclip configuration; verify it in the next configuration review rather than relying on implicit defaults.
