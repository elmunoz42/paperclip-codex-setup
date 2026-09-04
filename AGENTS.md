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

Begin with the minimum roster in `docs/content-engine.md`. Create specialized roles only after the thin slice exposes repeatable workload or quality needs. Escalate conflicts between speed and accuracy to Carlos.
