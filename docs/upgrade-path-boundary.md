# Public-safe upgrade path boundary

Use this page when Free Lite users ask whether they should stay on the free workflow, evaluate the draft template pack, or scope an AI workflow audit/pilot.

## What can stay public

Public GitHub issues are safe for high-level, sanitized fit questions such as:

- whether the Free Lite workflow imported successfully;
- which public repository or synthetic sample was used;
- which next integration is most useful: Slack, Discord, Notion, or Claude-style narrative review;
- whether the user wants self-serve templates, an audit checklist, or a scoped pilot discussion;
- sanitized constraints such as team size range, preferred self-hosted tools, and review-first workflow goals.

Keep examples public-safe. Do not include tokens, private repository URLs, customer data, production logs, credentials, security incident details, procurement/legal documents, checkout/payment information, KYC, tax, bank, wallet, or payout details.

## Free Lite vs. draft paid paths

| Path | Public-safe signal | Do not request publicly |
|---|---|---|
| Free Lite | Import friction, markdown output feedback, public repo smoke-test notes | Tokens, private repository URLs, customer data, production logs |
| Starter/Pro template pack | Which workflow family is needed and whether the user can self-host n8n | Checkout, payment, invoice, KYC, tax, bank, wallet, or payout details |
| AI Workflow Audit beta | Sanitized automation goals, tools in use at a category level, review/security requirements | Credentials, client/private data, workplace exports, legal commitments |
| Implementation pilot | A narrow draft/review-mode outcome after an approved private scope exists | Production access, private outreach details, guaranteed ROI promises |

## Safe first response for inquiries

If someone opens a public inquiry, answer with a short public-safe triage request:

```text
Thanks — please keep this public-safe. Could you share:
1. Which path you are evaluating: Free Lite, template pack, audit, or pilot?
2. Your n8n setup at a high level: self-hosted/cloud/unknown, no URLs needed.
3. The workflow outcome you want in one sentence.
4. Whether you can test with a public repo or synthetic sample first.

Please do not post tokens, private repository URLs, customer data, production logs, credentials, checkout/payment/KYC/tax/bank/payout details, or legal/procurement documents here.
```

## Boundary for paid claims

- No guaranteed ROI.
- No promise that a workflow is production-ready without the buyer's own security and permissions review.
- No checkout, payment, invoice, KYC, tax, bank, wallet, payout, or contract handling in public GitHub issues.
- No request for credentials, private repository URLs, customer data, proprietary workflow exports, or production logs in public.
- If a paid engagement is approved later, sensitive implementation details should move to an approved private channel before any private-data work begins.
