# Public release checks

Use this checklist before tagging a Free Lite release or replying to setup reports in public issues.

## 1. Static safety check

Run:

```bash
python3 scripts/validate_free_lite.py
```

Expected result:

```text
OK: Free Lite workflow JSON is valid and passes static public-safety checks.
```

This confirms the workflow JSON parses, still includes the read-only GitHub snapshot nodes, keeps `GITHUB_TOKEN` optional, and does not include common posting/mutating integrations or secret-like markers.

## 2. Manual import smoke test

1. Import `workflows/free-lite-github-weekly-snapshot.json` into n8n.
2. Leave `GITHUB_TOKEN` blank.
3. Use a public repository such as `n8n-io/n8n`.
4. Run manually.
5. Confirm the final node returns a `markdown` field with commits, merged PRs, closed issues, stale items, and Claude-ready review questions.

## 3. Public support hygiene

When answering a public issue, ask only for sanitized details:

- n8n version;
- public test repository, or “private repo tested” without naming it;
- node name that failed;
- redacted error text;
- whether the final `markdown` field appeared.

Do not request or post tokens, private repository URLs, customer data, production logs, internal screenshots, paid account details, invoices, legal/KYC/tax information, or credentials. If a reporter needs examples, link them to `docs/public-safe-issue-examples.md`.

## 4. Release note template

```markdown
## Free Lite release check

- Static validator: passed
- Manual import smoke test: passed on a public repo
- Output reviewed: markdown only, no posting/writing integrations
- Public issue safety reminder: included
```
