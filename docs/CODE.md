# Mapa do código

## Estrutura da raiz

| Caminho | Papel e ponto de atenção |
| --- | --- |
| [src/](../src/) | Objetos PHP legados, modelos de negócio e módulos namespaced |
| [src/Glpi/](../src/Glpi/) | Kernel, controllers, console, APIs, serviços e módulos atuais |
| [src/Twig/](../src/Twig/) | Extensões e componentes Twig |
| [src/autoload/](../src/autoload/) | Constantes, configuração-base, funções e autoload legado |
| [front/](../front/) | Páginas/handlers históricos, incluindo login, cron e CSS dinâmico |
| [ajax/](../ajax/) | Handlers usados pela interface; não equivalem à API pública |
| [inc/](../inc/) | Bootstrap compatível e mapa explícito de relações |
| [public/](../public/) | Document root e recursos públicos; builds ignorados são gerados aqui |
| [templates/](../templates/) | Views Twig, layouts, componentes e páginas por domínio |
| [js/](../js/), [css/](../css/) | Interface, módulos JavaScript, Vue e estilos |
| [lib/](../lib/) | Bibliotecas/bundles e recursos versionados para a interface |
| [resources/](../resources/) | Recursos auxiliares, dados e arquivos de suporte |
| [locales/](../locales/), [.tx/](../.tx/) | Catálogos de tradução e configuração de tradução |
| [dependency_injection/](../dependency_injection/), [routes/](../routes/) | Serviços e rotas específicas por ambiente |
| [install/](../install/) | Instalador, dados iniciais, DDL e migrações |
| [config/](../config/) | Configuração gerada/local, chaves; conteúdo operacional ignorado |
| [files/](../files/) | Cache, logs, sessões, documentos e arquivos transitórios |
| [plugins/](../plugins/), [marketplace/](../marketplace/) | Extensões instaladas; diretórios vazios no checkout base |
| [tests/](../tests/), [tools/](../tools/), [stubs/](../stubs/) | Testes, ferramentas e suporte à análise/desenvolvimento |
| [bin/](../bin/) | Entrada CLI |
| [.github/](../.github/) | CI, automações e auxiliares de build/teste upstream |
| [.docker/](../.docker/), [.devcontainer/](../.devcontainer/) | Infraestrutura de desenvolvimento |
| [deploy/](../deploy/) | Implantação local de Prod e candidato por commit |
| [version/](../version/) | Marcador de versão usado na integridade e identificação de recursos |

O [CODE_INDEX.md](CODE_INDEX.md) enumera todos os arquivos versionados fora de `docs/`, com primeira declaração PHP quando existente. `vendor/`, `node_modules/`, arquivos gerados, banco e segredos não entram nesse inventário.

## Autoload

[composer.json](../composer.json) registra `Glpi\` → `src/Glpi/`, `Twig\` → `src/Twig/` e o namespace global em `src/`. Também carrega funções/constantes de `src/autoload/`. `autoload-dev` acrescenta `Glpi\Tools\`, `Glpi\Tests\` e funções de teste.

A imagem Prod usa `composer dump-autoload --no-dev` e exclui `tests/` e `tools/`. Remover os diretórios sem reconstruir o autoload gera referências a arquivos/classes inexistentes. Os pacotes dev podem continuar fisicamente no `vendor/` copiado: desativar autoload-dev não equivale a instalar somente dependências de runtime.

## Classes estruturantes

| Origem | Função |
| --- | --- |
| [CommonDBTM](../src/CommonDBTM.php) | Base de objetos persistidos; `add`, `update`, `delete`, permissões, hooks e histórico |
| [CommonDBChild](../src/CommonDBChild.php) | Objetos dependentes de outro objeto |
| [CommonDBRelation](../src/CommonDBRelation.php) | Objetos de associação |
| [CommonITILObject](../src/CommonITILObject.php) | Base de Ticket, Change e Problem; atores, fluxo e objetos ITIL |
| [DBmysql](../src/DBmysql.php), [DBmysqlIterator](../src/DBmysqlIterator.php) | Conexão, consultas e iteração de resultados |
| [Session](../src/Session.php), [Auth](../src/Auth.php) | Contexto de usuário, autenticação e acesso |
| [Profile](../src/Profile.php), [Entity](../src/Entity.php) | Direitos e escopo organizacional |
| [Plugin](../src/Plugin.php) | Descoberta/ciclo de vida de plugins |
| [CronTask](../src/CronTask.php) | Definição e execução de ações automáticas |

## Percursos úteis de investigação

- Ticket: `front/ticket.form.php` e controllers/handlers relacionados → `Ticket` → `CommonITILObject`/`CommonDBTM` → tabelas ITIL; apresentação em templates e módulos JS ITIL.
- Formulário: controllers `src/Glpi/Controller/Form/` → `src/Glpi/Form/` → perguntas, respostas, condições e destinos; UI em templates e módulos de formulário.
- API HL: `ApiController` → `Api\HL\Router` → middleware → controller de domínio → `ResourceAccessor`/objetos; schemas documentados em atributos `Doc`.
- Inventário: `InventoryController`/listener de agentes → `src/Glpi/Inventory/` → regras e objetos de ativos.

Esses percursos indicam as camadas; o handler exato depende da rota, operação e tipo do item. Para alterar um comportamento, seguir o método concreto e seus overrides, não apenas a classe-base.

## Convenções de mudança

Permissões e contexto de entidade devem ser mantidos em todas as entradas. Relacionamentos e efeitos de exclusão podem ser tratados nos modelos e em `inc/relation.constant.php`. Alterações de campos devem contemplar DDL, migração, modelo, busca, API, templates, traduções e testes pertinentes. Consulte [MODULES.md](MODULES.md) para localizar o domínio e [TESTING.md](TESTING.md) para validar.
