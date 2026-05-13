# Free Lite troubleshooting FAQ

Use this FAQ when the Free Lite workflow imports but the first run does not produce the expected Markdown snapshot.

Public-safety rule: reproduce with a public repository or sanitized sample first. Do not paste tokens, private repository URLs, customer data, production logs, webhook URLs, paid account details, or internal screenshots into public issues.

## Quick diagnostic path

1. Run `python3 scripts/validate_free_lite.py` from the repository root.
2. Re-import `workflows/free-lite-github-weekly-snapshot.json` into n8n.
3. Leave `GITHUB_TOKEN` blank for the first test.
4. Set `GITHUB_REPO=n8n-io/n8n` and `LOOKBACK_DAYS=7`.
5. Execute manually and inspect the final node's `markdown` field.

If that public-repo run succeeds, the workflow itself is healthy and the issue is likely repo permissions, rate limits, or private-data configuration in your local environment.

## Common symptoms

| Symptom | Likely cause | Safe next check |
| --- | --- | --- |
| Workflow import fails | n8n version/import compatibility or edited JSON | Re-download the release asset, run the static validator, and note your n8n version. |
| GitHub API node returns 403/rate limit | Anonymous GitHub API limit reached | Wait for reset or add a GitHub token locally. Do not post the token or full header output. |
| GitHub API node returns 404 | Repository name typo, private repo, or insufficient token scope | Test with `n8n-io/n8n`; if private, only say “private repo tested” in public. |
| Final node has no `markdown` field | A prior node failed or the workflow JSON was modified | Check the failed node name and sanitized error text only. |
| Markdown is empty or sparse | No matching commits/issues/PRs in the lookback window | Increase `LOOKBACK_DAYS` locally or test a busier public repo. |
| Schedule trigger does not run | Workflow inactive or timezone expectation mismatch | Run manually first, then confirm n8n workflow activation and instance timezone locally. |

## Safe public issue template

```text
n8n version: 1.x.x
Workflow import: succeeded / failed
Public test repo used: n8n-io/n8n or another public repo
Failed node: <node name only>
Sanitized error: <redacted message with no tokens, URLs to private repos, or internal logs>
Final markdown field appeared: yes / no
```

## What not to share publicly

- API keys, bearer tokens, cookies, private keys, credentials, or credential IDs.
- Private repository names/URLs, internal branch names, customer names, or incident details.
- Full execution screenshots if they reveal secrets, workspace names, or proprietary data.
- Webhook URLs, Slack/Discord channel IDs from private workspaces, or Notion workspace data.
- Procurement, legal, tax, KYC, bank, wallet, payout, invoice, or checkout details.

If troubleshooting requires any of the above, keep it out of this public repo and move only after a separately approved private engagement is scoped.
