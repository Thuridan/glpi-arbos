# Fluxo obrigatório de desenvolvimento do GLPI Arbos

- Este checkout e a porta 8080 são o ambiente Dev. Trabalhar na branch `dev`.
- Implementar e validar alterações em Dev antes de criar commits.
- Após a validação em Dev, criar o commit em `dev` e publicar em `origin/dev`.
- Implantar em Prod (porta 8081) a imagem do commit exato publicado em `dev`, usando `deploy/candidate.sh`.
- Validar a mudança em Prod, incluindo os critérios funcionais do pedido, além das verificações técnicas.
- Somente após a validação em Prod, promover esse mesmo commit para `main` por fast-forward e publicar `origin/main`.
- Não editar código em Prod, não implementar diretamente em `main`, não promover mudanças sem validação, não usar force push.
- Manter bancos, configurações, chaves, uploads, sessões e caches independentes entre Dev e Prod.
- Antes de migrations em Prod, fazer backup e avaliar a compatibilidade do rollback. Reverter uma imagem não reverte o banco.
- Nunca versionar credenciais, dados dos ambientes ou backups.
- Ao concluir, registrar o commit, os testes realizados e o resultado de cada ambiente.

Consulte `FLUXO-DESENVOLVIMENTO.md` para os comandos de operação.
