# ArduinoDevicev2propertyvalue

ArduinoDevicev2propertyvalue media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**value** | [**ArduinoDevicev2propertyvalueValue**](ArduinoDevicev2propertyvalueValue.md) |  | [optional] 

## Example

```python
from iot_api_client.models.arduino_devicev2propertyvalue import ArduinoDevicev2propertyvalue

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2propertyvalue from a JSON string
arduino_devicev2propertyvalue_instance = ArduinoDevicev2propertyvalue.from_json(json)
# print the JSON string representation of the object
print(ArduinoDevicev2propertyvalue.to_json())

# convert the object into a dict
arduino_devicev2propertyvalue_dict = arduino_devicev2propertyvalue_instance.to_dict()
# create an instance of ArduinoDevicev2propertyvalue from a dict
arduino_devicev2propertyvalue_from_dict = ArduinoDevicev2propertyvalue.from_dict(arduino_devicev2propertyvalue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


