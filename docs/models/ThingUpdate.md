# iot_api_client.model.thing_update.ThingUpdate

Payload to update an existing thing

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Payload to update an existing thing | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | str, uuid.UUID,  | str,  | The arn of the associated device | [optional] value must be a uuid
**id** | str, uuid.UUID,  | str,  | The id of the thing | [optional] value must be a uuid
**name** | str,  | str,  | The friendly name of the thing | [optional] 
**[properties](#properties)** | list, tuple,  | tuple,  | The properties of the thing | [optional] 
**timezone** | str,  | str,  | A time zone name. Check /v2/timezones for a list of valid names. | [optional] 
**webhook_active** | bool,  | BoolClass,  | Webhook uri | [optional] 
**webhook_uri** | str,  | str,  | Webhook uri | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# properties

The properties of the thing

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The properties of the thing | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) | [**ModelProperty**](ModelProperty.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

