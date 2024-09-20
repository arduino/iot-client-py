# iot_api_client.model.arduino_series_batch_sampled.ArduinoSeriesBatchSampled

ArduinoSeriesBatchSampled media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoSeriesBatchSampled media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resp_version** | decimal.Decimal, int,  | decimal.Decimal,  | Response version | value must be a 64 bit integer
**[responses](#responses)** | list, tuple,  | tuple,  | Responses of the request | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# responses

Responses of the request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Responses of the request | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ArduinoSeriesSampledResponse**](ArduinoSeriesSampledResponse.md) | [**ArduinoSeriesSampledResponse**](ArduinoSeriesSampledResponse.md) | [**ArduinoSeriesSampledResponse**](ArduinoSeriesSampledResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

