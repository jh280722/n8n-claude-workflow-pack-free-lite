# QUICKSTART — cloned repo to one public-safe Free Lite run

Use this if you cloned the repository and want the shortest offline path before opening a public issue. Keep everything public-only: do not paste tokens, credentials, private repository URLs, customer data, production logs, internal screenshots, checkout/payment details, payout/wallet/bank/Stripe details, tax/KYC/contract details, DM/email/forms/private outreach requests, paid ads instructions, or guaranteed ROI assumptions.

## 1. Run local public-safety checks

From the repository root:

```bash
python3 scripts/validate_free_lite.py
git diff --check
python3 scripts/clone_run_receipt.py
```

Expected validator result:

```text
OK: Free Lite workflow JSON and public issue forms pass static public-safety checks.
```

`clone_run_receipt.py` prints a clone-run public receipt skeleton. Keep it local until you add only public-safe n8n/import results.

## 2. Import and run one safe workflow test

1. Open `workflows/free-lite-github-weekly-snapshot.json`.
2. Import it into your own n8n instance.
3. For the first run, leave `GITHUB_TOKEN` blank unless you need higher public API rate limits.
4. Use a public test repository such as `n8n-io/n8n`.
5. Confirm the final node returns a `markdown` field.
6. Compare the result with `samples/sample-output.md` and `docs/free-lite-output-review-guide.md`.

## 3. Choose the next public route

- Setup/import failed: read `docs/free-lite-import-checklist.md` and `docs/free-lite-troubleshooting-faq.md`, then open `free-lite-setup.yml`.
- Output was unclear: read `docs/public-sample-output-next-steps.md`, then open `free-lite-feedback.yml`.
- You want template-pack fit only: read `docs/public-implementation-scope-menu.md`, then open `workflow-pack-inquiry.yml`.
- You want an audit/pilot fit check: read `docs/public-safe-onboarding-playbook.md`, then open `audit-pilot-inquiry.yml`.
- Unsure which route fits: use `docs/public-inquiry-router.md` and `docs/public-safe-issue-examples.md`.

Public issue links:

- Free Lite setup question: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-setup.yml>
- Free Lite feedback / integration request: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-feedback.yml>
- Template/customization inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=workflow-pack-inquiry.yml>
- Workflow audit / pilot inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=audit-pilot-inquiry.yml>

## Boundary

This quickstart does not activate checkout/payment, capture payment, request payout/wallet/bank/Stripe setup, require KYC/tax/bank/contract information, create a DM/email/forms/private outreach flow, buy paid ads, or make guaranteed ROI claims. Use public repositories or redacted sample data only.
