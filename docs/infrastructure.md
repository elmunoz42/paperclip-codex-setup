# Infrastructure

## Verified posture — September 5, 2026

Paperclip runs as the `paperclipai.service` systemd user service and listens on `127.0.0.1:3100`. Hermes's dashboard runs as `hermes-dashboard.service` on `127.0.0.1:9119`; its service is enabled and user lingering is enabled. No reboot test was performed during the Hermes setup.

The host has 2 vCPUs, 3.7 GiB RAM, and 4 GiB swap. After dashboard and TUI startup testing, approximately 2.2 GiB RAM and 17 GiB disk remained available. These are point-in-time observations; monitor actual concurrent workloads and retain swap.

See [Hermes setup and verification](hermes-setup.md) for installation, CEO configuration, browser chat, SSH forwarding, and the [dashboard service template](../ops/systemd/hermes-dashboard.service.example).

## Operating checks

```bash
systemctl --user status paperclipai.service hermes-dashboard.service
curl -fsS http://127.0.0.1:3100/api/health
curl -fsS http://127.0.0.1:9119/api/status
free -h
```

Keep both listeners on loopback and access through SSH tunnels. Do not commit local unit exports containing host-specific values or any credentials. Review runtime logs locally.

The [older Paperclip unit example](../ops/systemd/paperclip.service.example) is a historical migration sketch, not the currently installed user service. Do not install it alongside the existing service. Future Paperclip changes should first inspect the actual user unit, health, and backup status, then define a maintenance window and rollback.

## Models and team

The new CEO runs `hermes_local` with `openai-codex`, `gpt-6-astra`, and high reasoning. A full Paperclip run verified its identity and reporting line. Chief of Staff retains `gpt-5.6-sol` with its existing cheaper `gpt-5.6-terra` profile; this setup did not re-test its inference. Specialists remain under the Chief of Staff. Historical model-failure notes are not current model-selection instructions.

## Recovery scope

Service persistence is configured; complete backup coverage, encrypted off-host recovery, and an isolated restore rehearsal are not established by this setup. Keep the [persistence/recovery checklist](../agent-os/specs/2026-09-05-0200-persistence-recovery/tasks.md) as separate work. Do not mark all recovery tasks complete based on a healthy service or Git push.
