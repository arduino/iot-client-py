# iot_api_client.model.batch_query_raw_request_media_v1.BatchQueryRawRequestMediaV1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**q** | str,  | str,  | Query | 
**from** | str, datetime,  | str,  | From timestamp | [optional] value must conform to RFC-3339 date-time
**series_limit** | decimal.Decimal, int,  | decimal.Decimal,  | Max of values | [optional] value must be a 64 bit integer
**sort** | str,  | str,  | Sorting | [optional] must be one of ["ASC", "DESC", ] if omitted the server will use the default value of "DESC"
**to** | str, datetime,  | str,  | To timestamp | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

