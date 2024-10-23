# ThingClone

Payload to clone a new thing from an existing one

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_tags** | **bool** | Include tags in clone procedure | [optional] 
**name** | **str** | The friendly name of the thing | 

## Example

```python
from iot_api_client.models.thing_clone import ThingClone

# TODO update the JSON string below
json = "{}"
# create an instance of ThingClone from a JSON string
thing_clone_instance = ThingClone.from_json(json)
# print the JSON string representation of the object
print(ThingClone.to_json())

# convert the object into a dict
thing_clone_dict = thing_clone_instance.to_dict()
# create an instance of ThingClone from a dict
thing_clone_from_dict = ThingClone.from_dict(thing_clone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


