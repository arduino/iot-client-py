# UserRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address of the user | [optional] 
**id** | **str** | The id of the user | 
**username** | **str** | The username of the user | [optional] 

## Example

```python
from iot_api_client.models.user_recipient import UserRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of UserRecipient from a JSON string
user_recipient_instance = UserRecipient.from_json(json)
# print the JSON string representation of the object
print(UserRecipient.to_json())

# convert the object into a dict
user_recipient_dict = user_recipient_instance.to_dict()
# create an instance of UserRecipient from a dict
user_recipient_from_dict = UserRecipient.from_dict(user_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


