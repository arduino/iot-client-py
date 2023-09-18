# iot_api_client.model.error.Error

Error response media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Error response media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  | an application-specific error code, expressed as a string value. | [optional] 
**detail** | str,  | str,  | a human-readable explanation specific to this occurrence of the problem. | [optional] 
**id** | str,  | str,  | a unique identifier for this particular occurrence of the problem. | [optional] 
**[meta](#meta)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | a meta object containing non-standard meta-information about the error. | [optional] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  | the HTTP status code applicable to this problem | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# meta

a meta object containing non-standard meta-information about the error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | a meta object containing non-standard meta-information about the error. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

