# Public sample output next steps

Use this page after reading `samples/sample-output.md` or running the Free Lite workflow once. The goal is to turn a quick sample-output check into the safest public next step without asking for secrets, private repository details, checkout/payment details, or private outreach.

## 1. Compare the sample to your public-only test run

Start with a public repository or a synthetic sample. Do not paste tokens, credentials, private repository URLs, customer data, production logs, internal incidents, payment details, payout/wallet/bank/Stripe details, tax/KYC/contract details, or proprietary workflow exports into public issues.

| Question | Public-safe check | If the answer is "yes" |
|---|---|---|
| Did the workflow import and run? | Confirm the final node returned a `markdown` field. | Use `docs/free-lite-output-review-guide.md` to score usefulness. |
| Does the sample output cover your weekly status needs? | Compare counts, notable commits, merged PRs, closed issues, and follow-up questions. | Open `free-lite-feedback.yml` with sanitized notes. |
| Do you need a Claude narrative, Slack/Notion delivery, or PR risk digest? | Name the workflow family only; do not share private repo names or credentials. | Use `workflow-pack-inquiry.yml` or `docs/public-implementation-scope-menu.md`. |
| Do you need help deciding between template pack vs audit/pilot? | Use ranges/placeholders, not private revenue, payroll, customer, or repo data. | Use `audit-pilot-inquiry.yml` or `docs/public-evaluation-scorecard.md`. |

## 2. Choose the public route

- Setup/import problem: open a [Free Lite setup question](https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-setup.yml) with n8n version, affected node, and redacted symptom only.
- Output usefulness feedback: open [Free Lite feedback / integration request](https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-feedback.yml) with what the sample output missed and whether you tested a public repo or synthetic payload.
- Template/customization fit: open [Template/customization inquiry](https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=workflow-pack-inquiry.yml) using public-only workflow-family needs.
- Audit/pilot uncertainty: open [Workflow audit / pilot inquiry](https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=audit-pilot-inquiry.yml) using sanitized goals and placeholders only.

If you are unsure, use `docs/public-inquiry-router.md` before posting.

## 3. Keep the boundary intact

This repo is checkout-disabled and public-only. Do not request or provide checkout/payment activation, payment capture, payout/wallet/bank/Stripe details, tax/KYC/contract details, DM/email/forms/private outreach, paid ads, legal commitments, production access, or guaranteed ROI. No guaranteed ROI is offered; use `docs/public-roi-assumption-worksheet.md` only for rough public placeholder estimates.
