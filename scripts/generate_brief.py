import json
from pathlib import Path
projects=json.loads(Path('data/projects.json').read_text())
print('# Daily BRIEF')
for p in projects:
    print('- '+p['priority']+' '+p['name']+': '+p['next_action'])
