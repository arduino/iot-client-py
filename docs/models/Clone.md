# iot_api_client.model.clone.Clone

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[overrides](#overrides)** | list, tuple,  | tuple,  | The overrides to apply to the cloned dashboard. An override is a tuple of ids: the id of the thing to override and the id of the new thing to link | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# overrides

The overrides to apply to the cloned dashboard. An override is a tuple of ids: the id of the thing to override and the id of the new thing to link

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The overrides to apply to the cloned dashboard. An override is a tuple of ids: the id of the thing to override and the id of the new thing to link | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Override**](Override.md) | [**Override**](Override.md) | [**Override**](Override.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

