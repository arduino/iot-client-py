# iot_api_client.model.arduino_series_response.ArduinoSeriesResponse

ArduinoSeriesResponse media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoSeriesResponse media type (default view) | 

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
**aggregation** | str,  | str,  | Aggregation statistic function. For numeric values, AVG statistic is used by default. PCT_X compute the Xth approximate percentile (e.g. PCT_95 is the 95th approximate percentile). For boolean, BOOL_OR statistic is used as default. | [optional] must be one of ["AVG", "MIN", "MAX", "SUM", "COUNT", "PCT_99", "PCT_95", "PCT_90", "PCT_75", "PCT_50", "PCT_15", "PCT_5", "BOOL_OR", "BOOL_AND", ] 
**message** | str,  | str,  | If the response is different than &#x27;ok&#x27; | [optional] if omitted the server will use the default value of ""
**property_id** | str, uuid.UUID,  | str,  | Property id | [optional] value must be a uuid
**property_name** | str,  | str,  | Property name | [optional] 
**property_type** | str,  | str,  | Property type | [optional] 
**series_limit** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of values returned after data aggregation, if any | [optional] value must be a 64 bit integer
**thing_id** | str, uuid.UUID,  | str,  | Thing id | [optional] value must be a uuid
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
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

