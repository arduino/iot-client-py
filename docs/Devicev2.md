# Devicev2

DeviceV2 describes a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | The type of the connections selected by the user when multiple connections are available | [optional] 
**fqbn** | **str** | The fully qualified board name | [optional] 
**name** | **str** | The friendly name of the device | [optional] 
**serial** | **str** | The serial uuid of the device | [optional] 
**type** | **str** | The type of the device | [optional] 
**user_id** | **str** | The user_id associated to the device. If absent it will be inferred from the authentication header | [optional] 
**wifi_fw_version** | **str** | The version of the NINA/WIFI101 firmware running on the device | [optional] 

## Example

```python
from iot_api_client.models.devicev2 import Devicev2

# TODO update the JSON string below
json = "{}"
# create an instance of Devicev2 from a JSON string
devicev2_instance = Devicev2.from_json(json)
# print the JSON string representation of the object
print(Devicev2.to_json())

# convert the object into a dict
devicev2_dict = devicev2_instance.to_dict()
# create an instance of Devicev2 from a dict
devicev2_from_dict = Devicev2.from_dict(devicev2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


