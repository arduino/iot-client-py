# ArduinoDevicev2propertyvalueValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** |  | [optional] 
**seqno** | **int** |  | [optional] 
**statistics** | [**ArduinoDevicev2propertyvalueValueStatistics**](ArduinoDevicev2propertyvalueValueStatistics.md) |  | [optional] 

## Example

```python
from iot_api_client.models.arduino_devicev2propertyvalue_value import ArduinoDevicev2propertyvalueValue

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2propertyvalueValue from a JSON string
arduino_devicev2propertyvalue_value_instance = ArduinoDevicev2propertyvalueValue.from_json(json)
# print the JSON string representation of the object
print ArduinoDevicev2propertyvalueValue.to_json()

# convert the object into a dict
arduino_devicev2propertyvalue_value_dict = arduino_devicev2propertyvalue_value_instance.to_dict()
# create an instance of ArduinoDevicev2propertyvalueValue from a dict
arduino_devicev2propertyvalue_value_form_dict = arduino_devicev2propertyvalue_value.from_dict(arduino_devicev2propertyvalue_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


