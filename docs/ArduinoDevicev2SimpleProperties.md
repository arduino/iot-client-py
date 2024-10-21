# ArduinoDevicev2SimpleProperties

ArduinoDevicev2SimpleProperties media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the property | 
**updated_at** | **datetime** | Update date of the property | 
**value** | **object** | Value of the property | 

## Example

```python
from iot_api_client.models.arduino_devicev2_simple_properties import ArduinoDevicev2SimpleProperties

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2SimpleProperties from a JSON string
arduino_devicev2_simple_properties_instance = ArduinoDevicev2SimpleProperties.from_json(json)
# print the JSON string representation of the object
print ArduinoDevicev2SimpleProperties.to_json()

# convert the object into a dict
arduino_devicev2_simple_properties_dict = arduino_devicev2_simple_properties_instance.to_dict()
# create an instance of ArduinoDevicev2SimpleProperties from a dict
arduino_devicev2_simple_properties_form_dict = arduino_devicev2_simple_properties.from_dict(arduino_devicev2_simple_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


