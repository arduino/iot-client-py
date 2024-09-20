# iot_api_client.model.batch_query_request_media_v1.BatchQueryRequestMediaV1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**q** | str,  | str,  | Data selection query (e.g. property.2a99729d-2556-4220-a139-023348a1e6b5 or thing.95717675-4786-4ffc-afcc-799777755391) | 
**from** | str, datetime,  | str,  | From timestamp | value must conform to RFC-3339 date-time
**to** | str, datetime,  | str,  | To timestamp | value must conform to RFC-3339 date-time
**aggregation** | str,  | str,  | Aggregation statistic function. For numeric values, AVG statistic is used by default. PCT_X compute the Xth approximate percentile (e.g. PCT_95 is the 95th approximate percentile). For boolean, BOOL_OR statistic is used as default. | [optional] must be one of ["AVG", "MIN", "MAX", "SUM", "COUNT", "PCT_99", "PCT_95", "PCT_90", "PCT_75", "PCT_50", "PCT_15", "PCT_5", "BOOL_OR", "BOOL_AND", ] 
**interval** | decimal.Decimal, int,  | decimal.Decimal,  | Resolution in seconds (max allowed: 86400) | [optional] value must be a 64 bit integer
**series_limit** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of values returned after data aggregation, if any (default: 300, limit: 1000 - 10000 in case of thing query) | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

