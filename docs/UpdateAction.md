# UpdateAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the trigger | [optional] 
**email** | [**EmailAction**](EmailAction.md) |  | [optional] 
**name** | **str** | The name of the action | [optional] 
**push_notification** | [**PushAction**](PushAction.md) |  | [optional] 
**trigger_id** | **str** | Id of the trigger the action is associated to | [optional] 

## Example

```python
from iot_api_client.models.update_action import UpdateAction

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAction from a JSON string
update_action_instance = UpdateAction.from_json(json)
# print the JSON string representation of the object
print(UpdateAction.to_json())

# convert the object into a dict
update_action_dict = update_action_instance.to_dict()
# create an instance of UpdateAction from a dict
update_action_from_dict = UpdateAction.from_dict(update_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


