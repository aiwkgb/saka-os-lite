#!/usr/bin/env python3
"""Sync JSON demo data into dashboard/app-data.js."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / 'data'
OUT = ROOT / 'dashboard' / 'app-data.js'

payload = {}
for path in sorted(DATA_DIR.glob('*.json')):
    payload[path.stem] = json.loads(path.read_text(encoding='utf-8'))

OUT.write_text('window.SAKA_DATA = ' + json.dumps(payload, indent=2, ensure_ascii=False) + ';\n', encoding='utf-8')
print(f'OK: {OUT.relative_to(ROOT)} written')
