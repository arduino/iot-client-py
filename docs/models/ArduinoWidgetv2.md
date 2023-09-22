# iot_api_client.model.arduino_widgetv2.ArduinoWidgetv2

Widget describes a dashboard widget (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Widget describes a dashboard widget (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[options](#options)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Widget options | 
**width** | decimal.Decimal, int,  | decimal.Decimal,  | Widget current width for desktop | value must be a 64 bit integer
**x** | decimal.Decimal, int,  | decimal.Decimal,  | Widget x position for desktop | value must be a 64 bit integer
**y** | decimal.Decimal, int,  | decimal.Decimal,  | Widget y position for desktop | value must be a 64 bit integer
**id** | str, uuid.UUID,  | str,  | The UUID of the widget, set by client | value must be a uuid
**type** | str,  | str,  | The type of the widget | must be one of ["slider, gauge", ] 
**height** | decimal.Decimal, int,  | decimal.Decimal,  | Widget current height for desktop | value must be a 64 bit integer
**has_permission_incompatibility** | bool,  | BoolClass,  | True if the linked variables permissions are incompatible with the widget | [optional] 
**has_type_incompatibility** | bool,  | BoolClass,  | True if the linked variables types are incompatible with the widget | [optional] 
**has_unlinked_variable** | bool,  | BoolClass,  | If it&#x27;s true the widget is linked to a soft-deleted variable | [optional] 
**height_mobile** | decimal.Decimal, int,  | decimal.Decimal,  | Widget current height for mobile | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The name of the widget | [optional] 
**variables** | [**ArduinoLinkedvariableCollection**](ArduinoLinkedvariableCollection.md) | [**ArduinoLinkedvariableCollection**](ArduinoLinkedvariableCollection.md) |  | [optional] 
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

