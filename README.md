# SAKA OS Lite

**SAKA OS Lite** is a public-safe operating template for solo operators, freelancers, and Indonesian UMKM operators who want an AI-assisted daily command center.

It is designed for people who do not need a complex SaaS stack yet. They need a simple way to see priorities, keep projects moving, prepare content, track opportunities, and resume work without starting from zero.

## Ringkasan Bahasa Indonesia

SAKA OS Lite adalah template operating system ringan untuk solo operator, freelancer, dan pelaku UMKM yang ingin punya pusat kendali harian berbasis file sederhana.

Fokusnya:

- Project Radar
- Daily BRIEF / LOG
- Content Pipeline
- Opportunity Tracker
- Static Dashboard
- Privacy-first demo data

## Live demo

After GitHub Pages is enabled:

https://aiwkgb.github.io/saka-os-lite/

Local dashboard:

```text
dashboard/index.html
```

## Who this is for

- Solo operators who juggle many small projects.
- Freelancers who need a lightweight daily cockpit.
- UMKM operators who want simple follow-up and content tracking.
- AI-assisted builders who want an agent-ready operating habit before adding automation.
- Non-technical founders who need clarity before using AI tools.

## What it includes

- **Project Radar** — active projects, priority, next action, owner.
- **Daily BRIEF** — a generated text summary of what matters today.
- **Daily LOG template** — a simple end-of-day reflection/checkpoint.
- **Content Pipeline** — demo content workflow from idea to publish.
- **Opportunity Tracker** — demo bounty/freebie/credit/opportunity watchlist.
- **Static Dashboard** — local dashboard generated from JSON data.
- **Sanitization guide** — privacy checklist before publishing or adapting.

## Quick start

Requirements:

- Python 3
- Git
- A browser

Run from repo root:

```bash
python3 scripts/validate.py
python3 scripts/generate_brief.py
python3 scripts/generate_log_template.py
python3 scripts/sync_dashboard_data.py
```

Then open:

```text
dashboard/index.html
```

For a more detailed guide, read [`docs/QUICKSTART.md`](docs/QUICKSTART.md).

## Documentation

- [`docs/WHY.md`](docs/WHY.md) — why this project exists.
- [`docs/QUICKSTART.md`](docs/QUICKSTART.md) — beginner-friendly setup and first run.
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — public roadmap.
- [`docs/SANITIZATION.md`](docs/SANITIZATION.md) — privacy and public repo safety checklist.
- [`docs/SCREENSHOTS.md`](docs/SCREENSHOTS.md) — how to capture safe screenshots.
- [`docs/RELEASE_NOTES_v0.2.0.md`](docs/RELEASE_NOTES_v0.2.0.md) — current release notes.

## Data files

```text
data/projects.json
data/content_pipeline.json
data/opportunities.json
```

All data in this public repo is demo data. Replace it with your own private copy if you use this for real operations.

## Privacy first

This public template contains only demo data.

Do not commit:

- real client names,
- phone numbers,
- emails,
- ad account IDs,
- API keys/tokens/passwords,
- invoices,
- private leads,
- screenshots from real accounts,
- sensitive personal/family/finance/legal data.

Use [`docs/SANITIZATION.md`](docs/SANITIZATION.md) before publishing any adapted version.

## How this relates to AI agents

SAKA OS Lite is not a full autonomous agent framework. It is the operating substrate that makes agents more useful later:

1. clear data,
2. explicit next actions,
3. simple validation,
4. public-safe templates,
5. repeatable daily loop.

Start with structure. Add automation later.

## License

MIT License. See [`LICENSE`](LICENSE).
