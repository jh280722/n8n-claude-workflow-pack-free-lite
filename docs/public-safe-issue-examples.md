# Public-safe issue examples

Use these examples when reporting Free Lite setup problems or sharing feedback. They are written to keep GitHub issues useful without exposing secrets, private repository names, customer data, or production logs.

Public-only boundary: copy these examples into public GitHub issue forms only after removing tokens, credentials, private repository URLs, customer data, production logs, internal screenshots, checkout/payment details, payout/wallet/bank/Stripe details, tax/KYC/contract details, DM/email/forms/private outreach requests, paid ads instructions, and guaranteed ROI assumptions. If the issue needs sensitive details, stop at a high-level public symptom and wait for an approved private channel.

Use the guided forms instead of blank issues:

- `free-lite-setup.yml` for import or execution setup questions.
- `free-lite-feedback.yml` for output feedback or future integration ideas.
- `workflow-pack-inquiry.yml` for template-pack or customization fit.
- `audit-pilot-inquiry.yml` for workflow audit or later pilot interest.

## Good setup report

```markdown
## n8n version
1.100.0 self-hosted Docker

## Import result
Import succeeded.

## Test repository
Public test repo: n8n-io/n8n

## Failing node
GitHub: list merged PRs

## Redacted error
GitHub API returned 403 rate limit exceeded. No token was included in this public report.

## Final markdown field
Did not appear because execution stopped at the GitHub node.
```

Why this is good:

- uses a public repository;
- names the failing node;
- redacts credential details;
- does not include tokens, private URLs, screenshots with secrets, or customer data.

## Good feedback report

```markdown
## What worked
The workflow imported cleanly and produced a Markdown snapshot for n8n-io/n8n.

## What was unclear
I was not sure where to set LOOKBACK_DAYS in my n8n environment.

## Desired next integration
Slack draft message only, with a manual approval step before posting.

## Safety note
I tested on public data only and did not include private repository names or credentials.
```

Why this is good:

- gives actionable product feedback;
- keeps the next-integration request scoped to draft/review mode;
- avoids private workspace details.

## Good template-pack inquiry

```markdown
## Use case
I want a self-hosted n8n template pack for weekly engineering updates and PR review digests.

## Environment
n8n self-hosted; GitHub; Slack may be added later.

## Data boundary
Public-safe description only. Private repo names, tokens, workspace URLs, and customer data are not included here.

## Desired delivery
Importable workflows, sample payloads, and setup docs. No production credential setup through GitHub issues.
```

Why this is good:

- identifies buyer intent without requesting private details;
- keeps paid implementation, credentials, KYC/tax, and contract topics out of public GitHub.

## Do not post

Do **not** include:

- API keys, OAuth tokens, cookies, session IDs, or webhook URLs;
- private repository URLs or internal organization names;
- customer data, production logs, incident details, invoices, contracts, bank/tax/KYC information;
- screenshots that reveal secrets, staff names, private channels, billing data, or internal dashboards;
- prompts or automation configs that include proprietary business logic.

If a report needs sensitive details, keep the public issue high level and move the sensitive review only to an approved private channel after scope approval.

## Fast self-check before submitting

Before opening an issue, confirm:

- [ ] I can reproduce the issue with a public repo or sanitized sample.
- [ ] Any error text is redacted.
- [ ] No token, private URL, customer data, production log, or billing/legal/KYC detail is included.
- [ ] No checkout/payment, payout/wallet/bank/Stripe, tax/KYC/contract, DM/email/forms/private outreach, paid ads, or guaranteed ROI detail is included.
- [ ] I named the failing n8n node and described whether import succeeded.
- [ ] I included whether the final `markdown` field appeared.
