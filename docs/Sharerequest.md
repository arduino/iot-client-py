# Sharerequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message the user want to send to the dashboard owner | [optional] 

## Example

```python
from iot_api_client.models.sharerequest import Sharerequest

# TODO update the JSON string below
json = "{}"
# create an instance of Sharerequest from a JSON string
sharerequest_instance = Sharerequest.from_json(json)
# print the JSON string representation of the object
print(Sharerequest.to_json())

# convert the object into a dict
sharerequest_dict = sharerequest_instance.to_dict()
# create an instance of Sharerequest from a dict
sharerequest_from_dict = Sharerequest.from_dict(sharerequest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


