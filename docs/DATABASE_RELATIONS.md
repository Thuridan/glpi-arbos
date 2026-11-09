# Relações declaradas pela aplicação

Extraído de `$RELATION` em [inc/relation.constant.php](../inc/relation.constant.php).

Não são foreign keys DDL. O lado esquerdo de cada seção é a tabela referenciada; as linhas indicam a tabela que aponta para ela. Prefixo `_` na tabela ligada desativa o controle genérico de uso durante exclusão porque há tratamento específico na aplicação. Pares `items_id`/`itemtype` representam relações polimórficas.

Além deste mapa existem relações inferidas em classes e módulos; não trate esta lista como todas as invariantes de negócio.
## glpi_agents

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_refusedequipments | `"agents_id"` |
| glpi_rulematchedlogs | `"agents_id"` |
| glpi_unmanageds | `"agents_id"` |

## glpi_agenttypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_agents | `"agenttypes_id"` |

## glpi_applianceenvironments

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_appliances | `"applianceenvironments_id"` |
| _glpi_appliances_items_relations | `[["items_id", "itemtype"]]` |

## glpi_appliances

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_appliances_items | `["appliances_id", ["items_id", "itemtype"]]` |
| _glpi_certificates_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_appliances_items

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_appliances_items_relations | `"appliances_items_id"` |

## glpi_appliancetypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_appliances | `"appliancetypes_id"` |

## glpi_assets_assetdefinitions

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_assets_assets | `"assets_assetdefinitions_id"` |
| _glpi_assets_assetmodels | `"assets_assetdefinitions_id"` |
| _glpi_assets_assettypes | `"assets_assetdefinitions_id"` |
| _glpi_assets_customfielddefinitions | `"assets_assetdefinitions_id"` |

## glpi_assets_assetmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_assets_assets | `"assets_assetmodels_id"` |

## glpi_assets_assettypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_assets_assets | `"assets_assettypes_id"` |

## glpi_authldaps

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_authldapreplicates | `"authldaps_id"` |
| glpi_entities | `"authldaps_id"` |
| glpi_users | `"auths_id"` |

## glpi_authmails

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_users | `"auths_id"` |

## glpi_autoupdatesystems

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_clusters | `"autoupdatesystems_id"` |
| glpi_computers | `"autoupdatesystems_id"` |
| glpi_databaseinstances | `"autoupdatesystems_id"` |
| glpi_monitors | `"autoupdatesystems_id"` |
| glpi_networkequipments | `"autoupdatesystems_id"` |
| glpi_pdus | `"autoupdatesystems_id"` |
| glpi_plugs | `"autoupdatesystems_id"` |
| glpi_peripherals | `"autoupdatesystems_id"` |
| glpi_phones | `"autoupdatesystems_id"` |
| glpi_printers | `"autoupdatesystems_id"` |
| glpi_refusedequipments | `"autoupdatesystems_id"` |
| glpi_unmanageds | `"autoupdatesystems_id"` |
| glpi_assets_assets | `"autoupdatesystems_id"` |

## glpi_budgets

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_changecosts | `"budgets_id"` |
| glpi_contractcosts | `"budgets_id"` |
| glpi_infocoms | `"budgets_id"` |
| glpi_problemcosts | `"budgets_id"` |
| glpi_projectcosts | `"budgets_id"` |
| glpi_ticketcosts | `"budgets_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |

## glpi_budgettypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_budgets | `"budgettypes_id"` |

## glpi_businesscriticities

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_businesscriticities | `"businesscriticities_id"` |
| glpi_infocoms | `"businesscriticities_id"` |

## glpi_cables

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_cablestrands

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_cables | `"cablestrands_id"` |

## glpi_cabletypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_cables | `"cabletypes_id"` |

## glpi_calendars

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_calendars_holidays | `"calendars_id"` |
| _glpi_calendarsegments | `"calendars_id"` |
| glpi_entities | `"calendars_id"` |
| glpi_olas | `"calendars_id"` |
| glpi_slas | `"calendars_id"` |
| glpi_slms | `"calendars_id"` |
| glpi_recurrentchanges | `"calendars_id"` |
| glpi_ticketrecurrents | `"calendars_id"` |
| glpi_pendingreasons | `"calendars_id"` |

## glpi_cartridgeitems

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_cartridgeitems_printermodels | `"cartridgeitems_id"` |
| _glpi_cartridges | `"cartridgeitems_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_cartridgeitemtypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_cartridgeitems | `"cartridgeitemtypes_id"` |

## glpi_cartridges

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_certificates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_certificates_items | `"certificates_id"` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_certificatetypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_certificates | `"certificatetypes_id"` |

## glpi_changes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_changecosts | `"changes_id"` |
| _glpi_changes_changes | `["changes_id_1", "changes_id_2"]` |
| _glpi_changes_groups | `"changes_id"` |
| _glpi_changes_items | `"changes_id"` |
| _glpi_changes_problems | `"changes_id"` |
| _glpi_changes_suppliers | `"changes_id"` |
| _glpi_changes_tickets | `"changes_id"` |
| _glpi_changes_users | `"changes_id"` |
| _glpi_changesatisfactions | `"changes_id"` |
| _glpi_changetasks | `"changes_id"` |
| _glpi_changevalidations | `"changes_id"` |
| _glpi_itils_projects | `[["items_id", "itemtype"]]` |
| _glpi_itilfollowups | `[["items_id", "itemtype"]]` |
| _glpi_itils_validationsteps | `[["items_id", "itemtype"]]` |
| _glpi_itilsolutions | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |

## glpi_changetasks

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_vobjects | `[["items_id", "itemtype"]]` |

## glpi_changetemplates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_entities | `"changetemplates_id"` |
| glpi_itilcategories | `["changetemplates_id"]` |
| glpi_changes | `"changetemplates_id"` |
| _glpi_changetemplatehiddenfields | `"changetemplates_id"` |
| _glpi_changetemplatemandatoryfields | `"changetemplates_id"` |
| _glpi_changetemplatepredefinedfields | `"changetemplates_id"` |
| _glpi_changetemplatereadonlyfields | `"changetemplates_id"` |
| glpi_profiles | `"changetemplates_id"` |
| glpi_recurrentchanges | `"changetemplates_id"` |

## glpi_clusters

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_items_clusters | `"clusters_id"` |
| _glpi_appliances_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_networkports | `[["items_id", "itemtype"]]` |
| glpi_ipaddresses | `[["mainitems_id", "mainitemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_clustertypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_clusters | `"clustertypes_id"` |

## glpi_computermodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_computers | `"computermodels_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_computers

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_networknames | `[["items_id", "itemtype"]]` |
| _glpi_agents | `[["items_id", "itemtype"]]` |
| _glpi_appliances_items | `[["items_id", "itemtype"]]` |
| _glpi_certificates_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_databaseinstances | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_clusters | `[["items_id", "itemtype"]]` |
| _glpi_items_disks | `[["items_id", "itemtype"]]` |
| _glpi_items_enclosures | `[["items_id", "itemtype"]]` |
| _glpi_items_operatingsystems | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_racks | `[["items_id", "itemtype"]]` |
| _glpi_items_softwarelicenses | `[["items_id", "itemtype"]]` |
| _glpi_items_softwareversions | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_itemantiviruses | `[["items_id", "itemtype"]]` |
| _glpi_itemvirtualmachines | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |
| _glpi_networkports | `[["items_id", "itemtype"]]` |
| _glpi_reservationitems | `[["items_id", "itemtype"]]` |
| _glpi_sockets | `[["items_id", "itemtype"]]` |
| _glpi_items_devicenetworkcards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicedrives | `[["items_id", "itemtype"]]` |
| _glpi_items_devicegraphiccards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesoundcards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepcis | `[["items_id", "itemtype"]]` |
| _glpi_items_devicecameras | `[["items_id", "itemtype"]]` |
| _glpi_items_devicebatteries | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepowersupplies | `[["items_id", "itemtype"]]` |
| _glpi_items_devicemotherboards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicefirmwares | `[["items_id", "itemtype"]]` |
| _glpi_items_deviceprocessors | `[["items_id", "itemtype"]]` |
| _glpi_items_devicecontrols | `[["items_id", "itemtype"]]` |
| _glpi_items_devicecases | `[["items_id", "itemtype"]]` |
| _glpi_items_devicegenerics | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesimcards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesensors | `[["items_id", "itemtype"]]` |
| _glpi_items_devicememories | `[["items_id", "itemtype"]]` |
| _glpi_items_deviceharddrives | `[["items_id", "itemtype"]]` |
| glpi_ipaddresses | `[["mainitems_id", "mainitemtype"]]` |
| _glpi_assets_assets_peripheralassets | `[["itemtype_asset", "items_id_asset"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_computertypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_computers | `"computertypes_id"` |

## glpi_consumableitems

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_consumables | `"consumableitems_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_consumableitemtypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_consumableitems | `"consumableitemtypes_id"` |

