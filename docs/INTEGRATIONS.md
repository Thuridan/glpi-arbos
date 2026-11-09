# Integrações e automações

## Catálogo

| Integração | Código principal | Dados/fluxo |
| --- | --- | --- |
| Agentes de inventário | `src/Glpi/Inventory/`, `InventoryController`, listener de agentes | Receber inventário, aplicar regras e atualizar ativos |
| LDAP | `AuthLDAP`, comandos `ldap:*` | Autenticação e sincronização conforme configuração |
| CAS | `Auth`, dependência phpCAS, controllers de reautenticação | Autenticação delegada |
| OAuth/OIDC | `src/Glpi/OAuth/`, infraestrutura de autenticação e clientes OAuth | Emissão de tokens HL e integrações de identidade suportadas |
| REST/GraphQL | `src/Glpi/Api/` | Leitura/escrita de objetos por contratos de API |
| CalDAV | `src/Glpi/CalDAV/` | Calendários compatíveis com Sabre DAV |
| Coleta de e-mail | `MailCollector`, `AuthMail`, `src/Glpi/Mail/` | Receber mensagens e aplicar regras/ações de atendimento |
| Notificações | `Notification`, `NotificationTemplate`, objetos/filas relacionados | Renderizar/enfileirar/enviar comunicações |
| Webhooks | objetos de webhook no código e APIs internas | Chamadas externas conforme eventos/configurações |
| Marketplace/plugins | `Plugin`, `src/Glpi/Marketplace/` | Descoberta/instalação/execução de extensões |
| Importação/exportação | módulos e console por domínio | Documentos, dados e formulários com contratos específicos |

As capacidades acima foram identificadas no código; credenciais, disponibilidade de servidores e regras de negócio configuradas não foram exportadas nem ativadas neste trabalho.

## Processos automáticos

[CronTask](../src/CronTask.php), [front/cron.php](../front/cron.php) e [comandos Task](../src/Glpi/Console/Task/) são referências para ações automáticas. Definições e histórico vivem em tabelas `glpi_crontasks` e `glpi_crontasklogs`.

Fluxo típico: tarefa elegível → método do objeto responsável → processamento de itens → registros de execução. Notificações e coleta de mensagens dependem de configuração e agendamento adequados; subir Apache e MariaDB não comprova que todos os jobs estejam agendados externamente.

## Serviços presentes no Compose Dev

Mailpit está ativo nas portas 1025 internas e 8025 públicas. A presença de Mailpit não garante que o SMTP do GLPI esteja apontado para ele; isso exige configuração da aplicação. DBGate e OpenLDAP constam no Compose upstream, mas não são iniciados pelo conjunto local `app db mailpit`. Keycloak é opt-in pelo profile `keycloak`; não está ativo por padrão.

Prod contém somente app e banco no Compose atual. Não possui Mailpit, LDAP, Keycloak, Redis, SMTP externo ou scheduler dedicado declarados como serviços nesse arquivo.

## Contratos e limites operacionais

Antes de conectar uma integração, identificar o ambiente de destino, endpoint, versão, permissões e autenticação. Nunca reutilizar tokens de Prod em Dev. Evitar testes de escrita em Prod antes de validar os efeitos e rollback, incluindo notificações, chamadas externas e filas.

Para agentes de inventário, conferir regras de importação/reconciliação para não duplicar ativos. Para e-mail e webhooks, conferir idempotência, logs, reprocessamento e tratamento de falhas no fluxo específico. O mapeamento não testa disponibilidade externa nem simula eventos de negócio.
