# Sanitization Checklist

Use this checklist before publishing a fork, screenshot, demo, blog post, or public template based on SAKA OS Lite.

## Quick rule

If the data came from a real person, client, account, invoice, chat, legal document, ad account, or private operation, do not publish it.

Use demo data only.

## Remove before publishing

- Real client or brand names unless explicitly approved.
- Phone numbers and WhatsApp numbers.
- Email addresses.
- Ad account IDs, campaign IDs, pixel IDs, analytics IDs.
- API keys, tokens, passwords, private keys, `.env` files.
- Invoices, receipts, contracts, legal documents.
- Bank, e-wallet, finance, debt, salary, or payment details.
- Private leads, prospects, customer notes, or support tickets.
- Screenshots from real dashboards, chats, ads accounts, finance apps, or private tools.
- Local machine paths that reveal private usernames or sensitive structure.

## Safe replacements

Use:

- fictional names,
- placeholder contact values,
- fake project names,
- demo metrics,
- generic screenshots,
- redacted screenshots only if you are sure nothing private remains.

## Files to check

Before publishing, review:

```text
data/*.json
dashboard/app-data.js
README.md
docs/*.md
docs/*.html
screenshots or assets
commit history
```

## Commands

Run validation:

```bash
python3 scripts/validate.py
```

Optional text scan examples:

```bash
grep -R "API_KEY\|TOKEN\|PASSWORD\|SECRET" .
grep -R "PHONE_PLACEHOLDER\|WHATSAPP_PLACEHOLDER" .
```

## Public repo standard

A public SAKA OS Lite-based repo should include:

- demo data only,
- clear README,
- privacy note,
- sanitization checklist,
- license,
- no private operational state.

## If unsure

Do not publish. Create a new demo example from scratch.
