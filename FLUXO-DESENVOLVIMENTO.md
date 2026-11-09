# Dev → Prod → main

| Ambiente | Código | Endereço | Dados |
| --- | --- | --- | --- |
| Dev | checkout `/home/toor/glpi`, branch `dev` | http://192.168.63.128:8080 | banco `glpi_db` e arquivos locais |
| Prod | imagem `glpi-arbos:<commit-dev>` | http://192.168.63.128:8081 | volumes `glpi-prod_db`, `glpi-prod_config`, `glpi-prod_files` e `glpi-prod_marketplace` |

Os ambientes compartilham este host. O código de Prod está na imagem, sem montagem
do checkout Dev. A aplicação de Prod usa o modo `production`; o runtime PHP é
baseado na imagem local validada em Dev. Este setup usa HTTP na rede local.

## 1. Implementar e validar em Dev

```bash
cd /home/toor/glpi
git switch dev
git pull --ff-only origin dev
sudo docker compose up -d app db mailpit
```

Implementar o pedido e testar seus critérios de aceitação na porta 8080.
Executar os testes e verificações apropriados à alteração. Se mudar dependências
ou recursos da interface, reinstalar/compilar em Dev antes de preparar a imagem.

## 2. Commit em dev após a validação

```bash
git add caminho/dos/arquivos
git diff --cached --check
git commit -m 'Descreve a mudança validada em Dev'
git push origin dev
```

## 3. Candidato em Prod e validação

Antes de alterar o banco Prod, fazer backup fora do repositório. Exemplo:

```bash
mkdir -p ~/.local/state/glpi-arbos/backups
chmod 700 ~/.local/state/glpi-arbos/backups
sudo docker compose --env-file ~/.config/glpi-arbos/prod.env \
  -f deploy/compose.prod.yaml exec -T db \
  sh -c 'exec mariadb-dump -uroot -p"$MARIADB_ROOT_PASSWORD" --single-transaction glpi' \
  > ~/.local/state/glpi-arbos/backups/prod-$(date +%Y%m%d-%H%M%S).sql
```

A imagem atual é registrada em `GLPI_PROD_IMAGE` no arquivo privado
`~/.config/glpi-arbos/prod.env`. Anotar essa imagem para eventual rollback.

```bash
./deploy/candidate.sh
```

O script exige branch `dev`, checkout limpo e commit publicado em `origin/dev`.
Ele empacota o código e as dependências compiladas locais; valide-os em Dev antes.
Os bancos não são copiados nem sincronizados entre ambientes.

Se houver migrações, executá-las de maneira planejada no candidato antes de
validar a funcionalidade. Não executar novamente `database:install` em banco existente.
Validar em Prod a mudança solicitada, login, recursos visuais e os requisitos:

```bash
# Use a imagem candidata indicada pelo script nos comandos Compose:
export GLPI_PROD_IMAGE="glpi-arbos:$(git rev-parse dev)"
sudo --preserve-env=GLPI_PROD_IMAGE docker compose \
  --env-file ~/.config/glpi-arbos/prod.env -f deploy/compose.prod.yaml \
  exec -T app php bin/console system:check_requirements
sudo --preserve-env=GLPI_PROD_IMAGE docker compose \
  --env-file ~/.config/glpi-arbos/prod.env -f deploy/compose.prod.yaml \
  exec -T app php bin/console database:check_schema_integrity
```

Falha na validação: manter `main` inalterada, corrigir em Dev e repetir o ciclo.
Para rollback, subir a imagem anterior com os mesmos volumes. Se houve migração,
avaliar também a restauração do banco; trocar a imagem não desfaz migrações.

## 4. Promover para main somente após validar Prod

Registrar os resultados da validação. Publicar em `main` exatamente o commit
que está rodando em Prod, sem criar outro commit de conteúdo após os testes:

```bash
validated_commit=$(git rev-parse dev)
git fetch origin main dev
test "$validated_commit" = "$(git rev-parse origin/dev)"
git merge-base --is-ancestor origin/main "$validated_commit"
git push origin "$validated_commit:refs/heads/main"
git branch -f main "$validated_commit"
```

O push normal rejeita sobrescritas de histórico. O checkout permanece em `dev`.
Atualizar `GLPI_PROD_IMAGE` no arquivo privado para a imagem aprovada. Essa etapa
registra a versão em `main` após a validação de Prod, como definido para o projeto.

## Configuração privada e operação

O arquivo `~/.config/glpi-arbos/prod.env` tem permissão 600 e contém
`GLPI_PROD_IMAGE`, `GLPI_PROD_DB_PASSWORD` e `GLPI_PROD_DB_ROOT_PASSWORD`.
Nunca versionar esse arquivo. O banco não publica a porta 3306 no host.
Não usar `docker compose down -v` para parar ambientes com dados a preservar.
