# iot_api_client.model.arduino_devicev2properties.ArduinoDevicev2properties

ArduinoDevicev2properties media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoDevicev2properties media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**data_retention_days** | decimal.Decimal, int, float,  | decimal.Decimal,  | How many days the data will be kept | value must be a 64 bit float
**user_id** | str, uuid.UUID,  | str,  | The user id of the owner | value must be a uuid
**deviceId** | str, uuid.UUID,  | str,  | The device of the property | value must be a uuid
**properties** | [**ArduinoPropertyCollection**](ArduinoPropertyCollection.md) | [**ArduinoPropertyCollection**](ArduinoPropertyCollection.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

