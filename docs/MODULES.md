# Módulos e domínios funcionais

## Domínios de negócio

| Domínio | Entradas/modelos de referência | Dados/efeitos principais |
| --- | --- | --- |
| Atendimento ITIL | `Ticket`, `Change`, `Problem`, `CommonITILObject`, módulos `ITIL`/`Helpdesk` | Atores, tarefas, acompanhamento, solução, validação, SLAs/OLAs e histórico |
| Patrimônio e inventário | `Computer`, `Monitor`, `Printer`, `NetworkEquipment`, `Glpi/Inventory`, `Glpi/Asset` | Inventário, componentes, estado, localização e vínculos de ativos |
| Software/licenças | `Software`, `SoftwareVersion`, `SoftwareLicense` | Instalações, versões e licenciamento de software |
| Identidade e organização | `User`, `Group`, `Profile`, `Entity`, `Auth`, `AuthLDAP` | Autenticação, direitos, grupos e escopo organizacional |
| Documentos | `Document`, `Document_Item` | Metadados no banco, arquivos e ligações polimórficas |
| Base de conhecimento | `KnowbaseItem`, `Glpi/Knowbase` | Artigos, traduções, permissões e revisões |
| Formulários e catálogo | `Glpi/Form`, controllers `Form` e `ServiceCatalog` | Perguntas, seções, condições, respostas e destinos |
| Projetos e planejamento | `Project`, `ProjectTask`, `Planning`, calendário/CalDAV | Tarefas, atores, calendário e relações ITIL |
| Financeiro e contratos | `Infocom`, `Budget`, `Contract`, `Supplier`, `Contact` | Dados financeiros, contratos e fornecedores |
| Datacenter e rede | `Datacenter`, `DCRoom`, `Rack`, `NetworkPort`, `Cable` | Espaços físicos, racks, portas e conectividade |
| Regras | `Rule`, coleções e subclasses por domínio | Critérios e ações sobre importação, atribuição e dados |
| Notificações | `Notification`, templates e alvos de notificação | Eventos, conteúdo, destinatários, fila e envio |
| Automação | `CronTask`, console, `MailCollector` | Execução periódica, coleta e processamento |
| Extensões | `Plugin`, `Glpi/Plugin`, `Glpi/Marketplace` | Hooks e ciclo de vida de plugins |

Os exemplos acima localizam domínios; o inventário de arquivos e declarações está em [CODE_INDEX.md](CODE_INDEX.md). Uma funcionalidade atravessa vários módulos e não corresponde necessariamente a um único namespace.

## Todos os diretórios imediatos de src/Glpi

