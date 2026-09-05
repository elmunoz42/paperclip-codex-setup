# Observed stack and boundaries

- Headquarters: Markdown, Git, and Agent OS 3.0 project files.
- Runtime outside this repository: Paperclip 2026.831.1, embedded PostgreSQL, local file storage, Codex-backed agents.
- September 4 host documentation records Amazon Linux 2023, Node 24.20.0, Codex CLI 0.153.2, approximately 3.7 GiB RAM and 4 GiB swap. These are dated observations, not current probes.
- Local configuration specifies loopback binding and hourly local database backups.
- Production WordPress and immersive-app stacks/access remain outside this repository and unverified.
- Runtime databases, auth files, logs, secrets, and company execution state are excluded from Git.

See [infrastructure](../../docs/infrastructure.md). Do not use historical model failures to infer present model availability; later September 5 logs show completed runs with the formerly failing model setting.
