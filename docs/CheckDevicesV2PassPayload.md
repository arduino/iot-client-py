# CheckDevicesV2PassPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password for the device | 

## Example

```python
from iot_api_client.models.check_devices_v2_pass_payload import CheckDevicesV2PassPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDevicesV2PassPayload from a JSON string
check_devices_v2_pass_payload_instance = CheckDevicesV2PassPayload.from_json(json)
# print the JSON string representation of the object
print CheckDevicesV2PassPayload.to_json()

# convert the object into a dict
check_devices_v2_pass_payload_dict = check_devices_v2_pass_payload_instance.to_dict()
# create an instance of CheckDevicesV2PassPayload from a dict
check_devices_v2_pass_payload_form_dict = check_devices_v2_pass_payload.from_dict(check_devices_v2_pass_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


