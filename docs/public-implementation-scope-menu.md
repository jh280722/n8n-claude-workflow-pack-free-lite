# Public implementation scope menu

Use this public-only menu after a Free Lite run, buyer-fit check, or ROI assumption worksheet when you need to decide which next step is safe to discuss in public.

It is intentionally checkout/payment-disabled: it does not collect payment details, activate checkout, request payout data, or ask for KYC, tax, bank, wallet, Stripe, contracts, tokens, credentials, private repository URLs, customer data, production logs, DM/email/forms, private outreach, paid ads, or guaranteed ROI assumptions.

## 1. Pick the smallest useful next step

| Public signal you can share safely | Better-fit lane | Public-only next action |
|---|---|---|
| “I downloaded the release ZIP and have not run it yet.” | Free Lite first-run path | Use `docs/free-lite-download-first-run-guide.md` to complete one public-repo run before opening a setup, feedback, or paid-scope issue. |
| “I imported Free Lite and want more workflow templates.” | Starter template pack | Open the template/customization issue with n8n version, public/synthetic test context, and the workflow families you want. |
| “I want reusable setup notes, demos, and adaptation worksheets.” | Pro template pack | Add public-safe constraints: self-hosted vs cloud n8n, target integrations, and which docs/examples you need. |
| “I am not sure what to automate first.” | AI Workflow Audit beta | Share sanitized workflow categories, team size range, current manual-review bottleneck, and what a useful backlog would include. |
| “We already know the first workflow to implement.” | Later implementation pilot | Do not post private details publicly. Use the public issue only to state the general workflow family and request approved private scoping later. |
| “I only need help debugging Free Lite import/output.” | Free Lite support path | Use setup/feedback issue forms and keep examples public-repo or synthetic only. |

## 2. What to include in a public issue

Keep it short and non-sensitive:

1. Lane: `Free Lite`, `Starter`, `Pro`, `Audit`, or `Pilot later`.
2. n8n environment type: self-hosted, n8n Cloud, or still deciding.
3. Test input type: public repository, synthetic sample payload, or redacted local test.
4. Workflow family: GitHub weekly summary, PR review, Slack/Notion brief, meeting actions, KB/RAG gaps, audit backlog, ROI assumptions, lead-fit/proposal triage, or another broad category.
5. Desired output format: Markdown, checklist, Slack-ready draft, Notion-ready draft, CSV, or JSON.
6. Public-safe blocker: import friction, unclear docs, missing workflow family, unclear pricing lane, or needs private scoping later.

## 3. What not to include publicly

Do not post:

- tokens, credentials, private repository URLs, customer data, production logs, internal screenshots, private workflow exports, or proprietary prompts;
- checkout/payment details, invoices, payout/wallet/bank/Stripe details, tax/KYC information, contracts, procurement/legal documents, or support/refund/SLA requests;
- DM/email/forms/private outreach requests, paid ads instructions, private contact information, or guaranteed ROI claims.

If the conversation needs private implementation data, stop at a sanitized public issue and wait for a separately approved private channel and commercial scope.

## 4. Route to the right public form

- Template/customization inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=workflow-pack-inquiry.yml>
- Audit/pilot inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=audit-pilot-inquiry.yml>
- Free Lite setup question: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-setup.yml>
- Free Lite feedback/integration request: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-feedback.yml>

If you are unsure, start with the public inquiry router: `docs/public-inquiry-router.md`.

## 5. Suggested safe issue title patterns

- `Starter template inquiry: GitHub weekly summary + PR review templates`
- `Audit beta inquiry: public-safe workflow backlog for ops updates`
- `Free Lite feedback: output format request for Markdown summary`
- `Pilot later: sanitized request for a review-first Slack/Notion draft workflow`

These titles describe intent without revealing private repositories, customer names, credentials, or transaction details.
