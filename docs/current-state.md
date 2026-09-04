# Current state

Verified on 2026-09-04 from the EC2 workspace:

| Area | Verified state |
| --- | --- |
| Host | Amazon Linux 2023.12; kernel 6.18.44 |
| Capacity | 30 GB volume, 19 GB available; 3.7 GiB RAM; 4 GiB swap present and unused |
| Tooling | Node v24.20.0; Codex CLI 0.153.2; systemd 252 |
| Paperclip | Running locally and listening only on `127.0.0.1:3100` |
| tmux | `tmux` command is not installed in this execution environment; prior tmux claim is not currently verifiable |
| Headquarters repository | Remote `git@github.com:elmunoz42/paperclip-codex-setup.git` exists, has `main` at `22db81a`, and initially contained only `.gitignore` |

## Known product state

- The WordPress site is live; its repository, hosting path, and integration constraints have not been supplied.
- A separate immersive solar-system application exists; its source and deployment details are not in this repository and must not be assumed.
- CMS integration for that application has begun but its current interface and gaps are unknown.

## Assumptions and unresolved decisions

- The model requested in the original brief, `gpt-5.6-sol`, is unavailable in this ChatGPT-backed environment. The board has changed the active model to `gpt-5.6-terra`; use that configuration unless instructed otherwise.
- No production access is needed for the first thin slice.
- The first content topic and publication cadence still require Carlos's editorial choice.
