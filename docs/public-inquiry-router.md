# Public inquiry router

Use this page to decide which public GitHub issue form or public doc link to share when someone asks about the Free Lite workflow, the draft full pack, or a workflow audit. It is designed for public-only conversations and does not replace private scoping, checkout/payment setup, or legal/commercial review.

## Fast route by reader problem

| Reader problem | Best public next step | What to ask for publicly | What not to ask for publicly |
|---|---|---|---|
| “Can I import the free workflow?” | Free Lite setup question: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-setup.yml> | n8n version, public test repo, node name, sanitized error text | tokens, credentials, private repository URLs, production logs |
| “Did the output look useful?” | Free Lite feedback: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-feedback.yml> | public repo used, whether the Markdown sections helped, sanitized example of missing context | customer data, internal incidents, confidential screenshots |
| “Would the full template pack fit my team?” | Workflow pack inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=workflow-pack-inquiry.yml> | desired workflow family, n8n hosting mode, public/synthetic test plan, template-only vs later implementation need | checkout/payment details, KYC, tax, bank, contracts, private repo names |
| “Do we need an audit or pilot instead of templates?” | Audit/pilot inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=audit-pilot-inquiry.yml> | public-safe process description, target outcome, assumptions, synthetic examples | private data, client data, credentials, legal commitments, guaranteed ROI requirements |

## Suggested public response pattern

```markdown
Thanks — for public-safe triage, the best path is the [public inquiry router](docs/public-inquiry-router.md).

Please use the matching issue form and keep the example sanitized: n8n version, public test repo or synthetic sample, affected node, and redacted symptom. Do not post tokens, credentials, private repository URLs, customer data, production logs, checkout/payment details, KYC, tax, bank, contracts, DM/email/form private outreach details, paid ads plans, or guaranteed ROI requirements.
```

## Qualification cues

Share the Free Lite path when the reader wants to validate import friction, public GitHub weekly summaries, or Markdown output quality.

Share the workflow pack inquiry when the reader already knows they want reusable templates for weekly status, PR review, Slack/Notion-ready briefs, meeting actions, knowledge-base gap finding, audit intake, lead-fit triage, pilot scoping, or approval-first review helpers.

Share the audit/pilot inquiry when the reader has a messy process but cannot yet name the workflow template they need. Keep it public-safe: ask for the outcome, current manual step count, and synthetic examples only.

## Hard boundary

This router is for public-only triage. It must not request or process tokens, API keys, credentials, private repository URLs, customer data, production logs, private workflow exports, confidential screenshots, checkout/payment activation, payment capture, payout/wallet/bank/Stripe/tax/KYC/contract details, invoices, DM, email, forms, private outreach, paid ads, subscriptions, spend, legal/SLA/support/refund promises, or no guaranteed ROI claims.

If a buyer needs private scoping, payment, KYC, tax, bank, contracts, custom implementation, or client/workplace data review, stop at a public-safe acknowledgment and get fresh approval before moving to any private channel or transaction step.
