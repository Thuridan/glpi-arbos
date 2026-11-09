# Extensibilidade e plugins

## Pontos de extensão

| Mecanismo | Referência | Finalidade |
| --- | --- | --- |
| Plugins | [Plugin](../src/Plugin.php), [src/Glpi/Plugin/](../src/Glpi/Plugin/) | Descoberta, instalação, ativação e hooks |
| Hooks | [Hooks](../src/Glpi/Plugin/Hooks.php), [HookManager](../src/Glpi/Plugin/HookManager.php) | Pontos de integração de ciclo de vida, UI e processamento |
| Controllers/middleware HL | `Api/HL/Router.php`, hooks de API | Acrescentar contratos externos e tratamento de request/response |
| Modelos persistidos | `CommonDBTM` e subclasses | Validar input, hooks de adição/alteração/exclusão e limpeza |
| Comportamentos por trait/interface | [src/Glpi/Features/](../src/Glpi/Features/) | Capacidades reutilizáveis como inventário, timeline, kanban e árvore |
| Ativos customizáveis | [src/Glpi/Asset/](../src/Glpi/Asset/) | Definições, tipos, modelos, capacidades e campos |
| Objetos customizados | [src/Glpi/CustomObject/](../src/Glpi/CustomObject/) | Definições e managers para objetos configuráveis |
| Formulários | `src/Glpi/Form/QuestionType/`, `Condition/`, `Destination/` | Tipos de pergunta, regras e destinos de resposta |
| Templates/serviços | `src/Twig/`, `dependency_injection/` | Apresentação e integração com container Symfony |

## Ciclo de vida dos objetos

O fluxo `CommonDBTM` possui preparação de input, gravação e callbacks posteriores, além de permissões e histórico. Pontos como `prepareInputForAdd`, `post_addItem` e métodos relacionados a update/delete permitem especializar comportamento. Ler a implementação e assinatura da versão antes de sobrescrever; uma escrita SQL direta pode contornar regras, hooks e trilhas de auditoria.

As relações são parcialmente declaradas em `inc/relation.constant.php`, com tratamentos adicionais nas subclasses. Ao criar um novo relacionamento, avaliar exclusão lógica/purge, associações, entidades e efeitos de limpeza.

## Instalação de plugins nos ambientes

`plugins/` e `marketplace/` são locais de extensão. O checkout base contém apenas marcadores. O estado real de instalação depende também de registros/configuração do banco.

Em Prod, `marketplace/` tem volume próprio; o código empacotado de plugins pode coexistir com estado persistente. Um plugin instalado diretamente pelo runtime não se torna automaticamente parte da branch ou da identidade do commit. Controlar sua versão e migrações pelo mesmo fluxo de validação antes de promovê-lo.

## Customização do núcleo ou plugin

O sistema oferece vários mecanismos de extensão, mas eles não cobrem necessariamente qualquer mudança desejada. Antes de modificar o núcleo, identificar um hook, capacidade ou serviço existente. Se o núcleo for alterado, registrar o impacto no merge futuro do upstream, nas APIs e nas migrações. Este mapa não escolhe uma estratégia de customização sem um requisito funcional concreto.
