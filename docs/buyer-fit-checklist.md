# Buyer fit checklist for the draft full pack

Use this public-safe checklist before opening a template-pack or audit inquiry. It is meant to help buyers decide whether the checkout-disabled full-pack preview is worth discussing without posting private data or activating payment.

## Strong fit signals

You are probably a fit if most of these are true:

- You already use n8n or are comfortable importing and editing workflow JSON files.
- You want review-first automations that produce draft Markdown, checklists, or briefs before anything is posted or written.
- Your first evaluation can use a public repository, synthetic sample payload, or sanitized export.
- You need repeatable workflows for GitHub summaries, PR review/risk notes, Slack/Notion-ready ops briefs, meeting actions, workflow audits, or lead/scope triage.
- You can wire your own API credentials in your own n8n instance after your internal security review.
- You understand that the draft pack is templates and playbooks, not managed production support, a legal commitment, or a no guaranteed ROI / guaranteed outcome promise.

## Weak fit / pause signals

Pause before inquiring publicly if any of these apply:

- You need someone to enter or inspect production credentials, private repository URLs, customer data, confidential logs, or private workflow exports in a public GitHub issue.
- You need checkout, payment, invoice, payout, bank, tax, KYC, contract, refund, SLA, or procurement details handled inside this public repo.
- You need an autonomous workflow that posts to Slack, writes to Notion, comments on GitHub, or changes production systems without a human review gate.
- You need guaranteed revenue, guaranteed time savings, legal advice, security certification, or production incident response.
- You cannot test the first pass with public or sanitized data.

## Public inquiry preflight

Before opening an issue, prepare public-safe answers to these questions:

1. Which lane are you evaluating: Starter template pack, Pro template pack, AI Workflow Audit beta, or a later implementation pilot?
2. Which n8n environment are you using: self-hosted, n8n Cloud, or still deciding?
3. Which one workflow outcome matters most: weekly status, PR review, Slack/Notion brief, meeting actions, KB/RAG gap finding, audit backlog, ROI assumptions, or lead/scope triage?
4. What sample can be discussed publicly: a public repository, synthetic payload, redacted workflow shape, or high-level process description?
5. What must stay private and therefore should **not** be posted in GitHub issues?
6. Do you want templates only, a checklist-style audit, or later implementation help after private approval?

## What not to post publicly

Do not include tokens, credentials, private repository URLs, private workspace names, customer data, production logs, confidential screenshots, procurement/legal documents, checkout/payment details, payout/wallet/bank information, Stripe details, tax/KYC information, contracts, private workflow exports, or guaranteed ROI requirements.

## Next step

If the checklist still looks like a fit, use the sanitized public issue form that matches your intent:

- Template pack / customization inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=workflow-pack-inquiry.yml>
- Workflow audit / pilot inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=audit-pilot-inquiry.yml>

This page is informational only. It does not publish the paid ZIP, activate checkout, collect payment, request KYC/tax/bank details, create a contract, or promise guaranteed ROI.
