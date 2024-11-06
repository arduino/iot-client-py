# Trigger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[CreateAction]**](CreateAction.md) | A list of actions to be associated with the trigger | [optional] 
**active** | **bool** | Is true if the trigger is enabled | [optional] 
**description** | **str** | The description of the trigger | [optional] 
**device_status_source** | [**DeviceStatusSource**](DeviceStatusSource.md) |  | [optional] 
**id** | **str** | The id of the trigger | [optional] 
**name** | **str** | The name of the trigger | [optional] 
**property_id** | **str** | Id of the property the trigger is associated to (mutually exclusive with &#39;device_status_source&#39;) | [optional] 
**soft_deleted** | **bool** | If false, restore the thing from the soft deletion | [optional] [default to False]

## Example

```python
from iot_api_client.models.trigger import Trigger

# TODO update the JSON string below
json = "{}"
# create an instance of Trigger from a JSON string
trigger_instance = Trigger.from_json(json)
# print the JSON string representation of the object
print(Trigger.to_json())

# convert the object into a dict
trigger_dict = trigger_instance.to_dict()
# create an instance of Trigger from a dict
trigger_from_dict = Trigger.from_dict(trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


