# Operação e implantação local

## Topologia

| Serviço | Dev | Prod |
| --- | --- | --- |
| Aplicação | `glpi-app-1`, porta 8080 | `glpi-prod-app-1`, porta 8081 |
| Banco | `glpi-db-1`, volume `glpi_db` | `glpi-prod-db-1`, volume `glpi-prod_db` |
| E-mail de teste | `glpi-mailpit-1`, porta 8025 | não declarado |
| Código | bind do checkout `dev` | imagem por commit |
| Configuração/dados | arquivos locais e volumes Dev | volumes independentes |

O nome de projeto padrão Dev deriva do diretório `glpi`; o Compose Prod fixa `name: glpi-prod`. Redes padrão são separadas por projeto Docker. Bancos se comunicam apenas nas respectivas redes, sem publicação da porta 3306.

## Fluxo obrigatório

A sequência de trabalho está em [AGENTS.md](../AGENTS.md) e [FLUXO-DESENVOLVIMENTO.md](../FLUXO-DESENVOLVIMENTO.md): implementar/testar em Dev → commit/push `dev` → candidato em Prod → validar a mudança → fast-forward/push `main`. O checkout permanece em `dev`.

[deploy/candidate.sh](../deploy/candidate.sh) exige branch `dev`, checkout limpo e HEAD igual a `origin/dev`. Constrói a imagem com label `org.opencontainers.image.revision` e executa Compose Prod com `up -d --wait`. Isso verifica o ciclo de containers/healthchecks declarados, mas não substitui login, critérios funcionais e checagens de banco.

## Comandos de leitura

```bash
cd /home/toor/glpi
sudo docker compose ps
sudo docker compose logs --tail=100 app db
sudo docker compose exec -T app php bin/console system:check_requirements
sudo docker compose exec -T app php bin/console database:check_schema_integrity

sudo docker compose --env-file ~/.config/glpi-arbos/prod.env \
  -f deploy/compose.prod.yaml ps
sudo docker compose --env-file ~/.config/glpi-arbos/prod.env \
  -f deploy/compose.prod.yaml logs --tail=100 app db
```

Logs podem conter dados privados: revisar antes de compartilhar. O catálogo de comandos da aplicação está em [CLI_COMMANDS.md](CLI_COMMANDS.md); não executar comandos só por constarem no inventário.

## Saúde e verificação após deploy

1. Containers ativos; MariaDB passa em `healthcheck.sh --connect --innodb_initialized`.
2. Imagem/label correspondem ao commit publicado em `dev`.
3. Modo Prod, sem profiler/debug na interface.
4. Login e fluxo funcional da mudança passam; CSS/chunks/downloads pertinentes carregam.
5. Requisitos e esquema íntegros; revisar logs relevantes.
6. Persistência e cookies independentes; Dev permanece disponível.
7. Registrar resultado e promover o mesmo commit para `main`.

HTTP 200 de uma página isolada não valida todos os módulos ou integrações. Nem `restart: unless-stopped` substitui monitoramento externo ou backup.

## Persistência, backup e rollback

Preservar banco, documentos, chaves e configuração de Prod. O procedimento de dump está no fluxo de desenvolvimento. Um backup deve ser restaurável, com consistência entre registros e arquivos. Não versionar dumps ou chaves.

A referência da imagem aprovada fica no `prod.env` privado. Para rollback, usar a imagem anterior com os mesmos volumes e avaliar compatibilidade do esquema. Migrações exigem backup prévio e análise de restauração; o comando de deploy não desfaz migrações automaticamente.

`docker compose stop` preserva dados. `down -v` remove volumes e não deve ser usado como rotina de parada. Não usar `prune` indiscriminadamente para limpar imagens de rollback ou volumes de dados.

## Limitações observadas

Os ambientes compartilham host/recursos; isso não é alta disponibilidade. Imagens são locais e usam a base Dev existente. Não há registry de releases, TLS, scheduler dedicado, monitoramento externo ou backup agendado demonstrado pela configuração atual. Os workflows upstream em `.github/` não substituem o procedimento local de promoção de Prod.
