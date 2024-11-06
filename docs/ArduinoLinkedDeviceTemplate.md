# ArduinoLinkedDeviceTemplate

ArduinoLinked_device_template media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thing_id** | **str** | The thing the device is associated to | 

## Example

```python
from iot_api_client.models.arduino_linked_device_template import ArduinoLinkedDeviceTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoLinkedDeviceTemplate from a JSON string
arduino_linked_device_template_instance = ArduinoLinkedDeviceTemplate.from_json(json)
# print the JSON string representation of the object
print(ArduinoLinkedDeviceTemplate.to_json())

# convert the object into a dict
arduino_linked_device_template_dict = arduino_linked_device_template_instance.to_dict()
# create an instance of ArduinoLinkedDeviceTemplate from a dict
arduino_linked_device_template_from_dict = ArduinoLinkedDeviceTemplate.from_dict(arduino_linked_device_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


