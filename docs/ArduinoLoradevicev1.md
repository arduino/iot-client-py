# ArduinoLoradevicev1

ArduinoLoradevicev1 media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_eui** | **str** | The eui of the app | 
**app_key** | **str** | The key of the device | 
**device_id** | **str** | The id of the device | 
**eui** | **str** | The eui of the lora device | 

## Example

```python
from iot_api_client.models.arduino_loradevicev1 import ArduinoLoradevicev1

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoLoradevicev1 from a JSON string
arduino_loradevicev1_instance = ArduinoLoradevicev1.from_json(json)
# print the JSON string representation of the object
print(ArduinoLoradevicev1.to_json())

# convert the object into a dict
arduino_loradevicev1_dict = arduino_loradevicev1_instance.to_dict()
# create an instance of ArduinoLoradevicev1 from a dict
arduino_loradevicev1_from_dict = ArduinoLoradevicev1.from_dict(arduino_loradevicev1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


