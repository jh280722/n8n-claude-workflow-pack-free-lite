# Public evaluation scorecard

Use this scorecard after a Free Lite test run to decide whether the repo is enough, whether to open a public issue, or whether the checkout-disabled full-pack preview is relevant.

This is a public-only evaluation aid. It does not activate checkout/payment, collect payment details, request payout setup, KYC, tax, bank, contracts, credentials, private repository URLs, customer data, production logs, DM/email/forms/private outreach, paid ads, or any guaranteed ROI commitment.

## 10-minute scorecard

Score each row from 0 to 2 using only a public repository or synthetic sample payload.

| Check | 0 | 1 | 2 | Public proof or next link |
|---|---:|---:|---:|---|
| Import | Workflow did not import | Imported after manual edits | Imported cleanly | `docs/free-lite-import-checklist.md` |
| Data fetch | No public GitHub activity returned | Partial activity returned | Commits, merged PRs, and closed issues appeared | `workflows/free-lite-github-weekly-snapshot.json` |
| Markdown usefulness | Output was not reviewable | Useful with edits | Useful enough for a weekly status draft | `samples/sample-output.md` and `docs/free-lite-output-review-guide.md` |
| Safety fit | Requires private data to evaluate | Can use redacted/synthetic data | Works with public/sanitized data only | `SECURITY.md` and `docs/public-proof-index.md` |
| Next workflow pull | No need beyond Free Lite | One adjacent integration needed | Multiple review-first workflows or an audit backlog would help | `docs/full-pack-public-listing.md` and `docs/buyer-fit-checklist.md` |

## Interpreting the score

| Total | Public-safe interpretation | Suggested next action |
|---:|---|---|
| 0–3 | Free Lite is not yet proving value for this setup. | Open a sanitized setup issue with n8n version, node name, and redacted symptom text. |
| 4–6 | The workflow is directionally useful but needs clearer examples or adaptation notes. | Open a public feedback issue and include only public repo or synthetic sample context. |
| 7–10 | The pattern is useful enough to evaluate a fuller template pack or audit path. | Review the checkout-disabled listing preview, buyer fit checklist, proof index, and public inquiry router before opening a public inquiry. |

## Safe public issue template

Copy this into the closest guided public issue form only after removing anything sensitive:

```markdown
Scorecard total: __/10
n8n version: __
Test data: public repo or synthetic sample only
Best result: __
Main friction: __
Next workflow interest: Free Lite / Starter-Pro template pack / audit / pilot / unsure
Sensitive details removed: yes
```

Do not include tokens, API keys, credentials, private repository URLs, customer data, production logs, internal screenshots, private workflow exports, checkout/payment details, payout/wallet/bank/Stripe details, KYC, tax, contracts, DM/email/forms/private outreach details, paid ads plans, legal/support/refund promises, or guaranteed ROI requirements.

## Where to go next

- If setup failed: `docs/free-lite-troubleshooting-faq.md`
- If output quality is the question: `docs/free-lite-output-review-guide.md`
- If the buyer fit is unclear: `docs/buyer-fit-checklist.md`
- If public proof is needed first: `docs/public-proof-index.md`
- If the right issue form is unclear: `docs/public-inquiry-router.md`
