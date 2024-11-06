# ArduinoLinkedDevice

ArduinoLinked_device media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**ArduinoDevicev2**](ArduinoDevicev2.md) |  | 
**status** | **str** | The status of the linked device | 

## Example

```python
from iot_api_client.models.arduino_linked_device import ArduinoLinkedDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoLinkedDevice from a JSON string
arduino_linked_device_instance = ArduinoLinkedDevice.from_json(json)
# print the JSON string representation of the object
print(ArduinoLinkedDevice.to_json())

# convert the object into a dict
arduino_linked_device_dict = arduino_linked_device_instance.to_dict()
# create an instance of ArduinoLinkedDevice from a dict
arduino_linked_device_from_dict = ArduinoLinkedDevice.from_dict(arduino_linked_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


