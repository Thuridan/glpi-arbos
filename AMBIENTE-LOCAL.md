# GLPI neste host

Repositório do projeto: https://github.com/Thuridan/glpi-arbos
Upstream: https://github.com/glpi-project/glpi
Branch de trabalho: `main`, baseada na `12.0/bugfixes` do GLPI; commit inicial: `96af3bc`.

## Estrutura

- `src/`: classes PHP e módulos de negócio; `src/Glpi/` contém kernel, controllers, API, console e serviços.
- `front/`, `ajax/`, `inc/`: páginas, endpoints e integração com o código legado.
- `templates/`: templates Twig.
- `js/`, `css/`, `resources/`: interface, componentes Vue e recursos de compilação.
- `public/`: raiz pública do Apache, front controller e recursos gerados.
- `config/`: configuração local e conexão com o banco.
- `files/`: documentos, cache, sessões e logs.
- `install/`: esquema e migrações do banco.
- `plugins/`, `marketplace/`: extensões.
- `bin/console`: instalação, manutenção e administração via CLI.
- `tests/`: testes PHP, JavaScript e Playwright.
- `composer.json` / `composer.lock`: dependências PHP.
- `package.json` / `package-lock.json`: dependências JavaScript e compilação Webpack.
- `.docker/`, `docker-compose.yaml`, `Makefile`: ambiente de desenvolvimento oficial.

## Execução

O código do host é montado em `/var/www/glpi` no container `app`.
A imagem usa PHP 8.4 e Apache. O MariaDB 11.8 persiste em `glpi_db`.
Os serviços iniciam automaticamente com a política `unless-stopped`.

```bash
cd /home/toor/glpi
sudo docker compose up -d app db mailpit
sudo docker compose ps
sudo docker compose logs --tail=100 app db
sudo docker compose stop
```

GLPI: http://192.168.63.128:8080
Mailpit (caixa de e-mails de teste): http://192.168.63.128:8025

Este compose é destinado a desenvolvimento, com credenciais locais definidas pelo upstream.
O banco não publica a porta 3306 no host. Serviços opcionais DBGate, LDAP e Keycloak não foram iniciados.
Não usar `docker compose down -v` se quiser preservar o banco.

## Dependências

```bash
sudo docker compose exec app php bin/console dependencies install
```

O processo instala Composer e npm, gera fontes, compila a interface e os catálogos de tradução.

### Download do HtmlDiff

O download do arquivo ZIP no Codeberg ficou sem resposta. Foi configurada a preferência
local do Composer por Git apenas para esse pacote, mantendo o commit
`b7bc848b01ae6e26a3e4ad4f07cd816e6faa8fe8` do lockfile:

```bash
sudo docker compose exec app composer config --global preferred-install.ssddanbrown/htmldiff source
```

## Acesso e validação

- Administrador inicial: usuário `glpi`, senha `glpi`.
- Autenticação validada com redirecionamento para `/front/central.php`.
- Requisitos obrigatórios aprovados por `system:check_requirements`.
- Esquema aprovado por `database:check_schema_integrity`.
- Interface compilada com `npm run build`; traduções compiladas via console.

Ajustes PHP persistidos no volume `glpi_custom_php_ini`, arquivo `local-runtime.ini`:

```ini
xdebug.mode=off
max_execution_time=180
memory_limit=512M
```

Esses ajustes desativam a instrumentação Xdebug e permitem a primeira compilação
SCSS no host com 2 GB de RAM. Os arquivos CSS gerados ficam em cache.

Validação final: GLPI pelo IP do host, login administrativo, CSS principal,
paletas, CSS de bibliotecas e Mailpit retornaram HTTP 200. A compilação SCSS
passou após desativar Xdebug (CSS principal gerado em aproximadamente 4 segundos).


## Integração GitHub

O remote `origin` aponta para `Thuridan/glpi-arbos` e `upstream` mantém o GLPI oficial.
O histórico original é preservado. O autor dos novos commits neste repositório é
`Thuridan <270490005+Thuridan@users.noreply.github.com>`.

O fetch de `origin` usa HTTPS público e o push usa SSH com uma chave dedicada
no diretório `~/.ssh`, fora do repositório. Essa chave pública precisa estar
cadastrada na conta GitHub. A configuração SSH é restrita a este checkout.

```bash
cd /home/toor/glpi
git remote -v
git switch -c feature/minha-alteracao
# editar e validar as alterações
git add caminho/do/arquivo
git commit -m "Descreve a alteração"
git push -u origin feature/minha-alteracao
```

Abra um pull request da branch de trabalho para `main` em `Thuridan/glpi-arbos`.
Para consultar atualizações do projeto original:

```bash
git fetch upstream
git log --oneline main..upstream/12.0/bugfixes
```

Os arquivos de conexão, chaves do GLPI, sessões, uploads, logs, dependências e
`.env` são ignorados pelas regras existentes. O banco está no volume Docker,
fora do Git. Use caminhos explícitos em `git add` e revise `git diff --cached`
antes de criar commits.
