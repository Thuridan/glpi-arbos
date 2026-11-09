# Mapeamento técnico do GLPI Arbos

Documentação do sistema em `/home/toor/glpi`, baseada no código `12.0.2-dev` do commit-base `da39b904ef` e na configuração local Dev/Prod. O [resumo de extração](inventory/summary.json) registra versão, commit de origem, contagens e hash do DDL. Os commits posteriores desta tarefa acrescentam documentação, sem alterar o esquema ou as regras de negócio descritas.

## Mapas explicativos

| Documento | Conteúdo |
| --- | --- |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Camadas, bootstrap, dependências entre componentes e topologia |
| [CODE.md](CODE.md) | Diretórios, autoload, classes-base e percursos de investigação |
| [MODULES.md](MODULES.md) | Domínios de negócio e todos os diretórios imediatos de `src/Glpi/` |
| [DATA_FLOWS.md](DATA_FLOWS.md) | Gravação, atendimento, formulários, inventário, documentos e exclusão |
| [APIS.md](APIS.md) | REST legada, API HL, OAuth, GraphQL, inventário e CalDAV |
| [DATABASE.md](DATABASE.md) | Persistência, convenções, relações lógicas, migrações e separação de dados |
| [DEPENDENCIES.md](DEPENDENCIES.md) | Plataforma, bibliotecas, ferramentas e preparação dos artefatos |
| [FRONTEND.md](FRONTEND.md) | Twig, JavaScript/Vue, estilos, build e traduções |
| [SECURITY.md](SECURITY.md) | Autenticação, perfis/entidades, CSRF, chaves e fronteiras de confiança |
| [CONFIGURATION.md](CONFIGURATION.md) | Configuração PHP/banco/Compose, flags e diretórios de estado |
| [INTEGRATIONS.md](INTEGRATIONS.md) | Agentes, identidade, e-mail, notificações, tarefas e serviços opcionais |
| [EXTENSIBILITY.md](EXTENSIBILITY.md) | Hooks, plugins, capacidades e customização |
| [OPERATIONS.md](OPERATIONS.md) | Ambientes, implantação, saúde, persistência, backup e rollback |
| [TESTING.md](TESTING.md) | Suítes, CI, critérios de teste e validação do mapeamento |

## Catálogos completos gerados

| Catálogo | Cobertura neste snapshot |
| --- | --- |
| [CODE_INDEX.md](CODE_INDEX.md) | 5.223 arquivos versionados fora de `docs/`; símbolos PHP principais |
| [DATABASE_SCHEMA.md](DATABASE_SCHEMA.md) | 447 tabelas e 4.748 colunas; definições SQL e índices |
| [DATABASE_RELATIONS.md](DATABASE_RELATIONS.md) | Mapa `$RELATION` da aplicação; não são FKs físicas |
| [DEPENDENCIES_LOCK.md](DEPENDENCIES_LOCK.md) | Requisitos diretos, 225 pacotes Composer e 1.017 instalações npm |
| [API_ROUTES.md](API_ROUTES.md) | 570 rotas únicas HL, métodos, versões, scopes e implementação |
| [WEB_ROUTES.md](WEB_ROUTES.md) | 152 rotas Symfony coletadas em Dev |
| [CLI_COMMANDS.md](CLI_COMMANDS.md) | 113 comandos CLI coletados em Dev |

## Método e limites

A análise utiliza arquivos versionados, DDL, manifestos/lockfiles, introspecção de rotas/comandos e metadados do banco Dev. Os mapas distinguem código disponível de integração habilitada; não foram exportados registros de negócio, credenciais, tokens, chaves ou configurações privadas.

O catálogo SQL cobre o esquema de instalação atual, não uma execução de todas as migrações históricas. O catálogo de relações cobre a declaração central; regras adicionais estão em classes e módulos. As rotas HL incluem declarações de versões diferentes e não garantem acesso de um cliente específico. As rotas web de Dev incluem recursos que não existem em Prod.

Os arquivos e dependências têm inventários completos; a explicação de comportamento é estrutural. Esta documentação não corresponde a uma auditoria linha a linha, a um pentest, a um grafo completo de chamadas ou à validação funcional de todos os endpoints.

## Atualização dos inventários

A extração deve ser feita em Dev. O script PHP abaixo apenas lê estruturas da aplicação, embora o bootstrap possa aquecer caches locais. Não requer habilitar a API pública.

```bash
cd /home/toor/glpi
sudo docker compose exec -T app php < docs/tools/export_runtime.php > /tmp/glpi-runtime.json
sudo docker compose exec -T app php bin/console list --format=json > /tmp/glpi-commands.json
```

Após revisar os JSONs, atualizar `inventory/runtime.json` e `inventory/commands.json`. O snapshot de comandos versionado contém somente nome/aliases/descrição, sem parâmetros de conexão ou valores de configuração. O de runtime contém somente versão, rotas e relações declaradas. Regenerar os catálogos com:

```bash
python3 docs/tools/update_snapshots.py /tmp/glpi-runtime.json /tmp/glpi-commands.json
python3 docs/tools/generate_inventory.py
python3 docs/tools/validate_docs.py
```

O gerador percorre apenas arquivos do índice Git e os manifestos conhecidos. Documentos explicativos e números do README devem ser revisados quando o código mudar. Manter o snapshot consistente com o commit realmente analisado; não trocar apenas a versão no texto.

## Fluxo de desenvolvimento

Este diretório também segue [AGENTS.md](../AGENTS.md) e [FLUXO-DESENVOLVIMENTO.md](../FLUXO-DESENVOLVIMENTO.md): validar em Dev, commit/push em `dev`, implantar o mesmo commit em Prod, validar e só então promover para `main`. Documentação não é publicada no document root; fica no repositório e na imagem como material técnico.
