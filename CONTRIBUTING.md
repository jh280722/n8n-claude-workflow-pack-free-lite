# Contributing safely

Thanks for helping test the Free Lite n8n workflow. This repository is intentionally public, so every issue, pull request, screenshot, log snippet, and example must stay public-safe.

## Public-only contribution boundary

You can contribute:

- documentation fixes for the Free Lite workflow;
- reproducible setup notes using a public repository such as `n8n-io/n8n`;
- sanitized sample-output improvements based on `samples/sample-output.md`;
- validator improvements that keep the workflow read-only and review-first;
- issue-form or routing improvements that help users avoid sharing secrets.

Do not include or request:

- tokens, API keys, credentials, cookies, SSH keys, webhook URLs, or production logs;
- private repository URLs, customer data, internal incident details, proprietary workflow exports, or private screenshots;
- checkout/payment details, payout/wallet/bank/Stripe details, tax/KYC/contract details, invoices, legal commitments, refund promises, or procurement details;
- DM/email/forms/private outreach requests, paid ads instructions, platform-fee steps, or guaranteed ROI claims.

If a contribution needs private data to reproduce, reduce it to a public repo or synthetic sample first. If that is not possible, describe the symptom at a high level and stop before posting private details.

## Before opening a public issue

1. Read `docs/free-lite-download-first-run-guide.md` if you downloaded the release ZIP.
2. Read `docs/free-lite-troubleshooting-faq.md` if import, GitHub API, or output generation failed.
3. Compare your output with `samples/sample-output.md` and `docs/free-lite-output-review-guide.md`.
4. Use `docs/public-inquiry-router.md` to choose the right public issue form.
5. Redact details until the issue can be understood without tokens, credentials, private repository URLs, customer data, checkout/payment details, tax/KYC/contract details, DM/email/forms, or private outreach.

## Before opening a pull request

Run the local static checks from the repository root:

```bash
python3 scripts/validate_free_lite.py
git diff --check
```

For docs-only changes, also scan your added text for secret-like strings before pushing. A safe PR description should include:

- what public-safe route or setup step changed;
- which public docs or issue forms were updated;
- the exact validation commands you ran;
- confirmation that no tokens, credentials, private repository URLs, customer data, checkout/payment details, payout/wallet/bank/Stripe details, tax/KYC/contract details, DM/email/forms/private outreach, paid ads, or guaranteed ROI claims were added.

## Good public test data

Use public or synthetic examples only:

- public repo name: `n8n-io/n8n` or another public repository you are allowed to reference;
- n8n version and node name;
- sanitized error text with secrets removed;
- whether the final `markdown` field appeared;
- a short note on which public guide you followed.

If you are evaluating the draft paid pack, keep the discussion at the public-safe level using `docs/public-implementation-scope-menu.md`, `docs/public-proof-index.md`, and `docs/full-pack-public-listing.md`. This repo does not activate checkout/payment, collect payout details, accept KYC/tax/bank/contract information, or promise guaranteed ROI.
