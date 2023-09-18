# iot_api_client.model.arduino_devicev2_event_properties.ArduinoDevicev2EventProperties

ArduinoDevicev2EventProperties media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoDevicev2EventProperties media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str, uuid.UUID,  | str,  | The device of the property | value must be a uuid
**events** | [**ArduinoDevicev2SimplePropertiesCollection**](ArduinoDevicev2SimplePropertiesCollection.md) | [**ArduinoDevicev2SimplePropertiesCollection**](ArduinoDevicev2SimplePropertiesCollection.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

