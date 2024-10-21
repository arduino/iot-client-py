# ArduinoDevicev2propertyvalueValueStatistics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adr** | **float** |  | [optional] 
**channel** | **float** |  | [optional] 
**duplicate** | **float** |  | [optional] 
**freq** | **float** |  | [optional] 
**mod_bw** | **float** |  | [optional] 
**rssi** | **float** |  | [optional] 
**seqno** | **float** |  | [optional] 
**sf** | **float** |  | [optional] 
**snr** | **float** |  | [optional] 
**time** | **float** |  | [optional] 

## Example

```python
from iot_api_client.models.arduino_devicev2propertyvalue_value_statistics import ArduinoDevicev2propertyvalueValueStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2propertyvalueValueStatistics from a JSON string
arduino_devicev2propertyvalue_value_statistics_instance = ArduinoDevicev2propertyvalueValueStatistics.from_json(json)
# print the JSON string representation of the object
print ArduinoDevicev2propertyvalueValueStatistics.to_json()

# convert the object into a dict
arduino_devicev2propertyvalue_value_statistics_dict = arduino_devicev2propertyvalue_value_statistics_instance.to_dict()
# create an instance of ArduinoDevicev2propertyvalueValueStatistics from a dict
arduino_devicev2propertyvalue_value_statistics_form_dict = arduino_devicev2propertyvalue_value_statistics.from_dict(arduino_devicev2propertyvalue_value_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


