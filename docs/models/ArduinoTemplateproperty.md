# iot_api_client.model.arduino_templateproperty.ArduinoTemplateproperty

ArduinoTemplateproperty media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoTemplateproperty media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_strategy** | str,  | str,  | The update strategy for the property value | 
**name** | str,  | str,  | The friendly name of the property | 
**permission** | str,  | str,  | The permission of the property | 
**type** | str,  | str,  | The type of the property | 
**id** | str,  | str,  | The friendly id of the property | [optional] 
**update_parameter** | decimal.Decimal, int, float,  | decimal.Decimal,  | The update frequency in seconds, or the amount of the property has to change in order to trigger an update | [optional] value must be a 64 bit float
**variable_name** | str,  | str,  | The sketch variable name of the property | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

