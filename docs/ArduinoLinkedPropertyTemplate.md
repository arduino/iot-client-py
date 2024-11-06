# ArduinoLinkedPropertyTemplate

ArduinoLinked_property_template media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | The property the trigger is associated to | 
**thing_id** | **str** | The thing the trigger is associated to | 

## Example

```python
from iot_api_client.models.arduino_linked_property_template import ArduinoLinkedPropertyTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoLinkedPropertyTemplate from a JSON string
arduino_linked_property_template_instance = ArduinoLinkedPropertyTemplate.from_json(json)
# print the JSON string representation of the object
print(ArduinoLinkedPropertyTemplate.to_json())

# convert the object into a dict
arduino_linked_property_template_dict = arduino_linked_property_template_instance.to_dict()
# create an instance of ArduinoLinkedPropertyTemplate from a dict
arduino_linked_property_template_from_dict = ArduinoLinkedPropertyTemplate.from_dict(arduino_linked_property_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


