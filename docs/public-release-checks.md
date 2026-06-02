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

Confirm `docs/free-lite-download-first-run-guide.md` remains linked from `README.md` before handling release ZIP download/setup questions; it routes a downloader from local unzip to one safe public-repo run before any paid or private scope.

Confirm `docs/free-lite-output-review-guide.md` remains linked from `README.md` before handling feedback about generated Markdown quality; it keeps output review tied to `samples/sample-output.md` and sanitized public issue details.

Confirm `docs/upgrade-path-boundary.md`, `docs/full-pack-public-listing.md`, `docs/buyer-fit-checklist.md`, `docs/public-evaluation-scorecard.md`, `docs/public-share-kit.md`, `docs/public-inquiry-router.md`, `docs/public-proof-index.md`, `docs/public-roi-assumption-worksheet.md`, `docs/public-safe-onboarding-playbook.md`, `docs/public-implementation-scope-menu.md`, `docs/free-lite-download-first-run-guide.md`, and `PRICING.md` remain linked before handling paid-pack, audit, evaluation, proof, value-estimate, onboarding, scope-selection, release-download, or public-only outreach questions; they keep conversion, scorecard, inquiry routing, proof requests, rough ROI assumptions, onboarding, scope-selection, first-run download, and sharing questions public-safe without requesting checkout, payment, KYC/tax, credentials, private repository URLs, customer data, or private outreach.

## 2. Manual import smoke test

1. Import `workflows/free-lite-github-weekly-snapshot.json` into n8n.
2. Leave `GITHUB_TOKEN` blank.
3. Use a public repository such as `n8n-io/n8n`.
4. Run manually.
5. Confirm the final node returns a `markdown` field with commits, merged PRs, closed issues, stale items, and Claude-ready review questions.
6. Compare the generated Markdown with `samples/sample-output.md` and the output review scorecard in `docs/free-lite-output-review-guide.md` before requesting feedback.

## 3. Public support hygiene

When answering a public issue, ask only for sanitized details:

- n8n version;
- public test repository, or “private repo tested” without naming it;
- node name that failed;
- redacted error text;
- whether the final `markdown` field appeared.

Do not request or post tokens, private repository URLs, customer data, production logs, internal screenshots, paid account details, invoices, legal/KYC/tax information, credentials, or exploit details for a real private system. If a reporter needs examples, link them to `docs/public-safe-issue-examples.md`; if they ask what can be shared publicly, link `SECURITY.md`.

## 4. Security boundary smoke check

Before a release or public support reply, confirm:

- `SECURITY.md` is present and linked from `README.md`;
- the four issue forms linked from `README.md` are present under `.github/ISSUE_TEMPLATE/` and keep blank issues disabled;
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
