# ArduinoDevicev2StatusEvent

ArduinoDevicev2StatusEvent media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** | Update timestamp of the status event | 
**value** | **str** | The status event of the device | 

## Example

```python
from iot_api_client.models.arduino_devicev2_status_event import ArduinoDevicev2StatusEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2StatusEvent from a JSON string
arduino_devicev2_status_event_instance = ArduinoDevicev2StatusEvent.from_json(json)
# print the JSON string representation of the object
print(ArduinoDevicev2StatusEvent.to_json())

# convert the object into a dict
arduino_devicev2_status_event_dict = arduino_devicev2_status_event_instance.to_dict()
# create an instance of ArduinoDevicev2StatusEvent from a dict
arduino_devicev2_status_event_from_dict = ArduinoDevicev2StatusEvent.from_dict(arduino_devicev2_status_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


