# Headquarters operating rules

## Purpose and scope

This repository coordinates Space Exploration News work. It does not contain production website, WordPress, or immersive-app source code. Link to external repositories only after their owner and access path are supplied.

## Default operating rules

- Prefer a small, reviewable Markdown artifact over a new tool or service.
- Preserve attribution: every factual research claim must have a primary-source URL, publisher, date accessed, and claim-specific note.
- Label statements as **verified fact**, **analysis**, **proposal**, or **open question**. Do not silently promote analysis to fact.
- Do not publish, deploy, change DNS/AWS/authentication/billing, create paid services, or touch production systems without Carlos's explicit approval.
- Do not store credentials, tokens, private keys, generated instance data, or local Paperclip/Codex auth files. Keep `.env` files ignored.
- Do not stop/restart Paperclip, remove swap, or activate a systemd unit from this repository during the initial setup.
- Keep decisions short in `docs/decisions/`; record the context, choice, consequences, owner, and revisit trigger.

## Human approval boundaries

Carlos approves editorial angle, scripts, factual/risk-sensitive claims, public responses, publication, sponsorship/affiliate/commercial activity, spend, and production changes. Agents may research, organize, draft, and test offline artifacts within approved scope.

## Definition of a useful handoff

Deliverables identify their intended audience, source material, assumptions, unresolved questions, and a clear review action. Never present a draft as ready to publish.

## Collaboration

Carlos uses this assistant as a strategic adviser: save recommendations and proposed prompts in `recommendations/`; Carlos routes them to the Chief of Staff, and implementation agents execute. Do not treat proposed prompts as installed or automatically send handoffs. Small educational notebooks may live here as content artifacts; production applications remain separate.

Begin with the minimum roster in `docs/content-engine.md`. Create specialized roles only after the thin slice exposes repeatable workload or quality needs. Escalate conflicts between speed and accuracy to Carlos.

## Agent OS and progress tracking

Read `agent-os/README.md`, `agent-os/progress.md`, the standards index, and the assigned spec before significant work. Use spec task IDs in handoffs. Update task checkboxes only with completion evidence; mirror relevant Paperclip issue IDs without creating duplicates. Root rules and explicit user instructions take precedence over workflow templates. Specs do not independently authorize production, publication, permissions, or spend changes.
