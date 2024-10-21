# ArduinoLorafreqplansv1

ArduinoLorafreqplansv1 media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency_plans** | [**List[ArduinoLorafreqplanv1]**](ArduinoLorafreqplanv1.md) | The list of frequency plans | [optional] 

## Example

```python
from iot_api_client.models.arduino_lorafreqplansv1 import ArduinoLorafreqplansv1

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoLorafreqplansv1 from a JSON string
arduino_lorafreqplansv1_instance = ArduinoLorafreqplansv1.from_json(json)
# print the JSON string representation of the object
print ArduinoLorafreqplansv1.to_json()

# convert the object into a dict
arduino_lorafreqplansv1_dict = arduino_lorafreqplansv1_instance.to_dict()
# create an instance of ArduinoLorafreqplansv1 from a dict
arduino_lorafreqplansv1_form_dict = arduino_lorafreqplansv1.from_dict(arduino_lorafreqplansv1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


