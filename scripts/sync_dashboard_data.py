from pathlib import Path
import json
payload={p.stem: json.loads(p.read_text()) for p in Path('data').glob('*.json')}
Path('dashboard/app-data.js').write_text('window.SAKA_DATA = '+json.dumps(payload, indent=2)+';'+chr(10))
print('OK: dashboard/app-data.js written')
