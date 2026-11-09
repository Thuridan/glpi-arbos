#!/usr/bin/env python3
"""Generate structural Markdown inventories without reading application data or secrets."""
import collections
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / 'docs'
INV = DOCS / 'inventory'

def text(path):
    return (ROOT / path).read_text(errors='replace')

def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ').replace('\r', '')

def source(path):
    return f'[{cell(path)}](../{path})'

def write(name, lines):
    (DOCS / name).write_text('\n'.join(lines).rstrip() + '\n')

def table(lines, headers, rows):
    lines += ['', '| ' + ' | '.join(headers) + ' |', '| ' + ' | '.join('---' for _ in headers) + ' |']
    lines += ['| ' + ' | '.join(cell(v) for v in row) + ' |' for row in rows]
    lines += ['']

files = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
files = sorted(p for p in files if p and not p.startswith('docs/'))
sql = text('install/mysql/glpi-empty.sql')
blocks = list(re.finditer(r'^CREATE TABLE `([^`]+)` \((.*?)^\) (ENGINE\s*=\s*[^;]+);', sql, re.S | re.M))
assert {m[1] for m in blocks} == set(re.findall(r'CREATE TABLE `([^`]+)`', sql)), 'Incomplete schema extraction'
columns = 0
lines = ['# Dicionário completo do esquema SQL', '',
         'Gerado por [generate_inventory.py](tools/generate_inventory.py). Fonte: ' + source('install/mysql/glpi-empty.sql') + '.', '',
         'Contém tipos, nulabilidade, defaults, índices e opções de todas as tabelas do esquema de instalação. Não contém registros do banco.', '',
         'Os nomes de colunas não comprovam foreign keys físicas. Consulte [DATABASE.md](DATABASE.md) e [DATABASE_RELATIONS.md](DATABASE_RELATIONS.md).']
table(lines, ['Tabela', 'Colunas', 'Índices declarados'], ((f'[{m[1]}](#{m[1]})', len(re.findall(r'^[ \t]+`',m[2],re.M)), len(re.findall(r'^[ \t]+(?:PRIMARY KEY|UNIQUE KEY|KEY|FULLTEXT KEY|SPATIAL KEY)',m[2],re.M))) for m in blocks))
for m in blocks:
    cols = re.findall(r'^[ \t]+`([^`]+)`[ \t]+(.*?)(?:,)?$', m[2], re.M)
    columns += len(cols)
    line = sql.count('\n', 0, m.start()) + 1
    lines += [f'## {m[1]}', '', f'Origem: [DDL, linha {line}](../install/mysql/glpi-empty.sql#L{line}).', '', '`' + m[3] + '`']
    table(lines, ['Coluna', 'Definição SQL'], ((f'`{name}`', f'`{definition.rstrip(",")}`') for name,definition in cols))
    indexes = [s.strip().rstrip(',') for s in m[2].splitlines() if s.strip().startswith(('PRIMARY KEY', 'UNIQUE KEY', 'KEY ', 'FULLTEXT KEY', 'SPATIAL KEY', 'CONSTRAINT'))]
    if indexes:
        lines += ['Índices/constraints declarados:', '', '```sql'] + indexes + ['```', '']
write('DATABASE_SCHEMA.md', lines)

lines = ['# Inventário completo de arquivos versionados', '',
         'Gerado do índice Git, excluindo `docs/` para evitar um inventário recursivo. Arquivos ignorados, dependências instaladas, segredos e dados locais não são percorridos.', '',
         'O símbolo exibido é a primeira declaração de classe/interface/trait/enum encontrada; não é um grafo de chamadas. Arquivos de terceiros versionados em `lib/` fazem parte do catálogo.']
