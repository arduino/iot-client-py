# Variable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The template expression that extracts the value from the respective entity | 
**entity** | **str** | Type of the entity being referenced | 
**id** | **str** | The ID of the referenced entity | [optional] 
**placeholder** | **str** | Name of the variable as referenced by the expression | 
**property_id** | **str** | The ID of the property referenced entity | [optional] 
**thing_id** | **str** | The ID of the thing referenced entity | [optional] 

## Example

```python
from iot_api_client.models.variable import Variable

# TODO update the JSON string below
json = "{}"
# create an instance of Variable from a JSON string
variable_instance = Variable.from_json(json)
# print the JSON string representation of the object
print(Variable.to_json())

# convert the object into a dict
variable_dict = variable_instance.to_dict()
# create an instance of Variable from a dict
variable_from_dict = Variable.from_dict(variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


