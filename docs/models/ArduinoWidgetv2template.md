# iot_api_client.model.arduino_widgetv2template.ArduinoWidgetv2template

ArduinoWidgetv2template media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoWidgetv2template media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[options](#options)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Widget options | 
**width** | decimal.Decimal, int,  | decimal.Decimal,  | Widget current width for desktop | value must be a 64 bit integer
**x** | decimal.Decimal, int,  | decimal.Decimal,  | Widget x position for desktop | value must be a 64 bit integer
**y** | decimal.Decimal, int,  | decimal.Decimal,  | Widget y position for desktop | value must be a 64 bit integer
**type** | str,  | str,  | The type of the widget | 
**height** | decimal.Decimal, int,  | decimal.Decimal,  | Widget current height for desktop | value must be a 64 bit integer
**height_mobile** | decimal.Decimal, int,  | decimal.Decimal,  | Widget current height for mobile | [optional] value must be a 64 bit integer
**name** | str,  | str,  | The name of the widget | [optional] 
**variables** | [**ArduinoTemplatevariableCollection**](ArduinoTemplatevariableCollection.md) | [**ArduinoTemplatevariableCollection**](ArduinoTemplatevariableCollection.md) |  | [optional] 
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