## glpi_consumables

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_contacts

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contacts_suppliers | `"contacts_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_contacttypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_contacts | `"contacttypes_id"` |

## glpi_contracts

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contractcosts | `"contracts_id"` |
| _glpi_contracts_items | `"contracts_id"` |
| _glpi_contracts_suppliers | `"contracts_id"` |
| glpi_entities | `"contracts_id_default"` |
| _glpi_tickets_contracts | `"contracts_id"` |
| _glpi_contracts_users | `"contracts_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |

## glpi_contracttypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_contracts | `"contracttypes_id"` |

## glpi_crontasklogs

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_crontasklogs | `"crontasklogs_id"` |

## glpi_crontasks

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_crontasklogs | `"crontasks_id"` |

## glpi_dashboards_dashboards

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_dashboards_filters | `"dashboards_dashboards_id"` |
| _glpi_dashboards_items | `"dashboards_dashboards_id"` |
| _glpi_dashboards_rights | `"dashboards_dashboards_id"` |

## glpi_databaseinstancecategories

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_databaseinstances | `"databaseinstancecategories_id"` |

## glpi_databaseinstances

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_databases | `"databaseinstances_id"` |
| _glpi_appliances_items | `[["items_id", "itemtype"]]` |
| _glpi_certificates_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_databaseinstancetypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_databaseinstances | `"databaseinstancetypes_id"` |

## glpi_databases

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_appliances_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |

## glpi_datacenters

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_dcrooms | `"datacenters_id"` |

## glpi_dcrooms

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_racks | `"dcrooms_id"` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |

## glpi_devicebatteries

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicebatteries | `["devicebatteries_id"]` |

## glpi_devicebatterymodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicebatteries | `"devicebatterymodels_id"` |

## glpi_devicebatterytypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicebatteries | `"devicebatterytypes_id"` |

## glpi_devicecameramodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicecameras | `"devicecameramodels_id"` |

## glpi_devicecameras

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicecameras | `["devicecameras_id"]` |

## glpi_devicecasemodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicecases | `"devicecasemodels_id"` |

## glpi_devicecases

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicecases | `["devicecases_id"]` |

## glpi_devicecasetypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicecases | `"devicecasetypes_id"` |

## glpi_devicecontrolmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicecontrols | `"devicecontrolmodels_id"` |

## glpi_devicecontrols

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicecontrols | `["devicecontrols_id"]` |

## glpi_devicedrivemodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicedrives | `"devicedrivemodels_id"` |

## glpi_devicedrives

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicedrives | `["devicedrives_id"]` |

## glpi_devicefirmwaremodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicefirmwares | `"devicefirmwaremodels_id"` |

## glpi_devicefirmwares

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicefirmwares | `["devicefirmwares_id"]` |

## glpi_devicefirmwaretypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicefirmwares | `"devicefirmwaretypes_id"` |

## glpi_devicegenericmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicegenerics | `"devicegenericmodels_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_devicegenerics

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicegenerics | `["devicegenerics_id"]` |

## glpi_devicegenerictypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicegenerics | `"devicegenerictypes_id"` |

## glpi_devicegraphiccardmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicegraphiccards | `"devicegraphiccardmodels_id"` |

## glpi_devicegraphiccards

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicegraphiccards | `["devicegraphiccards_id"]` |

## glpi_deviceharddrivemodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_deviceharddrives | `"deviceharddrivemodels_id"` |

## glpi_deviceharddrives

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_deviceharddrives | `["deviceharddrives_id"]` |

## glpi_deviceharddrivetypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_deviceharddrives | `"deviceharddrivetypes_id"` |

## glpi_devicememories

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicememories | `["devicememories_id"]` |

## glpi_devicememorymodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicememories | `"devicememorymodels_id"` |

## glpi_devicememorytypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicememories | `"devicememorytypes_id"` |

## glpi_devicemotherboardmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicemotherboards | `"devicemotherboardmodels_id"` |

## glpi_devicemotherboards

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicemotherboards | `["devicemotherboards_id"]` |

## glpi_devicenetworkcardmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicenetworkcards | `"devicenetworkcardmodels_id"` |
| glpi_devicepcis | `"devicenetworkcardmodels_id"` |

## glpi_devicenetworkcards

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicenetworkcards | `["devicenetworkcards_id"]` |

## glpi_devicepcimodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicepcis | `"devicepcimodels_id"` |

## glpi_devicepcis

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepcis | `["devicepcis_id"]` |

## glpi_devicepowersupplies

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepowersupplies | `["devicepowersupplies_id"]` |

## glpi_devicepowersupplymodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicepowersupplies | `"devicepowersupplymodels_id"` |

## glpi_deviceprocessormodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_deviceprocessors | `"deviceprocessormodels_id"` |

## glpi_deviceprocessors

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_deviceprocessors | `["deviceprocessors_id"]` |

## glpi_devicesensormodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicesensors | `"devicesensormodels_id"` |

## glpi_devicesensors

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesensors | `["devicesensors_id"]` |

## glpi_devicesensortypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicesensors | `"devicesensortypes_id"` |

## glpi_devicesimcards

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesimcards | `["devicesimcards_id"]` |

## glpi_devicesimcardtypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicesimcards | `"devicesimcardtypes_id"` |

## glpi_devicesoundcardmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicesoundcards | `"devicesoundcardmodels_id"` |

## glpi_devicesoundcards

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesoundcards | `["devicesoundcards_id"]` |

## glpi_documentcategories

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_documentcategories | `"documentcategories_id"` |
| glpi_documents | `"documentcategories_id"` |

## glpi_documents

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `["documents_id", ["items_id", "itemtype"]]` |

## glpi_domainrecords

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_domainrecordtypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_domainrecords | `"domainrecordtypes_id"` |

## glpi_domainrelations

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_domains_items | `"domainrelations_id"` |

## glpi_domains

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_domainrecords | `"domains_id"` |
| _glpi_domains_items | `"domains_id"` |
| _glpi_appliances_items_relations | `[["items_id", "itemtype"]]` |
| _glpi_certificates_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_domaintypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_domains | `"domaintypes_id"` |

## glpi_dropdowns_dropdowndefinitions

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_dropdowns_dropdowns | `"dropdowns_dropdowndefinitions_id"` |

## glpi_dropdowns_dropdowns

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_dropdowns_dropdowns | `"dropdowns_dropdowns_id"` |

## glpi_enclosuremodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_enclosures | `"enclosuremodels_id"` |

