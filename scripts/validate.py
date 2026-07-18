#!/usr/bin/env python3
"""Validate SAKA OS Lite demo JSON data and basic repo hygiene."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'data'

REQUIRED_FILES = {
    'projects.json': {'id', 'name', 'status', 'priority', 'next_action', 'owner'},
    'content_pipeline.json': {'id', 'brand', 'channel', 'status', 'hook', 'cta'},
    'opportunities.json': {'id', 'type', 'title', 'status', 'source_url', 'next_action'},
}

FORBIDDEN_MARKERS = ['api_key', 'secret', 'password', 'token=', 'private_key', 'BEGIN RSA PRIVATE KEY']


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        raise SystemExit(f'ERROR: invalid JSON in {path.relative_to(ROOT)}: {exc}') from exc


def validate_rows(path: Path, required: set[str]) -> int:
    rows = load_json(path)
    if not isinstance(rows, list):
        raise SystemExit(f'ERROR: {path.relative_to(ROOT)} must be a JSON array')
    seen = set()
    for idx, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            raise SystemExit(f'ERROR: {path.relative_to(ROOT)} row {idx} must be an object')
        missing = sorted(required - set(row))
        if missing:
            raise SystemExit(f'ERROR: {path.relative_to(ROOT)} row {idx} missing keys: {", ".join(missing)}')
        row_id = str(row.get('id', '')).strip()
        if not row_id:
            raise SystemExit(f'ERROR: {path.relative_to(ROOT)} row {idx} has empty id')
        if row_id in seen:
            raise SystemExit(f'ERROR: duplicate id {row_id!r} in {path.relative_to(ROOT)}')
        seen.add(row_id)
    return len(rows)


def scan_for_secret_markers() -> None:
    # Scan executable/demo payload areas. Docs intentionally mention words like
    # "secrets" in safety checklists, so scanning docs would create false positives.
    scan_paths = [ROOT / 'data', ROOT / 'dashboard']
    for base in scan_paths:
        for path in base.rglob('*'):
            if not path.is_file() or path.suffix.lower() not in {'.json', '.js', '.md', '.py', '.html', '.css'}:
                continue
            text = path.read_text(encoding='utf-8', errors='ignore').lower()
            for marker in FORBIDDEN_MARKERS:
                if marker.lower() in text:
                    raise SystemExit(f'ERROR: possible secret marker {marker!r} in {path.relative_to(ROOT)}')


def main() -> None:
    if not DATA_DIR.exists():
        raise SystemExit('ERROR: data/ directory missing')
    counts = {}
    for filename, required in REQUIRED_FILES.items():
        path = DATA_DIR / filename
        if not path.exists():
            raise SystemExit(f'ERROR: missing {path.relative_to(ROOT)}')
        counts[filename] = validate_rows(path, required)
    scan_for_secret_markers()
    print('OK: SAKA OS Lite demo data valid')
    print('Counts: ' + ', '.join(f'{name}={count}' for name, count in counts.items()))


if __name__ == '__main__':
    main()
