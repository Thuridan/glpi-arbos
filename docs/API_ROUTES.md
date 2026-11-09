# Catálogo das rotas da API de alto nível

Snapshot obtido por introspecção de `Router::getAllRoutes()` em Dev. Versão padrão do roteador: `3.0.0`.

Prefixar os caminhos abaixo com `/api.php` ou `/api.php/v<versão>`. O catálogo inclui as declarações de todas as versões; disponibilidade depende de `introduced`, `deprecated`, `removed`, configuração e permissões.

Entradas idênticas retornadas pelo registro foram deduplicadas. Um método HTTP múltiplo permanece na mesma linha. Segurança 0 significa rota declarada sem autenticação; isso não ignora a configuração global que desativa a API.

Corpos, schemas e parâmetros completos são definidos pelas anotações `Doc` e pelo gerador OpenAPI. Este catálogo não substitui o contrato `/api.php/doc.json`.

| Controller | Rotas únicas |
| --- | --- |
| AdministrationController | 60 |
| AssetController | 172 |
| ComponentController | 17 |
| CoreController | 16 |
| CustomAssetController | 16 |
| DropdownController | 16 |
| GraphQLController | 2 |
| ITILController | 58 |
| InventoryController | 8 |
| KnowbaseController | 19 |
| ManagementController | 46 |
| NotepadController | 5 |
| NotificationController | 27 |
| ProjectController | 42 |
| ReportController | 8 |
| RuleController | 20 |
| SecurityController | 4 |
| SetupController | 28 |
| ToolController | 6 |

