# Public-safe onboarding playbook

Use this playbook to guide your onboarding from first importing the Free Lite workflow to deciding whether you need the full template pack, customized private scoping, or a fixed-scope AI workflow audit.

This onboarding path is public-only and does not request checkout/payment, payout details, KYC, tax, bank details, contracts, tokens, credentials, private repository URLs, customer data, DM/email/forms, private outreach, paid ads, or guaranteed ROI.

## The onboarding journey

The onboarding journey is structured into four progressive phases, ensuring you can verify safety, compatibility, and value at every step before any private details or credentials are ever discussed.

```text
+----------------------------+     +----------------------------+
|  Phase 1: Safe Verification| --> |  Phase 2: Review-First Rule|
|  Import Free Lite & test   |     |  Run read-only draft checks|
+----------------------------+     +----------------------------+
                                                 |
                                                 v
+----------------------------+     +----------------------------+
|  Phase 4: Public Route     | <-- |  Phase 3: Value Mapping    |
|  Select public issues/forms|     |  Buyer fit & ROI formulas  |
+----------------------------+     +----------------------------+
```

---

## Phase 1: Local import and safe verification

The first step is to verify that the core weekly snapshot workflow runs successfully in your environment without exposing credentials or connecting active output channels.

1. **Download and Import**: Import `workflows/free-lite-github-weekly-snapshot.json` into your local or self-hosted n8n instance.
2. **First Run Configuration**: Leave `GITHUB_TOKEN` blank on your first manual test. This proves the workflow can safely query public repository metadata without credentials.
3. **Point to a Public Target**: Set `GITHUB_REPO` to a large public repository with frequent activity (for example, `n8n-io/n8n`) and set `LOOKBACK_DAYS` to `7`.
4. **Manual Run & Verification**: Click "Execute Workflow" and confirm the final **Output Markdown Snapshot** node successfully populates the `markdown` field with weekly commit, pull request, and issue counts.

---

## Phase 2: Private adaptation and the "Review-First" rule

Once you have verified that the workflow operates correctly on public metadata, you can safely adapt it for private repository monitoring inside your own secure network.

1. **Keep Credentials Local**: If you configure a `GITHUB_TOKEN` for private repositories, ensure it remains inside your private n8n environment or local environment variables. Never copy or paste credentials into public issues or share them in any public forum.
2. **Apply the Review-First Principle**: Keep all automated output restricted to read-only drafts or internal summaries first. Before connecting Slack webhooks or Notion databases, review the generated Markdown output locally.
3. **Use the Review Guide**: Use [`docs/free-lite-output-review-guide.md`](free-lite-output-review-guide.md) to establish quality checks for the weekly summary before sharing it with your team.
4. **Red-team Preflight**: Use [`docs/free-lite-validation-preflight.md`](free-lite-validation-preflight.md) to establish a manual verification preflight routine for any local modifications before pushing changes or requesting team feedback.

---

## Phase 3: Scope and value mapping

Before moving beyond Free Lite, use our public planning collateral to map out what you need and estimate the potential efficiency impact of automated reviews.

1. **Check Buyer Fit**: Check [`docs/buyer-fit-checklist.md`](buyer-fit-checklist.md) to see if your operational goals match the patterns covered by the broader template pack.
2. **Calculate Value Assumptions**: Use the public-safe formulas in [`docs/public-roi-assumption-worksheet.md`](public-roi-assumption-worksheet.md) to outline rough time-saving ranges. Use ranges and placeholders only; do not include actual payroll, private revenue, or customer counts.
3. **Grade Your Readiness**: Grade your current automation readiness using [`docs/public-evaluation-scorecard.md`](public-evaluation-scorecard.md). This scorecard guides you on whether to stick with Free Lite or move toward more comprehensive templates.
4. **Compare Options**: Review `PRICING.md` and the checkout-disabled full-pack preview in `docs/full-pack-public-listing.md` to compare different template levels and audit packages.

---

## Phase 4: Navigating the public inquiry route

If your value mapping indicates that you need custom delivery nodes (Slack, Discord, Notion), PR review risk digests, or a custom AI workflow audit, use our structured public inquiry route.

1. **Consult the Inquiry Router**: Read [`docs/public-inquiry-router.md`](public-inquiry-router.md) to identify the correct public GitHub issue template for your specific goal.
2. **Submit a Sanitized Request**: Open one of the guided issue templates under `.github/ISSUE_TEMPLATE/`. The templates are designed to ensure you only post sanitized, public-safe technical specifications.
3. **Stay on the Safe Side of the Boundary**: Do not post API keys, private repository names, internal database structures, customer data, or billing details in your issue body.
4. **Transition to Private Scoping**: If a paid template pack, fixed-scope audit, or implementation pilot is approved, any detailed credential review, private repository access, or sensitive onboarding details will be moved to a secure, private communication channel before implementation begins.

---

## Onboarding guardrails (What NOT to do/share)

To protect your system security and personal privacy, always maintain these strict safety boundaries during your onboarding process:

* **No Credentials**: Never post GITHUB_TOKEN, ANTHROPIC_API_KEY, SLACK_WEBHOOK_URL, or any other API secrets in public issues or screenshots.
* **No Private Repository URLs**: Redact repository names or use placeholders (e.g., `owner/repo`) when describing setup symptoms.
* **No Private Customer Data**: Never include internal customer names, email addresses, database rows, or live production log dumps in any public setup report.
* **No Payment/Invoicing Details**: Do not post bank account numbers, tax IDs, credit card details, Stripe account IDs, KYC documents, or legal contract drafts.
* **No DM/Email/Forms/Private Outreach**: We do not solicit or conduct private outreach via direct message, email, or unguided private forms on this public repository. All initial inquiries must follow the public issue templates.
* **No Guaranteed ROI**: All calculations, worksheets, and scorecards are informational planning tools based on your own assumptions. We make no guaranteed ROI claims.

---

## Related public-safe documentation

* **Free Lite Quick Start**: [`../README.md`](../README.md)
* **Import Checklist & Troubleshooting**: [`docs/free-lite-import-checklist.md`](free-lite-import-checklist.md)
* **10-Minute Demo Runbook**: [`docs/free-lite-demo-runbook.md`](free-lite-demo-runbook.md)
* **Troubleshooting FAQ**: [`docs/free-lite-troubleshooting-faq.md`](free-lite-troubleshooting-faq.md)
* **Public Inquiry Router**: [`docs/public-inquiry-router.md`](public-inquiry-router.md)
* **Public Evaluation Scorecard**: [`docs/public-evaluation-scorecard.md`](public-evaluation-scorecard.md)
* **Public ROI Assumption Worksheet**: [`docs/public-roi-assumption-worksheet.md`](public-roi-assumption-worksheet.md)
* **Buyer Fit Checklist**: [`docs/buyer-fit-checklist.md`](buyer-fit-checklist.md)
* **Checkout-Disabled Public Listing Preview**: [`docs/full-pack-public-listing.md`](full-pack-public-listing.md)
* **Public Proof Index**: [`docs/public-proof-index.md`](public-proof-index.md)
* **Public Support Boundary**: [`SECURITY.md`](../SECURITY.md)
