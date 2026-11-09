# Dicionário completo do esquema SQL

Gerado por [generate_inventory.py](tools/generate_inventory.py). Fonte: [install/mysql/glpi-empty.sql](../install/mysql/glpi-empty.sql).

Contém tipos, nulabilidade, defaults, índices e opções de todas as tabelas do esquema de instalação. Não contém registros do banco.

Os nomes de colunas não comprovam foreign keys físicas. Consulte [DATABASE.md](DATABASE.md) e [DATABASE_RELATIONS.md](DATABASE_RELATIONS.md).

| Tabela | Colunas | Índices declarados |
| --- | --- | --- |
| [glpi_alerts](#glpi_alerts) | 5 | 4 |
| [glpi_authldapreplicates](#glpi_authldapreplicates) | 6 | 3 |
| [glpi_authldaps](#glpi_authldaps) | 51 | 7 |
| [glpi_authmails](#glpi_authmails) | 9 | 5 |
| [glpi_apiclients](#glpi_apiclients) | 14 | 7 |
| [glpi_autoupdatesystems](#glpi_autoupdatesystems) | 5 | 4 |
| [glpi_blacklistedmailcontents](#glpi_blacklistedmailcontents) | 6 | 4 |
| [glpi_blacklists](#glpi_blacklists) | 7 | 5 |
| [glpi_savedsearches](#glpi_savedsearches) | 15 | 13 |
| [glpi_savedsearches_users](#glpi_savedsearches_users) | 4 | 3 |
| [glpi_savedsearches_alerts](#glpi_savedsearches_alerts) | 9 | 6 |
| [glpi_budgets](#glpi_budgets) | 15 | 12 |
| [glpi_budgettypes](#glpi_budgettypes) | 5 | 4 |
| [glpi_businesscriticities](#glpi_businesscriticities) | 12 | 8 |
| [glpi_calendars](#glpi_calendars) | 8 | 6 |
| [glpi_calendars_holidays](#glpi_calendars_holidays) | 3 | 3 |
| [glpi_calendarsegments](#glpi_calendarsegments) | 7 | 5 |
| [glpi_cartridgeitems](#glpi_cartridgeitems) | 17 | 13 |
| [glpi_printers_cartridgeinfos](#glpi_printers_cartridgeinfos) | 6 | 4 |
| [glpi_cartridgeitems_printermodels](#glpi_cartridgeitems_printermodels) | 3 | 3 |
| [glpi_cartridgeitemtypes](#glpi_cartridgeitemtypes) | 5 | 4 |
| [glpi_cartridges](#glpi_cartridges) | 10 | 6 |
| [glpi_certificates](#glpi_certificates) | 27 | 14 |
| [glpi_certificates_items](#glpi_certificates_items) | 6 | 5 |
| [glpi_certificatetypes](#glpi_certificatetypes) | 7 | 6 |
| [glpi_changecosts](#glpi_changecosts) | 17 | 12 |
| [glpi_changes](#glpi_changes) | 32 | 21 |
| [glpi_changes_groups](#glpi_changes_groups) | 4 | 3 |
| [glpi_changes_items](#glpi_changes_items) | 4 | 3 |
| [glpi_changes_problems](#glpi_changes_problems) | 4 | 3 |
| [glpi_changes_suppliers](#glpi_changes_suppliers) | 6 | 3 |
| [glpi_changes_tickets](#glpi_changes_tickets) | 4 | 3 |
| [glpi_changes_users](#glpi_changes_users) | 6 | 3 |
| [glpi_changetasks](#glpi_changetasks) | 19 | 16 |
| [glpi_changevalidations](#glpi_changevalidations) | 19 | 14 |
| [glpi_itemantiviruses](#glpi_itemantiviruses) | 14 | 13 |
| [glpi_items_disks](#glpi_items_disks) | 18 | 13 |
| [glpi_computermodels](#glpi_computermodels) | 15 | 5 |
| [glpi_computers](#glpi_computers) | 28 | 21 |
| [glpi_assets_assets_peripheralassets](#glpi_assets_assets_peripheralassets) | 7 | 5 |
| [glpi_items_softwarelicenses](#glpi_items_softwarelicenses) | 6 | 5 |
| [glpi_items_softwareversions](#glpi_items_softwareversions) | 10 | 9 |
| [glpi_computertypes](#glpi_computertypes) | 5 | 4 |
| [glpi_itemvirtualmachines](#glpi_itemvirtualmachines) | 16 | 14 |
| [glpi_items_operatingsystems](#glpi_items_operatingsystems) | 21 | 15 |
| [glpi_operatingsystemkernels](#glpi_operatingsystemkernels) | 5 | 4 |
| [glpi_operatingsystemkernelversions](#glpi_operatingsystemkernelversions) | 6 | 5 |
| [glpi_operatingsystemeditions](#glpi_operatingsystemeditions) | 5 | 4 |
| [glpi_configs](#glpi_configs) | 4 | 3 |
| [glpi_impactrelations](#glpi_impactrelations) | 6 | 4 |
| [glpi_impactcompounds](#glpi_impactcompounds) | 3 | 2 |
| [glpi_impactitems](#glpi_impactitems) | 6 | 5 |
| [glpi_impactcontexts](#glpi_impactcontexts) | 11 | 1 |
| [glpi_consumableitems](#glpi_consumableitems) | 18 | 14 |
| [glpi_consumableitemtypes](#glpi_consumableitemtypes) | 5 | 4 |
| [glpi_consumables](#glpi_consumables) | 9 | 8 |
| [glpi_contacts](#glpi_contacts) | 23 | 9 |
| [glpi_contacts_suppliers](#glpi_contacts_suppliers) | 3 | 3 |
| [glpi_contacttypes](#glpi_contacttypes) | 5 | 4 |
| [glpi_contractcosts](#glpi_contractcosts) | 14 | 12 |
| [glpi_contracts](#glpi_contracts) | 31 | 15 |
| [glpi_contracts_items](#glpi_contracts_items) | 4 | 3 |
| [glpi_contracts_suppliers](#glpi_contracts_suppliers) | 3 | 3 |
| [glpi_contracttypes](#glpi_contracttypes) | 5 | 4 |
| [glpi_crontasklogs](#glpi_crontasklogs) | 8 | 4 |
| [glpi_crontasks](#glpi_crontasks) | 18 | 6 |
| [glpi_dashboards_dashboards](#glpi_dashboards_dashboards) | 7 | 6 |
| [glpi_dashboards_filters](#glpi_dashboards_filters) | 6 | 5 |
| [glpi_dashboards_items](#glpi_dashboards_items) | 11 | 4 |
| [glpi_dashboards_rights](#glpi_dashboards_rights) | 4 | 3 |
| [glpi_devicecasemodels](#glpi_devicecasemodels) | 9 | 5 |
| [glpi_devicecases](#glpi_devicecases) | 10 | 9 |
| [glpi_devicecasetypes](#glpi_devicecasetypes) | 5 | 4 |
| [glpi_devicecontrolmodels](#glpi_devicecontrolmodels) | 6 | 5 |
| [glpi_devicecontrols](#glpi_devicecontrols) | 11 | 9 |
| [glpi_devicedrivemodels](#glpi_devicedrivemodels) | 9 | 5 |
| [glpi_devicedrives](#glpi_devicedrives) | 12 | 9 |
| [glpi_devicegenericmodels](#glpi_devicegenericmodels) | 9 | 5 |
| [glpi_devicegenerics](#glpi_devicegenerics) | 11 | 10 |
| [glpi_devicegenerictypes](#glpi_devicegenerictypes) | 5 | 4 |
| [glpi_devicegraphiccardmodels](#glpi_devicegraphiccardmodels) | 9 | 5 |
| [glpi_devicegraphiccards](#glpi_devicegraphiccards) | 12 | 10 |
| [glpi_deviceharddrivemodels](#glpi_deviceharddrivemodels) | 9 | 5 |
| [glpi_deviceharddrivetypes](#glpi_deviceharddrivetypes) | 5 | 4 |
| [glpi_deviceharddrives](#glpi_deviceharddrives) | 14 | 10 |
| [glpi_devicecameras](#glpi_devicecameras) | 15 | 8 |
| [glpi_items_devicecameras](#glpi_items_devicecameras) | 10 | 10 |
| [glpi_devicecameramodels](#glpi_devicecameramodels) | 9 | 5 |
| [glpi_imageformats](#glpi_imageformats) | 7 | 6 |
| [glpi_imageresolutions](#glpi_imageresolutions) | 8 | 7 |
| [glpi_items_devicecameras_imageformats](#glpi_items_devicecameras_imageformats) | 5 | 5 |
| [glpi_items_devicecameras_imageresolutions](#glpi_items_devicecameras_imageresolutions) | 5 | 5 |
| [glpi_devicememorymodels](#glpi_devicememorymodels) | 9 | 5 |
| [glpi_devicememories](#glpi_devicememories) | 12 | 9 |
| [glpi_devicememorytypes](#glpi_devicememorytypes) | 5 | 4 |
| [glpi_devicemotherboardmodels](#glpi_devicemotherboardmodels) | 9 | 5 |
| [glpi_devicemotherboards](#glpi_devicemotherboards) | 10 | 8 |
| [glpi_devicenetworkcardmodels](#glpi_devicenetworkcardmodels) | 9 | 5 |
| [glpi_devicenetworkcards](#glpi_devicenetworkcards) | 11 | 8 |
| [glpi_devicepcimodels](#glpi_devicepcimodels) | 9 | 5 |
| [glpi_devicepcis](#glpi_devicepcis) | 10 | 9 |
| [glpi_devicepowersupplymodels](#glpi_devicepowersupplymodels) | 9 | 5 |
| [glpi_devicepowersupplies](#glpi_devicepowersupplies) | 11 | 8 |
| [glpi_deviceprocessormodels](#glpi_deviceprocessormodels) | 9 | 5 |
| [glpi_deviceprocessors](#glpi_deviceprocessors) | 13 | 8 |
| [glpi_devicesensors](#glpi_devicesensors) | 11 | 10 |
| [glpi_devicesensormodels](#glpi_devicesensormodels) | 9 | 5 |
| [glpi_devicesensortypes](#glpi_devicesensortypes) | 5 | 4 |
| [glpi_devicesimcards](#glpi_devicesimcards) | 11 | 8 |
| [glpi_items_devicesimcards](#glpi_items_devicesimcards) | 21 | 14 |
| [glpi_devicesimcardtypes](#glpi_devicesimcardtypes) | 5 | 4 |
| [glpi_devicesoundcardmodels](#glpi_devicesoundcardmodels) | 9 | 5 |
| [glpi_devicesoundcards](#glpi_devicesoundcards) | 10 | 8 |
| [glpi_displaypreferences](#glpi_displaypreferences) | 6 | 5 |
| [glpi_documentcategories](#glpi_documentcategories) | 10 | 6 |
| [glpi_documents](#glpi_documents) | 19 | 12 |
| [glpi_documents_items](#glpi_documents_items) | 12 | 11 |
| [glpi_documenttypes](#glpi_documenttypes) | 9 | 6 |
| [glpi_domains](#glpi_domains) | 16 | 14 |
| [glpi_dropdowntranslations](#glpi_dropdowntranslations) | 6 | 4 |
| [glpi_entities](#glpi_entities) | 129 | 14 |
| [glpi_entities_knowbaseitems](#glpi_entities_knowbaseitems) | 4 | 4 |
| [glpi_entities_reminders](#glpi_entities_reminders) | 4 | 4 |
| [glpi_entities_rssfeeds](#glpi_entities_rssfeeds) | 4 | 4 |
| [glpi_events](#glpi_events) | 7 | 4 |
| [glpi_fieldblacklists](#glpi_fieldblacklists) | 10 | 6 |
| [glpi_fieldunicities](#glpi_fieldunicities) | 12 | 7 |
| [glpi_filesystems](#glpi_filesystems) | 5 | 4 |
| [glpi_fqdns](#glpi_fqdns) | 8 | 7 |
| [glpi_groups](#glpi_groups) | 26 | 18 |
| [glpi_groups_knowbaseitems](#glpi_groups_knowbaseitems) | 6 | 5 |
| [glpi_groups_problems](#glpi_groups_problems) | 4 | 3 |
| [glpi_groups_reminders](#glpi_groups_reminders) | 6 | 5 |
| [glpi_groups_rssfeeds](#glpi_groups_rssfeeds) | 6 | 5 |
| [glpi_groups_tickets](#glpi_groups_tickets) | 4 | 3 |
| [glpi_groups_users](#glpi_groups_users) | 6 | 6 |
| [glpi_helpdesks_tiles_items_tiles](#glpi_helpdesks_tiles_items_tiles) | 6 | 4 |
| [glpi_helpdesks_tiles_formtiles](#glpi_helpdesks_tiles_formtiles) | 2 | 2 |
| [glpi_helpdesks_tiles_glpipagetiles](#glpi_helpdesks_tiles_glpipagetiles) | 5 | 1 |
| [glpi_helpdesks_tiles_externalpagetiles](#glpi_helpdesks_tiles_externalpagetiles) | 5 | 1 |
| [glpi_holidays](#glpi_holidays) | 10 | 9 |
| [glpi_infocoms](#glpi_infocoms) | 30 | 11 |
| [glpi_interfacetypes](#glpi_interfacetypes) | 5 | 4 |
| [glpi_ipaddresses](#glpi_ipaddresses) | 14 | 8 |
| [glpi_ipaddresses_ipnetworks](#glpi_ipaddresses_ipnetworks) | 3 | 3 |
| [glpi_ipnetworks](#glpi_ipnetworks) | 29 | 11 |
| [glpi_ipnetworks_vlans](#glpi_ipnetworks_vlans) | 3 | 3 |
| [glpi_items_devicecases](#glpi_items_devicecases) | 12 | 11 |
| [glpi_items_devicecontrols](#glpi_items_devicecontrols) | 13 | 12 |
| [glpi_items_devicedrives](#glpi_items_devicedrives) | 13 | 12 |
| [glpi_items_devicegenerics](#glpi_items_devicegenerics) | 12 | 11 |
| [glpi_items_devicegraphiccards](#glpi_items_devicegraphiccards) | 14 | 13 |
| [glpi_items_deviceharddrives](#glpi_items_deviceharddrives) | 14 | 13 |
| [glpi_items_devicememories](#glpi_items_devicememories) | 14 | 13 |
| [glpi_items_devicemotherboards](#glpi_items_devicemotherboards) | 12 | 11 |
| [glpi_items_devicenetworkcards](#glpi_items_devicenetworkcards) | 14 | 13 |
| [glpi_items_devicepcis](#glpi_items_devicepcis) | 13 | 12 |
| [glpi_items_devicepowersupplies](#glpi_items_devicepowersupplies) | 12 | 11 |
| [glpi_items_deviceprocessors](#glpi_items_deviceprocessors) | 16 | 15 |
| [glpi_items_devicesensors](#glpi_items_devicesensors) | 12 | 11 |
| [glpi_items_devicesoundcards](#glpi_items_devicesoundcards) | 13 | 12 |
| [glpi_items_problems](#glpi_items_problems) | 4 | 3 |
| [glpi_items_processes](#glpi_items_processes) | 13 | 4 |
| [glpi_items_environments](#glpi_items_environments) | 7 | 4 |
| [glpi_items_projects](#glpi_items_projects) | 4 | 3 |
| [glpi_items_tickets](#glpi_items_tickets) | 4 | 3 |
| [glpi_itilcategories](#glpi_itilcategories) | 25 | 20 |
| [glpi_itils_projects](#glpi_itils_projects) | 4 | 3 |
| [glpi_knowbaseitems](#glpi_knowbaseitems) | 17 | 13 |
| [glpi_knowbaseitems_knowbaseitems](#glpi_knowbaseitems_knowbaseitems) | 3 | 3 |
| [glpi_knowbaseitems_profiles](#glpi_knowbaseitems_profiles) | 6 | 5 |
| [glpi_knowbaseitems_favorites](#glpi_knowbaseitems_favorites) | 3 | 3 |
| [glpi_knowbaseitems_users](#glpi_knowbaseitems_users) | 3 | 3 |
| [glpi_knowbaseitemtranslations](#glpi_knowbaseitemtranslations) | 8 | 8 |
| [glpi_lines](#glpi_lines) | 16 | 13 |
| [glpi_lineoperators](#glpi_lineoperators) | 9 | 7 |
| [glpi_linetypes](#glpi_linetypes) | 5 | 4 |
| [glpi_links](#glpi_links) | 9 | 6 |
| [glpi_links_itemtypes](#glpi_links_itemtypes) | 3 | 3 |
| [glpi_locations](#glpi_locations) | 24 | 8 |
| [glpi_logs](#glpi_logs) | 12 | 7 |
| [glpi_mailcollectors](#glpi_mailcollectors) | 20 | 6 |
| [glpi_manufacturers](#glpi_manufacturers) | 5 | 4 |
| [glpi_monitormodels](#glpi_monitormodels) | 15 | 5 |
| [glpi_monitors](#glpi_monitors) | 35 | 21 |
| [glpi_monitortypes](#glpi_monitortypes) | 5 | 4 |
| [glpi_sockets](#glpi_sockets) | 12 | 9 |
| [glpi_cables](#glpi_cables) | 25 | 21 |
| [glpi_cabletypes](#glpi_cabletypes) | 5 | 4 |
| [glpi_cablestrands](#glpi_cablestrands) | 5 | 4 |
| [glpi_socketmodels](#glpi_socketmodels) | 5 | 4 |
| [glpi_networkaliases](#glpi_networkaliases) | 8 | 7 |
| [glpi_networkequipmentmodels](#glpi_networkequipmentmodels) | 15 | 5 |
| [glpi_networkequipments](#glpi_networkequipments) | 32 | 22 |
| [glpi_networkequipmenttypes](#glpi_networkequipmenttypes) | 5 | 4 |
| [glpi_networkinterfaces](#glpi_networkinterfaces) | 5 | 4 |
| [glpi_networknames](#glpi_networknames) | 12 | 10 |
| [glpi_networkportaggregates](#glpi_networkportaggregates) | 5 | 4 |
| [glpi_networkportaliases](#glpi_networkportaliases) | 5 | 5 |
| [glpi_networkportdialups](#glpi_networkportdialups) | 4 | 4 |
| [glpi_networkportethernets](#glpi_networkportethernets) | 7 | 7 |
| [glpi_networkportfiberchanneltypes](#glpi_networkportfiberchanneltypes) | 5 | 4 |
| [glpi_networkportfiberchannels](#glpi_networkportfiberchannels) | 8 | 8 |
| [glpi_networkportlocals](#glpi_networkportlocals) | 4 | 4 |
| [glpi_networkports](#glpi_networkports) | 29 | 10 |
| [glpi_networkports_networkports](#glpi_networkports_networkports) | 3 | 3 |
| [glpi_networkports_vlans](#glpi_networkports_vlans) | 4 | 3 |
| [glpi_networkportwifis](#glpi_networkportwifis) | 9 | 9 |
| [glpi_networks](#glpi_networks) | 5 | 4 |
| [glpi_notepads](#glpi_notepads) | 9 | 6 |
| [glpi_notifications](#glpi_notifications) | 12 | 8 |
| [glpi_notifications_notificationtemplates](#glpi_notifications_notificationtemplates) | 4 | 4 |
| [glpi_notificationtargets](#glpi_notificationtargets) | 5 | 4 |
| [glpi_notificationtemplates](#glpi_notificationtemplates) | 7 | 5 |
| [glpi_notificationtemplatetranslations](#glpi_notificationtemplatetranslations) | 6 | 2 |
| [glpi_notimportedemails](#glpi_notimportedemails) | 9 | 3 |
| [glpi_objectlocks](#glpi_objectlocks) | 5 | 4 |
| [glpi_operatingsystemarchitectures](#glpi_operatingsystemarchitectures) | 5 | 4 |
| [glpi_operatingsystems](#glpi_operatingsystems) | 5 | 4 |
| [glpi_operatingsystemservicepacks](#glpi_operatingsystemservicepacks) | 5 | 4 |
| [glpi_operatingsystemversions](#glpi_operatingsystemversions) | 5 | 4 |
| [glpi_passivedcequipments](#glpi_passivedcequipments) | 19 | 15 |
| [glpi_passivedcequipmentmodels](#glpi_passivedcequipmentmodels) | 15 | 5 |
| [glpi_passivedcequipmenttypes](#glpi_passivedcequipmenttypes) | 5 | 4 |
| [glpi_peripheralmodels](#glpi_peripheralmodels) | 15 | 5 |
| [glpi_peripherals](#glpi_peripherals) | 27 | 21 |
| [glpi_peripheraltypes](#glpi_peripheraltypes) | 5 | 4 |
| [glpi_phonemodels](#glpi_phonemodels) | 9 | 5 |
| [glpi_phonepowersupplies](#glpi_phonepowersupplies) | 5 | 4 |
| [glpi_phones](#glpi_phones) | 32 | 22 |
| [glpi_phonetypes](#glpi_phonetypes) | 5 | 4 |
| [glpi_planningrecalls](#glpi_planningrecalls) | 6 | 5 |
| [glpi_plugins](#glpi_plugins) | 9 | 4 |
| [glpi_printermodels](#glpi_printermodels) | 9 | 5 |
| [glpi_printers](#glpi_printers) | 38 | 24 |
| [glpi_printertypes](#glpi_printertypes) | 5 | 4 |
| [glpi_problemcosts](#glpi_problemcosts) | 16 | 11 |
| [glpi_problems](#glpi_problems) | 29 | 20 |
| [glpi_problems_suppliers](#glpi_problems_suppliers) | 6 | 3 |
| [glpi_problems_tickets](#glpi_problems_tickets) | 4 | 3 |
| [glpi_problems_users](#glpi_problems_users) | 6 | 3 |
| [glpi_problemtasks](#glpi_problemtasks) | 19 | 16 |
| [glpi_profilerights](#glpi_profilerights) | 4 | 3 |
| [glpi_profiles](#glpi_profiles) | 22 | 10 |
| [glpi_profiles_reminders](#glpi_profiles_reminders) | 6 | 5 |
| [glpi_profiles_rssfeeds](#glpi_profiles_rssfeeds) | 6 | 5 |
| [glpi_profiles_users](#glpi_profiles_users) | 7 | 6 |
| [glpi_projectcosts](#glpi_projectcosts) | 14 | 12 |
| [glpi_projects](#glpi_projects) | 27 | 23 |
| [glpi_projectstates](#glpi_projectstates) | 7 | 5 |
| [glpi_projecttasks](#glpi_projecttasks) | 29 | 21 |
| [glpi_projecttasklinks](#glpi_projecttasklinks) | 8 | 3 |
| [glpi_projecttasktemplates](#glpi_projecttasktemplates) | 22 | 17 |
| [glpi_projecttasks_tickets](#glpi_projecttasks_tickets) | 3 | 3 |
| [glpi_projecttaskteams](#glpi_projecttaskteams) | 4 | 3 |
| [glpi_projecttasktypes](#glpi_projecttasktypes) | 5 | 4 |
| [glpi_projectteams](#glpi_projectteams) | 4 | 3 |
| [glpi_projecttypes](#glpi_projecttypes) | 5 | 4 |
| [glpi_queuednotifications](#glpi_queuednotifications) | 28 | 12 |
| [glpi_registeredids](#glpi_registeredids) | 5 | 4 |
| [glpi_reminders](#glpi_reminders) | 14 | 11 |
| [glpi_remindertranslations](#glpi_remindertranslations) | 8 | 5 |
| [glpi_reminders_users](#glpi_reminders_users) | 3 | 3 |
| [glpi_requesttypes](#glpi_requesttypes) | 12 | 11 |
| [glpi_reservationitems](#glpi_reservationitems) | 9 | 8 |
| [glpi_reservations](#glpi_reservations) | 9 | 7 |
| [glpi_rssfeeds](#glpi_rssfeeds) | 11 | 7 |
| [glpi_rssfeeds_users](#glpi_rssfeeds_users) | 3 | 3 |
| [glpi_ruleactions](#glpi_ruleactions) | 5 | 3 |
| [glpi_rulecriterias](#glpi_rulecriterias) | 5 | 3 |
| [glpi_rulerightparameters](#glpi_rulerightparameters) | 6 | 4 |
| [glpi_rules](#glpi_rules) | 14 | 9 |
| [glpi_slalevelactions](#glpi_slalevelactions) | 5 | 2 |
| [glpi_slalevelcriterias](#glpi_slalevelcriterias) | 5 | 3 |
| [glpi_slalevels](#glpi_slalevels) | 9 | 6 |
| [glpi_slalevels_tickets](#glpi_slalevels_tickets) | 4 | 3 |
| [glpi_olalevelactions](#glpi_olalevelactions) | 5 | 2 |
| [glpi_olalevelcriterias](#glpi_olalevelcriterias) | 5 | 3 |
| [glpi_olalevels](#glpi_olalevels) | 9 | 6 |
| [glpi_olalevels_tickets](#glpi_olalevels_tickets) | 4 | 3 |
| [glpi_slms](#glpi_slms) | 9 | 7 |
| [glpi_slas](#glpi_slas) | 14 | 8 |
| [glpi_olas](#glpi_olas) | 15 | 9 |
| [glpi_items_olas](#glpi_items_olas) | 11 | 3 |
| [glpi_softwarecategories](#glpi_softwarecategories) | 10 | 6 |
| [glpi_softwarelicenses](#glpi_softwarelicenses) | 34 | 24 |
| [glpi_softwarelicensetypes](#glpi_softwarelicensetypes) | 12 | 8 |
| [glpi_softwares](#glpi_softwares) | 21 | 16 |
| [glpi_softwareversions](#glpi_softwareversions) | 11 | 10 |
| [glpi_solutiontemplates](#glpi_solutiontemplates) | 9 | 7 |
| [glpi_solutiontypes](#glpi_solutiontypes) | 11 | 10 |
| [glpi_itilsolutions](#glpi_itilsolutions) | 16 | 10 |
| [glpi_ssovariables](#glpi_ssovariables) | 5 | 4 |
| [glpi_states](#glpi_states) | 13 | 9 |
| [glpi_dropdownvisibilities](#glpi_dropdownvisibilities) | 5 | 3 |
| [glpi_suppliers](#glpi_suppliers) | 21 | 9 |
| [glpi_suppliers_tickets](#glpi_suppliers_tickets) | 6 | 3 |
| [glpi_suppliertypes](#glpi_suppliertypes) | 5 | 4 |
| [glpi_taskcategories](#glpi_taskcategories) | 15 | 11 |
| [glpi_tasktemplates](#glpi_tasktemplates) | 16 | 11 |
| [glpi_ticketcosts](#glpi_ticketcosts) | 16 | 11 |
| [glpi_ticketrecurrents](#glpi_ticketrecurrents) | 15 | 10 |
| [glpi_recurrentchanges](#glpi_recurrentchanges) | 15 | 10 |
| [glpi_tickets](#glpi_tickets) | 36 | 27 |
| [glpi_tickets_tickets](#glpi_tickets_tickets) | 4 | 3 |
| [glpi_tickets_users](#glpi_tickets_users) | 6 | 3 |
| [glpi_ticketsatisfactions](#glpi_ticketsatisfactions) | 8 | 2 |
| [glpi_tickettasks](#glpi_tickettasks) | 21 | 18 |
| [glpi_tickettemplatehiddenfields](#glpi_tickettemplatehiddenfields) | 3 | 2 |
| [glpi_changetemplatehiddenfields](#glpi_changetemplatehiddenfields) | 3 | 2 |
| [glpi_problemtemplatehiddenfields](#glpi_problemtemplatehiddenfields) | 3 | 2 |
| [glpi_tickettemplatereadonlyfields](#glpi_tickettemplatereadonlyfields) | 3 | 2 |
| [glpi_changetemplatereadonlyfields](#glpi_changetemplatereadonlyfields) | 3 | 2 |
| [glpi_problemtemplatereadonlyfields](#glpi_problemtemplatereadonlyfields) | 3 | 2 |
| [glpi_tickettemplatemandatoryfields](#glpi_tickettemplatemandatoryfields) | 3 | 2 |
| [glpi_changetemplatemandatoryfields](#glpi_changetemplatemandatoryfields) | 3 | 2 |
| [glpi_problemtemplatemandatoryfields](#glpi_problemtemplatemandatoryfields) | 3 | 2 |
| [glpi_tickettemplatepredefinedfields](#glpi_tickettemplatepredefinedfields) | 4 | 2 |
| [glpi_changetemplatepredefinedfields](#glpi_changetemplatepredefinedfields) | 4 | 2 |
| [glpi_problemtemplatepredefinedfields](#glpi_problemtemplatepredefinedfields) | 4 | 2 |
| [glpi_tickettemplates](#glpi_tickettemplates) | 8 | 6 |
| [glpi_changetemplates](#glpi_changetemplates) | 8 | 6 |
| [glpi_problemtemplates](#glpi_problemtemplates) | 8 | 6 |
| [glpi_ticketvalidations](#glpi_ticketvalidations) | 16 | 11 |
| [glpi_validationsteps](#glpi_validationsteps) | 7 | 4 |
| [glpi_itils_validationsteps](#glpi_itils_validationsteps) | 5 | 3 |
| [glpi_transfers](#glpi_transfers) | 38 | 4 |
| [glpi_usercategories](#glpi_usercategories) | 5 | 4 |
| [glpi_useremails](#glpi_useremails) | 5 | 5 |
| [glpi_users](#glpi_users) | 111 | 26 |
| [glpi_usertitles](#glpi_usertitles) | 5 | 4 |
| [glpi_virtualmachinestates](#glpi_virtualmachinestates) | 5 | 4 |
| [glpi_virtualmachinesystems](#glpi_virtualmachinesystems) | 5 | 4 |
| [glpi_virtualmachinetypes](#glpi_virtualmachinetypes) | 5 | 4 |
| [glpi_vlans](#glpi_vlans) | 8 | 7 |
| [glpi_wifinetworks](#glpi_wifinetworks) | 9 | 7 |
| [glpi_knowbaseitems_items](#glpi_knowbaseitems_items) | 6 | 5 |
| [glpi_knowbaseitems_revisions](#glpi_knowbaseitems_revisions) | 8 | 5 |
| [glpi_knowbaseitems_comments](#glpi_knowbaseitems_comments) | 12 | 6 |
| [glpi_devicebatterymodels](#glpi_devicebatterymodels) | 9 | 5 |
| [glpi_devicebatteries](#glpi_devicebatteries) | 12 | 9 |
| [glpi_items_devicebatteries](#glpi_items_devicebatteries) | 14 | 11 |
| [glpi_devicebatterytypes](#glpi_devicebatterytypes) | 5 | 4 |
| [glpi_devicefirmwaremodels](#glpi_devicefirmwaremodels) | 6 | 5 |
| [glpi_devicefirmwares](#glpi_devicefirmwares) | 12 | 9 |
| [glpi_items_devicefirmwares](#glpi_items_devicefirmwares) | 12 | 11 |
| [glpi_devicefirmwaretypes](#glpi_devicefirmwaretypes) | 5 | 4 |
| [glpi_datacenters](#glpi_datacenters) | 9 | 8 |
| [glpi_dcrooms](#glpi_dcrooms) | 16 | 9 |
| [glpi_rackmodels](#glpi_rackmodels) | 7 | 5 |
| [glpi_racktypes](#glpi_racktypes) | 7 | 6 |
| [glpi_racks](#glpi_racks) | 30 | 16 |
| [glpi_items_racks](#glpi_items_racks) | 9 | 3 |
| [glpi_enclosuremodels](#glpi_enclosuremodels) | 15 | 5 |
| [glpi_enclosures](#glpi_enclosures) | 20 | 14 |
| [glpi_items_enclosures](#glpi_items_enclosures) | 5 | 3 |
| [glpi_pdumodels](#glpi_pdumodels) | 16 | 6 |
| [glpi_pdutypes](#glpi_pdutypes) | 7 | 6 |
| [glpi_pdus](#glpi_pdus) | 24 | 18 |
| [glpi_plugtypes](#glpi_plugtypes) | 7 | 6 |
| [glpi_plugs](#glpi_plugs) | 17 | 12 |
| [glpi_pdus_racks](#glpi_pdus_racks) | 8 | 5 |
| [glpi_itilfollowuptemplates](#glpi_itilfollowuptemplates) | 11 | 9 |
| [glpi_itilfollowups](#glpi_itilfollowups) | 14 | 11 |
| [glpi_clustertypes](#glpi_clustertypes) | 7 | 6 |
| [glpi_clusters](#glpi_clusters) | 15 | 12 |
| [glpi_items_clusters](#glpi_items_clusters) | 4 | 3 |
| [glpi_planningexternalevents](#glpi_planningexternalevents) | 19 | 15 |
| [glpi_planningexternaleventtemplates](#glpi_planningexternaleventtemplates) | 13 | 7 |
| [glpi_planningeventcategories](#glpi_planningeventcategories) | 6 | 4 |
| [glpi_items_kanbans](#glpi_items_kanbans) | 7 | 5 |
| [glpi_vobjects](#glpi_vobjects) | 6 | 5 |
| [glpi_domaintypes](#glpi_domaintypes) | 7 | 6 |
| [glpi_domainrelations](#glpi_domainrelations) | 7 | 6 |
| [glpi_domains_items](#glpi_domains_items) | 7 | 6 |
| [glpi_domainrecordtypes](#glpi_domainrecordtypes) | 8 | 6 |
| [glpi_domainrecords](#glpi_domainrecords) | 15 | 11 |
| [glpi_appliances](#glpi_appliances) | 22 | 18 |
| [glpi_appliances_items](#glpi_appliances_items) | 4 | 3 |
| [glpi_appliancetypes](#glpi_appliancetypes) | 8 | 7 |
| [glpi_applianceenvironments](#glpi_applianceenvironments) | 5 | 4 |
| [glpi_appliances_items_relations](#glpi_appliances_items_relations) | 4 | 3 |
| [glpi_agenttypes](#glpi_agenttypes) | 4 | 4 |
| [glpi_agents](#glpi_agents) | 27 | 7 |
| [glpi_rulematchedlogs](#glpi_rulematchedlogs) | 8 | 4 |
| [glpi_lockedfields](#glpi_lockedfields) | 8 | 5 |
| [glpi_unmanageds](#glpi_unmanageds) | 28 | 19 |
| [glpi_networkporttypes](#glpi_networkporttypes) | 10 | 8 |
| [glpi_printerlogs](#glpi_printerlogs) | 18 | 5 |
| [glpi_networkportconnectionlogs](#glpi_networkportconnectionlogs) | 5 | 4 |
| [glpi_networkportmetrics](#glpi_networkportmetrics) | 9 | 5 |
| [glpi_refusedequipments](#glpi_refusedequipments) | 14 | 8 |
| [glpi_usbvendors](#glpi_usbvendors) | 9 | 8 |
| [glpi_pcivendors](#glpi_pcivendors) | 9 | 8 |
| [glpi_items_remotemanagements](#glpi_items_remotemanagements) | 7 | 4 |
| [glpi_pendingreasons](#glpi_pendingreasons) | 14 | 9 |
| [glpi_pendingreasons_items](#glpi_pendingreasons_items) | 11 | 6 |
| [glpi_manuallinks](#glpi_manuallinks) | 10 | 6 |
| [glpi_tickets_contracts](#glpi_tickets_contracts) | 3 | 3 |
| [glpi_databaseinstancetypes](#glpi_databaseinstancetypes) | 5 | 4 |
| [glpi_databaseinstancecategories](#glpi_databaseinstancecategories) | 5 | 4 |
| [glpi_databaseinstances](#glpi_databaseinstances) | 27 | 19 |
| [glpi_databases](#glpi_databases) | 14 | 10 |
| [glpi_snmpcredentials](#glpi_snmpcredentials) | 12 | 6 |
| [glpi_forms_categories](#glpi_forms_categories) | 12 | 6 |
| [glpi_forms_forms](#glpi_forms_forms) | 19 | 11 |
| [glpi_forms_sections](#glpi_forms_sections) | 8 | 4 |
| [glpi_forms_questions](#glpi_forms_questions) | 16 | 5 |
| [glpi_forms_comments](#glpi_forms_comments) | 10 | 5 |
| [glpi_forms_answerssets](#glpi_forms_answerssets) | 9 | 7 |
| [glpi_forms_destinations_answerssets_formdestinationitems](#glpi_forms_destinations_answerssets_formdestinationitems) | 4 | 3 |
| [glpi_forms_destinations_formdestinations](#glpi_forms_destinations_formdestinations) | 7 | 4 |
| [glpi_forms_accesscontrols_formaccesscontrols](#glpi_forms_accesscontrols_formaccesscontrols) | 5 | 3 |
| [glpi_items_ticketrecurrents](#glpi_items_ticketrecurrents) | 4 | 4 |
| [glpi_items_lines](#glpi_items_lines) | 4 | 3 |
| [glpi_changes_changes](#glpi_changes_changes) | 4 | 3 |
| [glpi_problems_problems](#glpi_problems_problems) | 4 | 3 |
| [glpi_changesatisfactions](#glpi_changesatisfactions) | 8 | 2 |
| [glpi_oauth_access_tokens](#glpi_oauth_access_tokens) | 8 | 3 |
| [glpi_oauth_refresh_tokens](#glpi_oauth_refresh_tokens) | 4 | 2 |
| [glpi_oauth_auth_codes](#glpi_oauth_auth_codes) | 6 | 2 |
| [glpi_oauthclients](#glpi_oauthclients) | 13 | 6 |
| [glpi_validatorsubstitutes](#glpi_validatorsubstitutes) | 3 | 3 |
| [glpi_searches_criteriafilters](#glpi_searches_criteriafilters) | 5 | 3 |
| [glpi_itilvalidationtemplates](#glpi_itilvalidationtemplates) | 9 | 7 |
| [glpi_itilvalidationtemplates_targets](#glpi_itilvalidationtemplates_targets) | 5 | 4 |
| [glpi_itilreminders](#glpi_itilreminders) | 8 | 6 |
| [glpi_defaultfilters](#glpi_defaultfilters) | 7 | 6 |
| [glpi_webhooks](#glpi_webhooks) | 27 | 9 |
| [glpi_webhookcategories](#glpi_webhookcategories) | 10 | 6 |
| [glpi_queuedwebhooks](#glpi_queuedwebhooks) | 18 | 9 |
| [glpi_stencils](#glpi_stencils) | 7 | 4 |
| [glpi_assets_assetdefinitions](#glpi_assets_assetdefinitions) | 13 | 6 |
| [glpi_assets_assets](#glpi_assets_assets) | 27 | 19 |
| [glpi_assets_assetmodels](#glpi_assets_assetmodels) | 17 | 6 |
| [glpi_assets_assettypes](#glpi_assets_assettypes) | 6 | 5 |
| [glpi_groups_items](#glpi_groups_items) | 5 | 4 |
| [glpi_dropdowns_dropdowndefinitions](#glpi_dropdowns_dropdowndefinitions) | 10 | 6 |
| [glpi_dropdowns_dropdowns](#glpi_dropdowns_dropdowns) | 13 | 9 |
| [glpi_assets_customfielddefinitions](#glpi_assets_customfielddefinitions) | 11 | 6 |
| [glpi_contracts_users](#glpi_contracts_users) | 3 | 3 |
| [glpi_softwarelicenses_users](#glpi_softwarelicenses_users) | 3 | 3 |
| [glpi_itemtranslations_itemtranslations](#glpi_itemtranslations_itemtranslations) | 7 | 3 |
| [glpi_sharetokens](#glpi_sharetokens) | 11 | 10 |
| [glpi_usertokens](#glpi_usertokens) | 6 | 5 |
| [glpi_users_sessions](#glpi_users_sessions) | 9 | 4 |
| [glpi_users_sessionhistories](#glpi_users_sessionhistories) | 10 | 4 |

## glpi_alerts

Origem: [DDL, linha 39](../install/mysql/glpi-empty.sql#L39).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '0'` |
| `date` | `timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`type`)
KEY `type` (`type`)
KEY `date` (`date`)
```

## glpi_authldapreplicates

Origem: [DDL, linha 55](../install/mysql/glpi-empty.sql#L55).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `authldaps_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `host` | `varchar(255) DEFAULT NULL` |
| `port` | `int NOT NULL DEFAULT '389'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `timeout` | `int NOT NULL DEFAULT '10'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `authldaps_id` (`authldaps_id`)
```

## glpi_authldaps

Origem: [DDL, linha 71](../install/mysql/glpi-empty.sql#L71).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `host` | `varchar(255) DEFAULT NULL` |
| `basedn` | `varchar(255) DEFAULT NULL` |
| `rootdn` | `varchar(255) DEFAULT NULL` |
| `port` | `int NOT NULL DEFAULT '389'` |
| `condition` | `text` |
| `login_field` | `varchar(255) DEFAULT 'uid'` |
| `sync_field` | `varchar(255) DEFAULT NULL` |
| `use_tls` | `tinyint NOT NULL DEFAULT '0'` |
| `group_field` | `varchar(255) DEFAULT NULL` |
| `group_condition` | `text` |
| `group_search_type` | `int NOT NULL DEFAULT '0'` |
| `group_member_field` | `varchar(255) DEFAULT NULL` |
| `email1_field` | `varchar(255) DEFAULT NULL` |
| `realname_field` | `varchar(255) DEFAULT NULL` |
| `firstname_field` | `varchar(255) DEFAULT NULL` |
| `phone_field` | `varchar(255) DEFAULT NULL` |
| `phone2_field` | `varchar(255) DEFAULT NULL` |
| `mobile_field` | `varchar(255) DEFAULT NULL` |
| `comment_field` | `varchar(255) DEFAULT NULL` |
| `use_dn` | `tinyint NOT NULL DEFAULT '1'` |
| `time_offset` | `int NOT NULL DEFAULT '0'` |
| `deref_option` | `int NOT NULL DEFAULT '0'` |
| `title_field` | `varchar(255) DEFAULT NULL` |
| `category_field` | `varchar(255) DEFAULT NULL` |
| `language_field` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `is_default` | `tinyint NOT NULL DEFAULT '0'` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `rootdn_passwd` | `varchar(255) DEFAULT NULL` |
| `registration_number_field` | `varchar(255) DEFAULT NULL` |
| `email2_field` | `varchar(255) DEFAULT NULL` |
| `email3_field` | `varchar(255) DEFAULT NULL` |
| `email4_field` | `varchar(255) DEFAULT NULL` |
| `location_field` | `varchar(255) DEFAULT NULL` |
| `responsible_field` | `varchar(255) DEFAULT NULL` |
| `pagesize` | `int NOT NULL DEFAULT '0'` |
| `ldap_maxlimit` | `int NOT NULL DEFAULT '0'` |
| `can_support_pagesize` | `tinyint NOT NULL DEFAULT '0'` |
| `picture_field` | `varchar(255) DEFAULT NULL` |
| `begin_date_field` | `varchar(255) DEFAULT NULL` |
| `end_date_field` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `inventory_domain` | `varchar(255) DEFAULT NULL` |
| `tls_certfile` | `text` |
| `tls_keyfile` | `text` |
| `use_bind` | `tinyint NOT NULL DEFAULT '1'` |
| `timeout` | `int NOT NULL DEFAULT '10'` |
| `tls_version` | `varchar(10) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `is_default` (`is_default`)
KEY `is_active` (`is_active`)
KEY `date_creation` (`date_creation`)
KEY `sync_field` (`sync_field`)
```

## glpi_authmails

Origem: [DDL, linha 136](../install/mysql/glpi-empty.sql#L136).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `connect_string` | `varchar(255) DEFAULT NULL` |
| `host` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `is_default` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `is_active` (`is_active`)
```

## glpi_apiclients

Origem: [DDL, linha 156](../install/mysql/glpi-empty.sql#L156).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `ipv4_range_start` | `bigint DEFAULT NULL` |
| `ipv4_range_end` | `bigint DEFAULT NULL` |
| `ipv6` | `varchar(255) DEFAULT NULL` |
| `app_token` | `varchar(255) DEFAULT NULL` |
| `app_token_date` | `timestamp NULL DEFAULT NULL` |
| `dolog_method` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `is_active` (`is_active`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_autoupdatesystems

Origem: [DDL, linha 184](../install/mysql/glpi-empty.sql#L184).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_blacklistedmailcontents

Origem: [DDL, linha 200](../install/mysql/glpi-empty.sql#L200).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `content` | `text` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_blacklists

Origem: [DDL, linha 217](../install/mysql/glpi-empty.sql#L217).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `type` | `int NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `value` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `type` (`type`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_savedsearches

Origem: [DDL, linha 236](../install/mysql/glpi-empty.sql#L236).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `type` | `int NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_private` | `tinyint NOT NULL DEFAULT '1'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `query` | `text` |
| `last_execution_time` | `int DEFAULT NULL` |
| `do_count` | `tinyint NOT NULL DEFAULT '2'` |
| `last_execution_date` | `timestamp NULL DEFAULT NULL` |
| `counter` | `int NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `type` (`type`)
KEY `itemtype` (`itemtype`)
KEY `entities_id` (`entities_id`)
KEY `users_id` (`users_id`)
KEY `is_private` (`is_private`)
KEY `is_recursive` (`is_recursive`)
KEY `last_execution_time` (`last_execution_time`)
KEY `last_execution_date` (`last_execution_date`)
KEY `do_count` (`do_count`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_savedsearches_users

Origem: [DDL, linha 271](../install/mysql/glpi-empty.sql#L271).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `savedsearches_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`users_id`,`itemtype`)
KEY `savedsearches_id` (`savedsearches_id`)
```

## glpi_savedsearches_alerts

Origem: [DDL, linha 285](../install/mysql/glpi-empty.sql#L285).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `savedsearches_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `operator` | `tinyint NOT NULL` |
| `value` | `int NOT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `frequency` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`savedsearches_id`,`operator`,`value`)
KEY `name` (`name`)
KEY `is_active` (`is_active`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_budgets

Origem: [DDL, linha 307](../install/mysql/glpi-empty.sql#L307).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `begin_date` | `date DEFAULT NULL` |
| `end_date` | `date DEFAULT NULL` |
| `value` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `budgettypes_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_recursive` (`is_recursive`)
KEY `entities_id` (`entities_id`)
KEY `begin_date` (`begin_date`)
KEY `end_date` (`end_date`)
KEY `is_template` (`is_template`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `locations_id` (`locations_id`)
KEY `budgettypes_id` (`budgettypes_id`)
```

## glpi_budgettypes

Origem: [DDL, linha 341](../install/mysql/glpi-empty.sql#L341).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_businesscriticities

Origem: [DDL, linha 356](../install/mysql/glpi-empty.sql#L356).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `businesscriticities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `completename` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`businesscriticities_id`,`name`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `level` (`level`)
```

## glpi_calendars

Origem: [DDL, linha 383](../install/mysql/glpi-empty.sql#L383).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `cache_duration` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_calendars_holidays

Origem: [DDL, linha 404](../install/mysql/glpi-empty.sql#L404).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `calendars_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `holidays_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`calendars_id`,`holidays_id`)
KEY `holidays_id` (`holidays_id`)
```

## glpi_calendarsegments

Origem: [DDL, linha 417](../install/mysql/glpi-empty.sql#L417).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `calendars_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `day` | `tinyint NOT NULL DEFAULT '1'` |
| `begin` | `time DEFAULT NULL` |
| `end` | `time DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `calendars_id` (`calendars_id`)
KEY `day` (`day`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_cartridgeitems

Origem: [DDL, linha 436](../install/mysql/glpi-empty.sql#L436).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `ref` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `cartridgeitemtypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `alarm_threshold` | `int NOT NULL DEFAULT '10'` |
| `stock_target` | `int NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `pictures` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `locations_id` (`locations_id`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `cartridgeitemtypes_id` (`cartridgeitemtypes_id`)
KEY `is_deleted` (`is_deleted`)
KEY `alarm_threshold` (`alarm_threshold`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_printers_cartridgeinfos

Origem: [DDL, linha 470](../install/mysql/glpi-empty.sql#L470).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `printers_id` | `int unsigned NOT NULL` |
| `property` | `varchar(255) NOT NULL` |
| `value` | `varchar(255) NOT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `printers_id` (`printers_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_cartridgeitems_printermodels

Origem: [DDL, linha 486](../install/mysql/glpi-empty.sql#L486).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `cartridgeitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `printermodels_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`printermodels_id`,`cartridgeitems_id`)
KEY `cartridgeitems_id` (`cartridgeitems_id`)
```

## glpi_cartridgeitemtypes

Origem: [DDL, linha 499](../install/mysql/glpi-empty.sql#L499).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_cartridges

Origem: [DDL, linha 515](../install/mysql/glpi-empty.sql#L515).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `cartridgeitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `printers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_in` | `date DEFAULT NULL` |
| `date_use` | `date DEFAULT NULL` |
| `date_out` | `date DEFAULT NULL` |
| `pages` | `int NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `cartridgeitems_id` (`cartridgeitems_id`)
KEY `printers_id` (`printers_id`)
KEY `entities_id` (`entities_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_certificates

Origem: [DDL, linha 538](../install/mysql/glpi-empty.sql#L538).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `certificatetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `dns_name` | `varchar(255) DEFAULT NULL` |
| `dns_suffix` | `varchar(255) DEFAULT NULL` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `contact` | `varchar(255) DEFAULT NULL` |
| `contact_num` | `varchar(255) DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_autosign` | `tinyint NOT NULL DEFAULT '0'` |
| `date_expiration` | `date DEFAULT NULL` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `command` | `text` |
| `certificate_request` | `text` |
| `certificate_item` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_template` (`is_template`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `certificatetypes_id` (`certificatetypes_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `users_id` (`users_id`)
KEY `locations_id` (`locations_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `states_id` (`states_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_certificates_items

Origem: [DDL, linha 586](../install/mysql/glpi-empty.sql#L586).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `certificates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`certificates_id`,`itemtype`,`items_id`)
KEY `item` (`itemtype`,`items_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_certificatetypes

Origem: [DDL, linha 604](../install/mysql/glpi-empty.sql#L604).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_changecosts

Origem: [DDL, linha 624](../install/mysql/glpi-empty.sql#L624).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `begin_date` | `date DEFAULT NULL` |
| `end_date` | `date DEFAULT NULL` |
| `actiontime` | `int NOT NULL DEFAULT '0'` |
| `cost_time` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `cost_fixed` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `cost_material` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `budgets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_lastupdater` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `changes_id` (`changes_id`)
KEY `begin_date` (`begin_date`)
KEY `end_date` (`end_date`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `budgets_id` (`budgets_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `users_id` (`users_id`)
KEY `users_id_lastupdater` (`users_id_lastupdater`)
```

## glpi_changes

Origem: [DDL, linha 660](../install/mysql/glpi-empty.sql#L660).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `status` | `int NOT NULL DEFAULT '1'` |
| `content` | `longtext` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `solvedate` | `timestamp NULL DEFAULT NULL` |
| `closedate` | `timestamp NULL DEFAULT NULL` |
| `time_to_resolve` | `timestamp NULL DEFAULT NULL` |
| `users_id_recipient` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_lastupdater` | `int unsigned NOT NULL DEFAULT '0'` |
| `urgency` | `int NOT NULL DEFAULT '1'` |
| `impact` | `int NOT NULL DEFAULT '1'` |
| `priority` | `int NOT NULL DEFAULT '1'` |
| `itilcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `impactcontent` | `longtext` |
| `controlistcontent` | `longtext` |
| `rolloutplancontent` | `longtext` |
| `backoutplancontent` | `longtext` |
| `checklistcontent` | `longtext` |
| `global_validation` | `int NOT NULL DEFAULT '1'` |
| `actiontime` | `int NOT NULL DEFAULT '0'` |
| `begin_waiting_date` | `timestamp NULL DEFAULT NULL` |
| `waiting_duration` | `int NOT NULL DEFAULT '0'` |
| `close_delay_stat` | `int NOT NULL DEFAULT '0'` |
| `solve_delay_stat` | `int NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `changetemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_deleted` (`is_deleted`)
KEY `date` (`date`)
KEY `closedate` (`closedate`)
KEY `status` (`status`)
KEY `priority` (`priority`)
KEY `date_mod` (`date_mod`)
KEY `itilcategories_id` (`itilcategories_id`)
KEY `users_id_recipient` (`users_id_recipient`)
KEY `solvedate` (`solvedate`)
KEY `urgency` (`urgency`)
KEY `impact` (`impact`)
KEY `time_to_resolve` (`time_to_resolve`)
KEY `global_validation` (`global_validation`)
KEY `users_id_lastupdater` (`users_id_lastupdater`)
KEY `date_creation` (`date_creation`)
KEY `changetemplates_id` (`changetemplates_id`)
KEY `locations_id` (`locations_id`)
```

## glpi_changes_groups

Origem: [DDL, linha 720](../install/mysql/glpi-empty.sql#L720).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`changes_id`,`type`,`groups_id`)
KEY `group` (`groups_id`,`type`)
```

## glpi_changes_items

Origem: [DDL, linha 734](../install/mysql/glpi-empty.sql#L734).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`changes_id`,`itemtype`,`items_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_changes_problems

Origem: [DDL, linha 748](../install/mysql/glpi-empty.sql#L748).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `problems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `link` | `int NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`changes_id`,`problems_id`)
KEY `problems_id` (`problems_id`)
```

## glpi_changes_suppliers

Origem: [DDL, linha 762](../install/mysql/glpi-empty.sql#L762).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `suppliers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |
| `use_notification` | `tinyint NOT NULL DEFAULT '0'` |
| `alternative_email` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`changes_id`,`type`,`suppliers_id`)
KEY `group` (`suppliers_id`,`type`)
```

## glpi_changes_tickets

Origem: [DDL, linha 778](../install/mysql/glpi-empty.sql#L778).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `link` | `int NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`changes_id`,`tickets_id`)
KEY `tickets_id` (`tickets_id`)
```

## glpi_changes_users

Origem: [DDL, linha 792](../install/mysql/glpi-empty.sql#L792).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |
| `use_notification` | `tinyint NOT NULL DEFAULT '0'` |
| `alternative_email` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`changes_id`,`type`,`users_id`,`alternative_email`)
KEY `user` (`users_id`,`type`)
```

## glpi_changetasks

Origem: [DDL, linha 808](../install/mysql/glpi-empty.sql#L808).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `changes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `taskcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `state` | `int NOT NULL DEFAULT '0'` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `begin` | `timestamp NULL DEFAULT NULL` |
| `end` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_editor` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `content` | `longtext` |
| `actiontime` | `int NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `tasktemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `timeline_position` | `tinyint NOT NULL DEFAULT '0'` |
| `is_private` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `uuid` (`uuid`)
KEY `changes_id` (`changes_id`)
KEY `state` (`state`)
KEY `users_id` (`users_id`)
KEY `users_id_editor` (`users_id_editor`)
KEY `users_id_tech` (`users_id_tech`)
KEY `groups_id_tech` (`groups_id_tech`)
KEY `date` (`date`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `begin` (`begin`)
KEY `end` (`end`)
KEY `taskcategories_id` (`taskcategories_id`)
KEY `tasktemplates_id` (`tasktemplates_id`)
KEY `is_private` (`is_private`)
```

## glpi_changevalidations

Origem: [DDL, linha 850](../install/mysql/glpi-empty.sql#L850).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itils_validationsteps_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `changes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_validate` | `int unsigned NOT NULL DEFAULT '0'` |
| `itilvalidationtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype_target` | `varchar(255) NOT NULL` |
| `items_id_target` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment_submission` | `text` |
| `comment_validation` | `text` |
| `status` | `int NOT NULL DEFAULT '2'` |
| `submission_date` | `timestamp NULL DEFAULT NULL` |
| `validation_date` | `timestamp NULL DEFAULT NULL` |
| `timeline_position` | `tinyint NOT NULL DEFAULT '0'` |
| `last_reminder_date` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `users_id` (`users_id`)
KEY `users_id_validate` (`users_id_validate`)
KEY `itilvalidationtemplates_id` (`itilvalidationtemplates_id`)
KEY `item_target` (`itemtype_target`,`items_id_target`)
KEY `changes_id` (`changes_id`)
KEY `submission_date` (`submission_date`)
KEY `validation_date` (`validation_date`)
KEY `status` (`status`)
KEY `itils_validationsteps_id` (`itils_validationsteps_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_itemantiviruses

Origem: [DDL, linha 890](../install/mysql/glpi-empty.sql#L890).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `antivirus_version` | `varchar(255) DEFAULT NULL` |
| `signature_version` | `varchar(255) DEFAULT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_uptodate` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `date_expiration` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `antivirus_version` (`antivirus_version`)
KEY `signature_version` (`signature_version`)
KEY `is_active` (`is_active`)
KEY `is_uptodate` (`is_uptodate`)
KEY `is_dynamic` (`is_dynamic`)
KEY `is_deleted` (`is_deleted`)
KEY `date_expiration` (`date_expiration`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_items_disks

Origem: [DDL, linha 924](../install/mysql/glpi-empty.sql#L924).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `device` | `varchar(255) DEFAULT NULL` |
| `mountpoint` | `varchar(255) DEFAULT NULL` |
| `filesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `totalsize` | `bigint NOT NULL DEFAULT '0'` |
| `freesize` | `bigint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `encryption_status` | `int NOT NULL DEFAULT '0'` |
| `encryption_tool` | `varchar(255) DEFAULT NULL` |
| `encryption_algorithm` | `varchar(255) DEFAULT NULL` |
| `encryption_type` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `device` (`device`)
KEY `mountpoint` (`mountpoint`)
KEY `totalsize` (`totalsize`)
KEY `freesize` (`freesize`)
KEY `item` (`itemtype`,`items_id`)
KEY `filesystems_id` (`filesystems_id`)
KEY `entities_id` (`entities_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_computermodels

Origem: [DDL, linha 962](../install/mysql/glpi-empty.sql#L962).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `weight` | `int NOT NULL DEFAULT '0'` |
| `required_units` | `int NOT NULL DEFAULT '1'` |
| `depth` | `float NOT NULL DEFAULT '1'` |
| `power_connections` | `int NOT NULL DEFAULT '0'` |
| `power_consumption` | `int NOT NULL DEFAULT '0'` |
| `is_half_rack` | `tinyint NOT NULL DEFAULT '0'` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `product_number` (`product_number`)
```

## glpi_computers

Origem: [DDL, linha 989](../install/mysql/glpi-empty.sql#L989).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `contact` | `varchar(255) DEFAULT NULL` |
| `contact_num` | `varchar(255) DEFAULT NULL` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `computermodels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `computertypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ticket_tco` | `decimal(20,4) DEFAULT '0.0000'` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `last_inventory_update` | `timestamp NULL DEFAULT NULL` |
| `last_boot` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `date_mod` (`date_mod`)
KEY `name` (`name`)
KEY `is_template` (`is_template`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
KEY `entities_id` (`entities_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `users_id` (`users_id`)
KEY `locations_id` (`locations_id`)
KEY `computermodels_id` (`computermodels_id`)
KEY `networks_id` (`networks_id`)
KEY `states_id` (`states_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `computertypes_id` (`computertypes_id`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `is_dynamic` (`is_dynamic`)
KEY `serial` (`serial`)
KEY `otherserial` (`otherserial`)
KEY `uuid` (`uuid`)
KEY `date_creation` (`date_creation`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_assets_assets_peripheralassets

Origem: [DDL, linha 1046](../install/mysql/glpi-empty.sql#L1046).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype_asset` | `varchar(255) NOT NULL` |
| `items_id_asset` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_id_peripheral` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype_peripheral` | `varchar(255) NOT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item_asset` (`itemtype_asset`,`items_id_asset`)
KEY `item_peripheral` (`itemtype_peripheral`,`items_id_peripheral`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
```

## glpi_items_softwarelicenses

Origem: [DDL, linha 1066](../install/mysql/glpi-empty.sql#L1066).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `softwarelicenses_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`,`items_id`)
KEY `softwarelicenses_id` (`softwarelicenses_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
```

## glpi_items_softwareversions

Origem: [DDL, linha 1084](../install/mysql/glpi-empty.sql#L1084).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `softwareversions_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted_item` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template_item` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `date_install` | `date DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`softwareversions_id`)
KEY `softwareversions_id` (`softwareversions_id`)
KEY `computers_info` (`entities_id`,`is_template_item`,`is_deleted_item`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `is_deleted_item` (`is_deleted_item`)
KEY `is_template_item` (`is_template_item`)
KEY `date_install` (`date_install`)
```

## glpi_computertypes

Origem: [DDL, linha 1110](../install/mysql/glpi-empty.sql#L1110).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_itemvirtualmachines

Origem: [DDL, linha 1126](../install/mysql/glpi-empty.sql#L1126).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `virtualmachinestates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `virtualmachinesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `virtualmachinetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `uuid` | `varchar(255) NOT NULL DEFAULT ''` |
| `vcpu` | `int NOT NULL DEFAULT '0'` |
| `ram` | `int unsigned DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`, `items_id`)
KEY `entities_id` (`entities_id`)
KEY `name` (`name`)
KEY `virtualmachinestates_id` (`virtualmachinestates_id`)
KEY `virtualmachinesystems_id` (`virtualmachinesystems_id`)
KEY `vcpu` (`vcpu`)
KEY `ram` (`ram`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `uuid` (`uuid`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `virtualmachinetypes_id` (`virtualmachinetypes_id`)
```

## glpi_items_operatingsystems

Origem: [DDL, linha 1163](../install/mysql/glpi-empty.sql#L1163).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `operatingsystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `operatingsystemversions_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `operatingsystemservicepacks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `operatingsystemarchitectures_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `operatingsystemkernelversions_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `license_number` | `varchar(255) DEFAULT NULL` |
| `licenseid` | `varchar(255) DEFAULT NULL` |
| `company` | `varchar(255) DEFAULT NULL` |
| `owner` | `varchar(255) DEFAULT NULL` |
| `hostid` | `varchar(255) DEFAULT NULL` |
| `operatingsystemeditions_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `install_date` | `date NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`items_id`,`itemtype`,`operatingsystems_id`,`operatingsystemarchitectures_id`)
KEY `item` (`itemtype`,`items_id`)
KEY `operatingsystems_id` (`operatingsystems_id`)
KEY `operatingsystemservicepacks_id` (`operatingsystemservicepacks_id`)
KEY `operatingsystemversions_id` (`operatingsystemversions_id`)
KEY `operatingsystemarchitectures_id` (`operatingsystemarchitectures_id`)
KEY `operatingsystemkernelversions_id` (`operatingsystemkernelversions_id`)
KEY `operatingsystemeditions_id` (`operatingsystemeditions_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_operatingsystemkernels

Origem: [DDL, linha 1206](../install/mysql/glpi-empty.sql#L1206).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_operatingsystemkernelversions

Origem: [DDL, linha 1222](../install/mysql/glpi-empty.sql#L1222).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `operatingsystemkernels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `operatingsystemkernels_id` (`operatingsystemkernels_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_operatingsystemeditions

Origem: [DDL, linha 1239](../install/mysql/glpi-empty.sql#L1239).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_configs

Origem: [DDL, linha 1254](../install/mysql/glpi-empty.sql#L1254).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `context` | `varchar(150) DEFAULT NULL` |
| `name` | `varchar(150) DEFAULT NULL` |
| `value` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`context`,`name`)
KEY `name` (`name`)
```

## glpi_impactrelations

Origem: [DDL, linha 1267](../install/mysql/glpi-empty.sql#L1267).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `itemtype_source` | `varchar(255) NOT NULL DEFAULT ''` |
| `items_id_source` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype_impacted` | `varchar(255) NOT NULL DEFAULT ''` |
| `items_id_impacted` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype_source`,`items_id_source`,`itemtype_impacted`,`items_id_impacted`)
KEY `name` (`name`)
KEY `impacted_asset` (`itemtype_impacted`,`items_id_impacted`)
```

## glpi_impactcompounds

Origem: [DDL, linha 1284](../install/mysql/glpi-empty.sql#L1284).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT ''` |
| `color` | `varchar(255) NOT NULL DEFAULT ''` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
```

## glpi_impactitems

Origem: [DDL, linha 1296](../install/mysql/glpi-empty.sql#L1296).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL DEFAULT ''` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `parent_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `impactcontexts_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_dependent` | `tinyint NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`)
KEY `source` (`itemtype`,`items_id`)
KEY `parent_id` (`parent_id`)
KEY `impactcontexts_id` (`impactcontexts_id`)
```

## glpi_impactcontexts

Origem: [DDL, linha 1313](../install/mysql/glpi-empty.sql#L1313).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `positions` | `mediumtext NOT NULL` |
| `zoom` | `float NOT NULL DEFAULT '0'` |
| `pan_x` | `float NOT NULL DEFAULT '0'` |
| `pan_y` | `float NOT NULL DEFAULT '0'` |
| `impact_color` | `varchar(255) NOT NULL DEFAULT ''` |
| `depends_color` | `varchar(255) NOT NULL DEFAULT ''` |
| `impact_and_depends_color` | `varchar(255) NOT NULL DEFAULT ''` |
| `show_depends` | `tinyint NOT NULL DEFAULT '1'` |
| `show_impact` | `tinyint NOT NULL DEFAULT '1'` |
| `max_depth` | `int NOT NULL DEFAULT '5'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
```

## glpi_consumableitems

Origem: [DDL, linha 1331](../install/mysql/glpi-empty.sql#L1331).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `ref` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `consumableitemtypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `alarm_threshold` | `int NOT NULL DEFAULT '10'` |
| `stock_target` | `int NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `pictures` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `locations_id` (`locations_id`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `consumableitemtypes_id` (`consumableitemtypes_id`)
KEY `is_deleted` (`is_deleted`)
KEY `alarm_threshold` (`alarm_threshold`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `otherserial` (`otherserial`)
```

## glpi_consumableitemtypes

Origem: [DDL, linha 1370](../install/mysql/glpi-empty.sql#L1370).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_consumables

Origem: [DDL, linha 1386](../install/mysql/glpi-empty.sql#L1386).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `consumableitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_in` | `date DEFAULT NULL` |
| `date_out` | `date DEFAULT NULL` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `date_in` (`date_in`)
KEY `date_out` (`date_out`)
KEY `consumableitems_id` (`consumableitems_id`)
KEY `entities_id` (`entities_id`)
KEY `item` (`itemtype`,`items_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_contacts

Origem: [DDL, linha 1410](../install/mysql/glpi-empty.sql#L1410).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `firstname` | `varchar(255) DEFAULT NULL` |
| `registration_number` | `varchar(255) DEFAULT NULL` |
| `phone` | `varchar(255) DEFAULT NULL` |
| `phone2` | `varchar(255) DEFAULT NULL` |
| `mobile` | `varchar(255) DEFAULT NULL` |
| `fax` | `varchar(255) DEFAULT NULL` |
| `email` | `varchar(255) DEFAULT NULL` |
| `contacttypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `usertitles_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `address` | `text` |
| `postcode` | `varchar(255) DEFAULT NULL` |
| `town` | `varchar(255) DEFAULT NULL` |
| `state` | `varchar(255) DEFAULT NULL` |
| `country` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `pictures` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `contacttypes_id` (`contacttypes_id`)
KEY `is_deleted` (`is_deleted`)
KEY `usertitles_id` (`usertitles_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_contacts_suppliers

Origem: [DDL, linha 1449](../install/mysql/glpi-empty.sql#L1449).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `suppliers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `contacts_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`suppliers_id`,`contacts_id`)
KEY `contacts_id` (`contacts_id`)
```

## glpi_contacttypes

Origem: [DDL, linha 1462](../install/mysql/glpi-empty.sql#L1462).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_contractcosts

Origem: [DDL, linha 1478](../install/mysql/glpi-empty.sql#L1478).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `contracts_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `begin_date` | `date DEFAULT NULL` |
| `end_date` | `date DEFAULT NULL` |
| `cost` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `budgets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_lastupdater` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `contracts_id` (`contracts_id`)
KEY `begin_date` (`begin_date`)
KEY `end_date` (`end_date`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `budgets_id` (`budgets_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `users_id` (`users_id`)
KEY `users_id_lastupdater` (`users_id_lastupdater`)
```

## glpi_contracts

Origem: [DDL, linha 1511](../install/mysql/glpi-empty.sql#L1511).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `num` | `varchar(255) DEFAULT NULL` |
| `contracttypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `begin_date` | `date DEFAULT NULL` |
| `duration` | `int NOT NULL DEFAULT '0'` |
| `notice` | `int NOT NULL DEFAULT '0'` |
| `periodicity` | `int NOT NULL DEFAULT '0'` |
| `billing` | `int NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `accounting_number` | `varchar(255) DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `week_begin_hour` | `time NOT NULL DEFAULT '00:00:00'` |
| `week_end_hour` | `time NOT NULL DEFAULT '00:00:00'` |
| `saturday_begin_hour` | `time NOT NULL DEFAULT '00:00:00'` |
| `saturday_end_hour` | `time NOT NULL DEFAULT '00:00:00'` |
| `use_saturday` | `tinyint NOT NULL DEFAULT '0'` |
| `sunday_begin_hour` | `time NOT NULL DEFAULT '00:00:00'` |
| `sunday_end_hour` | `time NOT NULL DEFAULT '00:00:00'` |
| `use_sunday` | `tinyint NOT NULL DEFAULT '0'` |
| `max_links_allowed` | `int NOT NULL DEFAULT '0'` |
| `alert` | `int NOT NULL DEFAULT '0'` |
| `renewal` | `int NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `begin_date` (`begin_date`)
KEY `name` (`name`)
KEY `contracttypes_id` (`contracttypes_id`)
KEY `locations_id` (`locations_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_template` (`is_template`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `use_sunday` (`use_sunday`)
KEY `use_saturday` (`use_saturday`)
KEY `alert` (`alert`)
KEY `states_id` (`states_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_contracts_items

Origem: [DDL, linha 1564](../install/mysql/glpi-empty.sql#L1564).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `contracts_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`contracts_id`,`itemtype`,`items_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_contracts_suppliers

Origem: [DDL, linha 1578](../install/mysql/glpi-empty.sql#L1578).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `suppliers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `contracts_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`suppliers_id`,`contracts_id`)
KEY `contracts_id` (`contracts_id`)
```

## glpi_contracttypes

Origem: [DDL, linha 1591](../install/mysql/glpi-empty.sql#L1591).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_crontasklogs

Origem: [DDL, linha 1607](../install/mysql/glpi-empty.sql#L1607).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `crontasks_id` | `int unsigned NOT NULL` |
| `crontasklogs_id` | `int unsigned NOT NULL` |
| `date` | `timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP` |
| `state` | `int NOT NULL` |
| `elapsed` | `float NOT NULL` |
| `volume` | `int NOT NULL` |
| `content` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `date` (`date`)
KEY `crontasks_id` (`crontasks_id`)
KEY `crontasklogs_id_state` (`crontasklogs_id`,`state`)
```

## glpi_crontasks

Origem: [DDL, linha 1626](../install/mysql/glpi-empty.sql#L1626).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='Task run by internal / external cron.'`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `name` | `varchar(150) NOT NULL` |
| `frequency` | `int NOT NULL` |
| `param` | `int DEFAULT NULL` |
| `state` | `int NOT NULL DEFAULT '1'` |
| `mode` | `int NOT NULL DEFAULT '1'` |
| `allowmode` | `int NOT NULL DEFAULT '3'` |
| `hourmin` | `int NOT NULL DEFAULT '0'` |
| `hourmax` | `int NOT NULL DEFAULT '24'` |
| `logs_lifetime` | `int NOT NULL DEFAULT '30'` |
| `lastrun` | `timestamp NULL DEFAULT NULL` |
| `lastcode` | `int DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `error_count` | `int NOT NULL DEFAULT '0'` |
| `next_run` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`name`)
KEY `name` (`name`)
KEY `mode` (`mode`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_dashboards_dashboards

Origem: [DDL, linha 1656](../install/mysql/glpi-empty.sql#L1656).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `key` | `varchar(100) NOT NULL` |
| `name` | `varchar(100) NOT NULL` |
| `context` | `varchar(100) NOT NULL DEFAULT 'core'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `key` (`key`)
KEY `name` (`name`)
KEY `users_id` (`users_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_dashboards_filters

Origem: [DDL, linha 1675](../install/mysql/glpi-empty.sql#L1675).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `dashboards_dashboards_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `filter` | `longtext` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `dashboards_dashboards_id` (`dashboards_dashboards_id`)
KEY `users_id` (`users_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_dashboards_items

Origem: [DDL, linha 1692](../install/mysql/glpi-empty.sql#L1692).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `dashboards_dashboards_id` | `int unsigned NOT NULL` |
| `gridstack_id` | `varchar(255) NOT NULL` |
| `card_id` | `varchar(255) NOT NULL` |
| `x` | `int DEFAULT NULL` |
| `y` | `int DEFAULT NULL` |
| `width` | `int DEFAULT NULL` |
| `height` | `int DEFAULT NULL` |
| `card_options` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `dashboards_dashboards_id` (`dashboards_dashboards_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_dashboards_rights

Origem: [DDL, linha 1713](../install/mysql/glpi-empty.sql#L1713).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `dashboards_dashboards_id` | `int unsigned NOT NULL` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`dashboards_dashboards_id`,`itemtype`,`items_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_devicecasemodels

Origem: [DDL, linha 1726](../install/mysql/glpi-empty.sql#L1726).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicecases

Origem: [DDL, linha 1746](../install/mysql/glpi-empty.sql#L1746).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `devicecasetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicecasemodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `devicecasetypes_id` (`devicecasetypes_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicecasemodels_id` (`devicecasemodels_id`)
```

## glpi_devicecasetypes

Origem: [DDL, linha 1772](../install/mysql/glpi-empty.sql#L1772).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_devicecontrolmodels

Origem: [DDL, linha 1788](../install/mysql/glpi-empty.sql#L1788).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicecontrols

Origem: [DDL, linha 1805](../install/mysql/glpi-empty.sql#L1805).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `is_raid` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `interfacetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicecontrolmodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `interfacetypes_id` (`interfacetypes_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicecontrolmodels_id` (`devicecontrolmodels_id`)
```

## glpi_devicedrivemodels

Origem: [DDL, linha 1832](../install/mysql/glpi-empty.sql#L1832).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicedrives

Origem: [DDL, linha 1852](../install/mysql/glpi-empty.sql#L1852).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `is_writer` | `tinyint NOT NULL DEFAULT '1'` |
| `speed` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `interfacetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicedrivemodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `interfacetypes_id` (`interfacetypes_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicedrivemodels_id` (`devicedrivemodels_id`)
```

## glpi_devicegenericmodels

Origem: [DDL, linha 1880](../install/mysql/glpi-empty.sql#L1880).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicegenerics

Origem: [DDL, linha 1901](../install/mysql/glpi-empty.sql#L1901).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `devicegenerictypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `devicegenericmodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `devicegenerictypes_id` (`devicegenerictypes_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `locations_id` (`locations_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicegenericmodels_id` (`devicegenericmodels_id`)
```

## glpi_devicegenerictypes

Origem: [DDL, linha 1929](../install/mysql/glpi-empty.sql#L1929).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicegraphiccardmodels

Origem: [DDL, linha 1945](../install/mysql/glpi-empty.sql#L1945).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicegraphiccards

Origem: [DDL, linha 1965](../install/mysql/glpi-empty.sql#L1965).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `interfacetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `memory_default` | `int NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicegraphiccardmodels_id` | `int unsigned DEFAULT NULL` |
| `chipset` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `interfacetypes_id` (`interfacetypes_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `chipset` (`chipset`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicegraphiccardmodels_id` (`devicegraphiccardmodels_id`)
```

## glpi_deviceharddrivemodels

Origem: [DDL, linha 1994](../install/mysql/glpi-empty.sql#L1994).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_deviceharddrivetypes

Origem: [DDL, linha 2014](../install/mysql/glpi-empty.sql#L2014).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_deviceharddrives

Origem: [DDL, linha 2029](../install/mysql/glpi-empty.sql#L2029).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `rpm` | `varchar(255) DEFAULT NULL` |
| `interfacetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `cache` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `capacity_default` | `int NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `deviceharddrivemodels_id` | `int unsigned DEFAULT NULL` |
| `deviceharddrivetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `interfacetypes_id` (`interfacetypes_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `deviceharddrivemodels_id` (`deviceharddrivemodels_id`)
KEY `deviceharddrivetypes_id` (`deviceharddrivetypes_id`)
```

## glpi_devicecameras

Origem: [DDL, linha 2060](../install/mysql/glpi-empty.sql#L2060).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `flashunit` | `tinyint NOT NULL DEFAULT '0'` |
| `lensfacing` | `varchar(255) DEFAULT NULL` |
| `orientation` | `varchar(255) DEFAULT NULL` |
| `focallength` | `varchar(255) DEFAULT NULL` |
| `sensorsize` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicecameramodels_id` | `int unsigned DEFAULT NULL` |
| `support` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `devicecameramodels_id` (`devicecameramodels_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_items_devicecameras

Origem: [DDL, linha 2089](../install/mysql/glpi-empty.sql#L2089).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicecameras_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `items_id` (`items_id`)
KEY `devicecameras_id` (`devicecameras_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_devicecameramodels

Origem: [DDL, linha 2116](../install/mysql/glpi-empty.sql#L2116).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_imageformats

Origem: [DDL, linha 2137](../install/mysql/glpi-empty.sql#L2137).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_imageresolutions

Origem: [DDL, linha 2157](../install/mysql/glpi-empty.sql#L2157).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `is_video` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`name`)
KEY `date_mod` (`date_mod`)
KEY `is_video` (`is_video`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
```

## glpi_items_devicecameras_imageformats

Origem: [DDL, linha 2177](../install/mysql/glpi-empty.sql#L2177).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_devicecameras_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `imageformats_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `items_devicecameras_id` (`items_devicecameras_id`)
KEY `imageformats_id` (`imageformats_id`)
KEY `is_dynamic` (`is_dynamic`)
KEY `is_deleted` (`is_deleted`)
```

## glpi_items_devicecameras_imageresolutions

Origem: [DDL, linha 2191](../install/mysql/glpi-empty.sql#L2191).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_devicecameras_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `imageresolutions_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `items_devicecameras_id` (`items_devicecameras_id`)
KEY `imageresolutions_id` (`imageresolutions_id`)
KEY `is_dynamic` (`is_dynamic`)
KEY `is_deleted` (`is_deleted`)
```

## glpi_devicememorymodels

Origem: [DDL, linha 2208](../install/mysql/glpi-empty.sql#L2208).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicememories

Origem: [DDL, linha 2229](../install/mysql/glpi-empty.sql#L2229).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `frequence` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `size_default` | `int NOT NULL DEFAULT '0'` |
| `devicememorytypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicememorymodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `devicememorytypes_id` (`devicememorytypes_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicememorymodels_id` (`devicememorymodels_id`)
```

## glpi_devicememorytypes

Origem: [DDL, linha 2257](../install/mysql/glpi-empty.sql#L2257).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_devicemotherboardmodels

Origem: [DDL, linha 2273](../install/mysql/glpi-empty.sql#L2273).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicemotherboards

Origem: [DDL, linha 2293](../install/mysql/glpi-empty.sql#L2293).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `chipset` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicemotherboardmodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicemotherboardmodels_id` (`devicemotherboardmodels_id`)
```

## glpi_devicenetworkcardmodels

Origem: [DDL, linha 2318](../install/mysql/glpi-empty.sql#L2318).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicenetworkcards

Origem: [DDL, linha 2338](../install/mysql/glpi-empty.sql#L2338).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `bandwidth` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `mac_default` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicenetworkcardmodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicenetworkcardmodels_id` (`devicenetworkcardmodels_id`)
```

## glpi_devicepcimodels

Origem: [DDL, linha 2364](../install/mysql/glpi-empty.sql#L2364).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicepcis

Origem: [DDL, linha 2384](../install/mysql/glpi-empty.sql#L2384).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `devicenetworkcardmodels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicepcimodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `devicenetworkcardmodels_id` (`devicenetworkcardmodels_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicepcimodels_id` (`devicepcimodels_id`)
```

## glpi_devicepowersupplymodels

Origem: [DDL, linha 2410](../install/mysql/glpi-empty.sql#L2410).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicepowersupplies

Origem: [DDL, linha 2431](../install/mysql/glpi-empty.sql#L2431).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `power` | `varchar(255) DEFAULT NULL` |
| `is_atx` | `tinyint NOT NULL DEFAULT '1'` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicepowersupplymodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicepowersupplymodels_id` (`devicepowersupplymodels_id`)
```

## glpi_deviceprocessormodels

Origem: [DDL, linha 2457](../install/mysql/glpi-empty.sql#L2457).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_deviceprocessors

Origem: [DDL, linha 2477](../install/mysql/glpi-empty.sql#L2477).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `frequence` | `int NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `frequency_default` | `int NOT NULL DEFAULT '0'` |
| `nbcores_default` | `int DEFAULT NULL` |
| `nbthreads_default` | `int DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `deviceprocessormodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `deviceprocessormodels_id` (`deviceprocessormodels_id`)
```

## glpi_devicesensors

Origem: [DDL, linha 2505](../install/mysql/glpi-empty.sql#L2505).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `devicesensortypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `devicesensormodels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `devicesensortypes_id` (`devicesensortypes_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `locations_id` (`locations_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicesensormodels_id` (`devicesensormodels_id`)
```

## glpi_devicesensormodels

Origem: [DDL, linha 2533](../install/mysql/glpi-empty.sql#L2533).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicesensortypes

Origem: [DDL, linha 2554](../install/mysql/glpi-empty.sql#L2554).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicesimcards

Origem: [DDL, linha 2570](../install/mysql/glpi-empty.sql#L2570).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `voltage` | `int DEFAULT NULL` |
| `devicesimcardtypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `allow_voip` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `devicesimcardtypes_id` (`devicesimcardtypes_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `manufacturers_id` (`manufacturers_id`)
```

## glpi_items_devicesimcards

Origem: [DDL, linha 2596](../install/mysql/glpi-empty.sql#L2596).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `devicesimcards_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `lines_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `pin` | `varchar(255) NOT NULL DEFAULT ''` |
| `pin2` | `varchar(255) NOT NULL DEFAULT ''` |
| `puk` | `varchar(255) NOT NULL DEFAULT ''` |
| `puk2` | `varchar(255) NOT NULL DEFAULT ''` |
| `msin` | `varchar(255) NOT NULL DEFAULT ''` |
| `comment` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`,`items_id`)
KEY `devicesimcards_id` (`devicesimcards_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `otherserial` (`otherserial`)
KEY `states_id` (`states_id`)
KEY `locations_id` (`locations_id`)
KEY `lines_id` (`lines_id`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
```

## glpi_devicesimcardtypes

Origem: [DDL, linha 2638](../install/mysql/glpi-empty.sql#L2638).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_devicesoundcardmodels

Origem: [DDL, linha 2654](../install/mysql/glpi-empty.sql#L2654).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicesoundcards

Origem: [DDL, linha 2675](../install/mysql/glpi-empty.sql#L2675).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `type` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicesoundcardmodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicesoundcardmodels_id` (`devicesoundcardmodels_id`)
```

## glpi_displaypreferences

Origem: [DDL, linha 2700](../install/mysql/glpi-empty.sql#L2700).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `num` | `int NOT NULL DEFAULT '0'` |
| `rank` | `int NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `interface` | `varchar(255) NOT NULL DEFAULT 'central'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`users_id`,`itemtype`,`num`,`interface`)
KEY `rank` (`rank`)
KEY `num` (`num`)
KEY `itemtype` (`itemtype`)
```

## glpi_documentcategories

Origem: [DDL, linha 2718](../install/mysql/glpi-empty.sql#L2718).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `documentcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `completename` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`documentcategories_id`,`name`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `level` (`level`)
```

## glpi_documents

Origem: [DDL, linha 2741](../install/mysql/glpi-empty.sql#L2741).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `filename` | `varchar(255) DEFAULT NULL` |
| `filepath` | `varchar(255) DEFAULT NULL` |
| `documentcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `mime` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `link` | `varchar(255) DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `sha1sum` | `char(40) DEFAULT NULL` |
| `is_blacklisted` | `tinyint NOT NULL DEFAULT '0'` |
| `tag` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `filesize` | `int DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `date_mod` (`date_mod`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `tickets_id` (`tickets_id`)
KEY `users_id` (`users_id`)
KEY `documentcategories_id` (`documentcategories_id`)
KEY `is_deleted` (`is_deleted`)
KEY `sha1sum` (`sha1sum`)
KEY `tag` (`tag`)
KEY `date_creation` (`date_creation`)
```

## glpi_documents_items

Origem: [DDL, linha 2779](../install/mysql/glpi-empty.sql#L2779).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `documents_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned DEFAULT '0'` |
| `timeline_position` | `tinyint NOT NULL DEFAULT '0'` |
| `is_private` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`documents_id`,`itemtype`,`items_id`,`timeline_position`)
KEY `item` (`itemtype`,`items_id`,`entities_id`,`is_recursive`)
KEY `users_id` (`users_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `date` (`date`)
KEY `timeline_position` (`timeline_position`)
KEY `is_private` (`is_private`)
```

## glpi_documenttypes

Origem: [DDL, linha 2809](../install/mysql/glpi-empty.sql#L2809).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `ext` | `varchar(255) DEFAULT NULL` |
| `icon` | `varchar(255) DEFAULT NULL` |
| `mime` | `varchar(255) DEFAULT NULL` |
| `is_uploadable` | `tinyint NOT NULL DEFAULT '1'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`ext`)
KEY `name` (`name`)
KEY `is_uploadable` (`is_uploadable`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_domains

Origem: [DDL, linha 2831](../install/mysql/glpi-empty.sql#L2831).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `domaintypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_expiration` | `timestamp NULL DEFAULT NULL` |
| `date_domaincreation` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `domaintypes_id` (`domaintypes_id`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `date_mod` (`date_mod`)
KEY `is_template` (`is_template`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `is_active` (`is_active`)
KEY `date_expiration` (`date_expiration`)
KEY `date_domaincreation` (`date_domaincreation`)
KEY `date_creation` (`date_creation`)
```

## glpi_dropdowntranslations

Origem: [DDL, linha 2868](../install/mysql/glpi-empty.sql#L2868).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `language` | `varchar(10) DEFAULT NULL` |
| `field` | `varchar(100) DEFAULT NULL` |
| `value` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`language`,`field`)
KEY `language` (`language`)
KEY `field` (`field`)
```

## glpi_entities

Origem: [DDL, linha 2885](../install/mysql/glpi-empty.sql#L2885).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned DEFAULT '0'` |
| `completename` | `text` |
| `comment` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `sons_cache` | `longtext` |
| `ancestors_cache` | `longtext` |
| `registration_number` | `varchar(255) DEFAULT NULL` |
| `address` | `text` |
| `postcode` | `varchar(255) DEFAULT NULL` |
| `town` | `varchar(255) DEFAULT NULL` |
| `state` | `varchar(255) DEFAULT NULL` |
| `country` | `varchar(255) DEFAULT NULL` |
| `website` | `varchar(255) DEFAULT NULL` |
| `phonenumber` | `varchar(255) DEFAULT NULL` |
| `fax` | `varchar(255) DEFAULT NULL` |
| `email` | `varchar(255) DEFAULT NULL` |
| `admin_email` | `varchar(255) DEFAULT NULL` |
| `admin_email_name` | `varchar(255) DEFAULT NULL` |
| `from_email` | `varchar(255) DEFAULT NULL` |
| `from_email_name` | `varchar(255) DEFAULT NULL` |
| `noreply_email` | `varchar(255) DEFAULT NULL` |
| `noreply_email_name` | `varchar(255) DEFAULT NULL` |
| `replyto_email` | `varchar(255) DEFAULT NULL` |
| `replyto_email_name` | `varchar(255) DEFAULT NULL` |
| `notification_subject_tag` | `varchar(255) DEFAULT NULL` |
| `ldap_dn` | `varchar(255) DEFAULT NULL` |
| `tag` | `varchar(255) DEFAULT NULL` |
| `authldaps_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `mail_domain` | `varchar(255) DEFAULT NULL` |
| `entity_ldapfilter` | `text` |
| `mailing_signature` | `text` |
| `url_base` | `text` |
| `cartridges_alert_repeat` | `int NOT NULL DEFAULT '-2'` |
| `consumables_alert_repeat` | `int NOT NULL DEFAULT '-2'` |
| `use_licenses_alert` | `int NOT NULL DEFAULT '-2'` |
| `send_licenses_alert_before_delay` | `int NOT NULL DEFAULT '-2'` |
| `use_certificates_alert` | `int NOT NULL DEFAULT '-2'` |
| `send_certificates_alert_before_delay` | `int NOT NULL DEFAULT '-2'` |
| `certificates_alert_repeat_interval` | `int NOT NULL DEFAULT '-2'` |
| `use_contracts_alert` | `int NOT NULL DEFAULT '-2'` |
| `send_contracts_alert_before_delay` | `int NOT NULL DEFAULT '-2'` |
| `use_infocoms_alert` | `int NOT NULL DEFAULT '-2'` |
| `send_infocoms_alert_before_delay` | `int NOT NULL DEFAULT '-2'` |
| `use_reservations_alert` | `int NOT NULL DEFAULT '-2'` |
| `use_domains_alert` | `int NOT NULL DEFAULT '-2'` |
| `send_domains_alert_close_expiries_delay` | `int NOT NULL DEFAULT '-2'` |
| `send_domains_alert_expired_delay` | `int NOT NULL DEFAULT '-2'` |
| `autoclose_delay` | `int NOT NULL DEFAULT '-2'` |
| `autopurge_delay` | `int NOT NULL DEFAULT '-2'` |
| `notclosed_delay` | `int NOT NULL DEFAULT '-2'` |
| `calendars_strategy` | `tinyint NOT NULL DEFAULT '-2'` |
| `calendars_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `auto_assign_mode` | `int NOT NULL DEFAULT '-2'` |
| `tickettype` | `int NOT NULL DEFAULT '-2'` |
| `max_closedate` | `timestamp NULL DEFAULT NULL` |
| `inquest_config` | `int NOT NULL DEFAULT '-2'` |
| `inquest_rate` | `int NOT NULL DEFAULT '0'` |
| `inquest_delay` | `int NOT NULL DEFAULT '-10'` |
| `inquest_URL` | `text` |
| `inquest_max_rate` | `int NOT NULL DEFAULT '5'` |
| `inquest_default_rate` | `int NOT NULL DEFAULT '3'` |
| `inquest_mandatory_comment` | `int NOT NULL DEFAULT '0'` |
| `max_closedate_change` | `timestamp NULL DEFAULT NULL` |
| `inquest_config_change` | `int NOT NULL DEFAULT '-2'` |
| `inquest_rate_change` | `int NOT NULL DEFAULT '0'` |
| `inquest_delay_change` | `int NOT NULL DEFAULT '-10'` |
| `inquest_URL_change` | `text` |
| `inquest_max_rate_change` | `int NOT NULL DEFAULT '5'` |
| `inquest_default_rate_change` | `int NOT NULL DEFAULT '3'` |
| `inquest_mandatory_comment_change` | `int NOT NULL DEFAULT '0'` |
| `autofill_warranty_date` | `varchar(255) NOT NULL DEFAULT '-2'` |
| `autofill_use_date` | `varchar(255) NOT NULL DEFAULT '-2'` |
| `autofill_buy_date` | `varchar(255) NOT NULL DEFAULT '-2'` |
| `autofill_delivery_date` | `varchar(255) NOT NULL DEFAULT '-2'` |
| `autofill_order_date` | `varchar(255) NOT NULL DEFAULT '-2'` |
| `tickettemplates_strategy` | `tinyint NOT NULL DEFAULT '-2'` |
| `tickettemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `changetemplates_strategy` | `tinyint NOT NULL DEFAULT '-2'` |
| `changetemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `problemtemplates_strategy` | `tinyint NOT NULL DEFAULT '-2'` |
| `problemtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_strategy_software` | `tinyint NOT NULL DEFAULT '-2'` |
| `entities_id_software` | `int unsigned NOT NULL DEFAULT '0'` |
| `default_contract_alert` | `int NOT NULL DEFAULT '-2'` |
| `default_infocom_alert` | `int NOT NULL DEFAULT '-2'` |
| `default_cartridges_alarm_threshold` | `int NOT NULL DEFAULT '-2'` |
| `default_consumables_alarm_threshold` | `int NOT NULL DEFAULT '-2'` |
| `delay_send_emails` | `int NOT NULL DEFAULT '-2'` |
| `is_notif_enable_default` | `int NOT NULL DEFAULT '-2'` |
| `inquest_duration` | `int NOT NULL DEFAULT '0'` |
| `inquest_duration_change` | `int NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `autofill_decommission_date` | `varchar(255) NOT NULL DEFAULT '-2'` |
| `suppliers_as_private` | `int NOT NULL DEFAULT '-2'` |
| `anonymize_support_agents` | `int NOT NULL DEFAULT '-2'` |
| `display_users_initials` | `int NOT NULL DEFAULT '-2'` |
| `contracts_strategy_default` | `tinyint NOT NULL DEFAULT '-2'` |
| `contracts_id_default` | `int unsigned NOT NULL DEFAULT '0'` |
| `enable_custom_css` | `int NOT NULL DEFAULT '-2'` |
| `custom_css_code` | `text` |
| `latitude` | `varchar(255) DEFAULT NULL` |
| `longitude` | `varchar(255) DEFAULT NULL` |
| `altitude` | `varchar(255) DEFAULT NULL` |
| `transfers_strategy` | `tinyint NOT NULL DEFAULT '-2'` |
| `transfers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `agent_base_url` | `varchar(255) DEFAULT NULL` |
| `approval_reminder_repeat_interval` | `int NOT NULL DEFAULT '-2'` |
| `2fa_enforcement_strategy` | `tinyint NOT NULL DEFAULT '-2'` |
| `is_contact_autoupdate` | `tinyint NOT NULL DEFAULT '-2'` |
| `is_user_autoupdate` | `tinyint NOT NULL DEFAULT '-2'` |
| `is_group_autoupdate` | `tinyint NOT NULL DEFAULT '-2'` |
| `is_location_autoupdate` | `tinyint NOT NULL DEFAULT '-2'` |
| `state_autoupdate_mode` | `int NOT NULL DEFAULT '-2'` |
| `is_contact_autoclean` | `tinyint NOT NULL DEFAULT '-2'` |
| `is_user_autoclean` | `tinyint NOT NULL DEFAULT '-2'` |
| `is_group_autoclean` | `tinyint NOT NULL DEFAULT '-2'` |
| `is_location_autoclean` | `tinyint NOT NULL DEFAULT '-2'` |
| `state_autoclean_mode` | `int NOT NULL DEFAULT '-2'` |
| `show_tickets_properties_on_helpdesk` | `int NOT NULL DEFAULT '-2'` |
| `custom_helpdesk_home_scene_left` | `varchar(255) NOT NULL DEFAULT '-2'` |
| `custom_helpdesk_home_scene_right` | `varchar(255) NOT NULL DEFAULT '-2'` |
| `custom_helpdesk_home_title` | `varchar(255) NOT NULL DEFAULT '-2'` |
| `enable_helpdesk_home_search_bar` | `tinyint NOT NULL DEFAULT '-2'` |
| `enable_helpdesk_service_catalog` | `tinyint NOT NULL DEFAULT '-2'` |
| `expand_service_catalog` | `tinyint NOT NULL DEFAULT '-2'` |
| `service_catalog_default_sort_strategy` | `varchar(255) NOT NULL DEFAULT '-2'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`entities_id`,`name`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `tickettemplates_id` (`tickettemplates_id`)
KEY `changetemplates_id` (`changetemplates_id`)
KEY `problemtemplates_id` (`problemtemplates_id`)
KEY `transfers_id` (`transfers_id`)
KEY `authldaps_id` (`authldaps_id`)
KEY `calendars_id` (`calendars_id`)
KEY `entities_id_software` (`entities_id_software`)
KEY `contracts_id_default` (`contracts_id_default`)
KEY `level` (`level`)
```

## glpi_entities_knowbaseitems

Origem: [DDL, linha 3035](../install/mysql/glpi-empty.sql#L3035).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `knowbaseitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`knowbaseitems_id`,`entities_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_entities_reminders

Origem: [DDL, linha 3050](../install/mysql/glpi-empty.sql#L3050).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `reminders_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `reminders_id` (`reminders_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_entities_rssfeeds

Origem: [DDL, linha 3065](../install/mysql/glpi-empty.sql#L3065).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `rssfeeds_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `rssfeeds_id` (`rssfeeds_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_events

Origem: [DDL, linha 3080](../install/mysql/glpi-empty.sql#L3080).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `varchar(255) DEFAULT NULL` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `service` | `varchar(255) DEFAULT NULL` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `message` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `date` (`date`)
KEY `level` (`level`)
KEY `item` (`type`,`items_id`)
```

## glpi_fieldblacklists

Origem: [DDL, linha 3098](../install/mysql/glpi-empty.sql#L3098).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `field` | `varchar(255) NOT NULL DEFAULT ''` |
| `value` | `varchar(255) NOT NULL DEFAULT ''` |
| `itemtype` | `varchar(255) NOT NULL DEFAULT ''` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_fieldunicities

Origem: [DDL, linha 3121](../install/mysql/glpi-empty.sql#L3121).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC COMMENT='Stores field unicity criterias'`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL DEFAULT ''` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `fields` | `text` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `action_refuse` | `tinyint NOT NULL DEFAULT '0'` |
| `action_notify` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_active` (`is_active`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_filesystems

Origem: [DDL, linha 3147](../install/mysql/glpi-empty.sql#L3147).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_fqdns

Origem: [DDL, linha 3163](../install/mysql/glpi-empty.sql#L3163).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `fqdn` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `name` (`name`)
KEY `fqdn` (`fqdn`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_groups

Origem: [DDL, linha 3185](../install/mysql/glpi-empty.sql#L3185).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `code` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `ldap_field` | `varchar(255) DEFAULT NULL` |
| `ldap_value` | `text` |
| `ldap_group_dn` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `completename` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `is_requester` | `tinyint NOT NULL DEFAULT '1'` |
| `is_watcher` | `tinyint NOT NULL DEFAULT '1'` |
| `is_assign` | `tinyint NOT NULL DEFAULT '1'` |
| `is_task` | `tinyint NOT NULL DEFAULT '1'` |
| `is_notify` | `tinyint NOT NULL DEFAULT '1'` |
| `is_itemgroup` | `tinyint NOT NULL DEFAULT '1'` |
| `is_usergroup` | `tinyint NOT NULL DEFAULT '1'` |
| `is_manager` | `tinyint NOT NULL DEFAULT '1'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `recursive_membership` | `tinyint NOT NULL DEFAULT '0'` |
| `2fa_enforced` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `ldap_field` (`ldap_field`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `ldap_value` (`ldap_value`(200))
KEY `ldap_group_dn` (`ldap_group_dn`(200))
KEY `groups_id` (`groups_id`)
KEY `is_requester` (`is_requester`)
KEY `is_watcher` (`is_watcher`)
KEY `is_assign` (`is_assign`)
KEY `is_notify` (`is_notify`)
KEY `is_itemgroup` (`is_itemgroup`)
KEY `is_usergroup` (`is_usergroup`)
KEY `is_manager` (`is_manager`)
KEY `date_creation` (`date_creation`)
KEY `level` (`level`)
```

## glpi_groups_knowbaseitems

Origem: [DDL, linha 3236](../install/mysql/glpi-empty.sql#L3236).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `knowbaseitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned DEFAULT NULL` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `no_entity_restriction` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`knowbaseitems_id`,`groups_id`,`entities_id`)
KEY `groups_id` (`groups_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_groups_problems

Origem: [DDL, linha 3254](../install/mysql/glpi-empty.sql#L3254).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `problems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`problems_id`,`type`,`groups_id`)
KEY `group` (`groups_id`,`type`)
```

## glpi_groups_reminders

Origem: [DDL, linha 3268](../install/mysql/glpi-empty.sql#L3268).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `reminders_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned DEFAULT NULL` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `no_entity_restriction` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `reminders_id` (`reminders_id`)
KEY `groups_id` (`groups_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_groups_rssfeeds

Origem: [DDL, linha 3286](../install/mysql/glpi-empty.sql#L3286).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `rssfeeds_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned DEFAULT NULL` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `no_entity_restriction` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `rssfeeds_id` (`rssfeeds_id`)
KEY `groups_id` (`groups_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_groups_tickets

Origem: [DDL, linha 3304](../install/mysql/glpi-empty.sql#L3304).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`tickets_id`,`type`,`groups_id`)
KEY `group` (`groups_id`,`type`)
```

## glpi_groups_users

Origem: [DDL, linha 3318](../install/mysql/glpi-empty.sql#L3318).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `is_manager` | `tinyint NOT NULL DEFAULT '0'` |
| `is_userdelegate` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`users_id`,`groups_id`)
KEY `groups_id` (`groups_id`)
KEY `is_dynamic` (`is_dynamic`)
KEY `is_manager` (`is_manager`)
KEY `is_userdelegate` (`is_userdelegate`)
```

## glpi_helpdesks_tiles_items_tiles

Origem: [DDL, linha 3336](../install/mysql/glpi-empty.sql#L3336).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype_item` | `varchar(255) DEFAULT NULL` |
| `items_id_item` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype_tile` | `varchar(255) DEFAULT NULL` |
| `items_id_tile` | `int unsigned NOT NULL DEFAULT '0'` |
| `rank` | `int NOT NULL DEFAULT 0` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype_item`, `items_id_item`, `rank`)
UNIQUE KEY `item` (`itemtype_tile`,`items_id_tile`)
KEY `rank` (`rank`)
```

## glpi_helpdesks_tiles_formtiles

Origem: [DDL, linha 3352](../install/mysql/glpi-empty.sql#L3352).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `forms_forms_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `forms_forms_id` (`forms_forms_id`)
```

## glpi_helpdesks_tiles_glpipagetiles

Origem: [DDL, linha 3362](../install/mysql/glpi-empty.sql#L3362).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `title` | `varchar(255) DEFAULT NULL` |
| `description` | `text DEFAULT null` |
| `illustration` | `varchar(255) DEFAULT NULL` |
| `page` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
```

## glpi_helpdesks_tiles_externalpagetiles

Origem: [DDL, linha 3374](../install/mysql/glpi-empty.sql#L3374).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `title` | `varchar(255) DEFAULT NULL` |
| `description` | `text DEFAULT null` |
| `illustration` | `varchar(255) DEFAULT NULL` |
| `url` | `text DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
```

## glpi_holidays

Origem: [DDL, linha 3386](../install/mysql/glpi-empty.sql#L3386).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `begin_date` | `date DEFAULT NULL` |
| `end_date` | `date DEFAULT NULL` |
| `is_perpetual` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `begin_date` (`begin_date`)
KEY `end_date` (`end_date`)
KEY `is_perpetual` (`is_perpetual`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_infocoms

Origem: [DDL, linha 3412](../install/mysql/glpi-empty.sql#L3412).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `buy_date` | `date DEFAULT NULL` |
| `use_date` | `date DEFAULT NULL` |
| `warranty_duration` | `int NOT NULL DEFAULT '0'` |
| `warranty_info` | `varchar(255) DEFAULT NULL` |
| `suppliers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `order_number` | `varchar(255) DEFAULT NULL` |
| `delivery_number` | `varchar(255) DEFAULT NULL` |
| `immo_number` | `varchar(255) DEFAULT NULL` |
| `value` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `warranty_value` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `sink_time` | `int NOT NULL DEFAULT '0'` |
| `sink_type` | `int NOT NULL DEFAULT '0'` |
| `sink_coeff` | `float NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `bill` | `varchar(255) DEFAULT NULL` |
| `budgets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `alert` | `int NOT NULL DEFAULT '0'` |
| `order_date` | `date DEFAULT NULL` |
| `delivery_date` | `date DEFAULT NULL` |
| `inventory_date` | `date DEFAULT NULL` |
| `warranty_date` | `date DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `decommission_date` | `timestamp NULL DEFAULT NULL` |
| `businesscriticities_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`)
KEY `buy_date` (`buy_date`)
KEY `alert` (`alert`)
KEY `budgets_id` (`budgets_id`)
KEY `suppliers_id` (`suppliers_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `businesscriticities_id` (`businesscriticities_id`)
```

## glpi_interfacetypes

Origem: [DDL, linha 3460](../install/mysql/glpi-empty.sql#L3460).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_ipaddresses

Origem: [DDL, linha 3476](../install/mysql/glpi-empty.sql#L3476).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `version` | `tinyint unsigned DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `binary_0` | `int unsigned NOT NULL DEFAULT '0'` |
| `binary_1` | `int unsigned NOT NULL DEFAULT '0'` |
| `binary_2` | `int unsigned NOT NULL DEFAULT '0'` |
| `binary_3` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `mainitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `mainitemtype` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `binary` (`binary_0`,`binary_1`,`binary_2`,`binary_3`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `item` (`itemtype`,`items_id`,`is_deleted`)
KEY `mainitem` (`mainitemtype`,`mainitems_id`,`is_deleted`)
```

## glpi_ipaddresses_ipnetworks

Origem: [DDL, linha 3505](../install/mysql/glpi-empty.sql#L3505).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `ipaddresses_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ipnetworks_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`ipaddresses_id`,`ipnetworks_id`)
KEY `ipnetworks_id` (`ipnetworks_id`)
```

## glpi_ipnetworks

Origem: [DDL, linha 3518](../install/mysql/glpi-empty.sql#L3518).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `ipnetworks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `completename` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `addressable` | `tinyint NOT NULL DEFAULT '0'` |
| `version` | `tinyint unsigned DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `address` | `varchar(40) DEFAULT NULL` |
| `address_0` | `int unsigned NOT NULL DEFAULT '0'` |
| `address_1` | `int unsigned NOT NULL DEFAULT '0'` |
| `address_2` | `int unsigned NOT NULL DEFAULT '0'` |
| `address_3` | `int unsigned NOT NULL DEFAULT '0'` |
| `netmask` | `varchar(40) DEFAULT NULL` |
| `netmask_0` | `int unsigned NOT NULL DEFAULT '0'` |
| `netmask_1` | `int unsigned NOT NULL DEFAULT '0'` |
| `netmask_2` | `int unsigned NOT NULL DEFAULT '0'` |
| `netmask_3` | `int unsigned NOT NULL DEFAULT '0'` |
| `gateway` | `varchar(40) DEFAULT NULL` |
| `gateway_0` | `int unsigned NOT NULL DEFAULT '0'` |
| `gateway_1` | `int unsigned NOT NULL DEFAULT '0'` |
| `gateway_2` | `int unsigned NOT NULL DEFAULT '0'` |
| `gateway_3` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `is_recursive` (`is_recursive`)
KEY `network_definition` (`entities_id`,`address`,`netmask`)
KEY `address` (`address_0`,`address_1`,`address_2`,`address_3`)
KEY `netmask` (`netmask_0`,`netmask_1`,`netmask_2`,`netmask_3`)
KEY `gateway` (`gateway_0`,`gateway_1`,`gateway_2`,`gateway_3`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `ipnetworks_id` (`ipnetworks_id`)
KEY `level` (`level`)
```

## glpi_ipnetworks_vlans

Origem: [DDL, linha 3565](../install/mysql/glpi-empty.sql#L3565).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `ipnetworks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `vlans_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `link` (`ipnetworks_id`,`vlans_id`)
KEY `vlans_id` (`vlans_id`)
```

## glpi_items_devicecases

Origem: [DDL, linha 3578](../install/mysql/glpi-empty.sql#L3578).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicecases_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicecases_id` (`devicecases_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_devicecontrols

Origem: [DDL, linha 3608](../install/mysql/glpi-empty.sql#L3608).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicecontrols_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `busID` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicecontrols_id` (`devicecontrols_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `busID` (`busID`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_devicedrives

Origem: [DDL, linha 3640](../install/mysql/glpi-empty.sql#L3640).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicedrives_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `busID` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicedrives_id` (`devicedrives_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `busID` (`busID`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_devicegenerics

Origem: [DDL, linha 3672](../install/mysql/glpi-empty.sql#L3672).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicegenerics_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicegenerics_id` (`devicegenerics_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_devicegraphiccards

Origem: [DDL, linha 3702](../install/mysql/glpi-empty.sql#L3702).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicegraphiccards_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `memory` | `int NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `busID` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicegraphiccards_id` (`devicegraphiccards_id`)
KEY `specificity` (`memory`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `busID` (`busID`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_deviceharddrives

Origem: [DDL, linha 3736](../install/mysql/glpi-empty.sql#L3736).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `deviceharddrives_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `capacity` | `int NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `busID` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `deviceharddrives_id` (`deviceharddrives_id`)
KEY `specificity` (`capacity`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `serial` (`serial`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `busID` (`busID`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_devicememories

Origem: [DDL, linha 3770](../install/mysql/glpi-empty.sql#L3770).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicememories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `size` | `int NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `busID` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicememories_id` (`devicememories_id`)
KEY `specificity` (`size`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `serial` (`serial`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `busID` (`busID`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_devicemotherboards

Origem: [DDL, linha 3804](../install/mysql/glpi-empty.sql#L3804).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicemotherboards_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicemotherboards_id` (`devicemotherboards_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_devicenetworkcards

Origem: [DDL, linha 3834](../install/mysql/glpi-empty.sql#L3834).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicenetworkcards_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `mac` | `varchar(255) DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `busID` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicenetworkcards_id` (`devicenetworkcards_id`)
KEY `specificity` (`mac`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `busID` (`busID`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_devicepcis

Origem: [DDL, linha 3868](../install/mysql/glpi-empty.sql#L3868).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicepcis_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `busID` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicepcis_id` (`devicepcis_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `busID` (`busID`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_devicepowersupplies

Origem: [DDL, linha 3900](../install/mysql/glpi-empty.sql#L3900).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicepowersupplies_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicepowersupplies_id` (`devicepowersupplies_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_deviceprocessors

Origem: [DDL, linha 3930](../install/mysql/glpi-empty.sql#L3930).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `deviceprocessors_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `frequency` | `int NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `nbcores` | `int DEFAULT NULL` |
| `nbthreads` | `int DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `busID` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `deviceprocessors_id` (`deviceprocessors_id`)
KEY `specificity` (`frequency`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `serial` (`serial`)
KEY `nbcores` (`nbcores`)
KEY `nbthreads` (`nbthreads`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `busID` (`busID`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_devicesensors

Origem: [DDL, linha 3968](../install/mysql/glpi-empty.sql#L3968).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicesensors_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicesensors_id` (`devicesensors_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_devicesoundcards

Origem: [DDL, linha 3998](../install/mysql/glpi-empty.sql#L3998).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicesoundcards_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `busID` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicesoundcards_id` (`devicesoundcards_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `busID` (`busID`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_items_problems

Origem: [DDL, linha 4030](../install/mysql/glpi-empty.sql#L4030).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `problems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`problems_id`,`itemtype`,`items_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_items_processes

Origem: [DDL, linha 4043](../install/mysql/glpi-empty.sql#L4043).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `cmd` | `text` |
| `cpuusage` | `float NOT NULL DEFAULT '0'` |
| `memusage` | `float NOT NULL DEFAULT '0'` |
| `pid` | `int NOT NULL DEFAULT '1'` |
| `started` | `timestamp NULL DEFAULT NULL` |
| `tty` | `varchar(100) DEFAULT NULL` |
| `user` | `varchar(100) DEFAULT NULL` |
| `virtualmemory` | `bigint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`,`items_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
```

## glpi_items_environments

Origem: [DDL, linha 4067](../install/mysql/glpi-empty.sql#L4067).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `key` | `varchar(255) DEFAULT NULL` |
| `value` | `text` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`,`items_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
```

## glpi_items_projects

Origem: [DDL, linha 4085](../install/mysql/glpi-empty.sql#L4085).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `projects_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`projects_id`,`itemtype`,`items_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_items_tickets

Origem: [DDL, linha 4099](../install/mysql/glpi-empty.sql#L4099).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`tickets_id`)
KEY `tickets_id` (`tickets_id`)
```

## glpi_itilcategories

Origem: [DDL, linha 4113](../install/mysql/glpi-empty.sql#L4113).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `itilcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `completename` | `text` |
| `comment` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `knowbaseitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `code` | `varchar(255) DEFAULT NULL` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `is_helpdeskvisible` | `tinyint NOT NULL DEFAULT '1'` |
| `tickettemplates_id_incident` | `int unsigned NOT NULL DEFAULT '0'` |
| `tickettemplates_id_demand` | `int unsigned NOT NULL DEFAULT '0'` |
| `changetemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `problemtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_incident` | `int NOT NULL DEFAULT '1'` |
| `is_request` | `int NOT NULL DEFAULT '1'` |
| `is_problem` | `int NOT NULL DEFAULT '1'` |
| `is_change` | `tinyint NOT NULL DEFAULT '1'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `knowbaseitems_id` (`knowbaseitems_id`)
KEY `users_id` (`users_id`)
KEY `groups_id` (`groups_id`)
KEY `is_helpdeskvisible` (`is_helpdeskvisible`)
KEY `itilcategories_id` (`itilcategories_id`)
KEY `tickettemplates_id_incident` (`tickettemplates_id_incident`)
KEY `tickettemplates_id_demand` (`tickettemplates_id_demand`)
KEY `changetemplates_id` (`changetemplates_id`)
KEY `problemtemplates_id` (`problemtemplates_id`)
KEY `is_incident` (`is_incident`)
KEY `is_request` (`is_request`)
KEY `is_problem` (`is_problem`)
KEY `is_change` (`is_change`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `level` (`level`)
```

## glpi_itils_projects

Origem: [DDL, linha 4165](../install/mysql/glpi-empty.sql#L4165).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL DEFAULT ''` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `projects_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`projects_id`)
KEY `projects_id` (`projects_id`)
```

## glpi_knowbaseitems

Origem: [DDL, linha 4179](../install/mysql/glpi-empty.sql#L4179).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `forms_categories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `text` |
| `answer` | `longtext` |
| `is_faq` | `tinyint NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `view` | `int NOT NULL DEFAULT '0'` |
| `show_in_service_catalog` | `tinyint NOT NULL DEFAULT '0'` |
| `description` | `longtext DEFAULT NULL` |
| `illustration` | `varchar(255) DEFAULT NULL` |
| `is_pinned` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `begin_date` | `timestamp NULL DEFAULT NULL` |
| `end_date` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `forms_categories_id` (`forms_categories_id`)
KEY `is_recursive` (`is_recursive`)
KEY `users_id` (`users_id`)
KEY `is_faq` (`is_faq`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `begin_date` (`begin_date`)
KEY `end_date` (`end_date`)
FULLTEXT KEY `fulltext` (`name`,`answer`)
FULLTEXT KEY `name` (`name`)
FULLTEXT KEY `answer` (`answer`)
```

## glpi_knowbaseitems_knowbaseitems

Origem: [DDL, linha 4216](../install/mysql/glpi-empty.sql#L4216).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `knowbaseitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `knowbaseitems_id_parent` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`knowbaseitems_id`, `knowbaseitems_id_parent`)
KEY `knowbaseitems_id_parent` (`knowbaseitems_id_parent`)
```

## glpi_knowbaseitems_profiles

Origem: [DDL, linha 4229](../install/mysql/glpi-empty.sql#L4229).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `knowbaseitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `profiles_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned DEFAULT NULL` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `no_entity_restriction` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`knowbaseitems_id`,`profiles_id`,`entities_id`)
KEY `profiles_id` (`profiles_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_knowbaseitems_favorites

Origem: [DDL, linha 4247](../install/mysql/glpi-empty.sql#L4247).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `knowbaseitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`knowbaseitems_id`,`users_id`)
KEY `users_id` (`users_id`)
```

## glpi_knowbaseitems_users

Origem: [DDL, linha 4260](../install/mysql/glpi-empty.sql#L4260).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `knowbaseitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`knowbaseitems_id`,`users_id`)
KEY `users_id` (`users_id`)
```

## glpi_knowbaseitemtranslations

Origem: [DDL, linha 4273](../install/mysql/glpi-empty.sql#L4273).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `knowbaseitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `language` | `varchar(10) DEFAULT NULL` |
| `name` | `text` |
| `answer` | `longtext` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`knowbaseitems_id`,`language`)
KEY `users_id` (`users_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
FULLTEXT KEY `fulltext` (`name`,`answer`)
FULLTEXT KEY `name` (`name`)
FULLTEXT KEY `answer` (`answer`)
```

## glpi_lines

Origem: [DDL, linha 4296](../install/mysql/glpi-empty.sql#L4296).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `caller_num` | `varchar(255) NOT NULL DEFAULT ''` |
| `caller_name` | `varchar(255) NOT NULL DEFAULT ''` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `lineoperators_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `linetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_deleted` (`is_deleted`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `lineoperators_id` (`lineoperators_id`)
KEY `linetypes_id` (`linetypes_id`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_lineoperators

Origem: [DDL, linha 4332](../install/mysql/glpi-empty.sql#L4332).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `comment` | `text` |
| `mcc` | `int DEFAULT NULL` |
| `mnc` | `int DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`mcc`,`mnc`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_linetypes

Origem: [DDL, linha 4353](../install/mysql/glpi-empty.sql#L4353).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_links

Origem: [DDL, linha 4368](../install/mysql/glpi-empty.sql#L4368).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '1'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `link` | `varchar(255) DEFAULT NULL` |
| `data` | `text` |
| `open_window` | `tinyint NOT NULL DEFAULT '1'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_links_itemtypes

Origem: [DDL, linha 4390](../install/mysql/glpi-empty.sql#L4390).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `links_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`links_id`)
KEY `links_id` (`links_id`)
```

## glpi_locations

Origem: [DDL, linha 4403](../install/mysql/glpi-empty.sql#L4403).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `code` | `varchar(255) DEFAULT NULL` |
| `alias` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `completename` | `text` |
| `comment` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `address` | `text` |
| `postcode` | `varchar(255) DEFAULT NULL` |
| `town` | `varchar(255) DEFAULT NULL` |
| `state` | `varchar(255) DEFAULT NULL` |
| `country` | `varchar(255) DEFAULT NULL` |
| `building` | `varchar(255) DEFAULT NULL` |
| `room` | `varchar(255) DEFAULT NULL` |
| `latitude` | `varchar(255) DEFAULT NULL` |
| `longitude` | `varchar(255) DEFAULT NULL` |
| `altitude` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`entities_id`,`locations_id`,`name`)
KEY `locations_id` (`locations_id`)
KEY `name` (`name`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `level` (`level`)
```

## glpi_logs

Origem: [DDL, linha 4442](../install/mysql/glpi-empty.sql#L4442).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL DEFAULT ''` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype_link` | `varchar(255) NOT NULL DEFAULT ''` |
| `linked_action` | `int NOT NULL DEFAULT '0'` |
| `user_name` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `id_search_option` | `int NOT NULL DEFAULT '0'` |
| `old_value` | `varchar(255) DEFAULT NULL` |
| `new_value` | `varchar(255) DEFAULT NULL` |
| `old_id` | `int unsigned DEFAULT NULL` |
| `new_id` | `int unsigned DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `date_mod` (`date_mod`)
KEY `itemtype_link` (`itemtype_link`)
KEY `item` (`itemtype`,`items_id`)
KEY `id_search_option` (`id_search_option`)
KEY `old_id` (`old_id`)
KEY `new_id` (`new_id`)
```

## glpi_mailcollectors

Origem: [DDL, linha 4468](../install/mysql/glpi-empty.sql#L4468).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `host` | `varchar(255) DEFAULT NULL` |
| `login` | `varchar(255) DEFAULT NULL` |
| `filesize_max` | `int NOT NULL DEFAULT '2097152'` |
| `is_active` | `tinyint NOT NULL DEFAULT '1'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `passwd` | `varchar(255) DEFAULT NULL` |
| `accepted` | `varchar(255) DEFAULT NULL` |
| `refused` | `varchar(255) DEFAULT NULL` |
| `errors` | `int NOT NULL DEFAULT '0'` |
| `use_mail_date` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `requester_field` | `int NOT NULL DEFAULT '0'` |
| `add_to_to_observer` | `tinyint NOT NULL DEFAULT '1'` |
| `add_cc_to_observer` | `tinyint NOT NULL DEFAULT '0'` |
| `collect_only_unread` | `tinyint NOT NULL DEFAULT '0'` |
| `create_user_from_email` | `tinyint NOT NULL DEFAULT '0'` |
| `last_collect_date` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_active` (`is_active`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `last_collect_date` (`last_collect_date`)
```

## glpi_manufacturers

Origem: [DDL, linha 4501](../install/mysql/glpi-empty.sql#L4501).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_monitormodels

Origem: [DDL, linha 4517](../install/mysql/glpi-empty.sql#L4517).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `weight` | `int NOT NULL DEFAULT '0'` |
| `required_units` | `int NOT NULL DEFAULT '1'` |
| `depth` | `float NOT NULL DEFAULT '1'` |
| `power_connections` | `int NOT NULL DEFAULT '0'` |
| `power_consumption` | `int NOT NULL DEFAULT '0'` |
| `is_half_rack` | `tinyint NOT NULL DEFAULT '0'` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `product_number` (`product_number`)
```

## glpi_monitors

Origem: [DDL, linha 4544](../install/mysql/glpi-empty.sql#L4544).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `contact` | `varchar(255) DEFAULT NULL` |
| `contact_num` | `varchar(255) DEFAULT NULL` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `size` | `decimal(5,2) NOT NULL DEFAULT '0.00'` |
| `have_micro` | `tinyint NOT NULL DEFAULT '0'` |
| `have_speaker` | `tinyint NOT NULL DEFAULT '0'` |
| `have_subd` | `tinyint NOT NULL DEFAULT '0'` |
| `have_bnc` | `tinyint NOT NULL DEFAULT '0'` |
| `have_dvi` | `tinyint NOT NULL DEFAULT '0'` |
| `have_pivot` | `tinyint NOT NULL DEFAULT '0'` |
| `have_hdmi` | `tinyint NOT NULL DEFAULT '0'` |
| `have_displayport` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `monitortypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `monitormodels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_global` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ticket_tco` | `decimal(20,4) DEFAULT '0.0000'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_template` (`is_template`)
KEY `is_global` (`is_global`)
KEY `entities_id` (`entities_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `users_id` (`users_id`)
KEY `locations_id` (`locations_id`)
KEY `monitormodels_id` (`monitormodels_id`)
KEY `states_id` (`states_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `monitortypes_id` (`monitortypes_id`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `is_dynamic` (`is_dynamic`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
KEY `serial` (`serial`)
KEY `otherserial` (`otherserial`)
KEY `uuid` (`uuid`)
KEY `date_creation` (`date_creation`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
```

## glpi_monitortypes

Origem: [DDL, linha 4607](../install/mysql/glpi-empty.sql#L4607).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_sockets

Origem: [DDL, linha 4623](../install/mysql/glpi-empty.sql#L4623).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `position` | `int NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `socketmodels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `wiring_side` | `tinyint DEFAULT '1'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networkports_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `socketmodels_id` (`socketmodels_id`)
KEY `location_name` (`locations_id`,`name`)
KEY `item` (`itemtype`,`items_id`)
KEY `networkports_id` (`networkports_id`)
KEY `wiring_side` (`wiring_side`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_cables

Origem: [DDL, linha 4651](../install/mysql/glpi-empty.sql#L4651).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `itemtype_endpoint_a` | `varchar(255) DEFAULT NULL` |
| `itemtype_endpoint_b` | `varchar(255) DEFAULT NULL` |
| `items_id_endpoint_a` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_id_endpoint_b` | `int unsigned NOT NULL DEFAULT '0'` |
| `socketmodels_id_endpoint_a` | `int unsigned NOT NULL DEFAULT '0'` |
| `socketmodels_id_endpoint_b` | `int unsigned NOT NULL DEFAULT '0'` |
| `sockets_id_endpoint_a` | `int unsigned NOT NULL DEFAULT '0'` |
| `sockets_id_endpoint_b` | `int unsigned NOT NULL DEFAULT '0'` |
| `cablestrands_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `color` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `cabletypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `item_endpoint_a` (`itemtype_endpoint_a`,`items_id_endpoint_a`)
KEY `item_endpoint_b` (`itemtype_endpoint_b`,`items_id_endpoint_b`)
KEY `items_id_endpoint_b` (`items_id_endpoint_b`)
KEY `items_id_endpoint_a` (`items_id_endpoint_a`)
KEY `socketmodels_id_endpoint_a` (`socketmodels_id_endpoint_a`)
KEY `socketmodels_id_endpoint_b` (`socketmodels_id_endpoint_b`)
KEY `sockets_id_endpoint_a` (`sockets_id_endpoint_a`)
KEY `sockets_id_endpoint_b` (`sockets_id_endpoint_b`)
KEY `cablestrands_id` (`cablestrands_id`)
KEY `states_id` (`states_id`)
KEY `complete` (`entities_id`,`name`)
KEY `is_recursive` (`is_recursive`)
KEY `is_template` (`is_template`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `cabletypes_id` (`cabletypes_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `active_assets` (`is_deleted`, `is_template`)
```

## glpi_cabletypes

Origem: [DDL, linha 4704](../install/mysql/glpi-empty.sql#L4704).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_cablestrands

Origem: [DDL, linha 4720](../install/mysql/glpi-empty.sql#L4720).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_socketmodels

Origem: [DDL, linha 4735](../install/mysql/glpi-empty.sql#L4735).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_networkaliases

Origem: [DDL, linha 4751](../install/mysql/glpi-empty.sql#L4751).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networknames_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `fqdns_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `name` (`name`)
KEY `networknames_id` (`networknames_id`)
KEY `fqdns_id` (`fqdns_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_networkequipmentmodels

Origem: [DDL, linha 4773](../install/mysql/glpi-empty.sql#L4773).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `weight` | `int NOT NULL DEFAULT '0'` |
| `required_units` | `int NOT NULL DEFAULT '1'` |
| `depth` | `float NOT NULL DEFAULT '1'` |
| `power_connections` | `int NOT NULL DEFAULT '0'` |
| `power_consumption` | `int NOT NULL DEFAULT '0'` |
| `is_half_rack` | `tinyint NOT NULL DEFAULT '0'` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `product_number` (`product_number`)
```

## glpi_networkequipments

Origem: [DDL, linha 4800](../install/mysql/glpi-empty.sql#L4800).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `ram` | `int unsigned DEFAULT NULL` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `contact` | `varchar(255) DEFAULT NULL` |
| `contact_num` | `varchar(255) DEFAULT NULL` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networkequipmenttypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networkequipmentmodels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ticket_tco` | `decimal(20,4) DEFAULT '0.0000'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `sysdescr` | `text` |
| `cpu` | `int NOT NULL DEFAULT '0'` |
| `uptime` | `varchar(255) NOT NULL DEFAULT '0'` |
| `last_inventory_update` | `timestamp NULL DEFAULT NULL` |
| `snmpcredentials_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_template` (`is_template`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `users_id` (`users_id`)
KEY `locations_id` (`locations_id`)
KEY `networkequipmentmodels_id` (`networkequipmentmodels_id`)
KEY `networks_id` (`networks_id`)
KEY `states_id` (`states_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `networkequipmenttypes_id` (`networkequipmenttypes_id`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `date_mod` (`date_mod`)
KEY `is_dynamic` (`is_dynamic`)
KEY `serial` (`serial`)
KEY `otherserial` (`otherserial`)
KEY `uuid` (`uuid`)
KEY `date_creation` (`date_creation`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
KEY `snmpcredentials_id` (`snmpcredentials_id`)
```

## glpi_networkequipmenttypes

Origem: [DDL, linha 4861](../install/mysql/glpi-empty.sql#L4861).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_networkinterfaces

Origem: [DDL, linha 4877](../install/mysql/glpi-empty.sql#L4877).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_networknames

Origem: [DDL, linha 4893](../install/mysql/glpi-empty.sql#L4893).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `fqdns_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ipnetworks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `FQDN` (`name`,`fqdns_id`)
KEY `fqdns_id` (`fqdns_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `item` (`itemtype`,`items_id`,`is_deleted`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `ipnetworks_id` (`ipnetworks_id`)
```

## glpi_networkportaggregates

Origem: [DDL, linha 4922](../install/mysql/glpi-empty.sql#L4922).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `networkports_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networkports_id_list` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `networkports_id` (`networkports_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_networkportaliases

Origem: [DDL, linha 4938](../install/mysql/glpi-empty.sql#L4938).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `networkports_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networkports_id_alias` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `networkports_id` (`networkports_id`)
KEY `networkports_id_alias` (`networkports_id_alias`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_networkportdialups

Origem: [DDL, linha 4955](../install/mysql/glpi-empty.sql#L4955).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `networkports_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `networkports_id` (`networkports_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_networkportethernets

Origem: [DDL, linha 4970](../install/mysql/glpi-empty.sql#L4970).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `networkports_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_devicenetworkcards_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `varchar(10) DEFAULT ''` |
| `speed` | `int NOT NULL DEFAULT '10'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `networkports_id` (`networkports_id`)
KEY `card` (`items_devicenetworkcards_id`)
KEY `type` (`type`)
KEY `speed` (`speed`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_networkportfiberchanneltypes

Origem: [DDL, linha 4991](../install/mysql/glpi-empty.sql#L4991).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_networkportfiberchannels

Origem: [DDL, linha 5007](../install/mysql/glpi-empty.sql#L5007).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `networkports_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_devicenetworkcards_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networkportfiberchanneltypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `wwn` | `varchar(50) DEFAULT ''` |
| `speed` | `int NOT NULL DEFAULT '10'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `networkports_id` (`networkports_id`)
KEY `card` (`items_devicenetworkcards_id`)
KEY `type` (`networkportfiberchanneltypes_id`)
KEY `wwn` (`wwn`)
KEY `speed` (`speed`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_networkportlocals

Origem: [DDL, linha 5030](../install/mysql/glpi-empty.sql#L5030).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `networkports_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `networkports_id` (`networkports_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_networkports

Origem: [DDL, linha 5045](../install/mysql/glpi-empty.sql#L5045).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `logical_number` | `int NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `instantiation_type` | `varchar(255) DEFAULT NULL` |
| `mac` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `ifmtu` | `int NOT NULL DEFAULT '0'` |
| `ifspeed` | `bigint NOT NULL DEFAULT '0'` |
| `ifinternalstatus` | `varchar(255) DEFAULT NULL` |
| `ifconnectionstatus` | `int NOT NULL DEFAULT '0'` |
| `iflastchange` | `varchar(255) DEFAULT NULL` |
| `ifinbytes` | `bigint NOT NULL DEFAULT '0'` |
| `ifinerrors` | `bigint NOT NULL DEFAULT '0'` |
| `ifoutbytes` | `bigint NOT NULL DEFAULT '0'` |
| `ifouterrors` | `bigint NOT NULL DEFAULT '0'` |
| `ifstatus` | `varchar(255) DEFAULT NULL` |
| `ifdescr` | `varchar(255) DEFAULT NULL` |
| `ifalias` | `varchar(255) DEFAULT NULL` |
| `portduplex` | `varchar(255) DEFAULT NULL` |
| `trunk` | `tinyint NOT NULL DEFAULT '0'` |
| `lastup` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `item` (`itemtype`,`items_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `mac` (`mac`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_networkports_networkports

Origem: [DDL, linha 5091](../install/mysql/glpi-empty.sql#L5091).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `networkports_id_1` | `int unsigned NOT NULL DEFAULT '0'` |
| `networkports_id_2` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`networkports_id_1`,`networkports_id_2`)
KEY `networkports_id_2` (`networkports_id_2`)
```

## glpi_networkports_vlans

Origem: [DDL, linha 5104](../install/mysql/glpi-empty.sql#L5104).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `networkports_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `vlans_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `tagged` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`networkports_id`,`vlans_id`)
KEY `vlans_id` (`vlans_id`)
```

## glpi_networkportwifis

Origem: [DDL, linha 5118](../install/mysql/glpi-empty.sql#L5118).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `networkports_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_devicenetworkcards_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `wifinetworks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networkportwifis_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `version` | `varchar(20) DEFAULT NULL` |
| `mode` | `varchar(20) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `networkports_id` (`networkports_id`)
KEY `card` (`items_devicenetworkcards_id`)
KEY `essid` (`wifinetworks_id`)
KEY `version` (`version`)
KEY `mode` (`mode`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `networkportwifis_id` (`networkportwifis_id`)
```

## glpi_networks

Origem: [DDL, linha 5143](../install/mysql/glpi-empty.sql#L5143).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_notepads

Origem: [DDL, linha 5159](../install/mysql/glpi-empty.sql#L5159).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_lastupdater` | `int unsigned NOT NULL DEFAULT '0'` |
| `content` | `longtext` |
| `visible_from_ticket` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`,`items_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `users_id_lastupdater` (`users_id_lastupdater`)
KEY `users_id` (`users_id`)
```

## glpi_notifications

Origem: [DDL, linha 5181](../install/mysql/glpi-empty.sql#L5181).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `event` | `varchar(255) NOT NULL` |
| `comment` | `text` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `allow_response` | `tinyint NOT NULL DEFAULT '1'` |
| `attach_documents` | `tinyint NOT NULL DEFAULT '-2'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `itemtype` (`itemtype`)
KEY `entities_id` (`entities_id`)
KEY `is_active` (`is_active`)
KEY `date_mod` (`date_mod`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
```

## glpi_notifications_notificationtemplates

Origem: [DDL, linha 5209](../install/mysql/glpi-empty.sql#L5209).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `notifications_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `mode` | `varchar(20) NOT NULL` |
| `notificationtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`notifications_id`,`mode`,`notificationtemplates_id`)
KEY `notificationtemplates_id` (`notificationtemplates_id`)
KEY `mode` (`mode`)
```

## glpi_notificationtargets

Origem: [DDL, linha 5225](../install/mysql/glpi-empty.sql#L5225).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '0'` |
| `notifications_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_exclusion` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`notifications_id`,`items_id`,`type`)
KEY `items` (`type`,`items_id`)
KEY `is_exclusion` (`is_exclusion`)
```

## glpi_notificationtemplates

Origem: [DDL, linha 5241](../install/mysql/glpi-empty.sql#L5241).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `itemtype` | `varchar(255) NOT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `css` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `itemtype` (`itemtype`)
KEY `date_mod` (`date_mod`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
```

## glpi_notificationtemplatetranslations

Origem: [DDL, linha 5260](../install/mysql/glpi-empty.sql#L5260).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `notificationtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `language` | `varchar(10) NOT NULL DEFAULT ''` |
| `subject` | `varchar(255) NOT NULL` |
| `content_text` | `longtext` |
| `content_html` | `longtext` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `notificationtemplates_id` (`notificationtemplates_id`)
```

## glpi_notimportedemails

Origem: [DDL, linha 5275](../install/mysql/glpi-empty.sql#L5275).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `from` | `varchar(255) NOT NULL` |
| `to` | `varchar(255) NOT NULL` |
| `mailcollectors_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date` | `timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP` |
| `subject` | `text` |
| `messageid` | `varchar(1000) NOT NULL` |
| `reason` | `int NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `users_id` (`users_id`)
KEY `mailcollectors_id` (`mailcollectors_id`)
```

## glpi_objectlocks

Origem: [DDL, linha 5294](../install/mysql/glpi-empty.sql#L5294).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL` |
| `users_id` | `int unsigned NOT NULL` |
| `date` | `timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `item` (`itemtype`,`items_id`)
KEY `users_id` (`users_id`)
KEY `date` (`date`)
```

## glpi_operatingsystemarchitectures

Origem: [DDL, linha 5310](../install/mysql/glpi-empty.sql#L5310).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_operatingsystems

Origem: [DDL, linha 5326](../install/mysql/glpi-empty.sql#L5326).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_operatingsystemservicepacks

Origem: [DDL, linha 5342](../install/mysql/glpi-empty.sql#L5342).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_operatingsystemversions

Origem: [DDL, linha 5358](../install/mysql/glpi-empty.sql#L5358).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_passivedcequipments

Origem: [DDL, linha 5374](../install/mysql/glpi-empty.sql#L5374).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `passivedcequipmentmodels_id` | `int unsigned DEFAULT NULL` |
| `passivedcequipmenttypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `locations_id` (`locations_id`)
KEY `passivedcequipmentmodels_id` (`passivedcequipmentmodels_id`)
KEY `passivedcequipmenttypes_id` (`passivedcequipmenttypes_id`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `is_template` (`is_template`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `states_id` (`states_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_passivedcequipmentmodels

Origem: [DDL, linha 5415](../install/mysql/glpi-empty.sql#L5415).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `weight` | `int NOT NULL DEFAULT '0'` |
| `required_units` | `int NOT NULL DEFAULT '1'` |
| `depth` | `float NOT NULL DEFAULT '1'` |
| `power_connections` | `int NOT NULL DEFAULT '0'` |
| `power_consumption` | `int NOT NULL DEFAULT '0'` |
| `is_half_rack` | `tinyint NOT NULL DEFAULT '0'` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `product_number` (`product_number`)
```

## glpi_passivedcequipmenttypes

Origem: [DDL, linha 5444](../install/mysql/glpi-empty.sql#L5444).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_peripheralmodels

Origem: [DDL, linha 5458](../install/mysql/glpi-empty.sql#L5458).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `weight` | `int NOT NULL DEFAULT '0'` |
| `required_units` | `int NOT NULL DEFAULT '1'` |
| `depth` | `float NOT NULL DEFAULT '1'` |
| `power_connections` | `int NOT NULL DEFAULT '0'` |
| `power_consumption` | `int NOT NULL DEFAULT '0'` |
| `is_half_rack` | `tinyint NOT NULL DEFAULT '0'` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `product_number` (`product_number`)
```

## glpi_peripherals

Origem: [DDL, linha 5485](../install/mysql/glpi-empty.sql#L5485).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `contact` | `varchar(255) DEFAULT NULL` |
| `contact_num` | `varchar(255) DEFAULT NULL` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `peripheraltypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `peripheralmodels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `brand` | `varchar(255) DEFAULT NULL` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_global` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ticket_tco` | `decimal(20,4) DEFAULT '0.0000'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_template` (`is_template`)
KEY `is_global` (`is_global`)
KEY `entities_id` (`entities_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `users_id` (`users_id`)
KEY `locations_id` (`locations_id`)
KEY `peripheralmodels_id` (`peripheralmodels_id`)
KEY `states_id` (`states_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `peripheraltypes_id` (`peripheraltypes_id`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `date_mod` (`date_mod`)
KEY `is_dynamic` (`is_dynamic`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
KEY `serial` (`serial`)
KEY `otherserial` (`otherserial`)
KEY `uuid` (`uuid`)
KEY `date_creation` (`date_creation`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_peripheraltypes

Origem: [DDL, linha 5540](../install/mysql/glpi-empty.sql#L5540).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_phonemodels

Origem: [DDL, linha 5556](../install/mysql/glpi-empty.sql#L5556).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `product_number` (`product_number`)
```

## glpi_phonepowersupplies

Origem: [DDL, linha 5577](../install/mysql/glpi-empty.sql#L5577).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_phones

Origem: [DDL, linha 5593](../install/mysql/glpi-empty.sql#L5593).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `contact` | `varchar(255) DEFAULT NULL` |
| `contact_num` | `varchar(255) DEFAULT NULL` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `phonetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `phonemodels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `brand` | `varchar(255) DEFAULT NULL` |
| `phonepowersupplies_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `number_line` | `varchar(255) DEFAULT NULL` |
| `have_headset` | `tinyint NOT NULL DEFAULT '0'` |
| `have_hp` | `tinyint NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_global` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ticket_tco` | `decimal(20,4) DEFAULT '0.0000'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `last_inventory_update` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_template` (`is_template`)
KEY `is_global` (`is_global`)
KEY `entities_id` (`entities_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `users_id` (`users_id`)
KEY `locations_id` (`locations_id`)
KEY `phonemodels_id` (`phonemodels_id`)
KEY `phonepowersupplies_id` (`phonepowersupplies_id`)
KEY `states_id` (`states_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `phonetypes_id` (`phonetypes_id`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `date_mod` (`date_mod`)
KEY `is_dynamic` (`is_dynamic`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
KEY `serial` (`serial`)
KEY `otherserial` (`otherserial`)
KEY `uuid` (`uuid`)
KEY `date_creation` (`date_creation`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_phonetypes

Origem: [DDL, linha 5654](../install/mysql/glpi-empty.sql#L5654).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_planningrecalls

Origem: [DDL, linha 5670](../install/mysql/glpi-empty.sql#L5670).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `before_time` | `int NOT NULL DEFAULT '-10'` |
| `when` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`users_id`)
KEY `users_id` (`users_id`)
KEY `before_time` (`before_time`)
KEY `when` (`when`)
```

## glpi_plugins

Origem: [DDL, linha 5688](../install/mysql/glpi-empty.sql#L5688).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `directory` | `varchar(255) NOT NULL` |
| `name` | `varchar(255) NOT NULL` |
| `version` | `varchar(255) NOT NULL` |
| `state` | `int NOT NULL DEFAULT '0'` |
| `author` | `varchar(255) DEFAULT NULL` |
| `highest_available_version` | `varchar(255)` |
| `homepage` | `varchar(255) DEFAULT NULL` |
| `license` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`directory`)
KEY `name` (`name`)
KEY `state` (`state`)
```

## glpi_printermodels

Origem: [DDL, linha 5708](../install/mysql/glpi-empty.sql#L5708).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `product_number` (`product_number`)
```

## glpi_printers

Origem: [DDL, linha 5729](../install/mysql/glpi-empty.sql#L5729).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `contact` | `varchar(255) DEFAULT NULL` |
| `contact_num` | `varchar(255) DEFAULT NULL` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `have_serial` | `tinyint NOT NULL DEFAULT '0'` |
| `have_parallel` | `tinyint NOT NULL DEFAULT '0'` |
| `have_usb` | `tinyint NOT NULL DEFAULT '0'` |
| `have_wifi` | `tinyint NOT NULL DEFAULT '0'` |
| `have_ethernet` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `memory_size` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `printertypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `printermodels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_global` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `init_pages_counter` | `int NOT NULL DEFAULT '0'` |
| `last_pages_counter` | `int NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ticket_tco` | `decimal(20,4) DEFAULT '0.0000'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `sysdescr` | `text` |
| `last_inventory_update` | `timestamp NULL DEFAULT NULL` |
| `snmpcredentials_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_template` (`is_template`)
KEY `is_global` (`is_global`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `users_id` (`users_id`)
KEY `locations_id` (`locations_id`)
KEY `printermodels_id` (`printermodels_id`)
KEY `networks_id` (`networks_id`)
KEY `states_id` (`states_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `printertypes_id` (`printertypes_id`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `date_mod` (`date_mod`)
KEY `last_pages_counter` (`last_pages_counter`)
KEY `is_dynamic` (`is_dynamic`)
KEY `serial` (`serial`)
KEY `otherserial` (`otherserial`)
KEY `uuid` (`uuid`)
KEY `date_creation` (`date_creation`)
KEY `snmpcredentials_id` (`snmpcredentials_id`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
```

## glpi_printertypes

Origem: [DDL, linha 5798](../install/mysql/glpi-empty.sql#L5798).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_problemcosts

Origem: [DDL, linha 5814](../install/mysql/glpi-empty.sql#L5814).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `problems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `begin_date` | `date DEFAULT NULL` |
| `end_date` | `date DEFAULT NULL` |
| `actiontime` | `int NOT NULL DEFAULT '0'` |
| `cost_time` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `cost_fixed` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `cost_material` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `budgets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_lastupdater` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `problems_id` (`problems_id`)
KEY `begin_date` (`begin_date`)
KEY `end_date` (`end_date`)
KEY `entities_id` (`entities_id`)
KEY `budgets_id` (`budgets_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `users_id` (`users_id`)
KEY `users_id_lastupdater` (`users_id_lastupdater`)
```

## glpi_problems

Origem: [DDL, linha 5848](../install/mysql/glpi-empty.sql#L5848).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `status` | `int NOT NULL DEFAULT '1'` |
| `content` | `longtext` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `solvedate` | `timestamp NULL DEFAULT NULL` |
| `closedate` | `timestamp NULL DEFAULT NULL` |
| `time_to_resolve` | `timestamp NULL DEFAULT NULL` |
| `users_id_recipient` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_lastupdater` | `int unsigned NOT NULL DEFAULT '0'` |
| `urgency` | `int NOT NULL DEFAULT '1'` |
| `impact` | `int NOT NULL DEFAULT '1'` |
| `priority` | `int NOT NULL DEFAULT '1'` |
| `itilcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `impactcontent` | `longtext` |
| `causecontent` | `longtext` |
| `symptomcontent` | `longtext` |
| `actiontime` | `int NOT NULL DEFAULT '0'` |
| `begin_waiting_date` | `timestamp NULL DEFAULT NULL` |
| `waiting_duration` | `int NOT NULL DEFAULT '0'` |
| `close_delay_stat` | `int NOT NULL DEFAULT '0'` |
| `solve_delay_stat` | `int NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `problemtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_deleted` (`is_deleted`)
KEY `date` (`date`)
KEY `closedate` (`closedate`)
KEY `status` (`status`)
KEY `priority` (`priority`)
KEY `date_mod` (`date_mod`)
KEY `itilcategories_id` (`itilcategories_id`)
KEY `users_id_recipient` (`users_id_recipient`)
KEY `solvedate` (`solvedate`)
KEY `urgency` (`urgency`)
KEY `impact` (`impact`)
KEY `time_to_resolve` (`time_to_resolve`)
KEY `users_id_lastupdater` (`users_id_lastupdater`)
KEY `date_creation` (`date_creation`)
KEY `problemtemplates_id` (`problemtemplates_id`)
KEY `locations_id` (`locations_id`)
```

## glpi_problems_suppliers

Origem: [DDL, linha 5904](../install/mysql/glpi-empty.sql#L5904).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `problems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `suppliers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |
| `use_notification` | `tinyint NOT NULL DEFAULT '0'` |
| `alternative_email` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`problems_id`,`type`,`suppliers_id`)
KEY `group` (`suppliers_id`,`type`)
```

## glpi_problems_tickets

Origem: [DDL, linha 5920](../install/mysql/glpi-empty.sql#L5920).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `problems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `link` | `int NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`problems_id`,`tickets_id`)
KEY `tickets_id` (`tickets_id`)
```

## glpi_problems_users

Origem: [DDL, linha 5934](../install/mysql/glpi-empty.sql#L5934).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `problems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |
| `use_notification` | `tinyint NOT NULL DEFAULT '0'` |
| `alternative_email` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`problems_id`,`type`,`users_id`,`alternative_email`)
KEY `user` (`users_id`,`type`)
```

## glpi_problemtasks

Origem: [DDL, linha 5950](../install/mysql/glpi-empty.sql#L5950).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `problems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `taskcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `begin` | `timestamp NULL DEFAULT NULL` |
| `end` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_editor` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `content` | `longtext` |
| `actiontime` | `int NOT NULL DEFAULT '0'` |
| `state` | `int NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `tasktemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `timeline_position` | `tinyint NOT NULL DEFAULT '0'` |
| `is_private` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `uuid` (`uuid`)
KEY `problems_id` (`problems_id`)
KEY `users_id` (`users_id`)
KEY `users_id_editor` (`users_id_editor`)
KEY `users_id_tech` (`users_id_tech`)
KEY `groups_id_tech` (`groups_id_tech`)
KEY `date` (`date`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `begin` (`begin`)
KEY `end` (`end`)
KEY `state` (`state`)
KEY `taskcategories_id` (`taskcategories_id`)
KEY `tasktemplates_id` (`tasktemplates_id`)
KEY `is_private` (`is_private`)
```

## glpi_profilerights

Origem: [DDL, linha 5992](../install/mysql/glpi-empty.sql#L5992).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `profiles_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `rights` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`profiles_id`,`name`)
KEY `name` (`name`)
```

## glpi_profiles

Origem: [DDL, linha 6005](../install/mysql/glpi-empty.sql#L6005).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `interface` | `varchar(255) DEFAULT 'helpdesk'` |
| `is_default` | `tinyint NOT NULL DEFAULT '0'` |
| `helpdesk_hardware` | `int NOT NULL DEFAULT '0'` |
| `helpdesk_item_type` | `text` |
| `use_mentions` | `int NOT NULL DEFAULT '1'` |
| `ticket_status` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `problem_status` | `text` |
| `create_ticket_on_login` | `tinyint NOT NULL DEFAULT '0'` |
| `tickettemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `changetemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `problemtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `change_status` | `text` |
| `managed_domainrecordtypes` | `text` |
| `excluded_searchoptions` | `text DEFAULT NULL` |
| `show_map` | `tinyint NOT NULL DEFAULT '1'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `2fa_enforced` | `tinyint NOT NULL DEFAULT '0'` |
| `last_rights_update` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `interface` (`interface`)
KEY `is_default` (`is_default`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `tickettemplates_id` (`tickettemplates_id`)
KEY `changetemplates_id` (`changetemplates_id`)
KEY `problemtemplates_id` (`problemtemplates_id`)
KEY `last_rights_update` (`last_rights_update`)
```

## glpi_profiles_reminders

Origem: [DDL, linha 6044](../install/mysql/glpi-empty.sql#L6044).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `reminders_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `profiles_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned DEFAULT NULL` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `no_entity_restriction` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `reminders_id` (`reminders_id`)
KEY `profiles_id` (`profiles_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_profiles_rssfeeds

Origem: [DDL, linha 6062](../install/mysql/glpi-empty.sql#L6062).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `rssfeeds_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `profiles_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned DEFAULT NULL` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `no_entity_restriction` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `rssfeeds_id` (`rssfeeds_id`)
KEY `profiles_id` (`profiles_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
```

## glpi_profiles_users

Origem: [DDL, linha 6080](../install/mysql/glpi-empty.sql#L6080).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `profiles_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '1'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `is_default_profile` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `profiles_id` (`profiles_id`)
KEY `users_id` (`users_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_dynamic` (`is_dynamic`)
```

## glpi_projectcosts

Origem: [DDL, linha 6100](../install/mysql/glpi-empty.sql#L6100).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `projects_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `begin_date` | `date DEFAULT NULL` |
| `end_date` | `date DEFAULT NULL` |
| `cost` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `budgets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_lastupdater` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `projects_id` (`projects_id`)
KEY `begin_date` (`begin_date`)
KEY `end_date` (`end_date`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `budgets_id` (`budgets_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `users_id` (`users_id`)
KEY `users_id_lastupdater` (`users_id_lastupdater`)
```

## glpi_projects

Origem: [DDL, linha 6133](../install/mysql/glpi-empty.sql#L6133).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `code` | `varchar(255) DEFAULT NULL` |
| `priority` | `int NOT NULL DEFAULT '1'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `projects_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `projectstates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `projecttypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `plan_start_date` | `timestamp NULL DEFAULT NULL` |
| `plan_end_date` | `timestamp NULL DEFAULT NULL` |
| `real_start_date` | `timestamp NULL DEFAULT NULL` |
| `real_end_date` | `timestamp NULL DEFAULT NULL` |
| `percent_done` | `int NOT NULL DEFAULT '0'` |
| `auto_percent_done` | `tinyint NOT NULL DEFAULT '0'` |
| `show_on_global_gantt` | `tinyint NOT NULL DEFAULT '0'` |
| `content` | `longtext` |
| `comment` | `longtext` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `projecttemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `code` (`code`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `projects_id` (`projects_id`)
KEY `projectstates_id` (`projectstates_id`)
KEY `projecttypes_id` (`projecttypes_id`)
KEY `priority` (`priority`)
KEY `date` (`date`)
KEY `date_mod` (`date_mod`)
KEY `users_id` (`users_id`)
KEY `groups_id` (`groups_id`)
KEY `plan_start_date` (`plan_start_date`)
KEY `plan_end_date` (`plan_end_date`)
KEY `real_start_date` (`real_start_date`)
KEY `real_end_date` (`real_end_date`)
KEY `percent_done` (`percent_done`)
KEY `show_on_global_gantt` (`show_on_global_gantt`)
KEY `date_creation` (`date_creation`)
KEY `projecttemplates_id` (`projecttemplates_id`)
KEY `is_template` (`is_template`)
KEY `active_assets` (`is_deleted`, `is_template`)
```

## glpi_projectstates

Origem: [DDL, linha 6190](../install/mysql/glpi-empty.sql#L6190).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `color` | `varchar(255) DEFAULT NULL` |
| `is_finished` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_finished` (`is_finished`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_projecttasks

Origem: [DDL, linha 6209](../install/mysql/glpi-empty.sql#L6209).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `name` | `varchar(255) DEFAULT NULL` |
| `content` | `longtext` |
| `comment` | `longtext` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `projects_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `projecttasks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `plan_start_date` | `timestamp NULL DEFAULT NULL` |
| `plan_end_date` | `timestamp NULL DEFAULT NULL` |
| `real_start_date` | `timestamp NULL DEFAULT NULL` |
| `real_end_date` | `timestamp NULL DEFAULT NULL` |
| `planned_duration` | `int NOT NULL DEFAULT '0'` |
| `effective_duration` | `int NOT NULL DEFAULT '0'` |
| `projectstates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `auto_projectstates` | `tinyint NOT NULL DEFAULT '0'` |
| `projecttasktypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `percent_done` | `int NOT NULL DEFAULT '0'` |
| `auto_percent_done` | `tinyint NOT NULL DEFAULT '0'` |
| `is_milestone` | `tinyint NOT NULL DEFAULT '0'` |
| `recall` | `int` |
| `projecttasktemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `uuid` (`uuid`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `projects_id` (`projects_id`)
KEY `projecttasks_id` (`projecttasks_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `users_id` (`users_id`)
KEY `plan_start_date` (`plan_start_date`)
KEY `plan_end_date` (`plan_end_date`)
KEY `real_start_date` (`real_start_date`)
KEY `real_end_date` (`real_end_date`)
KEY `percent_done` (`percent_done`)
KEY `projectstates_id` (`projectstates_id`)
KEY `projecttasktypes_id` (`projecttasktypes_id`)
KEY `projecttasktemplates_id` (`projecttasktemplates_id`)
KEY `is_template` (`is_template`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `is_milestone` (`is_milestone`)
```

## glpi_projecttasklinks

Origem: [DDL, linha 6266](../install/mysql/glpi-empty.sql#L6266).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `projecttasks_id_source` | `int unsigned NOT NULL` |
| `source_uuid` | `varchar(255) NOT NULL` |
| `projecttasks_id_target` | `int unsigned NOT NULL` |
| `target_uuid` | `varchar(255) NOT NULL` |
| `type` | `tinyint NOT NULL DEFAULT '0'` |
| `lag` | `smallint DEFAULT '0'` |
| `lead` | `smallint DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `projecttasks_id_source` (`projecttasks_id_source`)
KEY `projecttasks_id_target` (`projecttasks_id_target`)
```

## glpi_projecttasktemplates

Origem: [DDL, linha 6283](../install/mysql/glpi-empty.sql#L6283).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `description` | `longtext` |
| `comment` | `longtext` |
| `projects_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `projecttasks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `plan_start_date` | `timestamp NULL DEFAULT NULL` |
| `plan_end_date` | `timestamp NULL DEFAULT NULL` |
| `real_start_date` | `timestamp NULL DEFAULT NULL` |
| `real_end_date` | `timestamp NULL DEFAULT NULL` |
| `planned_duration` | `int NOT NULL DEFAULT '0'` |
| `effective_duration` | `int NOT NULL DEFAULT '0'` |
| `projectstates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `projecttasktypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `percent_done` | `int NOT NULL DEFAULT '0'` |
| `is_milestone` | `tinyint NOT NULL DEFAULT '0'` |
| `comments` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `projects_id` (`projects_id`)
KEY `projecttasks_id` (`projecttasks_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `users_id` (`users_id`)
KEY `plan_start_date` (`plan_start_date`)
KEY `plan_end_date` (`plan_end_date`)
KEY `real_start_date` (`real_start_date`)
KEY `real_end_date` (`real_end_date`)
KEY `percent_done` (`percent_done`)
KEY `projectstates_id` (`projectstates_id`)
KEY `projecttasktypes_id` (`projecttasktypes_id`)
KEY `is_milestone` (`is_milestone`)
```

## glpi_projecttasks_tickets

Origem: [DDL, linha 6329](../install/mysql/glpi-empty.sql#L6329).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `projecttasks_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`tickets_id`,`projecttasks_id`)
KEY `projects_id` (`projecttasks_id`)
```

## glpi_projecttaskteams

Origem: [DDL, linha 6342](../install/mysql/glpi-empty.sql#L6342).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `projecttasks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`projecttasks_id`,`itemtype`,`items_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_projecttasktypes

Origem: [DDL, linha 6356](../install/mysql/glpi-empty.sql#L6356).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_projectteams

Origem: [DDL, linha 6372](../install/mysql/glpi-empty.sql#L6372).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `projects_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`projects_id`,`itemtype`,`items_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_projecttypes

Origem: [DDL, linha 6386](../install/mysql/glpi-empty.sql#L6386).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_queuednotifications

Origem: [DDL, linha 6402](../install/mysql/glpi-empty.sql#L6402).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `notificationtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `sent_try` | `int NOT NULL DEFAULT '0'` |
| `create_time` | `timestamp NULL DEFAULT NULL` |
| `send_time` | `timestamp NULL DEFAULT NULL` |
| `sent_time` | `timestamp NULL DEFAULT NULL` |
| `name` | `text` |
| `sender` | `text` |
| `sendername` | `text` |
| `recipient` | `text` |
| `recipientname` | `text` |
| `replyto` | `text` |
| `replytoname` | `text` |
| `headers` | `text` |
| `body_html` | `longtext` |
| `body_text` | `longtext` |
| `messageid` | `text` |
| `documents` | `text` |
| `mode` | `varchar(20) NOT NULL` |
| `event` | `varchar(255) DEFAULT NULL` |
| `attach_documents` | `tinyint NOT NULL DEFAULT '0'` |
| `itemtype_trigger` | `varchar(255) DEFAULT NULL` |
| `items_id_trigger` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_body_encrypted` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`,`items_id`,`notificationtemplates_id`)
KEY `is_deleted` (`is_deleted`)
KEY `entities_id` (`entities_id`)
KEY `sent_try` (`sent_try`)
KEY `create_time` (`create_time`)
KEY `send_time` (`send_time`)
KEY `sent_time` (`sent_time`)
KEY `mode` (`mode`)
KEY `notificationtemplates_id` (`notificationtemplates_id`)
KEY `recipient` (`recipient`(255))
KEY `item_trigger` (`itemtype_trigger`,`items_id_trigger`)
```

## glpi_registeredids

Origem: [DDL, linha 6449](../install/mysql/glpi-empty.sql#L6449).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `device_type` | `varchar(255) NOT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `item` (`itemtype`,`items_id`)
KEY `device_type` (`device_type`)
```

## glpi_reminders

Origem: [DDL, linha 6465](../install/mysql/glpi-empty.sql#L6465).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `text` | `text` |
| `begin` | `timestamp NULL DEFAULT NULL` |
| `end` | `timestamp NULL DEFAULT NULL` |
| `is_planned` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `state` | `int NOT NULL DEFAULT '0'` |
| `begin_view_date` | `timestamp NULL DEFAULT NULL` |
| `end_view_date` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `uuid` (`uuid`)
KEY `name` (`name`)
KEY `date` (`date`)
KEY `begin` (`begin`)
KEY `end` (`end`)
KEY `users_id` (`users_id`)
KEY `is_planned` (`is_planned`)
KEY `state` (`state`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_remindertranslations

Origem: [DDL, linha 6496](../install/mysql/glpi-empty.sql#L6496).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `reminders_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `language` | `varchar(10) DEFAULT NULL` |
| `name` | `text` |
| `text` | `longtext` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`reminders_id`,`language`)
KEY `users_id` (`users_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_reminders_users

Origem: [DDL, linha 6515](../install/mysql/glpi-empty.sql#L6515).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `reminders_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `reminders_id` (`reminders_id`)
KEY `users_id` (`users_id`)
```

## glpi_requesttypes

Origem: [DDL, linha 6528](../install/mysql/glpi-empty.sql#L6528).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `is_helpdesk_default` | `tinyint NOT NULL DEFAULT '0'` |
| `is_followup_default` | `tinyint NOT NULL DEFAULT '0'` |
| `is_mail_default` | `tinyint NOT NULL DEFAULT '0'` |
| `is_mailfollowup_default` | `tinyint NOT NULL DEFAULT '0'` |
| `is_active` | `tinyint NOT NULL DEFAULT '1'` |
| `is_ticketheader` | `tinyint NOT NULL DEFAULT '1'` |
| `is_itilfollowup` | `tinyint NOT NULL DEFAULT '1'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_helpdesk_default` (`is_helpdesk_default`)
KEY `is_followup_default` (`is_followup_default`)
KEY `is_mail_default` (`is_mail_default`)
KEY `is_mailfollowup_default` (`is_mailfollowup_default`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `is_active` (`is_active`)
KEY `is_ticketheader` (`is_ticketheader`)
KEY `is_itilfollowup` (`is_itilfollowup`)
```

## glpi_reservationitems

Origem: [DDL, linha 6558](../install/mysql/glpi-empty.sql#L6558).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `is_active` | `tinyint NOT NULL DEFAULT '1'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`)
KEY `is_active` (`is_active`)
KEY `item` (`itemtype`,`items_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_reservations

Origem: [DDL, linha 6582](../install/mysql/glpi-empty.sql#L6582).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `reservationitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `begin` | `timestamp NULL DEFAULT NULL` |
| `end` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `group` | `int NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `begin` (`begin`)
KEY `end` (`end`)
KEY `users_id` (`users_id`)
KEY `resagroup` (`reservationitems_id`,`group`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_rssfeeds

Origem: [DDL, linha 6605](../install/mysql/glpi-empty.sql#L6605).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `url` | `text` |
| `refresh_rate` | `int NOT NULL DEFAULT '86400'` |
| `max_items` | `int NOT NULL DEFAULT '20'` |
| `have_error` | `tinyint NOT NULL DEFAULT '0'` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `users_id` (`users_id`)
KEY `date_mod` (`date_mod`)
KEY `have_error` (`have_error`)
KEY `is_active` (`is_active`)
KEY `date_creation` (`date_creation`)
```

## glpi_rssfeeds_users

Origem: [DDL, linha 6630](../install/mysql/glpi-empty.sql#L6630).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `rssfeeds_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `rssfeeds_id` (`rssfeeds_id`)
KEY `users_id` (`users_id`)
```

## glpi_ruleactions

Origem: [DDL, linha 6643](../install/mysql/glpi-empty.sql#L6643).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `rules_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `action_type` | `varchar(255) DEFAULT NULL` |
| `field` | `varchar(255) DEFAULT NULL` |
| `value` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `rules_id` (`rules_id`)
KEY `field_value` (`field`(50),`value`(50))
```

## glpi_rulecriterias

Origem: [DDL, linha 6658](../install/mysql/glpi-empty.sql#L6658).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `rules_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `criteria` | `varchar(255) DEFAULT NULL` |
| `condition` | `int NOT NULL DEFAULT '0'` |
| `pattern` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `rules_id` (`rules_id`)
KEY `condition` (`condition`)
```

## glpi_rulerightparameters

Origem: [DDL, linha 6673](../install/mysql/glpi-empty.sql#L6673).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `value` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_rules

Origem: [DDL, linha 6690](../install/mysql/glpi-empty.sql#L6690).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `sub_type` | `varchar(255) NOT NULL DEFAULT ''` |
| `ranking` | `int NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `description` | `text` |
| `match` | `char(10) DEFAULT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '1'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `condition` | `int NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_active` (`is_active`)
KEY `sub_type` (`sub_type`)
KEY `date_mod` (`date_mod`)
KEY `is_recursive` (`is_recursive`)
KEY `condition` (`condition`)
KEY `date_creation` (`date_creation`)
```

## glpi_slalevelactions

Origem: [DDL, linha 6720](../install/mysql/glpi-empty.sql#L6720).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `slalevels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `action_type` | `varchar(255) DEFAULT NULL` |
| `field` | `varchar(255) DEFAULT NULL` |
| `value` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `slalevels_id` (`slalevels_id`)
```

## glpi_slalevelcriterias

Origem: [DDL, linha 6734](../install/mysql/glpi-empty.sql#L6734).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `slalevels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `criteria` | `varchar(255) DEFAULT NULL` |
| `condition` | `int NOT NULL DEFAULT '0'` |
| `pattern` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `slalevels_id` (`slalevels_id`)
KEY `condition` (`condition`)
```

## glpi_slalevels

Origem: [DDL, linha 6749](../install/mysql/glpi-empty.sql#L6749).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `slas_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `execution_time` | `int NOT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '1'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `match` | `char(10) DEFAULT NULL` |
| `uuid` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_active` (`is_active`)
KEY `slas_id` (`slas_id`)
```

## glpi_slalevels_tickets

Origem: [DDL, linha 6771](../install/mysql/glpi-empty.sql#L6771).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `slalevels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`tickets_id`,`slalevels_id`)
KEY `slalevels_id` (`slalevels_id`)
```

## glpi_olalevelactions

Origem: [DDL, linha 6784](../install/mysql/glpi-empty.sql#L6784).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `olalevels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `action_type` | `varchar(255) DEFAULT NULL` |
| `field` | `varchar(255) DEFAULT NULL` |
| `value` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `olalevels_id` (`olalevels_id`)
```

## glpi_olalevelcriterias

Origem: [DDL, linha 6798](../install/mysql/glpi-empty.sql#L6798).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `olalevels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `criteria` | `varchar(255) DEFAULT NULL` |
| `condition` | `int NOT NULL DEFAULT '0'` |
| `pattern` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `olalevels_id` (`olalevels_id`)
KEY `condition` (`condition`)
```

## glpi_olalevels

Origem: [DDL, linha 6813](../install/mysql/glpi-empty.sql#L6813).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `olas_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `execution_time` | `int NOT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '1'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `match` | `char(10) DEFAULT NULL` |
| `uuid` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_active` (`is_active`)
KEY `olas_id` (`olas_id`)
```

## glpi_olalevels_tickets

Origem: [DDL, linha 6835](../install/mysql/glpi-empty.sql#L6835).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `olalevels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`tickets_id`,`olalevels_id`)
KEY `olalevels_id` (`olalevels_id`)
```

## glpi_slms

Origem: [DDL, linha 6848](../install/mysql/glpi-empty.sql#L6848).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `use_ticket_calendar` | `tinyint NOT NULL DEFAULT '0'` |
| `calendars_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `calendars_id` (`calendars_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_slas

Origem: [DDL, linha 6870](../install/mysql/glpi-empty.sql#L6870).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `number_time` | `int NOT NULL` |
| `use_ticket_calendar` | `tinyint NOT NULL DEFAULT '0'` |
| `calendars_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `definition_time` | `varchar(255) DEFAULT NULL` |
| `end_of_working_day` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `slms_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `calendars_id` (`calendars_id`)
KEY `slms_id` (`slms_id`)
```

## glpi_olas

Origem: [DDL, linha 6898](../install/mysql/glpi-empty.sql#L6898).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `number_time` | `int NOT NULL` |
| `use_ticket_calendar` | `tinyint NOT NULL DEFAULT '0'` |
| `calendars_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `definition_time` | `varchar(255) DEFAULT NULL` |
| `end_of_working_day` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `slms_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `calendars_id` (`calendars_id`)
KEY `slms_id` (`slms_id`)
KEY `groups_id` (`groups_id`)
```

## glpi_items_olas

Origem: [DDL, linha 6928](../install/mysql/glpi-empty.sql#L6928).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `due_time` | `timestamp` |
| `end_time` | `timestamp` |
| `items_id` | `int unsigned NOT NULL` |
| `itemtype` | `varchar(255) NOT NULL` |
| `olas_id` | `int unsigned NOT NULL` |
| `ola_type` | `tinyint NOT NULL` |
| `start_time` | `timestamp` |
| `waiting_time` | `int NOT NULL DEFAULT 0` |
| `waiting_start` | `timestamp` |
| `is_late` | `tinyint NOT NULL DEFAULT 0` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`,`items_id`)
KEY `olas_id` (`olas_id`)
```

## glpi_softwarecategories

Origem: [DDL, linha 6948](../install/mysql/glpi-empty.sql#L6948).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `softwarecategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `completename` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `softwarecategories_id` (`softwarecategories_id`)
KEY `level` (`level`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_softwarelicenses

Origem: [DDL, linha 6971](../install/mysql/glpi-empty.sql#L6971).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `softwares_id` | `int unsigned` |
| `softwarelicenses_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `completename` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `number` | `int NOT NULL DEFAULT '0'` |
| `softwarelicensetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `softwareversions_id_buy` | `int unsigned NOT NULL DEFAULT '0'` |
| `softwareversions_id_use` | `int unsigned NOT NULL DEFAULT '0'` |
| `expire` | `date DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `is_valid` | `tinyint NOT NULL DEFAULT '1'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_helpdesk_visible` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `contact` | `varchar(255) DEFAULT NULL` |
| `contact_num` | `varchar(255) DEFAULT NULL` |
| `allow_overquota` | `tinyint NOT NULL DEFAULT '0'` |
| `pictures` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_template` (`is_template`)
KEY `serial` (`serial`)
KEY `otherserial` (`otherserial`)
KEY `expire` (`expire`)
KEY `softwareversions_id_buy` (`softwareversions_id_buy`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `softwarelicensetypes_id` (`softwarelicensetypes_id`)
KEY `softwareversions_id_use` (`softwareversions_id_use`)
KEY `date_mod` (`date_mod`)
KEY `softwares_id_expire_number` (`softwares_id`,`expire`,`number`)
KEY `locations_id` (`locations_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `users_id` (`users_id`)
KEY `is_helpdesk_visible` (`is_helpdesk_visible`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `date_creation` (`date_creation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `states_id` (`states_id`)
KEY `allow_overquota` (`allow_overquota`)
KEY `softwarelicenses_id` (`softwarelicenses_id`)
KEY `level` (`level`)
```

## glpi_softwarelicensetypes

Origem: [DDL, linha 7036](../install/mysql/glpi-empty.sql#L7036).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `softwarelicensetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `completename` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `softwarelicensetypes_id` (`softwarelicensetypes_id`)
KEY `level` (`level`)
```

## glpi_softwares

Origem: [DDL, linha 7063](../install/mysql/glpi-empty.sql#L7063).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_update` | `tinyint NOT NULL DEFAULT '0'` |
| `softwares_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ticket_tco` | `decimal(20,4) DEFAULT '0.0000'` |
| `is_helpdesk_visible` | `tinyint NOT NULL DEFAULT '1'` |
| `softwarecategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_valid` | `tinyint NOT NULL DEFAULT '1'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `pictures` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `date_mod` (`date_mod`)
KEY `name` (`name`)
KEY `is_template` (`is_template`)
KEY `is_update` (`is_update`)
KEY `softwarecategories_id` (`softwarecategories_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `users_id` (`users_id`)
KEY `locations_id` (`locations_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `softwares_id` (`softwares_id`)
KEY `is_helpdesk_visible` (`is_helpdesk_visible`)
KEY `date_creation` (`date_creation`)
KEY `active_assets` (`is_deleted`,`is_template`)
```

## glpi_softwareversions

Origem: [DDL, linha 7107](../install/mysql/glpi-empty.sql#L7107).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `softwares_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `arch` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `operatingsystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `arch` (`arch`)
KEY `softwares_id` (`softwares_id`)
KEY `states_id` (`states_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `operatingsystems_id` (`operatingsystems_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_solutiontemplates

Origem: [DDL, linha 7135](../install/mysql/glpi-empty.sql#L7135).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `content` | `mediumtext` |
| `solutiontypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_recursive` (`is_recursive`)
KEY `solutiontypes_id` (`solutiontypes_id`)
KEY `entities_id` (`entities_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_solutiontypes

Origem: [DDL, linha 7158](../install/mysql/glpi-empty.sql#L7158).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '1'` |
| `is_incident` | `tinyint NOT NULL DEFAULT '1'` |
| `is_request` | `tinyint NOT NULL DEFAULT '1'` |
| `is_problem` | `tinyint NOT NULL DEFAULT '1'` |
| `is_change` | `tinyint NOT NULL DEFAULT '1'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_incident` (`is_incident`)
KEY `is_request` (`is_request`)
KEY `is_problem` (`is_problem`)
KEY `is_change` (`is_change`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_itilsolutions

Origem: [DDL, linha 7185](../install/mysql/glpi-empty.sql#L7185).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `solutiontypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `solutiontype_name` | `varchar(255) DEFAULT NULL` |
| `content` | `longtext` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_approval` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `user_name` | `varchar(255) DEFAULT NULL` |
| `users_id_editor` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_approval` | `int unsigned NOT NULL DEFAULT '0'` |
| `user_name_approval` | `varchar(255) DEFAULT NULL` |
| `status` | `int NOT NULL DEFAULT '1'` |
| `itilfollowups_id` | `int unsigned DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`,`items_id`)
KEY `solutiontypes_id` (`solutiontypes_id`)
KEY `users_id` (`users_id`)
KEY `users_id_editor` (`users_id_editor`)
KEY `users_id_approval` (`users_id_approval`)
KEY `status` (`status`)
KEY `itilfollowups_id` (`itilfollowups_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_ssovariables

Origem: [DDL, linha 7218](../install/mysql/glpi-empty.sql#L7218).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_states

Origem: [DDL, linha 7234](../install/mysql/glpi-empty.sql#L7234).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `completename` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `is_helpdesk_visible` | `tinyint NOT NULL DEFAULT '1'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`states_id`,`name`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_helpdesk_visible` (`is_helpdesk_visible`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `level` (`level`)
```

## glpi_dropdownvisibilities

Origem: [DDL, linha 7260](../install/mysql/glpi-empty.sql#L7260).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL DEFAULT ''` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `visible_itemtype` | `varchar(255) NOT NULL DEFAULT ''` |
| `is_visible` | `tinyint NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `visible_itemtype` (`visible_itemtype`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_suppliers

Origem: [DDL, linha 7274](../install/mysql/glpi-empty.sql#L7274).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `suppliertypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `registration_number` | `varchar(255) DEFAULT NULL` |
| `address` | `text` |
| `postcode` | `varchar(255) DEFAULT NULL` |
| `town` | `varchar(255) DEFAULT NULL` |
| `state` | `varchar(255) DEFAULT NULL` |
| `country` | `varchar(255) DEFAULT NULL` |
| `website` | `varchar(255) DEFAULT NULL` |
| `phonenumber` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `fax` | `varchar(255) DEFAULT NULL` |
| `email` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `pictures` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `suppliertypes_id` (`suppliertypes_id`)
KEY `is_deleted` (`is_deleted`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `is_active` (`is_active`)
```

## glpi_suppliers_tickets

Origem: [DDL, linha 7311](../install/mysql/glpi-empty.sql#L7311).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `suppliers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |
| `use_notification` | `tinyint NOT NULL DEFAULT '1'` |
| `alternative_email` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`tickets_id`,`type`,`suppliers_id`)
KEY `group` (`suppliers_id`,`type`)
```

## glpi_suppliertypes

Origem: [DDL, linha 7327](../install/mysql/glpi-empty.sql#L7327).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_taskcategories

Origem: [DDL, linha 7343](../install/mysql/glpi-empty.sql#L7343).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `taskcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `completename` | `text` |
| `comment` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `is_active` | `tinyint NOT NULL DEFAULT '1'` |
| `is_helpdeskvisible` | `tinyint NOT NULL DEFAULT '1'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `knowbaseitems_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `taskcategories_id` (`taskcategories_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_active` (`is_active`)
KEY `is_helpdeskvisible` (`is_helpdeskvisible`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `knowbaseitems_id` (`knowbaseitems_id`)
KEY `level` (`level`)
```

## glpi_tasktemplates

Origem: [DDL, linha 7376](../install/mysql/glpi-empty.sql#L7376).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `content` | `mediumtext` |
| `taskcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `actiontime` | `int NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `pendingreasons_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `state` | `int NOT NULL DEFAULT '0'` |
| `is_private` | `tinyint NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `use_current_user` | `tinyint NOT NULL DEFAULT '0'` |
| `groups_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_recursive` (`is_recursive`)
KEY `taskcategories_id` (`taskcategories_id`)
KEY `entities_id` (`entities_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `is_private` (`is_private`)
KEY `users_id_tech` (`users_id_tech`)
KEY `groups_id_tech` (`groups_id_tech`)
KEY `pendingreasons_id` (`pendingreasons_id`)
```

## glpi_ticketcosts

Origem: [DDL, linha 7410](../install/mysql/glpi-empty.sql#L7410).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `begin_date` | `date DEFAULT NULL` |
| `end_date` | `date DEFAULT NULL` |
| `actiontime` | `int NOT NULL DEFAULT '0'` |
| `cost_time` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `cost_fixed` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `cost_material` | `decimal(20,4) NOT NULL DEFAULT '0.0000'` |
| `budgets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_lastupdater` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `tickets_id` (`tickets_id`)
KEY `begin_date` (`begin_date`)
KEY `end_date` (`end_date`)
KEY `entities_id` (`entities_id`)
KEY `budgets_id` (`budgets_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `users_id` (`users_id`)
KEY `users_id_lastupdater` (`users_id_lastupdater`)
```

## glpi_ticketrecurrents

Origem: [DDL, linha 7444](../install/mysql/glpi-empty.sql#L7444).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `tickettemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `begin_date` | `timestamp NULL DEFAULT NULL` |
| `periodicity` | `varchar(255) DEFAULT NULL` |
| `create_before` | `int NOT NULL DEFAULT '0'` |
| `next_creation_date` | `timestamp NULL DEFAULT NULL` |
| `calendars_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `end_date` | `timestamp NULL DEFAULT NULL` |
| `ticket_per_item` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_active` (`is_active`)
KEY `tickettemplates_id` (`tickettemplates_id`)
KEY `next_creation_date` (`next_creation_date`)
KEY `calendars_id` (`calendars_id`)
KEY `ticket_per_item` (`ticket_per_item`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_recurrentchanges

Origem: [DDL, linha 7476](../install/mysql/glpi-empty.sql#L7476).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `changetemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `begin_date` | `timestamp NULL DEFAULT NULL` |
| `periodicity` | `varchar(255) DEFAULT NULL` |
| `create_before` | `int NOT NULL DEFAULT '0'` |
| `next_creation_date` | `timestamp NULL DEFAULT NULL` |
| `calendars_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `end_date` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_active` (`is_active`)
KEY `changetemplates_id` (`changetemplates_id`)
KEY `next_creation_date` (`next_creation_date`)
KEY `calendars_id` (`calendars_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_tickets

Origem: [DDL, linha 7507](../install/mysql/glpi-empty.sql#L7507).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `closedate` | `timestamp NULL DEFAULT NULL` |
| `solvedate` | `timestamp NULL DEFAULT NULL` |
| `takeintoaccountdate` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `users_id_lastupdater` | `int unsigned NOT NULL DEFAULT '0'` |
| `status` | `int NOT NULL DEFAULT '1'` |
| `users_id_recipient` | `int unsigned NOT NULL DEFAULT '0'` |
| `requesttypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `content` | `longtext` |
| `urgency` | `int NOT NULL DEFAULT '1'` |
| `impact` | `int NOT NULL DEFAULT '1'` |
| `priority` | `int NOT NULL DEFAULT '1'` |
| `itilcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |
| `global_validation` | `int NOT NULL DEFAULT '1'` |
| `slas_id_ttr` | `int unsigned NOT NULL DEFAULT '0'` |
| `slas_id_tto` | `int unsigned NOT NULL DEFAULT '0'` |
| `slalevels_id_ttr` | `int unsigned NOT NULL DEFAULT '0'` |
| `time_to_resolve` | `timestamp NULL DEFAULT NULL` |
| `time_to_own` | `timestamp NULL DEFAULT NULL` |
| `begin_waiting_date` | `timestamp NULL DEFAULT NULL` |
| `sla_waiting_duration` | `int NOT NULL DEFAULT '0'` |
| `waiting_duration` | `int NOT NULL DEFAULT '0'` |
| `close_delay_stat` | `int NOT NULL DEFAULT '0'` |
| `solve_delay_stat` | `int NOT NULL DEFAULT '0'` |
| `takeintoaccount_delay_stat` | `int NOT NULL DEFAULT '0'` |
| `actiontime` | `int NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `tickettemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `externalid` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `date` (`date`)
KEY `closedate` (`closedate`)
KEY `status` (`status`)
KEY `priority` (`priority`)
KEY `request_type` (`requesttypes_id`)
KEY `date_mod` (`date_mod`)
KEY `entities_id` (`entities_id`)
KEY `users_id_recipient` (`users_id_recipient`)
KEY `solvedate` (`solvedate`)
KEY `takeintoaccountdate` (`takeintoaccountdate`)
KEY `urgency` (`urgency`)
KEY `impact` (`impact`)
KEY `global_validation` (`global_validation`)
KEY `slas_id_tto` (`slas_id_tto`)
KEY `slas_id_ttr` (`slas_id_ttr`)
KEY `time_to_resolve` (`time_to_resolve`)
KEY `time_to_own` (`time_to_own`)
KEY `slalevels_id_ttr` (`slalevels_id_ttr`)
KEY `users_id_lastupdater` (`users_id_lastupdater`)
KEY `type` (`type`)
KEY `itilcategories_id` (`itilcategories_id`)
KEY `is_deleted` (`is_deleted`)
KEY `name` (`name`)
KEY `locations_id` (`locations_id`)
KEY `date_creation` (`date_creation`)
KEY `tickettemplates_id` (`tickettemplates_id`)
```

## glpi_tickets_tickets

Origem: [DDL, linha 7577](../install/mysql/glpi-empty.sql#L7577).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickets_id_1` | `int unsigned NOT NULL DEFAULT '0'` |
| `tickets_id_2` | `int unsigned NOT NULL DEFAULT '0'` |
| `link` | `int NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`tickets_id_1`,`tickets_id_2`)
KEY `tickets_id_2` (`tickets_id_2`)
```

## glpi_tickets_users

Origem: [DDL, linha 7591](../install/mysql/glpi-empty.sql#L7591).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |
| `use_notification` | `tinyint NOT NULL DEFAULT '1'` |
| `alternative_email` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`tickets_id`,`type`,`users_id`,`alternative_email`)
KEY `user` (`users_id`,`type`)
```

## glpi_ticketsatisfactions

Origem: [DDL, linha 7607](../install/mysql/glpi-empty.sql#L7607).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |
| `date_begin` | `timestamp NULL DEFAULT NULL` |
| `date_answered` | `timestamp NULL DEFAULT NULL` |
| `satisfaction` | `int DEFAULT NULL` |
| `satisfaction_scaled_to_5` | `float DEFAULT NULL` |
| `comment` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `tickets_id` (`tickets_id`)
```

## glpi_tickettasks

Origem: [DDL, linha 7624](../install/mysql/glpi-empty.sql#L7624).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `taskcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_editor` | `int unsigned NOT NULL DEFAULT '0'` |
| `content` | `longtext` |
| `is_private` | `tinyint NOT NULL DEFAULT '0'` |
| `actiontime` | `int NOT NULL DEFAULT '0'` |
| `begin` | `timestamp NULL DEFAULT NULL` |
| `end` | `timestamp NULL DEFAULT NULL` |
| `state` | `int NOT NULL DEFAULT '1'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `tasktemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `timeline_position` | `tinyint NOT NULL DEFAULT '0'` |
| `sourceitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `sourceof_items_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `uuid` (`uuid`)
KEY `date` (`date`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `users_id` (`users_id`)
KEY `users_id_editor` (`users_id_editor`)
KEY `tickets_id` (`tickets_id`)
KEY `is_private` (`is_private`)
KEY `taskcategories_id` (`taskcategories_id`)
KEY `state` (`state`)
KEY `users_id_tech` (`users_id_tech`)
KEY `groups_id_tech` (`groups_id_tech`)
KEY `begin` (`begin`)
KEY `end` (`end`)
KEY `tasktemplates_id` (`tasktemplates_id`)
KEY `sourceitems_id` (`sourceitems_id`)
KEY `sourceof_items_id` (`sourceof_items_id`)
```

## glpi_tickettemplatehiddenfields

Origem: [DDL, linha 7670](../install/mysql/glpi-empty.sql#L7670).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickettemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`tickettemplates_id`,`num`)
```

## glpi_changetemplatehiddenfields

Origem: [DDL, linha 7681](../install/mysql/glpi-empty.sql#L7681).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changetemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`changetemplates_id`,`num`)
```

## glpi_problemtemplatehiddenfields

Origem: [DDL, linha 7692](../install/mysql/glpi-empty.sql#L7692).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `problemtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`problemtemplates_id`,`num`)
```

## glpi_tickettemplatereadonlyfields

Origem: [DDL, linha 7703](../install/mysql/glpi-empty.sql#L7703).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickettemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`tickettemplates_id`,`num`)
```

## glpi_changetemplatereadonlyfields

Origem: [DDL, linha 7714](../install/mysql/glpi-empty.sql#L7714).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changetemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`changetemplates_id`,`num`)
```

## glpi_problemtemplatereadonlyfields

Origem: [DDL, linha 7725](../install/mysql/glpi-empty.sql#L7725).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `problemtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`problemtemplates_id`,`num`)
```

## glpi_tickettemplatemandatoryfields

Origem: [DDL, linha 7736](../install/mysql/glpi-empty.sql#L7736).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickettemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`tickettemplates_id`,`num`)
```

## glpi_changetemplatemandatoryfields

Origem: [DDL, linha 7748](../install/mysql/glpi-empty.sql#L7748).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changetemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`changetemplates_id`,`num`)
```

## glpi_problemtemplatemandatoryfields

Origem: [DDL, linha 7759](../install/mysql/glpi-empty.sql#L7759).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `problemtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`problemtemplates_id`,`num`)
```

## glpi_tickettemplatepredefinedfields

Origem: [DDL, linha 7770](../install/mysql/glpi-empty.sql#L7770).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickettemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |
| `value` | `longtext` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `tickettemplates_id` (`tickettemplates_id`)
```

## glpi_changetemplatepredefinedfields

Origem: [DDL, linha 7782](../install/mysql/glpi-empty.sql#L7782).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changetemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |
| `value` | `longtext` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `changetemplates_id` (`changetemplates_id`)
```

## glpi_problemtemplatepredefinedfields

Origem: [DDL, linha 7794](../install/mysql/glpi-empty.sql#L7794).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `problemtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `num` | `int NOT NULL DEFAULT '0'` |
| `value` | `longtext` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `problemtemplates_id` (`problemtemplates_id`)
```

## glpi_tickettemplates

Origem: [DDL, linha 7808](../install/mysql/glpi-empty.sql#L7808).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `allowed_statuses` | `varchar(255) NOT NULL DEFAULT '[1,10,2,3,4,5,6]'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_changetemplates

Origem: [DDL, linha 7829](../install/mysql/glpi-empty.sql#L7829).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `allowed_statuses` | `varchar(255) NOT NULL DEFAULT '[1,9,10,7,4,11,12,5,8,6,14,13]'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_problemtemplates

Origem: [DDL, linha 7849](../install/mysql/glpi-empty.sql#L7849).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `allowed_statuses` | `varchar(255) NOT NULL DEFAULT '[1,7,2,3,4,5,8,6]'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_ticketvalidations

Origem: [DDL, linha 7869](../install/mysql/glpi-empty.sql#L7869).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itils_validationsteps_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_validate` | `int unsigned NOT NULL DEFAULT '0'` |
| `itilvalidationtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype_target` | `varchar(255) NOT NULL` |
| `items_id_target` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment_submission` | `text` |
| `comment_validation` | `text` |
| `status` | `int NOT NULL DEFAULT '2'` |
| `submission_date` | `timestamp NULL DEFAULT NULL` |
| `validation_date` | `timestamp NULL DEFAULT NULL` |
| `timeline_position` | `tinyint NOT NULL DEFAULT '0'` |
| `last_reminder_date` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `users_id` (`users_id`)
KEY `users_id_validate` (`users_id_validate`)
KEY `itilvalidationtemplates_id` (`itilvalidationtemplates_id`)
KEY `item_target` (`itemtype_target`,`items_id_target`)
KEY `tickets_id` (`tickets_id`)
KEY `submission_date` (`submission_date`)
KEY `validation_date` (`validation_date`)
KEY `status` (`status`)
KEY `itils_validationsteps_id` (`itils_validationsteps_id`)
```

## glpi_validationsteps

Origem: [DDL, linha 7903](../install/mysql/glpi-empty.sql#L7903).

`ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned          NOT NULL    AUTO_INCREMENT` |
| `name` | `varchar(255)                      DEFAULT NULL` |
| `minimal_required_validation_percent` | `tinyint unsigned      NOT NULL    DEFAULT '100'` |
| `is_default` | `tinyint               NOT NULL    DEFAULT '0'` |
| `date_mod` | `timestamp             NULL        DEFAULT NULL` |
| `date_creation` | `timestamp             NULL        DEFAULT NULL` |
| `comment` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_itils_validationsteps

Origem: [DDL, linha 7920](../install/mysql/glpi-empty.sql#L7920).

`ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned        NOT NULL AUTO_INCREMENT` |
| `minimal_required_validation_percent` | `tinyint unsigned    NOT NULL` |
| `validationsteps_id` | `int unsigned        NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255)        NOT NULL` |
| `items_id` | `int unsigned        NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`validationsteps_id`)
KEY `validationsteps_id` (`validationsteps_id`)
```

## glpi_transfers

Origem: [DDL, linha 7934](../install/mysql/glpi-empty.sql#L7934).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `keep_ticket` | `int NOT NULL DEFAULT '0'` |
| `keep_networklink` | `int NOT NULL DEFAULT '0'` |
| `keep_reservation` | `int NOT NULL DEFAULT '0'` |
| `keep_history` | `int NOT NULL DEFAULT '0'` |
| `keep_device` | `int NOT NULL DEFAULT '0'` |
| `keep_infocom` | `int NOT NULL DEFAULT '0'` |
| `keep_dc_monitor` | `int NOT NULL DEFAULT '0'` |
| `clean_dc_monitor` | `int NOT NULL DEFAULT '0'` |
| `keep_dc_phone` | `int NOT NULL DEFAULT '0'` |
| `clean_dc_phone` | `int NOT NULL DEFAULT '0'` |
| `keep_dc_peripheral` | `int NOT NULL DEFAULT '0'` |
| `clean_dc_peripheral` | `int NOT NULL DEFAULT '0'` |
| `keep_dc_printer` | `int NOT NULL DEFAULT '0'` |
| `clean_dc_printer` | `int NOT NULL DEFAULT '0'` |
| `keep_supplier` | `int NOT NULL DEFAULT '0'` |
| `clean_supplier` | `int NOT NULL DEFAULT '0'` |
| `keep_contact` | `int NOT NULL DEFAULT '0'` |
| `clean_contact` | `int NOT NULL DEFAULT '0'` |
| `keep_contract` | `int NOT NULL DEFAULT '0'` |
| `clean_contract` | `int NOT NULL DEFAULT '0'` |
| `keep_software` | `int NOT NULL DEFAULT '0'` |
| `clean_software` | `int NOT NULL DEFAULT '0'` |
| `keep_document` | `int NOT NULL DEFAULT '0'` |
| `clean_document` | `int NOT NULL DEFAULT '0'` |
| `keep_cartridgeitem` | `int NOT NULL DEFAULT '0'` |
| `clean_cartridgeitem` | `int NOT NULL DEFAULT '0'` |
| `keep_cartridge` | `int NOT NULL DEFAULT '0'` |
| `keep_consumable` | `int NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `keep_disk` | `int NOT NULL DEFAULT '0'` |
| `keep_certificate` | `int NOT NULL DEFAULT '0'` |
| `clean_certificate` | `int NOT NULL DEFAULT '0'` |
| `lock_updated_fields` | `int NOT NULL DEFAULT '0'` |
| `keep_location` | `int NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_usercategories

Origem: [DDL, linha 7983](../install/mysql/glpi-empty.sql#L7983).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_useremails

Origem: [DDL, linha 7999](../install/mysql/glpi-empty.sql#L7999).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_default` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `email` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`users_id`,`email`)
KEY `email` (`email`)
KEY `is_default` (`is_default`)
KEY `is_dynamic` (`is_dynamic`)
```

## glpi_users

Origem: [DDL, linha 8016](../install/mysql/glpi-empty.sql#L8016).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `password` | `varchar(255) DEFAULT NULL` |
| `password_last_update` | `timestamp NULL DEFAULT NULL` |
| `phone` | `varchar(255) DEFAULT NULL` |
| `phone2` | `varchar(255) DEFAULT NULL` |
| `mobile` | `varchar(255) DEFAULT NULL` |
| `realname` | `varchar(255) DEFAULT NULL` |
| `firstname` | `varchar(255) DEFAULT NULL` |
| `middlename` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `language` | `char(10) DEFAULT NULL` |
| `use_mode` | `int NOT NULL DEFAULT '0'` |
| `list_limit` | `int DEFAULT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '1'` |
| `comment` | `text` |
| `auths_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `authtype` | `int NOT NULL DEFAULT '0'` |
| `last_login` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_sync` | `timestamp NULL DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `profiles_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned DEFAULT '0'` |
| `usertitles_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `usercategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_format` | `int DEFAULT NULL` |
| `number_format` | `int DEFAULT NULL` |
| `names_format` | `int DEFAULT NULL` |
| `csv_delimiter` | `char(1) DEFAULT NULL` |
| `is_ids_visible` | `tinyint DEFAULT NULL` |
| `use_flat_dropdowntree` | `tinyint DEFAULT NULL` |
| `use_flat_dropdowntree_on_search_result` | `tinyint DEFAULT NULL` |
| `show_jobs_at_login` | `tinyint DEFAULT NULL` |
| `priority_1` | `char(20) DEFAULT NULL` |
| `priority_2` | `char(20) DEFAULT NULL` |
| `priority_3` | `char(20) DEFAULT NULL` |
| `priority_4` | `char(20) DEFAULT NULL` |
| `priority_5` | `char(20) DEFAULT NULL` |
| `priority_6` | `char(20) DEFAULT NULL` |
| `followup_private` | `tinyint DEFAULT NULL` |
| `task_private` | `tinyint DEFAULT NULL` |
| `default_requesttypes_id` | `int unsigned DEFAULT NULL` |
| `password_forget_token` | `varchar(255) DEFAULT NULL` |
| `password_forget_token_date` | `timestamp NULL DEFAULT NULL` |
| `user_dn` | `text` |
| `user_dn_hash` | `varchar(32)` |
| `registration_number` | `varchar(255) DEFAULT NULL` |
| `show_count_on_tabs` | `tinyint DEFAULT NULL` |
| `refresh_views` | `int DEFAULT NULL` |
| `set_default_tech` | `tinyint DEFAULT NULL` |
| `set_followup_tech` | `tinyint DEFAULT NULL` |
| `set_solution_tech` | `tinyint DEFAULT NULL` |
| `personal_token` | `varchar(255) DEFAULT NULL` |
| `personal_token_date` | `timestamp NULL DEFAULT NULL` |
| `api_token` | `varchar(255) DEFAULT NULL` |
| `api_token_date` | `timestamp NULL DEFAULT NULL` |
| `display_count_on_home` | `int DEFAULT NULL` |
| `notification_to_myself` | `tinyint DEFAULT NULL` |
| `duedateok_color` | `varchar(255) DEFAULT NULL` |
| `duedatewarning_color` | `varchar(255) DEFAULT NULL` |
| `duedatecritical_color` | `varchar(255) DEFAULT NULL` |
| `duedatewarning_less` | `int DEFAULT NULL` |
| `duedatecritical_less` | `int DEFAULT NULL` |
| `duedatewarning_unit` | `varchar(255) DEFAULT NULL` |
| `duedatecritical_unit` | `varchar(255) DEFAULT NULL` |
| `is_deleted_ldap` | `tinyint NOT NULL DEFAULT '0'` |
| `pdffont` | `varchar(255) DEFAULT NULL` |
| `picture` | `varchar(255) DEFAULT NULL` |
| `begin_date` | `timestamp NULL DEFAULT NULL` |
| `end_date` | `timestamp NULL DEFAULT NULL` |
| `keep_devices_when_purging_item` | `tinyint DEFAULT NULL` |
| `privatebookmarkorder` | `longtext` |
| `backcreated` | `tinyint DEFAULT NULL` |
| `task_state` | `int DEFAULT NULL` |
| `planned_task_state` | `int DEFAULT NULL` |
| `palette` | `char(20) DEFAULT NULL` |
| `page_layout` | `char(20) DEFAULT NULL` |
| `fold_menu` | `tinyint DEFAULT NULL` |
| `savedsearches_pinned` | `text` |
| `timeline_order` | `char(20) DEFAULT NULL` |
| `itil_layout` | `text` |
| `unfolded_knowbaseitems` | `json` |
| `richtext_layout` | `char(20) DEFAULT NULL` |
| `set_default_requester` | `tinyint DEFAULT NULL` |
| `lock_autolock_mode` | `tinyint DEFAULT NULL` |
| `lock_directunlock_notification` | `tinyint DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `highcontrast_css` | `tinyint DEFAULT '0'` |
| `plannings` | `text` |
| `sync_field` | `varchar(255) DEFAULT NULL` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_supervisor` | `int unsigned NOT NULL DEFAULT '0'` |
| `timezone` | `varchar(50) DEFAULT NULL` |
| `default_dashboard_central` | `varchar(100) DEFAULT NULL` |
| `default_dashboard_assets` | `varchar(100) DEFAULT NULL` |
| `default_dashboard_helpdesk` | `varchar(100) DEFAULT NULL` |
| `default_dashboard_mini_ticket` | `varchar(100) DEFAULT NULL` |
| `default_central_tab` | `tinyint DEFAULT '0'` |
| `nickname` | `varchar(255) DEFAULT NULL` |
| `substitution_end_date` | `timestamp NULL DEFAULT NULL` |
| `substitution_start_date` | `timestamp NULL DEFAULT NULL` |
| `toast_location` | `varchar(255) DEFAULT NULL` |
| `timeline_action_btn_layout` | `tinyint DEFAULT NULL` |
| `timeline_date_format` | `tinyint DEFAULT NULL` |
| `2fa` | `text` |
| `2fa_unenforced` | `tinyint NOT NULL DEFAULT 0 COMMENT 'If 1, the user is excluded from 2FA enforcement policies'` |
| `password_history` | `longtext` |
| `is_notif_enable_default` | `tinyint DEFAULT NULL` |
| `show_search_form` | `tinyint DEFAULT NULL` |
| `search_pagination_on_top` | `tinyint DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicityloginauth` (`name`,`authtype`,`auths_id`)
KEY `firstname` (`firstname`)
KEY `middlename` (`middlename`)
KEY `realname` (`realname`)
KEY `entities_id` (`entities_id`)
KEY `profiles_id` (`profiles_id`)
KEY `locations_id` (`locations_id`)
KEY `usertitles_id` (`usertitles_id`)
KEY `usercategories_id` (`usercategories_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_active` (`is_active`)
KEY `date_mod` (`date_mod`)
KEY `authitem` (`authtype`,`auths_id`)
KEY `is_deleted_ldap` (`is_deleted_ldap`)
KEY `date_creation` (`date_creation`)
KEY `begin_date` (`begin_date`)
KEY `end_date` (`end_date`)
KEY `sync_field` (`sync_field`)
KEY `groups_id` (`groups_id`)
KEY `users_id_supervisor` (`users_id_supervisor`)
KEY `auths_id` (`auths_id`)
KEY `default_requesttypes_id` (`default_requesttypes_id`)
KEY `user_dn_hash` (`user_dn_hash`)
KEY `substitution_end_date` (`substitution_end_date`)
KEY `substitution_start_date` (`substitution_start_date`)
```

## glpi_usertitles

Origem: [DDL, linha 8160](../install/mysql/glpi-empty.sql#L8160).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_virtualmachinestates

Origem: [DDL, linha 8176](../install/mysql/glpi-empty.sql#L8176).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_virtualmachinesystems

Origem: [DDL, linha 8192](../install/mysql/glpi-empty.sql#L8192).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_virtualmachinetypes

Origem: [DDL, linha 8208](../install/mysql/glpi-empty.sql#L8208).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_vlans

Origem: [DDL, linha 8224](../install/mysql/glpi-empty.sql#L8224).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `tag` | `int NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `tag` (`tag`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_wifinetworks

Origem: [DDL, linha 8246](../install/mysql/glpi-empty.sql#L8246).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `essid` | `varchar(255) DEFAULT NULL` |
| `mode` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `essid` (`essid`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_knowbaseitems_items

Origem: [DDL, linha 8268](../install/mysql/glpi-empty.sql#L8268).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `knowbaseitems_id` | `int unsigned NOT NULL` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`knowbaseitems_id`)
KEY `knowbaseitems_id` (`knowbaseitems_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_knowbaseitems_revisions

Origem: [DDL, linha 8285](../install/mysql/glpi-empty.sql#L8285).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `knowbaseitems_id` | `int unsigned NOT NULL` |
| `revision` | `int NOT NULL` |
| `name` | `text` |
| `answer` | `longtext` |
| `language` | `varchar(10) DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`knowbaseitems_id`,`revision`,`language`)
KEY `revision` (`revision`)
KEY `users_id` (`users_id`)
KEY `date` (`date`)
```

## glpi_knowbaseitems_comments

Origem: [DDL, linha 8304](../install/mysql/glpi-empty.sql#L8304).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `knowbaseitems_id` | `int unsigned NOT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `language` | `varchar(10) DEFAULT NULL` |
| `comment` | `text` |
| `parent_comment_id` | `int unsigned DEFAULT NULL` |
| `anchor_prefix` | `varchar(255) DEFAULT NULL` |
| `anchor_exact` | `varchar(1000) DEFAULT NULL` |
| `anchor_suffix` | `varchar(255) DEFAULT NULL` |
| `anchor_occurrence` | `int DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `knowbaseitems_id` (`knowbaseitems_id`)
KEY `parent_comment_id` (`parent_comment_id`)
KEY `users_id` (`users_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_devicebatterymodels

Origem: [DDL, linha 8328](../install/mysql/glpi-empty.sql#L8328).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicebatteries

Origem: [DDL, linha 8348](../install/mysql/glpi-empty.sql#L8348).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `voltage` | `int DEFAULT NULL` |
| `capacity` | `int DEFAULT NULL` |
| `devicebatterytypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicebatterymodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicebatterymodels_id` (`devicebatterymodels_id`)
KEY `devicebatterytypes_id` (`devicebatterytypes_id`)
```

## glpi_items_devicebatteries

Origem: [DDL, linha 8375](../install/mysql/glpi-empty.sql#L8375).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicebatteries_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturing_date` | `date DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `real_capacity` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicebatteries_id` (`devicebatteries_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_devicebatterytypes

Origem: [DDL, linha 8404](../install/mysql/glpi-empty.sql#L8404).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_devicefirmwaremodels

Origem: [DDL, linha 8419](../install/mysql/glpi-empty.sql#L8419).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_devicefirmwares

Origem: [DDL, linha 8436](../install/mysql/glpi-empty.sql#L8436).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `designation` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date` | `date DEFAULT NULL` |
| `version` | `varchar(255) DEFAULT NULL` |
| `devicefirmwaretypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `devicefirmwaremodels_id` | `int unsigned DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `designation` (`designation`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `devicefirmwaremodels_id` (`devicefirmwaremodels_id`)
KEY `devicefirmwaretypes_id` (`devicefirmwaretypes_id`)
```

## glpi_items_devicefirmwares

Origem: [DDL, linha 8463](../install/mysql/glpi-empty.sql#L8463).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `devicefirmwares_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `devicefirmwares_id` (`devicefirmwares_id`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `serial` (`serial`)
KEY `item` (`itemtype`,`items_id`)
KEY `otherserial` (`otherserial`)
KEY `locations_id` (`locations_id`)
KEY `states_id` (`states_id`)
```

## glpi_devicefirmwaretypes

Origem: [DDL, linha 8490](../install/mysql/glpi-empty.sql#L8490).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_datacenters

Origem: [DDL, linha 8506](../install/mysql/glpi-empty.sql#L8506).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `pictures` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `locations_id` (`locations_id`)
KEY `is_deleted` (`is_deleted`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_dcrooms

Origem: [DDL, linha 8527](../install/mysql/glpi-empty.sql#L8527).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `vis_cols` | `int DEFAULT NULL` |
| `vis_rows` | `int DEFAULT NULL` |
| `vis_cell_width` | `int NOT NULL DEFAULT '40'` |
| `vis_cell_height` | `int NOT NULL DEFAULT '40'` |
| `column_labels` | `text` |
| `row_labels` | `text` |
| `blueprint` | `text` |
| `datacenters_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `locations_id` (`locations_id`)
KEY `datacenters_id` (`datacenters_id`)
KEY `is_deleted` (`is_deleted`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_rackmodels

Origem: [DDL, linha 8556](../install/mysql/glpi-empty.sql#L8556).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `pictures` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_racktypes

Origem: [DDL, linha 8572](../install/mysql/glpi-empty.sql#L8572).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_racks

Origem: [DDL, linha 8589](../install/mysql/glpi-empty.sql#L8589).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `rackmodels_id` | `int unsigned DEFAULT NULL` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `racktypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `width` | `int DEFAULT NULL` |
| `height` | `int DEFAULT NULL` |
| `depth` | `int DEFAULT NULL` |
| `number_units` | `int DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `dcrooms_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `room_orientation` | `int NOT NULL DEFAULT '0'` |
| `position` | `varchar(50) DEFAULT NULL` |
| `bgcolor` | `varchar(7) DEFAULT NULL` |
| `max_power` | `int NOT NULL DEFAULT '0'` |
| `mesured_power` | `int NOT NULL DEFAULT '0'` |
| `max_weight` | `int NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `locations_id` (`locations_id`)
KEY `rackmodels_id` (`rackmodels_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `racktypes_id` (`racktypes_id`)
KEY `states_id` (`states_id`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `is_template` (`is_template`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `dcrooms_id` (`dcrooms_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_items_racks

Origem: [DDL, linha 8639](../install/mysql/glpi-empty.sql#L8639).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `racks_id` | `int unsigned NOT NULL` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL` |
| `position` | `int NOT NULL` |
| `orientation` | `tinyint DEFAULT NULL` |
| `bgcolor` | `varchar(7) DEFAULT NULL` |
| `hpos` | `tinyint NOT NULL DEFAULT '0'` |
| `is_reserved` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `item` (`itemtype`,`items_id`,`is_reserved`)
KEY `relation` (`racks_id`,`itemtype`,`items_id`)
```

## glpi_enclosuremodels

Origem: [DDL, linha 8655](../install/mysql/glpi-empty.sql#L8655).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `weight` | `int NOT NULL DEFAULT '0'` |
| `required_units` | `int NOT NULL DEFAULT '1'` |
| `depth` | `float NOT NULL DEFAULT '1'` |
| `power_connections` | `int NOT NULL DEFAULT '0'` |
| `power_consumption` | `int NOT NULL DEFAULT '0'` |
| `is_half_rack` | `tinyint NOT NULL DEFAULT '0'` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `product_number` (`product_number`)
```

## glpi_enclosures

Origem: [DDL, linha 8679](../install/mysql/glpi-empty.sql#L8679).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `enclosuremodels_id` | `int unsigned DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `orientation` | `tinyint DEFAULT NULL` |
| `power_supplies` | `tinyint NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `locations_id` (`locations_id`)
KEY `enclosuremodels_id` (`enclosuremodels_id`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `is_template` (`is_template`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `states_id` (`states_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_items_enclosures

Origem: [DDL, linha 8717](../install/mysql/glpi-empty.sql#L8717).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `enclosures_id` | `int unsigned NOT NULL` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL` |
| `position` | `int NOT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `item` (`itemtype`,`items_id`)
KEY `relation` (`enclosures_id`,`itemtype`,`items_id`)
```

## glpi_pdumodels

Origem: [DDL, linha 8729](../install/mysql/glpi-empty.sql#L8729).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `weight` | `int NOT NULL DEFAULT '0'` |
| `required_units` | `int NOT NULL DEFAULT '1'` |
| `depth` | `float NOT NULL DEFAULT '1'` |
| `power_connections` | `int NOT NULL DEFAULT '0'` |
| `max_power` | `int NOT NULL DEFAULT '0'` |
| `is_half_rack` | `tinyint NOT NULL DEFAULT '0'` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `is_rackable` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_rackable` (`is_rackable`)
KEY `product_number` (`product_number`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_pdutypes

Origem: [DDL, linha 8755](../install/mysql/glpi-empty.sql#L8755).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_pdus

Origem: [DDL, linha 8773](../install/mysql/glpi-empty.sql#L8773).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `pdumodels_id` | `int unsigned DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `sysdescr` | `text` |
| `last_inventory_update` | `timestamp NULL DEFAULT NULL` |
| `snmpcredentials_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `pdutypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `locations_id` (`locations_id`)
KEY `pdumodels_id` (`pdumodels_id`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `is_template` (`is_template`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `states_id` (`states_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `pdutypes_id` (`pdutypes_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `snmpcredentials_id` (`snmpcredentials_id`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
KEY `is_dynamic` (`is_dynamic`)
```

## glpi_plugtypes

Origem: [DDL, linha 8819](../install/mysql/glpi-empty.sql#L8819).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_plugs

Origem: [DDL, linha 8836](../install/mysql/glpi-empty.sql#L8836).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `custom_name` | `varchar(255) DEFAULT NULL` |
| `number` | `int NOT NULL DEFAULT '0'` |
| `plugtypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype_main` | `varchar(255) DEFAULT NULL` |
| `items_id_main` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype_asset` | `varchar(255) NOT NULL DEFAULT ''` |
| `items_id_asset` | `int unsigned NOT NULL DEFAULT '0'` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `asset_item` (`itemtype_asset`, `items_id_asset`)
KEY `main_item` (`itemtype_main`, `items_id_main`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
KEY `is_dynamic` (`is_dynamic`)
KEY `plugtypes_id` (`plugtypes_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_deleted` (`is_deleted`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_pdus_racks

Origem: [DDL, linha 8869](../install/mysql/glpi-empty.sql#L8869).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `racks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `pdus_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `side` | `int DEFAULT '0'` |
| `position` | `int NOT NULL` |
| `bgcolor` | `varchar(7) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `racks_id` (`racks_id`)
KEY `pdus_id` (`pdus_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_itilfollowuptemplates

Origem: [DDL, linha 8887](../install/mysql/glpi-empty.sql#L8887).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `content` | `mediumtext` |
| `requesttypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_private` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `pendingreasons_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_recursive` (`is_recursive`)
KEY `requesttypes_id` (`requesttypes_id`)
KEY `entities_id` (`entities_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `is_private` (`is_private`)
KEY `pendingreasons_id` (`pendingreasons_id`)
```

## glpi_itilfollowups

Origem: [DDL, linha 8911](../install/mysql/glpi-empty.sql#L8911).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_editor` | `int unsigned NOT NULL DEFAULT '0'` |
| `content` | `longtext` |
| `is_private` | `tinyint NOT NULL DEFAULT '0'` |
| `requesttypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `timeline_position` | `tinyint NOT NULL DEFAULT '0'` |
| `sourceitems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `sourceof_items_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`,`items_id`)
KEY `date` (`date`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `users_id` (`users_id`)
KEY `users_id_editor` (`users_id_editor`)
KEY `is_private` (`is_private`)
KEY `requesttypes_id` (`requesttypes_id`)
KEY `sourceitems_id` (`sourceitems_id`)
KEY `sourceof_items_id` (`sourceof_items_id`)
```

## glpi_clustertypes

Origem: [DDL, linha 8940](../install/mysql/glpi-empty.sql#L8940).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_clusters

Origem: [DDL, linha 8957](../install/mysql/glpi-empty.sql#L8957).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `version` | `varchar(255) DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `clustertypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `is_deleted` (`is_deleted`)
KEY `states_id` (`states_id`)
KEY `clustertypes_id` (`clustertypes_id`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_items_clusters

Origem: [DDL, linha 8988](../install/mysql/glpi-empty.sql#L8988).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `clusters_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`clusters_id`,`itemtype`,`items_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_planningexternalevents

Origem: [DDL, linha 9001](../install/mysql/glpi-empty.sql#L9001).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `planningexternaleventtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '1'` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_guests` | `text` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `text` | `text` |
| `begin` | `timestamp NULL DEFAULT NULL` |
| `end` | `timestamp NULL DEFAULT NULL` |
| `rrule` | `text` |
| `state` | `int NOT NULL DEFAULT '0'` |
| `planningeventcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `background` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `uuid` (`uuid`)
KEY `name` (`name`)
KEY `planningexternaleventtemplates_id` (`planningexternaleventtemplates_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date` (`date`)
KEY `begin` (`begin`)
KEY `end` (`end`)
KEY `users_id` (`users_id`)
KEY `groups_id` (`groups_id`)
KEY `state` (`state`)
KEY `planningeventcategories_id` (`planningeventcategories_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_planningexternaleventtemplates

Origem: [DDL, linha 9041](../install/mysql/glpi-empty.sql#L9041).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `text` | `mediumtext` |
| `comment` | `text` |
| `duration` | `int NOT NULL DEFAULT '0'` |
| `before_time` | `int NOT NULL DEFAULT '0'` |
| `rrule` | `text` |
| `state` | `int NOT NULL DEFAULT '0'` |
| `planningeventcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `background` | `tinyint NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `state` (`state`)
KEY `planningeventcategories_id` (`planningeventcategories_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_planningeventcategories

Origem: [DDL, linha 9067](../install/mysql/glpi-empty.sql#L9067).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `color` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_items_kanbans

Origem: [DDL, linha 9083](../install/mysql/glpi-empty.sql#L9083).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL` |
| `state` | `mediumtext` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`users_id`)
KEY `users_id` (`users_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_vobjects

Origem: [DDL, linha 9101](../install/mysql/glpi-empty.sql#L9101).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `data` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`)
KEY `item` (`itemtype`,`items_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_domaintypes

Origem: [DDL, linha 9116](../install/mysql/glpi-empty.sql#L9116).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_domainrelations

Origem: [DDL, linha 9133](../install/mysql/glpi-empty.sql#L9133).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_domains_items

Origem: [DDL, linha 9150](../install/mysql/glpi-empty.sql#L9150).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `domains_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `domainrelations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`domains_id`,`itemtype`,`items_id`)
KEY `domainrelations_id` (`domainrelations_id`)
KEY `item` (`itemtype`,`items_id`)
KEY `is_dynamic` (`is_dynamic`)
KEY `is_deleted` (`is_deleted`)
```

## glpi_domainrecordtypes

Origem: [DDL, linha 9167](../install/mysql/glpi-empty.sql#L9167).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `fields` | `text` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_domainrecords

Origem: [DDL, linha 9185](../install/mysql/glpi-empty.sql#L9185).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `data` | `text` |
| `data_obj` | `text` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `domains_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `domainrecordtypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ttl` | `int NOT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `domains_id` (`domains_id`)
KEY `domainrecordtypes_id` (`domainrecordtypes_id`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `date_mod` (`date_mod`)
KEY `is_deleted` (`is_deleted`)
KEY `date_creation` (`date_creation`)
```

## glpi_appliances

Origem: [DDL, linha 9215](../install/mysql/glpi-empty.sql#L9215).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `appliancetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `applianceenvironments_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `externalidentifier` | `varchar(255) DEFAULT NULL` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `contact` | `varchar(255) DEFAULT NULL` |
| `contact_num` | `varchar(255) DEFAULT NULL` |
| `is_helpdesk_visible` | `tinyint NOT NULL DEFAULT '1'` |
| `pictures` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`externalidentifier`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `name` (`name`)
KEY `is_deleted` (`is_deleted`)
KEY `appliancetypes_id` (`appliancetypes_id`)
KEY `locations_id` (`locations_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `applianceenvironments_id` (`applianceenvironments_id`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `states_id` (`states_id`)
KEY `serial` (`serial`)
KEY `otherserial` (`otherserial`)
KEY `is_helpdesk_visible` (`is_helpdesk_visible`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_appliances_items

Origem: [DDL, linha 9259](../install/mysql/glpi-empty.sql#L9259).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `appliances_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL DEFAULT ''` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`appliances_id`,`items_id`,`itemtype`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_appliancetypes

Origem: [DDL, linha 9270](../install/mysql/glpi-empty.sql#L9270).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `comment` | `text` |
| `externalidentifier` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `externalidentifier` (`externalidentifier`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_applianceenvironments

Origem: [DDL, linha 9289](../install/mysql/glpi-empty.sql#L9289).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_appliances_items_relations

Origem: [DDL, linha 9302](../install/mysql/glpi-empty.sql#L9302).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `appliances_items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `appliances_items_id` (`appliances_items_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_agenttypes

Origem: [DDL, linha 9313](../install/mysql/glpi-empty.sql#L9313).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_agents

Origem: [DDL, linha 9325](../install/mysql/glpi-empty.sql#L9325).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `deviceid` | `varchar(255) NOT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `agenttypes_id` | `int unsigned NOT NULL` |
| `last_contact` | `timestamp NULL DEFAULT NULL` |
| `version` | `varchar(255) DEFAULT NULL` |
| `locked` | `tinyint NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL` |
| `useragent` | `varchar(255) DEFAULT NULL` |
| `tag` | `varchar(255) DEFAULT NULL` |
| `port` | `varchar(6) DEFAULT NULL` |
| `remote_addr` | `varchar(255) DEFAULT NULL` |
| `threads_networkdiscovery` | `int NOT NULL DEFAULT '1'` |
| `threads_networkinventory` | `int NOT NULL DEFAULT '1'` |
| `timeout_networkdiscovery` | `int NOT NULL DEFAULT '0'` |
| `timeout_networkinventory` | `int NOT NULL DEFAULT '0'` |
| `use_module_wake_on_lan` | `tinyint NOT NULL DEFAULT '0'` |
| `use_module_computer_inventory` | `tinyint NOT NULL DEFAULT '0'` |
| `use_module_esx_remote_inventory` | `tinyint NOT NULL DEFAULT '0'` |
| `use_module_remote_inventory` | `tinyint NOT NULL DEFAULT '0'` |
| `use_module_network_inventory` | `tinyint NOT NULL DEFAULT '0'` |
| `use_module_network_discovery` | `tinyint NOT NULL DEFAULT '0'` |
| `use_module_package_deployment` | `tinyint NOT NULL DEFAULT '0'` |
| `use_module_collect_data` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `deviceid` (`deviceid`)
KEY `name` (`name`)
KEY `agenttypes_id` (`agenttypes_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_rulematchedlogs

Origem: [DDL, linha 9363](../install/mysql/glpi-empty.sql#L9363).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `rules_id` | `int unsigned DEFAULT NULL` |
| `agents_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `method` | `varchar(255) DEFAULT NULL` |
| `input` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `agents_id` (`agents_id`)
KEY `item` (`itemtype`,`items_id`)
KEY `rules_id` (`rules_id`)
```

## glpi_lockedfields

Origem: [DDL, linha 9379](../install/mysql/glpi-empty.sql#L9379).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `field` | `varchar(50) NOT NULL` |
| `value` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `is_global` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`field`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `is_global` (`is_global`)
```

## glpi_unmanageds

Origem: [DDL, linha 9396](../install/mysql/glpi-empty.sql#L9396).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `contact` | `varchar(255) DEFAULT NULL` |
| `contact_num` | `varchar(255) DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `networks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `sysdescr` | `text` |
| `agents_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `accepted` | `tinyint NOT NULL DEFAULT '0'` |
| `hub` | `tinyint NOT NULL DEFAULT '0'` |
| `ip` | `varchar(255) DEFAULT NULL` |
| `snmpcredentials_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `last_inventory_update` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `users_id` (`users_id`)
KEY `locations_id` (`locations_id`)
KEY `networks_id` (`networks_id`)
KEY `states_id` (`states_id`)
KEY `is_deleted` (`is_deleted`)
KEY `date_mod` (`date_mod`)
KEY `is_dynamic` (`is_dynamic`)
KEY `serial` (`serial`)
KEY `otherserial` (`otherserial`)
KEY `date_creation` (`date_creation`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
KEY `agents_id` (`agents_id`)
KEY `snmpcredentials_id` (`snmpcredentials_id`)
KEY `users_id_tech` (`users_id_tech`)
```

## glpi_networkporttypes

Origem: [DDL, linha 9447](../install/mysql/glpi-empty.sql#L9447).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `value_decimal` | `int NOT NULL` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `is_importable` | `tinyint NOT NULL DEFAULT '0'` |
| `instantiation_type` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `value_decimal` (`value_decimal`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_importable` (`is_importable`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_printerlogs

Origem: [DDL, linha 9470](../install/mysql/glpi-empty.sql#L9470).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `total_pages` | `int NOT NULL DEFAULT '0'` |
| `bw_pages` | `int NOT NULL DEFAULT '0'` |
| `color_pages` | `int NOT NULL DEFAULT '0'` |
| `rv_pages` | `int NOT NULL DEFAULT '0'` |
| `prints` | `int NOT NULL DEFAULT '0'` |
| `bw_prints` | `int NOT NULL DEFAULT '0'` |
| `color_prints` | `int NOT NULL DEFAULT '0'` |
| `copies` | `int NOT NULL DEFAULT '0'` |
| `bw_copies` | `int NOT NULL DEFAULT '0'` |
| `color_copies` | `int NOT NULL DEFAULT '0'` |
| `scanned` | `int NOT NULL DEFAULT '0'` |
| `date` | `date DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `faxed` | `int NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`date`)
KEY `date` (`date`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_networkportconnectionlogs

Origem: [DDL, linha 9498](../install/mysql/glpi-empty.sql#L9498).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `date` | `timestamp NULL DEFAULT NULL` |
| `connected` | `tinyint NOT NULL DEFAULT '0'` |
| `networkports_id_source` | `int unsigned NOT NULL DEFAULT '0'` |
| `networkports_id_destination` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `date` (`date`)
KEY `networkports_id_source` (`networkports_id_source`)
KEY `networkports_id_destination` (`networkports_id_destination`)
```

## glpi_networkportmetrics

Origem: [DDL, linha 9512](../install/mysql/glpi-empty.sql#L9512).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `date` | `date DEFAULT NULL` |
| `ifinbytes` | `bigint NOT NULL DEFAULT '0'` |
| `ifinerrors` | `bigint NOT NULL DEFAULT '0'` |
| `ifoutbytes` | `bigint NOT NULL DEFAULT '0'` |
| `ifouterrors` | `bigint NOT NULL DEFAULT '0'` |
| `networkports_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`networkports_id`,`date`)
KEY `date` (`date`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_refusedequipments

Origem: [DDL, linha 9530](../install/mysql/glpi-empty.sql#L9530).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ip` | `text` |
| `mac` | `text` |
| `rules_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `method` | `varchar(255) DEFAULT NULL` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `agents_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `agents_id` (`agents_id`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
KEY `rules_id` (`rules_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_usbvendors

Origem: [DDL, linha 9556](../install/mysql/glpi-empty.sql#L9556).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `vendorid` | `varchar(4) NOT NULL` |
| `deviceid` | `varchar(4) DEFAULT NULL` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`vendorid`,`deviceid`)
KEY `deviceid` (`deviceid`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_pcivendors

Origem: [DDL, linha 9577](../install/mysql/glpi-empty.sql#L9577).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `vendorid` | `varchar(4) NOT NULL` |
| `deviceid` | `varchar(4) DEFAULT NULL` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`vendorid`,`deviceid`)
KEY `deviceid` (`deviceid`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_items_remotemanagements

Origem: [DDL, linha 9598](../install/mysql/glpi-empty.sql#L9598).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `remoteid` | `varchar(255) DEFAULT NULL` |
| `type` | `varchar(255) DEFAULT NULL` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `is_dynamic` (`is_dynamic`)
KEY `is_deleted` (`is_deleted`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_pendingreasons

Origem: [DDL, linha 9613](../install/mysql/glpi-empty.sql#L9613).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `is_default` | `tinyint NOT NULL DEFAULT '0'` |
| `is_pending_per_default` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `followup_frequency` | `int NOT NULL DEFAULT '0'` |
| `followups_before_resolution` | `int NOT NULL DEFAULT '0'` |
| `itilfollowuptemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `solutiontemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `calendars_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `itilfollowuptemplates_id` (`itilfollowuptemplates_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `solutiontemplates_id` (`solutiontemplates_id`)
KEY `calendars_id` (`calendars_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_pendingreasons_items

Origem: [DDL, linha 9640](../install/mysql/glpi-empty.sql#L9640).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `pendingreasons_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL DEFAULT ''` |
| `followup_frequency` | `int NOT NULL DEFAULT '0'` |
| `followups_before_resolution` | `int NOT NULL DEFAULT '0'` |
| `bump_count` | `int NOT NULL DEFAULT '0'` |
| `last_bump_date` | `timestamp NULL DEFAULT NULL` |
| `previous_status` | `int DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`items_id`,`itemtype`)
KEY `pendingreasons_id` (`pendingreasons_id`)
KEY `item` (`itemtype`,`items_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_manuallinks

Origem: [DDL, linha 9661](../install/mysql/glpi-empty.sql#L9661).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `url` | `varchar(8096) NOT NULL` |
| `open_window` | `tinyint NOT NULL DEFAULT '1'` |
| `icon` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `item` (`itemtype`,`items_id`)
KEY `items_id` (`items_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_tickets_contracts

Origem: [DDL, linha 9681](../install/mysql/glpi-empty.sql#L9681).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `tickets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `contracts_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`tickets_id`,`contracts_id`)
KEY `contracts_id` (`contracts_id`)
```

## glpi_databaseinstancetypes

Origem: [DDL, linha 9691](../install/mysql/glpi-empty.sql#L9691).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_databaseinstancecategories

Origem: [DDL, linha 9704](../install/mysql/glpi-empty.sql#L9704).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_databaseinstances

Origem: [DDL, linha 9718](../install/mysql/glpi-empty.sql#L9718).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `version` | `varchar(255) NOT NULL DEFAULT ''` |
| `port` | `varchar(10) NOT NULL DEFAULT ''` |
| `path` | `varchar(255) NOT NULL DEFAULT ''` |
| `databaseinstancetypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `databaseinstancecategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL DEFAULT ''` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_onbackup` | `tinyint NOT NULL DEFAULT '0'` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_helpdesk_visible` | `tinyint NOT NULL DEFAULT '1'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_lastboot` | `timestamp NULL DEFAULT NULL` |
| `date_lastbackup` | `timestamp NULL DEFAULT NULL` |
| `comment` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `name` (`name`)
KEY `databaseinstancetypes_id` (`databaseinstancetypes_id`)
KEY `databaseinstancecategories_id` (`databaseinstancecategories_id`)
KEY `locations_id` (`locations_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `states_id` (`states_id`)
KEY `item` (`itemtype`,`items_id`)
KEY `is_active` (`is_active`)
KEY `is_deleted` (`is_deleted`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `is_helpdesk_visible` (`is_helpdesk_visible`)
KEY `is_dynamic` (`is_dynamic`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
```

## glpi_databases

Origem: [DDL, linha 9768](../install/mysql/glpi-empty.sql#L9768).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `size` | `int NOT NULL DEFAULT '0'` |
| `databaseinstances_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_onbackup` | `tinyint NOT NULL DEFAULT '0'` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_update` | `timestamp NULL DEFAULT NULL` |
| `date_lastbackup` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `name` (`name`)
KEY `is_active` (`is_active`)
KEY `is_deleted` (`is_deleted`)
KEY `is_dynamic` (`is_dynamic`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `databaseinstances_id` (`databaseinstances_id`)
```

## glpi_snmpcredentials

Origem: [DDL, linha 9797](../install/mysql/glpi-empty.sql#L9797).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(64) DEFAULT NULL` |
| `snmpversion` | `varchar(8) NOT NULL DEFAULT '1'` |
| `community` | `varchar(255) DEFAULT NULL` |
| `username` | `varchar(255) DEFAULT NULL` |
| `authentication` | `varchar(255) DEFAULT NULL` |
| `auth_passphrase` | `varchar(255) DEFAULT NULL` |
| `encryption` | `varchar(255) DEFAULT NULL` |
| `priv_passphrase` | `varchar(255) DEFAULT NULL` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `snmpversion` (`snmpversion`)
KEY `is_deleted` (`is_deleted`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_forms_categories

Origem: [DDL, linha 9819](../install/mysql/glpi-empty.sql#L9819).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `description` | `longtext` |
| `illustration` | `varchar(255) NOT NULL DEFAULT ''` |
| `forms_categories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `completename` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `comment` | `text` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `level` (`level`)
KEY `forms_categories_id` (`forms_categories_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_forms_forms

Origem: [DDL, linha 9841](../install/mysql/glpi-empty.sql#L9841).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `uuid` | `varchar(255) NOT NULL DEFAULT ''` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_draft` | `tinyint NOT NULL DEFAULT '0'` |
| `is_pinned` | `tinyint NOT NULL DEFAULT '0'` |
| `render_layout` | `varchar(30) NOT NULL DEFAULT ''` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `header` | `longtext` |
| `illustration` | `varchar(255) NOT NULL DEFAULT ''` |
| `description` | `longtext` |
| `forms_categories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `usage_count` | `int unsigned NOT NULL DEFAULT '0'` |
| `submit_button_visibility_strategy` | `varchar(30) NOT NULL DEFAULT ''` |
| `submit_button_conditions` | `JSON NOT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `uuid` (`uuid`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `is_active` (`is_active`)
KEY `is_deleted` (`is_deleted`)
KEY `is_draft` (`is_draft`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `forms_categories_id` (`forms_categories_id`)
```

## glpi_forms_sections

Origem: [DDL, linha 9875](../install/mysql/glpi-empty.sql#L9875).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `uuid` | `varchar(255) NOT NULL DEFAULT ''` |
| `forms_forms_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `description` | `longtext` |
| `rank` | `int NOT NULL DEFAULT '0'` |
| `visibility_strategy` | `varchar(30) NOT NULL DEFAULT ''` |
| `conditions` | `JSON NOT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `uuid` (`uuid`)
KEY `name` (`name`)
KEY `forms_forms_id` (`forms_forms_id`)
```

## glpi_forms_questions

Origem: [DDL, linha 9891](../install/mysql/glpi-empty.sql#L9891).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `uuid` | `varchar(255) NOT NULL DEFAULT ''` |
| `forms_sections_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `forms_sections_uuid` | `varchar(255) NOT NULL DEFAULT ''` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `type` | `varchar(255) NOT NULL DEFAULT ''` |
| `is_mandatory` | `tinyint NOT NULL DEFAULT '0'` |
| `vertical_rank` | `int NOT NULL DEFAULT '0'` |
| `horizontal_rank` | `int DEFAULT NULL` |
| `description` | `longtext` |
| `default_value` | `text COMMENT 'JSON - The default value type may not be the same for all questions type'` |
| `extra_data` | `text COMMENT 'JSON - Extra configuration field(s) depending on the questions type'` |
| `visibility_strategy` | `varchar(30) NOT NULL DEFAULT ''` |
| `conditions` | `JSON NOT NULL` |
| `validation_strategy` | `varchar(30) NOT NULL DEFAULT ''` |
| `validation_conditions` | `JSON NOT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `uuid` (`uuid`)
KEY `name` (`name`)
KEY `forms_sections_id` (`forms_sections_id`)
KEY `forms_sections_uuid` (`forms_sections_uuid`)
```

## glpi_forms_comments

Origem: [DDL, linha 9916](../install/mysql/glpi-empty.sql#L9916).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `uuid` | `varchar(255) NOT NULL DEFAULT ''` |
| `forms_sections_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `forms_sections_uuid` | `varchar(255) NOT NULL DEFAULT ''` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `description` | `longtext` |
| `vertical_rank` | `int NOT NULL DEFAULT '0'` |
| `horizontal_rank` | `int DEFAULT NULL` |
| `visibility_strategy` | `varchar(30) NOT NULL DEFAULT ''` |
| `conditions` | `JSON NOT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `uuid` (`uuid`)
KEY `name` (`name`)
KEY `forms_sections_id` (`forms_sections_id`)
KEY `forms_sections_uuid` (`forms_sections_uuid`)
```

## glpi_forms_answerssets

Origem: [DDL, linha 9935](../install/mysql/glpi-empty.sql#L9935).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `forms_forms_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `index` | `int NOT NULL DEFAULT '0'` |
| `answers` | `json COMMENT 'JSON - Answers for each questions of the parent form'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `forms_forms_id` (`forms_forms_id`)
KEY `users_id` (`users_id`)
KEY `entities_id` (`entities_id`)
```

## glpi_forms_destinations_answerssets_formdestinationitems

Origem: [DDL, linha 9955](../install/mysql/glpi-empty.sql#L9955).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `forms_answerssets_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`forms_answerssets_id`,`itemtype`,`items_id`)
KEY `item` (`itemtype`, `items_id`)
```

## glpi_forms_destinations_formdestinations

Origem: [DDL, linha 9966](../install/mysql/glpi-empty.sql#L9966).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `forms_forms_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `name` | `varchar(255) NOT NULL` |
| `config` | `JSON NOT NULL COMMENT 'Extra configuration field(s) depending on the destination type'` |
| `creation_strategy` | `varchar(30) NOT NULL DEFAULT ''` |
| `conditions` | `JSON NOT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `itemtype` (`itemtype`)
KEY `forms_forms_id` (`forms_forms_id`)
```

## glpi_forms_accesscontrols_formaccesscontrols

Origem: [DDL, linha 9981](../install/mysql/glpi-empty.sql#L9981).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `forms_forms_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `strategy` | `varchar(255) NOT NULL` |
| `config` | `JSON NOT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`forms_forms_id`, `strategy`)
KEY `is_active` (`is_active`)
```

## glpi_items_ticketrecurrents

Origem: [DDL, linha 9993](../install/mysql/glpi-empty.sql#L9993).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `ticketrecurrents_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`,`ticketrecurrents_id`)
KEY `items_id` (`items_id`)
KEY `ticketrecurrents_id` (`ticketrecurrents_id`)
```

## glpi_items_lines

Origem: [DDL, linha 10005](../install/mysql/glpi-empty.sql#L10005).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `lines_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`lines_id`,`itemtype`,`items_id`)
KEY `item` (`itemtype`,`items_id`)
```

## glpi_changes_changes

Origem: [DDL, linha 10016](../install/mysql/glpi-empty.sql#L10016).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changes_id_1` | `int unsigned NOT NULL DEFAULT '0'` |
| `changes_id_2` | `int unsigned NOT NULL DEFAULT '0'` |
| `link` | `int NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`changes_id_1`,`changes_id_2`)
KEY `changes_id_2` (`changes_id_2`)
```

## glpi_problems_problems

Origem: [DDL, linha 10027](../install/mysql/glpi-empty.sql#L10027).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `problems_id_1` | `int unsigned NOT NULL DEFAULT '0'` |
| `problems_id_2` | `int unsigned NOT NULL DEFAULT '0'` |
| `link` | `int NOT NULL DEFAULT '1'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`problems_id_1`,`problems_id_2`)
KEY `problems_id_2` (`problems_id_2`)
```

## glpi_changesatisfactions

Origem: [DDL, linha 10038](../install/mysql/glpi-empty.sql#L10038).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `changes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `int NOT NULL DEFAULT '1'` |
| `date_begin` | `timestamp NULL DEFAULT NULL` |
| `date_answered` | `timestamp NULL DEFAULT NULL` |
| `satisfaction` | `int DEFAULT NULL` |
| `satisfaction_scaled_to_5` | `float DEFAULT NULL` |
| `comment` | `text` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `changes_id` (`changes_id`)
```

## glpi_oauth_access_tokens

Origem: [DDL, linha 10052](../install/mysql/glpi-empty.sql#L10052).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `identifier` | `varchar(255) NOT NULL` |
| `uuid` | `varchar(255) NOT NULL` |
| `client` | `varchar(255) NOT NULL` |
| `date_expiration` | `timestamp NOT NULL` |
| `user_identifier` | `varchar(255) DEFAULT NULL` |
| `scopes` | `text DEFAULT NULL` |
| `ip_address` | `varchar(45) DEFAULT NULL` |
| `user_agent` | `varchar(512) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`identifier`)
UNIQUE KEY `uuid` (`uuid`)
KEY `client` (`client`)
```

## glpi_oauth_refresh_tokens

Origem: [DDL, linha 10067](../install/mysql/glpi-empty.sql#L10067).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `identifier` | `varchar(255) NOT NULL` |
| `access_token` | `varchar(255) NOT NULL` |
| `date_expiration` | `timestamp NOT NULL` |
| `ip_address` | `varchar(45) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`identifier`)
KEY `access_token` (`access_token`)
```

## glpi_oauth_auth_codes

Origem: [DDL, linha 10077](../install/mysql/glpi-empty.sql#L10077).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `identifier` | `varchar(255) NOT NULL` |
| `client` | `varchar(255) NOT NULL` |
| `date_expiration` | `timestamp NOT NULL` |
| `user_identifier` | `varchar(255) DEFAULT NULL` |
| `scopes` | `text DEFAULT NULL` |
| `ip_address` | `varchar(45) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`identifier`)
KEY `client` (`client`)
```

## glpi_oauthclients

Origem: [DDL, linha 10089](../install/mysql/glpi-empty.sql#L10089).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `identifier` | `varchar(255) NOT NULL` |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT COMMENT 'Internal GLPI ID'` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `comment` | `text DEFAULT NULL` |
| `secret` | `varchar(255) NOT NULL` |
| `redirect_uri` | `TEXT NOT NULL` |
| `grants` | `text NOT NULL` |
| `scopes` | `text NOT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '1'` |
| `is_confidential` | `tinyint NOT NULL DEFAULT '1'` |
| `allowed_ips` | `text DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`identifier`)
KEY `id` (`id`)
KEY `name` (`name`)
KEY `is_active` (`is_active`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_validatorsubstitutes

Origem: [DDL, linha 10112](../install/mysql/glpi-empty.sql#L10112).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `users_id` | `int unsigned  NOT NULL DEFAULT '0' COMMENT 'Delegator user'` |
| `users_id_substitute` | `int unsigned  NOT NULL DEFAULT '0' COMMENT 'Substitute user'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `users_id_users_id_substitute` (`users_id`, `users_id_substitute`)
KEY `users_id_substitute` (`users_id_substitute`)
```

## glpi_searches_criteriafilters

Origem: [DDL, linha 10122](../install/mysql/glpi-empty.sql#L10122).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `search_itemtype` | `varchar(255) DEFAULT NULL` |
| `search_criteria` | `longtext DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `item` (`itemtype`, `items_id`)
KEY `search_itemtype` (`search_itemtype`)
```

## glpi_itilvalidationtemplates

Origem: [DDL, linha 10134](../install/mysql/glpi-empty.sql#L10134).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `validationsteps_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) NOT NULL DEFAULT ''` |
| `content` | `text` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `name` (`name`)
KEY `validationsteps_id` (`validationsteps_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_itilvalidationtemplates_targets

Origem: [DDL, linha 10154](../install/mysql/glpi-empty.sql#L10154).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itilvalidationtemplates_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `groups_id` | `int unsigned DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `itilvalidationtemplates_id` (`itilvalidationtemplates_id`)
KEY `item` (`itemtype`,`items_id`)
KEY `groups_id` (`groups_id`)
```

## glpi_itilreminders

Origem: [DDL, linha 10167](../install/mysql/glpi-empty.sql#L10167).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `pendingreasons_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `content` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`,`items_id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `pendingreasons_id` (`pendingreasons_id`)
```

## glpi_defaultfilters

Origem: [DDL, linha 10185](../install/mysql/glpi-empty.sql#L10185).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `is_active` | `tinyint NOT NULL DEFAULT '1'` |
| `comment` | `text DEFAULT NULL` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `itemtype` (`itemtype`)
KEY `name` (`name`)
KEY `is_active` (`is_active`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_webhooks

Origem: [DDL, linha 10202](../install/mysql/glpi-empty.sql#L10202).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `webhookcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `event` | `varchar(255) DEFAULT NULL` |
| `payload` | `longtext` |
| `use_default_payload` | `tinyint NOT NULL DEFAULT '1'` |
| `custom_headers` | `text` |
| `url` | `text DEFAULT NULL` |
| `secret` | `text` |
| `use_cra_challenge` | `tinyint NOT NULL DEFAULT '0'` |
| `http_method` | `varchar(255) DEFAULT 'POST'` |
| `sent_try` | `tinyint NOT NULL DEFAULT '3'` |
| `expiration` | `int NOT NULL DEFAULT '0'` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `save_response_body` | `tinyint NOT NULL DEFAULT '0'` |
| `log_in_item_history` | `tinyint NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `use_oauth` | `tinyint NOT NULL DEFAULT '0'` |
| `oauth_url` | `varchar(255) DEFAULT NULL` |
| `clientid` | `varchar(255) DEFAULT NULL` |
| `clientsecret` | `varchar(255) DEFAULT NULL` |
| `pinned_version` | `varchar(255) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `name` (`name`)
KEY `is_active` (`is_active`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `use_cra_challenge` (`use_cra_challenge`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `webhookcategories_id` (`webhookcategories_id`)
```

## glpi_webhookcategories

Origem: [DDL, linha 10242](../install/mysql/glpi-empty.sql#L10242).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `webhookcategories_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `completename` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`webhookcategories_id`,`name`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `level` (`level`)
```

## glpi_queuedwebhooks

Origem: [DDL, linha 10262](../install/mysql/glpi-empty.sql#L10262).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) DEFAULT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `sent_try` | `int NOT NULL DEFAULT '0'` |
| `webhooks_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `url` | `text DEFAULT NULL` |
| `create_time` | `timestamp NULL DEFAULT NULL` |
| `send_time` | `timestamp NULL DEFAULT NULL` |
| `sent_time` | `timestamp NULL DEFAULT NULL` |
| `headers` | `text` |
| `body` | `longtext` |
| `event` | `varchar(255) DEFAULT NULL` |
| `last_status_code` | `int DEFAULT NULL` |
| `save_response_body` | `tinyint NOT NULL DEFAULT '0'` |
| `response_body` | `longtext` |
| `http_method` | `varchar(255) DEFAULT 'POST'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `item` (`itemtype`,`items_id`)
KEY `entities_id` (`entities_id`)
KEY `webhooks_id` (`webhooks_id`)
KEY `is_deleted` (`is_deleted`)
KEY `sent_try` (`sent_try`)
KEY `create_time` (`create_time`)
KEY `send_time` (`send_time`)
KEY `sent_time` (`sent_time`)
```

## glpi_stencils

Origem: [DDL, linha 10293](../install/mysql/glpi-empty.sql#L10293).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `nb_zones` | `int NOT NULL DEFAULT '1'` |
| `zones` | `JSON` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`itemtype`,`items_id`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_assets_assetdefinitions

Origem: [DDL, linha 10308](../install/mysql/glpi-empty.sql#L10308).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `system_name` | `varchar(255) DEFAULT NULL` |
| `label` | `varchar(255) NOT NULL` |
| `icon` | `varchar(255) DEFAULT NULL` |
| `picture` | `text` |
| `comment` | `text` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `capacities` | `JSON NOT NULL` |
| `profiles` | `JSON NOT NULL` |
| `translations` | `JSON NOT NULL` |
| `fields_display` | `JSON NOT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `system_name` (`system_name`)
KEY `label` (`label`)
KEY `is_active` (`is_active`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_assets_assets

Origem: [DDL, linha 10331](../install/mysql/glpi-empty.sql#L10331).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `assets_assetdefinitions_id` | `int unsigned NOT NULL` |
| `assets_assetmodels_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `assets_assettypes_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `uuid` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `serial` | `varchar(255) DEFAULT NULL` |
| `otherserial` | `varchar(255) DEFAULT NULL` |
| `contact` | `varchar(255) DEFAULT NULL` |
| `contact_num` | `varchar(255) DEFAULT NULL` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id_tech` | `int unsigned NOT NULL DEFAULT '0'` |
| `locations_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `manufacturers_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `states_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `is_deleted` | `tinyint NOT NULL DEFAULT '0'` |
| `is_template` | `tinyint NOT NULL DEFAULT '0'` |
| `is_dynamic` | `tinyint NOT NULL DEFAULT '0'` |
| `template_name` | `varchar(255) DEFAULT NULL` |
| `autoupdatesystems_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `last_inventory_update` | `timestamp NULL DEFAULT NULL` |
| `custom_fields` | `json` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `assets_assetdefinitions_id` (`assets_assetdefinitions_id`)
KEY `assets_assetmodels_id` (`assets_assetmodels_id`)
KEY `assets_assettypes_id` (`assets_assettypes_id`)
KEY `name` (`name`)
KEY `uuid` (`uuid`)
KEY `users_id` (`users_id`)
KEY `users_id_tech` (`users_id_tech`)
KEY `locations_id` (`locations_id`)
KEY `manufacturers_id` (`manufacturers_id`)
KEY `states_id` (`states_id`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `active_assets` (`is_deleted`, `is_template`)
KEY `is_template` (`is_template`)
KEY `is_dynamic` (`is_dynamic`)
KEY `autoupdatesystems_id` (`autoupdatesystems_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_assets_assetmodels

Origem: [DDL, linha 10381](../install/mysql/glpi-empty.sql#L10381).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `assets_assetdefinitions_id` | `int unsigned NOT NULL` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `product_number` | `varchar(255) DEFAULT NULL` |
| `weight` | `int NOT NULL DEFAULT '0'` |
| `required_units` | `int NOT NULL DEFAULT '1'` |
| `depth` | `float NOT NULL DEFAULT '1'` |
| `power_connections` | `int NOT NULL DEFAULT '0'` |
| `power_consumption` | `int NOT NULL DEFAULT '0'` |
| `max_power` | `int NOT NULL DEFAULT '0'` |
| `is_half_rack` | `tinyint NOT NULL DEFAULT '0'` |
| `picture_front` | `text` |
| `picture_rear` | `text` |
| `pictures` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `assets_assetdefinitions_id` (`assets_assetdefinitions_id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
KEY `product_number` (`product_number`)
```

## glpi_assets_assettypes

Origem: [DDL, linha 10408](../install/mysql/glpi-empty.sql#L10408).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `assets_assetdefinitions_id` | `int unsigned NOT NULL` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `assets_assetdefinitions_id` (`assets_assetdefinitions_id`)
KEY `name` (`name`)
KEY `date_mod` (`date_mod`)
KEY `date_creation` (`date_creation`)
```

## glpi_groups_items

Origem: [DDL, linha 10423](../install/mysql/glpi-empty.sql#L10423).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `groups_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL DEFAULT ''` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `type` | `tinyint NOT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`groups_id`,`itemtype`,`items_id`, `type`)
KEY `item` (`itemtype`, `items_id`)
KEY `type` (`type`)
```

## glpi_dropdowns_dropdowndefinitions

Origem: [DDL, linha 10436](../install/mysql/glpi-empty.sql#L10436).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `system_name` | `varchar(255) DEFAULT NULL` |
| `label` | `varchar(255) NOT NULL` |
| `icon` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `is_active` | `tinyint NOT NULL DEFAULT '0'` |
| `profiles` | `JSON NOT NULL` |
| `translations` | `JSON NOT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `system_name` (`system_name`)
KEY `label` (`label`)
KEY `is_active` (`is_active`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_dropdowns_dropdowns

Origem: [DDL, linha 10456](../install/mysql/glpi-empty.sql#L10456).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `dropdowns_dropdowndefinitions_id` | `int unsigned NOT NULL` |
| `name` | `varchar(255) DEFAULT NULL` |
| `comment` | `text` |
| `entities_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `is_recursive` | `tinyint NOT NULL DEFAULT '0'` |
| `dropdowns_dropdowns_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `completename` | `text` |
| `level` | `int NOT NULL DEFAULT '0'` |
| `ancestors_cache` | `longtext` |
| `sons_cache` | `longtext` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `dropdowns_dropdowndefinitions_id` (`dropdowns_dropdowndefinitions_id`)
KEY `name` (`name`)
KEY `entities_id` (`entities_id`)
KEY `is_recursive` (`is_recursive`)
KEY `dropdowns_dropdowns_id` (`dropdowns_dropdowns_id`)
KEY `level` (`level`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_assets_customfielddefinitions

Origem: [DDL, linha 10482](../install/mysql/glpi-empty.sql#L10482).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `assets_assetdefinitions_id` | `int unsigned NOT NULL` |
| `system_name` | `varchar(255) NOT NULL` |
| `label` | `varchar(255) NOT NULL` |
| `type` | `varchar(255) NOT NULL` |
| `field_options` | `json` |
| `itemtype` | `VARCHAR(255) NULL DEFAULT NULL` |
| `default_value` | `text` |
| `translations` | `JSON NOT NULL` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`assets_assetdefinitions_id`, `system_name`)
KEY `system_name` (`system_name`)
KEY `label` (`label`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
```

## glpi_contracts_users

Origem: [DDL, linha 10503](../install/mysql/glpi-empty.sql#L10503).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `contracts_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unicity` (`contracts_id`, `users_id`)
KEY `item` (`users_id`)
```

## glpi_softwarelicenses_users

Origem: [DDL, linha 10513](../install/mysql/glpi-empty.sql#L10513).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `softwarelicenses_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `softwarelicenses_id` (`softwarelicenses_id`)
KEY `users_id` (`users_id`)
```

## glpi_itemtranslations_itemtranslations

Origem: [DDL, linha 10523](../install/mysql/glpi-empty.sql#L10523).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `itemtype` | `varchar(255) NOT NULL` |
| `key` | `varchar(255) NOT NULL` |
| `language` | `varchar(10) NOT NULL` |
| `translations` | `JSON NOT NULL` |
| `hash` | `varchar(32) DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `unique_item_key` (`items_id`, `itemtype`, `key`, `language`)
KEY `item` (`itemtype`, `items_id`)
```

## glpi_sharetokens

Origem: [DDL, linha 10537](../install/mysql/glpi-empty.sql#L10537).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `itemtype` | `varchar(255) NOT NULL` |
| `items_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `name` | `varchar(255) DEFAULT NULL` |
| `token` | `varchar(255) NOT NULL` |
| `token_hint` | `varchar(16) NOT NULL DEFAULT ''` |
| `is_active` | `tinyint NOT NULL DEFAULT '1'` |
| `users_id` | `int unsigned NOT NULL DEFAULT '0'` |
| `date_creation` | `timestamp NULL DEFAULT NULL` |
| `date_mod` | `timestamp NULL DEFAULT NULL` |
| `date_expiration` | `timestamp NULL DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `token` (`token`)
KEY `token_hint` (`token_hint`)
KEY `item` (`itemtype`, `items_id`)
KEY `name` (`name`)
KEY `is_active` (`is_active`)
KEY `users_id` (`users_id`)
KEY `date_creation` (`date_creation`)
KEY `date_mod` (`date_mod`)
KEY `date_expiration` (`date_expiration`)
```

## glpi_usertokens

Origem: [DDL, linha 10562](../install/mysql/glpi-empty.sql#L10562).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `users_id` | `int unsigned NOT NULL` |
| `type` | `varchar(64) NOT NULL` |
| `token_uid` | `char(16) NOT NULL` |
| `token_hash` | `varchar(255) NOT NULL` |
| `date_expiration` | `timestamp NOT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `token_uid` (`token_uid`)
KEY `users_id` (`users_id`)
KEY `type` (`type`)
KEY `date_expiration` (`date_expiration`)
```

## glpi_users_sessions

Origem: [DDL, linha 10577](../install/mysql/glpi-empty.sql#L10577).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `users_id` | `int unsigned NOT NULL` |
| `login_session_uid` | `varchar(64) NOT NULL` |
| `session_file` | `varchar(261) NOT NULL COMMENT 'Current session filename. PHP allows up to 256 characters for session IDs + the "sess_" prefix used by default.'` |
| `ip_address` | `varchar(45) NOT NULL` |
| `user_agent` | `varchar(512) NOT NULL` |
| `auth_type` | `tinyint NOT NULL` |
| `created_at` | `timestamp NOT NULL` |
| `last_activity_at` | `timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
UNIQUE KEY `login_session_uid` (`login_session_uid`)
KEY `users_id` (`users_id`)
KEY `last_activity_at` (`last_activity_at`)
```

## glpi_users_sessionhistories

Origem: [DDL, linha 10594](../install/mysql/glpi-empty.sql#L10594).

`ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC`

| Coluna | Definição SQL |
| --- | --- |
| `id` | `int unsigned NOT NULL AUTO_INCREMENT` |
| `users_id` | `int unsigned NOT NULL` |
| `login_session_uid` | `varchar(64) NOT NULL` |
| `ip_address` | `varchar(45) NOT NULL` |
| `user_agent` | `varchar(512) NOT NULL` |
| `auth_type` | `tinyint NOT NULL` |
| `logged_in_at` | `timestamp NOT NULL` |
| `logged_out_at` | `timestamp NULL DEFAULT NULL` |
| `logout_reason` | `enum('user', 'admin', 'expired') DEFAULT NULL` |
| `users_id_revoked_by` | `int unsigned DEFAULT NULL` |

Índices/constraints declarados:

```sql
PRIMARY KEY (`id`)
KEY `users_id` (`users_id`, `logged_in_at` DESC)
KEY `users_id_revoked_by` (`users_id_revoked_by`)
KEY `logged_out_at` (`logged_out_at`)
```
