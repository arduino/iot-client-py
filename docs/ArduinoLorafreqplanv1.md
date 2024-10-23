# ArduinoLorafreqplanv1

ArduinoLorafreqplanv1 media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced** | **bool** | Frequency plan only for advanced users | 
**id** | **str** | The ID of the frequency paln | 
**name** | **str** | The name of the frequency plan | 

## Example

```python
from iot_api_client.models.arduino_lorafreqplanv1 import ArduinoLorafreqplanv1

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoLorafreqplanv1 from a JSON string
arduino_lorafreqplanv1_instance = ArduinoLorafreqplanv1.from_json(json)
# print the JSON string representation of the object
print(ArduinoLorafreqplanv1.to_json())

# convert the object into a dict
arduino_lorafreqplanv1_dict = arduino_lorafreqplanv1_instance.to_dict()
# create an instance of ArduinoLorafreqplanv1 from a dict
arduino_lorafreqplanv1_from_dict = ArduinoLorafreqplanv1.from_dict(arduino_lorafreqplanv1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