## glpi_enclosures

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_items_enclosures | `["enclosures_id", ["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_racks | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_networkports | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepcis | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepowersupplies | `[["items_id", "itemtype"]]` |
| _glpi_items_devicegenerics | `[["items_id", "itemtype"]]` |
| glpi_ipaddresses | `[["mainitems_id", "mainitemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_entities

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_agents | `"entities_id"` |
| glpi_apiclients | `"entities_id"` |
| glpi_appliances | `"entities_id"` |
| glpi_appliancetypes | `"entities_id"` |
| glpi_assets_assets | `"entities_id"` |
| glpi_budgets | `"entities_id"` |
| glpi_businesscriticities | `"entities_id"` |
| glpi_cables | `"entities_id"` |
| glpi_calendars | `"entities_id"` |
| _glpi_calendarsegments | `"entities_id"` |
| glpi_cartridgeitems | `"entities_id"` |
| _glpi_cartridges | `"entities_id"` |
| glpi_certificates | `"entities_id"` |
| glpi_certificatetypes | `"entities_id"` |
| _glpi_changecosts | `"entities_id"` |
| glpi_changes | `"entities_id"` |
| glpi_changetemplates | `"entities_id"` |
| _glpi_changevalidations | `"entities_id"` |
| glpi_clusters | `"entities_id"` |
| glpi_clustertypes | `"entities_id"` |
| glpi_computers | `"entities_id"` |
| glpi_dropdowns_dropdowns | `"entities_id"` |
| glpi_consumableitems | `"entities_id"` |
| _glpi_consumables | `"entities_id"` |
| glpi_contacts | `"entities_id"` |
| _glpi_contractcosts | `"entities_id"` |
| glpi_contracts | `"entities_id"` |
| glpi_databaseinstances | `"entities_id"` |
| _glpi_databases | `"entities_id"` |
| glpi_datacenters | `"entities_id"` |
| glpi_dcrooms | `"entities_id"` |
| glpi_devicebatteries | `"entities_id"` |
| glpi_devicecameras | `"entities_id"` |
| glpi_devicecases | `"entities_id"` |
| glpi_devicecontrols | `"entities_id"` |
| glpi_devicedrives | `"entities_id"` |
| glpi_devicefirmwares | `"entities_id"` |
| glpi_devicegenerics | `"entities_id"` |
| glpi_devicegraphiccards | `"entities_id"` |
| glpi_deviceharddrives | `"entities_id"` |
| glpi_devicememories | `"entities_id"` |
| glpi_devicemotherboards | `"entities_id"` |
| glpi_devicenetworkcards | `"entities_id"` |
| glpi_devicepcis | `"entities_id"` |
| glpi_devicepowersupplies | `"entities_id"` |
| glpi_deviceprocessors | `"entities_id"` |
| glpi_devicesensors | `"entities_id"` |
| glpi_devicesimcards | `"entities_id"` |
| glpi_devicesoundcards | `"entities_id"` |
| glpi_documents | `"entities_id"` |
| _glpi_documents_items | `["entities_id", ["items_id", "itemtype"]]` |
| glpi_domainrelations | `"entities_id"` |
| glpi_domainrecords | `"entities_id"` |
| glpi_domainrecordtypes | `"entities_id"` |
| glpi_domains | `"entities_id"` |
| glpi_domaintypes | `"entities_id"` |
| glpi_enclosures | `"entities_id"` |
| _glpi_entities | `"entities_id"` |
| glpi_entities | `"entities_id_software"` |
| _glpi_entities_knowbaseitems | `"entities_id"` |
| _glpi_entities_reminders | `"entities_id"` |
| _glpi_entities_rssfeeds | `"entities_id"` |
| glpi_fieldblacklists | `"entities_id"` |
| glpi_fieldunicities | `"entities_id"` |
| glpi_forms_forms | `"entities_id"` |
| glpi_forms_answerssets | `"entities_id"` |
| glpi_fqdns | `"entities_id"` |
| glpi_groups | `"entities_id"` |
| glpi_groups_knowbaseitems | `"entities_id"` |
| glpi_groups_reminders | `"entities_id"` |
| glpi_groups_rssfeeds | `"entities_id"` |
| glpi_holidays | `"entities_id"` |
| glpi_imageformats | `"entities_id"` |
| glpi_imageresolutions | `"entities_id"` |
| _glpi_infocoms | `"entities_id"` |
| glpi_ipaddresses | `"entities_id"` |
| glpi_ipnetworks | `"entities_id"` |
| _glpi_items_devicebatteries | `"entities_id"` |
| _glpi_items_devicecases | `"entities_id"` |
| _glpi_items_devicecameras | `"entities_id"` |
| _glpi_items_devicecontrols | `"entities_id"` |
| _glpi_items_devicedrives | `"entities_id"` |
| _glpi_items_devicefirmwares | `"entities_id"` |
| _glpi_items_devicegenerics | `"entities_id"` |
| _glpi_items_devicegraphiccards | `"entities_id"` |
| _glpi_items_deviceharddrives | `"entities_id"` |
| _glpi_items_devicememories | `"entities_id"` |
| _glpi_items_devicemotherboards | `"entities_id"` |
| _glpi_items_devicenetworkcards | `"entities_id"` |
| _glpi_items_devicepcis | `"entities_id"` |
| _glpi_items_devicepowersupplies | `"entities_id"` |
| _glpi_items_deviceprocessors | `"entities_id"` |
| _glpi_items_devicesensors | `"entities_id"` |
| _glpi_items_devicesimcards | `"entities_id"` |
| _glpi_items_devicesoundcards | `"entities_id"` |
| _glpi_items_disks | `"entities_id"` |
| _glpi_items_operatingsystems | `"entities_id"` |
| _glpi_items_softwareversions | `"entities_id"` |
| _glpi_itemvirtualmachines | `"entities_id"` |
| glpi_itilcategories | `"entities_id"` |
| glpi_itilfollowuptemplates | `"entities_id"` |
| glpi_itilvalidationtemplates | `"entities_id"` |
| glpi_knowbaseitems | `"entities_id"` |
| glpi_knowbaseitems_profiles | `"entities_id"` |
| glpi_lineoperators | `"entities_id"` |
| glpi_lines | `"entities_id"` |
| glpi_links | `"entities_id"` |
| glpi_locations | `"entities_id"` |
| glpi_monitors | `"entities_id"` |
| _glpi_networkaliases | `"entities_id"` |
| glpi_networkequipments | `"entities_id"` |
| glpi_networknames | `"entities_id"` |
| _glpi_networkports | `"entities_id"` |
| glpi_networkporttypes | `"entities_id"` |
| glpi_notifications | `"entities_id"` |
| _glpi_olalevels | `"entities_id"` |
| _glpi_olas | `"entities_id"` |
| glpi_passivedcequipments | `"entities_id"` |
| glpi_pcivendors | `"entities_id"` |
| glpi_pdus | `"entities_id"` |
| glpi_pdutypes | `"entities_id"` |
| glpi_pendingreasons | `"entities_id"` |
| glpi_peripherals | `"entities_id"` |
| glpi_phones | `"entities_id"` |
| glpi_planningexternalevents | `"entities_id"` |
| glpi_planningexternaleventtemplates | `"entities_id"` |
| glpi_plugs | `"entities_id"` |
| glpi_plugtypes | `"entities_id"` |
| glpi_printers | `"entities_id"` |
| _glpi_problemcosts | `"entities_id"` |
| glpi_problems | `"entities_id"` |
| glpi_problemtemplates | `"entities_id"` |
| glpi_profiles_reminders | `"entities_id"` |
| glpi_profiles_rssfeeds | `"entities_id"` |
| _glpi_profiles_users | `"entities_id"` |
| _glpi_projectcosts | `"entities_id"` |
| glpi_projects | `"entities_id"` |
| _glpi_projecttasks | `"entities_id"` |
| glpi_projecttasktemplates | `"entities_id"` |
| glpi_queuednotifications | `"entities_id"` |
| glpi_racks | `"entities_id"` |
| glpi_racktypes | `"entities_id"` |
| glpi_recurrentchanges | `"entities_id"` |
| glpi_refusedequipments | `"entities_id"` |
| _glpi_reservationitems | `"entities_id"` |
| glpi_rules | `"entities_id"` |
| glpi_savedsearches | `"entities_id"` |
| _glpi_slalevels | `"entities_id"` |
| _glpi_slas | `"entities_id"` |
| glpi_slms | `"entities_id"` |
| glpi_softwarelicenses | `"entities_id"` |
| glpi_softwarelicensetypes | `"entities_id"` |
| glpi_softwares | `"entities_id"` |
| _glpi_softwareversions | `"entities_id"` |
| glpi_solutiontemplates | `"entities_id"` |
| glpi_solutiontypes | `"entities_id"` |
| glpi_states | `"entities_id"` |
| glpi_suppliers | `"entities_id"` |
| glpi_taskcategories | `"entities_id"` |
| glpi_tasktemplates | `"entities_id"` |
| _glpi_ticketcosts | `"entities_id"` |
| glpi_ticketrecurrents | `"entities_id"` |
| glpi_tickets | `"entities_id"` |
| glpi_tickettemplates | `"entities_id"` |
| _glpi_ticketvalidations | `"entities_id"` |
| glpi_unmanageds | `"entities_id"` |
| glpi_usbvendors | `"entities_id"` |
| glpi_users | `"entities_id"` |
| glpi_vlans | `"entities_id"` |
| glpi_wifinetworks | `"entities_id"` |
| glpi_webhooks | `"entities_id"` |
| glpi_queuedwebhooks | `"entities_id"` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |

## glpi_filesystems

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_items_disks | `"filesystems_id"` |

## glpi_forms_answerssets

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_forms_destinations_answerssets_formdestinationitems | `"forms_answerssets_id"` |

## glpi_forms_categories

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_forms_categories | `"forms_categories_id"` |
| glpi_forms_forms | `"forms_categories_id"` |
| glpi_knowbaseitems | `"forms_categories_id"` |

## glpi_forms_forms

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_forms_accesscontrols_formaccesscontrols | `"forms_forms_id"` |
| _glpi_forms_answerssets | `"forms_forms_id"` |
| _glpi_forms_destinations_formdestinations | `"forms_forms_id"` |
| _glpi_forms_sections | `"forms_forms_id"` |
| _glpi_helpdesks_tiles_formtiles | `"forms_forms_id"` |

## glpi_forms_sections

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_forms_questions | `"forms_sections_id"` |
| _glpi_forms_comments | `"forms_sections_id"` |

## glpi_fqdns

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_networkaliases | `"fqdns_id"` |
| glpi_networknames | `"fqdns_id"` |

## glpi_groups

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_changes_groups | `"groups_id"` |
| glpi_changetasks | `"groups_id_tech"` |
| glpi_groups | `"groups_id"` |
| _glpi_groups_items | `"groups_id"` |
| _glpi_groups_knowbaseitems | `"groups_id"` |
| _glpi_groups_problems | `"groups_id"` |
| _glpi_groups_reminders | `"groups_id"` |
| _glpi_groups_rssfeeds | `"groups_id"` |
| _glpi_groups_tickets | `"groups_id"` |
| _glpi_groups_users | `"groups_id"` |
| glpi_itilcategories | `"groups_id"` |
| glpi_planningexternalevents | `"groups_id"` |
| glpi_problemtasks | `"groups_id_tech"` |
| glpi_projects | `"groups_id"` |
| glpi_tasktemplates | `"groups_id_tech"` |
| glpi_tickettasks | `"groups_id_tech"` |
| glpi_users | `"groups_id"` |
| glpi_itilvalidationtemplates_targets | `"groups_id"` |
| glpi_olas | `"groups_id"` |
| _glpi_consumables | `[["items_id", "itemtype"]]` |

## glpi_holidays

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_calendars_holidays | `"holidays_id"` |

## glpi_imageformats

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_items_devicecameras_imageformats | `"imageformats_id"` |

## glpi_imageresolutions

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_items_devicecameras_imageresolutions | `"imageresolutions_id"` |

## glpi_impactcontexts

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_impactitems | `"impactcontexts_id"` |

## glpi_interfacetypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_devicecontrols | `"interfacetypes_id"` |
| glpi_devicedrives | `"interfacetypes_id"` |
| glpi_devicegraphiccards | `"interfacetypes_id"` |
| glpi_deviceharddrives | `"interfacetypes_id"` |

## glpi_ipaddresses

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_ipaddresses_ipnetworks | `"ipaddresses_id"` |

## glpi_ipnetworks

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_ipaddresses_ipnetworks | `"ipnetworks_id"` |
| glpi_networknames | `"ipnetworks_id"` |
| glpi_ipnetworks | `"ipnetworks_id"` |
| _glpi_ipnetworks_vlans | `"ipnetworks_id"` |

## glpi_items_devicebatteries

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicecameras

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_items_devicecameras_imageformats | `"items_devicecameras_id"` |
| _glpi_items_devicecameras_imageresolutions | `"items_devicecameras_id"` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicecases

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicecontrols

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicedrives

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicefirmwares

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicegenerics

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicegraphiccards

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_devicefirmwares | `[["items_id", "itemtype"]]` |

## glpi_items_deviceharddrives

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_devicefirmwares | `[["items_id", "itemtype"]]` |

## glpi_items_devicememories

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicemotherboards

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicenetworkcards

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_networkportethernets | `"items_devicenetworkcards_id"` |
| glpi_networkportfiberchannels | `"items_devicenetworkcards_id"` |
| glpi_networkportwifis | `"items_devicenetworkcards_id"` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_devicefirmwares | `[["items_id", "itemtype"]]` |

## glpi_items_devicepcis

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicepowersupplies

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_devicefirmwares | `[["items_id", "itemtype"]]` |

## glpi_items_deviceprocessors

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicesensors

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_items_devicesimcards

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_items_devicesoundcards

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |

## glpi_itilcategories

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_changes | `"itilcategories_id"` |
| glpi_itilcategories | `"itilcategories_id"` |
| glpi_problems | `"itilcategories_id"` |
| glpi_tickets | `"itilcategories_id"` |

## glpi_itilfollowups

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_itilsolutions | `"itilfollowups_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_itilfollowuptemplates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_pendingreasons | `"itilfollowuptemplates_id"` |

## glpi_itils_validationsteps

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_ticketvalidations | `"itils_validationsteps_id"` |
| glpi_changevalidations | `"itils_validationsteps_id"` |

## glpi_itilsolutions

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_itilvalidationtemplates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_itilvalidationtemplates_targets | `"itilvalidationtemplates_id"` |
| glpi_changevalidations | `"itilvalidationtemplates_id"` |
| glpi_ticketvalidations | `"itilvalidationtemplates_id"` |

## glpi_knowbaseitems

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_entities_knowbaseitems | `"knowbaseitems_id"` |
| _glpi_groups_knowbaseitems | `"knowbaseitems_id"` |
| _glpi_knowbaseitems_comments | `"knowbaseitems_id"` |
| _glpi_knowbaseitems_favorites | `"knowbaseitems_id"` |
| _glpi_knowbaseitems_items | `"knowbaseitems_id"` |
| _glpi_knowbaseitems_knowbaseitems | `["knowbaseitems_id", "knowbaseitems_id_parent"]` |
| _glpi_knowbaseitems_profiles | `"knowbaseitems_id"` |
| _glpi_knowbaseitems_revisions | `"knowbaseitems_id"` |
| _glpi_knowbaseitems_users | `"knowbaseitems_id"` |
| _glpi_knowbaseitemtranslations | `"knowbaseitems_id"` |
| glpi_itilcategories | `"knowbaseitems_id"` |
| glpi_taskcategories | `"knowbaseitems_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_knowbaseitems_comments

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_knowbaseitems_comments | `"parent_comment_id"` |

## glpi_lineoperators

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_lines | `"lineoperators_id"` |

## glpi_lines

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_items_devicesimcards | `"lines_id"` |
| _glpi_items_lines | `"lines_id"` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_linetypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_lines | `"linetypes_id"` |

## glpi_links

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_links_itemtypes | `"links_id"` |

## glpi_locations

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_appliances | `"locations_id"` |
| glpi_assets_assets | `"locations_id"` |
| glpi_budgets | `"locations_id"` |
| glpi_cartridgeitems | `"locations_id"` |
| glpi_certificates | `"locations_id"` |
| glpi_changes | `"locations_id"` |
| glpi_computers | `"locations_id"` |
| glpi_contracts | `"locations_id"` |
| glpi_consumableitems | `"locations_id"` |
| glpi_databaseinstances | `"locations_id"` |
| glpi_datacenters | `"locations_id"` |
| glpi_dcrooms | `"locations_id"` |
| glpi_devicegenerics | `"locations_id"` |
| glpi_devicesensors | `"locations_id"` |
| glpi_enclosures | `"locations_id"` |
| glpi_items_devicebatteries | `"locations_id"` |
| glpi_items_devicecameras | `"locations_id"` |
| glpi_items_devicecases | `"locations_id"` |
| glpi_items_devicecontrols | `"locations_id"` |
| glpi_items_devicedrives | `"locations_id"` |
| glpi_items_devicefirmwares | `"locations_id"` |
| glpi_items_devicegenerics | `"locations_id"` |
| glpi_items_devicegraphiccards | `"locations_id"` |
| glpi_items_deviceharddrives | `"locations_id"` |
| glpi_items_devicememories | `"locations_id"` |
| glpi_items_devicemotherboards | `"locations_id"` |
| glpi_items_devicenetworkcards | `"locations_id"` |
| glpi_items_devicepcis | `"locations_id"` |
| glpi_items_devicepowersupplies | `"locations_id"` |
| glpi_items_deviceprocessors | `"locations_id"` |
| glpi_items_devicesensors | `"locations_id"` |
| glpi_items_devicesimcards | `"locations_id"` |
| glpi_items_devicesoundcards | `"locations_id"` |
| glpi_lines | `"locations_id"` |
| glpi_locations | `"locations_id"` |
| glpi_monitors | `"locations_id"` |
| glpi_networkequipments | `"locations_id"` |
| glpi_passivedcequipments | `"locations_id"` |
| glpi_pdus | `"locations_id"` |
| glpi_peripherals | `"locations_id"` |
| glpi_phones | `"locations_id"` |
| glpi_printers | `"locations_id"` |
| glpi_problems | `"locations_id"` |
| glpi_racks | `"locations_id"` |
| glpi_sockets | `"locations_id"` |
| glpi_softwarelicenses | `"locations_id"` |
| glpi_softwares | `"locations_id"` |
| glpi_tickets | `"locations_id"` |
| glpi_unmanageds | `"locations_id"` |
| glpi_users | `"locations_id"` |
| _glpi_appliances_items_relations | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_mailcollectors

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_notimportedemails | `"mailcollectors_id"` |

## glpi_manufacturers

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_appliances | `"manufacturers_id"` |
| glpi_assets_assets | `"manufacturers_id"` |
| glpi_cartridgeitems | `"manufacturers_id"` |
| glpi_certificates | `"manufacturers_id"` |
| glpi_itemantiviruses | `"manufacturers_id"` |
| glpi_computers | `"manufacturers_id"` |
| glpi_consumableitems | `"manufacturers_id"` |
| glpi_databaseinstances | `"manufacturers_id"` |
| glpi_devicebatteries | `"manufacturers_id"` |
| glpi_devicecameras | `"manufacturers_id"` |
| glpi_devicecases | `"manufacturers_id"` |
| glpi_devicecontrols | `"manufacturers_id"` |
| glpi_devicedrives | `"manufacturers_id"` |
| glpi_devicefirmwares | `"manufacturers_id"` |
| glpi_devicegenerics | `"manufacturers_id"` |
| glpi_devicegraphiccards | `"manufacturers_id"` |
| glpi_deviceharddrives | `"manufacturers_id"` |
| glpi_devicememories | `"manufacturers_id"` |
| glpi_devicemotherboards | `"manufacturers_id"` |
| glpi_devicenetworkcards | `"manufacturers_id"` |
| glpi_devicepcis | `"manufacturers_id"` |
| glpi_devicepowersupplies | `"manufacturers_id"` |
| glpi_deviceprocessors | `"manufacturers_id"` |
| glpi_devicesensors | `"manufacturers_id"` |
| glpi_devicesimcards | `"manufacturers_id"` |
| glpi_devicesoundcards | `"manufacturers_id"` |
| glpi_enclosures | `"manufacturers_id"` |
| glpi_monitors | `"manufacturers_id"` |
| glpi_networkequipments | `"manufacturers_id"` |
| glpi_passivedcequipments | `"manufacturers_id"` |
| glpi_pdus | `"manufacturers_id"` |
| glpi_peripherals | `"manufacturers_id"` |
| glpi_phones | `"manufacturers_id"` |
| glpi_printers | `"manufacturers_id"` |
| glpi_racks | `"manufacturers_id"` |
| glpi_softwarelicenses | `"manufacturers_id"` |
| glpi_softwares | `"manufacturers_id"` |
| glpi_unmanageds | `"manufacturers_id"` |

## glpi_monitormodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_monitors | `"monitormodels_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_monitors

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_appliances_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_enclosures | `[["items_id", "itemtype"]]` |
| _glpi_items_operatingsystems | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_racks | `[["items_id", "itemtype"]]` |
| _glpi_items_softwarelicenses | `[["items_id", "itemtype"]]` |
| _glpi_items_softwareversions | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |
| _glpi_networkports | `[["items_id", "itemtype"]]` |
| _glpi_reservationitems | `[["items_id", "itemtype"]]` |
| glpi_ipaddresses | `[["mainitems_id", "mainitemtype"]]` |
| _glpi_assets_assets_peripheralassets | `[["itemtype_peripheral", "items_id_peripheral"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_monitortypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_monitors | `"monitortypes_id"` |

## glpi_networkequipmentmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_networkequipments | `"networkequipmentmodels_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_networkequipments

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_appliances_items | `[["items_id", "itemtype"]]` |
| _glpi_certificates_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_clusters | `[["items_id", "itemtype"]]` |
| _glpi_items_disks | `[["items_id", "itemtype"]]` |
| _glpi_items_enclosures | `[["items_id", "itemtype"]]` |
| _glpi_items_operatingsystems | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_racks | `[["items_id", "itemtype"]]` |
| _glpi_items_softwarelicenses | `[["items_id", "itemtype"]]` |
| _glpi_items_softwareversions | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |
| _glpi_networkports | `[["items_id", "itemtype"]]` |
| _glpi_reservationitems | `[["items_id", "itemtype"]]` |
| _glpi_sockets | `[["items_id", "itemtype"]]` |
| _glpi_items_devicenetworkcards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepcis | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepowersupplies | `[["items_id", "itemtype"]]` |
| _glpi_items_devicefirmwares | `[["items_id", "itemtype"]]` |
| _glpi_items_devicecontrols | `[["items_id", "itemtype"]]` |
| _glpi_items_devicegenerics | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesimcards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicememories | `[["items_id", "itemtype"]]` |
| _glpi_items_deviceharddrives | `[["items_id", "itemtype"]]` |
| glpi_ipaddresses | `[["mainitems_id", "mainitemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_networkequipmenttypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_networkequipments | `"networkequipmenttypes_id"` |

## glpi_networknames

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_networkaliases | `"networknames_id"` |

## glpi_networkportfiberchanneltypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_networkportfiberchannels | `"networkportfiberchanneltypes_id"` |

## glpi_networkports

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_networkportaggregates | `"networkports_id"` |
| _glpi_networkportaliases | `"networkports_id"` |
| glpi_networkportaliases | `"networkports_id_alias"` |
| _glpi_networkportconnectionlogs | `["networkports_id_destination", "networkports_id_source"]` |
| _glpi_networkportdialups | `"networkports_id"` |
| _glpi_networkportethernets | `"networkports_id"` |
| _glpi_networkportfiberchannels | `"networkports_id"` |
| _glpi_networkportlocals | `"networkports_id"` |
| _glpi_networkportmetrics | `"networkports_id"` |
| _glpi_networkports_networkports | `["networkports_id_1", "networkports_id_2"]` |
| _glpi_networkports_vlans | `"networkports_id"` |
| _glpi_networkportwifis | `"networkports_id"` |
| glpi_sockets | `"networkports_id"` |

## glpi_networkportwifis

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_networkportwifis | `"networkportwifis_id"` |

## glpi_networks

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_computers | `"networks_id"` |
| glpi_networkequipments | `"networks_id"` |
| glpi_printers | `"networks_id"` |
| glpi_unmanageds | `"networks_id"` |
| _glpi_appliances_items_relations | `[["items_id", "itemtype"]]` |

## glpi_notifications

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_notifications_notificationtemplates | `"notifications_id"` |
| _glpi_notificationtargets | `"notifications_id"` |

## glpi_notificationtemplates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_notifications_notificationtemplates | `"notificationtemplates_id"` |
| _glpi_notificationtemplatetranslations | `"notificationtemplates_id"` |
| _glpi_queuednotifications | `"notificationtemplates_id"` |

## glpi_olalevels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_olalevelactions | `"olalevels_id"` |
| _glpi_olalevelcriterias | `"olalevels_id"` |
| _glpi_olalevels_tickets | `"olalevels_id"` |

## glpi_olas

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_olalevels | `"olas_id"` |
| _glpi_items_olas | `"olas_id"` |

## glpi_operatingsystemarchitectures

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_items_operatingsystems | `"operatingsystemarchitectures_id"` |

## glpi_operatingsystemeditions

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_items_operatingsystems | `"operatingsystemeditions_id"` |

## glpi_operatingsystemkernels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_operatingsystemkernelversions | `"operatingsystemkernels_id"` |

## glpi_operatingsystemkernelversions

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_items_operatingsystems | `"operatingsystemkernelversions_id"` |

## glpi_operatingsystems

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_items_operatingsystems | `"operatingsystems_id"` |
| glpi_softwareversions | `"operatingsystems_id"` |

## glpi_operatingsystemservicepacks

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_items_operatingsystems | `"operatingsystemservicepacks_id"` |

## glpi_operatingsystemversions

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_items_operatingsystems | `"operatingsystemversions_id"` |

## glpi_passivedcequipmentmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_passivedcequipments | `"passivedcequipmentmodels_id"` |

## glpi_passivedcequipments

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_enclosures | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_racks | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_sockets | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_passivedcequipmenttypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_passivedcequipments | `"passivedcequipmenttypes_id"` |

## glpi_pdumodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_pdus | `"pdumodels_id"` |

## glpi_pdus

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_pdus_racks | `"pdus_id"` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_enclosures | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_racks | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_networkports | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepcis | `[["items_id", "itemtype"]]` |
| _glpi_items_devicegenerics | `[["items_id", "itemtype"]]` |
| glpi_ipaddresses | `[["mainitems_id", "mainitemtype"]]` |
| _glpi_plugs | `[["items_id_main", "itemtype_main"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_pdutypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_pdus | `"pdutypes_id"` |

## glpi_pendingreasons

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_pendingreasons_items | `"pendingreasons_id"` |
| glpi_itilreminders | `"pendingreasons_id"` |
| glpi_itilfollowuptemplates | `"pendingreasons_id"` |
| glpi_tasktemplates | `"pendingreasons_id"` |

## glpi_peripheralmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_peripherals | `"peripheralmodels_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_peripherals

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_appliances_items | `[["items_id", "itemtype"]]` |
| _glpi_certificates_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_enclosures | `[["items_id", "itemtype"]]` |
| _glpi_items_operatingsystems | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_racks | `[["items_id", "itemtype"]]` |
| _glpi_items_softwarelicenses | `[["items_id", "itemtype"]]` |
| _glpi_items_softwareversions | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |
| _glpi_networkports | `[["items_id", "itemtype"]]` |
| _glpi_reservationitems | `[["items_id", "itemtype"]]` |
| _glpi_sockets | `[["items_id", "itemtype"]]` |
| _glpi_items_devicenetworkcards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicedrives | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepcis | `[["items_id", "itemtype"]]` |
| _glpi_items_devicebatteries | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepowersupplies | `[["items_id", "itemtype"]]` |
| _glpi_items_devicefirmwares | `[["items_id", "itemtype"]]` |
| _glpi_items_devicecontrols | `[["items_id", "itemtype"]]` |
| _glpi_items_devicegenerics | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesimcards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesensors | `[["items_id", "itemtype"]]` |
| _glpi_items_devicememories | `[["items_id", "itemtype"]]` |
| _glpi_items_deviceharddrives | `[["items_id", "itemtype"]]` |
| glpi_ipaddresses | `[["mainitems_id", "mainitemtype"]]` |
| _glpi_assets_assets_peripheralassets | `[["itemtype_peripheral", "items_id_peripheral"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_peripheraltypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_peripherals | `"peripheraltypes_id"` |

## glpi_phonemodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_phones | `"phonemodels_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_phonepowersupplies

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_phones | `"phonepowersupplies_id"` |

## glpi_phones

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_agents | `[["items_id", "itemtype"]]` |
| _glpi_appliances_items | `[["items_id", "itemtype"]]` |
| _glpi_certificates_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_disks | `[["items_id", "itemtype"]]` |
| _glpi_items_operatingsystems | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_softwarelicenses | `[["items_id", "itemtype"]]` |
| _glpi_items_softwareversions | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_itemantiviruses | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |
| _glpi_networkports | `[["items_id", "itemtype"]]` |
| _glpi_reservationitems | `[["items_id", "itemtype"]]` |
| _glpi_sockets | `[["items_id", "itemtype"]]` |
| _glpi_items_devicenetworkcards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicegraphiccards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepcis | `[["items_id", "itemtype"]]` |
| _glpi_items_devicecameras | `[["items_id", "itemtype"]]` |
| _glpi_items_devicebatteries | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepowersupplies | `[["items_id", "itemtype"]]` |
| _glpi_items_devicemotherboards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicefirmwares | `[["items_id", "itemtype"]]` |
| _glpi_items_deviceprocessors | `[["items_id", "itemtype"]]` |
| _glpi_items_devicecontrols | `[["items_id", "itemtype"]]` |
| _glpi_items_devicegenerics | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesimcards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesensors | `[["items_id", "itemtype"]]` |
| _glpi_items_devicememories | `[["items_id", "itemtype"]]` |
| _glpi_items_deviceharddrives | `[["items_id", "itemtype"]]` |
| glpi_ipaddresses | `[["mainitems_id", "mainitemtype"]]` |
| _glpi_assets_assets_peripheralassets | `[["itemtype_peripheral", "items_id_peripheral"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_phonetypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_phones | `"phonetypes_id"` |

## glpi_planningeventcategories

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_planningexternalevents | `"planningeventcategories_id"` |
| glpi_planningexternaleventtemplates | `"planningeventcategories_id"` |

## glpi_planningexternalevents

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_vobjects | `[["items_id", "itemtype"]]` |

## glpi_planningexternaleventtemplates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_planningexternalevents | `"planningexternaleventtemplates_id"` |

## glpi_plugtypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_plugs | `"plugtypes_id"` |

## glpi_printermodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_cartridgeitems_printermodels | `"printermodels_id"` |
| glpi_printers | `"printermodels_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_printers

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_cartridges | `"printers_id"` |
| _glpi_printerlogs | `["items_id", "itemtype"]` |
| _glpi_printers_cartridgeinfos | `"printers_id"` |
| _glpi_appliances_items | `[["items_id", "itemtype"]]` |
| _glpi_certificates_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_disks | `[["items_id", "itemtype"]]` |
| _glpi_items_operatingsystems | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_softwarelicenses | `[["items_id", "itemtype"]]` |
| _glpi_items_softwareversions | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |
| _glpi_networkports | `[["items_id", "itemtype"]]` |
| _glpi_reservationitems | `[["items_id", "itemtype"]]` |
| _glpi_sockets | `[["items_id", "itemtype"]]` |
| _glpi_items_devicenetworkcards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicepcis | `[["items_id", "itemtype"]]` |
| _glpi_items_devicebatteries | `[["items_id", "itemtype"]]` |
| _glpi_items_devicefirmwares | `[["items_id", "itemtype"]]` |
| _glpi_items_devicecontrols | `[["items_id", "itemtype"]]` |
| _glpi_items_devicegenerics | `[["items_id", "itemtype"]]` |
| _glpi_items_devicesimcards | `[["items_id", "itemtype"]]` |
| _glpi_items_devicememories | `[["items_id", "itemtype"]]` |
| _glpi_items_deviceharddrives | `[["items_id", "itemtype"]]` |
| glpi_ipaddresses | `[["mainitems_id", "mainitemtype"]]` |
| _glpi_assets_assets_peripheralassets | `[["itemtype_peripheral", "items_id_peripheral"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_printertypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_printers | `"printertypes_id"` |

## glpi_problems

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_changes_problems | `"problems_id"` |
| _glpi_groups_problems | `"problems_id"` |
| _glpi_items_problems | `"problems_id"` |
| _glpi_itils_projects | `[["items_id", "itemtype"]]` |
| _glpi_itilfollowups | `[["items_id", "itemtype"]]` |
| _glpi_itilsolutions | `[["items_id", "itemtype"]]` |
| _glpi_problemcosts | `"problems_id"` |
| _glpi_problems_problems | `["problems_id_1", "problems_id_2"]` |
| _glpi_problems_suppliers | `"problems_id"` |
| _glpi_problems_tickets | `"problems_id"` |
| _glpi_problems_users | `"problems_id"` |
| _glpi_problemtasks | `"problems_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |

## glpi_problemtasks

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_vobjects | `[["items_id", "itemtype"]]` |

## glpi_problemtemplates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_entities | `"problemtemplates_id"` |
| glpi_itilcategories | `["problemtemplates_id"]` |
| glpi_problems | `"problemtemplates_id"` |
| _glpi_problemtemplatehiddenfields | `"problemtemplates_id"` |
| _glpi_problemtemplatemandatoryfields | `"problemtemplates_id"` |
| _glpi_problemtemplatepredefinedfields | `"problemtemplates_id"` |
| _glpi_problemtemplatereadonlyfields | `"problemtemplates_id"` |
| glpi_profiles | `"problemtemplates_id"` |

## glpi_profiles

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_knowbaseitems_profiles | `"profiles_id"` |
| _glpi_profilerights | `"profiles_id"` |
| _glpi_profiles_reminders | `"profiles_id"` |
| _glpi_profiles_rssfeeds | `"profiles_id"` |
| _glpi_profiles_users | `"profiles_id"` |
| glpi_users | `"profiles_id"` |

## glpi_projects

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_itils_projects | `"projects_id"` |
| _glpi_items_projects | `"projects_id"` |
| _glpi_projectcosts | `"projects_id"` |
| glpi_projects | `"projects_id"` |
| _glpi_projecttasks | `"projects_id"` |
| glpi_projecttasktemplates | `"projects_id"` |
| _glpi_projectteams | `"projects_id"` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_items_kanbans | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |

## glpi_projectstates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_projects | `"projectstates_id"` |
| glpi_projecttasks | `"projectstates_id"` |
| glpi_projecttasktemplates | `"projectstates_id"` |

## glpi_projecttasks

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_projecttasklinks | `["projecttasks_id_source", "projecttasks_id_target"]` |
| glpi_projecttasks | `"projecttasks_id"` |
| _glpi_projecttasks_tickets | `"projecttasks_id"` |
| _glpi_projecttaskteams | `"projecttasks_id"` |
| glpi_projecttasktemplates | `"projecttasks_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_vobjects | `[["items_id", "itemtype"]]` |

## glpi_projecttasktemplates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_projecttasks | `"projecttasktemplates_id"` |

## glpi_projecttasktypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_projecttasks | `"projecttasktypes_id"` |
| glpi_projecttasktemplates | `"projecttasktypes_id"` |

## glpi_projecttypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_projects | `"projecttypes_id"` |

## glpi_rackmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_racks | `"rackmodels_id"` |

## glpi_racks

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_items_racks | `"racks_id"` |
| _glpi_pdus_racks | `"racks_id"` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_reservationitems | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_racktypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_racks | `"racktypes_id"` |

## glpi_reminders

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_entities_reminders | `"reminders_id"` |
| _glpi_groups_reminders | `"reminders_id"` |
| _glpi_profiles_reminders | `"reminders_id"` |
| _glpi_remindertranslations | `"reminders_id"` |
| _glpi_reminders_users | `"reminders_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_vobjects | `[["items_id", "itemtype"]]` |

## glpi_requesttypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_itilfollowups | `"requesttypes_id"` |
| glpi_itilfollowuptemplates | `"requesttypes_id"` |
| glpi_tickets | `"requesttypes_id"` |
| glpi_users | `"default_requesttypes_id"` |

## glpi_reservationitems

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_reservations | `"reservationitems_id"` |

## glpi_rssfeeds

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_entities_rssfeeds | `"rssfeeds_id"` |
| _glpi_groups_rssfeeds | `"rssfeeds_id"` |
| _glpi_profiles_rssfeeds | `"rssfeeds_id"` |
| _glpi_rssfeeds_users | `"rssfeeds_id"` |

## glpi_rules

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_refusedequipments | `"rules_id"` |
| _glpi_ruleactions | `"rules_id"` |
| _glpi_rulecriterias | `"rules_id"` |
| glpi_rulematchedlogs | `"rules_id"` |

## glpi_savedsearches

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_savedsearches_alerts | `"savedsearches_id"` |
| _glpi_savedsearches_users | `"savedsearches_id"` |

## glpi_slalevels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_slalevelactions | `"slalevels_id"` |
| _glpi_slalevelcriterias | `"slalevels_id"` |
| _glpi_slalevels_tickets | `"slalevels_id"` |
| glpi_tickets | `"slalevels_id_ttr"` |

## glpi_slas

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_slalevels | `"slas_id"` |
| glpi_tickets | `["slas_id_ttr", "slas_id_tto"]` |

## glpi_slms

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_olas | `"slms_id"` |
| _glpi_slas | `"slms_id"` |

## glpi_snmpcredentials

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_networkequipments | `"snmpcredentials_id"` |
| glpi_pdus | `"snmpcredentials_id"` |
| glpi_printers | `"snmpcredentials_id"` |
| glpi_unmanageds | `"snmpcredentials_id"` |

## glpi_socketmodels

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_cables | `["socketmodels_id_endpoint_a", "socketmodels_id_endpoint_b"]` |
| glpi_sockets | `"socketmodels_id"` |

## glpi_sockets

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_cables | `["sockets_id_endpoint_a", "sockets_id_endpoint_b"]` |

## glpi_softwarecategories

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_softwarecategories | `"softwarecategories_id"` |
| glpi_softwares | `"softwarecategories_id"` |

## glpi_softwarelicenses

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_items_softwarelicenses | `"softwarelicenses_id"` |
| _glpi_softwarelicenses | `"softwarelicenses_id"` |
| _glpi_softwarelicenses_users | `"softwarelicenses_id"` |
| _glpi_certificates_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_softwarelicensetypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_softwarelicenses | `"softwarelicensetypes_id"` |
| _glpi_softwarelicensetypes | `"softwarelicensetypes_id"` |

## glpi_softwares

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_softwarelicenses | `"softwares_id"` |
| glpi_softwares | `"softwares_id"` |
| _glpi_softwareversions | `"softwares_id"` |
| _glpi_appliances_items | `[["items_id", "itemtype"]]` |
| _glpi_changes_items | `[["items_id", "itemtype"]]` |
| _glpi_contracts_items | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_infocoms | `[["items_id", "itemtype"]]` |
| _glpi_items_problems | `[["items_id", "itemtype"]]` |
| _glpi_items_projects | `[["items_id", "itemtype"]]` |
| _glpi_items_tickets | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |
| _glpi_reservationitems | `[["items_id", "itemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_softwareversions

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_items_softwareversions | `"softwareversions_id"` |
| glpi_softwarelicenses | `["softwareversions_id_buy", "softwareversions_id_use"]` |

## glpi_solutiontemplates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_pendingreasons | `"solutiontemplates_id"` |

## glpi_solutiontypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_itilsolutions | `"solutiontypes_id"` |
| glpi_solutiontemplates | `"solutiontypes_id"` |

## glpi_states

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_appliances | `"states_id"` |
| glpi_assets_assets | `"states_id"` |
| glpi_cables | `"states_id"` |
| glpi_certificates | `"states_id"` |
| glpi_clusters | `"states_id"` |
| glpi_computers | `"states_id"` |
| glpi_contracts | `"states_id"` |
| glpi_databaseinstances | `"states_id"` |
| glpi_enclosures | `"states_id"` |
| glpi_items_devicebatteries | `"states_id"` |
| glpi_items_devicecameras | `"states_id"` |
| glpi_items_devicecases | `"states_id"` |
| glpi_items_devicecontrols | `"states_id"` |
| glpi_items_devicedrives | `"states_id"` |
| glpi_items_devicefirmwares | `"states_id"` |
| glpi_items_devicegenerics | `"states_id"` |
| glpi_items_devicegraphiccards | `"states_id"` |
| glpi_items_deviceharddrives | `"states_id"` |
| glpi_items_devicememories | `"states_id"` |
| glpi_items_devicemotherboards | `"states_id"` |
| glpi_items_devicenetworkcards | `"states_id"` |
| glpi_items_devicepcis | `"states_id"` |
| glpi_items_devicepowersupplies | `"states_id"` |
| glpi_items_deviceprocessors | `"states_id"` |
| glpi_items_devicesensors | `"states_id"` |
| glpi_items_devicesimcards | `"states_id"` |
| glpi_items_devicesoundcards | `"states_id"` |
| glpi_lines | `"states_id"` |
| glpi_monitors | `"states_id"` |
| glpi_networkequipments | `"states_id"` |
| glpi_passivedcequipments | `"states_id"` |
| glpi_pdus | `"states_id"` |
| glpi_peripherals | `"states_id"` |
| glpi_phones | `"states_id"` |
| glpi_printers | `"states_id"` |
| glpi_racks | `"states_id"` |
| glpi_softwarelicenses | `"states_id"` |
| glpi_softwareversions | `"states_id"` |
| glpi_states | `"states_id"` |
| glpi_unmanageds | `"states_id"` |

## glpi_suppliers

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_changes_suppliers | `"suppliers_id"` |
| _glpi_contacts_suppliers | `"suppliers_id"` |
| _glpi_contracts_suppliers | `"suppliers_id"` |
| glpi_infocoms | `"suppliers_id"` |
| _glpi_problems_suppliers | `"suppliers_id"` |
| _glpi_suppliers_tickets | `"suppliers_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |

## glpi_suppliertypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_suppliers | `"suppliertypes_id"` |

## glpi_taskcategories

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_changetasks | `"taskcategories_id"` |
| glpi_problemtasks | `"taskcategories_id"` |
| glpi_taskcategories | `"taskcategories_id"` |
| glpi_tasktemplates | `"taskcategories_id"` |
| glpi_tickettasks | `"taskcategories_id"` |

## glpi_tasktemplates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_changetasks | `"tasktemplates_id"` |
| glpi_problemtasks | `"tasktemplates_id"` |
| glpi_tickettasks | `"tasktemplates_id"` |

## glpi_ticketrecurrents

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_items_ticketrecurrents | `"ticketrecurrents_id"` |

## glpi_tickets

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_changes_tickets | `"tickets_id"` |
| glpi_documents | `"tickets_id"` |
| _glpi_groups_tickets | `"tickets_id"` |
| _glpi_items_tickets | `"tickets_id"` |
| _glpi_itils_projects | `[["items_id", "itemtype"]]` |
| _glpi_itilfollowups | `[["items_id", "itemtype"]]` |
| _glpi_itils_validationsteps | `[["items_id", "itemtype"]]` |
| _glpi_itilsolutions | `[["items_id", "itemtype"]]` |
| _glpi_olalevels_tickets | `"tickets_id"` |
| _glpi_problems_tickets | `"tickets_id"` |
| _glpi_projecttasks_tickets | `"tickets_id"` |
| _glpi_slalevels_tickets | `"tickets_id"` |
| _glpi_suppliers_tickets | `"tickets_id"` |
| _glpi_ticketcosts | `"tickets_id"` |
| _glpi_tickets_contracts | `"tickets_id"` |
| _glpi_tickets_tickets | `["tickets_id_1", "tickets_id_2"]` |
| _glpi_tickets_users | `"tickets_id"` |
| _glpi_ticketsatisfactions | `"tickets_id"` |
| _glpi_tickettasks | `"tickets_id"` |
| _glpi_ticketvalidations | `"tickets_id"` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_knowbaseitems_items | `[["items_id", "itemtype"]]` |

## glpi_tickettasks

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |
| _glpi_vobjects | `[["items_id", "itemtype"]]` |

## glpi_tickettemplates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_entities | `"tickettemplates_id"` |
| glpi_itilcategories | `["tickettemplates_id_incident", "tickettemplates_id_demand"]` |
| glpi_profiles | `"tickettemplates_id"` |
| glpi_tickets | `"tickettemplates_id"` |
| glpi_ticketrecurrents | `"tickettemplates_id"` |
| _glpi_tickettemplatehiddenfields | `"tickettemplates_id"` |
| _glpi_tickettemplatemandatoryfields | `"tickettemplates_id"` |
| _glpi_tickettemplatepredefinedfields | `"tickettemplates_id"` |
| _glpi_tickettemplatereadonlyfields | `"tickettemplates_id"` |

## glpi_transfers

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_entities | `"transfers_id"` |

## glpi_unmanageds

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_domains_items | `[["items_id", "itemtype"]]` |
| _glpi_networkports | `[["items_id", "itemtype"]]` |
| glpi_ipaddresses | `[["mainitems_id", "mainitemtype"]]` |
| _glpi_groups_items | `[["itemtype", "items_id"]]` |

## glpi_usercategories

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_users | `"usercategories_id"` |

## glpi_users

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_appliances | `["users_id_tech", "users_id"]` |
| glpi_assets_assets | `["users_id_tech", "users_id"]` |
| glpi_cables | `["users_id_tech", "users_id"]` |
| glpi_cartridgeitems | `["users_id_tech", "users_id"]` |
| glpi_certificates | `["users_id_tech", "users_id"]` |
| glpi_changes | `["users_id_recipient", "users_id_lastupdater"]` |
| glpi_changecosts | `["users_id", "users_id_lastupdater"]` |
| _glpi_changes_users | `"users_id"` |
| glpi_changetasks | `["users_id", "users_id_editor", "users_id_tech"]` |
| glpi_changevalidations | `["users_id", "users_id_validate"]` |
| glpi_clusters | `["users_id_tech", "users_id"]` |
| glpi_computers | `["users_id_tech", "users_id"]` |
| glpi_consumableitems | `["users_id_tech", "users_id"]` |
| glpi_contractcosts | `["users_id", "users_id_lastupdater"]` |
| _glpi_dashboards_dashboards | `"users_id"` |
| glpi_dashboards_filters | `"users_id"` |
| glpi_databaseinstances | `["users_id_tech", "users_id"]` |
| _glpi_displaypreferences | `"users_id"` |
| glpi_domains | `["users_id_tech", "users_id"]` |
| glpi_domainrecords | `["users_id_tech", "users_id"]` |
| glpi_documents | `"users_id"` |
| glpi_documents_items | `"users_id"` |
| glpi_enclosures | `["users_id_tech", "users_id"]` |
| glpi_forms_answerssets | `"users_id"` |
| _glpi_groups_users | `"users_id"` |
| glpi_items_devicesimcards | `["users_id_tech", "users_id"]` |
| _glpi_items_kanbans | `"users_id"` |
| glpi_itilcategories | `"users_id"` |
| glpi_itilfollowups | `["users_id", "users_id_editor"]` |
| glpi_itilsolutions | `["users_id_approval", "users_id_editor", "users_id"]` |
| glpi_knowbaseitems | `"users_id"` |
| glpi_knowbaseitems_comments | `"users_id"` |
| glpi_knowbaseitems_revisions | `"users_id"` |
| _glpi_knowbaseitems_favorites | `"users_id"` |
| _glpi_knowbaseitems_users | `"users_id"` |
| glpi_knowbaseitemtranslations | `"users_id"` |
| glpi_lines | `["users_id_tech", "users_id"]` |
| glpi_monitors | `["users_id_tech", "users_id"]` |
| glpi_networkequipments | `["users_id_tech", "users_id"]` |
| glpi_notepads | `["users_id", "users_id_lastupdater"]` |
| glpi_notimportedemails | `"users_id"` |
| _glpi_objectlocks | `"users_id"` |
| glpi_passivedcequipments | `["users_id_tech", "users_id"]` |
| glpi_pdus | `["users_id_tech", "users_id"]` |
| glpi_peripherals | `["users_id_tech", "users_id"]` |
| glpi_phones | `["users_id_tech", "users_id"]` |
| glpi_planningexternalevents | `"users_id"` |
| glpi_planningrecalls | `"users_id"` |
| glpi_printers | `["users_id_tech", "users_id"]` |
| glpi_problems | `["users_id_recipient", "users_id_lastupdater"]` |
| glpi_problemcosts | `["users_id", "users_id_lastupdater"]` |
| _glpi_problems_users | `"users_id"` |
| glpi_problemtasks | `["users_id", "users_id_editor", "users_id_tech"]` |
| _glpi_profiles_users | `"users_id"` |
| glpi_projects | `"users_id"` |
| glpi_projectcosts | `["users_id", "users_id_lastupdater"]` |
| glpi_projecttasks | `"users_id"` |
| glpi_projecttasktemplates | `"users_id"` |
| glpi_racks | `["users_id_tech", "users_id"]` |
| _glpi_reminders | `"users_id"` |
| _glpi_reminders_users | `"users_id"` |
| _glpi_remindertranslations | `"users_id"` |
| glpi_reservations | `"users_id"` |
| glpi_rssfeeds | `"users_id"` |
| _glpi_rssfeeds_users | `"users_id"` |
| _glpi_savedsearches | `"users_id"` |
| _glpi_savedsearches_users | `"users_id"` |
| glpi_sharetokens | `"users_id"` |
| glpi_softwarelicenses | `["users_id_tech", "users_id"]` |
| glpi_softwares | `["users_id_tech", "users_id"]` |
| glpi_tasktemplates | `"users_id_tech"` |
| glpi_tickets | `["users_id_recipient", "users_id_lastupdater"]` |
| glpi_ticketcosts | `["users_id", "users_id_lastupdater"]` |
| _glpi_tickets_users | `"users_id"` |
| glpi_tickettasks | `["users_id", "users_id_editor", "users_id_tech"]` |
| glpi_ticketvalidations | `["users_id", "users_id_validate"]` |
| glpi_unmanageds | `["users_id_tech", "users_id"]` |
| _glpi_useremails | `"users_id"` |
| glpi_users | `"users_id_supervisor"` |
| _glpi_validatorsubstitutes | `["users_id", "users_id_substitute"]` |
| _glpi_softwarelicenses_users | `"users_id"` |
| _glpi_contracts_users | `"users_id"` |
| _glpi_certificates_items | `[["items_id", "itemtype"]]` |
| _glpi_consumables | `[["items_id", "itemtype"]]` |
| _glpi_documents_items | `[["items_id", "itemtype"]]` |

## glpi_usertitles

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_contacts | `"usertitles_id"` |
| glpi_users | `"usertitles_id"` |

## glpi_validationsteps

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_itilvalidationtemplates | `"validationsteps_id"` |
| glpi_itils_validationsteps | `"validationsteps_id"` |

## glpi_virtualmachinestates

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_itemvirtualmachines | `"virtualmachinestates_id"` |

## glpi_virtualmachinesystems

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_itemvirtualmachines | `"virtualmachinesystems_id"` |

## glpi_virtualmachinetypes

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_itemvirtualmachines | `"virtualmachinetypes_id"` |

## glpi_vlans

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_ipnetworks_vlans | `"vlans_id"` |
| _glpi_networkports_vlans | `"vlans_id"` |

## glpi_webhookcategories

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_webhookcategories | `"webhookcategories_id"` |
| glpi_webhooks | `"webhookcategories_id"` |

## glpi_webhooks

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| _glpi_queuedwebhooks | `"webhooks_id"` |

## glpi_wifinetworks

| Tabela ligada (nome no mapa) | Coluna ou estrutura de ligação |
| --- | --- |
| glpi_networkportwifis | `"wifinetworks_id"` |
