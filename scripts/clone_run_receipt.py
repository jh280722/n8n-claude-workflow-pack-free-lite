#!/usr/bin/env python3
"""Build a public-safe clone-run receipt for Free Lite cloners.

The helper is intentionally local-only: it runs static checks, does not need
network access, and prints a Markdown receipt skeleton that should be sanitized
before posting to a public GitHub issue.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_free_lite.py"

SAFETY_REMINDER = (
    "Before posting, remove tokens, credentials, private repository URLs, "
    "customer data, production logs, internal screenshots, checkout/payment "
    "details, payout/wallet/bank/Stripe details, tax/KYC/contract details, "
    "DM/email/forms/private outreach requests, paid ads instructions, and "
    "guaranteed ROI assumptions."
)

NEXT_PUBLIC_ROUTES = (
    (
        "Free Lite setup question",
        "https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-setup.yml",
    ),
    (
        "Free Lite feedback / integration request",
        "https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-feedback.yml",
    ),
    (
        "Template/customization inquiry",
        "https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=workflow-pack-inquiry.yml",
    ),
    (
        "Workflow audit / pilot inquiry",
        "https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=audit-pilot-inquiry.yml",
    ),
)


def run_check(command: list[str]) -> tuple[str, str]:
    """Run a local check and return (status, compact_output)."""
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=60,
        )
    except Exception as exc:  # pragma: no cover - defensive CLI path
        return "failed", f"{type(exc).__name__}: {exc}"

    output = " ".join(completed.stdout.strip().split())
    if not output:
        output = "no output"
    if len(output) > 240:
        output = output[:237] + "..."
    return ("passed" if completed.returncode == 0 else "failed", output)


def build_receipt(args: argparse.Namespace, validator_status: str, diff_status: str) -> str:
    public_repo = args.public_test_repository or "owner/repo or private repo tested; name redacted"
    n8n_version = args.n8n_version or "unknown"
    import_result = args.import_result or "not tried yet"
    markdown_result = args.final_markdown or "not checked yet"
    comparison = args.sample_output_comparison or "not compared yet"
    next_route = args.next_safe_route or "setup help / output feedback / template-pack fit / audit-pilot fit"

    return f"""### Clone-run public receipt

- n8n version: {n8n_version}
- Free Lite source: cloned repo
- Local validation: `python3 scripts/validate_free_lite.py` {validator_status}; `git diff --check` {diff_status}
- Public test repository: {public_repo}
- `GITHUB_TOKEN`: blank / optional higher-rate-limit token used locally, not shared
- Import result: {import_result}
- Final `markdown` field appeared: {markdown_result}
- Sample-output comparison: {comparison}
- Node that failed, if any: {args.failed_node or "none / not checked"}
- Redacted error text, if any: {args.redacted_error or "none"}
- Next safe route requested: {next_route}
"""


def build_route_block() -> str:
    lines = ["### Next public issue routes"]
    lines.extend(f"- {label}: {url}" for label, url in NEXT_PUBLIC_ROUTES)
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run local Free Lite checks and print a public-safe clone-run receipt skeleton."
    )
    parser.add_argument("--n8n-version", default="", help="Optional public-safe n8n version, e.g. 1.90.0")
    parser.add_argument(
        "--public-test-repository",
        default="",
        help="Use owner/repo only for a public repo; otherwise leave blank and redact in the issue.",
    )
    parser.add_argument("--import-result", default="", help="Optional: succeeded, failed, or not tried yet")
    parser.add_argument("--final-markdown", default="", help="Optional: yes, no, not sure, or did not reach final node")
    parser.add_argument("--sample-output-comparison", default="", help="Optional: matches, partially matches, unclear")
    parser.add_argument("--failed-node", default="", help="Optional public-safe node name only")
    parser.add_argument("--redacted-error", default="", help="Optional sanitized, redacted error summary")
    parser.add_argument("--next-safe-route", default="", help="Optional: setup help, output feedback, template-pack fit, audit-pilot fit")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    validator_status, validator_output = run_check([sys.executable, str(VALIDATOR)])
    diff_status, diff_output = run_check(["git", "diff", "--check"])

    print(build_receipt(args, validator_status, diff_status))
    print("### Local check output")
    print(f"- Validator: {validator_status} — {validator_output}")
    print(f"- Whitespace diff check: {diff_status} — {diff_output}")
    print(f"\n{build_route_block()}")
    print(f"\nSafety reminder: {SAFETY_REMINDER}")

    return 0 if validator_status == "passed" and diff_status == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
