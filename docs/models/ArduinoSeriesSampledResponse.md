# iot_api_client.model.arduino_series_sampled_response.ArduinoSeriesSampledResponse

ArduinoSeriesSampledResponse media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoSeriesSampledResponse media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count_values** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of values in the array &#x27;values&#x27; | value must be a 64 bit integer
**resp_version** | decimal.Decimal, int,  | decimal.Decimal,  | Response version | value must be a 64 bit integer
**[times](#times)** | list, tuple,  | tuple,  | Timestamp in RFC3339 | 
**from_date** | str, datetime,  | str,  | From date | value must conform to RFC-3339 date-time
**to_date** | str, datetime,  | str,  | To date | value must conform to RFC-3339 date-time
**query** | str,  | str,  | Query of for the data | 
**[values](#values)** | list, tuple,  | tuple,  | Values in Float | 
**interval** | decimal.Decimal, int,  | decimal.Decimal,  | Resolution in seconds | value must be a 64 bit integer
**status** | str,  | str,  | Status of the response | 
**message** | str,  | str,  | If the response is different than &#x27;ok&#x27; | [optional] if omitted the server will use the default value of ""
**series_limit** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of values returned after data aggregation, if any | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# times

Timestamp in RFC3339

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Timestamp in RFC3339 | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# values

Values in Float

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Values in Float | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

