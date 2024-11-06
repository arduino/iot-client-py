# ArduinoLinkedProperty

ArduinoLinked_property media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | [**ArduinoProperty**](ArduinoProperty.md) |  | 
**status** | **str** | The status of the linked property | 

## Example

```python
from iot_api_client.models.arduino_linked_property import ArduinoLinkedProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoLinkedProperty from a JSON string
arduino_linked_property_instance = ArduinoLinkedProperty.from_json(json)
# print the JSON string representation of the object
print(ArduinoLinkedProperty.to_json())

# convert the object into a dict
arduino_linked_property_dict = arduino_linked_property_instance.to_dict()
# create an instance of ArduinoLinkedProperty from a dict
arduino_linked_property_from_dict = ArduinoLinkedProperty.from_dict(arduino_linked_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


