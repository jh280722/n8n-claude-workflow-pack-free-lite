# Free Lite 10-minute demo runbook

Use this runbook to prove the Free Lite workflow imported cleanly and produced a reviewable Markdown snapshot without adding private data, webhooks, or Claude/API posting steps.

## Scope

This runbook is for a public-safe smoke test only:

- use a public repository first;
- keep `GITHUB_TOKEN` blank unless you are configuring it privately inside your own n8n environment;
- do not connect Slack, Discord, Notion, email, or Claude delivery nodes during this smoke test;
- do not paste private repository names, API keys, customer data, production logs, or screenshots with secrets into public GitHub issues.

## Recommended demo settings

| Setting | Public-safe value | Why |
|---|---|---|
| `GITHUB_REPO` | `n8n-io/n8n` | Public repo with enough activity for a non-empty output. |
| `LOOKBACK_DAYS` | `7` first, then `30` if output is sparse | Keeps the first output small while giving an easy fallback. |
| `GITHUB_TOKEN` | blank for first run | Proves the workflow works without credentials for public data. |
| Trigger | Manual Trigger | Avoids scheduled noise while validating import/setup. |

## Demo steps

1. Import `workflows/free-lite-github-weekly-snapshot.json` into n8n.
2. Open the workflow and keep only the **Manual Trigger** execution path active for the test run.
3. Set `GITHUB_REPO=n8n-io/n8n` and `LOOKBACK_DAYS=7` using your preferred n8n environment/config method.
4. Leave `GITHUB_TOKEN` blank for the first public-repo smoke test.
5. Execute the workflow manually.
6. Open **Output Markdown Snapshot**.
7. Confirm the final item includes a `markdown` field with these sections:
   - `Weekly GitHub Snapshot`
   - `Commits`
   - `Merged PRs`
   - `Closed Issues`
   - `Claude-ready review questions`
8. Copy the Markdown into a local note or internal draft doc. Do not auto-post it from this Free Lite workflow.

## Pass/fail checklist

| Check | Pass condition | Safe fallback if it fails |
|---|---|---|
| Import | n8n accepts the JSON workflow. | Re-download the release asset and retry import. |
| Manual run | Workflow reaches **Output Markdown Snapshot**. | Re-run with `GITHUB_REPO=n8n-io/n8n` and no token. |
| Markdown field | Final node contains `markdown`. | Open the previous GitHub fetch node and record the sanitized error. |
| Activity counts | Output shows counts for commits, merged PRs, and closed issues. | Increase `LOOKBACK_DAYS` to `30`. |
| Safety | No credentials, private URLs, or customer data appear in the workflow output or screenshots. | Redact locally before sharing any public issue. |

## What to include in a public issue

If the demo fails, include only:

- n8n version;
- whether import succeeded;
- `GITHUB_REPO` if it is a public test repo, or say `private repo tested, name withheld`;
- `LOOKBACK_DAYS` value;
- failing node name;
- redacted error text;
- whether the final `markdown` field appeared.

Use `docs/public-safe-issue-examples.md` for copyable examples.

## When to consider the paid/full pack

The Free Lite workflow intentionally stops at draft Markdown. A fuller implementation may be useful if you need:

- Claude-written narrative summaries;
- Slack/Discord/Notion draft delivery with manual approval;
- PR review risk digests;
- audit-ready setup docs and sample payloads;
- customization for a team workflow after private scoping.

Keep full-pack, audit, or customization inquiries public-safe. Do not post credentials, private workspace names, legal/KYC/tax details, payout information, or production access requests in GitHub issues.
