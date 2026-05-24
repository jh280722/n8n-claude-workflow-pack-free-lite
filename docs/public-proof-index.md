# Public proof index

Use this page when a reader wants evidence for the Free Lite workflow and the checkout-disabled full-pack preview without opening a private sales thread, activating checkout/payment, or sharing sensitive details.

This is a public-only proof map. It points to public files that can be checked in this repository and explains which claims still require a private, separately approved transaction or implementation review.

## Publicly verifiable proof

| Claim or reader question | Public proof to inspect | Safe interpretation |
|---|---|---|
| “Is there an importable free workflow?” | `workflows/free-lite-github-weekly-snapshot.json` | The Free Lite workflow is included in this public repo. |
| “Does it avoid posting or mutating by default?” | `scripts/validate_free_lite.py` and `docs/public-release-checks.md` | Static checks guard against common Slack/Notion/GitHub posting or write patterns in the Free Lite workflow. |
| “What should the output look like?” | `samples/sample-output.md` and `docs/free-lite-output-review-guide.md` | The public sample shows Markdown review output only; it is not a production guarantee. |
| “What should I do after a test run?” | `docs/public-evaluation-scorecard.md` | A 10-minute scorecard routes public-safe next steps without checkout/payment, private data, or guaranteed ROI claims. |
| “Can I test it safely?” | `docs/free-lite-demo-runbook.md` and `docs/free-lite-validation-preflight.md` | Start with a public repository or synthetic sample and review the Markdown before adapting anything. |
| “How do public support or feedback reports stay safe?” | `.github/ISSUE_TEMPLATE/`, `docs/public-inquiry-router.md`, `docs/public-safe-issue-examples.md`, and `SECURITY.md` | Public issues should include sanitized setup or feedback details only. |
| “What would the paid/full pack include?” | `docs/full-pack-public-listing.md`, `PRICING.md`, and `docs/buyer-fit-checklist.md` | These pages are a checkout-disabled preview and fit checklist, not active checkout or payment capture. |
| “Can I share this publicly?” | `docs/public-share-kit.md` | Share only in relevant public threads and keep the copy non-spammy and public-safe. |

## What is intentionally not public proof

The paid ZIP, private implementation details, buyer-specific support, payment flow, checkout/payment activation, payout setup, KYC, tax, bank, contracts, private repository URLs, customer data, credentials, production logs, DM/email/forms/private outreach, paid ads, and custom legal/support commitments are not included in this public proof index.

No guaranteed ROI is claimed. The Free Lite workflow and public listing pages are evaluation materials; users remain responsible for their own n8n instance, API permissions, security review, legal review, and production approvals.

## Public-safe proof request checklist

If someone asks for more proof in public, ask only for sanitized, non-sensitive context:

1. Which public file or claim they are checking.
2. Their n8n version if the import path is relevant.
3. A public test repository or synthetic sample payload.
4. The affected node name or public doc section.
5. Redacted symptom text or a public-safe screenshot with tokens and credentials removed.

Do not ask for or post tokens, API keys, credentials, private repository URLs, customer data, production logs, private workflow exports, confidential screenshots, checkout/payment details, KYC, tax, bank, contracts, DM/email/forms/private outreach details, paid ads plans, legal commitments, support/refund promises, or guaranteed ROI requirements.

## Best next public link

If the reader has already run Free Lite, send them to the public evaluation scorecard: `docs/public-evaluation-scorecard.md`. If they are not sure which issue form to use, send them to the public inquiry router: `docs/public-inquiry-router.md`.
