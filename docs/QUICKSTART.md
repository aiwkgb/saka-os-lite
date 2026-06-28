# Quick Start

This guide helps you run SAKA OS Lite locally.

## 1. Clone the repo

```bash
git clone https://github.com/aiwkgb/saka-os-lite.git
cd saka-os-lite
```

## 2. Validate demo data

```bash
python3 scripts/validate.py
```

Expected output:

```text
OK: SAKA OS Lite demo data valid
```

## 3. Generate a Daily BRIEF

```bash
python3 scripts/generate_brief.py
```

Example output:

```text
# Daily BRIEF
- P0 Website Service Offer: Publish one landing page offer and contact 5 prospects
- P1 Content Engine: Prepare 3 posts tied to one paid offer
```

## 4. Generate a LOG template

```bash
python3 scripts/generate_log_template.py
```

Use the output as an end-of-day checkpoint.

## 5. Sync dashboard data

```bash
python3 scripts/sync_dashboard_data.py
```

This refreshes:

```text
dashboard/app-data.js
```

## 6. Open dashboard

Open this file in your browser:

```text
dashboard/index.html
```

## 7. Edit demo data

Try editing:

```text
data/projects.json
data/content_pipeline.json
data/opportunities.json
```

Then run again:

```bash
python3 scripts/validate.py
python3 scripts/sync_dashboard_data.py
```

## 8. Safety reminder

If you fork or adapt this repo publicly, keep it demo-only.

Do not commit real names, phone numbers, emails, ad account IDs, API keys, invoices, or private operational data.

Read [`SANITIZATION.md`](SANITIZATION.md) before publishing.
