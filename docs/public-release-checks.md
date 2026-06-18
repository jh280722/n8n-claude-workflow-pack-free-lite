# Public release checks

Use this checklist before tagging a Free Lite release or replying to setup reports in public issues.

## 1. Static safety check

Run:

```bash
python3 scripts/validate_free_lite.py
```

Expected result:

```text
OK: Free Lite workflow JSON and public issue forms pass static public-safety checks.
```

This confirms the workflow JSON parses, still includes the read-only GitHub snapshot nodes, keeps `GITHUB_TOKEN` optional, does not include common posting/mutating integrations or secret-like markers, and keeps public issue forms present with explicit no-secrets/no-private-data reminders.

Also run the local preflight in `docs/free-lite-validation-preflight.md` before release/support decisions; it adds `git diff --check`, public-safe screenshot/example checks, and issue-response hygiene.

Confirm the troubleshooting FAQ in `docs/free-lite-troubleshooting-faq.md` remains linked from `README.md` before replying to setup issues; it keeps common import/API/output debugging public-safe.

Confirm `CONTRIBUTING.md` remains linked from `README.md` before inviting public issues, pull requests, examples, or validator changes; it keeps contributor guidance public-only and blocks tokens, credentials, private repository URLs, customer data, checkout/payment details, tax/KYC/contract details, DM/email/forms, private outreach, paid ads, and guaranteed ROI claims.

Confirm `docs/free-lite-download-first-run-guide.md` remains linked from `README.md` before handling release ZIP download/setup questions; it routes a downloader from local unzip to one safe public-repo run before any paid or private scope.

Confirm `docs/clone-to-first-success.md` remains linked from `README.md` and the GitHub issue chooser before handling visitors who cloned the repo before reading the docs; it routes a cloner through local validation, one public-repo n8n run, a clone-run public receipt, sanitized issue evidence, and public issue forms without requesting secrets, private data, checkout/payment, payout, KYC/tax/bank/contract, DM/email/forms/private outreach, paid ads, or guaranteed ROI claims. Confirm `scripts/clone_run_receipt.py` still runs locally so cloners can prefill the local-validation lines before adding public-safe n8n/import results.

Confirm `workflows/README.md` and `scripts/README.md` remain linked from `README.md` before handling visitors who landed directly on workflow JSON, the workflow folder, or validator scripts from GitHub traffic/search; they route those visitors back to public-only first-run, validation, issue, and contribution paths without requesting secrets, private data, checkout/payment, payout, KYC/tax/bank/contract, DM/email/forms/private outreach, paid ads, or guaranteed ROI claims.

Confirm `docs/free-lite-output-review-guide.md` remains linked from `README.md` before handling feedback about generated Markdown quality; it keeps output review tied to `samples/sample-output.md` and sanitized public issue details.

Confirm `docs/public-safe-issue-examples.md` remains linked from `README.md` and the issue chooser before asking a visitor to open a setup, feedback, template-pack, or audit/pilot issue; it gives copyable public-only examples and blocks checkout/payment, payout/wallet/bank/Stripe, tax/KYC/contract, DM/email/forms/private outreach, paid ads, and guaranteed ROI claims.

Confirm `docs/upgrade-path-boundary.md`, `docs/full-pack-public-listing.md`, `docs/buyer-fit-checklist.md`, `docs/public-evaluation-scorecard.md`, `docs/public-share-kit.md`, `docs/public-inquiry-router.md`, `docs/public-proof-index.md`, `docs/public-roi-assumption-worksheet.md`, `docs/public-safe-onboarding-playbook.md`, `docs/public-implementation-scope-menu.md`, `docs/free-lite-download-first-run-guide.md`, `docs/clone-to-first-success.md`, `docs/public-sample-output-next-steps.md`, and `PRICING.md` remain linked before handling paid-pack, audit, evaluation, proof, value-estimate, onboarding, scope-selection, release-download, clone-first, sample-output, or public-only outreach questions; they keep conversion, scorecard, inquiry routing, proof requests, rough ROI assumptions, onboarding, scope-selection, first-run download, clone-to-first-success, clone-run public receipt, sample-output review, and sharing questions public-safe without requesting checkout, payment, KYC/tax, credentials, private repository URLs, customer data, or private outreach.

## 2. Manual import smoke test

1. Import `workflows/free-lite-github-weekly-snapshot.json` into n8n.
2. Leave `GITHUB_TOKEN` blank.
3. Use a public repository such as `n8n-io/n8n`.
4. Run manually.
5. Confirm the final node returns a `markdown` field with commits, merged PRs, closed issues, stale items, and Claude-ready review questions.
6. Compare the generated Markdown with `samples/sample-output.md`, the output review scorecard in `docs/free-lite-output-review-guide.md`, and `docs/public-sample-output-next-steps.md` before requesting feedback.

## 3. Public support hygiene

When answering a public issue, ask only for sanitized details:

- n8n version;
- source path: cloned repo or release ZIP;
- local validation result for `python3 scripts/validate_free_lite.py` and `git diff --check`, if they cloned the repo;
- public test repository, or “private repo tested” without naming it;
- node name that failed;
- redacted error text;
- whether the final `markdown` field appeared;
- sample-output comparison against `samples/sample-output.md`;
- next safe route requested: setup help, output feedback, template-pack fit, or audit/pilot fit.

Do not request or post tokens, private repository URLs, customer data, production logs, internal screenshots, paid account details, invoices, legal/KYC/tax information, credentials, or exploit details for a real private system. If a reporter needs examples, link them to `docs/public-safe-issue-examples.md`; if they ask what can be shared publicly, link `SECURITY.md`.

## 4. Security boundary smoke check

Before a release or public support reply, confirm:

- `SECURITY.md` is present and linked from `README.md`;
- the four issue forms linked from `README.md` are present under `.github/ISSUE_TEMPLATE/` and keep blank issues disabled;
- the GitHub issue chooser contact links point visitors to `docs/clone-to-first-success.md`, `docs/free-lite-download-first-run-guide.md`, `docs/public-inquiry-router.md`, `docs/public-sample-output-next-steps.md`, and `SECURITY.md` before they choose a form;
- the GitHub issue chooser also links `docs/public-safe-issue-examples.md` so visitors can copy a sanitized setup, feedback, template-pack, or audit/pilot example before posting;
- issue replies ask for sanitized symptoms only, not secrets or private repo details;
- any security-sensitive finding is reproducible on `n8n-io/n8n` or a synthetic sample before it is discussed publicly;
- setup troubleshooting links to `docs/free-lite-troubleshooting-faq.md` before asking for more details;
- output quality feedback links to `docs/free-lite-output-review-guide.md` before asking for examples;
- custom private-repo integrations, credential review, or production debugging are not promised in the free public repo.

## 5. Release note template

```markdown
## Free Lite release check

- Static validator: passed
- Manual import smoke test: passed on a public repo
- Output reviewed: markdown only, no posting/writing integrations
- Public issue safety reminder: included
```
