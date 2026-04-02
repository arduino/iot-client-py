# CreateClaimedDevicesV2Payload

DeviceV2 describes a device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the device | [optional] 
**ble_mac** | **str** |  | [optional] 
**connection_type** | **str** | The type of the connections selected by the user when multiple connections are available | [optional] 
**fqbn** | **str** | The fully qualified board name | [optional] 
**name** | **str** | The friendly name of the device | [optional] 
**serial** | **str** | The serial uuid of the device | [optional] 
**type** | **str** | The type of the device | 
**unique_hardware_id** | **str** | The unique hardware id of the device | 
**user_id** | **str** | The user_id associated to the device. If absent it will be inferred from the authentication header | 
**wifi_fw_version** | **str** | The version of the NINA/WIFI101 firmware running on the device | [optional] 

## Example

```python
from iot_api_client.models.create_claimed_devices_v2_payload import CreateClaimedDevicesV2Payload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClaimedDevicesV2Payload from a JSON string
create_claimed_devices_v2_payload_instance = CreateClaimedDevicesV2Payload.from_json(json)
# print the JSON string representation of the object
print(CreateClaimedDevicesV2Payload.to_json())

# convert the object into a dict
create_claimed_devices_v2_payload_dict = create_claimed_devices_v2_payload_instance.to_dict()
# create an instance of CreateClaimedDevicesV2Payload from a dict
create_claimed_devices_v2_payload_from_dict = CreateClaimedDevicesV2Payload.from_dict(create_claimed_devices_v2_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


