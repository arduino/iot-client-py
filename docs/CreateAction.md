# CreateAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the trigger | [optional] 
**email** | [**EmailAction**](EmailAction.md) |  | [optional] 
**kind** | **str** | The kind of the action | 
**name** | **str** | The name of the action | 
**organization_id** | **str** | Id of the organization the trigger belongs to | [optional] 
**push_notification** | [**PushAction**](PushAction.md) |  | [optional] 
**trigger_id** | **str** | Id of the trigger the action is associated to | [optional] 

## Example

```python
from iot_api_client.models.create_action import CreateAction

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAction from a JSON string
create_action_instance = CreateAction.from_json(json)
# print the JSON string representation of the object
print(CreateAction.to_json())

# convert the object into a dict
create_action_dict = create_action_instance.to_dict()
# create an instance of CreateAction from a dict
create_action_from_dict = CreateAction.from_dict(create_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


