# DeviceStatusSourceWithLinkedDevices

Device_status_source_with_linked_devices media type (default view)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | **str** | The criteria of the trigger, could be INCLUDE or EXCLUDE | 
**grace_period_offline** | **int** | The amount of seconds the trigger will wait before considering a matching device as offline | [optional] 
**grace_period_online** | **int** | The amount of seconds the trigger will wait before considering a matching device as online | [optional] 
**linked_devices** | [**List[ArduinoLinkedDevice]**](ArduinoLinkedDevice.md) | A list of devices the trigger is associated to | [optional] 

## Example

```python
from iot_api_client.models.device_status_source_with_linked_devices import DeviceStatusSourceWithLinkedDevices

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceStatusSourceWithLinkedDevices from a JSON string
device_status_source_with_linked_devices_instance = DeviceStatusSourceWithLinkedDevices.from_json(json)
# print the JSON string representation of the object
print(DeviceStatusSourceWithLinkedDevices.to_json())

# convert the object into a dict
device_status_source_with_linked_devices_dict = device_status_source_with_linked_devices_instance.to_dict()
# create an instance of DeviceStatusSourceWithLinkedDevices from a dict
device_status_source_with_linked_devices_from_dict = DeviceStatusSourceWithLinkedDevices.from_dict(device_status_source_with_linked_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


