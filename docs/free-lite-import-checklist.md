# Free Lite import checklist and troubleshooting

Use this checklist before opening a public issue. It is designed for public or sanitized repository tests only.

## 5-minute import check

1. Import `workflows/free-lite-github-weekly-snapshot.json` into n8n.
2. Leave `GITHUB_TOKEN` blank for the first run and use a public repo such as `n8n-io/n8n`.
3. Run the workflow manually.
4. Open the final **Output Markdown Snapshot** node.
5. Confirm the `markdown` field contains counts for commits, merged PRs, and closed issues.

## Optional environment variables

| Variable | Example | Required? | Notes |
|---|---|---:|---|
| `GITHUB_REPO` | `n8n-io/n8n` | No | Must be `owner/repo`. Defaults to `n8n-io/n8n`. |
| `LOOKBACK_DAYS` | `7` | No | Use a small number first to keep output readable. |
| `GITHUB_TOKEN` | not shown | No | Only use a token inside your own n8n credential/env setup. Never paste it into issues. |

## Common issues

### Import succeeds, but execution returns `GitHub ... failed: 403`

Likely causes:

- public GitHub API rate limit was reached;
- a token was configured incorrectly;
- the selected repo is private or inaccessible from the current environment.

Safe next step: retry with `GITHUB_REPO=n8n-io/n8n` and no token. If that works, review your own repo/token permissions privately.

### Execution fails with `Set GITHUB_REPO as owner/repo`

Set `GITHUB_REPO` to exactly two path parts, for example:

```text
owner/repo
```

Do not paste full private URLs, access tokens, or internal organization names into public issues.

### The output has zero commits, PRs, or issues

Likely causes:

- the repo had no matching activity inside `LOOKBACK_DAYS`;
- `LOOKBACK_DAYS` is too small;
- the workflow is pointed at a fork or test repo with little activity.

Safe next step: test with `LOOKBACK_DAYS=30` on a public repo.

### The output is useful, but you want Slack/Notion/Claude delivery

This free workflow intentionally stops at draft Markdown. That keeps the first test read-only and reviewable. Open a sanitized template/customization issue if you want a public-safe discussion of next integrations.

## Public issue checklist

When opening a setup issue, include only:

- n8n version;
- whether import succeeded;
- public test repo used, or state that a private repo was tested without naming it;
- failing node name;
- redacted error text;
- whether the final `markdown` field appeared.

For copyable public-safe examples, see `docs/public-safe-issue-examples.md`.

Do **not** include API keys, tokens, private repository names, customer data, production logs, invoices, legal/KYC/tax details, or internal screenshots.
