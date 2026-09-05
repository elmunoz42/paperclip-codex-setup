# Agent OS for Space Exploration News

Start with [progress](progress.md), then the relevant spec and its task checklist.

Builder Methods Agent OS supplies standards, product context, and spec workflows. Paperclip remains the runtime and assignment system. This installation does not create live Paperclip issues or change agent settings.

## Installation provenance

- Upstream: https://github.com/buildermethods/agent-os
- Version: config 3.0; git describe `v3.0.0-7-g475b0ca`
- Commit: `475b0cac4c7c5cf2336ad5a663b691a6d3415e05`
- Installed: 2026-09-05 with the reviewed upstream `scripts/project-install.sh`, default profile.
- Base checkout: `~/agent-os`; project commands: `.claude/commands/agent-os/`.
- The upstream default profile installed no standards. This project's standards were extracted from the existing headquarters rules.
- MIT license: [LICENSE](LICENSE).

## Using it with Paperclip agents

Read the root `AGENTS.md`, [standards index](standards/index.yml), relevant standards, and the assigned spec's `plan.md` and `tasks.md`. The checked-in Markdown is usable directly by any agent; the upstream slash commands are installed for Claude Code, and are not claimed to be registered Codex commands.

The existing strategy supplied enough context to write these specs directly. The upstream interactive shape-spec command was not executed. Its plan-mode instructions remain unchanged for future users of that command.

Task checkboxes are the repository's durable progress record; Paperclip owns live execution status. When a task is assigned there, record its issue identifier alongside the task ID. Do not create duplicate issues for SPA-12, SPA-13, or SPA-14. Update checkboxes only with linked evidence and an actual completion result. An agent turn ending successfully is not completion evidence.

## Updating

Review upstream changes in the base checkout before updating. Run `bash ~/agent-os/scripts/project-install.sh --commands-only` from this repository to preserve custom standards. Inspect the diff, update the provenance commit, and validate links and secret exclusions before committing. Retain the upstream license.
