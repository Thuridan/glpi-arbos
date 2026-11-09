# Testes, qualidade e validação

## Camadas disponíveis

| Camada | Local/configuração | Uso |
| --- | --- | --- |
| PHP unitário/funcional | `tests/functional/`, `phpunit.xml.dist` | Objetos, regras, serviços e persistência |
| Paralelização PHP | ParaTest, alvos no Makefile | Suítes PHP com bancos de teste adequados |
| Web/API | `tests/web/` | Contratos web e API no contexto de teste |
| JavaScript | `tests/js/`, `vitest.config.ts` | Lógica/componentes com Vitest e jsdom |
| E2E | `tests/e2e/`, `playwright.config.ts`, `playwright.isolated.config.ts` | Fluxos reais de navegador |
| Integração LDAP/IMAP | `tests/LDAP/`, `tests/imap/` | Servidores/fixtures específicos |
| Lint/análise | PHPStan, Psalm, Rector, PHP-CS-Fixer, TwigCS, ESLint, Stylelint, TypeScript | Contratos estáticos e convenções |
| Instalação/migração | `.github/actions/test_install.sh`, scripts de update | Instalar/atualizar esquemas de versões distintas |

Embora a suíte PHPUnit seja nomeada `Unit` no XML, inclui `tests/functional/`; não presumir que seja independente de banco. [tests/README.md](../tests/README.md) explica a preparação do ambiente.

## Bancos de teste

Testes utilizam ambiente `testing` e configuração em `tests/config/`. E2E possui ambiente próprio. Os alvos do Makefile incluem instalação de bancos de teste; não foram executados sobre Dev/Prod para produzir este mapeamento.

Nunca apontar esses testes para o banco Prod. Fixtures, instalação com force e clones de bancos podem alterar/apagar dados. Antes de executar, confirmar configuração e endpoints do teste.

## Comandos por escopo

```bash
# Exemplos: executar apenas após preparar o ambiente de testes apropriado.
sudo docker compose exec app php vendor/bin/phpunit tests/functional/ --filter NomeDoTeste
sudo docker compose exec app npm run test:run
sudo docker compose exec app php vendor/bin/phpstan analyse
```

Para E2E, utilizar os alvos `playwright`/`playwright-isolated` do Makefile ou as instruções da suíte. O runner Playwright pode usar uma imagem separada, e o alvo verifica/prepara o contexto do banco E2E. Não apontar a URL dos testes para Prod por conveniência.

## CI

[.github/workflows/ci.yml](../.github/workflows/ci.yml) contém jobs, matrizes PHP e gatilhos de branches/PR/schedule. A matriz e as condições são a autoridade atual; nem todo workflow upstream é adequado ou habilitado neste repositório. Scripts em `.github/actions/` cuidam de containers, fixtures, lint e testes.

## Critérios para cada mudança

- Código de negócio: testar o comportamento solicitado, autorização, entidades e efeitos colaterais.
- Banco: DDL/migração, preservação de dados, integridade e rollback.
- Interface: renderização, interações, assets, traduções e permissões.
- API: contrato, métodos/status, autenticação, scope, filtros e direitos.
- Infraestrutura: build, configuração, isolamento, persistência e disponibilidade dos ambientes.
- Documentação: links, dados extraídos, cobertura dos catálogos, ausência de segredos e coerência com o código.

Executar a suíte inteira não é requisito automático para uma mudança documental. Escolher verificações que possam detectar os erros introduzidos.

## Validação específica deste mapeamento

Os inventários devem cobrir todas as tabelas DDL, todos os arquivos versionados fora de docs, todas as dependências lock e as rotas coletadas por introspecção. Links locais devem resolver; scripts de extração devem passar em sintaxe e reproduzir os resultados.

Após publicar `dev`, o mesmo commit é implantado em Prod e os arquivos da documentação na imagem são comparados aos de Dev, sem expô-los pelo document root. Repetir smoke tests HTTP/recursos e integridade/requisitos pertinentes antes de promover `main`. Os resultados e o commit final são registrados no recibo de validação externo e na conclusão da tarefa.
