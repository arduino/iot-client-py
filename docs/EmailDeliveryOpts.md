# EmailDeliveryOpts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bcc** | [**List[UserRecipient]**](UserRecipient.md) | The \&quot;bcc:\&quot; field of an e-mail | [optional] 
**cc** | [**List[UserRecipient]**](UserRecipient.md) | The \&quot;cc:\&quot; field of an e-mail | [optional] 
**to** | [**List[UserRecipient]**](UserRecipient.md) | The \&quot;to:\&quot; field of an e-mail | 

## Example

```python
from iot_api_client.models.email_delivery_opts import EmailDeliveryOpts

# TODO update the JSON string below
json = "{}"
# create an instance of EmailDeliveryOpts from a JSON string
email_delivery_opts_instance = EmailDeliveryOpts.from_json(json)
# print the JSON string representation of the object
print(EmailDeliveryOpts.to_json())

# convert the object into a dict
email_delivery_opts_dict = email_delivery_opts_instance.to_dict()
# create an instance of EmailDeliveryOpts from a dict
email_delivery_opts_from_dict = EmailDeliveryOpts.from_dict(email_delivery_opts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


