# CreateLoraDevicesV1Payload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **str** | The app name | 
**app_eui** | **str** | The app eui of the lora device | [optional] 
**app_key** | **str** | The app key of the lora device | [optional] 
**eui** | **str** | The eui of the lora device | 
**frequency_plan** | **str** | The frequency plan required by your country  | 
**name** | **str** | A common name for the device | 
**serial** | **str** | The optional serial number | [optional] 
**type** | **str** | The type of device | 
**user_id** | **str** | The id of the user. Can be the special string &#39;me&#39; | 

## Example

```python
from iot_api_client.models.create_lora_devices_v1_payload import CreateLoraDevicesV1Payload

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLoraDevicesV1Payload from a JSON string
create_lora_devices_v1_payload_instance = CreateLoraDevicesV1Payload.from_json(json)
# print the JSON string representation of the object
print(CreateLoraDevicesV1Payload.to_json())

# convert the object into a dict
create_lora_devices_v1_payload_dict = create_lora_devices_v1_payload_instance.to_dict()
# create an instance of CreateLoraDevicesV1Payload from a dict
create_lora_devices_v1_payload_from_dict = CreateLoraDevicesV1Payload.from_dict(create_lora_devices_v1_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


