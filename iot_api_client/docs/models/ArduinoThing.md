# iot_api_client.model.arduino_thing.ArduinoThing

ArduinoThing media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoThing media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_id** | str, uuid.UUID,  | str,  | The user id of the owner | value must be a uuid
**timezone** | str,  | str,  | Time zone of the thing | 
**name** | str,  | str,  | The friendly name of the thing | 
**href** | str,  | str,  | The api reference of this thing | 
**id** | str, uuid.UUID,  | str,  | The id of the thing | value must be a uuid
**created_at** | str, datetime,  | str,  | Creation date of the thing | [optional] value must conform to RFC-3339 date-time
**deleted_at** | str, datetime,  | str,  | Delete date of the thing | [optional] value must conform to RFC-3339 date-time
**device_fqbn** | str,  | str,  | The fqbn of the attached device, if any | [optional] 
**device_id** | str, uuid.UUID,  | str,  | The id of the device | [optional] value must be a uuid
**device_name** | str,  | str,  | The name of the attached device, if any | [optional] 
**device_type** | str,  | str,  | The type of the attached device, if any | [optional] 
**organization_id** | str, uuid.UUID,  | str,  | Id of the organization the thing belongs to | [optional] value must be a uuid
**properties** | [**ArduinoPropertyCollection**](ArduinoPropertyCollection.md) | [**ArduinoPropertyCollection**](ArduinoPropertyCollection.md) |  | [optional] 
**properties_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of properties of the thing | [optional] value must be a 64 bit integer
**sketch_id** | str, uuid.UUID,  | str,  | The id of the attached sketch | [optional] value must be a uuid
**[tags](#tags)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Tags of the thing | [optional] 
**updated_at** | str, datetime,  | str,  | Update date of the thing | [optional] value must conform to RFC-3339 date-time
**webhook_active** | bool,  | BoolClass,  | Webhook uri | [optional] 
**webhook_uri** | str,  | str,  | Webhook uri | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Tags of the thing

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Tags of the thing | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

