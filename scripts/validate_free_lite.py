#!/usr/bin/env python3
"""Validate the Free Lite n8n workflow for public-safe release checks.

This intentionally checks only static properties so it can run in CI without
secrets, network access, n8n, or private repository data.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = ROOT / "workflows" / "free-lite-github-weekly-snapshot.json"

FORBIDDEN_MUTATING_PATTERNS = [
    r"api\.github\.com/repos/[^`'\"\s]+/[^`'\"\s]+/issues/[^`'\"\s]+/comments",
    r"api\.github\.com/repos/[^`'\"\s]+/[^`'\"\s]+/contents",
    r"slack\.com/api/chat\.postMessage",
    r"discord(?:app)?\.com/api/webhooks",
    r"notion\.com/v1/pages",
]

REQUIRED_NODE_NAMES = {
    "Manual Trigger",
    "Optional Friday 5pm Trigger",
    "Config - Public Repo Snapshot",
    "Fetch GitHub Activity and Build Markdown",
    "Output Markdown Snapshot",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    try:
        raw = WORKFLOW_PATH.read_text(encoding="utf-8")
        workflow = json.loads(raw)
    except FileNotFoundError:
        fail(f"missing workflow file: {WORKFLOW_PATH.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"workflow JSON is invalid: {exc}")

    nodes = workflow.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        fail("workflow.nodes must be a non-empty list")

    names = {node.get("name") for node in nodes if isinstance(node, dict)}
    missing = sorted(REQUIRED_NODE_NAMES - names)
    if missing:
        fail(f"missing required node(s): {', '.join(missing)}")

    if "$env.GITHUB_TOKEN" not in raw:
        fail("workflow should keep GITHUB_TOKEN optional via environment variable")
    if "https://api.github.com/repos/" not in raw:
        fail("workflow should fetch public GitHub repository activity")
    if "markdown" not in raw:
        fail("workflow should emit a markdown field for review-first output")

    for pattern in FORBIDDEN_MUTATING_PATTERNS:
        if re.search(pattern, raw, flags=re.IGNORECASE):
            fail(f"workflow appears to contain a mutating/posting integration: {pattern}")

    for secret_like in ("sk-ant-", "ghp_", "github_pat_", "xoxb-", "BEGIN PRIVATE KEY"):
        if secret_like in raw:
            fail(f"workflow contains a secret-like marker: {secret_like}")

    print("OK: Free Lite workflow JSON is valid and passes static public-safety checks.")


if __name__ == "__main__":
    main()
