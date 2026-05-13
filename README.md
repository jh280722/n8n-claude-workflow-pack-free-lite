# n8n + Claude Workflow Pack — Free Lite

A free, importable n8n workflow that generates a Markdown weekly snapshot for a public GitHub repository.

This is the public preview for a larger operator-grade workflow pack for engineering and ops teams using n8n, GitHub, Slack/Notion, and Claude-style review workflows.

## What this free workflow helps you test

This Free Lite workflow turns public or sanitized GitHub repository activity into a weekly Markdown snapshot you can review before wiring anything into Slack, Discord, Notion, or a Claude-powered narrative workflow.

It is useful if you want to:

- sanity-check weekly repo activity before a team update;
- evaluate n8n import/setup friction with a small workflow;
- produce a reviewable summary of recent PRs, issues, stale items, and follow-up questions;
- test an approval-first automation pattern before adding private workspace data.

### Safety boundary

Start with a public repo or sanitized sample payload. Do **not** paste tokens, private repository URLs, customer data, production logs, or proprietary workflow exports into public issues or screenshots.

If you try it and hit setup friction, open a public issue with:

1. your n8n version,
2. whether import succeeded,
3. which node failed,
4. sanitized error text,
5. whether you tested with a public repo or redacted sample data.

## What you get for free

- `workflows/free-lite-github-weekly-snapshot.json`
- Manual trigger + optional Friday 5pm schedule trigger
- Public GitHub API fetch for commits, merged PRs, and closed issues
- Markdown output that can be copied into Slack, Notion, Linear, or a weekly status doc
- Import checklist and public-safe troubleshooting guide: `docs/free-lite-import-checklist.md`
- 10-minute public demo runbook: `docs/free-lite-demo-runbook.md`
- Local validation preflight: `docs/free-lite-validation-preflight.md`
- Copyable sanitized issue examples: `docs/public-safe-issue-examples.md`
- Troubleshooting FAQ for import/API/output symptoms: `docs/free-lite-troubleshooting-faq.md`
- Public support/security boundary: `SECURITY.md`
- No Claude/Anthropic API key required
- No Slack webhook required
- No private repo access required by default

## Quick start

1. Import `workflows/free-lite-github-weekly-snapshot.json` into n8n.
2. Optionally set environment variables:
   - `GITHUB_REPO=owner/repo` — defaults to `n8n-io/n8n`
   - `LOOKBACK_DAYS=7`
   - `GITHUB_TOKEN=...` — optional, only for higher rate limits or repos you are authorized to inspect
3. Run the workflow manually and inspect the `markdown` field in the final node.
4. For a safer first pass, follow the 10-minute public demo runbook in `docs/free-lite-demo-runbook.md`.
5. If import or execution fails, use the 5-minute checklist in `docs/free-lite-import-checklist.md` and the troubleshooting FAQ in `docs/free-lite-troubleshooting-faq.md` before opening a public issue.

## Safety defaults

- The workflow reads GitHub activity and produces draft Markdown only.
- It does not post to Slack, write to Notion, merge PRs, comment on issues, or mutate repositories.
- It ships with placeholders only; do not paste secrets into workflow code.
- Review permissions and API credentials before adapting it for private repositories.

## Static validation

Run the included public-safety validator before sharing a modified workflow:

```bash
python3 scripts/validate_free_lite.py
```

The local validation preflight in `docs/free-lite-validation-preflight.md` expands this into a short release/support routine with `git diff --check`, screenshot safety checks, and public issue hygiene.

The validator checks that the workflow JSON is parseable, still includes the expected read-only GitHub snapshot nodes, keeps `GITHUB_TOKEN` optional, and does not contain common posting/mutating integrations or secret-like markers.

Before tagging a release or responding to public setup reports, also use the manual release/support checklist in `docs/public-release-checks.md`. For a public-safe first-run walkthrough, see `docs/free-lite-demo-runbook.md`. For copyable examples of safe public issue content, see `docs/public-safe-issue-examples.md`; for common import/API/output failures, see `docs/free-lite-troubleshooting-faq.md`.

## Full pack / paid help

The broader local pack currently contains additional workflows and support collateral for:

- Claude-powered weekly GitHub narrative summaries
- PR review risk digests
- Destructive command guard reports
- Meeting transcript action extraction
- Slack/Notion ops briefs
- Knowledge-base gap finding for RAG/search readiness
- AI workflow audit intake-to-backlog generation
- ROI snapshot calculation
- Lead-fit/proposal triage
- Pilot scope and quote drafting

If you want the full template pack, customization, or a fixed-scope AI workflow audit, open an inquiry here:

- **Template pack / customization inquiry:** https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=workflow-pack-inquiry.yml
- **Workflow audit / pilot inquiry:** https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=audit-pilot-inquiry.yml
- **Free Lite setup question:** https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-setup.yml
- **Free Lite feedback / integration request:** https://github.com/jh280722/n8n-claude-workflow-pack-free-lite/issues/new?template=free-lite-feedback.yml

## Public issue safety

The guided issue forms are designed for sanitized, public context only and blank issues are disabled. Do not post API keys, private repository URLs, customer data, internal logs with secrets, procurement/legal/KYC details, production credentials, or exploit details for a real private system. For the full public-support boundary, see `SECURITY.md`. If a paid engagement is scoped later, sensitive details should move to an approved private channel before implementation work begins.

## Support boundary

This free repo is a public preview and does not include managed implementation support. Buyers/users are responsible for their own n8n instance, API credentials, workspace permissions, and security review. Custom integration work should be scoped separately.

## Feedback requested

I am validating whether this small workflow is useful before adding heavier Claude/Slack/Notion automations.

Helpful feedback:

- Did the workflow import cleanly?
- Which setup step was unclear?
- Is the weekly summary format useful for maintainers or small teams?
- Which integration would be most useful next: Slack, Discord, Notion, or a Claude narrative summary?

Please keep feedback public-safe: no tokens, private repo names, customer data, internal incidents, or production logs.

## License

The free lite workflow in this repository is provided under the MIT License. The unreleased full pack, customizations, and client-specific implementation materials are not included in this repository.
