# ArduinoDevicev2

ArduinoDevicev2 media type (default view)
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | The type of the connections selected by the user when multiple connections are available | [optional] 
**created_at** | **datetime** | Creation date of the device | [optional] 
**events** | [**list[ArduinoDevicev2SimpleProperties]**](ArduinoDevicev2SimpleProperties.md) | ArduinoDevicev2SimplePropertiesCollection is the media type for an array of ArduinoDevicev2SimpleProperties (default view) | [optional] 
**fqbn** | **str** | The fully qualified board name | [optional] 
**href** | **str** | The api reference of this device | 
**id** | **str** | The arn of the device | 
**label** | **str** | The label of the device | 
**last_activity_at** | **datetime** | Last activity date | [optional] 
**latest_wifi_fw_version** | **str** | The latest version of the NINA/WIFI101 firmware available for this device | [optional] 
**metadata** | **dict(str, object)** | The metadata of the device | [optional] 
**name** | **str** | The friendly name of the device | 
**no_sketch** | **bool** | True if the device type can not have an associated sketch | [optional] 
**organization_id** | **str** | Id of the organization the device belongs to | [optional] 
**ota_available** | **bool** | True if the device type is ready to receive OTA updated | [optional] 
**ota_compatible** | **bool** | True if the device type is OTA compatible | [optional] 
**required_wifi_fw_version** | **str** | The required version of the NINA/WIFI101 firmware needed by IoT Cloud | [optional] 
**serial** | **str** | The serial uuid of the device | 
**tags** | **dict(str, object)** | Tags belonging to the device | [optional] 
**thing** | [**ArduinoThing**](ArduinoThing.md) |  | [optional] 
**type** | **str** | The type of the device | 
**user_id** | **str** | The id of the user | 
**webhooks** | [**list[ArduinoDevicev2Webhook]**](ArduinoDevicev2Webhook.md) | ArduinoDevicev2WebhookCollection is the media type for an array of ArduinoDevicev2Webhook (default view) | [optional] 
**wifi_fw_version** | **str** | The version of the NINA/WIFI101 firmware running on the device | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


