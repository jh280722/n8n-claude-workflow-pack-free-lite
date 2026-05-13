# Free Lite validation preflight

Use this preflight before modifying the Free Lite workflow, preparing a release, or answering a public setup report.

The goal is to keep the public workflow importable, read-only, and safe to discuss without collecting secrets or private repository data.

## Required local check

Run from the repository root:

```bash
python3 scripts/validate_free_lite.py
git diff --check
```

Expected validator output:

```text
OK: Free Lite workflow JSON is valid and passes static public-safety checks.
```

## What the validator protects

The static validator checks that:

- `workflows/free-lite-github-weekly-snapshot.json` is valid JSON;
- the expected read-only GitHub snapshot nodes are still present;
- `GITHUB_TOKEN` remains optional and environment-variable based;
- the workflow still emits review-first Markdown instead of posting to another system;
- common mutating/posting integrations and secret-like markers are not present.

## Public-safe review checklist

Before publishing a release or replying to an issue, confirm:

1. The validator passes locally.
2. `git diff --check` reports no whitespace errors.
3. Any screenshots or examples use public repositories or synthetic sample data only.
4. No issue reply asks for tokens, private repository URLs, customer data, production logs, payout/KYC/tax details, or exploit details for a real private system.
5. Any custom/private-repo adaptation is described as separately scoped work, not as included public support.

## Optional CI note

If you add your own CI later, it should run only the same local static command and use read-only repository permissions. It should not require GitHub tokens, n8n credentials, Claude/Anthropic keys, Slack/Notion webhooks, paid accounts, or private repository fixtures.
