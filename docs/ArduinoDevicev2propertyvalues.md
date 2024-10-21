# ArduinoDevicev2propertyvalues

ArduinoDevicev2propertyvalues media type (default view)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**last_evaluated_key** | [**ArduinoDevicev2propertyvaluesLastEvaluatedKey**](ArduinoDevicev2propertyvaluesLastEvaluatedKey.md) |  | 
**name** | **str** |  | 
**values** | [**List[ArduinoDevicev2propertyvalue]**](ArduinoDevicev2propertyvalue.md) | ArduinoDevicev2propertyvalueCollection is the media type for an array of ArduinoDevicev2propertyvalue (default view) | 

## Example

```python
from iot_api_client.models.arduino_devicev2propertyvalues import ArduinoDevicev2propertyvalues

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2propertyvalues from a JSON string
arduino_devicev2propertyvalues_instance = ArduinoDevicev2propertyvalues.from_json(json)
# print the JSON string representation of the object
print ArduinoDevicev2propertyvalues.to_json()

# convert the object into a dict
arduino_devicev2propertyvalues_dict = arduino_devicev2propertyvalues_instance.to_dict()
# create an instance of ArduinoDevicev2propertyvalues from a dict
arduino_devicev2propertyvalues_form_dict = arduino_devicev2propertyvalues.from_dict(arduino_devicev2propertyvalues_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


