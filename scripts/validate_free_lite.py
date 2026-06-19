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
WORKFLOW_LANDING_PATH = ROOT / "workflows" / "README.md"
SCRIPTS_LANDING_PATH = ROOT / "scripts" / "README.md"
CLONE_RECEIPT_HELPER_PATH = ROOT / "scripts" / "clone_run_receipt.py"
QUICKSTART_PATH = ROOT / "QUICKSTART.md"
ISSUE_TEMPLATE_DIR = ROOT / ".github" / "ISSUE_TEMPLATE"
ISSUE_TEMPLATE_CONFIG_PATH = ISSUE_TEMPLATE_DIR / "config.yml"
TROUBLESHOOTING_FAQ_PATH = ROOT / "docs" / "free-lite-troubleshooting-faq.md"
DOWNLOAD_FIRST_RUN_GUIDE_PATH = ROOT / "docs" / "free-lite-download-first-run-guide.md"
CLONE_FIRST_SUCCESS_PATH = ROOT / "docs" / "clone-to-first-success.md"
PUBLIC_SAFE_ISSUE_EXAMPLES_PATH = ROOT / "docs" / "public-safe-issue-examples.md"
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
PUBLIC_SAMPLE_OUTPUT_NEXT_STEPS_PATH = ROOT / "docs" / "public-sample-output-next-steps.md"
CONTRIBUTING_PATH = ROOT / "CONTRIBUTING.md"

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
    if not WORKFLOW_LANDING_PATH.exists():
        fail("missing traffic-aware workflow landing guide")
    if not SCRIPTS_LANDING_PATH.exists():
        fail("missing traffic-aware scripts landing guide")
    if not CLONE_RECEIPT_HELPER_PATH.exists():
        fail("missing clone-run public receipt helper")
    if not QUICKSTART_PATH.exists():
        fail("missing top-level clone-first quickstart")
    if not DOWNLOAD_FIRST_RUN_GUIDE_PATH.exists():
        fail("missing public-safe download-to-first-run guide")
    if not CLONE_FIRST_SUCCESS_PATH.exists():
        fail("missing public-safe clone-to-first-success guide")
    if not PUBLIC_SAFE_ISSUE_EXAMPLES_PATH.exists():
        fail("missing public-safe issue examples")

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
    if not PUBLIC_SAMPLE_OUTPUT_NEXT_STEPS_PATH.exists():
        fail("missing public sample output next steps")
    if not CONTRIBUTING_PATH.exists():
        fail("missing public-safe contribution guide")

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

    workflow_landing_text = WORKFLOW_LANDING_PATH.read_text(encoding="utf-8").lower()
    workflow_landing_required_markers = (
        "public-only",
        "workflows/free-lite-github-weekly-snapshot.json",
        "github_token",
        "docs/free-lite-download-first-run-guide.md",
        "docs/free-lite-import-checklist.md",
        "docs/public-inquiry-router.md",
        "docs/public-safe-issue-examples.md",
        "free-lite-setup.yml",
        "free-lite-feedback.yml",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "checkout/payment",
        "payout/wallet/bank/stripe",
        "tax/kyc/contract",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
    )
    missing_workflow_landing_markers = [
        marker for marker in workflow_landing_required_markers if marker not in workflow_landing_text
    ]
    if missing_workflow_landing_markers:
        fail(
            "traffic-aware workflow landing guide is missing marker(s): "
            f"{', '.join(missing_workflow_landing_markers)}"
        )

    scripts_landing_text = SCRIPTS_LANDING_PATH.read_text(encoding="utf-8").lower()
    scripts_landing_required_markers = (
        "public-safety validator",
        "python3 scripts/validate_free_lite.py",
        "clone_run_receipt.py",
        "python3 scripts/clone_run_receipt.py",
        "clone-run public receipt",
        "git diff --check",
        "contributing.md",
        "docs/public-release-checks.md",
        "docs/clone-to-first-success.md",
        "docs/public-inquiry-router.md",
        "free-lite-setup.yml",
        "free-lite-feedback.yml",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "checkout/payment",
        "payout/wallet/bank/stripe",
        "tax/kyc/contract",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
    )
    missing_scripts_landing_markers = [
        marker for marker in scripts_landing_required_markers if marker not in scripts_landing_text
    ]
    if missing_scripts_landing_markers:
        fail(
            "traffic-aware scripts landing guide is missing marker(s): "
            f"{', '.join(missing_scripts_landing_markers)}"
        )

    quickstart_text = QUICKSTART_PATH.read_text(encoding="utf-8").lower()
    quickstart_required_markers = (
        "public-only",
        "python3 scripts/validate_free_lite.py",
        "git diff --check",
        "python3 scripts/clone_run_receipt.py",
        "workflows/free-lite-github-weekly-snapshot.json",
        "samples/sample-output.md",
        "docs/free-lite-output-review-guide.md",
        "docs/free-lite-import-checklist.md",
        "docs/free-lite-troubleshooting-faq.md",
        "docs/public-sample-output-next-steps.md",
        "docs/public-implementation-scope-menu.md",
        "docs/public-safe-onboarding-playbook.md",
        "docs/public-inquiry-router.md",
        "docs/public-safe-issue-examples.md",
        "free-lite-setup.yml",
        "free-lite-feedback.yml",
        "workflow-pack-inquiry.yml",
        "audit-pilot-inquiry.yml",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "checkout/payment",
        "payout/wallet/bank/stripe",
        "tax/kyc/contract",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
    )
    missing_quickstart_markers = [
        marker for marker in quickstart_required_markers if marker not in quickstart_text
    ]
    if missing_quickstart_markers:
        fail(
            "top-level clone-first quickstart is missing marker(s): "
            f"{', '.join(missing_quickstart_markers)}"
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

    clone_first_success_text = CLONE_FIRST_SUCCESS_PATH.read_text(encoding="utf-8").lower()
    clone_first_success_required_markers = (
        "public-only",
        "python3 scripts/validate_free_lite.py",
        "python3 scripts/clone_run_receipt.py",
        "git diff --check",
        "workflows/free-lite-github-weekly-snapshot.json",
        "samples/sample-output.md",
        "docs/free-lite-output-review-guide.md",
        "docs/public-evaluation-scorecard.md",
        "docs/free-lite-import-checklist.md",
        "docs/free-lite-troubleshooting-faq.md",
        "docs/public-inquiry-router.md",
        "docs/public-safe-issue-examples.md",
        "clone-run public receipt",
        "clone_run_receipt.py",
        "n8n version",
        "public test repository",
        "redacted error text",
        "free-lite-setup.yml",
        "free-lite-feedback.yml",
        "workflow-pack-inquiry.yml",
        "audit-pilot-inquiry.yml",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "checkout/payment",
        "payout/wallet/bank/stripe",
        "tax/kyc/contract",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
    )
    missing_clone_first_success_markers = [
        marker for marker in clone_first_success_required_markers if marker not in clone_first_success_text
    ]
    if missing_clone_first_success_markers:
        fail(
            "public-safe clone-to-first-success guide is missing marker(s): "
            f"{', '.join(missing_clone_first_success_markers)}"
        )

    public_safe_issue_examples_text = PUBLIC_SAFE_ISSUE_EXAMPLES_PATH.read_text(encoding="utf-8").lower()
    public_safe_issue_examples_required_markers = (
        "public-only",
        "free-lite-setup.yml",
        "free-lite-feedback.yml",
        "workflow-pack-inquiry.yml",
        "audit-pilot-inquiry.yml",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "checkout/payment",
        "payout/wallet/bank/stripe",
        "tax/kyc/contract",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
    )
    missing_public_safe_issue_examples_markers = [
        marker
        for marker in public_safe_issue_examples_required_markers
        if marker not in public_safe_issue_examples_text
    ]
    if missing_public_safe_issue_examples_markers:
        fail(
            "public-safe issue examples are missing marker(s): "
            f"{', '.join(missing_public_safe_issue_examples_markers)}"
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

    sample_output_next_steps_text = PUBLIC_SAMPLE_OUTPUT_NEXT_STEPS_PATH.read_text(encoding="utf-8").lower()
    sample_output_next_steps_required_markers = (
        "public-only",
        "samples/sample-output.md",
        "docs/free-lite-output-review-guide.md",
        "docs/public-evaluation-scorecard.md",
        "docs/public-inquiry-router.md",
        "free-lite-feedback.yml",
        "workflow-pack-inquiry.yml",
        "audit-pilot-inquiry.yml",
        "checkout/payment",
        "payout/wallet/bank/stripe",
        "tax/kyc/contract",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
    )
    missing_sample_output_next_steps_markers = [
        marker for marker in sample_output_next_steps_required_markers if marker not in sample_output_next_steps_text
    ]
    if missing_sample_output_next_steps_markers:
        fail(
            "public sample output next steps is missing marker(s): "
            f"{', '.join(missing_sample_output_next_steps_markers)}"
        )

    contributing_text = CONTRIBUTING_PATH.read_text(encoding="utf-8").lower()
    contributing_required_markers = (
        "public-only",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "checkout/payment",
        "payout/wallet/bank/stripe",
        "tax/kyc/contract",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
        "python3 scripts/validate_free_lite.py",
        "git diff --check",
        "docs/public-inquiry-router.md",
    )
    missing_contributing_markers = [
        marker for marker in contributing_required_markers if marker not in contributing_text
    ]
    if missing_contributing_markers:
        fail(
            "public-safe contribution guide is missing marker(s): "
            f"{', '.join(missing_contributing_markers)}"
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
        if label in {"README.md", "docs/public-release-checks.md"}:
            if "quickstart.md" not in text:
                fail(f"{label} is missing the top-level clone-first quickstart link")
            if "docs/clone-to-first-success.md" not in text and "clone-to-first-success.md" not in text:
                fail(f"{label} is missing the clone-to-first-success guide link")
            if "clone-run public receipt" not in text:
                fail(f"{label} is missing the clone-run public receipt marker")
            if "scripts/clone_run_receipt.py" not in text and "clone_run_receipt.py" not in text:
                fail(f"{label} is missing the clone-run receipt helper link")
        if "docs/public-safe-issue-examples.md" not in text and "public-safe-issue-examples.md" not in text:
            fail(f"{label} is missing the public-safe issue examples link")
        if "docs/public-sample-output-next-steps.md" not in text and "public-sample-output-next-steps.md" not in text:
            fail(f"{label} is missing the public sample output next steps link")

    readme_text = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    release_checks_text = (ROOT / "docs" / "public-release-checks.md").read_text(encoding="utf-8").lower()
    if "contributing.md" not in readme_text:
        fail("README.md is missing the public-safe contribution guide link")
    if "workflows/readme.md" not in readme_text:
        fail("README.md is missing the traffic-aware workflow landing guide link")
    if "scripts/readme.md" not in readme_text:
        fail("README.md is missing the traffic-aware scripts landing guide link")
    if "scripts/clone_run_receipt.py" not in readme_text:
        fail("README.md is missing the clone-run receipt helper link")
    if "quickstart.md" not in readme_text:
        fail("README.md is missing the top-level clone-first quickstart link")
    if "contributing.md" not in release_checks_text:
        fail("docs/public-release-checks.md is missing the public-safe contribution guide check")
    if "workflows/readme.md" not in release_checks_text or "scripts/readme.md" not in release_checks_text:
        fail("docs/public-release-checks.md is missing traffic-aware landing guide checks")
    if "scripts/clone_run_receipt.py" not in release_checks_text:
        fail("docs/public-release-checks.md is missing the clone-run receipt helper check")
    if "quickstart.md" not in release_checks_text:
        fail("docs/public-release-checks.md is missing the top-level clone-first quickstart check")
    readme_path_router_required_markers = (
        "choose your next safe path",
        "public-only",
        "free-lite-setup.yml",
        "free-lite-feedback.yml",
        "workflow-pack-inquiry.yml",
        "audit-pilot-inquiry.yml",
        "tokens",
        "credentials",
        "private repository urls",
        "customer data",
        "checkout/payment details",
        "payout/wallet/bank/stripe",
        "tax/kyc/contract",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
    )
    missing_readme_path_router_markers = [
        marker for marker in readme_path_router_required_markers if marker not in readme_text
    ]
    if missing_readme_path_router_markers:
        fail(
            "README safe-path router is missing marker(s): "
            f"{', '.join(missing_readme_path_router_markers)}"
        )

    missing_templates = sorted(
        name for name in REQUIRED_ISSUE_TEMPLATES if not (ISSUE_TEMPLATE_DIR / name).exists()
    )
    if missing_templates:
        fail(f"missing public issue template(s): {', '.join(missing_templates)}")

    issue_template_config_text = ISSUE_TEMPLATE_CONFIG_PATH.read_text(encoding="utf-8").lower()
    issue_template_config_required_markers = (
        "blank_issues_enabled: false",
        "docs/clone-to-first-success.md",
        "clone-run public receipt",
        "docs/free-lite-download-first-run-guide.md",
        "docs/public-inquiry-router.md",
        "docs/public-sample-output-next-steps.md",
        "docs/public-safe-issue-examples.md",
        "security.md",
        "public-safe",
        "tokens",
        "private data",
        "checkout/payment",
        "dm/email/forms",
        "private outreach",
    )
    missing_issue_template_config_markers = [
        marker
        for marker in issue_template_config_required_markers
        if marker not in issue_template_config_text
    ]
    if missing_issue_template_config_markers:
        fail(
            "public issue chooser config is missing marker(s): "
            f"{', '.join(missing_issue_template_config_markers)}"
        )

    setup_template_text = (ISSUE_TEMPLATE_DIR / "free-lite-setup.yml").read_text(encoding="utf-8").lower()
    setup_template_required_markers = (
        "docs/clone-to-first-success.md",
        "clone-run public receipt",
        "python3 scripts/validate_free_lite.py",
        "git diff --check",
        "local validation",
        "public test repository",
        "final markdown field",
        "sample-output comparison",
        "next safe route",
        "checkout/payment details",
        "payout/wallet/bank/stripe details",
        "tax/kyc/contract details",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
    )
    missing_setup_template_markers = [
        marker for marker in setup_template_required_markers if marker not in setup_template_text
    ]
    if missing_setup_template_markers:
        fail(
            "Free Lite setup issue template is missing clone-run receipt marker(s): "
            f"{', '.join(missing_setup_template_markers)}"
        )

    feedback_template_text = (ISSUE_TEMPLATE_DIR / "free-lite-feedback.yml").read_text(encoding="utf-8").lower()
    feedback_template_required_markers = (
        "docs/clone-to-first-success.md",
        "clone-run public receipt",
        "local validation",
        "public test repository",
        "final `markdown` field",
        "sample-output comparison",
        "next safe route",
        "checkout/payment details",
        "payout/wallet/bank/stripe details",
        "tax/kyc/contract details",
        "dm/email/forms",
        "private outreach",
        "paid ads",
        "guaranteed roi",
    )
    missing_feedback_template_markers = [
        marker for marker in feedback_template_required_markers if marker not in feedback_template_text
    ]
    if missing_feedback_template_markers:
        fail(
            "Free Lite feedback issue template is missing clone-run receipt marker(s): "
            f"{', '.join(missing_feedback_template_markers)}"
        )

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
