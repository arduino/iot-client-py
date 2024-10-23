# Override


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_thing_id** | **str** | The id of the new thing to link | 
**old_thing_id** | **str** | The id of the thing to override | 

## Example

```python
from iot_api_client.models.override import Override

# TODO update the JSON string below
json = "{}"
# create an instance of Override from a JSON string
override_instance = Override.from_json(json)
# print the JSON string representation of the object
print(Override.to_json())

# convert the object into a dict
override_dict = override_instance.to_dict()
# create an instance of Override from a dict
override_from_dict = Override.from_dict(override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


