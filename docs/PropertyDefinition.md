# PropertyDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | Property name | 
**value** | **object** | The property value | 

## Example

```python
from iot_api_client.models.property_definition import PropertyDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyDefinition from a JSON string
property_definition_instance = PropertyDefinition.from_json(json)
# print the JSON string representation of the object
print(PropertyDefinition.to_json())

# convert the object into a dict
property_definition_dict = property_definition_instance.to_dict()
# create an instance of PropertyDefinition from a dict
property_definition_from_dict = PropertyDefinition.from_dict(property_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


