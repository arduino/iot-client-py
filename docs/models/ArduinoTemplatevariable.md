# iot_api_client.model.arduino_templatevariable.ArduinoTemplatevariable

ArduinoTemplatevariable media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoTemplatevariable media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**variable_id** | str,  | str,  | The name of the variable in the code | 
**thing_id** | str,  | str,  | The name of the related thing | 
**name** | str,  | str,  | The name of the variable | 
**permission** | str,  | str,  | The permission of the linked variable | 
**type** | str,  | str,  | The type of the variable | 
**thing_timezone** | [**ArduinoTimezone**](ArduinoTimezone.md) | [**ArduinoTimezone**](ArduinoTimezone.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

