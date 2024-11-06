# DeviceStatusSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | **str** | The matching criteria of the trigger, this allows to interpret device_ids as an inclusion or exclusion list | 
**device_ids** | **List[str]** | A list of device IDs to be included in or excluded from the trigger (see criteria). Mutually exclusive with property_id. | [optional] 
**grace_period_offline** | **int** | Amount of seconds the trigger will wait before the device will be considered disconnected (requires &#39;device_id&#39;) | [optional] 
**grace_period_online** | **int** | Amount of seconds the trigger will wait before the device will be considered connected (requires &#39;device_id&#39;) | [optional] 

## Example

```python
from iot_api_client.models.device_status_source import DeviceStatusSource

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceStatusSource from a JSON string
device_status_source_instance = DeviceStatusSource.from_json(json)
# print the JSON string representation of the object
print(DeviceStatusSource.to_json())

# convert the object into a dict
device_status_source_dict = device_status_source_instance.to_dict()
# create an instance of DeviceStatusSource from a dict
device_status_source_from_dict = DeviceStatusSource.from_dict(device_status_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


