# iot_api_client.model.arduino_propertytype.ArduinoPropertytype

ArduinoPropertytype media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoPropertytype media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**rw** | bool,  | BoolClass,  | Tell if the type allow a R/W permission | 
**deprecated** | bool,  | BoolClass,  | Tell if this type is deprecated | 
**name** | str,  | str,  | The friendly name of the property type | 
**type** | str,  | str,  | The api reference of this type | 
**declaration** | str,  | str,  | The c++ type we are using for this variable type | 
**[assistants](#assistants)** | list, tuple,  | tuple,  | The voice assistants available for this type | [optional] 
**example** | str,  | str,  | Example of use | [optional] 
**supersededBy** | str,  | str,  | The type of property to use if it&#x27;s deprecated | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  | The tags related to the type | [optional] 
**[units](#units)** | list, tuple,  | tuple,  | The measure units available for this type | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# assistants

The voice assistants available for this type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The voice assistants available for this type | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# tags

The tags related to the type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The tags related to the type | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# units

The measure units available for this type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The measure units available for this type | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

