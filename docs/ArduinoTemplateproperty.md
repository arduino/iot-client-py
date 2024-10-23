# ArduinoTemplateproperty

ArduinoTemplateproperty media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The friendly id of the property | [optional] 
**name** | **str** | The friendly name of the property | 
**permission** | **str** | The permission of the property | 
**type** | **str** | The type of the property | 
**update_parameter** | **float** | The update frequency in seconds, or the amount of the property has to change in order to trigger an update | [optional] 
**update_strategy** | **str** | The update strategy for the property value | 
**variable_name** | **str** | The sketch variable name of the property | [optional] 

## Example

```python
from iot_api_client.models.arduino_templateproperty import ArduinoTemplateproperty

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoTemplateproperty from a JSON string
arduino_templateproperty_instance = ArduinoTemplateproperty.from_json(json)
# print the JSON string representation of the object
print(ArduinoTemplateproperty.to_json())

# convert the object into a dict
arduino_templateproperty_dict = arduino_templateproperty_instance.to_dict()
# create an instance of ArduinoTemplateproperty from a dict
arduino_templateproperty_from_dict = ArduinoTemplateproperty.from_dict(arduino_templateproperty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


