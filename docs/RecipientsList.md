# RecipientsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **List[str]** | List of recipients to be removed | 

## Example

```python
from iot_api_client.models.recipients_list import RecipientsList

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientsList from a JSON string
recipients_list_instance = RecipientsList.from_json(json)
# print the JSON string representation of the object
print(RecipientsList.to_json())

# convert the object into a dict
recipients_list_dict = recipients_list_instance.to_dict()
# create an instance of RecipientsList from a dict
recipients_list_from_dict = RecipientsList.from_dict(recipients_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


