# ArduinoThingresult

ArduinoThingresult media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | UUID of the attached device | [optional] 
**id** | **str** | UUID of the created Thing | 
**sketch_id** | **str** | UUID of the created Sketch | 

## Example

```python
from iot_api_client.models.arduino_thingresult import ArduinoThingresult

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoThingresult from a JSON string
arduino_thingresult_instance = ArduinoThingresult.from_json(json)
# print the JSON string representation of the object
print ArduinoThingresult.to_json()

# convert the object into a dict
arduino_thingresult_dict = arduino_thingresult_instance.to_dict()
# create an instance of ArduinoThingresult from a dict
arduino_thingresult_form_dict = arduino_thingresult.from_dict(arduino_thingresult_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


