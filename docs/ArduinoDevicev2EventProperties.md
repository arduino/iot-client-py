# ArduinoDevicev2EventProperties

ArduinoDevicev2EventProperties media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[ArduinoDevicev2SimpleProperties]**](ArduinoDevicev2SimpleProperties.md) | ArduinoDevicev2SimplePropertiesCollection is the media type for an array of ArduinoDevicev2SimpleProperties (default view) | 
**id** | **str** | The device of the property | 

## Example

```python
from iot_api_client.models.arduino_devicev2_event_properties import ArduinoDevicev2EventProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2EventProperties from a JSON string
arduino_devicev2_event_properties_instance = ArduinoDevicev2EventProperties.from_json(json)
# print the JSON string representation of the object
print ArduinoDevicev2EventProperties.to_json()

# convert the object into a dict
arduino_devicev2_event_properties_dict = arduino_devicev2_event_properties_instance.to_dict()
# create an instance of ArduinoDevicev2EventProperties from a dict
arduino_devicev2_event_properties_form_dict = arduino_devicev2_event_properties.from_dict(arduino_devicev2_event_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