counts = collections.Counter(p.split('/')[0] if '/' in p else '(raiz)' for p in files)
table(lines,['Área','Arquivos'],sorted(counts.items()))
for area in sorted(counts):
    lines += [f'## {area}', '']
    rows = []
    for p in files:
        if (p.split('/')[0] if '/' in p else '(raiz)') != area: continue
        symbol = ''
        if p.endswith('.php') and (ROOT/p).is_file():
            s = text(p)
            decl = re.search(r'^(?:(?:abstract|final|readonly)\s+)*(class|interface|trait|enum)\s+(\w+)(?:\s+extends\s+([\w\\]+))?',s,re.M)
            ns = re.search(r'^namespace\s+([^;]+);',s,re.M)
            if decl: symbol = decl[1]+' '+((ns[1]+'\\') if ns else '')+decl[2]+((' extends '+decl[3]) if decl[3] else '')
        rows.append((source(p),Path(p).suffix or 'sem extensão',symbol or '—'))
    table(lines,['Arquivo','Extensão','Declaração principal'],rows)
write('CODE_INDEX.md',lines)

composer=json.loads(text('composer.json')); lock=json.loads(text('composer.lock'))
package=json.loads(text('package.json')); npm=json.loads(text('package-lock.json'))
lines=['# Dependências: inventário dos manifestos e lockfiles','','Gerado dos quatro manifestos/lockfiles da raiz. Versões são o snapshot do repositório; não são uma verificação de vulnerabilidades nem de licenças. Restrições e versões resolvidas são informações diferentes.']
for label,key in [('PHP: requisitos diretos de runtime','require'),('PHP: requisitos diretos de desenvolvimento','require-dev')]:
    lines += [f'## {label}']
    resolved={p['name']:p['version'] for p in lock['packages']+lock.get('packages-dev',[])}
    table(lines,['Pacote ou plataforma','Restrição','Resolvido'],((k,v,resolved.get(k,'plataforma/extensão')) for k,v in sorted(composer[key].items())))
for label,key in [('npm: requisitos diretos de runtime','dependencies'),('npm: requisitos diretos de desenvolvimento','devDependencies')]:
    lines += [f'## {label}']
    table(lines,['Pacote','Restrição','Resolvido'],((k,v,npm['packages'].get('node_modules/'+k,{}).get('version','—')) for k,v in sorted(package[key].items())))
lines += ['## Composer: todos os pacotes resolvidos']
table(lines,['Pacote','Versão','Grupo','Licença declarada'],((p['name'],p['version'],group,', '.join(p.get('license',[]))) for group,key in [('runtime','packages'),('dev','packages-dev')] for p in sorted(lock.get(key,[]),key=lambda p:p['name'])))
lines += ['## npm: todas as instalações resolvidas','','Inclui instalações aninhadas. A coluna dev é o marcador do lockfile, não uma análise independente de uso no código.']
table(lines,['Caminho de instalação','Versão','Dev','Licença declarada'],((path,p.get('version','—'),p.get('dev',False),p.get('license','—')) for path,p in sorted(npm['packages'].items()) if path))
for label,key in [('Composer: sugestões de extensão/pacote','suggest'),('Composer: provide','provide'),('Composer: replace','replace')]:
    lines += ['## '+label]
    table(lines,['Nome','Declaração'],sorted(composer.get(key,{}).items()))
for label,scripts in [('Composer: scripts',composer.get('scripts',{})),('npm: scripts',package.get('scripts',{})),('npm: overrides',package.get('overrides',{}))]:
    lines += ['## '+label]
    table(lines,['Nome','Definição'],((k,'`'+json.dumps(v,ensure_ascii=False)+'`') for k,v in scripts.items()))
write('DEPENDENCIES_LOCK.md',lines)

runtime=json.loads((INV/'runtime.json').read_text())
unique={json.dumps(r,sort_keys=True):r for r in runtime['api']}
routes=sorted(unique.values(),key=lambda r:(r['path'],str(r['methods']),r['controller'],r['method']))
lines=['# Catálogo das rotas da API de alto nível','','Snapshot obtido por introspecção de `Router::getAllRoutes()` em Dev. Versão padrão do roteador: `'+runtime['api_version']+'`.', '',
       'Prefixar os caminhos abaixo com `/api.php` ou `/api.php/v<versão>`. O catálogo inclui as declarações de todas as versões; disponibilidade depende de `introduced`, `deprecated`, `removed`, configuração e permissões.', '',
       'Entradas idênticas retornadas pelo registro foram deduplicadas. Um método HTTP múltiplo permanece na mesma linha. Segurança 0 significa rota declarada sem autenticação; isso não ignora a configuração global que desativa a API.', '',
       'Corpos, schemas e parâmetros completos são definidos pelas anotações `Doc` e pelo gerador OpenAPI. Este catálogo não substitui o contrato `/api.php/doc.json`.']
