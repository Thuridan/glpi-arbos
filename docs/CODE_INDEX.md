# Inventário completo de arquivos versionados

Gerado do índice Git, excluindo `docs/` para evitar um inventário recursivo. Arquivos ignorados, dependências instaladas, segredos e dados locais não são percorridos.

O símbolo exibido é a primeira declaração de classe/interface/trait/enum encontrada; não é um grafo de chamadas. Arquivos de terceiros versionados em `lib/` fazem parte do catálogo.

| Área | Arquivos |
| --- | --- |
| (raiz) | 43 |
| .devcontainer | 2 |
| .docker | 5 |
| .github | 48 |
| .tx | 1 |
| ajax | 119 |
| bin | 1 |
| config | 1 |
| css | 85 |
| dependency_injection | 5 |
| deploy | 4 |
| files | 14 |
| front | 325 |
| inc | 2 |
| install | 429 |
| js | 134 |
| lib | 25 |
| locales | 70 |
| marketplace | 1 |
| plugins | 1 |
| public | 279 |
| resources | 10 |
| routes | 3 |
| src | 1744 |
| stubs | 4 |
| templates | 524 |
| tests | 1308 |
| tools | 35 |
| version | 1 |

## (raiz)


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [.editorconfig](../.editorconfig) | sem extensão | — |
| [.gettext.config.js](../.gettext.config.js) | .js | — |
| [.gitignore](../.gitignore) | sem extensão | — |
| [.npmrc](../.npmrc) | sem extensão | — |
| [.php-cs-fixer.dist.php](../.php-cs-fixer.dist.php) | .php | — |
| [.phpstan-baseline.missingType.iterableValue.php](../.phpstan-baseline.missingType.iterableValue.php) | .php | — |
| [.phpstan-baseline.php](../.phpstan-baseline.php) | .php | — |
| [.phpstan-baseline.specific.php](../.phpstan-baseline.specific.php) | .php | — |
| [.pr_agent.toml](../.pr_agent.toml) | .toml | — |
| [.stylelintrc.js](../.stylelintrc.js) | .js | — |
| [.vue.webpack.config.js](../.vue.webpack.config.js) | .js | — |
| [.webpack.config.js](../.webpack.config.js) | .js | — |
| [AGENTS.md](../AGENTS.md) | .md | — |
| [AMBIENTE-LOCAL.md](../AMBIENTE-LOCAL.md) | .md | — |
| [CHANGELOG.md](../CHANGELOG.md) | .md | — |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | .md | — |
| [FLUXO-DESENVOLVIMENTO.md](../FLUXO-DESENVOLVIMENTO.md) | .md | — |
| [INSTALL.md](../INSTALL.md) | .md | — |
| [LICENSE](../LICENSE) | sem extensão | — |
| [Makefile](../Makefile) | sem extensão | — |
| [PluginsMakefile.mk](../PluginsMakefile.mk) | .mk | — |
| [PluginsPhpCsFixer.php](../PluginsPhpCsFixer.php) | .php | — |
| [PluginsRector.php](../PluginsRector.php) | .php | — |
| [README.md](../README.md) | .md | — |
| [SECURITY.md](../SECURITY.md) | .md | — |
| [SUPPORT.md](../SUPPORT.md) | .md | — |
| [apirest.md](../apirest.md) | .md | — |
| [composer-dependency-analyser.php](../composer-dependency-analyser.php) | .php | — |
| [composer.json](../composer.json) | .json | — |
| [composer.lock](../composer.lock) | .lock | — |
| [docker-compose.yaml](../docker-compose.yaml) | .yaml | — |
| [eslint.config.mjs](../eslint.config.mjs) | .mjs | — |
| [index.html](../index.html) | .html | — |
| [package-lock.json](../package-lock.json) | .json | — |
| [package.json](../package.json) | .json | — |
| [phpstan.neon.dist](../phpstan.neon.dist) | .dist | — |
| [phpunit.xml.dist](../phpunit.xml.dist) | .dist | — |
| [playwright.config.ts](../playwright.config.ts) | .ts | — |
| [playwright.isolated.config.ts](../playwright.isolated.config.ts) | .ts | — |
| [psalm.xml](../psalm.xml) | .xml | — |
| [rector.php](../rector.php) | .php | — |
| [tsconfig.json](../tsconfig.json) | .json | — |
| [vitest.config.ts](../vitest.config.ts) | .ts | — |

## .devcontainer


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [.devcontainer/README.md](../.devcontainer/README.md) | .md | — |
| [.devcontainer/devcontainer.json](../.devcontainer/devcontainer.json) | .json | — |

## .docker


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [.docker/README.md](../.docker/README.md) | .md | — |
| [.docker/app/Dockerfile](../.docker/app/Dockerfile) | sem extensão | — |
| [.docker/initdb.sql](../.docker/initdb.sql) | .sql | — |
| [.docker/keycloak/README.md](../.docker/keycloak/README.md) | .md | — |
| [.docker/keycloak/realm-glpi.json](../.docker/keycloak/realm-glpi.json) | .json | — |

## .github


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [.github/FUNDING.yml](../.github/FUNDING.yml) | .yml | — |
| [.github/ISSUE_TEMPLATE/bug_report.yml](../.github/ISSUE_TEMPLATE/bug_report.yml) | .yml | — |
| [.github/ISSUE_TEMPLATE/config.yml](../.github/ISSUE_TEMPLATE/config.yml) | .yml | — |
| [.github/ISSUE_TEMPLATE/contributing.yml](../.github/ISSUE_TEMPLATE/contributing.yml) | .yml | — |
| [.github/actions/docker-compose-app.yml](../.github/actions/docker-compose-app.yml) | .yml | — |
| [.github/actions/docker-compose-services.yml](../.github/actions/docker-compose-services.yml) | .yml | — |
| [.github/actions/e2e_install.sh](../.github/actions/e2e_install.sh) | .sh | — |
| [.github/actions/init_build.sh](../.github/actions/init_build.sh) | .sh | — |
| [.github/actions/init_clone-databases.sh](../.github/actions/init_clone-databases.sh) | .sh | — |
| [.github/actions/init_containers-start.sh](../.github/actions/init_containers-start.sh) | .sh | — |
| [.github/actions/init_containers-wait.sh](../.github/actions/init_containers-wait.sh) | .sh | — |
| [.github/actions/init_initialize-0.85.5-db.sh](../.github/actions/init_initialize-0.85.5-db.sh) | .sh | — |
| [.github/actions/init_initialize-9.5-db.sh](../.github/actions/init_initialize-9.5-db.sh) | .sh | — |
| [.github/actions/init_initialize-imap-fixtures.sh](../.github/actions/init_initialize-imap-fixtures.sh) | .sh | — |
| [.github/actions/init_initialize-ldap-fixtures.sh](../.github/actions/init_initialize-ldap-fixtures.sh) | .sh | — |
| [.github/actions/init_show-versions.sh](../.github/actions/init_show-versions.sh) | .sh | — |
| [.github/actions/lint_js-lint.sh](../.github/actions/lint_js-lint.sh) | .sh | — |
| [.github/actions/lint_misc-lint.sh](../.github/actions/lint_misc-lint.sh) | .sh | — |
| [.github/actions/lint_php-lint.sh](../.github/actions/lint_php-lint.sh) | .sh | — |
| [.github/actions/lint_scss-lint.sh](../.github/actions/lint_scss-lint.sh) | .sh | — |
| [.github/actions/lint_twig-lint.sh](../.github/actions/lint_twig-lint.sh) | .sh | — |
| [.github/actions/test_install.sh](../.github/actions/test_install.sh) | .sh | — |
| [.github/actions/test_javascript.sh](../.github/actions/test_javascript.sh) | .sh | — |
| [.github/actions/test_tests-cache.sh](../.github/actions/test_tests-cache.sh) | .sh | — |
| [.github/actions/test_tests-functional.sh](../.github/actions/test_tests-functional.sh) | .sh | — |
| [.github/actions/test_tests-imap.sh](../.github/actions/test_tests-imap.sh) | .sh | — |
| [.github/actions/test_tests-ldap.sh](../.github/actions/test_tests-ldap.sh) | .sh | — |
| [.github/actions/test_tests-web.sh](../.github/actions/test_tests-web.sh) | .sh | — |
| [.github/actions/test_update-from-9.5.sh](../.github/actions/test_update-from-9.5.sh) | .sh | — |
| [.github/actions/test_update-from-older-version.sh](../.github/actions/test_update-from-older-version.sh) | .sh | — |
| [.github/copilot-instructions.md](../.github/copilot-instructions.md) | .md | — |
| [.github/dependabot.yml](../.github/dependabot.yml) | .yml | — |
| [.github/instructions/e2e.instructions.md](../.github/instructions/e2e.instructions.md) | .md | — |
| [.github/instructions/php.instructions.md](../.github/instructions/php.instructions.md) | .md | — |
| [.github/label-commenter-config.yml](../.github/label-commenter-config.yml) | .yml | — |
| [.github/pull_request_template.md](../.github/pull_request_template.md) | .md | — |
| [.github/workflows/branch_build.yml](../.github/workflows/branch_build.yml) | .yml | — |
| [.github/workflows/bump_version_after_release.yml](../.github/workflows/bump_version_after_release.yml) | .yml | — |
| [.github/workflows/ci.yml](../.github/workflows/ci.yml) | .yml | — |
| [.github/workflows/commit-authorship.yml](../.github/workflows/commit-authorship.yml) | .yml | — |
| [.github/workflows/docker_rebuild.yml](../.github/workflows/docker_rebuild.yml) | .yml | — |
| [.github/workflows/docker_releases.yml](../.github/workflows/docker_releases.yml) | .yml | — |
| [.github/workflows/label-commenter.yml](../.github/workflows/label-commenter.yml) | .yml | — |
| [.github/workflows/label-external-prs.yml](../.github/workflows/label-external-prs.yml) | .yml | — |
| [.github/workflows/locales-update-source.yml](../.github/workflows/locales-update-source.yml) | .yml | — |
| [.github/workflows/lock_closed.yaml](../.github/workflows/lock_closed.yaml) | .yaml | — |
| [.github/workflows/nightly_build.yml](../.github/workflows/nightly_build.yml) | .yml | — |
| [.github/workflows/security-scan.yml](../.github/workflows/security-scan.yml) | .yml | — |

## .tx


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [.tx/config](../.tx/config) | sem extensão | — |

## ajax


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [ajax/2fa.php](../ajax/2fa.php) | .php | — |
| [ajax/actorinformation.php](../ajax/actorinformation.php) | .php | — |
| [ajax/actors.php](../ajax/actors.php) | .php | — |
| [ajax/agent.php](../ajax/agent.php) | .php | — |
| [ajax/asset/assetdefinition.php](../ajax/asset/assetdefinition.php) | .php | — |
| [ajax/asset/customfield.php](../ajax/asset/customfield.php) | .php | — |
| [ajax/cable.php](../ajax/cable.php) | .php | — |
| [ajax/central.php](../ajax/central.php) | .php | — |
| [ajax/change_item.php](../ajax/change_item.php) | .php | — |
| [ajax/comments.php](../ajax/comments.php) | .php | — |
| [ajax/common.tabs.php](../ajax/common.tabs.php) | .php | — |
| [ajax/commonitilobject_item.php](../ajax/commonitilobject_item.php) | .php | — |
| [ajax/commonitilsatisfaction.php](../ajax/commonitilsatisfaction.php) | .php | — |
| [ajax/criteria_filter.php](../ajax/criteria_filter.php) | .php | — |
| [ajax/dashboard.php](../ajax/dashboard.php) | .php | — |
| [ajax/dcroom_size.php](../ajax/dcroom_size.php) | .php | — |
| [ajax/debug.php](../ajax/debug.php) | .php | — |
| [ajax/displayMessageAfterRedirect.php](../ajax/displayMessageAfterRedirect.php) | .php | — |
| [ajax/displaypreference.php](../ajax/displaypreference.php) | .php | — |
| [ajax/domainrecord_data_form.php](../ajax/domainrecord_data_form.php) | .php | — |
| [ajax/dropdownAllItems.php](../ajax/dropdownAllItems.php) | .php | — |
| [ajax/dropdownConnect.php](../ajax/dropdownConnect.php) | .php | — |
| [ajax/dropdownConnectNetworkPort.php](../ajax/dropdownConnectNetworkPort.php) | .php | — |
| [ajax/dropdownConnectNetworkPortDeviceType.php](../ajax/dropdownConnectNetworkPortDeviceType.php) | .php | — |
| [ajax/dropdownFieldsBlacklist.php](../ajax/dropdownFieldsBlacklist.php) | .php | — |
| [ajax/dropdownInstallVersion.php](../ajax/dropdownInstallVersion.php) | .php | — |
| [ajax/dropdownItilActors.php](../ajax/dropdownItilActors.php) | .php | — |
| [ajax/dropdownLocation.php](../ajax/dropdownLocation.php) | .php | — |
| [ajax/dropdownMassiveAction.php](../ajax/dropdownMassiveAction.php) | .php | — |
| [ajax/dropdownMassiveActionAddActor.php](../ajax/dropdownMassiveActionAddActor.php) | .php | — |
| [ajax/dropdownMassiveActionAddValidator.php](../ajax/dropdownMassiveActionAddValidator.php) | .php | — |
| [ajax/dropdownMassiveActionAuthMethods.php](../ajax/dropdownMassiveActionAuthMethods.php) | .php | — |
| [ajax/dropdownMassiveActionField.php](../ajax/dropdownMassiveActionField.php) | .php | — |
| [ajax/dropdownMassiveActionOs.php](../ajax/dropdownMassiveActionOs.php) | .php | — |
| [ajax/dropdownNotificationEvent.php](../ajax/dropdownNotificationEvent.php) | .php | — |
| [ajax/dropdownNotificationTemplate.php](../ajax/dropdownNotificationTemplate.php) | .php | — |
| [ajax/dropdownProjectTaskTicket.php](../ajax/dropdownProjectTaskTicket.php) | .php | — |
| [ajax/dropdownRubDocument.php](../ajax/dropdownRubDocument.php) | .php | — |
| [ajax/dropdownShowIPNetwork.php](../ajax/dropdownShowIPNetwork.php) | .php | — |
| [ajax/dropdownSoftwareLicense.php](../ajax/dropdownSoftwareLicense.php) | .php | — |
| [ajax/dropdownTicketCategories.php](../ajax/dropdownTicketCategories.php) | .php | — |
| [ajax/dropdownTrackingDeviceType.php](../ajax/dropdownTrackingDeviceType.php) | .php | — |
| [ajax/dropdownUnicityFields.php](../ajax/dropdownUnicityFields.php) | .php | — |
| [ajax/dropdownValidator.php](../ajax/dropdownValidator.php) | .php | — |
| [ajax/dropdownValuesBlacklist.php](../ajax/dropdownValuesBlacklist.php) | .php | — |
| [ajax/entitytreesons.php](../ajax/entitytreesons.php) | .php | — |
| [ajax/fileupload.php](../ajax/fileupload.php) | .php | — |
| [ajax/form/allowListDropdownValue.php](../ajax/form/allowListDropdownValue.php) | .php | — |
| [ajax/fuzzysearch.php](../ajax/fuzzysearch.php) | .php | — |
| [ajax/genericdate.php](../ajax/genericdate.php) | .php | — |
| [ajax/getAbstractRightDropdownValue.php](../ajax/getAbstractRightDropdownValue.php) | .php | — |
| [ajax/getDropdownConnect.php](../ajax/getDropdownConnect.php) | .php | — |
| [ajax/getDropdownFindNum.php](../ajax/getDropdownFindNum.php) | .php | — |
| [ajax/getDropdownMyDevices.php](../ajax/getDropdownMyDevices.php) | .php | — |
| [ajax/getDropdownNumber.php](../ajax/getDropdownNumber.php) | .php | — |
| [ajax/getDropdownUsers.php](../ajax/getDropdownUsers.php) | .php | — |
| [ajax/getDropdownValue.php](../ajax/getDropdownValue.php) | .php | — |
| [ajax/getFileTag.php](../ajax/getFileTag.php) | .php | — |
| [ajax/getKnowbaseItemAnswer.php](../ajax/getKnowbaseItemAnswer.php) | .php | — |
| [ajax/getMapPoint.php](../ajax/getMapPoint.php) | .php | — |
| [ajax/getPlurals.php](../ajax/getPlurals.php) | .php | — |
| [ajax/getProjectTaskTeamDropdownValue.php](../ajax/getProjectTaskTeamDropdownValue.php) | .php | — |
| [ajax/getShareDashboardDropdownValue.php](../ajax/getShareDashboardDropdownValue.php) | .php | — |
| [ajax/getUserPicture.php](../ajax/getUserPicture.php) | .php | — |
| [ajax/get_item_content.php](../ajax/get_item_content.php) | .php | — |
| [ajax/impact.php](../ajax/impact.php) | .php | — |
| [ajax/item_problem.php](../ajax/item_problem.php) | .php | — |
| [ajax/item_ticket.php](../ajax/item_ticket.php) | .php | — |
| [ajax/item_ticketrecurrent.php](../ajax/item_ticketrecurrent.php) | .php | — |
| [ajax/itilfollowup.php](../ajax/itilfollowup.php) | .php | — |
| [ajax/itillayout.php](../ajax/itillayout.php) | .php | — |
| [ajax/itilvalidation.php](../ajax/itilvalidation.php) | .php | — |
| [ajax/kanban.php](../ajax/kanban.php) | .php | — |
| [ajax/kblink.php](../ajax/kblink.php) | .php | — |
| [ajax/logviewer.php](../ajax/logviewer.php) | .php | — |
| [ajax/mailcollector.php](../ajax/mailcollector.php) | .php | — |
| [ajax/map.php](../ajax/map.php) | .php | — |
| [ajax/marketplace.php](../ajax/marketplace.php) | .php | — |
| [ajax/massiveaction.php](../ajax/massiveaction.php) | .php | — |
| [ajax/networkname.php](../ajax/networkname.php) | .php | — |
| [ajax/notificationmailingsettings.php](../ajax/notificationmailingsettings.php) | .php | — |
| [ajax/notifications_ajax.php](../ajax/notifications_ajax.php) | .php | — |
| [ajax/pendingreason.php](../ajax/pendingreason.php) | .php | — |
| [ajax/pin_savedsearches.php](../ajax/pin_savedsearches.php) | .php | — |
| [ajax/planning.php](../ajax/planning.php) | .php | — |
| [ajax/planningend.php](../ajax/planningend.php) | .php | — |
| [ajax/priority.php](../ajax/priority.php) | .php | — |
| [ajax/projecttask.php](../ajax/projecttask.php) | .php | — |
| [ajax/rack.php](../ajax/rack.php) | .php | — |
| [ajax/resaperiod.php](../ajax/resaperiod.php) | .php | — |
| [ajax/reservable_items.php](../ajax/reservable_items.php) | .php | — |
| [ajax/reservations.php](../ajax/reservations.php) | .php | — |
| [ajax/rule.php](../ajax/rule.php) | .php | — |
| [ajax/ruleaction.php](../ajax/ruleaction.php) | .php | — |
| [ajax/ruleactionvalue.php](../ajax/ruleactionvalue.php) | .php | — |
| [ajax/rulecriteria.php](../ajax/rulecriteria.php) | .php | — |
| [ajax/rulecriteriavalue.php](../ajax/rulecriteriavalue.php) | .php | — |
| [ajax/savedsearch.php](../ajax/savedsearch.php) | .php | — |
| [ajax/search.php](../ajax/search.php) | .php | — |
| [ajax/selectUnaffectedOrNewItem_Device.php](../ajax/selectUnaffectedOrNewItem_Device.php) | .php | — |
| [ajax/solution.php](../ajax/solution.php) | .php | — |
| [ajax/stencil.php](../ajax/stencil.php) | .php | — |
| [ajax/subvisibility.php](../ajax/subvisibility.php) | .php | — |
| [ajax/switchdebug.php](../ajax/switchdebug.php) | .php | — |
| [ajax/switchfoldmenu.php](../ajax/switchfoldmenu.php) | .php | — |
| [ajax/task.php](../ajax/task.php) | .php | — |
| [ajax/telemetry.php](../ajax/telemetry.php) | .php | — |
| [ajax/ticketiteminformation.php](../ajax/ticketiteminformation.php) | .php | — |
| [ajax/timeline.php](../ajax/timeline.php) | .php | — |
| [ajax/transfers.php](../ajax/transfers.php) | .php | — |
| [ajax/treebrowse.php](../ajax/treebrowse.php) | .php | — |
| [ajax/uemailUpdate.php](../ajax/uemailUpdate.php) | .php | — |
| [ajax/unlockobject.php](../ajax/unlockobject.php) | .php | — |
| [ajax/updateTranslationFields.php](../ajax/updateTranslationFields.php) | .php | — |
| [ajax/updateTranslationValue.php](../ajax/updateTranslationValue.php) | .php | — |
| [ajax/updatecurrenttab.php](../ajax/updatecurrenttab.php) | .php | — |
| [ajax/viewsubitem.php](../ajax/viewsubitem.php) | .php | — |
| [ajax/visibility.php](../ajax/visibility.php) | .php | — |
| [ajax/webhook.php](../ajax/webhook.php) | .php | — |

## bin


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [bin/console](../bin/console) | sem extensão | — |

## config


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [config/.gitkeep](../config/.gitkeep) | sem extensão | — |

## css


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [css/core_palettes.scss](../css/core_palettes.scss) | .scss | — |
| [css/glpi.scss](../css/glpi.scss) | .scss | — |
| [css/helpdesk_home.scss](../css/helpdesk_home.scss) | .scss | — |
| [css/includes/_base.scss](../css/includes/_base.scss) | .scss | — |
| [css/includes/_highcontrast.scss](../css/includes/_highcontrast.scss) | .scss | — |
| [css/includes/_includes.scss](../css/includes/_includes.scss) | .scss | — |
| [css/includes/_palette_dark.scss](../css/includes/_palette_dark.scss) | .scss | — |
| [css/includes/_tabler_compat.scss](../css/includes/_tabler_compat.scss) | .scss | — |
| [css/includes/components/_asset-form.scss](../css/includes/components/_asset-form.scss) | .scss | — |
| [css/includes/components/_autocomplete.css](../css/includes/components/_autocomplete.css) | .css | — |
| [css/includes/components/_browser_tree.scss](../css/includes/components/_browser_tree.scss) | .scss | — |
| [css/includes/components/_buttons-group.scss](../css/includes/components/_buttons-group.scss) | .scss | — |
| [css/includes/components/_content-editable-inputs.scss](../css/includes/components/_content-editable-inputs.scss) | .scss | — |
| [css/includes/components/_creator_badge.scss](../css/includes/components/_creator_badge.scss) | .scss | — |
| [css/includes/components/_datatable.scss](../css/includes/components/_datatable.scss) | .scss | — |
| [css/includes/components/_debug-toolbar.scss](../css/includes/components/_debug-toolbar.scss) | .scss | — |
| [css/includes/components/_documentation.scss](../css/includes/components/_documentation.scss) | .scss | — |
| [css/includes/components/_file-uploader.scss](../css/includes/components/_file-uploader.scss) | .scss | — |
| [css/includes/components/_fileupload.scss](../css/includes/components/_fileupload.scss) | .scss | — |
| [css/includes/components/_flatpickr.scss](../css/includes/components/_flatpickr.scss) | .scss | — |
| [css/includes/components/_floating-buttons.scss](../css/includes/components/_floating-buttons.scss) | .scss | — |
| [css/includes/components/_fuzzy.scss](../css/includes/components/_fuzzy.scss) | .scss | — |
| [css/includes/components/_global-menu.scss](../css/includes/components/_global-menu.scss) | .scss | — |
| [css/includes/components/_illustration-picker.scss](../css/includes/components/_illustration-picker.scss) | .scss | — |
| [css/includes/components/_kb.scss](../css/includes/components/_kb.scss) | .scss | — |
| [css/includes/components/_log_viewer.scss](../css/includes/components/_log_viewer.scss) | .scss | — |
| [css/includes/components/_mini-tabs.scss](../css/includes/components/_mini-tabs.scss) | .scss | — |
| [css/includes/components/_networkport.scss](../css/includes/components/_networkport.scss) | .scss | — |
| [css/includes/components/_notes.scss](../css/includes/components/_notes.scss) | .scss | — |
| [css/includes/components/_pictures.scss](../css/includes/components/_pictures.scss) | .scss | — |
| [css/includes/components/_process-chart.scss](../css/includes/components/_process-chart.scss) | .scss | — |
| [css/includes/components/_racks.scss](../css/includes/components/_racks.scss) | .scss | — |
| [css/includes/components/_richtext.scss](../css/includes/components/_richtext.scss) | .scss | — |
| [css/includes/components/_rules.scss](../css/includes/components/_rules.scss) | .scss | — |
| [css/includes/components/_saved-searches.scss](../css/includes/components/_saved-searches.scss) | .scss | — |
| [css/includes/components/_scrollbars.scss](../css/includes/components/_scrollbars.scss) | .scss | — |
| [css/includes/components/_search_input.scss](../css/includes/components/_search_input.scss) | .scss | — |
| [css/includes/components/_select2.scss](../css/includes/components/_select2.scss) | .scss | — |
| [css/includes/components/_sortable.scss](../css/includes/components/_sortable.scss) | .scss | — |
| [css/includes/components/_tabs.scss](../css/includes/components/_tabs.scss) | .scss | — |
| [css/includes/components/_text-selection.scss](../css/includes/components/_text-selection.scss) | .scss | — |
| [css/includes/components/_tinymce.scss](../css/includes/components/_tinymce.scss) | .scss | — |
| [css/includes/components/_utils.scss](../css/includes/components/_utils.scss) | .scss | — |
| [css/includes/components/form/_form-destination.scss](../css/includes/components/form/_form-destination.scss) | .scss | — |
| [css/includes/components/form/_form-editor-horizontal-layout.scss](../css/includes/components/form/_form-editor-horizontal-layout.scss) | .scss | — |
| [css/includes/components/form/_form-editor.scss](../css/includes/components/form/_form-editor.scss) | .scss | — |
| [css/includes/components/form/_form-renderer.scss](../css/includes/components/form/_form-renderer.scss) | .scss | — |
| [css/includes/components/form/_helpdesk-home-config-for-empty-entity.scss](../css/includes/components/form/_helpdesk-home-config-for-empty-entity.scss) | .scss | — |
| [css/includes/components/form/_item-translations.scss](../css/includes/components/form/_item-translations.scss) | .scss | — |
| [css/includes/components/itilobject/_actors.scss](../css/includes/components/itilobject/_actors.scss) | .scss | — |
| [css/includes/components/itilobject/_dates_timelines.scss](../css/includes/components/itilobject/_dates_timelines.scss) | .scss | — |
| [css/includes/components/itilobject/_footer.scss](../css/includes/components/itilobject/_footer.scss) | .scss | — |
| [css/includes/components/itilobject/_layout.scss](../css/includes/components/itilobject/_layout.scss) | .scss | — |
| [css/includes/components/itilobject/_status.scss](../css/includes/components/itilobject/_status.scss) | .scss | — |
| [css/includes/components/itilobject/_timeline.scss](../css/includes/components/itilobject/_timeline.scss) | .scss | — |
| [css/includes/components/setup/_dropdowns_list.scss](../css/includes/components/setup/_dropdowns_list.scss) | .scss | — |
| [css/includes/mixins/_badges_fixes.scss](../css/includes/mixins/_badges_fixes.scss) | .scss | — |
| [css/includes/pages/_search.scss](../css/includes/pages/_search.scss) | .scss | — |
| [css/install.scss](../css/install.scss) | .scss | — |
| [css/legacy/includes/_impact.scss](../css/legacy/includes/_impact.scss) | .scss | — |
| [css/legacy/includes/_inputs.scss](../css/legacy/includes/_inputs.scss) | .scss | — |
| [css/legacy/includes/_responsive_fixes.scss](../css/legacy/includes/_responsive_fixes.scss) | .scss | — |
| [css/legacy/includes/_styles.scss](../css/legacy/includes/_styles.scss) | .scss | — |
| [css/palettes/_aerialgreen.scss](../css/palettes/_aerialgreen.scss) | .scss | — |
| [css/palettes/_auror.scss](../css/palettes/_auror.scss) | .scss | — |
| [css/palettes/_auror_dark.scss](../css/palettes/_auror_dark.scss) | .scss | — |
| [css/palettes/_automn.scss](../css/palettes/_automn.scss) | .scss | — |
| [css/palettes/_classic.scss](../css/palettes/_classic.scss) | .scss | — |
| [css/palettes/_clockworkorange.scss](../css/palettes/_clockworkorange.scss) | .scss | — |
| [css/palettes/_dark.scss](../css/palettes/_dark.scss) | .scss | — |
| [css/palettes/_darker.scss](../css/palettes/_darker.scss) | .scss | — |
| [css/palettes/_flood.scss](../css/palettes/_flood.scss) | .scss | — |
| [css/palettes/_greenflat.scss](../css/palettes/_greenflat.scss) | .scss | — |
| [css/palettes/_hipster.scss](../css/palettes/_hipster.scss) | .scss | — |
| [css/palettes/_icecream.scss](../css/palettes/_icecream.scss) | .scss | — |
| [css/palettes/_lightblue.scss](../css/palettes/_lightblue.scss) | .scss | — |
| [css/palettes/_midnight.scss](../css/palettes/_midnight.scss) | .scss | — |
| [css/palettes/_premiumred.scss](../css/palettes/_premiumred.scss) | .scss | — |
| [css/palettes/_purplehaze.scss](../css/palettes/_purplehaze.scss) | .scss | — |
| [css/palettes/_teclib.scss](../css/palettes/_teclib.scss) | .scss | — |
| [css/palettes/_vintage.scss](../css/palettes/_vintage.scss) | .scss | — |
| [css/standalone/chartist.scss](../css/standalone/chartist.scss) | .scss | — |
| [css/standalone/dashboard.scss](../css/standalone/dashboard.scss) | .scss | — |
| [css/standalone/marketplace.scss](../css/standalone/marketplace.scss) | .scss | — |
| [css/standalone/stencil-editor.scss](../css/standalone/stencil-editor.scss) | .scss | — |

## dependency_injection


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [dependency_injection/framework.php](../dependency_injection/framework.php) | .php | — |
| [dependency_injection/services.php](../dependency_injection/services.php) | .php | — |
| [dependency_injection/twig.php](../dependency_injection/twig.php) | .php | — |
| [dependency_injection/twig_component.php](../dependency_injection/twig_component.php) | .php | — |
| [dependency_injection/web_profiler.php](../dependency_injection/web_profiler.php) | .php | — |

## deploy


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [deploy/Dockerfile.prod](../deploy/Dockerfile.prod) | .prod | — |
| [deploy/Dockerfile.prod.dockerignore](../deploy/Dockerfile.prod.dockerignore) | .dockerignore | — |
| [deploy/candidate.sh](../deploy/candidate.sh) | .sh | — |
| [deploy/compose.prod.yaml](../deploy/compose.prod.yaml) | .yaml | — |

## files


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [files/_cache/.gitkeep](../files/_cache/.gitkeep) | sem extensão | — |
| [files/_cron/.gitkeep](../files/_cron/.gitkeep) | sem extensão | — |
| [files/_graphs/.gitkeep](../files/_graphs/.gitkeep) | sem extensão | — |
| [files/_inventories/.gitkeep](../files/_inventories/.gitkeep) | sem extensão | — |
| [files/_locales/.gitkeep](../files/_locales/.gitkeep) | sem extensão | — |
| [files/_lock/.gitkeep](../files/_lock/.gitkeep) | sem extensão | — |
| [files/_log/.gitkeep](../files/_log/.gitkeep) | sem extensão | — |
| [files/_pictures/.gitkeep](../files/_pictures/.gitkeep) | sem extensão | — |
| [files/_plugins/.gitkeep](../files/_plugins/.gitkeep) | sem extensão | — |
| [files/_rss/.gitkeep](../files/_rss/.gitkeep) | sem extensão | — |
| [files/_sessions/.gitkeep](../files/_sessions/.gitkeep) | sem extensão | — |
| [files/_themes/.gitkeep](../files/_themes/.gitkeep) | sem extensão | — |
| [files/_tmp/.gitkeep](../files/_tmp/.gitkeep) | sem extensão | — |
| [files/_uploads/.gitkeep](../files/_uploads/.gitkeep) | sem extensão | — |

## front


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [front/_check_webserver_config.php](../front/_check_webserver_config.php) | .php | — |
| [front/appliance_item.form.php](../front/appliance_item.form.php) | .php | — |
| [front/appliance_item_relation.form.php](../front/appliance_item_relation.form.php) | .php | — |
| [front/asset/asset.form.php](../front/asset/asset.form.php) | .php | — |
| [front/asset/asset_peripheralasset.form.php](../front/asset/asset_peripheralasset.form.php) | .php | — |
| [front/asset/assetdefinition.form.php](../front/asset/assetdefinition.form.php) | .php | — |
| [front/asset/customfielddefinition.form.php](../front/asset/customfielddefinition.form.php) | .php | — |
| [front/asset/ruledictionarymodel.form.php](../front/asset/ruledictionarymodel.form.php) | .php | — |
| [front/asset/ruledictionarymodel.php](../front/asset/ruledictionarymodel.php) | .php | — |
| [front/asset/ruledictionarytype.form.php](../front/asset/ruledictionarytype.form.php) | .php | — |
| [front/asset/ruledictionarytype.php](../front/asset/ruledictionarytype.php) | .php | — |
| [front/auth.others.php](../front/auth.others.php) | .php | — |
| [front/auth.settings.php](../front/auth.settings.php) | .php | — |
| [front/authldap.form.php](../front/authldap.form.php) | .php | — |
| [front/calendar_holiday.form.php](../front/calendar_holiday.form.php) | .php | — |
| [front/calendarsegment.form.php](../front/calendarsegment.form.php) | .php | — |
| [front/cartridge.form.php](../front/cartridge.form.php) | .php | — |
| [front/cartridgeitem_printermodel.form.php](../front/cartridgeitem_printermodel.form.php) | .php | — |
| [front/certificate_item.form.php](../front/certificate_item.form.php) | .php | — |
| [front/change.form.php](../front/change.form.php) | .php | — |
| [front/change_group.form.php](../front/change_group.form.php) | .php | — |
| [front/change_item.form.php](../front/change_item.form.php) | .php | — |
| [front/change_problem.form.php](../front/change_problem.form.php) | .php | — |
| [front/change_supplier.form.php](../front/change_supplier.form.php) | .php | — |
| [front/change_ticket.form.php](../front/change_ticket.form.php) | .php | — |
| [front/change_user.form.php](../front/change_user.form.php) | .php | — |
| [front/changecost.form.php](../front/changecost.form.php) | .php | — |
| [front/changesatisfaction.form.php](../front/changesatisfaction.form.php) | .php | — |
| [front/changetask.form.php](../front/changetask.form.php) | .php | — |
| [front/changetemplatehiddenfield.form.php](../front/changetemplatehiddenfield.form.php) | .php | — |
| [front/changetemplatemandatoryfield.form.php](../front/changetemplatemandatoryfield.form.php) | .php | — |
| [front/changetemplatepredefinedfield.form.php](../front/changetemplatepredefinedfield.form.php) | .php | — |
| [front/changetemplatereadonlyfield.form.php](../front/changetemplatereadonlyfield.form.php) | .php | — |
| [front/changevalidation.form.php](../front/changevalidation.form.php) | .php | — |
| [front/commonitilcost.form.php](../front/commonitilcost.form.php) | .php | — |
| [front/commonitilobject_commonitilobject.form.php](../front/commonitilobject_commonitilobject.form.php) | .php | — |
| [front/commonitilobject_item.form.php](../front/commonitilobject_item.form.php) | .php | — |
| [front/commonitiltask.form.php](../front/commonitiltask.form.php) | .php | — |
| [front/commonitilvalidation.form.php](../front/commonitilvalidation.form.php) | .php | — |
| [front/config.form.php](../front/config.form.php) | .php | — |
| [front/consumable.form.php](../front/consumable.form.php) | .php | — |
| [front/consumableitem.form.php](../front/consumableitem.form.php) | .php | — |
| [front/consumableitem.php](../front/consumableitem.php) | .php | — |
| [front/contact_supplier.form.php](../front/contact_supplier.form.php) | .php | — |
| [front/contenttemplates/documentation.php](../front/contenttemplates/documentation.php) | .php | — |
| [front/contract_item.form.php](../front/contract_item.form.php) | .php | — |
| [front/contract_supplier.form.php](../front/contract_supplier.form.php) | .php | — |
| [front/contractcost.form.php](../front/contractcost.form.php) | .php | — |
| [front/cron.php](../front/cron.php) | .php | — |
| [front/crontask.form.php](../front/crontask.form.php) | .php | — |
| [front/css.php](../front/css.php) | .php | — |
| [front/dashboard_assets.php](../front/dashboard_assets.php) | .php | — |
| [front/dashboard_helpdesk.php](../front/dashboard_helpdesk.php) | .php | — |
| [front/database.form.php](../front/database.form.php) | .php | — |
| [front/databaseinstance.form.php](../front/databaseinstance.form.php) | .php | — |
| [front/datacenter.form.php](../front/datacenter.form.php) | .php | — |
| [front/dcroom.form.php](../front/dcroom.form.php) | .php | — |
| [front/defaultfilter.form.php](../front/defaultfilter.form.php) | .php | — |
| [front/devices.php](../front/devices.php) | .php | — |
| [front/dictionnary.php](../front/dictionnary.php) | .php | — |
| [front/displaypreference.form.php](../front/displaypreference.form.php) | .php | — |
| [front/document.form.php](../front/document.form.php) | .php | — |
| [front/document.send.php](../front/document.send.php) | .php | — |
| [front/document_item.form.php](../front/document_item.form.php) | .php | — |
| [front/documenttype.list.php](../front/documenttype.list.php) | .php | — |
| [front/domain.form.php](../front/domain.form.php) | .php | — |
| [front/domainrecord.form.php](../front/domainrecord.form.php) | .php | — |
| [front/dropdown.common.form.php](../front/dropdown.common.form.php) | .php | — |
| [front/dropdown.common.php](../front/dropdown.common.php) | .php | — |
| [front/dropdown.php](../front/dropdown.php) | .php | — |
| [front/dropdown/dropdowndefinition.form.php](../front/dropdown/dropdowndefinition.form.php) | .php | — |
| [front/dropdowntranslation.form.php](../front/dropdowntranslation.form.php) | .php | — |
| [front/form/access_control.form.php](../front/form/access_control.form.php) | .php | — |
| [front/form/answersset.form.php](../front/form/answersset.form.php) | .php | — |
| [front/form/form.form.php](../front/form/form.form.php) | .php | — |
| [front/graph.send.php](../front/graph.send.php) | .php | — |
| [front/group.form.php](../front/group.form.php) | .php | — |
| [front/group_problem.form.php](../front/group_problem.form.php) | .php | — |
| [front/group_ticket.form.php](../front/group_ticket.form.php) | .php | — |
| [front/group_user.form.php](../front/group_user.form.php) | .php | — |
| [front/helpdesk.faq.php](../front/helpdesk.faq.php) | .php | — |
| [front/impactcsv.php](../front/impactcsv.php) | .php | — |
| [front/impactitem.form.php](../front/impactitem.form.php) | .php | — |
| [front/initpassword.php](../front/initpassword.php) | .php | — |
| [front/ipnetwork_vlan.form.php](../front/ipnetwork_vlan.form.php) | .php | — |
| [front/item_cluster.form.php](../front/item_cluster.form.php) | .php | — |
| [front/item_device.common.form.php](../front/item_device.common.form.php) | .php | — |
| [front/item_device.php](../front/item_device.php) | .php | — |
| [front/item_devicebattery.form.php](../front/item_devicebattery.form.php) | .php | — |
| [front/item_devicecamera.form.php](../front/item_devicecamera.form.php) | .php | — |
| [front/item_devicecase.form.php](../front/item_devicecase.form.php) | .php | — |
| [front/item_devicecontrol.form.php](../front/item_devicecontrol.form.php) | .php | — |
| [front/item_devicedrive.form.php](../front/item_devicedrive.form.php) | .php | — |
| [front/item_devicefirmware.form.php](../front/item_devicefirmware.form.php) | .php | — |
| [front/item_devicegeneric.form.php](../front/item_devicegeneric.form.php) | .php | — |
| [front/item_devicegraphiccard.form.php](../front/item_devicegraphiccard.form.php) | .php | — |
| [front/item_deviceharddrive.form.php](../front/item_deviceharddrive.form.php) | .php | — |
| [front/item_devicememory.form.php](../front/item_devicememory.form.php) | .php | — |
| [front/item_devicemotherboard.form.php](../front/item_devicemotherboard.form.php) | .php | — |
| [front/item_devicenetworkcard.form.php](../front/item_devicenetworkcard.form.php) | .php | — |
| [front/item_devicepci.form.php](../front/item_devicepci.form.php) | .php | — |
| [front/item_devicepowersupply.form.php](../front/item_devicepowersupply.form.php) | .php | — |
| [front/item_deviceprocessor.form.php](../front/item_deviceprocessor.form.php) | .php | — |
| [front/item_devices.form.php](../front/item_devices.form.php) | .php | — |
| [front/item_devicesensor.form.php](../front/item_devicesensor.form.php) | .php | — |
| [front/item_devicesimcard.form.php](../front/item_devicesimcard.form.php) | .php | — |
| [front/item_devicesoundcard.form.php](../front/item_devicesoundcard.form.php) | .php | — |
| [front/item_disk.form.php](../front/item_disk.form.php) | .php | — |
| [front/item_enclosure.form.php](../front/item_enclosure.form.php) | .php | — |
| [front/item_line.form.php](../front/item_line.form.php) | .php | — |
| [front/item_operatingsystem.form.php](../front/item_operatingsystem.form.php) | .php | — |
| [front/item_problem.form.php](../front/item_problem.form.php) | .php | — |
| [front/item_project.form.php](../front/item_project.form.php) | .php | — |
| [front/item_rack.form.php](../front/item_rack.form.php) | .php | — |
| [front/item_remotemanagement.form.php](../front/item_remotemanagement.form.php) | .php | — |
| [front/item_softwarelicense.form.php](../front/item_softwarelicense.form.php) | .php | — |
| [front/item_softwareversion.form.php](../front/item_softwareversion.form.php) | .php | — |
| [front/item_ticket.form.php](../front/item_ticket.form.php) | .php | — |
| [front/item_ticketrecurrent.form.php](../front/item_ticketrecurrent.form.php) | .php | — |
| [front/itemantivirus.form.php](../front/itemantivirus.form.php) | .php | — |
| [front/itemvirtualmachine.form.php](../front/itemvirtualmachine.form.php) | .php | — |
| [front/itil_project.form.php](../front/itil_project.form.php) | .php | — |
| [front/itilfollowup.form.php](../front/itilfollowup.form.php) | .php | — |
| [front/itilsolution.form.php](../front/itilsolution.form.php) | .php | — |
| [front/itiltemplatefield.form.php](../front/itiltemplatefield.form.php) | .php | — |
| [front/knowbaseitem.php](../front/knowbaseitem.php) | .php | — |
| [front/knowbaseitem_item.form.php](../front/knowbaseitem_item.form.php) | .php | — |
| [front/knowbaseitemtranslation.form.php](../front/knowbaseitemtranslation.form.php) | .php | — |
| [front/ldap.group.import.php](../front/ldap.group.import.php) | .php | — |
| [front/ldap.group.php](../front/ldap.group.php) | .php | — |
| [front/ldap.import.php](../front/ldap.import.php) | .php | — |
| [front/ldap.php](../front/ldap.php) | .php | — |
| [front/link.send.php](../front/link.send.php) | .php | — |
| [front/link_itemtype.form.php](../front/link_itemtype.form.php) | .php | — |
| [front/locale.php](../front/locale.php) | .php | — |
| [front/lock.form.php](../front/lock.form.php) | .php | — |
| [front/log/export.php](../front/log/export.php) | .php | — |
| [front/login.php](../front/login.php) | .php | — |
| [front/logout.php](../front/logout.php) | .php | — |
| [front/logs.php](../front/logs.php) | .php | — |
| [front/logviewer.php](../front/logviewer.php) | .php | — |
| [front/lostpassword.php](../front/lostpassword.php) | .php | — |
| [front/manuallink.form.php](../front/manuallink.form.php) | .php | — |
| [front/marketplace.download.php](../front/marketplace.download.php) | .php | — |
| [front/marketplace.php](../front/marketplace.php) | .php | — |
| [front/massiveaction.php](../front/massiveaction.php) | .php | — |
| [front/networkalias.form.php](../front/networkalias.form.php) | .php | — |
| [front/networkequipment.form.php](../front/networkequipment.form.php) | .php | — |
| [front/networkname.form.php](../front/networkname.form.php) | .php | — |
| [front/networkport.form.php](../front/networkport.form.php) | .php | — |
| [front/networkport_vlan.form.php](../front/networkport_vlan.form.php) | .php | — |
| [front/notepad.form.php](../front/notepad.form.php) | .php | — |
| [front/notification.form.php](../front/notification.form.php) | .php | — |
| [front/notification.tags.php](../front/notification.tags.php) | .php | — |
| [front/notification_notificationtemplate.form.php](../front/notification_notificationtemplate.form.php) | .php | — |
| [front/notificationajaxsetting.form.php](../front/notificationajaxsetting.form.php) | .php | — |
| [front/notificationmailingsetting.form.php](../front/notificationmailingsetting.form.php) | .php | — |
| [front/notificationtarget.form.php](../front/notificationtarget.form.php) | .php | — |
| [front/notificationtemplate.form.php](../front/notificationtemplate.form.php) | .php | — |
| [front/notificationtemplatetranslation.form.php](../front/notificationtemplatetranslation.form.php) | .php | — |
| [front/oauthclient.form.php](../front/oauthclient.form.php) | .php | — |
| [front/olalevel.form.php](../front/olalevel.form.php) | .php | — |
| [front/olalevelaction.form.php](../front/olalevelaction.form.php) | .php | — |
| [front/olalevelcriteria.form.php](../front/olalevelcriteria.form.php) | .php | — |
| [front/palette_preview.php](../front/palette_preview.php) | .php | — |
| [front/pdu_rack.form.php](../front/pdu_rack.form.php) | .php | — |
| [front/planning.form.php](../front/planning.form.php) | .php | — |
| [front/planning.php](../front/planning.php) | .php | — |
| [front/planningcsv.php](../front/planningcsv.php) | .php | — |
| [front/planningexternalevent.form.php](../front/planningexternalevent.form.php) | .php | — |
| [front/planningrecall.form.php](../front/planningrecall.form.php) | .php | — |
| [front/plugin.form.php](../front/plugin.form.php) | .php | — |
| [front/plugin.php](../front/plugin.php) | .php | — |
| [front/pluginimage.send.php](../front/pluginimage.send.php) | .php | — |
| [front/preference.php](../front/preference.php) | .php | — |
| [front/printerlogcsv.php](../front/printerlogcsv.php) | .php | — |
| [front/problem.form.php](../front/problem.form.php) | .php | — |
| [front/problem_supplier.form.php](../front/problem_supplier.form.php) | .php | — |
| [front/problem_ticket.form.php](../front/problem_ticket.form.php) | .php | — |
| [front/problem_user.form.php](../front/problem_user.form.php) | .php | — |
| [front/problemcost.form.php](../front/problemcost.form.php) | .php | — |
| [front/problemtask.form.php](../front/problemtask.form.php) | .php | — |
| [front/problemtemplatehiddenfield.form.php](../front/problemtemplatehiddenfield.form.php) | .php | — |
| [front/problemtemplatemandatoryfield.form.php](../front/problemtemplatemandatoryfield.form.php) | .php | — |
| [front/problemtemplatepredefinedfield.form.php](../front/problemtemplatepredefinedfield.form.php) | .php | — |
| [front/problemtemplatereadonlyfield.form.php](../front/problemtemplatereadonlyfield.form.php) | .php | — |
| [front/profile.form.php](../front/profile.form.php) | .php | — |
| [front/profile_user.form.php](../front/profile_user.form.php) | .php | — |
| [front/project.form.php](../front/project.form.php) | .php | — |
| [front/projectcost.form.php](../front/projectcost.form.php) | .php | — |
| [front/projecttask.form.php](../front/projecttask.form.php) | .php | — |
| [front/projecttask_ticket.form.php](../front/projecttask_ticket.form.php) | .php | — |
| [front/projecttaskteam.form.php](../front/projecttaskteam.form.php) | .php | — |
| [front/projectteam.form.php](../front/projectteam.form.php) | .php | — |
| [front/queuednotification.form.php](../front/queuednotification.form.php) | .php | — |
| [front/queuedwebhook.form.php](../front/queuedwebhook.form.php) | .php | — |
| [front/rack.form.php](../front/rack.form.php) | .php | — |
| [front/refusedequipment.form.php](../front/refusedequipment.form.php) | .php | — |
| [front/reminder.form.php](../front/reminder.form.php) | .php | — |
| [front/remindertranslation.form.php](../front/remindertranslation.form.php) | .php | — |
| [front/report.contract.php](../front/report.contract.php) | .php | — |
| [front/report.default.php](../front/report.default.php) | .php | — |
| [front/report.dynamic.php](../front/report.dynamic.php) | .php | — |
| [front/report.infocom.conso.php](../front/report.infocom.conso.php) | .php | — |
| [front/report.infocom.php](../front/report.infocom.php) | .php | — |
| [front/report.networking.php](../front/report.networking.php) | .php | — |
| [front/report.php](../front/report.php) | .php | — |
| [front/report.reservation.php](../front/report.reservation.php) | .php | — |
| [front/report.state.php](../front/report.state.php) | .php | — |
| [front/report.year.php](../front/report.year.php) | .php | — |
| [front/reservation.form.php](../front/reservation.form.php) | .php | — |
| [front/reservation.php](../front/reservation.php) | .php | — |
| [front/reservationitem.form.php](../front/reservationitem.form.php) | .php | — |
| [front/reservationitem.php](../front/reservationitem.php) | .php | — |
| [front/rssfeed.form.php](../front/rssfeed.form.php) | .php | — |
| [front/rule.backup.php](../front/rule.backup.php) | .php | — |
| [front/rule.common.form.php](../front/rule.common.form.php) | .php | — |
| [front/rule.common.php](../front/rule.common.php) | .php | — |
| [front/rule.generic.form.php](../front/rule.generic.form.php) | .php | — |
| [front/rule.php](../front/rule.php) | .php | — |
| [front/rule.test.php](../front/rule.test.php) | .php | — |
| [front/ruleaction.form.php](../front/ruleaction.form.php) | .php | — |
| [front/ruleasset.form.php](../front/ruleasset.form.php) | .php | — |
| [front/ruleasset.php](../front/ruleasset.php) | .php | — |
| [front/rulechange.form.php](../front/rulechange.form.php) | .php | — |
| [front/rulechange.php](../front/rulechange.php) | .php | — |
| [front/rulecriteria.form.php](../front/rulecriteria.form.php) | .php | — |
| [front/ruledefineitemtype.form.php](../front/ruledefineitemtype.form.php) | .php | — |
| [front/ruledefineitemtype.php](../front/ruledefineitemtype.php) | .php | — |
| [front/ruledictionnarycomputermodel.form.php](../front/ruledictionnarycomputermodel.form.php) | .php | — |
| [front/ruledictionnarycomputermodel.php](../front/ruledictionnarycomputermodel.php) | .php | — |
| [front/ruledictionnarycomputertype.form.php](../front/ruledictionnarycomputertype.form.php) | .php | — |
| [front/ruledictionnarycomputertype.php](../front/ruledictionnarycomputertype.php) | .php | — |
| [front/ruledictionnarymanufacturer.form.php](../front/ruledictionnarymanufacturer.form.php) | .php | — |
| [front/ruledictionnarymanufacturer.php](../front/ruledictionnarymanufacturer.php) | .php | — |
| [front/ruledictionnarymonitormodel.form.php](../front/ruledictionnarymonitormodel.form.php) | .php | — |
| [front/ruledictionnarymonitormodel.php](../front/ruledictionnarymonitormodel.php) | .php | — |
| [front/ruledictionnarymonitortype.form.php](../front/ruledictionnarymonitortype.form.php) | .php | — |
| [front/ruledictionnarymonitortype.php](../front/ruledictionnarymonitortype.php) | .php | — |
| [front/ruledictionnarynetworkequipmentmodel.form.php](../front/ruledictionnarynetworkequipmentmodel.form.php) | .php | — |
| [front/ruledictionnarynetworkequipmentmodel.php](../front/ruledictionnarynetworkequipmentmodel.php) | .php | — |
| [front/ruledictionnarynetworkequipmenttype.form.php](../front/ruledictionnarynetworkequipmenttype.form.php) | .php | — |
| [front/ruledictionnarynetworkequipmenttype.php](../front/ruledictionnarynetworkequipmenttype.php) | .php | — |
| [front/ruledictionnaryoperatingsystem.form.php](../front/ruledictionnaryoperatingsystem.form.php) | .php | — |
| [front/ruledictionnaryoperatingsystem.php](../front/ruledictionnaryoperatingsystem.php) | .php | — |
| [front/ruledictionnaryoperatingsystemarchitecture.form.php](../front/ruledictionnaryoperatingsystemarchitecture.form.php) | .php | — |
| [front/ruledictionnaryoperatingsystemarchitecture.php](../front/ruledictionnaryoperatingsystemarchitecture.php) | .php | — |
| [front/ruledictionnaryoperatingsystemedition.form.php](../front/ruledictionnaryoperatingsystemedition.form.php) | .php | — |
| [front/ruledictionnaryoperatingsystemedition.php](../front/ruledictionnaryoperatingsystemedition.php) | .php | — |
| [front/ruledictionnaryoperatingsystemservicepack.form.php](../front/ruledictionnaryoperatingsystemservicepack.form.php) | .php | — |
| [front/ruledictionnaryoperatingsystemservicepack.php](../front/ruledictionnaryoperatingsystemservicepack.php) | .php | — |
| [front/ruledictionnaryoperatingsystemversion.form.php](../front/ruledictionnaryoperatingsystemversion.form.php) | .php | — |
| [front/ruledictionnaryoperatingsystemversion.php](../front/ruledictionnaryoperatingsystemversion.php) | .php | — |
| [front/ruledictionnaryperipheralmodel.form.php](../front/ruledictionnaryperipheralmodel.form.php) | .php | — |
| [front/ruledictionnaryperipheralmodel.php](../front/ruledictionnaryperipheralmodel.php) | .php | — |
| [front/ruledictionnaryperipheraltype.form.php](../front/ruledictionnaryperipheraltype.form.php) | .php | — |
| [front/ruledictionnaryperipheraltype.php](../front/ruledictionnaryperipheraltype.php) | .php | — |
| [front/ruledictionnaryphonemodel.form.php](../front/ruledictionnaryphonemodel.form.php) | .php | — |
| [front/ruledictionnaryphonemodel.php](../front/ruledictionnaryphonemodel.php) | .php | — |
| [front/ruledictionnaryphonetype.form.php](../front/ruledictionnaryphonetype.form.php) | .php | — |
| [front/ruledictionnaryphonetype.php](../front/ruledictionnaryphonetype.php) | .php | — |
| [front/ruledictionnaryprinter.form.php](../front/ruledictionnaryprinter.form.php) | .php | — |
| [front/ruledictionnaryprinter.php](../front/ruledictionnaryprinter.php) | .php | — |
| [front/ruledictionnaryprintermodel.form.php](../front/ruledictionnaryprintermodel.form.php) | .php | — |
| [front/ruledictionnaryprintermodel.php](../front/ruledictionnaryprintermodel.php) | .php | — |
| [front/ruledictionnaryprintertype.form.php](../front/ruledictionnaryprintertype.form.php) | .php | — |
| [front/ruledictionnaryprintertype.php](../front/ruledictionnaryprintertype.php) | .php | — |
| [front/ruledictionnarysoftware.form.php](../front/ruledictionnarysoftware.form.php) | .php | — |
| [front/ruledictionnarysoftware.php](../front/ruledictionnarysoftware.php) | .php | — |
| [front/ruleimportasset.form.php](../front/ruleimportasset.form.php) | .php | — |
| [front/ruleimportasset.php](../front/ruleimportasset.php) | .php | — |
| [front/ruleimportentity.form.php](../front/ruleimportentity.form.php) | .php | — |
| [front/ruleimportentity.php](../front/ruleimportentity.php) | .php | — |
| [front/rulelocation.form.php](../front/rulelocation.form.php) | .php | — |
| [front/rulelocation.php](../front/rulelocation.php) | .php | — |
| [front/rulemailcollector.form.php](../front/rulemailcollector.form.php) | .php | — |
| [front/rulemailcollector.php](../front/rulemailcollector.php) | .php | — |
| [front/ruleproblem.form.php](../front/ruleproblem.form.php) | .php | — |
| [front/ruleproblem.php](../front/ruleproblem.php) | .php | — |
| [front/ruleright.form.php](../front/ruleright.form.php) | .php | — |
| [front/ruleright.php](../front/ruleright.php) | .php | — |
| [front/rulesengine.test.php](../front/rulesengine.test.php) | .php | — |
| [front/rulesoftwarecategory.form.php](../front/rulesoftwarecategory.form.php) | .php | — |
| [front/rulesoftwarecategory.php](../front/rulesoftwarecategory.php) | .php | — |
| [front/ruleticket.form.php](../front/ruleticket.form.php) | .php | — |
| [front/ruleticket.php](../front/ruleticket.php) | .php | — |
| [front/savedsearch.php](../front/savedsearch.php) | .php | — |
| [front/savedsearch_alert.form.php](../front/savedsearch_alert.form.php) | .php | — |
| [front/search.php](../front/search.php) | .php | — |
| [front/setup.auth.php](../front/setup.auth.php) | .php | — |
| [front/setup.notification.php](../front/setup.notification.php) | .php | — |
| [front/setup.templates.php](../front/setup.templates.php) | .php | — |
| [front/slalevel.form.php](../front/slalevel.form.php) | .php | — |
| [front/slalevelaction.form.php](../front/slalevelaction.form.php) | .php | — |
| [front/slalevelcriteria.form.php](../front/slalevelcriteria.form.php) | .php | — |
| [front/smtp_oauth2_callback.php](../front/smtp_oauth2_callback.php) | .php | — |
| [front/snmpcredential.form.php](../front/snmpcredential.form.php) | .php | — |
| [front/socket.form.php](../front/socket.form.php) | .php | — |
| [front/softwarelicense.form.php](../front/softwarelicense.form.php) | .php | — |
| [front/softwareversion.form.php](../front/softwareversion.form.php) | .php | — |
| [front/stat.global.php](../front/stat.global.php) | .php | — |
| [front/stat.graph.php](../front/stat.graph.php) | .php | — |
| [front/stat.item.php](../front/stat.item.php) | .php | — |
| [front/stat.location.php](../front/stat.location.php) | .php | — |
| [front/stat.php](../front/stat.php) | .php | — |
| [front/stat.tracking.php](../front/stat.tracking.php) | .php | — |
| [front/stencil.form.php](../front/stencil.form.php) | .php | — |
| [front/supplier_ticket.form.php](../front/supplier_ticket.form.php) | .php | — |
| [front/ticket.form.php](../front/ticket.form.php) | .php | — |
| [front/ticket.php](../front/ticket.php) | .php | — |
| [front/ticket_contract.form.php](../front/ticket_contract.form.php) | .php | — |
| [front/ticket_ticket.form.php](../front/ticket_ticket.form.php) | .php | — |
| [front/ticket_user.form.php](../front/ticket_user.form.php) | .php | — |
| [front/ticketcost.form.php](../front/ticketcost.form.php) | .php | — |
| [front/ticketsatisfaction.form.php](../front/ticketsatisfaction.form.php) | .php | — |
| [front/tickettask.form.php](../front/tickettask.form.php) | .php | — |
| [front/tickettemplatehiddenfield.form.php](../front/tickettemplatehiddenfield.form.php) | .php | — |
| [front/tickettemplatemandatoryfield.form.php](../front/tickettemplatemandatoryfield.form.php) | .php | — |
| [front/tickettemplatepredefinedfield.form.php](../front/tickettemplatepredefinedfield.form.php) | .php | — |
| [front/tickettemplatereadonlyfield.form.php](../front/tickettemplatereadonlyfield.form.php) | .php | — |
| [front/ticketvalidation.form.php](../front/ticketvalidation.form.php) | .php | — |
| [front/transfer.action.php](../front/transfer.action.php) | .php | — |
| [front/updatepassword.php](../front/updatepassword.php) | .php | — |
| [front/user.form.php](../front/user.form.php) | .php | — |
| [front/validatorsubstitute.form.php](../front/validatorsubstitute.form.php) | .php | — |

## inc


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [inc/includes.php](../inc/includes.php) | .php | — |
| [inc/relation.constant.php](../inc/relation.constant.php) | .php | — |

## install


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [install/empty_data.php](../install/empty_data.php) | .php | — |
| [install/install.php](../install/install.php) | .php | — |
| [install/migrations/update_0.85.x_to_0.90.0.php](../install/migrations/update_0.85.x_to_0.90.0.php) | .php | — |
| [install/migrations/update_0.90.0_to_0.90.1.php](../install/migrations/update_0.90.0_to_0.90.1.php) | .php | — |
| [install/migrations/update_0.90.1_to_0.90.5.php](../install/migrations/update_0.90.1_to_0.90.5.php) | .php | — |
| [install/migrations/update_0.90.x_to_9.1.0.php](../install/migrations/update_0.90.x_to_9.1.0.php) | .php | — |
| [install/migrations/update_10.0.0_to_10.0.1.php](../install/migrations/update_10.0.0_to_10.0.1.php) | .php | — |
| [install/migrations/update_10.0.0_to_10.0.1/configs.php](../install/migrations/update_10.0.0_to_10.0.1/configs.php) | .php | — |
| [install/migrations/update_10.0.0_to_10.0.1/fixaction.php](../install/migrations/update_10.0.0_to_10.0.1/fixaction.php) | .php | — |
| [install/migrations/update_10.0.0_to_10.0.1/lockedfields.php](../install/migrations/update_10.0.0_to_10.0.1/lockedfields.php) | .php | — |
| [install/migrations/update_10.0.0_to_10.0.1/pdf.php](../install/migrations/update_10.0.0_to_10.0.1/pdf.php) | .php | — |
| [install/migrations/update_10.0.0_to_10.0.1/rename_itemtypes.php](../install/migrations/update_10.0.0_to_10.0.1/rename_itemtypes.php) | .php | — |
| [install/migrations/update_10.0.0_to_10.0.1/rulelocation.php](../install/migrations/update_10.0.0_to_10.0.1/rulelocation.php) | .php | — |
| [install/migrations/update_10.0.0_to_10.0.1/schema_fixes.php](../install/migrations/update_10.0.0_to_10.0.1/schema_fixes.php) | .php | — |
| [install/migrations/update_10.0.10_to_10.0.11.php](../install/migrations/update_10.0.10_to_10.0.11.php) | .php | — |
| [install/migrations/update_10.0.10_to_10.0.11/duplicate_searchopt_fixes.php](../install/migrations/update_10.0.10_to_10.0.11/duplicate_searchopt_fixes.php) | .php | — |
| [install/migrations/update_10.0.10_to_10.0.11/fix_document_item_index.php](../install/migrations/update_10.0.10_to_10.0.11/fix_document_item_index.php) | .php | — |
| [install/migrations/update_10.0.10_to_10.0.11/item_operatingsystem.php](../install/migrations/update_10.0.10_to_10.0.11/item_operatingsystem.php) | .php | — |
| [install/migrations/update_10.0.10_to_10.0.11/lockedfield.php](../install/migrations/update_10.0.10_to_10.0.11/lockedfield.php) | .php | — |
| [install/migrations/update_10.0.10_to_10.0.11/pendingreason.php](../install/migrations/update_10.0.10_to_10.0.11/pendingreason.php) | .php | — |
| [install/migrations/update_10.0.10_to_10.0.11/refusedequipment.php](../install/migrations/update_10.0.10_to_10.0.11/refusedequipment.php) | .php | — |
| [install/migrations/update_10.0.10_to_10.0.11/states.php](../install/migrations/update_10.0.10_to_10.0.11/states.php) | .php | — |
| [install/migrations/update_10.0.10_to_10.0.11/transfer.php](../install/migrations/update_10.0.10_to_10.0.11/transfer.php) | .php | — |
| [install/migrations/update_10.0.11_to_10.0.12.php](../install/migrations/update_10.0.11_to_10.0.12.php) | .php | — |
| [install/migrations/update_10.0.11_to_10.0.12/duplicate_searchopt_fixes.php](../install/migrations/update_10.0.11_to_10.0.12/duplicate_searchopt_fixes.php) | .php | — |
| [install/migrations/update_10.0.11_to_10.0.12/log_rights.php](../install/migrations/update_10.0.11_to_10.0.12/log_rights.php) | .php | — |
| [install/migrations/update_10.0.11_to_10.0.12/user.php](../install/migrations/update_10.0.11_to_10.0.12/user.php) | .php | — |
| [install/migrations/update_10.0.12_to_10.0.13.php](../install/migrations/update_10.0.12_to_10.0.13.php) | .php | — |
| [install/migrations/update_10.0.12_to_10.0.13/configs.php](../install/migrations/update_10.0.12_to_10.0.13/configs.php) | .php | — |
| [install/migrations/update_10.0.12_to_10.0.13/location.php](../install/migrations/update_10.0.12_to_10.0.13/location.php) | .php | — |
| [install/migrations/update_10.0.14_to_10.0.15.php](../install/migrations/update_10.0.14_to_10.0.15.php) | .php | — |
| [install/migrations/update_10.0.14_to_10.0.15/items_disks.php](../install/migrations/update_10.0.14_to_10.0.15/items_disks.php) | .php | — |
| [install/migrations/update_10.0.14_to_10.0.15/user.php](../install/migrations/update_10.0.14_to_10.0.15/user.php) | .php | — |
| [install/migrations/update_10.0.15_to_10.0.16.php](../install/migrations/update_10.0.15_to_10.0.16.php) | .php | — |
| [install/migrations/update_10.0.15_to_10.0.16/config.php](../install/migrations/update_10.0.15_to_10.0.16/config.php) | .php | — |
| [install/migrations/update_10.0.15_to_10.0.16/configs.php](../install/migrations/update_10.0.15_to_10.0.16/configs.php) | .php | — |
| [install/migrations/update_10.0.15_to_10.0.16/entities.php](../install/migrations/update_10.0.15_to_10.0.16/entities.php) | .php | — |
| [install/migrations/update_10.0.15_to_10.0.16/items_disks.php](../install/migrations/update_10.0.15_to_10.0.16/items_disks.php) | .php | — |
| [install/migrations/update_10.0.15_to_10.0.16/queuednotifications.php](../install/migrations/update_10.0.15_to_10.0.16/queuednotifications.php) | .php | — |
| [install/migrations/update_10.0.16_to_10.0.17.php](../install/migrations/update_10.0.16_to_10.0.17.php) | .php | — |
| [install/migrations/update_10.0.16_to_10.0.17/entities.php](../install/migrations/update_10.0.16_to_10.0.17/entities.php) | .php | — |
| [install/migrations/update_10.0.16_to_10.0.17/logs.php](../install/migrations/update_10.0.16_to_10.0.17/logs.php) | .php | — |
| [install/migrations/update_10.0.16_to_10.0.17/rule_tickets.php](../install/migrations/update_10.0.16_to_10.0.17/rule_tickets.php) | .php | — |
| [install/migrations/update_10.0.16_to_10.0.17/tree_dropdowns.php](../install/migrations/update_10.0.16_to_10.0.17/tree_dropdowns.php) | .php | — |
| [install/migrations/update_10.0.16_to_10.0.17/users.php](../install/migrations/update_10.0.16_to_10.0.17/users.php) | .php | — |
| [install/migrations/update_10.0.17_to_10.0.18.php](../install/migrations/update_10.0.17_to_10.0.18.php) | .php | — |
| [install/migrations/update_10.0.17_to_10.0.18/configs.php](../install/migrations/update_10.0.17_to_10.0.18/configs.php) | .php | — |
| [install/migrations/update_10.0.1_to_10.0.2.php](../install/migrations/update_10.0.1_to_10.0.2.php) | .php | — |
| [install/migrations/update_10.0.1_to_10.0.2/agent.php](../install/migrations/update_10.0.1_to_10.0.2/agent.php) | .php | — |
| [install/migrations/update_10.0.1_to_10.0.2/configs.php](../install/migrations/update_10.0.1_to_10.0.2/configs.php) | .php | — |
| [install/migrations/update_10.0.1_to_10.0.2/dates.php](../install/migrations/update_10.0.1_to_10.0.2/dates.php) | .php | — |
| [install/migrations/update_10.0.1_to_10.0.2/native_inventory.php](../install/migrations/update_10.0.1_to_10.0.2/native_inventory.php) | .php | — |
| [install/migrations/update_10.0.20_to_10.0.21.php](../install/migrations/update_10.0.20_to_10.0.21.php) | .php | — |
| [install/migrations/update_10.0.20_to_10.0.21/tokens.php](../install/migrations/update_10.0.20_to_10.0.21/tokens.php) | .php | — |
| [install/migrations/update_10.0.21_to_10.0.23.php](../install/migrations/update_10.0.21_to_10.0.23.php) | .php | — |
| [install/migrations/update_10.0.21_to_10.0.23/iftypes.php](../install/migrations/update_10.0.21_to_10.0.23/iftypes.php) | .php | — |
| [install/migrations/update_10.0.24_to_10.0.25.php](../install/migrations/update_10.0.24_to_10.0.25.php) | .php | — |
| [install/migrations/update_10.0.24_to_10.0.25/config.php](../install/migrations/update_10.0.24_to_10.0.25/config.php) | .php | — |
| [install/migrations/update_10.0.2_to_10.0.3.php](../install/migrations/update_10.0.2_to_10.0.3.php) | .php | — |
| [install/migrations/update_10.0.2_to_10.0.3/inventory.php](../install/migrations/update_10.0.2_to_10.0.3/inventory.php) | .php | — |
| [install/migrations/update_10.0.2_to_10.0.3/notifications.php](../install/migrations/update_10.0.2_to_10.0.3/notifications.php) | .php | — |
| [install/migrations/update_10.0.2_to_10.0.3/schema_fixes.php](../install/migrations/update_10.0.2_to_10.0.3/schema_fixes.php) | .php | — |
| [install/migrations/update_10.0.3_to_10.0.4.php](../install/migrations/update_10.0.3_to_10.0.4.php) | .php | — |
| [install/migrations/update_10.0.3_to_10.0.4/computer.php](../install/migrations/update_10.0.3_to_10.0.4/computer.php) | .php | — |
| [install/migrations/update_10.0.3_to_10.0.4/config.php](../install/migrations/update_10.0.3_to_10.0.4/config.php) | .php | — |
| [install/migrations/update_10.0.3_to_10.0.4/dashboard.php](../install/migrations/update_10.0.3_to_10.0.4/dashboard.php) | .php | — |
| [install/migrations/update_10.0.3_to_10.0.4/inventory.php](../install/migrations/update_10.0.3_to_10.0.4/inventory.php) | .php | — |
| [install/migrations/update_10.0.3_to_10.0.4/ticket.php](../install/migrations/update_10.0.3_to_10.0.4/ticket.php) | .php | — |
| [install/migrations/update_10.0.4_to_10.0.5.php](../install/migrations/update_10.0.4_to_10.0.5.php) | .php | — |
| [install/migrations/update_10.0.4_to_10.0.5/.gitkeep](../install/migrations/update_10.0.4_to_10.0.5/.gitkeep) | sem extensão | — |
| [install/migrations/update_10.0.5_to_10.0.6.php](../install/migrations/update_10.0.5_to_10.0.6.php) | .php | — |
| [install/migrations/update_10.0.5_to_10.0.6/.gitkeep](../install/migrations/update_10.0.5_to_10.0.6/.gitkeep) | sem extensão | — |
| [install/migrations/update_10.0.5_to_10.0.6/appliance.php](../install/migrations/update_10.0.5_to_10.0.6/appliance.php) | .php | — |
| [install/migrations/update_10.0.5_to_10.0.6/blacklist.php](../install/migrations/update_10.0.5_to_10.0.6/blacklist.php) | .php | — |
| [install/migrations/update_10.0.5_to_10.0.6/cable.php](../install/migrations/update_10.0.5_to_10.0.6/cable.php) | .php | — |
| [install/migrations/update_10.0.5_to_10.0.6/configs.php](../install/migrations/update_10.0.5_to_10.0.6/configs.php) | .php | — |
| [install/migrations/update_10.0.5_to_10.0.6/inventory.php](../install/migrations/update_10.0.5_to_10.0.6/inventory.php) | .php | — |
| [install/migrations/update_10.0.5_to_10.0.6/networkport.php](../install/migrations/update_10.0.5_to_10.0.6/networkport.php) | .php | — |
| [install/migrations/update_10.0.5_to_10.0.6/queuednotification.php](../install/migrations/update_10.0.5_to_10.0.6/queuednotification.php) | .php | — |
| [install/migrations/update_10.0.5_to_10.0.6/rule.php](../install/migrations/update_10.0.5_to_10.0.6/rule.php) | .php | — |
| [install/migrations/update_10.0.5_to_10.0.6/simcard.php](../install/migrations/update_10.0.5_to_10.0.6/simcard.php) | .php | — |
| [install/migrations/update_10.0.5_to_10.0.6/transfer.php](../install/migrations/update_10.0.5_to_10.0.6/transfer.php) | .php | — |
| [install/migrations/update_10.0.5_to_10.0.6/unmanaged.php](../install/migrations/update_10.0.5_to_10.0.6/unmanaged.php) | .php | — |
| [install/migrations/update_10.0.6_to_10.0.7.php](../install/migrations/update_10.0.6_to_10.0.7.php) | .php | — |
| [install/migrations/update_10.0.6_to_10.0.7/.gitkeep](../install/migrations/update_10.0.6_to_10.0.7/.gitkeep) | sem extensão | — |
| [install/migrations/update_10.0.6_to_10.0.7/contract.php](../install/migrations/update_10.0.6_to_10.0.7/contract.php) | .php | — |
| [install/migrations/update_10.0.6_to_10.0.7/domains_items.php](../install/migrations/update_10.0.6_to_10.0.7/domains_items.php) | .php | — |
| [install/migrations/update_10.0.6_to_10.0.7/indexes.php](../install/migrations/update_10.0.6_to_10.0.7/indexes.php) | .php | — |
| [install/migrations/update_10.0.6_to_10.0.7/oauth_smtp.php](../install/migrations/update_10.0.6_to_10.0.7/oauth_smtp.php) | .php | — |
| [install/migrations/update_10.0.6_to_10.0.7/profils.php](../install/migrations/update_10.0.6_to_10.0.7/profils.php) | .php | — |
| [install/migrations/update_10.0.6_to_10.0.7/ruleticket.php](../install/migrations/update_10.0.6_to_10.0.7/ruleticket.php) | .php | — |
| [install/migrations/update_10.0.6_to_10.0.7/softwarelicense.php](../install/migrations/update_10.0.6_to_10.0.7/softwarelicense.php) | .php | — |
| [install/migrations/update_10.0.6_to_10.0.7/ticket_fix_internal_tto_escalation.php](../install/migrations/update_10.0.6_to_10.0.7/ticket_fix_internal_tto_escalation.php) | .php | — |
| [install/migrations/update_10.0.6_to_10.0.7/unmanageds.php](../install/migrations/update_10.0.6_to_10.0.7/unmanageds.php) | .php | — |
| [install/migrations/update_10.0.6_to_10.0.7/wrong_fkey.php](../install/migrations/update_10.0.6_to_10.0.7/wrong_fkey.php) | .php | — |
| [install/migrations/update_10.0.7_to_10.0.8.php](../install/migrations/update_10.0.7_to_10.0.8.php) | .php | — |
| [install/migrations/update_10.0.7_to_10.0.8/.gitkeep](../install/migrations/update_10.0.7_to_10.0.8/.gitkeep) | sem extensão | — |
| [install/migrations/update_10.0.7_to_10.0.8/changes.php](../install/migrations/update_10.0.7_to_10.0.8/changes.php) | .php | — |
| [install/migrations/update_10.0.7_to_10.0.8/configs.php](../install/migrations/update_10.0.7_to_10.0.8/configs.php) | .php | — |
| [install/migrations/update_10.0.7_to_10.0.8/dates.php](../install/migrations/update_10.0.7_to_10.0.8/dates.php) | .php | — |
| [install/migrations/update_10.0.7_to_10.0.8/networkport.php](../install/migrations/update_10.0.7_to_10.0.8/networkport.php) | .php | — |
| [install/migrations/update_10.0.7_to_10.0.8/problems.php](../install/migrations/update_10.0.7_to_10.0.8/problems.php) | .php | — |
| [install/migrations/update_10.0.7_to_10.0.8/queuednotification.php](../install/migrations/update_10.0.7_to_10.0.8/queuednotification.php) | .php | — |
| [install/migrations/update_10.0.7_to_10.0.8/ram_field.php](../install/migrations/update_10.0.7_to_10.0.8/ram_field.php) | .php | — |
| [install/migrations/update_10.0.7_to_10.0.8/rule.php](../install/migrations/update_10.0.7_to_10.0.8/rule.php) | .php | — |
| [install/migrations/update_10.0.7_to_10.0.8/rule_tickets.php](../install/migrations/update_10.0.7_to_10.0.8/rule_tickets.php) | .php | — |
| [install/migrations/update_10.0.8_to_10.0.9.php](../install/migrations/update_10.0.8_to_10.0.9.php) | .php | — |
| [install/migrations/update_10.0.8_to_10.0.9/queuednotification.php](../install/migrations/update_10.0.8_to_10.0.9/queuednotification.php) | .php | — |
| [install/migrations/update_10.0.9_to_10.0.10.php](../install/migrations/update_10.0.9_to_10.0.10.php) | .php | — |
| [install/migrations/update_10.0.9_to_10.0.10/configs.php](../install/migrations/update_10.0.9_to_10.0.10/configs.php) | .php | — |
| [install/migrations/update_10.0.9_to_10.0.10/ldap_fields.php](../install/migrations/update_10.0.9_to_10.0.10/ldap_fields.php) | .php | — |
| [install/migrations/update_10.0.9_to_10.0.10/mailcollector.php](../install/migrations/update_10.0.9_to_10.0.10/mailcollector.php) | .php | — |
| [install/migrations/update_10.0.9_to_10.0.10/templates.php](../install/migrations/update_10.0.9_to_10.0.10/templates.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0.php](../install/migrations/update_10.0.x_to_11.0.0.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/.gitkeep](../install/migrations/update_10.0.x_to_11.0.0/.gitkeep) | sem extensão | — |
| [install/migrations/update_10.0.x_to_11.0.0/antivirus.php](../install/migrations/update_10.0.x_to_11.0.0/antivirus.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/approval_reminder.php](../install/migrations/update_10.0.x_to_11.0.0/approval_reminder.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/assets.php](../install/migrations/update_10.0.x_to_11.0.0/assets.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/assets_peripheralassets.php](../install/migrations/update_10.0.x_to_11.0.0/assets_peripheralassets.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/assignable_items.php](../install/migrations/update_10.0.x_to_11.0.0/assignable_items.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/authldap.php](../install/migrations/update_10.0.x_to_11.0.0/authldap.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/authmail.php](../install/migrations/update_10.0.x_to_11.0.0/authmail.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/cable.php](../install/migrations/update_10.0.x_to_11.0.0/cable.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/change_rules.php](../install/migrations/update_10.0.x_to_11.0.0/change_rules.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/changesatisfactions.php](../install/migrations/update_10.0.x_to_11.0.0/changesatisfactions.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/commonitilobject_commonitilobject.php](../install/migrations/update_10.0.x_to_11.0.0/commonitilobject_commonitilobject.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/configs.php](../install/migrations/update_10.0.x_to_11.0.0/configs.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/consumable.php](../install/migrations/update_10.0.x_to_11.0.0/consumable.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/contract_user.php](../install/migrations/update_10.0.x_to_11.0.0/contract_user.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/criteriafilter.php](../install/migrations/update_10.0.x_to_11.0.0/criteriafilter.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/crontask.php](../install/migrations/update_10.0.x_to_11.0.0/crontask.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/databaseinstance.php](../install/migrations/update_10.0.x_to_11.0.0/databaseinstance.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/dcroom.php](../install/migrations/update_10.0.x_to_11.0.0/dcroom.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/deviceharddrivetypes.php](../install/migrations/update_10.0.x_to_11.0.0/deviceharddrivetypes.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/displaypreference.php](../install/migrations/update_10.0.x_to_11.0.0/displaypreference.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/dropdowns.php](../install/migrations/update_10.0.x_to_11.0.0/dropdowns.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/entity.php](../install/migrations/update_10.0.x_to_11.0.0/entity.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/environments.php](../install/migrations/update_10.0.x_to_11.0.0/environments.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/event.php](../install/migrations/update_10.0.x_to_11.0.0/event.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/form.php](../install/migrations/update_10.0.x_to_11.0.0/form.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/group.php](../install/migrations/update_10.0.x_to_11.0.0/group.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/group_user.php](../install/migrations/update_10.0.x_to_11.0.0/group_user.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/impactrelations.php](../install/migrations/update_10.0.x_to_11.0.0/impactrelations.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/impersonate_right.php](../install/migrations/update_10.0.x_to_11.0.0/impersonate_right.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/items_lines.php](../install/migrations/update_10.0.x_to_11.0.0/items_lines.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/items_ticketrecurrents.php](../install/migrations/update_10.0.x_to_11.0.0/items_ticketrecurrents.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/itemtranslations.php](../install/migrations/update_10.0.x_to_11.0.0/itemtranslations.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/itilfollowup.php](../install/migrations/update_10.0.x_to_11.0.0/itilfollowup.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/itilfollowuptemplates.php](../install/migrations/update_10.0.x_to_11.0.0/itilfollowuptemplates.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/itilobject_templates.php](../install/migrations/update_10.0.x_to_11.0.0/itilobject_templates.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/itilreminders.php](../install/migrations/update_10.0.x_to_11.0.0/itilreminders.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/itilvalidationtemplates.php](../install/migrations/update_10.0.x_to_11.0.0/itilvalidationtemplates.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/knowbase.php](../install/migrations/update_10.0.x_to_11.0.0/knowbase.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/knowbaseitem.php](../install/migrations/update_10.0.x_to_11.0.0/knowbaseitem.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/links.php](../install/migrations/update_10.0.x_to_11.0.0/links.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/locations.php](../install/migrations/update_10.0.x_to_11.0.0/locations.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/logs.php](../install/migrations/update_10.0.x_to_11.0.0/logs.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/mailcollector_rules.php](../install/migrations/update_10.0.x_to_11.0.0/mailcollector_rules.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/mailcollectors.php](../install/migrations/update_10.0.x_to_11.0.0/mailcollectors.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/mailer.php](../install/migrations/update_10.0.x_to_11.0.0/mailer.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/mfa.php](../install/migrations/update_10.0.x_to_11.0.0/mfa.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/networkportmigrations.php](../install/migrations/update_10.0.x_to_11.0.0/networkportmigrations.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/notepads.php](../install/migrations/update_10.0.x_to_11.0.0/notepads.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/notifications.php](../install/migrations/update_10.0.x_to_11.0.0/notifications.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/oauth.php](../install/migrations/update_10.0.x_to_11.0.0/oauth.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/password_history.php](../install/migrations/update_10.0.x_to_11.0.0/password_history.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/pendingreason.php](../install/migrations/update_10.0.x_to_11.0.0/pendingreason.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/plugs.php](../install/migrations/update_10.0.x_to_11.0.0/plugs.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/printerlog.php](../install/migrations/update_10.0.x_to_11.0.0/printerlog.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/problem_rules.php](../install/migrations/update_10.0.x_to_11.0.0/problem_rules.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/processes.php](../install/migrations/update_10.0.x_to_11.0.0/processes.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/profiles.php](../install/migrations/update_10.0.x_to_11.0.0/profiles.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/projecttask.php](../install/migrations/update_10.0.x_to_11.0.0/projecttask.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/queued_notification.php](../install/migrations/update_10.0.x_to_11.0.0/queued_notification.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/recursive_groups.php](../install/migrations/update_10.0.x_to_11.0.0/recursive_groups.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/remindertranslations.php](../install/migrations/update_10.0.x_to_11.0.0/remindertranslations.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/rulesmatchedlogs.php](../install/migrations/update_10.0.x_to_11.0.0/rulesmatchedlogs.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/slm.php](../install/migrations/update_10.0.x_to_11.0.0/slm.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/software_license.php](../install/migrations/update_10.0.x_to_11.0.0/software_license.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/softwarelicense_user.php](../install/migrations/update_10.0.x_to_11.0.0/softwarelicense_user.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/softwares.php](../install/migrations/update_10.0.x_to_11.0.0/softwares.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/solutiontypes.php](../install/migrations/update_10.0.x_to_11.0.0/solutiontypes.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/state_is_helpdesk_visible.php](../install/migrations/update_10.0.x_to_11.0.0/state_is_helpdesk_visible.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/states.php](../install/migrations/update_10.0.x_to_11.0.0/states.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/stencil.php](../install/migrations/update_10.0.x_to_11.0.0/stencil.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/tasktemplate.php](../install/migrations/update_10.0.x_to_11.0.0/tasktemplate.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/tasktemplates.php](../install/migrations/update_10.0.x_to_11.0.0/tasktemplates.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/text_cols.php](../install/migrations/update_10.0.x_to_11.0.0/text_cols.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/ticket.php](../install/migrations/update_10.0.x_to_11.0.0/ticket.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/ticketrecurrents.php](../install/migrations/update_10.0.x_to_11.0.0/ticketrecurrents.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/tickettask.php](../install/migrations/update_10.0.x_to_11.0.0/tickettask.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/tls_version.php](../install/migrations/update_10.0.x_to_11.0.0/tls_version.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/translations.php](../install/migrations/update_10.0.x_to_11.0.0/translations.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/user.php](../install/migrations/update_10.0.x_to_11.0.0/user.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/user_deleted_ldap.php](../install/migrations/update_10.0.x_to_11.0.0/user_deleted_ldap.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/validations.php](../install/migrations/update_10.0.x_to_11.0.0/validations.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/validationsteps.php](../install/migrations/update_10.0.x_to_11.0.0/validationsteps.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/validatorsubstitute.php](../install/migrations/update_10.0.x_to_11.0.0/validatorsubstitute.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/virtualmachines.php](../install/migrations/update_10.0.x_to_11.0.0/virtualmachines.php) | .php | — |
| [install/migrations/update_10.0.x_to_11.0.0/webhook.php](../install/migrations/update_10.0.x_to_11.0.0/webhook.php) | .php | — |
| [install/migrations/update_11.0.11_to_11.0.12.php](../install/migrations/update_11.0.11_to_11.0.12.php) | .php | — |
| [install/migrations/update_11.0.11_to_11.0.12/config.php](../install/migrations/update_11.0.11_to_11.0.12/config.php) | .php | — |
| [install/migrations/update_11.0.1_to_11.0.2.php](../install/migrations/update_11.0.1_to_11.0.2.php) | .php | — |
| [install/migrations/update_11.0.1_to_11.0.2/configs.php](../install/migrations/update_11.0.1_to_11.0.2/configs.php) | .php | — |
| [install/migrations/update_11.0.1_to_11.0.2/documenttypes.php](../install/migrations/update_11.0.1_to_11.0.2/documenttypes.php) | .php | — |
| [install/migrations/update_11.0.1_to_11.0.2/mailer.php](../install/migrations/update_11.0.1_to_11.0.2/mailer.php) | .php | — |
| [install/migrations/update_11.0.1_to_11.0.2/planningexternalevents.php](../install/migrations/update_11.0.1_to_11.0.2/planningexternalevents.php) | .php | — |
| [install/migrations/update_11.0.2_to_11.0.3.php](../install/migrations/update_11.0.2_to_11.0.3.php) | .php | — |
| [install/migrations/update_11.0.2_to_11.0.3/index_for_active_assets.php](../install/migrations/update_11.0.2_to_11.0.3/index_for_active_assets.php) | .php | — |
| [install/migrations/update_11.0.2_to_11.0.3/printerlogs.php](../install/migrations/update_11.0.2_to_11.0.3/printerlogs.php) | .php | — |
| [install/migrations/update_11.0.2_to_11.0.3/processes.php](../install/migrations/update_11.0.2_to_11.0.3/processes.php) | .php | — |
| [install/migrations/update_11.0.2_to_11.0.3/tokens.php](../install/migrations/update_11.0.2_to_11.0.3/tokens.php) | .php | — |
| [install/migrations/update_11.0.3_to_11.0.5.php](../install/migrations/update_11.0.3_to_11.0.5.php) | .php | — |
| [install/migrations/update_11.0.3_to_11.0.5/assets.php](../install/migrations/update_11.0.3_to_11.0.5/assets.php) | .php | — |
| [install/migrations/update_11.0.3_to_11.0.5/configs.php](../install/migrations/update_11.0.3_to_11.0.5/configs.php) | .php | — |
| [install/migrations/update_11.0.3_to_11.0.5/entities.php](../install/migrations/update_11.0.3_to_11.0.5/entities.php) | .php | — |
| [install/migrations/update_11.0.3_to_11.0.5/iftypes.php](../install/migrations/update_11.0.3_to_11.0.5/iftypes.php) | .php | — |
| [install/migrations/update_11.0.5_to_11.0.6.php](../install/migrations/update_11.0.5_to_11.0.6.php) | .php | — |
| [install/migrations/update_11.0.5_to_11.0.6/itil_templates_values.php](../install/migrations/update_11.0.5_to_11.0.6/itil_templates_values.php) | .php | — |
| [install/migrations/update_11.0.5_to_11.0.6/notificationtargets.php](../install/migrations/update_11.0.5_to_11.0.6/notificationtargets.php) | .php | — |
| [install/migrations/update_11.0.5_to_11.0.6/plugins.php](../install/migrations/update_11.0.5_to_11.0.6/plugins.php) | .php | — |
| [install/migrations/update_11.0.6_to_11.0.7.php](../install/migrations/update_11.0.6_to_11.0.7.php) | .php | — |
| [install/migrations/update_11.0.6_to_11.0.7/notimportedmails.php](../install/migrations/update_11.0.6_to_11.0.7/notimportedmails.php) | .php | — |
| [install/migrations/update_11.0.7_to_11.0.8.php](../install/migrations/update_11.0.7_to_11.0.8.php) | .php | — |
| [install/migrations/update_11.0.7_to_11.0.8/asset_and_dropdown_definitions_profiles.php](../install/migrations/update_11.0.7_to_11.0.8/asset_and_dropdown_definitions_profiles.php) | .php | — |
| [install/migrations/update_11.0.7_to_11.0.8/service_catalog.php](../install/migrations/update_11.0.7_to_11.0.8/service_catalog.php) | .php | — |
| [install/migrations/update_11.0.8_to_11.0.9.php](../install/migrations/update_11.0.8_to_11.0.9.php) | .php | — |
| [install/migrations/update_11.0.8_to_11.0.9/crontask.php](../install/migrations/update_11.0.8_to_11.0.9/crontask.php) | .php | — |
| [install/migrations/update_11.0.8_to_11.0.9/notification.php](../install/migrations/update_11.0.8_to_11.0.9/notification.php) | .php | — |
| [install/migrations/update_11.0.8_to_11.0.9/notification_templates_encoding.php](../install/migrations/update_11.0.8_to_11.0.9/notification_templates_encoding.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0.php](../install/migrations/update_11.0.x_to_12.0.0.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/.gitkeep](../install/migrations/update_11.0.x_to_12.0.0/.gitkeep) | sem extensão | — |
| [install/migrations/update_11.0.x_to_12.0.0/configs.php](../install/migrations/update_11.0.x_to_12.0.0/configs.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/costs.php](../install/migrations/update_11.0.x_to_12.0.0/costs.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/crontask.php](../install/migrations/update_11.0.x_to_12.0.0/crontask.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/dates.php](../install/migrations/update_11.0.x_to_12.0.0/dates.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/db.php](../install/migrations/update_11.0.x_to_12.0.0/db.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/dcroom_axis_labels.php](../install/migrations/update_11.0.x_to_12.0.0/dcroom_axis_labels.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/document_item_private.php](../install/migrations/update_11.0.x_to_12.0.0/document_item_private.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/documents.php](../install/migrations/update_11.0.x_to_12.0.0/documents.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/enclosure_right.php](../install/migrations/update_11.0.x_to_12.0.0/enclosure_right.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/form_question_item_multiple_items.php](../install/migrations/update_11.0.x_to_12.0.0/form_question_item_multiple_items.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/impact.php](../install/migrations/update_11.0.x_to_12.0.0/impact.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/itemtypes.php](../install/migrations/update_11.0.x_to_12.0.0/itemtypes.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/knowbaseitem_comments.php](../install/migrations/update_11.0.x_to_12.0.0/knowbaseitem_comments.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/knowbaseitem_comments_anchor.php](../install/migrations/update_11.0.x_to_12.0.0/knowbaseitem_comments_anchor.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/knowbaseitem_folds.php](../install/migrations/update_11.0.x_to_12.0.0/knowbaseitem_folds.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/knowbaseitemcategory_to_article.php](../install/migrations/update_11.0.x_to_12.0.0/knowbaseitemcategory_to_article.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/knowbaseitems_favorites.php](../install/migrations/update_11.0.x_to_12.0.0/knowbaseitems_favorites.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/knowbaseitems_root_article.php](../install/migrations/update_11.0.x_to_12.0.0/knowbaseitems_root_article.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/knowbaseitems_targets.php](../install/migrations/update_11.0.x_to_12.0.0/knowbaseitems_targets.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/knowbaseitemtranslations.php](../install/migrations/update_11.0.x_to_12.0.0/knowbaseitemtranslations.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/notifications.php](../install/migrations/update_11.0.x_to_12.0.0/notifications.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/oauth.php](../install/migrations/update_11.0.x_to_12.0.0/oauth.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/ola.php](../install/migrations/update_11.0.x_to_12.0.0/ola.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/pdus.php](../install/migrations/update_11.0.x_to_12.0.0/pdus.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/plugs.php](../install/migrations/update_11.0.x_to_12.0.0/plugs.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/profile_search_list.php](../install/migrations/update_11.0.x_to_12.0.0/profile_search_list.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/project_task_reminder.php](../install/migrations/update_11.0.x_to_12.0.0/project_task_reminder.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/sessions.php](../install/migrations/update_11.0.x_to_12.0.0/sessions.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/sharetokens.php](../install/migrations/update_11.0.x_to_12.0.0/sharetokens.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/users.php](../install/migrations/update_11.0.x_to_12.0.0/users.php) | .php | — |
| [install/migrations/update_11.0.x_to_12.0.0/webhooks.php](../install/migrations/update_11.0.x_to_12.0.0/webhooks.php) | .php | — |
| [install/migrations/update_12.0.0_to_12.0.1.php](../install/migrations/update_12.0.0_to_12.0.1.php) | .php | — |
| [install/migrations/update_12.0.0_to_12.0.1/config.php](../install/migrations/update_12.0.0_to_12.0.1/config.php) | .php | — |
| [install/migrations/update_12.0.0_to_12.0.1/configs.php](../install/migrations/update_12.0.0_to_12.0.1/configs.php) | .php | — |
| [install/migrations/update_9.1.0_to_9.1.1.php](../install/migrations/update_9.1.0_to_9.1.1.php) | .php | — |
| [install/migrations/update_9.1.1_to_9.1.3.php](../install/migrations/update_9.1.1_to_9.1.3.php) | .php | — |
| [install/migrations/update_9.1.x_to_9.2.0.php](../install/migrations/update_9.1.x_to_9.2.0.php) | .php | — |
| [install/migrations/update_9.2.0_to_9.2.1.php](../install/migrations/update_9.2.0_to_9.2.1.php) | .php | — |
| [install/migrations/update_9.2.1_to_9.2.2.php](../install/migrations/update_9.2.1_to_9.2.2.php) | .php | — |
| [install/migrations/update_9.2.2_to_9.2.3.php](../install/migrations/update_9.2.2_to_9.2.3.php) | .php | — |
| [install/migrations/update_9.2.x_to_9.3.0.php](../install/migrations/update_9.2.x_to_9.3.0.php) | .php | — |
| [install/migrations/update_9.3.0_to_9.3.1.php](../install/migrations/update_9.3.0_to_9.3.1.php) | .php | — |
| [install/migrations/update_9.3.1_to_9.3.2.php](../install/migrations/update_9.3.1_to_9.3.2.php) | .php | — |
| [install/migrations/update_9.3.x_to_9.4.0.php](../install/migrations/update_9.3.x_to_9.4.0.php) | .php | — |
| [install/migrations/update_9.4.0_to_9.4.1.php](../install/migrations/update_9.4.0_to_9.4.1.php) | .php | — |
| [install/migrations/update_9.4.1_to_9.4.2.php](../install/migrations/update_9.4.1_to_9.4.2.php) | .php | — |
| [install/migrations/update_9.4.2_to_9.4.3.php](../install/migrations/update_9.4.2_to_9.4.3.php) | .php | — |
| [install/migrations/update_9.4.3_to_9.4.5.php](../install/migrations/update_9.4.3_to_9.4.5.php) | .php | — |
| [install/migrations/update_9.4.5_to_9.4.6.php](../install/migrations/update_9.4.5_to_9.4.6.php) | .php | — |
| [install/migrations/update_9.4.6_to_9.4.7.php](../install/migrations/update_9.4.6_to_9.4.7.php) | .php | — |
| [install/migrations/update_9.4.x_to_9.5.0.php](../install/migrations/update_9.4.x_to_9.5.0.php) | .php | — |
| [install/migrations/update_9.4.x_to_9.5.0/appliances.php](../install/migrations/update_9.4.x_to_9.5.0/appliances.php) | .php | — |
| [install/migrations/update_9.4.x_to_9.5.0/dashboards.php](../install/migrations/update_9.4.x_to_9.5.0/dashboards.php) | .php | — |
| [install/migrations/update_9.5.1_to_9.5.2.php](../install/migrations/update_9.5.1_to_9.5.2.php) | .php | — |
| [install/migrations/update_9.5.2_to_9.5.3.php](../install/migrations/update_9.5.2_to_9.5.3.php) | .php | — |
| [install/migrations/update_9.5.3_to_9.5.4.php](../install/migrations/update_9.5.3_to_9.5.4.php) | .php | — |
| [install/migrations/update_9.5.4_to_9.5.5.php](../install/migrations/update_9.5.4_to_9.5.5.php) | .php | — |
| [install/migrations/update_9.5.5_to_9.5.6.php](../install/migrations/update_9.5.5_to_9.5.6.php) | .php | — |
| [install/migrations/update_9.5.6_to_9.5.7.php](../install/migrations/update_9.5.6_to_9.5.7.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0.php](../install/migrations/update_9.5.x_to_10.0.0.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/cable.php](../install/migrations/update_9.5.x_to_10.0.0/cable.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/cache.php](../install/migrations/update_9.5.x_to_10.0.0/cache.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/cameras.php](../install/migrations/update_9.5.x_to_10.0.0/cameras.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/configs.php](../install/migrations/update_9.5.x_to_10.0.0/configs.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/contact.php](../install/migrations/update_9.5.x_to_10.0.0/contact.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/contracts.php](../install/migrations/update_9.5.x_to_10.0.0/contracts.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/dashboard_filters.php](../install/migrations/update_9.5.x_to_10.0.0/dashboard_filters.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/data_fixes.php](../install/migrations/update_9.5.x_to_10.0.0/data_fixes.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/databases.php](../install/migrations/update_9.5.x_to_10.0.0/databases.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/devicebattery.php](../install/migrations/update_9.5.x_to_10.0.0/devicebattery.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/documents.php](../install/migrations/update_9.5.x_to_10.0.0/documents.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/domains.php](../install/migrations/update_9.5.x_to_10.0.0/domains.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/dropdowns.php](../install/migrations/update_9.5.x_to_10.0.0/dropdowns.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/entity.php](../install/migrations/update_9.5.x_to_10.0.0/entity.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/event.php](../install/migrations/update_9.5.x_to_10.0.0/event.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/gantt.php](../install/migrations/update_9.5.x_to_10.0.0/gantt.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/impact.php](../install/migrations/update_9.5.x_to_10.0.0/impact.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/inventory_management.php](../install/migrations/update_9.5.x_to_10.0.0/inventory_management.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/item_operatingsystem.php](../install/migrations/update_9.5.x_to_10.0.0/item_operatingsystem.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/itemtype_pictures.php](../install/migrations/update_9.5.x_to_10.0.0/itemtype_pictures.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/knowbaseitem_knowbaseitemcategory.php](../install/migrations/update_9.5.x_to_10.0.0/knowbaseitem_knowbaseitemcategory.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/ldaps.php](../install/migrations/update_9.5.x_to_10.0.0/ldaps.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/manuallinks.php](../install/migrations/update_9.5.x_to_10.0.0/manuallinks.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/native_inventory.php](../install/migrations/update_9.5.x_to_10.0.0/native_inventory.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/networknames.php](../install/migrations/update_9.5.x_to_10.0.0/networknames.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/networkportalias.php](../install/migrations/update_9.5.x_to_10.0.0/networkportalias.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/nicknames.php](../install/migrations/update_9.5.x_to_10.0.0/nicknames.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/notifications.php](../install/migrations/update_9.5.x_to_10.0.0/notifications.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/pendingreason.php](../install/migrations/update_9.5.x_to_10.0.0/pendingreason.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/planning_work_days.php](../install/migrations/update_9.5.x_to_10.0.0/planning_work_days.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/recurrentchange.php](../install/migrations/update_9.5.x_to_10.0.0/recurrentchange.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/reservationitem.php](../install/migrations/update_9.5.x_to_10.0.0/reservationitem.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/ruleticketaction.php](../install/migrations/update_9.5.x_to_10.0.0/ruleticketaction.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/savedsearch.php](../install/migrations/update_9.5.x_to_10.0.0/savedsearch.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/savedsearch_alert.php](../install/migrations/update_9.5.x_to_10.0.0/savedsearch_alert.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/schema_fixes.php](../install/migrations/update_9.5.x_to_10.0.0/schema_fixes.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/slm.php](../install/migrations/update_9.5.x_to_10.0.0/slm.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/softwares.php](../install/migrations/update_9.5.x_to_10.0.0/softwares.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/stock_thresholds.php](../install/migrations/update_9.5.x_to_10.0.0/stock_thresholds.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/supplier.php](../install/migrations/update_9.5.x_to_10.0.0/supplier.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/ticket.php](../install/migrations/update_9.5.x_to_10.0.0/ticket.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/ticket_contract.php](../install/migrations/update_9.5.x_to_10.0.0/ticket_contract.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/tickettask.php](../install/migrations/update_9.5.x_to_10.0.0/tickettask.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/transfer.php](../install/migrations/update_9.5.x_to_10.0.0/transfer.php) | .php | — |
| [install/migrations/update_9.5.x_to_10.0.0/uuids.php](../install/migrations/update_9.5.x_to_10.0.0/uuids.php) | .php | — |
| [install/mysql/glpi-0.85.5-empty.sql](../install/mysql/glpi-0.85.5-empty.sql) | .sql | — |
| [install/mysql/glpi-0.90.0-empty.sql](../install/mysql/glpi-0.90.0-empty.sql) | .sql | — |
| [install/mysql/glpi-0.90.1-empty.sql](../install/mysql/glpi-0.90.1-empty.sql) | .sql | — |
| [install/mysql/glpi-0.90.2-empty.sql](../install/mysql/glpi-0.90.2-empty.sql) | .sql | — |
| [install/mysql/glpi-0.90.3-empty.sql](../install/mysql/glpi-0.90.3-empty.sql) | .sql | — |
| [install/mysql/glpi-0.90.4-empty.sql](../install/mysql/glpi-0.90.4-empty.sql) | .sql | — |
| [install/mysql/glpi-0.90.5-empty.sql](../install/mysql/glpi-0.90.5-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.0-empty.sql](../install/mysql/glpi-10.0.0-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.1-empty.sql](../install/mysql/glpi-10.0.1-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.10-empty.sql](../install/mysql/glpi-10.0.10-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.11-empty.sql](../install/mysql/glpi-10.0.11-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.12-empty.sql](../install/mysql/glpi-10.0.12-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.13-empty.sql](../install/mysql/glpi-10.0.13-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.14-empty.sql](../install/mysql/glpi-10.0.14-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.15-empty.sql](../install/mysql/glpi-10.0.15-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.16-empty.sql](../install/mysql/glpi-10.0.16-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.17-empty.sql](../install/mysql/glpi-10.0.17-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.18-empty.sql](../install/mysql/glpi-10.0.18-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.19-empty.sql](../install/mysql/glpi-10.0.19-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.2-empty.sql](../install/mysql/glpi-10.0.2-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.20-empty.sql](../install/mysql/glpi-10.0.20-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.21-empty.sql](../install/mysql/glpi-10.0.21-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.22-empty.sql](../install/mysql/glpi-10.0.22-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.23-empty.sql](../install/mysql/glpi-10.0.23-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.24-empty.sql](../install/mysql/glpi-10.0.24-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.25-empty.sql](../install/mysql/glpi-10.0.25-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.26-empty.sql](../install/mysql/glpi-10.0.26-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.27-empty.sql](../install/mysql/glpi-10.0.27-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.28-empty.sql](../install/mysql/glpi-10.0.28-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.3-empty.sql](../install/mysql/glpi-10.0.3-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.4-empty.sql](../install/mysql/glpi-10.0.4-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.5-empty.sql](../install/mysql/glpi-10.0.5-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.6-empty.sql](../install/mysql/glpi-10.0.6-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.7-empty.sql](../install/mysql/glpi-10.0.7-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.8-empty.sql](../install/mysql/glpi-10.0.8-empty.sql) | .sql | — |
| [install/mysql/glpi-10.0.9-empty.sql](../install/mysql/glpi-10.0.9-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.0-empty.sql](../install/mysql/glpi-11.0.0-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.1-empty.sql](../install/mysql/glpi-11.0.1-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.10-empty.sql](../install/mysql/glpi-11.0.10-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.11-empty.sql](../install/mysql/glpi-11.0.11-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.12-empty.sql](../install/mysql/glpi-11.0.12-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.2-empty.sql](../install/mysql/glpi-11.0.2-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.3-empty.sql](../install/mysql/glpi-11.0.3-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.4-empty.sql](../install/mysql/glpi-11.0.4-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.5-empty.sql](../install/mysql/glpi-11.0.5-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.6-empty.sql](../install/mysql/glpi-11.0.6-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.7-empty.sql](../install/mysql/glpi-11.0.7-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.8-empty.sql](../install/mysql/glpi-11.0.8-empty.sql) | .sql | — |
| [install/mysql/glpi-11.0.9-empty.sql](../install/mysql/glpi-11.0.9-empty.sql) | .sql | — |
| [install/mysql/glpi-12.0.0-empty.sql](../install/mysql/glpi-12.0.0-empty.sql) | .sql | — |
| [install/mysql/glpi-12.0.1-empty.sql](../install/mysql/glpi-12.0.1-empty.sql) | .sql | — |
| [install/mysql/glpi-9.1.0-empty.sql](../install/mysql/glpi-9.1.0-empty.sql) | .sql | — |
| [install/mysql/glpi-9.1.1-empty.sql](../install/mysql/glpi-9.1.1-empty.sql) | .sql | — |
| [install/mysql/glpi-9.1.2-empty.sql](../install/mysql/glpi-9.1.2-empty.sql) | .sql | — |
| [install/mysql/glpi-9.1.3-empty.sql](../install/mysql/glpi-9.1.3-empty.sql) | .sql | — |
| [install/mysql/glpi-9.1.4-empty.sql](../install/mysql/glpi-9.1.4-empty.sql) | .sql | — |
| [install/mysql/glpi-9.1.5-empty.sql](../install/mysql/glpi-9.1.5-empty.sql) | .sql | — |
| [install/mysql/glpi-9.1.6-empty.sql](../install/mysql/glpi-9.1.6-empty.sql) | .sql | — |
| [install/mysql/glpi-9.1.7-empty.sql](../install/mysql/glpi-9.1.7-empty.sql) | .sql | — |
| [install/mysql/glpi-9.2.0-empty.sql](../install/mysql/glpi-9.2.0-empty.sql) | .sql | — |
| [install/mysql/glpi-9.2.1-empty.sql](../install/mysql/glpi-9.2.1-empty.sql) | .sql | — |
| [install/mysql/glpi-9.2.2-empty.sql](../install/mysql/glpi-9.2.2-empty.sql) | .sql | — |
| [install/mysql/glpi-9.2.3-empty.sql](../install/mysql/glpi-9.2.3-empty.sql) | .sql | — |
| [install/mysql/glpi-9.2.4-empty.sql](../install/mysql/glpi-9.2.4-empty.sql) | .sql | — |
| [install/mysql/glpi-9.3.0-empty.sql](../install/mysql/glpi-9.3.0-empty.sql) | .sql | — |
| [install/mysql/glpi-9.3.1-empty.sql](../install/mysql/glpi-9.3.1-empty.sql) | .sql | — |
| [install/mysql/glpi-9.3.2-empty.sql](../install/mysql/glpi-9.3.2-empty.sql) | .sql | — |
| [install/mysql/glpi-9.3.3-empty.sql](../install/mysql/glpi-9.3.3-empty.sql) | .sql | — |
| [install/mysql/glpi-9.3.4-empty.sql](../install/mysql/glpi-9.3.4-empty.sql) | .sql | — |
| [install/mysql/glpi-9.4.0-empty.sql](../install/mysql/glpi-9.4.0-empty.sql) | .sql | — |
| [install/mysql/glpi-9.4.1-empty.sql](../install/mysql/glpi-9.4.1-empty.sql) | .sql | — |
| [install/mysql/glpi-9.4.2-empty.sql](../install/mysql/glpi-9.4.2-empty.sql) | .sql | — |
| [install/mysql/glpi-9.4.3-empty.sql](../install/mysql/glpi-9.4.3-empty.sql) | .sql | — |
| [install/mysql/glpi-9.4.4-empty.sql](../install/mysql/glpi-9.4.4-empty.sql) | .sql | — |
| [install/mysql/glpi-9.4.5-empty.sql](../install/mysql/glpi-9.4.5-empty.sql) | .sql | — |
| [install/mysql/glpi-9.4.6-empty.sql](../install/mysql/glpi-9.4.6-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.0-empty.sql](../install/mysql/glpi-9.5.0-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.1-empty.sql](../install/mysql/glpi-9.5.1-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.10-empty.sql](../install/mysql/glpi-9.5.10-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.11-empty.sql](../install/mysql/glpi-9.5.11-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.12-empty.sql](../install/mysql/glpi-9.5.12-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.13-empty.sql](../install/mysql/glpi-9.5.13-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.2-empty.sql](../install/mysql/glpi-9.5.2-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.3-empty.sql](../install/mysql/glpi-9.5.3-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.4-empty.sql](../install/mysql/glpi-9.5.4-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.5-empty.sql](../install/mysql/glpi-9.5.5-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.6-empty.sql](../install/mysql/glpi-9.5.6-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.7-empty.sql](../install/mysql/glpi-9.5.7-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.8-empty.sql](../install/mysql/glpi-9.5.8-empty.sql) | .sql | — |
| [install/mysql/glpi-9.5.9-empty.sql](../install/mysql/glpi-9.5.9-empty.sql) | .sql | — |
| [install/mysql/glpi-empty.sql](../install/mysql/glpi-empty.sql) | .sql | — |
| [install/update.php](../install/update.php) | .php | — |

## js


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [js/RichText/ContentTemplatesParameters.js](../js/RichText/ContentTemplatesParameters.js) | .js | — |
| [js/RichText/FormTags.js](../js/RichText/FormTags.js) | .js | — |
| [js/RichText/UserMention.js](../js/RichText/UserMention.js) | .js | — |
| [js/cable.js](../js/cable.js) | .js | — |
| [js/clipboard.js](../js/clipboard.js) | .js | — |
| [js/common.js](../js/common.js) | .js | — |
| [js/common_ajax_controller.js](../js/common_ajax_controller.js) | .js | — |
| [js/fileupload.js](../js/fileupload.js) | .js | — |
| [js/flatpickr_buttons_plugin.js](../js/flatpickr_buttons_plugin.js) | .js | — |
| [js/glpi_dialog.js](../js/glpi_dialog.js) | .js | — |
| [js/impact.js](../js/impact.js) | .js | — |
| [js/log_filters.js](../js/log_filters.js) | .js | — |
| [js/marketplace.js](../js/marketplace.js) | .js | — |
| [js/misc.js](../js/misc.js) | .js | — |
| [js/modules/Ajax.js](../js/modules/Ajax.js) | .js | — |
| [js/modules/Dashboard/Dashboard.js](../js/modules/Dashboard/Dashboard.js) | .js | — |
| [js/modules/DynamicDropdownController.js](../js/modules/DynamicDropdownController.js) | .js | — |
| [js/modules/FileUploader.js](../js/modules/FileUploader.js) | .js | — |
| [js/modules/Form/GeolocationField.js](../js/modules/Form/GeolocationField.js) | .js | — |
| [js/modules/Form/ItemtypeCommentPopover.js](../js/modules/Form/ItemtypeCommentPopover.js) | .js | — |
| [js/modules/Form/WebIconSelector.js](../js/modules/Form/WebIconSelector.js) | .js | — |
| [js/modules/Forms/BaseConditionEditorController.js](../js/modules/Forms/BaseConditionEditorController.js) | .js | — |
| [js/modules/Forms/Condition/Engine.js](../js/modules/Forms/Condition/Engine.js) | .js | — |
| [js/modules/Forms/ConditionValidationEditorController.js](../js/modules/Forms/ConditionValidationEditorController.js) | .js | — |
| [js/modules/Forms/ConditionVisibilityEditorController.js](../js/modules/Forms/ConditionVisibilityEditorController.js) | .js | — |
| [js/modules/Forms/DestinationAccordionController.js](../js/modules/Forms/DestinationAccordionController.js) | .js | — |
| [js/modules/Forms/DestinationAutoConfigController.js](../js/modules/Forms/DestinationAutoConfigController.js) | .js | — |
| [js/modules/Forms/DestinationConditionController.js](../js/modules/Forms/DestinationConditionController.js) | .js | — |
| [js/modules/Forms/EditorController.js](../js/modules/Forms/EditorController.js) | .js | — |
| [js/modules/Forms/EditorConvertedExtractedDefaultValue.js](../js/modules/Forms/EditorConvertedExtractedDefaultValue.js) | .js | — |
| [js/modules/Forms/EditorConvertedExtractedSelectableDefaultValue.js](../js/modules/Forms/EditorConvertedExtractedSelectableDefaultValue.js) | .js | — |
| [js/modules/Forms/FieldDestinationAssociatedItem.js](../js/modules/Forms/FieldDestinationAssociatedItem.js) | .js | — |
| [js/modules/Forms/FieldDestinationMultipleConfig.js](../js/modules/Forms/FieldDestinationMultipleConfig.js) | .js | — |
| [js/modules/Forms/ItemAdvancedConfig.js](../js/modules/Forms/ItemAdvancedConfig.js) | .js | — |
| [js/modules/Forms/ItemDropdownAdvancedConfig.js](../js/modules/Forms/ItemDropdownAdvancedConfig.js) | .js | — |
| [js/modules/Forms/QuestionDateTime.js](../js/modules/Forms/QuestionDateTime.js) | .js | — |
| [js/modules/Forms/QuestionDropdown.js](../js/modules/Forms/QuestionDropdown.js) | .js | — |
| [js/modules/Forms/QuestionItem.js](../js/modules/Forms/QuestionItem.js) | .js | — |
| [js/modules/Forms/QuestionSelectable.js](../js/modules/Forms/QuestionSelectable.js) | .js | — |
| [js/modules/Forms/RendererController.js](../js/modules/Forms/RendererController.js) | .js | — |
| [js/modules/Forms/ServiceCatalogController.js](../js/modules/Forms/ServiceCatalogController.js) | .js | — |
| [js/modules/GlpiInstall.js](../js/modules/GlpiInstall.js) | .js | — |
| [js/modules/Helpdesk/HelpdeskConfigController.js](../js/modules/Helpdesk/HelpdeskConfigController.js) | .js | — |
| [js/modules/Helpdesk/HelpdeskConfigForEmptyEntityController.js](../js/modules/Helpdesk/HelpdeskConfigForEmptyEntityController.js) | .js | — |
| [js/modules/Helpdesk/IndexController.js](../js/modules/Helpdesk/IndexController.js) | .js | — |
| [js/modules/ITIL/Timeline/DocumentForm.js](../js/modules/ITIL/Timeline/DocumentForm.js) | .js | — |
| [js/modules/IllustrationPicker/Controller.js](../js/modules/IllustrationPicker/Controller.js) | .js | — |
| [js/modules/Knowbase/ArticleController.js](../js/modules/Knowbase/ArticleController.js) | .js | — |
| [js/modules/Knowbase/ArticleSidePanelController.js](../js/modules/Knowbase/ArticleSidePanelController.js) | .js | — |
| [js/modules/Knowbase/AsideAutoscroll.js](../js/modules/Knowbase/AsideAutoscroll.js) | .js | — |
| [js/modules/Knowbase/AsideController.js](../js/modules/Knowbase/AsideController.js) | .js | — |
| [js/modules/Knowbase/AsideDragController.js](../js/modules/Knowbase/AsideDragController.js) | .js | — |
| [js/modules/Knowbase/AsideTree.js](../js/modules/Knowbase/AsideTree.js) | .js | — |
| [js/modules/Knowbase/CommentAnchor.js](../js/modules/Knowbase/CommentAnchor.js) | .js | — |
| [js/modules/Knowbase/CommentHighlighter.js](../js/modules/Knowbase/CommentHighlighter.js) | .js | — |
| [js/modules/Knowbase/CommentsPanelController.js](../js/modules/Knowbase/CommentsPanelController.js) | .js | — |
| [js/modules/Knowbase/DocumentLinkController.js](../js/modules/Knowbase/DocumentLinkController.js) | .js | — |
| [js/modules/Knowbase/DomTextIndex.js](../js/modules/Knowbase/DomTextIndex.js) | .js | — |
| [js/modules/Knowbase/EditorActions.js](../js/modules/Knowbase/EditorActions.js) | .js | — |
| [js/modules/Knowbase/LinkItemFormController.js](../js/modules/Knowbase/LinkItemFormController.js) | .js | — |
| [js/modules/Knowbase/MoveModalController.js](../js/modules/Knowbase/MoveModalController.js) | .js | — |
| [js/modules/Knowbase/PermissionsFormController.js](../js/modules/Knowbase/PermissionsFormController.js) | .js | — |
| [js/modules/Knowbase/ReadModeSelectionBubble.js](../js/modules/Knowbase/ReadModeSelectionBubble.js) | .js | — |
| [js/modules/Knowbase/RevisionsPanelController.js](../js/modules/Knowbase/RevisionsPanelController.js) | .js | — |
| [js/modules/Knowbase/ServiceCatalogPanelController.js](../js/modules/Knowbase/ServiceCatalogPanelController.js) | .js | — |
| [js/modules/Knowbase/SharePopoverController.js](../js/modules/Knowbase/SharePopoverController.js) | .js | — |
| [js/modules/Knowbase/UploadController.js](../js/modules/Knowbase/UploadController.js) | .js | — |
| [js/modules/KnowbaseEditor.js](../js/modules/KnowbaseEditor.js) | .js | — |
| [js/modules/Monaco/MonacoEditor.js](../js/modules/Monaco/MonacoEditor.js) | .js | — |
| [js/modules/ObjectLock.js](../js/modules/ObjectLock.js) | .js | — |
| [js/modules/ProgressIndicator.js](../js/modules/ProgressIndicator.js) | .js | — |
| [js/modules/Screenshot/Screenshot.js](../js/modules/Screenshot/Screenshot.js) | .js | — |
| [js/modules/Search/GenericView.js](../js/modules/Search/GenericView.js) | .js | — |
| [js/modules/Search/ResultsView.js](../js/modules/Search/ResultsView.js) | .js | — |
| [js/modules/Search/Table.js](../js/modules/Search/Table.js) | .js | — |
| [js/modules/Security/MfaCodeInput.js](../js/modules/Security/MfaCodeInput.js) | .js | — |
| [js/modules/TipTap/Base64ImageHandlerExtension.js](../js/modules/TipTap/Base64ImageHandlerExtension.js) | .js | — |
| [js/modules/TipTap/CommentHighlightExtension.js](../js/modules/TipTap/CommentHighlightExtension.js) | .js | — |
| [js/modules/TipTap/CommentPosition.js](../js/modules/TipTap/CommentPosition.js) | .js | — |
| [js/modules/TipTap/EditorDialog.js](../js/modules/TipTap/EditorDialog.js) | .js | — |
| [js/modules/TipTap/LinkDialog.js](../js/modules/TipTap/LinkDialog.js) | .js | — |
| [js/modules/TipTap/SlashCommandsExtension.js](../js/modules/TipTap/SlashCommandsExtension.js) | .js | — |
| [js/modules/TipTap/TableContextMenu.js](../js/modules/TipTap/TableContextMenu.js) | .js | — |
| [js/modules/TipTap/TableGripsExtension.js](../js/modules/TipTap/TableGripsExtension.js) | .js | — |
| [js/modules/TipTap/VideoEmbedExtension.js](../js/modules/TipTap/VideoEmbedExtension.js) | .js | — |
| [js/modules/TipTap/tableQueries.js](../js/modules/TipTap/tableQueries.js) | .js | — |
| [js/modules/package.json](../js/modules/package.json) | .json | — |
| [js/notifications_ajax.js](../js/notifications_ajax.js) | .js | — |
| [js/rack.js](../js/rack.js) | .js | — |
| [js/src/vue/CustomObject/FieldPreview/Field.vue](../js/src/vue/CustomObject/FieldPreview/Field.vue) | .vue | — |
| [js/src/vue/CustomObject/FieldPreview/FieldDisplay.vue](../js/src/vue/CustomObject/FieldPreview/FieldDisplay.vue) | .vue | — |
| [js/src/vue/CustomObject/FieldPreview/Sidebar.vue](../js/src/vue/CustomObject/FieldPreview/Sidebar.vue) | .vue | — |
| [js/src/vue/Debug/Toolbar.vue](../js/src/vue/Debug/Toolbar.vue) | .vue | — |
| [js/src/vue/Debug/Widget/ClientPerformance.vue](../js/src/vue/Debug/Widget/ClientPerformance.vue) | .vue | — |
| [js/src/vue/Debug/Widget/Globals.vue](../js/src/vue/Debug/Widget/Globals.vue) | .vue | — |
| [js/src/vue/Debug/Widget/HTTPRequests.vue](../js/src/vue/Debug/Widget/HTTPRequests.vue) | .vue | — |
| [js/src/vue/Debug/Widget/Profiler.vue](../js/src/vue/Debug/Widget/Profiler.vue) | .vue | — |
| [js/src/vue/Debug/Widget/ProfilerTable.vue](../js/src/vue/Debug/Widget/ProfilerTable.vue) | .vue | — |
| [js/src/vue/Debug/Widget/RequestSummary.vue](../js/src/vue/Debug/Widget/RequestSummary.vue) | .vue | — |
| [js/src/vue/Debug/Widget/RequestTimeline.vue](../js/src/vue/Debug/Widget/RequestTimeline.vue) | .vue | — |
| [js/src/vue/Debug/Widget/SQLRequests.vue](../js/src/vue/Debug/Widget/SQLRequests.vue) | .vue | — |
| [js/src/vue/Debug/Widget/SearchOptions.vue](../js/src/vue/Debug/Widget/SearchOptions.vue) | .vue | — |
| [js/src/vue/Debug/Widget/ServerPerformance.vue](../js/src/vue/Debug/Widget/ServerPerformance.vue) | .vue | — |
| [js/src/vue/Debug/Widget/ThemeSwitcher.vue](../js/src/vue/Debug/Widget/ThemeSwitcher.vue) | .vue | — |
| [js/src/vue/Debug/WidgetButton.vue](../js/src/vue/Debug/WidgetButton.vue) | .vue | — |
| [js/src/vue/EntitySelector/EntitySelector.vue](../js/src/vue/EntitySelector/EntitySelector.vue) | .vue | — |
| [js/src/vue/EntitySelector/useEntitySelector.js](../js/src/vue/EntitySelector/useEntitySelector.js) | .js | — |
| [js/src/vue/FullCalendar/BaseFullCalendar.vue](../js/src/vue/FullCalendar/BaseFullCalendar.vue) | .vue | — |
| [js/src/vue/FullCalendar/useScheduler.js](../js/src/vue/FullCalendar/useScheduler.js) | .js | — |
| [js/src/vue/FuzzySearch/Modal.vue](../js/src/vue/FuzzySearch/Modal.vue) | .vue | — |
| [js/src/vue/Kanban/AddItemForm.vue](../js/src/vue/Kanban/AddItemForm.vue) | .vue | — |
| [js/src/vue/Kanban/Card.vue](../js/src/vue/Kanban/Card.vue) | .vue | — |
| [js/src/vue/Kanban/Column.vue](../js/src/vue/Kanban/Column.vue) | .vue | — |
| [js/src/vue/Kanban/Kanban.vue](../js/src/vue/Kanban/Kanban.vue) | .vue | — |
| [js/src/vue/Kanban/KanbanApp.vue](../js/src/vue/Kanban/KanbanApp.vue) | .vue | — |
| [js/src/vue/Kanban/Rights.js](../js/src/vue/Kanban/Rights.js) | .js | — |
| [js/src/vue/Kanban/SearchInput.js](../js/src/vue/Kanban/SearchInput.js) | .js | — |
| [js/src/vue/Kanban/SearchToken.js](../js/src/vue/Kanban/SearchToken.js) | .js | — |
| [js/src/vue/Kanban/SearchTokenizer.js](../js/src/vue/Kanban/SearchTokenizer.js) | .js | — |
| [js/src/vue/Kanban/SearchTokenizerResult.js](../js/src/vue/Kanban/SearchTokenizerResult.js) | .js | — |
| [js/src/vue/Kanban/TeamBadgeProvider.js](../js/src/vue/Kanban/TeamBadgeProvider.js) | .js | — |
| [js/src/vue/Planning/PlanningEvent.vue](../js/src/vue/Planning/PlanningEvent.vue) | .vue | — |
| [js/src/vue/Planning/PlanningFilter.vue](../js/src/vue/Planning/PlanningFilter.vue) | .vue | — |
| [js/src/vue/Planning/PlanningFiltersList.vue](../js/src/vue/Planning/PlanningFiltersList.vue) | .vue | — |
| [js/src/vue/Planning/PlanningFiltersPanel.vue](../js/src/vue/Planning/PlanningFiltersPanel.vue) | .vue | — |
| [js/src/vue/Planning/PlanningScheduler.vue](../js/src/vue/Planning/PlanningScheduler.vue) | .vue | — |
| [js/src/vue/Planning/PlanningView.vue](../js/src/vue/Planning/PlanningView.vue) | .vue | — |
| [js/src/vue/Planning/usePlanningScheduler.js](../js/src/vue/Planning/usePlanningScheduler.js) | .js | — |
| [js/src/vue/Reservations/ReservationEvent.vue](../js/src/vue/Reservations/ReservationEvent.vue) | .vue | — |
| [js/src/vue/Reservations/ReservationScheduler.vue](../js/src/vue/Reservations/ReservationScheduler.vue) | .vue | — |
| [js/src/vue/app.js](../js/src/vue/app.js) | .js | — |
| [js/src/vue/package.json](../js/src/vue/package.json) | .json | — |
| [js/stencil-editor.js](../js/stencil-editor.js) | .js | — |
| [js/webkit_fix.js](../js/webkit_fix.js) | .js | — |

## lib


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [lib/blueimp/jquery-file-upload/LICENSE.txt](../lib/blueimp/jquery-file-upload/LICENSE.txt) | .txt | — |
| [lib/blueimp/jquery-file-upload/jquery.fileupload-process.js](../lib/blueimp/jquery-file-upload/jquery.fileupload-process.js) | .js | — |
| [lib/blueimp/jquery-file-upload/jquery.fileupload-validate.js](../lib/blueimp/jquery-file-upload/jquery.fileupload-validate.js) | .js | — |
| [lib/blueimp/jquery-file-upload/jquery.fileupload.js](../lib/blueimp/jquery-file-upload/jquery.fileupload.js) | .js | — |
| [lib/blueimp/jquery-file-upload/jquery.iframe-transport.js](../lib/blueimp/jquery-file-upload/jquery.iframe-transport.js) | .js | — |
| [lib/bundles/altcha.js](../lib/bundles/altcha.js) | .js | — |
| [lib/bundles/base.js](../lib/bundles/base.js) | .js | — |
| [lib/bundles/cropper.js](../lib/bundles/cropper.js) | .js | — |
| [lib/bundles/cytoscape.js](../lib/bundles/cytoscape.js) | .js | — |
| [lib/bundles/echarts.js](../lib/bundles/echarts.js) | .js | — |
| [lib/bundles/flatpickr.js](../lib/bundles/flatpickr.js) | .js | — |
| [lib/bundles/fuzzy.js](../lib/bundles/fuzzy.js) | .js | — |
| [lib/bundles/gridstack.js](../lib/bundles/gridstack.js) | .js | — |
| [lib/bundles/jquery-file-upload.js](../lib/bundles/jquery-file-upload.js) | .js | — |
| [lib/bundles/leaflet.js](../lib/bundles/leaflet.js) | .js | — |
| [lib/bundles/masonry.js](../lib/bundles/masonry.js) | .js | — |
| [lib/bundles/monaco.js](../lib/bundles/monaco.js) | .js | — |
| [lib/bundles/photoswipe.js](../lib/bundles/photoswipe.js) | .js | — |
| [lib/bundles/sortable.js](../lib/bundles/sortable.js) | .js | — |
| [lib/bundles/swagger-ui.js](../lib/bundles/swagger-ui.js) | .js | — |
| [lib/bundles/tabler.scss](../lib/bundles/tabler.scss) | .scss | — |
| [lib/bundles/tablericons-definitions.js](../lib/bundles/tablericons-definitions.js) | .js | — |
| [lib/bundles/tinycolor.js](../lib/bundles/tinycolor.js) | .js | — |
| [lib/bundles/tinymce.js](../lib/bundles/tinymce.js) | .js | — |
| [lib/bundles/tiptap.js](../lib/bundles/tiptap.js) | .js | — |

## locales


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [locales/ar_IQ.po](../locales/ar_IQ.po) | .po | — |
| [locales/ar_SA.po](../locales/ar_SA.po) | .po | — |
| [locales/ar_SY.po](../locales/ar_SY.po) | .po | — |
| [locales/az_AZ.po](../locales/az_AZ.po) | .po | — |
| [locales/be_BY.po](../locales/be_BY.po) | .po | — |
| [locales/bg_BG.po](../locales/bg_BG.po) | .po | — |
| [locales/bn_BD.po](../locales/bn_BD.po) | .po | — |
| [locales/ca_ES.po](../locales/ca_ES.po) | .po | — |
| [locales/cs_CZ.po](../locales/cs_CZ.po) | .po | — |
| [locales/da_DK.po](../locales/da_DK.po) | .po | — |
| [locales/de_DE.po](../locales/de_DE.po) | .po | — |
| [locales/el_GR.po](../locales/el_GR.po) | .po | — |
| [locales/en_GB.po](../locales/en_GB.po) | .po | — |
| [locales/en_US.po](../locales/en_US.po) | .po | — |
| [locales/eo.po](../locales/eo.po) | .po | — |
| [locales/es_419.po](../locales/es_419.po) | .po | — |
| [locales/es_AR.po](../locales/es_AR.po) | .po | — |
| [locales/es_CL.po](../locales/es_CL.po) | .po | — |
| [locales/es_CO.po](../locales/es_CO.po) | .po | — |
| [locales/es_EC.po](../locales/es_EC.po) | .po | — |
| [locales/es_ES.po](../locales/es_ES.po) | .po | — |
| [locales/es_MX.po](../locales/es_MX.po) | .po | — |
| [locales/es_VE.po](../locales/es_VE.po) | .po | — |
| [locales/et_EE.po](../locales/et_EE.po) | .po | — |
| [locales/eu_ES.po](../locales/eu_ES.po) | .po | — |
| [locales/fa_IR.po](../locales/fa_IR.po) | .po | — |
| [locales/fi_FI.po](../locales/fi_FI.po) | .po | — |
| [locales/fr_BE.po](../locales/fr_BE.po) | .po | — |
| [locales/fr_CA.po](../locales/fr_CA.po) | .po | — |
| [locales/fr_FR.po](../locales/fr_FR.po) | .po | — |
| [locales/gl_ES.po](../locales/gl_ES.po) | .po | — |
| [locales/glpi.pot](../locales/glpi.pot) | .pot | — |
| [locales/he_IL.po](../locales/he_IL.po) | .po | — |
| [locales/hi_IN.po](../locales/hi_IN.po) | .po | — |
| [locales/hr_HR.po](../locales/hr_HR.po) | .po | — |
| [locales/hu_HU.po](../locales/hu_HU.po) | .po | — |
| [locales/id_ID.po](../locales/id_ID.po) | .po | — |
| [locales/is_IS.po](../locales/is_IS.po) | .po | — |
| [locales/it_IT.po](../locales/it_IT.po) | .po | — |
| [locales/ja_JP.po](../locales/ja_JP.po) | .po | — |
| [locales/ka_GE.po](../locales/ka_GE.po) | .po | — |
| [locales/km_KH.po](../locales/km_KH.po) | .po | — |
| [locales/kn.po](../locales/kn.po) | .po | — |
| [locales/ko_KR.po](../locales/ko_KR.po) | .po | — |
| [locales/lt_LT.po](../locales/lt_LT.po) | .po | — |
| [locales/lv_LV.po](../locales/lv_LV.po) | .po | — |
| [locales/mk_MK.po](../locales/mk_MK.po) | .po | — |
| [locales/mn_MN.po](../locales/mn_MN.po) | .po | — |
| [locales/ms_MY.po](../locales/ms_MY.po) | .po | — |
| [locales/nb_NO.po](../locales/nb_NO.po) | .po | — |
| [locales/nl_BE.po](../locales/nl_BE.po) | .po | — |
| [locales/nl_NL.po](../locales/nl_NL.po) | .po | — |
| [locales/nn_NO.po](../locales/nn_NO.po) | .po | — |
| [locales/pl_PL.po](../locales/pl_PL.po) | .po | — |
| [locales/pt_BR.po](../locales/pt_BR.po) | .po | — |
| [locales/pt_PT.po](../locales/pt_PT.po) | .po | — |
| [locales/ro_RO.po](../locales/ro_RO.po) | .po | — |
| [locales/ru_RU.po](../locales/ru_RU.po) | .po | — |
| [locales/sk_SK.po](../locales/sk_SK.po) | .po | — |
| [locales/sl_SI.po](../locales/sl_SI.po) | .po | — |
| [locales/sq_AL.po](../locales/sq_AL.po) | .po | — |
| [locales/sr_RS.po](../locales/sr_RS.po) | .po | — |
| [locales/sv_SE.po](../locales/sv_SE.po) | .po | — |
| [locales/th_TH.po](../locales/th_TH.po) | .po | — |
| [locales/tr_TR.po](../locales/tr_TR.po) | .po | — |
| [locales/uk_UA.po](../locales/uk_UA.po) | .po | — |
| [locales/vi_VN.po](../locales/vi_VN.po) | .po | — |
| [locales/zh_CN.po](../locales/zh_CN.po) | .po | — |
| [locales/zh_HK.po](../locales/zh_HK.po) | .po | — |
| [locales/zh_TW.po](../locales/zh_TW.po) | .po | — |

## marketplace


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [marketplace/.gitkeep](../marketplace/.gitkeep) | sem extensão | — |

## plugins


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [plugins/.gitkeep](../plugins/.gitkeep) | sem extensão | — |

## public


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [public/css/tinymce_empty_skin/content.css](../public/css/tinymce_empty_skin/content.css) | .css | — |
| [public/css/tinymce_empty_skin/skin.css](../public/css/tinymce_empty_skin/skin.css) | .css | — |
| [public/index.php](../public/index.php) | .php | — |
| [public/pics/PICS-AUTHORS.txt](../public/pics/PICS-AUTHORS.txt) | .txt | — |
| [public/pics/accepted.png](../public/pics/accepted.png) | .png | — |
| [public/pics/actualiser.png](../public/pics/actualiser.png) | .png | — |
| [public/pics/add_dark.png](../public/pics/add_dark.png) | .png | — |
| [public/pics/add_dropdown.png](../public/pics/add_dropdown.png) | .png | — |
| [public/pics/addresa.png](../public/pics/addresa.png) | .png | — |
| [public/pics/answer.png](../public/pics/answer.png) | .png | — |
| [public/pics/approbation.png](../public/pics/approbation.png) | .png | — |
| [public/pics/assign.png](../public/pics/assign.png) | .png | — |
| [public/pics/charts/area.png](../public/pics/charts/area.png) | .png | — |
| [public/pics/charts/articles.png](../public/pics/charts/articles.png) | .png | — |
| [public/pics/charts/bar.png](../public/pics/charts/bar.png) | .png | — |
| [public/pics/charts/bignumber.png](../public/pics/charts/bignumber.png) | .png | — |
| [public/pics/charts/donut.png](../public/pics/charts/donut.png) | .png | — |
| [public/pics/charts/halfdonut.png](../public/pics/charts/halfdonut.png) | .png | — |
| [public/pics/charts/halfpie.png](../public/pics/charts/halfpie.png) | .png | — |
| [public/pics/charts/hbar.png](../public/pics/charts/hbar.png) | .png | — |
| [public/pics/charts/hstacked.png](../public/pics/charts/hstacked.png) | .png | — |
| [public/pics/charts/line.png](../public/pics/charts/line.png) | .png | — |
| [public/pics/charts/markdown.png](../public/pics/charts/markdown.png) | .png | — |
| [public/pics/charts/multiplenumbers.png](../public/pics/charts/multiplenumbers.png) | .png | — |
| [public/pics/charts/pie.png](../public/pics/charts/pie.png) | .png | — |
| [public/pics/charts/sources.md](../public/pics/charts/sources.md) | .md | — |
| [public/pics/charts/stacked.png](../public/pics/charts/stacked.png) | .png | — |
| [public/pics/charts/summarynumber.png](../public/pics/charts/summarynumber.png) | .png | — |
| [public/pics/charts/table.png](../public/pics/charts/table.png) | .png | — |
| [public/pics/close.png](../public/pics/close.png) | .png | — |
| [public/pics/closed.png](../public/pics/closed.png) | .png | — |
| [public/pics/collapse.gif](../public/pics/collapse.gif) | .gif | — |
| [public/pics/collapse.png](../public/pics/collapse.png) | .png | — |
| [public/pics/corners.gif](../public/pics/corners.gif) | .gif | — |
| [public/pics/d.png](../public/pics/d.png) | .png | — |
| [public/pics/delete.png](../public/pics/delete.png) | .png | — |
| [public/pics/deplier_down.png](../public/pics/deplier_down.png) | .png | — |
| [public/pics/deplier_up.png](../public/pics/deplier_up.png) | .png | — |
| [public/pics/dollar.png](../public/pics/dollar.png) | .png | — |
| [public/pics/dollaradd.png](../public/pics/dollaradd.png) | .png | — |
| [public/pics/down.png](../public/pics/down.png) | .png | — |
| [public/pics/drag.png](../public/pics/drag.png) | .png | — |
| [public/pics/edit.png](../public/pics/edit.png) | .png | — |
| [public/pics/evaluation.png](../public/pics/evaluation.png) | .png | — |
| [public/pics/expand.gif](../public/pics/expand.gif) | .gif | — |
| [public/pics/expand.png](../public/pics/expand.png) | .png | — |
| [public/pics/faqadd.png](../public/pics/faqadd.png) | .png | — |
| [public/pics/faqedit.png](../public/pics/faqedit.png) | .png | — |
| [public/pics/favicon.ico](../public/pics/favicon.ico) | .ico | — |
| [public/pics/fd_footer.png](../public/pics/fd_footer.png) | .png | — |
| [public/pics/fd_hoverlink.png](../public/pics/fd_hoverlink.png) | .png | — |
| [public/pics/fd_logo.png](../public/pics/fd_logo.png) | .png | — |
| [public/pics/fd_nav1.png](../public/pics/fd_nav1.png) | .png | — |
| [public/pics/fd_nav3.png](../public/pics/fd_nav3.png) | .png | — |
| [public/pics/fd_ssmenu.png](../public/pics/fd_ssmenu.png) | .png | — |
| [public/pics/first.png](../public/pics/first.png) | .png | — |
| [public/pics/first_off.png](../public/pics/first_off.png) | .png | — |
| [public/pics/fond-central.png](../public/pics/fond-central.png) | .png | — |
| [public/pics/fond_form.png](../public/pics/fond_form.png) | .png | — |
| [public/pics/fond_form_on.png](../public/pics/fond_form_on.png) | .png | — |
| [public/pics/fond_onglet.png](../public/pics/fond_onglet.png) | .png | — |
| [public/pics/fond_th.png](../public/pics/fond_th.png) | .png | — |
| [public/pics/glpi.png](../public/pics/glpi.png) | .png | — |
| [public/pics/greenbutton.png](../public/pics/greenbutton.png) | .png | — |
| [public/pics/groupes.png](../public/pics/groupes.png) | .png | — |
| [public/pics/icones/ai-dist.png](../public/pics/icones/ai-dist.png) | .png | — |
| [public/pics/icones/aiff-dist.png](../public/pics/icones/aiff-dist.png) | .png | — |
| [public/pics/icones/asf-dist.png](../public/pics/icones/asf-dist.png) | .png | — |
| [public/pics/icones/avi-dist.png](../public/pics/icones/avi-dist.png) | .png | — |
| [public/pics/icones/bmp-dist.png](../public/pics/icones/bmp-dist.png) | .png | — |
| [public/pics/icones/bz2-dist.png](../public/pics/icones/bz2-dist.png) | .png | — |
| [public/pics/icones/c-dist.png](../public/pics/icones/c-dist.png) | .png | — |
| [public/pics/icones/csv-dist.png](../public/pics/icones/csv-dist.png) | .png | — |
| [public/pics/icones/deb-dist.png](../public/pics/icones/deb-dist.png) | .png | — |
| [public/pics/icones/defaut-dist.png](../public/pics/icones/defaut-dist.png) | .png | — |
| [public/pics/icones/doc-dist.png](../public/pics/icones/doc-dist.png) | .png | — |
| [public/pics/icones/dvi-dist.png](../public/pics/icones/dvi-dist.png) | .png | — |
| [public/pics/icones/eps-dist.png](../public/pics/icones/eps-dist.png) | .png | — |
| [public/pics/icones/gif-dist.png](../public/pics/icones/gif-dist.png) | .png | — |
| [public/pics/icones/gz-dist.png](../public/pics/icones/gz-dist.png) | .png | — |
| [public/pics/icones/h-dist.png](../public/pics/icones/h-dist.png) | .png | — |
| [public/pics/icones/html-dist.png](../public/pics/icones/html-dist.png) | .png | — |
| [public/pics/icones/jpg-dist.png](../public/pics/icones/jpg-dist.png) | .png | — |
| [public/pics/icones/mid-dist.png](../public/pics/icones/mid-dist.png) | .png | — |
| [public/pics/icones/mov-dist.png](../public/pics/icones/mov-dist.png) | .png | — |
| [public/pics/icones/mp3-dist.png](../public/pics/icones/mp3-dist.png) | .png | — |
| [public/pics/icones/mpg-dist.png](../public/pics/icones/mpg-dist.png) | .png | — |
| [public/pics/icones/odb-dist.png](../public/pics/icones/odb-dist.png) | .png | — |
| [public/pics/icones/odc-dist.png](../public/pics/icones/odc-dist.png) | .png | — |
| [public/pics/icones/odf-dist.png](../public/pics/icones/odf-dist.png) | .png | — |
| [public/pics/icones/odg-dist.png](../public/pics/icones/odg-dist.png) | .png | — |
| [public/pics/icones/odm-dist.png](../public/pics/icones/odm-dist.png) | .png | — |
| [public/pics/icones/odp-dist.png](../public/pics/icones/odp-dist.png) | .png | — |
| [public/pics/icones/ods-dist.png](../public/pics/icones/ods-dist.png) | .png | — |
| [public/pics/icones/odt-dist.png](../public/pics/icones/odt-dist.png) | .png | — |
| [public/pics/icones/ogg-dist.png](../public/pics/icones/ogg-dist.png) | .png | — |
| [public/pics/icones/otg-dist.png](../public/pics/icones/otg-dist.png) | .png | — |
| [public/pics/icones/oth-dist.png](../public/pics/icones/oth-dist.png) | .png | — |
| [public/pics/icones/otp-dist.png](../public/pics/icones/otp-dist.png) | .png | — |
| [public/pics/icones/ots-dist.png](../public/pics/icones/ots-dist.png) | .png | — |
| [public/pics/icones/ott-dist.png](../public/pics/icones/ott-dist.png) | .png | — |
| [public/pics/icones/pas-dist.png](../public/pics/icones/pas-dist.png) | .png | — |
| [public/pics/icones/pdf-dist.png](../public/pics/icones/pdf-dist.png) | .png | — |
| [public/pics/icones/png-dist.png](../public/pics/icones/png-dist.png) | .png | — |
| [public/pics/icones/ppt-dist.png](../public/pics/icones/ppt-dist.png) | .png | — |
| [public/pics/icones/ps-dist.png](../public/pics/icones/ps-dist.png) | .png | — |
| [public/pics/icones/psd-dist.png](../public/pics/icones/psd-dist.png) | .png | — |
| [public/pics/icones/qt-dist.png](../public/pics/icones/qt-dist.png) | .png | — |
| [public/pics/icones/ra-dist.png](../public/pics/icones/ra-dist.png) | .png | — |
| [public/pics/icones/ram-dist.png](../public/pics/icones/ram-dist.png) | .png | — |
| [public/pics/icones/rm-dist.png](../public/pics/icones/rm-dist.png) | .png | — |
| [public/pics/icones/rpm-dist.png](../public/pics/icones/rpm-dist.png) | .png | — |
| [public/pics/icones/rtf-dist.png](../public/pics/icones/rtf-dist.png) | .png | — |
| [public/pics/icones/sdd-dist.png](../public/pics/icones/sdd-dist.png) | .png | — |
| [public/pics/icones/sdw-dist.png](../public/pics/icones/sdw-dist.png) | .png | — |
| [public/pics/icones/sit-dist.png](../public/pics/icones/sit-dist.png) | .png | — |
| [public/pics/icones/svg-dist.png](../public/pics/icones/svg-dist.png) | .png | — |
| [public/pics/icones/swf-dist.png](../public/pics/icones/swf-dist.png) | .png | — |
| [public/pics/icones/sxc-dist.png](../public/pics/icones/sxc-dist.png) | .png | — |
| [public/pics/icones/sxd-dist.png](../public/pics/icones/sxd-dist.png) | .png | — |
| [public/pics/icones/sxi-dist.png](../public/pics/icones/sxi-dist.png) | .png | — |
| [public/pics/icones/sxw-dist.png](../public/pics/icones/sxw-dist.png) | .png | — |
| [public/pics/icones/tex-dist.png](../public/pics/icones/tex-dist.png) | .png | — |
| [public/pics/icones/tgz-dist.png](../public/pics/icones/tgz-dist.png) | .png | — |
| [public/pics/icones/tif-dist.png](../public/pics/icones/tif-dist.png) | .png | — |
| [public/pics/icones/txt-dist.png](../public/pics/icones/txt-dist.png) | .png | — |
| [public/pics/icones/wav-dist.png](../public/pics/icones/wav-dist.png) | .png | — |
| [public/pics/icones/webp-dist.png](../public/pics/icones/webp-dist.png) | .png | — |
| [public/pics/icones/wmv-dist.png](../public/pics/icones/wmv-dist.png) | .png | — |
| [public/pics/icones/xcf-dist.png](../public/pics/icones/xcf-dist.png) | .png | — |
| [public/pics/icones/xls-dist.png](../public/pics/icones/xls-dist.png) | .png | — |
| [public/pics/icones/xml-dist.png](../public/pics/icones/xml-dist.png) | .png | — |
| [public/pics/icones/zip-dist.png](../public/pics/icones/zip-dist.png) | .png | — |
| [public/pics/impact/README.txt](../public/pics/impact/README.txt) | .txt | — |
| [public/pics/impact/appliance.png](../public/pics/impact/appliance.png) | .png | — |
| [public/pics/impact/authldap.png](../public/pics/impact/authldap.png) | .png | — |
| [public/pics/impact/cartridgeitem.png](../public/pics/impact/cartridgeitem.png) | .png | — |
| [public/pics/impact/cluster.png](../public/pics/impact/cluster.png) | .png | — |
| [public/pics/impact/computer.png](../public/pics/impact/computer.png) | .png | — |
| [public/pics/impact/contract.png](../public/pics/impact/contract.png) | .png | — |
| [public/pics/impact/crontask.png](../public/pics/impact/crontask.png) | .png | — |
| [public/pics/impact/database.png](../public/pics/impact/database.png) | .png | — |
| [public/pics/impact/databaseinstance.png](../public/pics/impact/databaseinstance.png) | .png | — |
| [public/pics/impact/datacenter.png](../public/pics/impact/datacenter.png) | .png | — |
| [public/pics/impact/dcroom.png](../public/pics/impact/dcroom.png) | .png | — |
| [public/pics/impact/default.png](../public/pics/impact/default.png) | .png | — |
| [public/pics/impact/devicesimcard.png](../public/pics/impact/devicesimcard.png) | .png | — |
| [public/pics/impact/domain.png](../public/pics/impact/domain.png) | .png | — |
| [public/pics/impact/enclosure.png](../public/pics/impact/enclosure.png) | .png | — |
| [public/pics/impact/entity.png](../public/pics/impact/entity.png) | .png | — |
| [public/pics/impact/group.png](../public/pics/impact/group.png) | .png | — |
| [public/pics/impact/itilcategory.png](../public/pics/impact/itilcategory.png) | .png | — |
| [public/pics/impact/line.png](../public/pics/impact/line.png) | .png | — |
| [public/pics/impact/location.png](../public/pics/impact/location.png) | .png | — |
| [public/pics/impact/mailcollector.png](../public/pics/impact/mailcollector.png) | .png | — |
| [public/pics/impact/monitor.png](../public/pics/impact/monitor.png) | .png | — |
| [public/pics/impact/networkequipment.png](../public/pics/impact/networkequipment.png) | .png | — |
| [public/pics/impact/notification.png](../public/pics/impact/notification.png) | .png | — |
| [public/pics/impact/pdu.png](../public/pics/impact/pdu.png) | .png | — |
| [public/pics/impact/peripheral.png](../public/pics/impact/peripheral.png) | .png | — |
| [public/pics/impact/phone.png](../public/pics/impact/phone.png) | .png | — |
| [public/pics/impact/printer.png](../public/pics/impact/printer.png) | .png | — |
| [public/pics/impact/profile.png](../public/pics/impact/profile.png) | .png | — |
| [public/pics/impact/project.png](../public/pics/impact/project.png) | .png | — |
| [public/pics/impact/rack.png](../public/pics/impact/rack.png) | .png | — |
| [public/pics/impact/slm.png](../public/pics/impact/slm.png) | .png | — |
| [public/pics/impact/software.png](../public/pics/impact/software.png) | .png | — |
| [public/pics/impact/softwarelicense.png](../public/pics/impact/softwarelicense.png) | .png | — |
| [public/pics/impact/supplier.png](../public/pics/impact/supplier.png) | .png | — |
| [public/pics/impact/user.png](../public/pics/impact/user.png) | .png | — |
| [public/pics/jquery/pbar-ani.gif](../public/pics/jquery/pbar-ani.gif) | .gif | — |
| [public/pics/ko_min.png](../public/pics/ko_min.png) | .png | — |
| [public/pics/l.gif](../public/pics/l.gif) | .gif | — |
| [public/pics/last.png](../public/pics/last.png) | .png | — |
| [public/pics/last_off.png](../public/pics/last_off.png) | .png | — |
| [public/pics/layout/global_layout_horizontal.png](../public/pics/layout/global_layout_horizontal.png) | .png | — |
| [public/pics/layout/global_layout_vertical.png](../public/pics/layout/global_layout_vertical.png) | .png | — |
| [public/pics/left.png](../public/pics/left.png) | .png | — |
| [public/pics/left_off.png](../public/pics/left_off.png) | .png | — |
| [public/pics/loader.png](../public/pics/loader.png) | .png | — |
| [public/pics/lock.png](../public/pics/lock.png) | .png | — |
| [public/pics/login_logo_glpi.png](../public/pics/login_logo_glpi.png) | .png | — |
| [public/pics/logos/logo-G-100-black.png](../public/pics/logos/logo-G-100-black.png) | .png | — |
| [public/pics/logos/logo-G-100-grey.png](../public/pics/logos/logo-G-100-grey.png) | .png | — |
| [public/pics/logos/logo-G-100-white.png](../public/pics/logos/logo-G-100-white.png) | .png | — |
| [public/pics/logos/logo-GLPI-100-black.png](../public/pics/logos/logo-GLPI-100-black.png) | .png | — |
| [public/pics/logos/logo-GLPI-100-grey.png](../public/pics/logos/logo-GLPI-100-grey.png) | .png | — |
| [public/pics/logos/logo-GLPI-100-white.png](../public/pics/logos/logo-GLPI-100-white.png) | .png | — |
| [public/pics/logos/logo-GLPI-250-black.png](../public/pics/logos/logo-GLPI-250-black.png) | .png | — |
| [public/pics/logos/logo-GLPI-250-grey.png](../public/pics/logos/logo-GLPI-250-grey.png) | .png | — |
| [public/pics/logos/logo-GLPI-250-white.png](../public/pics/logos/logo-GLPI-250-white.png) | .png | — |
| [public/pics/logos/sources/GLPI_Logo-color.svg](../public/pics/logos/sources/GLPI_Logo-color.svg) | .svg | — |
| [public/pics/logos/sources/GLPI_Logo-white.svg](../public/pics/logos/sources/GLPI_Logo-white.svg) | .svg | — |
| [public/pics/menu_add.png](../public/pics/menu_add.png) | .png | — |
| [public/pics/menu_add_off.png](../public/pics/menu_add_off.png) | .png | — |
| [public/pics/menu_addtemplate.png](../public/pics/menu_addtemplate.png) | .png | — |
| [public/pics/menu_all.png](../public/pics/menu_all.png) | .png | — |
| [public/pics/menu_config.png](../public/pics/menu_config.png) | .png | — |
| [public/pics/menu_search.png](../public/pics/menu_search.png) | .png | — |
| [public/pics/menu_search_off.png](../public/pics/menu_search_off.png) | .png | — |
| [public/pics/menu_show.png](../public/pics/menu_show.png) | .png | — |
| [public/pics/meta_moins.png](../public/pics/meta_moins.png) | .png | — |
| [public/pics/meta_plus.png](../public/pics/meta_plus.png) | .png | — |
| [public/pics/moins.png](../public/pics/moins.png) | .png | — |
| [public/pics/new.png](../public/pics/new.png) | .png | — |
| [public/pics/nothing.gif](../public/pics/nothing.gif) | .gif | — |
| [public/pics/observe.png](../public/pics/observe.png) | .png | — |
| [public/pics/ok.png](../public/pics/ok.png) | .png | — |
| [public/pics/ok_min.png](../public/pics/ok_min.png) | .png | — |
| [public/pics/options_search.png](../public/pics/options_search.png) | .png | — |
| [public/pics/picture.png](../public/pics/picture.png) | .png | — |
| [public/pics/plan.png](../public/pics/plan.png) | .png | — |
| [public/pics/plus.png](../public/pics/plus.png) | .png | — |
| [public/pics/puce.gif](../public/pics/puce.gif) | .gif | — |
| [public/pics/qualification.png](../public/pics/qualification.png) | .png | — |
| [public/pics/r.gif](../public/pics/r.gif) | .gif | — |
| [public/pics/rdv.png](../public/pics/rdv.png) | .png | — |
| [public/pics/rdv_interv.png](../public/pics/rdv_interv.png) | .png | — |
| [public/pics/rdv_private.png](../public/pics/rdv_private.png) | .png | — |
| [public/pics/rdv_public.png](../public/pics/rdv_public.png) | .png | — |
| [public/pics/redbutton.png](../public/pics/redbutton.png) | .png | — |
| [public/pics/refresh.png](../public/pics/refresh.png) | .png | — |
| [public/pics/reservation.png](../public/pics/reservation.png) | .png | — |
| [public/pics/reset.png](../public/pics/reset.png) | .png | — |
| [public/pics/right.png](../public/pics/right.png) | .png | — |
| [public/pics/right_off.png](../public/pics/right_off.png) | .png | — |
| [public/pics/screenshots/asset.png](../public/pics/screenshots/asset.png) | .png | — |
| [public/pics/screenshots/components.png](../public/pics/screenshots/components.png) | .png | — |
| [public/pics/screenshots/dashboard.png](../public/pics/screenshots/dashboard.png) | .png | — |
| [public/pics/screenshots/dcim_racks_draganddrop.gif](../public/pics/screenshots/dcim_racks_draganddrop.gif) | .gif | — |
| [public/pics/screenshots/dcim_racks_toggleimages.gif](../public/pics/screenshots/dcim_racks_toggleimages.gif) | .gif | — |
| [public/pics/screenshots/marketplace.png](../public/pics/screenshots/marketplace.png) | .png | — |
| [public/pics/screenshots/ticket.png](../public/pics/screenshots/ticket.png) | .png | — |
| [public/pics/screenshots/timeline.png](../public/pics/screenshots/timeline.png) | .png | — |
| [public/pics/search.png](../public/pics/search.png) | .png | — |
| [public/pics/showdeleted.png](../public/pics/showdeleted.png) | .png | — |
| [public/pics/showselect.png](../public/pics/showselect.png) | .png | — |
| [public/pics/solved.png](../public/pics/solved.png) | .png | — |
| [public/pics/spinner.48.gif](../public/pics/spinner.48.gif) | .gif | — |
| [public/pics/spinner.gif](../public/pics/spinner.gif) | .gif | — |
| [public/pics/stats_item.png](../public/pics/stats_item.png) | .png | — |
| [public/pics/sub_dropdown.png](../public/pics/sub_dropdown.png) | .png | — |
| [public/pics/tb.gif](../public/pics/tb.gif) | .gif | — |
| [public/pics/test.png](../public/pics/test.png) | .png | — |
| [public/pics/timeline/1.png](../public/pics/timeline/1.png) | .png | — |
| [public/pics/timeline/2.png](../public/pics/timeline/2.png) | .png | — |
| [public/pics/timeline/3.png](../public/pics/timeline/3.png) | .png | — |
| [public/pics/timeline/4.png](../public/pics/timeline/4.png) | .png | — |
| [public/pics/timeline/5.png](../public/pics/timeline/5.png) | .png | — |
| [public/pics/timeline/delete.png](../public/pics/timeline/delete.png) | .png | — |
| [public/pics/timeline/done.png](../public/pics/timeline/done.png) | .png | — |
| [public/pics/timeline/edit.png](../public/pics/timeline/edit.png) | .png | — |
| [public/pics/timeline/file.png](../public/pics/timeline/file.png) | .png | — |
| [public/pics/timeline/followup.png](../public/pics/timeline/followup.png) | .png | — |
| [public/pics/timeline/group.png](../public/pics/timeline/group.png) | .png | — |
| [public/pics/timeline/information.png](../public/pics/timeline/information.png) | .png | — |
| [public/pics/timeline/reset.png](../public/pics/timeline/reset.png) | .png | — |
| [public/pics/timeline/task.png](../public/pics/timeline/task.png) | .png | — |
| [public/pics/timeline/todo.png](../public/pics/timeline/todo.png) | .png | — |
| [public/pics/timeline/user.png](../public/pics/timeline/user.png) | .png | — |
| [public/pics/timeline/user_grey.png](../public/pics/timeline/user_grey.png) | .png | — |
| [public/pics/timeline/validation_min.png](../public/pics/timeline/validation_min.png) | .png | — |
| [public/pics/timeline/validation_min_active.png](../public/pics/timeline/validation_min_active.png) | .png | — |
| [public/pics/toggle-left.png](../public/pics/toggle-left.png) | .png | — |
| [public/pics/toggle-right.png](../public/pics/toggle-right.png) | .png | — |
| [public/pics/treeroot.png](../public/pics/treeroot.png) | .png | — |
| [public/pics/users.png](../public/pics/users.png) | .png | — |
| [public/pics/waiting.png](../public/pics/waiting.png) | .png | — |
| [public/pics/warning.png](../public/pics/warning.png) | .png | — |
| [public/pics/warning_min.png](../public/pics/warning_min.png) | .png | — |
| [public/pics/web.png](../public/pics/web.png) | .png | — |
| [public/sound/sound_a.mp3](../public/sound/sound_a.mp3) | .mp3 | — |
| [public/sound/sound_a.ogg](../public/sound/sound_a.ogg) | .ogg | — |
| [public/sound/sound_b.mp3](../public/sound/sound_b.mp3) | .mp3 | — |
| [public/sound/sound_b.ogg](../public/sound/sound_b.ogg) | .ogg | — |
| [public/sound/sound_c.mp3](../public/sound/sound_c.mp3) | .mp3 | — |
| [public/sound/sound_c.ogg](../public/sound/sound_c.ogg) | .ogg | — |
| [public/sound/sound_d.mp3](../public/sound/sound_d.mp3) | .mp3 | — |
| [public/sound/sound_d.ogg](../public/sound/sound_d.ogg) | .ogg | — |

## resources


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [resources/Rules/RuleAsset.xml](../resources/Rules/RuleAsset.xml) | .xml | — |
| [resources/Rules/RuleDictionnaryOperatingSystem.xml](../resources/Rules/RuleDictionnaryOperatingSystem.xml) | .xml | — |
| [resources/Rules/RuleDictionnaryOperatingSystemEdition.xml](../resources/Rules/RuleDictionnaryOperatingSystemEdition.xml) | .xml | — |
| [resources/Rules/RuleDictionnaryOperatingSystemVersion.xml](../resources/Rules/RuleDictionnaryOperatingSystemVersion.xml) | .xml | — |
| [resources/Rules/RuleImportAsset.xml](../resources/Rules/RuleImportAsset.xml) | .xml | — |
| [resources/Rules/RuleMailCollector.xml](../resources/Rules/RuleMailCollector.xml) | .xml | — |
| [resources/Rules/RuleRight.xml](../resources/Rules/RuleRight.xml) | .xml | — |
| [resources/Rules/RuleSoftwareCategory.xml](../resources/Rules/RuleSoftwareCategory.xml) | .xml | — |
| [resources/Rules/RuleTicket.xml](../resources/Rules/RuleTicket.xml) | .xml | — |
| [resources/api_doc.MD](../resources/api_doc.MD) | .MD | — |

## routes


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [routes/development.php](../routes/development.php) | .php | — |
| [routes/e2e_testing.php](../routes/e2e_testing.php) | .php | — |
| [routes/testing.php](../routes/testing.php) | .php | — |

## src


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [src/APIClient.php](../src/APIClient.php) | .php | class APIClient extends CommonDBTM |
| [src/AbstractITILChildTemplate.php](../src/AbstractITILChildTemplate.php) | .php | class AbstractITILChildTemplate extends CommonDropdown |
| [src/AbstractQuery.php](../src/AbstractQuery.php) | .php | class AbstractQuery |
| [src/AbstractRightsDropdown.php](../src/AbstractRightsDropdown.php) | .php | class AbstractRightsDropdown |
| [src/Agent.php](../src/Agent.php) | .php | class Agent extends CommonDBTM |
| [src/AgentType.php](../src/AgentType.php) | .php | class AgentType extends CommonDBTM |
| [src/Ajax.php](../src/Ajax.php) | .php | class Ajax |
| [src/Alert.php](../src/Alert.php) | .php | class Alert extends CommonDBTM |
| [src/AllAssets.php](../src/AllAssets.php) | .php | class AllAssets extends CommonGLPI |
| [src/Appliance.php](../src/Appliance.php) | .php | class Appliance extends CommonDBTM |
| [src/ApplianceEnvironment.php](../src/ApplianceEnvironment.php) | .php | class ApplianceEnvironment extends CommonDropdown |
| [src/ApplianceType.php](../src/ApplianceType.php) | .php | class ApplianceType extends CommonDropdown |
| [src/Appliance_Item.php](../src/Appliance_Item.php) | .php | class Appliance_Item extends CommonDBRelation |
| [src/Appliance_Item_Relation.php](../src/Appliance_Item_Relation.php) | .php | class Appliance_Item_Relation extends CommonDBRelation |
| [src/Auth.php](../src/Auth.php) | .php | class Auth extends CommonGLPI |
| [src/AuthLDAP.php](../src/AuthLDAP.php) | .php | class AuthLDAP extends CommonDBTM |
| [src/AuthLdapReplicate.php](../src/AuthLdapReplicate.php) | .php | class AuthLdapReplicate extends CommonDBTM |
| [src/AuthMail.php](../src/AuthMail.php) | .php | class AuthMail extends CommonDBTM |
| [src/AutoUpdateSystem.php](../src/AutoUpdateSystem.php) | .php | class AutoUpdateSystem extends CommonDropdown |
| [src/BarcodeManager.php](../src/BarcodeManager.php) | .php | class BarcodeManager |
| [src/Blacklist.php](../src/Blacklist.php) | .php | class Blacklist extends CommonDropdown |
| [src/BlacklistedMailContent.php](../src/BlacklistedMailContent.php) | .php | class BlacklistedMailContent extends CommonDropdown |
| [src/Budget.php](../src/Budget.php) | .php | class Budget extends CommonDropdown |
| [src/BudgetType.php](../src/BudgetType.php) | .php | class BudgetType extends CommonType |
| [src/BusinessCriticity.php](../src/BusinessCriticity.php) | .php | class BusinessCriticity extends CommonTreeDropdown |
| [src/Cable.php](../src/Cable.php) | .php | class Cable extends CommonDBTM |
| [src/CableStrand.php](../src/CableStrand.php) | .php | class CableStrand extends CommonDropdown |
| [src/CableType.php](../src/CableType.php) | .php | class CableType extends CommonDropdown |
| [src/Calendar.php](../src/Calendar.php) | .php | class Calendar extends CommonDropdown |
| [src/CalendarSegment.php](../src/CalendarSegment.php) | .php | class CalendarSegment extends CommonDBChild |
| [src/Calendar_Holiday.php](../src/Calendar_Holiday.php) | .php | class Calendar_Holiday extends CommonDBRelation |
| [src/Cartridge.php](../src/Cartridge.php) | .php | class Cartridge extends CommonDBRelation |
| [src/CartridgeItem.php](../src/CartridgeItem.php) | .php | class CartridgeItem extends CommonDBTM |
| [src/CartridgeItemType.php](../src/CartridgeItemType.php) | .php | class CartridgeItemType extends CommonType |
| [src/CartridgeItem_PrinterModel.php](../src/CartridgeItem_PrinterModel.php) | .php | class CartridgeItem_PrinterModel extends CommonDBRelation |
| [src/Central.php](../src/Central.php) | .php | class Central extends CommonGLPI |
| [src/Certificate.php](../src/Certificate.php) | .php | class Certificate extends CommonDBTM |
| [src/CertificateType.php](../src/CertificateType.php) | .php | class CertificateType extends CommonType |
| [src/Certificate_Item.php](../src/Certificate_Item.php) | .php | class Certificate_Item extends CommonDBRelation |
| [src/Change.php](../src/Change.php) | .php | class Change extends CommonITILObject |
| [src/ChangeCost.php](../src/ChangeCost.php) | .php | class ChangeCost extends CommonITILCost |
| [src/ChangeSatisfaction.php](../src/ChangeSatisfaction.php) | .php | class ChangeSatisfaction extends CommonITILSatisfaction |
| [src/ChangeTask.php](../src/ChangeTask.php) | .php | class ChangeTask extends CommonITILTask |
| [src/ChangeTemplate.php](../src/ChangeTemplate.php) | .php | class ChangeTemplate extends ITILTemplate |
| [src/ChangeTemplateHiddenField.php](../src/ChangeTemplateHiddenField.php) | .php | class ChangeTemplateHiddenField extends ITILTemplateHiddenField |
| [src/ChangeTemplateMandatoryField.php](../src/ChangeTemplateMandatoryField.php) | .php | class ChangeTemplateMandatoryField extends ITILTemplateMandatoryField |
| [src/ChangeTemplatePredefinedField.php](../src/ChangeTemplatePredefinedField.php) | .php | class ChangeTemplatePredefinedField extends ITILTemplatePredefinedField |
| [src/ChangeTemplateReadonlyField.php](../src/ChangeTemplateReadonlyField.php) | .php | class ChangeTemplateReadonlyField extends ITILTemplateReadonlyField |
| [src/ChangeValidation.php](../src/ChangeValidation.php) | .php | class ChangeValidation extends CommonITILValidation |
| [src/ChangeValidationStep.php](../src/ChangeValidationStep.php) | .php | class ChangeValidationStep extends ITIL_ValidationStep |
| [src/Change_Change.php](../src/Change_Change.php) | .php | class Change_Change extends CommonITILObject_CommonITILObject |
| [src/Change_Group.php](../src/Change_Group.php) | .php | class Change_Group extends CommonITILActor |
| [src/Change_Item.php](../src/Change_Item.php) | .php | class Change_Item extends CommonItilObject_Item |
| [src/Change_Problem.php](../src/Change_Problem.php) | .php | class Change_Problem extends CommonITILObject_CommonITILObject |
| [src/Change_Supplier.php](../src/Change_Supplier.php) | .php | class Change_Supplier extends CommonITILActor |
| [src/Change_Ticket.php](../src/Change_Ticket.php) | .php | class Change_Ticket extends CommonITILObject_CommonITILObject |
| [src/Change_User.php](../src/Change_User.php) | .php | class Change_User extends CommonITILActor |
| [src/CleanSoftwareCron.php](../src/CleanSoftwareCron.php) | .php | class CleanSoftwareCron extends CommonDBTM |
| [src/Cluster.php](../src/Cluster.php) | .php | class Cluster extends CommonDBTM |
| [src/ClusterType.php](../src/ClusterType.php) | .php | class ClusterType extends CommonType |
| [src/CommonDBChild.php](../src/CommonDBChild.php) | .php | class CommonDBChild extends CommonDBConnexity |
| [src/CommonDBConnexity.php](../src/CommonDBConnexity.php) | .php | class CommonDBConnexity extends CommonDBTM |
| [src/CommonDBConnexityItemNotFound.php](../src/CommonDBConnexityItemNotFound.php) | .php | class CommonDBConnexityItemNotFound extends Exception |
| [src/CommonDBRelation.php](../src/CommonDBRelation.php) | .php | class CommonDBRelation extends CommonDBConnexity |
| [src/CommonDBTM.php](../src/CommonDBTM.php) | .php | class CommonDBTM extends CommonGLPI |
| [src/CommonDBVisible.php](../src/CommonDBVisible.php) | .php | class CommonDBVisible extends CommonDBTM |
| [src/CommonDCModelDropdown.php](../src/CommonDCModelDropdown.php) | .php | class CommonDCModelDropdown extends CommonDropdown |
| [src/CommonDevice.php](../src/CommonDevice.php) | .php | class CommonDevice extends CommonDropdown |
| [src/CommonDeviceModel.php](../src/CommonDeviceModel.php) | .php | class CommonDeviceModel extends CommonDropdown |
| [src/CommonDeviceType.php](../src/CommonDeviceType.php) | .php | class CommonDeviceType extends CommonType |
| [src/CommonDropdown.php](../src/CommonDropdown.php) | .php | class CommonDropdown extends CommonDBTM |
| [src/CommonGLPI.php](../src/CommonGLPI.php) | .php | class CommonGLPI |
| [src/CommonGLPIInterface.php](../src/CommonGLPIInterface.php) | .php | interface CommonGLPIInterface |
| [src/CommonITILActor.php](../src/CommonITILActor.php) | .php | class CommonITILActor extends CommonDBRelation |
| [src/CommonITILCost.php](../src/CommonITILCost.php) | .php | class CommonITILCost extends CommonDBChild |
| [src/CommonITILObject.php](../src/CommonITILObject.php) | .php | class CommonITILObject extends CommonDBTM |
| [src/CommonITILObject_CommonITILObject.php](../src/CommonITILObject_CommonITILObject.php) | .php | class CommonITILObject_CommonITILObject extends CommonDBRelation |
| [src/CommonITILRecurrent.php](../src/CommonITILRecurrent.php) | .php | class CommonITILRecurrent extends CommonDropdown |
| [src/CommonITILRecurrentCron.php](../src/CommonITILRecurrentCron.php) | .php | class CommonITILRecurrentCron extends CommonDBTM |
| [src/CommonITILSatisfaction.php](../src/CommonITILSatisfaction.php) | .php | class CommonITILSatisfaction extends CommonDBTM |
| [src/CommonITILTask.php](../src/CommonITILTask.php) | .php | class CommonITILTask extends CommonDBTM |
| [src/CommonITILValidation.php](../src/CommonITILValidation.php) | .php | class CommonITILValidation extends CommonDBChild |
| [src/CommonITILValidationCron.php](../src/CommonITILValidationCron.php) | .php | class CommonITILValidationCron extends CommonDBTM |
| [src/CommonImplicitTreeDropdown.php](../src/CommonImplicitTreeDropdown.php) | .php | class CommonImplicitTreeDropdown extends CommonTreeDropdown |
| [src/CommonItilObject_Item.php](../src/CommonItilObject_Item.php) | .php | class CommonItilObject_Item extends CommonDBRelation |
| [src/CommonTreeDropdown.php](../src/CommonTreeDropdown.php) | .php | class CommonTreeDropdown extends CommonDropdown |
| [src/CommonType.php](../src/CommonType.php) | .php | class CommonType extends CommonDropdown |
| [src/Computer.php](../src/Computer.php) | .php | class Computer extends CommonDBTM |
| [src/ComputerModel.php](../src/ComputerModel.php) | .php | class ComputerModel extends CommonDCModelDropdown |
| [src/ComputerType.php](../src/ComputerType.php) | .php | class ComputerType extends CommonType |
| [src/Config.php](../src/Config.php) | .php | class Config extends CommonDBTM |
| [src/Consumable.php](../src/Consumable.php) | .php | class Consumable extends CommonDBChild |
| [src/ConsumableItem.php](../src/ConsumableItem.php) | .php | class ConsumableItem extends CommonDBTM |
| [src/ConsumableItemType.php](../src/ConsumableItemType.php) | .php | class ConsumableItemType extends CommonType |
| [src/Contact.php](../src/Contact.php) | .php | class Contact extends CommonDBTM |
| [src/ContactType.php](../src/ContactType.php) | .php | class ContactType extends CommonType |
| [src/Contact_Supplier.php](../src/Contact_Supplier.php) | .php | class Contact_Supplier extends CommonDBRelation |
| [src/Contract.php](../src/Contract.php) | .php | class Contract extends CommonDBTM |
| [src/ContractCost.php](../src/ContractCost.php) | .php | class ContractCost extends CommonDBChild |
| [src/ContractType.php](../src/ContractType.php) | .php | class ContractType extends CommonType |
| [src/Contract_Item.php](../src/Contract_Item.php) | .php | class Contract_Item extends CommonDBRelation |
| [src/Contract_Supplier.php](../src/Contract_Supplier.php) | .php | class Contract_Supplier extends CommonDBRelation |
| [src/Contract_User.php](../src/Contract_User.php) | .php | class Contract_User extends CommonDBRelation |
| [src/CronTask.php](../src/CronTask.php) | .php | class CronTask extends CommonDBTM |
| [src/CronTaskLog.php](../src/CronTaskLog.php) | .php | class CronTaskLog extends CommonDBChild |
| [src/DBConnection.php](../src/DBConnection.php) | .php | class DBConnection extends CommonGLPI |
| [src/DBmysql.php](../src/DBmysql.php) | .php | class DBmysql |
| [src/DBmysqlIterator.php](../src/DBmysqlIterator.php) | .php | class DBmysqlIterator |
| [src/DCRoom.php](../src/DCRoom.php) | .php | class DCRoom extends CommonDBTM |
| [src/Database.php](../src/Database.php) | .php | class Database extends CommonDBChild |
| [src/DatabaseInstance.php](../src/DatabaseInstance.php) | .php | class DatabaseInstance extends CommonDBTM |
| [src/DatabaseInstanceCategory.php](../src/DatabaseInstanceCategory.php) | .php | class DatabaseInstanceCategory extends CommonDropdown |
| [src/DatabaseInstanceType.php](../src/DatabaseInstanceType.php) | .php | class DatabaseInstanceType extends CommonDropdown |
| [src/Datacenter.php](../src/Datacenter.php) | .php | class Datacenter extends CommonDBTM |
| [src/DbUtils.php](../src/DbUtils.php) | .php | class DbUtils |
| [src/DefaultFilter.php](../src/DefaultFilter.php) | .php | class DefaultFilter extends CommonDBTM |
| [src/DeviceBattery.php](../src/DeviceBattery.php) | .php | class DeviceBattery extends CommonDevice |
| [src/DeviceBatteryModel.php](../src/DeviceBatteryModel.php) | .php | class DeviceBatteryModel extends CommonDeviceModel |
| [src/DeviceBatteryType.php](../src/DeviceBatteryType.php) | .php | class DeviceBatteryType extends CommonDeviceType |
| [src/DeviceCamera.php](../src/DeviceCamera.php) | .php | class DeviceCamera extends CommonDevice |
| [src/DeviceCameraModel.php](../src/DeviceCameraModel.php) | .php | class DeviceCameraModel extends CommonDeviceModel |
| [src/DeviceCase.php](../src/DeviceCase.php) | .php | class DeviceCase extends CommonDevice |
| [src/DeviceCaseModel.php](../src/DeviceCaseModel.php) | .php | class DeviceCaseModel extends CommonDeviceModel |
| [src/DeviceCaseType.php](../src/DeviceCaseType.php) | .php | class DeviceCaseType extends CommonDeviceType |
| [src/DeviceControl.php](../src/DeviceControl.php) | .php | class DeviceControl extends CommonDevice |
| [src/DeviceControlModel.php](../src/DeviceControlModel.php) | .php | class DeviceControlModel extends CommonDeviceModel |
| [src/DeviceDrive.php](../src/DeviceDrive.php) | .php | class DeviceDrive extends CommonDevice |
| [src/DeviceDriveModel.php](../src/DeviceDriveModel.php) | .php | class DeviceDriveModel extends CommonDeviceModel |
| [src/DeviceFirmware.php](../src/DeviceFirmware.php) | .php | class DeviceFirmware extends CommonDevice |
| [src/DeviceFirmwareModel.php](../src/DeviceFirmwareModel.php) | .php | class DeviceFirmwareModel extends CommonDeviceModel |
| [src/DeviceFirmwareType.php](../src/DeviceFirmwareType.php) | .php | class DeviceFirmwareType extends CommonDeviceType |
| [src/DeviceGeneric.php](../src/DeviceGeneric.php) | .php | class DeviceGeneric extends CommonDevice |
| [src/DeviceGenericModel.php](../src/DeviceGenericModel.php) | .php | class DeviceGenericModel extends CommonDeviceModel |
| [src/DeviceGenericType.php](../src/DeviceGenericType.php) | .php | class DeviceGenericType extends CommonDeviceType |
| [src/DeviceGraphicCard.php](../src/DeviceGraphicCard.php) | .php | class DeviceGraphicCard extends CommonDevice |
| [src/DeviceGraphicCardModel.php](../src/DeviceGraphicCardModel.php) | .php | class DeviceGraphicCardModel extends CommonDeviceModel |
| [src/DeviceHardDrive.php](../src/DeviceHardDrive.php) | .php | class DeviceHardDrive extends CommonDevice |
| [src/DeviceHardDriveModel.php](../src/DeviceHardDriveModel.php) | .php | class DeviceHardDriveModel extends CommonDeviceModel |
| [src/DeviceHardDriveType.php](../src/DeviceHardDriveType.php) | .php | class DeviceHardDriveType extends CommonDeviceType |
| [src/DeviceMemory.php](../src/DeviceMemory.php) | .php | class DeviceMemory extends CommonDevice |
| [src/DeviceMemoryModel.php](../src/DeviceMemoryModel.php) | .php | class DeviceMemoryModel extends CommonDeviceModel |
| [src/DeviceMemoryType.php](../src/DeviceMemoryType.php) | .php | class DeviceMemoryType extends CommonDeviceType |
| [src/DeviceMotherboard.php](../src/DeviceMotherboard.php) | .php | class DeviceMotherboard extends CommonDevice |
| [src/DeviceMotherboardModel.php](../src/DeviceMotherboardModel.php) | .php | class DeviceMotherboardModel extends CommonDeviceModel |
| [src/DeviceNetworkCard.php](../src/DeviceNetworkCard.php) | .php | class DeviceNetworkCard extends CommonDevice |
| [src/DeviceNetworkCardModel.php](../src/DeviceNetworkCardModel.php) | .php | class DeviceNetworkCardModel extends CommonDeviceModel |
| [src/DevicePci.php](../src/DevicePci.php) | .php | class DevicePci extends CommonDevice |
| [src/DevicePciModel.php](../src/DevicePciModel.php) | .php | class DevicePciModel extends CommonDeviceModel |
| [src/DevicePowerSupply.php](../src/DevicePowerSupply.php) | .php | class DevicePowerSupply extends CommonDevice |
| [src/DevicePowerSupplyModel.php](../src/DevicePowerSupplyModel.php) | .php | class DevicePowerSupplyModel extends CommonDeviceModel |
| [src/DeviceProcessor.php](../src/DeviceProcessor.php) | .php | class DeviceProcessor extends CommonDevice |
| [src/DeviceProcessorModel.php](../src/DeviceProcessorModel.php) | .php | class DeviceProcessorModel extends CommonDeviceModel |
| [src/DeviceSensor.php](../src/DeviceSensor.php) | .php | class DeviceSensor extends CommonDevice |
| [src/DeviceSensorModel.php](../src/DeviceSensorModel.php) | .php | class DeviceSensorModel extends CommonDeviceModel |
| [src/DeviceSensorType.php](../src/DeviceSensorType.php) | .php | class DeviceSensorType extends CommonDeviceType |
| [src/DeviceSimcard.php](../src/DeviceSimcard.php) | .php | class DeviceSimcard extends CommonDevice |
| [src/DeviceSimcardType.php](../src/DeviceSimcardType.php) | .php | class DeviceSimcardType extends CommonDeviceType |
| [src/DeviceSoundCard.php](../src/DeviceSoundCard.php) | .php | class DeviceSoundCard extends CommonDevice |
| [src/DeviceSoundCardModel.php](../src/DeviceSoundCardModel.php) | .php | class DeviceSoundCardModel extends CommonDeviceModel |
| [src/DisplayPreference.php](../src/DisplayPreference.php) | .php | class DisplayPreference extends CommonDBTM |
| [src/Document.php](../src/Document.php) | .php | class Document extends CommonDBTM |
| [src/DocumentCategory.php](../src/DocumentCategory.php) | .php | class DocumentCategory extends CommonTreeDropdown |
| [src/DocumentType.php](../src/DocumentType.php) | .php | class DocumentType extends CommonDropdown |
| [src/Document_Item.php](../src/Document_Item.php) | .php | class Document_Item extends CommonDBRelation |
| [src/Domain.php](../src/Domain.php) | .php | class Domain extends CommonDBTM |
| [src/DomainRecord.php](../src/DomainRecord.php) | .php | class DomainRecord extends CommonDBChild |
| [src/DomainRecordType.php](../src/DomainRecordType.php) | .php | class DomainRecordType extends CommonDropdown |
| [src/DomainRelation.php](../src/DomainRelation.php) | .php | class DomainRelation extends CommonDropdown |
| [src/DomainType.php](../src/DomainType.php) | .php | class DomainType extends CommonDropdown |
| [src/Domain_Item.php](../src/Domain_Item.php) | .php | class Domain_Item extends CommonDBRelation |
| [src/Dropdown.php](../src/Dropdown.php) | .php | class Dropdown |
| [src/DropdownTranslation.php](../src/DropdownTranslation.php) | .php | class DropdownTranslation extends CommonDBChild |
| [src/DropdownVisibility.php](../src/DropdownVisibility.php) | .php | class DropdownVisibility extends CommonDBChild |
| [src/Enclosure.php](../src/Enclosure.php) | .php | class Enclosure extends CommonDBTM |
| [src/EnclosureModel.php](../src/EnclosureModel.php) | .php | class EnclosureModel extends CommonDCModelDropdown |
| [src/Entity.php](../src/Entity.php) | .php | class Entity extends CommonTreeDropdown |
| [src/Entity_KnowbaseItem.php](../src/Entity_KnowbaseItem.php) | .php | class Entity_KnowbaseItem extends CommonDBRelation |
| [src/Entity_RSSFeed.php](../src/Entity_RSSFeed.php) | .php | class Entity_RSSFeed extends CommonDBRelation |
| [src/Entity_Reminder.php](../src/Entity_Reminder.php) | .php | class Entity_Reminder extends CommonDBRelation |
| [src/ExtraVisibilityCriteria.php](../src/ExtraVisibilityCriteria.php) | .php | interface ExtraVisibilityCriteria |
| [src/FQDN.php](../src/FQDN.php) | .php | class FQDN extends CommonDropdown |
| [src/FQDNLabel.php](../src/FQDNLabel.php) | .php | class FQDNLabel extends CommonDBChild |
| [src/FieldUnicity.php](../src/FieldUnicity.php) | .php | class FieldUnicity extends CommonDropdown |
| [src/Fieldblacklist.php](../src/Fieldblacklist.php) | .php | class Fieldblacklist extends CommonDropdown |
| [src/Filesystem.php](../src/Filesystem.php) | .php | class Filesystem extends CommonDropdown |
| [src/GLPIKey.php](../src/GLPIKey.php) | .php | class GLPIKey |
| [src/GLPIMailer.php](../src/GLPIMailer.php) | .php | class GLPIMailer |
| [src/GLPINetwork.php](../src/GLPINetwork.php) | .php | class GLPINetwork extends CommonGLPI |
| [src/GLPIPDF.php](../src/GLPIPDF.php) | .php | class GLPIPDF extends TCPDF |
| [src/GLPIUploadHandler.php](../src/GLPIUploadHandler.php) | .php | class GLPIUploadHandler extends UploadHandler |
| [src/Glpi/Agent/Communication/AbstractRequest.php](../src/Glpi/Agent/Communication/AbstractRequest.php) | .php | class Glpi\Agent\Communication\AbstractRequest |
| [src/Glpi/Agent/Communication/Headers/Common.php](../src/Glpi/Agent/Communication/Headers/Common.php) | .php | class Glpi\Agent\Communication\Headers\Common |
| [src/Glpi/Altcha/AltchaManager.php](../src/Glpi/Altcha/AltchaManager.php) | .php | class Glpi\Altcha\AltchaManager |
| [src/Glpi/Altcha/AltchaMode.php](../src/Glpi/Altcha/AltchaMode.php) | .php | enum Glpi\Altcha\AltchaMode |
| [src/Glpi/Altcha/InvalidPayloadException.php](../src/Glpi/Altcha/InvalidPayloadException.php) | .php | class Glpi\Altcha\InvalidPayloadException extends Exception |
| [src/Glpi/Api/API.php](../src/Glpi/Api/API.php) | .php | class Glpi\Api\API |
| [src/Glpi/Api/APIRest.php](../src/Glpi/Api/APIRest.php) | .php | class Glpi\Api\APIRest extends API |
| [src/Glpi/Api/Deprecated/CommonDeprecatedTrait.php](../src/Glpi/Api/Deprecated/CommonDeprecatedTrait.php) | .php | trait Glpi\Api\Deprecated\CommonDeprecatedTrait |
| [src/Glpi/Api/Deprecated/ComputerAntivirus.php](../src/Glpi/Api/Deprecated/ComputerAntivirus.php) | .php | class Glpi\Api\Deprecated\ComputerAntivirus |
| [src/Glpi/Api/Deprecated/ComputerVirtualMachine.php](../src/Glpi/Api/Deprecated/ComputerVirtualMachine.php) | .php | class Glpi\Api\Deprecated\ComputerVirtualMachine |
| [src/Glpi/Api/Deprecated/Computer_Item.php](../src/Glpi/Api/Deprecated/Computer_Item.php) | .php | class Glpi\Api\Deprecated\Computer_Item |
| [src/Glpi/Api/Deprecated/Computer_SoftwareLicense.php](../src/Glpi/Api/Deprecated/Computer_SoftwareLicense.php) | .php | class Glpi\Api\Deprecated\Computer_SoftwareLicense |
| [src/Glpi/Api/Deprecated/Computer_SoftwareVersion.php](../src/Glpi/Api/Deprecated/Computer_SoftwareVersion.php) | .php | class Glpi\Api\Deprecated\Computer_SoftwareVersion |
| [src/Glpi/Api/Deprecated/DeprecatedInterface.php](../src/Glpi/Api/Deprecated/DeprecatedInterface.php) | .php | interface Glpi\Api\Deprecated\DeprecatedInterface |
| [src/Glpi/Api/Deprecated/Item_Plug.php](../src/Glpi/Api/Deprecated/Item_Plug.php) | .php | class Glpi\Api\Deprecated\Item_Plug |
| [src/Glpi/Api/Deprecated/Netpoint.php](../src/Glpi/Api/Deprecated/Netpoint.php) | .php | class Glpi\Api\Deprecated\Netpoint |
| [src/Glpi/Api/Deprecated/Pdu_Plug.php](../src/Glpi/Api/Deprecated/Pdu_Plug.php) | .php | class Glpi\Api\Deprecated\Pdu_Plug |
| [src/Glpi/Api/Deprecated/TicketFollowup.php](../src/Glpi/Api/Deprecated/TicketFollowup.php) | .php | class Glpi\Api\Deprecated\TicketFollowup |
| [src/Glpi/Api/HL/APIException.php](../src/Glpi/Api/HL/APIException.php) | .php | class Glpi\Api\HL\APIException extends Exception |
| [src/Glpi/Api/HL/Controller/AbstractController.php](../src/Glpi/Api/HL/Controller/AbstractController.php) | .php | class Glpi\Api\HL\Controller\AbstractController |
| [src/Glpi/Api/HL/Controller/AdministrationController.php](../src/Glpi/Api/HL/Controller/AdministrationController.php) | .php | class Glpi\Api\HL\Controller\AdministrationController extends AbstractController |
| [src/Glpi/Api/HL/Controller/AssetController.php](../src/Glpi/Api/HL/Controller/AssetController.php) | .php | class Glpi\Api\HL\Controller\AssetController extends AbstractController |
| [src/Glpi/Api/HL/Controller/CRUDControllerTrait.php](../src/Glpi/Api/HL/Controller/CRUDControllerTrait.php) | .php | trait Glpi\Api\HL\Controller\CRUDControllerTrait |
| [src/Glpi/Api/HL/Controller/ComponentController.php](../src/Glpi/Api/HL/Controller/ComponentController.php) | .php | class Glpi\Api\HL\Controller\ComponentController extends AbstractController |
| [src/Glpi/Api/HL/Controller/CoreController.php](../src/Glpi/Api/HL/Controller/CoreController.php) | .php | class Glpi\Api\HL\Controller\CoreController extends AbstractController |
| [src/Glpi/Api/HL/Controller/CustomAssetController.php](../src/Glpi/Api/HL/Controller/CustomAssetController.php) | .php | class Glpi\Api\HL\Controller\CustomAssetController extends AbstractController |
| [src/Glpi/Api/HL/Controller/DashboardController.php](../src/Glpi/Api/HL/Controller/DashboardController.php) | .php | class Glpi\Api\HL\Controller\DashboardController extends AbstractController |
| [src/Glpi/Api/HL/Controller/DropdownController.php](../src/Glpi/Api/HL/Controller/DropdownController.php) | .php | class Glpi\Api\HL\Controller\DropdownController extends AbstractController |
| [src/Glpi/Api/HL/Controller/GraphQLController.php](../src/Glpi/Api/HL/Controller/GraphQLController.php) | .php | class Glpi\Api\HL\Controller\GraphQLController extends AbstractController |
| [src/Glpi/Api/HL/Controller/ITILController.php](../src/Glpi/Api/HL/Controller/ITILController.php) | .php | class Glpi\Api\HL\Controller\ITILController extends AbstractController |
| [src/Glpi/Api/HL/Controller/InventoryController.php](../src/Glpi/Api/HL/Controller/InventoryController.php) | .php | class Glpi\Api\HL\Controller\InventoryController extends AbstractController |
| [src/Glpi/Api/HL/Controller/KnowbaseController.php](../src/Glpi/Api/HL/Controller/KnowbaseController.php) | .php | class Glpi\Api\HL\Controller\KnowbaseController extends AbstractController |
| [src/Glpi/Api/HL/Controller/ManagementController.php](../src/Glpi/Api/HL/Controller/ManagementController.php) | .php | class Glpi\Api\HL\Controller\ManagementController extends AbstractController |
| [src/Glpi/Api/HL/Controller/NotepadController.php](../src/Glpi/Api/HL/Controller/NotepadController.php) | .php | class Glpi\Api\HL\Controller\NotepadController extends AbstractController |
| [src/Glpi/Api/HL/Controller/NotificationController.php](../src/Glpi/Api/HL/Controller/NotificationController.php) | .php | class Glpi\Api\HL\Controller\NotificationController extends AbstractController |
| [src/Glpi/Api/HL/Controller/ProjectController.php](../src/Glpi/Api/HL/Controller/ProjectController.php) | .php | class Glpi\Api\HL\Controller\ProjectController extends AbstractController |
| [src/Glpi/Api/HL/Controller/ReportController.php](../src/Glpi/Api/HL/Controller/ReportController.php) | .php | class Glpi\Api\HL\Controller\ReportController extends AbstractController |
| [src/Glpi/Api/HL/Controller/RuleController.php](../src/Glpi/Api/HL/Controller/RuleController.php) | .php | class Glpi\Api\HL\Controller\RuleController extends AbstractController |
| [src/Glpi/Api/HL/Controller/SecurityController.php](../src/Glpi/Api/HL/Controller/SecurityController.php) | .php | class Glpi\Api\HL\Controller\SecurityController extends AbstractController |
| [src/Glpi/Api/HL/Controller/SetupController.php](../src/Glpi/Api/HL/Controller/SetupController.php) | .php | class Glpi\Api\HL\Controller\SetupController extends AbstractController |
| [src/Glpi/Api/HL/Controller/ToolController.php](../src/Glpi/Api/HL/Controller/ToolController.php) | .php | class Glpi\Api\HL\Controller\ToolController extends AbstractController |
| [src/Glpi/Api/HL/Doc/CreateRoute.php](../src/Glpi/Api/HL/Doc/CreateRoute.php) | .php | class Glpi\Api\HL\Doc\CreateRoute extends Route |
| [src/Glpi/Api/HL/Doc/DeleteRoute.php](../src/Glpi/Api/HL/Doc/DeleteRoute.php) | .php | class Glpi\Api\HL\Doc\DeleteRoute extends Route |
| [src/Glpi/Api/HL/Doc/GetRoute.php](../src/Glpi/Api/HL/Doc/GetRoute.php) | .php | class Glpi\Api\HL\Doc\GetRoute extends Route |
| [src/Glpi/Api/HL/Doc/Parameter.php](../src/Glpi/Api/HL/Doc/Parameter.php) | .php | class Glpi\Api\HL\Doc\Parameter |
| [src/Glpi/Api/HL/Doc/ParameterReference.php](../src/Glpi/Api/HL/Doc/ParameterReference.php) | .php | class Glpi\Api\HL\Doc\ParameterReference extends Parameter |
| [src/Glpi/Api/HL/Doc/Response.php](../src/Glpi/Api/HL/Doc/Response.php) | .php | class Glpi\Api\HL\Doc\Response |
| [src/Glpi/Api/HL/Doc/Route.php](../src/Glpi/Api/HL/Doc/Route.php) | .php | class Glpi\Api\HL\Doc\Route |
| [src/Glpi/Api/HL/Doc/Schema.php](../src/Glpi/Api/HL/Doc/Schema.php) | .php | class Glpi\Api\HL\Doc\Schema |
| [src/Glpi/Api/HL/Doc/SchemaReference.php](../src/Glpi/Api/HL/Doc/SchemaReference.php) | .php | class Glpi\Api\HL\Doc\SchemaReference |
| [src/Glpi/Api/HL/Doc/SearchRoute.php](../src/Glpi/Api/HL/Doc/SearchRoute.php) | .php | class Glpi\Api\HL\Doc\SearchRoute extends Route |
| [src/Glpi/Api/HL/Doc/UpdateRoute.php](../src/Glpi/Api/HL/Doc/UpdateRoute.php) | .php | class Glpi\Api\HL\Doc\UpdateRoute extends Route |
| [src/Glpi/Api/HL/GraphQL.php](../src/Glpi/Api/HL/GraphQL.php) | .php | class Glpi\Api\HL\GraphQL |
| [src/Glpi/Api/HL/GraphQL/CachedObject.php](../src/Glpi/Api/HL/GraphQL/CachedObject.php) | .php | class Glpi\Api\HL\GraphQL\CachedObject |
| [src/Glpi/Api/HL/GraphQL/DefaultResolvers.php](../src/Glpi/Api/HL/GraphQL/DefaultResolvers.php) | .php | class Glpi\Api\HL\GraphQL\DefaultResolvers |
| [src/Glpi/Api/HL/GraphQL/Error/FieldAccessDeniedError.php](../src/Glpi/Api/HL/GraphQL/Error/FieldAccessDeniedError.php) | .php | class Glpi\Api\HL\GraphQL\Error\FieldAccessDeniedError extends Error |
| [src/Glpi/Api/HL/GraphQL/ObjectCache.php](../src/Glpi/Api/HL/GraphQL/ObjectCache.php) | .php | class Glpi\Api\HL\GraphQL\ObjectCache |
| [src/Glpi/Api/HL/GraphQL/SchemaGenerator.php](../src/Glpi/Api/HL/GraphQL/SchemaGenerator.php) | .php | class Glpi\Api\HL\GraphQL\SchemaGenerator |
| [src/Glpi/Api/HL/GraphQL/Type/DateTimeType.php](../src/Glpi/Api/HL/GraphQL/Type/DateTimeType.php) | .php | class Glpi\Api\HL\GraphQL\Type\DateTimeType extends StringType |
| [src/Glpi/Api/HL/GraphQL/Types.php](../src/Glpi/Api/HL/GraphQL/Types.php) | .php | class Glpi\Api\HL\GraphQL\Types |
| [src/Glpi/Api/HL/Middleware/AbstractMiddleware.php](../src/Glpi/Api/HL/Middleware/AbstractMiddleware.php) | .php | class Glpi\Api\HL\Middleware\AbstractMiddleware |
| [src/Glpi/Api/HL/Middleware/AuthMiddlewareInterface.php](../src/Glpi/Api/HL/Middleware/AuthMiddlewareInterface.php) | .php | interface Glpi\Api\HL\Middleware\AuthMiddlewareInterface |
| [src/Glpi/Api/HL/Middleware/CRUDRequestMiddleware.php](../src/Glpi/Api/HL/Middleware/CRUDRequestMiddleware.php) | .php | class Glpi\Api\HL\Middleware\CRUDRequestMiddleware extends AbstractMiddleware |
| [src/Glpi/Api/HL/Middleware/CookieAuthMiddleware.php](../src/Glpi/Api/HL/Middleware/CookieAuthMiddleware.php) | .php | class Glpi\Api\HL\Middleware\CookieAuthMiddleware extends AbstractMiddleware |
| [src/Glpi/Api/HL/Middleware/DebugRequestMiddleware.php](../src/Glpi/Api/HL/Middleware/DebugRequestMiddleware.php) | .php | class Glpi\Api\HL\Middleware\DebugRequestMiddleware extends AbstractMiddleware |
| [src/Glpi/Api/HL/Middleware/DebugResponseMiddleware.php](../src/Glpi/Api/HL/Middleware/DebugResponseMiddleware.php) | .php | class Glpi\Api\HL\Middleware\DebugResponseMiddleware extends AbstractMiddleware |
| [src/Glpi/Api/HL/Middleware/IPRestrictionRequestMiddleware.php](../src/Glpi/Api/HL/Middleware/IPRestrictionRequestMiddleware.php) | .php | class Glpi\Api\HL\Middleware\IPRestrictionRequestMiddleware extends AbstractMiddleware |
| [src/Glpi/Api/HL/Middleware/InternalAuthMiddleware.php](../src/Glpi/Api/HL/Middleware/InternalAuthMiddleware.php) | .php | class Glpi\Api\HL\Middleware\InternalAuthMiddleware extends AbstractMiddleware |
| [src/Glpi/Api/HL/Middleware/MiddlewareInput.php](../src/Glpi/Api/HL/Middleware/MiddlewareInput.php) | .php | class Glpi\Api\HL\Middleware\MiddlewareInput |
| [src/Glpi/Api/HL/Middleware/OAuthRequestMiddleware.php](../src/Glpi/Api/HL/Middleware/OAuthRequestMiddleware.php) | .php | class Glpi\Api\HL\Middleware\OAuthRequestMiddleware extends AbstractMiddleware |
| [src/Glpi/Api/HL/Middleware/RSQLRequestMiddleware.php](../src/Glpi/Api/HL/Middleware/RSQLRequestMiddleware.php) | .php | class Glpi\Api\HL\Middleware\RSQLRequestMiddleware extends AbstractMiddleware |
| [src/Glpi/Api/HL/Middleware/RequestMiddlewareInterface.php](../src/Glpi/Api/HL/Middleware/RequestMiddlewareInterface.php) | .php | interface Glpi\Api\HL\Middleware\RequestMiddlewareInterface |
| [src/Glpi/Api/HL/Middleware/ResponseMiddlewareInterface.php](../src/Glpi/Api/HL/Middleware/ResponseMiddlewareInterface.php) | .php | interface Glpi\Api\HL\Middleware\ResponseMiddlewareInterface |
| [src/Glpi/Api/HL/Middleware/ResultFormatterMiddleware.php](../src/Glpi/Api/HL/Middleware/ResultFormatterMiddleware.php) | .php | class Glpi\Api\HL\Middleware\ResultFormatterMiddleware extends AbstractMiddleware |
| [src/Glpi/Api/HL/Middleware/SecurityResponseMiddleware.php](../src/Glpi/Api/HL/Middleware/SecurityResponseMiddleware.php) | .php | class Glpi\Api\HL\Middleware\SecurityResponseMiddleware extends AbstractMiddleware |
| [src/Glpi/Api/HL/OpenAPIGenerator.php](../src/Glpi/Api/HL/OpenAPIGenerator.php) | .php | class Glpi\Api\HL\OpenAPIGenerator |
| [src/Glpi/Api/HL/RSQL/Error.php](../src/Glpi/Api/HL/RSQL/Error.php) | .php | enum Glpi\Api\HL\RSQL\Error |
| [src/Glpi/Api/HL/RSQL/Lexer.php](../src/Glpi/Api/HL/RSQL/Lexer.php) | .php | class Glpi\Api\HL\RSQL\Lexer |
| [src/Glpi/Api/HL/RSQL/Parser.php](../src/Glpi/Api/HL/RSQL/Parser.php) | .php | class Glpi\Api\HL\RSQL\Parser |
| [src/Glpi/Api/HL/RSQL/RSQLException.php](../src/Glpi/Api/HL/RSQL/RSQLException.php) | .php | class Glpi\Api\HL\RSQL\RSQLException extends APIException |
| [src/Glpi/Api/HL/RSQL/Result.php](../src/Glpi/Api/HL/RSQL/Result.php) | .php | class Glpi\Api\HL\RSQL\Result |
| [src/Glpi/Api/HL/ResourceAccessor.php](../src/Glpi/Api/HL/ResourceAccessor.php) | .php | class Glpi\Api\HL\ResourceAccessor |
| [src/Glpi/Api/HL/RightConditionNotMetException.php](../src/Glpi/Api/HL/RightConditionNotMetException.php) | .php | class Glpi\Api\HL\RightConditionNotMetException extends APIException |
| [src/Glpi/Api/HL/Route.php](../src/Glpi/Api/HL/Route.php) | .php | class Glpi\Api\HL\Route |
| [src/Glpi/Api/HL/RoutePath.php](../src/Glpi/Api/HL/RoutePath.php) | .php | class Glpi\Api\HL\RoutePath |
| [src/Glpi/Api/HL/RouteVersion.php](../src/Glpi/Api/HL/RouteVersion.php) | .php | class Glpi\Api\HL\RouteVersion |
| [src/Glpi/Api/HL/Router.php](../src/Glpi/Api/HL/Router.php) | .php | class Glpi\Api\HL\Router |
| [src/Glpi/Api/HL/Schemas.php](../src/Glpi/Api/HL/Schemas.php) | .php | class Glpi\Api\HL\Schemas |
| [src/Glpi/Api/HL/Search.php](../src/Glpi/Api/HL/Search.php) | .php | class Glpi\Api\HL\Search |
| [src/Glpi/Api/HL/Search/CursorPagination.php](../src/Glpi/Api/HL/Search/CursorPagination.php) | .php | class Glpi\Api\HL\Search\CursorPagination |
| [src/Glpi/Api/HL/Search/RecordSet.php](../src/Glpi/Api/HL/Search/RecordSet.php) | .php | class Glpi\Api\HL\Search\RecordSet |
| [src/Glpi/Api/HL/Search/SearchContext.php](../src/Glpi/Api/HL/Search/SearchContext.php) | .php | class Glpi\Api\HL\Search\SearchContext |
| [src/Glpi/Api/HL/StreamedResponseWrapper.php](../src/Glpi/Api/HL/StreamedResponseWrapper.php) | .php | class Glpi\Api\HL\StreamedResponseWrapper extends Response |
| [src/Glpi/Application/Environment.php](../src/Glpi/Application/Environment.php) | .php | enum Glpi\Application\Environment |
| [src/Glpi/Application/ImportMapGenerator.php](../src/Glpi/Application/ImportMapGenerator.php) | .php | class Glpi\Application\ImportMapGenerator |
| [src/Glpi/Application/ResourcesChecker.php](../src/Glpi/Application/ResourcesChecker.php) | .php | class Glpi\Application\ResourcesChecker |
| [src/Glpi/Application/SystemConfigurator.php](../src/Glpi/Application/SystemConfigurator.php) | .php | class Glpi\Application\SystemConfigurator |
| [src/Glpi/Application/View/Extension/ConfigExtension.php](../src/Glpi/Application/View/Extension/ConfigExtension.php) | .php | class Glpi\Application\View\Extension\ConfigExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/DataHelpersExtension.php](../src/Glpi/Application/View/Extension/DataHelpersExtension.php) | .php | class Glpi\Application\View\Extension\DataHelpersExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/DocumentExtension.php](../src/Glpi/Application/View/Extension/DocumentExtension.php) | .php | class Glpi\Application\View\Extension\DocumentExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/FrontEndAssetsExtension.php](../src/Glpi/Application/View/Extension/FrontEndAssetsExtension.php) | .php | class Glpi\Application\View\Extension\FrontEndAssetsExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/HtmlExtension.php](../src/Glpi/Application/View/Extension/HtmlExtension.php) | .php | class Glpi\Application\View\Extension\HtmlExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/I18nExtension.php](../src/Glpi/Application/View/Extension/I18nExtension.php) | .php | class Glpi\Application\View\Extension\I18nExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/IllustrationExtension.php](../src/Glpi/Application/View/Extension/IllustrationExtension.php) | .php | class Glpi\Application\View\Extension\IllustrationExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/ItemtypeExtension.php](../src/Glpi/Application/View/Extension/ItemtypeExtension.php) | .php | class Glpi\Application\View\Extension\ItemtypeExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/PhpExtension.php](../src/Glpi/Application/View/Extension/PhpExtension.php) | .php | class Glpi\Application\View\Extension\PhpExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/PluginExtension.php](../src/Glpi/Application/View/Extension/PluginExtension.php) | .php | class Glpi\Application\View\Extension\PluginExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/RoutingExtension.php](../src/Glpi/Application/View/Extension/RoutingExtension.php) | .php | class Glpi\Application\View\Extension\RoutingExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/SearchExtension.php](../src/Glpi/Application/View/Extension/SearchExtension.php) | .php | class Glpi\Application\View\Extension\SearchExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/SecurityExtension.php](../src/Glpi/Application/View/Extension/SecurityExtension.php) | .php | class Glpi\Application\View\Extension\SecurityExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/SessionExtension.php](../src/Glpi/Application/View/Extension/SessionExtension.php) | .php | class Glpi\Application\View\Extension\SessionExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/SuperGlobalsExtension.php](../src/Glpi/Application/View/Extension/SuperGlobalsExtension.php) | .php | class Glpi\Application\View\Extension\SuperGlobalsExtension extends AbstractExtension |
| [src/Glpi/Application/View/Extension/TeamExtension.php](../src/Glpi/Application/View/Extension/TeamExtension.php) | .php | class Glpi\Application\View\Extension\TeamExtension extends AbstractExtension |
| [src/Glpi/Application/View/TemplateRenderer.php](../src/Glpi/Application/View/TemplateRenderer.php) | .php | class Glpi\Application\View\TemplateRenderer |
| [src/Glpi/Asset/Asset.php](../src/Glpi/Asset/Asset.php) | .php | class Glpi\Asset\Asset extends CommonDBTM |
| [src/Glpi/Asset/AssetDefinition.php](../src/Glpi/Asset/AssetDefinition.php) | .php | class Glpi\Asset\AssetDefinition extends AbstractDefinition |
| [src/Glpi/Asset/AssetDefinitionManager.php](../src/Glpi/Asset/AssetDefinitionManager.php) | .php | class Glpi\Asset\AssetDefinitionManager extends AbstractDefinitionManager |
| [src/Glpi/Asset/AssetModel.php](../src/Glpi/Asset/AssetModel.php) | .php | class Glpi\Asset\AssetModel extends CommonDCModelDropdown |
| [src/Glpi/Asset/AssetType.php](../src/Glpi/Asset/AssetType.php) | .php | class Glpi\Asset\AssetType extends CommonType |
| [src/Glpi/Asset/Asset_PeripheralAsset.php](../src/Glpi/Asset/Asset_PeripheralAsset.php) | .php | class Glpi\Asset\Asset_PeripheralAsset extends CommonDBRelation |
| [src/Glpi/Asset/Capacity.php](../src/Glpi/Asset/Capacity.php) | .php | class Glpi\Asset\Capacity |
| [src/Glpi/Asset/Capacity/AbstractCapacity.php](../src/Glpi/Asset/Capacity/AbstractCapacity.php) | .php | class Glpi\Asset\Capacity\AbstractCapacity |
| [src/Glpi/Asset/Capacity/AllowedInGlobalSearchCapacity.php](../src/Glpi/Asset/Capacity/AllowedInGlobalSearchCapacity.php) | .php | class Glpi\Asset\Capacity\AllowedInGlobalSearchCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/CapacityInterface.php](../src/Glpi/Asset/Capacity/CapacityInterface.php) | .php | interface Glpi\Asset\Capacity\CapacityInterface |
| [src/Glpi/Asset/Capacity/HasAntivirusCapacity.php](../src/Glpi/Asset/Capacity/HasAntivirusCapacity.php) | .php | class Glpi\Asset\Capacity\HasAntivirusCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasAppliancesCapacity.php](../src/Glpi/Asset/Capacity/HasAppliancesCapacity.php) | .php | class Glpi\Asset\Capacity\HasAppliancesCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasCertificatesCapacity.php](../src/Glpi/Asset/Capacity/HasCertificatesCapacity.php) | .php | class Glpi\Asset\Capacity\HasCertificatesCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasContractsCapacity.php](../src/Glpi/Asset/Capacity/HasContractsCapacity.php) | .php | class Glpi\Asset\Capacity\HasContractsCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasDatabaseInstanceCapacity.php](../src/Glpi/Asset/Capacity/HasDatabaseInstanceCapacity.php) | .php | class Glpi\Asset\Capacity\HasDatabaseInstanceCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasDevicesCapacity.php](../src/Glpi/Asset/Capacity/HasDevicesCapacity.php) | .php | class Glpi\Asset\Capacity\HasDevicesCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasDocumentsCapacity.php](../src/Glpi/Asset/Capacity/HasDocumentsCapacity.php) | .php | class Glpi\Asset\Capacity\HasDocumentsCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasDomainsCapacity.php](../src/Glpi/Asset/Capacity/HasDomainsCapacity.php) | .php | class Glpi\Asset\Capacity\HasDomainsCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasHistoryCapacity.php](../src/Glpi/Asset/Capacity/HasHistoryCapacity.php) | .php | class Glpi\Asset\Capacity\HasHistoryCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasImpactCapacity.php](../src/Glpi/Asset/Capacity/HasImpactCapacity.php) | .php | class Glpi\Asset\Capacity\HasImpactCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasInfocomCapacity.php](../src/Glpi/Asset/Capacity/HasInfocomCapacity.php) | .php | class Glpi\Asset\Capacity\HasInfocomCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasKnowbaseCapacity.php](../src/Glpi/Asset/Capacity/HasKnowbaseCapacity.php) | .php | class Glpi\Asset\Capacity\HasKnowbaseCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasLinksCapacity.php](../src/Glpi/Asset/Capacity/HasLinksCapacity.php) | .php | class Glpi\Asset\Capacity\HasLinksCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasNetworkPortCapacity.php](../src/Glpi/Asset/Capacity/HasNetworkPortCapacity.php) | .php | class Glpi\Asset\Capacity\HasNetworkPortCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasNotepadCapacity.php](../src/Glpi/Asset/Capacity/HasNotepadCapacity.php) | .php | class Glpi\Asset\Capacity\HasNotepadCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasOperatingSystemCapacity.php](../src/Glpi/Asset/Capacity/HasOperatingSystemCapacity.php) | .php | class Glpi\Asset\Capacity\HasOperatingSystemCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasPeripheralAssetsCapacity.php](../src/Glpi/Asset/Capacity/HasPeripheralAssetsCapacity.php) | .php | class Glpi\Asset\Capacity\HasPeripheralAssetsCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasPlugCapacity.php](../src/Glpi/Asset/Capacity/HasPlugCapacity.php) | .php | class Glpi\Asset\Capacity\HasPlugCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasRemoteManagementCapacity.php](../src/Glpi/Asset/Capacity/HasRemoteManagementCapacity.php) | .php | class Glpi\Asset\Capacity\HasRemoteManagementCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasSocketCapacity.php](../src/Glpi/Asset/Capacity/HasSocketCapacity.php) | .php | class Glpi\Asset\Capacity\HasSocketCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasSoftwaresCapacity.php](../src/Glpi/Asset/Capacity/HasSoftwaresCapacity.php) | .php | class Glpi\Asset\Capacity\HasSoftwaresCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasVirtualMachineCapacity.php](../src/Glpi/Asset/Capacity/HasVirtualMachineCapacity.php) | .php | class Glpi\Asset\Capacity\HasVirtualMachineCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/HasVolumesCapacity.php](../src/Glpi/Asset/Capacity/HasVolumesCapacity.php) | .php | class Glpi\Asset\Capacity\HasVolumesCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/IsInventoriableCapacity.php](../src/Glpi/Asset/Capacity/IsInventoriableCapacity.php) | .php | class Glpi\Asset\Capacity\IsInventoriableCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/IsProjectAssetCapacity.php](../src/Glpi/Asset/Capacity/IsProjectAssetCapacity.php) | .php | class Glpi\Asset\Capacity\IsProjectAssetCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/IsRackableCapacity.php](../src/Glpi/Asset/Capacity/IsRackableCapacity.php) | .php | class Glpi\Asset\Capacity\IsRackableCapacity extends AbstractCapacity |
| [src/Glpi/Asset/Capacity/IsReservableCapacity.php](../src/Glpi/Asset/Capacity/IsReservableCapacity.php) | .php | class Glpi\Asset\Capacity\IsReservableCapacity extends AbstractCapacity |
| [src/Glpi/Asset/CapacityConfig.php](../src/Glpi/Asset/CapacityConfig.php) | .php | class Glpi\Asset\CapacityConfig |
| [src/Glpi/Asset/CustomFieldDefinition.php](../src/Glpi/Asset/CustomFieldDefinition.php) | .php | class Glpi\Asset\CustomFieldDefinition extends CommonDBChild |
| [src/Glpi/Asset/CustomFieldOption/AbstractOption.php](../src/Glpi/Asset/CustomFieldOption/AbstractOption.php) | .php | class Glpi\Asset\CustomFieldOption\AbstractOption |
| [src/Glpi/Asset/CustomFieldOption/BooleanOption.php](../src/Glpi/Asset/CustomFieldOption/BooleanOption.php) | .php | class Glpi\Asset\CustomFieldOption\BooleanOption extends AbstractOption |
| [src/Glpi/Asset/CustomFieldOption/NumberOption.php](../src/Glpi/Asset/CustomFieldOption/NumberOption.php) | .php | class Glpi\Asset\CustomFieldOption\NumberOption extends AbstractOption |
| [src/Glpi/Asset/CustomFieldOption/OptionInterface.php](../src/Glpi/Asset/CustomFieldOption/OptionInterface.php) | .php | interface Glpi\Asset\CustomFieldOption\OptionInterface |
| [src/Glpi/Asset/CustomFieldOption/ProfileRestrictOption.php](../src/Glpi/Asset/CustomFieldOption/ProfileRestrictOption.php) | .php | class Glpi\Asset\CustomFieldOption\ProfileRestrictOption extends AbstractOption |
| [src/Glpi/Asset/CustomFieldType/AbstractType.php](../src/Glpi/Asset/CustomFieldType/AbstractType.php) | .php | class Glpi\Asset\CustomFieldType\AbstractType |
| [src/Glpi/Asset/CustomFieldType/BooleanType.php](../src/Glpi/Asset/CustomFieldType/BooleanType.php) | .php | class Glpi\Asset\CustomFieldType\BooleanType extends AbstractType |
| [src/Glpi/Asset/CustomFieldType/DateTimeType.php](../src/Glpi/Asset/CustomFieldType/DateTimeType.php) | .php | class Glpi\Asset\CustomFieldType\DateTimeType extends AbstractType |
| [src/Glpi/Asset/CustomFieldType/DateType.php](../src/Glpi/Asset/CustomFieldType/DateType.php) | .php | class Glpi\Asset\CustomFieldType\DateType extends AbstractType |
| [src/Glpi/Asset/CustomFieldType/DropdownType.php](../src/Glpi/Asset/CustomFieldType/DropdownType.php) | .php | class Glpi\Asset\CustomFieldType\DropdownType extends AbstractType |
| [src/Glpi/Asset/CustomFieldType/NumberType.php](../src/Glpi/Asset/CustomFieldType/NumberType.php) | .php | class Glpi\Asset\CustomFieldType\NumberType extends AbstractType |
| [src/Glpi/Asset/CustomFieldType/RawType.php](../src/Glpi/Asset/CustomFieldType/RawType.php) | .php | class Glpi\Asset\CustomFieldType\RawType extends AbstractType |
| [src/Glpi/Asset/CustomFieldType/StringType.php](../src/Glpi/Asset/CustomFieldType/StringType.php) | .php | class Glpi\Asset\CustomFieldType\StringType extends AbstractType |
| [src/Glpi/Asset/CustomFieldType/TextType.php](../src/Glpi/Asset/CustomFieldType/TextType.php) | .php | class Glpi\Asset\CustomFieldType\TextType extends AbstractType |
| [src/Glpi/Asset/CustomFieldType/TypeInterface.php](../src/Glpi/Asset/CustomFieldType/TypeInterface.php) | .php | interface Glpi\Asset\CustomFieldType\TypeInterface |
| [src/Glpi/Asset/CustomFieldType/URLType.php](../src/Glpi/Asset/CustomFieldType/URLType.php) | .php | class Glpi\Asset\CustomFieldType\URLType extends StringType |
| [src/Glpi/Asset/RuleDictionaryModel.php](../src/Glpi/Asset/RuleDictionaryModel.php) | .php | class Glpi\Asset\RuleDictionaryModel extends RuleDictionnaryDropdown |
| [src/Glpi/Asset/RuleDictionaryModelCollection.php](../src/Glpi/Asset/RuleDictionaryModelCollection.php) | .php | class Glpi\Asset\RuleDictionaryModelCollection extends RuleDictionnaryDropdownCollection |
| [src/Glpi/Asset/RuleDictionaryType.php](../src/Glpi/Asset/RuleDictionaryType.php) | .php | class Glpi\Asset\RuleDictionaryType extends RuleDictionnaryDropdown |
| [src/Glpi/Asset/RuleDictionaryTypeCollection.php](../src/Glpi/Asset/RuleDictionaryTypeCollection.php) | .php | class Glpi\Asset\RuleDictionaryTypeCollection extends RuleDictionnaryDropdownCollection |
| [src/Glpi/Cache/CacheManager.php](../src/Glpi/Cache/CacheManager.php) | .php | class Glpi\Cache\CacheManager |
| [src/Glpi/Cache/I18nCache.php](../src/Glpi/Cache/I18nCache.php) | .php | class Glpi\Cache\I18nCache |
| [src/Glpi/Cache/SimpleCache.php](../src/Glpi/Cache/SimpleCache.php) | .php | class Glpi\Cache\SimpleCache extends Psr16Cache |
| [src/Glpi/CalDAV/Backend/Auth.php](../src/Glpi/CalDAV/Backend/Auth.php) | .php | class Glpi\CalDAV\Backend\Auth extends AbstractBasic |
| [src/Glpi/CalDAV/Backend/Calendar.php](../src/Glpi/CalDAV/Backend/Calendar.php) | .php | class Glpi\CalDAV\Backend\Calendar extends AbstractBackend |
| [src/Glpi/CalDAV/Backend/Principal.php](../src/Glpi/CalDAV/Backend/Principal.php) | .php | class Glpi\CalDAV\Backend\Principal extends AbstractBackend |
| [src/Glpi/CalDAV/Contracts/CalDAVCompatibleItemInterface.php](../src/Glpi/CalDAV/Contracts/CalDAVCompatibleItemInterface.php) | .php | interface Glpi\CalDAV\Contracts\CalDAVCompatibleItemInterface |
| [src/Glpi/CalDAV/Node/CalendarRoot.php](../src/Glpi/CalDAV/Node/CalendarRoot.php) | .php | class Glpi\CalDAV\Node\CalendarRoot extends \Sabre\CalDAV\CalendarRoot |
| [src/Glpi/CalDAV/Node/Property.php](../src/Glpi/CalDAV/Node/Property.php) | .php | class Glpi\CalDAV\Node\Property |
| [src/Glpi/CalDAV/Plugin/Acl.php](../src/Glpi/CalDAV/Plugin/Acl.php) | .php | class Glpi\CalDAV\Plugin\Acl extends Plugin |
| [src/Glpi/CalDAV/Plugin/Browser.php](../src/Glpi/CalDAV/Plugin/Browser.php) | .php | class Glpi\CalDAV\Plugin\Browser extends Plugin |
| [src/Glpi/CalDAV/Plugin/CalDAV.php](../src/Glpi/CalDAV/Plugin/CalDAV.php) | .php | class Glpi\CalDAV\Plugin\CalDAV extends Plugin |
| [src/Glpi/CalDAV/Server.php](../src/Glpi/CalDAV/Server.php) | .php | class Glpi\CalDAV\Server extends DAV\Server |
| [src/Glpi/CalDAV/Traits/CalDAVPrincipalsTrait.php](../src/Glpi/CalDAV/Traits/CalDAVPrincipalsTrait.php) | .php | trait Glpi\CalDAV\Traits\CalDAVPrincipalsTrait |
| [src/Glpi/CalDAV/Traits/CalDAVUriUtilTrait.php](../src/Glpi/CalDAV/Traits/CalDAVUriUtilTrait.php) | .php | trait Glpi\CalDAV\Traits\CalDAVUriUtilTrait |
| [src/Glpi/CalDAV/Traits/VobjectConverterTrait.php](../src/Glpi/CalDAV/Traits/VobjectConverterTrait.php) | .php | trait Glpi\CalDAV\Traits\VobjectConverterTrait |
| [src/Glpi/Config/ConfigContainer.php](../src/Glpi/Config/ConfigContainer.php) | .php | class Glpi\Config\ConfigContainer |
| [src/Glpi/Config/DataAndPrivacyConfig.php](../src/Glpi/Config/DataAndPrivacyConfig.php) | .php | class Glpi\Config\DataAndPrivacyConfig extends Config |
| [src/Glpi/Config/ProxyExclusion.php](../src/Glpi/Config/ProxyExclusion.php) | .php | class Glpi\Config\ProxyExclusion |
| [src/Glpi/Config/ProxyExclusions.php](../src/Glpi/Config/ProxyExclusions.php) | .php | class Glpi\Config\ProxyExclusions |
| [src/Glpi/Console/AbstractCommand.php](../src/Glpi/Console/AbstractCommand.php) | .php | class Glpi\Console\AbstractCommand extends Command |
| [src/Glpi/Console/Application.php](../src/Glpi/Console/Application.php) | .php | class Glpi\Console\Application extends BaseApplication |
| [src/Glpi/Console/Assets/CleanSoftwareCommand.php](../src/Glpi/Console/Assets/CleanSoftwareCommand.php) | .php | class Glpi\Console\Assets\CleanSoftwareCommand extends AbstractCommand |
| [src/Glpi/Console/Assets/PurgeSoftwareCommand.php](../src/Glpi/Console/Assets/PurgeSoftwareCommand.php) | .php | class Glpi\Console\Assets\PurgeSoftwareCommand extends AbstractCommand |
| [src/Glpi/Console/Build/CompileScssCommand.php](../src/Glpi/Console/Build/CompileScssCommand.php) | .php | class Glpi\Console\Build\CompileScssCommand extends Command |
| [src/Glpi/Console/Build/GenerateCodeManifestCommand.php](../src/Glpi/Console/Build/GenerateCodeManifestCommand.php) | .php | class Glpi\Console\Build\GenerateCodeManifestCommand extends Command |
| [src/Glpi/Console/Cache/ClearCommand.php](../src/Glpi/Console/Cache/ClearCommand.php) | .php | class Glpi\Console\Cache\ClearCommand extends Command |
| [src/Glpi/Console/Cache/ConfigureCommand.php](../src/Glpi/Console/Cache/ConfigureCommand.php) | .php | class Glpi\Console\Cache\ConfigureCommand extends AbstractCommand |
| [src/Glpi/Console/Cache/DebugCommand.php](../src/Glpi/Console/Cache/DebugCommand.php) | .php | class Glpi\Console\Cache\DebugCommand extends Command |
| [src/Glpi/Console/Cache/SetNamespacePrefixCommand.php](../src/Glpi/Console/Cache/SetNamespacePrefixCommand.php) | .php | class Glpi\Console\Cache\SetNamespacePrefixCommand extends AbstractCommand |
| [src/Glpi/Console/Command/ConfigurationCommandInterface.php](../src/Glpi/Console/Command/ConfigurationCommandInterface.php) | .php | interface Glpi\Console\Command\ConfigurationCommandInterface |
| [src/Glpi/Console/Command/GlpiCommandInterface.php](../src/Glpi/Console/Command/GlpiCommandInterface.php) | .php | interface Glpi\Console\Command\GlpiCommandInterface |
| [src/Glpi/Console/CommandLoader.php](../src/Glpi/Console/CommandLoader.php) | .php | class Glpi\Console\CommandLoader |
| [src/Glpi/Console/Config/SetCommand.php](../src/Glpi/Console/Config/SetCommand.php) | .php | class Glpi\Console\Config\SetCommand extends AbstractCommand |
| [src/Glpi/Console/Database/AbstractConfigureCommand.php](../src/Glpi/Console/Database/AbstractConfigureCommand.php) | .php | class Glpi\Console\Database\AbstractConfigureCommand extends AbstractCommand |
| [src/Glpi/Console/Database/CheckSchemaIntegrityCommand.php](../src/Glpi/Console/Database/CheckSchemaIntegrityCommand.php) | .php | class Glpi\Console\Database\CheckSchemaIntegrityCommand extends AbstractCommand |
| [src/Glpi/Console/Database/ConfigureCommand.php](../src/Glpi/Console/Database/ConfigureCommand.php) | .php | class Glpi\Console\Database\ConfigureCommand extends AbstractConfigureCommand |
| [src/Glpi/Console/Database/EnableTimezonesCommand.php](../src/Glpi/Console/Database/EnableTimezonesCommand.php) | .php | class Glpi\Console\Database\EnableTimezonesCommand extends AbstractCommand |
| [src/Glpi/Console/Database/InstallCommand.php](../src/Glpi/Console/Database/InstallCommand.php) | .php | class Glpi\Console\Database\InstallCommand extends AbstractConfigureCommand |
| [src/Glpi/Console/Database/IsUpToDateCommand.php](../src/Glpi/Console/Database/IsUpToDateCommand.php) | .php | class Glpi\Console\Database\IsUpToDateCommand extends AbstractCommand |
| [src/Glpi/Console/Database/UpdateCommand.php](../src/Glpi/Console/Database/UpdateCommand.php) | .php | class Glpi\Console\Database\UpdateCommand extends AbstractCommand |
| [src/Glpi/Console/Diagnostic/CheckDocumentsIntegrityCommand.php](../src/Glpi/Console/Diagnostic/CheckDocumentsIntegrityCommand.php) | .php | class Glpi\Console\Diagnostic\CheckDocumentsIntegrityCommand extends AbstractCommand |
| [src/Glpi/Console/Diagnostic/CheckOrphanedUserPicturesCommand.php](../src/Glpi/Console/Diagnostic/CheckOrphanedUserPicturesCommand.php) | .php | class Glpi\Console\Diagnostic\CheckOrphanedUserPicturesCommand extends AbstractCommand |
| [src/Glpi/Console/Diagnostic/CheckSourceCodeIntegrityCommand.php](../src/Glpi/Console/Diagnostic/CheckSourceCodeIntegrityCommand.php) | .php | class Glpi\Console\Diagnostic\CheckSourceCodeIntegrityCommand extends AbstractCommand |
| [src/Glpi/Console/Exception/EarlyExitException.php](../src/Glpi/Console/Exception/EarlyExitException.php) | .php | class Glpi\Console\Exception\EarlyExitException extends Exception |
| [src/Glpi/Console/Ldap/SynchronizeUsersCommand.php](../src/Glpi/Console/Ldap/SynchronizeUsersCommand.php) | .php | class Glpi\Console\Ldap\SynchronizeUsersCommand extends AbstractCommand |
| [src/Glpi/Console/Maintenance/DisableMaintenanceModeCommand.php](../src/Glpi/Console/Maintenance/DisableMaintenanceModeCommand.php) | .php | class Glpi\Console\Maintenance\DisableMaintenanceModeCommand extends AbstractCommand |
| [src/Glpi/Console/Maintenance/EnableMaintenanceModeCommand.php](../src/Glpi/Console/Maintenance/EnableMaintenanceModeCommand.php) | .php | class Glpi\Console\Maintenance\EnableMaintenanceModeCommand extends AbstractCommand |
| [src/Glpi/Console/Marketplace/AbstractMarketplaceCommand.php](../src/Glpi/Console/Marketplace/AbstractMarketplaceCommand.php) | .php | class Glpi\Console\Marketplace\AbstractMarketplaceCommand extends AbstractCommand |
| [src/Glpi/Console/Marketplace/DownloadCommand.php](../src/Glpi/Console/Marketplace/DownloadCommand.php) | .php | class Glpi\Console\Marketplace\DownloadCommand extends AbstractMarketplaceCommand |
| [src/Glpi/Console/Marketplace/InfoCommand.php](../src/Glpi/Console/Marketplace/InfoCommand.php) | .php | class Glpi\Console\Marketplace\InfoCommand extends AbstractMarketplaceCommand |
| [src/Glpi/Console/Marketplace/SearchCommand.php](../src/Glpi/Console/Marketplace/SearchCommand.php) | .php | class Glpi\Console\Marketplace\SearchCommand extends AbstractCommand |
| [src/Glpi/Console/Marketplace/UpgradeCommand.php](../src/Glpi/Console/Marketplace/UpgradeCommand.php) | .php | class Glpi\Console\Marketplace\UpgradeCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/AbstractPluginMigrationCommand.php](../src/Glpi/Console/Migration/AbstractPluginMigrationCommand.php) | .php | class Glpi\Console\Migration\AbstractPluginMigrationCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/AbstractPluginToCoreCommand.php](../src/Glpi/Console/Migration/AbstractPluginToCoreCommand.php) | .php | class Glpi\Console\Migration\AbstractPluginToCoreCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/AppliancesPluginToCoreCommand.php](../src/Glpi/Console/Migration/AppliancesPluginToCoreCommand.php) | .php | class Glpi\Console\Migration\AppliancesPluginToCoreCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/BuildMissingTimestampsCommand.php](../src/Glpi/Console/Migration/BuildMissingTimestampsCommand.php) | .php | class Glpi\Console\Migration\BuildMissingTimestampsCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/ComputeDocumentsSizeCommand.php](../src/Glpi/Console/Migration/ComputeDocumentsSizeCommand.php) | .php | class Glpi\Console\Migration\ComputeDocumentsSizeCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/DatabasesPluginToCoreCommand.php](../src/Glpi/Console/Migration/DatabasesPluginToCoreCommand.php) | .php | class Glpi\Console\Migration\DatabasesPluginToCoreCommand extends AbstractPluginToCoreCommand |
| [src/Glpi/Console/Migration/DomainsPluginToCoreCommand.php](../src/Glpi/Console/Migration/DomainsPluginToCoreCommand.php) | .php | class Glpi\Console\Migration\DomainsPluginToCoreCommand extends AbstractPluginToCoreCommand |
| [src/Glpi/Console/Migration/DynamicRowFormatCommand.php](../src/Glpi/Console/Migration/DynamicRowFormatCommand.php) | .php | class Glpi\Console\Migration\DynamicRowFormatCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/FormCreatorPluginToCoreCommand.php](../src/Glpi/Console/Migration/FormCreatorPluginToCoreCommand.php) | .php | class Glpi\Console\Migration\FormCreatorPluginToCoreCommand extends AbstractPluginMigrationCommand |
| [src/Glpi/Console/Migration/GenericobjectPluginToCoreCommand.php](../src/Glpi/Console/Migration/GenericobjectPluginToCoreCommand.php) | .php | class Glpi\Console\Migration\GenericobjectPluginToCoreCommand extends AbstractPluginMigrationCommand |
| [src/Glpi/Console/Migration/MigrateAllCommand.php](../src/Glpi/Console/Migration/MigrateAllCommand.php) | .php | class Glpi\Console\Migration\MigrateAllCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/MyIsamToInnoDbCommand.php](../src/Glpi/Console/Migration/MyIsamToInnoDbCommand.php) | .php | class Glpi\Console\Migration\MyIsamToInnoDbCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/RacksPluginToCoreCommand.php](../src/Glpi/Console/Migration/RacksPluginToCoreCommand.php) | .php | class Glpi\Console\Migration\RacksPluginToCoreCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/TimestampsCommand.php](../src/Glpi/Console/Migration/TimestampsCommand.php) | .php | class Glpi\Console\Migration\TimestampsCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/UnsignedKeysCommand.php](../src/Glpi/Console/Migration/UnsignedKeysCommand.php) | .php | class Glpi\Console\Migration\UnsignedKeysCommand extends AbstractCommand |
| [src/Glpi/Console/Migration/Utf8mb4Command.php](../src/Glpi/Console/Migration/Utf8mb4Command.php) | .php | class Glpi\Console\Migration\Utf8mb4Command extends AbstractCommand |
| [src/Glpi/Console/Plugin/AbstractPluginCommand.php](../src/Glpi/Console/Plugin/AbstractPluginCommand.php) | .php | class Glpi\Console\Plugin\AbstractPluginCommand extends AbstractCommand |
| [src/Glpi/Console/Plugin/ActivateCommand.php](../src/Glpi/Console/Plugin/ActivateCommand.php) | .php | class Glpi\Console\Plugin\ActivateCommand extends AbstractPluginCommand |
| [src/Glpi/Console/Plugin/DeactivateCommand.php](../src/Glpi/Console/Plugin/DeactivateCommand.php) | .php | class Glpi\Console\Plugin\DeactivateCommand extends AbstractPluginCommand |
| [src/Glpi/Console/Plugin/InstallCommand.php](../src/Glpi/Console/Plugin/InstallCommand.php) | .php | class Glpi\Console\Plugin\InstallCommand extends AbstractPluginCommand |
| [src/Glpi/Console/Plugin/ListCommand.php](../src/Glpi/Console/Plugin/ListCommand.php) | .php | class Glpi\Console\Plugin\ListCommand extends AbstractCommand |
| [src/Glpi/Console/Plugin/ResumeExecutionCommand.php](../src/Glpi/Console/Plugin/ResumeExecutionCommand.php) | .php | class Glpi\Console\Plugin\ResumeExecutionCommand extends AbstractCommand |
| [src/Glpi/Console/Plugin/SuspendExecutionCommand.php](../src/Glpi/Console/Plugin/SuspendExecutionCommand.php) | .php | class Glpi\Console\Plugin\SuspendExecutionCommand extends AbstractCommand |
| [src/Glpi/Console/Plugin/UninstallCommand.php](../src/Glpi/Console/Plugin/UninstallCommand.php) | .php | class Glpi\Console\Plugin\UninstallCommand extends AbstractPluginCommand |
| [src/Glpi/Console/Rules/ProcessSoftwareCategoryRulesCommand.php](../src/Glpi/Console/Rules/ProcessSoftwareCategoryRulesCommand.php) | .php | class Glpi\Console\Rules\ProcessSoftwareCategoryRulesCommand extends AbstractCommand |
| [src/Glpi/Console/Rules/ReplayDictionnaryRulesCommand.php](../src/Glpi/Console/Rules/ReplayDictionnaryRulesCommand.php) | .php | class Glpi\Console\Rules\ReplayDictionnaryRulesCommand extends AbstractCommand |
| [src/Glpi/Console/Security/ChangeOAuthKeyCommand.php](../src/Glpi/Console/Security/ChangeOAuthKeyCommand.php) | .php | class Glpi\Console\Security\ChangeOAuthKeyCommand extends AbstractCommand |
| [src/Glpi/Console/Security/ChangekeyCommand.php](../src/Glpi/Console/Security/ChangekeyCommand.php) | .php | class Glpi\Console\Security\ChangekeyCommand extends AbstractCommand |
| [src/Glpi/Console/Security/DisableTFACommand.php](../src/Glpi/Console/Security/DisableTFACommand.php) | .php | class Glpi\Console\Security\DisableTFACommand extends AbstractCommand |
| [src/Glpi/Console/Security/SessionListCommand.php](../src/Glpi/Console/Security/SessionListCommand.php) | .php | class Glpi\Console\Security\SessionListCommand extends AbstractCommand |
| [src/Glpi/Console/Security/SessionRevokeCommand.php](../src/Glpi/Console/Security/SessionRevokeCommand.php) | .php | class Glpi\Console\Security\SessionRevokeCommand extends AbstractCommand |
| [src/Glpi/Console/System/CheckRequirementsCommand.php](../src/Glpi/Console/System/CheckRequirementsCommand.php) | .php | class Glpi\Console\System\CheckRequirementsCommand extends AbstractCommand |
| [src/Glpi/Console/System/CheckStatusCommand.php](../src/Glpi/Console/System/CheckStatusCommand.php) | .php | class Glpi\Console\System\CheckStatusCommand extends AbstractCommand |
| [src/Glpi/Console/System/ListServicesCommand.php](../src/Glpi/Console/System/ListServicesCommand.php) | .php | class Glpi\Console\System\ListServicesCommand extends AbstractCommand |
| [src/Glpi/Console/Task/UnlockCommand.php](../src/Glpi/Console/Task/UnlockCommand.php) | .php | class Glpi\Console\Task\UnlockCommand extends AbstractCommand |
| [src/Glpi/Console/Traits/PluginMigrationTrait.php](../src/Glpi/Console/Traits/PluginMigrationTrait.php) | .php | trait Glpi\Console\Traits\PluginMigrationTrait |
| [src/Glpi/Console/Traits/TelemetryActivationTrait.php](../src/Glpi/Console/Traits/TelemetryActivationTrait.php) | .php | trait Glpi\Console\Traits\TelemetryActivationTrait |
| [src/Glpi/Console/User/AbstractUserCommand.php](../src/Glpi/Console/User/AbstractUserCommand.php) | .php | class Glpi\Console\User\AbstractUserCommand extends AbstractCommand |
| [src/Glpi/Console/User/CreateCommand.php](../src/Glpi/Console/User/CreateCommand.php) | .php | class Glpi\Console\User\CreateCommand extends AbstractUserCommand |
| [src/Glpi/Console/User/DeleteCommand.php](../src/Glpi/Console/User/DeleteCommand.php) | .php | class Glpi\Console\User\DeleteCommand extends AbstractUserCommand |
| [src/Glpi/Console/User/DisableCommand.php](../src/Glpi/Console/User/DisableCommand.php) | .php | class Glpi\Console\User\DisableCommand extends AbstractUserCommand |
| [src/Glpi/Console/User/EnableCommand.php](../src/Glpi/Console/User/EnableCommand.php) | .php | class Glpi\Console\User\EnableCommand extends AbstractUserCommand |
| [src/Glpi/Console/User/GrantCommand.php](../src/Glpi/Console/User/GrantCommand.php) | .php | class Glpi\Console\User\GrantCommand extends AbstractUserCommand |
| [src/Glpi/Console/User/ResetPasswordCommand.php](../src/Glpi/Console/User/ResetPasswordCommand.php) | .php | class Glpi\Console\User\ResetPasswordCommand extends AbstractUserCommand |
| [src/Glpi/ContentTemplates/Parameters/AbstractParameters.php](../src/Glpi/ContentTemplates/Parameters/AbstractParameters.php) | .php | class Glpi\ContentTemplates\Parameters\AbstractParameters |
| [src/Glpi/ContentTemplates/Parameters/AssetParameters.php](../src/Glpi/ContentTemplates/Parameters/AssetParameters.php) | .php | class Glpi\ContentTemplates\Parameters\AssetParameters extends AbstractParameters |
| [src/Glpi/ContentTemplates/Parameters/ChangeParameters.php](../src/Glpi/ContentTemplates/Parameters/ChangeParameters.php) | .php | class Glpi\ContentTemplates\Parameters\ChangeParameters extends CommonITILObjectParameters |
| [src/Glpi/ContentTemplates/Parameters/CommonITILObjectParameters.php](../src/Glpi/ContentTemplates/Parameters/CommonITILObjectParameters.php) | .php | class Glpi\ContentTemplates\Parameters\CommonITILObjectParameters extends AbstractParameters |
| [src/Glpi/ContentTemplates/Parameters/DropdownParameters.php](../src/Glpi/ContentTemplates/Parameters/DropdownParameters.php) | .php | class Glpi\ContentTemplates\Parameters\DropdownParameters extends AbstractParameters |
| [src/Glpi/ContentTemplates/Parameters/EntityParameters.php](../src/Glpi/ContentTemplates/Parameters/EntityParameters.php) | .php | class Glpi\ContentTemplates\Parameters\EntityParameters extends TreeDropdownParameters |
| [src/Glpi/ContentTemplates/Parameters/GroupParameters.php](../src/Glpi/ContentTemplates/Parameters/GroupParameters.php) | .php | class Glpi\ContentTemplates\Parameters\GroupParameters extends TreeDropdownParameters |
| [src/Glpi/ContentTemplates/Parameters/ITILCategoryParameters.php](../src/Glpi/ContentTemplates/Parameters/ITILCategoryParameters.php) | .php | class Glpi\ContentTemplates\Parameters\ITILCategoryParameters extends TreeDropdownParameters |
| [src/Glpi/ContentTemplates/Parameters/KnowbaseItemParameters.php](../src/Glpi/ContentTemplates/Parameters/KnowbaseItemParameters.php) | .php | class Glpi\ContentTemplates\Parameters\KnowbaseItemParameters extends AbstractParameters |
| [src/Glpi/ContentTemplates/Parameters/LevelAgreementParameters.php](../src/Glpi/ContentTemplates/Parameters/LevelAgreementParameters.php) | .php | class Glpi\ContentTemplates\Parameters\LevelAgreementParameters extends AbstractParameters |
| [src/Glpi/ContentTemplates/Parameters/LocationParameters.php](../src/Glpi/ContentTemplates/Parameters/LocationParameters.php) | .php | class Glpi\ContentTemplates\Parameters\LocationParameters extends TreeDropdownParameters |
| [src/Glpi/ContentTemplates/Parameters/OLAParameters.php](../src/Glpi/ContentTemplates/Parameters/OLAParameters.php) | .php | class Glpi\ContentTemplates\Parameters\OLAParameters extends LevelAgreementParameters |
| [src/Glpi/ContentTemplates/Parameters/ParametersTypes/AbstractParameterType.php](../src/Glpi/ContentTemplates/Parameters/ParametersTypes/AbstractParameterType.php) | .php | class Glpi\ContentTemplates\Parameters\ParametersTypes\AbstractParameterType |
| [src/Glpi/ContentTemplates/Parameters/ParametersTypes/ArrayParameter.php](../src/Glpi/ContentTemplates/Parameters/ParametersTypes/ArrayParameter.php) | .php | class Glpi\ContentTemplates\Parameters\ParametersTypes\ArrayParameter extends AbstractParameterType |
| [src/Glpi/ContentTemplates/Parameters/ParametersTypes/AttributeParameter.php](../src/Glpi/ContentTemplates/Parameters/ParametersTypes/AttributeParameter.php) | .php | class Glpi\ContentTemplates\Parameters\ParametersTypes\AttributeParameter extends AbstractParameterType |
| [src/Glpi/ContentTemplates/Parameters/ParametersTypes/ObjectParameter.php](../src/Glpi/ContentTemplates/Parameters/ParametersTypes/ObjectParameter.php) | .php | class Glpi\ContentTemplates\Parameters\ParametersTypes\ObjectParameter extends AbstractParameterType |
| [src/Glpi/ContentTemplates/Parameters/ParametersTypes/ParameterTypeInterface.php](../src/Glpi/ContentTemplates/Parameters/ParametersTypes/ParameterTypeInterface.php) | .php | interface Glpi\ContentTemplates\Parameters\ParametersTypes\ParameterTypeInterface |
| [src/Glpi/ContentTemplates/Parameters/ProblemParameters.php](../src/Glpi/ContentTemplates/Parameters/ProblemParameters.php) | .php | class Glpi\ContentTemplates\Parameters\ProblemParameters extends CommonITILObjectParameters |
| [src/Glpi/ContentTemplates/Parameters/RequestTypeParameters.php](../src/Glpi/ContentTemplates/Parameters/RequestTypeParameters.php) | .php | class Glpi\ContentTemplates\Parameters\RequestTypeParameters extends DropdownParameters |
| [src/Glpi/ContentTemplates/Parameters/SLAParameters.php](../src/Glpi/ContentTemplates/Parameters/SLAParameters.php) | .php | class Glpi\ContentTemplates\Parameters\SLAParameters extends LevelAgreementParameters |
| [src/Glpi/ContentTemplates/Parameters/SupplierParameters.php](../src/Glpi/ContentTemplates/Parameters/SupplierParameters.php) | .php | class Glpi\ContentTemplates\Parameters\SupplierParameters extends TreeDropdownParameters |
| [src/Glpi/ContentTemplates/Parameters/TemplatesParametersInterface.php](../src/Glpi/ContentTemplates/Parameters/TemplatesParametersInterface.php) | .php | interface Glpi\ContentTemplates\Parameters\TemplatesParametersInterface |
| [src/Glpi/ContentTemplates/Parameters/TicketParameters.php](../src/Glpi/ContentTemplates/Parameters/TicketParameters.php) | .php | class Glpi\ContentTemplates\Parameters\TicketParameters extends CommonITILObjectParameters |
| [src/Glpi/ContentTemplates/Parameters/TreeDropdownParameters.php](../src/Glpi/ContentTemplates/Parameters/TreeDropdownParameters.php) | .php | class Glpi\ContentTemplates\Parameters\TreeDropdownParameters extends DropdownParameters |
| [src/Glpi/ContentTemplates/Parameters/UserCategoryParameters.php](../src/Glpi/ContentTemplates/Parameters/UserCategoryParameters.php) | .php | class Glpi\ContentTemplates\Parameters\UserCategoryParameters extends DropdownParameters |
| [src/Glpi/ContentTemplates/Parameters/UserParameters.php](../src/Glpi/ContentTemplates/Parameters/UserParameters.php) | .php | class Glpi\ContentTemplates\Parameters\UserParameters extends AbstractParameters |
| [src/Glpi/ContentTemplates/Parameters/UserTitleParameters.php](../src/Glpi/ContentTemplates/Parameters/UserTitleParameters.php) | .php | class Glpi\ContentTemplates\Parameters\UserTitleParameters extends DropdownParameters |
| [src/Glpi/ContentTemplates/ParametersPreset.php](../src/Glpi/ContentTemplates/ParametersPreset.php) | .php | class Glpi\ContentTemplates\ParametersPreset |
| [src/Glpi/ContentTemplates/TemplateDocumentation.php](../src/Glpi/ContentTemplates/TemplateDocumentation.php) | .php | class Glpi\ContentTemplates\TemplateDocumentation |
| [src/Glpi/ContentTemplates/TemplateManager.php](../src/Glpi/ContentTemplates/TemplateManager.php) | .php | class Glpi\ContentTemplates\TemplateManager |
| [src/Glpi/Controller/AbstractController.php](../src/Glpi/Controller/AbstractController.php) | .php | class Glpi\Controller\AbstractController |
| [src/Glpi/Controller/AbstractDocumentUploadController.php](../src/Glpi/Controller/AbstractDocumentUploadController.php) | .php | class Glpi\Controller\AbstractDocumentUploadController extends AbstractController |
| [src/Glpi/Controller/Altcha/ChallengeController.php](../src/Glpi/Controller/Altcha/ChallengeController.php) | .php | class Glpi\Controller\Altcha\ChallengeController extends AbstractController |
| [src/Glpi/Controller/ApiController.php](../src/Glpi/Controller/ApiController.php) | .php | class Glpi\Controller\ApiController extends AbstractController |
| [src/Glpi/Controller/ApiRestController.php](../src/Glpi/Controller/ApiRestController.php) | .php | class Glpi\Controller\ApiRestController extends AbstractController |
| [src/Glpi/Controller/CaldavController.php](../src/Glpi/Controller/CaldavController.php) | .php | class Glpi\Controller\CaldavController extends AbstractController |
| [src/Glpi/Controller/CentralController.php](../src/Glpi/Controller/CentralController.php) | .php | class Glpi\Controller\CentralController extends AbstractController |
| [src/Glpi/Controller/Config/DataAndPrivacyConfigController.php](../src/Glpi/Controller/Config/DataAndPrivacyConfigController.php) | .php | class Glpi\Controller\Config\DataAndPrivacyConfigController extends AbstractController |
| [src/Glpi/Controller/Config/Helpdesk/AbstractTileController.php](../src/Glpi/Controller/Config/Helpdesk/AbstractTileController.php) | .php | class Glpi\Controller\Config\Helpdesk\AbstractTileController extends AbstractController |
| [src/Glpi/Controller/Config/Helpdesk/AddTileController.php](../src/Glpi/Controller/Config/Helpdesk/AddTileController.php) | .php | class Glpi\Controller\Config\Helpdesk\AddTileController extends AbstractTileController |
| [src/Glpi/Controller/Config/Helpdesk/CopyParentEntityController.php](../src/Glpi/Controller/Config/Helpdesk/CopyParentEntityController.php) | .php | class Glpi\Controller\Config\Helpdesk\CopyParentEntityController extends AbstractTileController |
| [src/Glpi/Controller/Config/Helpdesk/DeleteTileController.php](../src/Glpi/Controller/Config/Helpdesk/DeleteTileController.php) | .php | class Glpi\Controller\Config\Helpdesk\DeleteTileController extends AbstractTileController |
| [src/Glpi/Controller/Config/Helpdesk/SetTilesOrderController.php](../src/Glpi/Controller/Config/Helpdesk/SetTilesOrderController.php) | .php | class Glpi\Controller\Config\Helpdesk\SetTilesOrderController extends AbstractTileController |
| [src/Glpi/Controller/Config/Helpdesk/ShowAddTileFormController.php](../src/Glpi/Controller/Config/Helpdesk/ShowAddTileFormController.php) | .php | class Glpi\Controller\Config\Helpdesk\ShowAddTileFormController extends AbstractTileController |
| [src/Glpi/Controller/Config/Helpdesk/ShowEditTileFormController.php](../src/Glpi/Controller/Config/Helpdesk/ShowEditTileFormController.php) | .php | class Glpi\Controller\Config\Helpdesk\ShowEditTileFormController extends AbstractTileController |
| [src/Glpi/Controller/Config/Helpdesk/UpdateTileController.php](../src/Glpi/Controller/Config/Helpdesk/UpdateTileController.php) | .php | class Glpi\Controller\Config\Helpdesk\UpdateTileController extends AbstractTileController |
| [src/Glpi/Controller/Config/LDAPController.php](../src/Glpi/Controller/Config/LDAPController.php) | .php | class Glpi\Controller\Config\LDAPController extends AbstractController |
| [src/Glpi/Controller/CrudControllerTrait.php](../src/Glpi/Controller/CrudControllerTrait.php) | .php | trait Glpi\Controller\CrudControllerTrait |
| [src/Glpi/Controller/DCRoom/UpdateAxisLabelController.php](../src/Glpi/Controller/DCRoom/UpdateAxisLabelController.php) | .php | class Glpi\Controller\DCRoom\UpdateAxisLabelController extends AbstractController |
| [src/Glpi/Controller/DropdownFormController.php](../src/Glpi/Controller/DropdownFormController.php) | .php | class Glpi\Controller\DropdownFormController extends AbstractController |
| [src/Glpi/Controller/ErrorController.php](../src/Glpi/Controller/ErrorController.php) | .php | class Glpi\Controller\ErrorController extends AbstractController |
| [src/Glpi/Controller/Form/AllowListDropdown/CountUsersController.php](../src/Glpi/Controller/Form/AllowListDropdown/CountUsersController.php) | .php | class Glpi\Controller\Form\AllowListDropdown\CountUsersController extends AbstractController |
| [src/Glpi/Controller/Form/Condition/EditorController.php](../src/Glpi/Controller/Form/Condition/EditorController.php) | .php | class Glpi\Controller\Form\Condition\EditorController extends AbstractController |
| [src/Glpi/Controller/Form/Condition/EngineController.php](../src/Glpi/Controller/Form/Condition/EngineController.php) | .php | class Glpi\Controller\Form\Condition\EngineController extends AbstractController |
| [src/Glpi/Controller/Form/DelegationController.php](../src/Glpi/Controller/Form/DelegationController.php) | .php | class Glpi\Controller\Form\DelegationController extends AbstractController |
| [src/Glpi/Controller/Form/Destination/AddDestinationController.php](../src/Glpi/Controller/Form/Destination/AddDestinationController.php) | .php | class Glpi\Controller\Form\Destination\AddDestinationController extends AbstractController |
| [src/Glpi/Controller/Form/Destination/GetDestinationFormController.php](../src/Glpi/Controller/Form/Destination/GetDestinationFormController.php) | .php | class Glpi\Controller\Form\Destination\GetDestinationFormController extends AbstractController |
| [src/Glpi/Controller/Form/Destination/PurgeDestinationController.php](../src/Glpi/Controller/Form/Destination/PurgeDestinationController.php) | .php | class Glpi\Controller\Form\Destination\PurgeDestinationController extends AbstractController |
| [src/Glpi/Controller/Form/Destination/UpdateDestinationController.php](../src/Glpi/Controller/Form/Destination/UpdateDestinationController.php) | .php | class Glpi\Controller\Form\Destination\UpdateDestinationController extends AbstractController |
| [src/Glpi/Controller/Form/ExportController.php](../src/Glpi/Controller/Form/ExportController.php) | .php | class Glpi\Controller\Form\ExportController extends AbstractController |
| [src/Glpi/Controller/Form/Import/Step1IndexController.php](../src/Glpi/Controller/Form/Import/Step1IndexController.php) | .php | class Glpi\Controller\Form\Import\Step1IndexController extends AbstractController |
| [src/Glpi/Controller/Form/Import/Step2PreviewController.php](../src/Glpi/Controller/Form/Import/Step2PreviewController.php) | .php | class Glpi\Controller\Form\Import\Step2PreviewController extends AbstractController |
| [src/Glpi/Controller/Form/Import/Step3ResolveIssuesController.php](../src/Glpi/Controller/Form/Import/Step3ResolveIssuesController.php) | .php | class Glpi\Controller\Form\Import\Step3ResolveIssuesController extends AbstractController |
| [src/Glpi/Controller/Form/Import/Step4ExecuteController.php](../src/Glpi/Controller/Form/Import/Step4ExecuteController.php) | .php | class Glpi\Controller\Form\Import\Step4ExecuteController extends AbstractController |
| [src/Glpi/Controller/Form/QuestionActorsDropdownController.php](../src/Glpi/Controller/Form/QuestionActorsDropdownController.php) | .php | class Glpi\Controller\Form\QuestionActorsDropdownController extends AbstractController |
| [src/Glpi/Controller/Form/QuestionDropdownValuesController.php](../src/Glpi/Controller/Form/QuestionDropdownValuesController.php) | .php | class Glpi\Controller\Form\QuestionDropdownValuesController extends AbstractController |
| [src/Glpi/Controller/Form/RendererController.php](../src/Glpi/Controller/Form/RendererController.php) | .php | class Glpi\Controller\Form\RendererController extends AbstractController |
| [src/Glpi/Controller/Form/SubmitAnswerController.php](../src/Glpi/Controller/Form/SubmitAnswerController.php) | .php | class Glpi\Controller\Form\SubmitAnswerController extends AbstractController |
| [src/Glpi/Controller/Form/TagListController.php](../src/Glpi/Controller/Form/TagListController.php) | .php | class Glpi\Controller\Form\TagListController extends AbstractController |
| [src/Glpi/Controller/Form/Translation/AddNewFormTranslationController.php](../src/Glpi/Controller/Form/Translation/AddNewFormTranslationController.php) | .php | class Glpi\Controller\Form\Translation\AddNewFormTranslationController extends AbstractTranslationController |
| [src/Glpi/Controller/Form/Translation/DeleteFormTranslationController.php](../src/Glpi/Controller/Form/Translation/DeleteFormTranslationController.php) | .php | class Glpi\Controller\Form\Translation\DeleteFormTranslationController extends AbstractTranslationController |
| [src/Glpi/Controller/Form/Translation/GetFormTranslationController.php](../src/Glpi/Controller/Form/Translation/GetFormTranslationController.php) | .php | class Glpi\Controller\Form\Translation\GetFormTranslationController extends AbstractController |
| [src/Glpi/Controller/Form/Translation/UpdateFormTranslationController.php](../src/Glpi/Controller/Form/Translation/UpdateFormTranslationController.php) | .php | class Glpi\Controller\Form\Translation\UpdateFormTranslationController extends AbstractTranslationController |
| [src/Glpi/Controller/Form/Utils/CanCheckAccessPolicies.php](../src/Glpi/Controller/Form/Utils/CanCheckAccessPolicies.php) | .php | trait Glpi\Controller\Form\Utils\CanCheckAccessPolicies |
| [src/Glpi/Controller/Form/ValidateAnswerController.php](../src/Glpi/Controller/Form/ValidateAnswerController.php) | .php | class Glpi\Controller\Form\ValidateAnswerController extends AbstractController |
| [src/Glpi/Controller/GenericAjaxCrudController.php](../src/Glpi/Controller/GenericAjaxCrudController.php) | .php | class Glpi\Controller\GenericAjaxCrudController extends AbstractController |
| [src/Glpi/Controller/GenericFormController.php](../src/Glpi/Controller/GenericFormController.php) | .php | class Glpi\Controller\GenericFormController extends AbstractController |
| [src/Glpi/Controller/GenericListController.php](../src/Glpi/Controller/GenericListController.php) | .php | class Glpi\Controller\GenericListController extends AbstractController |
| [src/Glpi/Controller/Helpdesk/IndexController.php](../src/Glpi/Controller/Helpdesk/IndexController.php) | .php | class Glpi\Controller\Helpdesk\IndexController extends AbstractController |
| [src/Glpi/Controller/Helpdesk/SearchController.php](../src/Glpi/Controller/Helpdesk/SearchController.php) | .php | class Glpi\Controller\Helpdesk\SearchController extends AbstractController |
| [src/Glpi/Controller/Helpdesk/Translation/AddNewHelpdeskTranslationController.php](../src/Glpi/Controller/Helpdesk/Translation/AddNewHelpdeskTranslationController.php) | .php | class Glpi\Controller\Helpdesk\Translation\AddNewHelpdeskTranslationController extends AbstractTranslationController |
| [src/Glpi/Controller/Helpdesk/Translation/DeleteHelpdeskTranslationController.php](../src/Glpi/Controller/Helpdesk/Translation/DeleteHelpdeskTranslationController.php) | .php | class Glpi\Controller\Helpdesk\Translation\DeleteHelpdeskTranslationController extends AbstractTranslationController |
| [src/Glpi/Controller/Helpdesk/Translation/UpdateHelpdeskTranslationController.php](../src/Glpi/Controller/Helpdesk/Translation/UpdateHelpdeskTranslationController.php) | .php | class Glpi\Controller\Helpdesk\Translation\UpdateHelpdeskTranslationController extends AbstractTranslationController |
| [src/Glpi/Controller/IndexController.php](../src/Glpi/Controller/IndexController.php) | .php | class Glpi\Controller\IndexController extends AbstractController |
| [src/Glpi/Controller/InstallController.php](../src/Glpi/Controller/InstallController.php) | .php | class Glpi\Controller\InstallController extends AbstractController |
| [src/Glpi/Controller/InventoryController.php](../src/Glpi/Controller/InventoryController.php) | .php | class Glpi\Controller\InventoryController extends AbstractController |
| [src/Glpi/Controller/ItemType/Form/AuthMailFormController.php](../src/Glpi/Controller/ItemType/Form/AuthMailFormController.php) | .php | class Glpi\Controller\ItemType\Form\AuthMailFormController extends GenericFormController |
| [src/Glpi/Controller/ItemType/Form/ContactFormController.php](../src/Glpi/Controller/ItemType/Form/ContactFormController.php) | .php | class Glpi\Controller\ItemType\Form\ContactFormController extends GenericFormController |
| [src/Glpi/Controller/ItemType/Form/MailCollectorFormController.php](../src/Glpi/Controller/ItemType/Form/MailCollectorFormController.php) | .php | class Glpi\Controller\ItemType\Form\MailCollectorFormController extends GenericFormController |
| [src/Glpi/Controller/ItemType/Form/PlugFormController.php](../src/Glpi/Controller/ItemType/Form/PlugFormController.php) | .php | class Glpi\Controller\ItemType\Form\PlugFormController extends GenericFormController |
| [src/Glpi/Controller/ItemType/Form/SavedSearchFormController.php](../src/Glpi/Controller/ItemType/Form/SavedSearchFormController.php) | .php | class Glpi\Controller\ItemType\Form\SavedSearchFormController extends GenericFormController |
| [src/Glpi/Controller/ItemType/List/PlugListController.php](../src/Glpi/Controller/ItemType/List/PlugListController.php) | .php | class Glpi\Controller\ItemType\List\PlugListController extends AbstractController |
| [src/Glpi/Controller/Knowbase/AbstractCompareController.php](../src/Glpi/Controller/Knowbase/AbstractCompareController.php) | .php | class Glpi\Controller\Knowbase\AbstractCompareController extends AbstractController |
| [src/Glpi/Controller/Knowbase/AddCommentController.php](../src/Glpi/Controller/Knowbase/AddCommentController.php) | .php | class Glpi\Controller\Knowbase\AddCommentController extends AbstractController |
| [src/Glpi/Controller/Knowbase/AddPermissionController.php](../src/Glpi/Controller/Knowbase/AddPermissionController.php) | .php | class Glpi\Controller\Knowbase\AddPermissionController extends AbstractController |
| [src/Glpi/Controller/Knowbase/AsideActionsController.php](../src/Glpi/Controller/Knowbase/AsideActionsController.php) | .php | class Glpi\Controller\Knowbase\AsideActionsController extends AbstractController |
| [src/Glpi/Controller/Knowbase/AsideArticleChildrenController.php](../src/Glpi/Controller/Knowbase/AsideArticleChildrenController.php) | .php | class Glpi\Controller\Knowbase\AsideArticleChildrenController extends AbstractController |
| [src/Glpi/Controller/Knowbase/AsideArticleFoldController.php](../src/Glpi/Controller/Knowbase/AsideArticleFoldController.php) | .php | class Glpi\Controller\Knowbase\AsideArticleFoldController extends AbstractController |
| [src/Glpi/Controller/Knowbase/AsideSearchController.php](../src/Glpi/Controller/Knowbase/AsideSearchController.php) | .php | class Glpi\Controller\Knowbase\AsideSearchController extends AbstractController |
| [src/Glpi/Controller/Knowbase/CompareRevisionController.php](../src/Glpi/Controller/Knowbase/CompareRevisionController.php) | .php | class Glpi\Controller\Knowbase\CompareRevisionController extends AbstractCompareController |
| [src/Glpi/Controller/Knowbase/CompareTranslationRevisionController.php](../src/Glpi/Controller/Knowbase/CompareTranslationRevisionController.php) | .php | class Glpi\Controller\Knowbase\CompareTranslationRevisionController extends AbstractCompareController |
| [src/Glpi/Controller/Knowbase/CreateArticleController.php](../src/Glpi/Controller/Knowbase/CreateArticleController.php) | .php | class Glpi\Controller\Knowbase\CreateArticleController extends AbstractController |
| [src/Glpi/Controller/Knowbase/DeleteArticleController.php](../src/Glpi/Controller/Knowbase/DeleteArticleController.php) | .php | class Glpi\Controller\Knowbase\DeleteArticleController extends AbstractController |
| [src/Glpi/Controller/Knowbase/DeleteTranslationController.php](../src/Glpi/Controller/Knowbase/DeleteTranslationController.php) | .php | class Glpi\Controller\Knowbase\DeleteTranslationController extends AbstractController |
| [src/Glpi/Controller/Knowbase/GetTranslationContentController.php](../src/Glpi/Controller/Knowbase/GetTranslationContentController.php) | .php | class Glpi\Controller\Knowbase\GetTranslationContentController extends AbstractController |
| [src/Glpi/Controller/Knowbase/HistoryPageController.php](../src/Glpi/Controller/Knowbase/HistoryPageController.php) | .php | class Glpi\Controller\Knowbase\HistoryPageController extends AbstractController |
| [src/Glpi/Controller/Knowbase/KnowbaseItemController.php](../src/Glpi/Controller/Knowbase/KnowbaseItemController.php) | .php | class Glpi\Controller\Knowbase\KnowbaseItemController extends AbstractController |
| [src/Glpi/Controller/Knowbase/LinkDocumentController.php](../src/Glpi/Controller/Knowbase/LinkDocumentController.php) | .php | class Glpi\Controller\Knowbase\LinkDocumentController extends AbstractController |
| [src/Glpi/Controller/Knowbase/LinkItemController.php](../src/Glpi/Controller/Knowbase/LinkItemController.php) | .php | class Glpi\Controller\Knowbase\LinkItemController extends AbstractController |
| [src/Glpi/Controller/Knowbase/LinkItemModalController.php](../src/Glpi/Controller/Knowbase/LinkItemModalController.php) | .php | class Glpi\Controller\Knowbase\LinkItemModalController extends AbstractController |
| [src/Glpi/Controller/Knowbase/ListTranslationLanguagesController.php](../src/Glpi/Controller/Knowbase/ListTranslationLanguagesController.php) | .php | class Glpi\Controller\Knowbase\ListTranslationLanguagesController extends AbstractController |
| [src/Glpi/Controller/Knowbase/MoveArticleController.php](../src/Glpi/Controller/Knowbase/MoveArticleController.php) | .php | class Glpi\Controller\Knowbase\MoveArticleController extends AbstractController |
| [src/Glpi/Controller/Knowbase/MoveModalController.php](../src/Glpi/Controller/Knowbase/MoveModalController.php) | .php | class Glpi\Controller\Knowbase\MoveModalController extends AbstractController |
| [src/Glpi/Controller/Knowbase/PermissionDropdownController.php](../src/Glpi/Controller/Knowbase/PermissionDropdownController.php) | .php | class Glpi\Controller\Knowbase\PermissionDropdownController extends AbstractController |
| [src/Glpi/Controller/Knowbase/PermissionSubvisibilityController.php](../src/Glpi/Controller/Knowbase/PermissionSubvisibilityController.php) | .php | class Glpi\Controller\Knowbase\PermissionSubvisibilityController extends AbstractController |
| [src/Glpi/Controller/Knowbase/PurgeCommentController.php](../src/Glpi/Controller/Knowbase/PurgeCommentController.php) | .php | class Glpi\Controller\Knowbase\PurgeCommentController extends AbstractController |
| [src/Glpi/Controller/Knowbase/RevertRevisionController.php](../src/Glpi/Controller/Knowbase/RevertRevisionController.php) | .php | class Glpi\Controller\Knowbase\RevertRevisionController extends AbstractController |
| [src/Glpi/Controller/Knowbase/RevertTranslationRevisionController.php](../src/Glpi/Controller/Knowbase/RevertTranslationRevisionController.php) | .php | class Glpi\Controller\Knowbase\RevertTranslationRevisionController extends AbstractController |
| [src/Glpi/Controller/Knowbase/SaveTranslationController.php](../src/Glpi/Controller/Knowbase/SaveTranslationController.php) | .php | class Glpi\Controller\Knowbase\SaveTranslationController extends AbstractController |
| [src/Glpi/Controller/Knowbase/SidePanelController.php](../src/Glpi/Controller/Knowbase/SidePanelController.php) | .php | class Glpi\Controller\Knowbase\SidePanelController extends AbstractController |
| [src/Glpi/Controller/Knowbase/ToggleFavoriteController.php](../src/Glpi/Controller/Knowbase/ToggleFavoriteController.php) | .php | class Glpi\Controller\Knowbase\ToggleFavoriteController extends AbstractController |
| [src/Glpi/Controller/Knowbase/ToggleFieldController.php](../src/Glpi/Controller/Knowbase/ToggleFieldController.php) | .php | class Glpi\Controller\Knowbase\ToggleFieldController extends AbstractController |
| [src/Glpi/Controller/Knowbase/UnlinkDocumentController.php](../src/Glpi/Controller/Knowbase/UnlinkDocumentController.php) | .php | class Glpi\Controller\Knowbase\UnlinkDocumentController extends AbstractController |
| [src/Glpi/Controller/Knowbase/UnlinkItemController.php](../src/Glpi/Controller/Knowbase/UnlinkItemController.php) | .php | class Glpi\Controller\Knowbase\UnlinkItemController extends AbstractController |
| [src/Glpi/Controller/Knowbase/UpdateCommentController.php](../src/Glpi/Controller/Knowbase/UpdateCommentController.php) | .php | class Glpi\Controller\Knowbase\UpdateCommentController extends AbstractController |
| [src/Glpi/Controller/Knowbase/UpdateServiceCatalogController.php](../src/Glpi/Controller/Knowbase/UpdateServiceCatalogController.php) | .php | class Glpi\Controller\Knowbase\UpdateServiceCatalogController extends AbstractController |
| [src/Glpi/Controller/Knowbase/UpdateVisibilityDatesController.php](../src/Glpi/Controller/Knowbase/UpdateVisibilityDatesController.php) | .php | class Glpi\Controller\Knowbase\UpdateVisibilityDatesController extends AbstractController |
| [src/Glpi/Controller/Knowbase/UploadDocumentsController.php](../src/Glpi/Controller/Knowbase/UploadDocumentsController.php) | .php | class Glpi\Controller\Knowbase\UploadDocumentsController extends AbstractDocumentUploadController |
| [src/Glpi/Controller/Knowbase/UploadInlineImageController.php](../src/Glpi/Controller/Knowbase/UploadInlineImageController.php) | .php | class Glpi\Controller\Knowbase\UploadInlineImageController extends AbstractController |
| [src/Glpi/Controller/LegacyFileLoadController.php](../src/Glpi/Controller/LegacyFileLoadController.php) | .php | class Glpi\Controller\LegacyFileLoadController |
| [src/Glpi/Controller/MaintenanceController.php](../src/Glpi/Controller/MaintenanceController.php) | .php | class Glpi\Controller\MaintenanceController extends AbstractController |
| [src/Glpi/Controller/Plugin/LogoController.php](../src/Glpi/Controller/Plugin/LogoController.php) | .php | class Glpi\Controller\Plugin\LogoController extends AbstractController |
| [src/Glpi/Controller/ProgressController.php](../src/Glpi/Controller/ProgressController.php) | .php | class Glpi\Controller\ProgressController extends AbstractController |
| [src/Glpi/Controller/RequestException.php](../src/Glpi/Controller/RequestException.php) | .php | class Glpi\Controller\RequestException extends Exception |
| [src/Glpi/Controller/Security/MFAController.php](../src/Glpi/Controller/Security/MFAController.php) | .php | class Glpi\Controller\Security\MFAController extends AbstractController |
| [src/Glpi/Controller/Security/ReAuthController.php](../src/Glpi/Controller/Security/ReAuthController.php) | .php | class Glpi\Controller\Security\ReAuthController extends AbstractController |
| [src/Glpi/Controller/Security/Reauth/CASController.php](../src/Glpi/Controller/Security/Reauth/CASController.php) | .php | class Glpi\Controller\Security\Reauth\CASController extends AbstractController |
| [src/Glpi/Controller/Security/SecurityConfigController.php](../src/Glpi/Controller/Security/SecurityConfigController.php) | .php | class Glpi\Controller\Security\SecurityConfigController extends AbstractController |
| [src/Glpi/Controller/Security/SessionTrackerController.php](../src/Glpi/Controller/Security/SessionTrackerController.php) | .php | class Glpi\Controller\Security\SessionTrackerController extends AbstractController |
| [src/Glpi/Controller/ServiceCatalog/IndexController.php](../src/Glpi/Controller/ServiceCatalog/IndexController.php) | .php | class Glpi\Controller\ServiceCatalog\IndexController extends AbstractController |
| [src/Glpi/Controller/ServiceCatalog/ItemsController.php](../src/Glpi/Controller/ServiceCatalog/ItemsController.php) | .php | class Glpi\Controller\ServiceCatalog\ItemsController extends AbstractController |
| [src/Glpi/Controller/Session/ChangeEntityController.php](../src/Glpi/Controller/Session/ChangeEntityController.php) | .php | class Glpi\Controller\Session\ChangeEntityController extends AbstractController |
| [src/Glpi/Controller/Session/ChangeProfileController.php](../src/Glpi/Controller/Session/ChangeProfileController.php) | .php | class Glpi\Controller\Session\ChangeProfileController extends AbstractController |
| [src/Glpi/Controller/ShareAccessController.php](../src/Glpi/Controller/ShareAccessController.php) | .php | class Glpi\Controller\ShareAccessController extends AbstractController |
| [src/Glpi/Controller/ShareTokenController.php](../src/Glpi/Controller/ShareTokenController.php) | .php | class Glpi\Controller\ShareTokenController extends AbstractController |
| [src/Glpi/Controller/StatusController.php](../src/Glpi/Controller/StatusController.php) | .php | class Glpi\Controller\StatusController extends AbstractController |
| [src/Glpi/Controller/Traits/AsyncOperationProgressControllerTrait.php](../src/Glpi/Controller/Traits/AsyncOperationProgressControllerTrait.php) | .php | trait Glpi\Controller\Traits\AsyncOperationProgressControllerTrait |
| [src/Glpi/Controller/Translation/AbstractTranslationController.php](../src/Glpi/Controller/Translation/AbstractTranslationController.php) | .php | class Glpi\Controller\Translation\AbstractTranslationController extends AbstractController |
| [src/Glpi/Controller/UI/Illustration/CustomIllustrationController.php](../src/Glpi/Controller/UI/Illustration/CustomIllustrationController.php) | .php | class Glpi\Controller\UI\Illustration\CustomIllustrationController extends AbstractController |
| [src/Glpi/Controller/UI/Illustration/CustomSceneController.php](../src/Glpi/Controller/UI/Illustration/CustomSceneController.php) | .php | class Glpi\Controller\UI\Illustration\CustomSceneController extends AbstractController |
| [src/Glpi/Controller/UI/Illustration/SearchController.php](../src/Glpi/Controller/UI/Illustration/SearchController.php) | .php | class Glpi\Controller\UI\Illustration\SearchController extends AbstractController |
| [src/Glpi/Controller/UI/Illustration/UploadController.php](../src/Glpi/Controller/UI/Illustration/UploadController.php) | .php | class Glpi\Controller\UI\Illustration\UploadController extends AbstractController |
| [src/Glpi/Controller/User/InfoCardController.php](../src/Glpi/Controller/User/InfoCardController.php) | .php | class Glpi\Controller\User\InfoCardController extends AbstractController |
| [src/Glpi/Controller/WellKnownController.php](../src/Glpi/Controller/WellKnownController.php) | .php | class Glpi\Controller\WellKnownController extends AbstractController |
| [src/Glpi/Csv/CsvResponse.php](../src/Glpi/Csv/CsvResponse.php) | .php | class Glpi\Csv\CsvResponse |
| [src/Glpi/Csv/ExportToCsvInterface.php](../src/Glpi/Csv/ExportToCsvInterface.php) | .php | interface Glpi\Csv\ExportToCsvInterface |
| [src/Glpi/Csv/ImpactCsvExport.php](../src/Glpi/Csv/ImpactCsvExport.php) | .php | class Glpi\Csv\ImpactCsvExport |
| [src/Glpi/Csv/LogCsvExport.php](../src/Glpi/Csv/LogCsvExport.php) | .php | class Glpi\Csv\LogCsvExport |
| [src/Glpi/Csv/PlanningCsv.php](../src/Glpi/Csv/PlanningCsv.php) | .php | class Glpi\Csv\PlanningCsv |
| [src/Glpi/Csv/PrinterLogCsvExport.php](../src/Glpi/Csv/PrinterLogCsvExport.php) | .php | class Glpi\Csv\PrinterLogCsvExport |
| [src/Glpi/Csv/PrinterLogCsvExportComparison.php](../src/Glpi/Csv/PrinterLogCsvExportComparison.php) | .php | class Glpi\Csv\PrinterLogCsvExportComparison |
| [src/Glpi/Csv/StatCsvExport.php](../src/Glpi/Csv/StatCsvExport.php) | .php | class Glpi\Csv\StatCsvExport |
| [src/Glpi/CustomObject/AbstractDefinition.php](../src/Glpi/CustomObject/AbstractDefinition.php) | .php | class Glpi\CustomObject\AbstractDefinition extends CommonDBTM |
| [src/Glpi/CustomObject/AbstractDefinitionManager.php](../src/Glpi/CustomObject/AbstractDefinitionManager.php) | .php | class Glpi\CustomObject\AbstractDefinitionManager |
| [src/Glpi/CustomObject/CustomObjectTrait.php](../src/Glpi/CustomObject/CustomObjectTrait.php) | .php | trait Glpi\CustomObject\CustomObjectTrait |
| [src/Glpi/DBAL/JsonFieldInterface.php](../src/Glpi/DBAL/JsonFieldInterface.php) | .php | interface Glpi\DBAL\JsonFieldInterface extends JsonSerializable |
| [src/Glpi/DBAL/Operator.php](../src/Glpi/DBAL/Operator.php) | .php | enum Glpi\DBAL\Operator |
| [src/Glpi/DBAL/Parts/BasePart.php](../src/Glpi/DBAL/Parts/BasePart.php) | .php | class Glpi\DBAL\Parts\BasePart |
| [src/Glpi/DBAL/Parts/Delete.php](../src/Glpi/DBAL/Parts/Delete.php) | .php | class Glpi\DBAL\Parts\Delete extends BasePart |
| [src/Glpi/DBAL/Parts/Having.php](../src/Glpi/DBAL/Parts/Having.php) | .php | class Glpi\DBAL\Parts\Having extends Where |
| [src/Glpi/DBAL/Parts/Insert.php](../src/Glpi/DBAL/Parts/Insert.php) | .php | class Glpi\DBAL\Parts\Insert extends BasePart |
| [src/Glpi/DBAL/Parts/LeftJoin.php](../src/Glpi/DBAL/Parts/LeftJoin.php) | .php | class Glpi\DBAL\Parts\LeftJoin extends BasePart |
| [src/Glpi/DBAL/Parts/Select.php](../src/Glpi/DBAL/Parts/Select.php) | .php | class Glpi\DBAL\Parts\Select extends BasePart |
| [src/Glpi/DBAL/Parts/Update.php](../src/Glpi/DBAL/Parts/Update.php) | .php | class Glpi\DBAL\Parts\Update extends BasePart |
| [src/Glpi/DBAL/Parts/Where.php](../src/Glpi/DBAL/Parts/Where.php) | .php | class Glpi\DBAL\Parts\Where extends BasePart |
| [src/Glpi/DBAL/PrepareForCloneInterface.php](../src/Glpi/DBAL/PrepareForCloneInterface.php) | .php | interface Glpi\DBAL\PrepareForCloneInterface |
| [src/Glpi/DBAL/QueryAliasInterface.php](../src/Glpi/DBAL/QueryAliasInterface.php) | .php | interface Glpi\DBAL\QueryAliasInterface |
| [src/Glpi/DBAL/QueryAliasTrait.php](../src/Glpi/DBAL/QueryAliasTrait.php) | .php | trait Glpi\DBAL\QueryAliasTrait |
| [src/Glpi/DBAL/QueryElementInterface.php](../src/Glpi/DBAL/QueryElementInterface.php) | .php | interface Glpi\DBAL\QueryElementInterface extends Stringable |
| [src/Glpi/DBAL/QueryExpression.php](../src/Glpi/DBAL/QueryExpression.php) | .php | class Glpi\DBAL\QueryExpression |
| [src/Glpi/DBAL/QueryFunction.php](../src/Glpi/DBAL/QueryFunction.php) | .php | class Glpi\DBAL\QueryFunction |
| [src/Glpi/DBAL/QueryIdentifier.php](../src/Glpi/DBAL/QueryIdentifier.php) | .php | class Glpi\DBAL\QueryIdentifier |
| [src/Glpi/DBAL/QueryParam.php](../src/Glpi/DBAL/QueryParam.php) | .php | class Glpi\DBAL\QueryParam |
| [src/Glpi/DBAL/QuerySubQuery.php](../src/Glpi/DBAL/QuerySubQuery.php) | .php | class Glpi\DBAL\QuerySubQuery extends AbstractQuery |
| [src/Glpi/DBAL/QueryUnion.php](../src/Glpi/DBAL/QueryUnion.php) | .php | class Glpi\DBAL\QueryUnion extends AbstractQuery |
| [src/Glpi/DBAL/QueryValue.php](../src/Glpi/DBAL/QueryValue.php) | .php | class Glpi\DBAL\QueryValue |
| [src/Glpi/Dashboard/Dashboard.php](../src/Glpi/Dashboard/Dashboard.php) | .php | class Glpi\Dashboard\Dashboard extends CommonDBTM |
| [src/Glpi/Dashboard/FakeProvider.php](../src/Glpi/Dashboard/FakeProvider.php) | .php | class Glpi\Dashboard\FakeProvider extends Provider |
| [src/Glpi/Dashboard/Filter.php](../src/Glpi/Dashboard/Filter.php) | .php | class Glpi\Dashboard\Filter extends CommonDBChild |
| [src/Glpi/Dashboard/Filters/AbstractFilter.php](../src/Glpi/Dashboard/Filters/AbstractFilter.php) | .php | class Glpi\Dashboard\Filters\AbstractFilter |
| [src/Glpi/Dashboard/Filters/AbstractGroupFilter.php](../src/Glpi/Dashboard/Filters/AbstractGroupFilter.php) | .php | class Glpi\Dashboard\Filters\AbstractGroupFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/AssignedITILUserFilterTrait.php](../src/Glpi/Dashboard/Filters/AssignedITILUserFilterTrait.php) | .php | trait Glpi\Dashboard\Filters\AssignedITILUserFilterTrait |
| [src/Glpi/Dashboard/Filters/DatesFilter.php](../src/Glpi/Dashboard/Filters/DatesFilter.php) | .php | class Glpi\Dashboard\Filters\DatesFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/DatesModFilter.php](../src/Glpi/Dashboard/Filters/DatesModFilter.php) | .php | class Glpi\Dashboard\Filters\DatesModFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/EntityFilter.php](../src/Glpi/Dashboard/Filters/EntityFilter.php) | .php | class Glpi\Dashboard\Filters\EntityFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/GroupRequesterFilter.php](../src/Glpi/Dashboard/Filters/GroupRequesterFilter.php) | .php | class Glpi\Dashboard\Filters\GroupRequesterFilter extends AbstractGroupFilter |
| [src/Glpi/Dashboard/Filters/GroupTechFilter.php](../src/Glpi/Dashboard/Filters/GroupTechFilter.php) | .php | class Glpi\Dashboard\Filters\GroupTechFilter extends AbstractGroupFilter |
| [src/Glpi/Dashboard/Filters/ItilCategoryFilter.php](../src/Glpi/Dashboard/Filters/ItilCategoryFilter.php) | .php | class Glpi\Dashboard\Filters\ItilCategoryFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/LocationFilter.php](../src/Glpi/Dashboard/Filters/LocationFilter.php) | .php | class Glpi\Dashboard\Filters\LocationFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/ManufacturerFilter.php](../src/Glpi/Dashboard/Filters/ManufacturerFilter.php) | .php | class Glpi\Dashboard\Filters\ManufacturerFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/RequestTypeFilter.php](../src/Glpi/Dashboard/Filters/RequestTypeFilter.php) | .php | class Glpi\Dashboard\Filters\RequestTypeFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/SlaFilter.php](../src/Glpi/Dashboard/Filters/SlaFilter.php) | .php | class Glpi\Dashboard\Filters\SlaFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/StateFilter.php](../src/Glpi/Dashboard/Filters/StateFilter.php) | .php | class Glpi\Dashboard\Filters\StateFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/TicketStatusFilter.php](../src/Glpi/Dashboard/Filters/TicketStatusFilter.php) | .php | class Glpi\Dashboard\Filters\TicketStatusFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/TicketTypeFilter.php](../src/Glpi/Dashboard/Filters/TicketTypeFilter.php) | .php | class Glpi\Dashboard\Filters\TicketTypeFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/UserAssignedFilter.php](../src/Glpi/Dashboard/Filters/UserAssignedFilter.php) | .php | class Glpi\Dashboard\Filters\UserAssignedFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Filters/UserTechFilter.php](../src/Glpi/Dashboard/Filters/UserTechFilter.php) | .php | class Glpi\Dashboard\Filters\UserTechFilter extends AbstractFilter |
| [src/Glpi/Dashboard/Grid.php](../src/Glpi/Dashboard/Grid.php) | .php | class Glpi\Dashboard\Grid |
| [src/Glpi/Dashboard/Item.php](../src/Glpi/Dashboard/Item.php) | .php | class Glpi\Dashboard\Item extends CommonDBChild |
| [src/Glpi/Dashboard/Palette.php](../src/Glpi/Dashboard/Palette.php) | .php | class Glpi\Dashboard\Palette |
| [src/Glpi/Dashboard/Provider.php](../src/Glpi/Dashboard/Provider.php) | .php | class Glpi\Dashboard\Provider |
| [src/Glpi/Dashboard/Right.php](../src/Glpi/Dashboard/Right.php) | .php | class Glpi\Dashboard\Right extends CommonDBChild |
| [src/Glpi/Dashboard/Widget.php](../src/Glpi/Dashboard/Widget.php) | .php | class Glpi\Dashboard\Widget |
| [src/Glpi/Debug/Profile.php](../src/Glpi/Debug/Profile.php) | .php | class Glpi\Debug\Profile |
| [src/Glpi/Debug/Profiler.php](../src/Glpi/Debug/Profiler.php) | .php | class Glpi\Debug\Profiler |
| [src/Glpi/Debug/ProfilerSection.php](../src/Glpi/Debug/ProfilerSection.php) | .php | class Glpi\Debug\ProfilerSection |
| [src/Glpi/DependencyInjection/Compiler/RemoveUnwantedTwigExtensionsPass.php](../src/Glpi/DependencyInjection/Compiler/RemoveUnwantedTwigExtensionsPass.php) | .php | class Glpi\DependencyInjection\Compiler\RemoveUnwantedTwigExtensionsPass |
| [src/Glpi/DependencyInjection/PluginContainer.php](../src/Glpi/DependencyInjection/PluginContainer.php) | .php | class Glpi\DependencyInjection\PluginContainer |
| [src/Glpi/DependencyInjection/PublicService.php](../src/Glpi/DependencyInjection/PublicService.php) | .php | interface Glpi\DependencyInjection\PublicService |
| [src/Glpi/Dropdown/Dropdown.php](../src/Glpi/Dropdown/Dropdown.php) | .php | class Glpi\Dropdown\Dropdown extends CommonTreeDropdown |
| [src/Glpi/Dropdown/DropdownDefinition.php](../src/Glpi/Dropdown/DropdownDefinition.php) | .php | class Glpi\Dropdown\DropdownDefinition extends AbstractDefinition |
| [src/Glpi/Dropdown/DropdownDefinitionManager.php](../src/Glpi/Dropdown/DropdownDefinitionManager.php) | .php | class Glpi\Dropdown\DropdownDefinitionManager extends AbstractDefinitionManager |
| [src/Glpi/Error/ErrorDisplayHandler/CliDisplayHandler.php](../src/Glpi/Error/ErrorDisplayHandler/CliDisplayHandler.php) | .php | class Glpi\Error\ErrorDisplayHandler\CliDisplayHandler |
| [src/Glpi/Error/ErrorDisplayHandler/ConsoleErrorDisplayHandler.php](../src/Glpi/Error/ErrorDisplayHandler/ConsoleErrorDisplayHandler.php) | .php | class Glpi\Error\ErrorDisplayHandler\ConsoleErrorDisplayHandler |
| [src/Glpi/Error/ErrorDisplayHandler/ErrorDisplayHandler.php](../src/Glpi/Error/ErrorDisplayHandler/ErrorDisplayHandler.php) | .php | interface Glpi\Error\ErrorDisplayHandler\ErrorDisplayHandler |
| [src/Glpi/Error/ErrorDisplayHandler/HtmlErrorDisplayHandler.php](../src/Glpi/Error/ErrorDisplayHandler/HtmlErrorDisplayHandler.php) | .php | class Glpi\Error\ErrorDisplayHandler\HtmlErrorDisplayHandler |
| [src/Glpi/Error/ErrorHandler.php](../src/Glpi/Error/ErrorHandler.php) | .php | class Glpi\Error\ErrorHandler extends BaseErrorHandler |
| [src/Glpi/Error/ErrorUtils.php](../src/Glpi/Error/ErrorUtils.php) | .php | class Glpi\Error\ErrorUtils |
| [src/Glpi/Error/InputTruncationReason.php](../src/Glpi/Error/InputTruncationReason.php) | .php | enum Glpi\Error\InputTruncationReason |
| [src/Glpi/Error/StartupErrors.php](../src/Glpi/Error/StartupErrors.php) | .php | class Glpi\Error\StartupErrors |
| [src/Glpi/Event.php](../src/Glpi/Event.php) | .php | class Glpi\Event extends CommonDBTM |
| [src/Glpi/Exception/AuthenticationFailedException.php](../src/Glpi/Exception/AuthenticationFailedException.php) | .php | class Glpi\Exception\AuthenticationFailedException extends Exception |
| [src/Glpi/Exception/Database/QueryException.php](../src/Glpi/Exception/Database/QueryException.php) | .php | class Glpi\Exception\Database\QueryException extends RuntimeException |
| [src/Glpi/Exception/Database/StatementException.php](../src/Glpi/Exception/Database/StatementException.php) | .php | class Glpi\Exception\Database\StatementException extends RuntimeException |
| [src/Glpi/Exception/EmptyCurlContentException.php](../src/Glpi/Exception/EmptyCurlContentException.php) | .php | class Glpi\Exception\EmptyCurlContentException extends Exception |
| [src/Glpi/Exception/ForgetPasswordException.php](../src/Glpi/Exception/ForgetPasswordException.php) | .php | class Glpi\Exception\ForgetPasswordException extends Exception |
| [src/Glpi/Exception/Http/AccessDeniedHttpException.php](../src/Glpi/Exception/Http/AccessDeniedHttpException.php) | .php | class Glpi\Exception\Http\AccessDeniedHttpException extends BaseException |
| [src/Glpi/Exception/Http/BadRequestHttpException.php](../src/Glpi/Exception/Http/BadRequestHttpException.php) | .php | class Glpi\Exception\Http\BadRequestHttpException extends BaseException |
| [src/Glpi/Exception/Http/HttpException.php](../src/Glpi/Exception/Http/HttpException.php) | .php | class Glpi\Exception\Http\HttpException extends BaseException |
| [src/Glpi/Exception/Http/HttpExceptionInterface.php](../src/Glpi/Exception/Http/HttpExceptionInterface.php) | .php | interface Glpi\Exception\Http\HttpExceptionInterface extends \Symfony\Component\HttpKernel\Exception\HttpExceptionInterface |
| [src/Glpi/Exception/Http/HttpExceptionTrait.php](../src/Glpi/Exception/Http/HttpExceptionTrait.php) | .php | trait Glpi\Exception\Http\HttpExceptionTrait |
| [src/Glpi/Exception/Http/NotFoundHttpException.php](../src/Glpi/Exception/Http/NotFoundHttpException.php) | .php | class Glpi\Exception\Http\NotFoundHttpException extends BaseException |
| [src/Glpi/Exception/Http/UnprocessableEntityHttpException.php](../src/Glpi/Exception/Http/UnprocessableEntityHttpException.php) | .php | class Glpi\Exception\Http\UnprocessableEntityHttpException extends BaseException |
| [src/Glpi/Exception/ItemLinkException.php](../src/Glpi/Exception/ItemLinkException.php) | .php | class Glpi\Exception\ItemLinkException extends Exception |
| [src/Glpi/Exception/OAuth2KeyException.php](../src/Glpi/Exception/OAuth2KeyException.php) | .php | class Glpi\Exception\OAuth2KeyException extends Exception |
| [src/Glpi/Exception/PasswordTooWeakException.php](../src/Glpi/Exception/PasswordTooWeakException.php) | .php | class Glpi\Exception\PasswordTooWeakException extends Exception |
| [src/Glpi/Exception/RedirectException.php](../src/Glpi/Exception/RedirectException.php) | .php | class Glpi\Exception\RedirectException extends Exception |
| [src/Glpi/Exception/SessionExpiredException.php](../src/Glpi/Exception/SessionExpiredException.php) | .php | class Glpi\Exception\SessionExpiredException extends Exception |
| [src/Glpi/Exception/TooManyResultsException.php](../src/Glpi/Exception/TooManyResultsException.php) | .php | class Glpi\Exception\TooManyResultsException extends RuntimeException |
| [src/Glpi/Features/AssetImage.php](../src/Glpi/Features/AssetImage.php) | .php | trait Glpi\Features\AssetImage |
| [src/Glpi/Features/AssignableItem.php](../src/Glpi/Features/AssignableItem.php) | .php | trait Glpi\Features\AssignableItem |
| [src/Glpi/Features/AssignableItemInterface.php](../src/Glpi/Features/AssignableItemInterface.php) | .php | interface Glpi\Features\AssignableItemInterface |
| [src/Glpi/Features/CacheableListInterface.php](../src/Glpi/Features/CacheableListInterface.php) | .php | interface Glpi\Features\CacheableListInterface |
| [src/Glpi/Features/Clonable.php](../src/Glpi/Features/Clonable.php) | .php | trait Glpi\Features\Clonable |
| [src/Glpi/Features/CloneMapper.php](../src/Glpi/Features/CloneMapper.php) | .php | class Glpi\Features\CloneMapper |
| [src/Glpi/Features/CloneWithoutNameSuffix.php](../src/Glpi/Features/CloneWithoutNameSuffix.php) | .php | class Glpi\Features\CloneWithoutNameSuffix |
| [src/Glpi/Features/DCBreadcrumb.php](../src/Glpi/Features/DCBreadcrumb.php) | .php | trait Glpi\Features\DCBreadcrumb |
| [src/Glpi/Features/DCBreadcrumbInterface.php](../src/Glpi/Features/DCBreadcrumbInterface.php) | .php | interface Glpi\Features\DCBreadcrumbInterface |
| [src/Glpi/Features/Inventoriable.php](../src/Glpi/Features/Inventoriable.php) | .php | trait Glpi\Features\Inventoriable |
| [src/Glpi/Features/Kanban.php](../src/Glpi/Features/Kanban.php) | .php | trait Glpi\Features\Kanban |
| [src/Glpi/Features/KanbanInterface.php](../src/Glpi/Features/KanbanInterface.php) | .php | interface Glpi\Features\KanbanInterface |
| [src/Glpi/Features/ParentStatus.php](../src/Glpi/Features/ParentStatus.php) | .php | trait Glpi\Features\ParentStatus |
| [src/Glpi/Features/PlanningEvent.php](../src/Glpi/Features/PlanningEvent.php) | .php | trait Glpi\Features\PlanningEvent |
| [src/Glpi/Features/State.php](../src/Glpi/Features/State.php) | .php | trait Glpi\Features\State |
| [src/Glpi/Features/StateInterface.php](../src/Glpi/Features/StateInterface.php) | .php | interface Glpi\Features\StateInterface |
| [src/Glpi/Features/Teamwork.php](../src/Glpi/Features/Teamwork.php) | .php | trait Glpi\Features\Teamwork |
| [src/Glpi/Features/TeamworkInterface.php](../src/Glpi/Features/TeamworkInterface.php) | .php | interface Glpi\Features\TeamworkInterface |
| [src/Glpi/Features/Timeline.php](../src/Glpi/Features/Timeline.php) | .php | trait Glpi\Features\Timeline |
| [src/Glpi/Features/TreeBrowse.php](../src/Glpi/Features/TreeBrowse.php) | .php | trait Glpi\Features\TreeBrowse |
| [src/Glpi/Features/TreeBrowseInterface.php](../src/Glpi/Features/TreeBrowseInterface.php) | .php | interface Glpi\Features\TreeBrowseInterface |
| [src/Glpi/Features/ZonableModelPicture.php](../src/Glpi/Features/ZonableModelPicture.php) | .php | interface Glpi\Features\ZonableModelPicture |
| [src/Glpi/Form/AccessControl/AccessVote.php](../src/Glpi/Form/AccessControl/AccessVote.php) | .php | enum Glpi\Form\AccessControl\AccessVote |
| [src/Glpi/Form/AccessControl/ControlType/AllowList.php](../src/Glpi/Form/AccessControl/ControlType/AllowList.php) | .php | class Glpi\Form\AccessControl\ControlType\AllowList |
| [src/Glpi/Form/AccessControl/ControlType/AllowListConfig.php](../src/Glpi/Form/AccessControl/ControlType/AllowListConfig.php) | .php | class Glpi\Form\AccessControl\ControlType\AllowListConfig |
| [src/Glpi/Form/AccessControl/ControlType/AllowListDropdown.php](../src/Glpi/Form/AccessControl/ControlType/AllowListDropdown.php) | .php | class Glpi\Form\AccessControl\ControlType\AllowListDropdown extends AbstractRightsDropdown |
| [src/Glpi/Form/AccessControl/ControlType/ControlTypeInterface.php](../src/Glpi/Form/AccessControl/ControlType/ControlTypeInterface.php) | .php | interface Glpi\Form\AccessControl\ControlType\ControlTypeInterface |
| [src/Glpi/Form/AccessControl/ControlType/DirectAccess.php](../src/Glpi/Form/AccessControl/ControlType/DirectAccess.php) | .php | class Glpi\Form\AccessControl\ControlType\DirectAccess |
| [src/Glpi/Form/AccessControl/ControlType/DirectAccessConfig.php](../src/Glpi/Form/AccessControl/ControlType/DirectAccessConfig.php) | .php | class Glpi\Form\AccessControl\ControlType\DirectAccessConfig |
| [src/Glpi/Form/AccessControl/FormAccessControl.php](../src/Glpi/Form/AccessControl/FormAccessControl.php) | .php | class Glpi\Form\AccessControl\FormAccessControl extends CommonDBChild |
| [src/Glpi/Form/AccessControl/FormAccessControlManager.php](../src/Glpi/Form/AccessControl/FormAccessControlManager.php) | .php | class Glpi\Form\AccessControl\FormAccessControlManager |
| [src/Glpi/Form/AccessControl/FormAccessParameters.php](../src/Glpi/Form/AccessControl/FormAccessParameters.php) | .php | class Glpi\Form\AccessControl\FormAccessParameters |
| [src/Glpi/Form/Answer.php](../src/Glpi/Form/Answer.php) | .php | class Glpi\Form\Answer |
| [src/Glpi/Form/AnswersHandler/AnswersHandler.php](../src/Glpi/Form/AnswersHandler/AnswersHandler.php) | .php | class Glpi\Form\AnswersHandler\AnswersHandler |
| [src/Glpi/Form/AnswersSet.php](../src/Glpi/Form/AnswersSet.php) | .php | class Glpi\Form\AnswersSet extends CommonDBChild |
| [src/Glpi/Form/BlockInterface.php](../src/Glpi/Form/BlockInterface.php) | .php | interface Glpi\Form\BlockInterface extends ProvideTranslationsInterface |
| [src/Glpi/Form/Category.php](../src/Glpi/Form/Category.php) | .php | class Glpi\Form\Category extends CommonTreeDropdown |
| [src/Glpi/Form/Clone/FormCloneHelper.php](../src/Glpi/Form/Clone/FormCloneHelper.php) | .php | class Glpi\Form\Clone\FormCloneHelper |
| [src/Glpi/Form/Clone/MappedItemNotFoundException.php](../src/Glpi/Form/Clone/MappedItemNotFoundException.php) | .php | class Glpi\Form\Clone\MappedItemNotFoundException extends Exception |
| [src/Glpi/Form/Comment.php](../src/Glpi/Form/Comment.php) | .php | class Glpi\Form\Comment extends CommonDBChild |
| [src/Glpi/Form/Condition/CommentData.php](../src/Glpi/Form/Condition/CommentData.php) | .php | class Glpi\Form\Condition\CommentData |
| [src/Glpi/Form/Condition/ConditionData.php](../src/Glpi/Form/Condition/ConditionData.php) | .php | class Glpi\Form\Condition\ConditionData |
| [src/Glpi/Form/Condition/ConditionHandler/AbstractDateTimeConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/AbstractDateTimeConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\AbstractDateTimeConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/ActorConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/ActorConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\ActorConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/ArrayConditionHandlerTrait.php](../src/Glpi/Form/Condition/ConditionHandler/ArrayConditionHandlerTrait.php) | .php | trait Glpi\Form\Condition\ConditionHandler\ArrayConditionHandlerTrait |
| [src/Glpi/Form/Condition/ConditionHandler/ConditionHandlerInterface.php](../src/Glpi/Form/Condition/ConditionHandler/ConditionHandlerInterface.php) | .php | interface Glpi\Form\Condition\ConditionHandler\ConditionHandlerInterface |
| [src/Glpi/Form/Condition/ConditionHandler/DateAndTimeConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/DateAndTimeConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\DateAndTimeConditionHandler extends AbstractDateTimeConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/DateConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/DateConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\DateConditionHandler extends AbstractDateTimeConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/EmptyConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/EmptyConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\EmptyConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/ItemAsTextConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/ItemAsTextConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\ItemAsTextConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/ItemConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/ItemConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\ItemConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/MultipleChoiceFromValuesConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/MultipleChoiceFromValuesConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\MultipleChoiceFromValuesConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/NumberConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/NumberConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\NumberConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/RegexConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/RegexConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\RegexConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/RequestTypeConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/RequestTypeConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\RequestTypeConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/RichTextConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/RichTextConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\RichTextConditionHandler extends StringConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/SingleChoiceFromValuesConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/SingleChoiceFromValuesConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\SingleChoiceFromValuesConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/StringConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/StringConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\StringConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/TimeConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/TimeConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\TimeConditionHandler extends AbstractDateTimeConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/UrgencyConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/UrgencyConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\UrgencyConditionHandler extends NumberConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/UserDevicesAsTextConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/UserDevicesAsTextConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\UserDevicesAsTextConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/UserDevicesConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/UserDevicesConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\UserDevicesConditionHandler |
| [src/Glpi/Form/Condition/ConditionHandler/VisibilityConditionHandler.php](../src/Glpi/Form/Condition/ConditionHandler/VisibilityConditionHandler.php) | .php | class Glpi\Form\Condition\ConditionHandler\VisibilityConditionHandler |
| [src/Glpi/Form/Condition/ConditionValueTransformerInterface.php](../src/Glpi/Form/Condition/ConditionValueTransformerInterface.php) | .php | interface Glpi\Form\Condition\ConditionValueTransformerInterface |
| [src/Glpi/Form/Condition/ConditionableCreationInterface.php](../src/Glpi/Form/Condition/ConditionableCreationInterface.php) | .php | interface Glpi\Form\Condition\ConditionableCreationInterface extends ConditionableInterface |
| [src/Glpi/Form/Condition/ConditionableCreationTrait.php](../src/Glpi/Form/Condition/ConditionableCreationTrait.php) | .php | trait Glpi\Form\Condition\ConditionableCreationTrait |
| [src/Glpi/Form/Condition/ConditionableInterface.php](../src/Glpi/Form/Condition/ConditionableInterface.php) | .php | interface Glpi\Form\Condition\ConditionableInterface |
| [src/Glpi/Form/Condition/ConditionableTrait.php](../src/Glpi/Form/Condition/ConditionableTrait.php) | .php | trait Glpi\Form\Condition\ConditionableTrait |
| [src/Glpi/Form/Condition/ConditionableValidationTrait.php](../src/Glpi/Form/Condition/ConditionableValidationTrait.php) | .php | trait Glpi\Form\Condition\ConditionableValidationTrait |
| [src/Glpi/Form/Condition/ConditionableVisibilityInterface.php](../src/Glpi/Form/Condition/ConditionableVisibilityInterface.php) | .php | interface Glpi\Form\Condition\ConditionableVisibilityInterface extends ConditionableInterface |
| [src/Glpi/Form/Condition/ConditionableVisibilityTrait.php](../src/Glpi/Form/Condition/ConditionableVisibilityTrait.php) | .php | trait Glpi\Form\Condition\ConditionableVisibilityTrait |
| [src/Glpi/Form/Condition/CreationStrategy.php](../src/Glpi/Form/Condition/CreationStrategy.php) | .php | enum Glpi\Form\Condition\CreationStrategy |
| [src/Glpi/Form/Condition/EditorManager.php](../src/Glpi/Form/Condition/EditorManager.php) | .php | class Glpi\Form\Condition\EditorManager |
| [src/Glpi/Form/Condition/Engine.php](../src/Glpi/Form/Condition/Engine.php) | .php | class Glpi\Form\Condition\Engine |
| [src/Glpi/Form/Condition/EngineCreationOutput.php](../src/Glpi/Form/Condition/EngineCreationOutput.php) | .php | class Glpi\Form\Condition\EngineCreationOutput |
| [src/Glpi/Form/Condition/EngineInput.php](../src/Glpi/Form/Condition/EngineInput.php) | .php | class Glpi\Form\Condition\EngineInput |
| [src/Glpi/Form/Condition/EngineValidationOutput.php](../src/Glpi/Form/Condition/EngineValidationOutput.php) | .php | class Glpi\Form\Condition\EngineValidationOutput |
| [src/Glpi/Form/Condition/EngineVisibilityOutput.php](../src/Glpi/Form/Condition/EngineVisibilityOutput.php) | .php | class Glpi\Form\Condition\EngineVisibilityOutput |
| [src/Glpi/Form/Condition/FormData.php](../src/Glpi/Form/Condition/FormData.php) | .php | class Glpi\Form\Condition\FormData |
| [src/Glpi/Form/Condition/LogicOperator.php](../src/Glpi/Form/Condition/LogicOperator.php) | .php | enum Glpi\Form\Condition\LogicOperator |
| [src/Glpi/Form/Condition/QuestionData.php](../src/Glpi/Form/Condition/QuestionData.php) | .php | class Glpi\Form\Condition\QuestionData |
| [src/Glpi/Form/Condition/SectionData.php](../src/Glpi/Form/Condition/SectionData.php) | .php | class Glpi\Form\Condition\SectionData |
| [src/Glpi/Form/Condition/StrategyInterface.php](../src/Glpi/Form/Condition/StrategyInterface.php) | .php | interface Glpi\Form\Condition\StrategyInterface |
| [src/Glpi/Form/Condition/Type.php](../src/Glpi/Form/Condition/Type.php) | .php | enum Glpi\Form\Condition\Type |
| [src/Glpi/Form/Condition/UsedAsCriteriaInterface.php](../src/Glpi/Form/Condition/UsedAsCriteriaInterface.php) | .php | interface Glpi\Form\Condition\UsedAsCriteriaInterface |
| [src/Glpi/Form/Condition/ValidationStrategy.php](../src/Glpi/Form/Condition/ValidationStrategy.php) | .php | enum Glpi\Form\Condition\ValidationStrategy |
| [src/Glpi/Form/Condition/ValueOperator.php](../src/Glpi/Form/Condition/ValueOperator.php) | .php | enum Glpi\Form\Condition\ValueOperator |
| [src/Glpi/Form/Condition/VisibilityStrategy.php](../src/Glpi/Form/Condition/VisibilityStrategy.php) | .php | enum Glpi\Form\Condition\VisibilityStrategy |
| [src/Glpi/Form/DelegationData.php](../src/Glpi/Form/DelegationData.php) | .php | class Glpi\Form\DelegationData |
| [src/Glpi/Form/Destination/AbstractCommonITILFormDestination.php](../src/Glpi/Form/Destination/AbstractCommonITILFormDestination.php) | .php | class Glpi\Form\Destination\AbstractCommonITILFormDestination |
| [src/Glpi/Form/Destination/AbstractConfigField.php](../src/Glpi/Form/Destination/AbstractConfigField.php) | .php | class Glpi\Form\Destination\AbstractConfigField |
| [src/Glpi/Form/Destination/AnswersSet_FormDestinationItem.php](../src/Glpi/Form/Destination/AnswersSet_FormDestinationItem.php) | .php | class Glpi\Form\Destination\AnswersSet_FormDestinationItem extends CommonDBRelation |
| [src/Glpi/Form/Destination/CommonITILField/AbstractTextAreaField.php](../src/Glpi/Form/Destination/CommonITILField/AbstractTextAreaField.php) | .php | class Glpi\Form\Destination\CommonITILField\AbstractTextAreaField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/AssigneeField.php](../src/Glpi/Form/Destination/CommonITILField/AssigneeField.php) | .php | class Glpi\Form\Destination\CommonITILField\AssigneeField extends ITILActorField |
| [src/Glpi/Form/Destination/CommonITILField/AssigneeFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/AssigneeFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\AssigneeFieldConfig extends ITILActorFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/AssociatedItemsField.php](../src/Glpi/Form/Destination/CommonITILField/AssociatedItemsField.php) | .php | class Glpi\Form\Destination\CommonITILField\AssociatedItemsField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/AssociatedItemsFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/AssociatedItemsFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\AssociatedItemsFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/AssociatedItemsFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/AssociatedItemsFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\AssociatedItemsFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/BackupPlanField.php](../src/Glpi/Form/Destination/CommonITILField/BackupPlanField.php) | .php | class Glpi\Form\Destination\CommonITILField\BackupPlanField extends AbstractTextAreaField |
| [src/Glpi/Form/Destination/CommonITILField/Category.php](../src/Glpi/Form/Destination/CommonITILField/Category.php) | .php | enum Glpi\Form\Destination\CommonITILField\Category |
| [src/Glpi/Form/Destination/CommonITILField/CausesField.php](../src/Glpi/Form/Destination/CommonITILField/CausesField.php) | .php | class Glpi\Form\Destination\CommonITILField\CausesField extends AbstractTextAreaField |
| [src/Glpi/Form/Destination/CommonITILField/CheckListField.php](../src/Glpi/Form/Destination/CommonITILField/CheckListField.php) | .php | class Glpi\Form\Destination\CommonITILField\CheckListField extends AbstractTextAreaField |
| [src/Glpi/Form/Destination/CommonITILField/ContentField.php](../src/Glpi/Form/Destination/CommonITILField/ContentField.php) | .php | class Glpi\Form\Destination\CommonITILField\ContentField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/ControlsListField.php](../src/Glpi/Form/Destination/CommonITILField/ControlsListField.php) | .php | class Glpi\Form\Destination\CommonITILField\ControlsListField extends AbstractTextAreaField |
| [src/Glpi/Form/Destination/CommonITILField/DeploymentPlanField.php](../src/Glpi/Form/Destination/CommonITILField/DeploymentPlanField.php) | .php | class Glpi\Form\Destination\CommonITILField\DeploymentPlanField extends AbstractTextAreaField |
| [src/Glpi/Form/Destination/CommonITILField/EntityField.php](../src/Glpi/Form/Destination/CommonITILField/EntityField.php) | .php | class Glpi\Form\Destination\CommonITILField\EntityField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/EntityFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/EntityFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\EntityFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/EntityFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/EntityFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\EntityFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/ITILActorField.php](../src/Glpi/Form/Destination/CommonITILField/ITILActorField.php) | .php | class Glpi\Form\Destination\CommonITILField\ITILActorField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/ITILActorFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/ITILActorFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\ITILActorFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/ITILActorFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/ITILActorFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\ITILActorFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/ITILCategoryField.php](../src/Glpi/Form/Destination/CommonITILField/ITILCategoryField.php) | .php | class Glpi\Form\Destination\CommonITILField\ITILCategoryField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/ITILCategoryFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/ITILCategoryFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\ITILCategoryFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/ITILCategoryFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/ITILCategoryFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\ITILCategoryFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/ITILFollowupField.php](../src/Glpi/Form/Destination/CommonITILField/ITILFollowupField.php) | .php | class Glpi\Form\Destination\CommonITILField\ITILFollowupField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/ITILFollowupFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/ITILFollowupFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\ITILFollowupFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/ITILFollowupFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/ITILFollowupFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\ITILFollowupFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/ITILTaskField.php](../src/Glpi/Form/Destination/CommonITILField/ITILTaskField.php) | .php | class Glpi\Form\Destination\CommonITILField\ITILTaskField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/ITILTaskFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/ITILTaskFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\ITILTaskFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/ITILTaskFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/ITILTaskFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\ITILTaskFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/ImpactsField.php](../src/Glpi/Form/Destination/CommonITILField/ImpactsField.php) | .php | class Glpi\Form\Destination\CommonITILField\ImpactsField extends AbstractTextAreaField |
| [src/Glpi/Form/Destination/CommonITILField/LinkedITILObjectsField.php](../src/Glpi/Form/Destination/CommonITILField/LinkedITILObjectsField.php) | .php | class Glpi\Form\Destination\CommonITILField\LinkedITILObjectsField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/LinkedITILObjectsFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/LinkedITILObjectsFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\LinkedITILObjectsFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/LinkedITILObjectsFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/LinkedITILObjectsFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\LinkedITILObjectsFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/LinkedITILObjectsFieldStrategyConfig.php](../src/Glpi/Form/Destination/CommonITILField/LinkedITILObjectsFieldStrategyConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\LinkedITILObjectsFieldStrategyConfig |
| [src/Glpi/Form/Destination/CommonITILField/LocationField.php](../src/Glpi/Form/Destination/CommonITILField/LocationField.php) | .php | class Glpi\Form\Destination\CommonITILField\LocationField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/LocationFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/LocationFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\LocationFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/LocationFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/LocationFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\LocationFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/OLAField.php](../src/Glpi/Form/Destination/CommonITILField/OLAField.php) | .php | class Glpi\Form\Destination\CommonITILField\OLAField extends SLMField |
| [src/Glpi/Form/Destination/CommonITILField/OLATTOField.php](../src/Glpi/Form/Destination/CommonITILField/OLATTOField.php) | .php | class Glpi\Form\Destination\CommonITILField\OLATTOField extends OLAField |
| [src/Glpi/Form/Destination/CommonITILField/OLATTOFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/OLATTOFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\OLATTOFieldConfig extends SLMFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/OLATTRField.php](../src/Glpi/Form/Destination/CommonITILField/OLATTRField.php) | .php | class Glpi\Form\Destination\CommonITILField\OLATTRField extends OLAField |
| [src/Glpi/Form/Destination/CommonITILField/OLATTRFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/OLATTRFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\OLATTRFieldConfig extends SLMFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/ObserverField.php](../src/Glpi/Form/Destination/CommonITILField/ObserverField.php) | .php | class Glpi\Form\Destination\CommonITILField\ObserverField extends ITILActorField |
| [src/Glpi/Form/Destination/CommonITILField/ObserverFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/ObserverFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\ObserverFieldConfig extends ITILActorFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/RequestSourceField.php](../src/Glpi/Form/Destination/CommonITILField/RequestSourceField.php) | .php | class Glpi\Form\Destination\CommonITILField\RequestSourceField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/RequestSourceFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/RequestSourceFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\RequestSourceFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/RequestSourceFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/RequestSourceFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\RequestSourceFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/RequestTypeField.php](../src/Glpi/Form/Destination/CommonITILField/RequestTypeField.php) | .php | class Glpi\Form\Destination\CommonITILField\RequestTypeField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/RequestTypeFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/RequestTypeFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\RequestTypeFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/RequestTypeFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/RequestTypeFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\RequestTypeFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/RequesterField.php](../src/Glpi/Form/Destination/CommonITILField/RequesterField.php) | .php | class Glpi\Form\Destination\CommonITILField\RequesterField extends ITILActorField |
| [src/Glpi/Form/Destination/CommonITILField/RequesterFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/RequesterFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\RequesterFieldConfig extends ITILActorFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/SLAField.php](../src/Glpi/Form/Destination/CommonITILField/SLAField.php) | .php | class Glpi\Form\Destination\CommonITILField\SLAField extends SLMField |
| [src/Glpi/Form/Destination/CommonITILField/SLATTOField.php](../src/Glpi/Form/Destination/CommonITILField/SLATTOField.php) | .php | class Glpi\Form\Destination\CommonITILField\SLATTOField extends SLAField |
| [src/Glpi/Form/Destination/CommonITILField/SLATTOFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/SLATTOFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\SLATTOFieldConfig extends SLMFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/SLATTRField.php](../src/Glpi/Form/Destination/CommonITILField/SLATTRField.php) | .php | class Glpi\Form\Destination\CommonITILField\SLATTRField extends SLAField |
| [src/Glpi/Form/Destination/CommonITILField/SLATTRFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/SLATTRFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\SLATTRFieldConfig extends SLMFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/SLMField.php](../src/Glpi/Form/Destination/CommonITILField/SLMField.php) | .php | class Glpi\Form\Destination\CommonITILField\SLMField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/SLMFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/SLMFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\SLMFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/SLMFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/SLMFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\SLMFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/SimpleValueConfig.php](../src/Glpi/Form/Destination/CommonITILField/SimpleValueConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\SimpleValueConfig |
| [src/Glpi/Form/Destination/CommonITILField/StatusField.php](../src/Glpi/Form/Destination/CommonITILField/StatusField.php) | .php | class Glpi\Form\Destination\CommonITILField\StatusField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/SymptomsField.php](../src/Glpi/Form/Destination/CommonITILField/SymptomsField.php) | .php | class Glpi\Form\Destination\CommonITILField\SymptomsField extends AbstractTextAreaField |
| [src/Glpi/Form/Destination/CommonITILField/TemplateField.php](../src/Glpi/Form/Destination/CommonITILField/TemplateField.php) | .php | class Glpi\Form\Destination\CommonITILField\TemplateField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/TemplateFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/TemplateFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\TemplateFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/TemplateFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/TemplateFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\TemplateFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/TitleField.php](../src/Glpi/Form/Destination/CommonITILField/TitleField.php) | .php | class Glpi\Form\Destination\CommonITILField\TitleField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/UrgencyField.php](../src/Glpi/Form/Destination/CommonITILField/UrgencyField.php) | .php | class Glpi\Form\Destination\CommonITILField\UrgencyField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/UrgencyFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/UrgencyFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\UrgencyFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/UrgencyFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/UrgencyFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\UrgencyFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/ValidationField.php](../src/Glpi/Form/Destination/CommonITILField/ValidationField.php) | .php | class Glpi\Form\Destination\CommonITILField\ValidationField extends AbstractConfigField |
| [src/Glpi/Form/Destination/CommonITILField/ValidationFieldConfig.php](../src/Glpi/Form/Destination/CommonITILField/ValidationFieldConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\ValidationFieldConfig |
| [src/Glpi/Form/Destination/CommonITILField/ValidationFieldStrategy.php](../src/Glpi/Form/Destination/CommonITILField/ValidationFieldStrategy.php) | .php | enum Glpi\Form\Destination\CommonITILField\ValidationFieldStrategy |
| [src/Glpi/Form/Destination/CommonITILField/ValidationFieldStrategyConfig.php](../src/Glpi/Form/Destination/CommonITILField/ValidationFieldStrategyConfig.php) | .php | class Glpi\Form\Destination\CommonITILField\ValidationFieldStrategyConfig |
| [src/Glpi/Form/Destination/ConfigFieldWithStrategiesInterface.php](../src/Glpi/Form/Destination/ConfigFieldWithStrategiesInterface.php) | .php | interface Glpi\Form\Destination\ConfigFieldWithStrategiesInterface |
| [src/Glpi/Form/Destination/DeserializeStrategiesTrait.php](../src/Glpi/Form/Destination/DeserializeStrategiesTrait.php) | .php | trait Glpi\Form\Destination\DeserializeStrategiesTrait |
| [src/Glpi/Form/Destination/DestinationFieldInterface.php](../src/Glpi/Form/Destination/DestinationFieldInterface.php) | .php | interface Glpi\Form\Destination\DestinationFieldInterface |
| [src/Glpi/Form/Destination/FormDestination.php](../src/Glpi/Form/Destination/FormDestination.php) | .php | class Glpi\Form\Destination\FormDestination extends CommonDBChild |
| [src/Glpi/Form/Destination/FormDestinationChange.php](../src/Glpi/Form/Destination/FormDestinationChange.php) | .php | class Glpi\Form\Destination\FormDestinationChange extends AbstractCommonITILFormDestination |
| [src/Glpi/Form/Destination/FormDestinationInterface.php](../src/Glpi/Form/Destination/FormDestinationInterface.php) | .php | interface Glpi\Form\Destination\FormDestinationInterface |
| [src/Glpi/Form/Destination/FormDestinationManager.php](../src/Glpi/Form/Destination/FormDestinationManager.php) | .php | class Glpi\Form\Destination\FormDestinationManager |
| [src/Glpi/Form/Destination/FormDestinationProblem.php](../src/Glpi/Form/Destination/FormDestinationProblem.php) | .php | class Glpi\Form\Destination\FormDestinationProblem extends AbstractCommonITILFormDestination |
| [src/Glpi/Form/Destination/FormDestinationTicket.php](../src/Glpi/Form/Destination/FormDestinationTicket.php) | .php | class Glpi\Form\Destination\FormDestinationTicket extends AbstractCommonITILFormDestination |
| [src/Glpi/Form/Destination/HasFieldWithDestinationId.php](../src/Glpi/Form/Destination/HasFieldWithDestinationId.php) | .php | class Glpi\Form\Destination\HasFieldWithDestinationId |
| [src/Glpi/Form/Destination/HasFieldWithQuestionId.php](../src/Glpi/Form/Destination/HasFieldWithQuestionId.php) | .php | class Glpi\Form\Destination\HasFieldWithQuestionId |
| [src/Glpi/Form/Destination/HasFormTags.php](../src/Glpi/Form/Destination/HasFormTags.php) | .php | class Glpi\Form\Destination\HasFormTags |
| [src/Glpi/Form/Dropdown/FormActorsDropdown.php](../src/Glpi/Form/Dropdown/FormActorsDropdown.php) | .php | class Glpi\Form\Dropdown\FormActorsDropdown extends AbstractRightsDropdown |
| [src/Glpi/Form/EndUserInputNameProvider.php](../src/Glpi/Form/EndUserInputNameProvider.php) | .php | class Glpi\Form\EndUserInputNameProvider |
| [src/Glpi/Form/Export/Context/DatabaseMapper.php](../src/Glpi/Form/Export/Context/DatabaseMapper.php) | .php | class Glpi\Form\Export\Context\DatabaseMapper |
| [src/Glpi/Form/Export/Result/ExportResult.php](../src/Glpi/Form/Export/Result/ExportResult.php) | .php | class Glpi\Form\Export\Result\ExportResult |
| [src/Glpi/Form/Export/Result/ImportError.php](../src/Glpi/Form/Export/Result/ImportError.php) | .php | enum Glpi\Form\Export\Result\ImportError |
| [src/Glpi/Form/Export/Result/ImportResult.php](../src/Glpi/Form/Export/Result/ImportResult.php) | .php | class Glpi\Form\Export\Result\ImportResult |
| [src/Glpi/Form/Export/Result/ImportResultIssues.php](../src/Glpi/Form/Export/Result/ImportResultIssues.php) | .php | class Glpi\Form\Export\Result\ImportResultIssues |
| [src/Glpi/Form/Export/Result/ImportResultPreview.php](../src/Glpi/Form/Export/Result/ImportResultPreview.php) | .php | class Glpi\Form\Export\Result\ImportResultPreview |
| [src/Glpi/Form/Export/Serializer/AbstractFormSerializer.php](../src/Glpi/Form/Export/Serializer/AbstractFormSerializer.php) | .php | class Glpi\Form\Export\Serializer\AbstractFormSerializer |
| [src/Glpi/Form/Export/Serializer/CustomIllustrationContentSpecificationNormalizer.php](../src/Glpi/Form/Export/Serializer/CustomIllustrationContentSpecificationNormalizer.php) | .php | class Glpi\Form\Export\Serializer\CustomIllustrationContentSpecificationNormalizer |
| [src/Glpi/Form/Export/Serializer/DynamicExportData.php](../src/Glpi/Form/Export/Serializer/DynamicExportData.php) | .php | class Glpi\Form\Export\Serializer\DynamicExportData |
| [src/Glpi/Form/Export/Serializer/DynamicExportDataField.php](../src/Glpi/Form/Export/Serializer/DynamicExportDataField.php) | .php | class Glpi\Form\Export\Serializer\DynamicExportDataField |
| [src/Glpi/Form/Export/Serializer/FormSerializer.php](../src/Glpi/Form/Export/Serializer/FormSerializer.php) | .php | class Glpi\Form\Export\Serializer\FormSerializer extends AbstractFormSerializer |
| [src/Glpi/Form/Export/Specification/AccesControlPolicyContentSpecification.php](../src/Glpi/Form/Export/Specification/AccesControlPolicyContentSpecification.php) | .php | class Glpi\Form\Export\Specification\AccesControlPolicyContentSpecification |
| [src/Glpi/Form/Export/Specification/CommentContentSpecification.php](../src/Glpi/Form/Export/Specification/CommentContentSpecification.php) | .php | class Glpi\Form\Export\Specification\CommentContentSpecification |
| [src/Glpi/Form/Export/Specification/ConditionDataSpecification.php](../src/Glpi/Form/Export/Specification/ConditionDataSpecification.php) | .php | class Glpi\Form\Export\Specification\ConditionDataSpecification |
| [src/Glpi/Form/Export/Specification/ContentSpecificationInterface.php](../src/Glpi/Form/Export/Specification/ContentSpecificationInterface.php) | .php | interface Glpi\Form\Export\Specification\ContentSpecificationInterface |
| [src/Glpi/Form/Export/Specification/CustomIllustrationContentSpecification.php](../src/Glpi/Form/Export/Specification/CustomIllustrationContentSpecification.php) | .php | class Glpi\Form\Export\Specification\CustomIllustrationContentSpecification |
| [src/Glpi/Form/Export/Specification/CustomTypeRequirementSpecification.php](../src/Glpi/Form/Export/Specification/CustomTypeRequirementSpecification.php) | .php | class Glpi\Form\Export\Specification\CustomTypeRequirementSpecification |
| [src/Glpi/Form/Export/Specification/DataRequirementSpecification.php](../src/Glpi/Form/Export/Specification/DataRequirementSpecification.php) | .php | class Glpi\Form\Export\Specification\DataRequirementSpecification |
| [src/Glpi/Form/Export/Specification/DestinationContentSpecification.php](../src/Glpi/Form/Export/Specification/DestinationContentSpecification.php) | .php | class Glpi\Form\Export\Specification\DestinationContentSpecification |
| [src/Glpi/Form/Export/Specification/ExportContentSpecification.php](../src/Glpi/Form/Export/Specification/ExportContentSpecification.php) | .php | class Glpi\Form\Export\Specification\ExportContentSpecification |
| [src/Glpi/Form/Export/Specification/FormContentSpecification.php](../src/Glpi/Form/Export/Specification/FormContentSpecification.php) | .php | class Glpi\Form\Export\Specification\FormContentSpecification |
| [src/Glpi/Form/Export/Specification/PluginRequirementSpecification.php](../src/Glpi/Form/Export/Specification/PluginRequirementSpecification.php) | .php | class Glpi\Form\Export\Specification\PluginRequirementSpecification |
| [src/Glpi/Form/Export/Specification/QuestionContentSpecification.php](../src/Glpi/Form/Export/Specification/QuestionContentSpecification.php) | .php | class Glpi\Form\Export\Specification\QuestionContentSpecification |
| [src/Glpi/Form/Export/Specification/SectionContentSpecification.php](../src/Glpi/Form/Export/Specification/SectionContentSpecification.php) | .php | class Glpi\Form\Export\Specification\SectionContentSpecification |
| [src/Glpi/Form/Export/Specification/TranslationContentSpecification.php](../src/Glpi/Form/Export/Specification/TranslationContentSpecification.php) | .php | class Glpi\Form\Export\Specification\TranslationContentSpecification |
| [src/Glpi/Form/Form.php](../src/Glpi/Form/Form.php) | .php | class Glpi\Form\Form extends CommonDBTM |
| [src/Glpi/Form/FormTranslation.php](../src/Glpi/Form/FormTranslation.php) | .php | class Glpi\Form\FormTranslation extends ItemTranslation |
| [src/Glpi/Form/Migration/ConditionHandlerDataConverterInterface.php](../src/Glpi/Form/Migration/ConditionHandlerDataConverterInterface.php) | .php | interface Glpi\Form\Migration\ConditionHandlerDataConverterInterface |
| [src/Glpi/Form/Migration/DestinationFieldConverterInterface.php](../src/Glpi/Form/Migration/DestinationFieldConverterInterface.php) | .php | interface Glpi\Form\Migration\DestinationFieldConverterInterface |
| [src/Glpi/Form/Migration/FallbackToAnotherOperatorException.php](../src/Glpi/Form/Migration/FallbackToAnotherOperatorException.php) | .php | class Glpi\Form\Migration\FallbackToAnotherOperatorException extends Exception |
| [src/Glpi/Form/Migration/FormMigration.php](../src/Glpi/Form/Migration/FormMigration.php) | .php | class Glpi\Form\Migration\FormMigration extends AbstractPluginMigration |
| [src/Glpi/Form/Migration/FormQuestionDataConverterInterface.php](../src/Glpi/Form/Migration/FormQuestionDataConverterInterface.php) | .php | interface Glpi\Form\Migration\FormQuestionDataConverterInterface |
| [src/Glpi/Form/Migration/TagConversionTrait.php](../src/Glpi/Form/Migration/TagConversionTrait.php) | .php | trait Glpi\Form\Migration\TagConversionTrait |
| [src/Glpi/Form/Migration/TypesConversionMapper.php](../src/Glpi/Form/Migration/TypesConversionMapper.php) | .php | class Glpi\Form\Migration\TypesConversionMapper |
| [src/Glpi/Form/Migration/UnresolvedConditionValueException.php](../src/Glpi/Form/Migration/UnresolvedConditionValueException.php) | .php | class Glpi\Form\Migration\UnresolvedConditionValueException extends Exception |
| [src/Glpi/Form/Question.php](../src/Glpi/Form/Question.php) | .php | class Glpi\Form\Question extends CommonDBChild |
| [src/Glpi/Form/QuestionType/AbstractQuestionType.php](../src/Glpi/Form/QuestionType/AbstractQuestionType.php) | .php | class Glpi\Form\QuestionType\AbstractQuestionType |
| [src/Glpi/Form/QuestionType/AbstractQuestionTypeActors.php](../src/Glpi/Form/QuestionType/AbstractQuestionTypeActors.php) | .php | class Glpi\Form\QuestionType\AbstractQuestionTypeActors extends AbstractQuestionType |
| [src/Glpi/Form/QuestionType/AbstractQuestionTypeSelectable.php](../src/Glpi/Form/QuestionType/AbstractQuestionTypeSelectable.php) | .php | class Glpi\Form\QuestionType\AbstractQuestionTypeSelectable extends AbstractQuestionType |
| [src/Glpi/Form/QuestionType/AbstractQuestionTypeShortAnswer.php](../src/Glpi/Form/QuestionType/AbstractQuestionTypeShortAnswer.php) | .php | class Glpi\Form\QuestionType\AbstractQuestionTypeShortAnswer extends AbstractQuestionType |
| [src/Glpi/Form/QuestionType/CustomMandatoryMessageInterface.php](../src/Glpi/Form/QuestionType/CustomMandatoryMessageInterface.php) | .php | interface Glpi\Form\QuestionType\CustomMandatoryMessageInterface |
| [src/Glpi/Form/QuestionType/PredefinedValueValidationInterface.php](../src/Glpi/Form/QuestionType/PredefinedValueValidationInterface.php) | .php | interface Glpi\Form\QuestionType\PredefinedValueValidationInterface |
| [src/Glpi/Form/QuestionType/QuestionTypeActorsDefaultValueConfig.php](../src/Glpi/Form/QuestionType/QuestionTypeActorsDefaultValueConfig.php) | .php | class Glpi\Form\QuestionType\QuestionTypeActorsDefaultValueConfig |
| [src/Glpi/Form/QuestionType/QuestionTypeActorsExtraDataConfig.php](../src/Glpi/Form/QuestionType/QuestionTypeActorsExtraDataConfig.php) | .php | class Glpi\Form\QuestionType\QuestionTypeActorsExtraDataConfig |
| [src/Glpi/Form/QuestionType/QuestionTypeAssignee.php](../src/Glpi/Form/QuestionType/QuestionTypeAssignee.php) | .php | class Glpi\Form\QuestionType\QuestionTypeAssignee extends AbstractQuestionTypeActors |
| [src/Glpi/Form/QuestionType/QuestionTypeCategory.php](../src/Glpi/Form/QuestionType/QuestionTypeCategory.php) | .php | enum Glpi\Form\QuestionType\QuestionTypeCategory |
| [src/Glpi/Form/QuestionType/QuestionTypeCategoryInterface.php](../src/Glpi/Form/QuestionType/QuestionTypeCategoryInterface.php) | .php | interface Glpi\Form\QuestionType\QuestionTypeCategoryInterface |
| [src/Glpi/Form/QuestionType/QuestionTypeCheckbox.php](../src/Glpi/Form/QuestionType/QuestionTypeCheckbox.php) | .php | class Glpi\Form\QuestionType\QuestionTypeCheckbox extends AbstractQuestionTypeSelectable |
| [src/Glpi/Form/QuestionType/QuestionTypeDateTime.php](../src/Glpi/Form/QuestionType/QuestionTypeDateTime.php) | .php | class Glpi\Form\QuestionType\QuestionTypeDateTime extends AbstractQuestionType |
| [src/Glpi/Form/QuestionType/QuestionTypeDateTimeExtraDataConfig.php](../src/Glpi/Form/QuestionType/QuestionTypeDateTimeExtraDataConfig.php) | .php | class Glpi\Form\QuestionType\QuestionTypeDateTimeExtraDataConfig |
| [src/Glpi/Form/QuestionType/QuestionTypeDropdown.php](../src/Glpi/Form/QuestionType/QuestionTypeDropdown.php) | .php | class Glpi\Form\QuestionType\QuestionTypeDropdown extends AbstractQuestionTypeSelectable |
| [src/Glpi/Form/QuestionType/QuestionTypeDropdownExtraDataConfig.php](../src/Glpi/Form/QuestionType/QuestionTypeDropdownExtraDataConfig.php) | .php | class Glpi\Form\QuestionType\QuestionTypeDropdownExtraDataConfig extends QuestionTypeSelectableExtraDataConfig |
| [src/Glpi/Form/QuestionType/QuestionTypeEmail.php](../src/Glpi/Form/QuestionType/QuestionTypeEmail.php) | .php | class Glpi\Form\QuestionType\QuestionTypeEmail extends AbstractQuestionTypeShortAnswer |
| [src/Glpi/Form/QuestionType/QuestionTypeFile.php](../src/Glpi/Form/QuestionType/QuestionTypeFile.php) | .php | class Glpi\Form\QuestionType\QuestionTypeFile extends AbstractQuestionType |
| [src/Glpi/Form/QuestionType/QuestionTypeInterface.php](../src/Glpi/Form/QuestionType/QuestionTypeInterface.php) | .php | interface Glpi\Form\QuestionType\QuestionTypeInterface extends UsedAsCriteriaInterface |
| [src/Glpi/Form/QuestionType/QuestionTypeItem.php](../src/Glpi/Form/QuestionType/QuestionTypeItem.php) | .php | class Glpi\Form\QuestionType\QuestionTypeItem extends AbstractQuestionType |
| [src/Glpi/Form/QuestionType/QuestionTypeItemDefaultValueConfig.php](../src/Glpi/Form/QuestionType/QuestionTypeItemDefaultValueConfig.php) | .php | class Glpi\Form\QuestionType\QuestionTypeItemDefaultValueConfig |
| [src/Glpi/Form/QuestionType/QuestionTypeItemDropdown.php](../src/Glpi/Form/QuestionType/QuestionTypeItemDropdown.php) | .php | class Glpi\Form\QuestionType\QuestionTypeItemDropdown extends QuestionTypeItem |
| [src/Glpi/Form/QuestionType/QuestionTypeItemDropdownExtraDataConfig.php](../src/Glpi/Form/QuestionType/QuestionTypeItemDropdownExtraDataConfig.php) | .php | class Glpi\Form\QuestionType\QuestionTypeItemDropdownExtraDataConfig extends QuestionTypeItemExtraDataConfig |
| [src/Glpi/Form/QuestionType/QuestionTypeItemExtraDataConfig.php](../src/Glpi/Form/QuestionType/QuestionTypeItemExtraDataConfig.php) | .php | class Glpi\Form\QuestionType\QuestionTypeItemExtraDataConfig |
| [src/Glpi/Form/QuestionType/QuestionTypeLongText.php](../src/Glpi/Form/QuestionType/QuestionTypeLongText.php) | .php | class Glpi\Form\QuestionType\QuestionTypeLongText extends AbstractQuestionType |
| [src/Glpi/Form/QuestionType/QuestionTypeNumber.php](../src/Glpi/Form/QuestionType/QuestionTypeNumber.php) | .php | class Glpi\Form\QuestionType\QuestionTypeNumber extends AbstractQuestionTypeShortAnswer |
| [src/Glpi/Form/QuestionType/QuestionTypeObserver.php](../src/Glpi/Form/QuestionType/QuestionTypeObserver.php) | .php | class Glpi\Form\QuestionType\QuestionTypeObserver extends AbstractQuestionTypeActors |
| [src/Glpi/Form/QuestionType/QuestionTypeRadio.php](../src/Glpi/Form/QuestionType/QuestionTypeRadio.php) | .php | class Glpi\Form\QuestionType\QuestionTypeRadio extends AbstractQuestionTypeSelectable |
| [src/Glpi/Form/QuestionType/QuestionTypeRequestType.php](../src/Glpi/Form/QuestionType/QuestionTypeRequestType.php) | .php | class Glpi\Form\QuestionType\QuestionTypeRequestType extends AbstractQuestionType |
| [src/Glpi/Form/QuestionType/QuestionTypeRequester.php](../src/Glpi/Form/QuestionType/QuestionTypeRequester.php) | .php | class Glpi\Form\QuestionType\QuestionTypeRequester extends AbstractQuestionTypeActors |
| [src/Glpi/Form/QuestionType/QuestionTypeSelectableExtraDataConfig.php](../src/Glpi/Form/QuestionType/QuestionTypeSelectableExtraDataConfig.php) | .php | class Glpi\Form\QuestionType\QuestionTypeSelectableExtraDataConfig |
| [src/Glpi/Form/QuestionType/QuestionTypeShortText.php](../src/Glpi/Form/QuestionType/QuestionTypeShortText.php) | .php | class Glpi\Form\QuestionType\QuestionTypeShortText extends AbstractQuestionTypeShortAnswer |
| [src/Glpi/Form/QuestionType/QuestionTypeUrgency.php](../src/Glpi/Form/QuestionType/QuestionTypeUrgency.php) | .php | class Glpi\Form\QuestionType\QuestionTypeUrgency extends AbstractQuestionType |
| [src/Glpi/Form/QuestionType/QuestionTypeUserDevice.php](../src/Glpi/Form/QuestionType/QuestionTypeUserDevice.php) | .php | class Glpi\Form\QuestionType\QuestionTypeUserDevice extends AbstractQuestionType |
| [src/Glpi/Form/QuestionType/QuestionTypeUserDevicesConfig.php](../src/Glpi/Form/QuestionType/QuestionTypeUserDevicesConfig.php) | .php | class Glpi\Form\QuestionType\QuestionTypeUserDevicesConfig |
| [src/Glpi/Form/QuestionType/QuestionTypeValidationInterface.php](../src/Glpi/Form/QuestionType/QuestionTypeValidationInterface.php) | .php | interface Glpi\Form\QuestionType\QuestionTypeValidationInterface |
| [src/Glpi/Form/QuestionType/QuestionTypesManager.php](../src/Glpi/Form/QuestionType/QuestionTypesManager.php) | .php | class Glpi\Form\QuestionType\QuestionTypesManager |
| [src/Glpi/Form/QuestionType/RawAnswerIsHtmlInterface.php](../src/Glpi/Form/QuestionType/RawAnswerIsHtmlInterface.php) | .php | interface Glpi\Form\QuestionType\RawAnswerIsHtmlInterface |
| [src/Glpi/Form/QuestionType/TranslationAwareQuestionType.php](../src/Glpi/Form/QuestionType/TranslationAwareQuestionType.php) | .php | interface Glpi\Form\QuestionType\TranslationAwareQuestionType |
| [src/Glpi/Form/RenderLayout.php](../src/Glpi/Form/RenderLayout.php) | .php | enum Glpi\Form\RenderLayout |
| [src/Glpi/Form/Section.php](../src/Glpi/Form/Section.php) | .php | class Glpi\Form\Section extends CommonDBChild |
| [src/Glpi/Form/ServiceCatalog/HomeSearchManager.php](../src/Glpi/Form/ServiceCatalog/HomeSearchManager.php) | .php | class Glpi\Form\ServiceCatalog\HomeSearchManager |
| [src/Glpi/Form/ServiceCatalog/ItemRequest.php](../src/Glpi/Form/ServiceCatalog/ItemRequest.php) | .php | class Glpi\Form\ServiceCatalog\ItemRequest |
| [src/Glpi/Form/ServiceCatalog/ItemRequestContext.php](../src/Glpi/Form/ServiceCatalog/ItemRequestContext.php) | .php | enum Glpi\Form\ServiceCatalog\ItemRequestContext |
| [src/Glpi/Form/ServiceCatalog/Provider/CategoryProvider.php](../src/Glpi/Form/ServiceCatalog/Provider/CategoryProvider.php) | .php | class Glpi\Form\ServiceCatalog\Provider\CategoryProvider |
| [src/Glpi/Form/ServiceCatalog/Provider/CompositeProviderInterface.php](../src/Glpi/Form/ServiceCatalog/Provider/CompositeProviderInterface.php) | .php | interface Glpi\Form\ServiceCatalog\Provider\CompositeProviderInterface extends ItemProviderInterface |
| [src/Glpi/Form/ServiceCatalog/Provider/FormProvider.php](../src/Glpi/Form/ServiceCatalog/Provider/FormProvider.php) | .php | class Glpi\Form\ServiceCatalog\Provider\FormProvider |
| [src/Glpi/Form/ServiceCatalog/Provider/ItemProviderInterface.php](../src/Glpi/Form/ServiceCatalog/Provider/ItemProviderInterface.php) | .php | interface Glpi\Form\ServiceCatalog\Provider\ItemProviderInterface |
| [src/Glpi/Form/ServiceCatalog/Provider/KnowbaseItemProvider.php](../src/Glpi/Form/ServiceCatalog/Provider/KnowbaseItemProvider.php) | .php | class Glpi\Form\ServiceCatalog\Provider\KnowbaseItemProvider |
| [src/Glpi/Form/ServiceCatalog/Provider/LeafProviderInterface.php](../src/Glpi/Form/ServiceCatalog/Provider/LeafProviderInterface.php) | .php | interface Glpi\Form\ServiceCatalog\Provider\LeafProviderInterface extends ItemProviderInterface |
| [src/Glpi/Form/ServiceCatalog/ServiceCatalog.php](../src/Glpi/Form/ServiceCatalog/ServiceCatalog.php) | .php | class Glpi\Form\ServiceCatalog\ServiceCatalog extends CommonGLPI |
| [src/Glpi/Form/ServiceCatalog/ServiceCatalogCompositeInterface.php](../src/Glpi/Form/ServiceCatalog/ServiceCatalogCompositeInterface.php) | .php | interface Glpi\Form\ServiceCatalog\ServiceCatalogCompositeInterface extends ServiceCatalogItemInterface |
| [src/Glpi/Form/ServiceCatalog/ServiceCatalogItemInterface.php](../src/Glpi/Form/ServiceCatalog/ServiceCatalogItemInterface.php) | .php | interface Glpi\Form\ServiceCatalog\ServiceCatalogItemInterface |
| [src/Glpi/Form/ServiceCatalog/ServiceCatalogLeafInterface.php](../src/Glpi/Form/ServiceCatalog/ServiceCatalogLeafInterface.php) | .php | interface Glpi\Form\ServiceCatalog\ServiceCatalogLeafInterface extends ServiceCatalogItemInterface |
| [src/Glpi/Form/ServiceCatalog/ServiceCatalogManager.php](../src/Glpi/Form/ServiceCatalog/ServiceCatalogManager.php) | .php | class Glpi\Form\ServiceCatalog\ServiceCatalogManager |
| [src/Glpi/Form/ServiceCatalog/SortStrategy/AbstractSortStrategy.php](../src/Glpi/Form/ServiceCatalog/SortStrategy/AbstractSortStrategy.php) | .php | class Glpi\Form\ServiceCatalog\SortStrategy\AbstractSortStrategy |
| [src/Glpi/Form/ServiceCatalog/SortStrategy/AlphabeticalSort.php](../src/Glpi/Form/ServiceCatalog/SortStrategy/AlphabeticalSort.php) | .php | class Glpi\Form\ServiceCatalog\SortStrategy\AlphabeticalSort extends AbstractSortStrategy |
| [src/Glpi/Form/ServiceCatalog/SortStrategy/PopularitySort.php](../src/Glpi/Form/ServiceCatalog/SortStrategy/PopularitySort.php) | .php | class Glpi\Form\ServiceCatalog\SortStrategy\PopularitySort extends AbstractSortStrategy |
| [src/Glpi/Form/ServiceCatalog/SortStrategy/ReverseAlphabeticalSort.php](../src/Glpi/Form/ServiceCatalog/SortStrategy/ReverseAlphabeticalSort.php) | .php | class Glpi\Form\ServiceCatalog\SortStrategy\ReverseAlphabeticalSort extends AbstractSortStrategy |
| [src/Glpi/Form/ServiceCatalog/SortStrategy/SortStrategyEnum.php](../src/Glpi/Form/ServiceCatalog/SortStrategy/SortStrategyEnum.php) | .php | enum Glpi\Form\ServiceCatalog\SortStrategy\SortStrategyEnum |
| [src/Glpi/Form/ServiceCatalog/SortStrategy/SortStrategyInterface.php](../src/Glpi/Form/ServiceCatalog/SortStrategy/SortStrategyInterface.php) | .php | interface Glpi\Form\ServiceCatalog\SortStrategy\SortStrategyInterface |
| [src/Glpi/Form/Tag/AnswerTagProvider.php](../src/Glpi/Form/Tag/AnswerTagProvider.php) | .php | class Glpi\Form\Tag\AnswerTagProvider |
| [src/Glpi/Form/Tag/CommentDescriptionTagProvider.php](../src/Glpi/Form/Tag/CommentDescriptionTagProvider.php) | .php | class Glpi\Form\Tag\CommentDescriptionTagProvider |
| [src/Glpi/Form/Tag/CommentTitleTagProvider.php](../src/Glpi/Form/Tag/CommentTitleTagProvider.php) | .php | class Glpi\Form\Tag\CommentTitleTagProvider |
| [src/Glpi/Form/Tag/CompositeTagValueInterface.php](../src/Glpi/Form/Tag/CompositeTagValueInterface.php) | .php | interface Glpi\Form\Tag\CompositeTagValueInterface extends TagWithIdValueInterface |
| [src/Glpi/Form/Tag/FormTagProvider.php](../src/Glpi/Form/Tag/FormTagProvider.php) | .php | class Glpi\Form\Tag\FormTagProvider |
| [src/Glpi/Form/Tag/FormTagsManager.php](../src/Glpi/Form/Tag/FormTagsManager.php) | .php | class Glpi\Form\Tag\FormTagsManager |
| [src/Glpi/Form/Tag/FullFormTagProvider.php](../src/Glpi/Form/Tag/FullFormTagProvider.php) | .php | class Glpi\Form\Tag\FullFormTagProvider |
| [src/Glpi/Form/Tag/ItemPropertyTagProvider.php](../src/Glpi/Form/Tag/ItemPropertyTagProvider.php) | .php | class Glpi\Form\Tag\ItemPropertyTagProvider |
| [src/Glpi/Form/Tag/QuestionTagProvider.php](../src/Glpi/Form/Tag/QuestionTagProvider.php) | .php | class Glpi\Form\Tag\QuestionTagProvider |
| [src/Glpi/Form/Tag/SectionTagProvider.php](../src/Glpi/Form/Tag/SectionTagProvider.php) | .php | class Glpi\Form\Tag\SectionTagProvider |
| [src/Glpi/Form/Tag/Tag.php](../src/Glpi/Form/Tag/Tag.php) | .php | class Glpi\Form\Tag\Tag |
| [src/Glpi/Form/Tag/TagProviderInterface.php](../src/Glpi/Form/Tag/TagProviderInterface.php) | .php | interface Glpi\Form\Tag\TagProviderInterface |
| [src/Glpi/Form/Tag/TagWithIdValueInterface.php](../src/Glpi/Form/Tag/TagWithIdValueInterface.php) | .php | interface Glpi\Form\Tag\TagWithIdValueInterface |
| [src/Glpi/Form/ValidationResult.php](../src/Glpi/Form/ValidationResult.php) | .php | class Glpi\Form\ValidationResult |
| [src/Glpi/FuzzyMatcher/FuzzyMatcher.php](../src/Glpi/FuzzyMatcher/FuzzyMatcher.php) | .php | class Glpi\FuzzyMatcher\FuzzyMatcher |
| [src/Glpi/FuzzyMatcher/FuzzyMatcherStrategyInterface.php](../src/Glpi/FuzzyMatcher/FuzzyMatcherStrategyInterface.php) | .php | interface Glpi\FuzzyMatcher\FuzzyMatcherStrategyInterface |
| [src/Glpi/FuzzyMatcher/PartialMatchStrategy.php](../src/Glpi/FuzzyMatcher/PartialMatchStrategy.php) | .php | class Glpi\FuzzyMatcher\PartialMatchStrategy |
| [src/Glpi/Helpdesk/DefaultDataManager.php](../src/Glpi/Helpdesk/DefaultDataManager.php) | .php | class Glpi\Helpdesk\DefaultDataManager |
| [src/Glpi/Helpdesk/HelpdeskTranslation.php](../src/Glpi/Helpdesk/HelpdeskTranslation.php) | .php | class Glpi\Helpdesk\HelpdeskTranslation extends ItemTranslation |
| [src/Glpi/Helpdesk/HomePageTabs.php](../src/Glpi/Helpdesk/HomePageTabs.php) | .php | class Glpi\Helpdesk\HomePageTabs extends CommonGLPI |
| [src/Glpi/Helpdesk/Tile/ExternalPageTile.php](../src/Glpi/Helpdesk/Tile/ExternalPageTile.php) | .php | class Glpi\Helpdesk\Tile\ExternalPageTile extends CommonDBTM |
| [src/Glpi/Helpdesk/Tile/FormTile.php](../src/Glpi/Helpdesk/Tile/FormTile.php) | .php | class Glpi\Helpdesk\Tile\FormTile extends CommonDBChild |
| [src/Glpi/Helpdesk/Tile/GlpiPageTile.php](../src/Glpi/Helpdesk/Tile/GlpiPageTile.php) | .php | class Glpi\Helpdesk\Tile\GlpiPageTile extends CommonDBTM |
| [src/Glpi/Helpdesk/Tile/InvalidTileException.php](../src/Glpi/Helpdesk/Tile/InvalidTileException.php) | .php | class Glpi\Helpdesk\Tile\InvalidTileException extends RuntimeException |
| [src/Glpi/Helpdesk/Tile/Item_Tile.php](../src/Glpi/Helpdesk/Tile/Item_Tile.php) | .php | class Glpi\Helpdesk\Tile\Item_Tile extends CommonDBRelation |
| [src/Glpi/Helpdesk/Tile/LinkableToTilesInterface.php](../src/Glpi/Helpdesk/Tile/LinkableToTilesInterface.php) | .php | interface Glpi\Helpdesk\Tile\LinkableToTilesInterface |
| [src/Glpi/Helpdesk/Tile/TileInterface.php](../src/Glpi/Helpdesk/Tile/TileInterface.php) | .php | interface Glpi\Helpdesk\Tile\TileInterface |
| [src/Glpi/Helpdesk/Tile/TileRightTrait.php](../src/Glpi/Helpdesk/Tile/TileRightTrait.php) | .php | trait Glpi\Helpdesk\Tile\TileRightTrait |
| [src/Glpi/Helpdesk/Tile/TilesManager.php](../src/Glpi/Helpdesk/Tile/TilesManager.php) | .php | class Glpi\Helpdesk\Tile\TilesManager |
| [src/Glpi/Http/Firewall.php](../src/Glpi/Http/Firewall.php) | .php | class Glpi\Http\Firewall |
| [src/Glpi/Http/HeaderlessStreamedResponse.php](../src/Glpi/Http/HeaderlessStreamedResponse.php) | .php | class Glpi\Http\HeaderlessStreamedResponse extends StreamedResponse |
| [src/Glpi/Http/JSONResponse.php](../src/Glpi/Http/JSONResponse.php) | .php | class Glpi\Http\JSONResponse extends Response |
| [src/Glpi/Http/RedirectResponse.php](../src/Glpi/Http/RedirectResponse.php) | .php | class Glpi\Http\RedirectResponse extends \Symfony\Component\HttpFoundation\RedirectResponse |
| [src/Glpi/Http/Request.php](../src/Glpi/Http/Request.php) | .php | class Glpi\Http\Request extends ServerRequest |
| [src/Glpi/Http/RequestRouterTrait.php](../src/Glpi/Http/RequestRouterTrait.php) | .php | trait Glpi\Http\RequestRouterTrait |
| [src/Glpi/Http/Response.php](../src/Glpi/Http/Response.php) | .php | class Glpi\Http\Response extends \GuzzleHttp\Psr7\Response |
| [src/Glpi/Http/SessionManager.php](../src/Glpi/Http/SessionManager.php) | .php | class Glpi\Http\SessionManager |
| [src/Glpi/Inventory/Asset/Antivirus.php](../src/Glpi/Inventory/Asset/Antivirus.php) | .php | class Glpi\Inventory\Asset\Antivirus extends InventoryAsset |
| [src/Glpi/Inventory/Asset/Battery.php](../src/Glpi/Inventory/Asset/Battery.php) | .php | class Glpi\Inventory\Asset\Battery extends Device |
| [src/Glpi/Inventory/Asset/Bios.php](../src/Glpi/Inventory/Asset/Bios.php) | .php | class Glpi\Inventory\Asset\Bios extends Device |
| [src/Glpi/Inventory/Asset/Camera.php](../src/Glpi/Inventory/Asset/Camera.php) | .php | class Glpi\Inventory\Asset\Camera extends Device |
| [src/Glpi/Inventory/Asset/Cartridge.php](../src/Glpi/Inventory/Asset/Cartridge.php) | .php | class Glpi\Inventory\Asset\Cartridge extends InventoryAsset |
| [src/Glpi/Inventory/Asset/Controller.php](../src/Glpi/Inventory/Asset/Controller.php) | .php | class Glpi\Inventory\Asset\Controller extends Device |
| [src/Glpi/Inventory/Asset/DatabaseInstance.php](../src/Glpi/Inventory/Asset/DatabaseInstance.php) | .php | class Glpi\Inventory\Asset\DatabaseInstance extends InventoryAsset |
| [src/Glpi/Inventory/Asset/Device.php](../src/Glpi/Inventory/Asset/Device.php) | .php | class Glpi\Inventory\Asset\Device extends InventoryAsset |
| [src/Glpi/Inventory/Asset/Drive.php](../src/Glpi/Inventory/Asset/Drive.php) | .php | class Glpi\Inventory\Asset\Drive extends Device |
| [src/Glpi/Inventory/Asset/Environment.php](../src/Glpi/Inventory/Asset/Environment.php) | .php | class Glpi\Inventory\Asset\Environment extends InventoryAsset |
| [src/Glpi/Inventory/Asset/Firmware.php](../src/Glpi/Inventory/Asset/Firmware.php) | .php | class Glpi\Inventory\Asset\Firmware extends Device |
| [src/Glpi/Inventory/Asset/GraphicCard.php](../src/Glpi/Inventory/Asset/GraphicCard.php) | .php | class Glpi\Inventory\Asset\GraphicCard extends Device |
| [src/Glpi/Inventory/Asset/HardDrive.php](../src/Glpi/Inventory/Asset/HardDrive.php) | .php | class Glpi\Inventory\Asset\HardDrive extends Device |
| [src/Glpi/Inventory/Asset/InventoryAsset.php](../src/Glpi/Inventory/Asset/InventoryAsset.php) | .php | class Glpi\Inventory\Asset\InventoryAsset |
| [src/Glpi/Inventory/Asset/InventoryNetworkPort.php](../src/Glpi/Inventory/Asset/InventoryNetworkPort.php) | .php | trait Glpi\Inventory\Asset\InventoryNetworkPort |
| [src/Glpi/Inventory/Asset/Memory.php](../src/Glpi/Inventory/Asset/Memory.php) | .php | class Glpi\Inventory\Asset\Memory extends Device |
| [src/Glpi/Inventory/Asset/Monitor.php](../src/Glpi/Inventory/Asset/Monitor.php) | .php | class Glpi\Inventory\Asset\Monitor extends InventoryAsset |
| [src/Glpi/Inventory/Asset/NetworkCard.php](../src/Glpi/Inventory/Asset/NetworkCard.php) | .php | class Glpi\Inventory\Asset\NetworkCard extends Device |
| [src/Glpi/Inventory/Asset/NetworkPort.php](../src/Glpi/Inventory/Asset/NetworkPort.php) | .php | class Glpi\Inventory\Asset\NetworkPort extends InventoryAsset |
| [src/Glpi/Inventory/Asset/OperatingSystem.php](../src/Glpi/Inventory/Asset/OperatingSystem.php) | .php | class Glpi\Inventory\Asset\OperatingSystem extends InventoryAsset |
| [src/Glpi/Inventory/Asset/Peripheral.php](../src/Glpi/Inventory/Asset/Peripheral.php) | .php | class Glpi\Inventory\Asset\Peripheral extends InventoryAsset |
| [src/Glpi/Inventory/Asset/Plug.php](../src/Glpi/Inventory/Asset/Plug.php) | .php | class Glpi\Inventory\Asset\Plug extends InventoryAsset |
| [src/Glpi/Inventory/Asset/PowerSupply.php](../src/Glpi/Inventory/Asset/PowerSupply.php) | .php | class Glpi\Inventory\Asset\PowerSupply extends Device |
| [src/Glpi/Inventory/Asset/Printer.php](../src/Glpi/Inventory/Asset/Printer.php) | .php | class Glpi\Inventory\Asset\Printer extends InventoryAsset |
| [src/Glpi/Inventory/Asset/Process.php](../src/Glpi/Inventory/Asset/Process.php) | .php | class Glpi\Inventory\Asset\Process extends InventoryAsset |
| [src/Glpi/Inventory/Asset/Processor.php](../src/Glpi/Inventory/Asset/Processor.php) | .php | class Glpi\Inventory\Asset\Processor extends Device |
| [src/Glpi/Inventory/Asset/RemoteManagement.php](../src/Glpi/Inventory/Asset/RemoteManagement.php) | .php | class Glpi\Inventory\Asset\RemoteManagement extends InventoryAsset |
| [src/Glpi/Inventory/Asset/Sensor.php](../src/Glpi/Inventory/Asset/Sensor.php) | .php | class Glpi\Inventory\Asset\Sensor extends Device |
| [src/Glpi/Inventory/Asset/Simcard.php](../src/Glpi/Inventory/Asset/Simcard.php) | .php | class Glpi\Inventory\Asset\Simcard extends Device |
| [src/Glpi/Inventory/Asset/Software.php](../src/Glpi/Inventory/Asset/Software.php) | .php | class Glpi\Inventory\Asset\Software extends InventoryAsset |
| [src/Glpi/Inventory/Asset/SoundCard.php](../src/Glpi/Inventory/Asset/SoundCard.php) | .php | class Glpi\Inventory\Asset\SoundCard extends Device |
| [src/Glpi/Inventory/Asset/VirtualMachine.php](../src/Glpi/Inventory/Asset/VirtualMachine.php) | .php | class Glpi\Inventory\Asset\VirtualMachine extends InventoryAsset |
| [src/Glpi/Inventory/Asset/Volume.php](../src/Glpi/Inventory/Asset/Volume.php) | .php | class Glpi\Inventory\Asset\Volume extends InventoryAsset |
| [src/Glpi/Inventory/Conf.php](../src/Glpi/Inventory/Conf.php) | .php | class Glpi\Inventory\Conf extends CommonGLPI |
| [src/Glpi/Inventory/ImportResult.php](../src/Glpi/Inventory/ImportResult.php) | .php | class Glpi\Inventory\ImportResult |
| [src/Glpi/Inventory/Inventory.php](../src/Glpi/Inventory/Inventory.php) | .php | class Glpi\Inventory\Inventory |
| [src/Glpi/Inventory/MainAsset/Computer.php](../src/Glpi/Inventory/MainAsset/Computer.php) | .php | class Glpi\Inventory\MainAsset\Computer extends MainAsset |
| [src/Glpi/Inventory/MainAsset/GenericAsset.php](../src/Glpi/Inventory/MainAsset/GenericAsset.php) | .php | class Glpi\Inventory\MainAsset\GenericAsset extends Computer |
| [src/Glpi/Inventory/MainAsset/GenericNetworkAsset.php](../src/Glpi/Inventory/MainAsset/GenericNetworkAsset.php) | .php | class Glpi\Inventory\MainAsset\GenericNetworkAsset extends NetworkEquipment |
| [src/Glpi/Inventory/MainAsset/GenericPrinterAsset.php](../src/Glpi/Inventory/MainAsset/GenericPrinterAsset.php) | .php | class Glpi\Inventory\MainAsset\GenericPrinterAsset extends Printer |
| [src/Glpi/Inventory/MainAsset/Itemtype.php](../src/Glpi/Inventory/MainAsset/Itemtype.php) | .php | class Glpi\Inventory\MainAsset\Itemtype extends MainAsset |
| [src/Glpi/Inventory/MainAsset/MainAsset.php](../src/Glpi/Inventory/MainAsset/MainAsset.php) | .php | class Glpi\Inventory\MainAsset\MainAsset extends InventoryAsset |
| [src/Glpi/Inventory/MainAsset/NetworkEquipment.php](../src/Glpi/Inventory/MainAsset/NetworkEquipment.php) | .php | class Glpi\Inventory\MainAsset\NetworkEquipment extends MainAsset |
| [src/Glpi/Inventory/MainAsset/PDU.php](../src/Glpi/Inventory/MainAsset/PDU.php) | .php | class Glpi\Inventory\MainAsset\PDU extends NetworkEquipment |
| [src/Glpi/Inventory/MainAsset/Phone.php](../src/Glpi/Inventory/MainAsset/Phone.php) | .php | class Glpi\Inventory\MainAsset\Phone extends MainAsset |
| [src/Glpi/Inventory/MainAsset/Printer.php](../src/Glpi/Inventory/MainAsset/Printer.php) | .php | class Glpi\Inventory\MainAsset\Printer extends NetworkEquipment |
| [src/Glpi/Inventory/MainAsset/Unmanaged.php](../src/Glpi/Inventory/MainAsset/Unmanaged.php) | .php | class Glpi\Inventory\MainAsset\Unmanaged extends MainAsset |
| [src/Glpi/Inventory/Request.php](../src/Glpi/Inventory/Request.php) | .php | class Glpi\Inventory\Request extends AbstractRequest |
| [src/Glpi/ItemTranslation/CldrLanguage.php](../src/Glpi/ItemTranslation/CldrLanguage.php) | .php | class Glpi\ItemTranslation\CldrLanguage |
| [src/Glpi/ItemTranslation/Context/ProvideTranslationsInterface.php](../src/Glpi/ItemTranslation/Context/ProvideTranslationsInterface.php) | .php | interface Glpi\ItemTranslation\Context\ProvideTranslationsInterface |
| [src/Glpi/ItemTranslation/Context/TranslationHandler.php](../src/Glpi/ItemTranslation/Context/TranslationHandler.php) | .php | class Glpi\ItemTranslation\Context\TranslationHandler |
| [src/Glpi/ItemTranslation/ItemTranslation.php](../src/Glpi/ItemTranslation/ItemTranslation.php) | .php | class Glpi\ItemTranslation\ItemTranslation extends CommonDBChild |
| [src/Glpi/Kernel/Kernel.php](../src/Glpi/Kernel/Kernel.php) | .php | class Glpi\Kernel\Kernel extends BaseKernel |
| [src/Glpi/Kernel/KernelListenerTrait.php](../src/Glpi/Kernel/KernelListenerTrait.php) | .php | trait Glpi\Kernel\KernelListenerTrait |
| [src/Glpi/Kernel/Listener/ControllerListener/CheckCsrfListener.php](../src/Glpi/Kernel/Listener/ControllerListener/CheckCsrfListener.php) | .php | class Glpi\Kernel\Listener\ControllerListener\CheckCsrfListener |
| [src/Glpi/Kernel/Listener/ControllerListener/FirewallStrategyListener.php](../src/Glpi/Kernel/Listener/ControllerListener/FirewallStrategyListener.php) | .php | class Glpi\Kernel\Listener\ControllerListener\FirewallStrategyListener |
| [src/Glpi/Kernel/Listener/ExceptionListener/AccessErrorListener.php](../src/Glpi/Kernel/Listener/ExceptionListener/AccessErrorListener.php) | .php | class Glpi\Kernel\Listener\ExceptionListener\AccessErrorListener |
| [src/Glpi/Kernel/Listener/ExceptionListener/ProgressErrorListener.php](../src/Glpi/Kernel/Listener/ExceptionListener/ProgressErrorListener.php) | .php | class Glpi\Kernel\Listener\ExceptionListener\ProgressErrorListener |
| [src/Glpi/Kernel/Listener/ExceptionListener/RedirectExceptionListener.php](../src/Glpi/Kernel/Listener/ExceptionListener/RedirectExceptionListener.php) | .php | class Glpi\Kernel\Listener\ExceptionListener\RedirectExceptionListener |
| [src/Glpi/Kernel/Listener/PostBootListener/BootPlugins.php](../src/Glpi/Kernel/Listener/PostBootListener/BootPlugins.php) | .php | class Glpi\Kernel\Listener\PostBootListener\BootPlugins |
| [src/Glpi/Kernel/Listener/PostBootListener/CheckPluginsStates.php](../src/Glpi/Kernel/Listener/PostBootListener/CheckPluginsStates.php) | .php | class Glpi\Kernel\Listener\PostBootListener\CheckPluginsStates |
| [src/Glpi/Kernel/Listener/PostBootListener/CustomObjectsAutoloaderRegistration.php](../src/Glpi/Kernel/Listener/PostBootListener/CustomObjectsAutoloaderRegistration.php) | .php | class Glpi\Kernel\Listener\PostBootListener\CustomObjectsAutoloaderRegistration |
| [src/Glpi/Kernel/Listener/PostBootListener/CustomObjectsBoot.php](../src/Glpi/Kernel/Listener/PostBootListener/CustomObjectsBoot.php) | .php | class Glpi\Kernel\Listener\PostBootListener\CustomObjectsBoot |
| [src/Glpi/Kernel/Listener/PostBootListener/InitializeCache.php](../src/Glpi/Kernel/Listener/PostBootListener/InitializeCache.php) | .php | class Glpi\Kernel\Listener\PostBootListener\InitializeCache |
| [src/Glpi/Kernel/Listener/PostBootListener/InitializeDbConnection.php](../src/Glpi/Kernel/Listener/PostBootListener/InitializeDbConnection.php) | .php | class Glpi\Kernel\Listener\PostBootListener\InitializeDbConnection |
| [src/Glpi/Kernel/Listener/PostBootListener/InitializePlugins.php](../src/Glpi/Kernel/Listener/PostBootListener/InitializePlugins.php) | .php | class Glpi\Kernel\Listener\PostBootListener\InitializePlugins |
| [src/Glpi/Kernel/Listener/PostBootListener/InitializeTwigEnvironment.php](../src/Glpi/Kernel/Listener/PostBootListener/InitializeTwigEnvironment.php) | .php | class Glpi\Kernel\Listener\PostBootListener\InitializeTwigEnvironment |
| [src/Glpi/Kernel/Listener/PostBootListener/LoadLanguage.php](../src/Glpi/Kernel/Listener/PostBootListener/LoadLanguage.php) | .php | class Glpi\Kernel\Listener\PostBootListener\LoadLanguage |
| [src/Glpi/Kernel/Listener/PostBootListener/LoadLegacyConfiguration.php](../src/Glpi/Kernel/Listener/PostBootListener/LoadLegacyConfiguration.php) | .php | class Glpi\Kernel\Listener\PostBootListener\LoadLegacyConfiguration |
| [src/Glpi/Kernel/Listener/PostBootListener/ProfilerStart.php](../src/Glpi/Kernel/Listener/PostBootListener/ProfilerStart.php) | .php | class Glpi\Kernel\Listener\PostBootListener\ProfilerStart |
| [src/Glpi/Kernel/Listener/PostBootListener/SessionStart.php](../src/Glpi/Kernel/Listener/PostBootListener/SessionStart.php) | .php | class Glpi\Kernel\Listener\PostBootListener\SessionStart |
| [src/Glpi/Kernel/Listener/PostBootListener/SetDbSessionVars.php](../src/Glpi/Kernel/Listener/PostBootListener/SetDbSessionVars.php) | .php | class Glpi\Kernel\Listener\PostBootListener\SetDbSessionVars |
| [src/Glpi/Kernel/Listener/RequestListener/CatchInventoryAgentRequestListener.php](../src/Glpi/Kernel/Listener/RequestListener/CatchInventoryAgentRequestListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\CatchInventoryAgentRequestListener |
| [src/Glpi/Kernel/Listener/RequestListener/CheckDatabaseStatusListener.php](../src/Glpi/Kernel/Listener/RequestListener/CheckDatabaseStatusListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\CheckDatabaseStatusListener |
| [src/Glpi/Kernel/Listener/RequestListener/CheckMaintenanceListener.php](../src/Glpi/Kernel/Listener/RequestListener/CheckMaintenanceListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\CheckMaintenanceListener |
| [src/Glpi/Kernel/Listener/RequestListener/CheckStartupErrorsListener.php](../src/Glpi/Kernel/Listener/RequestListener/CheckStartupErrorsListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\CheckStartupErrorsListener |
| [src/Glpi/Kernel/Listener/RequestListener/ConfigureTrustedProxies.php](../src/Glpi/Kernel/Listener/RequestListener/ConfigureTrustedProxies.php) | .php | class Glpi\Kernel\Listener\RequestListener\ConfigureTrustedProxies |
| [src/Glpi/Kernel/Listener/RequestListener/ErrorHandlerRequestListener.php](../src/Glpi/Kernel/Listener/RequestListener/ErrorHandlerRequestListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\ErrorHandlerRequestListener |
| [src/Glpi/Kernel/Listener/RequestListener/FlushBootErrors.php](../src/Glpi/Kernel/Listener/RequestListener/FlushBootErrors.php) | .php | class Glpi\Kernel\Listener\RequestListener\FlushBootErrors |
| [src/Glpi/Kernel/Listener/RequestListener/FrontEndAssetsListener.php](../src/Glpi/Kernel/Listener/RequestListener/FrontEndAssetsListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\FrontEndAssetsListener |
| [src/Glpi/Kernel/Listener/RequestListener/LegacyItemtypeRouteListener.php](../src/Glpi/Kernel/Listener/RequestListener/LegacyItemtypeRouteListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\LegacyItemtypeRouteListener |
| [src/Glpi/Kernel/Listener/RequestListener/LegacyRouterListener.php](../src/Glpi/Kernel/Listener/RequestListener/LegacyRouterListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\LegacyRouterListener |
| [src/Glpi/Kernel/Listener/RequestListener/PluginsRouterListener.php](../src/Glpi/Kernel/Listener/RequestListener/PluginsRouterListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\PluginsRouterListener |
| [src/Glpi/Kernel/Listener/RequestListener/ReAuthReplayListener.php](../src/Glpi/Kernel/Listener/RequestListener/ReAuthReplayListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\ReAuthReplayListener |
| [src/Glpi/Kernel/Listener/RequestListener/RedirectLegacyRouteListener.php](../src/Glpi/Kernel/Listener/RequestListener/RedirectLegacyRouteListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\RedirectLegacyRouteListener |
| [src/Glpi/Kernel/Listener/RequestListener/SessionActivityListener.php](../src/Glpi/Kernel/Listener/RequestListener/SessionActivityListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\SessionActivityListener |
| [src/Glpi/Kernel/Listener/RequestListener/SessionCheckCookieListener.php](../src/Glpi/Kernel/Listener/RequestListener/SessionCheckCookieListener.php) | .php | class Glpi\Kernel\Listener\RequestListener\SessionCheckCookieListener |
| [src/Glpi/Kernel/Listener/RequestListener/SessionVariables.php](../src/Glpi/Kernel/Listener/RequestListener/SessionVariables.php) | .php | class Glpi\Kernel\Listener\RequestListener\SessionVariables |
| [src/Glpi/Kernel/ListenersPriority.php](../src/Glpi/Kernel/ListenersPriority.php) | .php | class Glpi\Kernel\ListenersPriority |
| [src/Glpi/Kernel/PostBootEvent.php](../src/Glpi/Kernel/PostBootEvent.php) | .php | class Glpi\Kernel\PostBootEvent |
| [src/Glpi/Knowbase/Aside/Article.php](../src/Glpi/Knowbase/Aside/Article.php) | .php | class Glpi\Knowbase\Aside\Article |
| [src/Glpi/Knowbase/Aside/Builder.php](../src/Glpi/Knowbase/Aside/Builder.php) | .php | class Glpi\Knowbase\Aside\Builder |
| [src/Glpi/Knowbase/Aside/MoveCandidates.php](../src/Glpi/Knowbase/Aside/MoveCandidates.php) | .php | class Glpi\Knowbase\Aside\MoveCandidates |
| [src/Glpi/Knowbase/Aside/Node.php](../src/Glpi/Knowbase/Aside/Node.php) | .php | interface Glpi\Knowbase\Aside\Node |
| [src/Glpi/Knowbase/Aside/SearchResult.php](../src/Glpi/Knowbase/Aside/SearchResult.php) | .php | class Glpi\Knowbase\Aside\SearchResult |
| [src/Glpi/Knowbase/Aside/SearchResults.php](../src/Glpi/Knowbase/Aside/SearchResults.php) | .php | class Glpi\Knowbase\Aside\SearchResults |
| [src/Glpi/Knowbase/Aside/SearchResultsBuilder.php](../src/Glpi/Knowbase/Aside/SearchResultsBuilder.php) | .php | class Glpi\Knowbase\Aside\SearchResultsBuilder |
| [src/Glpi/Knowbase/Aside/Tree.php](../src/Glpi/Knowbase/Aside/Tree.php) | .php | class Glpi\Knowbase\Aside\Tree |
| [src/Glpi/Knowbase/CommentsThread.php](../src/Glpi/Knowbase/CommentsThread.php) | .php | class Glpi\Knowbase\CommentsThread |
| [src/Glpi/Knowbase/EditorAction.php](../src/Glpi/Knowbase/EditorAction.php) | .php | class Glpi\Knowbase\EditorAction |
| [src/Glpi/Knowbase/EditorActionSeparator.php](../src/Glpi/Knowbase/EditorActionSeparator.php) | .php | class Glpi\Knowbase\EditorActionSeparator |
| [src/Glpi/Knowbase/EditorActionType.php](../src/Glpi/Knowbase/EditorActionType.php) | .php | enum Glpi\Knowbase\EditorActionType |
| [src/Glpi/Knowbase/History/CreationEvent.php](../src/Glpi/Knowbase/History/CreationEvent.php) | .php | class Glpi\Knowbase\History\CreationEvent |
| [src/Glpi/Knowbase/History/CurrentTranslationEvent.php](../src/Glpi/Knowbase/History/CurrentTranslationEvent.php) | .php | class Glpi\Knowbase\History\CurrentTranslationEvent |
| [src/Glpi/Knowbase/History/CurrentVersionLogEvent.php](../src/Glpi/Knowbase/History/CurrentVersionLogEvent.php) | .php | class Glpi\Knowbase\History\CurrentVersionLogEvent extends LogEvent |
| [src/Glpi/Knowbase/History/HistoryBuilder.php](../src/Glpi/Knowbase/History/HistoryBuilder.php) | .php | class Glpi\Knowbase\History\HistoryBuilder |
| [src/Glpi/Knowbase/History/HistoryEventInterface.php](../src/Glpi/Knowbase/History/HistoryEventInterface.php) | .php | interface Glpi\Knowbase\History\HistoryEventInterface |
| [src/Glpi/Knowbase/History/HistoryEventList.php](../src/Glpi/Knowbase/History/HistoryEventList.php) | .php | class Glpi\Knowbase\History\HistoryEventList |
| [src/Glpi/Knowbase/History/LogEvent.php](../src/Glpi/Knowbase/History/LogEvent.php) | .php | class Glpi\Knowbase\History\LogEvent |
| [src/Glpi/Knowbase/History/RevisionEvent.php](../src/Glpi/Knowbase/History/RevisionEvent.php) | .php | class Glpi\Knowbase\History\RevisionEvent |
| [src/Glpi/Knowbase/History/TranslationRevisionEvent.php](../src/Glpi/Knowbase/History/TranslationRevisionEvent.php) | .php | class Glpi\Knowbase\History\TranslationRevisionEvent extends RevisionEvent |
| [src/Glpi/Knowbase/LastUpdateInfo.php](../src/Glpi/Knowbase/LastUpdateInfo.php) | .php | class Glpi\Knowbase\LastUpdateInfo |
| [src/Glpi/Knowbase/SidePanel/CommentsRenderer.php](../src/Glpi/Knowbase/SidePanel/CommentsRenderer.php) | .php | class Glpi\Knowbase\SidePanel\CommentsRenderer |
| [src/Glpi/Knowbase/SidePanel/HistoryRenderer.php](../src/Glpi/Knowbase/SidePanel/HistoryRenderer.php) | .php | class Glpi\Knowbase\SidePanel\HistoryRenderer |
| [src/Glpi/Knowbase/SidePanel/PermissionsRenderer.php](../src/Glpi/Knowbase/SidePanel/PermissionsRenderer.php) | .php | class Glpi\Knowbase\SidePanel\PermissionsRenderer |
| [src/Glpi/Knowbase/SidePanel/RendererInterface.php](../src/Glpi/Knowbase/SidePanel/RendererInterface.php) | .php | interface Glpi\Knowbase\SidePanel\RendererInterface |
| [src/Glpi/Knowbase/SidePanel/ScheduleVisibilityRenderer.php](../src/Glpi/Knowbase/SidePanel/ScheduleVisibilityRenderer.php) | .php | class Glpi\Knowbase\SidePanel\ScheduleVisibilityRenderer |
| [src/Glpi/Knowbase/SidePanel/ServiceCatalogRenderer.php](../src/Glpi/Knowbase/SidePanel/ServiceCatalogRenderer.php) | .php | class Glpi\Knowbase\SidePanel\ServiceCatalogRenderer |
| [src/Glpi/Knowbase/SidePanel/SharingRenderer.php](../src/Glpi/Knowbase/SidePanel/SharingRenderer.php) | .php | class Glpi\Knowbase\SidePanel\SharingRenderer |
| [src/Glpi/Locale/Language.php](../src/Glpi/Locale/Language.php) | .php | class Glpi\Locale\Language |
| [src/Glpi/Locale/LanguageRegistry.php](../src/Glpi/Locale/LanguageRegistry.php) | .php | class Glpi\Locale\LanguageRegistry |
| [src/Glpi/Log/AbstractLogHandler.php](../src/Glpi/Log/AbstractLogHandler.php) | .php | class Glpi\Log\AbstractLogHandler extends StreamHandler |
| [src/Glpi/Log/AbstractLogLineFormatter.php](../src/Glpi/Log/AbstractLogLineFormatter.php) | .php | class Glpi\Log\AbstractLogLineFormatter extends LineFormatter |
| [src/Glpi/Log/AccessLogHandler.php](../src/Glpi/Log/AccessLogHandler.php) | .php | class Glpi\Log\AccessLogHandler extends AbstractLogHandler |
| [src/Glpi/Log/AccessLogLineFormatter.php](../src/Glpi/Log/AccessLogLineFormatter.php) | .php | class Glpi\Log\AccessLogLineFormatter extends AbstractLogLineFormatter |
| [src/Glpi/Log/ErrorLogHandler.php](../src/Glpi/Log/ErrorLogHandler.php) | .php | class Glpi\Log\ErrorLogHandler extends AbstractLogHandler |
| [src/Glpi/Log/ErrorLogLineFormatter.php](../src/Glpi/Log/ErrorLogLineFormatter.php) | .php | class Glpi\Log\ErrorLogLineFormatter extends AbstractLogLineFormatter |
| [src/Glpi/Mail/Protocol/ProtocolInterface.php](../src/Glpi/Mail/Protocol/ProtocolInterface.php) | .php | interface Glpi\Mail\Protocol\ProtocolInterface |
| [src/Glpi/Mail/SMTP/OauthConfig.php](../src/Glpi/Mail/SMTP/OauthConfig.php) | .php | class Glpi\Mail\SMTP\OauthConfig |
| [src/Glpi/Mail/SMTP/OauthProvider/Azure.php](../src/Glpi/Mail/SMTP/OauthProvider/Azure.php) | .php | class Glpi\Mail\SMTP\OauthProvider\Azure extends \TheNetworg\OAuth2\Client\Provider\Azure |
| [src/Glpi/Mail/SMTP/OauthProvider/Google.php](../src/Glpi/Mail/SMTP/OauthProvider/Google.php) | .php | class Glpi\Mail\SMTP\OauthProvider\Google extends \League\OAuth2\Client\Provider\Google |
| [src/Glpi/Mail/SMTP/OauthProvider/ProviderInterface.php](../src/Glpi/Mail/SMTP/OauthProvider/ProviderInterface.php) | .php | interface Glpi\Mail\SMTP\OauthProvider\ProviderInterface |
| [src/Glpi/Marketplace/Api/Plugins.php](../src/Glpi/Marketplace/Api/Plugins.php) | .php | class Glpi\Marketplace\Api\Plugins |
| [src/Glpi/Marketplace/Controller.php](../src/Glpi/Marketplace/Controller.php) | .php | class Glpi\Marketplace\Controller extends CommonGLPI |
| [src/Glpi/Marketplace/NotificationTargetController.php](../src/Glpi/Marketplace/NotificationTargetController.php) | .php | class Glpi\Marketplace\NotificationTargetController extends NotificationTarget |
| [src/Glpi/Marketplace/View.php](../src/Glpi/Marketplace/View.php) | .php | class Glpi\Marketplace\View extends CommonGLPI |
| [src/Glpi/Message/MessageType.php](../src/Glpi/Message/MessageType.php) | .php | enum Glpi\Message\MessageType |
| [src/Glpi/Migration/AbstractPluginMigration.php](../src/Glpi/Migration/AbstractPluginMigration.php) | .php | class Glpi\Migration\AbstractPluginMigration |
| [src/Glpi/Migration/GenericobjectPluginMigration.php](../src/Glpi/Migration/GenericobjectPluginMigration.php) | .php | class Glpi\Migration\GenericobjectPluginMigration extends AbstractPluginMigration |
| [src/Glpi/Migration/MigrationException.php](../src/Glpi/Migration/MigrationException.php) | .php | class Glpi\Migration\MigrationException extends RuntimeException |
| [src/Glpi/Migration/PluginMigrationResult.php](../src/Glpi/Migration/PluginMigrationResult.php) | .php | class Glpi\Migration\PluginMigrationResult |
| [src/Glpi/OAuth/AccessToken.php](../src/Glpi/OAuth/AccessToken.php) | .php | class Glpi\OAuth\AccessToken |
| [src/Glpi/OAuth/AccessTokenRepository.php](../src/Glpi/OAuth/AccessTokenRepository.php) | .php | class Glpi\OAuth\AccessTokenRepository |
| [src/Glpi/OAuth/AuthCode.php](../src/Glpi/OAuth/AuthCode.php) | .php | class Glpi\OAuth\AuthCode |
| [src/Glpi/OAuth/AuthCodeRepository.php](../src/Glpi/OAuth/AuthCodeRepository.php) | .php | class Glpi\OAuth\AuthCodeRepository |
| [src/Glpi/OAuth/Client.php](../src/Glpi/OAuth/Client.php) | .php | class Glpi\OAuth\Client |
| [src/Glpi/OAuth/ClientRepository.php](../src/Glpi/OAuth/ClientRepository.php) | .php | class Glpi\OAuth\ClientRepository |
| [src/Glpi/OAuth/RefreshToken.php](../src/Glpi/OAuth/RefreshToken.php) | .php | class Glpi\OAuth\RefreshToken |
| [src/Glpi/OAuth/RefreshTokenRepository.php](../src/Glpi/OAuth/RefreshTokenRepository.php) | .php | class Glpi\OAuth\RefreshTokenRepository |
| [src/Glpi/OAuth/Scope.php](../src/Glpi/OAuth/Scope.php) | .php | class Glpi\OAuth\Scope |
| [src/Glpi/OAuth/ScopeRepository.php](../src/Glpi/OAuth/ScopeRepository.php) | .php | class Glpi\OAuth\ScopeRepository |
| [src/Glpi/OAuth/Server.php](../src/Glpi/OAuth/Server.php) | .php | class Glpi\OAuth\Server |
| [src/Glpi/OAuth/User.php](../src/Glpi/OAuth/User.php) | .php | class Glpi\OAuth\User |
| [src/Glpi/OAuth/UserRepository.php](../src/Glpi/OAuth/UserRepository.php) | .php | class Glpi\OAuth\UserRepository |
| [src/Glpi/Plugin/HookManager.php](../src/Glpi/Plugin/HookManager.php) | .php | class Glpi\Plugin\HookManager |
| [src/Glpi/Plugin/Hooks.php](../src/Glpi/Plugin/Hooks.php) | .php | class Glpi\Plugin\Hooks |
| [src/Glpi/Progress/AbstractProgressIndicator.php](../src/Glpi/Progress/AbstractProgressIndicator.php) | .php | class Glpi\Progress\AbstractProgressIndicator |
| [src/Glpi/Progress/ConsoleProgressIndicator.php](../src/Glpi/Progress/ConsoleProgressIndicator.php) | .php | class Glpi\Progress\ConsoleProgressIndicator extends AbstractProgressIndicator |
| [src/Glpi/Progress/ProgressStorage.php](../src/Glpi/Progress/ProgressStorage.php) | .php | class Glpi\Progress\ProgressStorage |
| [src/Glpi/Progress/StoredProgressIndicator.php](../src/Glpi/Progress/StoredProgressIndicator.php) | .php | class Glpi\Progress\StoredProgressIndicator extends AbstractProgressIndicator |
| [src/Glpi/RichText/RichText.php](../src/Glpi/RichText/RichText.php) | .php | class Glpi\RichText\RichText |
| [src/Glpi/RichText/UserMention.php](../src/Glpi/RichText/UserMention.php) | .php | class Glpi\RichText\UserMention |
| [src/Glpi/RichText/VideoEmbedRenderer.php](../src/Glpi/RichText/VideoEmbedRenderer.php) | .php | class Glpi\RichText\VideoEmbedRenderer |
| [src/Glpi/Routing/Attribute/ItemtypeFormRoute.php](../src/Glpi/Routing/Attribute/ItemtypeFormRoute.php) | .php | class Glpi\Routing\Attribute\ItemtypeFormRoute extends Route |
| [src/Glpi/Routing/Attribute/ItemtypeListRoute.php](../src/Glpi/Routing/Attribute/ItemtypeListRoute.php) | .php | class Glpi\Routing\Attribute\ItemtypeListRoute extends Route |
| [src/Glpi/Routing/PluginRoutesLoader.php](../src/Glpi/Routing/PluginRoutesLoader.php) | .php | class Glpi\Routing\PluginRoutesLoader extends Loader |
| [src/Glpi/Rules/RulesManager.php](../src/Glpi/Rules/RulesManager.php) | .php | class Glpi\Rules\RulesManager |
| [src/Glpi/Search/CriteriaFilter.php](../src/Glpi/Search/CriteriaFilter.php) | .php | class Glpi\Search\CriteriaFilter extends CommonDBChild |
| [src/Glpi/Search/DefaultSearchRequestInterface.php](../src/Glpi/Search/DefaultSearchRequestInterface.php) | .php | interface Glpi\Search\DefaultSearchRequestInterface |
| [src/Glpi/Search/FilterableInterface.php](../src/Glpi/Search/FilterableInterface.php) | .php | interface Glpi\Search\FilterableInterface |
| [src/Glpi/Search/FilterableTrait.php](../src/Glpi/Search/FilterableTrait.php) | .php | trait Glpi\Search\FilterableTrait |
| [src/Glpi/Search/Input/QueryBuilder.php](../src/Glpi/Search/Input/QueryBuilder.php) | .php | class Glpi\Search\Input\QueryBuilder |
| [src/Glpi/Search/Input/SearchInputInterface.php](../src/Glpi/Search/Input/SearchInputInterface.php) | .php | interface Glpi\Search\Input\SearchInputInterface |
| [src/Glpi/Search/Output/AbstractSearchOutput.php](../src/Glpi/Search/Output/AbstractSearchOutput.php) | .php | class Glpi\Search\Output\AbstractSearchOutput |
| [src/Glpi/Search/Output/Csv.php](../src/Glpi/Search/Output/Csv.php) | .php | class Glpi\Search\Output\Csv extends Spreadsheet |
| [src/Glpi/Search/Output/ExportSearchOutput.php](../src/Glpi/Search/Output/ExportSearchOutput.php) | .php | class Glpi\Search\Output\ExportSearchOutput extends AbstractSearchOutput |
| [src/Glpi/Search/Output/HTMLSearchOutput.php](../src/Glpi/Search/Output/HTMLSearchOutput.php) | .php | class Glpi\Search\Output\HTMLSearchOutput extends AbstractSearchOutput |
| [src/Glpi/Search/Output/MapSearchOutput.php](../src/Glpi/Search/Output/MapSearchOutput.php) | .php | class Glpi\Search\Output\MapSearchOutput extends HTMLSearchOutput |
| [src/Glpi/Search/Output/NamesListSearchOutput.php](../src/Glpi/Search/Output/NamesListSearchOutput.php) | .php | class Glpi\Search\Output\NamesListSearchOutput extends ExportSearchOutput |
| [src/Glpi/Search/Output/Ods.php](../src/Glpi/Search/Output/Ods.php) | .php | class Glpi\Search\Output\Ods extends Spreadsheet |
| [src/Glpi/Search/Output/Pdf.php](../src/Glpi/Search/Output/Pdf.php) | .php | class Glpi\Search\Output\Pdf extends Spreadsheet |
| [src/Glpi/Search/Output/Spreadsheet.php](../src/Glpi/Search/Output/Spreadsheet.php) | .php | class Glpi\Search\Output\Spreadsheet extends ExportSearchOutput |
| [src/Glpi/Search/Output/SpreadsheetValueBinder.php](../src/Glpi/Search/Output/SpreadsheetValueBinder.php) | .php | class Glpi\Search\Output\SpreadsheetValueBinder extends DefaultValueBinder |
| [src/Glpi/Search/Output/Tcpdf.php](../src/Glpi/Search/Output/Tcpdf.php) | .php | class Glpi\Search\Output\Tcpdf extends \PhpOffice\PhpSpreadsheet\Writer\Pdf\Tcpdf |
| [src/Glpi/Search/Output/Xlsx.php](../src/Glpi/Search/Output/Xlsx.php) | .php | class Glpi\Search\Output\Xlsx extends Spreadsheet |
| [src/Glpi/Search/Provider/SQLProvider.php](../src/Glpi/Search/Provider/SQLProvider.php) | .php | class Glpi\Search\Provider\SQLProvider |
| [src/Glpi/Search/Provider/SearchProviderInterface.php](../src/Glpi/Search/Provider/SearchProviderInterface.php) | .php | interface Glpi\Search\Provider\SearchProviderInterface |
| [src/Glpi/Search/SearchEngine.php](../src/Glpi/Search/SearchEngine.php) | .php | class Glpi\Search\SearchEngine |
| [src/Glpi/Search/SearchOption.php](../src/Glpi/Search/SearchOption.php) | .php | class Glpi\Search\SearchOption |
| [src/Glpi/Security/Attribute/SecurityStrategy.php](../src/Glpi/Security/Attribute/SecurityStrategy.php) | .php | class Glpi\Security\Attribute\SecurityStrategy |
| [src/Glpi/Security/PermissionManager.php](../src/Glpi/Security/PermissionManager.php) | .php | class Glpi\Security\PermissionManager |
| [src/Glpi/Security/ReAuth/CasReAuthStrategy.php](../src/Glpi/Security/ReAuth/CasReAuthStrategy.php) | .php | class Glpi\Security\ReAuth\CasReAuthStrategy |
| [src/Glpi/Security/ReAuth/FallbackReAuthStrategy.php](../src/Glpi/Security/ReAuth/FallbackReAuthStrategy.php) | .php | class Glpi\Security\ReAuth\FallbackReAuthStrategy extends InPlaceReAuthStrategy |
| [src/Glpi/Security/ReAuth/InPlaceReAuthStrategy.php](../src/Glpi/Security/ReAuth/InPlaceReAuthStrategy.php) | .php | class Glpi\Security\ReAuth\InPlaceReAuthStrategy |
| [src/Glpi/Security/ReAuth/LdapReAuthStrategy.php](../src/Glpi/Security/ReAuth/LdapReAuthStrategy.php) | .php | class Glpi\Security\ReAuth\LdapReAuthStrategy extends InPlaceReAuthStrategy |
| [src/Glpi/Security/ReAuth/MailReAuthStrategy.php](../src/Glpi/Security/ReAuth/MailReAuthStrategy.php) | .php | class Glpi\Security\ReAuth\MailReAuthStrategy extends InPlaceReAuthStrategy |
| [src/Glpi/Security/ReAuth/PasswordReAuthStrategy.php](../src/Glpi/Security/ReAuth/PasswordReAuthStrategy.php) | .php | class Glpi\Security\ReAuth\PasswordReAuthStrategy extends InPlaceReAuthStrategy |
| [src/Glpi/Security/ReAuth/ReAuthManager.php](../src/Glpi/Security/ReAuth/ReAuthManager.php) | .php | class Glpi\Security\ReAuth\ReAuthManager |
| [src/Glpi/Security/ReAuth/ReAuthStrategyEnum.php](../src/Glpi/Security/ReAuth/ReAuthStrategyEnum.php) | .php | enum Glpi\Security\ReAuth\ReAuthStrategyEnum |
| [src/Glpi/Security/ReAuth/ReAuthStrategyInterface.php](../src/Glpi/Security/ReAuth/ReAuthStrategyInterface.php) | .php | interface Glpi\Security\ReAuth\ReAuthStrategyInterface |
| [src/Glpi/Security/ReAuth/TOTPReAuthStrategy.php](../src/Glpi/Security/ReAuth/TOTPReAuthStrategy.php) | .php | class Glpi\Security\ReAuth\TOTPReAuthStrategy extends InPlaceReAuthStrategy |
| [src/Glpi/Security/SecurityConfig.php](../src/Glpi/Security/SecurityConfig.php) | .php | class Glpi\Security\SecurityConfig extends Config |
| [src/Glpi/Security/SessionTracker.php](../src/Glpi/Security/SessionTracker.php) | .php | class Glpi\Security\SessionTracker |
| [src/Glpi/Security/ShareTokenManager.php](../src/Glpi/Security/ShareTokenManager.php) | .php | class Glpi\Security\ShareTokenManager |
| [src/Glpi/Security/TOTPManager.php](../src/Glpi/Security/TOTPManager.php) | .php | class Glpi\Security\TOTPManager |
| [src/Glpi/Security/User_SessionHistory.php](../src/Glpi/Security/User_SessionHistory.php) | .php | class Glpi\Security\User_SessionHistory extends CommonDBTM |
| [src/Glpi/Session/SessionInfo.php](../src/Glpi/Session/SessionInfo.php) | .php | class Glpi\Session\SessionInfo |
| [src/Glpi/ShareToken.php](../src/Glpi/ShareToken.php) | .php | class Glpi\ShareToken extends CommonDBChild |
| [src/Glpi/ShareableInterface.php](../src/Glpi/ShareableInterface.php) | .php | interface Glpi\ShareableInterface |
| [src/Glpi/Socket.php](../src/Glpi/Socket.php) | .php | class Glpi\Socket extends CommonDBChild |
| [src/Glpi/SocketModel.php](../src/Glpi/SocketModel.php) | .php | class Glpi\SocketModel extends CommonDropdown |
| [src/Glpi/Stat/Data/Graph/StatDataSatisfaction.php](../src/Glpi/Stat/Data/Graph/StatDataSatisfaction.php) | .php | class Glpi\Stat\Data\Graph\StatDataSatisfaction extends StatDataAlwaysDisplay |
| [src/Glpi/Stat/Data/Graph/StatDataSatisfactionSurvey.php](../src/Glpi/Stat/Data/Graph/StatDataSatisfactionSurvey.php) | .php | class Glpi\Stat\Data\Graph\StatDataSatisfactionSurvey extends StatDataAlwaysDisplay |
| [src/Glpi/Stat/Data/Graph/StatDataTicketAverageTime.php](../src/Glpi/Stat/Data/Graph/StatDataTicketAverageTime.php) | .php | class Glpi\Stat\Data\Graph\StatDataTicketAverageTime extends StatDataAlwaysDisplay |
| [src/Glpi/Stat/Data/Graph/StatDataTicketNumber.php](../src/Glpi/Stat/Data/Graph/StatDataTicketNumber.php) | .php | class Glpi\Stat\Data\Graph\StatDataTicketNumber extends StatDataAlwaysDisplay |
| [src/Glpi/Stat/Data/Location/StatDataClosed.php](../src/Glpi/Stat/Data/Location/StatDataClosed.php) | .php | class Glpi\Stat\Data\Location\StatDataClosed extends StatDataLocation |
| [src/Glpi/Stat/Data/Location/StatDataLate.php](../src/Glpi/Stat/Data/Location/StatDataLate.php) | .php | class Glpi\Stat\Data\Location\StatDataLate extends StatDataLocation |
| [src/Glpi/Stat/Data/Location/StatDataLocation.php](../src/Glpi/Stat/Data/Location/StatDataLocation.php) | .php | class Glpi\Stat\Data\Location\StatDataLocation extends StatData |
| [src/Glpi/Stat/Data/Location/StatDataOpenSatisfaction.php](../src/Glpi/Stat/Data/Location/StatDataOpenSatisfaction.php) | .php | class Glpi\Stat\Data\Location\StatDataOpenSatisfaction extends StatDataLocation |
| [src/Glpi/Stat/Data/Location/StatDataOpened.php](../src/Glpi/Stat/Data/Location/StatDataOpened.php) | .php | class Glpi\Stat\Data\Location\StatDataOpened extends StatDataLocation |
| [src/Glpi/Stat/Data/Location/StatDataSolved.php](../src/Glpi/Stat/Data/Location/StatDataSolved.php) | .php | class Glpi\Stat\Data\Location\StatDataSolved extends StatDataLocation |
| [src/Glpi/Stat/Data/Sglobal/StatDataAverageSatisfaction.php](../src/Glpi/Stat/Data/Sglobal/StatDataAverageSatisfaction.php) | .php | class Glpi\Stat\Data\Sglobal\StatDataAverageSatisfaction extends StatDataAlwaysDisplay |
| [src/Glpi/Stat/Data/Sglobal/StatDataSatisfaction.php](../src/Glpi/Stat/Data/Sglobal/StatDataSatisfaction.php) | .php | class Glpi\Stat\Data\Sglobal\StatDataSatisfaction extends StatDataAlwaysDisplay |
| [src/Glpi/Stat/Data/Sglobal/StatDataTicketAverageTime.php](../src/Glpi/Stat/Data/Sglobal/StatDataTicketAverageTime.php) | .php | class Glpi\Stat\Data\Sglobal\StatDataTicketAverageTime extends StatDataAlwaysDisplay |
| [src/Glpi/Stat/Data/Sglobal/StatDataTicketNumber.php](../src/Glpi/Stat/Data/Sglobal/StatDataTicketNumber.php) | .php | class Glpi\Stat\Data\Sglobal\StatDataTicketNumber extends StatDataAlwaysDisplay |
| [src/Glpi/Stat/StatData.php](../src/Glpi/Stat/StatData.php) | .php | class Glpi\Stat\StatData |
| [src/Glpi/Stat/StatDataAlwaysDisplay.php](../src/Glpi/Stat/StatDataAlwaysDisplay.php) | .php | class Glpi\Stat\StatDataAlwaysDisplay extends StatData |
| [src/Glpi/System/Diagnostic/AbstractDatabaseChecker.php](../src/Glpi/System/Diagnostic/AbstractDatabaseChecker.php) | .php | class Glpi\System\Diagnostic\AbstractDatabaseChecker |
| [src/Glpi/System/Diagnostic/DatabaseKeysChecker.php](../src/Glpi/System/Diagnostic/DatabaseKeysChecker.php) | .php | class Glpi\System\Diagnostic\DatabaseKeysChecker extends AbstractDatabaseChecker |
| [src/Glpi/System/Diagnostic/DatabaseSchemaConsistencyChecker.php](../src/Glpi/System/Diagnostic/DatabaseSchemaConsistencyChecker.php) | .php | class Glpi\System\Diagnostic\DatabaseSchemaConsistencyChecker extends AbstractDatabaseChecker |
| [src/Glpi/System/Diagnostic/DatabaseSchemaIntegrityChecker.php](../src/Glpi/System/Diagnostic/DatabaseSchemaIntegrityChecker.php) | .php | class Glpi\System\Diagnostic\DatabaseSchemaIntegrityChecker |
| [src/Glpi/System/Diagnostic/SourceCodeIntegrityChecker.php](../src/Glpi/System/Diagnostic/SourceCodeIntegrityChecker.php) | .php | class Glpi\System\Diagnostic\SourceCodeIntegrityChecker |
| [src/Glpi/System/Log/LogParser.php](../src/Glpi/System/Log/LogParser.php) | .php | class Glpi\System\Log\LogParser extends CommonGLPI |
| [src/Glpi/System/Log/LogViewer.php](../src/Glpi/System/Log/LogViewer.php) | .php | class Glpi\System\Log\LogViewer extends CommonGLPI |
| [src/Glpi/System/Requirement/AbstractRequirement.php](../src/Glpi/System/Requirement/AbstractRequirement.php) | .php | class Glpi\System\Requirement\AbstractRequirement |
| [src/Glpi/System/Requirement/DatabaseTablesEngine.php](../src/Glpi/System/Requirement/DatabaseTablesEngine.php) | .php | class Glpi\System\Requirement\DatabaseTablesEngine extends AbstractRequirement |
| [src/Glpi/System/Requirement/DbConfiguration.php](../src/Glpi/System/Requirement/DbConfiguration.php) | .php | class Glpi\System\Requirement\DbConfiguration extends AbstractRequirement |
| [src/Glpi/System/Requirement/DbEngine.php](../src/Glpi/System/Requirement/DbEngine.php) | .php | class Glpi\System\Requirement\DbEngine extends AbstractRequirement |
| [src/Glpi/System/Requirement/DbTimezones.php](../src/Glpi/System/Requirement/DbTimezones.php) | .php | class Glpi\System\Requirement\DbTimezones extends AbstractRequirement |
| [src/Glpi/System/Requirement/DirectoriesWriteAccess.php](../src/Glpi/System/Requirement/DirectoriesWriteAccess.php) | .php | class Glpi\System\Requirement\DirectoriesWriteAccess extends AbstractRequirement |
| [src/Glpi/System/Requirement/DirectoryWriteAccess.php](../src/Glpi/System/Requirement/DirectoryWriteAccess.php) | .php | class Glpi\System\Requirement\DirectoryWriteAccess extends AbstractRequirement |
| [src/Glpi/System/Requirement/Extension.php](../src/Glpi/System/Requirement/Extension.php) | .php | class Glpi\System\Requirement\Extension extends AbstractRequirement |
| [src/Glpi/System/Requirement/ExtensionClass.php](../src/Glpi/System/Requirement/ExtensionClass.php) | .php | class Glpi\System\Requirement\ExtensionClass extends Extension |
| [src/Glpi/System/Requirement/ExtensionConstant.php](../src/Glpi/System/Requirement/ExtensionConstant.php) | .php | class Glpi\System\Requirement\ExtensionConstant extends AbstractRequirement |
| [src/Glpi/System/Requirement/ExtensionFunction.php](../src/Glpi/System/Requirement/ExtensionFunction.php) | .php | class Glpi\System\Requirement\ExtensionFunction extends Extension |
| [src/Glpi/System/Requirement/ExtensionGroup.php](../src/Glpi/System/Requirement/ExtensionGroup.php) | .php | class Glpi\System\Requirement\ExtensionGroup extends AbstractRequirement |
| [src/Glpi/System/Requirement/IntegerSize.php](../src/Glpi/System/Requirement/IntegerSize.php) | .php | class Glpi\System\Requirement\IntegerSize extends AbstractRequirement |
| [src/Glpi/System/Requirement/LogsWriteAccess.php](../src/Glpi/System/Requirement/LogsWriteAccess.php) | .php | class Glpi\System\Requirement\LogsWriteAccess extends AbstractRequirement |
| [src/Glpi/System/Requirement/MemoryLimit.php](../src/Glpi/System/Requirement/MemoryLimit.php) | .php | class Glpi\System\Requirement\MemoryLimit extends AbstractRequirement |
| [src/Glpi/System/Requirement/PhpSupportedVersion.php](../src/Glpi/System/Requirement/PhpSupportedVersion.php) | .php | class Glpi\System\Requirement\PhpSupportedVersion extends AbstractRequirement |
| [src/Glpi/System/Requirement/PhpVersion.php](../src/Glpi/System/Requirement/PhpVersion.php) | .php | class Glpi\System\Requirement\PhpVersion extends AbstractRequirement |
| [src/Glpi/System/Requirement/RequirementInterface.php](../src/Glpi/System/Requirement/RequirementInterface.php) | .php | interface Glpi\System\Requirement\RequirementInterface |
| [src/Glpi/System/Requirement/SeLinux.php](../src/Glpi/System/Requirement/SeLinux.php) | .php | class Glpi\System\Requirement\SeLinux extends AbstractRequirement |
| [src/Glpi/System/Requirement/SecurityKeysAccess.php](../src/Glpi/System/Requirement/SecurityKeysAccess.php) | .php | class Glpi\System\Requirement\SecurityKeysAccess extends AbstractRequirement |
| [src/Glpi/System/Requirement/SessionsConfiguration.php](../src/Glpi/System/Requirement/SessionsConfiguration.php) | .php | class Glpi\System\Requirement\SessionsConfiguration extends AbstractRequirement |
| [src/Glpi/System/Requirement/SessionsSecurityConfiguration.php](../src/Glpi/System/Requirement/SessionsSecurityConfiguration.php) | .php | class Glpi\System\Requirement\SessionsSecurityConfiguration extends AbstractRequirement |
| [src/Glpi/System/RequirementsList.php](../src/Glpi/System/RequirementsList.php) | .php | class Glpi\System\RequirementsList |
| [src/Glpi/System/RequirementsManager.php](../src/Glpi/System/RequirementsManager.php) | .php | class Glpi\System\RequirementsManager |
| [src/Glpi/System/Status/StatusChecker.php](../src/Glpi/System/Status/StatusChecker.php) | .php | class Glpi\System\Status\StatusChecker |
| [src/Glpi/System/Variables.php](../src/Glpi/System/Variables.php) | .php | class Glpi\System\Variables |
| [src/Glpi/Team/Team.php](../src/Glpi/Team/Team.php) | .php | class Glpi\Team\Team |
| [src/Glpi/Toolbox/ArrayNormalizer.php](../src/Glpi/Toolbox/ArrayNormalizer.php) | .php | class Glpi\Toolbox\ArrayNormalizer |
| [src/Glpi/Toolbox/ArrayPathAccessor.php](../src/Glpi/Toolbox/ArrayPathAccessor.php) | .php | class Glpi\Toolbox\ArrayPathAccessor |
| [src/Glpi/Toolbox/DataExport.php](../src/Glpi/Toolbox/DataExport.php) | .php | class Glpi\Toolbox\DataExport |
| [src/Glpi/Toolbox/DatabaseSchema.php](../src/Glpi/Toolbox/DatabaseSchema.php) | .php | class Glpi\Toolbox\DatabaseSchema |
| [src/Glpi/Toolbox/FileInfo.php](../src/Glpi/Toolbox/FileInfo.php) | .php | class Glpi\Toolbox\FileInfo |
| [src/Glpi/Toolbox/Filesystem.php](../src/Glpi/Toolbox/Filesystem.php) | .php | class Glpi\Toolbox\Filesystem |
| [src/Glpi/Toolbox/FrontEnd.php](../src/Glpi/Toolbox/FrontEnd.php) | .php | class Glpi\Toolbox\FrontEnd |
| [src/Glpi/Toolbox/HttpClient.php](../src/Glpi/Toolbox/HttpClient.php) | .php | class Glpi\Toolbox\HttpClient |
| [src/Glpi/Toolbox/IPUtilities.php](../src/Glpi/Toolbox/IPUtilities.php) | .php | class Glpi\Toolbox\IPUtilities |
| [src/Glpi/Toolbox/MapperInterface.php](../src/Glpi/Toolbox/MapperInterface.php) | .php | interface Glpi\Toolbox\MapperInterface |
| [src/Glpi/Toolbox/MarkdownBuilder.php](../src/Glpi/Toolbox/MarkdownBuilder.php) | .php | class Glpi\Toolbox\MarkdownBuilder |
| [src/Glpi/Toolbox/MarkdownRenderer.php](../src/Glpi/Toolbox/MarkdownRenderer.php) | .php | class Glpi\Toolbox\MarkdownRenderer |
| [src/Glpi/Toolbox/SanitizedStringsDecoder.php](../src/Glpi/Toolbox/SanitizedStringsDecoder.php) | .php | class Glpi\Toolbox\SanitizedStringsDecoder |
| [src/Glpi/Toolbox/SingletonTrait.php](../src/Glpi/Toolbox/SingletonTrait.php) | .php | trait Glpi\Toolbox\SingletonTrait |
| [src/Glpi/Toolbox/URL.php](../src/Glpi/Toolbox/URL.php) | .php | class Glpi\Toolbox\URL |
| [src/Glpi/Toolbox/UserCache.php](../src/Glpi/Toolbox/UserCache.php) | .php | class Glpi\Toolbox\UserCache |
| [src/Glpi/Toolbox/UuidStore.php](../src/Glpi/Toolbox/UuidStore.php) | .php | class Glpi\Toolbox\UuidStore |
| [src/Glpi/Toolbox/VersionParser.php](../src/Glpi/Toolbox/VersionParser.php) | .php | class Glpi\Toolbox\VersionParser |
| [src/Glpi/UI/IllustrationManager.php](../src/Glpi/UI/IllustrationManager.php) | .php | class Glpi\UI\IllustrationManager |
| [src/Glpi/UI/Theme.php](../src/Glpi/UI/Theme.php) | .php | class Glpi\UI\Theme |
| [src/Glpi/UI/ThemeManager.php](../src/Glpi/UI/ThemeManager.php) | .php | class Glpi\UI\ThemeManager |
| [src/Glpi/Urgency.php](../src/Glpi/Urgency.php) | .php | enum Glpi\Urgency |
| [src/Group.php](../src/Group.php) | .php | class Group extends CommonTreeDropdown |
| [src/Group_Item.php](../src/Group_Item.php) | .php | class Group_Item extends CommonDBRelation |
| [src/Group_KnowbaseItem.php](../src/Group_KnowbaseItem.php) | .php | class Group_KnowbaseItem extends CommonDBRelation |
| [src/Group_Problem.php](../src/Group_Problem.php) | .php | class Group_Problem extends CommonITILActor |
| [src/Group_RSSFeed.php](../src/Group_RSSFeed.php) | .php | class Group_RSSFeed extends CommonDBRelation |
| [src/Group_Reminder.php](../src/Group_Reminder.php) | .php | class Group_Reminder extends CommonDBRelation |
| [src/Group_Ticket.php](../src/Group_Ticket.php) | .php | class Group_Ticket extends CommonITILActor |
| [src/Group_User.php](../src/Group_User.php) | .php | class Group_User extends CommonDBRelation |
| [src/HTMLCompositeTableInterface.php](../src/HTMLCompositeTableInterface.php) | .php | interface HTMLCompositeTableInterface |
| [src/HTMLTableBase.php](../src/HTMLTableBase.php) | .php | class HTMLTableBase |
| [src/HTMLTableCell.php](../src/HTMLTableCell.php) | .php | class HTMLTableCell extends HTMLTableEntity |
| [src/HTMLTableCellFatherCoherentHeader.php](../src/HTMLTableCellFatherCoherentHeader.php) | .php | class HTMLTableCellFatherCoherentHeader extends Exception |
| [src/HTMLTableCellFatherSameRow.php](../src/HTMLTableCellFatherSameRow.php) | .php | class HTMLTableCellFatherSameRow extends Exception |
| [src/HTMLTableCellWithoutFather.php](../src/HTMLTableCellWithoutFather.php) | .php | class HTMLTableCellWithoutFather extends Exception |
| [src/HTMLTableEntity.php](../src/HTMLTableEntity.php) | .php | class HTMLTableEntity |
| [src/HTMLTableGroup.php](../src/HTMLTableGroup.php) | .php | class HTMLTableGroup extends HTMLTableBase |
| [src/HTMLTableHeader.php](../src/HTMLTableHeader.php) | .php | class HTMLTableHeader extends HTMLTableEntity |
| [src/HTMLTableMain.php](../src/HTMLTableMain.php) | .php | class HTMLTableMain extends HTMLTableBase |
| [src/HTMLTableRow.php](../src/HTMLTableRow.php) | .php | class HTMLTableRow extends HTMLTableEntity |
| [src/HTMLTableSubHeader.php](../src/HTMLTableSubHeader.php) | .php | class HTMLTableSubHeader extends HTMLTableHeader |
| [src/HTMLTableSuperHeader.php](../src/HTMLTableSuperHeader.php) | .php | class HTMLTableSuperHeader extends HTMLTableHeader |
| [src/HTMLTableUnknownHeader.php](../src/HTMLTableUnknownHeader.php) | .php | class HTMLTableUnknownHeader extends Exception |
| [src/HTMLTableUnknownHeaders.php](../src/HTMLTableUnknownHeaders.php) | .php | class HTMLTableUnknownHeaders extends Exception |
| [src/HTMLTableUnknownHeadersOrder.php](../src/HTMLTableUnknownHeadersOrder.php) | .php | class HTMLTableUnknownHeadersOrder extends Exception |
| [src/Holiday.php](../src/Holiday.php) | .php | class Holiday extends CommonDropdown |
| [src/Html.php](../src/Html.php) | .php | class Html |
| [src/IPAddress.php](../src/IPAddress.php) | .php | class IPAddress extends CommonDBChild |
| [src/IPAddress_IPNetwork.php](../src/IPAddress_IPNetwork.php) | .php | class IPAddress_IPNetwork extends CommonDBRelation |
| [src/IPNetmask.php](../src/IPNetmask.php) | .php | class IPNetmask extends IPAddress |
| [src/IPNetwork.php](../src/IPNetwork.php) | .php | class IPNetwork extends CommonImplicitTreeDropdown |
| [src/IPNetwork_Vlan.php](../src/IPNetwork_Vlan.php) | .php | class IPNetwork_Vlan extends CommonDBRelation |
| [src/ITILCategory.php](../src/ITILCategory.php) | .php | class ITILCategory extends CommonTreeDropdown |
| [src/ITILFollowup.php](../src/ITILFollowup.php) | .php | class ITILFollowup extends CommonDBChild |
| [src/ITILFollowupTemplate.php](../src/ITILFollowupTemplate.php) | .php | class ITILFollowupTemplate extends AbstractITILChildTemplate |
| [src/ITILReminder.php](../src/ITILReminder.php) | .php | class ITILReminder extends CommonDBChild |
| [src/ITILSolution.php](../src/ITILSolution.php) | .php | class ITILSolution extends CommonDBChild |
| [src/ITILSubItemRights.php](../src/ITILSubItemRights.php) | .php | trait ITILSubItemRights |
| [src/ITILTemplate.php](../src/ITILTemplate.php) | .php | class ITILTemplate extends CommonDropdown |
| [src/ITILTemplateField.php](../src/ITILTemplateField.php) | .php | class ITILTemplateField extends CommonDBChild |
| [src/ITILTemplateHiddenField.php](../src/ITILTemplateHiddenField.php) | .php | class ITILTemplateHiddenField extends ITILTemplateField |
| [src/ITILTemplateMandatoryField.php](../src/ITILTemplateMandatoryField.php) | .php | class ITILTemplateMandatoryField extends ITILTemplateField |
| [src/ITILTemplatePredefinedField.php](../src/ITILTemplatePredefinedField.php) | .php | class ITILTemplatePredefinedField extends ITILTemplateField |
| [src/ITILTemplateReadonlyField.php](../src/ITILTemplateReadonlyField.php) | .php | class ITILTemplateReadonlyField extends ITILTemplateField |
| [src/ITILValidationTemplate.php](../src/ITILValidationTemplate.php) | .php | class ITILValidationTemplate extends AbstractITILChildTemplate |
| [src/ITILValidationTemplate_Target.php](../src/ITILValidationTemplate_Target.php) | .php | class ITILValidationTemplate_Target extends CommonDBRelation |
| [src/ITIL_ValidationStep.php](../src/ITIL_ValidationStep.php) | .php | class ITIL_ValidationStep extends CommonDBChild |
| [src/ImageFormat.php](../src/ImageFormat.php) | .php | class ImageFormat extends CommonDropdown |
| [src/ImageResolution.php](../src/ImageResolution.php) | .php | class ImageResolution extends CommonDropdown |
| [src/Impact.php](../src/Impact.php) | .php | class Impact extends CommonGLPI |
| [src/ImpactCompound.php](../src/ImpactCompound.php) | .php | class ImpactCompound extends CommonDBTM |
| [src/ImpactContext.php](../src/ImpactContext.php) | .php | class ImpactContext extends CommonDBTM |
| [src/ImpactItem.php](../src/ImpactItem.php) | .php | class ImpactItem extends CommonDBTM |
| [src/ImpactRelation.php](../src/ImpactRelation.php) | .php | class ImpactRelation extends CommonDBRelation |
| [src/Infocom.php](../src/Infocom.php) | .php | class Infocom extends CommonDBChild |
| [src/InterfaceType.php](../src/InterfaceType.php) | .php | class InterfaceType extends CommonDropdown |
| [src/ItemAntivirus.php](../src/ItemAntivirus.php) | .php | class ItemAntivirus extends CommonDBChild |
| [src/ItemVirtualMachine.php](../src/ItemVirtualMachine.php) | .php | class ItemVirtualMachine extends CommonDBChild |
| [src/Item_Cluster.php](../src/Item_Cluster.php) | .php | class Item_Cluster extends CommonDBRelation |
| [src/Item_DeviceBattery.php](../src/Item_DeviceBattery.php) | .php | class Item_DeviceBattery extends Item_Devices |
| [src/Item_DeviceCamera.php](../src/Item_DeviceCamera.php) | .php | class Item_DeviceCamera extends Item_Devices |
| [src/Item_DeviceCamera_ImageFormat.php](../src/Item_DeviceCamera_ImageFormat.php) | .php | class Item_DeviceCamera_ImageFormat extends CommonDBRelation |
| [src/Item_DeviceCamera_ImageResolution.php](../src/Item_DeviceCamera_ImageResolution.php) | .php | class Item_DeviceCamera_ImageResolution extends CommonDBRelation |
| [src/Item_DeviceCase.php](../src/Item_DeviceCase.php) | .php | class Item_DeviceCase extends Item_Devices |
| [src/Item_DeviceControl.php](../src/Item_DeviceControl.php) | .php | class Item_DeviceControl extends Item_Devices |
| [src/Item_DeviceDrive.php](../src/Item_DeviceDrive.php) | .php | class Item_DeviceDrive extends Item_Devices |
| [src/Item_DeviceFirmware.php](../src/Item_DeviceFirmware.php) | .php | class Item_DeviceFirmware extends Item_Devices |
| [src/Item_DeviceGeneric.php](../src/Item_DeviceGeneric.php) | .php | class Item_DeviceGeneric extends Item_Devices |
| [src/Item_DeviceGraphicCard.php](../src/Item_DeviceGraphicCard.php) | .php | class Item_DeviceGraphicCard extends Item_Devices |
| [src/Item_DeviceHardDrive.php](../src/Item_DeviceHardDrive.php) | .php | class Item_DeviceHardDrive extends Item_Devices |
| [src/Item_DeviceMemory.php](../src/Item_DeviceMemory.php) | .php | class Item_DeviceMemory extends Item_Devices |
| [src/Item_DeviceMotherboard.php](../src/Item_DeviceMotherboard.php) | .php | class Item_DeviceMotherboard extends Item_Devices |
| [src/Item_DeviceNetworkCard.php](../src/Item_DeviceNetworkCard.php) | .php | class Item_DeviceNetworkCard extends Item_Devices |
| [src/Item_DevicePci.php](../src/Item_DevicePci.php) | .php | class Item_DevicePci extends Item_Devices |
| [src/Item_DevicePowerSupply.php](../src/Item_DevicePowerSupply.php) | .php | class Item_DevicePowerSupply extends Item_Devices |
| [src/Item_DeviceProcessor.php](../src/Item_DeviceProcessor.php) | .php | class Item_DeviceProcessor extends Item_Devices |
| [src/Item_DeviceSensor.php](../src/Item_DeviceSensor.php) | .php | class Item_DeviceSensor extends Item_Devices |
| [src/Item_DeviceSimcard.php](../src/Item_DeviceSimcard.php) | .php | class Item_DeviceSimcard extends Item_Devices |
| [src/Item_DeviceSoundCard.php](../src/Item_DeviceSoundCard.php) | .php | class Item_DeviceSoundCard extends Item_Devices |
| [src/Item_Devices.php](../src/Item_Devices.php) | .php | class Item_Devices extends CommonDBRelation |
| [src/Item_Disk.php](../src/Item_Disk.php) | .php | class Item_Disk extends CommonDBChild |
| [src/Item_Enclosure.php](../src/Item_Enclosure.php) | .php | class Item_Enclosure extends CommonDBRelation |
| [src/Item_Environment.php](../src/Item_Environment.php) | .php | class Item_Environment extends CommonDBChild |
| [src/Item_Kanban.php](../src/Item_Kanban.php) | .php | class Item_Kanban extends CommonDBRelation |
| [src/Item_Line.php](../src/Item_Line.php) | .php | class Item_Line extends CommonDBRelation |
| [src/Item_Ola.php](../src/Item_Ola.php) | .php | class Item_Ola extends CommonDBRelation |
| [src/Item_OperatingSystem.php](../src/Item_OperatingSystem.php) | .php | class Item_OperatingSystem extends CommonDBRelation |
| [src/Item_Problem.php](../src/Item_Problem.php) | .php | class Item_Problem extends CommonItilObject_Item |
| [src/Item_Process.php](../src/Item_Process.php) | .php | class Item_Process extends CommonDBChild |
| [src/Item_Project.php](../src/Item_Project.php) | .php | class Item_Project extends CommonDBRelation |
| [src/Item_Rack.php](../src/Item_Rack.php) | .php | class Item_Rack extends CommonDBRelation |
| [src/Item_RemoteManagement.php](../src/Item_RemoteManagement.php) | .php | class Item_RemoteManagement extends CommonDBChild |
| [src/Item_SoftwareLicense.php](../src/Item_SoftwareLicense.php) | .php | class Item_SoftwareLicense extends CommonDBRelation |
| [src/Item_SoftwareVersion.php](../src/Item_SoftwareVersion.php) | .php | class Item_SoftwareVersion extends CommonDBRelation |
| [src/Item_Ticket.php](../src/Item_Ticket.php) | .php | class Item_Ticket extends CommonItilObject_Item |
| [src/Item_TicketRecurrent.php](../src/Item_TicketRecurrent.php) | .php | class Item_TicketRecurrent extends CommonItilObject_Item |
| [src/Itil_Project.php](../src/Itil_Project.php) | .php | class Itil_Project extends CommonDBRelation |
| [src/Knowbase.php](../src/Knowbase.php) | .php | class Knowbase extends CommonGLPI |
| [src/KnowbaseItem.php](../src/KnowbaseItem.php) | .php | class KnowbaseItem extends CommonDBVisible |
| [src/KnowbaseItemTranslation.php](../src/KnowbaseItemTranslation.php) | .php | class KnowbaseItemTranslation extends CommonDBChild |
| [src/KnowbaseItem_Comment.php](../src/KnowbaseItem_Comment.php) | .php | class KnowbaseItem_Comment extends CommonDBTM |
| [src/KnowbaseItem_Favorite.php](../src/KnowbaseItem_Favorite.php) | .php | class KnowbaseItem_Favorite extends CommonDBRelation |
| [src/KnowbaseItem_Item.php](../src/KnowbaseItem_Item.php) | .php | class KnowbaseItem_Item extends CommonDBRelation |
| [src/KnowbaseItem_KnowbaseItem.php](../src/KnowbaseItem_KnowbaseItem.php) | .php | class KnowbaseItem_KnowbaseItem extends CommonDBRelation |
| [src/KnowbaseItem_Profile.php](../src/KnowbaseItem_Profile.php) | .php | class KnowbaseItem_Profile extends CommonDBRelation |
| [src/KnowbaseItem_Revision.php](../src/KnowbaseItem_Revision.php) | .php | class KnowbaseItem_Revision extends CommonDBTM |
| [src/KnowbaseItem_User.php](../src/KnowbaseItem_User.php) | .php | class KnowbaseItem_User extends CommonDBRelation |
| [src/LevelAgreement.php](../src/LevelAgreement.php) | .php | class LevelAgreement extends CommonDBChild |
| [src/LevelAgreementLevel.php](../src/LevelAgreementLevel.php) | .php | class LevelAgreementLevel extends RuleTicket |
| [src/Line.php](../src/Line.php) | .php | class Line extends CommonDBTM |
| [src/LineOperator.php](../src/LineOperator.php) | .php | class LineOperator extends CommonDropdown |
| [src/LineType.php](../src/LineType.php) | .php | class LineType extends CommonType |
| [src/Link.php](../src/Link.php) | .php | class Link extends CommonDBTM |
| [src/Link_Itemtype.php](../src/Link_Itemtype.php) | .php | class Link_Itemtype extends CommonDBChild |
| [src/Location.php](../src/Location.php) | .php | class Location extends CommonTreeDropdown |
| [src/Lock.php](../src/Lock.php) | .php | class Lock extends CommonGLPI |
| [src/Lockedfield.php](../src/Lockedfield.php) | .php | class Lockedfield extends CommonDBTM |
| [src/Log.php](../src/Log.php) | .php | class Log extends CommonDBTM |
| [src/MailCollector.php](../src/MailCollector.php) | .php | class MailCollector extends CommonDBTM |
| [src/ManualLink.php](../src/ManualLink.php) | .php | class ManualLink extends CommonDBChild |
| [src/Manufacturer.php](../src/Manufacturer.php) | .php | class Manufacturer extends CommonDropdown |
| [src/MapGeolocation.php](../src/MapGeolocation.php) | .php | trait MapGeolocation |
| [src/MassiveAction.php](../src/MassiveAction.php) | .php | class MassiveAction |
| [src/Migration.php](../src/Migration.php) | .php | class Migration |
| [src/Monitor.php](../src/Monitor.php) | .php | class Monitor extends CommonDBTM |
| [src/MonitorModel.php](../src/MonitorModel.php) | .php | class MonitorModel extends CommonDCModelDropdown |
| [src/MonitorType.php](../src/MonitorType.php) | .php | class MonitorType extends CommonType |
| [src/Network.php](../src/Network.php) | .php | class Network extends CommonDropdown |
| [src/NetworkAlias.php](../src/NetworkAlias.php) | .php | class NetworkAlias extends FQDNLabel |
| [src/NetworkEquipment.php](../src/NetworkEquipment.php) | .php | class NetworkEquipment extends CommonDBTM |
| [src/NetworkEquipmentModel.php](../src/NetworkEquipmentModel.php) | .php | class NetworkEquipmentModel extends CommonDCModelDropdown |
| [src/NetworkEquipmentModelStencil.php](../src/NetworkEquipmentModelStencil.php) | .php | class NetworkEquipmentModelStencil extends Stencil |
| [src/NetworkEquipmentType.php](../src/NetworkEquipmentType.php) | .php | class NetworkEquipmentType extends CommonDropdown |
| [src/NetworkInterface.php](../src/NetworkInterface.php) | .php | class NetworkInterface extends CommonDropdown |
| [src/NetworkName.php](../src/NetworkName.php) | .php | class NetworkName extends FQDNLabel |
| [src/NetworkPort.php](../src/NetworkPort.php) | .php | class NetworkPort extends CommonDBChild |
| [src/NetworkPortAggregate.php](../src/NetworkPortAggregate.php) | .php | class NetworkPortAggregate extends NetworkPortInstantiation |
| [src/NetworkPortAlias.php](../src/NetworkPortAlias.php) | .php | class NetworkPortAlias extends NetworkPortInstantiation |
| [src/NetworkPortConnectionLog.php](../src/NetworkPortConnectionLog.php) | .php | class NetworkPortConnectionLog extends CommonDBRelation |
| [src/NetworkPortDialup.php](../src/NetworkPortDialup.php) | .php | class NetworkPortDialup extends NetworkPortInstantiation |
| [src/NetworkPortEthernet.php](../src/NetworkPortEthernet.php) | .php | class NetworkPortEthernet extends NetworkPortInstantiation |
| [src/NetworkPortFiberchannel.php](../src/NetworkPortFiberchannel.php) | .php | class NetworkPortFiberchannel extends NetworkPortInstantiation |
| [src/NetworkPortFiberchannelType.php](../src/NetworkPortFiberchannelType.php) | .php | class NetworkPortFiberchannelType extends CommonDropdown |
| [src/NetworkPortInstantiation.php](../src/NetworkPortInstantiation.php) | .php | class NetworkPortInstantiation extends CommonDBChild |
| [src/NetworkPortLocal.php](../src/NetworkPortLocal.php) | .php | class NetworkPortLocal extends NetworkPortInstantiation |
| [src/NetworkPortMetrics.php](../src/NetworkPortMetrics.php) | .php | class NetworkPortMetrics extends CommonDBChild |
| [src/NetworkPortType.php](../src/NetworkPortType.php) | .php | class NetworkPortType extends CommonDropdown |
| [src/NetworkPortWifi.php](../src/NetworkPortWifi.php) | .php | class NetworkPortWifi extends NetworkPortInstantiation |
| [src/NetworkPort_NetworkPort.php](../src/NetworkPort_NetworkPort.php) | .php | class NetworkPort_NetworkPort extends CommonDBRelation |
| [src/NetworkPort_Vlan.php](../src/NetworkPort_Vlan.php) | .php | class NetworkPort_Vlan extends CommonDBRelation |
| [src/NotImportedEmail.php](../src/NotImportedEmail.php) | .php | class NotImportedEmail extends CommonDBTM |
| [src/Notepad.php](../src/Notepad.php) | .php | class Notepad extends CommonDBChild |
| [src/Notification.php](../src/Notification.php) | .php | class Notification extends CommonDBTM |
| [src/NotificationAjax.php](../src/NotificationAjax.php) | .php | class NotificationAjax |
| [src/NotificationAjaxSetting.php](../src/NotificationAjaxSetting.php) | .php | class NotificationAjaxSetting extends NotificationSetting |
| [src/NotificationEvent.php](../src/NotificationEvent.php) | .php | class NotificationEvent extends CommonDBTM |
| [src/NotificationEventAbstract.php](../src/NotificationEventAbstract.php) | .php | class NotificationEventAbstract |
| [src/NotificationEventAjax.php](../src/NotificationEventAjax.php) | .php | class NotificationEventAjax extends NotificationEventAbstract |
| [src/NotificationEventInterface.php](../src/NotificationEventInterface.php) | .php | interface NotificationEventInterface |
| [src/NotificationEventMailing.php](../src/NotificationEventMailing.php) | .php | class NotificationEventMailing extends NotificationEventAbstract |
| [src/NotificationInterface.php](../src/NotificationInterface.php) | .php | interface NotificationInterface |
| [src/NotificationMailing.php](../src/NotificationMailing.php) | .php | class NotificationMailing |
| [src/NotificationMailingSetting.php](../src/NotificationMailingSetting.php) | .php | class NotificationMailingSetting extends NotificationSetting |
| [src/NotificationSetting.php](../src/NotificationSetting.php) | .php | class NotificationSetting extends CommonDBTM |
| [src/NotificationSettingConfig.php](../src/NotificationSettingConfig.php) | .php | class NotificationSettingConfig extends CommonDBTM |
| [src/NotificationTarget.php](../src/NotificationTarget.php) | .php | class NotificationTarget extends CommonDBChild |
| [src/NotificationTargetCartridgeItem.php](../src/NotificationTargetCartridgeItem.php) | .php | class NotificationTargetCartridgeItem extends NotificationTarget |
| [src/NotificationTargetCertificate.php](../src/NotificationTargetCertificate.php) | .php | class NotificationTargetCertificate extends NotificationTarget |
| [src/NotificationTargetChange.php](../src/NotificationTargetChange.php) | .php | class NotificationTargetChange extends NotificationTargetCommonITILObject |
| [src/NotificationTargetCommonITILObject.php](../src/NotificationTargetCommonITILObject.php) | .php | class NotificationTargetCommonITILObject extends NotificationTarget |
| [src/NotificationTargetConsumableItem.php](../src/NotificationTargetConsumableItem.php) | .php | class NotificationTargetConsumableItem extends NotificationTarget |
| [src/NotificationTargetContract.php](../src/NotificationTargetContract.php) | .php | class NotificationTargetContract extends NotificationTarget |
| [src/NotificationTargetCronTask.php](../src/NotificationTargetCronTask.php) | .php | class NotificationTargetCronTask extends NotificationTarget |
| [src/NotificationTargetDBConnection.php](../src/NotificationTargetDBConnection.php) | .php | class NotificationTargetDBConnection extends NotificationTarget |
| [src/NotificationTargetDomain.php](../src/NotificationTargetDomain.php) | .php | class NotificationTargetDomain extends NotificationTarget |
| [src/NotificationTargetFieldUnicity.php](../src/NotificationTargetFieldUnicity.php) | .php | class NotificationTargetFieldUnicity extends NotificationTarget |
| [src/NotificationTargetInfocom.php](../src/NotificationTargetInfocom.php) | .php | class NotificationTargetInfocom extends NotificationTarget |
| [src/NotificationTargetKnowbaseItem.php](../src/NotificationTargetKnowbaseItem.php) | .php | class NotificationTargetKnowbaseItem extends NotificationTarget |
| [src/NotificationTargetMailCollector.php](../src/NotificationTargetMailCollector.php) | .php | class NotificationTargetMailCollector extends NotificationTarget |
| [src/NotificationTargetObjectLock.php](../src/NotificationTargetObjectLock.php) | .php | class NotificationTargetObjectLock extends NotificationTarget |
| [src/NotificationTargetPlanningRecall.php](../src/NotificationTargetPlanningRecall.php) | .php | class NotificationTargetPlanningRecall extends NotificationTarget |
| [src/NotificationTargetProblem.php](../src/NotificationTargetProblem.php) | .php | class NotificationTargetProblem extends NotificationTargetCommonITILObject |
| [src/NotificationTargetProject.php](../src/NotificationTargetProject.php) | .php | class NotificationTargetProject extends NotificationTarget |
| [src/NotificationTargetProjectTask.php](../src/NotificationTargetProjectTask.php) | .php | class NotificationTargetProjectTask extends NotificationTarget |
| [src/NotificationTargetReservation.php](../src/NotificationTargetReservation.php) | .php | class NotificationTargetReservation extends NotificationTarget |
| [src/NotificationTargetSavedSearch_Alert.php](../src/NotificationTargetSavedSearch_Alert.php) | .php | class NotificationTargetSavedSearch_Alert extends NotificationTarget |
| [src/NotificationTargetSoftwareLicense.php](../src/NotificationTargetSoftwareLicense.php) | .php | class NotificationTargetSoftwareLicense extends NotificationTarget |
| [src/NotificationTargetTicket.php](../src/NotificationTargetTicket.php) | .php | class NotificationTargetTicket extends NotificationTargetCommonITILObject |
| [src/NotificationTargetUser.php](../src/NotificationTargetUser.php) | .php | class NotificationTargetUser extends NotificationTarget |
| [src/NotificationTemplate.php](../src/NotificationTemplate.php) | .php | class NotificationTemplate extends CommonDBTM |
| [src/NotificationTemplateTranslation.php](../src/NotificationTemplateTranslation.php) | .php | class NotificationTemplateTranslation extends CommonDBChild |
| [src/Notification_NotificationTemplate.php](../src/Notification_NotificationTemplate.php) | .php | class Notification_NotificationTemplate extends CommonDBRelation |
| [src/OAuthClient.php](../src/OAuthClient.php) | .php | class OAuthClient extends CommonDBTM |
| [src/OLA.php](../src/OLA.php) | .php | class OLA extends LevelAgreement |
| [src/ObjectLock.php](../src/ObjectLock.php) | .php | class ObjectLock extends CommonDBTM |
| [src/OlaLevel.php](../src/OlaLevel.php) | .php | class OlaLevel extends LevelAgreementLevel |
| [src/OlaLevelAction.php](../src/OlaLevelAction.php) | .php | class OlaLevelAction extends RuleAction |
| [src/OlaLevelCriteria.php](../src/OlaLevelCriteria.php) | .php | class OlaLevelCriteria extends RuleCriteria |
| [src/OlaLevel_Ticket.php](../src/OlaLevel_Ticket.php) | .php | class OlaLevel_Ticket extends CommonDBTM |
| [src/OperatingSystem.php](../src/OperatingSystem.php) | .php | class OperatingSystem extends CommonDropdown |
| [src/OperatingSystemArchitecture.php](../src/OperatingSystemArchitecture.php) | .php | class OperatingSystemArchitecture extends CommonDropdown |
| [src/OperatingSystemEdition.php](../src/OperatingSystemEdition.php) | .php | class OperatingSystemEdition extends CommonDropdown |
| [src/OperatingSystemKernel.php](../src/OperatingSystemKernel.php) | .php | class OperatingSystemKernel extends CommonDropdown |
| [src/OperatingSystemKernelVersion.php](../src/OperatingSystemKernelVersion.php) | .php | class OperatingSystemKernelVersion extends CommonDropdown |
| [src/OperatingSystemServicePack.php](../src/OperatingSystemServicePack.php) | .php | class OperatingSystemServicePack extends CommonDropdown |
| [src/OperatingSystemVersion.php](../src/OperatingSystemVersion.php) | .php | class OperatingSystemVersion extends CommonDropdown |
| [src/PCIVendor.php](../src/PCIVendor.php) | .php | class PCIVendor extends CommonDropdown |
| [src/PDU.php](../src/PDU.php) | .php | class PDU extends CommonDBTM |
| [src/PDUModel.php](../src/PDUModel.php) | .php | class PDUModel extends CommonDCModelDropdown |
| [src/PDUType.php](../src/PDUType.php) | .php | class PDUType extends CommonType |
| [src/PDU_Rack.php](../src/PDU_Rack.php) | .php | class PDU_Rack extends CommonDBRelation |
| [src/PassiveDCEquipment.php](../src/PassiveDCEquipment.php) | .php | class PassiveDCEquipment extends CommonDBTM |
| [src/PassiveDCEquipmentModel.php](../src/PassiveDCEquipmentModel.php) | .php | class PassiveDCEquipmentModel extends CommonDCModelDropdown |
| [src/PassiveDCEquipmentType.php](../src/PassiveDCEquipmentType.php) | .php | class PassiveDCEquipmentType extends CommonType |
| [src/PasswordHistory.php](../src/PasswordHistory.php) | .php | class PasswordHistory |
| [src/PendingReason.php](../src/PendingReason.php) | .php | class PendingReason extends CommonDropdown |
| [src/PendingReasonCron.php](../src/PendingReasonCron.php) | .php | class PendingReasonCron extends CommonDBTM |
| [src/PendingReason_Item.php](../src/PendingReason_Item.php) | .php | class PendingReason_Item extends CommonDBRelation |
| [src/Peripheral.php](../src/Peripheral.php) | .php | class Peripheral extends CommonDBTM |
| [src/PeripheralModel.php](../src/PeripheralModel.php) | .php | class PeripheralModel extends CommonDCModelDropdown |
| [src/PeripheralType.php](../src/PeripheralType.php) | .php | class PeripheralType extends CommonType |
| [src/Phone.php](../src/Phone.php) | .php | class Phone extends CommonDBTM |
| [src/PhoneModel.php](../src/PhoneModel.php) | .php | class PhoneModel extends CommonDropdown |
| [src/PhonePowerSupply.php](../src/PhonePowerSupply.php) | .php | class PhonePowerSupply extends CommonDropdown |
| [src/PhoneType.php](../src/PhoneType.php) | .php | class PhoneType extends CommonType |
| [src/Planning.php](../src/Planning.php) | .php | class Planning extends CommonGLPI |
| [src/PlanningEventCategory.php](../src/PlanningEventCategory.php) | .php | class PlanningEventCategory extends CommonDropdown |
| [src/PlanningExternalEvent.php](../src/PlanningExternalEvent.php) | .php | class PlanningExternalEvent extends CommonDBTM |
| [src/PlanningExternalEventTemplate.php](../src/PlanningExternalEventTemplate.php) | .php | class PlanningExternalEventTemplate extends CommonDropdown |
| [src/PlanningRecall.php](../src/PlanningRecall.php) | .php | class PlanningRecall extends CommonDBChild |
| [src/Plug.php](../src/Plug.php) | .php | class Plug extends CommonDBRelation |
| [src/PlugType.php](../src/PlugType.php) | .php | class PlugType extends CommonType |
| [src/Plugin.php](../src/Plugin.php) | .php | class Plugin extends CommonDBTM |
| [src/Preference.php](../src/Preference.php) | .php | class Preference extends CommonGLPI |
| [src/Printer.php](../src/Printer.php) | .php | class Printer extends CommonDBTM |
| [src/PrinterLog.php](../src/PrinterLog.php) | .php | class PrinterLog extends CommonDBChild |
| [src/PrinterModel.php](../src/PrinterModel.php) | .php | class PrinterModel extends CommonDropdown |
| [src/PrinterType.php](../src/PrinterType.php) | .php | class PrinterType extends CommonType |
| [src/Printer_CartridgeInfo.php](../src/Printer_CartridgeInfo.php) | .php | class Printer_CartridgeInfo extends CommonDBChild |
| [src/Problem.php](../src/Problem.php) | .php | class Problem extends CommonITILObject |
| [src/ProblemCost.php](../src/ProblemCost.php) | .php | class ProblemCost extends CommonITILCost |
| [src/ProblemTask.php](../src/ProblemTask.php) | .php | class ProblemTask extends CommonITILTask |
| [src/ProblemTemplate.php](../src/ProblemTemplate.php) | .php | class ProblemTemplate extends ITILTemplate |
| [src/ProblemTemplateHiddenField.php](../src/ProblemTemplateHiddenField.php) | .php | class ProblemTemplateHiddenField extends ITILTemplateHiddenField |
| [src/ProblemTemplateMandatoryField.php](../src/ProblemTemplateMandatoryField.php) | .php | class ProblemTemplateMandatoryField extends ITILTemplateMandatoryField |
| [src/ProblemTemplatePredefinedField.php](../src/ProblemTemplatePredefinedField.php) | .php | class ProblemTemplatePredefinedField extends ITILTemplatePredefinedField |
| [src/ProblemTemplateReadonlyField.php](../src/ProblemTemplateReadonlyField.php) | .php | class ProblemTemplateReadonlyField extends ITILTemplateReadonlyField |
| [src/Problem_Problem.php](../src/Problem_Problem.php) | .php | class Problem_Problem extends CommonITILObject_CommonITILObject |
| [src/Problem_Supplier.php](../src/Problem_Supplier.php) | .php | class Problem_Supplier extends CommonITILActor |
| [src/Problem_Ticket.php](../src/Problem_Ticket.php) | .php | class Problem_Ticket extends CommonITILObject_CommonITILObject |
| [src/Problem_User.php](../src/Problem_User.php) | .php | class Problem_User extends CommonITILActor |
| [src/Profile.php](../src/Profile.php) | .php | class Profile extends CommonDBTM |
| [src/ProfileRight.php](../src/ProfileRight.php) | .php | class ProfileRight extends CommonDBChild |
| [src/Profile_RSSFeed.php](../src/Profile_RSSFeed.php) | .php | class Profile_RSSFeed extends CommonDBRelation |
| [src/Profile_Reminder.php](../src/Profile_Reminder.php) | .php | class Profile_Reminder extends CommonDBRelation |
| [src/Profile_User.php](../src/Profile_User.php) | .php | class Profile_User extends CommonDBRelation |
| [src/Project.php](../src/Project.php) | .php | class Project extends CommonDBTM |
| [src/ProjectCost.php](../src/ProjectCost.php) | .php | class ProjectCost extends CommonDBChild |
| [src/ProjectState.php](../src/ProjectState.php) | .php | class ProjectState extends CommonDropdown |
| [src/ProjectTask.php](../src/ProjectTask.php) | .php | class ProjectTask extends CommonDBChild |
| [src/ProjectTaskLink.php](../src/ProjectTaskLink.php) | .php | class ProjectTaskLink extends CommonDBRelation |
| [src/ProjectTaskTeam.php](../src/ProjectTaskTeam.php) | .php | class ProjectTaskTeam extends CommonDBRelation |
| [src/ProjectTaskTeamDropdown.php](../src/ProjectTaskTeamDropdown.php) | .php | class ProjectTaskTeamDropdown extends AbstractRightsDropdown |
| [src/ProjectTaskTemplate.php](../src/ProjectTaskTemplate.php) | .php | class ProjectTaskTemplate extends CommonDropdown |
| [src/ProjectTaskType.php](../src/ProjectTaskType.php) | .php | class ProjectTaskType extends CommonDropdown |
| [src/ProjectTask_Ticket.php](../src/ProjectTask_Ticket.php) | .php | class ProjectTask_Ticket extends CommonDBRelation |
| [src/ProjectTeam.php](../src/ProjectTeam.php) | .php | class ProjectTeam extends CommonDBRelation |
| [src/ProjectType.php](../src/ProjectType.php) | .php | class ProjectType extends CommonDropdown |
| [src/PurgeLogs.php](../src/PurgeLogs.php) | .php | class PurgeLogs extends CommonDBTM |
| [src/PurgeSoftwareTask.php](../src/PurgeSoftwareTask.php) | .php | class PurgeSoftwareTask |
| [src/QueuedNotification.php](../src/QueuedNotification.php) | .php | class QueuedNotification extends CommonDBTM |
| [src/QueuedWebhook.php](../src/QueuedWebhook.php) | .php | class QueuedWebhook extends CommonDBChild |
| [src/RSSFeed.php](../src/RSSFeed.php) | .php | class RSSFeed extends CommonDBVisible |
| [src/RSSFeed_User.php](../src/RSSFeed_User.php) | .php | class RSSFeed_User extends CommonDBRelation |
| [src/Rack.php](../src/Rack.php) | .php | class Rack extends CommonDBTM |
| [src/RackModel.php](../src/RackModel.php) | .php | class RackModel extends CommonDropdown |
| [src/RackType.php](../src/RackType.php) | .php | class RackType extends CommonType |
| [src/RecurrentChange.php](../src/RecurrentChange.php) | .php | class RecurrentChange extends CommonITILRecurrent |
| [src/RefusedEquipment.php](../src/RefusedEquipment.php) | .php | class RefusedEquipment extends CommonDBTM |
| [src/RegisteredID.php](../src/RegisteredID.php) | .php | class RegisteredID extends CommonDBChild |
| [src/Reminder.php](../src/Reminder.php) | .php | class Reminder extends CommonDBVisible |
| [src/ReminderTranslation.php](../src/ReminderTranslation.php) | .php | class ReminderTranslation extends CommonDBChild |
| [src/Reminder_User.php](../src/Reminder_User.php) | .php | class Reminder_User extends CommonDBRelation |
| [src/Report.php](../src/Report.php) | .php | class Report extends CommonGLPI |
| [src/RequestType.php](../src/RequestType.php) | .php | class RequestType extends CommonDropdown |
| [src/Reservation.php](../src/Reservation.php) | .php | class Reservation extends CommonDBChild |
| [src/ReservationItem.php](../src/ReservationItem.php) | .php | class ReservationItem extends CommonDBChild |
| [src/Rule.php](../src/Rule.php) | .php | class Rule extends CommonDBTM |
| [src/RuleAction.php](../src/RuleAction.php) | .php | class RuleAction extends CommonDBChild |
| [src/RuleAsset.php](../src/RuleAsset.php) | .php | class RuleAsset extends Rule |
| [src/RuleAssetCollection.php](../src/RuleAssetCollection.php) | .php | class RuleAssetCollection extends RuleCollection |
| [src/RuleChange.php](../src/RuleChange.php) | .php | class RuleChange extends RuleCommonITILObject |
| [src/RuleChangeCollection.php](../src/RuleChangeCollection.php) | .php | class RuleChangeCollection extends RuleCommonITILObjectCollection |
| [src/RuleCollection.php](../src/RuleCollection.php) | .php | class RuleCollection extends CommonDBTM |
| [src/RuleCommonITILObject.php](../src/RuleCommonITILObject.php) | .php | class RuleCommonITILObject extends Rule |
| [src/RuleCommonITILObjectCollection.php](../src/RuleCommonITILObjectCollection.php) | .php | class RuleCommonITILObjectCollection extends RuleCollection |
| [src/RuleCriteria.php](../src/RuleCriteria.php) | .php | class RuleCriteria extends CommonDBChild |
| [src/RuleDefineItemtype.php](../src/RuleDefineItemtype.php) | .php | class RuleDefineItemtype extends Rule |
| [src/RuleDefineItemtypeCollection.php](../src/RuleDefineItemtypeCollection.php) | .php | class RuleDefineItemtypeCollection extends RuleCollection |
| [src/RuleDictionnaryComputerModel.php](../src/RuleDictionnaryComputerModel.php) | .php | class RuleDictionnaryComputerModel extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryComputerModelCollection.php](../src/RuleDictionnaryComputerModelCollection.php) | .php | class RuleDictionnaryComputerModelCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryComputerType.php](../src/RuleDictionnaryComputerType.php) | .php | class RuleDictionnaryComputerType extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryComputerTypeCollection.php](../src/RuleDictionnaryComputerTypeCollection.php) | .php | class RuleDictionnaryComputerTypeCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryDropdown.php](../src/RuleDictionnaryDropdown.php) | .php | class RuleDictionnaryDropdown extends Rule |
| [src/RuleDictionnaryDropdownCollection.php](../src/RuleDictionnaryDropdownCollection.php) | .php | class RuleDictionnaryDropdownCollection extends RuleCollection |
| [src/RuleDictionnaryManufacturer.php](../src/RuleDictionnaryManufacturer.php) | .php | class RuleDictionnaryManufacturer extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryManufacturerCollection.php](../src/RuleDictionnaryManufacturerCollection.php) | .php | class RuleDictionnaryManufacturerCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryMonitorModel.php](../src/RuleDictionnaryMonitorModel.php) | .php | class RuleDictionnaryMonitorModel extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryMonitorModelCollection.php](../src/RuleDictionnaryMonitorModelCollection.php) | .php | class RuleDictionnaryMonitorModelCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryMonitorType.php](../src/RuleDictionnaryMonitorType.php) | .php | class RuleDictionnaryMonitorType extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryMonitorTypeCollection.php](../src/RuleDictionnaryMonitorTypeCollection.php) | .php | class RuleDictionnaryMonitorTypeCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryNetworkEquipmentModel.php](../src/RuleDictionnaryNetworkEquipmentModel.php) | .php | class RuleDictionnaryNetworkEquipmentModel extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryNetworkEquipmentModelCollection.php](../src/RuleDictionnaryNetworkEquipmentModelCollection.php) | .php | class RuleDictionnaryNetworkEquipmentModelCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryNetworkEquipmentType.php](../src/RuleDictionnaryNetworkEquipmentType.php) | .php | class RuleDictionnaryNetworkEquipmentType extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryNetworkEquipmentTypeCollection.php](../src/RuleDictionnaryNetworkEquipmentTypeCollection.php) | .php | class RuleDictionnaryNetworkEquipmentTypeCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryOperatingSystem.php](../src/RuleDictionnaryOperatingSystem.php) | .php | class RuleDictionnaryOperatingSystem extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryOperatingSystemArchitecture.php](../src/RuleDictionnaryOperatingSystemArchitecture.php) | .php | class RuleDictionnaryOperatingSystemArchitecture extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryOperatingSystemArchitectureCollection.php](../src/RuleDictionnaryOperatingSystemArchitectureCollection.php) | .php | class RuleDictionnaryOperatingSystemArchitectureCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryOperatingSystemCollection.php](../src/RuleDictionnaryOperatingSystemCollection.php) | .php | class RuleDictionnaryOperatingSystemCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryOperatingSystemEdition.php](../src/RuleDictionnaryOperatingSystemEdition.php) | .php | class RuleDictionnaryOperatingSystemEdition extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryOperatingSystemEditionCollection.php](../src/RuleDictionnaryOperatingSystemEditionCollection.php) | .php | class RuleDictionnaryOperatingSystemEditionCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryOperatingSystemServicePack.php](../src/RuleDictionnaryOperatingSystemServicePack.php) | .php | class RuleDictionnaryOperatingSystemServicePack extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryOperatingSystemServicePackCollection.php](../src/RuleDictionnaryOperatingSystemServicePackCollection.php) | .php | class RuleDictionnaryOperatingSystemServicePackCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryOperatingSystemVersion.php](../src/RuleDictionnaryOperatingSystemVersion.php) | .php | class RuleDictionnaryOperatingSystemVersion extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryOperatingSystemVersionCollection.php](../src/RuleDictionnaryOperatingSystemVersionCollection.php) | .php | class RuleDictionnaryOperatingSystemVersionCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryPeripheralModel.php](../src/RuleDictionnaryPeripheralModel.php) | .php | class RuleDictionnaryPeripheralModel extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryPeripheralModelCollection.php](../src/RuleDictionnaryPeripheralModelCollection.php) | .php | class RuleDictionnaryPeripheralModelCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryPeripheralType.php](../src/RuleDictionnaryPeripheralType.php) | .php | class RuleDictionnaryPeripheralType extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryPeripheralTypeCollection.php](../src/RuleDictionnaryPeripheralTypeCollection.php) | .php | class RuleDictionnaryPeripheralTypeCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryPhoneModel.php](../src/RuleDictionnaryPhoneModel.php) | .php | class RuleDictionnaryPhoneModel extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryPhoneModelCollection.php](../src/RuleDictionnaryPhoneModelCollection.php) | .php | class RuleDictionnaryPhoneModelCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryPhoneType.php](../src/RuleDictionnaryPhoneType.php) | .php | class RuleDictionnaryPhoneType extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryPhoneTypeCollection.php](../src/RuleDictionnaryPhoneTypeCollection.php) | .php | class RuleDictionnaryPhoneTypeCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryPrinter.php](../src/RuleDictionnaryPrinter.php) | .php | class RuleDictionnaryPrinter extends Rule |
| [src/RuleDictionnaryPrinterCollection.php](../src/RuleDictionnaryPrinterCollection.php) | .php | class RuleDictionnaryPrinterCollection extends RuleCollection |
| [src/RuleDictionnaryPrinterModel.php](../src/RuleDictionnaryPrinterModel.php) | .php | class RuleDictionnaryPrinterModel extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryPrinterModelCollection.php](../src/RuleDictionnaryPrinterModelCollection.php) | .php | class RuleDictionnaryPrinterModelCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnaryPrinterType.php](../src/RuleDictionnaryPrinterType.php) | .php | class RuleDictionnaryPrinterType extends RuleDictionnaryDropdown |
| [src/RuleDictionnaryPrinterTypeCollection.php](../src/RuleDictionnaryPrinterTypeCollection.php) | .php | class RuleDictionnaryPrinterTypeCollection extends RuleDictionnaryDropdownCollection |
| [src/RuleDictionnarySoftware.php](../src/RuleDictionnarySoftware.php) | .php | class RuleDictionnarySoftware extends Rule |
| [src/RuleDictionnarySoftwareCollection.php](../src/RuleDictionnarySoftwareCollection.php) | .php | class RuleDictionnarySoftwareCollection extends RuleCollection |
| [src/RuleImportAsset.php](../src/RuleImportAsset.php) | .php | class RuleImportAsset extends Rule |
| [src/RuleImportAssetCollection.php](../src/RuleImportAssetCollection.php) | .php | class RuleImportAssetCollection extends RuleCollection |
| [src/RuleImportEntity.php](../src/RuleImportEntity.php) | .php | class RuleImportEntity extends Rule |
| [src/RuleImportEntityCollection.php](../src/RuleImportEntityCollection.php) | .php | class RuleImportEntityCollection extends RuleCollection |
| [src/RuleLocation.php](../src/RuleLocation.php) | .php | class RuleLocation extends Rule |
| [src/RuleLocationCollection.php](../src/RuleLocationCollection.php) | .php | class RuleLocationCollection extends RuleCollection |
| [src/RuleMailCollector.php](../src/RuleMailCollector.php) | .php | class RuleMailCollector extends Rule |
| [src/RuleMailCollectorCollection.php](../src/RuleMailCollectorCollection.php) | .php | class RuleMailCollectorCollection extends RuleCollection |
| [src/RuleMatchedLog.php](../src/RuleMatchedLog.php) | .php | class RuleMatchedLog extends CommonDBTM |
| [src/RuleProblem.php](../src/RuleProblem.php) | .php | class RuleProblem extends RuleCommonITILObject |
| [src/RuleProblemCollection.php](../src/RuleProblemCollection.php) | .php | class RuleProblemCollection extends RuleCommonITILObjectCollection |
| [src/RuleRight.php](../src/RuleRight.php) | .php | class RuleRight extends Rule |
| [src/RuleRightCollection.php](../src/RuleRightCollection.php) | .php | class RuleRightCollection extends RuleCollection |
| [src/RuleRightParameter.php](../src/RuleRightParameter.php) | .php | class RuleRightParameter extends CommonDropdown |
| [src/RuleSoftwareCategory.php](../src/RuleSoftwareCategory.php) | .php | class RuleSoftwareCategory extends Rule |
| [src/RuleSoftwareCategoryCollection.php](../src/RuleSoftwareCategoryCollection.php) | .php | class RuleSoftwareCategoryCollection extends RuleCollection |
| [src/RuleTicket.php](../src/RuleTicket.php) | .php | class RuleTicket extends RuleCommonITILObject |
| [src/RuleTicketCollection.php](../src/RuleTicketCollection.php) | .php | class RuleTicketCollection extends RuleCommonITILObjectCollection |
| [src/SLA.php](../src/SLA.php) | .php | class SLA extends LevelAgreement |
| [src/SLM.php](../src/SLM.php) | .php | class SLM extends CommonDBTM |
| [src/SNMPCredential.php](../src/SNMPCredential.php) | .php | class SNMPCredential extends CommonDBTM |
| [src/SavedSearch.php](../src/SavedSearch.php) | .php | class SavedSearch extends CommonDBTM |
| [src/SavedSearch_Alert.php](../src/SavedSearch_Alert.php) | .php | class SavedSearch_Alert extends CommonDBChild |
| [src/SavedSearch_User.php](../src/SavedSearch_User.php) | .php | class SavedSearch_User extends CommonDBRelation |
| [src/Search.php](../src/Search.php) | .php | class Search |
| [src/Session.php](../src/Session.php) | .php | class Session |
| [src/ShareDashboardDropdown.php](../src/ShareDashboardDropdown.php) | .php | class ShareDashboardDropdown extends AbstractRightsDropdown |
| [src/SingletonRuleList.php](../src/SingletonRuleList.php) | .php | class SingletonRuleList |
| [src/SlaLevel.php](../src/SlaLevel.php) | .php | class SlaLevel extends LevelAgreementLevel |
| [src/SlaLevelAction.php](../src/SlaLevelAction.php) | .php | class SlaLevelAction extends RuleAction |
| [src/SlaLevelCriteria.php](../src/SlaLevelCriteria.php) | .php | class SlaLevelCriteria extends RuleCriteria |
| [src/SlaLevel_Ticket.php](../src/SlaLevel_Ticket.php) | .php | class SlaLevel_Ticket extends CommonDBTM |
| [src/Software.php](../src/Software.php) | .php | class Software extends CommonDBTM |
| [src/SoftwareCategory.php](../src/SoftwareCategory.php) | .php | class SoftwareCategory extends CommonTreeDropdown |
| [src/SoftwareLicense.php](../src/SoftwareLicense.php) | .php | class SoftwareLicense extends CommonTreeDropdown |
| [src/SoftwareLicenseType.php](../src/SoftwareLicenseType.php) | .php | class SoftwareLicenseType extends CommonTreeDropdown |
| [src/SoftwareLicense_User.php](../src/SoftwareLicense_User.php) | .php | class SoftwareLicense_User extends CommonDBRelation |
| [src/SoftwareVersion.php](../src/SoftwareVersion.php) | .php | class SoftwareVersion extends CommonDBChild |
| [src/SolutionTemplate.php](../src/SolutionTemplate.php) | .php | class SolutionTemplate extends AbstractITILChildTemplate |
| [src/SolutionType.php](../src/SolutionType.php) | .php | class SolutionType extends CommonDropdown |
| [src/SsoVariable.php](../src/SsoVariable.php) | .php | class SsoVariable extends CommonDropdown |
| [src/Stat.php](../src/Stat.php) | .php | class Stat extends CommonGLPI |
| [src/State.php](../src/State.php) | .php | class State extends CommonTreeDropdown |
| [src/Stencil.php](../src/Stencil.php) | .php | class Stencil extends CommonDBChild |
| [src/Supplier.php](../src/Supplier.php) | .php | class Supplier extends CommonDBTM |
| [src/SupplierType.php](../src/SupplierType.php) | .php | class SupplierType extends CommonType |
| [src/Supplier_Ticket.php](../src/Supplier_Ticket.php) | .php | class Supplier_Ticket extends CommonITILActor |
| [src/TaskCategory.php](../src/TaskCategory.php) | .php | class TaskCategory extends CommonTreeDropdown |
| [src/TaskTemplate.php](../src/TaskTemplate.php) | .php | class TaskTemplate extends AbstractITILChildTemplate |
| [src/Telemetry.php](../src/Telemetry.php) | .php | class Telemetry extends CommonGLPI |
| [src/Ticket.php](../src/Ticket.php) | .php | class Ticket extends CommonITILObject |
| [src/TicketCost.php](../src/TicketCost.php) | .php | class TicketCost extends CommonITILCost |
| [src/TicketRecurrent.php](../src/TicketRecurrent.php) | .php | class TicketRecurrent extends CommonITILRecurrent |
| [src/TicketSatisfaction.php](../src/TicketSatisfaction.php) | .php | class TicketSatisfaction extends CommonITILSatisfaction |
| [src/TicketTask.php](../src/TicketTask.php) | .php | class TicketTask extends CommonITILTask |
| [src/TicketTemplate.php](../src/TicketTemplate.php) | .php | class TicketTemplate extends ITILTemplate |
| [src/TicketTemplateHiddenField.php](../src/TicketTemplateHiddenField.php) | .php | class TicketTemplateHiddenField extends ITILTemplateHiddenField |
| [src/TicketTemplateMandatoryField.php](../src/TicketTemplateMandatoryField.php) | .php | class TicketTemplateMandatoryField extends ITILTemplateMandatoryField |
| [src/TicketTemplatePredefinedField.php](../src/TicketTemplatePredefinedField.php) | .php | class TicketTemplatePredefinedField extends ITILTemplatePredefinedField |
| [src/TicketTemplateReadonlyField.php](../src/TicketTemplateReadonlyField.php) | .php | class TicketTemplateReadonlyField extends ITILTemplateReadonlyField |
| [src/TicketValidation.php](../src/TicketValidation.php) | .php | class TicketValidation extends CommonITILValidation |
| [src/TicketValidationStep.php](../src/TicketValidationStep.php) | .php | class TicketValidationStep extends ITIL_ValidationStep |
| [src/Ticket_Contract.php](../src/Ticket_Contract.php) | .php | class Ticket_Contract extends CommonDBRelation |
| [src/Ticket_Ticket.php](../src/Ticket_Ticket.php) | .php | class Ticket_Ticket extends CommonITILObject_CommonITILObject |
| [src/Ticket_User.php](../src/Ticket_User.php) | .php | class Ticket_User extends CommonITILActor |
| [src/Toolbox.php](../src/Toolbox.php) | .php | class Toolbox |
| [src/Transfer.php](../src/Transfer.php) | .php | class Transfer extends CommonDBTM |
| [src/Twig/Components/Alert/AbstractAlert.php](../src/Twig/Components/Alert/AbstractAlert.php) | .php | class Twig\Components\Alert\AbstractAlert |
| [src/Twig/Components/Alert/Alert.php](../src/Twig/Components/Alert/Alert.php) | .php | class Twig\Components\Alert\Alert extends AbstractAlert |
| [src/Twig/Components/Alert/Danger.php](../src/Twig/Components/Alert/Danger.php) | .php | class Twig\Components\Alert\Danger extends AbstractAlert |
| [src/Twig/Components/Alert/Info.php](../src/Twig/Components/Alert/Info.php) | .php | class Twig\Components\Alert\Info extends AbstractAlert |
| [src/Twig/Components/Alert/Success.php](../src/Twig/Components/Alert/Success.php) | .php | class Twig\Components\Alert\Success extends AbstractAlert |
| [src/Twig/Components/Alert/Warning.php](../src/Twig/Components/Alert/Warning.php) | .php | class Twig\Components\Alert\Warning extends AbstractAlert |
| [src/Twig/Components/Mfa/CodeInput.php](../src/Twig/Components/Mfa/CodeInput.php) | .php | class Twig\Components\Mfa\CodeInput |
| [src/USBVendor.php](../src/USBVendor.php) | .php | class USBVendor extends CommonDropdown |
| [src/Unmanaged.php](../src/Unmanaged.php) | .php | class Unmanaged extends CommonDBTM |
| [src/Update.php](../src/Update.php) | .php | class Update |
| [src/UploadHandler.php](../src/UploadHandler.php) | .php | class UploadHandler |
| [src/User.php](../src/User.php) | .php | class User extends CommonDBTM |
| [src/UserCategory.php](../src/UserCategory.php) | .php | class UserCategory extends CommonDropdown |
| [src/UserEmail.php](../src/UserEmail.php) | .php | class UserEmail extends CommonDBChild |
| [src/UserTitle.php](../src/UserTitle.php) | .php | class UserTitle extends CommonDropdown |
| [src/VObject.php](../src/VObject.php) | .php | class VObject extends CommonDBChild |
| [src/ValidationStep.php](../src/ValidationStep.php) | .php | class ValidationStep extends CommonDropdown |
| [src/ValidatorSubstitute.php](../src/ValidatorSubstitute.php) | .php | class ValidatorSubstitute extends CommonDBTM |
| [src/VirtualMachineState.php](../src/VirtualMachineState.php) | .php | class VirtualMachineState extends CommonDropdown |
| [src/VirtualMachineSystem.php](../src/VirtualMachineSystem.php) | .php | class VirtualMachineSystem extends CommonDropdown |
| [src/VirtualMachineType.php](../src/VirtualMachineType.php) | .php | class VirtualMachineType extends CommonDropdown |
| [src/Vlan.php](../src/Vlan.php) | .php | class Vlan extends CommonDropdown |
| [src/Webhook.php](../src/Webhook.php) | .php | class Webhook extends CommonDBTM |
| [src/WebhookCategory.php](../src/WebhookCategory.php) | .php | class WebhookCategory extends CommonTreeDropdown |
| [src/WifiNetwork.php](../src/WifiNetwork.php) | .php | class WifiNetwork extends CommonDropdown |
| [src/XHProf.php](../src/XHProf.php) | .php | class XHProf |
| [src/autoload/CFG_GLPI.php](../src/autoload/CFG_GLPI.php) | .php | — |
| [src/autoload/constants.php](../src/autoload/constants.php) | .php | — |
| [src/autoload/dbutils-aliases.php](../src/autoload/dbutils-aliases.php) | .php | — |
| [src/autoload/i18n.php](../src/autoload/i18n.php) | .php | — |
| [src/autoload/legacy-autoloader.php](../src/autoload/legacy-autoloader.php) | .php | — |
| [src/autoload/misc-functions.php](../src/autoload/misc-functions.php) | .php | — |

## stubs


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [stubs/db_config_classes.php](../stubs/db_config_classes.php) | .php | — |
| [stubs/glpi_constants.php](../stubs/glpi_constants.php) | .php | — |
| [stubs/glpi_globals.php](../stubs/glpi_globals.php) | .php | — |
| [stubs/plugins_migrations_classes.php](../stubs/plugins_migrations_classes.php) | .php | — |

## templates


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [templates/central/embed_dashboard.html.twig](../templates/central/embed_dashboard.html.twig) | .twig | — |
| [templates/central/lists/itemtype_count.html.twig](../templates/central/lists/itemtype_count.html.twig) | .twig | — |
| [templates/central/lists/table.html.twig](../templates/central/lists/table.html.twig) | .twig | — |
| [templates/central/messages.html.twig](../templates/central/messages.html.twig) | .twig | — |
| [templates/central/widget_tab.html.twig](../templates/central/widget_tab.html.twig) | .twig | — |
| [templates/components/add_visibility_target.html.twig](../templates/components/add_visibility_target.html.twig) | .twig | — |
| [templates/components/alerts_macros.html.twig](../templates/components/alerts_macros.html.twig) | .twig | — |
| [templates/components/altcha/widget.html.twig](../templates/components/altcha/widget.html.twig) | .twig | — |
| [templates/components/assets/link_existing_or_new_item_device.html.twig](../templates/components/assets/link_existing_or_new_item_device.html.twig) | .twig | — |
| [templates/components/checkbox_matrix.html.twig](../templates/components/checkbox_matrix.html.twig) | .twig | — |
| [templates/components/danger_modal.html.twig](../templates/components/danger_modal.html.twig) | .twig | — |
| [templates/components/dashboard/reset.html.twig](../templates/components/dashboard/reset.html.twig) | .twig | — |
| [templates/components/dashboard/widget_form.html.twig](../templates/components/dashboard/widget_form.html.twig) | .twig | — |
| [templates/components/datatable.html.twig](../templates/components/datatable.html.twig) | .twig | — |
| [templates/components/dates_timeline.html.twig](../templates/components/dates_timeline.html.twig) | .twig | — |
| [templates/components/debug/debug_toolbar.html.twig](../templates/components/debug/debug_toolbar.html.twig) | .twig | — |
| [templates/components/dropdown/comments.html.twig](../templates/components/dropdown/comments.html.twig) | .twig | — |
| [templates/components/dropdown/dropdown.html.twig](../templates/components/dropdown/dropdown.html.twig) | .twig | — |
| [templates/components/dropdown/limit.html.twig](../templates/components/dropdown/limit.html.twig) | .twig | — |
| [templates/components/form/basic_inputs_macros.html.twig](../templates/components/form/basic_inputs_macros.html.twig) | .twig | — |
| [templates/components/form/buttons.html.twig](../templates/components/form/buttons.html.twig) | .twig | — |
| [templates/components/form/dates.html.twig](../templates/components/form/dates.html.twig) | .twig | — |
| [templates/components/form/fields_macros.html.twig](../templates/components/form/fields_macros.html.twig) | .twig | — |
| [templates/components/form/file_uploader.html.twig](../templates/components/form/file_uploader.html.twig) | .twig | — |
| [templates/components/form/flags.html.twig](../templates/components/form/flags.html.twig) | .twig | — |
| [templates/components/form/genericdate_picker.html.twig](../templates/components/form/genericdate_picker.html.twig) | .twig | — |
| [templates/components/form/header.html.twig](../templates/components/form/header.html.twig) | .twig | — |
| [templates/components/form/header_content.html.twig](../templates/components/form/header_content.html.twig) | .twig | — |
| [templates/components/form/inventory_info.html.twig](../templates/components/form/inventory_info.html.twig) | .twig | — |
| [templates/components/form/item_antivirus.html.twig](../templates/components/form/item_antivirus.html.twig) | .twig | — |
| [templates/components/form/item_device.html.twig](../templates/components/form/item_device.html.twig) | .twig | — |
| [templates/components/form/item_disk.html.twig](../templates/components/form/item_disk.html.twig) | .twig | — |
| [templates/components/form/item_itilobject_group.html.twig](../templates/components/form/item_itilobject_group.html.twig) | .twig | — |
| [templates/components/form/item_itilobject_item_list.html.twig](../templates/components/form/item_itilobject_item_list.html.twig) | .twig | — |
| [templates/components/form/item_remotemanagement_form.html.twig](../templates/components/form/item_remotemanagement_form.html.twig) | .twig | — |
| [templates/components/form/item_remotemanagement_list.html.twig](../templates/components/form/item_remotemanagement_list.html.twig) | .twig | — |
| [templates/components/form/itemvirtualmachine.html.twig](../templates/components/form/itemvirtualmachine.html.twig) | .twig | — |
| [templates/components/form/link_existing_or_new.html.twig](../templates/components/form/link_existing_or_new.html.twig) | .twig | — |
| [templates/components/form/modals_macros.html.twig](../templates/components/form/modals_macros.html.twig) | .twig | — |
| [templates/components/form/networkname.html.twig](../templates/components/form/networkname.html.twig) | .twig | — |
| [templates/components/form/pending_reason_is_default.html.twig](../templates/components/form/pending_reason_is_default.html.twig) | .twig | — |
| [templates/components/form/pictures.html.twig](../templates/components/form/pictures.html.twig) | .twig | — |
| [templates/components/form/rating.html.twig](../templates/components/form/rating.html.twig) | .twig | — |
| [templates/components/form/reservation.html.twig](../templates/components/form/reservation.html.twig) | .twig | — |
| [templates/components/form/reservationitem_comment.html.twig](../templates/components/form/reservationitem_comment.html.twig) | .twig | — |
| [templates/components/form/rulematchedlogs.html.twig](../templates/components/form/rulematchedlogs.html.twig) | .twig | — |
| [templates/components/form/single-action.html.twig](../templates/components/form/single-action.html.twig) | .twig | — |
| [templates/components/form/snmpcredential.html.twig](../templates/components/form/snmpcredential.html.twig) | .twig | — |
| [templates/components/form/support_hours.html.twig](../templates/components/form/support_hours.html.twig) | .twig | — |
| [templates/components/form/viewsubitem.html.twig](../templates/components/form/viewsubitem.html.twig) | .twig | — |
| [templates/components/group/info_card.html.twig](../templates/components/group/info_card.html.twig) | .twig | — |
| [templates/components/helpdesk_forms/delegation_alert.html.twig](../templates/components/helpdesk_forms/delegation_alert.html.twig) | .twig | — |
| [templates/components/helpdesk_forms/service_catalog_item.html.twig](../templates/components/helpdesk_forms/service_catalog_item.html.twig) | .twig | — |
| [templates/components/helpdesk_forms/service_catalog_items.html.twig](../templates/components/helpdesk_forms/service_catalog_items.html.twig) | .twig | — |
| [templates/components/helpdesk_forms/service_catalog_nested_item.html.twig](../templates/components/helpdesk_forms/service_catalog_nested_item.html.twig) | .twig | — |
| [templates/components/illustration/custom_icon.html.twig](../templates/components/illustration/custom_icon.html.twig) | .twig | — |
| [templates/components/illustration/icon.svg.twig](../templates/components/illustration/icon.svg.twig) | .twig | — |
| [templates/components/illustration/icon_picker.html.twig](../templates/components/illustration/icon_picker.html.twig) | .twig | — |
| [templates/components/illustration/icon_picker_modal.html.twig](../templates/components/illustration/icon_picker_modal.html.twig) | .twig | — |
| [templates/components/illustration/icon_picker_search_results.html.twig](../templates/components/illustration/icon_picker_search_results.html.twig) | .twig | — |
| [templates/components/infocom.html.twig](../templates/components/infocom.html.twig) | .twig | — |
| [templates/components/itilobject/actors/assign_to_me.html.twig](../templates/components/itilobject/actors/assign_to_me.html.twig) | .twig | — |
| [templates/components/itilobject/actors/field.html.twig](../templates/components/itilobject/actors/field.html.twig) | .twig | — |
| [templates/components/itilobject/actors/main.html.twig](../templates/components/itilobject/actors/main.html.twig) | .twig | — |
| [templates/components/itilobject/add_items.html.twig](../templates/components/itilobject/add_items.html.twig) | .twig | — |
| [templates/components/itilobject/answer.html.twig](../templates/components/itilobject/answer.html.twig) | .twig | — |
| [templates/components/itilobject/fields/global_validation.html.twig](../templates/components/itilobject/fields/global_validation.html.twig) | .twig | — |
| [templates/components/itilobject/fields/priority_matrix.html.twig](../templates/components/itilobject/fields/priority_matrix.html.twig) | .twig | — |
| [templates/components/itilobject/fields/status.html.twig](../templates/components/itilobject/fields/status.html.twig) | .twig | — |
| [templates/components/itilobject/fields_panel.html.twig](../templates/components/itilobject/fields_panel.html.twig) | .twig | — |
| [templates/components/itilobject/footer.html.twig](../templates/components/itilobject/footer.html.twig) | .twig | — |
| [templates/components/itilobject/itilsatisfaction.html.twig](../templates/components/itilobject/itilsatisfaction.html.twig) | .twig | — |
| [templates/components/itilobject/itiltemplate.html.twig](../templates/components/itilobject/itiltemplate.html.twig) | .twig | — |
| [templates/components/itilobject/layout.html.twig](../templates/components/itilobject/layout.html.twig) | .twig | — |
| [templates/components/itilobject/linked_itilobjects.html.twig](../templates/components/itilobject/linked_itilobjects.html.twig) | .twig | — |
| [templates/components/itilobject/mainform_close.html.twig](../templates/components/itilobject/mainform_close.html.twig) | .twig | — |
| [templates/components/itilobject/mainform_open.html.twig](../templates/components/itilobject/mainform_open.html.twig) | .twig | — |
| [templates/components/itilobject/service_levels.html.twig](../templates/components/itilobject/service_levels.html.twig) | .twig | — |
| [templates/components/itilobject/stats_dates.html.twig](../templates/components/itilobject/stats_dates.html.twig) | .twig | — |
| [templates/components/itilobject/stats_times.html.twig](../templates/components/itilobject/stats_times.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/approbation_form.html.twig](../templates/components/itilobject/timeline/approbation_form.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/document/document_list_item.html.twig](../templates/components/itilobject/timeline/document/document_list_item.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/document/post_figure_content.html.twig](../templates/components/itilobject/timeline/document/post_figure_content.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/filter_timeline.html.twig](../templates/components/itilobject/timeline/filter_timeline.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/form_document_item.html.twig](../templates/components/itilobject/timeline/form_document_item.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/form_followup.html.twig](../templates/components/itilobject/timeline/form_followup.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/form_solution.html.twig](../templates/components/itilobject/timeline/form_solution.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/form_task.html.twig](../templates/components/itilobject/timeline/form_task.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/form_task_main_form.html.twig](../templates/components/itilobject/timeline/form_task_main_form.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/form_timeline_item.html.twig](../templates/components/itilobject/timeline/form_timeline_item.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/form_validation.html.twig](../templates/components/itilobject/timeline/form_validation.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/knowledge_item.html.twig](../templates/components/itilobject/timeline/knowledge_item.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/main_description.html.twig](../templates/components/itilobject/timeline/main_description.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/new_form.html.twig](../templates/components/itilobject/timeline/new_form.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/pending_reasons.html.twig](../templates/components/itilobject/timeline/pending_reasons.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/pending_reasons_messages.html.twig](../templates/components/itilobject/timeline/pending_reasons_messages.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/satisfaction_survey.html.twig](../templates/components/itilobject/timeline/satisfaction_survey.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/simple_form.html.twig](../templates/components/itilobject/timeline/simple_form.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/sub_documents.html.twig](../templates/components/itilobject/timeline/sub_documents.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/timeline.html.twig](../templates/components/itilobject/timeline/timeline.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/timeline_item_header.html.twig](../templates/components/itilobject/timeline/timeline_item_header.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/timeline_item_header_badges.html.twig](../templates/components/itilobject/timeline/timeline_item_header_badges.html.twig) | .twig | — |
| [templates/components/itilobject/timeline/todo-list-summary.html.twig](../templates/components/itilobject/timeline/todo-list-summary.html.twig) | .twig | — |
| [templates/components/itilobject/validation.html.twig](../templates/components/itilobject/validation.html.twig) | .twig | — |
| [templates/components/itilobject/validationstep.html.twig](../templates/components/itilobject/validationstep.html.twig) | .twig | — |
| [templates/components/kanban/item_panels/default_panel.html.twig](../templates/components/kanban/item_panels/default_panel.html.twig) | .twig | — |
| [templates/components/kanban/kanban.html.twig](../templates/components/kanban/kanban.html.twig) | .twig | — |
| [templates/components/kanban/teammember.html.twig](../templates/components/kanban/teammember.html.twig) | .twig | — |
| [templates/components/logs.html.twig](../templates/components/logs.html.twig) | .twig | — |
| [templates/components/masonry_grid.html.twig](../templates/components/masonry_grid.html.twig) | .twig | — |
| [templates/components/massive_action/add_task.html.twig](../templates/components/massive_action/add_task.html.twig) | .twig | — |
| [templates/components/messages_after_redirect_alerts.html.twig](../templates/components/messages_after_redirect_alerts.html.twig) | .twig | — |
| [templates/components/messages_after_redirect_toasts.html.twig](../templates/components/messages_after_redirect_toasts.html.twig) | .twig | — |
| [templates/components/modal.html.twig](../templates/components/modal.html.twig) | .twig | — |
| [templates/components/notepad/form.html.twig](../templates/components/notepad/form.html.twig) | .twig | — |
| [templates/components/pager.html.twig](../templates/components/pager.html.twig) | .twig | — |
| [templates/components/photoswipe.html.twig](../templates/components/photoswipe.html.twig) | .twig | — |
| [templates/components/plugin_update_modal.html.twig](../templates/components/plugin_update_modal.html.twig) | .twig | — |
| [templates/components/printer_graph_buttons.html.twig](../templates/components/printer_graph_buttons.html.twig) | .twig | — |
| [templates/components/rss_feed.html.twig](../templates/components/rss_feed.html.twig) | .twig | — |
| [templates/components/search/controls.html.twig](../templates/components/search/controls.html.twig) | .twig | — |
| [templates/components/search/criteria_filter.html.twig](../templates/components/search/criteria_filter.html.twig) | .twig | — |
| [templates/components/search/criteria_filter_actions.html.twig](../templates/components/search/criteria_filter_actions.html.twig) | .twig | — |
| [templates/components/search/display_data.html.twig](../templates/components/search/display_data.html.twig) | .twig | — |
| [templates/components/search/displaypreference_config.html.twig](../templates/components/search/displaypreference_config.html.twig) | .twig | — |
| [templates/components/search/displaypreference_list.html.twig](../templates/components/search/displaypreference_list.html.twig) | .twig | — |
| [templates/components/search/displaypreference_modal.html.twig](../templates/components/search/displaypreference_modal.html.twig) | .twig | — |
| [templates/components/search/map.html.twig](../templates/components/search/map.html.twig) | .twig | — |
| [templates/components/search/query_builder/criteria.html.twig](../templates/components/search/query_builder/criteria.html.twig) | .twig | — |
| [templates/components/search/query_builder/criteria_group.html.twig](../templates/components/search/query_builder/criteria_group.html.twig) | .twig | — |
| [templates/components/search/query_builder/main.html.twig](../templates/components/search/query_builder/main.html.twig) | .twig | — |
| [templates/components/search/query_builder/metacriteria.html.twig](../templates/components/search/query_builder/metacriteria.html.twig) | .twig | — |
| [templates/components/search/query_builder/search_option.html.twig](../templates/components/search/query_builder/search_option.html.twig) | .twig | — |
| [templates/components/search/query_builder/search_option_value.html.twig](../templates/components/search/query_builder/search_option_value.html.twig) | .twig | — |
| [templates/components/search/query_builder/sort/criteria.html.twig](../templates/components/search/query_builder/sort/criteria.html.twig) | .twig | — |
| [templates/components/search/query_builder/sort/main.html.twig](../templates/components/search/query_builder/sort/main.html.twig) | .twig | — |
| [templates/components/search/status_area.html.twig](../templates/components/search/status_area.html.twig) | .twig | — |
| [templates/components/search/table.html.twig](../templates/components/search/table.html.twig) | .twig | — |
| [templates/components/supplier/info_card.html.twig](../templates/components/supplier/info_card.html.twig) | .twig | — |
| [templates/components/tab/addlink_block.html.twig](../templates/components/tab/addlink_block.html.twig) | .twig | — |
| [templates/components/table.html.twig](../templates/components/table.html.twig) | .twig | — |
| [templates/components/user/create_user.html.twig](../templates/components/user/create_user.html.twig) | .twig | — |
| [templates/components/user/info_card.html.twig](../templates/components/user/info_card.html.twig) | .twig | — |
| [templates/components/user/link_with_tooltip.html.twig](../templates/components/user/link_with_tooltip.html.twig) | .twig | — |
| [templates/components/user/password_security_checks.html.twig](../templates/components/user/password_security_checks.html.twig) | .twig | — |
| [templates/components/user/picture.html.twig](../templates/components/user/picture.html.twig) | .twig | — |
| [templates/dropdown_form.html.twig](../templates/dropdown_form.html.twig) | .twig | — |
| [templates/error_block.html.twig](../templates/error_block.html.twig) | .twig | — |
| [templates/error_page.html.twig](../templates/error_page.html.twig) | .twig | — |
| [templates/forgotpassword.html.twig](../templates/forgotpassword.html.twig) | .twig | — |
| [templates/generic_show_form.html.twig](../templates/generic_show_form.html.twig) | .twig | — |
| [templates/impact/edit_compound_modal.html.twig](../templates/impact/edit_compound_modal.html.twig) | .twig | — |
| [templates/impact/edit_edge_modal.html.twig](../templates/impact/edit_edge_modal.html.twig) | .twig | — |
| [templates/impact/ongoing_modal.html.twig](../templates/impact/ongoing_modal.html.twig) | .twig | — |
| [templates/install/accept_license.html.twig](../templates/install/accept_license.html.twig) | .twig | — |
| [templates/install/agree_unstable.html.twig](../templates/install/agree_unstable.html.twig) | .twig | — |
| [templates/install/blocks/requirements_table.html.twig](../templates/install/blocks/requirements_table.html.twig) | .twig | — |
| [templates/install/choose_language.html.twig](../templates/install/choose_language.html.twig) | .twig | — |
| [templates/install/install.install_required.html.twig](../templates/install/install.install_required.html.twig) | .twig | — |
| [templates/install/post_update_step.html.twig](../templates/install/post_update_step.html.twig) | .twig | — |
| [templates/install/step0.html.twig](../templates/install/step0.html.twig) | .twig | — |
| [templates/install/step1.html.twig](../templates/install/step1.html.twig) | .twig | — |
| [templates/install/step2.html.twig](../templates/install/step2.html.twig) | .twig | — |
| [templates/install/step3.html.twig](../templates/install/step3.html.twig) | .twig | — |
| [templates/install/step6.html.twig](../templates/install/step6.html.twig) | .twig | — |
| [templates/install/step7.html.twig](../templates/install/step7.html.twig) | .twig | — |
| [templates/install/step8.html.twig](../templates/install/step8.html.twig) | .twig | — |
| [templates/install/update.invalid_database.html.twig](../templates/install/update.invalid_database.html.twig) | .twig | — |
| [templates/install/update.need_update.html.twig](../templates/install/update.need_update.html.twig) | .twig | — |
| [templates/layout/page_card_notlogged.html.twig](../templates/layout/page_card_notlogged.html.twig) | .twig | — |
| [templates/layout/page_skeleton.html.twig](../templates/layout/page_skeleton.html.twig) | .twig | — |
| [templates/layout/page_without_tabs.html.twig](../templates/layout/page_without_tabs.html.twig) | .twig | — |
| [templates/layout/parts/breadcrumbs.html.twig](../templates/layout/parts/breadcrumbs.html.twig) | .twig | — |
| [templates/layout/parts/context_links.html.twig](../templates/layout/parts/context_links.html.twig) | .twig | — |
| [templates/layout/parts/dcbreadcrumbs.html.twig](../templates/layout/parts/dcbreadcrumbs.html.twig) | .twig | — |
| [templates/layout/parts/global_search_form.html.twig](../templates/layout/parts/global_search_form.html.twig) | .twig | — |
| [templates/layout/parts/goto_button.html.twig](../templates/layout/parts/goto_button.html.twig) | .twig | — |
| [templates/layout/parts/head.html.twig](../templates/layout/parts/head.html.twig) | .twig | — |
| [templates/layout/parts/impersonate_banner.html.twig](../templates/layout/parts/impersonate_banner.html.twig) | .twig | — |
| [templates/layout/parts/menu.html.twig](../templates/layout/parts/menu.html.twig) | .twig | — |
| [templates/layout/parts/objectlock_message.html.twig](../templates/layout/parts/objectlock_message.html.twig) | .twig | — |
| [templates/layout/parts/page_footer.html.twig](../templates/layout/parts/page_footer.html.twig) | .twig | — |
| [templates/layout/parts/page_header.html.twig](../templates/layout/parts/page_header.html.twig) | .twig | — |
| [templates/layout/parts/page_header_empty.html.twig](../templates/layout/parts/page_header_empty.html.twig) | .twig | — |
| [templates/layout/parts/profile_selector.html.twig](../templates/layout/parts/profile_selector.html.twig) | .twig | — |
| [templates/layout/parts/profile_selector_form.html.twig](../templates/layout/parts/profile_selector_form.html.twig) | .twig | — |
| [templates/layout/parts/saved_searches.html.twig](../templates/layout/parts/saved_searches.html.twig) | .twig | — |
| [templates/layout/parts/saved_searches_list.html.twig](../templates/layout/parts/saved_searches_list.html.twig) | .twig | — |
| [templates/layout/parts/user_header.html.twig](../templates/layout/parts/user_header.html.twig) | .twig | — |
| [templates/maintenance.html.twig](../templates/maintenance.html.twig) | .twig | — |
| [templates/pages/2fa/2fa_backup_codes.html.twig](../templates/pages/2fa/2fa_backup_codes.html.twig) | .twig | — |
| [templates/pages/2fa/2fa_config.html.twig](../templates/pages/2fa/2fa_config.html.twig) | .twig | — |
| [templates/pages/2fa/2fa_enforced_setup.html.twig](../templates/pages/2fa/2fa_enforced_setup.html.twig) | .twig | — |
| [templates/pages/2fa/2fa_new_secret.html.twig](../templates/pages/2fa/2fa_new_secret.html.twig) | .twig | — |
| [templates/pages/2fa/2fa_request.html.twig](../templates/pages/2fa/2fa_request.html.twig) | .twig | — |
| [templates/pages/2fa/2fa_status.html.twig](../templates/pages/2fa/2fa_status.html.twig) | .twig | — |
| [templates/pages/2fa/macros.html.twig](../templates/pages/2fa/macros.html.twig) | .twig | — |
| [templates/pages/admin/add_profile_authorization.html.twig](../templates/pages/admin/add_profile_authorization.html.twig) | .twig | — |
| [templates/pages/admin/assetdefinition/capacities.html.twig](../templates/pages/admin/assetdefinition/capacities.html.twig) | .twig | — |
| [templates/pages/admin/assetdefinition/capacity/is_inventoriable_capacity_configuration_form.html.twig](../templates/pages/admin/assetdefinition/capacity/is_inventoriable_capacity_configuration_form.html.twig) | .twig | — |
| [templates/pages/admin/assetdefinition/fields_display.html.twig](../templates/pages/admin/assetdefinition/fields_display.html.twig) | .twig | — |
| [templates/pages/admin/customobjects/main.html.twig](../templates/pages/admin/customobjects/main.html.twig) | .twig | — |
| [templates/pages/admin/customobjects/plurals.html.twig](../templates/pages/admin/customobjects/plurals.html.twig) | .twig | — |
| [templates/pages/admin/customobjects/profiles.html.twig](../templates/pages/admin/customobjects/profiles.html.twig) | .twig | — |
| [templates/pages/admin/customobjects/translations.html.twig](../templates/pages/admin/customobjects/translations.html.twig) | .twig | — |
| [templates/pages/admin/entity/address.html.twig](../templates/pages/admin/entity/address.html.twig) | .twig | — |
| [templates/pages/admin/entity/advanced.html.twig](../templates/pages/admin/entity/advanced.html.twig) | .twig | — |
| [templates/pages/admin/entity/assets.html.twig](../templates/pages/admin/entity/assets.html.twig) | .twig | — |
| [templates/pages/admin/entity/assistance.html.twig](../templates/pages/admin/entity/assistance.html.twig) | .twig | — |
| [templates/pages/admin/entity/custom_ui.html.twig](../templates/pages/admin/entity/custom_ui.html.twig) | .twig | — |
| [templates/pages/admin/entity/notifications.html.twig](../templates/pages/admin/entity/notifications.html.twig) | .twig | — |
| [templates/pages/admin/entity/survey_config.html.twig](../templates/pages/admin/entity/survey_config.html.twig) | .twig | — |
| [templates/pages/admin/external_page_tile_config_fields.html.twig](../templates/pages/admin/external_page_tile_config_fields.html.twig) | .twig | — |
| [templates/pages/admin/form/access_control.html.twig](../templates/pages/admin/form/access_control.html.twig) | .twig | — |
| [templates/pages/admin/form/access_control/allow_list.html.twig](../templates/pages/admin/form/access_control/allow_list.html.twig) | .twig | — |
| [templates/pages/admin/form/access_control/direct_access.html.twig](../templates/pages/admin/form/access_control/direct_access.html.twig) | .twig | — |
| [templates/pages/admin/form/condition_configuration.html.twig](../templates/pages/admin/form/condition_configuration.html.twig) | .twig | — |
| [templates/pages/admin/form/condition_handler_templates/actor.html.twig](../templates/pages/admin/form/condition_handler_templates/actor.html.twig) | .twig | — |
| [templates/pages/admin/form/condition_handler_templates/dropdown.html.twig](../templates/pages/admin/form/condition_handler_templates/dropdown.html.twig) | .twig | — |
| [templates/pages/admin/form/condition_handler_templates/dropdown_multiple.html.twig](../templates/pages/admin/form/condition_handler_templates/dropdown_multiple.html.twig) | .twig | — |
| [templates/pages/admin/form/condition_handler_templates/input.html.twig](../templates/pages/admin/form/condition_handler_templates/input.html.twig) | .twig | — |
| [templates/pages/admin/form/condition_handler_templates/item_dropdown.html.twig](../templates/pages/admin/form/condition_handler_templates/item_dropdown.html.twig) | .twig | — |
| [templates/pages/admin/form/condition_handler_templates/user_devices_dropdown.html.twig](../templates/pages/admin/form/condition_handler_templates/user_devices_dropdown.html.twig) | .twig | — |
| [templates/pages/admin/form/conditional_validation_dropdown.html.twig](../templates/pages/admin/form/conditional_validation_dropdown.html.twig) | .twig | — |
| [templates/pages/admin/form/conditional_validation_editor.html.twig](../templates/pages/admin/form/conditional_validation_editor.html.twig) | .twig | — |
| [templates/pages/admin/form/conditional_visibility_dropdown.html.twig](../templates/pages/admin/form/conditional_visibility_dropdown.html.twig) | .twig | — |
| [templates/pages/admin/form/conditional_visibility_editor.html.twig](../templates/pages/admin/form/conditional_visibility_editor.html.twig) | .twig | — |
| [templates/pages/admin/form/delete_non_empty_section_modal.html.twig](../templates/pages/admin/form/delete_non_empty_section_modal.html.twig) | .twig | — |
| [templates/pages/admin/form/destination_visibility_conditions_configuration.html.twig](../templates/pages/admin/form/destination_visibility_conditions_configuration.html.twig) | .twig | — |
| [templates/pages/admin/form/form_comment.html.twig](../templates/pages/admin/form/form_comment.html.twig) | .twig | — |
| [templates/pages/admin/form/form_destination.html.twig](../templates/pages/admin/form/form_destination.html.twig) | .twig | — |
| [templates/pages/admin/form/form_destination_actions.html.twig](../templates/pages/admin/form/form_destination_actions.html.twig) | .twig | — |
| [templates/pages/admin/form/form_destination_commonitil_config.html.twig](../templates/pages/admin/form/form_destination_commonitil_config.html.twig) | .twig | — |
| [templates/pages/admin/form/form_destination_form.html.twig](../templates/pages/admin/form/form_destination_form.html.twig) | .twig | — |
| [templates/pages/admin/form/form_editor.html.twig](../templates/pages/admin/form/form_editor.html.twig) | .twig | — |
| [templates/pages/admin/form/form_horizontal_block.html.twig](../templates/pages/admin/form/form_horizontal_block.html.twig) | .twig | — |
| [templates/pages/admin/form/form_horizontal_block_placeholder.html.twig](../templates/pages/admin/form/form_horizontal_block_placeholder.html.twig) | .twig | — |
| [templates/pages/admin/form/form_horizontal_block_toolbar.html.twig](../templates/pages/admin/form/form_horizontal_block_toolbar.html.twig) | .twig | — |
| [templates/pages/admin/form/form_question.html.twig](../templates/pages/admin/form/form_question.html.twig) | .twig | — |
| [templates/pages/admin/form/form_section.html.twig](../templates/pages/admin/form/form_section.html.twig) | .twig | — |
| [templates/pages/admin/form/form_toolbar.html.twig](../templates/pages/admin/form/form_toolbar.html.twig) | .twig | — |
| [templates/pages/admin/form/form_translation.html.twig](../templates/pages/admin/form/form_translation.html.twig) | .twig | — |
| [templates/pages/admin/form/form_translation_content.html.twig](../templates/pages/admin/form/form_translation_content.html.twig) | .twig | — |
| [templates/pages/admin/form/form_translations.html.twig](../templates/pages/admin/form/form_translations.html.twig) | .twig | — |
| [templates/pages/admin/form/import/step1_index.html.twig](../templates/pages/admin/form/import/step1_index.html.twig) | .twig | — |
| [templates/pages/admin/form/import/step2_preview.html.twig](../templates/pages/admin/form/import/step2_preview.html.twig) | .twig | — |
| [templates/pages/admin/form/import/step3_resolve_issues.html.twig](../templates/pages/admin/form/import/step3_resolve_issues.html.twig) | .twig | — |
| [templates/pages/admin/form/import/step4_execute.html.twig](../templates/pages/admin/form/import/step4_execute.html.twig) | .twig | — |
| [templates/pages/admin/form/item_has_conditions_for_deletion_modal.html.twig](../templates/pages/admin/form/item_has_conditions_for_deletion_modal.html.twig) | .twig | — |
| [templates/pages/admin/form/item_has_conditions_for_new_question_type_modal.html.twig](../templates/pages/admin/form/item_has_conditions_for_new_question_type_modal.html.twig) | .twig | — |
| [templates/pages/admin/form/item_has_conditions_modal_base.html.twig](../templates/pages/admin/form/item_has_conditions_modal_base.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/associated_items.html.twig](../templates/pages/admin/form/itil_config_fields/associated_items.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/entity.html.twig](../templates/pages/admin/form/itil_config_fields/entity.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/itilactor.html.twig](../templates/pages/admin/form/itil_config_fields/itilactor.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/itilcategory.html.twig](../templates/pages/admin/form/itil_config_fields/itilcategory.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/itilfollowuptemplate.html.twig](../templates/pages/admin/form/itil_config_fields/itilfollowuptemplate.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/itiltasktemplate.html.twig](../templates/pages/admin/form/itil_config_fields/itiltasktemplate.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/linked_itilobjects.html.twig](../templates/pages/admin/form/itil_config_fields/linked_itilobjects.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/location.html.twig](../templates/pages/admin/form/itil_config_fields/location.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/request_source.html.twig](../templates/pages/admin/form/itil_config_fields/request_source.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/request_type.html.twig](../templates/pages/admin/form/itil_config_fields/request_type.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/slm.html.twig](../templates/pages/admin/form/itil_config_fields/slm.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/template.html.twig](../templates/pages/admin/form/itil_config_fields/template.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/urgency.html.twig](../templates/pages/admin/form/itil_config_fields/urgency.html.twig) | .twig | — |
| [templates/pages/admin/form/itil_config_fields/validation.html.twig](../templates/pages/admin/form/itil_config_fields/validation.html.twig) | .twig | — |
| [templates/pages/admin/form/move_section_modal.html.twig](../templates/pages/admin/form/move_section_modal.html.twig) | .twig | — |
| [templates/pages/admin/form/question_type/actors_admin.html.twig](../templates/pages/admin/form/question_type/actors_admin.html.twig) | .twig | — |
| [templates/pages/admin/form/question_type/base_advanced_configuration.html.twig](../templates/pages/admin/form/question_type/base_advanced_configuration.html.twig) | .twig | — |
| [templates/pages/admin/form/question_type/dropdown/administration_options.html.twig](../templates/pages/admin/form/question_type/dropdown/administration_options.html.twig) | .twig | — |
| [templates/pages/admin/form/question_type/dropdown/administration_template.html.twig](../templates/pages/admin/form/question_type/dropdown/administration_template.html.twig) | .twig | — |
| [templates/pages/admin/form/question_type/dropdown/end_user_template.html.twig](../templates/pages/admin/form/question_type/dropdown/end_user_template.html.twig) | .twig | — |
| [templates/pages/admin/form/question_type/dropdown/end_user_template_ajax.html.twig](../templates/pages/admin/form/question_type/dropdown/end_user_template_ajax.html.twig) | .twig | — |
| [templates/pages/admin/form/question_type/dropdown/form_inline_script.html.twig](../templates/pages/admin/form/question_type/dropdown/form_inline_script.html.twig) | .twig | — |
| [templates/pages/admin/form/question_type/item/administration_template.html.twig](../templates/pages/admin/form/question_type/item/administration_template.html.twig) | .twig | — |
| [templates/pages/admin/form/question_type/item/advanced_configuration.html.twig](../templates/pages/admin/form/question_type/item/advanced_configuration.html.twig) | .twig | — |
| [templates/pages/admin/form/question_type/item/end_user_template.html.twig](../templates/pages/admin/form/question_type/item/end_user_template.html.twig) | .twig | — |
| [templates/pages/admin/form/question_type/item_dropdown/advanced_configuration.html.twig](../templates/pages/admin/form/question_type/item_dropdown/advanced_configuration.html.twig) | .twig | — |
| [templates/pages/admin/form/section_element_has_conditions_for_deletion_modal.html.twig](../templates/pages/admin/form/section_element_has_conditions_for_deletion_modal.html.twig) | .twig | — |
| [templates/pages/admin/form/service_catalog_tab.html.twig](../templates/pages/admin/form/service_catalog_tab.html.twig) | .twig | — |
| [templates/pages/admin/form/submit_button_conditional_visibility_dropdown.html.twig](../templates/pages/admin/form/submit_button_conditional_visibility_dropdown.html.twig) | .twig | — |
| [templates/pages/admin/form_tile_config_fields.html.twig](../templates/pages/admin/form_tile_config_fields.html.twig) | .twig | — |
| [templates/pages/admin/glpi_page_tile_config_fields.html.twig](../templates/pages/admin/glpi_page_tile_config_fields.html.twig) | .twig | — |
| [templates/pages/admin/group.html.twig](../templates/pages/admin/group.html.twig) | .twig | — |
| [templates/pages/admin/group_ldap.html.twig](../templates/pages/admin/group_ldap.html.twig) | .twig | — |
| [templates/pages/admin/group_user.html.twig](../templates/pages/admin/group_user.html.twig) | .twig | — |
| [templates/pages/admin/helpdesk_home_config.html.twig](../templates/pages/admin/helpdesk_home_config.html.twig) | .twig | — |
| [templates/pages/admin/helpdesk_home_config_add_tile_form.html.twig](../templates/pages/admin/helpdesk_home_config_add_tile_form.html.twig) | .twig | — |
| [templates/pages/admin/helpdesk_home_config_edit_tile_form.html.twig](../templates/pages/admin/helpdesk_home_config_edit_tile_form.html.twig) | .twig | — |
| [templates/pages/admin/helpdesk_home_config_for_empty_entity.html.twig](../templates/pages/admin/helpdesk_home_config_for_empty_entity.html.twig) | .twig | — |
| [templates/pages/admin/helpdesk_home_config_for_entity.html.twig](../templates/pages/admin/helpdesk_home_config_for_entity.html.twig) | .twig | — |
| [templates/pages/admin/helpdesk_home_config_tiles.html.twig](../templates/pages/admin/helpdesk_home_config_tiles.html.twig) | .twig | — |
| [templates/pages/admin/helpdesk_home_translation.html.twig](../templates/pages/admin/helpdesk_home_translation.html.twig) | .twig | — |
| [templates/pages/admin/helpdesk_home_translations.html.twig](../templates/pages/admin/helpdesk_home_translations.html.twig) | .twig | — |
| [templates/pages/admin/inventory/agent.html.twig](../templates/pages/admin/inventory/agent.html.twig) | .twig | — |
| [templates/pages/admin/inventory/conf/config_form.html.twig](../templates/pages/admin/inventory/conf/config_form.html.twig) | .twig | — |
| [templates/pages/admin/inventory/conf/index.html.twig](../templates/pages/admin/inventory/conf/index.html.twig) | .twig | — |
| [templates/pages/admin/inventory/lockedfield.html.twig](../templates/pages/admin/inventory/lockedfield.html.twig) | .twig | — |
| [templates/pages/admin/inventory/upload_form.html.twig](../templates/pages/admin/inventory/upload_form.html.twig) | .twig | — |
| [templates/pages/admin/inventory/upload_result.html.twig](../templates/pages/admin/inventory/upload_result.html.twig) | .twig | — |
| [templates/pages/admin/ldap.group_criteria.html.twig](../templates/pages/admin/ldap.group_criteria.html.twig) | .twig | — |
| [templates/pages/admin/ldap.groups.html.twig](../templates/pages/admin/ldap.groups.html.twig) | .twig | — |
| [templates/pages/admin/ldap.user_criteria.html.twig](../templates/pages/admin/ldap.user_criteria.html.twig) | .twig | — |
| [templates/pages/admin/ldap.users.html.twig](../templates/pages/admin/ldap.users.html.twig) | .twig | — |
| [templates/pages/admin/log_viewer.html.twig](../templates/pages/admin/log_viewer.html.twig) | .twig | — |
| [templates/pages/admin/logs_list.html.twig](../templates/pages/admin/logs_list.html.twig) | .twig | — |
| [templates/pages/admin/plugins/list_suspend_banner.html.twig](../templates/pages/admin/plugins/list_suspend_banner.html.twig) | .twig | — |
| [templates/pages/admin/plugins/updatable_alert.html.twig](../templates/pages/admin/plugins/updatable_alert.html.twig) | .twig | — |
| [templates/pages/admin/profile/admin.html.twig](../templates/pages/admin/profile/admin.html.twig) | .twig | — |
| [templates/pages/admin/profile/assets.html.twig](../templates/pages/admin/profile/assets.html.twig) | .twig | — |
| [templates/pages/admin/profile/assistance.html.twig](../templates/pages/admin/profile/assistance.html.twig) | .twig | — |
| [templates/pages/admin/profile/assistance_simple.html.twig](../templates/pages/admin/profile/assistance_simple.html.twig) | .twig | — |
| [templates/pages/admin/profile/base_tab.html.twig](../templates/pages/admin/profile/base_tab.html.twig) | .twig | — |
| [templates/pages/admin/profile/form.html.twig](../templates/pages/admin/profile/form.html.twig) | .twig | — |
| [templates/pages/admin/profile/legend.html.twig](../templates/pages/admin/profile/legend.html.twig) | .twig | — |
| [templates/pages/admin/profile/lifecycle.html.twig](../templates/pages/admin/profile/lifecycle.html.twig) | .twig | — |
| [templates/pages/admin/profile/lifecycle_simple.html.twig](../templates/pages/admin/profile/lifecycle_simple.html.twig) | .twig | — |
| [templates/pages/admin/profile/management.html.twig](../templates/pages/admin/profile/management.html.twig) | .twig | — |
| [templates/pages/admin/profile/search_list.html.twig](../templates/pages/admin/profile/search_list.html.twig) | .twig | — |
| [templates/pages/admin/profile/setup.html.twig](../templates/pages/admin/profile/setup.html.twig) | .twig | — |
| [templates/pages/admin/profile/setup_simple.html.twig](../templates/pages/admin/profile/setup_simple.html.twig) | .twig | — |
| [templates/pages/admin/profile/tools.html.twig](../templates/pages/admin/profile/tools.html.twig) | .twig | — |
| [templates/pages/admin/profile/tools_simple.html.twig](../templates/pages/admin/profile/tools_simple.html.twig) | .twig | — |
| [templates/pages/admin/rules/action.html.twig](../templates/pages/admin/rules/action.html.twig) | .twig | — |
| [templates/pages/admin/rules/backup_header.html.twig](../templates/pages/admin/rules/backup_header.html.twig) | .twig | — |
| [templates/pages/admin/rules/collections_list.html.twig](../templates/pages/admin/rules/collections_list.html.twig) | .twig | — |
| [templates/pages/admin/rules/criteria.html.twig](../templates/pages/admin/rules/criteria.html.twig) | .twig | — |
| [templates/pages/admin/rules/engine_preview_criteria.html.twig](../templates/pages/admin/rules/engine_preview_criteria.html.twig) | .twig | — |
| [templates/pages/admin/rules/engine_preview_results.html.twig](../templates/pages/admin/rules/engine_preview_results.html.twig) | .twig | — |
| [templates/pages/admin/rules/engine_summary.html.twig](../templates/pages/admin/rules/engine_summary.html.twig) | .twig | — |
| [templates/pages/admin/rules/form.html.twig](../templates/pages/admin/rules/form.html.twig) | .twig | — |
| [templates/pages/admin/rules/import.html.twig](../templates/pages/admin/rules/import.html.twig) | .twig | — |
| [templates/pages/admin/rules/import_preview.html.twig](../templates/pages/admin/rules/import_preview.html.twig) | .twig | — |
| [templates/pages/admin/rules/index.html.twig](../templates/pages/admin/rules/index.html.twig) | .twig | — |
| [templates/pages/admin/rules/preview_criteria.html.twig](../templates/pages/admin/rules/preview_criteria.html.twig) | .twig | — |
| [templates/pages/admin/rules/ruleright_form.html.twig](../templates/pages/admin/rules/ruleright_form.html.twig) | .twig | — |
| [templates/pages/admin/transfer.html.twig](../templates/pages/admin/transfer.html.twig) | .twig | — |
| [templates/pages/admin/transfer_list.html.twig](../templates/pages/admin/transfer_list.html.twig) | .twig | — |
| [templates/pages/admin/user.substitute.html.twig](../templates/pages/admin/user.substitute.html.twig) | .twig | — |
| [templates/pages/admin/user/change_other_password.html.twig](../templates/pages/admin/user/change_other_password.html.twig) | .twig | — |
| [templates/pages/admin/user/user.html.twig](../templates/pages/admin/user/user.html.twig) | .twig | — |
| [templates/pages/admin/user/user_picture_field.html.twig](../templates/pages/admin/user/user_picture_field.html.twig) | .twig | — |
| [templates/pages/assets/asset.html.twig](../templates/pages/assets/asset.html.twig) | .twig | — |
| [templates/pages/assets/cable.html.twig](../templates/pages/assets/cable.html.twig) | .twig | — |
| [templates/pages/assets/cartridge.html.twig](../templates/pages/assets/cartridge.html.twig) | .twig | — |
| [templates/pages/assets/cartridgeitem.html.twig](../templates/pages/assets/cartridgeitem.html.twig) | .twig | — |
| [templates/pages/assets/consumable_list.html.twig](../templates/pages/assets/consumable_list.html.twig) | .twig | — |
| [templates/pages/assets/consumableitem.html.twig](../templates/pages/assets/consumableitem.html.twig) | .twig | — |
| [templates/pages/assets/customfield.html.twig](../templates/pages/assets/customfield.html.twig) | .twig | — |
| [templates/pages/assets/enclosure.html.twig](../templates/pages/assets/enclosure.html.twig) | .twig | — |
| [templates/pages/assets/monitor.html.twig](../templates/pages/assets/monitor.html.twig) | .twig | — |
| [templates/pages/assets/networkport/form.html.twig](../templates/pages/assets/networkport/form.html.twig) | .twig | — |
| [templates/pages/assets/networkport/networkname_short.html.twig](../templates/pages/assets/networkport/networkname_short.html.twig) | .twig | — |
| [templates/pages/assets/operatingsystem.html.twig](../templates/pages/assets/operatingsystem.html.twig) | .twig | — |
| [templates/pages/assets/phone.html.twig](../templates/pages/assets/phone.html.twig) | .twig | — |
| [templates/pages/assets/plug.html.twig](../templates/pages/assets/plug.html.twig) | .twig | — |
| [templates/pages/assets/printer.html.twig](../templates/pages/assets/printer.html.twig) | .twig | — |
| [templates/pages/assets/rack.html.twig](../templates/pages/assets/rack.html.twig) | .twig | — |
| [templates/pages/assets/socket.html.twig](../templates/pages/assets/socket.html.twig) | .twig | — |
| [templates/pages/assets/socket_networkport.html.twig](../templates/pages/assets/socket_networkport.html.twig) | .twig | — |
| [templates/pages/assets/socket_short_form.html.twig](../templates/pages/assets/socket_short_form.html.twig) | .twig | — |
| [templates/pages/assets/software.html.twig](../templates/pages/assets/software.html.twig) | .twig | — |
| [templates/pages/assets/template_list.html.twig](../templates/pages/assets/template_list.html.twig) | .twig | — |
| [templates/pages/assets/unmanaged.html.twig](../templates/pages/assets/unmanaged.html.twig) | .twig | — |
| [templates/pages/assistance/planning/add_classic_event.html.twig](../templates/pages/assistance/planning/add_classic_event.html.twig) | .twig | — |
| [templates/pages/assistance/planning/availability.html.twig](../templates/pages/assistance/planning/availability.html.twig) | .twig | — |
| [templates/pages/assistance/planning/external_event.html.twig](../templates/pages/assistance/planning/external_event.html.twig) | .twig | — |
| [templates/pages/assistance/planning/planning.html.twig](../templates/pages/assistance/planning/planning.html.twig) | .twig | — |
| [templates/pages/assistance/stats/form.html.twig](../templates/pages/assistance/stats/form.html.twig) | .twig | — |
| [templates/pages/assistance/stats/global_form.html.twig](../templates/pages/assistance/stats/global_form.html.twig) | .twig | — |
| [templates/pages/assistance/stats/single_item_pager.html.twig](../templates/pages/assistance/stats/single_item_pager.html.twig) | .twig | — |
| [templates/pages/assistance/stats/title.html.twig](../templates/pages/assistance/stats/title.html.twig) | .twig | — |
| [templates/pages/central/index.html.twig](../templates/pages/central/index.html.twig) | .twig | — |
| [templates/pages/form_renderer.html.twig](../templates/pages/form_renderer.html.twig) | .twig | — |
| [templates/pages/generic_form.html.twig](../templates/pages/generic_form.html.twig) | .twig | — |
| [templates/pages/generic_in_modal.html.twig](../templates/pages/generic_in_modal.html.twig) | .twig | — |
| [templates/pages/generic_list.html.twig](../templates/pages/generic_list.html.twig) | .twig | — |
| [templates/pages/helpdesk/index.html.twig](../templates/pages/helpdesk/index.html.twig) | .twig | — |
| [templates/pages/helpdesk/search.html.twig](../templates/pages/helpdesk/search.html.twig) | .twig | — |
| [templates/pages/login.html.twig](../templates/pages/login.html.twig) | .twig | — |
| [templates/pages/login_error.html.twig](../templates/pages/login_error.html.twig) | .twig | — |
| [templates/pages/management/appliance.html.twig](../templates/pages/management/appliance.html.twig) | .twig | — |
| [templates/pages/management/budget.html.twig](../templates/pages/management/budget.html.twig) | .twig | — |
| [templates/pages/management/certificate.html.twig](../templates/pages/management/certificate.html.twig) | .twig | — |
| [templates/pages/management/contact_supplier.html.twig](../templates/pages/management/contact_supplier.html.twig) | .twig | — |
| [templates/pages/management/contract.html.twig](../templates/pages/management/contract.html.twig) | .twig | — |
| [templates/pages/management/cost.html.twig](../templates/pages/management/cost.html.twig) | .twig | — |
| [templates/pages/management/database.html.twig](../templates/pages/management/database.html.twig) | .twig | — |
| [templates/pages/management/databaseinstance.html.twig](../templates/pages/management/databaseinstance.html.twig) | .twig | — |
| [templates/pages/management/dcroom.html.twig](../templates/pages/management/dcroom.html.twig) | .twig | — |
| [templates/pages/management/dcroom_racks.html.twig](../templates/pages/management/dcroom_racks.html.twig) | .twig | — |
| [templates/pages/management/document.html.twig](../templates/pages/management/document.html.twig) | .twig | — |
| [templates/pages/management/document_item.html.twig](../templates/pages/management/document_item.html.twig) | .twig | — |
| [templates/pages/management/domainrecord.html.twig](../templates/pages/management/domainrecord.html.twig) | .twig | — |
| [templates/pages/management/domainrecordtype_helper.html.twig](../templates/pages/management/domainrecordtype_helper.html.twig) | .twig | — |
| [templates/pages/management/license_progressbar.html.twig](../templates/pages/management/license_progressbar.html.twig) | .twig | — |
| [templates/pages/management/line.html.twig](../templates/pages/management/line.html.twig) | .twig | — |
| [templates/pages/management/softwarelicense.html.twig](../templates/pages/management/softwarelicense.html.twig) | .twig | — |
| [templates/pages/oauth/authorize.html.twig](../templates/pages/oauth/authorize.html.twig) | .twig | — |
| [templates/pages/reauth/cas_form.html.twig](../templates/pages/reauth/cas_form.html.twig) | .twig | — |
| [templates/pages/reauth/fallback_form.html.twig](../templates/pages/reauth/fallback_form.html.twig) | .twig | — |
| [templates/pages/reauth/password_form.html.twig](../templates/pages/reauth/password_form.html.twig) | .twig | — |
| [templates/pages/reauth/prompt.html.twig](../templates/pages/reauth/prompt.html.twig) | .twig | — |
| [templates/pages/reauth/totp_form.html.twig](../templates/pages/reauth/totp_form.html.twig) | .twig | — |
| [templates/pages/redirect_post.html.twig](../templates/pages/redirect_post.html.twig) | .twig | — |
| [templates/pages/self-service/service_catalog.html.twig](../templates/pages/self-service/service_catalog.html.twig) | .twig | — |
| [templates/pages/service-levels/levelagreement.html.twig](../templates/pages/service-levels/levelagreement.html.twig) | .twig | — |
| [templates/pages/setup/apiclient.html.twig](../templates/pages/setup/apiclient.html.twig) | .twig | — |
| [templates/pages/setup/authentication.html.twig](../templates/pages/setup/authentication.html.twig) | .twig | — |
| [templates/pages/setup/authentication/ldap_replicate.html.twig](../templates/pages/setup/authentication/ldap_replicate.html.twig) | .twig | — |
| [templates/pages/setup/authentication/mail.html.twig](../templates/pages/setup/authentication/mail.html.twig) | .twig | — |
| [templates/pages/setup/authentication/other_ext_setup.html.twig](../templates/pages/setup/authentication/other_ext_setup.html.twig) | .twig | — |
| [templates/pages/setup/authentication/setup.html.twig](../templates/pages/setup/authentication/setup.html.twig) | .twig | — |
| [templates/pages/setup/authentication/sync.html.twig](../templates/pages/setup/authentication/sync.html.twig) | .twig | — |
| [templates/pages/setup/calendar_holiday.html.twig](../templates/pages/setup/calendar_holiday.html.twig) | .twig | — |
| [templates/pages/setup/calendarsegment.html.twig](../templates/pages/setup/calendarsegment.html.twig) | .twig | — |
| [templates/pages/setup/crontask/crontask.html.twig](../templates/pages/setup/crontask/crontask.html.twig) | .twig | — |
| [templates/pages/setup/crontask/statistics.html.twig](../templates/pages/setup/crontask/statistics.html.twig) | .twig | — |
| [templates/pages/setup/custom_dropdown.html.twig](../templates/pages/setup/custom_dropdown.html.twig) | .twig | — |
| [templates/pages/setup/data_privacy/session_retention.html.twig](../templates/pages/setup/data_privacy/session_retention.html.twig) | .twig | — |
| [templates/pages/setup/dropdowns_list.html.twig](../templates/pages/setup/dropdowns_list.html.twig) | .twig | — |
| [templates/pages/setup/dropdowntranslation.html.twig](../templates/pages/setup/dropdowntranslation.html.twig) | .twig | — |
| [templates/pages/setup/externallink.html.twig](../templates/pages/setup/externallink.html.twig) | .twig | — |
| [templates/pages/setup/externallink_itemtype.html.twig](../templates/pages/setup/externallink_itemtype.html.twig) | .twig | — |
| [templates/pages/setup/general/api_apiclients_section.html.twig](../templates/pages/setup/general/api_apiclients_section.html.twig) | .twig | — |
| [templates/pages/setup/general/api_setup.html.twig](../templates/pages/setup/general/api_setup.html.twig) | .twig | — |
| [templates/pages/setup/general/assets_setup.html.twig](../templates/pages/setup/general/assets_setup.html.twig) | .twig | — |
| [templates/pages/setup/general/assistance_setup.html.twig](../templates/pages/setup/general/assistance_setup.html.twig) | .twig | — |
| [templates/pages/setup/general/base_form.html.twig](../templates/pages/setup/general/base_form.html.twig) | .twig | — |
| [templates/pages/setup/general/dbreplica_setup.html.twig](../templates/pages/setup/general/dbreplica_setup.html.twig) | .twig | — |
| [templates/pages/setup/general/general_setup.html.twig](../templates/pages/setup/general/general_setup.html.twig) | .twig | — |
| [templates/pages/setup/general/glpinetwork_setup.html.twig](../templates/pages/setup/general/glpinetwork_setup.html.twig) | .twig | — |
| [templates/pages/setup/general/logs_setup.html.twig](../templates/pages/setup/general/logs_setup.html.twig) | .twig | — |
| [templates/pages/setup/general/management_setup.html.twig](../templates/pages/setup/general/management_setup.html.twig) | .twig | — |
| [templates/pages/setup/general/performance.html.twig](../templates/pages/setup/general/performance.html.twig) | .twig | — |
| [templates/pages/setup/general/preferences_setup.html.twig](../templates/pages/setup/general/preferences_setup.html.twig) | .twig | — |
| [templates/pages/setup/general/systeminfo_form.html.twig](../templates/pages/setup/general/systeminfo_form.html.twig) | .twig | — |
| [templates/pages/setup/general/systeminfo_table.html.twig](../templates/pages/setup/general/systeminfo_table.html.twig) | .twig | — |
| [templates/pages/setup/ldap/adv_info.html.twig](../templates/pages/setup/ldap/adv_info.html.twig) | .twig | — |
| [templates/pages/setup/ldap/form.html.twig](../templates/pages/setup/ldap/form.html.twig) | .twig | — |
| [templates/pages/setup/ldap/group_config.html.twig](../templates/pages/setup/ldap/group_config.html.twig) | .twig | — |
| [templates/pages/setup/ldap/test_form.html.twig](../templates/pages/setup/ldap/test_form.html.twig) | .twig | — |
| [templates/pages/setup/ldap/user_config_form.html.twig](../templates/pages/setup/ldap/user_config_form.html.twig) | .twig | — |
| [templates/pages/setup/levelagreement_level.html.twig](../templates/pages/setup/levelagreement_level.html.twig) | .twig | — |
| [templates/pages/setup/mailcollector/folder_list.html.twig](../templates/pages/setup/mailcollector/folder_list.html.twig) | .twig | — |
| [templates/pages/setup/mailcollector/server_config_fields.html.twig](../templates/pages/setup/mailcollector/server_config_fields.html.twig) | .twig | — |
| [templates/pages/setup/mailcollector/setup_form.html.twig](../templates/pages/setup/mailcollector/setup_form.html.twig) | .twig | — |
| [templates/pages/setup/manuallink.html.twig](../templates/pages/setup/manuallink.html.twig) | .twig | — |
| [templates/pages/setup/marketplace/card.html.twig](../templates/pages/setup/marketplace/card.html.twig) | .twig | — |
| [templates/pages/setup/notification/ajax_setting.html.twig](../templates/pages/setup/notification/ajax_setting.html.twig) | .twig | — |
| [templates/pages/setup/notification/group_notifications.html.twig](../templates/pages/setup/notification/group_notifications.html.twig) | .twig | — |
| [templates/pages/setup/notification/mailing_setting.html.twig](../templates/pages/setup/notification/mailing_setting.html.twig) | .twig | — |
| [templates/pages/setup/notification/notification.html.twig](../templates/pages/setup/notification/notification.html.twig) | .twig | — |
| [templates/pages/setup/notification/notification_notificationtemplate.html.twig](../templates/pages/setup/notification/notification_notificationtemplate.html.twig) | .twig | — |
| [templates/pages/setup/notification/queued_notification.html.twig](../templates/pages/setup/notification/queued_notification.html.twig) | .twig | — |
| [templates/pages/setup/notification/recipients.html.twig](../templates/pages/setup/notification/recipients.html.twig) | .twig | — |
| [templates/pages/setup/notification/template.html.twig](../templates/pages/setup/notification/template.html.twig) | .twig | — |
| [templates/pages/setup/notification/translation.html.twig](../templates/pages/setup/notification/translation.html.twig) | .twig | — |
| [templates/pages/setup/notification/translation_debug.html.twig](../templates/pages/setup/notification/translation_debug.html.twig) | .twig | — |
| [templates/pages/setup/oauthclient.html.twig](../templates/pages/setup/oauthclient.html.twig) | .twig | — |
| [templates/pages/setup/security/2fa.html.twig](../templates/pages/setup/security/2fa.html.twig) | .twig | — |
| [templates/pages/setup/security/password_policy.html.twig](../templates/pages/setup/security/password_policy.html.twig) | .twig | — |
| [templates/pages/setup/sessiontracker/sessiontracker.html.twig](../templates/pages/setup/sessiontracker/sessiontracker.html.twig) | .twig | — |
| [templates/pages/setup/setup_notifications.html.twig](../templates/pages/setup/setup_notifications.html.twig) | .twig | — |
| [templates/pages/setup/webhook/payload_editor.html.twig](../templates/pages/setup/webhook/payload_editor.html.twig) | .twig | — |
| [templates/pages/setup/webhook/queuedwebhook.html.twig](../templates/pages/setup/webhook/queuedwebhook.html.twig) | .twig | — |
| [templates/pages/setup/webhook/webhook.html.twig](../templates/pages/setup/webhook/webhook.html.twig) | .twig | — |
| [templates/pages/setup/webhook/webhook_headers.html.twig](../templates/pages/setup/webhook/webhook_headers.html.twig) | .twig | — |
| [templates/pages/setup/webhook/webhook_security.html.twig](../templates/pages/setup/webhook/webhook_security.html.twig) | .twig | — |
| [templates/pages/setup/webhook/webhooktest.html.twig](../templates/pages/setup/webhook/webhooktest.html.twig) | .twig | — |
| [templates/pages/tools/find_available_reservation.html.twig](../templates/pages/tools/find_available_reservation.html.twig) | .twig | — |
| [templates/pages/tools/item_project.html.twig](../templates/pages/tools/item_project.html.twig) | .twig | — |
| [templates/pages/tools/kb/_actions_menu.html.twig](../templates/pages/tools/kb/_actions_menu.html.twig) | .twig | — |
| [templates/pages/tools/kb/_article_row.html.twig](../templates/pages/tools/kb/_article_row.html.twig) | .twig | — |
| [templates/pages/tools/kb/article.html.twig](../templates/pages/tools/kb/article.html.twig) | .twig | — |
| [templates/pages/tools/kb/aside.html.twig](../templates/pages/tools/kb/aside.html.twig) | .twig | — |
| [templates/pages/tools/kb/aside_actions.html.twig](../templates/pages/tools/kb/aside_actions.html.twig) | .twig | — |
| [templates/pages/tools/kb/aside_children.html.twig](../templates/pages/tools/kb/aside_children.html.twig) | .twig | — |
| [templates/pages/tools/kb/aside_search_results.html.twig](../templates/pages/tools/kb/aside_search_results.html.twig) | .twig | — |
| [templates/pages/tools/kb/aside_tree.html.twig](../templates/pages/tools/kb/aside_tree.html.twig) | .twig | — |
| [templates/pages/tools/kb/child_article_row.html.twig](../templates/pages/tools/kb/child_article_row.html.twig) | .twig | — |
| [templates/pages/tools/kb/comment_form.html.twig](../templates/pages/tools/kb/comment_form.html.twig) | .twig | — |
| [templates/pages/tools/kb/document_badge.html.twig](../templates/pages/tools/kb/document_badge.html.twig) | .twig | — |
| [templates/pages/tools/kb/faq_article.html.twig](../templates/pages/tools/kb/faq_article.html.twig) | .twig | — |
| [templates/pages/tools/kb/knowbaseitem_item.html.twig](../templates/pages/tools/kb/knowbaseitem_item.html.twig) | .twig | — |
| [templates/pages/tools/kb/modal/move.html.twig](../templates/pages/tools/kb/modal/move.html.twig) | .twig | — |
| [templates/pages/tools/kb/modal/permissions.html.twig](../templates/pages/tools/kb/modal/permissions.html.twig) | .twig | — |
| [templates/pages/tools/kb/modal/schedule_visibility.html.twig](../templates/pages/tools/kb/modal/schedule_visibility.html.twig) | .twig | — |
| [templates/pages/tools/kb/modal/service_catalog.html.twig](../templates/pages/tools/kb/modal/service_catalog.html.twig) | .twig | — |
| [templates/pages/tools/kb/permission_dropdown.html.twig](../templates/pages/tools/kb/permission_dropdown.html.twig) | .twig | — |
| [templates/pages/tools/kb/permission_entry.html.twig](../templates/pages/tools/kb/permission_entry.html.twig) | .twig | — |
| [templates/pages/tools/kb/permission_subvisibility.html.twig](../templates/pages/tools/kb/permission_subvisibility.html.twig) | .twig | — |
| [templates/pages/tools/kb/related_item_badge.html.twig](../templates/pages/tools/kb/related_item_badge.html.twig) | .twig | — |
| [templates/pages/tools/kb/share_popover.html.twig](../templates/pages/tools/kb/share_popover.html.twig) | .twig | — |
| [templates/pages/tools/kb/shared_article.html.twig](../templates/pages/tools/kb/shared_article.html.twig) | .twig | — |
| [templates/pages/tools/kb/sidepanel/base.html.twig](../templates/pages/tools/kb/sidepanel/base.html.twig) | .twig | — |
| [templates/pages/tools/kb/sidepanel/comment.html.twig](../templates/pages/tools/kb/sidepanel/comment.html.twig) | .twig | — |
| [templates/pages/tools/kb/sidepanel/comment_reply_form.html.twig](../templates/pages/tools/kb/sidepanel/comment_reply_form.html.twig) | .twig | — |
| [templates/pages/tools/kb/sidepanel/comments.html.twig](../templates/pages/tools/kb/sidepanel/comments.html.twig) | .twig | — |
| [templates/pages/tools/kb/sidepanel/comments_thread.html.twig](../templates/pages/tools/kb/sidepanel/comments_thread.html.twig) | .twig | — |
| [templates/pages/tools/kb/sidepanel/revision_item.html.twig](../templates/pages/tools/kb/sidepanel/revision_item.html.twig) | .twig | — |
| [templates/pages/tools/kb/sidepanel/revisions.html.twig](../templates/pages/tools/kb/sidepanel/revisions.html.twig) | .twig | — |
| [templates/pages/tools/kb/sidepanel/revisions_page.html.twig](../templates/pages/tools/kb/sidepanel/revisions_page.html.twig) | .twig | — |
| [templates/pages/tools/project.html.twig](../templates/pages/tools/project.html.twig) | .twig | — |
| [templates/pages/tools/project_task.html.twig](../templates/pages/tools/project_task.html.twig) | .twig | — |
| [templates/pages/tools/reminder.html.twig](../templates/pages/tools/reminder.html.twig) | .twig | — |
| [templates/pages/tools/reminder_planning.html.twig](../templates/pages/tools/reminder_planning.html.twig) | .twig | — |
| [templates/pages/tools/reminder_translation.html.twig](../templates/pages/tools/reminder_translation.html.twig) | .twig | — |
| [templates/pages/tools/report/network_criteria.html.twig](../templates/pages/tools/report/network_criteria.html.twig) | .twig | — |
| [templates/pages/tools/rss_form.html.twig](../templates/pages/tools/rss_form.html.twig) | .twig | — |
| [templates/pages/tools/savedsearch/alert.html.twig](../templates/pages/tools/savedsearch/alert.html.twig) | .twig | — |
| [templates/pages/tools/savedsearch/alert_list_notification.html.twig](../templates/pages/tools/savedsearch/alert_list_notification.html.twig) | .twig | — |
| [templates/pages/tools/savedsearch/form.html.twig](../templates/pages/tools/savedsearch/form.html.twig) | .twig | — |
| [templates/pages/tools/savedsearch/save_button.html.twig](../templates/pages/tools/savedsearch/save_button.html.twig) | .twig | — |
| [templates/pages/tools/search_knowbaseitem.html.twig](../templates/pages/tools/search_knowbaseitem.html.twig) | .twig | — |
| [templates/password_form.html.twig](../templates/password_form.html.twig) | .twig | — |
| [templates/stencil/editor.html.twig](../templates/stencil/editor.html.twig) | .twig | — |
| [templates/stencil/parts/label.html.twig](../templates/stencil/parts/label.html.twig) | .twig | — |
| [templates/stencil/parts/port/popover.html.twig](../templates/stencil/parts/port/popover.html.twig) | .twig | — |
| [templates/stencil/parts/port/status.html.twig](../templates/stencil/parts/port/status.html.twig) | .twig | — |
| [templates/stencil/parts/zones.html.twig](../templates/stencil/parts/zones.html.twig) | .twig | — |
| [templates/stencil/view.html.twig](../templates/stencil/view.html.twig) | .twig | — |
| [templates/twig_components/Alert/Base.html.twig](../templates/twig_components/Alert/Base.html.twig) | .twig | — |
| [templates/twig_components/Mfa/CodeInput.html.twig](../templates/twig_components/Mfa/CodeInput.html.twig) | .twig | — |
| [templates/updatepassword.html.twig](../templates/updatepassword.html.twig) | .twig | — |

## tests


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [tests/Autoload.php](../tests/Autoload.php) | .php | class Autoload extends DbTestCase |
| [tests/LDAP/AuthLdapTest.php](../tests/LDAP/AuthLdapTest.php) | .php | class tests\units\AuthLdapTest extends DbTestCase |
| [tests/LDAP/LdapReAuthStrategyTest.php](../tests/LDAP/LdapReAuthStrategyTest.php) | .php | class tests\units\LdapReAuthStrategyTest extends DbTestCase |
| [tests/LDAP/README.ldap](../tests/LDAP/README.ldap) | .ldap | — |
| [tests/LDAP/ldif/00-admin.ldif](../tests/LDAP/ldif/00-admin.ldif) | .ldif | — |
| [tests/LDAP/ldif/10-users.ldif](../tests/LDAP/ldif/10-users.ldif) | .ldif | — |
| [tests/NotificationSettingInstance.php](../tests/NotificationSettingInstance.php) | .php | class NotificationSettingInstance extends NotificationSetting |
| [tests/README.md](../tests/README.md) | .md | — |
| [tests/bin/test-updated-data](../tests/bin/test-updated-data) | sem extensão | — |
| [tests/bootstrap.php](../tests/bootstrap.php) | .php | — |
| [tests/config/.gitignore](../tests/config/.gitignore) | sem extensão | — |
| [tests/deprecated-searchoptions/ComputerAntivirus.json](../tests/deprecated-searchoptions/ComputerAntivirus.json) | .json | — |
| [tests/deprecated-searchoptions/ComputerVirtualMachine.json](../tests/deprecated-searchoptions/ComputerVirtualMachine.json) | .json | — |
| [tests/deprecated-searchoptions/Computer_Item.json](../tests/deprecated-searchoptions/Computer_Item.json) | .json | — |
| [tests/deprecated-searchoptions/Computer_SoftwareLicense.json](../tests/deprecated-searchoptions/Computer_SoftwareLicense.json) | .json | — |
| [tests/deprecated-searchoptions/Computer_SoftwareVersion.json](../tests/deprecated-searchoptions/Computer_SoftwareVersion.json) | .json | — |
| [tests/deprecated-searchoptions/TicketFollowup.json](../tests/deprecated-searchoptions/TicketFollowup.json) | .json | — |
| [tests/e2e/.env](../tests/e2e/.env) | sem extensão | — |
| [tests/e2e/README.md](../tests/e2e/README.md) | .md | — |
| [tests/e2e/fixtures/glpi_fixture.ts](../tests/e2e/fixtures/glpi_fixture.ts) | .ts | — |
| [tests/e2e/fixtures/uploads/test-image.png](../tests/e2e/fixtures/uploads/test-image.png) | .png | — |
| [tests/e2e/fixtures/uploads/test.json](../tests/e2e/fixtures/uploads/test.json) | .json | — |
| [tests/e2e/glpi_config/.gitignore](../tests/e2e/glpi_config/.gitignore) | sem extensão | — |
| [tests/e2e/glpi_files/.gitignore](../tests/e2e/glpi_files/.gitignore) | sem extensão | — |
| [tests/e2e/pages/AssetDefinitionPage.ts](../tests/e2e/pages/AssetDefinitionPage.ts) | .ts | — |
| [tests/e2e/pages/ComputerPage.ts](../tests/e2e/pages/ComputerPage.ts) | .ts | — |
| [tests/e2e/pages/DisplayPreferencePage.ts](../tests/e2e/pages/DisplayPreferencePage.ts) | .ts | — |
| [tests/e2e/pages/DocumentPage.ts](../tests/e2e/pages/DocumentPage.ts) | .ts | — |
| [tests/e2e/pages/EntityPage.ts](../tests/e2e/pages/EntityPage.ts) | .ts | — |
| [tests/e2e/pages/EntityPageTabs.ts](../tests/e2e/pages/EntityPageTabs.ts) | .ts | — |
| [tests/e2e/pages/FormCategoryPage.ts](../tests/e2e/pages/FormCategoryPage.ts) | .ts | — |
| [tests/e2e/pages/FormPage.ts](../tests/e2e/pages/FormPage.ts) | .ts | — |
| [tests/e2e/pages/FormRenderPage.ts](../tests/e2e/pages/FormRenderPage.ts) | .ts | — |
| [tests/e2e/pages/FormTranslationPage.ts](../tests/e2e/pages/FormTranslationPage.ts) | .ts | — |
| [tests/e2e/pages/GlpiPage.ts](../tests/e2e/pages/GlpiPage.ts) | .ts | — |
| [tests/e2e/pages/HelpdeskConfigTab.ts](../tests/e2e/pages/HelpdeskConfigTab.ts) | .ts | — |
| [tests/e2e/pages/HelpdeskTranslationPage.ts](../tests/e2e/pages/HelpdeskTranslationPage.ts) | .ts | — |
| [tests/e2e/pages/IllustrationPickerPage.ts](../tests/e2e/pages/IllustrationPickerPage.ts) | .ts | — |
| [tests/e2e/pages/ImpactPage.ts](../tests/e2e/pages/ImpactPage.ts) | .ts | — |
| [tests/e2e/pages/KnowbaseItemPage.ts](../tests/e2e/pages/KnowbaseItemPage.ts) | .ts | — |
| [tests/e2e/pages/LogViewerPage.ts](../tests/e2e/pages/LogViewerPage.ts) | .ts | — |
| [tests/e2e/pages/LoginPage.ts](../tests/e2e/pages/LoginPage.ts) | .ts | — |
| [tests/e2e/pages/NetworkEquipmentModelPage.ts](../tests/e2e/pages/NetworkEquipmentModelPage.ts) | .ts | — |
| [tests/e2e/pages/NotificationPage.ts](../tests/e2e/pages/NotificationPage.ts) | .ts | — |
| [tests/e2e/pages/NotificationTemplatePage.ts](../tests/e2e/pages/NotificationTemplatePage.ts) | .ts | — |
| [tests/e2e/pages/PlanningPage.ts](../tests/e2e/pages/PlanningPage.ts) | .ts | — |
| [tests/e2e/pages/PreferencePage.ts](../tests/e2e/pages/PreferencePage.ts) | .ts | — |
| [tests/e2e/pages/PrinterPage.ts](../tests/e2e/pages/PrinterPage.ts) | .ts | — |
| [tests/e2e/pages/ReAuthPromptPage.ts](../tests/e2e/pages/ReAuthPromptPage.ts) | .ts | — |
| [tests/e2e/pages/ReservationPage.ts](../tests/e2e/pages/ReservationPage.ts) | .ts | — |
| [tests/e2e/pages/SearchEnginePage.ts](../tests/e2e/pages/SearchEnginePage.ts) | .ts | — |
| [tests/e2e/pages/ServiceCatalogPage.ts](../tests/e2e/pages/ServiceCatalogPage.ts) | .ts | — |
| [tests/e2e/pages/TicketPage.ts](../tests/e2e/pages/TicketPage.ts) | .ts | — |
| [tests/e2e/pages/UserPage.ts](../tests/e2e/pages/UserPage.ts) | .ts | — |
| [tests/e2e/pages/WebhookPage.ts](../tests/e2e/pages/WebhookPage.ts) | .ts | — |
| [tests/e2e/specs/Accessibility/autocomplete_hints.spec.ts](../tests/e2e/specs/Accessibility/autocomplete_hints.spec.ts) | .ts | — |
| [tests/e2e/specs/Admin/log_viewer.spec.ts](../tests/e2e/specs/Admin/log_viewer.spec.ts) | .ts | — |
| [tests/e2e/specs/Admin/user.spec.ts](../tests/e2e/specs/Admin/user.spec.ts) | .ts | — |
| [tests/e2e/specs/Asset/asset_definition.spec.ts](../tests/e2e/specs/Asset/asset_definition.spec.ts) | .ts | — |
| [tests/e2e/specs/Asset/computer.spec.ts](../tests/e2e/specs/Asset/computer.spec.ts) | .ts | — |
| [tests/e2e/specs/Asset/custom_fields.spec.ts](../tests/e2e/specs/Asset/custom_fields.spec.ts) | .ts | — |
| [tests/e2e/specs/Asset/impact.spec.ts](../tests/e2e/specs/Asset/impact.spec.ts) | .ts | — |
| [tests/e2e/specs/Asset/network_ports_graphical_definition.spec.ts](../tests/e2e/specs/Asset/network_ports_graphical_definition.spec.ts) | .ts | — |
| [tests/e2e/specs/Asset/printer.spec.ts](../tests/e2e/specs/Asset/printer.spec.ts) | .ts | — |
| [tests/e2e/specs/Controller/ajax_controller.spec.ts](../tests/e2e/specs/Controller/ajax_controller.spec.ts) | .ts | — |
| [tests/e2e/specs/Dashboard/dashboards.spec.ts](../tests/e2e/specs/Dashboard/dashboards.spec.ts) | .ts | — |
| [tests/e2e/specs/DebugMode/debug_bar.spec.ts](../tests/e2e/specs/DebugMode/debug_bar.spec.ts) | .ts | — |
| [tests/e2e/specs/DebugMode/debug_mode.spec.ts](../tests/e2e/specs/DebugMode/debug_mode.spec.ts) | .ts | — |
| [tests/e2e/specs/Document/image_paste.spec.ts](../tests/e2e/specs/Document/image_paste.spec.ts) | .ts | — |
| [tests/e2e/specs/Document/upload.spec.ts](../tests/e2e/specs/Document/upload.spec.ts) | .ts | — |
| [tests/e2e/specs/Dropdown/dropdown_a11y.spec.ts](../tests/e2e/specs/Dropdown/dropdown_a11y.spec.ts) | .ts | — |
| [tests/e2e/specs/Entity/entity.spec.ts](../tests/e2e/specs/Entity/entity.spec.ts) | .ts | — |
| [tests/e2e/specs/Entity/entity_creation.spec.ts](../tests/e2e/specs/Entity/entity_creation.spec.ts) | .ts | — |
| [tests/e2e/specs/Entity/entity_selector.spec.ts](../tests/e2e/specs/Entity/entity_selector.spec.ts) | .ts | — |
| [tests/e2e/specs/Entity/notes.spec.ts](../tests/e2e/specs/Entity/notes.spec.ts) | .ts | — |
| [tests/e2e/specs/Error/error_page.spec.ts](../tests/e2e/specs/Error/error_page.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/AccessPolicies/access_control.spec.ts](../tests/e2e/specs/Form/AccessPolicies/access_control.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/AccessPolicies/direct_access.spec.ts](../tests/e2e/specs/Form/AccessPolicies/direct_access.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/actors.spec.ts](../tests/e2e/specs/Form/DestinationConfig/actors.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/associated_items.spec.ts](../tests/e2e/specs/Form/DestinationConfig/associated_items.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/content.spec.ts](../tests/e2e/specs/Form/DestinationConfig/content.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/entity.spec.ts](../tests/e2e/specs/Form/DestinationConfig/entity.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/itilcategory.spec.ts](../tests/e2e/specs/Form/DestinationConfig/itilcategory.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/itilfollowup.spec.ts](../tests/e2e/specs/Form/DestinationConfig/itilfollowup.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/itiltask.spec.ts](../tests/e2e/specs/Form/DestinationConfig/itiltask.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/linked_itilobjects.spec.ts](../tests/e2e/specs/Form/DestinationConfig/linked_itilobjects.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/location.spec.ts](../tests/e2e/specs/Form/DestinationConfig/location.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/request_source.spec.ts](../tests/e2e/specs/Form/DestinationConfig/request_source.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/request_type.spec.ts](../tests/e2e/specs/Form/DestinationConfig/request_type.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/service_levels.spec.ts](../tests/e2e/specs/Form/DestinationConfig/service_levels.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/template.spec.ts](../tests/e2e/specs/Form/DestinationConfig/template.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/title.spec.ts](../tests/e2e/specs/Form/DestinationConfig/title.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/urgency.spec.ts](../tests/e2e/specs/Form/DestinationConfig/urgency.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/DestinationConfig/validation.spec.ts](../tests/e2e/specs/Form/DestinationConfig/validation.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/QuestionTypes/actors.spec.ts](../tests/e2e/specs/Form/QuestionTypes/actors.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/QuestionTypes/date_and_time.spec.ts](../tests/e2e/specs/Form/QuestionTypes/date_and_time.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/QuestionTypes/dropdown.spec.ts](../tests/e2e/specs/Form/QuestionTypes/dropdown.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/QuestionTypes/dropdown_item.spec.ts](../tests/e2e/specs/Form/QuestionTypes/dropdown_item.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/QuestionTypes/item.spec.ts](../tests/e2e/specs/Form/QuestionTypes/item.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/QuestionTypes/number.spec.ts](../tests/e2e/specs/Form/QuestionTypes/number.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/QuestionTypes/selectables.spec.ts](../tests/e2e/specs/Form/QuestionTypes/selectables.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/QuestionTypes/user_device.spec.ts](../tests/e2e/specs/Form/QuestionTypes/user_device.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/Serializer/export.spec.ts](../tests/e2e/specs/Form/Serializer/export.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/Serializer/import.spec.ts](../tests/e2e/specs/Form/Serializer/import.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/ServiceCatalog/default_forms.spec.ts](../tests/e2e/specs/Form/ServiceCatalog/default_forms.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/ServiceCatalog/service_catalog_tab.spec.ts](../tests/e2e/specs/Form/ServiceCatalog/service_catalog_tab.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/category.spec.ts](../tests/e2e/specs/Form/category.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/comment.spec.ts](../tests/e2e/specs/Form/comment.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/conditions_applied.spec.ts](../tests/e2e/specs/Form/conditions_applied.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/conditions_dependencies.spec.ts](../tests/e2e/specs/Form/conditions_dependencies.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/conditions_editor.spec.ts](../tests/e2e/specs/Form/conditions_editor.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/conditions_editor_on_each_question_types.spec.ts](../tests/e2e/specs/Form/conditions_editor_on_each_question_types.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/convert_default_values.spec.ts](../tests/e2e/specs/Form/convert_default_values.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/delegation.spec.ts](../tests/e2e/specs/Form/delegation.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/destination.spec.ts](../tests/e2e/specs/Form/destination.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/editor.spec.ts](../tests/e2e/specs/Form/editor.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/form_rendering.spec.ts](../tests/e2e/specs/Form/form_rendering.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/form_tags.spec.ts](../tests/e2e/specs/Form/form_tags.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/form_translation.spec.ts](../tests/e2e/specs/Form/form_translation.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/form_translations.spec.ts](../tests/e2e/specs/Form/form_translations.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/horizontal_layout.spec.ts](../tests/e2e/specs/Form/horizontal_layout.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/plugins.spec.ts](../tests/e2e/specs/Form/plugins.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/preview.spec.ts](../tests/e2e/specs/Form/preview.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/public.spec.ts](../tests/e2e/specs/Form/public.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/redirect_after_submit.spec.ts](../tests/e2e/specs/Form/redirect_after_submit.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/rendering_layouts.spec.ts](../tests/e2e/specs/Form/rendering_layouts.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/validation.spec.ts](../tests/e2e/specs/Form/validation.spec.ts) | .ts | — |
| [tests/e2e/specs/Form/validations.spec.ts](../tests/e2e/specs/Form/validations.spec.ts) | .ts | — |
| [tests/e2e/specs/Helpdesk/home.spec.ts](../tests/e2e/specs/Helpdesk/home.spec.ts) | .ts | — |
| [tests/e2e/specs/Helpdesk/home_config.spec.ts](../tests/e2e/specs/Helpdesk/home_config.spec.ts) | .ts | — |
| [tests/e2e/specs/Helpdesk/home_search.spec.ts](../tests/e2e/specs/Helpdesk/home_search.spec.ts) | .ts | — |
| [tests/e2e/specs/Helpdesk/service_catalog.spec.ts](../tests/e2e/specs/Helpdesk/service_catalog.spec.ts) | .ts | — |
| [tests/e2e/specs/Helpdesk/translation.spec.isolated.ts](../tests/e2e/specs/Helpdesk/translation.spec.isolated.ts) | .ts | — |
| [tests/e2e/specs/ITILObject/itiltask_template.spec.ts](../tests/e2e/specs/ITILObject/itiltask_template.spec.ts) | .ts | — |
| [tests/e2e/specs/ITILObject/massive_actions.spec.ts](../tests/e2e/specs/ITILObject/massive_actions.spec.ts) | .ts | — |
| [tests/e2e/specs/Illustration/illustration_picker.spec.ts](../tests/e2e/specs/Illustration/illustration_picker.spec.ts) | .ts | — |
| [tests/e2e/specs/Inventory/inventory_a11y.spec.ts](../tests/e2e/specs/Inventory/inventory_a11y.spec.ts) | .ts | — |
| [tests/e2e/specs/Itil/stats_tab_rendering.spec.ts](../tests/e2e/specs/Itil/stats_tab_rendering.spec.ts) | .ts | — |
| [tests/e2e/specs/Kanban/kanban.spec.ts](../tests/e2e/specs/Kanban/kanban.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/Comments/comment-on-selection.spec.ts](../tests/e2e/specs/Knowbase/Comments/comment-on-selection.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/Editor/bubble-menu.spec.ts](../tests/e2e/specs/Knowbase/Editor/bubble-menu.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/Editor/core.spec.ts](../tests/e2e/specs/Knowbase/Editor/core.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/Editor/image-insertion.spec.ts](../tests/e2e/specs/Knowbase/Editor/image-insertion.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/Editor/link-dialog.spec.ts](../tests/e2e/specs/Knowbase/Editor/link-dialog.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/Editor/slash-commands.spec.ts](../tests/e2e/specs/Knowbase/Editor/slash-commands.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/Editor/table.spec.ts](../tests/e2e/specs/Knowbase/Editor/table.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/Editor/video-embed.spec.ts](../tests/e2e/specs/Knowbase/Editor/video-embed.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/aside-actions-prefetch.spec.ts](../tests/e2e/specs/Knowbase/aside-actions-prefetch.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/aside-create-article.spec.ts](../tests/e2e/specs/Knowbase/aside-create-article.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/child_entities.spec.ts](../tests/e2e/specs/Knowbase/child_entities.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/comments.spec.ts](../tests/e2e/specs/Knowbase/comments.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/create.spec.ts](../tests/e2e/specs/Knowbase/create.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/delete.spec.ts](../tests/e2e/specs/Knowbase/delete.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/document_upload.spec.ts](../tests/e2e/specs/Knowbase/document_upload.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/entry_point.spec.ts](../tests/e2e/specs/Knowbase/entry_point.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/faq-aside.spec.ts](../tests/e2e/specs/Knowbase/faq-aside.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/faq.spec.ts](../tests/e2e/specs/Knowbase/faq.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/history-sharing.spec.ts](../tests/e2e/specs/Knowbase/history-sharing.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/illustration-optional.spec.ts](../tests/e2e/specs/Knowbase/illustration-optional.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/illustration.spec.ts](../tests/e2e/specs/Knowbase/illustration.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-aside-actions.spec.ts](../tests/e2e/specs/Knowbase/kb-aside-actions.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-aside-category-fold.spec.ts](../tests/e2e/specs/Knowbase/kb-aside-category-fold.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-aside-drag.spec.ts](../tests/e2e/specs/Knowbase/kb-aside-drag.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-aside-move-modal.spec.ts](../tests/e2e/specs/Knowbase/kb-aside-move-modal.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-aside-resize.spec.ts](../tests/e2e/specs/Knowbase/kb-aside-resize.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-aside-search.spec.ts](../tests/e2e/specs/Knowbase/kb-aside-search.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-aside-toggle.spec.ts](../tests/e2e/specs/Knowbase/kb-aside-toggle.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-favorites.spec.ts](../tests/e2e/specs/Knowbase/kb-favorites.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-link-document.spec.ts](../tests/e2e/specs/Knowbase/kb-link-document.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-sub-articles-tab.spec.ts](../tests/e2e/specs/Knowbase/kb-sub-articles-tab.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-translation-revisions.spec.ts](../tests/e2e/specs/Knowbase/kb-translation-revisions.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/kb-unlink-document.spec.ts](../tests/e2e/specs/Knowbase/kb-unlink-document.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/permissions.spec.ts](../tests/e2e/specs/Knowbase/permissions.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/related_items.spec.ts](../tests/e2e/specs/Knowbase/related_items.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/responsive_offcanvas.spec.ts](../tests/e2e/specs/Knowbase/responsive_offcanvas.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/revisions.spec.ts](../tests/e2e/specs/Knowbase/revisions.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/service_catalog.spec.ts](../tests/e2e/specs/Knowbase/service_catalog.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/sharing.spec.ts](../tests/e2e/specs/Knowbase/sharing.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/translations.spec.ts](../tests/e2e/specs/Knowbase/translations.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/tree_browse.spec.ts](../tests/e2e/specs/Knowbase/tree_browse.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/unsaved_changes.spec.ts](../tests/e2e/specs/Knowbase/unsaved_changes.spec.ts) | .ts | — |
| [tests/e2e/specs/Knowbase/visibility_dates.spec.ts](../tests/e2e/specs/Knowbase/visibility_dates.spec.ts) | .ts | — |
| [tests/e2e/specs/Layout/anonymous_help_link.spec.ts](../tests/e2e/specs/Layout/anonymous_help_link.spec.ts) | .ts | — |
| [tests/e2e/specs/Layout/page_layout.spec.ts](../tests/e2e/specs/Layout/page_layout.spec.ts) | .ts | — |
| [tests/e2e/specs/Layout/skip_links.spec.ts](../tests/e2e/specs/Layout/skip_links.spec.ts) | .ts | — |
| [tests/e2e/specs/Management/budget.spec.ts](../tests/e2e/specs/Management/budget.spec.ts) | .ts | — |
| [tests/e2e/specs/Planning/availability.spec.ts](../tests/e2e/specs/Planning/availability.spec.ts) | .ts | — |
| [tests/e2e/specs/Planning/external_event.spec.ts](../tests/e2e/specs/Planning/external_event.spec.ts) | .ts | — |
| [tests/e2e/specs/Planning/planning.spec.ts](../tests/e2e/specs/Planning/planning.spec.ts) | .ts | — |
| [tests/e2e/specs/Planning/planning_view.spec.ts](../tests/e2e/specs/Planning/planning_view.spec.ts) | .ts | — |
| [tests/e2e/specs/Reservation/reservation_calendar.spec.ts](../tests/e2e/specs/Reservation/reservation_calendar.spec.ts) | .ts | — |
| [tests/e2e/specs/Search/datetime_picker.spec.ts](../tests/e2e/specs/Search/datetime_picker.spec.ts) | .ts | — |
| [tests/e2e/specs/Search/display_preferences.spec.isolated.ts](../tests/e2e/specs/Search/display_preferences.spec.isolated.ts) | .ts | — |
| [tests/e2e/specs/Search/display_preferences.spec.ts](../tests/e2e/specs/Search/display_preferences.spec.ts) | .ts | — |
| [tests/e2e/specs/Search/filterable.spec.ts](../tests/e2e/specs/Search/filterable.spec.ts) | .ts | — |
| [tests/e2e/specs/Search/search_engine.spec.ts](../tests/e2e/specs/Search/search_engine.spec.ts) | .ts | — |
| [tests/e2e/specs/Search/toolbar.spec.ts](../tests/e2e/specs/Search/toolbar.spec.ts) | .ts | — |
| [tests/e2e/specs/Security/csrf.spec.ts](../tests/e2e/specs/Security/csrf.spec.ts) | .ts | — |
| [tests/e2e/specs/Security/oauth_authcode.spec.ts](../tests/e2e/specs/Security/oauth_authcode.spec.ts) | .ts | — |
| [tests/e2e/specs/Security/reauth.spec.ts](../tests/e2e/specs/Security/reauth.spec.ts) | .ts | — |
| [tests/e2e/specs/Security/session.spec.ts](../tests/e2e/specs/Security/session.spec.ts) | .ts | — |
| [tests/e2e/specs/Security/session_manager.spec.ts](../tests/e2e/specs/Security/session_manager.spec.ts) | .ts | — |
| [tests/e2e/specs/Security/xss.spec.ts](../tests/e2e/specs/Security/xss.spec.ts) | .ts | — |
| [tests/e2e/specs/Setup/Dropdowns/calendar.spec.ts](../tests/e2e/specs/Setup/Dropdowns/calendar.spec.ts) | .ts | — |
| [tests/e2e/specs/Setup/General/assets_config.spec.isolated.ts](../tests/e2e/specs/Setup/General/assets_config.spec.isolated.ts) | .ts | — |
| [tests/e2e/specs/Setup/General/displaypreference_list.spec.ts](../tests/e2e/specs/Setup/General/displaypreference_list.spec.ts) | .ts | — |
| [tests/e2e/specs/Setup/General/maintenance.spec.isolated.ts](../tests/e2e/specs/Setup/General/maintenance.spec.isolated.ts) | .ts | — |
| [tests/e2e/specs/Setup/authldap.spec.isolated.ts](../tests/e2e/specs/Setup/authldap.spec.isolated.ts) | .ts | — |
| [tests/e2e/specs/Setup/notifications.spec.ts](../tests/e2e/specs/Setup/notifications.spec.ts) | .ts | — |
| [tests/e2e/specs/Setup/webhook.spec.ts](../tests/e2e/specs/Setup/webhook.spec.ts) | .ts | — |
| [tests/e2e/specs/Setup/webhooks.spec.ts](../tests/e2e/specs/Setup/webhooks.spec.ts) | .ts | — |
| [tests/e2e/specs/Tabler/icons.spec.ts](../tests/e2e/specs/Tabler/icons.spec.ts) | .ts | — |
| [tests/e2e/specs/Tabler/icons.spec.ts-snapshots/Tabler-icons-are-displayed-as-expected-1-chromium-linux.png](../tests/e2e/specs/Tabler/icons.spec.ts-snapshots/Tabler-icons-are-displayed-as-expected-1-chromium-linux.png) | .png | — |
| [tests/e2e/specs/Tabs/tabs.spec.ts](../tests/e2e/specs/Tabs/tabs.spec.ts) | .ts | — |
| [tests/e2e/specs/Ticket/followup_template.spec.ts](../tests/e2e/specs/Ticket/followup_template.spec.ts) | .ts | — |
| [tests/e2e/specs/Ticket/followups.spec.ts](../tests/e2e/specs/Ticket/followups.spec.ts) | .ts | — |
| [tests/e2e/specs/Ticket/save_to_kb.spec.ts](../tests/e2e/specs/Ticket/save_to_kb.spec.ts) | .ts | — |
| [tests/e2e/specs/Ticket/ticket_form.spec.ts](../tests/e2e/specs/Ticket/ticket_form.spec.ts) | .ts | — |
| [tests/e2e/specs/Ticket/ticket_promotion.spec.ts](../tests/e2e/specs/Ticket/ticket_promotion.spec.ts) | .ts | — |
| [tests/e2e/specs/Ticket/ticket_video_download.spec.ts](../tests/e2e/specs/Ticket/ticket_video_download.spec.ts) | .ts | — |
| [tests/e2e/specs/Ticket/timeline_primary_action_visibility.spec.ts](../tests/e2e/specs/Ticket/timeline_primary_action_visibility.spec.ts) | .ts | — |
| [tests/e2e/specs/Ticket/unsaved_changes_warning.spec.ts](../tests/e2e/specs/Ticket/unsaved_changes_warning.spec.ts) | .ts | — |
| [tests/e2e/specs/Tools/dcroom.spec.ts](../tests/e2e/specs/Tools/dcroom.spec.ts) | .ts | — |
| [tests/e2e/specs/Tools/reminders.spec.ts](../tests/e2e/specs/Tools/reminders.spec.ts) | .ts | — |
| [tests/e2e/specs/Tools/reservations.spec.ts](../tests/e2e/specs/Tools/reservations.spec.ts) | .ts | — |
| [tests/e2e/specs/dropdown.spec.ts](../tests/e2e/specs/dropdown.spec.ts) | .ts | — |
| [tests/e2e/utils/Accessibility.ts](../tests/e2e/utils/Accessibility.ts) | .ts | — |
| [tests/e2e/utils/Api.ts](../tests/e2e/utils/Api.ts) | .ts | — |
| [tests/e2e/utils/BubbleMenuHelper.ts](../tests/e2e/utils/BubbleMenuHelper.ts) | .ts | — |
| [tests/e2e/utils/Config.ts](../tests/e2e/utils/Config.ts) | .ts | — |
| [tests/e2e/utils/Constants.ts](../tests/e2e/utils/Constants.ts) | .ts | — |
| [tests/e2e/utils/DebugModeSwitcher.ts](../tests/e2e/utils/DebugModeSwitcher.ts) | .ts | — |
| [tests/e2e/utils/EntitySwitcher.ts](../tests/e2e/utils/EntitySwitcher.ts) | .ts | — |
| [tests/e2e/utils/FormImporter.ts](../tests/e2e/utils/FormImporter.ts) | .ts | — |
| [tests/e2e/utils/GeneralConfig.ts](../tests/e2e/utils/GeneralConfig.ts) | .ts | — |
| [tests/e2e/utils/ImagePasteHelpers.ts](../tests/e2e/utils/ImagePasteHelpers.ts) | .ts | — |
| [tests/e2e/utils/ImportedFormInfo.ts](../tests/e2e/utils/ImportedFormInfo.ts) | .ts | — |
| [tests/e2e/utils/KnowbaseApi.ts](../tests/e2e/utils/KnowbaseApi.ts) | .ts | — |
| [tests/e2e/utils/ProfileSwitcher.ts](../tests/e2e/utils/ProfileSwitcher.ts) | .ts | — |
| [tests/e2e/utils/Profiles.ts](../tests/e2e/utils/Profiles.ts) | .ts | — |
| [tests/e2e/utils/Random.ts](../tests/e2e/utils/Random.ts) | .ts | — |
| [tests/e2e/utils/ReAuthenticator.ts](../tests/e2e/utils/ReAuthenticator.ts) | .ts | — |
| [tests/e2e/utils/ReadModeCommentBubbleHelper.ts](../tests/e2e/utils/ReadModeCommentBubbleHelper.ts) | .ts | — |
| [tests/e2e/utils/SlashMenuHelper.ts](../tests/e2e/utils/SlashMenuHelper.ts) | .ts | — |
| [tests/e2e/utils/TableEditorHelper.ts](../tests/e2e/utils/TableEditorHelper.ts) | .ts | — |
| [tests/e2e/utils/TipTapEditorHelper.ts](../tests/e2e/utils/TipTapEditorHelper.ts) | .ts | — |
| [tests/e2e/utils/WorkerEntities.ts](../tests/e2e/utils/WorkerEntities.ts) | .ts | — |
| [tests/e2e/utils/WorkerSessionCache.ts](../tests/e2e/utils/WorkerSessionCache.ts) | .ts | — |
| [tests/emails-tests/00-unicode-smileys.eml](../tests/emails-tests/00-unicode-smileys.eml) | .eml | — |
| [tests/emails-tests/01-inline-images.eml](../tests/emails-tests/01-inline-images.eml) | .eml | — |
| [tests/emails-tests/02-unknown_user.eml](../tests/emails-tests/02-unknown_user.eml) | .eml | — |
| [tests/emails-tests/03-tech.eml](../tests/emails-tests/03-tech.eml) | .eml | — |
| [tests/emails-tests/04.1-ticket-followup-from-oldformat-inreplyto.eml](../tests/emails-tests/04.1-ticket-followup-from-oldformat-inreplyto.eml) | .eml | — |
| [tests/emails-tests/04.2-ticket-followup-from-oldformat-references.eml](../tests/emails-tests/04.2-ticket-followup-from-oldformat-references.eml) | .eml | — |
| [tests/emails-tests/04.3-ticket-followup-from-subject.eml](../tests/emails-tests/04.3-ticket-followup-from-subject.eml) | .eml | — |
| [tests/emails-tests/04.4-ticket-followup-from-newformat-inreplyto.eml](../tests/emails-tests/04.4-ticket-followup-from-newformat-inreplyto.eml) | .eml | — |
| [tests/emails-tests/04.5-ticket-followup-from-newformat-references.eml](../tests/emails-tests/04.5-ticket-followup-from-newformat-references.eml) | .eml | — |
| [tests/emails-tests/05-empty-from.eml](../tests/emails-tests/05-empty-from.eml) | .eml | — |
| [tests/emails-tests/06-quoted-subject.eml](../tests/emails-tests/06-quoted-subject.eml) | .eml | — |
| [tests/emails-tests/07-quoted-rejected-subject.eml](../tests/emails-tests/07-quoted-rejected-subject.eml) | .eml | — |
| [tests/emails-tests/08-tech-and-cc.eml](../tests/emails-tests/08-tech-and-cc.eml) | .eml | — |
| [tests/emails-tests/09-reply-to-tech.eml](../tests/emails-tests/09-reply-to-tech.eml) | .eml | — |
| [tests/emails-tests/10-missing-content-transfer-encoding.eml](../tests/emails-tests/10-missing-content-transfer-encoding.eml) | .eml | — |
| [tests/emails-tests/11-missing-contenttype.eml](../tests/emails-tests/11-missing-contenttype.eml) | .eml | — |
| [tests/emails-tests/12-missing-to.eml](../tests/emails-tests/12-missing-to.eml) | .eml | — |
| [tests/emails-tests/13-koi8-r-encoded-body.eml](../tests/emails-tests/13-koi8-r-encoded-body.eml) | .eml | — |
| [tests/emails-tests/14-windows-1251-encoded-body.eml](../tests/emails-tests/14-windows-1251-encoded-body.eml) | .eml | — |
| [tests/emails-tests/15-image-with-no-content-disposition.eml](../tests/emails-tests/15-image-with-no-content-disposition.eml) | .eml | — |
| [tests/emails-tests/16-no-subject.eml](../tests/emails-tests/16-no-subject.eml) | .eml | — |
| [tests/emails-tests/17-malformed-email.eml](../tests/emails-tests/17-malformed-email.eml) | .eml | — |
| [tests/emails-tests/18-image-on-multiple-lines.eml](../tests/emails-tests/18-image-on-multiple-lines.eml) | .eml | — |
| [tests/emails-tests/19-attachement-rfc5987-multiline.eml](../tests/emails-tests/19-attachement-rfc5987-multiline.eml) | .eml | — |
| [tests/emails-tests/20-attachement-rfc5987-singleline.eml](../tests/emails-tests/20-attachement-rfc5987-singleline.eml) | .eml | — |
| [tests/emails-tests/21-monopart-html.eml](../tests/emails-tests/21-monopart-html.eml) | .eml | — |
| [tests/emails-tests/22.1-ticket-notification-from-glpi-9.x.eml](../tests/emails-tests/22.1-ticket-notification-from-glpi-9.x.eml) | .eml | — |
| [tests/emails-tests/22.2-ticket-notification-from-glpi-10.0.0.eml](../tests/emails-tests/22.2-ticket-notification-from-glpi-10.0.0.eml) | .eml | — |
| [tests/emails-tests/22.3-ticket-notification-from-glpi-10.0.7.eml](../tests/emails-tests/22.3-ticket-notification-from-glpi-10.0.7.eml) | .eml | — |
| [tests/emails-tests/22.4-softwarelicence-notification-from-glpi-9.x.eml](../tests/emails-tests/22.4-softwarelicence-notification-from-glpi-9.x.eml) | .eml | — |
| [tests/emails-tests/22.5-softwarelicence-notification-from-glpi-10.0.0.eml](../tests/emails-tests/22.5-softwarelicence-notification-from-glpi-10.0.0.eml) | .eml | — |
| [tests/emails-tests/22.6-softwarelicence-notification-from-glpi-10.0.7.eml](../tests/emails-tests/22.6-softwarelicence-notification-from-glpi-10.0.7.eml) | .eml | — |
| [tests/emails-tests/22.7-itemless-notification-from-glpi-9.x.eml](../tests/emails-tests/22.7-itemless-notification-from-glpi-9.x.eml) | .eml | — |
| [tests/emails-tests/22.8-itemless-notification-from-glpi-10.0.0.eml](../tests/emails-tests/22.8-itemless-notification-from-glpi-10.0.0.eml) | .eml | — |
| [tests/emails-tests/22.9-itemless-notification-from-glpi-10.0.7.eml](../tests/emails-tests/22.9-itemless-notification-from-glpi-10.0.7.eml) | .eml | — |
| [tests/emails-tests/23-uuid-from-another-glpi.eml](../tests/emails-tests/23-uuid-from-another-glpi.eml) | .eml | — |
| [tests/emails-tests/24.1-attachement-multibyte-name-with-continuation.eml](../tests/emails-tests/24.1-attachement-multibyte-name-with-continuation.eml) | .eml | — |
| [tests/emails-tests/24.2-attachement-multibyte-name-without-continuation.eml](../tests/emails-tests/24.2-attachement-multibyte-name-without-continuation.eml) | .eml | — |
| [tests/emails-tests/25-attachement-with-OS-incompatible-char.eml](../tests/emails-tests/25-attachement-with-OS-incompatible-char.eml) | .eml | — |
| [tests/emails-tests/26-illegal-char-in-body.eml](../tests/emails-tests/26-illegal-char-in-body.eml) | .eml | — |
| [tests/emails-tests/27-autoreply.eml](../tests/emails-tests/27-autoreply.eml) | .eml | — |
| [tests/emails-tests/28-multiple-attachments-no-extension.eml](../tests/emails-tests/28-multiple-attachments-no-extension.eml) | .eml | — |
| [tests/emails-tests/29.1-ticket-followup-above-header-and-under-footer-lines.eml](../tests/emails-tests/29.1-ticket-followup-above-header-and-under-footer-lines.eml) | .eml | — |
| [tests/emails-tests/29.2-ticket-followup-above-header-line.eml](../tests/emails-tests/29.2-ticket-followup-above-header-line.eml) | .eml | — |
| [tests/emails-tests/29.3-ticket-followup-under-footer-line.eml](../tests/emails-tests/29.3-ticket-followup-under-footer-line.eml) | .eml | — |
| [tests/emails-tests/29.4-ticket-followup-above-header-line-without-footer-line.eml](../tests/emails-tests/29.4-ticket-followup-above-header-line-without-footer-line.eml) | .eml | — |
| [tests/emails-tests/29.5-ticket-followup-under-footer-line-without-header-line.eml](../tests/emails-tests/29.5-ticket-followup-under-footer-line-without-header-line.eml) | .eml | — |
| [tests/emails-tests/29.6-ticket-followup-under-header-line-without-footer-line.eml](../tests/emails-tests/29.6-ticket-followup-under-header-line-without-footer-line.eml) | .eml | — |
| [tests/emails-tests/29.7-ticket-followup-above-footer-line-without-header-line.eml](../tests/emails-tests/29.7-ticket-followup-above-footer-line-without-header-line.eml) | .eml | — |
| [tests/emails-tests/30-subject-with-special-char.eml](../tests/emails-tests/30-subject-with-special-char.eml) | .eml | — |
| [tests/emails-tests/31-html-without-body.eml](../tests/emails-tests/31-html-without-body.eml) | .eml | — |
| [tests/emails-tests/32-html-with-attributes-on-body.eml](../tests/emails-tests/32-html-with-attributes-on-body.eml) | .eml | — |
| [tests/emails-tests/33-html-with-unwanted-tags-inside-body.eml](../tests/emails-tests/33-html-with-unwanted-tags-inside-body.eml) | .eml | — |
| [tests/emails-tests/34-no-message-id-header.eml](../tests/emails-tests/34-no-message-id-header.eml) | .eml | — |
| [tests/emails-tests/35-message-with-some-invalid-headers.eml](../tests/emails-tests/35-message-with-some-invalid-headers.eml) | .eml | — |
| [tests/emails-tests/36-microsoft-specific-code.eml](../tests/emails-tests/36-microsoft-specific-code.eml) | .eml | — |
| [tests/emails-tests/37-image-with-octet-stream-type.eml](../tests/emails-tests/37-image-with-octet-stream-type.eml) | .eml | — |
| [tests/emails-tests/38-email-address-too-long.eml](../tests/emails-tests/38-email-address-too-long.eml) | .eml | — |
| [tests/emails-tests/39-link-in-content.eml](../tests/emails-tests/39-link-in-content.eml) | .eml | — |
| [tests/emails-tests/40.1-empty-content-multipart.eml](../tests/emails-tests/40.1-empty-content-multipart.eml) | .eml | — |
| [tests/emails-tests/40.2-empty-content-html.eml](../tests/emails-tests/40.2-empty-content-html.eml) | .eml | — |
| [tests/emails-tests/40.3-empty-content-plaintext.eml](../tests/emails-tests/40.3-empty-content-plaintext.eml) | .eml | — |
| [tests/emails-tests/41-image-src-with-no-quote.eml](../tests/emails-tests/41-image-src-with-no-quote.eml) | .eml | — |
| [tests/emails-tests/42-missing-content-type.eml](../tests/emails-tests/42-missing-content-type.eml) | .eml | — |
| [tests/emails-tests/43-korean-encoding-issue.eml](../tests/emails-tests/43-korean-encoding-issue.eml) | .eml | — |
| [tests/emails-tests/44-hebrew-encoding-issue.eml](../tests/emails-tests/44-hebrew-encoding-issue.eml) | .eml | — |
| [tests/emails-tests/44-multiple-to.eml](../tests/emails-tests/44-multiple-to.eml) | .eml | — |
| [tests/emails-tests/45-multiple-messageid.eml](../tests/emails-tests/45-multiple-messageid.eml) | .eml | — |
| [tests/emails-tests/46-proton-android-mail-response.eml](../tests/emails-tests/46-proton-android-mail-response.eml) | .eml | — |
| [tests/emails-tests/47-missing-charset.eml](../tests/emails-tests/47-missing-charset.eml) | .eml | — |
| [tests/emails-tests/48-refused-missing-to.eml](../tests/emails-tests/48-refused-missing-to.eml) | .eml | — |
| [tests/emails-tests/49-invalid-cc-email-address.eml](../tests/emails-tests/49-invalid-cc-email-address.eml) | .eml | — |
| [tests/emails-tests/50-all-invalid-addresses.eml](../tests/emails-tests/50-all-invalid-addresses.eml) | .eml | — |
| [tests/emails-tests/51-supplier-reply.eml](../tests/emails-tests/51-supplier-reply.eml) | .eml | — |
| [tests/emails-tests/52-long-subject.eml](../tests/emails-tests/52-long-subject.eml) | .eml | — |
| [tests/emails-tests/53-large-html-body.eml](../tests/emails-tests/53-large-html-body.eml) | .eml | — |
| [tests/emails-tests/54-invalid-charset.eml](../tests/emails-tests/54-invalid-charset.eml) | .eml | — |
| [tests/emails-tests/55-invalid-utf8-body.eml](../tests/emails-tests/55-invalid-utf8-body.eml) | .eml | — |
| [tests/fixtures/another_test.php](../tests/fixtures/another_test.php) | .php | class Glpi\Another_Test extends \CommonDBTM |
| [tests/fixtures/export-of-2-forms.json](../tests/fixtures/export-of-2-forms.json) | .json | — |
| [tests/fixtures/forms/active-form.json](../tests/fixtures/forms/active-form.json) | .json | — |
| [tests/fixtures/forms/cascading-comment-visibility.json](../tests/fixtures/forms/cascading-comment-visibility.json) | .json | — |
| [tests/fixtures/forms/cascading-question-visibility.json](../tests/fixtures/forms/cascading-question-visibility.json) | .json | — |
| [tests/fixtures/forms/cascading-section-visibility.json](../tests/fixtures/forms/cascading-section-visibility.json) | .json | — |
| [tests/fixtures/forms/comment-conditions-applied.json](../tests/fixtures/forms/comment-conditions-applied.json) | .json | — |
| [tests/fixtures/forms/comment-hidden-if-default-checked-checkbox.json](../tests/fixtures/forms/comment-hidden-if-default-checked-checkbox.json) | .json | — |
| [tests/fixtures/forms/comment-used-in-conditions.json](../tests/fixtures/forms/comment-used-in-conditions.json) | .json | — |
| [tests/fixtures/forms/comment-with-item-condition.json](../tests/fixtures/forms/comment-with-item-condition.json) | .json | — |
| [tests/fixtures/forms/condition-priority-over-non-empty-section.json](../tests/fixtures/forms/condition-priority-over-non-empty-section.json) | .json | — |
| [tests/fixtures/forms/condition-subject-dropdown.json](../tests/fixtures/forms/condition-subject-dropdown.json) | .json | — |
| [tests/fixtures/forms/condition-subject-radio.json](../tests/fixtures/forms/condition-subject-radio.json) | .json | — |
| [tests/fixtures/forms/destination-with-item-condition.json](../tests/fixtures/forms/destination-with-item-condition.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/assignee-config.json](../tests/fixtures/forms/destination_config_fields/assignee-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/associated-items-config.json](../tests/fixtures/forms/destination_config_fields/associated-items-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/content-title-config.json](../tests/fixtures/forms/destination_config_fields/content-title-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/entity-config.json](../tests/fixtures/forms/destination_config_fields/entity-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/itilcategory-config.json](../tests/fixtures/forms/destination_config_fields/itilcategory-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/linked-itilobjects-config.json](../tests/fixtures/forms/destination_config_fields/linked-itilobjects-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/location-config.json](../tests/fixtures/forms/destination_config_fields/location-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/observer-config.json](../tests/fixtures/forms/destination_config_fields/observer-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/request-type-config.json](../tests/fixtures/forms/destination_config_fields/request-type-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/requester-config.json](../tests/fixtures/forms/destination_config_fields/requester-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/simple-form-config.json](../tests/fixtures/forms/destination_config_fields/simple-form-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/urgency-config.json](../tests/fixtures/forms/destination_config_fields/urgency-config.json) | .json | — |
| [tests/fixtures/forms/destination_config_fields/validation-config.json](../tests/fixtures/forms/destination_config_fields/validation-config.json) | .json | — |
| [tests/fixtures/forms/external-deps-block-section-deletion.json](../tests/fixtures/forms/external-deps-block-section-deletion.json) | .json | — |
| [tests/fixtures/forms/file-upload-conditions.json](../tests/fixtures/forms/file-upload-conditions.json) | .json | — |
| [tests/fixtures/forms/form-tags.json](../tests/fixtures/forms/form-tags.json) | .json | — |
| [tests/fixtures/forms/form-translations-base.json](../tests/fixtures/forms/form-translations-base.json) | .json | — |
| [tests/fixtures/forms/form-with-empty-specific-question-for-location.json](../tests/fixtures/forms/form-with-empty-specific-question-for-location.json) | .json | — |
| [tests/fixtures/forms/form-with-empty-specific-sla.json](../tests/fixtures/forms/form-with-empty-specific-sla.json) | .json | — |
| [tests/fixtures/forms/form-with-empty-specific-template.json](../tests/fixtures/forms/form-with-empty-specific-template.json) | .json | — |
| [tests/fixtures/forms/form-with-hammer-asset.json](../tests/fixtures/forms/form-with-hammer-asset.json) | .json | — |
| [tests/fixtures/forms/form-with-hidden-items.json](../tests/fixtures/forms/form-with-hidden-items.json) | .json | — |
| [tests/fixtures/forms/form-with-question-destination-submit-button-conditions.json](../tests/fixtures/forms/form-with-question-destination-submit-button-conditions.json) | .json | — |
| [tests/fixtures/forms/form-with-text-question.json](../tests/fixtures/forms/form-with-text-question.json) | .json | — |
| [tests/fixtures/forms/form-with-validation-2025-10-08.json](../tests/fixtures/forms/form-with-validation-2025-10-08.json) | .json | — |
| [tests/fixtures/forms/form_with_condition_on_richtext.json](../tests/fixtures/forms/form_with_condition_on_richtext.json) | .json | — |
| [tests/fixtures/forms/items-used-in-destination-conditions.json](../tests/fixtures/forms/items-used-in-destination-conditions.json) | .json | — |
| [tests/fixtures/forms/items-used-in-submit-button-conditions.json](../tests/fixtures/forms/items-used-in-submit-button-conditions.json) | .json | — |
| [tests/fixtures/forms/long-text-two-sections.json](../tests/fixtures/forms/long-text-two-sections.json) | .json | — |
| [tests/fixtures/forms/mandatory-file.json](../tests/fixtures/forms/mandatory-file.json) | .json | — |
| [tests/fixtures/forms/mandatory-questions-two-sections.json](../tests/fixtures/forms/mandatory-questions-two-sections.json) | .json | — |
| [tests/fixtures/forms/preset-form-fields.json](../tests/fixtures/forms/preset-form-fields.json) | .json | — |
| [tests/fixtures/forms/public-form-with-altcha.json](../tests/fixtures/forms/public-form-with-altcha.json) | .json | — |
| [tests/fixtures/forms/question-array-conditions-applied.json](../tests/fixtures/forms/question-array-conditions-applied.json) | .json | — |
| [tests/fixtures/forms/question-conditions-applied.json](../tests/fixtures/forms/question-conditions-applied.json) | .json | — |
| [tests/fixtures/forms/question-type-change-blocked-destination.json](../tests/fixtures/forms/question-type-change-blocked-destination.json) | .json | — |
| [tests/fixtures/forms/question-type-change-blocked-submit-button.json](../tests/fixtures/forms/question-type-change-blocked-submit-button.json) | .json | — |
| [tests/fixtures/forms/question-type-change-blocked.json](../tests/fixtures/forms/question-type-change-blocked.json) | .json | — |
| [tests/fixtures/forms/question-used-in-conditions.json](../tests/fixtures/forms/question-used-in-conditions.json) | .json | — |
| [tests/fixtures/forms/question-with-item-condition.json](../tests/fixtures/forms/question-with-item-condition.json) | .json | — |
| [tests/fixtures/forms/question_types/assignee-question.json](../tests/fixtures/forms/question_types/assignee-question.json) | .json | — |
| [tests/fixtures/forms/question_types/checkbox-question.json](../tests/fixtures/forms/question_types/checkbox-question.json) | .json | — |
| [tests/fixtures/forms/question_types/date-question.json](../tests/fixtures/forms/question_types/date-question.json) | .json | — |
| [tests/fixtures/forms/question_types/datetime-question.json](../tests/fixtures/forms/question_types/datetime-question.json) | .json | — |
| [tests/fixtures/forms/question_types/dropdown-editor-test.json](../tests/fixtures/forms/question_types/dropdown-editor-test.json) | .json | — |
| [tests/fixtures/forms/question_types/dropdown-multiple-question.json](../tests/fixtures/forms/question_types/dropdown-multiple-question.json) | .json | — |
| [tests/fixtures/forms/question_types/dropdown-question.json](../tests/fixtures/forms/question_types/dropdown-question.json) | .json | — |
| [tests/fixtures/forms/question_types/email-question.json](../tests/fixtures/forms/question_types/email-question.json) | .json | — |
| [tests/fixtures/forms/question_types/file-question.json](../tests/fixtures/forms/question_types/file-question.json) | .json | — |
| [tests/fixtures/forms/question_types/item-dropdown-question.json](../tests/fixtures/forms/question_types/item-dropdown-question.json) | .json | — |
| [tests/fixtures/forms/question_types/item-editor-test.json](../tests/fixtures/forms/question_types/item-editor-test.json) | .json | — |
| [tests/fixtures/forms/question_types/item-question.json](../tests/fixtures/forms/question_types/item-question.json) | .json | — |
| [tests/fixtures/forms/question_types/long-text-question.json](../tests/fixtures/forms/question_types/long-text-question.json) | .json | — |
| [tests/fixtures/forms/question_types/number-question.json](../tests/fixtures/forms/question_types/number-question.json) | .json | — |
| [tests/fixtures/forms/question_types/observer-question.json](../tests/fixtures/forms/question_types/observer-question.json) | .json | — |
| [tests/fixtures/forms/question_types/radio-question.json](../tests/fixtures/forms/question_types/radio-question.json) | .json | — |
| [tests/fixtures/forms/question_types/request-type-question.json](../tests/fixtures/forms/question_types/request-type-question.json) | .json | — |
| [tests/fixtures/forms/question_types/requester-question.json](../tests/fixtures/forms/question_types/requester-question.json) | .json | — |
| [tests/fixtures/forms/question_types/short-text-question.json](../tests/fixtures/forms/question_types/short-text-question.json) | .json | — |
| [tests/fixtures/forms/question_types/time-question.json](../tests/fixtures/forms/question_types/time-question.json) | .json | — |
| [tests/fixtures/forms/question_types/urgency-question.json](../tests/fixtures/forms/question_types/urgency-question.json) | .json | — |
| [tests/fixtures/forms/question_types/user-device-multiple-question.json](../tests/fixtures/forms/question_types/user-device-multiple-question.json) | .json | — |
| [tests/fixtures/forms/question_types/user-device-question.json](../tests/fixtures/forms/question_types/user-device-question.json) | .json | — |
| [tests/fixtures/forms/rendering_layouts/single-page-mixed-fields.json](../tests/fixtures/forms/rendering_layouts/single-page-mixed-fields.json) | .json | — |
| [tests/fixtures/forms/rendering_layouts/single-page-one-question.json](../tests/fixtures/forms/rendering_layouts/single-page-one-question.json) | .json | — |
| [tests/fixtures/forms/rendering_layouts/single-page-single-section.json](../tests/fixtures/forms/rendering_layouts/single-page-single-section.json) | .json | — |
| [tests/fixtures/forms/rendering_layouts/single-page-three-sections-mandatory.json](../tests/fixtures/forms/rendering_layouts/single-page-three-sections-mandatory.json) | .json | — |
| [tests/fixtures/forms/rendering_layouts/step-by-step-one-question.json](../tests/fixtures/forms/rendering_layouts/step-by-step-one-question.json) | .json | — |
| [tests/fixtures/forms/rendering_layouts/step-by-step-single-section.json](../tests/fixtures/forms/rendering_layouts/step-by-step-single-section.json) | .json | — |
| [tests/fixtures/forms/rendering_layouts/step-by-step-three-sections-mandatory.json](../tests/fixtures/forms/rendering_layouts/step-by-step-three-sections-mandatory.json) | .json | — |
| [tests/fixtures/forms/rendering_layouts/step-by-step-two-sections.json](../tests/fixtures/forms/rendering_layouts/step-by-step-two-sections.json) | .json | — |
| [tests/fixtures/forms/section-conditions-applied.json](../tests/fixtures/forms/section-conditions-applied.json) | .json | — |
| [tests/fixtures/forms/section-used-in-conditions.json](../tests/fixtures/forms/section-used-in-conditions.json) | .json | — |
| [tests/fixtures/forms/section-with-item-condition.json](../tests/fixtures/forms/section-with-item-condition.json) | .json | — |
| [tests/fixtures/forms/sections-with-conditions.json](../tests/fixtures/forms/sections-with-conditions.json) | .json | — |
| [tests/fixtures/forms/submit-button-visible-if-equals.json](../tests/fixtures/forms/submit-button-visible-if-equals.json) | .json | — |
| [tests/fixtures/forms/submit-with-item-condition.json](../tests/fixtures/forms/submit-with-item-condition.json) | .json | — |
| [tests/fixtures/forms/three-short-text-questions.json](../tests/fixtures/forms/three-short-text-questions.json) | .json | — |
| [tests/fixtures/forms/two-questions-one-comment.json](../tests/fixtures/forms/two-questions-one-comment.json) | .json | — |
| [tests/fixtures/forms/two-sections-three-questions.json](../tests/fixtures/forms/two-sections-three-questions.json) | .json | — |
| [tests/fixtures/forms/with-advancedforms-plugin-requirement.json](../tests/fixtures/forms/with-advancedforms-plugin-requirement.json) | .json | — |
| [tests/fixtures/forms/with-condition-on-sections.json](../tests/fixtures/forms/with-condition-on-sections.json) | .json | — |
| [tests/fixtures/forms/with-tester-plugin-requirement.json](../tests/fixtures/forms/with-tester-plugin-requirement.json) | .json | — |
| [tests/fixtures/genericobject-migration/genericobject-db.sql](../tests/fixtures/genericobject-migration/genericobject-db.sql) | .sql | — |
| [tests/fixtures/genericobject-migration/glpi-data.sql](../tests/fixtures/genericobject-migration/glpi-data.sql) | .sql | — |
| [tests/fixtures/hlapi/snapshots/2.3.0/components.json](../tests/fixtures/hlapi/snapshots/2.3.0/components.json) | .json | — |
| [tests/fixtures/hlapi/snapshots/2.3.0/paths.json](../tests/fixtures/hlapi/snapshots/2.3.0/paths.json) | .json | — |
| [tests/fixtures/hlapi/snapshots/3.0.0/components.json](../tests/fixtures/hlapi/snapshots/3.0.0/components.json) | .json | — |
| [tests/fixtures/hlapi/snapshots/3.0.0/paths.json](../tests/fixtures/hlapi/snapshots/3.0.0/paths.json) | .json | — |
| [tests/fixtures/ical/sample_1.ics](../tests/fixtures/ical/sample_1.ics) | .ics | — |
| [tests/fixtures/ical/sample_2.ics](../tests/fixtures/ical/sample_2.ics) | .ics | — |
| [tests/fixtures/images/blank.JPEG](../tests/fixtures/images/blank.JPEG) | .JPEG | — |
| [tests/fixtures/images/blank.bmp](../tests/fixtures/images/blank.bmp) | .bmp | — |
| [tests/fixtures/images/blank.jpg](../tests/fixtures/images/blank.jpg) | .jpg | — |
| [tests/fixtures/images/blank.webp](../tests/fixtures/images/blank.webp) | .webp | — |
| [tests/fixtures/images/empty.gif](../tests/fixtures/images/empty.gif) | .gif | — |
| [tests/fixtures/images/empty.png](../tests/fixtures/images/empty.png) | .png | — |
| [tests/fixtures/images/fake_gif.php](../tests/fixtures/images/fake_gif.php) | .php | — |
| [tests/fixtures/images/notanimage.jpg](../tests/fixtures/images/notanimage.jpg) | .jpg | — |
| [tests/fixtures/images/readme.txt](../tests/fixtures/images/readme.txt) | .txt | — |
| [tests/fixtures/inventories/cisco-C9300.xml](../tests/fixtures/inventories/cisco-C9300.xml) | .xml | — |
| [tests/fixtures/inventories/computer_locked_states_id.json](../tests/fixtures/inventories/computer_locked_states_id.json) | .json | — |
| [tests/fixtures/inventories/computer_networkportwifi.json](../tests/fixtures/inventories/computer_networkportwifi.json) | .json | — |
| [tests/fixtures/inventories/connected_switch.xml](../tests/fixtures/inventories/connected_switch.xml) | .xml | — |
| [tests/fixtures/inventories/dell_n3048p.xml](../tests/fixtures/inventories/dell_n3048p.xml) | .xml | — |
| [tests/fixtures/inventories/extreme_3650GTS.xml](../tests/fixtures/inventories/extreme_3650GTS.xml) | .xml | — |
| [tests/fixtures/inventories/extreme_5420F.xml](../tests/fixtures/inventories/extreme_5420F.xml) | .xml | — |
| [tests/fixtures/inventories/juniper.xml](../tests/fixtures/inventories/juniper.xml) | .xml | — |
| [tests/fixtures/inventories/lxc-server-1.json](../tests/fixtures/inventories/lxc-server-1.json) | .json | — |
| [tests/fixtures/inventories/software/01-test_software_with_special_chars_with_version.json](../tests/fixtures/inventories/software/01-test_software_with_special_chars_with_version.json) | .json | — |
| [tests/fixtures/inventories/software/01_computer_full_inventory_soft_and_os.json](../tests/fixtures/inventories/software/01_computer_full_inventory_soft_and_os.json) | .json | — |
| [tests/fixtures/inventories/software/02-test_software_with_special_chars_with_version.json](../tests/fixtures/inventories/software/02-test_software_with_special_chars_with_version.json) | .json | — |
| [tests/fixtures/inventories/software/02_computer_full_inventory_soft_and_os.json](../tests/fixtures/inventories/software/02_computer_full_inventory_soft_and_os.json) | .json | — |
| [tests/fixtures/inventories/software/03-test_software_with_special_chars_and_without_version.json](../tests/fixtures/inventories/software/03-test_software_with_special_chars_and_without_version.json) | .json | — |
| [tests/fixtures/inventories/software/03_computer_partial_inventory_with_os.json](../tests/fixtures/inventories/software/03_computer_partial_inventory_with_os.json) | .json | — |
| [tests/fixtures/inventories/software/04-test_software_with_special_chars_and_with_version_and_os.json](../tests/fixtures/inventories/software/04-test_software_with_special_chars_and_with_version_and_os.json) | .json | — |
| [tests/fixtures/inventories/software/04_computer_full_inventory_with_os_without_soft.json](../tests/fixtures/inventories/software/04_computer_full_inventory_with_os_without_soft.json) | .json | — |
| [tests/fixtures/inventories/software/05-test_software_with_special_chars_and_without_version_and_os.json](../tests/fixtures/inventories/software/05-test_software_with_special_chars_and_without_version_and_os.json) | .json | — |
| [tests/fixtures/inventories/software/05_computer_full_inventory_without_os_with_soft.json](../tests/fixtures/inventories/software/05_computer_full_inventory_without_os_with_soft.json) | .json | — |
| [tests/fixtures/inventories/stacked_switch_name.xml](../tests/fixtures/inventories/stacked_switch_name.xml) | .xml | — |
| [tests/fixtures/locales/en_GB.php](../tests/fixtures/locales/en_GB.php) | .php | — |
| [tests/fixtures/locales/fr_FR.php](../tests/fixtures/locales/fr_FR.php) | .php | — |
| [tests/fixtures/marketplace/myplugin/setup.php](../tests/fixtures/marketplace/myplugin/setup.php) | .php | — |
| [tests/fixtures/mocked_glpi_dir_for_illustrations/confidential_info.txt](../tests/fixtures/mocked_glpi_dir_for_illustrations/confidential_info.txt) | .txt | — |
| [tests/fixtures/mocked_glpi_dir_for_illustrations/my_svg.svg](../tests/fixtures/mocked_glpi_dir_for_illustrations/my_svg.svg) | .svg | — |
| [tests/fixtures/mocked_glpi_dir_for_illustrations/resources/illustration/valid_svg.svg](../tests/fixtures/mocked_glpi_dir_for_illustrations/resources/illustration/valid_svg.svg) | .svg | — |
| [tests/fixtures/pluginbarabstractstuff.php](../tests/fixtures/pluginbarabstractstuff.php) | .php | class GlpiPlugin\Bar\AbstractStuff extends \CommonDBTM |
| [tests/fixtures/pluginbarfoo.php](../tests/fixtures/pluginbarfoo.php) | .php | class GlpiPlugin\Bar\Foo extends \CommonDBTM |
| [tests/fixtures/pluginfoo_item_filter.php](../tests/fixtures/pluginfoo_item_filter.php) | .php | class GlpiPlugin\Foo\Item_Filter extends \CommonDBTM |
| [tests/fixtures/pluginfoo_search_a_b_c_d_e_f_g_bar.php](../tests/fixtures/pluginfoo_search_a_b_c_d_e_f_g_bar.php) | .php | class GlpiPlugin\Foo\A\B\C\D\E\F\G\Bar extends \CommonDBTM |
| [tests/fixtures/pluginfoo_search_item_filter.php](../tests/fixtures/pluginfoo_search_item_filter.php) | .php | class GlpiPlugin\Foo\Search\Item_Filter extends \CommonDBTM |
| [tests/fixtures/pluginfoobar.php](../tests/fixtures/pluginfoobar.php) | .php | class PluginFooBar extends CommonDBTM |
| [tests/fixtures/pluginfooservice.php](../tests/fixtures/pluginfooservice.php) | .php | class PluginFooService |
| [tests/fixtures/plugins/tester/inc/fakeprotocol.class.php](../tests/fixtures/plugins/tester/inc/fakeprotocol.class.php) | .php | class PluginTesterFakeProtocol |
| [tests/fixtures/plugins/tester/inc/fakestorage.class.php](../tests/fixtures/plugins/tester/inc/fakestorage.class.php) | .php | class PluginTesterFakeStorage extends Laminas\Mail\Storage\Imap |
| [tests/fixtures/plugins/tester/inc/mylegacyclass.class.php](../tests/fixtures/plugins/tester/inc/mylegacyclass.class.php) | .php | class PluginTesterMyLegacyClass extends CommonDBTM |
| [tests/fixtures/plugins/tester/inc/mylegacydropdown.class.php](../tests/fixtures/plugins/tester/inc/mylegacydropdown.class.php) | .php | class PluginTesterMyLegacyDropdown extends CommonDropdown |
| [tests/fixtures/plugins/tester/locales/en_GB.mo](../tests/fixtures/plugins/tester/locales/en_GB.mo) | .mo | — |
| [tests/fixtures/plugins/tester/locales/en_GB.po](../tests/fixtures/plugins/tester/locales/en_GB.po) | .po | — |
| [tests/fixtures/plugins/tester/locales/fr_FR.mo](../tests/fixtures/plugins/tester/locales/fr_FR.mo) | .mo | — |
| [tests/fixtures/plugins/tester/locales/fr_FR.po](../tests/fixtures/plugins/tester/locales/fr_FR.po) | .po | — |
| [tests/fixtures/plugins/tester/public/css/_mixins.scss](../tests/fixtures/plugins/tester/public/css/_mixins.scss) | .scss | — |
| [tests/fixtures/plugins/tester/public/css/static_1.css](../tests/fixtures/plugins/tester/public/css/static_1.css) | .css | — |
| [tests/fixtures/plugins/tester/public/css/static_1.min.css](../tests/fixtures/plugins/tester/public/css/static_1.min.css) | .css | — |
| [tests/fixtures/plugins/tester/public/css/static_2.css](../tests/fixtures/plugins/tester/public/css/static_2.css) | .css | — |
| [tests/fixtures/plugins/tester/public/css/styles.scss](../tests/fixtures/plugins/tester/public/css/styles.scss) | .scss | — |
| [tests/fixtures/plugins/tester/public/js/plugin_scripts_1.js](../tests/fixtures/plugins/tester/public/js/plugin_scripts_1.js) | .js | — |
| [tests/fixtures/plugins/tester/public/js/plugin_scripts_1.min.js](../tests/fixtures/plugins/tester/public/js/plugin_scripts_1.min.js) | .js | — |
| [tests/fixtures/plugins/tester/public/js/plugin_scripts_2.js](../tests/fixtures/plugins/tester/public/js/plugin_scripts_2.js) | .js | — |
| [tests/fixtures/plugins/tester/setup.php](../tests/fixtures/plugins/tester/setup.php) | .php | — |
| [tests/fixtures/plugins/tester/src/Asset/Capacity/HasFooCapacity.php](../tests/fixtures/plugins/tester/src/Asset/Capacity/HasFooCapacity.php) | .php | class GlpiPlugin\Tester\Asset\Capacity\HasFooCapacity extends AbstractCapacity |
| [tests/fixtures/plugins/tester/src/Asset/Foo.php](../tests/fixtures/plugins/tester/src/Asset/Foo.php) | .php | class GlpiPlugin\Tester\Asset\Foo extends CommonDBChild |
| [tests/fixtures/plugins/tester/src/Computer.php](../tests/fixtures/plugins/tester/src/Computer.php) | .php | class GlpiPlugin\Tester\Computer extends CommonDBTM |
| [tests/fixtures/plugins/tester/src/Controller/TesterController.php](../tests/fixtures/plugins/tester/src/Controller/TesterController.php) | .php | class GlpiPlugin\Tester\Controller\TesterController extends AbstractController |
| [tests/fixtures/plugins/tester/src/Form/ComputerDestination.php](../tests/fixtures/plugins/tester/src/Form/ComputerDestination.php) | .php | class GlpiPlugin\Tester\Form\ComputerDestination |
| [tests/fixtures/plugins/tester/src/Form/ComputerForServiceCatalog.php](../tests/fixtures/plugins/tester/src/Form/ComputerForServiceCatalog.php) | .php | class GlpiPlugin\Tester\Form\ComputerForServiceCatalog |
| [tests/fixtures/plugins/tester/src/Form/ComputerProvider.php](../tests/fixtures/plugins/tester/src/Form/ComputerProvider.php) | .php | class GlpiPlugin\Tester\Form\ComputerProvider |
| [tests/fixtures/plugins/tester/src/Form/CustomTile.php](../tests/fixtures/plugins/tester/src/Form/CustomTile.php) | .php | class GlpiPlugin\Tester\Form\CustomTile extends CommonDBTM |
| [tests/fixtures/plugins/tester/src/Form/DayOfTheWeekPolicy.php](../tests/fixtures/plugins/tester/src/Form/DayOfTheWeekPolicy.php) | .php | class GlpiPlugin\Tester\Form\DayOfTheWeekPolicy |
| [tests/fixtures/plugins/tester/src/Form/DayOfTheWeekPolicyConfig.php](../tests/fixtures/plugins/tester/src/Form/DayOfTheWeekPolicyConfig.php) | .php | class GlpiPlugin\Tester\Form\DayOfTheWeekPolicyConfig |
| [tests/fixtures/plugins/tester/src/Form/ExternalIDField.php](../tests/fixtures/plugins/tester/src/Form/ExternalIDField.php) | .php | class GlpiPlugin\Tester\Form\ExternalIDField extends AbstractConfigField |
| [tests/fixtures/plugins/tester/src/Form/ExternalIDFieldConfig.php](../tests/fixtures/plugins/tester/src/Form/ExternalIDFieldConfig.php) | .php | class GlpiPlugin\Tester\Form\ExternalIDFieldConfig |
| [tests/fixtures/plugins/tester/src/Form/ExternalIDFieldStrategy.php](../tests/fixtures/plugins/tester/src/Form/ExternalIDFieldStrategy.php) | .php | enum GlpiPlugin\Tester\Form\ExternalIDFieldStrategy |
| [tests/fixtures/plugins/tester/src/Form/QuestionTypeColor.php](../tests/fixtures/plugins/tester/src/Form/QuestionTypeColor.php) | .php | class GlpiPlugin\Tester\Form\QuestionTypeColor extends AbstractQuestionType |
| [tests/fixtures/plugins/tester/src/Form/QuestionTypeIpConverter.php](../tests/fixtures/plugins/tester/src/Form/QuestionTypeIpConverter.php) | .php | class GlpiPlugin\Tester\Form\QuestionTypeIpConverter |
| [tests/fixtures/plugins/tester/src/Form/QuestionTypeRange.php](../tests/fixtures/plugins/tester/src/Form/QuestionTypeRange.php) | .php | class GlpiPlugin\Tester\Form\QuestionTypeRange extends AbstractQuestionType |
| [tests/fixtures/plugins/tester/src/Form/TesterCategory.php](../tests/fixtures/plugins/tester/src/Form/TesterCategory.php) | .php | class GlpiPlugin\Tester\Form\TesterCategory |
| [tests/fixtures/plugins/tester/src/MyPsr4Class.php](../tests/fixtures/plugins/tester/src/MyPsr4Class.php) | .php | class GlpiPlugin\Tester\MyPsr4Class extends CommonDBTM |
| [tests/fixtures/plugins/tester/src/MyPsr4Dropdown.php](../tests/fixtures/plugins/tester/src/MyPsr4Dropdown.php) | .php | class GlpiPlugin\Tester\MyPsr4Dropdown extends CommonDropdown |
| [tests/fixtures/plugins/tester/src/PluginTesterMyPseudoPsr4Class.php](../tests/fixtures/plugins/tester/src/PluginTesterMyPseudoPsr4Class.php) | .php | class PluginTesterMyPseudoPsr4Class extends CommonDBTM |
| [tests/fixtures/plugins/tester/src/PluginTesterMyPseudoPsr4Dropdown.php](../tests/fixtures/plugins/tester/src/PluginTesterMyPseudoPsr4Dropdown.php) | .php | class PluginTesterMyPseudoPsr4Dropdown extends CommonDropdown |
| [tests/fixtures/plugins/tester/src/PluginTesterNotificationEventTestmode.php](../tests/fixtures/plugins/tester/src/PluginTesterNotificationEventTestmode.php) | .php | class PluginTesterNotificationEventTestmode |
| [tests/fixtures/plugins/tester/src/PluginTesterNotificationTestmode.php](../tests/fixtures/plugins/tester/src/PluginTesterNotificationTestmode.php) | .php | class PluginTesterNotificationTestmode |
| [tests/fixtures/plugins/tester/src/PluginTesterNotificationTestmodeSetting.php](../tests/fixtures/plugins/tester/src/PluginTesterNotificationTestmodeSetting.php) | .php | class PluginTesterNotificationTestmodeSetting extends NotificationSetting |
| [tests/fixtures/plugins/tester/templates/computer_destination.html.twig](../tests/fixtures/plugins/tester/templates/computer_destination.html.twig) | .twig | — |
| [tests/fixtures/plugins/tester/templates/custom_tile.html.twig](../tests/fixtures/plugins/tester/templates/custom_tile.html.twig) | .twig | — |
| [tests/fixtures/plugins/tester/templates/day_of_the_week_policy.html.twig](../tests/fixtures/plugins/tester/templates/day_of_the_week_policy.html.twig) | .twig | — |
| [tests/fixtures/plugins/tester/templates/external_id_config_field.html.twig](../tests/fixtures/plugins/tester/templates/external_id_config_field.html.twig) | .twig | — |
| [tests/fixtures/test_a_b.php](../tests/fixtures/test_a_b.php) | .php | class Glpi\Test\A_B extends \CommonDBTM |
| [tests/fixtures/test_icon.png](../tests/fixtures/test_icon.png) | .png | — |
| [tests/fixtures/uploads/bar.png](../tests/fixtures/uploads/bar.png) | .png | — |
| [tests/fixtures/uploads/bar.txt](../tests/fixtures/uploads/bar.txt) | .txt | — |
| [tests/fixtures/uploads/foo.png](../tests/fixtures/uploads/foo.png) | .png | — |
| [tests/fixtures/uploads/foo.txt](../tests/fixtures/uploads/foo.txt) | .txt | — |
| [tests/fixtures/uploads/test.mov](../tests/fixtures/uploads/test.mov) | .mov | — |
| [tests/functional/ActorEmailValidationTest.php](../tests/functional/ActorEmailValidationTest.php) | .php | class tests\units\ActorEmailValidationTest extends DbTestCase |
| [tests/functional/AgentTest.php](../tests/functional/AgentTest.php) | .php | class tests\units\AgentTest extends DbTestCase |
| [tests/functional/AlertTest.php](../tests/functional/AlertTest.php) | .php | class tests\units\AlertTest extends DbTestCase |
| [tests/functional/ApplianceTest.php](../tests/functional/ApplianceTest.php) | .php | class tests\units\ApplianceTest extends DbTestCase |
| [tests/functional/Appliance_ItemTest.php](../tests/functional/Appliance_ItemTest.php) | .php | class tests\units\Appliance_ItemTest extends DbTestCase |
| [tests/functional/Appliance_Item_RelationTest.php](../tests/functional/Appliance_Item_RelationTest.php) | .php | class tests\units\Appliance_Item_RelationTest extends DbTestCase |
| [tests/functional/AuthLdapReplicateTest.php](../tests/functional/AuthLdapReplicateTest.php) | .php | class tests\units\AuthLdapReplicateTest extends DbTestCase |
| [tests/functional/AuthLdapTest.php](../tests/functional/AuthLdapTest.php) | .php | class tests\units\AuthLdapTest extends DbTestCase |
| [tests/functional/AuthLdapUserRestoreTest.php](../tests/functional/AuthLdapUserRestoreTest.php) | .php | class tests\units\AuthLdapUserRestoreTest extends DbTestCase |
| [tests/functional/AuthMailTest.php](../tests/functional/AuthMailTest.php) | .php | class tests\units\AuthMailTest extends DbTestCase |
| [tests/functional/AuthTest.php](../tests/functional/AuthTest.php) | .php | class tests\units\AuthTest extends DbTestCase |
| [tests/functional/AutoloadTest.php](../tests/functional/AutoloadTest.php) | .php | class tests\units\AutoloadTest extends DbTestCase |
| [tests/functional/BarcodeManagerTest.php](../tests/functional/BarcodeManagerTest.php) | .php | class tests\units\BarcodeManagerTest extends DbTestCase |
| [tests/functional/BlacklistTest.php](../tests/functional/BlacklistTest.php) | .php | class tests\units\BlacklistTest extends DbTestCase |
| [tests/functional/BudgetTest.php](../tests/functional/BudgetTest.php) | .php | class tests\units\BudgetTest extends DbTestCase |
| [tests/functional/CableTest.php](../tests/functional/CableTest.php) | .php | class tests\units\CableTest extends DbTestCase |
| [tests/functional/CalendarSegmentTest.php](../tests/functional/CalendarSegmentTest.php) | .php | class tests\units\CalendarSegmentTest extends DbTestCase |
| [tests/functional/CalendarTest.php](../tests/functional/CalendarTest.php) | .php | class tests\units\CalendarTest extends DbTestCase |
| [tests/functional/Calendar_HolidayTest.php](../tests/functional/Calendar_HolidayTest.php) | .php | class tests\units\Calendar_HolidayTest extends DbTestCase |
| [tests/functional/CartridgeTest.php](../tests/functional/CartridgeTest.php) | .php | class tests\units\CartridgeTest extends DbTestCase |
| [tests/functional/CentralTest.php](../tests/functional/CentralTest.php) | .php | class tests\units\CentralTest extends DbTestCase |
| [tests/functional/CertificateTest.php](../tests/functional/CertificateTest.php) | .php | class tests\units\CertificateTest extends DbTestCase |
| [tests/functional/Certificate_ItemTest.php](../tests/functional/Certificate_ItemTest.php) | .php | class tests\units\Certificate_ItemTest extends DbTestCase |
| [tests/functional/ChangeITILTemplateReadonlyFieldTest.php](../tests/functional/ChangeITILTemplateReadonlyFieldTest.php) | .php | class functional\ChangeITILTemplateReadonlyFieldTest extends AbstractITILTemplateReadonlyFieldTest |
| [tests/functional/ChangeSatisfactionTest.php](../tests/functional/ChangeSatisfactionTest.php) | .php | class tests\units\ChangeSatisfactionTest extends CommonITILSatisfactionTest |
| [tests/functional/ChangeTaskTest.php](../tests/functional/ChangeTaskTest.php) | .php | class tests\units\ChangeTaskTest extends CommonITILTaskTestCase |
| [tests/functional/ChangeTemplatePredefinedFieldTest.php](../tests/functional/ChangeTemplatePredefinedFieldTest.php) | .php | class tests\units\ChangeTemplatePredefinedFieldTest extends AbstractITILTemplatePredefinedFieldTest |
| [tests/functional/ChangeTest.php](../tests/functional/ChangeTest.php) | .php | class tests\units\ChangeTest extends DbTestCase |
| [tests/functional/ChangeValidationTest.php](../tests/functional/ChangeValidationTest.php) | .php | class tests\units\ChangeValidationTest extends CommonITILValidationTest |
| [tests/functional/Change_ItemTest.php](../tests/functional/Change_ItemTest.php) | .php | class tests\units\Change_ItemTest extends AbstractCommonItilObject_ItemTest |
| [tests/functional/CleanSoftwareCronTest.php](../tests/functional/CleanSoftwareCronTest.php) | .php | class tests\units\CleanSoftwareCronTest extends DbTestCase |
| [tests/functional/ClusterTest.php](../tests/functional/ClusterTest.php) | .php | class tests\units\ClusterTest extends DbTestCase |
| [tests/functional/CommonDBChildTest.php](../tests/functional/CommonDBChildTest.php) | .php | class tests\units\CommonDBChildTest extends DbTestCase |
| [tests/functional/CommonDBConnexityTest.php](../tests/functional/CommonDBConnexityTest.php) | .php | class tests\units\CommonDBConnexityTest extends DbTestCase |
| [tests/functional/CommonDBRelationTest.php](../tests/functional/CommonDBRelationTest.php) | .php | class tests\units\CommonDBRelationTest extends DbTestCase |
| [tests/functional/CommonDBTMTest.php](../tests/functional/CommonDBTMTest.php) | .php | class tests\units\CommonDBTMTest extends DbTestCase |
| [tests/functional/CommonGLPITest.php](../tests/functional/CommonGLPITest.php) | .php | class tests\units\CommonGLPITest extends DbTestCase |
| [tests/functional/CommonITILActorTest.php](../tests/functional/CommonITILActorTest.php) | .php | class tests\units\CommonITILActorTest extends DbTestCase |
| [tests/functional/CommonITILObjectStatsTest.php](../tests/functional/CommonITILObjectStatsTest.php) | .php | class tests\units\CommonITILObjectStatsTest extends DbTestCase |
| [tests/functional/CommonITILObject_CommonITILObjectTest.php](../tests/functional/CommonITILObject_CommonITILObjectTest.php) | .php | class tests\units\CommonITILObject_CommonITILObjectTest extends DbTestCase |
| [tests/functional/CommonITILValidationCronTest.php](../tests/functional/CommonITILValidationCronTest.php) | .php | class tests\units\CommonITILValidationCronTest extends DbTestCase |
| [tests/functional/ComputerTest.php](../tests/functional/ComputerTest.php) | .php | class tests\units\ComputerTest extends DbTestCase |
| [tests/functional/ConfigTest.php](../tests/functional/ConfigTest.php) | .php | class tests\units\ConfigTest extends DbTestCase |
| [tests/functional/ConsumableTest.php](../tests/functional/ConsumableTest.php) | .php | class tests\units\ConsumableTest extends DbTestCase |
| [tests/functional/ContactTest.php](../tests/functional/ContactTest.php) | .php | class tests\units\ContactTest extends DbTestCase |
| [tests/functional/ContractTest.php](../tests/functional/ContractTest.php) | .php | class tests\units\ContractTest extends DbTestCase |
| [tests/functional/Contract_ItemTest.php](../tests/functional/Contract_ItemTest.php) | .php | class tests\units\Contract_ItemTest extends DbTestCase |
| [tests/functional/CronTaskTest.php](../tests/functional/CronTaskTest.php) | .php | class tests\units\CronTaskTest extends DbTestCase |
| [tests/functional/DBConnectionTest.php](../tests/functional/DBConnectionTest.php) | .php | class tests\units\DBConnectionTest extends GLPITestCase |
| [tests/functional/DBTest.php](../tests/functional/DBTest.php) | .php | class tests\units\DBTest extends GLPITestCase |
| [tests/functional/DBmysqlIteratorTest.php](../tests/functional/DBmysqlIteratorTest.php) | .php | class tests\units\DBmysqlIteratorTest extends DbTestCase |
| [tests/functional/DCRoomTest.php](../tests/functional/DCRoomTest.php) | .php | class tests\units\DCRoomTest extends DbTestCase |
| [tests/functional/DatabaseInstanceTest.php](../tests/functional/DatabaseInstanceTest.php) | .php | class tests\units\DatabaseInstanceTest extends DbTestCase |
| [tests/functional/DbUtilsTest.php](../tests/functional/DbUtilsTest.php) | .php | class tests\units\DbUtilsTest extends DbTestCase |
| [tests/functional/DefaultFilterTest.php](../tests/functional/DefaultFilterTest.php) | .php | class tests\units\DefaultFilterTest extends DbTestCase |
| [tests/functional/DeviceHardDriveTest.php](../tests/functional/DeviceHardDriveTest.php) | .php | class tests\units\DeviceHardDriveTest extends DbTestCase |
| [tests/functional/DeviceHardDriveTypeTest.php](../tests/functional/DeviceHardDriveTypeTest.php) | .php | class tests\units\DeviceHardDriveTypeTest extends DbTestCase |
| [tests/functional/DeviceSensorModelTest.php](../tests/functional/DeviceSensorModelTest.php) | .php | class tests\units\DeviceSensorModelTest extends DbTestCase |
| [tests/functional/DeviceSensorTest.php](../tests/functional/DeviceSensorTest.php) | .php | class tests\units\DeviceSensorTest extends DbTestCase |
| [tests/functional/DeviceSensorTypeTest.php](../tests/functional/DeviceSensorTypeTest.php) | .php | class tests\units\DeviceSensorTypeTest extends DbTestCase |
| [tests/functional/DeviceSimcardTest.php](../tests/functional/DeviceSimcardTest.php) | .php | class tests\units\DeviceSimcardTest extends DbTestCase |
| [tests/functional/DeviceSimcardTypeTest.php](../tests/functional/DeviceSimcardTypeTest.php) | .php | class tests\units\DeviceSimcardTypeTest extends DbTestCase |
| [tests/functional/DisplayPreferenceTest.php](../tests/functional/DisplayPreferenceTest.php) | .php | class tests\units\DisplayPreferenceTest extends DbTestCase |
| [tests/functional/DocumentTest.php](../tests/functional/DocumentTest.php) | .php | class tests\units\DocumentTest extends DbTestCase |
| [tests/functional/DocumentTypeTest.php](../tests/functional/DocumentTypeTest.php) | .php | class tests\units\DocumentTypeTest extends DbTestCase |
| [tests/functional/Document_ItemTest.php](../tests/functional/Document_ItemTest.php) | .php | class tests\units\Document_ItemTest extends DbTestCase |
| [tests/functional/DomainRecordTest.php](../tests/functional/DomainRecordTest.php) | .php | class tests\units\DomainRecordTest extends DbTestCase |
| [tests/functional/DomainRelationTest.php](../tests/functional/DomainRelationTest.php) | .php | class tests\units\DomainRelationTest extends DbTestCase |
| [tests/functional/DomainTest.php](../tests/functional/DomainTest.php) | .php | class tests\units\DomainTest extends DbTestCase |
| [tests/functional/Domain_ItemTest.php](../tests/functional/Domain_ItemTest.php) | .php | class tests\units\Domain_ItemTest extends DbTestCase |
| [tests/functional/DropdownTest.php](../tests/functional/DropdownTest.php) | .php | class tests\units\DropdownTest extends DbTestCase |
| [tests/functional/DropdownTranslationTest.php](../tests/functional/DropdownTranslationTest.php) | .php | class tests\units\DropdownTranslationTest extends DbTestCase |
| [tests/functional/DropdownValidatorTest.php](../tests/functional/DropdownValidatorTest.php) | .php | class tests\units\DropdownValidatorTest extends DbTestCase |
| [tests/functional/EntityTest.php](../tests/functional/EntityTest.php) | .php | class tests\units\EntityTest extends DbTestCase |
| [tests/functional/EventTest.php](../tests/functional/EventTest.php) | .php | class tests\units\EventTest extends DbTestCase |
| [tests/functional/FieldUnicityTest.php](../tests/functional/FieldUnicityTest.php) | .php | class tests\units\FieldUnicityTest extends DbTestCase |
| [tests/functional/GLPIKeyTest.php](../tests/functional/GLPIKeyTest.php) | .php | class tests\units\GLPIKeyTest extends DbTestCase |
| [tests/functional/GLPIMailerTest.php](../tests/functional/GLPIMailerTest.php) | .php | class tests\units\GLPIMailerTest extends DbTestCase |
| [tests/functional/GLPITest.php](../tests/functional/GLPITest.php) | .php | class tests\units\GLPITest extends GLPITestCase |
| [tests/functional/GLPIUploadHandlerTest.php](../tests/functional/GLPIUploadHandlerTest.php) | .php | class tests\units\GLPIUploadHandlerTest extends DbTestCase |
| [tests/functional/Glpi/Agent/Communication/Headers/CommonTest.php](../tests/functional/Glpi/Agent/Communication/Headers/CommonTest.php) | .php | class tests\units\Glpi\Agent\Communication\Headers\CommonTest extends GLPITestCase |
| [tests/functional/Glpi/Altcha/AltchaManagerTest.php](../tests/functional/Glpi/Altcha/AltchaManagerTest.php) | .php | class tests\units\Glpi\Altcha\AltchaManagerTest extends GLPITestCase |
| [tests/functional/Glpi/Api/APIRestGetItemTest.php](../tests/functional/Glpi/Api/APIRestGetItemTest.php) | .php | class tests\units\Glpi\Api\APIRestGetItemTest extends DbTestCase |
| [tests/functional/Glpi/Api/HL/Controller/AdministrationControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/AdministrationControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\AdministrationControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/AssetControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/AssetControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\AssetControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/ComponentControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/ComponentControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\ComponentControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/CoreControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/CoreControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\CoreControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/CustomAssetControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/CustomAssetControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\CustomAssetControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/DropdownControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/DropdownControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\DropdownControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/GraphQLControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/GraphQLControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\GraphQLControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/ITILControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/ITILControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\ITILControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/InventoryControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/InventoryControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\InventoryControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/KnowbaseControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/KnowbaseControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\KnowbaseControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/ManagementControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/ManagementControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\ManagementControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/NotepadControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/NotepadControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\NotepadControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/NotificationControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/NotificationControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\NotificationControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/ProjectControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/ProjectControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\ProjectControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/ReportControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/ReportControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\ReportControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/RuleControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/RuleControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\RuleControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/SecurityControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/SecurityControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\SecurityControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/SetupControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/SetupControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\SetupControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Controller/ToolControllerTest.php](../tests/functional/Glpi/Api/HL/Controller/ToolControllerTest.php) | .php | class tests\units\Glpi\Api\HL\Controller\ToolControllerTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/Doc/SchemaTest.php](../tests/functional/Glpi/Api/HL/Doc/SchemaTest.php) | .php | class tests\units\Glpi\Api\HL\Doc\SchemaTest extends GLPITestCase |
| [tests/functional/Glpi/Api/HL/Middleware/DebugRequestMiddlewareTest.php](../tests/functional/Glpi/Api/HL/Middleware/DebugRequestMiddlewareTest.php) | .php | class tests\units\Glpi\Api\HL\Middleware\DebugRequestMiddlewareTest extends DbTestCase |
| [tests/functional/Glpi/Api/HL/Middleware/IPRestrictionRequestMiddlewareTest.php](../tests/functional/Glpi/Api/HL/Middleware/IPRestrictionRequestMiddlewareTest.php) | .php | class tests\units\Glpi\Api\HL\Middleware\IPRestrictionRequestMiddlewareTest extends DbTestCase |
| [tests/functional/Glpi/Api/HL/OpenAPIGeneratorTest.php](../tests/functional/Glpi/Api/HL/OpenAPIGeneratorTest.php) | .php | class tests\units\Glpi\Api\HL\OpenAPIGeneratorTest extends HLAPITestCase |
| [tests/functional/Glpi/Api/HL/RSQL/LexerTest.php](../tests/functional/Glpi/Api/HL/RSQL/LexerTest.php) | .php | class tests\units\Glpi\Api\HL\RSQL\LexerTest extends GLPITestCase |
| [tests/functional/Glpi/Api/HL/RSQL/ParserTest.php](../tests/functional/Glpi/Api/HL/RSQL/ParserTest.php) | .php | class tests\units\Glpi\Api\HL\RSQL\ParserTest extends GLPITestCase |
| [tests/functional/Glpi/Api/HL/ResourceAccessorTest.php](../tests/functional/Glpi/Api/HL/ResourceAccessorTest.php) | .php | class tests\units\Glpi\Api\HL\ResourceAccessorTest extends DbTestCase |
| [tests/functional/Glpi/Api/HL/RouterTest.php](../tests/functional/Glpi/Api/HL/RouterTest.php) | .php | class tests\units\Glpi\Api\HL\RouterTest extends GLPITestCase |
| [tests/functional/Glpi/Application/ImportMapGeneratorTest.php](../tests/functional/Glpi/Application/ImportMapGeneratorTest.php) | .php | class tests\units\Glpi\Application\ImportMapGeneratorTest extends GLPITestCase |
| [tests/functional/Glpi/Application/ResourcesCheckerTest.php](../tests/functional/Glpi/Application/ResourcesCheckerTest.php) | .php | class tests\units\Glpi\Application\ResourcesCheckerTest extends GLPITestCase |
| [tests/functional/Glpi/Application/View/Extension/FrontEndAssetsExtensionTest.php](../tests/functional/Glpi/Application/View/Extension/FrontEndAssetsExtensionTest.php) | .php | class tests\units\Glpi\Application\View\Extension\FrontEndAssetsExtensionTest extends GLPITestCase |
| [tests/functional/Glpi/Application/View/Extension/RoutingExtensionTest.php](../tests/functional/Glpi/Application/View/Extension/RoutingExtensionTest.php) | .php | class tests\units\Glpi\Application\View\Extension\RoutingExtensionTest extends TestCase |
| [tests/functional/Glpi/Asset/AssetDefinitionManagerTest.php](../tests/functional/Glpi/Asset/AssetDefinitionManagerTest.php) | .php | class tests\units\Glpi\Asset\AssetDefinitionManagerTest extends DbTestCase |
| [tests/functional/Glpi/Asset/AssetDefinitionTest.php](../tests/functional/Glpi/Asset/AssetDefinitionTest.php) | .php | class tests\units\Glpi\Asset\AssetDefinitionTest extends DbTestCase |
| [tests/functional/Glpi/Asset/AssetModelTest.php](../tests/functional/Glpi/Asset/AssetModelTest.php) | .php | class tests\units\Glpi\Asset\AssetModelTest extends DbTestCase |
| [tests/functional/Glpi/Asset/AssetTest.php](../tests/functional/Glpi/Asset/AssetTest.php) | .php | class tests\units\Glpi\Asset\AssetTest extends DbTestCase |
| [tests/functional/Glpi/Asset/AssetTypeTest.php](../tests/functional/Glpi/Asset/AssetTypeTest.php) | .php | class tests\units\Glpi\Asset\AssetTypeTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Asset_PeripheralAssetTest.php](../tests/functional/Glpi/Asset/Asset_PeripheralAssetTest.php) | .php | class tests\units\Glpi\Asset\Asset_PeripheralAssetTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/AllowedInGlobalSearchCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/AllowedInGlobalSearchCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\AllowedInGlobalSearchCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasAntivirusCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasAntivirusCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasAntivirusCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasAppliancesCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasAppliancesCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasAppliancesCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasCertificatesCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasCertificatesCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasCertificatesCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasContractsCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasContractsCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasContractsCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasDatabaseInstanceCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasDatabaseInstanceCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasDatabaseInstanceCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasDevicesCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasDevicesCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasDevicesCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasDocumentsCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasDocumentsCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasDocumentsCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasDomainsCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasDomainsCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasDomainsCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasHistoryCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasHistoryCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasHistoryCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasImpactCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasImpactCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasImpactCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasInfocomCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasInfocomCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasInfocomCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasKnowbaseCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasKnowbaseCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasKnowbaseCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasLinksCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasLinksCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasLinksCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasNetworkPortCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasNetworkPortCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasNetworkPortCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasNotepadCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasNotepadCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasNotepadCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasOperatingSystemCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasOperatingSystemCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasOperatingSystemCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasPeripheralAssetsCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasPeripheralAssetsCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasPeripheralAssetsCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasPlugCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasPlugCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasPlugCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasRemoteManagementCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasRemoteManagementCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasRemoteManagementCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasSocketCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasSocketCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasSocketCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasSoftwaresCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasSoftwaresCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasSoftwaresCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasVirtualMachineCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasVirtualMachineCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasVirtualMachineCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/HasVolumesCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/HasVolumesCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\HasVolumesCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/IsInventoriableCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/IsInventoriableCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\IsInventoriableCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/IsProjectAssetCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/IsProjectAssetCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\IsProjectAssetCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/IsRackableCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/IsRackableCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\IsRackableCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/Capacity/IsReservableCapacityTest.php](../tests/functional/Glpi/Asset/Capacity/IsReservableCapacityTest.php) | .php | class tests\units\Glpi\Asset\Capacity\IsReservableCapacityTest extends DbTestCase |
| [tests/functional/Glpi/Asset/CustomFieldDefinitionTest.php](../tests/functional/Glpi/Asset/CustomFieldDefinitionTest.php) | .php | class tests\units\Glpi\Asset\CustomFieldDefinitionTest extends DbTestCase |
| [tests/functional/Glpi/Asset/DictionaryTest.php](../tests/functional/Glpi/Asset/DictionaryTest.php) | .php | class tests\units\Glpi\Asset\DictionaryTest extends DbTestCase |
| [tests/functional/Glpi/Cache/CacheManagerTest.php](../tests/functional/Glpi/Cache/CacheManagerTest.php) | .php | class tests\units\Glpi\Cache\CacheManagerTest extends GLPITestCase |
| [tests/functional/Glpi/Cache/SimpleCacheTest.php](../tests/functional/Glpi/Cache/SimpleCacheTest.php) | .php | class tests\units\Glpi\Cache\SimpleCacheTest extends GLPITestCase |
| [tests/functional/Glpi/CalDAV/ServerTest.php](../tests/functional/Glpi/CalDAV/ServerTest.php) | .php | class tests\units\Glpi\CalDAV\ServerTest extends DbTestCase |
| [tests/functional/Glpi/Config/ConfigContainerTest.php](../tests/functional/Glpi/Config/ConfigContainerTest.php) | .php | class tests\units\Glpi\Config\ConfigContainerTest extends GLPITestCase |
| [tests/functional/Glpi/Config/DataAndPrivacyConfigTest.php](../tests/functional/Glpi/Config/DataAndPrivacyConfigTest.php) | .php | class tests\units\Glpi\Config\DataAndPrivacyConfigTest extends DbTestCase |
| [tests/functional/Glpi/Console/CommandLoaderTest.php](../tests/functional/Glpi/Console/CommandLoaderTest.php) | .php | class tests\units\Glpi\Console\CommandLoaderTest extends GLPITestCase |
| [tests/functional/Glpi/ContentTemplates/Parameters/AssetParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/AssetParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\AssetParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/ChangeParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/ChangeParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\ChangeParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/EntityParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/EntityParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\EntityParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/GroupParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/GroupParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\GroupParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/ITILCategoryParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/ITILCategoryParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\ITILCategoryParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/KnowbaseItemParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/KnowbaseItemParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\KnowbaseItemParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/LocationParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/LocationParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\LocationParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/OLAParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/OLAParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\OLAParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/ProblemParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/ProblemParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\ProblemParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/RequestTypeParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/RequestTypeParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\RequestTypeParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/SLAParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/SLAParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\SLAParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/SupplierParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/SupplierParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\SupplierParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/TicketParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/TicketParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\TicketParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/UserCategoryParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/UserCategoryParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\UserCategoryParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/UserParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/UserParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\UserParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/Parameters/UserTitleParametersTest.php](../tests/functional/Glpi/ContentTemplates/Parameters/UserTitleParametersTest.php) | .php | class tests\units\Glpi\ContentTemplates\Parameters\UserTitleParametersTest extends AbstractParametersTest |
| [tests/functional/Glpi/ContentTemplates/TemplateManagerTest.php](../tests/functional/Glpi/ContentTemplates/TemplateManagerTest.php) | .php | class tests\units\Glpi\ContentTemplates\TemplateManagerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/DCRoom/UpdateAxisLabelControllerTest.php](../tests/functional/Glpi/Controller/DCRoom/UpdateAxisLabelControllerTest.php) | .php | class tests\units\Glpi\Controller\DCRoom\UpdateAxisLabelControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/ErrorControllerTest.php](../tests/functional/Glpi/Controller/ErrorControllerTest.php) | .php | class tests\units\Glpi\Controller\ErrorControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Form/ExportControllerTest.php](../tests/functional/Glpi/Controller/Form/ExportControllerTest.php) | .php | class tests\units\Glpi\Controller\Form\ExportControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Form/QuestionActorsDropdownControllerTest.php](../tests/functional/Glpi/Controller/Form/QuestionActorsDropdownControllerTest.php) | .php | class tests\units\Glpi\Controller\Form\QuestionActorsDropdownControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Form/SubmitAnswerControllerTest.php](../tests/functional/Glpi/Controller/Form/SubmitAnswerControllerTest.php) | .php | class tests\units\Glpi\Controller\Form\SubmitAnswerControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Form/Translation/GetFormTranslationControllerTest.php](../tests/functional/Glpi/Controller/Form/Translation/GetFormTranslationControllerTest.php) | .php | class tests\units\Glpi\Controller\Form\Translation\GetFormTranslationControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/GenericAjaxCrudControllerTest.php](../tests/functional/Glpi/Controller/GenericAjaxCrudControllerTest.php) | .php | class tests\units\Glpi\Controller\GenericAjaxCrudControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/AddCommentControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/AddCommentControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\AddCommentControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/AsideActionsControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/AsideActionsControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\AsideActionsControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/AsideArticleFoldControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/AsideArticleFoldControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\AsideArticleFoldControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/AsideSearchControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/AsideSearchControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\AsideSearchControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/CreateArticleControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/CreateArticleControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\CreateArticleControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/DeleteArticleControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/DeleteArticleControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\DeleteArticleControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/GetTranslationContentControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/GetTranslationContentControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\GetTranslationContentControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/HistoryPageControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/HistoryPageControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\HistoryPageControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/KnowbaseItemControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/KnowbaseItemControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\KnowbaseItemControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/MoveArticleControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/MoveArticleControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\MoveArticleControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/MoveModalControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/MoveModalControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\MoveModalControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/ToggleFavoriteControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/ToggleFavoriteControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\ToggleFavoriteControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/UploadDocumentsControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/UploadDocumentsControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\UploadDocumentsControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Knowbase/UploadInlineImageControllerTest.php](../tests/functional/Glpi/Controller/Knowbase/UploadInlineImageControllerTest.php) | .php | class tests\units\Glpi\Controller\Knowbase\UploadInlineImageControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Security/MFAControllerTest.php](../tests/functional/Glpi/Controller/Security/MFAControllerTest.php) | .php | class tests\units\Glpi\Controller\Security\MFAControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Security/ReAuthControllerTest.php](../tests/functional/Glpi/Controller/Security/ReAuthControllerTest.php) | .php | class tests\units\Glpi\Controller\Security\ReAuthControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/Security/Reauth/CASControllerTest.php](../tests/functional/Glpi/Controller/Security/Reauth/CASControllerTest.php) | .php | class tests\units\Glpi\Controller\Security\Reauth\CASControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/ServiceCatalog/IndexControllerTest.php](../tests/functional/Glpi/Controller/ServiceCatalog/IndexControllerTest.php) | .php | class tests\units\Glpi\Controller\ServiceCatalog\IndexControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/ShareAccessControllerTest.php](../tests/functional/Glpi/Controller/ShareAccessControllerTest.php) | .php | class tests\units\Glpi\Controller\ShareAccessControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/ShareTokenControllerTest.php](../tests/functional/Glpi/Controller/ShareTokenControllerTest.php) | .php | class tests\units\Glpi\Controller\ShareTokenControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/UI/Illustration/CustomIllustrationControllerTest.php](../tests/functional/Glpi/Controller/UI/Illustration/CustomIllustrationControllerTest.php) | .php | class tests\units\Glpi\Controller\UI\Illustration\CustomIllustrationControllerTest extends DbTestCase |
| [tests/functional/Glpi/Controller/UI/Illustration/UploadControllerTest.php](../tests/functional/Glpi/Controller/UI/Illustration/UploadControllerTest.php) | .php | class tests\units\Glpi\Controller\UI\Illustration\UploadControllerTest extends DbTestCase |
| [tests/functional/Glpi/Csv/CsvResponseTest.php](../tests/functional/Glpi/Csv/CsvResponseTest.php) | .php | class tests\units\Glpi\Csv\CsvResponseTest extends DbTestCase |
| [tests/functional/Glpi/Csv/LogCsvExportTest.php](../tests/functional/Glpi/Csv/LogCsvExportTest.php) | .php | class tests\units\Glpi\Csv\LogCsvExportTest extends CsvTestCase |
| [tests/functional/Glpi/Csv/PlanningCsvTest.php](../tests/functional/Glpi/Csv/PlanningCsvTest.php) | .php | class tests\units\Glpi\Csv\PlanningCsvTest extends CsvTestCase |
| [tests/functional/Glpi/DBAL/QueryExpressionTest.php](../tests/functional/Glpi/DBAL/QueryExpressionTest.php) | .php | class tests\units\Glpi\DBAL\QueryExpressionTest extends GLPITestCase |
| [tests/functional/Glpi/DBAL/QueryFunctionTest.php](../tests/functional/Glpi/DBAL/QueryFunctionTest.php) | .php | class tests\units\Glpi\DBAL\QueryFunctionTest extends GLPITestCase |
| [tests/functional/Glpi/DBAL/QueryIdentifierTest.php](../tests/functional/Glpi/DBAL/QueryIdentifierTest.php) | .php | class tests\units\Glpi\DBAL\QueryIdentifierTest extends GLPITestCase |
| [tests/functional/Glpi/DBAL/QueryParamTest.php](../tests/functional/Glpi/DBAL/QueryParamTest.php) | .php | class tests\units\Glpi\DBAL\QueryParamTest extends DbTestCase |
| [tests/functional/Glpi/DBAL/QueryValueTest.php](../tests/functional/Glpi/DBAL/QueryValueTest.php) | .php | class tests\units\Glpi\DBAL\QueryValueTest extends GLPITestCase |
| [tests/functional/Glpi/Dashboard/DashboardTest.php](../tests/functional/Glpi/Dashboard/DashboardTest.php) | .php | class tests\units\Glpi\Dashboard\DashboardTest extends DbTestCase |
| [tests/functional/Glpi/Dashboard/DatesFilterTest.php](../tests/functional/Glpi/Dashboard/DatesFilterTest.php) | .php | class tests\units\Glpi\Dashboard\DatesFilterTest extends DbTestCase |
| [tests/functional/Glpi/Dashboard/EntityFilterTest.php](../tests/functional/Glpi/Dashboard/EntityFilterTest.php) | .php | class tests\units\Glpi\Dashboard\EntityFilterTest extends DbTestCase |
| [tests/functional/Glpi/Dashboard/GridTest.php](../tests/functional/Glpi/Dashboard/GridTest.php) | .php | class tests\units\Glpi\Dashboard\GridTest extends DbTestCase |
| [tests/functional/Glpi/Dashboard/GroupFilterTest.php](../tests/functional/Glpi/Dashboard/GroupFilterTest.php) | .php | class tests\units\Glpi\Dashboard\GroupFilterTest extends DbTestCase |
| [tests/functional/Glpi/Dashboard/ProviderTest.php](../tests/functional/Glpi/Dashboard/ProviderTest.php) | .php | class tests\units\Glpi\Dashboard\ProviderTest extends DbTestCase |
| [tests/functional/Glpi/Dashboard/SlaFilterTest.php](../tests/functional/Glpi/Dashboard/SlaFilterTest.php) | .php | class tests\units\Glpi\Dashboard\SlaFilterTest extends DbTestCase |
| [tests/functional/Glpi/Dashboard/StateFilterTest.php](../tests/functional/Glpi/Dashboard/StateFilterTest.php) | .php | class tests\units\Glpi\Dashboard\StateFilterTest extends DbTestCase |
| [tests/functional/Glpi/Dashboard/TicketStatusFilterTest.php](../tests/functional/Glpi/Dashboard/TicketStatusFilterTest.php) | .php | class tests\units\Glpi\Dashboard\TicketStatusFilterTest extends DbTestCase |
| [tests/functional/Glpi/Dashboard/UserAssignedFilterTest.php](../tests/functional/Glpi/Dashboard/UserAssignedFilterTest.php) | .php | class tests\units\Glpi\Dashboard\UserAssignedFilterTest extends DbTestCase |
| [tests/functional/Glpi/Dashboard/WidgetTest.php](../tests/functional/Glpi/Dashboard/WidgetTest.php) | .php | class tests\units\Glpi\Dashboard\WidgetTest extends DbTestCase |
| [tests/functional/Glpi/Dropdown/DropdownDefinitionManagerTest.php](../tests/functional/Glpi/Dropdown/DropdownDefinitionManagerTest.php) | .php | class tests\units\Glpi\Dropdown\DropdownDefinitionManagerTest extends DbTestCase |
| [tests/functional/Glpi/Dropdown/DropdownDefinitionTest.php](../tests/functional/Glpi/Dropdown/DropdownDefinitionTest.php) | .php | class tests\units\Glpi\Dropdown\DropdownDefinitionTest extends DbTestCase |
| [tests/functional/Glpi/Dropdown/DropdownTest.php](../tests/functional/Glpi/Dropdown/DropdownTest.php) | .php | class tests\units\Glpi\Dropdown\DropdownTest extends DbTestCase |
| [tests/functional/Glpi/Error/ErrorUtilsTest.php](../tests/functional/Glpi/Error/ErrorUtilsTest.php) | .php | class Glpi\Error\ErrorUtilsTest extends DbTestCase |
| [tests/functional/Glpi/Error/InputTruncationReasonTest.php](../tests/functional/Glpi/Error/InputTruncationReasonTest.php) | .php | class tests\units\Glpi\Error\InputTruncationReasonTest extends TestCase |
| [tests/functional/Glpi/Error/StartupErrorsTest.php](../tests/functional/Glpi/Error/StartupErrorsTest.php) | .php | class tests\units\Glpi\Error\StartupErrorsTest extends TestCase |
| [tests/functional/Glpi/Features/AssignableItemTest.php](../tests/functional/Glpi/Features/AssignableItemTest.php) | .php | class tests\units\Glpi\Features\AssignableItemTest extends DbTestCase |
| [tests/functional/Glpi/Features/ClonableTest.php](../tests/functional/Glpi/Features/ClonableTest.php) | .php | class tests\units\Glpi\Features\ClonableTest extends DbTestCase |
| [tests/functional/Glpi/Features/DCBreadcrumbTest.php](../tests/functional/Glpi/Features/DCBreadcrumbTest.php) | .php | class tests\units\Glpi\Features\DCBreadcrumbTest extends DbTestCase |
| [tests/functional/Glpi/Form/AccessControl/ControlType/AllowListConfigTest.php](../tests/functional/Glpi/Form/AccessControl/ControlType/AllowListConfigTest.php) | .php | class tests\units\Glpi\Form\AccessControl\ControlType\AllowListConfigTest extends GLPITestCase |
| [tests/functional/Glpi/Form/AccessControl/ControlType/AllowListDropdownTest.php](../tests/functional/Glpi/Form/AccessControl/ControlType/AllowListDropdownTest.php) | .php | class tests\units\Glpi\Form\AccessControl\ControlType\AllowListDropdownTest extends DbTestCase |
| [tests/functional/Glpi/Form/AccessControl/ControlType/AllowListTest.php](../tests/functional/Glpi/Form/AccessControl/ControlType/AllowListTest.php) | .php | class tests\units\Glpi\Form\AccessControl\ControlType\AllowListTest extends DbTestCase |
| [tests/functional/Glpi/Form/AccessControl/ControlType/DirectAccessConfigTest.php](../tests/functional/Glpi/Form/AccessControl/ControlType/DirectAccessConfigTest.php) | .php | class tests\units\Glpi\Form\AccessControl\ControlType\DirectAccessConfigTest extends GLPITestCase |
| [tests/functional/Glpi/Form/AccessControl/ControlType/DirectAccessTest.php](../tests/functional/Glpi/Form/AccessControl/ControlType/DirectAccessTest.php) | .php | class tests\units\Glpi\Form\AccessControl\ControlType\DirectAccessTest extends DbTestCase |
| [tests/functional/Glpi/Form/AccessControl/FormAccessControlManagerTest.php](../tests/functional/Glpi/Form/AccessControl/FormAccessControlManagerTest.php) | .php | class tests\units\Glpi\Form\AccessControl\FormAccessControlManagerTest extends DbTestCase |
| [tests/functional/Glpi/Form/AccessControl/FormAccessControlTest.php](../tests/functional/Glpi/Form/AccessControl/FormAccessControlTest.php) | .php | class tests\units\Glpi\Form\AccessControl\FormAccessControlTest extends DbTestCase |
| [tests/functional/Glpi/Form/AccessControl/FormAccessParametersTest.php](../tests/functional/Glpi/Form/AccessControl/FormAccessParametersTest.php) | .php | class tests\units\Glpi\Form\AccessControl\FormAccessParametersTest extends GLPITestCase |
| [tests/functional/Glpi/Form/AnswerTest.php](../tests/functional/Glpi/Form/AnswerTest.php) | .php | class tests\unit\Glpi\Form\AnswerTest extends GLPITestCase |
| [tests/functional/Glpi/Form/AnswersHandler/AnswersHandlerTest.php](../tests/functional/Glpi/Form/AnswersHandler/AnswersHandlerTest.php) | .php | class tests\units\Glpi\Form\AnswersHandler\AnswersHandlerTest extends DbTestCase |
| [tests/functional/Glpi/Form/AnswersSetTest.php](../tests/functional/Glpi/Form/AnswersSetTest.php) | .php | class tests\units\Glpi\Form\AnswersSetTest extends DbTestCase |
| [tests/functional/Glpi/Form/CategoryTest.php](../tests/functional/Glpi/Form/CategoryTest.php) | .php | class tests\units\Glpi\Form\CategoryTest extends DbTestCase |
| [tests/functional/Glpi/Form/Clone/FormCloneHelperTest.php](../tests/functional/Glpi/Form/Clone/FormCloneHelperTest.php) | .php | class tests\units\Glpi\Form\Clone\FormCloneHelperTest extends DbTestCase |
| [tests/functional/Glpi/Form/CommentTest.php](../tests/functional/Glpi/Form/CommentTest.php) | .php | class tests\units\Glpi\Form\CommentTest extends DbTestCase |
| [tests/functional/Glpi/Form/Condition/ConditionDataTest.php](../tests/functional/Glpi/Form/Condition/ConditionDataTest.php) | .php | class tests\units\Glpi\Form\Condition\ConditionDataTest extends DbTestCase |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/ActorConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/ActorConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\ActorConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/DateConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/DateConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\DateConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/DateTimeConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/DateTimeConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\DateTimeConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/EmptyConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/EmptyConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\EmptyConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/ItemAsTextConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/ItemAsTextConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\ItemAsTextConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/ItemConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/ItemConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\ItemConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/MultipleChoiceFromValuesConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/MultipleChoiceFromValuesConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\MultipleChoiceFromValuesConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/NumberConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/NumberConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\NumberConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/RegexConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/RegexConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\RegexConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/RequestTypeConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/RequestTypeConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\RequestTypeConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/RichTextConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/RichTextConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\RichTextConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/SingleChoiceFromValuesConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/SingleChoiceFromValuesConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\SingleChoiceFromValuesConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/StringConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/StringConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\StringConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/TimeConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/TimeConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\TimeConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/UrgencyConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/UrgencyConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\UrgencyConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/UserDevicesAsTextConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/UserDevicesAsTextConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\UserDevicesAsTextConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/UserDevicesConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/UserDevicesConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\UserDevicesConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/ConditionHandler/VisibilityConditionHandlerTest.php](../tests/functional/Glpi/Form/Condition/ConditionHandler/VisibilityConditionHandlerTest.php) | .php | class Glpi\Form\Condition\ConditionHandler\VisibilityConditionHandlerTest extends AbstractConditionHandlerTest |
| [tests/functional/Glpi/Form/Condition/EditorManagerTest.php](../tests/functional/Glpi/Form/Condition/EditorManagerTest.php) | .php | class tests\units\Glpi\Form\Condition\EditorManagerTest extends GLPITestCase |
| [tests/functional/Glpi/Form/Condition/EngineTest.php](../tests/functional/Glpi/Form/Condition/EngineTest.php) | .php | class tests\units\Glpi\Form\Condition\EngineTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/AssigneeFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/AssigneeFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\AssigneeFieldTest extends AbstractActorFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/AssociatedItemsFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/AssociatedItemsFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\AssociatedItemsFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/BackupPlanFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/BackupPlanFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\BackupPlanFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/CausesFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/CausesFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\CausesFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/CheckListFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/CheckListFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\CheckListFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/ContentFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/ContentFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\ContentFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/ControlsListFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/ControlsListFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\ControlsListFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/DeploymentPlanFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/DeploymentPlanFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\DeploymentPlanFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/EntityFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/EntityFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\EntityFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/ITILCategoryFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/ITILCategoryFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\ITILCategoryFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/ITILFollowupFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/ITILFollowupFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\ITILFollowupFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/ITILTaskFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/ITILTaskFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\ITILTaskFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/ImpactsFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/ImpactsFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\ImpactsFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/LinkedITILObjectsFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/LinkedITILObjectsFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\LinkedITILObjectsFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/LocationFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/LocationFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\LocationFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/MailFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/MailFieldTest.php) | .php | class tests\units\MailFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/OLATTOFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/OLATTOFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\OLATTOFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/OLATTRFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/OLATTRFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\OLATTRFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/ObserverFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/ObserverFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\ObserverFieldTest extends AbstractActorFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/RequestSourceFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/RequestSourceFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\RequestSourceFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/RequestTypeFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/RequestTypeFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\RequestTypeFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/RequesterFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/RequesterFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\RequesterFieldTest extends AbstractActorFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/SLATTOFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/SLATTOFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\SLATTOFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/SLATTRFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/SLATTRFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\SLATTRFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/StatusFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/StatusFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\StatusFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/SymptomsFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/SymptomsFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\SymptomsFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/TemplateFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/TemplateFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\TemplateFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/TitleFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/TitleFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\TitleFieldTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/CommonITILField/UrgencyFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/UrgencyFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\UrgencyFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/CommonITILField/ValidationFieldTest.php](../tests/functional/Glpi/Form/Destination/CommonITILField/ValidationFieldTest.php) | .php | class tests\units\Glpi\Form\Destination\CommonITILField\ValidationFieldTest extends AbstractDestinationFieldTest |
| [tests/functional/Glpi/Form/Destination/FormDestinationChangeTest.php](../tests/functional/Glpi/Form/Destination/FormDestinationChangeTest.php) | .php | class tests\units\Glpi\Form\Destination\FormDestinationChangeTest extends AbstractCommonITILFormDestinationType |
| [tests/functional/Glpi/Form/Destination/FormDestinationManagerTest.php](../tests/functional/Glpi/Form/Destination/FormDestinationManagerTest.php) | .php | class tests\units\Glpi\Form\Destination\FormDestinationManagerTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/FormDestinationProblemTest.php](../tests/functional/Glpi/Form/Destination/FormDestinationProblemTest.php) | .php | class tests\units\Glpi\Form\Destination\FormDestinationProblemTest extends AbstractCommonITILFormDestinationType |
| [tests/functional/Glpi/Form/Destination/FormDestinationTest.php](../tests/functional/Glpi/Form/Destination/FormDestinationTest.php) | .php | class tests\units\Glpi\Form\Destination\FormDestinationTest extends DbTestCase |
| [tests/functional/Glpi/Form/Destination/FormDestinationTicketTest.php](../tests/functional/Glpi/Form/Destination/FormDestinationTicketTest.php) | .php | class tests\units\Glpi\Form\Destination\FormDestinationTicketTest extends AbstractCommonITILFormDestinationType |
| [tests/functional/Glpi/Form/Dropdown/FormActorsDropdownTest.php](../tests/functional/Glpi/Form/Dropdown/FormActorsDropdownTest.php) | .php | class tests\units\Glpi\Form\Dropdown\FormActorsDropdownTest extends DbTestCase |
| [tests/functional/Glpi/Form/EndUserInputNameProviderTest.php](../tests/functional/Glpi/Form/EndUserInputNameProviderTest.php) | .php | class tests\units\Glpi\Form\EndUserInputNameProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/Export/FormSerializerAccessPoliciesTest.php](../tests/functional/Glpi/Form/Export/FormSerializerAccessPoliciesTest.php) | .php | class tests\units\Glpi\Form\FormSerializerAccessPoliciesTest extends DbTestCase |
| [tests/functional/Glpi/Form/Export/FormSerializerDestinationTest.php](../tests/functional/Glpi/Form/Export/FormSerializerDestinationTest.php) | .php | class tests\units\Glpi\Form\FormSerializerDestinationTest extends DbTestCase |
| [tests/functional/Glpi/Form/Export/FormSerializerTest.php](../tests/functional/Glpi/Form/Export/FormSerializerTest.php) | .php | class tests\units\Glpi\Form\Export\FormSerializerTest extends DbTestCase |
| [tests/functional/Glpi/Form/FormTest.php](../tests/functional/Glpi/Form/FormTest.php) | .php | class tests\units\Glpi\Form\FormTest extends DbTestCase |
| [tests/functional/Glpi/Form/Migration/FormMigrationTest.php](../tests/functional/Glpi/Form/Migration/FormMigrationTest.php) | .php | class tests\units\Glpi\Form\Migration\FormMigrationTest extends DbTestCase |
| [tests/functional/Glpi/Form/Migration/QuestionTypeItemItemsIdsMigrationTest.php](../tests/functional/Glpi/Form/Migration/QuestionTypeItemItemsIdsMigrationTest.php) | .php | class tests\units\Glpi\Form\Migration\QuestionTypeItemItemsIdsMigrationTest extends DbTestCase |
| [tests/functional/Glpi/Form/Migration/TargetsMigrationTest.php](../tests/functional/Glpi/Form/Migration/TargetsMigrationTest.php) | .php | class tests\units\Glpi\Form\Migration\TargetsMigrationTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionTest.php](../tests/functional/Glpi/Form/QuestionTest.php) | .php | class tests\units\Glpi\Form\QuestionTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeAssigneeTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeAssigneeTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeAssigneeTest extends AbstractQuestionTypeActorsTest |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeCheckboxTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeCheckboxTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeCheckboxTest extends AbstractQuestionTypeSelectableTest |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeDateTimeTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeDateTimeTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeDateTimeTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeDropdownTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeDropdownTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeDropdownTest extends AbstractQuestionTypeSelectableTest |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeEmailTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeEmailTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeEmailTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeFileTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeFileTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeFileTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeItemDropdownTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeItemDropdownTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeItemDropdownTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeItemTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeItemTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeItemTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeLongTextTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeLongTextTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeLongTextTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeNumberTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeNumberTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeNumberTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeObserverTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeObserverTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeObserverTest extends AbstractQuestionTypeActorsTest |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeRadioTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeRadioTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeRadioTest extends AbstractQuestionTypeSelectableTest |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeRequestTypeTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeRequestTypeTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeRequestTypeTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeRequesterTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeRequesterTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeRequesterTest extends AbstractQuestionTypeActorsTest |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeShortTextTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeShortTextTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeShortTextTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeUrgencyTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeUrgencyTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeUrgencyTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypeUserDeviceTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypeUserDeviceTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypeUserDeviceTest extends DbTestCase |
| [tests/functional/Glpi/Form/QuestionType/QuestionTypesManagerTest.php](../tests/functional/Glpi/Form/QuestionType/QuestionTypesManagerTest.php) | .php | class tests\units\Glpi\Form\QuestionType\QuestionTypesManagerTest extends DbTestCase |
| [tests/functional/Glpi/Form/SectionTest.php](../tests/functional/Glpi/Form/SectionTest.php) | .php | class tests\units\Glpi\Form\SectionTest extends DbTestCase |
| [tests/functional/Glpi/Form/ServiceCatalog/HomeSearchManagerTest.php](../tests/functional/Glpi/Form/ServiceCatalog/HomeSearchManagerTest.php) | .php | class tests\units\Glpi\Form\ServiceCatalog\HomeSearchManagerTest extends DbTestCase |
| [tests/functional/Glpi/Form/ServiceCatalog/Provider/CategoryProviderTest.php](../tests/functional/Glpi/Form/ServiceCatalog/Provider/CategoryProviderTest.php) | .php | class tests\units\Glpi\Form\ServiceCatalog\Provider\CategoryProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/ServiceCatalog/Provider/FormProviderTest.php](../tests/functional/Glpi/Form/ServiceCatalog/Provider/FormProviderTest.php) | .php | class tests\units\Glpi\Form\ServiceCatalog\Provider\FormProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/ServiceCatalog/Provider/KnowbaseItemProviderTest.php](../tests/functional/Glpi/Form/ServiceCatalog/Provider/KnowbaseItemProviderTest.php) | .php | class tests\units\Glpi\Form\ServiceCatalog\Provider\KnowbaseItemProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/ServiceCatalog/ServiceCatalogManagerTest.php](../tests/functional/Glpi/Form/ServiceCatalog/ServiceCatalogManagerTest.php) | .php | class tests\units\Glpi\Form\ServiceCatalogManagerTest extends DbTestCase |
| [tests/functional/Glpi/Form/ServiceCatalog/SortStrategy/AlphabeticalSortTest.php](../tests/functional/Glpi/Form/ServiceCatalog/SortStrategy/AlphabeticalSortTest.php) | .php | class tests\units\Glpi\Form\AlphabeticalSortTest extends SortStrategyTestCase |
| [tests/functional/Glpi/Form/ServiceCatalog/SortStrategy/PopularitySortTest.php](../tests/functional/Glpi/Form/ServiceCatalog/SortStrategy/PopularitySortTest.php) | .php | class tests\units\Glpi\Form\PopularitySortTest extends SortStrategyTestCase |
| [tests/functional/Glpi/Form/ServiceCatalog/SortStrategy/ReverseAlphabeticalSortTest.php](../tests/functional/Glpi/Form/ServiceCatalog/SortStrategy/ReverseAlphabeticalSortTest.php) | .php | class tests\units\Glpi\Form\ReverseAlphabeticalSortTest extends SortStrategyTestCase |
| [tests/functional/Glpi/Form/Tag/AnswerTagProviderTest.php](../tests/functional/Glpi/Form/Tag/AnswerTagProviderTest.php) | .php | class tests\units\Glpi\Form\Tag\AnswerTagProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/Tag/CommentDescriptionTagProviderTest.php](../tests/functional/Glpi/Form/Tag/CommentDescriptionTagProviderTest.php) | .php | class tests\units\Glpi\Form\Tag\CommentDescriptionTagProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/Tag/CommentTitleTagProviderTest.php](../tests/functional/Glpi/Form/Tag/CommentTitleTagProviderTest.php) | .php | class tests\units\Glpi\Form\Tag\CommentTitleTagProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/Tag/FormTagProviderTest.php](../tests/functional/Glpi/Form/Tag/FormTagProviderTest.php) | .php | class tests\units\Glpi\Form\Tag\FormTagProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/Tag/FormTagsManagerTest.php](../tests/functional/Glpi/Form/Tag/FormTagsManagerTest.php) | .php | class tests\units\Glpi\Form\Tag\FormTagsManagerTest extends DbTestCase |
| [tests/functional/Glpi/Form/Tag/FullFormTagProviderTest.php](../tests/functional/Glpi/Form/Tag/FullFormTagProviderTest.php) | .php | class tests\units\Glpi\Form\Tag\FullFormTagProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/Tag/ItemPropertyTagProviderTest.php](../tests/functional/Glpi/Form/Tag/ItemPropertyTagProviderTest.php) | .php | class tests\units\Glpi\Form\Tag\ItemPropertyTagProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/Tag/QuestionTagProviderTest.php](../tests/functional/Glpi/Form/Tag/QuestionTagProviderTest.php) | .php | class tests\units\Glpi\Form\Tag\QuestionTagProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/Tag/SectionTagProviderTest.php](../tests/functional/Glpi/Form/Tag/SectionTagProviderTest.php) | .php | class tests\units\Glpi\Form\Tag\SectionTagProviderTest extends DbTestCase |
| [tests/functional/Glpi/Form/Tag/TagTest.php](../tests/functional/Glpi/Form/Tag/TagTest.php) | .php | class tests\units\Glpi\Form\Tag\TagTest extends DbTestCase |
| [tests/functional/Glpi/Form/Translation/FormTranslationTest.php](../tests/functional/Glpi/Form/Translation/FormTranslationTest.php) | .php | class tests\units\Glpi\Form\FormTranslationTest extends DbTestCase |
| [tests/functional/Glpi/Front/LocaleTest.php](../tests/functional/Glpi/Front/LocaleTest.php) | .php | class tests\units\Glpi\Front\LocaleTest extends DbTestCase |
| [tests/functional/Glpi/FuzzyMatcher/FuzzyMatcherTest.php](../tests/functional/Glpi/FuzzyMatcher/FuzzyMatcherTest.php) | .php | class tests\units\Glpi\FuzzyMatcher\FuzzyMatcherTest extends GLPITestCase |
| [tests/functional/Glpi/Helpdesk/DefaultDataManagerTest.php](../tests/functional/Glpi/Helpdesk/DefaultDataManagerTest.php) | .php | class test\units\Glpi\Helpdesk\DefaultDataManagerTest extends DbTestCase |
| [tests/functional/Glpi/Helpdesk/HomePageTabsTest.php](../tests/functional/Glpi/Helpdesk/HomePageTabsTest.php) | .php | class test\units\Glpi\Helpdesk\HomePageTabsTest extends DbTestCase |
| [tests/functional/Glpi/Helpdesk/Tile/ExternalPageTileTest.php](../tests/functional/Glpi/Helpdesk/Tile/ExternalPageTileTest.php) | .php | class tests\units\Glpi\Helpdesk\Tile\ExternalPageTileTest extends AbstractTileRightsTest |
| [tests/functional/Glpi/Helpdesk/Tile/FormTileTest.php](../tests/functional/Glpi/Helpdesk/Tile/FormTileTest.php) | .php | class tests\units\Glpi\Helpdesk\Tile\FormTileTest extends AbstractTileRightsTest |
| [tests/functional/Glpi/Helpdesk/Tile/GlpiPageTileTest.php](../tests/functional/Glpi/Helpdesk/Tile/GlpiPageTileTest.php) | .php | class tests\units\Glpi\Helpdesk\Tile\GlpiPageTileTest extends AbstractTileRightsTest |
| [tests/functional/Glpi/Helpdesk/Tile/TilesManagerTest.php](../tests/functional/Glpi/Helpdesk/Tile/TilesManagerTest.php) | .php | class tests\units\Glpi\Form\Helpdesk\TilesManagerTest\TilesManagerTest extends DbTestCase |
| [tests/functional/Glpi/Helpdesk/Translation/HelpdeskTranslationTest.php](../tests/functional/Glpi/Helpdesk/Translation/HelpdeskTranslationTest.php) | .php | class tests\units\Glpi\Form\HelpdeskTranslationTest extends DbTestCase |
| [tests/functional/Glpi/Http/FirewallTest.php](../tests/functional/Glpi/Http/FirewallTest.php) | .php | class tests\units\Glpi\Http\FirewallTest extends DbTestCase |
| [tests/functional/Glpi/Http/RequestRouterTraitTest.php](../tests/functional/Glpi/Http/RequestRouterTraitTest.php) | .php | class tests\units\Glpi\Http\RequestRouterTraitTest extends DbTestCase |
| [tests/functional/Glpi/Http/SessionManagerTest.php](../tests/functional/Glpi/Http/SessionManagerTest.php) | .php | class tests\units\Glpi\Http\SessionManagerTest extends DbTestCase |
| [tests/functional/Glpi/Inventory/Assets/AntivirusTest.php](../tests/functional/Glpi/Inventory/Assets/AntivirusTest.php) | .php | class tests\units\Glpi\Inventory\Asset\AntivirusTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/BatteryTest.php](../tests/functional/Glpi/Inventory/Assets/BatteryTest.php) | .php | class tests\units\Glpi\Inventory\Asset\BatteryTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/BiosTest.php](../tests/functional/Glpi/Inventory/Assets/BiosTest.php) | .php | class tests\units\Glpi\Inventory\Asset\BiosTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/CameraTest.php](../tests/functional/Glpi/Inventory/Assets/CameraTest.php) | .php | class tests\units\Glpi\Inventory\Asset\CameraTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/CartridgeTest.php](../tests/functional/Glpi/Inventory/Assets/CartridgeTest.php) | .php | class tests\units\Glpi\Inventory\Asset\CartridgeTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/ComputerTest.php](../tests/functional/Glpi/Inventory/Assets/ComputerTest.php) | .php | class tests\units\Glpi\Inventory\Asset\ComputerTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/ControllerTest.php](../tests/functional/Glpi/Inventory/Assets/ControllerTest.php) | .php | class tests\units\Glpi\Inventory\Asset\ControllerTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/DeviceTest.php](../tests/functional/Glpi/Inventory/Assets/DeviceTest.php) | .php | class tests\units\Glpi\Inventory\Asset\DeviceTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/DriveTest.php](../tests/functional/Glpi/Inventory/Assets/DriveTest.php) | .php | class tests\units\Glpi\Inventory\Asset\DriveTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/EnvironmentTest.php](../tests/functional/Glpi/Inventory/Assets/EnvironmentTest.php) | .php | class tests\units\Glpi\Inventory\Asset\EnvironmentTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/FirmwareTest.php](../tests/functional/Glpi/Inventory/Assets/FirmwareTest.php) | .php | class tests\units\Glpi\Inventory\Asset\FirmwareTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/GraphicCardTest.php](../tests/functional/Glpi/Inventory/Assets/GraphicCardTest.php) | .php | class tests\units\Glpi\Inventory\Asset\GraphicCardTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/MemoryTest.php](../tests/functional/Glpi/Inventory/Assets/MemoryTest.php) | .php | class tests\units\Glpi\Inventory\Asset\MemoryTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/MonitorTest.php](../tests/functional/Glpi/Inventory/Assets/MonitorTest.php) | .php | class tests\units\Glpi\Inventory\Asset\MonitorTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/NetworkCardTest.php](../tests/functional/Glpi/Inventory/Assets/NetworkCardTest.php) | .php | class tests\units\Glpi\Inventory\Asset\NetworkCardTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/NetworkEquipmentTest.php](../tests/functional/Glpi/Inventory/Assets/NetworkEquipmentTest.php) | .php | class tests\units\Glpi\Inventory\Asset\NetworkEquipmentTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/NetworkEquipmentUpdateTest.php](../tests/functional/Glpi/Inventory/Assets/NetworkEquipmentUpdateTest.php) | .php | class tests\units\Glpi\Inventory\Asset\NetworkEquipmentUpdateTest extends InventoryTestCase |
| [tests/functional/Glpi/Inventory/Assets/NetworkPortTest.php](../tests/functional/Glpi/Inventory/Assets/NetworkPortTest.php) | .php | class tests\units\Glpi\Inventory\Asset\NetworkPortTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/OperatingSystemTest.php](../tests/functional/Glpi/Inventory/Assets/OperatingSystemTest.php) | .php | class tests\units\Glpi\Inventory\Asset\OperatingSystemTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/PDUTest.php](../tests/functional/Glpi/Inventory/Assets/PDUTest.php) | .php | class tests\units\Glpi\Inventory\Asset\PDUTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/PeripheralTest.php](../tests/functional/Glpi/Inventory/Assets/PeripheralTest.php) | .php | class tests\units\Glpi\Inventory\Asset\PeripheralTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/PowerSupplyTest.php](../tests/functional/Glpi/Inventory/Assets/PowerSupplyTest.php) | .php | class tests\units\Glpi\Inventory\Asset\PowerSupplyTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/PrinterTest.php](../tests/functional/Glpi/Inventory/Assets/PrinterTest.php) | .php | class tests\units\Glpi\Inventory\Asset\PrinterTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/ProcessTest.php](../tests/functional/Glpi/Inventory/Assets/ProcessTest.php) | .php | class tests\units\Glpi\Inventory\Asset\ProcessTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/ProcessorTest.php](../tests/functional/Glpi/Inventory/Assets/ProcessorTest.php) | .php | class tests\units\Glpi\Inventory\Asset\ProcessorTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/RemoteManagementTest.php](../tests/functional/Glpi/Inventory/Assets/RemoteManagementTest.php) | .php | class tests\units\Glpi\Inventory\Asset\RemoteManagementTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/SensorTest.php](../tests/functional/Glpi/Inventory/Assets/SensorTest.php) | .php | class tests\units\Glpi\Inventory\Asset\SensorTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/SoftwareTest.php](../tests/functional/Glpi/Inventory/Assets/SoftwareTest.php) | .php | class tests\units\Glpi\Inventory\Asset\SoftwareTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/SoundCardTest.php](../tests/functional/Glpi/Inventory/Assets/SoundCardTest.php) | .php | class tests\units\Glpi\Inventory\Asset\SoundCardTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/UnmanagedTest.php](../tests/functional/Glpi/Inventory/Assets/UnmanagedTest.php) | .php | class tests\units\Glpi\Inventory\Asset\UnmanagedTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/VirtualMachineTest.php](../tests/functional/Glpi/Inventory/Assets/VirtualMachineTest.php) | .php | class tests\units\Glpi\Inventory\Asset\VirtualMachineTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/Assets/VolumeTest.php](../tests/functional/Glpi/Inventory/Assets/VolumeTest.php) | .php | class tests\units\Glpi\Inventory\Asset\VolumeTest extends AbstractInventoryAsset |
| [tests/functional/Glpi/Inventory/ConfTest.php](../tests/functional/Glpi/Inventory/ConfTest.php) | .php | class tests\units\Glpi\Inventory\ConfTest extends DbTestCase |
| [tests/functional/Glpi/Inventory/GenericAssetInventoryTest.php](../tests/functional/Glpi/Inventory/GenericAssetInventoryTest.php) | .php | class tests\units\Glpi\Inventory\GenericAssetInventoryTest extends InventoryTestCase |
| [tests/functional/Glpi/Inventory/GenericNetworkAssetInventoryTest.php](../tests/functional/Glpi/Inventory/GenericNetworkAssetInventoryTest.php) | .php | class tests\units\Glpi\Inventory\GenericNetworkAssetInventoryTest extends InventoryTestCase |
| [tests/functional/Glpi/Inventory/GenericPrinterAssetInventoryTest.php](../tests/functional/Glpi/Inventory/GenericPrinterAssetInventoryTest.php) | .php | class tests\units\Glpi\Inventory\GenericPrinterAssetInventoryTest extends InventoryTestCase |
| [tests/functional/Glpi/Inventory/ImportResultTest.php](../tests/functional/Glpi/Inventory/ImportResultTest.php) | .php | class tests\units\Glpi\Inventory\ImportResultTest extends GLPITestCase |
| [tests/functional/Glpi/Inventory/InventoryOptionsTest.php](../tests/functional/Glpi/Inventory/InventoryOptionsTest.php) | .php | class tests\units\Glpi\Inventory\InventoryOptionsTest extends InventoryTestCase |
| [tests/functional/Glpi/Inventory/InventoryTest.php](../tests/functional/Glpi/Inventory/InventoryTest.php) | .php | class tests\units\Glpi\Inventory\InventoryTest extends InventoryTestCase |
| [tests/functional/Glpi/Inventory/RequestTest.php](../tests/functional/Glpi/Inventory/RequestTest.php) | .php | class tests\units\Glpi\Inventory\RequestTest extends GLPITestCase |
| [tests/functional/Glpi/Kernel/Listener/ControllerListener/ControllerListenersPriorityTest.php](../tests/functional/Glpi/Kernel/Listener/ControllerListener/ControllerListenersPriorityTest.php) | .php | class tests\units\Glpi\Kernel\Listener\ControllerListener\ControllerListenersPriorityTest extends DbTestCase |
| [tests/functional/Glpi/Kernel/Listener/ExceptionListener/AccessErrorListenerTest.php](../tests/functional/Glpi/Kernel/Listener/ExceptionListener/AccessErrorListenerTest.php) | .php | class tests\units\Glpi\Kernel\Listener\ExceptionListener\AccessErrorListenerTest extends DbTestCase |
| [tests/functional/Glpi/Kernel/Listener/PostBootListener/SessionStartTest.php](../tests/functional/Glpi/Kernel/Listener/PostBootListener/SessionStartTest.php) | .php | class tests\units\Glpi\Kernel\Listener\PostBootListener\SessionStartTest extends GLPITestCase |
| [tests/functional/Glpi/Kernel/Listener/PostBootListener/SetDbSessionVarsTest.php](../tests/functional/Glpi/Kernel/Listener/PostBootListener/SetDbSessionVarsTest.php) | .php | class tests\units\Glpi\Kernel\Listener\PostBootListener\SetDbSessionVarsTest extends GLPITestCase |
| [tests/functional/Glpi/Kernel/Listener/RequestListener/CheckStartupErrorsListenerTest.php](../tests/functional/Glpi/Kernel/Listener/RequestListener/CheckStartupErrorsListenerTest.php) | .php | class tests\units\Glpi\Kernel\Listener\RequestListener\CheckStartupErrorsListenerTest extends GLPITestCase |
| [tests/functional/Glpi/Kernel/Listener/RequestListener/ConfigureTrustedProxiesTest.php](../tests/functional/Glpi/Kernel/Listener/RequestListener/ConfigureTrustedProxiesTest.php) | .php | class tests\units\Glpi\Kernel\Listener\RequestListener\ConfigureTrustedProxiesTest extends TestCase |
| [tests/functional/Glpi/Kernel/Listener/RequestListener/FrontEndAssetsListenerTest.php](../tests/functional/Glpi/Kernel/Listener/RequestListener/FrontEndAssetsListenerTest.php) | .php | class tests\units\Glpi\Kernel\Listener\RequestListener\FrontEndAssetsListenerTest extends GLPITestCase |
| [tests/functional/Glpi/Kernel/Listener/RequestListener/LegacyItemtypeRouteListenerTest.php](../tests/functional/Glpi/Kernel/Listener/RequestListener/LegacyItemtypeRouteListenerTest.php) | .php | class tests\units\Glpi\Kernel\Listener\RequestListener\LegacyItemtypeRouteListenerTest extends TestCase |
| [tests/functional/Glpi/Kernel/Listener/RequestListener/LegacyRouterListenerTest.php](../tests/functional/Glpi/Kernel/Listener/RequestListener/LegacyRouterListenerTest.php) | .php | class tests\units\Glpi\Kernel\Listener\RequestListener\LegacyRouterListenerTest extends GLPITestCase |
| [tests/functional/Glpi/Kernel/Listener/RequestListener/ReAuthReplayListenerTest.php](../tests/functional/Glpi/Kernel/Listener/RequestListener/ReAuthReplayListenerTest.php) | .php | class tests\units\Glpi\Kernel\Listener\RequestListener\ReAuthReplayListenerTest extends TestCase |
| [tests/functional/Glpi/Kernel/Listener/RequestListener/RedirectLegacyRouteListenerTest.php](../tests/functional/Glpi/Kernel/Listener/RequestListener/RedirectLegacyRouteListenerTest.php) | .php | class tests\units\Glpi\Kernel\Listener\RequestListener\RedirectLegacyRouteListenerTest extends TestCase |
| [tests/functional/Glpi/Knowbase/Aside/BuilderTest.php](../tests/functional/Glpi/Knowbase/Aside/BuilderTest.php) | .php | class tests\unit\Glpi\Knowbase\Aside\BuilderTest extends DbTestCase |
| [tests/functional/Glpi/Knowbase/Aside/MoveCandidatesTest.php](../tests/functional/Glpi/Knowbase/Aside/MoveCandidatesTest.php) | .php | class tests\unit\Glpi\Knowbase\Aside\MoveCandidatesTest extends DbTestCase |
| [tests/functional/Glpi/Knowbase/Aside/SearchResultsBuilderTest.php](../tests/functional/Glpi/Knowbase/Aside/SearchResultsBuilderTest.php) | .php | class tests\unit\Glpi\Knowbase\Aside\SearchResultsBuilderTest extends DbTestCase |
| [tests/functional/Glpi/Knowbase/History/HistoryBuilderTest.php](../tests/functional/Glpi/Knowbase/History/HistoryBuilderTest.php) | .php | class tests\unit\Glpi\Knowbase\History\HistoryBuilderTest extends DbTestCase |
| [tests/functional/Glpi/Knowbase/History/LogEventTest.php](../tests/functional/Glpi/Knowbase/History/LogEventTest.php) | .php | class tests\unit\Glpi\Knowbase\History\LogEventTest extends GLPITestCase |
| [tests/functional/Glpi/Knowbase/SidePanel/CommentsRendererTest.php](../tests/functional/Glpi/Knowbase/SidePanel/CommentsRendererTest.php) | .php | class tests\units\Glpi\Knowbase\SidePanel\CommentsRendererTest extends DbTestCase |
| [tests/functional/Glpi/Knowbase/SidePanel/HistoryRendererTest.php](../tests/functional/Glpi/Knowbase/SidePanel/HistoryRendererTest.php) | .php | class tests\units\Glpi\Knowbase\SidePanel\HistoryRendererTest extends DbTestCase |
| [tests/functional/Glpi/Knowbase/SidePanel/PermissionsRendererTest.php](../tests/functional/Glpi/Knowbase/SidePanel/PermissionsRendererTest.php) | .php | class tests\units\Glpi\Knowbase\SidePanel\PermissionsRendererTest extends DbTestCase |
| [tests/functional/Glpi/Knowbase/SidePanel/SharingRendererTest.php](../tests/functional/Glpi/Knowbase/SidePanel/SharingRendererTest.php) | .php | class tests\units\Glpi\Knowbase\SidePanel\SharingRendererTest extends DbTestCase |
| [tests/functional/Glpi/Locale/LanguageRegistryTest.php](../tests/functional/Glpi/Locale/LanguageRegistryTest.php) | .php | class tests\units\Glpi\Locale\LanguageRegistryTest extends GLPITestCase |
| [tests/functional/Glpi/Locale/LanguageTest.php](../tests/functional/Glpi/Locale/LanguageTest.php) | .php | class tests\units\Glpi\Locale\LanguageTest extends GLPITestCase |
| [tests/functional/Glpi/Log/ErrorLogHandlerTest.php](../tests/functional/Glpi/Log/ErrorLogHandlerTest.php) | .php | class tests\units\Glpi\Log\ErrorLogHandlerTest extends TestCase |
| [tests/functional/Glpi/Log/ErrorLogLineFormatterTest.php](../tests/functional/Glpi/Log/ErrorLogLineFormatterTest.php) | .php | class tests\units\Glpi\Log\ErrorLogLineFormatterTest extends TestCase |
| [tests/functional/Glpi/Migration/AbstractPluginMigrationTest.php](../tests/functional/Glpi/Migration/AbstractPluginMigrationTest.php) | .php | class tests\units\Glpi\Migration\AbstractPluginMigrationTest extends DbTestCase |
| [tests/functional/Glpi/Migration/GenericobjectPluginMigrationTest.php](../tests/functional/Glpi/Migration/GenericobjectPluginMigrationTest.php) | .php | class tests\units\Glpi\Migration\GenericobjectPluginMigrationTest extends DbTestCase |
| [tests/functional/Glpi/OAuth/AccessTokenRepositoryTest.php](../tests/functional/Glpi/OAuth/AccessTokenRepositoryTest.php) | .php | class tests\units\Glpi\OAuth\AccessTokenRepositoryTest extends DbTestCase |
| [tests/functional/Glpi/OAuth/RefreshTokenRepositoryTest.php](../tests/functional/Glpi/OAuth/RefreshTokenRepositoryTest.php) | .php | class tests\units\Glpi\OAuth\RefreshTokenRepositoryTest extends DbTestCase |
| [tests/functional/Glpi/OAuth/ServerTest.php](../tests/functional/Glpi/OAuth/ServerTest.php) | .php | class tests\units\Glpi\Migration\ServerTest extends DbTestCase |
| [tests/functional/Glpi/Plugin/HooksTest.php](../tests/functional/Glpi/Plugin/HooksTest.php) | .php | class tests\units\HooksTest extends GLPITestCase |
| [tests/functional/Glpi/Progress/AbstractProgressIndicatorTest.php](../tests/functional/Glpi/Progress/AbstractProgressIndicatorTest.php) | .php | class tests\units\Glpi\Log\AbstractProgressIndicatorTest extends GLPITestCase |
| [tests/functional/Glpi/Progress/ConsoleProgressIndicatorTest.php](../tests/functional/Glpi/Progress/ConsoleProgressIndicatorTest.php) | .php | class tests\units\Glpi\Log\ConsoleProgressIndicatorTest extends GLPITestCase |
| [tests/functional/Glpi/Progress/ProgressStorageTest.php](../tests/functional/Glpi/Progress/ProgressStorageTest.php) | .php | class tests\units\Glpi\Progress\ProgressStorageTest extends GLPITestCase |
| [tests/functional/Glpi/Progress/StoredProgressIndicatorTest.php](../tests/functional/Glpi/Progress/StoredProgressIndicatorTest.php) | .php | class tests\units\Glpi\Log\StoredProgressIndicatorTest extends GLPITestCase |
| [tests/functional/Glpi/RichText/RichTextTest.php](../tests/functional/Glpi/RichText/RichTextTest.php) | .php | class tests\units\Glpi\RichText\RichTextTest extends GLPITestCase |
| [tests/functional/Glpi/RichText/UserMentionTest.php](../tests/functional/Glpi/RichText/UserMentionTest.php) | .php | class tests\units\Glpi\RichText\UserMentionTest extends DbTestCase |
| [tests/functional/Glpi/RichText/VideoEmbedRendererTest.php](../tests/functional/Glpi/RichText/VideoEmbedRendererTest.php) | .php | class tests\units\Glpi\RichText\VideoEmbedRendererTest extends GLPITestCase |
| [tests/functional/Glpi/Routing/Attribute/ItemtypeFormRouteTest.php](../tests/functional/Glpi/Routing/Attribute/ItemtypeFormRouteTest.php) | .php | class tests\units\Glpi\Routing\Attribute\ItemtypeFormRouteTest extends GLPITestCase |
| [tests/functional/Glpi/Routing/Attribute/ItemtypeListRouteTest.php](../tests/functional/Glpi/Routing/Attribute/ItemtypeListRouteTest.php) | .php | class tests\units\Glpi\Routing\Attribute\ItemtypeListRouteTest extends GLPITestCase |
| [tests/functional/Glpi/Search/Input/QueryBuilderTest.php](../tests/functional/Glpi/Search/Input/QueryBuilderTest.php) | .php | class tests\units\Glpi\Search\Input\QueryBuilderTest extends GLPITestCase |
| [tests/functional/Glpi/Search/Output/SpreadsheetValueBinderTest.php](../tests/functional/Glpi/Search/Output/SpreadsheetValueBinderTest.php) | .php | class functional\Glpi\Search\Output\SpreadsheetValueBinderTest extends GLPITestCase |
| [tests/functional/Glpi/Search/Provider/SQLProviderTest.php](../tests/functional/Glpi/Search/Provider/SQLProviderTest.php) | .php | class tests\units\Glpi\Search\Provider\SQLProviderTest extends DbTestCase |
| [tests/functional/Glpi/Search/SearchEngineTest.php](../tests/functional/Glpi/Search/SearchEngineTest.php) | .php | class tests\units\Glpi\Search\SearchEngineTest extends DbTestCase |
| [tests/functional/Glpi/Search/SearchOptionTest.php](../tests/functional/Glpi/Search/SearchOptionTest.php) | .php | class tests\units\Glpi\Search\SearchOptionTest extends DbTestCase |
| [tests/functional/Glpi/Security/ReAuth/CasReAuthStrategyTest.php](../tests/functional/Glpi/Security/ReAuth/CasReAuthStrategyTest.php) | .php | class tests\units\Glpi\Security\ReAuth\CasReAuthStrategyTest extends DbTestCase |
| [tests/functional/Glpi/Security/ReAuth/FallbackReAuthStrategyTest.php](../tests/functional/Glpi/Security/ReAuth/FallbackReAuthStrategyTest.php) | .php | class tests\units\Glpi\Security\ReAuth\FallbackReAuthStrategyTest extends DbTestCase |
| [tests/functional/Glpi/Security/ReAuth/PasswordReAuthStrategyTest.php](../tests/functional/Glpi/Security/ReAuth/PasswordReAuthStrategyTest.php) | .php | class tests\units\Glpi\Security\ReAuth\PasswordReAuthStrategyTest extends DbTestCase |
| [tests/functional/Glpi/Security/ReAuth/ReAuthManagerTest.php](../tests/functional/Glpi/Security/ReAuth/ReAuthManagerTest.php) | .php | class tests\units\Glpi\Security\ReAuth\ReAuthManagerTest extends DbTestCase |
| [tests/functional/Glpi/Security/ReAuth/TOTPReAuthStrategyTest.php](../tests/functional/Glpi/Security/ReAuth/TOTPReAuthStrategyTest.php) | .php | class tests\units\Glpi\Security\ReAuth\TOTPReAuthStrategyTest extends DbTestCase |
| [tests/functional/Glpi/Security/SessionTrackerTest.php](../tests/functional/Glpi/Security/SessionTrackerTest.php) | .php | class tests\units\Glpi\Security\SessionTrackerTest extends DbTestCase |
| [tests/functional/Glpi/Security/ShareTokenManagerTest.php](../tests/functional/Glpi/Security/ShareTokenManagerTest.php) | .php | class tests\units\Glpi\Security\ShareTokenManagerTest extends DbTestCase |
| [tests/functional/Glpi/Security/TOTPManagerTest.php](../tests/functional/Glpi/Security/TOTPManagerTest.php) | .php | class tests\units\Glpi\Security\TOTPManagerTest extends DbTestCase |
| [tests/functional/Glpi/Session/SessionInfoTest.php](../tests/functional/Glpi/Session/SessionInfoTest.php) | .php | class tests\units\Glpi\Session\SessionInfoTest extends GLPITestCase |
| [tests/functional/Glpi/ShareTokenTest.php](../tests/functional/Glpi/ShareTokenTest.php) | .php | class tests\units\Glpi\ShareTokenTest extends DbTestCase |
| [tests/functional/Glpi/ShareableAccessTest.php](../tests/functional/Glpi/ShareableAccessTest.php) | .php | class tests\units\Glpi\ShareableAccessTest extends DbTestCase |
| [tests/functional/Glpi/SocketTest.php](../tests/functional/Glpi/SocketTest.php) | .php | class tests\units\Glpi\SocketTest extends DbTestCase |
| [tests/functional/Glpi/System/Diagnostic/DatabaseKeysCheckerTest.php](../tests/functional/Glpi/System/Diagnostic/DatabaseKeysCheckerTest.php) | .php | class tests\units\Glpi\System\Diagnostic\DatabaseKeysCheckerTest extends GLPITestCase |
| [tests/functional/Glpi/System/Diagnostic/DatabaseSchemaConsistencyCheckerTest.php](../tests/functional/Glpi/System/Diagnostic/DatabaseSchemaConsistencyCheckerTest.php) | .php | class tests\units\Glpi\System\Diagnostic\DatabaseSchemaConsistencyCheckerTest extends GLPITestCase |
| [tests/functional/Glpi/System/Diagnostic/DatabaseSchemaIntegrityCheckerTest.php](../tests/functional/Glpi/System/Diagnostic/DatabaseSchemaIntegrityCheckerTest.php) | .php | class tests\units\Glpi\System\Diagnostic\DatabaseSchemaIntegrityCheckerTest extends GLPITestCase |
| [tests/functional/Glpi/System/Diagnostic/SourceCodeIntegrityCheckerTest.php](../tests/functional/Glpi/System/Diagnostic/SourceCodeIntegrityCheckerTest.php) | .php | class tests\units\Glpi\System\Diagnostic\SourceCodeIntegrityCheckerTest extends GLPITestCase |
| [tests/functional/Glpi/System/Log/LogParserTest.php](../tests/functional/Glpi/System/Log/LogParserTest.php) | .php | class tests\units\Glpi\System\Log\LogParserTest extends GLPITestCase |
| [tests/functional/Glpi/System/Log/LogViewerTest.php](../tests/functional/Glpi/System/Log/LogViewerTest.php) | .php | class tests\units\Glpi\System\Log\LogViewerTest extends DbTestCase |
| [tests/functional/Glpi/System/Requirement/DatabaseTablesEngineTest.php](../tests/functional/Glpi/System/Requirement/DatabaseTablesEngineTest.php) | .php | class tests\units\Glpi\System\Requirement\DatabaseTablesEngineTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/DbConfigurationTest.php](../tests/functional/Glpi/System/Requirement/DbConfigurationTest.php) | .php | class tests\units\Glpi\System\Requirement\DbConfigurationTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/DbEngineTest.php](../tests/functional/Glpi/System/Requirement/DbEngineTest.php) | .php | class tests\units\Glpi\System\Requirement\DbEngineTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/DbTimezonesTest.php](../tests/functional/Glpi/System/Requirement/DbTimezonesTest.php) | .php | class tests\units\Glpi\System\Requirement\DbTimezonesTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/DirectoriesWriteAccessTest.php](../tests/functional/Glpi/System/Requirement/DirectoriesWriteAccessTest.php) | .php | class tests\units\Glpi\System\Requirement\DirectoriesWriteAccessTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/DirectoryWriteAccessTest.php](../tests/functional/Glpi/System/Requirement/DirectoryWriteAccessTest.php) | .php | class tests\units\Glpi\System\Requirement\DirectoryWriteAccessTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/ExtensionClassTest.php](../tests/functional/Glpi/System/Requirement/ExtensionClassTest.php) | .php | class tests\units\Glpi\System\Requirement\ExtensionClassTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/ExtensionConstantTest.php](../tests/functional/Glpi/System/Requirement/ExtensionConstantTest.php) | .php | class tests\units\Glpi\System\Requirement\ExtensionConstantTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/ExtensionFunctionTest.php](../tests/functional/Glpi/System/Requirement/ExtensionFunctionTest.php) | .php | class tests\units\Glpi\System\Requirement\ExtensionFunctionTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/ExtensionGroupTest.php](../tests/functional/Glpi/System/Requirement/ExtensionGroupTest.php) | .php | class tests\units\Glpi\System\Requirement\ExtensionGroupTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/ExtensionTest.php](../tests/functional/Glpi/System/Requirement/ExtensionTest.php) | .php | class tests\units\Glpi\System\Requirement\ExtensionTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/LogsWriteAccessTest.php](../tests/functional/Glpi/System/Requirement/LogsWriteAccessTest.php) | .php | class tests\units\Glpi\System\Requirement\LogsWriteAccessTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/MemoryLimitTest.php](../tests/functional/Glpi/System/Requirement/MemoryLimitTest.php) | .php | class tests\units\Glpi\System\Requirement\MemoryLimitTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/PhpSupportedVersionTest.php](../tests/functional/Glpi/System/Requirement/PhpSupportedVersionTest.php) | .php | class tests\units\Glpi\System\Requirement\PhpSupportedVersionTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/PhpVersionTest.php](../tests/functional/Glpi/System/Requirement/PhpVersionTest.php) | .php | class tests\units\Glpi\System\Requirement\PhpVersionTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/SeLinuxTest.php](../tests/functional/Glpi/System/Requirement/SeLinuxTest.php) | .php | class tests\units\Glpi\System\Requirement\SeLinuxTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/SecurityKeysAccessTest.php](../tests/functional/Glpi/System/Requirement/SecurityKeysAccessTest.php) | .php | class tests\units\Glpi\System\Requirement\SecurityKeysAccessTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/SessionsConfigurationTest.php](../tests/functional/Glpi/System/Requirement/SessionsConfigurationTest.php) | .php | class tests\units\Glpi\System\Requirement\SessionsConfigurationTest extends GLPITestCase |
| [tests/functional/Glpi/System/Requirement/SessionsSecurityConfigurationTest.php](../tests/functional/Glpi/System/Requirement/SessionsSecurityConfigurationTest.php) | .php | class tests\units\Glpi\System\Requirement\SessionsSecurityConfigurationTest extends GLPITestCase |
| [tests/functional/Glpi/System/StatusCheckerTest.php](../tests/functional/Glpi/System/StatusCheckerTest.php) | .php | class tests\units\Glpi\System\StatusCheckerTest extends GLPITestCase |
| [tests/functional/Glpi/Toolbox/ArrayNormalizerTest.php](../tests/functional/Glpi/Toolbox/ArrayNormalizerTest.php) | .php | class tests\units\Glpi\Cache\ArrayNormalizerTest extends GLPITestCase |
| [tests/functional/Glpi/Toolbox/DataExportTest.php](../tests/functional/Glpi/Toolbox/DataExportTest.php) | .php | class tests\units\Glpi\Toolbox\DataExportTest extends GLPITestCase |
| [tests/functional/Glpi/Toolbox/DatabaseSchemaTest.php](../tests/functional/Glpi/Toolbox/DatabaseSchemaTest.php) | .php | class tests\units\Glpi\Toolbox\DatabaseSchemaTest extends GLPITestCase |
| [tests/functional/Glpi/Toolbox/FileInfoTest.php](../tests/functional/Glpi/Toolbox/FileInfoTest.php) | .php | class tests\units\Glpi\Toolbox\FileInfoTest extends GLPITestCase |
| [tests/functional/Glpi/Toolbox/FilesystemTest.php](../tests/functional/Glpi/Toolbox/FilesystemTest.php) | .php | class tests\units\Glpi\Toolbox\FilesystemTest extends GLPITestCase |
| [tests/functional/Glpi/Toolbox/FrontEndTest.php](../tests/functional/Glpi/Toolbox/FrontEndTest.php) | .php | class tests\units\Glpi\Toolbox\FrontEndTest extends GLPITestCase |
| [tests/functional/Glpi/Toolbox/IPUtilitiesTest.php](../tests/functional/Glpi/Toolbox/IPUtilitiesTest.php) | .php | class tests\units\Glpi\Toolbox\IPUtilitiesTest extends GLPITestCase |
| [tests/functional/Glpi/Toolbox/NoPrivateNetworkHttpClientPatchTest.php](../tests/functional/Glpi/Toolbox/NoPrivateNetworkHttpClientPatchTest.php) | .php | class tests\units\Glpi\Toolbox\NoPrivateNetworkHttpClientPatchTest extends GLPITestCase |
| [tests/functional/Glpi/Toolbox/SanitizedStringsDecoderTest.php](../tests/functional/Glpi/Toolbox/SanitizedStringsDecoderTest.php) | .php | class tests\units\Glpi\Toolbox\SanitizedStringsDecoderTest extends GLPITestCase |
| [tests/functional/Glpi/Toolbox/URLTest.php](../tests/functional/Glpi/Toolbox/URLTest.php) | .php | class tests\units\Glpi\Toolbox\URLTest extends GLPITestCase |
| [tests/functional/Glpi/Toolbox/VersionParserTest.php](../tests/functional/Glpi/Toolbox/VersionParserTest.php) | .php | class tests\units\Glpi\Toolbox\VersionParserTest extends GLPITestCase |
| [tests/functional/Glpi/UI/IllustrationManagerTest.php](../tests/functional/Glpi/UI/IllustrationManagerTest.php) | .php | class tests\units\Glpi\UI\IllustrationManagerTest extends GLPITestCase |
| [tests/functional/Glpi/UI/ThemeTest.php](../tests/functional/Glpi/UI/ThemeTest.php) | .php | class tests\units\Glpi\UI\ThemeTest extends DbTestCase |
| [tests/functional/GroupTest.php](../tests/functional/GroupTest.php) | .php | class tests\units\GroupTest extends DbTestCase |
| [tests/functional/Group_UserTest.php](../tests/functional/Group_UserTest.php) | .php | class tests\units\Group_UserTest extends DbTestCase |
| [tests/functional/HtmlTest.php](../tests/functional/HtmlTest.php) | .php | class tests\units\HtmlTest extends DbTestCase |
| [tests/functional/IPAddressTest.php](../tests/functional/IPAddressTest.php) | .php | class tests\units\IPAddressTest extends DbTestCase |
| [tests/functional/ITILCategoryTest.php](../tests/functional/ITILCategoryTest.php) | .php | class tests\units\ITILCategoryTest extends DbTestCase |
| [tests/functional/ITILFollowupTemplateTest.php](../tests/functional/ITILFollowupTemplateTest.php) | .php | class tests\units\ITILFollowupTemplateTest extends AbstractITILChildTemplateTest |
| [tests/functional/ITILFollowupTest.php](../tests/functional/ITILFollowupTest.php) | .php | class tests\units\ITILFollowupTest extends DbTestCase |
| [tests/functional/ITILSolutionTest.php](../tests/functional/ITILSolutionTest.php) | .php | class tests\units\ITILSolutionTest extends DbTestCase |
| [tests/functional/ITILTemplateTest.php](../tests/functional/ITILTemplateTest.php) | .php | class tests\units\ITILTemplateTest extends DbTestCase |
| [tests/functional/ITILValidationTemplateTest.php](../tests/functional/ITILValidationTemplateTest.php) | .php | class tests\units\ITILValidationTemplateTest extends AbstractITILChildTemplateTest |
| [tests/functional/ImpactItemTest.php](../tests/functional/ImpactItemTest.php) | .php | class tests\units\ImpactItemTest extends DbTestCase |
| [tests/functional/ImpactRelationTest.php](../tests/functional/ImpactRelationTest.php) | .php | class tests\units\ImpactRelationTest extends DbTestCase |
| [tests/functional/ImpactTest.php](../tests/functional/ImpactTest.php) | .php | class tests\units\ImpactTest extends DbTestCase |
| [tests/functional/InfocomTest.php](../tests/functional/InfocomTest.php) | .php | class tests\units\InfocomTest extends DbTestCase |
| [tests/functional/ItemAntivirusTest.php](../tests/functional/ItemAntivirusTest.php) | .php | class tests\units\ItemAntivirusTest extends DbTestCase |
| [tests/functional/ItemVirtualMachineTest.php](../tests/functional/ItemVirtualMachineTest.php) | .php | class tests\units\ItemVirtualMachineTest extends DbTestCase |
| [tests/functional/Item_ClusterTest.php](../tests/functional/Item_ClusterTest.php) | .php | class tests\units\Item_ClusterTest extends DbTestCase |
| [tests/functional/Item_DeviceSensorTest.php](../tests/functional/Item_DeviceSensorTest.php) | .php | class tests\units\Item_DeviceSensorTest extends DbTestCase |
| [tests/functional/Item_DeviceSimcardTest.php](../tests/functional/Item_DeviceSimcardTest.php) | .php | class tests\units\Item_DeviceSimcardTest extends DbTestCase |
| [tests/functional/Item_DevicesTest.php](../tests/functional/Item_DevicesTest.php) | .php | class tests\units\Item_DevicesTest extends DbTestCase |
| [tests/functional/Item_DiskTest.php](../tests/functional/Item_DiskTest.php) | .php | class tests\units\Item_DiskTest extends DbTestCase |
| [tests/functional/Item_EnclosureTest.php](../tests/functional/Item_EnclosureTest.php) | .php | class tests\units\Item_EnclosureTest extends DbTestCase |
| [tests/functional/Item_EnvironmentTest.php](../tests/functional/Item_EnvironmentTest.php) | .php | class tests\units\Item_EnvironmentTest extends DbTestCase |
| [tests/functional/Item_LineTest.php](../tests/functional/Item_LineTest.php) | .php | class tests\units\Item_LineTest extends DbTestCase |
| [tests/functional/Item_OperatingSystemTest.php](../tests/functional/Item_OperatingSystemTest.php) | .php | class tests\units\Item_OperatingSystemTest extends DbTestCase |
| [tests/functional/Item_ProblemTest.php](../tests/functional/Item_ProblemTest.php) | .php | class tests\units\Item_ProblemTest extends AbstractCommonItilObject_ItemTest |
| [tests/functional/Item_ProcessTest.php](../tests/functional/Item_ProcessTest.php) | .php | class tests\units\Item_ProcessTest extends DbTestCase |
| [tests/functional/Item_ProjectTest.php](../tests/functional/Item_ProjectTest.php) | .php | class tests\units\Item_ProjectTest extends DbTestCase |
| [tests/functional/Item_RackTest.php](../tests/functional/Item_RackTest.php) | .php | class tests\units\Item_RackTest extends DbTestCase |
| [tests/functional/Item_RemoteManagementTest.php](../tests/functional/Item_RemoteManagementTest.php) | .php | class tests\units\Item_RemoteManagementTest extends DbTestCase |
| [tests/functional/Item_SoftwareLicenseTest.php](../tests/functional/Item_SoftwareLicenseTest.php) | .php | class tests\units\Item_SoftwareLicenseTest extends DbTestCase |
| [tests/functional/Item_SoftwareVersionTest.php](../tests/functional/Item_SoftwareVersionTest.php) | .php | class tests\units\Item_SoftwareVersionTest extends DbTestCase |
| [tests/functional/Item_TicketRecurrentTest.php](../tests/functional/Item_TicketRecurrentTest.php) | .php | class tests\units\Item_TicketRecurrentTest extends AbstractCommonItilObject_ItemTest |
| [tests/functional/Item_TicketTest.php](../tests/functional/Item_TicketTest.php) | .php | class tests\units\Item_TicketTest extends AbstractCommonItilObject_ItemTest |
| [tests/functional/Itil_ProjectTest.php](../tests/functional/Itil_ProjectTest.php) | .php | class tests\units\Itil_ProjectTest extends DbTestCase |
| [tests/functional/KnowbaseItemTargetUnicityTest.php](../tests/functional/KnowbaseItemTargetUnicityTest.php) | .php | class test\units\KnowbaseItemTargetUnicityTest extends DbTestCase |
| [tests/functional/KnowbaseItemTest.php](../tests/functional/KnowbaseItemTest.php) | .php | class test\units\KnowbaseItemTest extends DbTestCase |
| [tests/functional/KnowbaseItem_CommentTest.php](../tests/functional/KnowbaseItem_CommentTest.php) | .php | class tests\units\KnowbaseItem_CommentTest extends DbTestCase |
| [tests/functional/KnowbaseItem_FavoriteTest.php](../tests/functional/KnowbaseItem_FavoriteTest.php) | .php | class tests\units\KnowbaseItem_FavoriteTest extends DbTestCase |
| [tests/functional/KnowbaseItem_ItemTest.php](../tests/functional/KnowbaseItem_ItemTest.php) | .php | class test\units\KnowbaseItem_ItemTest extends DbTestCase |
| [tests/functional/KnowbaseItem_KnowbaseItemTest.php](../tests/functional/KnowbaseItem_KnowbaseItemTest.php) | .php | class test\units\KnowbaseItem_KnowbaseItemTest extends DbTestCase |
| [tests/functional/KnowbaseItem_RevisionTest.php](../tests/functional/KnowbaseItem_RevisionTest.php) | .php | class tests\units\KnowbaseItem_RevisionTest extends DbTestCase |
| [tests/functional/LineOperatorTest.php](../tests/functional/LineOperatorTest.php) | .php | class tests\units\LineOperatorTest extends DbTestCase |
| [tests/functional/LineTypeTest.php](../tests/functional/LineTypeTest.php) | .php | class tests\units\LineTypeTest extends DbTestCase |
| [tests/functional/LinkTest.php](../tests/functional/LinkTest.php) | .php | class tests\units\LinkTest extends DbTestCase |
| [tests/functional/LocationTest.php](../tests/functional/LocationTest.php) | .php | class tests\units\LocationTest extends DbTestCase |
| [tests/functional/LockedfieldTest.php](../tests/functional/LockedfieldTest.php) | .php | class tests\units\LockedfieldTest extends DbTestCase |
| [tests/functional/LogTest.php](../tests/functional/LogTest.php) | .php | class tests\units\LogTest extends DbTestCase |
| [tests/functional/ManualLinkTest.php](../tests/functional/ManualLinkTest.php) | .php | class tests\units\ManualLinkTest extends DbTestCase |
| [tests/functional/MassiveActionTest.php](../tests/functional/MassiveActionTest.php) | .php | class tests\units\MassiveActionTest extends DbTestCase |
| [tests/functional/MigrationTest.php](../tests/functional/MigrationTest.php) | .php | class tests\units\MigrationTest extends DbTestCase |
| [tests/functional/MonitorTest.php](../tests/functional/MonitorTest.php) | .php | class tests\units\MonitorTest extends DbTestCase |
| [tests/functional/NetworkEquipmentTest.php](../tests/functional/NetworkEquipmentTest.php) | .php | class tests\units\NetworkEquipmentTest extends DbTestCase |
| [tests/functional/NetworkNameTest.php](../tests/functional/NetworkNameTest.php) | .php | class tests\units\NetworkNameTest extends DbTestCase |
| [tests/functional/NetworkPortConnectionLogTest.php](../tests/functional/NetworkPortConnectionLogTest.php) | .php | class tests\units\NetworkPortConnectionLogTest extends DbTestCase |
| [tests/functional/NetworkPortMetricsTest.php](../tests/functional/NetworkPortMetricsTest.php) | .php | class tests\units\NetworkPortMetricsTest extends DbTestCase |
| [tests/functional/NetworkPortTest.php](../tests/functional/NetworkPortTest.php) | .php | class tests\units\NetworkPortTest extends DbTestCase |
| [tests/functional/NetworkPortTypeTest.php](../tests/functional/NetworkPortTypeTest.php) | .php | class tests\units\NetworkPortTypeTest extends DbTestCase |
| [tests/functional/NetworkPort_NetworkPortTest.php](../tests/functional/NetworkPort_NetworkPortTest.php) | .php | class tests\units\NetworkPort_NetworkPortTest extends DbTestCase |
| [tests/functional/NotificationAjaxSettingTest.php](../tests/functional/NotificationAjaxSettingTest.php) | .php | class tests\units\NotificationAjaxSettingTest extends DbTestCase |
| [tests/functional/NotificationAjaxTest.php](../tests/functional/NotificationAjaxTest.php) | .php | class tests\units\NotificationAjaxTest extends DbTestCase |
| [tests/functional/NotificationEventAjaxTest.php](../tests/functional/NotificationEventAjaxTest.php) | .php | class tests\units\NotificationEventAjaxTest extends DbTestCase |
| [tests/functional/NotificationEventMailingTest.php](../tests/functional/NotificationEventMailingTest.php) | .php | class tests\units\NotificationEventMailingTest extends DbTestCase |
| [tests/functional/NotificationEventTest.php](../tests/functional/NotificationEventTest.php) | .php | class tests\units\NotificationEventTest extends DbTestCase |
| [tests/functional/NotificationMailingSettingTest.php](../tests/functional/NotificationMailingSettingTest.php) | .php | class tests\units\NotificationMailingSettingTest extends DbTestCase |
| [tests/functional/NotificationMailingTest.php](../tests/functional/NotificationMailingTest.php) | .php | class tests\units\NotificationMailingTest extends DbTestCase |
| [tests/functional/NotificationSettingConfigTest.php](../tests/functional/NotificationSettingConfigTest.php) | .php | class tests\units\NotificationSettingConfigTest extends DbTestCase |
| [tests/functional/NotificationSettingInstanceTest.php](../tests/functional/NotificationSettingInstanceTest.php) | .php | class tests\units\NotificationSettingInstanceTest extends DbTestCase |
| [tests/functional/NotificationTargetKnowbaseItemTest.php](../tests/functional/NotificationTargetKnowbaseItemTest.php) | .php | class tests\units\NotificationTargetKnowbaseItemTest extends DbTestCase |
| [tests/functional/NotificationTargetProjectTaskTest.php](../tests/functional/NotificationTargetProjectTaskTest.php) | .php | class tests\units\NotificationTargetProjectTaskTest extends DbTestCase |
| [tests/functional/NotificationTargetSavedSearch_AlertTest.php](../tests/functional/NotificationTargetSavedSearch_AlertTest.php) | .php | class tests\units\NotificationTargetSavedSearch_AlertTest extends DbTestCase |
| [tests/functional/NotificationTargetTest.php](../tests/functional/NotificationTargetTest.php) | .php | class tests\units\NotificationTargetTest extends DbTestCase |
| [tests/functional/NotificationTargetTicketTest.php](../tests/functional/NotificationTargetTicketTest.php) | .php | class tests\units\NotificationTargetTicketTest extends DbTestCase |
| [tests/functional/NotificationTargetUserTest.php](../tests/functional/NotificationTargetUserTest.php) | .php | class tests\units\NotificationTargetUserTest extends DbTestCase |
| [tests/functional/NotificationTemplateTest.php](../tests/functional/NotificationTemplateTest.php) | .php | class tests\units\NotificationTemplateTest extends DbTestCase |
| [tests/functional/NotificationTemplateTranslationTest.php](../tests/functional/NotificationTemplateTranslationTest.php) | .php | class tests\units\NotificationTemplateTranslationTest extends DbTestCase |
| [tests/functional/NotificationTest.php](../tests/functional/NotificationTest.php) | .php | class tests\units\NotificationTest extends DbTestCase |
| [tests/functional/Notification_NotificationTemplateTest.php](../tests/functional/Notification_NotificationTemplateTest.php) | .php | class tests\units\Notification_NotificationTemplateTest extends DbTestCase |
| [tests/functional/OAuthClientTest.php](../tests/functional/OAuthClientTest.php) | .php | class tests\units\OAuthClientTest extends DbTestCase |
| [tests/functional/OLATest.php](../tests/functional/OLATest.php) | .php | class tests\units\OLATest extends DbTestCase |
| [tests/functional/ObjectLockTest.php](../tests/functional/ObjectLockTest.php) | .php | class tests\units\ObjectLockTest extends DbTestCase |
| [tests/functional/OperatingSystemArchitectureTest.php](../tests/functional/OperatingSystemArchitectureTest.php) | .php | class tests\units\OperatingSystemArchitectureTest extends CommonDropdownTest |
| [tests/functional/OperatingSystemEditionTest.php](../tests/functional/OperatingSystemEditionTest.php) | .php | class tests\units\OperatingSystemEditionTest extends CommonDropdownTest |
| [tests/functional/OperatingSystemKernelTest.php](../tests/functional/OperatingSystemKernelTest.php) | .php | class tests\units\OperatingSystemKernelTest extends CommonDropdownTest |
| [tests/functional/OperatingSystemKernelVersionTest.php](../tests/functional/OperatingSystemKernelVersionTest.php) | .php | class tests\units\OperatingSystemKernelVersionTest extends CommonDropdownTest |
| [tests/functional/OperatingSystemTest.php](../tests/functional/OperatingSystemTest.php) | .php | class tests\units\OperatingSystemTest extends CommonDropdownTest |
| [tests/functional/PCIVendorTest.php](../tests/functional/PCIVendorTest.php) | .php | class tests\units\PCIVendorTest extends DbTestCase |
| [tests/functional/PDU_RackTest.php](../tests/functional/PDU_RackTest.php) | .php | class tests\units\PDU_RackTest extends DbTestCase |
| [tests/functional/PassiveDCEquipmentTest.php](../tests/functional/PassiveDCEquipmentTest.php) | .php | class tests\units\PassiveDCEquipmentTest extends DbTestCase |
| [tests/functional/PasswordHistoryTest.php](../tests/functional/PasswordHistoryTest.php) | .php | class tests\units\PasswordHistoryTest extends DbTestCase |
| [tests/functional/PendingReasonTest.php](../tests/functional/PendingReasonTest.php) | .php | class tests\units\PendingReasonTest extends DbTestCase |
| [tests/functional/PlanningExternalEventTemplateTest.php](../tests/functional/PlanningExternalEventTemplateTest.php) | .php | class tests\units\PlanningExternalEventTemplateTest extends AbstractPlanningEventTest |
| [tests/functional/PlanningExternalEventTest.php](../tests/functional/PlanningExternalEventTest.php) | .php | class tests\units\PlanningExternalEventTest extends AbstractPlanningEventTest |
| [tests/functional/PlanningRecallTest.php](../tests/functional/PlanningRecallTest.php) | .php | class tests\units\PlanningRecallTest extends DbTestCase |
| [tests/functional/PlanningTest.php](../tests/functional/PlanningTest.php) | .php | class tests\units\PlanningTest extends DbTestCase |
| [tests/functional/PlugTest.php](../tests/functional/PlugTest.php) | .php | class tests\units\PlugTest extends DbTestCase |
| [tests/functional/PluginTest.php](../tests/functional/PluginTest.php) | .php | — |
| [tests/functional/PrinterLogTest.php](../tests/functional/PrinterLogTest.php) | .php | class tests\units\PrinterLogTest extends DbTestCase |
| [tests/functional/PrinterTest.php](../tests/functional/PrinterTest.php) | .php | class tests\units\PrinterTest extends DbTestCase |
| [tests/functional/Printer_CartridgeInfoTest.php](../tests/functional/Printer_CartridgeInfoTest.php) | .php | class tests\units\Printer_CartridgeInfoTest extends DbTestCase |
| [tests/functional/ProblemITILTemplateReadonlyFieldTest.php](../tests/functional/ProblemITILTemplateReadonlyFieldTest.php) | .php | class functional\ProblemITILTemplateReadonlyFieldTest extends AbstractITILTemplateReadonlyFieldTest |
| [tests/functional/ProblemTaskTest.php](../tests/functional/ProblemTaskTest.php) | .php | class tests\units\ProblemTaskTest extends CommonITILTaskTestCase |
| [tests/functional/ProblemTemplatePredefinedFieldTest.php](../tests/functional/ProblemTemplatePredefinedFieldTest.php) | .php | class tests\units\ProblemTemplatePredefinedFieldTest extends AbstractITILTemplatePredefinedFieldTest |
| [tests/functional/ProblemTest.php](../tests/functional/ProblemTest.php) | .php | class tests\units\ProblemTest extends DbTestCase |
| [tests/functional/ProfileRightTest.php](../tests/functional/ProfileRightTest.php) | .php | class tests\units\ProfileRightTest extends DbTestCase |
| [tests/functional/ProfileTest.php](../tests/functional/ProfileTest.php) | .php | class tests\units\ProfileTest extends DbTestCase |
| [tests/functional/Profile_UserTest.php](../tests/functional/Profile_UserTest.php) | .php | class tests\units\Profile_UserTest extends DbTestCase |
| [tests/functional/ProjectTaskLinkTest.php](../tests/functional/ProjectTaskLinkTest.php) | .php | class tests\units\ProjectTaskLinkTest extends DbTestCase |
| [tests/functional/ProjectTaskPlanningRecallTest.php](../tests/functional/ProjectTaskPlanningRecallTest.php) | .php | class tests\units\ProjectTaskPlanningRecallTest extends DbTestCase |
| [tests/functional/ProjectTaskTeamDropdownTest.php](../tests/functional/ProjectTaskTeamDropdownTest.php) | .php | class tests\units\ProjectTaskTeamDropdownTest extends DbTestCase |
| [tests/functional/ProjectTaskTest.php](../tests/functional/ProjectTaskTest.php) | .php | class tests\units\ProjectTaskTest extends DbTestCase |
| [tests/functional/ProjectTask_TicketTest.php](../tests/functional/ProjectTask_TicketTest.php) | .php | class tests\units\ProjectTask_TicketTest extends DbTestCase |
| [tests/functional/ProjectTeamTest.php](../tests/functional/ProjectTeamTest.php) | .php | class tests\units\ProjectTeamTest extends DbTestCase |
| [tests/functional/ProjectTest.php](../tests/functional/ProjectTest.php) | .php | class tests\units\ProjectTest extends DbTestCase |
| [tests/functional/PurgeLogsTest.php](../tests/functional/PurgeLogsTest.php) | .php | class tests\units\PurgeLogsTest extends DbTestCase |
| [tests/functional/PurgeSoftwareCronTest.php](../tests/functional/PurgeSoftwareCronTest.php) | .php | class tests\units\PurgeSoftwareCronTest extends DbTestCase |
| [tests/functional/QueuedNotificationTest.php](../tests/functional/QueuedNotificationTest.php) | .php | class tests\units\QueuedNotificationTest extends DbTestCase |
| [tests/functional/QueuedWebhookTest.php](../tests/functional/QueuedWebhookTest.php) | .php | class tests\units\QueuedWebhookTest extends DbTestCase |
| [tests/functional/RSSFeedTest.php](../tests/functional/RSSFeedTest.php) | .php | class tests\units\RSSFeedTest extends DbTestCase |
| [tests/functional/RecurrentChangeTest.php](../tests/functional/RecurrentChangeTest.php) | .php | class tests\units\RecurrentChangeTest extends CommonITILRecurrentTest |
| [tests/functional/ReminderTest.php](../tests/functional/ReminderTest.php) | .php | class tests\units\ReminderTest extends DbTestCase |
| [tests/functional/ReminderTranslationTest.php](../tests/functional/ReminderTranslationTest.php) | .php | class tests\units\ReminderTranslationTest extends DbTestCase |
| [tests/functional/ReportTest.php](../tests/functional/ReportTest.php) | .php | class tests\units\ReportTest extends DbTestCase |
| [tests/functional/ReservationTest.php](../tests/functional/ReservationTest.php) | .php | class tests\units\ReservationTest extends DbTestCase |
| [tests/functional/RuleAssetTest.php](../tests/functional/RuleAssetTest.php) | .php | class tests\units\RuleAssetTest extends DbTestCase |
| [tests/functional/RuleChangeTest.php](../tests/functional/RuleChangeTest.php) | .php | class tests\units\RuleChangeTest extends RuleCommonITILObjectTest |
| [tests/functional/RuleCriteriaTest.php](../tests/functional/RuleCriteriaTest.php) | .php | class tests\units\RuleCriteriaTest extends DbTestCase |
| [tests/functional/RuleDefineItemtypeCollectionTest.php](../tests/functional/RuleDefineItemtypeCollectionTest.php) | .php | class tests\units\RuleDefineItemtypeCollectionTest extends InventoryTestCase |
| [tests/functional/RuleDefineItemtypeTest.php](../tests/functional/RuleDefineItemtypeTest.php) | .php | class tests\units\RuleDefineItemtypeTest extends DbTestCase |
| [tests/functional/RuleDictionnaryPrinterModelCollectionTest.php](../tests/functional/RuleDictionnaryPrinterModelCollectionTest.php) | .php | class tests\units\RuleDictionnaryPrinterModelCollectionTest extends DbTestCase |
| [tests/functional/RuleDictionnaryPrinterModelTest.php](../tests/functional/RuleDictionnaryPrinterModelTest.php) | .php | class tests\units\RuleDictionnaryPrinterModelTest extends DbTestCase |
| [tests/functional/RuleDictionnarySoftwareCollectionTest.php](../tests/functional/RuleDictionnarySoftwareCollectionTest.php) | .php | class tests\units\RuleDictionnarySoftwareCollectionTest extends DbTestCase |
| [tests/functional/RuleDictionnarySoftwareTest.php](../tests/functional/RuleDictionnarySoftwareTest.php) | .php | class tests\units\RuleDictionnarySoftwareTest extends DbTestCase |
| [tests/functional/RuleImportAssetCollectionTest.php](../tests/functional/RuleImportAssetCollectionTest.php) | .php | class tests\units\RuleImportAssetCollectionTest extends InventoryTestCase |
| [tests/functional/RuleImportAssetTest.php](../tests/functional/RuleImportAssetTest.php) | .php | class tests\units\RuleImportAssetTest extends DbTestCase |
| [tests/functional/RuleImportEntityTest.php](../tests/functional/RuleImportEntityTest.php) | .php | class tests\units\RuleImportEntityTest extends DbTestCase |
| [tests/functional/RuleLocationTest.php](../tests/functional/RuleLocationTest.php) | .php | class tests\units\RuleLocationTest extends DbTestCase |
| [tests/functional/RuleMailCollectorTest.php](../tests/functional/RuleMailCollectorTest.php) | .php | class tests\units\RuleMailCollectorTest extends DbTestCase |
| [tests/functional/RuleMatchedLogTest.php](../tests/functional/RuleMatchedLogTest.php) | .php | class tests\units\RuleMatchedLogTest extends DbTestCase |
| [tests/functional/RuleProblemTest.php](../tests/functional/RuleProblemTest.php) | .php | class tests\units\RuleProblemTest extends RuleCommonITILObjectTest |
| [tests/functional/RuleRightCollectionTest.php](../tests/functional/RuleRightCollectionTest.php) | .php | class tests\units\RuleRightCollectionTest extends DbTestCase |
| [tests/functional/RuleRightTest.php](../tests/functional/RuleRightTest.php) | .php | class tests\units\RuleRightTest extends DbTestCase |
| [tests/functional/RuleSoftwareCategoryCollectionTest.php](../tests/functional/RuleSoftwareCategoryCollectionTest.php) | .php | class tests\units\RuleSoftwareCategoryCollectionTest extends DbTestCase |
| [tests/functional/RuleSoftwareCategoryTest.php](../tests/functional/RuleSoftwareCategoryTest.php) | .php | class tests\units\RuleSoftwareCategoryTest extends DbTestCase |
| [tests/functional/RuleTest.php](../tests/functional/RuleTest.php) | .php | class tests\units\RuleTest extends DbTestCase |
| [tests/functional/RuleTicketTest.php](../tests/functional/RuleTicketTest.php) | .php | class tests\units\RuleTicketTest extends RuleCommonITILObjectTest |
| [tests/functional/SLMTest.php](../tests/functional/SLMTest.php) | .php | class tests\units\SLMTest extends DbTestCase |
| [tests/functional/SavedSearchTest.php](../tests/functional/SavedSearchTest.php) | .php | class tests\units\SavedSearchTest extends DbTestCase |
| [tests/functional/SavedSearch_UserTest.php](../tests/functional/SavedSearch_UserTest.php) | .php | class tests\units\SavedSearch_UserTest extends DbTestCase |
| [tests/functional/SearchTest.php](../tests/functional/SearchTest.php) | .php | class tests\units\SearchTest extends DbTestCase |
| [tests/functional/SessionTest.php](../tests/functional/SessionTest.php) | .php | class tests\units\SessionTest extends DbTestCase |
| [tests/functional/ShareDashboardDropdownTest.php](../tests/functional/ShareDashboardDropdownTest.php) | .php | class tests\units\ShareDashboardDropdownTest extends AbstractRightsDropdownTest |
| [tests/functional/SlaLevel_TicketTest.php](../tests/functional/SlaLevel_TicketTest.php) | .php | class tests\units\SlaLevel_TicketTest extends DbTestCase |
| [tests/functional/SlaProgressBarTest.php](../tests/functional/SlaProgressBarTest.php) | .php | class tests\units\SlaProgressBarTest extends DbTestCase |
| [tests/functional/SoftwareLicenseTest.php](../tests/functional/SoftwareLicenseTest.php) | .php | class tests\units\SoftwareLicenseTest extends DbTestCase |
| [tests/functional/SoftwareTest.php](../tests/functional/SoftwareTest.php) | .php | class tests\units\SoftwareTest extends DbTestCase |
| [tests/functional/SoftwareVersionTest.php](../tests/functional/SoftwareVersionTest.php) | .php | class tests\units\SoftwareVersionTest extends DbTestCase |
| [tests/functional/SolutionTemplateTest.php](../tests/functional/SolutionTemplateTest.php) | .php | class tests\units\SolutionTemplateTest extends AbstractITILChildTemplateTest |
| [tests/functional/SsoVariableTest.php](../tests/functional/SsoVariableTest.php) | .php | class tests\units\SsoVariableTest extends DbTestCase |
| [tests/functional/StatTest.php](../tests/functional/StatTest.php) | .php | class tests\units\StatTest extends DbTestCase |
| [tests/functional/StateTest.php](../tests/functional/StateTest.php) | .php | class tests\units\StateTest extends DbTestCase |
| [tests/functional/SupplierTest.php](../tests/functional/SupplierTest.php) | .php | class tests\units\SupplierTest extends DbTestCase |
| [tests/functional/TaskTemplateTest.php](../tests/functional/TaskTemplateTest.php) | .php | class tests\units\TaskTemplateTest extends AbstractITILChildTemplateTest |
| [tests/functional/TelemetryTest.php](../tests/functional/TelemetryTest.php) | .php | class tests\units\TelemetryTest extends DbTestCase |
| [tests/functional/TicketCostTest.php](../tests/functional/TicketCostTest.php) | .php | class tests\units\TicketCostTest extends DbTestCase |
| [tests/functional/TicketITILTemplateReadonlyFieldTest.php](../tests/functional/TicketITILTemplateReadonlyFieldTest.php) | .php | class functional\TicketITILTemplateReadonlyFieldTest extends AbstractITILTemplateReadonlyFieldTest |
| [tests/functional/TicketRecurrentTest.php](../tests/functional/TicketRecurrentTest.php) | .php | class tests\units\TicketRecurrentTest extends CommonITILRecurrentTest |
| [tests/functional/TicketSatisfactionTest.php](../tests/functional/TicketSatisfactionTest.php) | .php | class tests\units\TicketSatisfactionTest extends CommonITILSatisfactionTest |
| [tests/functional/TicketTaskTest.php](../tests/functional/TicketTaskTest.php) | .php | class tests\units\TicketTaskTest extends CommonITILTaskTestCase |
| [tests/functional/TicketTemplatePredefinedFieldTest.php](../tests/functional/TicketTemplatePredefinedFieldTest.php) | .php | class tests\units\TicketTemplatePredefinedFieldTest extends AbstractITILTemplatePredefinedFieldTest |
| [tests/functional/TicketTest.php](../tests/functional/TicketTest.php) | .php | class tests\units\TicketTest extends DbTestCase |
| [tests/functional/TicketValidationTest.php](../tests/functional/TicketValidationTest.php) | .php | class tests\units\TicketValidationTest extends CommonITILValidationTest |
| [tests/functional/Ticket_TicketTest.php](../tests/functional/Ticket_TicketTest.php) | .php | class tests\units\Ticket_TicketTest extends DbTestCase |
| [tests/functional/ToolboxTest.php](../tests/functional/ToolboxTest.php) | .php | class tests\units\ToolboxTest extends DbTestCase |
| [tests/functional/Tools/Command/CheckDecorativeIconsCommandTest.php](../tests/functional/Tools/Command/CheckDecorativeIconsCommandTest.php) | .php | class tests\functional\Tools\Command\CheckDecorativeIconsCommandTest extends GLPITestCase |
| [tests/functional/Tools/Command/LicenceHeadersCheckCommandTest.php](../tests/functional/Tools/Command/LicenceHeadersCheckCommandTest.php) | .php | class tests\functional\Tools\Command\LicenceHeadersCheckCommandTest extends GLPITestCase |
| [tests/functional/Tools/Command/LocalesExtractCommandTest.php](../tests/functional/Tools/Command/LocalesExtractCommandTest.php) | .php | class tests\functional\Tools\Command\LocalesExtractCommandTest extends GLPITestCase |
| [tests/functional/TransferTest.php](../tests/functional/TransferTest.php) | .php | class tests\units\TransferTest extends DbTestCase |
| [tests/functional/Twig/Components/Alert/AlertRenderingTest.php](../tests/functional/Twig/Components/Alert/AlertRenderingTest.php) | .php | class tests\units\Twig\Components\Alert\AlertRenderingTest extends GLPITestCase |
| [tests/functional/Twig/Components/Alert/AlertTest.php](../tests/functional/Twig/Components/Alert/AlertTest.php) | .php | class tests\units\Twig\Components\Alert\AlertTest extends TestCase |
| [tests/functional/USBVendorTest.php](../tests/functional/USBVendorTest.php) | .php | class tests\units\USBVendorTest extends DbTestCase |
| [tests/functional/UnmanagedTest.php](../tests/functional/UnmanagedTest.php) | .php | class tests\units\UnmanagedTest extends DbTestCase |
| [tests/functional/UpdateTest.php](../tests/functional/UpdateTest.php) | .php | class tests\units\UpdateTest extends GLPITestCase |
| [tests/functional/UserEmailTest.php](../tests/functional/UserEmailTest.php) | .php | class tests\units\UserEmailTest extends DbTestCase |
| [tests/functional/UserTest.php](../tests/functional/UserTest.php) | .php | class tests\units\UserTest extends DbTestCase |
| [tests/functional/ValidationStepTest.php](../tests/functional/ValidationStepTest.php) | .php | class tests\units\ValidationStepTest extends DbTestCase |
| [tests/functional/ValidatorSubstituteTest.php](../tests/functional/ValidatorSubstituteTest.php) | .php | class tests\units\ValidatorSubstituteTest extends DbTestCase |
| [tests/functional/WebhookTest.php](../tests/functional/WebhookTest.php) | .php | class tests\units\WebhookTest extends DbTestCase |
| [tests/functional/autoload/MiscFunctionsTest.php](../tests/functional/autoload/MiscFunctionsTest.php) | .php | class tests\units\autoload\MiscFunctionsTest extends DbTestCase |
| [tests/glpi-0.85.5-empty.sql](../tests/glpi-0.85.5-empty.sql) | .sql | — |
| [tests/glpi-9.5-data.sql](../tests/glpi-9.5-data.sql) | .sql | — |
| [tests/glpi-formcreator-migration-data.sql](../tests/glpi-formcreator-migration-data.sql) | .sql | — |
| [tests/imap/MailCollectorAnonymousCreationTest.php](../tests/imap/MailCollectorAnonymousCreationTest.php) | .php | class tests\units\MailCollectorAnonymousCreationTest extends DbTestCase |
| [tests/imap/MailCollectorTest.php](../tests/imap/MailCollectorTest.php) | .php | class tests\units\MailCollectorTest extends DbTestCase |
| [tests/imap/MailReAuthStrategyTest.php](../tests/imap/MailReAuthStrategyTest.php) | .php | class tests\units\MailReAuthStrategyTest extends DbTestCase |
| [tests/js/bootstrap.mjs](../tests/js/bootstrap.mjs) | .mjs | — |
| [tests/js/cable.test.js](../tests/js/cable.test.js) | .js | — |
| [tests/js/common.test.js](../tests/js/common.test.js) | .js | — |
| [tests/js/fetch-mock.js](../tests/js/fetch-mock.js) | .js | — |
| [tests/js/impact.test.js](../tests/js/impact.test.js) | .js | — |
| [tests/js/modules/Dashboard/Dashboard.spec.js](../tests/js/modules/Dashboard/Dashboard.spec.js) | .js | — |
| [tests/js/modules/Form/WebIconSelector.spec.js](../tests/js/modules/Form/WebIconSelector.spec.js) | .js | — |
| [tests/js/modules/Forms/RendererController.test.js](../tests/js/modules/Forms/RendererController.test.js) | .js | — |
| [tests/js/modules/ObjectLock.spec.js](../tests/js/modules/ObjectLock.spec.js) | .js | — |
| [tests/js/modules/Screenshot/Screenshot.spec.js](../tests/js/modules/Screenshot/Screenshot.spec.js) | .js | — |
| [tests/js/modules/Search/ResultsView.spec.js](../tests/js/modules/Search/ResultsView.spec.js) | .js | — |
| [tests/js/modules/Search/Table.spec.js](../tests/js/modules/Search/Table.spec.js) | .js | — |
| [tests/js/modules/SearchTokenizer/SearchInput.spec.js](../tests/js/modules/SearchTokenizer/SearchInput.spec.js) | .js | — |
| [tests/js/modules/SearchTokenizer/SearchTokenizer.spec.js](../tests/js/modules/SearchTokenizer/SearchTokenizer.spec.js) | .js | — |
| [tests/js/modules/Security/MfaCodeInput.spec.js](../tests/js/modules/Security/MfaCodeInput.spec.js) | .js | — |
| [tests/js/modules/UserMention/UserMention.spec.js](../tests/js/modules/UserMention/UserMention.spec.js) | .js | — |
| [tests/js/rack.test.js](../tests/js/rack.test.js) | .js | — |
| [tests/js/vue/Debug/Toolbar.spec.js](../tests/js/vue/Debug/Toolbar.spec.js) | .js | — |
| [tests/js/vue/EntitySelector/EntitySelector.spec.js](../tests/js/vue/EntitySelector/EntitySelector.spec.js) | .js | — |
| [tests/js/vue/FuzzySearch/Modal.spec.js](../tests/js/vue/FuzzySearch/Modal.spec.js) | .js | — |
| [tests/js/vue/Kanban/Kanban.spec.js](../tests/js/vue/Kanban/Kanban.spec.js) | .js | — |
| [tests/js/vue/Planning/PlanningEvent.test.js](../tests/js/vue/Planning/PlanningEvent.test.js) | .js | — |
| [tests/js/vue/Planning/PlanningFiltersPanel.test.js](../tests/js/vue/Planning/PlanningFiltersPanel.test.js) | .js | — |
| [tests/js/vue/Planning/PlanningScheduler.test.js](../tests/js/vue/Planning/PlanningScheduler.test.js) | .js | — |
| [tests/js/vue/Planning/PlanningView.test.js](../tests/js/vue/Planning/PlanningView.test.js) | .js | — |
| [tests/js/webpack-config.test.js](../tests/js/webpack-config.test.js) | .js | — |
| [tests/local_en_GB.mo](../tests/local_en_GB.mo) | .mo | — |
| [tests/local_en_GB.po](../tests/local_en_GB.po) | .po | — |
| [tests/router.php](../tests/router.php) | .php | — |
| [tests/run_tests.sh](../tests/run_tests.sh) | .sh | — |
| [tests/src/AbstractActorFieldTest.php](../tests/src/AbstractActorFieldTest.php) | .php | class Glpi\Tests\AbstractActorFieldTest extends AbstractDestinationFieldTest |
| [tests/src/AbstractCommonItilObject_ItemTest.php](../tests/src/AbstractCommonItilObject_ItemTest.php) | .php | class Glpi\Tests\AbstractCommonItilObject_ItemTest extends DbTestCase |
| [tests/src/AbstractConditionHandlerTest.php](../tests/src/AbstractConditionHandlerTest.php) | .php | class Glpi\Tests\AbstractConditionHandlerTest extends DbTestCase |
| [tests/src/AbstractDestinationFieldTest.php](../tests/src/AbstractDestinationFieldTest.php) | .php | class Glpi\Tests\AbstractDestinationFieldTest extends DbTestCase |
| [tests/src/AbstractITILChildTemplateTest.php](../tests/src/AbstractITILChildTemplateTest.php) | .php | class Glpi\Tests\AbstractITILChildTemplateTest extends DbTestCase |
| [tests/src/AbstractITILTemplatePredefinedFieldTest.php](../tests/src/AbstractITILTemplatePredefinedFieldTest.php) | .php | class Glpi\Tests\AbstractITILTemplatePredefinedFieldTest extends DbTestCase |
| [tests/src/AbstractITILTemplateReadonlyFieldTest.php](../tests/src/AbstractITILTemplateReadonlyFieldTest.php) | .php | class Glpi\Tests\AbstractITILTemplateReadonlyFieldTest extends DbTestCase |
| [tests/src/AbstractInventoryAsset.php](../tests/src/AbstractInventoryAsset.php) | .php | class Glpi\Tests\AbstractInventoryAsset extends InventoryTestCase |
| [tests/src/AbstractParametersTest.php](../tests/src/AbstractParametersTest.php) | .php | class Glpi\Tests\AbstractParametersTest extends DbTestCase |
| [tests/src/AbstractPlanningEventTest.php](../tests/src/AbstractPlanningEventTest.php) | .php | class Glpi\Tests\AbstractPlanningEventTest extends DbTestCase |
| [tests/src/AbstractRightsDropdownTest.php](../tests/src/AbstractRightsDropdownTest.php) | .php | class Glpi\Tests\AbstractRightsDropdownTest extends GLPITestCase |
| [tests/src/AbstractTileRightsTest.php](../tests/src/AbstractTileRightsTest.php) | .php | class Glpi\Tests\AbstractTileRightsTest extends DbTestCase |
| [tests/src/Api/Deprecated/ComputerAntivirus.php](../tests/src/Api/Deprecated/ComputerAntivirus.php) | .php | class Glpi\Tests\Api\Deprecated\ComputerAntivirus |
| [tests/src/Api/Deprecated/ComputerVirtualMachine.php](../tests/src/Api/Deprecated/ComputerVirtualMachine.php) | .php | class Glpi\Tests\Api\Deprecated\ComputerVirtualMachine |
| [tests/src/Api/Deprecated/Computer_Item.php](../tests/src/Api/Deprecated/Computer_Item.php) | .php | class Glpi\Tests\Api\Deprecated\Computer_Item |
| [tests/src/Api/Deprecated/Computer_SoftwareLicense.php](../tests/src/Api/Deprecated/Computer_SoftwareLicense.php) | .php | class Glpi\Tests\Api\Deprecated\Computer_SoftwareLicense |
| [tests/src/Api/Deprecated/Computer_SoftwareVersion.php](../tests/src/Api/Deprecated/Computer_SoftwareVersion.php) | .php | class Glpi\Tests\Api\Deprecated\Computer_SoftwareVersion |
| [tests/src/Api/Deprecated/DeprecatedInterface.php](../tests/src/Api/Deprecated/DeprecatedInterface.php) | .php | interface Glpi\Tests\Api\Deprecated\DeprecatedInterface |
| [tests/src/Api/Deprecated/TicketFollowup.php](../tests/src/Api/Deprecated/TicketFollowup.php) | .php | class Glpi\Tests\Api\Deprecated\TicketFollowup |
| [tests/src/Command/TestUpdatedDataCommand.php](../tests/src/Command/TestUpdatedDataCommand.php) | .php | class Glpi\Tests\Command\TestUpdatedDataCommand extends Command |
| [tests/src/CommonDropdownTest.php](../tests/src/CommonDropdownTest.php) | .php | class Glpi\Tests\CommonDropdownTest extends DbTestCase |
| [tests/src/CommonITILRecurrentTest.php](../tests/src/CommonITILRecurrentTest.php) | .php | class Glpi\Tests\CommonITILRecurrentTest extends DbTestCase |
| [tests/src/CommonITILSatisfactionTest.php](../tests/src/CommonITILSatisfactionTest.php) | .php | class Glpi\Tests\CommonITILSatisfactionTest extends DbTestCase |
| [tests/src/CommonITILTaskTestCase.php](../tests/src/CommonITILTaskTestCase.php) | .php | class Glpi\Tests\CommonITILTaskTestCase extends DbTestCase |
| [tests/src/CommonITILValidationTest.php](../tests/src/CommonITILValidationTest.php) | .php | class Glpi\Tests\CommonITILValidationTest extends DbTestCase |
| [tests/src/Controller/PlanningFixturesController.php](../tests/src/Controller/PlanningFixturesController.php) | .php | class Glpi\Tests\Controller\PlanningFixturesController |
| [tests/src/Controller/Security/ReAuthTestController.php](../tests/src/Controller/Security/ReAuthTestController.php) | .php | class Glpi\Tests\Controller\Security\ReAuthTestController extends AbstractController |
| [tests/src/Controller/Tabler/TablerIconController.php](../tests/src/Controller/Tabler/TablerIconController.php) | .php | class Glpi\Tests\Controller\Tabler\TablerIconController extends AbstractController |
| [tests/src/CsvTestCase.php](../tests/src/CsvTestCase.php) | .php | class Glpi\Tests\CsvTestCase extends DbTestCase |
| [tests/src/DbTestCase.php](../tests/src/DbTestCase.php) | .php | class Glpi\Tests\DbTestCase extends GLPITestCase |
| [tests/src/Form/Destination/AbstractCommonITILFormDestinationType.php](../tests/src/Form/Destination/AbstractCommonITILFormDestinationType.php) | .php | class Glpi\Tests\Form\Destination\AbstractCommonITILFormDestinationType extends DbTestCase |
| [tests/src/Form/QuestionType/AbstractQuestionTypeSelectableTest.php](../tests/src/Form/QuestionType/AbstractQuestionTypeSelectableTest.php) | .php | class Glpi\Tests\Form\QuestionType\AbstractQuestionTypeSelectableTest extends DbTestCase |
| [tests/src/FormBuilder.php](../tests/src/FormBuilder.php) | .php | class Glpi\Tests\FormBuilder |
| [tests/src/FormTesterTrait.php](../tests/src/FormTesterTrait.php) | .php | trait Glpi\Tests\FormTesterTrait |
| [tests/src/FrontBaseClass.php](../tests/src/FrontBaseClass.php) | .php | class Glpi\Tests\FrontBaseClass extends GLPITestCase |
| [tests/src/GLPITestCase.php](../tests/src/GLPITestCase.php) | .php | class Glpi\Tests\GLPITestCase extends TestCase |
| [tests/src/Glpi/Asset/CapacityUsageTestTrait.php](../tests/src/Glpi/Asset/CapacityUsageTestTrait.php) | .php | trait Glpi\Tests\Glpi\Asset\CapacityUsageTestTrait |
| [tests/src/Glpi/Asset/ProviderTrait.php](../tests/src/Glpi/Asset/ProviderTrait.php) | .php | trait Glpi\Tests\Glpi\Asset\ProviderTrait |
| [tests/src/Glpi/Auth/HelpersTrait.php](../tests/src/Glpi/Auth/HelpersTrait.php) | .php | trait Glpi\Tests\Glpi\Auth\HelpersTrait |
| [tests/src/Glpi/Form/QuestionType/AbstractQuestionTypeActorsTest.php](../tests/src/Glpi/Form/QuestionType/AbstractQuestionTypeActorsTest.php) | .php | class Glpi\Tests\Glpi\Form\QuestionType\AbstractQuestionTypeActorsTest extends DbTestCase |
| [tests/src/Glpi/ITILTrait.php](../tests/src/Glpi/ITILTrait.php) | .php | trait Glpi\Tests\Glpi\ITILTrait |
| [tests/src/Glpi/SLMTrait.php](../tests/src/Glpi/SLMTrait.php) | .php | trait Glpi\Tests\Glpi\SLMTrait |
| [tests/src/Glpi/Security/ReAuth/ReAuthTrait.php](../tests/src/Glpi/Security/ReAuth/ReAuthTrait.php) | .php | trait Glpi\Tests\Glpi\Security\ReAuth\ReAuthTrait |
| [tests/src/Glpi/ValidationStepTrait.php](../tests/src/Glpi/ValidationStepTrait.php) | .php | trait Glpi\Tests\Glpi\ValidationStepTrait |
| [tests/src/HLAPITestCase.php](../tests/src/HLAPITestCase.php) | .php | class Glpi\Tests\HLAPITestCase extends DbTestCase |
| [tests/src/InventoryTestCase.php](../tests/src/InventoryTestCase.php) | .php | class Glpi\Tests\InventoryTestCase extends DbTestCase |
| [tests/src/Log/TestHandler.php](../tests/src/Log/TestHandler.php) | .php | class Glpi\Tests\Log\TestHandler extends BaseTestHandler |
| [tests/src/RuleBuilder.php](../tests/src/RuleBuilder.php) | .php | class Glpi\Tests\RuleBuilder |
| [tests/src/RuleCommonITILObjectTest.php](../tests/src/RuleCommonITILObjectTest.php) | .php | class Glpi\Tests\RuleCommonITILObjectTest extends DbTestCase |
| [tests/src/SortStrategyTestCase.php](../tests/src/SortStrategyTestCase.php) | .php | class Glpi\Tests\SortStrategyTestCase extends DbTestCase |
| [tests/src/autoload/functions.php](../tests/src/autoload/functions.php) | .php | — |
| [tests/templates/tabler/icons.html.twig](../tests/templates/tabler/icons.html.twig) | .twig | — |
| [tests/test_picture.png](../tests/test_picture.png) | .png | — |
| [tests/web/APIRestTest.php](../tests/web/APIRestTest.php) | .php | class tests\units\Glpi\Api\APIRestTest extends TestCase |
| [tests/web/ApiDetectionTest.php](../tests/web/ApiDetectionTest.php) | .php | class tests\units\ApiDetectionTest extends FrontBaseClass |
| [tests/web/ComputerTest.php](../tests/web/ComputerTest.php) | .php | class tests\units\ComputerTest extends FrontBaseClass |
| [tests/web/Glpi/Inventory/InventoryTest.php](../tests/web/Glpi/Inventory/InventoryTest.php) | .php | class tests\units\Glpi\Inventory\InventoryTest extends GLPITestCase |
| [tests/web/Glpi/Inventory/RequestTest.php](../tests/web/Glpi/Inventory/RequestTest.php) | .php | class tests\units\Glpi\Inventory\RequestTest extends TestCase |
| [tests/web/Glpi/RoutingTest.php](../tests/web/Glpi/RoutingTest.php) | .php | class tests\units\Glpi\RoutingTest extends FrontBaseClass |
| [tests/web/README.md](../tests/web/README.md) | .md | — |
| [tests/web/SNMPCredentialTest.php](../tests/web/SNMPCredentialTest.php) | .php | class tests\units\SNMPCredentialTest extends FrontBaseClass |
| [tests/web/TelemetryTest.php](../tests/web/TelemetryTest.php) | .php | class tests\units\TelemetryTest extends DbTestCase |
| [tests/web/TicketTest.php](../tests/web/TicketTest.php) | .php | class tests\units\TicketTest extends FrontBaseClass |

## tools


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [tools/HEADER](../tools/HEADER) | sem extensão | — |
| [tools/bin/check-twig-templates-syntax](../tools/bin/check-twig-templates-syntax) | sem extensão | — |
| [tools/build_fonts.sh](../tools/build_fonts.sh) | .sh | — |
| [tools/build_glpi.sh](../tools/build_glpi.sh) | .sh | — |
| [tools/cachebench.php](../tools/cachebench.php) | .php | — |
| [tools/fake_metrics.php](../tools/fake_metrics.php) | .php | — |
| [tools/fk_generate.php](../tools/fk_generate.php) | .php | — |
| [tools/getsearchoptions.php](../tools/getsearchoptions.php) | .php | — |
| [tools/github-nightly-description.sh](../tools/github-nightly-description.sh) | .sh | — |
| [tools/inventory.php](../tools/inventory.php) | .php | — |
| [tools/make_release.sh](../tools/make_release.sh) | .sh | — |
| [tools/patches/guzzlehttp-guzzle-restrict-http-methods.patch](../tools/patches/guzzlehttp-guzzle-restrict-http-methods.patch) | .patch | — |
| [tools/patches/laminas-laminas-mail-invalid-header-ignore.patch](../tools/patches/laminas-laminas-mail-invalid-header-ignore.patch) | .patch | — |
| [tools/patches/npm/gettext.js+2.0.3.patch](../tools/patches/npm/gettext.js+2.0.3.patch) | .patch | — |
| [tools/patches/symfony-http-client-no-private-network-allow-list.patch](../tools/patches/symfony-http-client-no-private-network-allow-list.patch) | .patch | — |
| [tools/src/Command/AbstractCommand.php](../tools/src/Command/AbstractCommand.php) | .php | class Glpi\Tools\Command\AbstractCommand extends Command |
| [tools/src/Command/CheckDatabaseKeysCommand.php](../tools/src/Command/CheckDatabaseKeysCommand.php) | .php | class Glpi\Tools\Command\CheckDatabaseKeysCommand extends AbstractCommand |
| [tools/src/Command/CheckDatabaseSchemaConsistencyCommand.php](../tools/src/Command/CheckDatabaseSchemaConsistencyCommand.php) | .php | class Glpi\Tools\Command\CheckDatabaseSchemaConsistencyCommand extends AbstractCommand |
| [tools/src/Command/CheckDecorativeIconsCommand.php](../tools/src/Command/CheckDecorativeIconsCommand.php) | .php | class Glpi\Tools\Command\CheckDecorativeIconsCommand extends AbstractCommand |
| [tools/src/Command/CheckTwigTemplatesSyntaxCommand.php](../tools/src/Command/CheckTwigTemplatesSyntaxCommand.php) | .php | class Glpi\Tools\Command\CheckTwigTemplatesSyntaxCommand extends Command |
| [tools/src/Command/CreateDevLdapCommand.php](../tools/src/Command/CreateDevLdapCommand.php) | .php | class Glpi\Tools\Command\CreateDevLdapCommand extends AbstractCommand |
| [tools/src/Command/DeleteOrphanLogsCommand.php](../tools/src/Command/DeleteOrphanLogsCommand.php) | .php | class Glpi\Tools\Command\DeleteOrphanLogsCommand extends AbstractCommand |
| [tools/src/Command/GenerateAPISnapshotCommand.php](../tools/src/Command/GenerateAPISnapshotCommand.php) | .php | class Glpi\Tools\Command\GenerateAPISnapshotCommand extends AbstractCommand |
| [tools/src/Command/GenerateFormForeachIllustrationsCommand.php](../tools/src/Command/GenerateFormForeachIllustrationsCommand.php) | .php | class Glpi\Tools\Command\GenerateFormForeachIllustrationsCommand extends AbstractCommand |
| [tools/src/Command/GenerateHooksDocumentationCommand.php](../tools/src/Command/GenerateHooksDocumentationCommand.php) | .php | class Glpi\Tools\Command\GenerateHooksDocumentationCommand extends AbstractCommand |
| [tools/src/Command/GenerateIllustrationTranslationFileCommand.php](../tools/src/Command/GenerateIllustrationTranslationFileCommand.php) | .php | class Glpi\Tools\Command\GenerateIllustrationTranslationFileCommand extends Command |
| [tools/src/Command/GenerateKnowbaseItemsCommand.php](../tools/src/Command/GenerateKnowbaseItemsCommand.php) | .php | class Glpi\Tools\Command\GenerateKnowbaseItemsCommand extends AbstractCommand |
| [tools/src/Command/LicenceHeadersCheckCommand.php](../tools/src/Command/LicenceHeadersCheckCommand.php) | .php | class Glpi\Tools\Command\LicenceHeadersCheckCommand extends AbstractCommand |
| [tools/src/Command/LocalesCompileCommand.php](../tools/src/Command/LocalesCompileCommand.php) | .php | class Glpi\Tools\Command\LocalesCompileCommand extends AbstractCommand |
| [tools/src/Command/LocalesExtractCommand.php](../tools/src/Command/LocalesExtractCommand.php) | .php | class Glpi\Tools\Command\LocalesExtractCommand extends AbstractCommand |
| [tools/src/GlpiTwigRuleset.php](../tools/src/GlpiTwigRuleset.php) | .php | class Glpi\Tools\GlpiTwigRuleset extends Official |
| [tools/src/Plugin/Command/AbstractPluginCommand.php](../tools/src/Plugin/Command/AbstractPluginCommand.php) | .php | class Glpi\Tools\Plugin\Command\AbstractPluginCommand extends AbstractCommand |
| [tools/src/Plugin/Command/PluginReleaseCommand.php](../tools/src/Plugin/Command/PluginReleaseCommand.php) | .php | class Glpi\Tools\Plugin\Command\PluginReleaseCommand extends AbstractPluginCommand |
| [tools/testmail.php](../tools/testmail.php) | .php | — |
| [tools/update_registered_ids.php](../tools/update_registered_ids.php) | .php | — |

## version


| Arquivo | Extensão | Declaração principal |
| --- | --- | --- |
| [version/12.0.2](../version/12.0.2) | .2 | — |
