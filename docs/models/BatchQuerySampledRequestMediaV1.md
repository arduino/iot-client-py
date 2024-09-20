# iot_api_client.model.batch_query_sampled_request_media_v1.BatchQuerySampledRequestMediaV1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**q** | str,  | str,  | Data selection query (e.g. property.2a99729d-2556-4220-a139-023348a1e6b5) | 
**from** | str, datetime,  | str,  | From timestamp (default: now UTC - 24h) | [optional] value must conform to RFC-3339 date-time
**interval** | decimal.Decimal, int,  | decimal.Decimal,  | Resolution in seconds (allowed min:60, max:86400) | [optional] if omitted the server will use the default value of 300
**series_limit** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of values returned after data aggregation, if any (default: 300, limit: 1000) | [optional] value must be a 64 bit integer
**to** | str, datetime,  | str,  | To timestamp (default: now UTC) | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

