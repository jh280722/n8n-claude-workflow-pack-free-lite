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
DOWNLOAD_FIRST_RUN_GUIDE_PATH = ROOT / "docs" / "free-lite-download-first-run-guide.md"
UPGRADE_BOUNDARY_PATH = ROOT / "docs" / "upgrade-path-boundary.md"
OUTPUT_REVIEW_GUIDE_PATH = ROOT / "docs" / "free-lite-output-review-guide.md"
FULL_PACK_LISTING_PATH = ROOT / "docs" / "full-pack-public-listing.md"
BUYER_FIT_CHECKLIST_PATH = ROOT / "docs" / "buyer-fit-checklist.md"
PUBLIC_SHARE_KIT_PATH = ROOT / "docs" / "public-share-kit.md"
PUBLIC_EVALUATION_SCORECARD_PATH = ROOT / "docs" / "public-evaluation-scorecard.md"
PUBLIC_INQUIRY_ROUTER_PATH = ROOT / "docs" / "public-inquiry-router.md"
PUBLIC_PROOF_INDEX_PATH = ROOT / "docs" / "public-proof-index.md"
PUBLIC_ROI_ASSUMPTION_WORKSHEET_PATH = ROOT / "docs" / "public-roi-assumption-worksheet.md"
PUBLIC_SAFE_ONBOARDING_PLAYBOOK_PATH = ROOT / "docs" / "public-safe-onboarding-playbook.md"
PUBLIC_IMPLEMENTATION_SCOPE_MENU_PATH = ROOT / "docs" / "public-implementation-scope-menu.md"

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
    if not DOWNLOAD_FIRST_RUN_GUIDE_PATH.exists():
        fail("missing public-safe download-to-first-run guide")

    if not UPGRADE_BOUNDARY_PATH.exists():
        fail("missing public-safe upgrade path boundary")
    if not OUTPUT_REVIEW_GUIDE_PATH.exists():
        fail("missing public-safe output review guide")
    if not FULL_PACK_LISTING_PATH.exists():
        fail("missing checkout-disabled full pack public listing preview")
    if not BUYER_FIT_CHECKLIST_PATH.exists():
        fail("missing public-safe buyer fit checklist")
    if not PUBLIC_SHARE_KIT_PATH.exists():
        fail("missing public-safe share kit")
    if not PUBLIC_EVALUATION_SCORECARD_PATH.exists():
        fail("missing public-safe evaluation scorecard")
    if not PUBLIC_INQUIRY_ROUTER_PATH.exists():
        fail("missing public-safe inquiry router")
    if not PUBLIC_PROOF_INDEX_PATH.exists():
        fail("missing public-safe proof index")
    if not PUBLIC_ROI_ASSUMPTION_WORKSHEET_PATH.exists():
        fail("missing public-safe ROI assumption worksheet")
    if not PUBLIC_SAFE_ONBOARDING_PLAYBOOK_PATH.exists():
        fail("missing public-safe onboarding playbook")
    if not PUBLIC_IMPLEMENTATION_SCOPE_MENU_PATH.exists():
        fail("missing public implementation scope menu")

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

    download_first_run_guide_text = DOWNLOAD_FIRST_RUN_GUIDE_PATH.read_text(encoding="utf-8").lower()
    download_first_run_guide_required_markers = (
        "public-only",
        "checkout/payment",
        "payout",
        "kyc",
        "tax",
        "bank",
        "contracts",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
        "docs/public-inquiry-router.md",
    )
    missing_download_first_run_guide_markers = [
        marker
        for marker in download_first_run_guide_required_markers
        if marker not in download_first_run_guide_text
    ]
    if missing_download_first_run_guide_markers:
        fail(
            "public-safe download-to-first-run guide is missing marker(s): "
            f"{', '.join(missing_download_first_run_guide_markers)}"
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

    buyer_fit_text = BUYER_FIT_CHECKLIST_PATH.read_text(encoding="utf-8").lower()
    buyer_fit_required_markers = (
        "public-safe",
        "checkout",
        "payment",
        "kyc",
        "tax",
        "bank",
        "contracts",
        "private repository urls",
        "customer data",
        "credentials",
        "no guaranteed roi",
    )
    missing_buyer_fit_markers = [
        marker for marker in buyer_fit_required_markers if marker not in buyer_fit_text
    ]
    if missing_buyer_fit_markers:
        fail(
            "public-safe buyer fit checklist is missing marker(s): "
            f"{', '.join(missing_buyer_fit_markers)}"
        )

    share_kit_text = PUBLIC_SHARE_KIT_PATH.read_text(encoding="utf-8").lower()
    share_kit_required_markers = (
        "public-only",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "checkout/payment",
        "kyc",
        "tax",
        "bank",
        "contracts",
        "dm",
        "email",
        "forms",
        "private outreach",
        "paid ads",
        "no guaranteed roi",
        "docs/public-proof-index.md",
    )
    missing_share_kit_markers = [
        marker for marker in share_kit_required_markers if marker not in share_kit_text
    ]
    if missing_share_kit_markers:
        fail(
            "public-safe share kit is missing marker(s): "
            f"{', '.join(missing_share_kit_markers)}"
        )

    evaluation_scorecard_text = PUBLIC_EVALUATION_SCORECARD_PATH.read_text(encoding="utf-8").lower()
    evaluation_scorecard_required_markers = (
        "public-only",
        "checkout/payment",
        "payment details",
        "payout",
        "kyc",
        "tax",
        "bank",
        "contracts",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
        "docs/public-inquiry-router.md",
    )
    missing_evaluation_scorecard_markers = [
        marker for marker in evaluation_scorecard_required_markers if marker not in evaluation_scorecard_text
    ]
    if missing_evaluation_scorecard_markers:
        fail(
            "public-safe evaluation scorecard is missing marker(s): "
            f"{', '.join(missing_evaluation_scorecard_markers)}"
        )

    inquiry_router_text = PUBLIC_INQUIRY_ROUTER_PATH.read_text(encoding="utf-8").lower()
    inquiry_router_required_markers = (
        "public-only",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "checkout/payment",
        "kyc",
        "tax",
        "bank",
        "contracts",
        "dm",
        "email",
        "forms",
        "private outreach",
        "paid ads",
        "no guaranteed roi",
        "free-lite-setup.yml",
        "free-lite-feedback.yml",
        "workflow-pack-inquiry.yml",
        "audit-pilot-inquiry.yml",
    )
    missing_inquiry_router_markers = [
        marker for marker in inquiry_router_required_markers if marker not in inquiry_router_text
    ]
    if missing_inquiry_router_markers:
        fail(
            "public-safe inquiry router is missing marker(s): "
            f"{', '.join(missing_inquiry_router_markers)}"
        )

    proof_index_text = PUBLIC_PROOF_INDEX_PATH.read_text(encoding="utf-8").lower()
    proof_index_required_markers = (
        "public-only",
        "checkout/payment",
        "kyc",
        "tax",
        "bank",
        "contracts",
        "private repository urls",
        "customer data",
        "credentials",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "no guaranteed roi",
        "docs/public-inquiry-router.md",
    )
    missing_proof_index_markers = [
        marker for marker in proof_index_required_markers if marker not in proof_index_text
    ]
    if missing_proof_index_markers:
        fail(
            "public-safe proof index is missing marker(s): "
            f"{', '.join(missing_proof_index_markers)}"
        )

    roi_assumption_text = PUBLIC_ROI_ASSUMPTION_WORKSHEET_PATH.read_text(encoding="utf-8").lower()
    roi_assumption_required_markers = (
        "public-only",
        "checkout/payment details",
        "payout",
        "kyc",
        "tax",
        "bank",
        "contracts",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
        "docs/public-inquiry-router.md",
    )
    missing_roi_assumption_markers = [
        marker for marker in roi_assumption_required_markers if marker not in roi_assumption_text
    ]
    if missing_roi_assumption_markers:
        fail(
            "public-safe ROI assumption worksheet is missing marker(s): "
            f"{', '.join(missing_roi_assumption_markers)}"
        )

    onboarding_playbook_text = PUBLIC_SAFE_ONBOARDING_PLAYBOOK_PATH.read_text(encoding="utf-8").lower()
    onboarding_playbook_required_markers = (
        "public-only",
        "checkout/payment",
        "kyc",
        "tax",
        "bank",
        "contracts",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
        "docs/public-inquiry-router.md",
    )
    missing_onboarding_playbook_markers = [
        marker for marker in onboarding_playbook_required_markers if marker not in onboarding_playbook_text
    ]
    if missing_onboarding_playbook_markers:
        fail(
            "public-safe onboarding playbook is missing marker(s): "
            f"{', '.join(missing_onboarding_playbook_markers)}"
        )

    implementation_scope_menu_text = PUBLIC_IMPLEMENTATION_SCOPE_MENU_PATH.read_text(encoding="utf-8").lower()
    implementation_scope_menu_required_markers = (
        "public-only",
        "checkout/payment",
        "payout",
        "kyc",
        "tax",
        "bank",
        "contracts",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
        "docs/public-inquiry-router.md",
    )
    missing_implementation_scope_menu_markers = [
        marker
        for marker in implementation_scope_menu_required_markers
        if marker not in implementation_scope_menu_text
    ]
    if missing_implementation_scope_menu_markers:
        fail(
            "public implementation scope menu is missing marker(s): "
            f"{', '.join(missing_implementation_scope_menu_markers)}"
        )

    cross_link_paths = {
        "README.md": ROOT / "README.md",
        "PRICING.md": ROOT / "PRICING.md",
        "docs/full-pack-public-listing.md": FULL_PACK_LISTING_PATH,
        "docs/public-release-checks.md": ROOT / "docs" / "public-release-checks.md",
    }
    for label, path in cross_link_paths.items():
        text = path.read_text(encoding="utf-8").lower()
        if "docs/public-safe-onboarding-playbook.md" not in text and "public-safe-onboarding-playbook.md" not in text:
            fail(f"{label} is missing the public-safe onboarding playbook link")
        if "docs/public-implementation-scope-menu.md" not in text and "public-implementation-scope-menu.md" not in text:
            fail(f"{label} is missing the public implementation scope menu link")
        if "docs/free-lite-download-first-run-guide.md" not in text and "free-lite-download-first-run-guide.md" not in text:
            fail(f"{label} is missing the download-to-first-run guide link")

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
