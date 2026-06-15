# Clone-to-first-success guide

Use this public-only guide if you cloned the repository instead of downloading the release ZIP. GitHub traffic shows some visitors clone first, so this page keeps the fastest local path focused on one safe Free Lite run before any paid, private, or checkout conversation.

## 10-minute local path

1. Start from a fresh clone and inspect the files locally.
2. Run the static public-safety check from the repository root:

   ```bash
   python3 scripts/validate_free_lite.py
   git diff --check
   ```

3. Open `workflows/free-lite-github-weekly-snapshot.json` and import it into your own n8n instance.
4. For the first run, use a public repository such as `n8n-io/n8n` and leave `GITHUB_TOKEN` blank unless you need higher public API rate limits.
5. Confirm the final node returns a `markdown` field.
6. Compare your result with `samples/sample-output.md`, then score the output using `docs/free-lite-output-review-guide.md` and `docs/public-evaluation-scorecard.md`.
7. Fill the clone-run public receipt below so you can open one sanitized issue without re-running the whole setup.
8. If setup fails, use `docs/free-lite-import-checklist.md` and `docs/free-lite-troubleshooting-faq.md` before opening a public issue.

## Clone-run public receipt

Copy only this public-safe receipt into a setup or feedback issue after your local check. Replace anything private with `redacted` or `public repo only`.

```markdown
### Clone-run public receipt

- n8n version:
- Free Lite source: cloned repo / release ZIP
- Local validation: `python3 scripts/validate_free_lite.py` passed/failed; `git diff --check` passed/failed
- Public test repository: owner/repo, or `private repo tested; name redacted`
- `GITHUB_TOKEN`: blank / optional higher-rate-limit token used locally, not shared
- Import result: succeeded/failed
- Final `markdown` field appeared: yes/no
- Sample-output comparison: matches / partially matches / unclear
- Node that failed, if any:
- Redacted error text, if any:
- Next safe route requested: setup help / output feedback / template-pack fit / audit-pilot fit
```

Before posting, remove tokens, credentials, private repository URLs, customer data, production logs, internal screenshots, checkout/payment details, payout/wallet/bank/Stripe details, tax/KYC/contract details, DM/email/forms/private outreach requests, paid ads instructions, and guaranteed ROI assumptions.

## Public-only evidence you can share

Safe public issue details:

- n8n version;
- whether you cloned or used the release ZIP;
- public test repository name, or “private repo tested” without naming it;
- node name that failed;
- redacted error text;
- whether the final `markdown` field appeared;
- whether `python3 scripts/validate_free_lite.py` and `git diff --check` passed locally;
- which next route fits: setup help, feedback, template-pack fit, or audit/pilot fit.

Do **not** share tokens, credentials, private repository URLs, customer data, production logs, internal screenshots, checkout/payment details, payout/wallet/bank/Stripe details, tax/KYC/contract details, DM/email/forms/private outreach requests, paid ads instructions, or guaranteed ROI assumptions.

## Next safe public route

- Setup/import issue: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-setup.yml>
- Feedback/integration request: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-feedback.yml>
- Template/customization inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=workflow-pack-inquiry.yml>
- Workflow audit / pilot inquiry: <https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=audit-pilot-inquiry.yml>
- Unsure which route fits: `docs/public-inquiry-router.md`
- Copyable sanitized issue text: `docs/public-safe-issue-examples.md`

This cloned-repo path does not activate checkout/payment, capture payment, request payout setup, require KYC/tax/bank/contract information, create a private outreach flow, or include managed implementation support.
