# Configuração e ambientes

## Resolução e pontos de configuração

[SystemConfigurator](../src/Glpi/Application/SystemConfigurator.php) reúne configuração do sistema e constantes. [Environment](../src/Glpi/Application/Environment.php) define ambientes e capacidades habilitadas. `GLPI_ENVIRONMENT_TYPE` distingue, entre outros, `development`, `production`, `testing` e `e2e_testing`. O console aceita `--env` para o contexto suportado.

| Arquivo/estrutura | Papel |
| --- | --- |
| `src/autoload/constants.php` | Versões do GLPI, esquema e recursos |
| `src/autoload/CFG_GLPI.php` | Configuração-base e convenções globais |
| `config/config_db.php` | Classe de conexão gerada pelo instalador |
| `config/local_define.php`, `inc/downstream.php` | Pontos de configuração local quando usados |
| `glpi_configs` / `$CFG_GLPI` | Configuração persistida e representação em memória |
| `dependency_injection/*.php` | Definições de container, framework e Twig |
| `routes/<ambiente>.php` | Rotas específicas de ambiente |
| `tests/config/` | Configuração dos ambientes de teste |

Não existe um único `.env` central que substitua toda a configuração GLPI. O `.env` de Compose e o `prod.env` externo pertencem à infraestrutura, enquanto a aplicação mantém configuração própria no banco e em PHP.

## Dev

- Branch ativa: `dev`; bind mount do checkout em `/var/www/glpi`.
- PHP 8.4 no runtime local; `GLPI_ENVIRONMENT_TYPE=development` herdado da imagem base.
- UID/GID configuráveis por `HOST_USER_ID`/`HOST_GROUP_ID`; defaults 1000.
- Customizações PHP persistidas no volume `glpi_custom_php_ini`.
- Banco em `glpi_db`; documentos/cache/sessões/logs em `files/` do checkout.
- Alterações locais em arquivos podem afetar a aplicação imediatamente.

## Prod local

- Imagem `glpi-arbos:<commit-dev>` escolhida antes da promoção em `main`.
- `GLPI_ENVIRONMENT_TYPE=production`, código empacotado; checkout não montado.
- Volumes `glpi-prod_config`, `glpi-prod_files`, `glpi-prod_marketplace` e `glpi-prod_db`.
- Arquivo privado `~/.config/glpi-arbos/prod.env`, permissão 600.
- Variáveis: `GLPI_PROD_IMAGE`, `GLPI_PROD_DB_PASSWORD`, `GLPI_PROD_DB_ROOT_PASSWORD`.
- `GLPI_URI=http://localhost:8081` no Compose; verificar URLs públicas configuradas no GLPI ao mudar host/domínio.

## Diretórios de estado

`GLPI_CONFIG_DIR` aponta por padrão para `config/`; `GLPI_VAR_DIR` para `files/`. Constantes específicas derivam cache, logs, documentos, sessões e temporários desse diretório. O nome físico de um subdiretório não substitui a constante se a instalação foi customizada.

Não compartilhar essas pastas entre Dev e Prod. Ajustes de permissões devem respeitar o usuário do servidor web; executar CLI como root pode produzir arquivos incompatíveis com o runtime.

## Cache e sessão

`src/Glpi/Cache/CacheManager.php` implementa opções de cache, inclusive Redis; suporte de código não equivale a serviço implantado. O kernel usa diretórios de cache com identificação de versão/ambiente. O deploy atual mantém persistência local/volumes; não configura Redis.

Ao alterar código/versão, avaliar caches afetados e usar os comandos suportados. Não limpar sessões, logs ou documentos por confundir esses diretórios com artefatos descartáveis.

## Flags de integração

`enable_api` controla a API legada e `enable_hlapi` a HL. As políticas de login/token da API legada são adicionais. LDAP, SMTP, coleta de mensagens, OAuth e plugins dependem de configuração específica. Este documento mapeia os mecanismos sem expor os valores privados instalados.
