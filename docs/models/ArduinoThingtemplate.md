# iot_api_client.model.arduino_thingtemplate.ArduinoThingtemplate

ArduinoThingtemplate media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoThingtemplate media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timezone** | str,  | str,  | Time zone of the thing | 
**name** | str,  | str,  | The friendly name of the thing | 
**device_metadata** | [**ArduinoDevicev2templatedevice**](ArduinoDevicev2templatedevice.md) | [**ArduinoDevicev2templatedevice**](ArduinoDevicev2templatedevice.md) |  | [optional] 
**id** | str,  | str,  | The friendly id of the thing | [optional] 
**organization_id** | str, uuid.UUID,  | str,  | Id of the organization the thing belongs to | [optional] value must be a uuid
**sketch_template** | str,  | str,  | The ID of the template&#x27;s sketch | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  | Tags of the thing | [optional] 
**variables** | [**ArduinoTemplatepropertyCollection**](ArduinoTemplatepropertyCollection.md) | [**ArduinoTemplatepropertyCollection**](ArduinoTemplatepropertyCollection.md) |  | [optional] 
**webhook_uri** | str,  | str,  | Webhook uri | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Tags of the thing

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Tags of the thing | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Tag**](Tag.md) | [**Tag**](Tag.md) | [**Tag**](Tag.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

