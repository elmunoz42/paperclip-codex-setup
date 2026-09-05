# Space Exploration News — Agent Headquarters

This repository is the durable operating system for the Space Exploration News agent team. It holds strategy, editorial workflows, decisions, runbooks, and plans—not production website or application source code.

## For portfolio reviewers

Current direction: [math-and-code learning artifacts and adviser handoffs](recommendations/README.md), including a Perseverance notebook specification and an Apollo interactive proposal. Implementation is pending.

This is a working example of an AI-assisted editorial operation: explicit specifications, source attribution, independent QA, human review gates, and evidence-backed task status. It documents both delivered work and unresolved limits.

Start with the [Mars review packet](docs/content/SPA-12-review.md), compare its [QA corrections](docs/content/SPA-12-qa-report.md), then inspect the [spec and task evidence](agent-os/specs/2026-09-05-0200-editorial-pilot/tasks.md). The content remains a draft; a completed agent task is not a claim of publication readiness.

[Public repository safety](SECURITY.md) explains exclusions, the local commit check, and the scope of the security scan. Runtime credentials, databases, and raw execution logs belong outside this repository.

## Start here

- [Vision](docs/vision.md): purpose, audience, and operating principles.
- [Current state](docs/current-state.md): verified environment facts and explicit unknowns.
- [Roadmap](docs/roadmap.md): five separate workstreams and 30/60/90-day priorities.
- [Content engine](docs/content-engine.md): the first review-ready content thin slice.
- [Two-week backlog](docs/backlog.md): actionable starting sprint.
- [Infrastructure](docs/infrastructure.md): current Paperclip/Hermes services, localhost access, and recovery scope.

- [Hermes CEO and dashboard](docs/hermes-setup.md): setup runbook, service template, and browser-chat access.

## Repository boundary

Keep immersive solar-system application code and WordPress theme/plugin code in their own repositories. Store only coordination artifacts and automation that is safe to run from this headquarters.

## Operating cadence

Run one content thin slice before expanding the agent roster or building management software. Carlos retains editorial, factual-risk, publishing, and spend decisions.

## Current execution

- [Progress and next actions](agent-os/progress.md)
- [Agent OS installation and usage](agent-os/README.md)
- [Preserved editorial work products](docs/content/README.md)
- [Dated audit findings](docs/audit-2026-09-05.md)

Agent OS holds standards and specs; Paperclip runs and assigns the work.
