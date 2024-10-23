# ArduinoLinkedvariable

ArduinoLinkedvariable media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the linked variable | 
**last_value** | **object** | Last value of the linked property | [optional] 
**last_value_updated_at** | **datetime** | Update date of the last value | [optional] 
**name** | **str** | The name of the variable | 
**permission** | **str** | The permission of the linked variable | 
**thing_id** | **str** | The id of the related thing | 
**thing_name** | **str** | The name of the related thing | 
**thing_timezone** | [**ArduinoTimezone**](ArduinoTimezone.md) |  | [optional] 
**type** | **str** | The type of the variable | 
**variable_name** | **str** | The name of the variable in the code | 

## Example

```python
from iot_api_client.models.arduino_linkedvariable import ArduinoLinkedvariable

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoLinkedvariable from a JSON string
arduino_linkedvariable_instance = ArduinoLinkedvariable.from_json(json)
# print the JSON string representation of the object
print(ArduinoLinkedvariable.to_json())

# convert the object into a dict
arduino_linkedvariable_dict = arduino_linkedvariable_instance.to_dict()
# create an instance of ArduinoLinkedvariable from a dict
arduino_linkedvariable_from_dict = ArduinoLinkedvariable.from_dict(arduino_linkedvariable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


