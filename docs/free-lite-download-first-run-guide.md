# Free Lite download-to-first-run guide

Use this public-only guide when you have downloaded the Free Lite release ZIP and want to get one useful, safe run before deciding whether to open a setup issue, share feedback, or compare paid template/audit options.

This guide is checkout/payment-disabled and does not request payout details, KYC, tax, bank, wallet, Stripe, contracts, tokens, credentials, private repository URLs, customer data, production logs, DM/email/forms, private outreach, paid ads, or guaranteed ROI claims.

## 1. Before you import

Keep the first run deliberately boring:

1. Unzip the release locally and locate `workflows/free-lite-github-weekly-snapshot.json`.
2. Pick a public repository target such as `n8n-io/n8n`, or another public repo you are allowed to inspect.
3. Leave `GITHUB_TOKEN` blank for the first run. Add a token only inside your own private n8n environment if rate limits require it later.
4. Avoid screenshots that show browser profiles, private repo names, internal URLs, API keys, Slack webhook URLs, customer names, or production logs.

## 2. Ten-minute first run

| Minute | Action | Public-safe pass condition |
|---:|---|---|
| 0–2 | Import the JSON into n8n. | Workflow imports without editing credentials. |
| 2–4 | Set `GITHUB_REPO` to a public repo and `LOOKBACK_DAYS` to `7`. | Config uses public metadata or synthetic input only. |
| 4–7 | Execute manually. | Final **Output Markdown Snapshot** node returns a `markdown` field. |
| 7–9 | Compare with `samples/sample-output.md`. | Output has commits, merged PRs, closed issues, stale items, and review questions. |
| 9–10 | Choose the next public route. | Setup issue, feedback issue, or scope menu path chosen without private data. |

If the import or run fails, use `docs/free-lite-import-checklist.md` and `docs/free-lite-troubleshooting-faq.md` before opening a public issue.

## 3. Decide what to do after the first run

| First-run result | Best next public action |
|---|---|
| Import failed before execution. | Open the Free Lite setup form with n8n version, failed node, sanitized error text, and whether the test used a public repo. |
| Workflow ran but output is unclear. | Use `docs/free-lite-output-review-guide.md`, then open a feedback issue with a sanitized description of the missing section. |
| Output is useful and you want to adapt it. | Follow `docs/public-safe-onboarding-playbook.md` and keep credentials/private repo details out of public issues. |
| You want more templates or an audit path. | Use `docs/public-implementation-scope-menu.md` and route through `docs/public-inquiry-router.md`. |
| You want to estimate value first. | Use ranges/placeholders in `docs/public-roi-assumption-worksheet.md`; do not post private revenue, payroll, or customer details. |

## 4. Safe public issue payload

When asking for help, keep the issue body to public-safe fields only:

- n8n version and hosting type, if you can share it safely;
- public repository used for the test, or “private repo tested locally” without naming it;
- node name that failed, if any;
- short redacted error text;
- whether the final `markdown` field appeared;
- which next lane you are considering: Free Lite support, Starter/Pro templates, Audit, or Pilot later.

Do not include tokens, credentials, private repository URLs, customer data, checkout/payment details, payout information, KYC/tax/bank/contract details, DM/email/forms/private outreach requests, paid ads instructions, private contact data, or guaranteed ROI assumptions.

## 5. Public routes

- Free Lite setup question: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-setup.yml>
- Free Lite feedback/integration request: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-feedback.yml>
- Template/customization inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=workflow-pack-inquiry.yml>
- Audit/pilot inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=audit-pilot-inquiry.yml>

If you are not sure which route fits, start with `docs/public-inquiry-router.md`.
