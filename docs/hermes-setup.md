# Hermes CEO and web dashboard

## Verified deployment — September 5, 2026

Hermes 0.21.0 runs alongside Paperclip on a 2-vCPU EC2 host with 3.7 GiB RAM and 4 GiB swap. After dashboard startup and a browser-terminal check, about 2.2 GiB RAM and 17 GiB disk remained available. This is a snapshot, not a peak-load guarantee. Start with one CEO run and one interactive chat; builds and multiple browser sessions can increase demand.

The CEO uses `hermes_local`, provider `openai-codex`, model `gpt-6-astra`, and high reasoning. A minimal inference request and a full Paperclip run succeeded. The run read the live identity and confirmed this reporting structure:

```text
Human owner / board
└── CEO (Hermes)
    └── Chief of Staff (existing Codex agent)
        ├── Business Strategist
        ├── Research & Editorial Producer
        └── Content Strategist
```

The Chief of Staff kept its model, runtime configuration, schedule, and specialist reports. Its manager and introductory role paragraph changed. CEO concurrency is one; its daily timer skips when there is no actionable work. Memory, skills, session recall, terminal, file, and planning tools are enabled.

## Install and authenticate

Use the [official installer](https://hermes-agent.nousresearch.com/docs/getting-started/installation/) and review its downloaded script before execution:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh -o /tmp/hermes-install.sh
less /tmp/hermes-install.sh
bash /tmp/hermes-install.sh --skip-setup --skip-browser --skip-computer-use
```

Amazon Linux required `sudo dnf install -y gcc-c++` before installation. The installer provisioned Python 3.11 in its own environment. Keep system Python intact. Installation paths below assume the normal per-user git installer.

Run `hermes model`, select the ChatGPT or Codex subscription provider, and complete its login flow. Hermes supports importing existing Codex credentials; the deployed setup used that path. Keep all OAuth state local. Account entitlement and quota still apply; verify the requested model instead of silently substituting another model or enabling an API-key fallback. See [Hermes provider authentication](https://hermes-agent.nousresearch.com/docs/integrations/providers).

Configure `model.provider: openai-codex` and `model.default: gpt-6-astra` in the local Hermes config. Verify with a minimal prompt before changing the team hierarchy.

## Paperclip configuration

Create a CEO with the built-in `hermes_local` adapter and the [CEO instruction template](../ops/hermes/ceo-instructions.md). Resolve all paths and agent IDs locally; do not commit an exported agent record.

| Setting | Deployed choice |
| --- | --- |
| Provider / model | `openai-codex` / `gpt-6-astra` |
| Hermes command | Absolute path to the user's `hermes` launcher |
| Working directory | A dedicated local CEO workspace |
| Extra CLI arguments | `["--reasoning", "high"]` |
| Toolsets | `terminal,file,skills,memory,session_search,todo` |
| Session persistence | Enabled |
| Timeout / max turns | 900 seconds / 40 |
| Max concurrent runs | 1 |
| Timer | Daily; skip when no actionable work |

The installed Hermes CLI uses `--reasoning`, despite older adapter documentation mentioning `--reasoning-effort`. Inspect `hermes chat --help` for the installed version. Include the Hermes virtual environment, Node, and ripgrep in the agent's local PATH.

Set the existing Chief of Staff's manager to the CEO. Correct only its top-level role description; preserve its model and operational workflows. Verify the org chart and run a read-only CEO readiness check through Paperclip.

Paperclip's environment checker in version 2026.831.1 checks system `python3` without the agent's PATH and can warn about missing API keys despite valid Codex OAuth. The deployed launcher uses Python 3.11 and the actual run succeeded. Treat the real run as the integration check; investigate any actual authentication failure.

## Dashboard and embedded chat

The [official web dashboard](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard) serves an embedded TUI over a WebSocket. The `web` and `pty` Python extras are required; they were already present in this installation. If missing, install them in the Hermes environment:

```bash
cd ~/.hermes/hermes-agent
~/.hermes/bin/uv pip install --python venv/bin/python -e '.[web,pty]'
hermes dashboard --host 127.0.0.1 --port 9119 --no-open
```

The first launch builds the web frontend. The embedded TUI also needs a Node build on first use. Confirm the Chat tab renders before treating installation as complete. Stop this foreground launch before starting a service on the same port.

Copy [the service template](../ops/systemd/hermes-dashboard.service.example) into `~/.config/systemd/user/hermes-dashboard.service`. Replace the Node and ripgrep PATH entries with verified local directories, create the working directory, and check the Hermes launcher path. Then:

```bash
systemd-analyze --user verify ~/.config/systemd/user/hermes-dashboard.service
systemctl --user daemon-reload
systemctl --user enable --now hermes-dashboard.service
loginctl show-user "$USER" -p Linger
```

If lingering is disabled, enable it with `sudo loginctl enable-linger "$USER"` so the user service survives logout and can start at boot. The deployed host already had lingering enabled. The service is configured for boot startup; a host reboot was not performed as part of this setup.

Verify the page, API, loopback listener, and actual chat terminal:

```bash
systemctl --user status hermes-dashboard.service
ss -ltn 'sport = :9119'
curl -fsS http://127.0.0.1:9119/api/status
journalctl --user -u hermes-dashboard.service -n 50
free -h
```

A stopped messaging gateway can make overall status appear degraded. The dashboard and storage components should be healthy; a messaging gateway is not required for browser chat. The deployed check opened the real chat WebSocket and observed the TUI render `gpt-6-astra`, without submitting a model prompt.

From a laptop, use the normal host alias and key options:

```bash
ssh -N -L 9119:127.0.0.1:9119 ec2-user@YOUR_EC2_HOST
```

Open `http://localhost:9119/chat`. `-N` starts no remote shell; `-L` forwards the laptop port to EC2's loopback port. Keep the tunnel running in a terminal tab. No public listener or security-group opening is needed.

## Dashboard chat versus Paperclip identity

Dashboard chats use the default Hermes profile's model, memory, skills, and session store. Paperclip separately injects the CEO's instructions and short-lived API identity when it launches a run. A fresh dashboard chat does not automatically have that identity or authority to update Paperclip.

Use the [opening prompt](../recommendations/prompts/hermes-ceo-opening.md) to establish context. It asks Hermes to verify access and prepare a handoff if authenticated task access is unavailable. Do not copy a run token into chat, scrape credentials from logs, or assume localhost reachability proves agent authentication. A persistent authenticated task bridge would be a separate configuration change.

## Maintenance and private data

Use `systemctl --user restart hermes-dashboard.service` after an approved update; rebuild the frontend when upstream changes require it. To disable the dashboard, use `systemctl --user disable --now hermes-dashboard.service`; this leaves Paperclip and Hermes data intact.

Keep `.hermes/`, credentials, session databases, memory, logs, backups, and generated setup/agent JSON outside this public repo. These templates do not back up live state. A complete recovery design and restore rehearsal remain separate work.
