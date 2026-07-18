# Adoption Guide

This guide explains how to adapt SAKA OS Lite without turning it into a heavy system.

## The 10-minute adaptation

1. Open `data/projects.json`.
2. Replace demo projects with 2-5 active projects.
3. Open `data/content_pipeline.json`.
4. Add 3-10 content ideas or sales messages.
5. Open `data/opportunities.json`.
6. Add grants, free credits, leads, events, or follow-up opportunities.
7. Run:

```bash
python3 scripts/validate.py
python3 scripts/sync_dashboard_data.py
```

8. Open `dashboard/index.html`.

## Daily loop

Morning:

```bash
python3 scripts/generate_brief.py
```

Night:

```bash
python3 scripts/generate_log_template.py
```

Weekly:

- remove stale projects,
- update next actions,
- archive content that shipped,
- review opportunities.

## Recommended first users

This template is most useful for:

- solo founders,
- freelancers,
- small agencies,
- UMKM operators,
- creators managing offers/content,
- AI-assisted builders who need structure before automation.

## What not to do

Do not use this public repo as your private CRM, finance ledger, legal vault, or customer database.

Fork privately if you want to store real operational data.
