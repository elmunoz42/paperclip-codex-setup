#!/usr/bin/env python3
"""Check the exact Git index for private paths and secrets before committing."""
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tempfile


def main():
    root = subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], text=True
    ).strip()
    os.chdir(root)
    scanner = shutil.which("gitleaks")
    fallback = Path.home() / ".local/bin/gitleaks"
    if not scanner and fallback.is_file():
        scanner = str(fallback)
    if not scanner:
        print("Commit blocked: install Gitleaks before committing. See SECURITY.md.")
        return 1

    private_dirs = {".paperclip", ".codex", ".aws", ".ssh", ".kube", "secrets", ".secrets", "backups"}
    private_names = {"auth.json", "credentials", "credentials.json", "id_rsa", "id_ed25519", "id_ecdsa", ".envrc", ".netrc", ".npmrc", ".pypirc", "kubeconfig"}
    private_suffixes = (".pem", ".key", ".p12", ".pfx", ".jks", ".keystore", ".db", ".sqlite", ".sqlite3", ".sql", ".sql.gz", ".dump", ".log", ".ndjson", ".zip", ".tar", ".tar.gz", ".tgz", ".bak", ".tfvars", ".tfvars.json")
    entries = subprocess.check_output(["git", "ls-files", "--stage", "-z"]).split(b"\0")
    with tempfile.TemporaryDirectory(prefix="public-index-") as temp:
        snapshot = Path(temp)
        for entry in filter(None, entries):
            metadata, raw_name = entry.split(b"\t", 1)
            mode, oid, stage = metadata.decode().split()
            name = os.fsdecode(raw_name)
            path = PurePosixPath(name)
            lower = path.name.lower()
            private_env = (lower == ".env" or lower.startswith(".env.")) and lower != ".env.example"
            private_claude = ".claude" in path.parts and not name.startswith(".claude/commands/agent-os/")
            if (path.is_absolute() or ".." in path.parts or stage != "0"
                    or mode not in {"100644", "100755"}
                    or private_dirs.intersection(part.lower() for part in path.parts)
                    or lower in private_names or private_env or private_claude
                    or lower.endswith(private_suffixes) or ".tfstate" in lower):
                print(f"Commit blocked: review private/generated path or unsupported index entry: {name}")
                return 1
            destination = snapshot / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(subprocess.check_output(["git", "cat-file", "blob", oid]))
        # No report artifact or secret value is emitted into the repository.
        # Ignore in-file suppression comments so accidental tokens are not hidden.
        return subprocess.run([
            scanner, "dir", str(snapshot), "--redact", "--no-banner",
            "--ignore-gitleaks-allow", "--max-archive-depth", "2",
        ], cwd=temp).returncode


if __name__ == "__main__":
    sys.exit(main())
