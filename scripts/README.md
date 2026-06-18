# Scripts landing guide

Use this page if you landed directly in the `scripts/` folder while checking how the Free Lite workflow is validated.

## What is here

- `validate_free_lite.py` is a static public-safety validator.
- `clone_run_receipt.py` runs the local validator plus `git diff --check`, then prints a clone-run public receipt skeleton for a sanitized setup or feedback issue.
- These scripts check that the n8n workflow JSON is parseable, still uses read-only GitHub activity, keeps `GITHUB_TOKEN` optional, keeps public issue forms and support docs wired, and blocks common posting/mutating integrations or secret-like markers.
- They do not need secrets, network access, private repository data, checkout/payment setup, payout setup, KYC, tax, bank, Stripe, contract details, or client/customer data.

## Safe local check

From the repository root:

```bash
python3 scripts/validate_free_lite.py
git diff --check
python3 scripts/clone_run_receipt.py
```

If validation fails, fix the public docs/workflow locally before opening a public issue or pull request. If you use `clone_run_receipt.py`, paste only the sanitized clone-run public receipt fields that match your own public or redacted test. Keep any report public-only: no tokens, credentials, private repository URLs, customer data, production logs, checkout/payment details, payout/wallet/bank/Stripe details, tax/KYC/contract details, DM/email/forms/private outreach requests, paid ads instructions, or guaranteed ROI assumptions.

## Next public route

- Contribution boundary and PR checklist: `../CONTRIBUTING.md`
- Release/support checklist: `../docs/public-release-checks.md`
- Clone-to-first-success guide and clone-run public receipt: `../docs/clone-to-first-success.md`
- Setup issue route: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-setup.yml>
- Feedback route: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-feedback.yml>
- Public route chooser: `../docs/public-inquiry-router.md`

This folder is validation-only. It does not activate checkout/payment, capture payment, request payout setup, require KYC/tax/bank/contract information, or provide private implementation support.
