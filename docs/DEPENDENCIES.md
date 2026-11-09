# Dependências, ferramentas e build

## Versões e arquivos de autoridade

| Item | Requisito ou configuração observada |
| --- | --- |
| GLPI | `12.0.2-dev` em `src/autoload/constants.php` |
| PHP | Composer exige `>=8.3`; front controller aceita 8.3 a 8.5; Docker Dev seleciona 8.4 |
| Node.js | `>=24.11` no `package.json` |
| MariaDB | imagem `mariadb:11.8` nos dois ambientes |
| Composer | usado dentro do runtime Dev; lockfile define versões PHP resolvidas |
| npm | usado no Dev; lockfile define versões e instalações JavaScript resolvidas |

[composer.json](../composer.json) e [package.json](../package.json) declaram restrições. Os lockfiles são a referência das versões resolvidas. O snapshot contém 150 pacotes Composer de runtime, 75 de desenvolvimento e 1.017 instalações npm (incluindo pacotes aninhados).

O inventário completo, com requisitos diretos e todos os pacotes transitivos, está em [DEPENDENCIES_LOCK.md](DEPENDENCIES_LOCK.md). Contagens não incluem extensões PHP como pacotes Composer instaláveis.

## Grupos técnicos principais

| Grupo | Dependências e uso |
| --- | --- |
| Plataforma HTTP | Symfony HttpKernel, HttpFoundation, Routing, FrameworkBundle e DependencyInjection |
| Templates | Twig, TwigBundle, UX TwigComponent, extras Markdown/string |
| Log/cache | Monolog, PSR e Symfony Cache |
| APIs | League OAuth2 Server/Client, GraphQL PHP, PSR-7 |
| Identidade | phpCAS, clientes OAuth Google/Azure, biblioteca TOTP |
| Conteúdo | CommonMark, HTML-to-Markdown, HtmlDiff, HTML2Text |
| Documentos | PhpSpreadsheet, TCPDF, fontes PDF, barcode/QR |
| Calendário | Sabre DAV/VObject, recorrência RRULE |
| Interface | Vue, jQuery, Tabler, TipTap, FullCalendar, ECharts, Select2 e Monaco |
| Build JS/CSS | Webpack, loaders de Vue/CSS/SCSS, Sass e plugins de cópia |
| Teste/análise | PHPUnit, ParaTest, PHPStan, Psalm, Rector, linters, Vitest e Playwright |

`composer.json` fornece fallbacks/replace para extensões e polyfills específicos; a presença de `provide` não significa que todas as extensões nativas estejam carregadas. Confirmar runtime com o comando de requisitos.

## Extensões PHP

Os requisitos completos estão no inventário: mysqli, mbstring, intl, gd, curl, bcmath, XML/DOM, fileinfo, session, openssl, zlib e demais extensões declaradas. LDAP, exif, posix, sodium nativo e Redis aparecem como sugestões conforme o uso. No host atual não há serviço Redis configurado, embora o código suporte essa opção de cache.

## Preparação de dependências em Dev

```bash
sudo docker compose exec app php bin/console dependencies install
```

[bin/console](../bin/console) trata esse comando antes do bootstrap completo: instala Composer, gera fontes TCPDF, instala npm, compila bibliotecas/Vue/ilustrações e compila traduções. Composer aplica patches versionados em `tools/patches/` e grava `.composer.hash`. npm possui hooks de patches e marcador `.package.hash`; não presumir que executar somente `npm ci` equivale a todo o fluxo acima.

O incidente local de download do HtmlDiff foi contornado com preferência Composer por Git apenas para esse pacote, preservando o commit do lockfile. Veja [AMBIENTE-LOCAL.md](../AMBIENTE-LOCAL.md).

## Artefatos e Prod

`vendor/`, `node_modules/`, recursos gerados em `public/`, catálogos `.mo` e marcadores de hash ficam fora do versionamento quando previsto pelo `.gitignore`. A imagem Prod copia o `vendor/` e recursos já preparados/validados em Dev, exclui testes/ferramentas/dados e regenera autoload sem desenvolvimento.

O [candidate.sh](../deploy/candidate.sh) não instala ou recompila dependências. Portanto, a identidade do commit fixa o código versionado, mas não prova sozinha a procedência/reprodutibilidade de artefatos ignorados. O pipeline atual depende da validação desses artefatos em Dev e da identificação da imagem implantada.

## Licenciamento e auditoria

O núcleo declara GPL-3.0-or-later. Licenças declaradas pelos pacotes aparecem no catálogo, mas não equivalem a uma revisão jurídica. As políticas de audit/block de Composer e os avisos de npm devem ser avaliados separadamente. Este mapeamento não atualizou versões, não executou `audit fix` e não certifica ausência de vulnerabilidades.
