#!/usr/bin/env python3
"""Generate a simple Daily BRIEF from demo project data."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
projects = json.loads((ROOT / 'data' / 'projects.json').read_text(encoding='utf-8'))

print('# Daily BRIEF')
for project in projects:
    priority = project.get('priority', 'P?')
    name = project.get('name', 'Untitled project')
    next_action = project.get('next_action', 'Choose the next action')
    print(f'- {priority} {name}: {next_action}')
