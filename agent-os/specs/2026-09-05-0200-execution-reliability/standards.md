# Applicable standards

## execution

Give each task one accountable owner, a concrete deliverable, dependencies, and acceptance criteria. Reuse existing Paperclip issues. In-review work needs a named reviewer and a real review interaction; blocked work needs a named unblock owner/action. End a run with a durable artifact and task disposition. Wake on actionable changes; repeated checks of unchanged blocked work are not progress. Do not re-request approval already granted within its scope. Keep draft QA inside the team and consolidate material decisions for Carlos.

## security

Never commit credentials, auth/session files, private keys, environment secrets, runtime databases, backups, raw run logs, or generated instance state. Use explicit staging and inspect all commits being pushed, not just the newest diff. Ignore rules do not remove tracked secrets. Any detected secret must be removed from outgoing history before push and reported without printing it. Do not publish, deploy, change production, authentication, infrastructure, or spend without the applicable explicit authorization. A written agent boundary is not proof that the runtime enforces it.

## progress

Use stable task IDs and checkboxes, with owner, dependency, and evidence for completion. Keep current execution in agent-os/progress.md and spec tasks.md; preserve older docs as dated context. Link the live Paperclip issue ID when known, and mark unknown current state as needing verification. Record outcomes, review minutes, revision rounds, material factual corrections, and failed/no-action runs where measurable; never invent baseline numbers. Archive selected deliverables with portable repository links and preserve their source issue and draft status.
