# iot_api_client.model.arduino_linkedvariable.ArduinoLinkedvariable

ArduinoLinkedvariable media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoLinkedvariable media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**thing_name** | str,  | str,  | The name of the related thing | 
**thing_id** | str, uuid.UUID,  | str,  | The id of the related thing | value must be a uuid
**name** | str,  | str,  | The name of the variable | 
**permission** | str,  | str,  | The permission of the linked variable | 
**id** | str, uuid.UUID,  | str,  | The id of the linked variable | value must be a uuid
**variable_name** | str,  | str,  | The name of the variable in the code | 
**type** | str,  | str,  | The type of the variable | 
**last_value** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Last value of the linked property | [optional] 
**last_value_updated_at** | str, datetime,  | str,  | Update date of the last value | [optional] value must conform to RFC-3339 date-time
**thing_timezone** | [**ArduinoTimezone**](ArduinoTimezone.md) | [**ArduinoTimezone**](ArduinoTimezone.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

