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
ISSUE_TEMPLATE_DIR = ROOT / ".github" / "ISSUE_TEMPLATE"
TROUBLESHOOTING_FAQ_PATH = ROOT / "docs" / "free-lite-troubleshooting-faq.md"
UPGRADE_BOUNDARY_PATH = ROOT / "docs" / "upgrade-path-boundary.md"
OUTPUT_REVIEW_GUIDE_PATH = ROOT / "docs" / "free-lite-output-review-guide.md"
FULL_PACK_LISTING_PATH = ROOT / "docs" / "full-pack-public-listing.md"

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

REQUIRED_ISSUE_TEMPLATES = {
    "free-lite-setup.yml",
    "free-lite-feedback.yml",
    "workflow-pack-inquiry.yml",
    "audit-pilot-inquiry.yml",
    "config.yml",
}

PUBLIC_SAFETY_MARKERS = (
    "tokens",
    "private",
    "customer data",
    "credentials",
)


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

    if not ISSUE_TEMPLATE_DIR.exists():
        fail("missing .github/ISSUE_TEMPLATE public inquiry forms")

    if not TROUBLESHOOTING_FAQ_PATH.exists():
        fail("missing public-safe troubleshooting FAQ")

    if not UPGRADE_BOUNDARY_PATH.exists():
        fail("missing public-safe upgrade path boundary")
    if not OUTPUT_REVIEW_GUIDE_PATH.exists():
        fail("missing public-safe output review guide")
    if not FULL_PACK_LISTING_PATH.exists():
        fail("missing checkout-disabled full pack public listing preview")

    faq_text = TROUBLESHOOTING_FAQ_PATH.read_text(encoding="utf-8").lower()
    faq_required_markers = (
        "public repository",
        "sanitized",
        "tokens",
        "private repository urls",
        "customer data",
        "credentials",
        "payout",
    )
    missing_faq_markers = [marker for marker in faq_required_markers if marker not in faq_text]
    if missing_faq_markers:
        fail(
            "public-safe troubleshooting FAQ is missing marker(s): "
            f"{', '.join(missing_faq_markers)}"
        )

    upgrade_text = UPGRADE_BOUNDARY_PATH.read_text(encoding="utf-8").lower()
    upgrade_required_markers = (
        "checkout",
        "payment",
        "kyc",
        "tax",
        "credentials",
        "private repository urls",
        "customer data",
        "no guaranteed roi",
    )
    missing_upgrade_markers = [
        marker for marker in upgrade_required_markers if marker not in upgrade_text
    ]
    if missing_upgrade_markers:
        fail(
            "public-safe upgrade path boundary is missing marker(s): "
            f"{', '.join(missing_upgrade_markers)}"
        )

    output_guide_text = OUTPUT_REVIEW_GUIDE_PATH.read_text(encoding="utf-8").lower()
    output_guide_required_markers = (
        "public repository",
        "sanitized",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "payment details",
        "kyc/tax information",
        "no guaranteed roi",
        "samples/sample-output.md",
    )
    missing_output_guide_markers = [
        marker for marker in output_guide_required_markers if marker not in output_guide_text
    ]
    if missing_output_guide_markers:
        fail(
            "public-safe output review guide is missing marker(s): "
            f"{', '.join(missing_output_guide_markers)}"
        )

    listing_text = FULL_PACK_LISTING_PATH.read_text(encoding="utf-8").lower()
    listing_required_markers = (
        "checkout-disabled",
        "local draft only",
        "payment",
        "kyc",
        "tax",
        "bank",
        "contracts",
        "private",
        "customer data",
        "no guaranteed roi",
    )
    missing_listing_markers = [
        marker for marker in listing_required_markers if marker not in listing_text
    ]
    if missing_listing_markers:
        fail(
            "full pack public listing preview is missing marker(s): "
            f"{', '.join(missing_listing_markers)}"
        )

    missing_templates = sorted(
        name for name in REQUIRED_ISSUE_TEMPLATES if not (ISSUE_TEMPLATE_DIR / name).exists()
    )
    if missing_templates:
        fail(f"missing public issue template(s): {', '.join(missing_templates)}")

    for template_name in sorted(REQUIRED_ISSUE_TEMPLATES - {"config.yml"}):
        template_text = (ISSUE_TEMPLATE_DIR / template_name).read_text(encoding="utf-8").lower()
        missing_markers = [marker for marker in PUBLIC_SAFETY_MARKERS if marker not in template_text]
        if missing_markers:
            fail(
                f"issue template {template_name} is missing public-safety marker(s): "
                f"{', '.join(missing_markers)}"
            )

    print("OK: Free Lite workflow JSON and public issue forms pass static public-safety checks.")


if __name__ == "__main__":
    main()
