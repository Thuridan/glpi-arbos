#!/usr/bin/env python3
"""Normalize reviewed structural exports; never import configuration/data dumps."""
import json
import sys
from pathlib import Path

if len(sys.argv)!=3:
    raise SystemExit('Usage: update_snapshots.py runtime-export.json commands-export.json')
output=Path(__file__).resolve().parents[1]/'inventory'
runtime=json.loads(Path(sys.argv[1]).read_text())
assert set(runtime)=={'version','api_version','api','web','relations'}
expected_api={'path','methods','security','scopes','version','controller','method','source','line'}
assert all(set(r)==expected_api for r in runtime['api'])
assert all(set(r)=={'name','path','methods','controller'} for r in runtime['web'])
runtime['api']=list({json.dumps(r,sort_keys=True):r for r in runtime['api']}.values())
commands=json.loads(Path(sys.argv[2]).read_text())
commands={'application':commands['application'],'commands':[
    {'name':c['name'],'aliases':c.get('aliases',[]),'description':c.get('description','')}
    for c in commands['commands']]}
for name,data in [('runtime.json',runtime),('commands.json',commands)]:
    (output/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print('Structural snapshots normalized; review the diff before committing.')
