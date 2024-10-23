# ArduinoDevicev2Pass

DeviceCertV2 describes a password associated to a device (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | Whether the password is set or not | 
**suggested_password** | **str** | A random suggested password | [optional] 

## Example

```python
from iot_api_client.models.arduino_devicev2_pass import ArduinoDevicev2Pass

# TODO update the JSON string below
json = "{}"
# create an instance of ArduinoDevicev2Pass from a JSON string
arduino_devicev2_pass_instance = ArduinoDevicev2Pass.from_json(json)
# print the JSON string representation of the object
print(ArduinoDevicev2Pass.to_json())

# convert the object into a dict
arduino_devicev2_pass_dict = arduino_devicev2_pass_instance.to_dict()
# create an instance of ArduinoDevicev2Pass from a dict
arduino_devicev2_pass_from_dict = ArduinoDevicev2Pass.from_dict(arduino_devicev2_pass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


