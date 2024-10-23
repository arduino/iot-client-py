# ArduinoDevicev2StatusEvents

ArduinoDevicev2StatusEvents media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[ArduinoDevicev2StatusEvent]**](ArduinoDevicev2StatusEvent.md) | ArduinoDevicev2StatusEventCollection is the media type for an array of ArduinoDevicev2StatusEvent (default view) | 
**id** | **str** | The id of the device | 

## Example

```python
from iot_api_client.models.arduino_devicev2_status_events import ArduinoDevicev2StatusEvents

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2StatusEvents from a JSON string
arduino_devicev2_status_events_instance = ArduinoDevicev2StatusEvents.from_json(json)
# print the JSON string representation of the object
print(ArduinoDevicev2StatusEvents.to_json())

# convert the object into a dict
arduino_devicev2_status_events_dict = arduino_devicev2_status_events_instance.to_dict()
# create an instance of ArduinoDevicev2StatusEvents from a dict
arduino_devicev2_status_events_from_dict = ArduinoDevicev2StatusEvents.from_dict(arduino_devicev2_status_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


