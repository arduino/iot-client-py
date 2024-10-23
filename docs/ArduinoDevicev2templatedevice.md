# ArduinoDevicev2templatedevice

ArduinoDevicev2templatedevice media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqbn** | **str** | The device fqbn | [optional] 
**name** | **str** | The device type name | [optional] 

## Example

```python
from iot_api_client.models.arduino_devicev2templatedevice import ArduinoDevicev2templatedevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2templatedevice from a JSON string
arduino_devicev2templatedevice_instance = ArduinoDevicev2templatedevice.from_json(json)
# print the JSON string representation of the object
print(ArduinoDevicev2templatedevice.to_json())

# convert the object into a dict
arduino_devicev2templatedevice_dict = arduino_devicev2templatedevice_instance.to_dict()
# create an instance of ArduinoDevicev2templatedevice from a dict
arduino_devicev2templatedevice_from_dict = ArduinoDevicev2templatedevice.from_dict(arduino_devicev2templatedevice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


