# Contributing

Thanks for your interest in SAKA OS Lite.

This project is intentionally small: demo JSON, beginner-readable Python scripts, and a static dashboard. Contributions should keep it useful for low-resource solo operators and small-business owners.

## Good first contributions

- Improve documentation clarity.
- Add safe demo examples.
- Fix typos.
- Improve accessibility and mobile layout.
- Add deployment notes.
- Add import/export examples that do not require paid APIs.
- Translate docs between English and Indonesian.

## Privacy rules

Do not include private client data, phone numbers, emails, API keys, ad account IDs, invoices, or screenshots from real accounts unless you have explicit permission.

Use demo/fake data only.

## Development

Run this before opening a pull request:

```bash
python3 scripts/validate.py
python3 scripts/generate_brief.py
python3 scripts/generate_log_template.py
python3 scripts/sync_dashboard_data.py
node --check dashboard/app.js
node --check dashboard/app-data.js
```

If you change data shape, update:

- `scripts/validate.py`
- `scripts/sync_dashboard_data.py`
- `dashboard/app.js`
- README/Quickstart docs

## Pull request checklist

- [ ] Demo data only; no private/sensitive data.
- [ ] Validation passes.
- [ ] Dashboard still opens with sample data.
- [ ] README/docs updated if behavior changed.
- [ ] The change keeps the project beginner-friendly.
