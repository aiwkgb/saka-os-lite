from pathlib import Path
import json
for path in Path('data').glob('*.json'):
    json.loads(path.read_text())
print('OK: SAKA OS Lite demo data valid')
