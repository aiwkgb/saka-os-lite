# SAKA OS Lite

**SAKA OS Lite** is an open-source starter template for solo founders, freelancers, and small-business operators who want a simple **AI-assisted daily operating cockpit** before they buy complex tools or build full automation.

> In 10 minutes, turn scattered work into one cockpit: focus, projects, content, opportunities, and an end-of-day log.

## Ringkasan Bahasa Indonesia

SAKA OS Lite adalah template operating system ringan untuk solo operator, freelancer, dan pelaku UMKM yang ingin punya pusat kendali harian berbasis file sederhana.

Fokusnya:

- Project Radar
- Daily BRIEF / LOG
- Content Pipeline
- Opportunity Tracker
- Static Dashboard
- Privacy-first demo data
- Approval/safety habits before automation

## Live demo

GitHub Pages:

https://aiwkgb.github.io/saka-os-lite/

Local dashboard:

```text
dashboard/index.html
```

## Who this is for

- Solo operators who juggle many small projects.
- Freelancers who need a lightweight daily cockpit.
- UMKM/small-business operators who need follow-up and content clarity.
- AI-assisted builders who want an agent-ready operating habit before adding automation.
- Non-technical founders who need structure before using AI tools.

## What problem it solves

Many small operators do not fail because they lack ideas. They fail because work is scattered:

```text
notes in chat apps
content ideas in random docs
follow-ups forgotten
opportunities not tracked
no daily focus
no clean handoff to AI assistants
```

SAKA OS Lite gives them a tiny source-of-truth that is easy to copy, inspect, and adapt.

## What it includes

- **Project Radar** — active projects, priority, next action, owner.
- **Daily BRIEF** — generated text summary of what matters today.
- **Daily LOG template** — simple end-of-day reflection/checkpoint.
- **Content Pipeline** — demo content workflow from idea to publish.
- **Opportunity Tracker** — demo bounty/freebie/credit/opportunity watchlist.
- **Static Dashboard** — local dashboard generated from JSON data.
- **Sanitization guide** — privacy checklist before publishing or adapting.
- **OSS-ready docs** — roadmap, contributing guide, security notes, issue templates.

## Quick start

Requirements:

- Python 3.10+
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

## Example operating loop

1. Edit `data/projects.json` with your active projects.
2. Edit `data/content_pipeline.json` with content ideas and approval status.
3. Edit `data/opportunities.json` with grants, leads, free credits, or events to watch.
4. Run `python3 scripts/validate.py`.
5. Run `python3 scripts/generate_brief.py` each morning.
6. Run `python3 scripts/generate_log_template.py` at night.
7. Run `python3 scripts/sync_dashboard_data.py` and open the dashboard.

## Documentation

- [`docs/WHY.md`](docs/WHY.md) — why this project exists.
- [`docs/QUICKSTART.md`](docs/QUICKSTART.md) — beginner-friendly setup and first run.
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — public roadmap.
- [`docs/ADOPTION.md`](docs/ADOPTION.md) — how to adapt this template.
- [`docs/OSS_READINESS_AUDIT.md`](docs/OSS_READINESS_AUDIT.md) — current readiness score and next improvements.
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
5. repeatable daily loop,
6. approval habits before automation.

Start with structure. Add automation later.

## Good first contributions

- Improve documentation and beginner onboarding.
- Add safe demo examples for different operator types.
- Improve dashboard accessibility/mobile layout.
- Add export/import examples.
- Translate docs between English and Indonesian.

## License

MIT License. See [`LICENSE`](LICENSE).
