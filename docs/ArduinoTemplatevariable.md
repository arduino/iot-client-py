# ArduinoTemplatevariable

ArduinoTemplatevariable media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the variable | 
**permission** | **str** | The permission of the linked variable | 
**thing_id** | **str** | The name of the related thing | 
**thing_timezone** | [**ArduinoTimezone**](ArduinoTimezone.md) |  | [optional] 
**type** | **str** | The type of the variable | 
**variable_id** | **str** | The name of the variable in the code | 

## Example

```python
from iot_api_client.models.arduino_templatevariable import ArduinoTemplatevariable

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoTemplatevariable from a JSON string
arduino_templatevariable_instance = ArduinoTemplatevariable.from_json(json)
# print the JSON string representation of the object
print(ArduinoTemplatevariable.to_json())

# convert the object into a dict
arduino_templatevariable_dict = arduino_templatevariable_instance.to_dict()
# create an instance of ArduinoTemplatevariable from a dict
arduino_templatevariable_from_dict = ArduinoTemplatevariable.from_dict(arduino_templatevariable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


