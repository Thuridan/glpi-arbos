# Comandos CLI disponíveis em Dev

Extraído de `php bin/console list --format=json`. A disponibilidade em Prod difere porque a imagem exclui `tools/` e usa autoload sem desenvolvimento.

Este documento lista comandos; não os executa. Comandos de instalação, atualização, limpeza e migração alteram estado. Consulte `php bin/console <comando> --help` e as condições do fluxo Dev/Prod antes de executá-los.

| Comando | Aliases | Descrição |
| --- | --- | --- |
| _complete |  | Internal command to provide shell completion suggestions |
| assets:cleansoftware |  | Remove software versions with no installation and software with no version |
| assets:purgesoftware |  | Purge software with no version that are deleted. |
| build:compile_scss |  | Compile SCSS file. |
| build:generate_code_manifest |  | Generate GLPI source code manifest that could be used to validate source code integrity. |
| cache:clear |  | Clear GLPI cache. |
| cache:configure |  | Define cache configuration |
| cache:debug |  | Debug GLPI cache. |
| cache:set_namespace_prefix |  | Define cache namespace prefix |
| completion |  | Dump the shell completion script |
| config:set |  | Set configuration value |
| database:check_schema_integrity |  | Check for schema differences between current database and installation file. |
| database:configure |  | Define database configuration and writes it to the configuration file |
| database:enable_timezones |  | Enable timezones usage. |
| database:install |  | Install database schema |
| database:is_up_to_date |  | Check if the database schema version matches the installed GLPI version. |
| database:update |  | Update database schema to new version |
| diagnostic:check_documents_integrity |  | Validate files integrity for GLPI's documents. |
| diagnostic:check_orphaned_user_pictures |  | Check user picture references that no longer exist on the filesystem. |
| diagnostic:check_source_code_integrity |  | Check GLPI source code file integrity. |
| help |  | Display help for a command |
| ldap:synchronize_users |  | Synchronize users against LDAP server information |
| list |  | List commands |
| maintenance:disable |  | Disable maintenance mode |
| maintenance:enable |  | Enable maintenance mode |
| marketplace:download |  | Download plugin from the GLPI marketplace |
| marketplace:info |  | Get information about a plugin |
| marketplace:search |  | Search GLPI marketplace |
| marketplace:upgrade |  | Download all plugins to their latest compatible versions, update all active plugins and reactivate those that were active. |
| migration:appliances_plugin_to_core |  | Migrate Appliances plugin data into GLPI core tables |
| migration:build_missing_timestamps |  | Set missing `date_creation` and `date_mod` values using log entries. |
| migration:compute_documents_size |  | Computes the missing file sizes in the database. |
| migration:databases_plugin_to_core |  | Migrate Databases plugin data into GLPI core tables |
| migration:domains_plugin_to_core |  | Migrate Domains plugin data into GLPI core tables |
| migration:dynamic_row_format |  | Convert database tables to "Dynamic" row format (required for "utf8mb4" character support). |
| migration:formcreator_plugin_to_core |  | Migrate Formcreator plugin data into GLPI core tables |
| migration:genericobject_plugin_to_core |  | Migrate plugin data into GLPI core tables |
| migration:migrate_all |  | Execute all recommended optional migrations. |
| migration:myisam_to_innodb |  | Migrate MyISAM tables to InnoDB |
| migration:racks_plugin_to_core |  | Migrate Racks plugin data into GLPI core tables |
| migration:timestamps |  | Convert "datetime" fields to "timestamp" to use timezones. |
| migration:unsigned_keys |  | Migrate primary/foreign keys to unsigned integers |
| migration:utf8mb4 |  | Convert database character set from "utf8" to "utf8mb4". |
| plugin:activate |  | Activate plugin(s) |
| plugin:deactivate |  | Deactivate plugin(s) |
| plugin:install |  | Run plugin(s) installation script |
| plugin:list |  | List all plugins present in the plugins directory or from the marketplace |
| plugin:resume_execution |  | Resume execution of all active plugins |
| plugin:suspend_execution |  | Suspend execution of all active plugins |
| plugin:uninstall |  | Run plugin(s) uninstallation script |
| rules:process_software_category_rules |  | Process software category rules |
| rules:replay_dictionnary_rules |  | Replay dictionary rules on existing items |
| security:change_key |  | Change password storage key and update values in database. |
| security:change_oauth_key |  | (Re)generate OAuth keys |
| security:disable_2fa |  | Disable 2FA for a user |
| security:session:list |  | List active sessions |
| security:session:revoke |  | Revoke login sessions |
| symfony:about |  | Display information about the current project |
| symfony:assets:install |  | Install bundle's web assets under a public directory |
| symfony:cache:clear |  | Clear the cache |
| symfony:cache:pool:clear |  | Clear cache pools |
| symfony:cache:pool:delete |  | Delete an item from a cache pool |
| symfony:cache:pool:invalidate-tags |  | Invalidate cache tags for all or a specific pool |
| symfony:cache:pool:list |  | List available cache pools |
| symfony:cache:pool:prune |  | Prune cache pools |
| symfony:cache:warmup |  | Warm up an empty cache |
| symfony:config:dump-reference |  | Dump the default configuration for an extension |
| symfony:debug:autowiring |  | List classes/interfaces you can use for autowiring |
| symfony:debug:config |  | Dump the current configuration for an extension |
| symfony:debug:container |  | Display current services for an application |
| symfony:debug:event-dispatcher |  | Display configured listeners for an application |
| symfony:debug:router |  | Display current routes for an application |
| symfony:debug:serializer |  | Display serialization information for classes |
| symfony:debug:twig |  | Show a list of twig functions, filters, globals and tests |
| symfony:debug:twig-component |  | Display components and them usages for an application |
| symfony:error:dump |  | Dump error pages to plain HTML files that can be directly served by a web server |
| symfony:lint:container |  | Ensure that arguments injected into services match type declarations |
| symfony:lint:twig |  | Lint a Twig template and outputs encountered errors |
| symfony:mailer:test |  | Test Mailer transports by sending an email |
| symfony:router:match |  | Help debug routes by simulating a path info match |
| symfony:secrets:decrypt-to-local |  | Decrypt all secrets and stores them in the local vault |
| symfony:secrets:encrypt-from-local |  | Encrypt all local secrets to the vault |
| symfony:secrets:generate-keys |  | Generate new encryption keys |
| symfony:secrets:list |  | List all secrets |
| symfony:secrets:remove |  | Remove a secret from the vault |
| symfony:secrets:reveal |  | Reveal the value of a secret |
| symfony:secrets:set |  | Set a secret in the vault |
| symfony:server:dump |  | Start a dump server that collects and displays dumps in a single place |
| system:check_requirements |  | Check system requirements |
| system:list_services |  | List system services |
| system:status |  | Check system status |
| task:unlock |  | Unlock automatic tasks |
| tools:check_database_keys |  | Check database for missing and errounous keys. |
| tools:check_database_schema_consistency |  | Check database schema consistency. |
| tools:check_decorative_icons |  | Check that decorative icons are hidden from assistive technologies. |
| tools:check_twig_templates_syntax |  | Check twig templates syntax is valid |
| tools:delete_orphan_logs |  | Delete orphan logs |
| tools:generate_api_snapshot |  | Updates a snapshot used for API version tests |
| tools:generate_dev_ldap |  | Create a ready to use AuthLDAP object. |
| tools:generate_forms_for_each_illustrations |  | Generate one form per available illustration. |
| tools:generate_hooks_documentation |  | Generate plugin hooks documentation |
| tools:generate_illustration_translations |  | Generate a files Illustrations tags and title. It's required for translations generation - tools:locales:extract |
| tools:generate_knowbase_items |  | Generate a large knowledge base article tree, to test the KB with a lot of data. |
| tools:licence_headers_check |  | Check licence header in code source files. |
| tools:locales:compile |  | Compile MO files from PO files. |
| tools:locales:extract |  | Extract strings from the project to generate POT file. |
| tools:plugin:release |  | Build a GLPI plugin release archive. |
| user:create |  | Create a new local GLPI user |
| user:delete |  | Delete a GLPI user |
| user:disable |  | Disable a GLPI user |
| user:enable |  | Enable a GLPI user |
| user:grant |  | Grant a profile assignment to a user |
| user:reset_password |  | Reset the password of a local GLPI user |
