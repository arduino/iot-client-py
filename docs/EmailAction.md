# EmailAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | [**BodyExpression**](BodyExpression.md) |  | 
**delivery** | [**EmailDeliveryOpts**](EmailDeliveryOpts.md) |  | 
**subject** | [**TitleExpression**](TitleExpression.md) |  | 

## Example

```python
from iot_api_client.models.email_action import EmailAction

# TODO update the JSON string below
json = "{}"
# create an instance of EmailAction from a JSON string
email_action_instance = EmailAction.from_json(json)
# print the JSON string representation of the object
print(EmailAction.to_json())

# convert the object into a dict
email_action_dict = email_action_instance.to_dict()
# create an instance of EmailAction from a dict
email_action_from_dict = EmailAction.from_dict(email_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


