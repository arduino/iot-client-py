# Clone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overrides** | [**List[Override]**](Override.md) | The overrides to apply to the cloned dashboard. An override is a tuple of ids: the id of the thing to override and the id of the new thing to link | [optional] 

## Example

```python
from iot_api_client.models.clone import Clone

# TODO update the JSON string below
json = "{}"
# create an instance of Clone from a JSON string
clone_instance = Clone.from_json(json)
# print the JSON string representation of the object
print(Clone.to_json())

# convert the object into a dict
clone_dict = clone_instance.to_dict()
# create an instance of Clone from a dict
clone_from_dict = Clone.from_dict(clone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


