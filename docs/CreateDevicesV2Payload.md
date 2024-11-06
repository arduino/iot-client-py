# CreateDevicesV2Payload

DeviceV2 describes a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | The type of the connections selected by the user when multiple connections are available | [optional] 
**fqbn** | **str** | The fully qualified board name | [optional] 
**name** | **str** | The friendly name of the device | [optional] 
**serial** | **str** | The serial uuid of the device | [optional] 
**soft_deleted** | **bool** | If false, restore the thing from the soft deletion | [optional] [default to False]
**type** | **str** | The type of the device | 
**user_id** | **str** | The user_id associated to the device. If absent it will be inferred from the authentication header | [optional] 
**wifi_fw_version** | **str** | The version of the NINA/WIFI101 firmware running on the device | [optional] 

## Example

```python
from iot_api_client.models.create_devices_v2_payload import CreateDevicesV2Payload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDevicesV2Payload from a JSON string
create_devices_v2_payload_instance = CreateDevicesV2Payload.from_json(json)
# print the JSON string representation of the object
print(CreateDevicesV2Payload.to_json())

# convert the object into a dict
create_devices_v2_payload_dict = create_devices_v2_payload_instance.to_dict()
# create an instance of CreateDevicesV2Payload from a dict
create_devices_v2_payload_from_dict = CreateDevicesV2Payload.from_dict(create_devices_v2_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