| Diretório | Arquivos PHP recursivos | Responsabilidade |
| --- | --- | --- |
| [Agent](../src/Glpi/Agent/) | 2 | Cadastro e suporte a agentes e canais de inventário. |
| [Altcha](../src/Glpi/Altcha/) | 3 | Desafios de verificação para proteção de formulários. |
| [Api](../src/Glpi/Api/) | 88 | API legada e HL, contratos, schemas, roteamento e middleware. |
| [Application](../src/Glpi/Application/) | 21 | Ambiente, bootstrap/configuração, recursos e renderização. |
| [Asset](../src/Glpi/Asset/) | 59 | Definições de ativos customizáveis, capacidades e campos. |
| [Cache](../src/Glpi/Cache/) | 3 | Gestão e implementações de cache. |
| [CalDAV](../src/Glpi/CalDAV/) | 13 | Backend, nós e contratos de calendários DAV. |
| [Config](../src/Glpi/Config/) | 4 | Integração e estruturas de configuração. |
| [Console](../src/Glpi/Console/) | 77 | Comandos de instalação, manutenção, migração e administração. |
| [ContentTemplates](../src/Glpi/ContentTemplates/) | 30 | Templates e contexto de conteúdo dinâmico. |
| [Controller](../src/Glpi/Controller/) | 124 | Entradas HTTP Symfony e adaptação para serviços/domínio. |
| [Csv](../src/Glpi/Csv/) | 8 | Suporte a representação e manipulação CSV. |
| [CustomObject](../src/Glpi/CustomObject/) | 3 | Definições/managers de objetos configuráveis. |
| [DBAL](../src/Glpi/DBAL/) | 21 | Expressões, operadores e partes da composição SQL. |
| [Dashboard](../src/Glpi/Dashboard/) | 27 | Estruturas e suporte a painéis. |
| [Debug](../src/Glpi/Debug/) | 3 | Suporte de depuração/desenvolvimento. |
| [DependencyInjection](../src/Glpi/DependencyInjection/) | 3 | Contratos e passes do container. |
| [Dropdown](../src/Glpi/Dropdown/) | 3 | Comportamentos e estruturas de listas de domínio. |
| [Error](../src/Glpi/Error/) | 8 | Erros de startup, captura, tratamento e apresentação. |
| [Exception](../src/Glpi/Exception/) | 18 | Exceções compartilhadas do núcleo. |
| [Features](../src/Glpi/Features/) | 22 | Traits/interfaces de capacidades reutilizáveis. |
| [Form](../src/Glpi/Form/) | 268 | Formulários, perguntas, respostas, condições, permissões e destinos. |
| [FuzzyMatcher](../src/Glpi/FuzzyMatcher/) | 3 | Comparação aproximada usada por funcionalidades do domínio. |
| [Helpdesk](../src/Glpi/Helpdesk/) | 12 | Serviços e estruturas de atendimento ao usuário. |
| [Http](../src/Glpi/Http/) | 8 | Abstrações e respostas HTTP usadas por APIs/serviços. |
| [Inventory](../src/Glpi/Inventory/) | 48 | Recepção, normalização e importação de inventário. |
| [ItemTranslation](../src/Glpi/ItemTranslation/) | 4 | Tradução de itens e conteúdo cadastrado. |
| [Kernel](../src/Glpi/Kernel/) | 38 | Kernel Symfony, eventos e listeners de ciclo HTTP/boot. |
| [Knowbase](../src/Glpi/Knowbase/) | 29 | Base de conhecimento e serviços relacionados. |
| [Locale](../src/Glpi/Locale/) | 2 | Suporte de localização/idiomas. |
| [Log](../src/Glpi/Log/) | 6 | Infraestrutura e representação de logs. |
| [Mail](../src/Glpi/Mail/) | 5 | Suporte e serviços de mensagens de e-mail. |
| [Marketplace](../src/Glpi/Marketplace/) | 4 | Integração com catálogo e gestão de extensões. |
| [Message](../src/Glpi/Message/) | 1 | Mensagens e estruturas de comunicação da aplicação. |
| [Migration](../src/Glpi/Migration/) | 4 | Migrações e auxiliares de transformação de dados. |
| [OAuth](../src/Glpi/OAuth/) | 13 | Servidor OAuth e repositories de clientes/tokens/scopes. |
| [Plugin](../src/Glpi/Plugin/) | 2 | Definições e execução de hooks. |
| [Progress](../src/Glpi/Progress/) | 4 | Armazenamento/indicação de progresso de processos. |
| [RichText](../src/Glpi/RichText/) | 3 | Processamento de conteúdo rico. |
| [Routing](../src/Glpi/Routing/) | 3 | Atributos e convenções de roteamento, inclusive itemtypes. |
| [Rules](../src/Glpi/Rules/) | 1 | Infraestrutura complementar de regras. |
| [Search](../src/Glpi/Search/) | 22 | Busca, critérios e renderização relacionada. |
| [Security](../src/Glpi/Security/) | 17 | Permissões, reautenticação, TOTP e sessões. |
| [Session](../src/Glpi/Session/) | 1 | Estruturas e suporte de sessão. |
| [Stat](../src/Glpi/Stat/) | 16 | Estatísticas. |
| [System](../src/Glpi/System/) | 33 | Serviços e integração de sistema. |
| [Team](../src/Glpi/Team/) | 1 | Estruturas de equipes e participantes. |
| [Toolbox](../src/Glpi/Toolbox/) | 18 | Utilitários namespaced. |
| [UI](../src/Glpi/UI/) | 3 | Componentes, ilustrações e serviços de interface. |

## Como rastrear uma alteração

1. Identificar a página, rota API ou comando que produz o comportamento.
2. Localizar controller/handler e modelo concreto, incluindo herança, traits e hooks.
3. Conferir autorização, entidades, consultas, relações e efeitos de escrita.
4. Localizar templates/módulos JS, traduções e recursos relacionados.
5. Consultar testes/fixtures do domínio e validar o comportamento em Dev.
6. Se houver alteração de dados, planejar migração e rollback antes de Prod.

Essa sequência evita tratar apenas a tela quando a mesma regra também atende API, console, e-mail ou inventário.
