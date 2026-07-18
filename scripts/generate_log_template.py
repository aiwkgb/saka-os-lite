#!/usr/bin/env python3
"""Generate a copy-pasteable Daily LOG template."""
from __future__ import annotations

from datetime import date

print(f'# Daily LOG - {date.today().isoformat()}')
print()
print('## Shipped')
print('- ')
print('## Leads / follow-up')
print('- ')
print('## Blockers')
print('- ')
print('## Tomorrow')
print('- ')
print('## Privacy check')
print('- Did I keep sensitive data out of public files? ')
