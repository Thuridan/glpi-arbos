# Mapa de segurança

Este documento localiza mecanismos existentes e fronteiras de confiança. Não é resultado de pentest nem atestado de segurança de produção.

## Autenticação e sessão

[Auth](../src/Auth.php), [User](../src/User.php), [Session](../src/Session.php) e módulos `src/Glpi/Security/` implementam partes da autenticação, controle de sessão e segurança da conta. Existem integrações com LDAP, CAS, OAuth e mecanismos adicionais; presença de código não significa que estejam habilitados.

[SystemConfigurator](../src/Glpi/Application/SystemConfigurator.php) configura cookies/sessões. O nome do cookie incorpora diretório, host, porta e versão; a validação local confirmou cookies distintos entre 8080 e 8081. Diretórios e dados de sessão continuam separados entre Dev e Prod.

MFA/TOTP e reautenticação estão em [TOTPManager](../src/Glpi/Security/TOTPManager.php), `Security/ReAuth/` e controllers `Security/`. O controle de sessões é tratado em `SessionTracker` e objetos relacionados.

## Direitos e isolamento lógico

Perfis, direitos, grupos e entidades compõem a autorização. `CommonDBTM::can*`, verificações em `Session`, [PermissionManager](../src/Glpi/Security/PermissionManager.php) e atributos em [Security/Attribute](../src/Glpi/Security/Attribute/) são pontos de investigação. Acesso a uma rota não implica permissão de ver todos os objetos.

`entities_id` e recursividade pertencem ao isolamento lógico do GLPI; Dev/Prod são isolamento operacional por containers/volumes. São mecanismos diferentes e ambos devem ser preservados.

## Firewall, CSRF e bridges

O [FirewallStrategyListener](../src/Glpi/Kernel/Listener/ControllerListener/FirewallStrategyListener.php) seleciona a estratégia apropriada para controllers. O [CheckCsrfListener](../src/Glpi/Kernel/Listener/ControllerListener/CheckCsrfListener.php) tem regras para recursos stateless, subrequests e métodos de request.

Nesta versão a proteção inclui verificação de `Sec-Fetch-Site` e fallback para `Origin`/`Host`; não presumir que todo formulário utiliza um hidden token clássico. Quando ambos os headers estão ausentes, esse listener considera a requisição não originada de navegador. Essa descrição não substitui a avaliação completa dos listeners e do contexto de autenticação.

Scripts legados, plugins e entradas API precisam preservar o bootstrap e a estratégia de segurança correspondente. Não expor diretamente o checkout como document root: o ponto público é `public/`.

## Credenciais e chaves

| Local lógico | Função | Regra |
| --- | --- | --- |
| `config/config_db.php` | Conexão com banco | Privado, próprio do ambiente |
| `config/glpicrypt.key` | Criptografia de dados sensíveis | Preservar em backup e separar por ambiente |
| `config/oauth.pem`, `config/oauth.pub` | Material usado pela infraestrutura OAuth | Chave privada não versionada |
| Arquivo externo `prod.env` | Referência da imagem e senhas do banco Prod | Permissão 600, fora do checkout |
| SSH do usuário do host | Autenticação GitHub | Fora do repositório e das imagens |

Nunca copiar valores desses arquivos para documentação, exemplos, logs ou snapshots. Backups do banco podem conter informações pessoais e credenciais cifradas; proteger também chaves e documentos.

## APIs, uploads e conteúdo

HL usa middleware OAuth/IP/scopes e permissões de domínio; a API legada tem sessões e tokens de cliente/usuário próprios. Ver [APIS.md](APIS.md). Downloads/documentos e upload de conteúdo devem ser autorizados no item, não apenas por existência do arquivo.

Bibliotecas de HTTP, HTML, e-mail e templates têm patches do projeto em `tools/patches/`. Não remover esses patches ou alterar escaping, redirecionamentos, URL fetching e renderização sem analisar os testes correspondentes.

## Situação da implantação local

Prod usa o modo `production`, sem barra de debug e com Xdebug/descritivos de erro desativados no PHP. Dev habilita recursos de desenvolvimento. Os bancos não publicam 3306 no host. Os ambientes ainda compartilham o mesmo host e estão acessíveis por HTTP na rede local.

O runtime da imagem Prod deriva da imagem de desenvolvimento e preserva suas ferramentas/pacotes base; isso não equivale a uma imagem mínima endurecida. TLS, política de rede, backup agendado, gestão externa de segredos e proteção de branches no GitHub não são demonstrados pelos arquivos atuais. Este mapeamento não afirma que essas proteções estejam implantadas.
