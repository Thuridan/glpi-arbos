# Interface e recursos estáticos

## Organização

A interface combina HTML renderizado no servidor por Twig, JavaScript legado e componentes Vue. Não há separação geral em uma SPA independente. O [app Vue](../js/src/vue/app.js) registra/inicializa a parte Vue; módulos da interface também vivem em [js/modules/](../js/modules/).

| Área | Conteúdo |
| --- | --- |
| `templates/` | Layouts, formulários, tabelas, páginas por domínio e componentes |
| `src/Twig/` | Integração PHP/Twig e componentes server-side |
| `js/modules/Form/`, `js/modules/Forms/` | Interações de formulários; são diretórios distintos |
| `js/modules/ITIL/`, `Helpdesk/`, `Search/` | Atendimento, experiência do usuário e busca |
| `js/modules/Dashboard/`, `Security/` | Painéis e funções de segurança da UI |
| `js/modules/TipTap/`, `js/RichText/` | Edição de conteúdo rico |
| `js/src/vue/` | Aplicação e componentes Vue |
| `css/`, `lib/bundles/` | Estilos do núcleo e composição de bibliotecas |
| `public/pics/`, `public/sound/` | Imagens e sons públicos versionados |
| `locales/` | Catálogos de tradução |

## Compilação

- [.webpack.config.js](../.webpack.config.js): descobre bundles e constrói/copía bibliotecas para `public/lib/`.
- [.vue.webpack.config.js](../.vue.webpack.config.js): entrada `js/src/vue/app.js`, saída `public/build/vue/app.js` e chunks.
- [package.json](../package.json): `build` encadeia `build:pack`, `build:vue` e geração de traduções de ilustrações.
- CSS de aplicação pode ser gerado em tempo de execução por [front/css.php](../front/css.php), com cache em `public/css_compiled/` conforme a configuração.
- Traduções são compiladas por `tools:locales:compile` no Dev.

```bash
sudo docker compose exec app npm run build
sudo docker compose exec app php bin/console tools:locales:compile
```

O servidor de desenvolvimento Vue pode usar a porta 9637, publicada no Compose Dev. A porta 8090 está reservada ao servidor E2E; publicação de uma porta não demonstra que um processo está escutando nela.

## Validação visual e funcional

Validar a página afetada, interações JavaScript, requisições AJAX/API, estados de loading/erro, permissões e traduções. Usar testes Vitest para lógica/componentes e Playwright para os fluxos adequados. Para documentação ou alteração sem frontend, basta o smoke test pertinente, sem recompilar toda a interface desnecessariamente.

No host, Xdebug foi desabilitado e o tempo/memória PHP ajustados para permitir o CSS inicial. Em Prod, o primeiro acesso pode aquecer caches próprios. Um HTTP 200 do HTML não comprova que CSS, fontes, chunks e ações JavaScript carregaram.

## Segurança do conteúdo

Textos ricos, HTML e arquivos enviados cruzam a fronteira de confiança. Preservar escaping/sanitização, políticas de upload, controle de acesso e proteção de requests. Não usar um handler AJAX para contornar os direitos implementados no domínio. Detalhes em [SECURITY.md](SECURITY.md).