## AdministrationController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Administration/Entity` | 2.0 / — / — | 1 / api | [searchEntities](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1229) |
| POST | `/Administration/Entity` | 2.0 / — / — | 1 / api | [createEntity](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1635) |
| DELETE | `/Administration/Entity/{id}` | 2.0 / — / — | 1 / api | [deleteEntityByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1659) |
| GET | `/Administration/Entity/{id}` | 2.0 / — / — | 1 / api | [getEntityByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1643) |
| PATCH | `/Administration/Entity/{id}` | 2.0 / — / — | 1 / api | [updateEntityByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1651) |
| GET | `/Administration/Entity/{items_id}/KBArticle` | 2.3 / — / — | 1 / api | [searchKBArticleItemLinks](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1945) |
| POST | `/Administration/Entity/{items_id}/KBArticle` | 2.3 / — / — | 1 / api | [createKBArticleItemLink](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1921) |
| DELETE | `/Administration/Entity/{items_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [deleteKBArticleItemLink](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1988) |
| GET | `/Administration/Entity/{items_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [getKBArticleItemLink](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1960) |
| PATCH | `/Administration/Entity/{items_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [updateKBArticleItemLink](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1975) |
| GET | `/Administration/EventLog` | 2.2 / — / — | 1 / api | [searchEventLogs](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1751) |
| GET | `/Administration/EventLog/{id}` | 2.2 / — / — | 1 / api | [getEventLogByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1759) |
| GET | `/Administration/Group` | 2.0 / — / — | 1 / api | [searchGroups](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1221) |
| POST | `/Administration/Group` | 2.0 / — / — | 1 / api | [createGroup](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1603) |
| DELETE | `/Administration/Group/{id}` | 2.0 / — / — | 1 / api | [deleteGroupByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1627) |
| GET | `/Administration/Group/{id}` | 2.0 / — / — | 1 / api | [getGroupByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1611) |
| PATCH | `/Administration/Group/{id}` | 2.0 / — / — | 1 / api | [updateGroupByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1619) |
| GET | `/Administration/Profile` | 2.0 / — / — | 1 / api | [searchProfiles](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1237) |
| POST | `/Administration/Profile` | 2.0 / — / — | 1 / api | [createProfile](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1667) |
| DELETE | `/Administration/Profile/{id}` | 2.0 / — / — | 1 / api | [deleteProfileByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1691) |
| GET | `/Administration/Profile/{id}` | 2.0 / — / — | 1 / api | [getProfileByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1675) |
| PATCH | `/Administration/Profile/{id}` | 2.0 / — / — | 1 / api | [updateProfileByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1683) |
| GET | `/Administration/User` | 2.0 / — / — | 1 / api | [searchUsers](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1213) |
| POST | `/Administration/User` | 2.0 / — / — | 1 / api | [createUser](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1428) |
| GET | `/Administration/User/Me` | 2.0 / — / — | 1 / user | [me](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1278) |
| GET | `/Administration/User/Me/Email` | 2.0 / — / — | 1 / user | [getMyEmails](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1292) |
| POST | `/Administration/User/Me/Email` | 2.0 / — / — | 1 / user | [addMyEmail](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1317) |
| GET | `/Administration/User/Me/Email/{id}` | 2.0 / — / — | 1 / user | [getMyEmail](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1362) |
| GET | `/Administration/User/Me/Emails/Default` | 2.0 / — / — | 1 / user, email | [getMyDefaultEmail](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1379) |
| GET | `/Administration/User/Me/ManagedItem` | 2.0 / — / — | 1 / user | [getMyManagedItems](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1574) |
| GET | `/Administration/User/Me/Picture` | 2.0 / — / — | 1 / user | [getMyPicture](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1411) |
| GET | `/Administration/User/Me/Preference` | 2.1 / — / — | 1 / api | [getMyPreferences](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1707) |
| PATCH | `/Administration/User/Me/Preference` | 2.1 / — / — | 1 / api | [updateMyPreferences](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1733) |
| GET | `/Administration/User/Me/UsedItem` | 2.0 / — / — | 1 / user | [getMyUsedItems](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1543) |
| DELETE | `/Administration/User/username/{username}` | 2.0 / — / — | 1 / api | [deleteUserByUsername](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1514) |
| GET | `/Administration/User/username/{username}` | 2.0 / — / — | 1 / api | [getUserByUsername](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1444) |
| PATCH | `/Administration/User/username/{username}` | 2.0 / — / — | 1 / api | [updateUserByUsername](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1498) |
| GET | `/Administration/User/username/{username}/ManagedItem` | 2.0 / — / — | 1 / api | [getUserManagedItemsByUsername](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1594) |
| GET | `/Administration/User/username/{username}/Picture` | 2.0 / — / — | 1 / api | [getUserPictureByUsername](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1473) |
| GET | `/Administration/User/username/{username}/UsedItem` | 2.0 / — / — | 1 / api | [getUserUsedItemsByUsername](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1563) |
| DELETE | `/Administration/User/{id}` | 2.0 / — / — | 1 / api | [deleteUserByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1506) |
| GET | `/Administration/User/{id}` | 2.0 / — / — | 1 / api | [getUserByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1436) |
| PATCH | `/Administration/User/{id}` | 2.0 / — / — | 1 / api | [updateUserByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1490) |
| GET | `/Administration/User/{id}/ManagedItem` | 2.0 / — / — | 1 / api | [getUserManagedItemsByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1584) |
| GET | `/Administration/User/{id}/Picture` | 2.0 / — / — | 1 / api | [getUserPictureByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1454) |
| GET | `/Administration/User/{id}/Preference` | 2.1 / — / — | 1 / api | [getUserPreferencesByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1699) |
| PATCH | `/Administration/User/{id}/Preference` | 2.1 / — / — | 1 / api | [updateUserPreferencesByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1725) |
| GET | `/Administration/User/{id}/UsedItem` | 2.0 / — / — | 1 / api | [getUserUsedItemsByID](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1553) |
| GET | `/Administration/User/{username}/Preference` | 2.1 / — / — | 1 / api | [getUserPreferencesByUsername](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1716) |
| PATCH | `/Administration/User/{username}/Preference` | 2.1 / — / — | 1 / api | [updateUserPreferencesByUsername](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1742) |
| GET | `/Administration/User/{users_id}/Certificate` | 2.3 / — / — | 1 / api | [searchCertificateItemLinks](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1864) |
| POST | `/Administration/User/{users_id}/Certificate` | 2.3 / — / — | 1 / api | [createCertificateItemLink](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1840) |
| DELETE | `/Administration/User/{users_id}/Certificate/{id}` | 2.3 / — / — | 1 / api | [deleteCertificateItemLink](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1908) |
| GET | `/Administration/User/{users_id}/Certificate/{id}` | 2.3 / — / — | 1 / api | [getCertificateItemLink](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1879) |
| PATCH | `/Administration/User/{users_id}/Certificate/{id}` | 2.3 / — / — | 1 / api | [updateCertificateItemLink](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1894) |
| GET | `/Administration/{itemtype}` | 2.2 / — / — | 1 / api | [search22](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1771) |
| POST | `/Administration/{itemtype}` | 2.2 / — / — | 1 / api | [createItem22](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1798) |
| DELETE | `/Administration/{itemtype}/{id}` | 2.2 / — / — | 1 / api | [deleteItem22](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1826) |
| GET | `/Administration/{itemtype}/{id}` | 2.2 / — / — | 1 / api | [getItem22](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1785) |
| PATCH | `/Administration/{itemtype}/{id}` | 2.2 / — / — | 1 / api | [updateItem22](../src/Glpi/Api/HL/Controller/AdministrationController.php#L1812) |

## AssetController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Assets/` | 2.0 / — / — | 1 / api | [index](../src/Glpi/Api/HL/Controller/AssetController.php#L2806) |
| GET | `/Assets/Cable` | 2.0 / — / — | 1 / api | [searchCables](../src/Glpi/Api/HL/Controller/AssetController.php#L3545) |
| POST | `/Assets/Cable` | 2.0 / — / — | 1 / api | [createCable](../src/Glpi/Api/HL/Controller/AssetController.php#L3561) |
| DELETE | `/Assets/Cable/{id}` | 2.0 / — / — | 1 / api | [deleteCable](../src/Glpi/Api/HL/Controller/AssetController.php#L3577) |
| GET | `/Assets/Cable/{id}` | 2.0 / — / — | 1 / api | [getCable](../src/Glpi/Api/HL/Controller/AssetController.php#L3553) |
| PATCH | `/Assets/Cable/{id}` | 2.0 / — / — | 1 / api | [updateCable](../src/Glpi/Api/HL/Controller/AssetController.php#L3569) |
| GET | `/Assets/Cartridge` | 2.0 / — / — | 1 / api | [searchCartridgeItems](../src/Glpi/Api/HL/Controller/AssetController.php#L3051) |
| POST | `/Assets/Cartridge` | 2.0 / — / — | 1 / api | [createCartridgeItems](../src/Glpi/Api/HL/Controller/AssetController.php#L3075) |
| POST | `/Assets/Cartridge/{cartridgeitems_id}` | 2.0 / — / — | 1 / api | [createCartridges](../src/Glpi/Api/HL/Controller/AssetController.php#L3122) |
| DELETE | `/Assets/Cartridge/{cartridgeitems_id}/{id}` | 2.0 / — / — | 1 / api | [deleteCartridges](../src/Glpi/Api/HL/Controller/AssetController.php#L3144) |
| GET | `/Assets/Cartridge/{cartridgeitems_id}/{id}` | 2.0 / — / — | 1 / api | [getCartridge](../src/Glpi/Api/HL/Controller/AssetController.php#L3112) |
| PATCH | `/Assets/Cartridge/{cartridgeitems_id}/{id}` | 2.0 / — / — | 1 / api | [updateCartridges](../src/Glpi/Api/HL/Controller/AssetController.php#L3133) |
| DELETE | `/Assets/Cartridge/{id}` | 2.0 / — / — | 1 / api | [deleteCartridgeItems](../src/Glpi/Api/HL/Controller/AssetController.php#L3101) |
| GET | `/Assets/Cartridge/{id}` | 2.0 / — / — | 1 / api | [getCartridgeItem](../src/Glpi/Api/HL/Controller/AssetController.php#L3064) |
| PATCH | `/Assets/Cartridge/{id}` | 2.0 / — / — | 1 / api | [updateCartridgeItems](../src/Glpi/Api/HL/Controller/AssetController.php#L3088) |
| GET | `/Assets/Consumable` | 2.0 / — / — | 1 / api | [searchConsumableItems](../src/Glpi/Api/HL/Controller/AssetController.php#L3155) |
| POST | `/Assets/Consumable` | 2.0 / — / — | 1 / api | [createConsumableItems](../src/Glpi/Api/HL/Controller/AssetController.php#L3177) |
| POST | `/Assets/Consumable/{consumableitems_id}` | 2.0 / — / — | 1 / api | [createConsumables](../src/Glpi/Api/HL/Controller/AssetController.php#L3218) |
| DELETE | `/Assets/Consumable/{consumableitems_id}/{id}` | 2.0 / — / — | 1 / api | [deleteConsumable](../src/Glpi/Api/HL/Controller/AssetController.php#L3240) |
| GET | `/Assets/Consumable/{consumableitems_id}/{id}` | 2.0 / — / — | 1 / api | [getConsumable](../src/Glpi/Api/HL/Controller/AssetController.php#L3210) |
| PATCH | `/Assets/Consumable/{consumableitems_id}/{id}` | 2.0 / — / — | 1 / api | [updateConsumable](../src/Glpi/Api/HL/Controller/AssetController.php#L3229) |
| DELETE | `/Assets/Consumable/{id}` | 2.0 / — / — | 1 / api | [deleteConsumableItems](../src/Glpi/Api/HL/Controller/AssetController.php#L3199) |
| GET | `/Assets/Consumable/{id}` | 2.0 / — / — | 1 / api | [getConsumableItem](../src/Glpi/Api/HL/Controller/AssetController.php#L3166) |
| PATCH | `/Assets/Consumable/{id}` | 2.0 / — / — | 1 / api | [updateConsumableItems](../src/Glpi/Api/HL/Controller/AssetController.php#L3188) |
| GET | `/Assets/Enclosure` | 2.0 / — / — | 1 / api | [searchEnclosure](../src/Glpi/Api/HL/Controller/AssetController.php#L3410) |
| POST | `/Assets/Enclosure` | 2.0 / — / — | 1 / api | [createEnclosure](../src/Glpi/Api/HL/Controller/AssetController.php#L3426) |
| DELETE | `/Assets/Enclosure/{id}` | 2.0 / — / — | 1 / api | [deleteEnclosure](../src/Glpi/Api/HL/Controller/AssetController.php#L3442) |
| GET | `/Assets/Enclosure/{id}` | 2.0 / — / — | 1 / api | [getEnclosure](../src/Glpi/Api/HL/Controller/AssetController.php#L3418) |
| PATCH | `/Assets/Enclosure/{id}` | 2.0 / — / — | 1 / api | [updateEnclosure](../src/Glpi/Api/HL/Controller/AssetController.php#L3434) |
| GET | `/Assets/Global` | 2.0 / — / — | 1 / api | [searchAll](../src/Glpi/Api/HL/Controller/AssetController.php#L2835) |
| GET | `/Assets/PDU` | 2.0 / — / — | 1 / api | [searchPDU](../src/Glpi/Api/HL/Controller/AssetController.php#L3450) |
| POST | `/Assets/PDU` | 2.0 / — / — | 1 / api | [createPDU](../src/Glpi/Api/HL/Controller/AssetController.php#L3466) |
| DELETE | `/Assets/PDU/{id}` | 2.0 / — / — | 1 / api | [deletePDU](../src/Glpi/Api/HL/Controller/AssetController.php#L3482) |
| GET | `/Assets/PDU/{id}` | 2.0 / — / — | 1 / api | [getPDU](../src/Glpi/Api/HL/Controller/AssetController.php#L3458) |
| PATCH | `/Assets/PDU/{id}` | 2.0 / — / — | 1 / api | [updatePDU](../src/Glpi/Api/HL/Controller/AssetController.php#L3474) |
| GET | `/Assets/PassiveDCEquipment` | 2.0 / — / — | 1 / api | [searchPassiveDCEquipment](../src/Glpi/Api/HL/Controller/AssetController.php#L3493) |
| POST | `/Assets/PassiveDCEquipment` | 2.0 / — / — | 1 / api | [createPassiveDCEquipment](../src/Glpi/Api/HL/Controller/AssetController.php#L3515) |
| DELETE | `/Assets/PassiveDCEquipment/{id}` | 2.0 / — / — | 1 / api | [deletePassiveDCEquipment](../src/Glpi/Api/HL/Controller/AssetController.php#L3537) |
| GET | `/Assets/PassiveDCEquipment/{id}` | 2.0 / — / — | 1 / api | [getPassiveDCEquipment](../src/Glpi/Api/HL/Controller/AssetController.php#L3504) |
| PATCH | `/Assets/PassiveDCEquipment/{id}` | 2.0 / — / — | 1 / api | [updatePassiveDCEquipment](../src/Glpi/Api/HL/Controller/AssetController.php#L3526) |
| GET | `/Assets/Rack` | 2.0 / — / — | 1 / api | [searchRack](../src/Glpi/Api/HL/Controller/AssetController.php#L3288) |
| POST | `/Assets/Rack` | 2.0 / — / — | 1 / api | [createRack](../src/Glpi/Api/HL/Controller/AssetController.php#L3304) |
| DELETE | `/Assets/Rack/{id}` | 2.0 / — / — | 1 / api | [deleteRack](../src/Glpi/Api/HL/Controller/AssetController.php#L3320) |
| GET | `/Assets/Rack/{id}` | 2.0 / — / — | 1 / api | [getRack](../src/Glpi/Api/HL/Controller/AssetController.php#L3296) |
| PATCH | `/Assets/Rack/{id}` | 2.0 / — / — | 1 / api | [updateRack](../src/Glpi/Api/HL/Controller/AssetController.php#L3312) |
| GET | `/Assets/Rack/{rack_id}/Item` | 2.0 / — / — | 1 / api | [getRackItems](../src/Glpi/Api/HL/Controller/AssetController.php#L3331) |
| POST | `/Assets/Rack/{rack_id}/Item` | 2.0 / — / — | 1 / api | [createRackItem](../src/Glpi/Api/HL/Controller/AssetController.php#L3372) |
| DELETE | `/Assets/Rack/{rack_id}/Item/{id}` | 2.0 / — / — | 1 / api | [deleteRackItem](../src/Glpi/Api/HL/Controller/AssetController.php#L3402) |
| GET | `/Assets/Rack/{rack_id}/Item/{id}` | 2.0 / — / — | 1 / api | [getRackItem](../src/Glpi/Api/HL/Controller/AssetController.php#L3346) |
| PATCH | `/Assets/Rack/{rack_id}/Item/{id}` | 2.0 / — / — | 1 / api | [updateRackItem](../src/Glpi/Api/HL/Controller/AssetController.php#L3361) |
| GET | `/Assets/Socket` | 2.0 / — / — | 1 / api | [searchSockets](../src/Glpi/Api/HL/Controller/AssetController.php#L3585) |
| POST | `/Assets/Socket` | 2.0 / — / — | 1 / api | [createSocket](../src/Glpi/Api/HL/Controller/AssetController.php#L3601) |
| DELETE | `/Assets/Socket/{id}` | 2.0 / — / — | 1 / api | [deleteSocket](../src/Glpi/Api/HL/Controller/AssetController.php#L3617) |
| GET | `/Assets/Socket/{id}` | 2.0 / — / — | 1 / api | [getSocket](../src/Glpi/Api/HL/Controller/AssetController.php#L3593) |
| PATCH | `/Assets/Socket/{id}` | 2.0 / — / — | 1 / api | [updateSocket](../src/Glpi/Api/HL/Controller/AssetController.php#L3609) |
| GET | `/Assets/Software` | 2.0 / — / — | 1 / api | [searchSoftware](../src/Glpi/Api/HL/Controller/AssetController.php#L3248) |
| POST | `/Assets/Software` | 2.0 / — / — | 1 / api | [createSoftware](../src/Glpi/Api/HL/Controller/AssetController.php#L3264) |
| DELETE | `/Assets/Software/{id}` | 2.0 / — / — | 1 / api | [deleteSoftware](../src/Glpi/Api/HL/Controller/AssetController.php#L3280) |
| GET | `/Assets/Software/{id}` | 2.0 / — / — | 1 / api | [getSoftware](../src/Glpi/Api/HL/Controller/AssetController.php#L3256) |
| PATCH | `/Assets/Software/{id}` | 2.0 / — / — | 1 / api | [updateSoftware](../src/Glpi/Api/HL/Controller/AssetController.php#L3272) |
| GET | `/Assets/Software/{software_id}/Version` | 2.0 / — / — | 1 / api | [searchSoftwareVersions](../src/Glpi/Api/HL/Controller/AssetController.php#L3628) |
| POST | `/Assets/Software/{software_id}/Version` | 2.0 / — / — | 1 / api | [createSoftwareVersion](../src/Glpi/Api/HL/Controller/AssetController.php#L3655) |
| DELETE | `/Assets/Software/{software_id}/Version/{id}` | 2.0 / — / — | 1 / api | [deleteSoftwareVersion](../src/Glpi/Api/HL/Controller/AssetController.php#L3690) |
| GET | `/Assets/Software/{software_id}/Version/{id}` | 2.0 / — / — | 1 / api | [getSoftwareVersion](../src/Glpi/Api/HL/Controller/AssetController.php#L3643) |
| PATCH | `/Assets/Software/{software_id}/Version/{id}` | 2.0 / — / — | 1 / api | [updateSoftwareVersion](../src/Glpi/Api/HL/Controller/AssetController.php#L3676) |
| GET | `/Assets/SoftwareLicense` | 2.0 / 2.4 / 3.0 | 1 / api | [bcSearchSoftwareLicenses](../src/Glpi/Api/HL/Controller/AssetController.php#L4765) |
| POST | `/Assets/SoftwareLicense` | 2.0 / 2.4 / 3.0 | 1 / api | [bcCreateSoftwareLicense](../src/Glpi/Api/HL/Controller/AssetController.php#L4778) |
| GET | `/Assets/SoftwareLicense/{asset_id}/Antivirus` | 2.3 / 2.4 / 3.0 | 1 / api | [bcSearchSoftwareLicenseAntivirus](../src/Glpi/Api/HL/Controller/AssetController.php#L4912) |
| GET | `/Assets/SoftwareLicense/{asset_id}/Antivirus/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcGetSoftwareLicenseAntivirus](../src/Glpi/Api/HL/Controller/AssetController.php#L4920) |
| GET | `/Assets/SoftwareLicense/{asset_id}/Appliance/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcGetSoftwareLicenseApplianceLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4976) |
| GET | `/Assets/SoftwareLicense/{asset_id}/Certificate` | 2.3 / 2.4 / 3.0 | 1 / api | [bcSearchSoftwareLicenseCertificateItemLinks](../src/Glpi/Api/HL/Controller/AssetController.php#L4997) |
| POST | `/Assets/SoftwareLicense/{asset_id}/Certificate` | 2.3 / 2.4 / 3.0 | 1 / api | [bcCreateSoftwareLicenseCertificateItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4986) |
| DELETE | `/Assets/SoftwareLicense/{asset_id}/Certificate/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcDeleteSoftwareLicenseCertificateItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L5033) |
| GET | `/Assets/SoftwareLicense/{asset_id}/Certificate/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcGetSoftwareLicenseCertificateItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L5009) |
| PATCH | `/Assets/SoftwareLicense/{asset_id}/Certificate/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcUpdateSoftwareLicenseCertificateItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L5021) |
| GET | `/Assets/SoftwareLicense/{asset_id}/Contract` | 2.3 / 2.4 / 3.0 | 1 / api | [bcSearchSoftwareLicenseContractItemLinks](../src/Glpi/Api/HL/Controller/AssetController.php#L5113) |
| POST | `/Assets/SoftwareLicense/{asset_id}/Contract` | 2.3 / 2.4 / 3.0 | 1 / api | [bcCreateSoftwareLicenseContractItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L5102) |
| DELETE | `/Assets/SoftwareLicense/{asset_id}/Contract/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcDeleteSoftwareLicenseContractItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L5149) |
| GET | `/Assets/SoftwareLicense/{asset_id}/Contract/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcGetSoftwareLicenseContractItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L5125) |
| PATCH | `/Assets/SoftwareLicense/{asset_id}/Contract/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcUpdateSoftwareLicenseContractItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L5137) |
| GET | `/Assets/SoftwareLicense/{asset_id}/KBArticle` | 2.3 / 2.4 / 3.0 | 1 / api | [bcSearchSoftwareLicenseKBArticleItemLinks](../src/Glpi/Api/HL/Controller/AssetController.php#L5055) |
| POST | `/Assets/SoftwareLicense/{asset_id}/KBArticle` | 2.3 / 2.4 / 3.0 | 1 / api | [bcCreateSoftwareLicenseKBArticleItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L5044) |
| DELETE | `/Assets/SoftwareLicense/{asset_id}/KBArticle/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcDeleteSoftwareLicenseKBArticleItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L5091) |
| GET | `/Assets/SoftwareLicense/{asset_id}/KBArticle/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcGetSoftwareLicenseKBArticleItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L5067) |
| PATCH | `/Assets/SoftwareLicense/{asset_id}/KBArticle/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcUpdateSoftwareLicenseKBArticleItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L5079) |
| GET | `/Assets/SoftwareLicense/{asset_id}/PeripheralConnection` | 2.3 / 2.4 / 3.0 | 1 / api | [bcSearchSoftwareLicensePeripheralConnection](../src/Glpi/Api/HL/Controller/AssetController.php#L4944) |
| GET | `/Assets/SoftwareLicense/{asset_id}/PeripheralConnection/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcGetSoftwareLicensePeripheralConnection](../src/Glpi/Api/HL/Controller/AssetController.php#L4952) |
| GET | `/Assets/SoftwareLicense/{asset_id}/RemoteManagement` | 2.3 / 2.4 / 3.0 | 1 / api | [bcSearchSoftwareLicenseRemoteManagement](../src/Glpi/Api/HL/Controller/AssetController.php#L4960) |
| GET | `/Assets/SoftwareLicense/{asset_id}/RemoteManagement/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcGetSoftwareLicenseRemoteManagement](../src/Glpi/Api/HL/Controller/AssetController.php#L4968) |
| GET | `/Assets/SoftwareLicense/{asset_id}/SoftwareInstallation` | 2.2 / 2.4 / 3.0 | 1 / api | [bcSearchSoftwareLicenseSoftwareInstallation](../src/Glpi/Api/HL/Controller/AssetController.php#L4896) |
| GET | `/Assets/SoftwareLicense/{asset_id}/SoftwareInstallation/{id}` | 2.2 / 2.4 / 3.0 | 1 / api | [bcGetSoftwareLicenseSoftwareInstallation](../src/Glpi/Api/HL/Controller/AssetController.php#L4904) |
| GET | `/Assets/SoftwareLicense/{asset_id}/VirtualMachine` | 2.3 / 2.4 / 3.0 | 1 / api | [bcSearchSoftwareLicenseVM](../src/Glpi/Api/HL/Controller/AssetController.php#L4928) |
| GET | `/Assets/SoftwareLicense/{asset_id}/VirtualMachine/{id}` | 2.3 / 2.4 / 3.0 | 1 / api | [bcGetSoftwareLicenseVM](../src/Glpi/Api/HL/Controller/AssetController.php#L4936) |
| DELETE | `/Assets/SoftwareLicense/{id}` | 2.0 / 2.4 / 3.0 | 1 / api | [bcDeleteSoftwareLicense](../src/Glpi/Api/HL/Controller/AssetController.php#L4823) |
| GET | `/Assets/SoftwareLicense/{id}` | 2.0 / 2.4 / 3.0 | 1 / api | [bcGetSoftwareLicense](../src/Glpi/Api/HL/Controller/AssetController.php#L4793) |
| PATCH | `/Assets/SoftwareLicense/{id}` | 2.0 / 2.4 / 3.0 | 1 / api | [bcUpdateSoftwareLicense](../src/Glpi/Api/HL/Controller/AssetController.php#L4808) |
| DELETE | `/Assets/SoftwareLicense/{id}/Infocom` | 2.2 / 2.4 / 3.0 | 1 / api | [bcDeleteSoftwareLicenseInfocom](../src/Glpi/Api/HL/Controller/AssetController.php#L4883) |
| GET | `/Assets/SoftwareLicense/{id}/Infocom` | 2.2 / 2.4 / 3.0 | 1 / api | [bcGetSoftwareLicenseInfocom](../src/Glpi/Api/HL/Controller/AssetController.php#L4838) |
| PATCH | `/Assets/SoftwareLicense/{id}/Infocom` | 2.2 / 2.4 / 3.0 | 1 / api | [bcUpdateSoftwareLicenseInfocom](../src/Glpi/Api/HL/Controller/AssetController.php#L4868) |
| POST | `/Assets/SoftwareLicense/{id}/Infocom` | 2.2 / 2.4 / 3.0 | 1 / api | [bcCreateSoftwareLicenseInfocom](../src/Glpi/Api/HL/Controller/AssetController.php#L4853) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Antivirus` | 2.3 / — / — | 1 / api | [searchItemAntivirus](../src/Glpi/Api/HL/Controller/AssetController.php#L3884) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/Antivirus` | 2.3 / — / — | 1 / api | [createItemAntivirus](../src/Glpi/Api/HL/Controller/AssetController.php#L3859) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/Antivirus/{id}` | 2.3 / — / — | 1 / api | [deleteItemAntivirus](../src/Glpi/Api/HL/Controller/AssetController.php#L3929) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Antivirus/{id}` | 2.3 / — / — | 1 / api | [getItemAntivirus](../src/Glpi/Api/HL/Controller/AssetController.php#L3898) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/Antivirus/{id}` | 2.3 / — / — | 1 / api | [updateItemAntivirus](../src/Glpi/Api/HL/Controller/AssetController.php#L3916) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/Appliance` | 2.3 / — / — | 1 / api | [createItemApplianceLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4192) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/Appliance/{id}` | 2.3 / — / — | 1 / api | [deleteItemApplianceLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4217) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Appliance/{id}` | 2.3 / — / — | 1 / api | [getItemApplianceLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4230) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Certificate` | 2.3 / — / — | 1 / api | [searchCertificateItemLinks](../src/Glpi/Api/HL/Controller/AssetController.php#L4362) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/Certificate` | 2.3 / — / — | 1 / api | [createCertificateItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4336) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/Certificate/{id}` | 2.3 / — / — | 1 / api | [deleteCertificateItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4409) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Certificate/{id}` | 2.3 / — / — | 1 / api | [getCertificateItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4378) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/Certificate/{id}` | 2.3 / — / — | 1 / api | [updateCertificateItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4394) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Contract` | 2.3 / — / — | 1 / api | [searchContractItemLinks](../src/Glpi/Api/HL/Controller/AssetController.php#L4710) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/Contract` | 2.3 / — / — | 1 / api | [createContractItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4684) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/Contract/{id}` | 2.3 / — / — | 1 / api | [deleteContractItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4757) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Contract/{id}` | 2.3 / — / — | 1 / api | [getContractItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4726) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/Contract/{id}` | 2.3 / — / — | 1 / api | [updateContractItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4742) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Domain` | 2.3 / — / — | 1 / api | [searchDomainItemLinks](../src/Glpi/Api/HL/Controller/AssetController.php#L4275) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/Domain` | 2.3 / — / — | 1 / api | [createDomainItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4249) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/Domain/{id}` | 2.3 / — / — | 1 / api | [deleteDomainItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4322) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Domain/{id}` | 2.3 / — / — | 1 / api | [getDomainItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4291) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/Domain/{id}` | 2.3 / — / — | 1 / api | [updateDomainItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4307) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/KBArticle` | 2.3 / — / — | 1 / api | [searchKBArticleItemLinks](../src/Glpi/Api/HL/Controller/AssetController.php#L4623) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/KBArticle` | 2.3 / — / — | 1 / api | [createKBArticleItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4597) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [deleteKBArticleItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4670) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [getKBArticleItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4639) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [updateKBArticleItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4655) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Line` | 2.3 / — / — | 1 / api | [searchLineItemLinks](../src/Glpi/Api/HL/Controller/AssetController.php#L4536) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/Line` | 2.3 / — / — | 1 / api | [createLineItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4510) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/Line/{id}` | 2.3 / — / — | 1 / api | [deleteLineItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4583) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Line/{id}` | 2.3 / — / — | 1 / api | [getLineItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4552) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/Line/{id}` | 2.3 / — / — | 1 / api | [updateLineItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4568) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/OSInstallation` | 2.2 / — / — | 1 / api | [searchItemOSInstallation](../src/Glpi/Api/HL/Controller/AssetController.php#L3724) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/OSInstallation` | 2.2 / — / — | 1 / api | [createItemOSInstallation](../src/Glpi/Api/HL/Controller/AssetController.php#L3701) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/OSInstallation/{id}` | 2.2 / — / — | 1 / api | [deleteOSInstallation](../src/Glpi/Api/HL/Controller/AssetController.php#L3763) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/OSInstallation/{id}` | 2.2 / — / — | 1 / api | [getOSInstallation](../src/Glpi/Api/HL/Controller/AssetController.php#L3736) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/OSInstallation/{id}` | 2.2 / — / — | 1 / api | [updateOSInstallation](../src/Glpi/Api/HL/Controller/AssetController.php#L3752) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/PeripheralConnection` | 2.3 / — / — | 1 / api | [searchItemPeripheralConnection](../src/Glpi/Api/HL/Controller/AssetController.php#L4050) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/PeripheralConnection` | 2.3 / — / — | 1 / api | [createItemPeripheralConnection](../src/Glpi/Api/HL/Controller/AssetController.php#L4025) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/PeripheralConnection/{id}` | 2.3 / — / — | 1 / api | [deleteItemPeripheralConnection](../src/Glpi/Api/HL/Controller/AssetController.php#L4095) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/PeripheralConnection/{id}` | 2.3 / — / — | 1 / api | [getItemPeripheralConnection](../src/Glpi/Api/HL/Controller/AssetController.php#L4064) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/PeripheralConnection/{id}` | 2.3 / — / — | 1 / api | [updateItemPeripheralConnection](../src/Glpi/Api/HL/Controller/AssetController.php#L4082) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Project` | 2.3 / — / — | 1 / api | [searchProjectItemLinks](../src/Glpi/Api/HL/Controller/AssetController.php#L4449) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/Project` | 2.3 / — / — | 1 / api | [createProjectItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4423) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/Project/{id}` | 2.3 / — / — | 1 / api | [deleteProjectItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4496) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Project/{id}` | 2.3 / — / — | 1 / api | [getProjectItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4465) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/Project/{id}` | 2.3 / — / — | 1 / api | [updateProjectItemLink](../src/Glpi/Api/HL/Controller/AssetController.php#L4481) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/RemoteManagement` | 2.3 / — / — | 1 / api | [searchItemRemoteManagement](../src/Glpi/Api/HL/Controller/AssetController.php#L4134) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/RemoteManagement` | 2.3 / — / — | 1 / api | [createItemRemoteManagement](../src/Glpi/Api/HL/Controller/AssetController.php#L4109) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/RemoteManagement/{id}` | 2.3 / — / — | 1 / api | [deleteItemRemoteManagement](../src/Glpi/Api/HL/Controller/AssetController.php#L4179) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/RemoteManagement/{id}` | 2.3 / — / — | 1 / api | [getItemRemoteManagement](../src/Glpi/Api/HL/Controller/AssetController.php#L4148) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/RemoteManagement/{id}` | 2.3 / — / — | 1 / api | [updateItemRemoteManagement](../src/Glpi/Api/HL/Controller/AssetController.php#L4166) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/SoftwareInstallation` | 2.2 / — / — | 1 / api | [searchItemSoftware](../src/Glpi/Api/HL/Controller/AssetController.php#L3801) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/SoftwareInstallation` | 2.2 / — / — | 1 / api | [createItemSoftwareVersion](../src/Glpi/Api/HL/Controller/AssetController.php#L3776) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/SoftwareInstallation/{id}` | 2.2 / — / — | 1 / api | [deleteSoftwareInstallation](../src/Glpi/Api/HL/Controller/AssetController.php#L3846) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/SoftwareInstallation/{id}` | 2.2 / — / — | 1 / api | [getSoftwareInstallation](../src/Glpi/Api/HL/Controller/AssetController.php#L3815) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/SoftwareInstallation/{id}` | 2.2 / — / — | 1 / api | [updateSoftwareInstallation](../src/Glpi/Api/HL/Controller/AssetController.php#L3833) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/VirtualMachine` | 2.3 / — / — | 1 / api | [searchItemVirtualMachine](../src/Glpi/Api/HL/Controller/AssetController.php#L3967) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/VirtualMachine` | 2.3 / — / — | 1 / api | [createItemVirtualMachine](../src/Glpi/Api/HL/Controller/AssetController.php#L3942) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/VirtualMachine/{id}` | 2.3 / — / — | 1 / api | [deleteItemVirtualMachine](../src/Glpi/Api/HL/Controller/AssetController.php#L4012) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/VirtualMachine/{id}` | 2.3 / — / — | 1 / api | [getItemVirtualMachine](../src/Glpi/Api/HL/Controller/AssetController.php#L3981) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/VirtualMachine/{id}` | 2.3 / — / — | 1 / api | [updateItemVirtualMachine](../src/Glpi/Api/HL/Controller/AssetController.php#L3999) |
| GET | `/Assets/{itemtype}` | 2.0 / — / — | 1 / api | [search](../src/Glpi/Api/HL/Controller/AssetController.php#L2848) |
| POST | `/Assets/{itemtype}` | 2.0 / — / — | 1 / api | [createItem](../src/Glpi/Api/HL/Controller/AssetController.php#L3009) |
| DELETE | `/Assets/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [deleteItem](../src/Glpi/Api/HL/Controller/AssetController.php#L3039) |
| GET | `/Assets/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [getItem](../src/Glpi/Api/HL/Controller/AssetController.php#L2863) |
| PATCH | `/Assets/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [updateItem](../src/Glpi/Api/HL/Controller/AssetController.php#L3024) |
| DELETE | `/Assets/{itemtype}/{id}/Infocom` | 2.2 / — / — | 1 / api | [deleteItemInfocom](../src/Glpi/Api/HL/Controller/AssetController.php#L2975) |
| GET | `/Assets/{itemtype}/{id}/Infocom` | 2.0 / — / — | 1 / api | [getItemInfocom](../src/Glpi/Api/HL/Controller/AssetController.php#L2878) |
| PATCH | `/Assets/{itemtype}/{id}/Infocom` | 2.2 / — / — | 1 / api | [updateItemInfocom](../src/Glpi/Api/HL/Controller/AssetController.php#L2939) |
| POST | `/Assets/{itemtype}/{id}/Infocom` | 2.2 / — / — | 1 / api | [createItemInfocom](../src/Glpi/Api/HL/Controller/AssetController.php#L2908) |

## ComponentController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Assets/SoftwareLicense/{asset_id}/Volume` | 2.0 / — / 3.0 | 1 / api | [bcSearchSoftwareLicenseVolumes](../src/Glpi/Api/HL/Controller/ComponentController.php#L1133) |
| GET | `/Assets/SoftwareLicense/{asset_id}/Volume/{id}` | 2.3 / — / — | 1 / api | [bcGetSoftwareLicenseVolume](../src/Glpi/Api/HL/Controller/ComponentController.php#L1153) |
| GET | `/Assets/SoftwareLicense/{id}/Component/{component_type}` | 2.0 / — / 3.0 | 1 / api | [bcGetSoftwareLicenseComponents](../src/Glpi/Api/HL/Controller/ComponentController.php#L1114) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Volume` | 2.3 / — / — | 1 / api | [searchAssetVolumes](../src/Glpi/Api/HL/Controller/ComponentController.php#L1013) |
| POST | `/Assets/{asset_itemtype}/{asset_id}/Volume` | 2.3 / — / — | 1 / api | [createAssetVolume](../src/Glpi/Api/HL/Controller/ComponentController.php#L1049) |
| DELETE | `/Assets/{asset_itemtype}/{asset_id}/Volume/{id}` | 2.3 / — / — | 1 / api | [deleteAssetVolume](../src/Glpi/Api/HL/Controller/ComponentController.php#L1093) |
| GET | `/Assets/{asset_itemtype}/{asset_id}/Volume/{id}` | 2.3 / — / — | 1 / api | [getAssetVolume](../src/Glpi/Api/HL/Controller/ComponentController.php#L1033) |
| PATCH | `/Assets/{asset_itemtype}/{asset_id}/Volume/{id}` | 2.3 / — / — | 1 / api | [updateAssetVolume](../src/Glpi/Api/HL/Controller/ComponentController.php#L1077) |
| GET | `/Assets/{itemtype}/{id}/Component/{component_type}` | 2.0 / — / — | 1 / api | [getAssetComponentsByType](../src/Glpi/Api/HL/Controller/ComponentController.php#L993) |
| GET | `/Components` | 2.0 / — / — | 1 / api | [index](../src/Glpi/Api/HL/Controller/ComponentController.php#L841) |
| GET | `/Components/{component_type}` | 2.0 / — / — | 1 / api | [listComponentTypes](../src/Glpi/Api/HL/Controller/ComponentController.php#L866) |
| POST | `/Components/{component_type}` | 2.0 / — / — | 1 / api | [createComponentType](../src/Glpi/Api/HL/Controller/ComponentController.php#L895) |
| GET | `/Components/{component_type}/Items/{id}` | 2.0 / — / — | 1 / api | [getComponent](../src/Glpi/Api/HL/Controller/ComponentController.php#L975) |
| DELETE | `/Components/{component_type}/{id}` | 2.0 / — / — | 1 / api | [deleteComponentType](../src/Glpi/Api/HL/Controller/ComponentController.php#L960) |
| GET | `/Components/{component_type}/{id}` | 2.0 / — / — | 1 / api | [getComponentType](../src/Glpi/Api/HL/Controller/ComponentController.php#L881) |
| PATCH | `/Components/{component_type}/{id}` | 2.0 / — / — | 1 / api | [updateComponentType](../src/Glpi/Api/HL/Controller/ComponentController.php#L945) |
| GET | `/Components/{component_type}/{id}/Items` | 2.0 / — / — | 1 / api | [getComponentsOfType](../src/Glpi/Api/HL/Controller/ComponentController.php#L912) |

## CoreController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/` | 2.0 / — / — | 0 / api | [index](../src/Glpi/Api/HL/Controller/CoreController.php#L314) |
| GET | `/Session/EntityTree` | 2.2 / — / — | 1 / api | [getSessionEntityTree](../src/Glpi/Api/HL/Controller/CoreController.php#L910) |
| POST | `/Transfer` | 2.0 / — / — | 1 / api | [transferEntity](../src/Glpi/Api/HL/Controller/CoreController.php#L840) |
| GET, POST | `/authorize` | 2.0 / — / — | 0 / api | [authorize](../src/Glpi/Api/HL/Controller/CoreController.php#L660) |
| GET | `/doc` | 2.0 / — / — | 0 / api | [showDocumentation](../src/Glpi/Api/HL/Controller/CoreController.php#L327) |
| GET | `/doc.json` | 2.0 / — / — | 0 / api | [getOpenAPISchema](../src/Glpi/Api/HL/Controller/CoreController.php#L406) |
| GET | `/getting-started` | 2.0 / — / — | 0 / api | [showGettingStarted](../src/Glpi/Api/HL/Controller/CoreController.php#L416) |
| GET | `/locales` | 2.3 / — / — | 1 / api | [getLocales](../src/Glpi/Api/HL/Controller/CoreController.php#L929) |
| GET | `/session` | 2.0 / — / — | 1 / api | [getSession](../src/Glpi/Api/HL/Controller/CoreController.php#L538) |
| GET | `/status` | 2.0 / — / — | 1 / status | [status](../src/Glpi/Api/HL/Controller/CoreController.php#L754) |
| GET | `/status/all` | 2.0 / — / — | 0 / status | [statusAllServices](../src/Glpi/Api/HL/Controller/CoreController.php#L791) |
| GET | `/status/{service}` | 2.0 / — / — | 1 / status | [statusByService](../src/Glpi/Api/HL/Controller/CoreController.php#L818) |
| GET | `/swagger-oauth-redirect` | 2.0 / — / — | 0 / api | [swaggerOAuthRedirect](../src/Glpi/Api/HL/Controller/CoreController.php#L736) |
| POST | `/token` | 2.0 / — / — | 0 / api | [token](../src/Glpi/Api/HL/Controller/CoreController.php#L720) |
| GET, POST, PATCH, PUT, DELETE | `/{req}` | 2.0 / — / — | 1 / api | [defaultRoute](../src/Glpi/Api/HL/Controller/CoreController.php#L487) |
| OPTIONS | `/{req}` | 2.0 / — / — | 0 / api | [defaultOptionsRoute](../src/Glpi/Api/HL/Controller/CoreController.php#L498) |

## CustomAssetController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Assets/Custom/` | 2.0 / — / — | 1 / api | [index](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L375) |
| GET | `/Assets/Custom/{itemtype}` | 2.0 / — / — | 1 / api | [search](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L395) |
| POST | `/Assets/Custom/{itemtype}` | 2.0 / — / — | 1 / api | [createItem](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L422) |
| DELETE | `/Assets/Custom/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [deleteItem](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L452) |
| GET | `/Assets/Custom/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [getItem](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L410) |
| PATCH | `/Assets/Custom/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [updateItem](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L437) |
| GET | `/Assets/Custom/{itemtype}Model` | 2.0 / — / — | 1 / api | [searchModels](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L465) |
| POST | `/Assets/Custom/{itemtype}Model` | 2.0 / — / — | 1 / api | [createItemModel](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L494) |
| DELETE | `/Assets/Custom/{itemtype}Model/{id}` | 2.0 / — / — | 1 / api | [deleteItemModel](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L524) |
| GET | `/Assets/Custom/{itemtype}Model/{id}` | 2.0 / — / — | 1 / api | [getItemModel](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L480) |
| PATCH | `/Assets/Custom/{itemtype}Model/{id}` | 2.0 / — / — | 1 / api | [updateItemModel](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L509) |
| GET | `/Assets/Custom/{itemtype}Type` | 2.0 / — / — | 1 / api | [searchTypes](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L538) |
| POST | `/Assets/Custom/{itemtype}Type` | 2.0 / — / — | 1 / api | [createItemType](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L565) |
| DELETE | `/Assets/Custom/{itemtype}Type/{id}` | 2.0 / — / — | 1 / api | [deleteItemType](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L595) |
| GET | `/Assets/Custom/{itemtype}Type/{id}` | 2.0 / — / — | 1 / api | [getItemType](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L553) |
| PATCH | `/Assets/Custom/{itemtype}Type/{id}` | 2.0 / — / — | 1 / api | [updateItemType](../src/Glpi/Api/HL/Controller/CustomAssetController.php#L580) |

## DropdownController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Dropdowns/` | 2.0 / — / — | 1 / api | [index](../src/Glpi/Api/HL/Controller/DropdownController.php#L2333) |
| GET | `/Dropdowns/{itemtype}` | 2.0 / — / — | 1 / api | [search20](../src/Glpi/Api/HL/Controller/DropdownController.php#L2361) |
| GET | `/Dropdowns/{itemtype}` | 2.2 / — / — | 1 / api | [search22](../src/Glpi/Api/HL/Controller/DropdownController.php#L2434) |
| GET | `/Dropdowns/{itemtype}` | 2.3 / — / — | 1 / api | [search23](../src/Glpi/Api/HL/Controller/DropdownController.php#L2507) |
| POST | `/Dropdowns/{itemtype}` | 2.0 / — / — | 1 / api | [createItem20](../src/Glpi/Api/HL/Controller/DropdownController.php#L2390) |
| POST | `/Dropdowns/{itemtype}` | 2.2 / — / — | 1 / api | [createItem22](../src/Glpi/Api/HL/Controller/DropdownController.php#L2463) |
| POST | `/Dropdowns/{itemtype}` | 2.3 / — / — | 1 / api | [createItem23](../src/Glpi/Api/HL/Controller/DropdownController.php#L2536) |
| DELETE | `/Dropdowns/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [deleteItem20](../src/Glpi/Api/HL/Controller/DropdownController.php#L2420) |
| DELETE | `/Dropdowns/{itemtype}/{id}` | 2.2 / — / — | 1 / api | [deleteItem22](../src/Glpi/Api/HL/Controller/DropdownController.php#L2493) |
| DELETE | `/Dropdowns/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [deleteItem23](../src/Glpi/Api/HL/Controller/DropdownController.php#L2566) |
| GET | `/Dropdowns/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [getItem20](../src/Glpi/Api/HL/Controller/DropdownController.php#L2376) |
| GET | `/Dropdowns/{itemtype}/{id}` | 2.2 / — / — | 1 / api | [getItem22](../src/Glpi/Api/HL/Controller/DropdownController.php#L2449) |
| GET | `/Dropdowns/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [getItem23](../src/Glpi/Api/HL/Controller/DropdownController.php#L2522) |
| PATCH | `/Dropdowns/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [updateItem20](../src/Glpi/Api/HL/Controller/DropdownController.php#L2405) |
| PATCH | `/Dropdowns/{itemtype}/{id}` | 2.2 / — / — | 1 / api | [updateItem22](../src/Glpi/Api/HL/Controller/DropdownController.php#L2478) |
| PATCH | `/Dropdowns/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [updateItem23](../src/Glpi/Api/HL/Controller/DropdownController.php#L2551) |

## GraphQLController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| POST | `/GraphQL/` | 2.0 / — / — | 1 / graphql | [index](../src/Glpi/Api/HL/Controller/GraphQLController.php#L54) |
| GET | `/GraphQL/Schema` | 2.0 / — / — | 1 / graphql | [getSchema](../src/Glpi/Api/HL/Controller/GraphQLController.php#L96) |

## ITILController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Assistance/ExternalEvent` | 2.0 / — / — | 1 / api | [searchExternalEvent](../src/Glpi/Api/HL/Controller/ITILController.php#L2695) |
| POST | `/Assistance/ExternalEvent` | 2.0 / — / — | 1 / api | [createExternalEvent](../src/Glpi/Api/HL/Controller/ITILController.php#L2713) |
| DELETE | `/Assistance/ExternalEvent/{id}` | 2.0 / — / — | 1 / api | [deleteExternalEvent](../src/Glpi/Api/HL/Controller/ITILController.php#L2733) |
| GET | `/Assistance/ExternalEvent/{id}` | 2.0 / — / — | 1 / api | [getExternalEvent](../src/Glpi/Api/HL/Controller/ITILController.php#L2705) |
| PATCH | `/Assistance/ExternalEvent/{id}` | 2.0 / — / — | 1 / api | [updateExternalEvent](../src/Glpi/Api/HL/Controller/ITILController.php#L2723) |
| GET | `/Assistance/PendingReason` | 2.3 / — / — | 1 / api | [searchPendingReason](../src/Glpi/Api/HL/Controller/ITILController.php#L2930) |
| POST | `/Assistance/PendingReason` | 2.3 / — / — | 1 / api | [createPendingReason](../src/Glpi/Api/HL/Controller/ITILController.php#L2948) |
| DELETE | `/Assistance/PendingReason/{id}` | 2.3 / — / — | 1 / api | [deletePendingReason](../src/Glpi/Api/HL/Controller/ITILController.php#L2968) |
| GET | `/Assistance/PendingReason/{id}` | 2.3 / — / — | 1 / api | [getPendingReason](../src/Glpi/Api/HL/Controller/ITILController.php#L2940) |
| PATCH | `/Assistance/PendingReason/{id}` | 2.3 / — / — | 1 / api | [updatePendingReason](../src/Glpi/Api/HL/Controller/ITILController.php#L2958) |
| GET | `/Assistance/PlanningReminder` | 2.3 / — / — | 1 / api | [searchPlanningReminder](../src/Glpi/Api/HL/Controller/ITILController.php#L2912) |
| GET | `/Assistance/PlanningReminder/{id}` | 2.3 / — / — | 1 / api | [getPlanningReminder](../src/Glpi/Api/HL/Controller/ITILController.php#L2922) |
| GET | `/Assistance/RecurringChange` | 2.0 / — / — | 1 / api | [searchRecurringChanges](../src/Glpi/Api/HL/Controller/ITILController.php#L2655) |
| POST | `/Assistance/RecurringChange` | 2.0 / — / — | 1 / api | [createRecurringChange](../src/Glpi/Api/HL/Controller/ITILController.php#L2671) |
| DELETE | `/Assistance/RecurringChange/{id}` | 2.0 / — / — | 1 / api | [deleteRecurringChange](../src/Glpi/Api/HL/Controller/ITILController.php#L2687) |
| GET | `/Assistance/RecurringChange/{id}` | 2.0 / — / — | 1 / api | [getRecurringChange](../src/Glpi/Api/HL/Controller/ITILController.php#L2663) |
| PATCH | `/Assistance/RecurringChange/{id}` | 2.0 / — / — | 1 / api | [updateRecurringChange](../src/Glpi/Api/HL/Controller/ITILController.php#L2679) |
| GET | `/Assistance/RecurringTicket` | 2.0 / — / — | 1 / api | [searchRecurringTickets](../src/Glpi/Api/HL/Controller/ITILController.php#L2615) |
| POST | `/Assistance/RecurringTicket` | 2.0 / — / — | 1 / api | [createRecurringTicket](../src/Glpi/Api/HL/Controller/ITILController.php#L2631) |
| DELETE | `/Assistance/RecurringTicket/{id}` | 2.0 / — / — | 1 / api | [deleteRecurringTicket](../src/Glpi/Api/HL/Controller/ITILController.php#L2647) |
| GET | `/Assistance/RecurringTicket/{id}` | 2.0 / — / — | 1 / api | [getRecurringTicket](../src/Glpi/Api/HL/Controller/ITILController.php#L2623) |
| PATCH | `/Assistance/RecurringTicket/{id}` | 2.0 / — / — | 1 / api | [updateRecurringTicket](../src/Glpi/Api/HL/Controller/ITILController.php#L2639) |
| GET | `/Assistance/{assistance_itemtype}/{assistance_id}/KBArticle` | 2.3 / — / — | 1 / api | [searchKBArticleItemLinks](../src/Glpi/Api/HL/Controller/ITILController.php#L2857) |
| POST | `/Assistance/{assistance_itemtype}/{assistance_id}/KBArticle` | 2.3 / — / — | 1 / api | [createKBArticleItemLink](../src/Glpi/Api/HL/Controller/ITILController.php#L2831) |
| DELETE | `/Assistance/{assistance_itemtype}/{assistance_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [deleteKBArticleItemLink](../src/Glpi/Api/HL/Controller/ITILController.php#L2904) |
| GET | `/Assistance/{assistance_itemtype}/{assistance_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [getKBArticleItemLink](../src/Glpi/Api/HL/Controller/ITILController.php#L2873) |
| PATCH | `/Assistance/{assistance_itemtype}/{assistance_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [updateKBArticleItemLink](../src/Glpi/Api/HL/Controller/ITILController.php#L2889) |
| GET | `/Assistance/{itemtype}` | 2.0 / — / — | 1 / api | [search](../src/Glpi/Api/HL/Controller/ITILController.php#L1801) |
| POST | `/Assistance/{itemtype}` | 2.0 / — / — | 1 / api | [createItem](../src/Glpi/Api/HL/Controller/ITILController.php#L1825) |
| DELETE | `/Assistance/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [deleteItem](../src/Glpi/Api/HL/Controller/ITILController.php#L1849) |
| GET | `/Assistance/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [getItem](../src/Glpi/Api/HL/Controller/ITILController.php#L1813) |
| PATCH | `/Assistance/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [updateItem](../src/Glpi/Api/HL/Controller/ITILController.php#L1837) |
| GET | `/Assistance/{itemtype}/{id}/Cost` | 2.3 / — / — | 1 / api | [searchCosts](../src/Glpi/Api/HL/Controller/ITILController.php#L2743) |
| POST | `/Assistance/{itemtype}/{id}/Cost` | 2.3 / — / — | 1 / api | [createCost](../src/Glpi/Api/HL/Controller/ITILController.php#L2762) |
| DELETE | `/Assistance/{itemtype}/{id}/Cost/{cost_id}` | 2.3 / — / — | 1 / api | [deleteCost](../src/Glpi/Api/HL/Controller/ITILController.php#L2815) |
| GET | `/Assistance/{itemtype}/{id}/Cost/{cost_id}` | 2.3 / — / — | 1 / api | [getCost](../src/Glpi/Api/HL/Controller/ITILController.php#L2789) |
| PATCH | `/Assistance/{itemtype}/{id}/Cost/{cost_id}` | 2.3 / — / — | 1 / api | [updateCost](../src/Glpi/Api/HL/Controller/ITILController.php#L2802) |
| GET | `/Assistance/{itemtype}/{id}/PendingReason` | 2.3 / — / — | 1 / api | [getItemPendingReason](../src/Glpi/Api/HL/Controller/ITILController.php#L2979) |
| DELETE | `/Assistance/{itemtype}/{id}/TeamMember` | 2.0 / — / — | 1 / api | [removeTeamMember](../src/Glpi/Api/HL/Controller/ITILController.php#L2590) |
| GET | `/Assistance/{itemtype}/{id}/TeamMember` | 2.0 / — / — | 1 / api | [getTeamMembers](../src/Glpi/Api/HL/Controller/ITILController.php#L2456) |
| POST | `/Assistance/{itemtype}/{id}/TeamMember` | 2.0 / — / — | 1 / api | [addTeamMember](../src/Glpi/Api/HL/Controller/ITILController.php#L2537) |
| GET | `/Assistance/{itemtype}/{id}/TeamMember/{role}` | 2.0 / — / — | 1 / api | [getTeamMembersByRole](../src/Glpi/Api/HL/Controller/ITILController.php#L2490) |
| GET | `/Assistance/{itemtype}/{id}/Timeline` | 2.0 / — / — | 1 / api | [getTimeline](../src/Glpi/Api/HL/Controller/ITILController.php#L1981) |
| GET | `/Assistance/{itemtype}/{id}/Timeline/Task` | 2.0 / — / — | 1 / api | [getTimelineTasks](../src/Glpi/Api/HL/Controller/ITILController.php#L2022) |
| POST | `/Assistance/{itemtype}/{id}/Timeline/Task` | 2.0 / — / — | 1 / api | [createTimelineTask](../src/Glpi/Api/HL/Controller/ITILController.php#L2166) |
| DELETE | `/Assistance/{itemtype}/{id}/Timeline/Task/{subitem_id}` | 2.0 / — / — | 1 / api | [deleteTimelineTask](../src/Glpi/Api/HL/Controller/ITILController.php#L2310) |
| GET | `/Assistance/{itemtype}/{id}/Timeline/Task/{subitem_id}` | 2.0 / — / — | 1 / api | [getTimelineTask](../src/Glpi/Api/HL/Controller/ITILController.php#L2108) |
| PATCH | `/Assistance/{itemtype}/{id}/Timeline/Task/{subitem_id}` | 2.0 / — / — | 1 / api | [updateTimelineTask](../src/Glpi/Api/HL/Controller/ITILController.php#L2244) |
| GET | `/Assistance/{itemtype}/{id}/Timeline/Validation` | 2.0 / — / — | 1 / api | [getTimelineValidations](../src/Glpi/Api/HL/Controller/ITILController.php#L2045) |
| POST | `/Assistance/{itemtype}/{id}/Timeline/Validation` | 2.0 / — / — | 1 / api | [createTimelineValidation](../src/Glpi/Api/HL/Controller/ITILController.php#L2192) |
| DELETE | `/Assistance/{itemtype}/{id}/Timeline/Validation/{subitem_id}` | 2.0 / — / — | 1 / api | [deleteTimelineValidation](../src/Glpi/Api/HL/Controller/ITILController.php#L2327) |
| GET | `/Assistance/{itemtype}/{id}/Timeline/Validation/{subitem_id}` | 2.0 / — / — | 1 / api | [getTimelineValidation](../src/Glpi/Api/HL/Controller/ITILController.php#L2125) |
| PATCH | `/Assistance/{itemtype}/{id}/Timeline/Validation/{subitem_id}` | 2.0 / — / — | 1 / api | [updateTimelineValidation](../src/Glpi/Api/HL/Controller/ITILController.php#L2269) |
| GET | `/Assistance/{itemtype}/{id}/Timeline/{subitem_type}` | 2.0 / — / — | 1 / api | [getTimelineItems](../src/Glpi/Api/HL/Controller/ITILController.php#L2000) |
| POST | `/Assistance/{itemtype}/{id}/Timeline/{subitem_type}` | 2.0 / — / — | 1 / api | [createTimelineItem](../src/Glpi/Api/HL/Controller/ITILController.php#L2141) |
| DELETE | `/Assistance/{itemtype}/{id}/Timeline/{subitem_type}/{subitem_id}` | 2.0 / — / — | 1 / api | [deleteTimelineItem](../src/Glpi/Api/HL/Controller/ITILController.php#L2293) |
| GET | `/Assistance/{itemtype}/{id}/Timeline/{subitem_type}/{subitem_id}` | 2.0 / — / — | 1 / api | [getTimelineItem](../src/Glpi/Api/HL/Controller/ITILController.php#L2093) |
| PATCH | `/Assistance/{itemtype}/{id}/Timeline/{subitem_type}/{subitem_id}` | 2.0 / — / — | 1 / api | [updateTimelineItem](../src/Glpi/Api/HL/Controller/ITILController.php#L2219) |

## InventoryController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Inventory/Agent/{id}/InventoryFile` | 2.3 / — / — | 1 / api | [getLastInventoryFile](../src/Glpi/Api/HL/Controller/InventoryController.php#L383) |
| POST | `/Inventory/Agent/{id}/InventoryRequest` | 2.3 / — / — | 1 / api | [requestInventory](../src/Glpi/Api/HL/Controller/InventoryController.php#L323) |
| POST | `/Inventory/Agent/{id}/StatusRequest` | 2.3 / — / — | 1 / api | [requestStatus](../src/Glpi/Api/HL/Controller/InventoryController.php#L355) |
| GET | `/Inventory/{itemtype}` | 2.3 / — / — | 1 / api | [search](../src/Glpi/Api/HL/Controller/InventoryController.php#L236) |
| POST | `/Inventory/{itemtype}` | 2.3 / — / — | 1 / api | [createItem](../src/Glpi/Api/HL/Controller/InventoryController.php#L265) |
| DELETE | `/Inventory/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [deleteItem](../src/Glpi/Api/HL/Controller/InventoryController.php#L296) |
| GET | `/Inventory/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [getItem](../src/Glpi/Api/HL/Controller/InventoryController.php#L250) |
| PATCH | `/Inventory/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [updateItem](../src/Glpi/Api/HL/Controller/InventoryController.php#L281) |

## KnowbaseController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Knowledgebase/Article` | 2.2 / — / — | 1 / api | [searchKBArticles](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L578) |
| POST | `/Knowledgebase/Article` | 2.2 / — / — | 1 / api | [createKBArticle](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L565) |
| DELETE | `/Knowledgebase/Article/{article_id}` | 2.2 / — / — | 1 / api | [deleteKBArticle](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L604) |
| GET | `/Knowledgebase/Article/{article_id}` | 2.2 / — / — | 1 / api | [getKBArticle](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L586) |
| PATCH | `/Knowledgebase/Article/{article_id}` | 2.2 / — / — | 1 / api | [updateKBArticle](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L595) |
| GET | `/Knowledgebase/Article/{article_id}/Comment` | 2.2 / — / — | 1 / api | [searchKBArticleComments](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L639) |
| POST | `/Knowledgebase/Article/{article_id}/Comment` | 2.2 / — / — | 1 / api | [createKBArticleComment](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L613) |
| DELETE | `/Knowledgebase/Article/{article_id}/Comment/{id}` | 2.2 / — / — | 1 / api | [deleteKBArticleComment](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L665) |
| GET | `/Knowledgebase/Article/{article_id}/Comment/{id}` | 2.2 / — / — | 1 / api | [getKBArticleComment](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L648) |
| PATCH | `/Knowledgebase/Article/{article_id}/Comment/{id}` | 2.2 / — / — | 1 / api | [updateKBArticleComment](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L657) |
| GET | `/Knowledgebase/Article/{article_id}/Revision` | 2.2 / — / — | 1 / api | [searchKBArticleDefaultLangRevisions](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L673) |
| GET | `/Knowledgebase/Article/{article_id}/Revision/{revision}` | 2.2 / — / — | 1 / api | [getKBArticleDefaultLangRevision](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L682) |
| GET | `/Knowledgebase/Article/{article_id}/{language}/Revision` | 2.2 / — / — | 1 / api | [searchKBArticleRevisions](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L696) |
| GET | `/Knowledgebase/Article/{article_id}/{language}/Revision/{revision}` | 2.2 / — / — | 1 / api | [getKBArticleRevision](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L705) |
| GET | `/Knowledgebase/Category` | 2.2 / — / 3.0.0 | 1 / api | [searchKBCategory](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L731) |
| POST | `/Knowledgebase/Category` | 2.2 / — / 3.0.0 | 1 / api | [createKBCategory](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L719) |
| DELETE | `/Knowledgebase/Category/{id}` | 2.2 / — / 3.0.0 | 1 / api | [deleteKBCategory](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L755) |
| GET | `/Knowledgebase/Category/{id}` | 2.2 / — / 3.0.0 | 1 / api | [getKBCategory](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L739) |
| PATCH | `/Knowledgebase/Category/{id}` | 2.2 / — / 3.0.0 | 1 / api | [updateKBCategory](../src/Glpi/Api/HL/Controller/KnowbaseController.php#L747) |

## ManagementController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Management/` | 2.0 / — / — | 1 / api | [index](../src/Glpi/Api/HL/Controller/ManagementController.php#L1188) |
| GET | `/Management/Budget/{items_id}/KBArticle` | 2.3 / — / — | 1 / api | [searchKBArticleItemLinks](../src/Glpi/Api/HL/Controller/ManagementController.php#L1727) |
| POST | `/Management/Budget/{items_id}/KBArticle` | 2.3 / — / — | 1 / api | [createKBArticleItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1703) |
| DELETE | `/Management/Budget/{items_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [deleteKBArticleItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1770) |
| GET | `/Management/Budget/{items_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [getKBArticleItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1742) |
| PATCH | `/Management/Budget/{items_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [updateKBArticleItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1757) |
| GET | `/Management/Contract/{id}/Cost` | 2.3 / — / — | 1 / api | [searchCosts](../src/Glpi/Api/HL/Controller/ManagementController.php#L1388) |
| POST | `/Management/Contract/{id}/Cost` | 2.3 / — / — | 1 / api | [createCost](../src/Glpi/Api/HL/Controller/ManagementController.php#L1398) |
| DELETE | `/Management/Contract/{id}/Cost/{cost_id}` | 2.3 / — / — | 1 / api | [deleteCost](../src/Glpi/Api/HL/Controller/ManagementController.php#L1438) |
| GET | `/Management/Contract/{id}/Cost/{cost_id}` | 2.3 / — / — | 1 / api | [getCost](../src/Glpi/Api/HL/Controller/ManagementController.php#L1416) |
| PATCH | `/Management/Contract/{id}/Cost/{cost_id}` | 2.3 / — / — | 1 / api | [updateCost](../src/Glpi/Api/HL/Controller/ManagementController.php#L1427) |
| GET | `/Management/Document/{id}/Download` | 2.0 / — / — | 1 / api | [downloadDocument](../src/Glpi/Api/HL/Controller/ManagementController.php#L1219) |
| GET | `/Management/{itemtype}` | 2.0 / — / — | 1 / api | [searchItems20](../src/Glpi/Api/HL/Controller/ManagementController.php#L1239) |
| GET | `/Management/{itemtype}` | 2.2 / — / — | 1 / api | [searchItems22](../src/Glpi/Api/HL/Controller/ManagementController.php#L1316) |
| GET | `/Management/{itemtype}` | 2.3 / — / — | 1 / api | [searchItems23](../src/Glpi/Api/HL/Controller/ManagementController.php#L1452) |
| POST | `/Management/{itemtype}` | 2.0 / — / — | 1 / api | [createItem20](../src/Glpi/Api/HL/Controller/ManagementController.php#L1268) |
| POST | `/Management/{itemtype}` | 2.2 / — / — | 1 / api | [createItem22](../src/Glpi/Api/HL/Controller/ManagementController.php#L1345) |
| POST | `/Management/{itemtype}` | 2.3 / — / — | 1 / api | [createItem23](../src/Glpi/Api/HL/Controller/ManagementController.php#L1481) |
| DELETE | `/Management/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [deleteItem20](../src/Glpi/Api/HL/Controller/ManagementController.php#L1302) |
| DELETE | `/Management/{itemtype}/{id}` | 2.2 / — / — | 1 / api | [deleteItem22](../src/Glpi/Api/HL/Controller/ManagementController.php#L1379) |
| DELETE | `/Management/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [deleteItem23](../src/Glpi/Api/HL/Controller/ManagementController.php#L1515) |
| GET | `/Management/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [getItem20](../src/Glpi/Api/HL/Controller/ManagementController.php#L1254) |
| GET | `/Management/{itemtype}/{id}` | 2.2 / — / — | 1 / api | [getItem22](../src/Glpi/Api/HL/Controller/ManagementController.php#L1331) |
| GET | `/Management/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [getItem23](../src/Glpi/Api/HL/Controller/ManagementController.php#L1467) |
| PATCH | `/Management/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [updateItem20](../src/Glpi/Api/HL/Controller/ManagementController.php#L1287) |
| PATCH | `/Management/{itemtype}/{id}` | 2.2 / — / — | 1 / api | [updateItem22](../src/Glpi/Api/HL/Controller/ManagementController.php#L1364) |
| PATCH | `/Management/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [updateItem23](../src/Glpi/Api/HL/Controller/ManagementController.php#L1500) |
| DELETE | `/Management/{itemtype}/{id}/Infocom` | 3.0 / — / — | 1 / api | [deleteItemInfocom](../src/Glpi/Api/HL/Controller/ManagementController.php#L1955) |
| GET | `/Management/{itemtype}/{id}/Infocom` | 3.0 / — / — | 1 / api | [getItemInfocom](../src/Glpi/Api/HL/Controller/ManagementController.php#L1868) |
| PATCH | `/Management/{itemtype}/{id}/Infocom` | 3.0 / — / — | 1 / api | [updateItemInfocom](../src/Glpi/Api/HL/Controller/ManagementController.php#L1923) |
| POST | `/Management/{itemtype}/{id}/Infocom` | 3.0 / — / — | 1 / api | [createItemInfocom](../src/Glpi/Api/HL/Controller/ManagementController.php#L1896) |
| GET | `/Management/{itemtype}/{items_id}/Certificate` | 2.3 / — / — | 1 / api | [searchCertificateItemLinks](../src/Glpi/Api/HL/Controller/ManagementController.php#L1643) |
| POST | `/Management/{itemtype}/{items_id}/Certificate` | 2.3 / — / — | 1 / api | [createCertificateItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1617) |
| DELETE | `/Management/{itemtype}/{items_id}/Certificate/{id}` | 2.3 / — / — | 1 / api | [deleteCertificateItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1690) |
| GET | `/Management/{itemtype}/{items_id}/Certificate/{id}` | 2.3 / — / — | 1 / api | [getCertificateItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1659) |
| PATCH | `/Management/{itemtype}/{items_id}/Certificate/{id}` | 2.3 / — / — | 1 / api | [updateCertificateItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1675) |
| GET | `/Management/{itemtype}/{items_id}/Contract` | 2.3 / — / — | 1 / api | [searchContractItemLinks](../src/Glpi/Api/HL/Controller/ManagementController.php#L1810) |
| POST | `/Management/{itemtype}/{items_id}/Contract` | 2.3 / — / — | 1 / api | [createContractItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1784) |
| DELETE | `/Management/{itemtype}/{items_id}/Contract/{id}` | 2.3 / — / — | 1 / api | [deleteContractItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1857) |
| GET | `/Management/{itemtype}/{items_id}/Contract/{id}` | 2.3 / — / — | 1 / api | [getContractItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1826) |
| PATCH | `/Management/{itemtype}/{items_id}/Contract/{id}` | 2.3 / — / — | 1 / api | [updateContractItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1842) |
| GET | `/Management/{itemtype}/{items_id}/Domain` | 2.3 / — / — | 1 / api | [searchDomainItemLinks](../src/Glpi/Api/HL/Controller/ManagementController.php#L1556) |
| POST | `/Management/{itemtype}/{items_id}/Domain` | 2.3 / — / — | 1 / api | [createDomainItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1530) |
| DELETE | `/Management/{itemtype}/{items_id}/Domain/{id}` | 2.3 / — / — | 1 / api | [deleteDomainItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1603) |
| GET | `/Management/{itemtype}/{items_id}/Domain/{id}` | 2.3 / — / — | 1 / api | [getDomainItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1572) |
| PATCH | `/Management/{itemtype}/{items_id}/Domain/{id}` | 2.3 / — / — | 1 / api | [updateDomainItemLink](../src/Glpi/Api/HL/Controller/ManagementController.php#L1588) |

## NotepadController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/{itemtype}/{items_id}/Note` | 2.2 / — / — | 1 / api | [searchNote](../src/Glpi/Api/HL/Controller/NotepadController.php#L151) |
| POST | `/{itemtype}/{items_id}/Note` | 2.2 / — / — | 1 / api | [createNote](../src/Glpi/Api/HL/Controller/NotepadController.php#L128) |
| DELETE | `/{itemtype}/{items_id}/Note/{id}` | 2.2 / — / — | 1 / api | [deleteNote](../src/Glpi/Api/HL/Controller/NotepadController.php#L197) |
| GET | `/{itemtype}/{items_id}/Note/{id}` | 2.2 / — / — | 1 / api | [getNote](../src/Glpi/Api/HL/Controller/NotepadController.php#L164) |
| PATCH | `/{itemtype}/{items_id}/Note/{id}` | 2.2 / — / — | 1 / api | [updateNote](../src/Glpi/Api/HL/Controller/NotepadController.php#L181) |

## NotificationController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Notifications/Notification` | 2.3 / — / — | 1 / api | [searchNotifications](../src/Glpi/Api/HL/Controller/NotificationController.php#L442) |
| POST | `/Notifications/Notification` | 2.3 / — / — | 1 / api | [createNotification](../src/Glpi/Api/HL/Controller/NotificationController.php#L462) |
| DELETE | `/Notifications/Notification/{id}` | 2.3 / — / — | 1 / api | [deleteNotification](../src/Glpi/Api/HL/Controller/NotificationController.php#L486) |
| GET | `/Notifications/Notification/{id}` | 2.3 / — / — | 1 / api | [getNotification](../src/Glpi/Api/HL/Controller/NotificationController.php#L450) |
| PATCH | `/Notifications/Notification/{id}` | 2.3 / — / — | 1 / api | [updateNotification](../src/Glpi/Api/HL/Controller/NotificationController.php#L474) |
| DELETE | `/Notifications/Notification/{notification_id}/NotificationTemplate` | 2.3 / — / — | 1 / api | [deleteNotification_NotificationTemplate](../src/Glpi/Api/HL/Controller/NotificationController.php#L715) |
| GET | `/Notifications/Notification/{notification_id}/NotificationTemplate` | 2.3 / — / — | 1 / api | [searchNotification_NotificationTemplates](../src/Glpi/Api/HL/Controller/NotificationController.php#L693) |
| GET | `/Notifications/Notification/{notification_id}/NotificationTemplate/{id}` | 2.3 / — / — | 1 / api | [getNotification_NotificationTemplate](../src/Glpi/Api/HL/Controller/NotificationController.php#L702) |
| GET | `/Notifications/Notification/{notification_id}/Recipient` | 2.3 / — / — | 1 / api | [searchNotificationRecipients](../src/Glpi/Api/HL/Controller/NotificationController.php#L498) |
| POST | `/Notifications/Notification/{notification_id}/Recipient` | 2.3 / — / — | 1 / api | [createNotificationRecipient](../src/Glpi/Api/HL/Controller/NotificationController.php#L520) |
| DELETE | `/Notifications/Notification/{notification_id}/Recipient/{id}` | 2.3 / — / — | 1 / api | [deleteNotificationRecipient](../src/Glpi/Api/HL/Controller/NotificationController.php#L533) |
| GET | `/Notifications/Notification/{notification_id}/Recipient/{id}` | 2.3 / — / — | 1 / api | [getNotificationRecipient](../src/Glpi/Api/HL/Controller/NotificationController.php#L507) |
| GET | `/Notifications/NotificationTemplate` | 2.3 / — / — | 1 / api | [searchNotificationTemplates](../src/Glpi/Api/HL/Controller/NotificationController.php#L545) |
| POST | `/Notifications/NotificationTemplate` | 2.3 / — / — | 1 / api | [createNotificationTemplate](../src/Glpi/Api/HL/Controller/NotificationController.php#L565) |
| DELETE | `/Notifications/NotificationTemplate/{id}` | 2.3 / — / — | 1 / api | [deleteNotificationTemplate](../src/Glpi/Api/HL/Controller/NotificationController.php#L589) |
| GET | `/Notifications/NotificationTemplate/{id}` | 2.3 / — / — | 1 / api | [getNotificationTemplate](../src/Glpi/Api/HL/Controller/NotificationController.php#L553) |
| PATCH | `/Notifications/NotificationTemplate/{id}` | 2.3 / — / — | 1 / api | [updateNotificationTemplate](../src/Glpi/Api/HL/Controller/NotificationController.php#L577) |
| GET | `/Notifications/NotificationTemplate/{template_id}/Translation` | 2.3 / — / — | 1 / api | [searchNotificationTemplateTranslations](../src/Glpi/Api/HL/Controller/NotificationController.php#L601) |
| POST | `/Notifications/NotificationTemplate/{template_id}/Translation` | 2.3 / — / — | 1 / api | [createNotificationTemplateTranslation](../src/Glpi/Api/HL/Controller/NotificationController.php#L654) |
| GET | `/Notifications/NotificationTemplate/{template_id}/Translation/Default` | 2.3 / — / — | 1 / api | [getNotificationTemplateTranslationDefaultLanguage](../src/Glpi/Api/HL/Controller/NotificationController.php#L639) |
| DELETE | `/Notifications/NotificationTemplate/{template_id}/Translation/{id}` | 2.3 / — / — | 1 / api | [deleteNotificationTemplateTranslation](../src/Glpi/Api/HL/Controller/NotificationController.php#L681) |
| GET | `/Notifications/NotificationTemplate/{template_id}/Translation/{id}` | 2.3 / — / — | 1 / api | [getNotificationTemplateTranslation](../src/Glpi/Api/HL/Controller/NotificationController.php#L610) |
| PATCH | `/Notifications/NotificationTemplate/{template_id}/Translation/{id}` | 2.3 / — / — | 1 / api | [updateNotificationTemplateTranslation](../src/Glpi/Api/HL/Controller/NotificationController.php#L667) |
| GET | `/Notifications/NotificationTemplate/{template_id}/Translation/{language}` | 2.3 / — / — | 1 / api | [getNotificationTemplateTranslationByLanguage](../src/Glpi/Api/HL/Controller/NotificationController.php#L625) |
| GET | `/Notifications/QueuedNotification` | 2.3 / — / — | 1 / api | [searchQueuedNotifications](../src/Glpi/Api/HL/Controller/NotificationController.php#L406) |
| GET | `/Notifications/QueuedNotification/{id}` | 2.3 / — / — | 1 / api | [getQueuedNotification](../src/Glpi/Api/HL/Controller/NotificationController.php#L414) |
| POST | `/Notifications/QueuedNotification/{id}/SendRequest` | 2.3 / — / — | 1 / api | [requestQueuedNotificationSend](../src/Glpi/Api/HL/Controller/NotificationController.php#L426) |

## ProjectController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Project/` | 2.0 / — / — | 1 / api | [searchProjects](../src/Glpi/Api/HL/Controller/ProjectController.php#L610) |
| POST | `/Project/` | 2.0 / — / — | 1 / api | [createProject](../src/Glpi/Api/HL/Controller/ProjectController.php#L626) |
| GET | `/Project/Project/{id}/Cost` | 2.3 / — / — | 1 / api | [searchCosts](../src/Glpi/Api/HL/Controller/ProjectController.php#L731) |
| POST | `/Project/Project/{id}/Cost` | 2.3 / — / — | 1 / api | [createCost](../src/Glpi/Api/HL/Controller/ProjectController.php#L741) |
| DELETE | `/Project/Project/{id}/Cost/{cost_id}` | 2.3 / — / — | 1 / api | [deleteCost](../src/Glpi/Api/HL/Controller/ProjectController.php#L781) |
| GET | `/Project/Project/{id}/Cost/{cost_id}` | 2.3 / — / — | 1 / api | [getCost](../src/Glpi/Api/HL/Controller/ProjectController.php#L759) |
| PATCH | `/Project/Project/{id}/Cost/{cost_id}` | 2.3 / — / — | 1 / api | [updateCost](../src/Glpi/Api/HL/Controller/ProjectController.php#L770) |
| GET | `/Project/Project/{items_id}/Contract` | 2.3 / — / — | 1 / api | [searchContractItemLinks](../src/Glpi/Api/HL/Controller/ProjectController.php#L899) |
| POST | `/Project/Project/{items_id}/Contract` | 2.3 / — / — | 1 / api | [createContractItemLink](../src/Glpi/Api/HL/Controller/ProjectController.php#L875) |
| DELETE | `/Project/Project/{items_id}/Contract/{id}` | 2.3 / — / — | 1 / api | [deleteContractItemLink](../src/Glpi/Api/HL/Controller/ProjectController.php#L943) |
| GET | `/Project/Project/{items_id}/Contract/{id}` | 2.3 / — / — | 1 / api | [getContractItemLink](../src/Glpi/Api/HL/Controller/ProjectController.php#L914) |
| PATCH | `/Project/Project/{items_id}/Contract/{id}` | 2.3 / — / — | 1 / api | [updateContractItemLink](../src/Glpi/Api/HL/Controller/ProjectController.php#L929) |
| GET | `/Project/Project/{items_id}/KBArticle` | 2.3 / — / — | 1 / api | [searchKBArticleItemLinks](../src/Glpi/Api/HL/Controller/ProjectController.php#L819) |
| POST | `/Project/Project/{items_id}/KBArticle` | 2.3 / — / — | 1 / api | [createKBArticleItemLink](../src/Glpi/Api/HL/Controller/ProjectController.php#L795) |
| DELETE | `/Project/Project/{items_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [deleteKBArticleItemLink](../src/Glpi/Api/HL/Controller/ProjectController.php#L862) |
| GET | `/Project/Project/{items_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [getKBArticleItemLink](../src/Glpi/Api/HL/Controller/ProjectController.php#L834) |
| PATCH | `/Project/Project/{items_id}/KBArticle/{id}` | 2.3 / — / — | 1 / api | [updateKBArticleItemLink](../src/Glpi/Api/HL/Controller/ProjectController.php#L849) |
| GET | `/Project/Task` | 2.0 / — / — | 1 / api | [searchTasks](../src/Glpi/Api/HL/Controller/ProjectController.php#L653) |
| POST | `/Project/Task` | 2.0 / — / — | 1 / api | [createTask](../src/Glpi/Api/HL/Controller/ProjectController.php#L675) |
| DELETE | `/Project/Task/{id}` | 2.0 / — / — | 1 / api | [deleteTask](../src/Glpi/Api/HL/Controller/ProjectController.php#L697) |
| GET | `/Project/Task/{id}` | 2.0 / — / — | 1 / api | [getTask](../src/Glpi/Api/HL/Controller/ProjectController.php#L664) |
| PATCH | `/Project/Task/{id}` | 2.0 / — / — | 1 / api | [updateTask](../src/Glpi/Api/HL/Controller/ProjectController.php#L686) |
| GET | `/Project/Task/{task_id}/TeamMember` | 2.3 / — / — | 1 / api | [getProjectTaskTeamMembers](../src/Glpi/Api/HL/Controller/ProjectController.php#L1172) |
| POST | `/Project/Task/{task_id}/TeamMember` | 2.3 / — / — | 1 / api | [addProjectTaskTeamMember](../src/Glpi/Api/HL/Controller/ProjectController.php#L1205) |
| DELETE | `/Project/Task/{task_id}/TeamMember/{teammember_id}` | 2.3 / — / — | 1 / api | [deleteProjectTaskTeamMember](../src/Glpi/Api/HL/Controller/ProjectController.php#L1190) |
| DELETE | `/Project/{id}` | 2.0 / — / — | 1 / api | [deleteProject](../src/Glpi/Api/HL/Controller/ProjectController.php#L642) |
| GET | `/Project/{id}` | 2.0 / — / — | 1 / api | [getProject](../src/Glpi/Api/HL/Controller/ProjectController.php#L618) |
| PATCH | `/Project/{id}` | 2.0 / — / — | 1 / api | [updateProject](../src/Glpi/Api/HL/Controller/ProjectController.php#L634) |
| GET | `/Project/{project_id}/Change` | 2.3 / — / — | 1 / api | [getLinkedChanges](../src/Glpi/Api/HL/Controller/ProjectController.php#L1012) |
| POST | `/Project/{project_id}/Change` | 2.3 / — / — | 1 / api | [addLinkedChange](../src/Glpi/Api/HL/Controller/ProjectController.php#L1024) |
| DELETE | `/Project/{project_id}/Change/{change_id}` | 2.3 / — / — | 1 / api | [deleteLinkedChange](../src/Glpi/Api/HL/Controller/ProjectController.php#L1038) |
| GET | `/Project/{project_id}/Problem` | 2.3 / — / — | 1 / api | [getLinkedProblems](../src/Glpi/Api/HL/Controller/ProjectController.php#L1070) |
| POST | `/Project/{project_id}/Problem` | 2.3 / — / — | 1 / api | [addLinkedProblem](../src/Glpi/Api/HL/Controller/ProjectController.php#L1082) |
| DELETE | `/Project/{project_id}/Problem/{problem_id}` | 2.3 / — / — | 1 / api | [deleteLinkedProblem](../src/Glpi/Api/HL/Controller/ProjectController.php#L1096) |
| GET | `/Project/{project_id}/Task` | 2.0 / — / — | 1 / api | [searchLinkedTasks](../src/Glpi/Api/HL/Controller/ProjectController.php#L708) |
| POST | `/Project/{project_id}/Task` | 2.0 / — / — | 1 / api | [createLinkedTask](../src/Glpi/Api/HL/Controller/ProjectController.php#L721) |
| GET | `/Project/{project_id}/TeamMember` | 2.3 / — / — | 1 / api | [getProjectTeamMembers](../src/Glpi/Api/HL/Controller/ProjectController.php#L1128) |
| POST | `/Project/{project_id}/TeamMember` | 2.3 / — / — | 1 / api | [addProjectTeamMember](../src/Glpi/Api/HL/Controller/ProjectController.php#L1155) |
| DELETE | `/Project/{project_id}/TeamMember/{teammember_id}` | 2.3 / — / — | 1 / api | [deleteProjectTeamMember](../src/Glpi/Api/HL/Controller/ProjectController.php#L1140) |
| GET | `/Project/{project_id}/Ticket` | 2.3 / — / — | 1 / api | [getLinkedTickets](../src/Glpi/Api/HL/Controller/ProjectController.php#L954) |
| POST | `/Project/{project_id}/Ticket` | 2.3 / — / — | 1 / api | [addLinkedTicket](../src/Glpi/Api/HL/Controller/ProjectController.php#L966) |
| DELETE | `/Project/{project_id}/Ticket/{ticket_id}` | 2.3 / — / — | 1 / api | [deleteLinkedTicket](../src/Glpi/Api/HL/Controller/ProjectController.php#L980) |

## ReportController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Assistance/Stat` | 2.0 / — / — | 1 / api | [listStatisticReports](../src/Glpi/Api/HL/Controller/ReportController.php#L345) |
| GET | `/Assistance/Stat/{assistance_type}/Asset` | 2.0 / — / — | 1 / api | [getAssetStats](../src/Glpi/Api/HL/Controller/ReportController.php#L683) |
| GET | `/Assistance/Stat/{assistance_type}/Asset/Export` | 2.0 / — / — | 1 / api | [exportAssetStats](../src/Glpi/Api/HL/Controller/ReportController.php#L752) |
| GET | `/Assistance/Stat/{assistance_type}/AssetCharacteristics` | 2.0 / — / — | 1 / api | [getAssetCharacteristicsStats](../src/Glpi/Api/HL/Controller/ReportController.php#L831) |
| GET | `/Assistance/Stat/{assistance_type}/AssetCharacteristics/Export` | 2.0 / — / — | 1 / api | [exportAssetCharacteristicsStats](../src/Glpi/Api/HL/Controller/ReportController.php#L962) |
| GET | `/Assistance/Stat/{assistance_type}/Characteristics` | 2.0 / — / — | 1 / api | [getITILStats](../src/Glpi/Api/HL/Controller/ReportController.php#L490) |
| GET | `/Assistance/Stat/{assistance_type}/Characteristics/Export` | 2.0 / — / — | 1 / api | [exportITILStats](../src/Glpi/Api/HL/Controller/ReportController.php#L610) |
| GET | `/Assistance/Stat/{assistance_type}/Global` | 2.0 / — / — | 1 / api | [getITILGlobalStats](../src/Glpi/Api/HL/Controller/ReportController.php#L426) |

## RuleController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Rule/Collection` | 2.0 / — / — | 1 / api | [getCollections](../src/Glpi/Api/HL/Controller/RuleController.php#L360) |
| GET | `/Rule/Collection/{collection}/ActionField` | 2.0 / — / — | 1 / api | [getRuleActionField](../src/Glpi/Api/HL/Controller/RuleController.php#L487) |
| GET | `/Rule/Collection/{collection}/ActionType` | 2.0 / — / — | 1 / api | [getRuleActionType](../src/Glpi/Api/HL/Controller/RuleController.php#L454) |
| GET | `/Rule/Collection/{collection}/CriteriaCondition` | 2.0 / — / — | 1 / api | [getRuleCriteriaConditions](../src/Glpi/Api/HL/Controller/RuleController.php#L396) |
| GET | `/Rule/Collection/{collection}/CriteriaCriteria` | 2.0 / — / — | 1 / api | [getRuleCriteriaCriteria](../src/Glpi/Api/HL/Controller/RuleController.php#L429) |
| GET | `/Rule/Collection/{collection}/Rule` | 2.0 / — / — | 1 / api | [getRules](../src/Glpi/Api/HL/Controller/RuleController.php#L511) |
| POST | `/Rule/Collection/{collection}/Rule` | 2.0 / — / — | 1 / api | [createRule](../src/Glpi/Api/HL/Controller/RuleController.php#L615) |
| DELETE | `/Rule/Collection/{collection}/Rule/{id}` | 2.0 / — / — | 1 / api | [deleteRule](../src/Glpi/Api/HL/Controller/RuleController.php#L655) |
| GET | `/Rule/Collection/{collection}/Rule/{id}` | 2.0 / — / — | 1 / api | [getRule](../src/Glpi/Api/HL/Controller/RuleController.php#L527) |
| PATCH | `/Rule/Collection/{collection}/Rule/{id}` | 2.0 / — / — | 1 / api | [updateRule](../src/Glpi/Api/HL/Controller/RuleController.php#L637) |
| GET | `/Rule/Collection/{collection}/Rule/{id}/Action` | 2.0 / — / — | 1 / api | [getRuleActions](../src/Glpi/Api/HL/Controller/RuleController.php#L581) |
| GET | `/Rule/Collection/{collection}/Rule/{id}/Criteria` | 2.0 / — / — | 1 / api | [getRuleCriteria](../src/Glpi/Api/HL/Controller/RuleController.php#L545) |
| POST | `/Rule/Collection/{collection}/Rule/{rule_id}/Action` | 2.0 / — / — | 1 / api | [createRuleAction](../src/Glpi/Api/HL/Controller/RuleController.php#L733) |
| DELETE | `/Rule/Collection/{collection}/Rule/{rule_id}/Action/{id}` | 2.0 / — / — | 1 / api | [deleteRuleAction](../src/Glpi/Api/HL/Controller/RuleController.php#L779) |
| GET | `/Rule/Collection/{collection}/Rule/{rule_id}/Action/{id}` | 2.0 / — / — | 1 / api | [getRuleAction](../src/Glpi/Api/HL/Controller/RuleController.php#L598) |
| PATCH | `/Rule/Collection/{collection}/Rule/{rule_id}/Action/{id}` | 2.0 / — / — | 1 / api | [updateRuleAction](../src/Glpi/Api/HL/Controller/RuleController.php#L756) |
| POST | `/Rule/Collection/{collection}/Rule/{rule_id}/Criteria` | 2.0 / — / — | 1 / api | [createRuleCriteria](../src/Glpi/Api/HL/Controller/RuleController.php#L669) |
| DELETE | `/Rule/Collection/{collection}/Rule/{rule_id}/Criteria/{id}` | 2.0 / — / — | 1 / api | [deleteRuleCriteria](../src/Glpi/Api/HL/Controller/RuleController.php#L715) |
| GET | `/Rule/Collection/{collection}/Rule/{rule_id}/Criteria/{id}` | 2.0 / — / — | 1 / api | [getRuleCriterion](../src/Glpi/Api/HL/Controller/RuleController.php#L562) |
| PATCH | `/Rule/Collection/{collection}/Rule/{rule_id}/Criteria/{id}` | 2.0 / — / — | 1 / api | [updateRuleCriteria](../src/Glpi/Api/HL/Controller/RuleController.php#L692) |

## SecurityController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Security/LoginSession/All` | 3.0 / — / — | 1 / api | [getAllLoginSessions](../src/Glpi/Api/HL/Controller/SecurityController.php#L331) |
| GET | `/Security/LoginSession/My` | 3.0 / — / — | 1 / api | [getMyLoginSessions](../src/Glpi/Api/HL/Controller/SecurityController.php#L309) |
| DELETE | `/Security/LoginSession/{login_session_uid}` | 3.0 / — / — | 1 / api | [revokeSession](../src/Glpi/Api/HL/Controller/SecurityController.php#L339) |
| GET | `/Security/LoginSession/{users_id}` | 3.0 / — / — | 1 / api | [getUserLoginSessions](../src/Glpi/Api/HL/Controller/SecurityController.php#L320) |

## SetupController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Setup/` | 2.0 / — / — | 1 / api | [index](../src/Glpi/Api/HL/Controller/SetupController.php#L1094) |
| GET | `/Setup/AutomaticAction/{id}` | 2.3 / — / — | 1 / api | [getAutomaticAction](../src/Glpi/Api/HL/Controller/SetupController.php#L1339) |
| PATCH | `/Setup/AutomaticAction/{id}` | 2.3 / — / — | 1 / api | [updateAutomaticAction](../src/Glpi/Api/HL/Controller/SetupController.php#L1350) |
| GET | `/Setup/AutomaticAction/{id}/Log` | 2.3 / — / — | 1 / api | [searchAutomaticActionLogs](../src/Glpi/Api/HL/Controller/SetupController.php#L1358) |
| GET | `/Setup/Config` | 2.1 / — / — | 1 / api | [searchConfigValues](../src/Glpi/Api/HL/Controller/SetupController.php#L1273) |
| GET | `/Setup/Config/{context}` | 2.1 / — / — | 1 / api | [searchConfigValuesByContext](../src/Glpi/Api/HL/Controller/SetupController.php#L1283) |
| DELETE | `/Setup/Config/{context}/{name}` | 2.1 / — / — | 1 / api | [deleteConfigValue](../src/Glpi/Api/HL/Controller/SetupController.php#L1320) |
| GET | `/Setup/Config/{context}/{name}` | 2.1 / — / — | 1 / api | [getConfigValue](../src/Glpi/Api/HL/Controller/SetupController.php#L1295) |
| PATCH | `/Setup/Config/{context}/{name}` | 2.1 / — / — | 1 / api | [setConfigValue](../src/Glpi/Api/HL/Controller/SetupController.php#L1248) |
| GET | `/Setup/NotImportedEmail` | 2.3 / — / — | 1 / api | [searchNotImportedEmails](../src/Glpi/Api/HL/Controller/SetupController.php#L1471) |
| DELETE | `/Setup/NotImportedEmail/{id}` | 2.3 / — / — | 1 / api | [deleteNotImportedEmail](../src/Glpi/Api/HL/Controller/SetupController.php#L1498) |
| GET | `/Setup/NotImportedEmail/{id}` | 2.3 / — / — | 1 / api | [getNotImportedEmail](../src/Glpi/Api/HL/Controller/SetupController.php#L1484) |
| GET | `/Setup/Plugin` | 2.3.0 / — / — | 1 / api | [listPlugins](../src/Glpi/Api/HL/Controller/SetupController.php#L1368) |
| POST | `/Setup/Plugin/{id}/Clean` | 2.3.0 / — / — | 1 / api | [cleanPlugin](../src/Glpi/Api/HL/Controller/SetupController.php#L1452) |
| POST | `/Setup/Plugin/{id}/Disable` | 2.3.0 / — / — | 1 / api | [disablePlugin](../src/Glpi/Api/HL/Controller/SetupController.php#L1396) |
| POST | `/Setup/Plugin/{id}/Enable` | 2.3.0 / — / — | 1 / api | [enablePlugin](../src/Glpi/Api/HL/Controller/SetupController.php#L1378) |
| POST | `/Setup/Plugin/{id}/Install` | 2.3.0 / — / — | 1 / api | [installPlugin](../src/Glpi/Api/HL/Controller/SetupController.php#L1414) |
| POST | `/Setup/Plugin/{id}/Uninstall` | 2.3.0 / — / — | 1 / api | [uninstallPlugin](../src/Glpi/Api/HL/Controller/SetupController.php#L1433) |
| GET | `/Setup/{itemtype}` | 2.0 / — / — | 1 / api | [search20](../src/Glpi/Api/HL/Controller/SetupController.php#L1114) |
| GET | `/Setup/{itemtype}` | 2.3 / — / — | 1 / api | [search23](../src/Glpi/Api/HL/Controller/SetupController.php#L1177) |
| POST | `/Setup/{itemtype}` | 2.0 / — / — | 1 / api | [createItem20](../src/Glpi/Api/HL/Controller/SetupController.php#L1137) |
| POST | `/Setup/{itemtype}` | 2.3 / — / — | 1 / api | [createItem23](../src/Glpi/Api/HL/Controller/SetupController.php#L1200) |
| DELETE | `/Setup/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [deleteItem20](../src/Glpi/Api/HL/Controller/SetupController.php#L1166) |
| DELETE | `/Setup/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [deleteItem23](../src/Glpi/Api/HL/Controller/SetupController.php#L1229) |
| GET | `/Setup/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [getItem20](../src/Glpi/Api/HL/Controller/SetupController.php#L1126) |
| GET | `/Setup/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [getItem23](../src/Glpi/Api/HL/Controller/SetupController.php#L1189) |
| PATCH | `/Setup/{itemtype}/{id}` | 2.0 / — / — | 1 / api | [updateItem20](../src/Glpi/Api/HL/Controller/SetupController.php#L1154) |
| PATCH | `/Setup/{itemtype}/{id}` | 2.3 / — / — | 1 / api | [updateItem23](../src/Glpi/Api/HL/Controller/SetupController.php#L1217) |

## ToolController

| Métodos | Caminho | Introduzida / depreciada / removida | Segurança / scopes | Implementação |
| --- | --- | --- | --- | --- |
| GET | `/Tools/` | 2.1 / — / — | 1 / api | [index](../src/Glpi/Api/HL/Controller/ToolController.php#L277) |
| GET | `/Tools/{itemtype}` | 2.1 / — / — | 1 / api | [search](../src/Glpi/Api/HL/Controller/ToolController.php#L296) |
| POST | `/Tools/{itemtype}` | 2.1 / — / — | 1 / api | [createItem](../src/Glpi/Api/HL/Controller/ToolController.php#L319) |
| DELETE | `/Tools/{itemtype}/{id}` | 2.1 / — / — | 1 / api | [deleteItem](../src/Glpi/Api/HL/Controller/ToolController.php#L343) |
| GET | `/Tools/{itemtype}/{id}` | 2.1 / — / — | 1 / api | [getItem](../src/Glpi/Api/HL/Controller/ToolController.php#L308) |
| PATCH | `/Tools/{itemtype}/{id}` | 2.1 / — / — | 1 / api | [updateItem](../src/Glpi/Api/HL/Controller/ToolController.php#L331) |
