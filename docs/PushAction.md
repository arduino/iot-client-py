# PushAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**BodyExpression**](BodyExpression.md) |  | 
**delivery** | [**PushDeliveryOpts**](PushDeliveryOpts.md) |  | 
**title** | [**TitleExpression**](TitleExpression.md) |  | 

## Example

```python
from iot_api_client.models.push_action import PushAction

# TODO update the JSON string below
json = "{}"
# create an instance of PushAction from a JSON string
push_action_instance = PushAction.from_json(json)
# print the JSON string representation of the object
print(PushAction.to_json())

# convert the object into a dict
push_action_dict = push_action_instance.to_dict()
# create an instance of PushAction from a dict
push_action_from_dict = PushAction.from_dict(push_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


