# Public ROI assumption worksheet

Use this worksheet when you want to decide whether the Free Lite workflow, the draft template pack, or a future audit/pilot is worth more discussion. It is public-only and assumption-based: it does not request checkout/payment details, payout details, KYC, tax, bank information, contracts, tokens, credentials, private repository URLs, customer data, DM/email/forms, private outreach, paid ads, or guaranteed ROI claims.

## What this worksheet is for

- Convert a vague automation idea into a small set of public-safe assumptions.
- Decide whether Free Lite is enough, whether a template-pack inquiry is reasonable, or whether a paid audit/pilot would need private scoping later.
- Keep public GitHub issues sanitized by using ranges and placeholders instead of private revenue, payroll, incident, or customer details.

This page is not a promise of savings or revenue. All numbers are rough planning inputs that a buyer must validate in their own environment before any paid implementation.

## 5-minute public-safe estimate

Copy this table into a private note first. If you later open a public issue, keep only the sanitized row labels and ranges that are safe to share.

| Question | Public-safe answer style | Example |
|---|---|---|
| Repeated workflow | Describe the job, not a private system name | Weekly GitHub status brief for a public/open-source repo |
| People affected | Range or role label | 1–3 maintainers, ops lead, solo consultant |
| Current manual time | Range, not payroll data | 30–90 minutes per week |
| Pain level | Low / medium / high | Medium: summaries are inconsistent |
| Failure risk | Describe category only | Missed stale PRs or unclear next actions |
| Review owner | Role, not personal details | Maintainer or project lead reviews before sharing |
| Safe test data | Public repo or synthetic payload | `n8n-io/n8n` or a redacted sample payload |
| Next safe step | One of the public paths below | Run Free Lite, open setup issue, or ask a sanitized inquiry |

## Simple assumption formula

Use ranges instead of exact private numbers:

```text
weekly manual time range × weekly frequency × confidence factor = rough time-saving assumption
```

Example:

```text
30–90 minutes/week × 1 weekly status cycle × 0.5 confidence = 15–45 minutes/week assumption
```

Then compare the result with setup effort:

- If the assumed saving is less than the setup time, stay with Free Lite and keep testing.
- If the workflow saves review time but needs more examples, open a public Free Lite feedback issue.
- If several workflows share the same pattern, use the template/customization inquiry.
- If the team needs prioritization before implementation, use the audit/pilot inquiry.

Do not publish confidential revenue, payroll, customer, incident, repository, or credential information to justify the estimate.

## Public decision route

| If your estimate says... | Public-safe next step |
|---|---|
| "I only need a weekly public repo summary" | Use Free Lite and the `free-lite-output-review-guide.md` checklist |
| "Import/setup failed" | Open `free-lite-setup.yml` with sanitized error text only |
| "The output is useful, but I need Slack/Notion/Claude variants" | Open `workflow-pack-inquiry.yml` with sanitized outcome/range details |
| "I am unsure what to automate first" | Open `audit-pilot-inquiry.yml` with public-safe role, workflow, and risk categories |
| "This requires private repo data, customer data, credentials, contracts, or payment setup" | Stop at a public placeholder; private scoping needs separate approval and a non-public channel |

## What not to share publicly

Do not include:

- tokens, credentials, API keys, secrets, or webhook URLs;
- private repository URLs, private workflow exports, internal screenshots, or production logs;
- customer data, personal data, incident details, payroll, margin, invoice, or bank information;
- checkout/payment details, payout, wallet, Stripe, KYC, tax, bank, contract, procurement, refund, SLA, or legal details;
- requests for DM/email/forms/private outreach, paid ads, or guaranteed ROI.

## Related public-safe pages

- Free Lite quick start: `../README.md`
- Output quality review: `free-lite-output-review-guide.md`
- Buyer fit checklist: `buyer-fit-checklist.md`
- Public evaluation scorecard: `public-evaluation-scorecard.md`
- Public inquiry router: `docs/public-inquiry-router.md`
- Public proof index: `public-proof-index.md`
- Checkout-disabled listing preview: `full-pack-public-listing.md`