table(lines,['Controller','Rotas únicas'],sorted(collections.Counter(r['controller'].split('\\')[-1] for r in routes).items()))
for controller in sorted(set(r['controller'] for r in routes)):
    lines += ['## '+controller.split('\\')[-1]]
    table(lines,['Métodos','Caminho','Introduzida / depreciada / removida','Segurança / scopes','Implementação'],(
        (', '.join(r['methods']) or 'qualquer', '`'+r['path']+'`', ' / '.join(r['version'].get(k,'') or '—' for k in ['introduced','deprecated','removed']), str(r['security'])+' / '+', '.join(r['scopes']), f"[{r['method']}](../{r['source']}#L{r['line']})")
        for r in routes if r['controller']==controller))
write('API_ROUTES.md',lines)
lines=['# Catálogo de rotas web Symfony','','Snapshot em Dev obtido de `router->getRouteCollection()`. Não é um inventário de endpoints REST legados nem das rotas internas do roteador HL.', '',
       'Métodos vazios significam ausência de restrição no objeto de rota. Reescrita, listeners, rotas de itemtype, plugins e ambiente podem alterar a resolução. Rotas de profiler/development não devem ser interpretadas como disponíveis em Prod.']
table(lines,['Nome','Caminho','Métodos','Controller'],((r['name'],'`'+r['path']+'`',', '.join(r['methods']) or 'qualquer',r['controller']) for r in runtime['web']))
write('WEB_ROUTES.md',lines)
lines=['# Relações declaradas pela aplicação','','Extraído de `$RELATION` em ' + source('inc/relation.constant.php') + '.', '',
       'Não são foreign keys DDL. O lado esquerdo de cada seção é a tabela referenciada; as linhas indicam a tabela que aponta para ela. Prefixo `_` na tabela ligada desativa o controle genérico de uso durante exclusão porque há tratamento específico na aplicação. Pares `items_id`/`itemtype` representam relações polimórficas.', '',
       'Além deste mapa existem relações inferidas em classes e módulos; não trate esta lista como todas as invariantes de negócio.']
relations=runtime.get('relations',{})
for target,refs in sorted(relations.items()):
    lines += ['## '+target]
    table(lines,['Tabela ligada (nome no mapa)','Coluna ou estrutura de ligação'],((k,'`'+json.dumps(v,ensure_ascii=False)+'`') for k,v in refs.items()))
write('DATABASE_RELATIONS.md',lines)
commands=json.loads((INV/'commands.json').read_text())
lines=['# Comandos CLI disponíveis em Dev','','Extraído de `php bin/console list --format=json`. A disponibilidade em Prod difere porque a imagem exclui `tools/` e usa autoload sem desenvolvimento.', '',
       'Este documento lista comandos; não os executa. Comandos de instalação, atualização, limpeza e migração alteram estado. Consulte `php bin/console <comando> --help` e as condições do fluxo Dev/Prod antes de executá-los.']
table(lines,['Comando','Aliases','Descrição'],((c['name'],', '.join(c.get('aliases',[])),c.get('description','')) for c in commands['commands']))
write('CLI_COMMANDS.md',lines)
summary={'source_commit':subprocess.check_output(['git','log','-1','--format=%H','--','.',':(exclude)docs/**'],cwd=ROOT,text=True).strip(),'glpi_version':runtime['version'],'api_version':runtime['api_version'],'tracked_files_outside_docs':len(files),'schema_tables':len(blocks),'schema_columns':columns,'schema_sha256':hashlib.sha256(sql.encode()).hexdigest(),'ddl_foreign_keys':len(re.findall(r'FOREIGN KEY\s*\(',sql)),'api_unique_routes':len(routes),'web_routes_dev':len(runtime['web']),'cli_commands_dev':len(commands['commands']),'composer_runtime_packages':len(lock['packages']),'composer_dev_packages':len(lock.get('packages-dev',[])),'npm_installations':len(npm['packages'])-1}
(INV/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
