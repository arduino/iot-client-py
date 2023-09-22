# iot_api_client.model.arduino_property.ArduinoProperty

ArduinoProperty media type (default view)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ArduinoProperty media type (default view) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_strategy** | str,  | str,  | The update strategy for the property value | 
**thing_id** | str, uuid.UUID,  | str,  | The id of the thing | value must be a uuid
**name** | str,  | str,  | The friendly name of the property | 
**permission** | str,  | str,  | The permission of the property | 
**href** | str,  | str,  | The api reference of this property | 
**id** | str, uuid.UUID,  | str,  | The id of the property | value must be a uuid
**type** | str,  | str,  | The type of the property | 
**created_at** | str, datetime,  | str,  | Creation date of the property | [optional] value must conform to RFC-3339 date-time
**deleted_at** | str, datetime,  | str,  | Delete date of the property | [optional] value must conform to RFC-3339 date-time
**last_value** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Last value of this property | [optional] 
**linked_to_trigger** | bool,  | BoolClass,  | Indicates if the property is involved in the activation of at least a trigger | [optional] 
**max_value** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum value of this property | [optional] value must be a 64 bit float
**min_value** | decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum value of this property | [optional] value must be a 64 bit float
**persist** | bool,  | BoolClass,  | If true, data will persist into a timeseries database | [optional] 
**sync_id** | str, uuid.UUID,  | str,  | The id of the sync pool | [optional] value must be a uuid
**tag** | decimal.Decimal, int, float,  | decimal.Decimal,  | The integer id of the property | [optional] value must be a 64 bit float
**thing_name** | str,  | str,  | The name of the associated thing | [optional] 
**update_parameter** | decimal.Decimal, int, float,  | decimal.Decimal,  | The update frequency in seconds, or the amount of the property has to change in order to trigger an update | [optional] value must be a 64 bit float
**updated_at** | str, datetime,  | str,  | Update date of the property | [optional] value must conform to RFC-3339 date-time
**value_updated_at** | str, datetime,  | str,  | Last update timestamp of this property | [optional] value must conform to RFC-3339 date-time
**variable_name** | str,  | str,  | The sketch variable name of the property | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

