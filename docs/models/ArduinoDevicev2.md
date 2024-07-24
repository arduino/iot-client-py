# iot_api_client.model.arduino_devicev2.ArduinoDevicev2

ArduinoDevicev2 media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoDevicev2 media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**serial** | str,  | str,  | The serial uuid of the device | 
**user_id** | str, uuid.UUID,  | str,  | The id of the user | value must be a uuid
**name** | str,  | str,  | The friendly name of the device | 
**href** | str,  | str,  | The api reference of this device | 
**id** | str, uuid.UUID,  | str,  | The arn of the device | value must be a uuid
**label** | str,  | str,  | The label of the device | 
**type** | str,  | str,  | The type of the device | 
**connection_type** | str,  | str,  | The type of the connections selected by the user when multiple connections are available | [optional] must be one of ["wifi", "eth", "wifiandsecret", "gsm", "nb", "lora", "catm1", "cellular", ] 
**created_at** | str, datetime,  | str,  | Creation date of the device | [optional] value must conform to RFC-3339 date-time
**device_status** | str,  | str,  | The connection status of the device | [optional] must be one of ["ONLINE", "OFFLINE", "UNKNOWN", ] 
**events** | [**ArduinoDevicev2SimplePropertiesCollection**](ArduinoDevicev2SimplePropertiesCollection.md) | [**ArduinoDevicev2SimplePropertiesCollection**](ArduinoDevicev2SimplePropertiesCollection.md) |  | [optional] 
**fqbn** | str,  | str,  | The fully qualified board name | [optional] 
**last_activity_at** | str, datetime,  | str,  | Last activity date | [optional] value must conform to RFC-3339 date-time
**latest_wifi_fw_version** | str,  | str,  | The latest version of the NINA/WIFI101 firmware available for this device | [optional] 
**[metadata](#metadata)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The metadata of the device | [optional] 
**no_sketch** | bool,  | BoolClass,  | True if the device type can not have an associated sketch | [optional] 
**organization_id** | str, uuid.UUID,  | str,  | Id of the organization the device belongs to | [optional] value must be a uuid
**ota_available** | bool,  | BoolClass,  | True if the device type is ready to receive OTA updated | [optional] 
**ota_compatible** | bool,  | BoolClass,  | True if the device type is OTA compatible | [optional] 
**required_wifi_fw_version** | str,  | str,  | The required version of the NINA/WIFI101 firmware needed by IoT Cloud | [optional] 
**[tags](#tags)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Tags belonging to the device | [optional] 
**thing** | [**ArduinoThing**](ArduinoThing.md) | [**ArduinoThing**](ArduinoThing.md) |  | [optional] 
**webhooks** | [**ArduinoDevicev2WebhookCollection**](ArduinoDevicev2WebhookCollection.md) | [**ArduinoDevicev2WebhookCollection**](ArduinoDevicev2WebhookCollection.md) |  | [optional] 
**wifi_fw_version** | str,  | str,  | The version of the NINA/WIFI101 firmware running on the device | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# metadata

The metadata of the device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The metadata of the device | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Tags belonging to the device

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Tags belonging to the device | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

