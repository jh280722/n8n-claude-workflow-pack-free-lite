# Free Lite output review guide

Use this guide after the workflow runs successfully and the final **Output Markdown Snapshot** node returns a `markdown` field. It helps you decide whether the Free Lite result is useful enough to keep, customize, or discuss as a sanitized upgrade/audit inquiry.

This guide is for a public repository or sanitized sample only. Do **not** paste tokens, credentials, private repository URLs, customer data, production logs, procurement details, KYC/tax information, payment details, or internal screenshots into public issues.

## 1. Confirm the output shape

Compare your result with `samples/sample-output.md`.

A healthy run should include:

- repository name and lookback window;
- counts for commits, merged PRs, and closed issues;
- short lists of notable commits, merged PRs, and closed issues when activity exists;
- a draft-only upgrade note or follow-up questions that you can review before sharing.

If the output is empty, first try a public repository with recent activity and increase `LOOKBACK_DAYS` to `30`. If it still looks wrong, use `docs/free-lite-troubleshooting-faq.md` before opening a public issue.

## 2. Score usefulness before asking for help

Use this quick local scorecard:

| Check | Good signal | If not true |
|---|---|---|
| Import worked | Workflow imports without missing node errors | Follow `docs/free-lite-import-checklist.md` |
| Activity appears | At least one section has real public repo activity | Increase `LOOKBACK_DAYS` or try a busier public repo |
| Markdown is reviewable | You can paste it into a team note after editing | Open sanitized feedback with the confusing section only |
| No accidental sharing risk | Output contains only public or synthetic information | Do not post it; rerun with a public repo or redacted sample |
| Next integration is clear | You know whether Slack, Discord, Notion, or Claude narrative is next | Open a sanitized integration request |

## 3. Public-safe feedback template

If you open an issue, share only public-safe details:

```markdown
## Output review

- n8n version:
- Public test repo used:
- LOOKBACK_DAYS:
- Did the final `markdown` field appear? yes/no
- Which section was most useful?
- Which section was confusing?
- Desired next integration: Slack / Discord / Notion / Claude narrative / other

I confirm this issue contains no tokens, credentials, private repository URLs, customer data, production logs, payment details, or KYC/tax information.
```

## 4. Upgrade/audit boundary

It is fine to ask public, sanitized questions about whether the draft template pack, customization, or an AI workflow audit might fit your use case.

Keep the discussion at the level of public workflow goals, sample output shape, integration preference, and generic constraints. Do not include secrets, private workspace details, customer data, proprietary incidents, or payment/KYC/tax information in the public repo.

No guaranteed ROI is claimed by this Free Lite repo. Any paid customization, audit, or implementation should be scoped separately with explicit approval and private handling of sensitive details.
