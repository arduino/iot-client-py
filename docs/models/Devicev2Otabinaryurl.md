# iot_api_client.model.devicev2_otabinaryurl.Devicev2Otabinaryurl

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**binary_key** | str,  | str,  | The object key of the binary | 
**async** | bool,  | BoolClass,  | If false, wait for the full OTA process, until it gets a result from the device | [optional] if omitted the server will use the default value of True
**expire_in_mins** | decimal.Decimal, int,  | decimal.Decimal,  | Binary expire time in minutes, default 10 mins | [optional] if omitted the server will use the default value of 10value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

