# Security and public-support boundary

This repository is a free, read-only n8n workflow template. It is not a hosted service and does not need production credentials for the default public-repo demo.

## What is safe to share publicly

When opening a GitHub issue, include only sanitized setup details:

- n8n version;
- whether import succeeded;
- the public test repository used, or the phrase `private repo tested` without naming it;
- failing node name;
- redacted error text;
- whether the final `markdown` field appeared.

## Do not post sensitive data

Do **not** paste any of the following into public issues, screenshots, logs, or workflow exports:

- GitHub tokens, Anthropic/Claude keys, Slack/Discord/Notion credentials, webhook URLs, cookies, or session tokens;
- private repository URLs, customer names, internal organization names, production incident details, or proprietary workflow exports;
- invoices, procurement details, legal/KYC/tax/bank/payout information, or contract terms;
- exploit payloads or reproduction steps that would expose a real private system.

## If you think you found a security issue

1. Reproduce it with the default public demo repository (`n8n-io/n8n`) or a fully synthetic sample.
2. Strip all secrets, private URLs, customer data, and production details.
3. Open a public issue only with the sanitized symptom, affected workflow node, n8n version, and expected/actual behavior.

If your finding cannot be described safely without exposing secrets or a real private system, do not publish the details in this repository. Keep the details private until an approved private disclosure channel exists.

## Maintainer response boundary

For this free preview, public support is limited to template import, static validation, public-repo demo runs, and sanitized troubleshooting. Custom private-repo integrations, production credential review, paid implementation work, or security-sensitive debugging must be scoped separately before any private data is shared.
