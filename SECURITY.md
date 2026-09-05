# Public repository safety

This public portfolio contains operating standards, specs, selected draft work products, and reviewed examples. It does not need live credentials, databases, raw run logs, or exported account/session state. Hermes profiles, memory, skills learned from private work, OAuth state, and local provisioning exports also stay outside this public repository. See [the Hermes runbook](docs/hermes-setup.md).

## Before committing

Install [Gitleaks](https://github.com/gitleaks/gitleaks/releases) and Python 3, then enable the repository-local check:

```sh
git config core.hooksPath .githooks
```

The hook scans the exact staged file contents, including unchanged tracked files, and rejects known private/generated paths even if force-added. Secrets in an untracked file are not safe to stage merely because it is currently ignored. An example environment file must contain placeholders only.

Run the checks manually when needed:

```sh
python3 scripts/check-public-index.py
gitleaks git --log-opts="--all --full-history" --redact --no-banner .
```

The hook is enabled in this working checkout. Git does not enable hooks automatically in new clones. These are local checks, not server-enforced push protection or a configured GitHub Actions check. Do not bypass a failing check to publish a credential.

## Audit scope — September 5, 2026

Gitleaks 8.30.1 found no leaks in the five existing commits through `b158edc` or the initial 55-file candidate snapshot. The final staged revision is checked again by the commit hook. A separate review checked secret-path exclusions and public-facing material. Hook checks verified that a clean index passes, a staged private environment file fails, and a staged synthetic token fails even when its working-tree copy has been replaced with clean text. Synthetic fixtures stayed in temporary repositories.

The official Linux x64 release archive was verified against its published SHA-256 before use: `551f6fc83ea457d62a0d98237cbad105af8d557003051f41f3e7ca7b3f2470eb`. The scanner executable and raw reports are kept outside the repository.

New handoff notes omit opaque runtime IDs, and the trial evaluation links to its repository artifact. Task IDs such as SPA-12 are retained for traceability. No history rewrite was needed for a detected secret.

This is a bounded repository secret review, not a guarantee that every possible secret is detectable or an audit of the live server, GitHub account settings, screenshots, or other repositories. Source-access limitations and editorial approval remain separate from security checks.

## If a credential is ever exposed

Revoke or rotate it first, then coordinate removal from all affected Git history and other copies. Deleting it from the latest file alone does not remove prior public exposure. Do not paste credentials into a public issue or security report; report the location and credential type without the value.
