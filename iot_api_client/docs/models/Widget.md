# iot_api_client.model.widget.Widget

Widget describes a dashboard widget

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Widget describes a dashboard widget | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[options](#options)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Widget options | 
**width** | decimal.Decimal, int,  | decimal.Decimal,  | Widget current width for desktop | value must be a 64 bit integer
**x** | decimal.Decimal, int,  | decimal.Decimal,  | Widget x position for desktop | value must be a 64 bit integer
**y** | decimal.Decimal, int,  | decimal.Decimal,  | Widget y position for desktop | value must be a 64 bit integer
**id** | str, uuid.UUID,  | str,  | The UUID of the widget, set by client | value must be a uuid
**type** | str,  | str,  | The type of the widget | 
**height** | decimal.Decimal, int,  | decimal.Decimal,  | Widget current height for desktop | value must be a 64 bit integer
**height_mobile** | decimal.Decimal, int,  | decimal.Decimal,  | Widget current height for mobile | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The name of the widget | [optional] 
**[variables](#variables)** | list, tuple,  | tuple,  |  | [optional] 
**width_mobile** | decimal.Decimal, int,  | decimal.Decimal,  | Widget current width for mobile | [optional] value must be a 64 bit integer
**x_mobile** | decimal.Decimal, int,  | decimal.Decimal,  | Widget x position for mobile | [optional] value must be a 64 bit integer
**y_mobile** | decimal.Decimal, int,  | decimal.Decimal,  | Widget y position for mobile | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# options

Widget options

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Widget options | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# variables

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, uuid.UUID,  | str,  |  | value must be a uuid

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

