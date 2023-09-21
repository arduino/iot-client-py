# iot_api_client.model.arduino_devicev2propertyvalues.ArduinoDevicev2propertyvalues

ArduinoDevicev2propertyvalues media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoDevicev2propertyvalues media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[last_evaluated_key](#last_evaluated_key)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**values** | [**ArduinoDevicev2propertyvalueCollection**](ArduinoDevicev2propertyvalueCollection.md) | [**ArduinoDevicev2propertyvalueCollection**](ArduinoDevicev2propertyvalueCollection.md) |  | 
**name** | str,  | str,  |  | 
**id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# last_evaluated_key

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

