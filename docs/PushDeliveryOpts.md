# PushDeliveryOpts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | [**List[UserRecipient]**](UserRecipient.md) | The recipient of a push notification | 

## Example

```python
from iot_api_client.models.push_delivery_opts import PushDeliveryOpts

# TODO update the JSON string below
json = "{}"
# create an instance of PushDeliveryOpts from a JSON string
push_delivery_opts_instance = PushDeliveryOpts.from_json(json)
# print the JSON string representation of the object
print(PushDeliveryOpts.to_json())

# convert the object into a dict
push_delivery_opts_dict = push_delivery_opts_instance.to_dict()
# create an instance of PushDeliveryOpts from a dict
push_delivery_opts_from_dict = PushDeliveryOpts.from_dict(push_delivery_opts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


