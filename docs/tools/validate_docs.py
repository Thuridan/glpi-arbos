#!/usr/bin/env python3
"""Check links and independently compare inventory coverage with source manifests."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

root=Path(__file__).resolve().parents[2]
docs=root/'docs'
errors=[]
summary=json.loads((docs/'inventory/summary.json').read_text())
def check(condition,message):
    if not condition: errors.append(message)

for p in docs.rglob('*.md'):
    data=p.read_text()
    for match in re.finditer(r'\[[^\]\n]*\]\(([^)\n]+)\)',data):
        target=match[1].strip().strip('<>')
        if target.startswith('#') or urlsplit(target).scheme: continue
        target=unquote(target.split('#',1)[0].split('?',1)[0])
        check((p.parent/target).exists(),f'Broken link: {p.relative_to(root)} -> {target}')
    check(not re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bgh[pousr]_[A-Za-z0-9]{30,}',data),f'Potential secret: {p}')
sql=(root/'install/mysql/glpi-empty.sql').read_text()
names=re.findall(r'^CREATE TABLE `([^`]+)`',sql,re.M)
headings=re.findall(r'^## (glpi_\S+)$',(docs/'DATABASE_SCHEMA.md').read_text(),re.M)
check(set(names)==set(headings) and len(names)==len(headings),'DDL table coverage differs')
column_count=len(re.findall(r'^[ \t]+`[^`]+`[ \t]+',sql,re.M))
check(column_count==summary['schema_columns'],'DDL column count differs')
check(len(names)==summary['schema_tables'],'DDL table count differs')
check(hashlib.sha256(sql.encode()).hexdigest()==summary['schema_sha256'],'DDL digest differs')
lock=json.loads((root/'composer.lock').read_text())
npm=json.loads((root/'package-lock.json').read_text())
check(summary['composer_runtime_packages']==len(lock['packages']),'Composer runtime count differs')
check(summary['composer_dev_packages']==len(lock['packages-dev']),'Composer dev count differs')
check(summary['npm_installations']==len(npm['packages'])-1,'npm count differs')
tracked=subprocess.check_output(['git','ls-files','-z'],cwd=root).decode().split('\0')
tracked={p for p in tracked if p and not p.startswith('docs/')}
check(len(tracked)==summary['tracked_files_outside_docs'],'Git inventory count differs')
code=(docs/'CODE_INDEX.md').read_text()
for p in tracked: check(f'](../{p})' in code,f'File absent from CODE_INDEX: {p}')
modules=(docs/'MODULES.md').read_text()
for p in (root/'src/Glpi').iterdir():
    if p.is_dir(): check(f'](../src/Glpi/{p.name}/)' in modules,f'Module absent: {p.name}')
runtime=json.loads((docs/'inventory/runtime.json').read_text())
unique={json.dumps(r,sort_keys=True) for r in runtime['api']}
check(len(unique)==summary['api_unique_routes'],'API route count differs')
check(len(runtime['web'])==summary['web_routes_dev'],'Web route count differs')
commands=json.loads((docs/'inventory/commands.json').read_text())
check(len(commands['commands'])==summary['cli_commands_dev'],'CLI count differs')
check(all(set(c)=={'name','aliases','description'} for c in commands['commands']),'Command snapshot has unexpected fields')
check(set(runtime)=={'version','api_version','api','web','relations'},'Runtime snapshot has unexpected fields')
if len(sys.argv)>1:
    actual={s.split('\t')[0] for s in Path(sys.argv[1]).read_text().splitlines() if s}
    check(actual==set(names),'Runtime database tables differ from source DDL')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'OK: links, {len(tracked)} files, {len(names)} tables, {column_count} columns, lockfile counts, modules, routes and snapshot fields')
